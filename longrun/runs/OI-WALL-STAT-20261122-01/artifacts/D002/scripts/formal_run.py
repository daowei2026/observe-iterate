"""D002：持共享锁运行原生默认实例，结果留在本 Run 独立存储。"""
import fcntl
import hashlib
import inspect
import json
import os
import resource
import subprocess
import sys
import time
import traceback
from datetime import datetime, timezone
from pathlib import Path

OUT = Path(__file__).resolve().parent
RUN = "OI-WALL-STAT-20261122-01"
PIN = OUT / "code/tis"
LOCK = Path("/dwdhome/fy/cgpterm/artifacts/wall-f-closure-20261122/FORMAL_PRODUCTION.lock")
preflight = json.loads((OUT / "preflight.json").read_text())


def now():
    return datetime.now(timezone.utc).isoformat()


def write_json(path, obj):
    temporary = Path(str(path) + ".tmp")
    temporary.write_text(json.dumps(obj, ensure_ascii=False, indent=2, default=str) + "\n")
    temporary.replace(path)


def sha256(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as handle:
        for block in iter(lambda: handle.read(4 * 1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def lock_evidence(fd):
    inode = str(os.fstat(fd).st_ino)
    return dict(inode=inode, pid=os.getpid(),
                proc_locks=[line for line in Path("/proc/locks").read_text().splitlines()
                            if line.split()[5].rsplit(":", 1)[-1] == inode],
                fdinfo=Path(f"/proc/self/fdinfo/{fd}").read_text())


def audit_writers(paths):
    result = dict(at=now(), surfaces=[str(path) for path in paths], conflicting_write_fds=[],
                  permission_limits=[])
    for proc in Path("/proc").iterdir():
        if not proc.name.isdigit() or int(proc.name) == os.getpid():
            continue
        try:
            if proc.stat().st_uid != os.getuid():
                continue
            for fd in (proc / "fd").iterdir():
                try:
                    value = os.readlink(fd).removesuffix(" (deleted)")
                    if not any(value == str(path) or value.startswith(str(path) + "/") for path in paths):
                        continue
                    flags_line = next(line for line in (proc / "fdinfo" / fd.name).read_text().splitlines()
                                      if line.startswith("flags:"))
                    flags = int(flags_line.split()[1], 8)
                    if flags & os.O_ACCMODE:
                        result["conflicting_write_fds"].append(dict(pid=int(proc.name), path=value))
                except (OSError, StopIteration):
                    continue
        except OSError:
            result["permission_limits"].append(int(proc.name))
    return result


lease = dict(run_id=RUN, call_id="C0004", pid=os.getpid(), lock_path=str(LOCK),
             requested_at=now(), status="WAITING_RESOURCE_LOCK")
write_json(OUT / "resource-lease.json", lease)
lock_handle = LOCK.open("a+")
while True:
    try:
        fcntl.flock(lock_handle.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
        break
    except BlockingIOError:
        print(now(), "等待另一 Run 释放正式生产资源锁", flush=True)
        time.sleep(15)
lease.update(status="HELD", acquired_at=now(), evidence=lock_evidence(lock_handle.fileno()))
assert lease["evidence"]["proc_locks"], "实际 flock 已返回，但 /proc/locks 无对应证据，停止生产"
write_json(OUT / "resource-lease.json", lease)
print(now(), "已取得共享生产锁", os.getpid(), flush=True)

overall = dict(run_id=RUN, call_id="C0004", started_at=now(), pid=os.getpid(),
               requested_symbols=["rb", "m"], requested_start="2021-01-01",
               requested_end="2021-12-31", mode="NEW_FORMAL_INSTANCE", symbols={})
try:
    import mquant
    assert "mquant.tis" not in sys.modules
    mquant.__path__.insert(0, str(OUT / "python/mquant"))
    import numpy as np
    import pandas as pd
    import pyarrow as pa
    import pyarrow.parquet as pq
    from m3tt import CurrTradeSet, CurrSymbol
    from mquant.quant import OptContext
    from mquant.frame import CurrCalendar
    from mquant.frame.lang.general import TmpStoreEnv
    from mquant.tis.hf.prel0.wall_assembler import WallAssembler
    from mquant.tis.hf.prel0.wall_assembler_core import run_wall_assembler_replay
    from mquant.tis.hf.prel0.p1_product_receipt import feature_code_fingerprint
    from mquant.tis.hf.prel0.p1_product_receipt import load_p1_product_receipt, validate_product_artifact

    assert Path(inspect.getfile(WallAssembler)).resolve() == PIN / "hf/prel0/wall_assembler.py"
    assert Path(inspect.getfile(run_wall_assembler_replay)).resolve() == PIN / "hf/prel0/wall_assembler_core.py"
    assert subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=PIN, text=True).strip() == preflight["code_version"]
    assert not subprocess.check_output(["git", "status", "--porcelain", "--untracked-files=no"], cwd=PIN, text=True).strip()
    for relative, expected_hash in preflight["loaded_tis_sources"].items():
        assert sha256(PIN / relative) == expected_hash, relative
    for filename, expected_hash in preflight["runtime_generated_sources"].items():
        assert sha256(filename) == expected_hash, filename
    context = OptContext(preflight["requested_config"])
    assert context.ppdict == preflight["context"]
    # 两个正式品种都保持原范围；先取得 m 的真实入口证据，单品种失败不取消另一品种。
    for symbol in ("m", "rb"):
        target = OUT / "results" / symbol
        target.mkdir(parents=True, exist_ok=False)
        state = dict(symbol=symbol, run_id=RUN, status="PREPARING", pid=os.getpid(),
                     started_at=now(), requested_config=preflight["requested_config"],
                     calendar="night_end_at_2300", formal_feature_call_started=False, tables={})
        started = time.monotonic()
        try:
            with CurrTradeSet(context.sof), CurrSymbol(symbol), CurrCalendar(state["calendar"]):
                feature = WallAssembler()
                expected = preflight["symbols"][symbol]
                assert feature.ppdict == expected["ppdict"]
                assert feature_code_fingerprint(inspect.getfile(WallAssembler), run_wall_assembler_replay) == expected["code_fingerprint"]
                with TmpStoreEnv(WallAssembler, str(OUT / "native-cache")):
                    native = Path(feature.full_dir)
                    assert str(native) == expected["run_full_dir"]
                    assert not native.exists()
                    assert not feature.backup_full_dirs
                    surfaces = [native] + [Path(item["full_dir"]) for item in expected["upstreams"].values()]
                    audit = audit_writers(surfaces)
                    write_json(target / "single-writer-check.json", audit)
                    assert not audit["conflicting_write_fds"], audit["conflicting_write_fds"]
                    state.update(status="FORMAL_RUNNING", formal_feature_call_started=True,
                                 formal_call_at=now(), full_dir=str(native), ppid=feature.ppid,
                                 ppdict=feature.ppdict, code_fingerprint=expected["code_fingerprint"],
                                 lock_evidence=lock_evidence(lock_handle.fileno()))
                    write_json(target / "result.json", state)
                    print(now(), symbol, "调用原生默认 WallAssembler().run()", str(native), flush=True)
                    result = feature.run()
                    frames = dict(result.F)
                    receipt = load_p1_product_receipt(feature, "wall_lifecycle")
                    validate_product_artifact(receipt, frames)
                    assert receipt["code_version"] == expected["code_fingerprint"]
                    assert receipt["actual_business_parameters"] == expected["effective_wall_parameters"]
                    write_json(target / "receipt.json", receipt)
                    state.update(status="EXPORTING", result_keys=list(frames))
                    write_json(target / "result.json", state)
                    exports = target / "tables"
                    exports.mkdir()
                    for key, frame in frames.items():
                        assert isinstance(frame, pd.DataFrame), key
                        path = exports / (key + ".parquet")
                        writer = None
                        try:
                            for start in range(0, max(1, len(frame)), 250000):
                                table = pa.Table.from_pandas(frame.iloc[start:start + 250000], preserve_index=True)
                                if writer is None:
                                    writer = pq.ParquetWriter(path, table.schema, compression="zstd")
                                writer.write_table(table, row_group_size=250000)
                        finally:
                            if writer is not None:
                                writer.close()
                        assert pq.read_metadata(path).num_rows == len(frame)
                        state["tables"][key] = dict(path=str(path), rows=len(frame), columns=list(frame.columns),
                                                    dtypes={str(key): str(value) for key, value in frame.dtypes.items()},
                                                    first_time=str(frame.index[0]) if len(frame) else None,
                                                    last_time=str(frame.index[-1]) if len(frame) else None,
                                                    sha256=sha256(path), bytes=path.stat().st_size,
                                                    sorted=bool(frame.index.is_monotonic_increasing))
                        write_json(target / "result.json", state)
                        print(now(), symbol, "已导出", key, len(frame), flush=True)
                    for name in ["fields.json", "p1_receipts/wall_lifecycle.json"]:
                        path = native / name
                        assert path.is_file(), path
                    state.update(status="FORMAL_RESULT_EXPORTED", native_fields_sha256=sha256(native/"fields.json"),
                                 native_receipt_sha256=sha256(native/"p1_receipts/wall_lifecycle.json"),
                                 independent_readback="PENDING")
                    del frames, result
        except BaseException as error:
            state.update(status="FAILED", error_type=type(error).__name__, error=str(error),
                         traceback=traceback.format_exc())
            print(now(), symbol, "正式尝试失败；保留证据并继续另一授权品种", flush=True)
            traceback.print_exc()
        finally:
            state.update(finished_at=now(), elapsed_seconds=time.monotonic() - started,
                         peak_rss_mib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024)
            write_json(target / "result.json", state)
            overall["symbols"][symbol] = {key: state.get(key) for key in
                                         ["status", "formal_feature_call_started", "full_dir", "error_type", "error"]}
            write_json(OUT / "formal-status.json", overall)
    overall["finished_at"] = now()
    overall["status"] = "PRODUCED_PENDING_READBACK" if all(item["status"] == "FORMAL_RESULT_EXPORTED" for item in overall["symbols"].values()) else "PARTIAL_OR_BLOCKED"
    write_json(OUT / "formal-status.json", overall)
finally:
    lease.update(status="RELEASED", released_at=now(), before_release=lock_evidence(lock_handle.fileno()))
    fcntl.flock(lock_handle.fileno(), fcntl.LOCK_UN)
    lock_handle.close()
    write_json(OUT / "resource-lease.json", lease)
    print(now(), "已释放共享生产锁", flush=True)
