"""未修改组件的诊断运行：物化资格/checkpoint，并全量对照已验证正式输出。"""
import fcntl
import hashlib
import inspect
import json
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

OUT=Path(__file__).resolve().parent
TARGET=OUT/"rb-upstream-checkpoint-replay"
TARGET.mkdir(exist_ok=False)
LOCK=Path('/dwdhome/fy/cgpterm/artifacts/wall-f-closure-20261122/FORMAL_PRODUCTION.lock')
lease=dict(run_id="OI-WALL-STAT-20261122-01",call_id="C0004",kind="READ_ONLY_COMPONENT_DIAGNOSTIC_REPLAY",
           pid=os.getpid(),status="WAITING_RESOURCE_LOCK")
def save(name,obj):
    (TARGET/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2,default=str)+"\n")
save("resource-lease.json",lease)
handle=LOCK.open("a+")
while True:
    try:
        fcntl.flock(handle.fileno(),fcntl.LOCK_EX|fcntl.LOCK_NB)
        break
    except BlockingIOError:
        time.sleep(15)
lease.update(status="HELD",acquired_at=datetime.now(timezone.utc).isoformat(),fdinfo=Path(f'/proc/self/fdinfo/{handle.fileno()}').read_text())
save("resource-lease.json",lease)
summary=dict(run_id="OI-WALL-STAT-20261122-01",symbol="rb",status="RUNNING",
             mode="UNMODIFIED_COMPONENT_DIAGNOSTIC_RESULT",formal_feature_code_changed=False,
             formal_output_contract_changed=False,formal_feature_called=False)
