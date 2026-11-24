"""只构造参数对象；任何 Feature.run/rerun 均在本探针内禁止。"""
import contextlib
import hashlib
import io
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path("/dwdhome/fy/BASE_E6_2_copy")
OUT = ROOT / "artifacts/OI-EAW-P1-ATTACK-STAT-20261124-01/D001/evidence"
OUT.mkdir(parents=True, exist_ok=True)
with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
    from mquant.frame.lang.internal.base import AbsFao
    def forbidden(*args, **kwargs):
        raise RuntimeError("D001_U_PROBE_FORBIDS_FEATURE_EXECUTION")
    AbsFao.run = forbidden
    AbsFao.rerun = forbidden
    AbsFao._run_with = forbidden
    import mquant.tis.hf.prel0.attack_flow_assembler as attack_module
    import mquant.tis.hf.prel0.attack_flow_assembler_core as core_module
    import mquant.tis.hf.prel0.wall_assembler as wall_module
    import mquant.tis.hf.prel0.pressure_big_deal as f4_module
    instance = attack_module.AttackFlowAssembler()
    def encode(value):
        if value is None or isinstance(value, (str, int, float, bool)):
            return value
        if isinstance(value, dict) or hasattr(value, "items"):
            return {str(k): encode(v) for k, v in value.items()}
        if isinstance(value, (tuple, list)):
            return [encode(v) for v in value]
        if hasattr(value, "val"):
            return encode(value.val)
        if hasattr(value, "P"):
            return {"type": type(value).__module__+"."+type(value).__name__, "parameters": encode(value.P)}
        return repr(value)
    result = {
        "probe_kind": "CONSTRUCTOR_AND_PARAMETER_INTROSPECTION_ONLY",
        "feature_executed": False,
        "feature_run_entrypoints_guarded": True,
        "actual_cwd": str(Path.cwd().resolve()),
        "sys_executable": sys.executable,
        "tis_head": subprocess.check_output(["git", "-C", str(ROOT/"mquant/tis"), "rev-parse", "HEAD"], text=True).strip(),
        "module_files": {name: str(Path(module.__file__).resolve()) for name,module in [("attack",attack_module),("core",core_module),("wall",wall_module),("f4",f4_module)]},
        "instance_type": type(instance).__module__+"."+type(instance).__name__,
        "parameters": encode(instance.P),
        "ppdict": encode(instance.ppdict),
        "ppid": str(instance.ppid),
        "upstream_instances": {
            key: {"type": type(value).__module__+"."+type(value).__name__, "parameters": encode(value.P), "ppdict": encode(value.ppdict), "ppid": str(value.ppid)}
            for key, value in [("wall",instance.P.wall),("tactical",instance.P.directed_large_deal_tactical),("structural",instance.P.directed_large_deal_structural)]
        },
        "runtime_receipts": "UNCONFIRMED",
        "formal_result_readback": "UNCONFIRMED"
    }
for name, path in result["module_files"].items():
    result.setdefault("module_sha256", {})[name] = hashlib.sha256(Path(path).read_bytes()).hexdigest()
(OUT/"instance_introspection.json").write_text(json.dumps(result, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
print(json.dumps({"probe_kind":result["probe_kind"], "feature_executed":False, "module_files":result["module_files"], "evidence_path":str(OUT/"instance_introspection.json")},ensure_ascii=False))

