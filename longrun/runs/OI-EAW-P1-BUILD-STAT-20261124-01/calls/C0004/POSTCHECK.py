import datetime as dt,fcntl,hashlib,json,os,subprocess,sys
from pathlib import Path
ROOT=Path("/dwdhome/fy/BASE_E6_2/artifacts/oi-eaw-p1-build-stat-20261124-01/calls/C0004")
WORKSPACE=Path("/dwdhome/fy/BASE_E6_2")
LOCK=Path("/dwdhome/fy/cgpterm/artifacts/wall-f-closure-20261122/FORMAL_PRODUCTION.lock")
def now():return dt.datetime.now(dt.timezone.utc).isoformat()
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def save(name,obj):(ROOT/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2,default=str)+"\n")
def inv(frames):return {k:{"rows":len(v),"columns":{c:str(t) for c,t in v.dtypes.items()},"first_index":str(v.index[0]) if len(v) else None,"last_index":str(v.index[-1]) if len(v) else None} for k,v in frames.items()}
lock=LOCK.open("r+b")
fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
proof={"lock_path":str(LOCK),"inode":os.fstat(lock.fileno()).st_ino,"acquired_at":now(),"size_before":os.fstat(lock.fileno()).st_size}
try:
    run=json.loads((ROOT/"run-manifest.json").read_text())
    assert "finished_at" in run,"production attempt still active/incomplete"
    sys.path.insert(0,str(WORKSPACE))
    from m3tt import CurrTradeSet,CurrSymbol
    from mquant.quant import OptContext
    from mquant.frame import CurrCalendar,TmpStoreEnv,AbsFao
    from mquant.tis.hf.prel0.build_assembler import BuildAssembler
    from mquant.tis.hf.prel0.tick_quote_context import VolQuant
    def deny(*args,**kwargs):raise RuntimeError("postcheck is strictly read-only")
    AbsFao._run_with=deny
    context=OptContext(run["context"])
    p=json.loads((ROOT/"preflight-context.json").read_text())
    reconciled=json.loads((ROOT/"rb-readback-reconciliation.json").read_text()) if (ROOT/"rb-readback-reconciliation.json").exists() else None
    out={"checked_at":now(),"run_status":run["status"],"symbols":{},"shared_historical_metadata":{},"stcalendar_sha256":sha(WORKSPACE/"mquant/tis/frpExample/STCalendar.py"),"tis_head":subprocess.check_output(["git","-C",str(WORKSPACE/"mquant/tis"),"rev-parse","HEAD"],text=True).strip(),"runtime_interpreter":sys.executable}
    with TmpStoreEnv(True,store_dir=str(ROOT/"formal_store")),CurrTradeSet(context.sof),CurrCalendar("night_end_at_2300"):
        for sym,s in run["symbols"].items():
            with CurrSymbol(sym):
                q=VolQuant(freq="1d",n=30,quantile=.997)
                x={"production_status":s["status"],"source_files_metadata_unchanged":s.get("input",{}).get("source_files_metadata_unchanged"),"wall_status":s.get("wall",{}).get("status"),"build_status":s.get("build",{}).get("status")}
                if (Path(q.full_dir)/"fields.json").exists():
                    qframes=dict(q.Dao.loadWith(str(q.full_dir)))
                    x["current_qt_readback"]={"path":q.full_dir,"ppid":q.ppid,"ppdict":q.ppdict,"inventory":inv(qframes),"fields_sha256":sha(Path(q.full_dir)/"fields.json"),"main_contract_input":{"path":str(Path(context.sof.sof_dir)/"tlist/main_contract"/(sym+".csv")),"sha256":sha(Path(context.sof.sof_dir)/"tlist/main_contract"/(sym+".csv"))}}
                verified_build=reconciled if sym=="rb" and reconciled and reconciled.get("status")=="COMPLETE_CURRENT_FORMAL" else s.get("build",{})
                x["effective_build_status"]=verified_build.get("status")
                if verified_build.get("status")=="COMPLETE_CURRENT_FORMAL":
                    b=BuildAssembler()
                    frames=dict(b.Dao.loadWith(str(b.full_dir)))
                    x["build_independent_readback"]={"path":b.full_dir,"keys":sorted(frames),"rows_by_key":{k:len(v) for k,v in frames.items()},"fields_sha256":sha(Path(b.full_dir)/"fields.json")}
                    assert set(frames)==set(verified_build["readback_inventory"])
                    assert {k:len(v) for k,v in frames.items()}=={k:v["rows"] for k,v in verified_build["readback_inventory"].items()}
                out["symbols"][sym]=x
                for name,old in p["symbols"][sym]["features"].items():
                    if name not in ["wall","build"] or not old.get("fields_exists"):continue
                    directory=Path(old["full_dir"])
                    checked={"path":str(directory),"fields_unchanged":sha(directory/"fields.json")==old["fields_sha256"],"receipt_unchanged":json.loads((directory/"p1_receipts"/(("wall_lifecycle" if name=="wall" else "build_activity")+".json")).read_text())==old["receipt"]}
                    assert checked["fields_unchanged"] and checked["receipt_unchanged"]
                    out["shared_historical_metadata"][sym+"_"+name]=checked
    assert out["stcalendar_sha256"]=="3001e49a3b812b5281ddca12795e5aa279d5ca09fd510ba0a4cfc330b42c6980"
    assert out["tis_head"]=="179016111ed0394f92025313e46bd13534932a74"
    save("postcheck.json",out)
    print(json.dumps({"postcheck":"DONE","symbols":{k:{"status":v["production_status"],"qt":v.get("current_qt_readback",{}).get("inventory"),"build_readback":v.get("build_independent_readback")} for k,v in out["symbols"].items()}},ensure_ascii=False))
finally:
    proof.update(released_at=now(),size_after=os.fstat(lock.fileno()).st_size)
    assert proof["size_before"]==proof["size_after"]==0
    fcntl.flock(lock,fcntl.LOCK_UN);lock.close();save("postcheck-lock.json",proof)