try:
    import mquant
    assert 'mquant.tis' not in sys.modules
    mquant.__path__.insert(0,str(OUT/'python/mquant'))
    import numpy as np
    import pandas as pd
    import pyarrow as pa
    import pyarrow.parquet as pq
    from m3tt import CurrTradeSet,CurrSymbol
    from mquant.quant import OptContext
    from mquant.frame import CurrCalendar
    from mquant.tis.hf.prel0.wall_assembler import WallAssembler
    from mquant.tis.hf.prel0.wall_assembler_core import run_wall_assembler_replay
    from mquant.tis.hf.prel0.tick_quote_context import normalize_tick_quote_context_inputs,_EVENT_TYPE_CODE
    from mquant.tis.hf.prel0.tick_quote_context_core import compute_large_quote_chunk,compute_relative_thickness_chunk,DEFAULT_EPS_VOL
    from mquant.tis.hf.prel0.track_wall_candidates_core import compute_wall_brick_candidate_tick
    from mquant.tis.t0.gen.attr import minimal_changes_of
    preflight=json.loads((OUT/'preflight.json').read_text())
    defaults=preflight['symbols']['rb']['ppdict']
    assert Path(inspect.getfile(WallAssembler)).resolve()==OUT/'code/tis/hf/prel0/wall_assembler.py'
    assert Path(inspect.getfile(run_wall_assembler_replay)).resolve()==OUT/'code/tis/hf/prel0/wall_assembler_core.py'
    original_trace=pd.read_parquet(OUT/'results/rb/tables/wall_assembler_state_trace.parquet')
    original_events=pd.read_parquet(OUT/'results/rb/tables/wall_assembler_sparse_events.parquet')
    context=OptContext(preflight['requested_config'])
    with CurrTradeSet(context.sof),CurrSymbol('rb'),CurrCalendar('night_end_at_2300'):
        feature=WallAssembler();assert feature.ppdict==defaults
        cc_df=feature._load_cc_df();qt_df=feature._load_qt_df()
        assert cc_df.index.equals(original_trace.index)
        plan=feature._trading_day_chunk_plan(cc_df)
        thickness_carry=None;wall_carry=None;next_id=1
        event_rows=[];checkpoint_rows=[];writer=None
        counts={side:dict(raw_observations=0,finite_quote_observations=0,positive_qt_observations=0,
                          large_quote_observations=0,wall_brick_observations=0,large_but_thin_observations=0,
                          start_occurrences=0,candidate_without_new_start=0) for side in ['bid','ask']}
        inputs_digest=hashlib.sha256();verified_ticks=0
        try:
            for chunk_id,trade_day,chunk_df in feature._iter_trading_day_chunks(cc_df,plan):
                meta=feature._chunk_meta(chunk_id=chunk_id,boundary_type='trading_day',chunk_df=chunk_df,trade_day=trade_day)
                tape=feature._build_context_tape_with_qt(chunk_df,qt_df=qt_df)
                arrays=normalize_tick_quote_context_inputs(tape)
                f1=compute_large_quote_chunk(bid_vol1=arrays['bid_vol1'],ask_vol1=arrays['ask_vol1'],
                    QT_bid=arrays['QT_bid'],QT_ask=arrays['QT_ask'],session_ok=arrays['session_ok'],
                    large_quote_ratio_min=defaults['large_quote_ratio_min'],allow_zero_qt_fallback=defaults['allow_zero_qt_fallback'],eps_vol=DEFAULT_EPS_VOL)['f1_out']
                thickness=compute_relative_thickness_chunk(bid_vol1=arrays['bid_vol1'],ask_vol1=arrays['ask_vol1'],
                    session_ok=arrays['session_ok'],W_depth_ref_ticks=defaults['w_depth_ref_ticks'],carry_in_state=thickness_carry,
                    thick_vs_hi_ratio=defaults['thick_vs_hi_ratio'],thin_vs_mid_ratio=defaults['thin_vs_mid_ratio'],eps_vol=DEFAULT_EPS_VOL)
                f2=thickness['f2_out']
                f6=compute_wall_brick_candidate_tick(bid_px1=arrays['bid_px1'],ask_px1=arrays['ask_px1'],
                    flag_large_quote_bid=f1['flag_large_quote_bid'],flag_large_quote_ask=f1['flag_large_quote_ask'],
                    thin_flag_bid=f2['thin_flag_bid'],thin_flag_ask=f2['thin_flag_ask'],
                    large_ratio_bid=f1['large_ratio_bid'],large_ratio_ask=f1['large_ratio_ask'],allow_thin_brick=defaults['allow_thin_brick'])
                kwargs={key:defaults[key] for key in inspect.signature(run_wall_assembler_replay).parameters if key in defaults}
                kwargs.update(uti=tape['uti'],ts=chunk_df.index.values,last_px=np.asarray(chunk_df.price.values,dtype=np.float64),
                    tick_size=float(minimal_changes_of(CurrSymbol.sym(),chunk_df.index[0])),carry_in_state=wall_carry,next_wall_id=next_id)
                for side in ['bid','ask']:
                    for key in [side+'_px1',side+'_vol1']:kwargs[key]=arrays[key]
                    for prefix in ['flag_wall_brick_candidate_','brick_price_','brick_strength_']:kwargs[prefix+side]=f6[prefix+side]
                    for prefix in ['flag_large_quote_','large_ratio_']:kwargs[prefix+side]=f1[prefix+side]
                    for prefix in ['thickness_ratio_','thick_flag_','thin_flag_']:kwargs[prefix+side]=f2[prefix+side]
                result=run_wall_assembler_replay(**kwargs)
                observed_trace=feature._wall_state_trace_frame(chunk_id,dict(uti=np.asarray(tape['uti'],dtype=np.int64),
                    ts=np.asarray(chunk_df.index.values,dtype='datetime64[ns]'),**result['wall_state_trace']))
                expected=original_trace.iloc[verified_ticks:verified_ticks+len(chunk_df)]
                pd.testing.assert_frame_equal(observed_trace.sort_index(axis=1),expected.sort_index(axis=1),check_exact=True)
                observation=pd.DataFrame(dict(uti=np.asarray(tape['uti'],dtype=np.int64)),index=chunk_df.index)
                for side in ['bid','ask']:
                    start_uti=[e['uti'] for e in result['events'] if e['side']==side and e['event_type']=='Wall.Start.ByBigQuote']
                    starts=np.isin(tape['uti'],start_uti)
                    large=f1['flag_large_quote_'+side]!=0;thin=f2['thin_flag_'+side]!=0;candidate=f6['flag_wall_brick_candidate_'+side]!=0
                    finite=np.isfinite(arrays[side+'_px1'])&np.isfinite(arrays[side+'_vol1'])&np.isfinite(kwargs['last_px'])
                    assert candidate[starts].all()
                    c=counts[side];c['raw_observations']+=len(chunk_df);c['finite_quote_observations']+=int(finite.sum())
                    c['positive_qt_observations']+=int((arrays['QT_'+side]>0).sum());c['large_quote_observations']+=int(large.sum())
                    c['wall_brick_observations']+=int(candidate.sum());c['large_but_thin_observations']+=int((large&thin).sum())
                    c['start_occurrences']+=len(start_uti);c['candidate_without_new_start']+=int((candidate&~starts).sum())
                    for name,value in [('finite_quote',finite),('positive_qt',arrays['QT_'+side]>0),('large_quote',large),('thin',thin),('wall_brick',candidate),('new_start',starts)]:
                        observation[name+'_'+side]=np.asarray(value,dtype=np.int8)
                table=pa.Table.from_pandas(observation,preserve_index=True)
                if writer is None:writer=pq.ParquetWriter(TARGET/'qualification-observations.parquet',table.schema,compression='zstd')
                writer.write_table(table)
                for event in result['events']:
                    row=dict(chunk_id=meta['chunk_id'],chunk_end_ts=meta['end_ts'],**feature._encode_wall_event(event))
                    row['event_type_code']=_EVENT_TYPE_CODE.get(row.pop('event_type'),0)
                    row['side_code']=1 if row.pop('side')=='bid' else 2
                    event_rows.append(row)
                for checkpoint in result['checkpoints']:
                    if 'event_type' in checkpoint:checkpoint_rows.append(dict(chunk_id=chunk_id,**checkpoint))
                raw_columns=['price','buy_price1','buy_vol1','sell_price1','sell_vol1','linear_ts']
                inputs_digest.update(pd.util.hash_pandas_object(chunk_df[raw_columns],index=True).values.tobytes())
                wall_carry=result['_carry_out_state'];next_id=result['_next_wall_id'];thickness_carry=thickness['carry_out_state']
                verified_ticks+=len(chunk_df)
                if (chunk_id+1)%25==0:print('诊断载体',chunk_id+1,'/',len(plan),'交易日，trace逐值相等',verified_ticks,flush=True)
        finally:
            if writer is not None:writer.close()
        events=pd.DataFrame.from_records(event_rows);events.index=pd.to_datetime(events.ts.values);events['availability_code']=np.int8(1)
        pd.testing.assert_frame_equal(events.sort_index(axis=1),original_events.sort_index(axis=1),check_exact=True)
        assert verified_ticks==len(original_trace)
        checkpoints=pd.DataFrame.from_records(checkpoint_rows);checkpoints.to_parquet(TARGET/'event-checkpoints.parquet',compression='zstd',index=False)
        far=checkpoints.loc[checkpoints.event_type.eq('Wall.End')&checkpoints.end_reason.eq('far_price')]
        assert len(far)==int((original_events.event_type_code.eq(7)&original_events.reason_code.eq(1)).sum())
        d4={side:dict(far_end_occurrences=int(far.side.eq(side).sum()),far_end_with_support=int((far.side.eq(side)&far.support_flag.ne(0)).sum()),
                     far_end_counter_below_hold=int((far.side.eq(side)&far.far_run_len.lt(preflight['symbols']['rb']['effective_wall_parameters']['end_far_hold_ticks'])).sum())) for side in ['bid','ask']}
        for side in ['bid','ask']:
            assert counts[side]['large_quote_observations']==counts[side]['wall_brick_observations']+counts[side]['large_but_thin_observations']
            assert counts[side]['wall_brick_observations']==counts[side]['start_occurrences']+counts[side]['candidate_without_new_start']
        for p in [TARGET/'qualification-observations.parquet',TARGET/'event-checkpoints.parquet']:
            d=hashlib.sha256()
            with p.open('rb') as f:
                for block in iter(lambda:f.read(4*1024*1024),b''):d.update(block)
            summary.setdefault('artifacts',[]).append(dict(path=str(p),sha256=d.hexdigest(),bytes=p.stat().st_size))
        summary.update(status='VERIFIED_DIAGNOSTIC_RESULT',code_version=preflight['code_version'],parameters=defaults,
            data_scope=preflight['requested_config'],calendar='night_end_at_2300',trace_rows_equal=verified_ticks,
            sparse_event_rows_equal=len(events),all_formal_trace_and_event_values_exact=True,
            input_values_hash_by_trading_day=inputs_digest.hexdigest(),qualification_counts=counts,d4_far_end_review=d4,
            checkpoint_rows=len(checkpoints),full_per_tick_far_history='NOT_EXPOSED',
            evidence_role='新增诊断运行载体，不冒充原WALL表中已有这些字段；未修改或替换正式Feature代码/输出。')
        save('diagnostic-result.json',summary)
        print(json.dumps(summary,ensure_ascii=False,indent=2),flush=True)
finally:
    lease.update(status='RELEASED',released_at=datetime.now(timezone.utc).isoformat())
    fcntl.flock(handle.fileno(),fcntl.LOCK_UN);handle.close();save('resource-lease.json',lease)
