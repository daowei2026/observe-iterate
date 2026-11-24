"""在正式声明上下文中，只定位六张已存 receipt；禁止运行和物化 Feature。"""
import contextlib
import io
import json
from pathlib import Path
import traceback

OUT = Path("/dwdhome/fy/BASE_E6_2_copy/artifacts/OI-EAW-P1-ATTACK-STAT-20261124-01/D001/evidence")
result = {"probe_kind":"EXISTING_RECEIPT_PATHS_ONLY", "feature_executed":False, "formal_data_readback":False,
          "declared_scope":{"sof_name":"TA_updto20240229_DBA", "symbols":["rb","m"], "requested_start_time":"2021-01-01", "requested_end_time":"2021-12-31", "calendar":"night_end_at_2300"}, "candidates":[], "errors":[]}
try:
    with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
        from mquant.frame.lang.internal.base import AbsFao
        def forbidden(*args,**kwargs):
            raise RuntimeError("D001_U_PROBE_FORBIDS_FEATURE_EXECUTION")
        AbsFao.run = forbidden
        AbsFao.rerun = forbidden
        AbsFao._run_with = forbidden
        from mquant.quant import OptContext
        from m3tt import CurrTradeSet, CurrSymbol
        from mquant.frame import CurrCalendar
        from mquant.tis.hf.prel0.attack_flow_assembler import AttackFlowAssembler
        instance = AttackFlowAssembler()
        ctx = OptContext({"sof_name":"TA_updto20240229_DBA", "startDay":"2021-01-01", "endDay":"2021-12-31"})
        for symbol in ("rb","m"):
            with CurrTradeSet(ctx.sof), CurrSymbol(symbol), CurrCalendar("night_end_at_2300"):
                for label,feature,kinds in [
                    ("attack",instance,("attack_segment","attack_formation_evidence","wall_relation_barrier")),
                    ("wall",instance.P.wall,("wall_lifecycle",)),
                    ("tactical",instance.P.directed_large_deal_tactical,("directed_large_deal_stream",)),
                    ("structural",instance.P.directed_large_deal_structural,("directed_large_deal_stream",))
                ]:
                    directory = Path(feature.full_dir)
                    for kind in kinds:
                        path = directory/"p1_receipts"/(kind+".json")
                        entry={"symbol":symbol,"feature":label,"product_kind":kind,"candidate_directory":str(directory),"receipt_path":str(path),"receipt_exists":path.is_file(),"qualification":"CANDIDATE_ONLY_NOT_X_BINDING"}
                        if path.is_file():
                            if path.stat().st_size > 262144:
                                entry["error"]="RECEIPT_OVER_256_KIB_NOT_READ"
                            else:
                                entry["receipt_content"]=json.loads(path.read_text())
                        fields=directory/"fields.json"
                        entry["fields_json_exists"]=fields.is_file()
                        result["candidates"].append(entry)
except Exception as exc:
    result["errors"].append({"type":type(exc).__name__,"message":str(exc)})
(OUT/"existing_receipt_lookup.json").write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"candidate_count":len(result["candidates"]),"receipts_found":sum(x["receipt_exists"] for x in result["candidates"]),"errors":result["errors"],"feature_executed":False},ensure_ascii=False))

