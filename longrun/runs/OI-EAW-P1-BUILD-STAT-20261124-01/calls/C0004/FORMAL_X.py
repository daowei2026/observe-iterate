"""C0004 / D002 original L0 X only. No TIS source edits, profiling or repair."""
import contextlib, datetime as dt, fcntl, gc, hashlib, inspect, json, os, subprocess, sys, time, traceback
from pathlib import Path
ROOT=Path("/dwdhome/fy/BASE_E6_2/artifacts/oi-eaw-p1-build-stat-20261124-01/calls/C0004")
WORKSPACE=Path("/dwdhome/fy/BASE_E6_2")
TIS=WORKSPACE/"mquant/tis"
LOCK=Path("/dwdhome/fy/cgpterm/artifacts/wall-f-closure-20261122/FORMAL_PRODUCTION.lock")
STORE=ROOT/"formal_store"
BASELINE="179016111ed0394f92025313e46bd13534932a74"
EXPECTED_STCAL="3001e49a3b812b5281ddca12795e5aa279d5ca09fd510ba0a4cfc330b42c6980"
def now():return dt.datetime.now(dt.timezone.utc).isoformat()
def write_json(path,obj):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    temp=path.with_name(path.name+".tmp")
    temp.write_text(json.dumps(obj,ensure_ascii=False,indent=2,default=str)+"\n")
    os.replace(temp,path)
def event(stage,**kw):
    e={"at":now(),"stage":stage,**kw}
    with (ROOT/"production-events.jsonl").open("a") as h:h.write(json.dumps(e,ensure_ascii=False,default=str)+"\n")
    write_json(ROOT/"production-status.json",e)
    print(json.dumps(e,ensure_ascii=False,default=str),flush=True)
def sha(path):
    h=hashlib.sha256()
    with Path(path).open("rb") as f:
        for block in iter(lambda:f.read(4*1024*1024),b""):h.update(block)
    return h.hexdigest()
def within(path,root=WORKSPACE):return Path(path).resolve().is_relative_to(root.resolve())
def source_stats(paths):
    return [{"path":str(p),"realpath":str(p.resolve()),"size":p.stat().st_size,"mtime_ns":p.stat().st_mtime_ns,"inode":p.stat().st_ino} for p in paths]
def frame_inventory(frames):
    return {str(k):{"rows":int(f.shape[0]),"columns":{str(c):str(t) for c,t in f.dtypes.items()},"index_dtype":str(f.index.dtype),"index_unique":bool(f.index.is_unique),"index_monotonic":bool(f.index.is_monotonic_increasing),"first_index":str(f.index[0]) if len(f) else None,"last_index":str(f.index[-1]) if len(f) else None} for k,f in frames.items()}
def result_file_manifest(path):
    files=sorted([p for p in path.iterdir() if p.is_file() and (p.suffix==".dba" or p.name=="fields.json")])
    receipt_dir=path/"p1_receipts"
    if receipt_dir.exists():files+=sorted(receipt_dir.glob("*.json"))
    return [{"path":str(p),"size":p.stat().st_size,"sha256":sha(p)} for p in files]
def path_descriptor(f):
    return {"ppid":f.ppid,"ppdict":f.ppdict,"param_path":f.param_path,"full_dir":str(f.full_dir),"realpath":str(Path(f.full_dir).resolve()),"backup_full_dirs":list(f.backup_full_dirs)}
def error_record(exc):
    return {"exception_type":type(exc).__name__,"message":str(exc),"traceback":traceback.format_exc()}
