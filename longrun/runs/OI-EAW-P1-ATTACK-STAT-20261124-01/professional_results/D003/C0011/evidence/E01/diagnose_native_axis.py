"""DIAGNOSTIC_ONLY：读取本Run真实市场输入，纯内存检查原生分块合同；禁止Feature/cache/DBA写入。"""
import datetime
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import time
import traceback

BASE = Path(__file__).resolve().parent
OUT = BASE/'diagnostic-E01'
OUT.mkdir(exist_ok=False)
TIS = Path('/dwdhome/fy/BASE_E6_2_copy/mquant/tis')
RUN = 'OI-EAW-P1-ATTACK-STAT-20261124-01'
state = {'run_id':RUN,'call_id':'C0011','delegation_id':'D003','experiment_id':'E01','qualification':'DIAGNOSTIC_ONLY','started_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'sys_executable':sys.executable,'actual_cwd':str(Path.cwd().resolve()),'feature_or_cache_writes_permitted':False,'formal_Feature_run_performed':False,'G_performed':False,'checks':{},'errors':[]}
def now():return datetime.datetime.now(datetime.timezone.utc).isoformat()
def save():
    (OUT/'diagnostic_progress.json').write_text(json.dumps(state,ensure_ascii=False,indent=2,default=str)+'\n')
def event(stage,**kw):
    row={'at':now(),'stage':stage,**kw};state.update(current_stage=stage,last_update=row['at'])
    with (OUT/'diagnostic_events.jsonl').open('a')as f:f.write(json.dumps(row,ensure_ascii=False,default=str)+'\n')
    save();print(json.dumps(row,ensure_ascii=False,default=str),flush=True)
def digest_file(path):
    h=hashlib.sha256()
    with path.open('rb')as f:
        for block in iter(lambda:f.read(1048576),b''):h.update(block)
    return h.hexdigest()
def index_digest(index):
    ar=index.values;h=hashlib.sha256();h.update(str(ar.dtype).encode());h.update(str(ar.shape).encode())
    for start in range(0,len(ar),262144):h.update(ar[start:start+262144].tobytes())
    return h.hexdigest()
def file_snapshot(path):
    s=path.stat();v={'path':str(path),'bytes':s.st_size,'mtime_ns':s.st_mtime_ns}
    if path.suffix=='.json':v['sha256']=digest_file(path)
    return v
def tree_snapshot(root):return [file_snapshot(p)for p in sorted(root.rglob('*'))if p.is_file()]

binding=json.loads((BASE/'sources/x_binding.json').read_text())
store=Path(binding['storage_binding']['store_root'])
before=tree_snapshot(store)
(OUT/'preexisting_artifact_manifest.json').write_text(json.dumps(before,ensure_ascii=False,indent=2)+'\n')
assert subprocess.check_output(['git','-C',str(TIS),'rev-parse','HEAD'],text=True).strip()=='179016111ed0394f92025313e46bd13534932a74'
assert not subprocess.check_output(['git','-C',str(TIS),'status','--porcelain','--untracked-files=no'],text=True).strip()
sources=[]
for rel in ['t0/gen/cc.py','hf/mc.py','hf/prel0/tick_quote_context.py','hf/prel0/pressure_big_deal.py','hf/prel0/pressure_big_deal_core.py','hf/prel0/wall_assembler.py','hf/prel0/attack_flow_assembler.py','hf/prel0/p1_dba_export.py']:
    p=TIS/rel;raw=p.read_bytes();blob=hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()
    assert blob==subprocess.check_output(['git','-C',str(TIS),'rev-parse','HEAD:'+rel],text=True).strip()
    sources.append({'ref':'daowei2026/tis@179016111ed0394f92025313e46bd13534932a74:'+rel,'path':str(p),'git_blob_sha':blob,'sha256':hashlib.sha256(raw).hexdigest()})
state['implementation_sources']=sources
event('READONLY_DIAGNOSTIC_PREFLIGHT_COMPLETE',preexisting_artifact_files=len(before))
try:
    import numpy as np
    import pandas as pd
    from mquant.quant import OptContext
    from m3tt import CurrTradeSet,CurrSymbol
    from mquant.frame import CurrCalendar,CurrCalType,CurrFaoCache,CalType
    from mquant.frame.lang.internal.base import AbsFao
    from mquant.frame.core.app.env import StraEnv
    from mquant.tis.t0.gen.cc import SubContinuousContract
    import mquant.tis.hf.prel0.tick_quote_context as tq
    import mquant.tis.hf.prel0.pressure_big_deal as f4
    import mquant.tis.hf.prel0.wall_assembler as wall
    import mquant.tis.hf.prel0.p1_dba_export as export
    from mquant.tis.hf.mc import trading_days
    original_run_with=AbsFao._run_with
    calls=[]
    def readonly_run_with(self,write=False,read=False):
        row={'class':self.__class__.__name__,'write_requested':write,'read_requested':read};calls.append(row)
        if write or self.__class__.__name__!='SubContinuousContract':raise RuntimeError('E01_FORBIDS_PRODUCT_OR_CACHE_WRITES_AND_NON_SOURCE_FEATURE_EXECUTION')
        return original_run_with(self,write=False,read=read)
    def forbidden(*args,**kw):raise RuntimeError('E01_FORBIDS_FEATURE_DUMP_AND_DBA_WRITER')
    AbsFao._run_with=readonly_run_with
    export.P1DbaExportMixin.dump=forbidden
    export._P1ChunkedDbaWriter.__init__=forbidden
    context=OptContext({'sof_name':'TA_updto20240229_DBA','stk_tlist':'m','startDay':'2021-01-01','endDay':'2021-12-31'})
    with CurrFaoCache(),CurrTradeSet(context.sof),CurrSymbol('m'),CurrCalendar('night_end_at_2300'),CurrCalType({'SubContinuousContract':'cal'}):
        assert list(CurrTradeSet.symbols())==['m']and CurrSymbol.ii()==0
        assert StraEnv.rcal_type(SubContinuousContract())==CalType.Cal
        sof=CurrTradeSet.sof()
        main=Path(sof.sof_dir)/'tlist/main_contract/m.csv'
        raw_root=Path(sof.ori_dir)
        raw_paths=[p for folder in [raw_root/'sub_continuous_contract/dba/m_night_end_at_2300',raw_root/'calendar/night_end_at_2300']for p in sorted(folder.iterdir())if p.is_file()]
        raw_before=[file_snapshot(p)for p in raw_paths]
        main_sha=digest_file(main)
        state['data_binding']={'sof_name':'TA_updto20240229_DBA','requested_start':'2021-01-01','requested_end':'2021-12-31','calendar':'night_end_at_2300','symbol':'m','stk_tlist':'m','actual_symbols':list(CurrTradeSet.symbols()),'symbol_index':CurrSymbol.ii(),'trading_unit':sof.symbols_unit[CurrSymbol.ii()],'main_contract_file':str(main),'main_contract_sha256':main_sha,'raw_source_files':raw_before,'source_feature_cal_type':'Cal','market_or_calendar_data_written':False}
        event('READING_NATIVE_REAL_MARKET_SOURCE')
        support=tq.TickQuoteContextWrapperSupport()
        cc=support._load_cc_df()
        index=cc.index
        intervals=[];covered=np.zeros(len(cc),dtype=bool)
        for day,contract,duration in trading_days():
            start=int(index.searchsorted(pd.Timestamp(duration.start),side='left'));stop=int(index.searchsorted(pd.Timestamp(duration.stop),side='right'))
            if stop>start:
                intervals.append({'trade_day':str(pd.Timestamp(day)),'contract':str(contract),'declared_start':str(duration.start),'declared_stop':str(duration.stop),'start_pos':start,'stop_pos':stop})
                covered[start:stop]=True
        outside=np.flatnonzero(~covered)
        quotes=['price','buy_price1','buy_vol1','sell_price1','sell_vol1']
        market=[c for c in cc.columns if c!='linear_ts']
        empty=np.ones(len(cc),dtype=bool)
        for column in quotes:empty&=cc[column].isna().to_numpy()
        segment_start=np.r_[True,np.diff(index.asi8)>pd.Timedelta(milliseconds=500).value]
        def inspect_rows(positions):
            values=[]
            for pos in positions:
                row=cc.iloc[int(pos)];sample={str(k):(None if pd.isna(v)else v.item()if isinstance(v,np.generic)else v)for k,v in row.items()}
                values.append({'position':int(pos),'timestamp':str(index[pos]),'covered_by_native_trading_day':bool(covered[pos]),'segment_start':bool(segment_start[pos]),'all_five_quotes_null':bool(empty[pos]),'all_market_columns_null':bool(row[market].isna().all()),'values':sample})
            return values
        def native_plan(frame):
            try:
                result=support._trading_day_chunk_plan(frame)
                return {'status':'PASS','chunks':len(result),'rows_covered':int(sum(stop-start for _id,_day,start,stop in result)),'rows':len(frame),'first_chunk_trade_day':None if not result else str(result[0][1]),'last_chunk_trade_day':None if not result else str(result[-1][1])}
            except Exception as exc:return {'status':'ERROR','type':type(exc).__name__,'message':str(exc),'rows':len(frame)}
        original=native_plan(cc)
        state['checks']['full_native_m']={'rows':len(cc),'columns':list(cc.columns),'first_index':str(index[0]),'last_index':str(index[-1]),'index_unique':bool(index.is_unique),'index_monotonic':bool(index.is_monotonic_increasing),'index_digest':index_digest(index),'nonempty_trading_day_intervals':len(intervals),'all_five_quote_null_count':int(empty.sum()),'outside_interval_count':len(outside),'outside_interval_rows':inspect_rows(outside),'empty_quote_rows':inspect_rows(np.flatnonzero(empty)),'native_plan':original}
        (OUT/'native_trading_day_intervals.json').write_text(json.dumps(intervals,ensure_ascii=False,indent=2)+'\n')
        assert original=={'status':'ERROR','type':'ValueError','message':'交易日区间在 2021-03-12 00:00:00 前不连续: 1792800 != 1792801','rows':len(cc)}
        assert len(outside)>0
        first=int(outside[0]);surrounding=list(range(max(0,first-3),min(len(cc),first+4)))
        local=cc.iloc[surrounding]
        local_original=native_plan(local)
        local_without_gap=local.loc[covered[surrounding]]
        local_counter=native_plan(local_without_gap)
        valid_position=next(pos for pos in surrounding if covered[pos]and not empty[pos])
        local_drop_valid=native_plan(cc.iloc[[pos for pos in surrounding if pos!=valid_position]])
        first_next=next(i for i,row in enumerate(intervals)if row['start_pos']>first)
        boundary_pair=intervals[max(0,first_next-1):first_next+1]
        state['checks']['minimal_real_boundary_contrast']={'selection_reason':'原生全年计划的首个未覆盖行，取其前后各最多3条真实行；同一上下文和原生helper，无人工生成行情','qualification':'DIAGNOSTIC_ONLY','rows':inspect_rows(surrounding),'adjacent_declared_intervals':boundary_pair,'original':local_original,'in_memory_remove_only_uncovered_rows':local_counter,'negative_control_remove_one_covered_valid_row_keep_uncovered':local_drop_valid,'source_files_or_formal_artifacts_modified':False}
        assert local_original['status']=='ERROR'and local_counter['status']=='PASS'and local_drop_valid['status']=='ERROR'
        normal=next(row for row in intervals if row['trade_day'].startswith('2021-03-11'))
        normal_slice=cc.iloc[normal['stop_pos']-3:normal['stop_pos']]
        state['checks']['normal_real_rows_control']={'selection_reason':'紧邻首个失败边界之前，同一品种/代码/时间基础的三个已覆盖真实行','rows':[str(x)for x in normal_slice.index],'native_plan':native_plan(normal_slice)}
        assert state['checks']['normal_real_rows_control']['native_plan']['status']=='PASS'
        assert np.all(empty[outside])and np.all(segment_start[outside])
        filtered=cc.loc[covered]
        whole_counter=native_plan(filtered)
        state['checks']['full_index_coverage_counterfactual']={'qualification':'DIAGNOSTIC_ONLY','in_memory_rows_removed':len(outside),'only_uncovered_all_empty_segment_starts_removed':True,'native_plan':whole_counter,'not_a_formal_F4_result_or_fix':True,'original_index_digest_after_checks':index_digest(cc.index)}
        assert whole_counter['status']=='PASS'and whole_counter['rows_covered']==len(filtered)
        wall_cc=wall._exclude_empty_calendar_padding(cc,tuple(slice(pd.Timestamp(x['declared_start']),pd.Timestamp(x['declared_stop']))for x in intervals))
        old_wall=next(x for x in binding['per_feature_results']if x['symbol']=='m'and x['feature']=='wall')
        expected=next(x for x in old_wall['tables']if x['key']=='wall_assembler_state_trace')['full_readback_digest']['__index__']
        actual=index_digest(wall_cc.index)
        state['checks']['existing_wall_axis_contrast']={'qualification':'DIAGNOSTIC_ONLY_READONLY_EXISTING_LOGIC','raw_rows':len(cc),'native_wall_rows':len(wall_cc),'excluded_by_existing_wall_logic':len(cc)-len(wall_cc),'wall_axis_digest':actual,'same_as_current_Run_qualified_wall_trace':actual==expected,'native_plan_on_wall_axis':native_plan(wall_cc),'Wall_code_or_results_changed':False}
        assert actual==expected and state['checks']['existing_wall_axis_contrast']['native_plan_on_wall_axis']['status']=='PASS'
        state['checks']['source_representation_unchanged']={'source_index_same':state['checks']['full_native_m']['index_digest']==index_digest(cc.index),'raw_files_size_mtime_same':raw_before==[file_snapshot(p)for p in raw_paths],'main_contract_file_sha256_same':main_sha==digest_file(main)}
        assert all(state['checks']['source_representation_unchanged'].values())
        state['source_feature_calls']=calls
        assert calls and all(not x['write_requested']and x['class']=='SubContinuousContract'for x in calls)
        event('NATIVE_REAL_MARKET_DIAGNOSTIC_CHECKS_COMPLETE',outside_rows=len(outside),all_empty_rows=int(empty.sum()),native_plan_error=original['message'])
    state['status']='CHECKS_COMPLETE'
except Exception as exc:
    state['errors'].append({'type':type(exc).__name__,'message':str(exc)})
    (OUT/'diagnostic_traceback.txt').write_text(traceback.format_exc())
    state['status']='CHECKS_INCOMPLETE'
    event('DIAGNOSTIC_ERROR_RECORDED',type=type(exc).__name__,message=str(exc))
finally:
    after=tree_snapshot(store)
    state['preexisting_artifact_files_unchanged']=before==after
    state['preexisting_artifact_file_count']=len(before)
    state['tracked_TIS_changes_after']=subprocess.check_output(['git','-C',str(TIS),'status','--porcelain','--untracked-files=no'],text=True)
    state['finished_at']=now()
    (OUT/'diagnostic_result.json').write_text(json.dumps(state,ensure_ascii=False,indent=2,default=str)+'\n')
    event('DIAGNOSTIC_FINISHED',status=state['status'],artifacts_unchanged=state['preexisting_artifact_files_unchanged'])
