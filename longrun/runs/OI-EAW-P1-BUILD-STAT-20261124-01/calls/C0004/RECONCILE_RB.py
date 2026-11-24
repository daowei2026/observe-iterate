"""Resolve original readback guard only; rerun full rb in memory, never overwrite artifacts."""
import datetime as dt,fcntl,hashlib,json,os,sys,time,traceback
from pathlib import Path
ROOT=Path("/dwdhome/fy/BASE_E6_2/artifacts/oi-eaw-p1-build-stat-20261124-01/calls/C0004");WORKSPACE=Path("/dwdhome/fy/BASE_E6_2")
LOCK=Path("/dwdhome/fy/cgpterm/artifacts/wall-f-closure-20261122/FORMAL_PRODUCTION.lock")
def now():return dt.datetime.now(dt.timezone.utc).isoformat()
def save(name,x):(ROOT/name).write_text(json.dumps(x,ensure_ascii=False,indent=2,default=str)+"\n")
def sha(path):
    h=hashlib.sha256()
    with Path(path).open("rb") as f:
        for b in iter(lambda:f.read(4*1024*1024),b""):h.update(b)
    return h.hexdigest()
def inventory(frames):
    return {k:{"rows":len(v),"columns":{c:str(t) for c,t in v.dtypes.items()},"index_dtype":str(v.index.dtype),"index_unique":v.index.is_unique,"index_monotonic":v.index.is_monotonic_increasing,"first_index":str(v.index[0]) if len(v) else None,"last_index":str(v.index[-1]) if len(v) else None} for k,v in frames.items()}
lock=LOCK.open("r+b");fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
proof={"path":str(LOCK),"inode":os.fstat(lock.fileno()).st_ino,"acquired_at":now(),"size_before":os.fstat(lock.fileno()).st_size}
try:
    run=json.loads((ROOT/"run-manifest.json").read_text())
    assert "finished_at" in run,"production must finish first"
    sr=run["symbols"]["rb"]
    sys.path.insert(0,str(WORKSPACE))
    import numpy as np,pandas as pd
    from m3tt import CurrTradeSet,CurrSymbol
    from mquant.quant import OptContext
    from mquant.frame import CurrCalendar,TmpStoreEnv,CurrCalType,CalType
    from mquant.tis.hf.prel0.build_assembler import BuildAssembler
    from mquant.tis.hf.prel0.p1_product_receipt import load_p1_product_receipt
    context=OptContext(run["context"])
    out={"started_at":now(),"purpose":"Independent full-formal-rb recompute in memory to distinguish metadata ordering/widening from value mismatch; no G/repair.","initial_guard_error":sr["build"].get("error"),"artifact_overwritten":False}
    with TmpStoreEnv(True,store_dir=str(ROOT/"formal_store")),CurrTradeSet(context.sof),CurrCalendar("night_end_at_2300"),CurrSymbol("rb"):
        b=BuildAssembler();directory=Path(b.full_dir)
        files=sorted([p for p in directory.iterdir() if p.is_file() and (p.suffix==".dba" or p.name=="fields.json")])+sorted((directory/"p1_receipts").glob("*.json"))
        before={str(p):{"size":p.stat().st_size,"mtime_ns":p.stat().st_mtime_ns,"sha256":sha(p)} for p in files}
        loaded=dict(b.Dao.loadWith(str(directory)))
        receipt=load_p1_product_receipt(b,"build_activity")
        assert receipt["code_version"]==sr["expected_build_code_version"]
        with CurrCalType({"BuildAssembler":CalType.Cal,"WallAssembler":CalType.OnlyRead,"VolQuant":CalType.OnlyRead,"SubContinuousContract":CalType.Cal}):
            expected=dict(b.rerun().F)
        assert set(loaded)==set(expected)
        comparisons={}
        for key,actual in loaded.items():
            want=expected[key]
            c={"rows":len(actual),"column_names_equal":set(actual.columns)==set(want.columns),"original_column_order_equal":list(actual.columns)==list(want.columns),"loaded_column_order":list(actual.columns),"producer_column_order":list(want.columns),"dtype_differences":{col:{"producer":str(want[col].dtype),"loaded":str(actual[col].dtype)} for col in actual.columns if str(actual[col].dtype)!=str(want[col].dtype)}}
            assert c["column_names_equal"]
            for col,pair in c["dtype_differences"].items():
                assert pair=={"producer":"int8","loaded":"int64"},(key,col,pair)
            pd.testing.assert_frame_equal(actual.sort_index(axis=1),want.sort_index(axis=1),check_dtype=False,check_names=False,check_exact=True)
            assert actual.index.is_unique and actual.index.is_monotonic_increasing
            assert pd.DatetimeIndex(pd.to_datetime(actual["ts"].values)).equals(actual.index)
            c["all_values_exact_after_name_alignment"]=True
            comparisons[key]=c
        after={str(p):{"size":p.stat().st_size,"mtime_ns":p.stat().st_mtime_ns,"sha256":sha(p)} for p in files}
        assert before==after,"verification overwrote committed result"
        assert receipt["source_scope"]==sr["input"]["source_scope"]
        wall_receipt=load_p1_product_receipt(b.P.wall,"wall_lifecycle")
        assert receipt["direct_upstream_artifacts"]==[{k:wall_receipt[k] for k in receipt["direct_upstream_artifacts"][0]}]
        out.update(status="COMPLETE_CURRENT_FORMAL",finished_at=now(),receipt=receipt,readback_inventory=inventory(loaded),comparisons=comparisons,all_values_exact=True,artifacts_unchanged=True,files=[{"path":p,**x} for p,x in after.items()],explanation="Initial DataFrame.equals compared column order. DBA fields metadata restores columns by name in sorted order; int8 availability is canonically widened to int64 by current P1 exporter. All column values and event timestamps match full native replay exactly.")
    save("rb-readback-reconciliation.json",out)
    print(json.dumps({"rb_reconciliation":out["status"],"lanes":len(comparisons),"all_values_exact":True,"artifact_overwritten":False},ensure_ascii=False))
except Exception as exc:
    save("rb-reconciliation-error.json",{"at":now(),"type":type(exc).__name__,"message":str(exc),"traceback":traceback.format_exc()})
    raise
finally:
    proof.update(released_at=now(),size_after=os.fstat(lock.fileno()).st_size)
    assert proof["size_before"]==proof["size_after"]==0
    fcntl.flock(lock,fcntl.LOCK_UN);lock.close();save("rb-reconciliation-lock.json",proof)
