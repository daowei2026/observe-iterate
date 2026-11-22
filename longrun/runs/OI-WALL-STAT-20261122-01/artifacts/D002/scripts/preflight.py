"""D002：读取隔离锁定实现、完整实例配置及原生结果身份。"""
import hashlib
import inspect
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

OUT = Path(__file__).resolve().parent
PIN = OUT / "code/tis"
VERSION = "6618d4d147d6ebbe634e61facddf2c9a0b996982"
import mquant
assert "mquant.tis" not in sys.modules
mquant.__path__.insert(0, str(OUT / "python/mquant"))

from m3tt import CurrTradeSet, CurrSymbol
from mquant.quant import OptContext
from mquant.frame import CurrCalendar
from mquant.frame.lang.general import TmpStoreEnv
from mquant.tis.hf.prel0.wall_assembler import WallAssembler
from mquant.tis.hf.prel0.wall_assembler_core import make_wall_params, run_wall_assembler_replay
from mquant.tis.hf.prel0.p1_product_receipt import feature_code_fingerprint
from mquant.tis.t0.gen.cc import SubContinuousContract
from mquant.tis.hf.qt import VolQuant

print("实际类文件", inspect.getfile(WallAssembler), flush=True)
print("实际core文件", inspect.getfile(run_wall_assembler_replay), flush=True)
print("TIS包搜索路径", list(sys.modules["mquant.tis"].__path__), flush=True)
module_paths = {name: str(Path(module.__file__).resolve())
                for name, module in list(sys.modules.items())
                if name.startswith("mquant.tis") and getattr(module, "__file__", None)}
(OUT / "loaded-module-paths.json").write_text(json.dumps(module_paths, ensure_ascii=False, indent=2) + "\n")
assert subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=PIN, text=True).strip() == VERSION
assert not subprocess.check_output(["git", "status", "--porcelain", "--untracked-files=no"], cwd=PIN, text=True).strip()
sources = {}
generated_sources = {}
assert Path(inspect.getfile(WallAssembler)).resolve() == PIN / "hf/prel0/wall_assembler.py"
assert Path(inspect.getfile(run_wall_assembler_replay)).resolve() == PIN / "hf/prel0/wall_assembler_core.py"
for module_name, module in list(sys.modules.items()):
    if module_name == "mquant.tis" or module_name.startswith("mquant.tis."):
        filename = getattr(module, "__file__", None)
        if filename:
            path = Path(filename).resolve()
            if path.suffix == ".py":
                original = Path("/dwdhome/fy/BASE_E6_2/mquant/tis")
                assert path.is_relative_to(PIN) or path.is_relative_to(original), (module_name, path)
                relative = path.relative_to(PIN if path.is_relative_to(PIN) else original).as_posix()
                pinned = subprocess.run(["git", "show", VERSION + ":" + relative], cwd=PIN, capture_output=True)
                if pinned.returncode == 0:
                    assert path.read_bytes() == pinned.stdout, (module_name, path)
                    sources[relative] = hashlib.sha256(path.read_bytes()).hexdigest()
                else:
                    generated_sources[str(path)] = hashlib.sha256(path.read_bytes()).hexdigest()

config = dict(sof_name="TA_updto20240229_DBA", stk_tlist="tick_test_all57_takeout_lcNsiNcy",
              startDay="2021-01-01", endDay="2021-12-31")
context = OptContext(config)
defaults = json.loads((Path("/dwdhome/fy/cgpterm/artifacts/wall-f-closure-20261122/OI-WALL-STAT-20261122-01/executor-records/longrun/runs/OI-WALL-STAT-20261122-01/calls/C0002/checks/DECLARED_DEFAULT_PARAMETERS.json")).read_text())["declared_defaults"]
report = dict(run_id="OI-WALL-STAT-20261122-01", call_id="C0004", code_version=VERSION,
              observed_at=datetime.now(timezone.utc).isoformat(), context=context.ppdict,
              requested_config=config, class_file=inspect.getfile(WallAssembler),
              class_realpath=str(Path(inspect.getfile(WallAssembler)).resolve()),
              loaded_tis_sources=sources, symbols={}, formal_feature_process_started=False)
report["runtime_generated_sources"] = generated_sources
for symbol in ("rb", "m"):
    with CurrTradeSet(context.sof), CurrSymbol(symbol), CurrCalendar("night_end_at_2300"):
        feature = WallAssembler()
        assert feature.ppdict == defaults
        normal_dir = Path(feature.full_dir)
        receipt_path = normal_dir / "p1_receipts/wall_lifecycle.json"
        existing = json.loads(receipt_path.read_text()) if receipt_path.exists() else None
        entry = dict(ppid=feature.ppid, ppdict=feature.ppdict, for_json=feature.for_json(),
                     calendar=CurrCalendar.name(True), cal_type=str(feature.hold_cal_type()),
                     original_full_dir=str(normal_dir), original_fields_exist=(normal_dir/"fields.json").exists(),
                     original_receipt=existing,
                     code_fingerprint=feature_code_fingerprint(inspect.getfile(WallAssembler), run_wall_assembler_replay),
                     effective_wall_parameters=make_wall_params(p_wall_ticks=1, t_wall_ticks=6), upstreams={})
        for key, upstream in [("cc", SubContinuousContract()), ("qt", VolQuant(freq="1d", n=30, quantile=.997))]:
            entry["upstreams"][key] = dict(ppid=upstream.ppid, full_dir=str(upstream.full_dir),
                                             fields_exists=(Path(upstream.full_dir)/"fields.json").exists(),
                                             cal_type=str(upstream.prop_cal_type))
        with TmpStoreEnv(WallAssembler, str(OUT / "native-cache")):
            entry["run_full_dir"] = str(feature.full_dir)
            entry["backup_full_dirs"] = list(feature.backup_full_dirs)
            assert Path(feature.full_dir).is_relative_to(OUT)
            assert not Path(feature.full_dir).exists(), feature.full_dir
            assert not feature.backup_full_dirs, feature.backup_full_dirs
        report["symbols"][symbol] = entry

path = OUT / "preflight.json"
path.write_text(json.dumps(report, ensure_ascii=False, indent=2, default=str) + "\n")
readback = json.loads(path.read_text())
assert readback["symbols"]["rb"]["ppdict"] == readback["symbols"]["m"]["ppdict"] == defaults
for symbol, entry in readback["symbols"].items():
    existing = entry["original_receipt"]
    print(symbol, "parameters=MATCH", "calendar=" + entry["calendar"],
          "old_code=" + (existing.get("code_version", "UNKNOWN") if existing else "NO_RECEIPT"),
          "new_full_dir=" + entry["run_full_dir"], flush=True)
print("锁定源码、完整参数和配置文件回读通过；尚未启动正式 Feature。", flush=True)