def assert_source_version():
    assert subprocess.check_output(["git","-C",str(TIS),"rev-parse","HEAD"],text=True).strip()==BASELINE
    assert sha(TIS/"frpExample/STCalendar.py")==EXPECTED_STCAL
    for rel in ["hf/prel0/build_assembler.py","hf/prel0/build_assembler_core.py","hf/prel0/wall_assembler.py","hf/prel0/wall_assembler_core.py","hf/prel0/p1_dba_export.py","hf/prel0/p1_product_receipt.py","hf/prel0/tick_quote_context.py","hf/prel0/pressure_big_deal.py","hf/prel0/pressure_big_deal_core.py"]:
        assert (TIS/rel).read_bytes()==subprocess.check_output(["git","-C",str(TIS),"show",BASELINE+":"+rel]),rel
lock_handle=LOCK.open("r+b")  # Exclusive NFS flock needs writable FD; no content writes.
lock_initial={"path":str(LOCK),"inode":os.fstat(lock_handle.fileno()).st_ino,"size":os.fstat(lock_handle.fileno()).st_size,"sha256":sha(LOCK)}
try:
    fcntl.flock(lock_handle,fcntl.LOCK_EX|fcntl.LOCK_NB)
except BlockingIOError:
    write_json(ROOT/"production-lock.json",{**lock_initial,"status":"CONTENDED","at":now()})
    raise SystemExit(75)
