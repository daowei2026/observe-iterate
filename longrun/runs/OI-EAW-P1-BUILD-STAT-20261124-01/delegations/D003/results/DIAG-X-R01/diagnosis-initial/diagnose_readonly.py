"""原诊断Skill的区分检查：只读本Run输入/旧产物，拒绝所有Feature写入。"""
import datetime as dt,gc,hashlib,json,subprocess,sys,traceback
from pathlib import Path
R=Path(__file__).resolve().parent
W=Path('/dwdhome/fy/BASE_E6_2')
OLD=W/'artifacts/oi-eaw-p1-build-stat-20261124-01/calls/C0004'
sys.path.insert(0,str(W))
def now():return dt.datetime.now(dt.timezone.utc).isoformat()
def save(name,obj):(R/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2,default=str)+'\n')
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
import numpy as np,pandas as pd
from m3tt import CurrTradeSet,CurrSymbol
from mquant.quant import OptContext
from mquant.frame import CurrCalendar,TmpStoreEnv,CurrCalType,CalType,AbsFao,StraApp
from mquant.tis.hf.prel0.build_assembler import BuildAssembler,BuildAssemblerWrapperSupport,_require_exact_axis
from mquant.tis.hf.prel0.tick_quote_context import SubContinuousContract
from mquant.tis.hf.prel0.p1_product_receipt import source_scope,load_p1_product_receipt
from mquant.tis.hf.mc import trading_days
calls=[]
original_run=AbsFao._run_with
def deny_write(self,write=False,read=False):
    calls.append({'feature':type(self).__name__,'write':write,'read':read})
    if write:raise RuntimeError('DIAGNOSTIC_ONLY: Feature DB/cache/result writes forbidden')
    return original_run(self,write=write,read=read)
AbsFao._run_with=deny_write
old=json.loads((OLD/'run-manifest.json').read_text())
oldpost=json.loads((OLD/'postcheck.json').read_text())
out={'started_at':now(),'scope':'DIAGNOSTIC_ONLY','formal_production_started':False,'shared_lock_acquired_for_production':False,'write_guard':'AbsFao._run_with(write=True) raises before implementation/load/dump','symbols':{}}
context=OptContext(old['context'])
quote=['price','buy_price1','buy_vol1','sell_price1','sell_vol1']
flow=['trade_volume','buy_order_price','buy_order_vol','sell_order_price','sell_order_vol']
wallcols=[f'wall_{field}_{side}' for side in ['bid','ask'] for field in ['id','side_code','status_code','band_lo','band_hi']]
def val(x):
    if pd.isna(x):return None
    if isinstance(x,(np.integer,np.floating)):return x.item()
    return str(x) if isinstance(x,(pd.Timestamp,np.datetime64)) else x
