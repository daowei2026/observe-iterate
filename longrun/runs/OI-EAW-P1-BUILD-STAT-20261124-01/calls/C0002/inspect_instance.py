import hashlib
import importlib
import inspect
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path("/dwdhome/fy/BASE_E6_2/artifacts/oi-eaw-p1-build-stat-20261124-01/calls/C0002")
WORKSPACE = Path("/dwdhome/fy/BASE_E6_2")
sys.path.insert(0, str(WORKSPACE))
m = importlib.import_module("mquant.tis.hf.prel0.build_assembler")
from mquant.frame import AbsFao
def forbidden(*args, **kwargs):
    raise RuntimeError("D001 U forbids Feature execution")
AbsFao._run_with = forbidden
f = m.BuildAssembler()
fields = [
    "parameter_set_id", "active_flow_same_best_tol_ticks", "t_build_ticks",
    "reload_start_ratio", "reload_stop_ratio", "build_start_window_ticks",
    "build_stop_window_ticks", "milestone_levels", "require_best_price_stable",
    "attack_near_band_ticks",
]
tis = WORKSPACE / "mquant/tis"
paths = [
    "hf/prel0/build_assembler.py", "hf/prel0/build_assembler_core.py",
    "hf/prel0/wall_assembler.py", "hf/prel0/wall_assembler_core.py",
    "hf/prel0/p1_dba_export.py", "hf/prel0/p1_product_receipt.py",
    "hf/prel0/tick_quote_context.py", "hf/prel0/pressure_big_deal.py",
    "hf/prel0/pressure_big_deal_core.py", "frp/EawBattleP.py",
    "frpExample/STCalendar.py",
]
versions = []
for rel in paths:
    data = (tis / rel).read_bytes()
    committed = subprocess.check_output(["git", "-C", str(tis), "show", "179016111ed0394f92025313e46bd13534932a74:" + rel])
    versions.append({"path": rel, "sha256": hashlib.sha256(data).hexdigest(), "git_blob": subprocess.check_output(["git", "-C", str(tis), "hash-object", str(tis / rel)], text=True).strip(), "baseline_blob": subprocess.check_output(["git", "-C", str(tis), "rev-parse", "179016111ed0394f92025313e46bd13534932a74:" + rel], text=True).strip(), "matches_baseline": data == committed})
from mquant.tis.hf.prel0.p1_product_receipt import feature_code_fingerprint
from mquant.tis.hf.prel0.build_assembler_core import make_build_params
params = {key: getattr(f.P, key) for key in fields}
effective = make_build_params(**{key: params[key] for key in ["t_build_ticks", "reload_start_ratio", "reload_stop_ratio", "build_start_window_ticks", "build_stop_window_ticks", "milestone_levels", "require_best_price_stable", "attack_near_band_ticks"]})
result = {
    "inspection_kind": "CONSTRUCTOR_AND_SOURCE_ONLY_NO_FEATURE_EXECUTION",
    "module": m.__name__, "module_file": inspect.getsourcefile(m.BuildAssembler),
    "class": type(f).__name__, "ppdict": f.ppdict, "ppid": f.ppid,
    "param_path": f.param_path, "parameters": params,
    "effective_core_parameters": effective,
    "wall": {"module": type(f.P.wall).__module__, "class": type(f.P.wall).__name__, "ppdict": f.P.wall.ppdict, "ppid": f.P.wall.ppid},
    "code_version": feature_code_fingerprint(m.__file__, m.run_build_assembler_replay, m.compute_transient_active_flow_chunk),
    "stcalendar_loaded_module": getattr(sys.modules.get("mquant.tis.frpExample.STCalendar"), "__file__", None),
    "versions": versions,
    "formal_scope": {"sof_name": "TA_updto20240229_DBA", "symbols": ["rb", "m"], "start": "2021-01-01", "end": "2021-12-31", "calendar": "night_end_at_2300", "actual_market_data_read": False, "formal_result_read": False},
}
(ROOT / "instance-inspection.json").write_text(json.dumps(result, ensure_ascii=False, indent=2, default=str) + "\n", encoding="utf-8")
print(json.dumps(result, ensure_ascii=False, indent=2, default=str))