lock_held={**lock_initial,"status":"HELD","acquired_at":now(),"pid":os.getpid()}
write_json(ROOT/"production-lock.json",lock_held)
results={}
try:
    event("LOCK_ACQUIRED",lock_path=str(LOCK),lock_inode=lock_initial["inode"])
    if STORE.exists():
        raise RuntimeError("formal_store already exists; reconcile previous evidence, do not overwrite")
    STORE.mkdir()
    assert_source_version()
    sys.path.insert(0,str(WORKSPACE))
    import numpy as np,pandas as pd
    from m3tt import CurrTradeSet,CurrSymbol
    from mquant.quant import OptContext
    from mquant.frame import CurrCalendar,TmpStoreEnv,StraApp
    from mquant.tis.hf.prel0.build_assembler import BuildAssembler
    from mquant.tis.hf.prel0.build_assembler_core import make_build_params,run_build_assembler_replay
    from mquant.tis.hf.prel0.wall_assembler import WallAssembler
    from mquant.tis.hf.prel0.wall_assembler_core import make_wall_params,run_wall_assembler_replay
    from mquant.tis.hf.prel0.tick_quote_context import SubContinuousContract,VolQuant,_uti_from_linear_ts
    from mquant.tis.hf.prel0.pressure_big_deal import compute_transient_active_flow_chunk
    from mquant.tis.hf.prel0.p1_product_receipt import feature_code_fingerprint,load_p1_product_receipt,validate_product_artifact,source_scope
    config=dict(sof_name="TA_updto20240229_DBA",stk_tlist="tick_test_all57_takeout_lcNsiNcy",startDay="2021-01-01",endDay="2021-12-31")
    context=OptContext(config);sof=context.sof
    preflight=json.loads((ROOT/"preflight-context.json").read_text())
    expected_u=json.loads((WORKSPACE/"artifacts/oi-eaw-p1-build-stat-20261124-01/calls/C0002/instance-inspection.json").read_text())
    run_meta={"run_id":"OI-EAW-P1-BUILD-STAT-20261124-01","call_id":"C0004","delegation_id":"D002","work_item_id":"EAW-P1-BUILD-X-R01","stage_instance_id":"X-R01","started_at":now(),"context":config,"selected_symbols":["rb","m"],"calendar":"night_end_at_2300","tis_commit":BASELINE,"store_override":{"mechanism":"original platform TmpStoreEnv(True, store_dir=STORE)","store_root":str(STORE),"business_parameters_changed":False,"shared_default_outputs_readonly_preflight_only":True},"scope":"X engineering only; no G, diagnosis or repair","lock":lock_held,"symbols":results}
    write_json(ROOT/"run-manifest.json",run_meta)
    with TmpStoreEnv(True,store_dir=str(STORE)),CurrTradeSet(sof),CurrCalendar("night_end_at_2300"):
        for symbol in ["rb","m"]:
            sr={"symbol":symbol,"started_at":now(),"status":"IN_PROGRESS","formal_requested_range":{"start":"2021-01-01","end":"2021-12-31"}}
            results[symbol]=sr
            try:
                with CurrSymbol(symbol):
                    build=BuildAssembler();wall=build.P.wall
                    qt=VolQuant(freq=wall.P.qt_freq,n=wall.P.qt_n,quantile=wall.P.qt_quantile)
                    assert build.ppid==expected_u["ppid"]
                    assert json.loads(json.dumps(dict(build.ppdict),default=str))==expected_u["ppdict"],"U canonical defaults changed"
                    sr["instance"]={"build":path_descriptor(build),"wall":path_descriptor(wall),"wall_qt":path_descriptor(qt),"symbol_index":CurrSymbol.ii(),"trading_unit":float(sof.symbols_unit[CurrSymbol.ii()]),"calendar":CurrCalendar.name(True)}
                    for name in ["build","wall","wall_qt"]:
                        f=sr["instance"][name]
                        assert within(f["full_dir"]) and Path(f["full_dir"]).is_relative_to(STORE)
                        assert all(within(p) for p in f["backup_full_dirs"])
                        assert not (Path(f["full_dir"])/"fields.json").exists(),"do not reuse new-run stale output"
                    sr["expected_build_code_version"]=feature_code_fingerprint(inspect.getsourcefile(BuildAssembler),run_build_assembler_replay,compute_transient_active_flow_chunk)
                    sr["expected_wall_code_version"]=feature_code_fingerprint(inspect.getsourcefile(WallAssembler),run_wall_assembler_replay)
                    sr["historical_candidates"]={name:{"path":old["full_dir"],"receipt_code":old.get("receipt",{}).get("code_version"),"decision":"NOT_REUSED; receipt/source binding does not match current locked implementation","overwritten":False} for name,old in preflight["symbols"][symbol]["features"].items() if name in ["build","wall"] and old.get("receipt_exists")}
                    write_json(ROOT/(symbol+"-state.json"),sr)
                    event("INPUT_READ_STARTED",symbol=symbol)
                    raw=SubContinuousContract().rerun().F.value
                    raw=raw[sof.startDay:sof.endDay]
                    if raw.empty:raise RuntimeError("formal market input is empty")
                    assert raw.index.is_unique and raw.index.is_monotonic_increasing
                    required=["price","buy_price1","buy_vol1","sell_price1","sell_vol1","trade_volume","buy_order_price","buy_order_vol","sell_order_price","sell_order_vol","linear_ts"]
                    assert not (set(required)-set(raw.columns))
                    ori=Path(sof.ori_dir);cal=ori/"calendar"/"night_end_at_2300";cc=ori/"sub_continuous_contract"/"dba"/(symbol+"_night_end_at_2300")
                    source_files=[cal/"natural_tsa.dba",cal/"linear_tsa.dba"]+[cc/(c+".dba") for c in required if c!="linear_ts"]
                    source_before=source_stats(source_files)
                    quote=["price","buy_price1","buy_vol1","sell_price1","sell_vol1"]
                    empty=raw[quote].isna().all(axis=1)
                    sr["input"]={"rows":len(raw),"first_timestamp":raw.index[0].isoformat(),"last_timestamp":raw.index[-1].isoformat(),"first_uti":int(_uti_from_linear_ts(raw.linear_ts.values[:1])[0]),"last_uti":int(_uti_from_linear_ts(raw.linear_ts.values[-1:])[0]),"index_unique":True,"index_monotonic":True,"required_columns":required,"null_cells_by_required_field":{c:int(raw[c].isna().sum()) for c in required},"all_empty_quote_timestamps":[x.isoformat() for x in raw.index[empty]],"source_scope":source_scope(symbol,raw,target=symbol,calendar=CurrCalendar.name(True)),"source_files_before":source_before}
                    assert "2021-01-01"<=str(raw.index[0].date())<="2021-01-08"
                    assert str(raw.index[-1].date())=="2021-12-31"
                    write_json(ROOT/(symbol+"-input.json"),sr["input"])
                    event("WALL_STARTED",symbol=symbol,output=wall.full_dir,input_rows=len(raw))
                    wall_started=time.monotonic()
                    wall_frames=dict(wall.run().F)
                    wall_receipt=load_p1_product_receipt(wall,"wall_lifecycle")
                    assert wall_receipt["status"]=="success"
                    assert wall_receipt["code_version"]==sr["expected_wall_code_version"]
                    assert wall_receipt["parameter_set_id"]=="wall-default"
                    assert wall_receipt["artifact_location"]==str(wall.full_dir)
                    validate_product_artifact(wall_receipt,wall_frames)
                    wall_loaded=dict(wall.Dao.loadWith(str(wall.full_dir)))
                    assert set(wall_loaded)==set(wall_frames)
                    wall_input=wall._load_cc_df()
                    trace=wall_loaded["wall_assembler_state_trace"]
                    assert trace.index.equals(wall_input.index)
                    assert wall_receipt["source_scope"]==source_scope(symbol,wall_input,target=symbol,calendar=CurrCalendar.name(True))
                    cols=[f"wall_{field}_{side}" for side in ["bid","ask"] for field in ["id","side_code","status_code","band_lo","band_hi"]]
                    assert set(cols)<=set(trace.columns)
                    assert not trace[cols].isna().any().any()
                    sr["wall"]={"status":"READY_EXACT_CURRENT","elapsed_seconds":time.monotonic()-wall_started,"receipt":wall_receipt,"readback_inventory":frame_inventory(wall_loaded),"input_rows":len(wall_input),"input_scope":wall_receipt["source_scope"],"trace_rows":len(trace),"trace_axis_matches_wall_input":True,"trace_axis_matches_build_input":trace.index.equals(raw.index),"excluded_from_build_axis":[x.isoformat() for x in raw.index.difference(trace.index)],"files":result_file_manifest(Path(wall.full_dir))}
                    write_json(ROOT/(symbol+"-wall-binding.json"),sr["wall"])
                    write_json(ROOT/(symbol+"-state.json"),sr)
                    event("WALL_READBACK_VERIFIED",symbol=symbol,trace_rows=len(trace),build_axis_equal=trace.index.equals(raw.index))
                    event("BUILD_STARTED",symbol=symbol,output=build.full_dir)
                    build_started=time.monotonic()
                    try:
                        built=build.run()
                        build_frames=dict(built.F)
                        receipt=load_p1_product_receipt(build,"build_activity")
                        assert receipt["status"]=="success" and receipt["code_version"]==sr["expected_build_code_version"]
                        assert receipt["parameter_set_id"]=="build-default" and receipt["artifact_location"]==str(build.full_dir)
                        assert receipt["source_scope"]==sr["input"]["source_scope"]
                        expected_params={**expected_u["effective_core_parameters"],"active_flow_same_best_tol_ticks":expected_u["parameters"]["active_flow_same_best_tol_ticks"]}
                        assert receipt["actual_business_parameters"]==expected_params
                        upstream=receipt["direct_upstream_artifacts"]
                        assert len(upstream)==1
                        assert upstream[0]=={k:wall_receipt[k] for k in upstream[0]}
                        validate_product_artifact(receipt,build_frames)
                        loaded=dict(build.Dao.loadWith(str(build.full_dir)))
                        assert set(loaded)==set(build_frames)
                        for key,df in loaded.items():
                            if key.startswith("build__"):
                                assert set(["build_id","wall_local_no","uti","ts","event_type_code","baseline_vol","cum_reload_proxy","availability_code","same_band_continuity_code","wall_slot_side_code"])<=set(df.columns)
                                assert df.index.is_unique and df.index.is_monotonic_increasing
                                assert df.equals(build_frames[key]),key
                                assert not df["build_id"].isna().any()
                                assert df.index.min()>=raw.index.min() and df.index.max()<=raw.index.max()
                                assert pd.DatetimeIndex(pd.to_datetime(df["ts"].values)).equals(df.index)
                        sr["build"]={"status":"COMPLETE_CURRENT_FORMAL","elapsed_seconds":time.monotonic()-build_started,"receipt":receipt,"readback_inventory":frame_inventory(loaded),"all_published_lanes_read":True,"actual_business_parameters_equal_u_effective":True,"exact_wall_receipt_reference_verified":True,"files":result_file_manifest(Path(build.full_dir))}
                        sr["status"]="COMPLETE_CURRENT_FORMAL"
                        write_json(ROOT/(symbol+"-build-binding.json"),sr["build"])
                        event("BUILD_READBACK_VERIFIED",symbol=symbol,result_keys=len(loaded))
                    except Exception as exc:
                        sr["build"]={"status":"BLOCKED_EXECUTION_OR_READBACK","elapsed_seconds":time.monotonic()-build_started,"error":error_record(exc),"fields_exists":(Path(build.full_dir)/"fields.json").exists(),"receipt_exists":(Path(build.full_dir)/"p1_receipts/build_activity.json").exists(),"artifact_directory":str(build.full_dir),"action":"No repair attempted; preserve actual exception for original manager."}
                        sr["status"]="PARTIAL_WALL_READY_BUILD_BLOCKED"
                        write_json(ROOT/(symbol+"-build-error.json"),sr["build"])
                        event("BUILD_BLOCKED",symbol=symbol,error_type=type(exc).__name__,message=str(exc))
                    sr["input"]["source_files_after"]=source_stats(source_files)
                    sr["input"]["source_files_metadata_unchanged"]=source_before==sr["input"]["source_files_after"]
                    if not sr["input"]["source_files_metadata_unchanged"]:sr["status"]="BLOCKED_SOURCE_CHANGED"
                    write_json(ROOT/(symbol+"-input.json"),sr["input"])
            except Exception as exc:
                sr["status"]="BLOCKED_PREREQUISITE"
                sr["prerequisite_error"]=error_record(exc)
                event("SYMBOL_PREREQUISITE_BLOCKED",symbol=symbol,error_type=type(exc).__name__,message=str(exc))
            finally:
                sr["finished_at"]=now()
                write_json(ROOT/(symbol+"-state.json"),sr)
                run_meta["symbols"]=results
                write_json(ROOT/"run-manifest.json",run_meta)
            # Release in-process feature/result caches before the other symbol, under same file lock.
            for name in ["raw","wall_input","wall_frames","wall_loaded","trace","build_frames","loaded","built"]:
                if name in globals():del globals()[name]
            StraApp.clear_cache();gc.collect()
    assert_source_version()
    run_meta["finished_at"]=now()
    run_meta["status"]="COMPLETE" if all(s["status"]=="COMPLETE_CURRENT_FORMAL" for s in results.values()) and len(results)==2 else "PARTIAL_OR_BLOCKED"
    write_json(ROOT/"run-manifest.json",run_meta)
    event("X_EPISODE_FINISHED",status=run_meta["status"],symbols={s:v["status"] for s,v in results.items()})
except BaseException as exc:
    write_json(ROOT/"fatal-error.json",error_record(exc));event("FATAL",error_type=type(exc).__name__,message=str(exc));raise
finally:
    assert os.fstat(lock_handle.fileno()).st_ino==lock_initial["inode"]
    assert sha(LOCK)==lock_initial["sha256"]
    released={**lock_initial,"status":"RELEASED","released_at":now(),"content_unchanged":True}
    fcntl.flock(lock_handle,fcntl.LOCK_UN);lock_handle.close()
    write_json(ROOT/"production-lock-release.json",released)
    event("LOCK_RELEASED",content_unchanged=True)