try:
 with TmpStoreEnv(True,store_dir=str(R/'diagnostic_unused_store')),CurrTradeSet(context.sof),CurrCalendar('night_end_at_2300'),CurrCalType({'SubContinuousContract':CalType.Cal}):
  for sym in ['rb','m']:
   with CurrSymbol(sym):
    raw=SubContinuousContract().rerun(CalType.Cal).F.value[context.sof.startDay:context.sof.endDay]
    b=BuildAssembler();wall=b.P.wall
    canonical=wall._load_cc_df()
    ranges=list(trading_days())
    covered=np.zeros(len(raw),dtype=bool)
    spans=[]
    for day,contract,duration in ranges:
     start=int(raw.index.searchsorted(pd.Timestamp(duration.start),'left'));stop=int(raw.index.searchsorted(pd.Timestamp(duration.stop),'right'))
     if stop>start:
      covered[start:stop]=True
      spans.append({'trade_day':str(day),'contract':contract,'start':start,'stop':stop,'duration_start':str(duration.start),'duration_stop':str(duration.stop)})
    support=BuildAssemblerWrapperSupport()
    try:old_plan=support._trading_day_chunk_plan(raw);raw_error=None
    except Exception as exc:old_plan=None;raw_error={'type':type(exc).__name__,'message':str(exc)}
    candidate=raw.loc[canonical.index].copy()
    candidate.attrs.update(canonical.attrs)
    plan=support._trading_day_chunk_plan(candidate)
    assert sum(stop-start for _,_,start,stop in plan)==len(candidate)
    assert raw.columns.equals(candidate.columns)
    pd.testing.assert_frame_equal(candidate[canonical.columns],canonical,check_exact=True)
    assert not len(canonical.index.difference(raw.index))
    removed=raw.index.difference(candidate.index)
    empty=raw[quote].isna().all(axis=1)
    assert removed.equals(raw.index[empty])
    assert not raw.index[~empty].difference(candidate.index).size
    oldwall=old['symbols'][sym]['wall']
    receipt=load_p1_product_receipt(oldwall['receipt']['artifact_location'],'wall_lifecycle')
    assert receipt==oldwall['receipt']
    frames=dict(wall.Dao.loadWith(receipt['artifact_location']))
    trace=frames['wall_assembler_state_trace']
    assert trace.index.equals(candidate.index)
    assert source_scope(sym,candidate,target=sym,calendar='night_end_at_2300')==receipt['source_scope']
    cases=[]
    for stamp in removed:
     pos=int(raw.index.get_loc(stamp))
     sample=raw.iloc[max(0,pos-1):min(len(raw),pos+3)]
     cases.append({'timestamp':stamp.isoformat(),'raw_position':pos,'inside_trading_day_duration':bool(covered[pos]),'prior_gap_ms':(stamp-raw.index[pos-1]).total_seconds()*1000 if pos else None,'row':{c:val(raw.iloc[pos][c]) for c in quote+flow+['linear_ts']},'neighbours':[{'timestamp':idx.isoformat(),**{c:val(row[c]) for c in quote+flow}} for idx,row in sample.iterrows()]})
    checks=[]
    if len(removed):
     stamp=removed[0];pos=int(raw.index.get_loc(stamp));idx=raw.index[max(0,pos-1):pos+2]
     try:_require_exact_axis('Wall artifact',trace,idx,wallcols);old_axis_error=None
     except Exception as exc:old_axis_error={'type':type(exc).__name__,'message':str(exc)}
     assert old_axis_error is not None
     good_idx=idx.intersection(candidate.index)
     _require_exact_axis('Wall artifact',trace,good_idx,wallcols)
     checks.append({'name':'同一真实局部输入只改变接入轴','raw_expected_axis_error':old_axis_error,'canonical_expected_axis_passes':True,'raw_axis':[str(x) for x in idx],'canonical_axis':[str(x) for x in good_idx]})
    main_csv=Path(context.sof.sof_dir)/'tlist/main_contract'/(sym+'.csv')
    assert sha(main_csv)==oldpost['symbols'][sym]['current_qt_readback']['main_contract_input']['sha256']
    source_meta=[]
    for before in old['symbols'][sym]['input']['source_files_after']:
     path=Path(before['path']);s=path.stat();after={'path':str(path),'realpath':str(path.resolve()),'size':s.st_size,'mtime_ns':s.st_mtime_ns,'inode':s.st_ino}
     assert before==after
     source_meta.append(after)
    out['symbols'][sym]={'raw_rows':len(raw),'raw_first':str(raw.index[0]),'raw_last':str(raw.index[-1]),'canonical_rows':len(candidate),'raw_chunk_plan_error':raw_error,'raw_chunks':None if old_plan is None else len(old_plan),'canonical_chunks':len(plan),'canonical_exact_wall_trace_axis':True,'canonical_receipt_source_scope_matches':True,'retained_all_flow_columns':list(candidate.columns),'all_nonempty_quote_rows_retained':True,'all_retained_values_exact':True,'removed_rows':cases,'raw_uncovered_positions':[{'position':int(p),'timestamp':str(raw.index[p])} for p in np.flatnonzero(~covered)],'trade_day_spans_around_failure':[x for x in spans if x['trade_day'].startswith(('2021-03-11','2021-03-12'))],'minimal_checks':checks,'canonical_source_scope':source_scope(sym,candidate,target=sym,calendar='night_end_at_2300'),'source_metadata_unchanged_since_C0004':True,'source_metadata':source_meta,'main_contract_csv_sha256':sha(main_csv),'default_ppid':b.ppid,'default_ppdict':dict(b.ppdict)}
    save('READONLY_DIAGNOSIS_EVIDENCE.json',out)
    print(json.dumps({'symbol':sym,'raw_rows':len(raw),'canonical_rows':len(candidate),'raw_error':raw_error,'canonical_chunks':len(plan),'removed_rows':len(removed),'uncovered_raw':int((~covered).sum())},ensure_ascii=False),flush=True)
   del raw,canonical,candidate,frames,trace
   StraApp.clear_cache();gc.collect()
 out.update(finished_at=now(),feature_calls=calls,all_feature_calls_read_only=all(not c['write'] for c in calls),status='COMPLETE_DIAGNOSTIC_CHECKS')
 assert out['all_feature_calls_read_only']
 assert subprocess.check_output(['git','-C',str(W/'mquant/tis'),'rev-parse','HEAD'],text=True).strip()=='179016111ed0394f92025313e46bd13534932a74'
 assert sha(W/'mquant/tis/frpExample/STCalendar.py')=='3001e49a3b812b5281ddca12795e5aa279d5ca09fd510ba0a4cfc330b42c6980'
 save('READONLY_DIAGNOSIS_EVIDENCE.json',out)
except Exception as exc:
 save('READONLY_DIAGNOSIS_ERROR.json',{'at':now(),'type':type(exc).__name__,'message':str(exc),'traceback':traceback.format_exc(),'feature_calls':calls})
 raise
