"""独立进程只经原生 Dao 读回，逐表对照本 Run 的完整导出。"""
import hashlib
import inspect
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

OUT = Path(__file__).resolve().parent
import mquant
assert "mquant.tis" not in sys.modules
mquant.__path__.insert(0, str(OUT / "python/mquant"))
import pandas as pd
import pyarrow.parquet as pq
from m3tt import CurrTradeSet, CurrSymbol
from mquant.quant import OptContext
from mquant.frame import CurrCalendar
from mquant.frame.lang.general import TmpStoreEnv
from mquant.tis.hf.mc import trading_days
from mquant.tis.hf.prel0.wall_assembler import WallAssembler
from mquant.tis.hf.prel0.wall_assembler_core import run_wall_assembler_replay
from mquant.tis.hf.prel0.p1_product_receipt import feature_code_fingerprint
from mquant.tis.hf.prel0.p1_product_receipt import load_p1_product_receipt, validate_product_artifact


def sha256(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as handle:
        for block in iter(lambda: handle.read(4 * 1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


preflight = json.loads((OUT / "preflight.json").read_text())
context = OptContext(preflight["requested_config"])
report = dict(started_at=datetime.now(timezone.utc).isoformat(), method="INDEPENDENT_NATIVE_DAO_READ_ONLY",
              run_id="OI-WALL-STAT-20261122-01", requested_symbols=["rb", "m"], symbols={})
for symbol in ("rb", "m"):
    target = OUT / "results" / symbol
    attempt = json.loads((target / "result.json").read_text())
    if attempt["status"] != "FORMAL_RESULT_EXPORTED":
        report["symbols"][symbol] = dict(status="NO_VALID_FORMAL_RESULT", attempt_status=attempt["status"])
        continue
    expected = preflight["symbols"][symbol]
    with CurrTradeSet(context.sof), CurrSymbol(symbol), CurrCalendar("night_end_at_2300"):
        with TmpStoreEnv(WallAssembler, str(OUT / "native-cache")):
            feature = WallAssembler()
            native = Path(feature.full_dir)
            assert str(native) == expected["run_full_dir"] == attempt["full_dir"]
            assert feature.ppdict == expected["ppdict"]
            assert feature_code_fingerprint(inspect.getfile(WallAssembler), run_wall_assembler_replay) == expected["code_fingerprint"]
            assert sha256(native/"fields.json") == attempt["native_fields_sha256"]
            assert sha256(native/"p1_receipts/wall_lifecycle.json") == attempt["native_receipt_sha256"]
            frames = dict(feature.Dao.loadWith(str(native)))
            receipt = load_p1_product_receipt(feature, "wall_lifecycle")
            validate_product_artifact(receipt, frames)
            assert receipt["code_version"] == expected["code_fingerprint"]
            assert receipt["actual_business_parameters"] == expected["effective_wall_parameters"]
            assert set(frames) == set(attempt["tables"])
            tables = {}
            for key, frame in frames.items():
                metadata = attempt["tables"][key]
                assert sha256(metadata["path"]) == metadata["sha256"]
                exported = pd.read_parquet(metadata["path"])
                pd.testing.assert_frame_equal(frame, exported, check_exact=True)
                tables[key] = dict(rows=len(frame), exact_native_export_match=True,
                                   columns=list(frame.columns), sha256=metadata["sha256"])
                del exported
            trace = frames["wall_assembler_state_trace"]
            coverage = []
            offset = 0
            for day, contract, duration in trading_days():
                start = int(trace.index.searchsorted(pd.Timestamp(duration.start), side="left"))
                stop = int(trace.index.searchsorted(pd.Timestamp(duration.stop), side="right"))
                if stop <= start:
                    continue
                assert start == offset
                coverage.append(dict(trade_day=str(pd.Timestamp(day).date()), contract=str(contract),
                                     tick_rows=stop-start, first_time=str(trace.index[start]),
                                     last_time=str(trace.index[stop-1])))
                offset = stop
            assert offset == len(trace)
            assert trace.index.is_monotonic_increasing and trace.index.is_unique
            assert trace.index.min() >= pd.Timestamp("2021-01-01")
            assert trace.index.max() < pd.Timestamp("2022-01-01")
            pd.DataFrame(coverage).to_csv(target/"coverage_by_trading_day.csv", index=False)
            streams = []
            for key in sorted(key for key in frames if key.startswith("wall__stream")):
                frame = frames[key].copy()
                frame["physical_result_key"] = key
                if "occurrence_ordinal" not in frame:
                    frame["occurrence_ordinal"] = 0
                streams.append(frame)
            events = pd.concat(streams, copy=False)
            events["_physical_time"] = events.index
            events.sort_values(["_physical_time", "occurrence_ordinal"], kind="stable", inplace=True)
            events.drop(columns="_physical_time", inplace=True)
            event_path = target/"wall_events.parquet"
            events.to_parquet(event_path, compression="zstd", index=True)
            entry = dict(status="VERIFIED", full_dir=str(native), code_fingerprint=receipt["code_version"],
                         tables=tables, tick_rows=len(trace), first_time=str(trace.index.min()),
                         last_time=str(trace.index.max()), trading_day_chunks=len(coverage),
                         event_rows=len(events), merged_events_sha256=sha256(event_path),
                         native_fields_sha256=attempt["native_fields_sha256"],
                         native_receipt_sha256=attempt["native_receipt_sha256"],
                         readback_was_read_only=True)
            (target/"independent-readback.json").write_text(json.dumps(entry, ensure_ascii=False, indent=2)+"\n")
            report["symbols"][symbol] = entry
            print(symbol, "原生 Dao 与完整导出逐表逐行相等；交易日覆盖", len(coverage), flush=True)
            del frames, trace, events
report["finished_at"] = datetime.now(timezone.utc).isoformat()
report["status"] = "VERIFIED" if all(value["status"] == "VERIFIED" for value in report["symbols"].values()) else "PARTIAL_BINDING"
(OUT/"readback-summary.json").write_text(json.dumps(report, ensure_ascii=False, indent=2)+"\n")
print("独立读回状态", report["status"], flush=True)
