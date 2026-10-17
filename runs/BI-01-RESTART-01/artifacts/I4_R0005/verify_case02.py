#!/usr/bin/env python3
"""Bounded BI-01 Case-02 diagnostics, not a U2/U3 producer or Gate.
Usage: python verify_case02.py --input-dir /path/to/zips --output-dir ./evidence
Python 3.10+, pandas, numpy. No network calls. Original input files are read-only.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import zipfile
import numpy as np
import pandas as pd

A = 'steel_U2_U3_执行结果_20261010.zip'
B = 'rb_hc_i_mid贴近转折_zig_small_K线_20210101_20240229.zip'
HASHES = {A:'7bebbee3fd7d425eb85116f33c5d0e01ae2163e6849818515fe3824a82b9a46c',
          B:'4fd1af4e7b34af6fc099e6289ffdd5d83125412fc16d2a9902af4fd9741b3987'}
BASE = 'baseline_U2_C0_N_C1/'
SINGLE = 'single_scale_U2_C1_S_C2_U3/'
CASE = 'refonly-671359b4c10f73db5c'
IDS = {'hc':'refonly-d5b779f4ad88a8a276','rb':'refonly-910213b3cc62a71bdf',
       'i':'refonly-4af5fd6260f29a3c68'}
COMMON_START = '2021-05-10 21:30:00'
T0 = '2021-05-11 10:30:00'
LAST_BOUNDARY = '2021-05-12 09:30:00'
FOLLOW = ['2021-05-14 10:00:00','2021-05-18 10:00:00']
METHOD = 'BI01-I4-CASE02-DIAGNOSTIC-R0005-v1'
INVOCATION = 'BI01-RESTART-01-R0005-427e020c096844a98f9f46148fce405c'
TOL = 1e-10  # verification tolerance, never a market-price comparison epsilon

def require(ok: bool, reason: str) -> None:
    if not ok:
        raise ValueError(reason)

def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def rec(df: pd.DataFrame) -> list[dict]:
    return json.loads(df.to_json(orient='records',double_precision=15))

def write_json(path: Path, obj) -> None:
    path.write_text(json.dumps(obj,ensure_ascii=False,indent=2,allow_nan=False)+'\n',encoding='utf-8')

def quantities(prices, direction: int) -> dict:
    p=np.asarray(prices,dtype=float)
    require(len(p)>0 and np.isfinite(p).all(),'Unavailable selected close path')
    require(direction in (-1,1),'Direction must be explicit')
    x=direction*(p-p[0]); best=np.maximum.accumulate(x)
    length=float(np.abs(np.diff(p)).sum()); progress=float(x[-1])
    if progress==0: progress=0.0
    peak=float(best[-1]); counter=float(np.max(best-x))
    return dict(P=progress,L=length,E=abs(progress)/length if length else None,
        efficiency_applicability='Applicable' if length else 'NotApplicableZeroPathLength',
        counter=counter,peak=peak,retained=progress/peak if peak>0 else None,
        retained_applicability='Applicable' if peak>0 else 'NotApplicableNoFavorablePeak',
        progress_pct=100*progress/float(p[0]),counter_pct=100*counter/float(p[0]),
        extremes=int((x[1:]>best[:-1]).sum()),h=len(p)-1)

def main(input_dir: Path, output_dir: Path) -> None:
    output_dir.mkdir(parents=True,exist_ok=True)
    # Byte guards enforce the accepted binding. They do not re-adjudicate R0004.
    for name,expected in HASHES.items():
        require(sha((input_dir/name).read_bytes())==expected,f'Wrong frozen input: {name}')
    with zipfile.ZipFile(input_dir/A) as a, zipfile.ZipFile(input_dir/B) as b:
        pref=next(n for n in b.namelist() if n.endswith('/manifest.json')).rsplit('/',1)[0]+'/'
        def load(name: str) -> pd.DataFrame:
            df=pd.read_csv(a.open(name)); df['_csv_line']=np.arange(len(df))+2
            return df
        turns=load(BASE+'C0/02_turn_occurrences.csv')
        episodes=load(BASE+'C0/04_segment_episodes.csv')
        metrics=load(BASE+'C0/05_completed_episode_metrics.csv')
        cuts=load(BASE+'C0/06_episode_and_working_cuts_30m.csv')
        nodes=load(BASE+'N/01_node_behavior_cuts.csv')
        candidates=load(BASE+'C1/01_equal_actual_uti_candidate_facts.csv')
        pair=load(BASE+'C1/02_pair_input_facts.csv')
        relations=load(BASE+'C1/03_eight_relation_raw_observations.csv')
        members=load(BASE+'C1/04_member_post_turn_at_common_cut.csv')
        cand=candidates[candidates.ref_reference_candidate.eq(CASE)]
        require(len(cand)==1,'Exact frozen candidate not unique')
        c=cand.iloc[0]
        require(c.actual_uti==75344399 and c.common_visible_asof==T0 and
                c.member_symbols=='hc|rb' and c.member_count==2 and
                c.source_turn_types=='Peak' and c.source_expected_directions=='Down',
                'Frozen Case-02 identity mismatch')
        require(c.formal_formation_candidate_status=='NOT_ISSUED_SCOPE_MATRIX_DELTA_AND_EPOCH_NOT_EVALUATED',
                'Unexpected formal status; do not infer a formal candidate')
        anchors=turns[turns.ref_turn_id.isin(IDS.values())]
        selected=episodes[episodes.start_turn_id.isin(IDS.values())]
        require(len(anchors)==3 and len(selected)==3,'Ambiguous anchor/Episode')
        require(set(anchors.turn_type)=={'Peak'} and set(anchors.expected_direction)=={'Down'},'Wrong direction/type')
        bars={s:pd.read_csv(b.open(pref+s+'_kline_30m.csv')) for s in IDS}
        for s,k in bars.items():
            require(k.bar_ts.is_unique and k.bar_ts.is_monotonic_increasing,'Ambiguous price time')
        shared=bars['hc'].bar_ts.between('2021-05-10 11:00:00',FOLLOW[-1])
        grid=bars['hc'].loc[shared,['bar_ts','closeUti']].reset_index(drop=True)
        for s in IDS:
            k=bars[s]; g=k.loc[k.bar_ts.between(grid.bar_ts.iloc[0],grid.bar_ts.iloc[-1]),['bar_ts','closeUti']]
            require(g.reset_index(drop=True).equals(grid),f'Non-common bar grid: {s}')
        def window(s: str, start: str, end: str, direction: int=-1) -> dict:
            k=bars[s]; ii=k.index[k.bar_ts.eq(start)]; jj=k.index[k.bar_ts.eq(end)]
            require(len(ii)==len(jj)==1 and ii[0]<=jj[0],'Unresolved exact path endpoints')
            p=k.loc[ii[0]:jj[0]]
            require(p[['open','high','low','close']].notna().all().all(),
                    f'Original blank OHLC in {s} {start}..{end}; do not fill or drop')
            return dict(symbol=s,start=start,end=end,start_price=float(p.close.iloc[0]),
                end_price=float(p.close.iloc[-1]),price_member=pref+s+'_kline_30m.csv',
                first_csv_line=int(ii[0])+2,last_csv_line=int(jj[0])+2,blank_ohlc=0,
                direction='Down' if direction==-1 else 'Up',**quantities(p.close,direction))
        bi={s:int(bars[s].index[bars[s].bar_ts.eq(anchors[anchors.symbol.eq(s)].iloc[0].actual_ts)][0]) for s in IDS}
        require(bi['hc']==bi['rb'] and bi['hc']-bi['i']==5,'Actual five-bar separation mismatch')
        times=bars['hc'].loc[bars['hc'].bar_ts.between(T0,LAST_BOUNDARY),'bar_ts'].tolist()+FOLLOW
        eidx=episodes.set_index('ref_episode_id'); midx=metrics.set_index('ref_episode_id')
        original=[]; current=[]; event=[]; forward=[]; checks=[]
        for at in times:
            for s in IDS:
                ep=selected[selected.symbol.eq(s)].iloc[0]
                completed=at>=ep.completed_visible_from_proxy
                end=ep.actual_end_ts if completed else at
                original.append(dict(asof=at,stage='Completed' if completed else 'Working',
                    episode_id=ep.ref_episode_id,knowledge_from=ep.start_turn_known_from_proxy,
                    completion_visible=ep.completed_visible_from_proxy,
                    **window(s,ep.actual_start_ts,end)))
                nr=nodes[nodes.symbol.eq(s)&nodes.asof_event_ts_proxy.eq(at)].iloc[0]
                cr=cuts[cuts.symbol.eq(s)&cuts.asof_event_ts_proxy.eq(at)].iloc[0]
                ne=eidx.loc[nr.working_episode_ref]
                require(cr.working_episode_ref==nr.working_episode_ref,'N/C0 current Episode mismatch')
                require(ne.start_turn_known_from_proxy<=at,'Future start in current N')
                require(pd.isna(ne.completed_visible_from_proxy) or ne.completed_visible_from_proxy>at,
                        'N working Episode already completed at cut')
                if not completed:
                    require(nr.working_episode_ref==ep.ref_episode_id,'Original working reference replaced unexpectedly')
                v=window(s,ne.actual_start_ts,at,1 if ne.source_expected_direction=='Up' else -1)
                nn={'P':'working_prefix_progress','E':'working_prefix_efficiency',
                    'counter':'working_prefix_counter','extremes':'working_prefix_extreme_updates'}
                cc={'P':'working_raw_progress','E':'working_path_efficiency',
                    'counter':'working_raw_counter_move','extremes':'working_extreme_update_count'}
                err=max(abs(float(v[q])-float(nr[n])) for q,n in nn.items())
                err=max(err,max(abs(float(v[q])-float(cr[n])) for q,n in cc.items()))
                require(err<TOL,'Current raw KLine/C0/N mismatch')
                current.append(dict(asof=at,episode_id=nr.working_episode_ref,
                    original_episode=(nr.working_episode_ref==ep.ref_episode_id),
                    n_csv_line=int(nr['_csv_line']),c0_cut_csv_line=int(cr['_csv_line']),
                    knowledge_from=ne.start_turn_known_from_proxy,**v))
                checks.append(dict(symbol=s,asof=at,max_error=err))
                event.append(dict(asof=at,domain='COMMON_START_EVENT_WINDOW_NOT_EPISODE',
                    crosses_original_end=bool(at>ep.actual_end_ts),**window(s,COMMON_START,at)))
                forward.append(dict(asof=at,domain='COMMON_KNOWLEDGE_FORWARD_NOT_PNL',**window(s,T0,at)))
        canonical=[]
        for ep in selected.itertuples():
            v=window(ep.symbol,ep.actual_start_ts,ep.actual_end_ts)
            m=midx.loc[ep.ref_episode_id]
            pairs={'P':'raw_progress','L':'path_length','E':'path_efficiency',
                   'counter':'raw_counter_move','extremes':'extreme_update_count'}
            require(max(abs(float(v[q])-float(m[f])) for q,f in pairs.items())<TOL,'Canonical metric mismatch')
            canonical.append(dict(episode_id=ep.ref_episode_id,completion_visible=ep.completed_visible_from_proxy,
                metric_csv_line=int(m['_csv_line']),**v))
        maturity=[]
        for s in IDS:
            ep=selected[selected.symbol.eq(s)].iloc[0]
            for h in [1,3,6]:
                end=str(bars[s].iloc[bi[s]+h].bar_ts)
                require(end<=T0,'Future price in matched prefix')
                maturity.append(dict(asof=T0,domain='EQUAL_AGE_DIFFERENT_CALENDAR_ENDS',
                    retrospective_cross_end=bool(end>ep.actual_end_ts),**window(s,ep.actual_start_ts,end)))
        # Only new T0 historical efficiency is load-bearing for this question.
        parts=[]; offset=0
        for ch in pd.read_csv(a.open(BASE+'N/02_node_behavior_metrics.csv'),chunksize=40000):
            ch['_csv_line']=np.arange(len(ch))+offset+2; offset+=len(ch)
            parts.append(ch[ch.asof_event_ts_proxy.eq(T0)&ch.metric.eq('path_efficiency')])
        nh=pd.concat(parts,ignore_index=True); nchecks=[]; nwindows=[]
        for n in nodes[nodes.asof_event_ts_proxy.eq(T0)].itertuples():
            recent=n.recent_exact_6_ids.split('|'); previous=n.previous_exact_6_ids.split('|')
            require(len(set(recent))==6 and len(set(previous))==6 and not set(recent)&set(previous),'Invalid exact six windows')
            require((eidx.loc[recent+previous].completed_visible_from_proxy<=T0).all(),'Future Episode in N history')
            eligible=episodes[episodes.symbol.eq(n.symbol)&episodes.completed_visible_from_proxy.le(T0)]
            last12=eligible.sort_values('actual_end_uti').tail(12)
            require(last12.actual_end_uti.is_unique,'Ambiguous end order needs source-origin resolution')
            require(last12.ref_episode_id.tolist()==previous+recent,'Not the latest exact twelve eligible Episodes')
            v=midx.loc[recent].path_efficiency.to_numpy(float); w=midx.loc[previous].path_efficiency.to_numpy(float)
            med=float(np.median(v)); prev=float(np.median(w))
            calculated=[med,prev,med-prev,float(np.median(abs(v-med))),
                        max(abs(med-float(np.median(np.delete(v,j)))) for j in range(6))]
            nr=nh[nh.symbol.eq(n.symbol)].iloc[0]
            cols=['current_level_median','previous_level_median','recent_change','recent_dispersion_MAD','LOO_max_shift']
            err=max(abs(float(nr[f])-value) for f,value in zip(cols,calculated))
            require(err<TOL,'N historical efficiency summary mismatch')
            nchecks.append(dict(symbol=n.symbol,max_error=err,values_checked=len(cols)))
            nwindows.append(dict(symbol=n.symbol,recent=recent,previous=previous,
                recent_efficiency=v.tolist(),previous_efficiency=w.tolist(),
                recent_start=eidx.loc[recent].actual_start_ts.min(),
                recent_end=eidx.loc[recent].actual_end_ts.max()))
        pr=pair[pair.ref_reference_candidate.eq(CASE)]
        rr=relations[relations.ref_reference_candidate.eq(CASE)]
        mm=members[members.ref_reference_candidate.eq(CASE)]
        require(len(pr)==1 and len(rr)==8 and len(mm)==2,'Unexpected diagnostic cardinality')
        for m in mm.to_dict('records'):
            v=next(x for x in original if x['asof']==T0 and x['symbol']==m['symbol'])
            for q,f in {'P':'raw_progress','E':'path_efficiency','counter':'raw_counter_move','extremes':'extreme_update_count'}.items():
                require(abs(float(v[q])-float(m[f]))<TOL,'C1 member/raw path mismatch')
        gap=abs(float(nh[nh.symbol.eq('hc')].current_level_median.iloc[0])-float(nh[nh.symbol.eq('rb')].current_level_median.iloc[0]))
        nr=rr[rr.relation_kind.eq('NodeBehaviorComparison')].iloc[0]
        require(abs(float(nr.raw_observation)-gap)<TOL,'C1 exported N median gap mismatch')
        # Read the distinct Case-01 carrier only to identify its different status, not to redo Case-01.
        old=load(SINGLE+'C1/02_case_eight_relations.csv')
        old=old[old.relation_kind.eq('NodeBehaviorComparison')]
        require((old.reference_result=='RawNWindowAvailableButNotJoined').all(),'Unexpected Case-01 single-scale carrier')
        u3_scope={}
        for name in ['U3/01_single_scale_shadow_bridge.csv','U3/02_movement_r02_objective_facts.csv','U3/03_r03_quality_withholding.csv']:
            f=load(SINGLE+name)
            u3_scope[name]=dict(case_refs=sorted(f.case_ref.unique().tolist()),case02_rows=int(f.case_ref.eq(CASE).sum()))
        # Check exact mid/Zig origins of relevant anchors, canonical ends and N current starts.
        required_ids=set(IDS.values())|set(selected.end_turn_id)
        required_ids|=set(eidx.loc[[x['episode_id'] for x in current]].start_turn_id)
        ss=turns[turns.ref_turn_id.isin(required_ids)].sort_values(['symbol','source_event_ts','actual_uti'])
        source_checks=[]
        for s in IDS:
            raw=pd.read_csv(b.open(pref+s+'_mid_scaleturn_value1_value2.csv'))
            zig=pd.read_csv(b.open(pref+s+'_mid_input_zig_small_confirmed.csv'))
            for t in ss[ss.symbol.eq(s)].to_dict('records'):
                u=raw.iloc[int(t['source_csv_row'])-1]; z=zig.iloc[int(t['zig_confirmed_csv_row'])-1]
                require(u['round']==t['source_channel'] and u.occurrence_ts==t['source_event_ts'] and
                    float(u.actual_uti)==t['actual_uti'] and float(u.actual_value)==t['actual_price'] and
                    float(u.confirm_uti)==t['confirm_uti'] and float(u.confirm_value)==t['confirm_price'],'Exact mid origin mismatch')
                require(float(z.lastPosUTI)==t['actual_uti'] and float(z.lastPrice)==t['actual_price'] and
                    z.confirm_event_ts==t['zig_confirm_event_ts'] and float(z.lastDirection)==t['zig_last_direction'],
                    'Exact Zig origin mismatch')
                source_checks.append(dict(symbol=s,turn_id=t['ref_turn_id'],turn_csv_line=t['_csv_line'],
                    mid_physical_line=int(t['source_csv_row'])+1,zig_physical_line=int(t['zig_confirmed_csv_row'])+1,
                    actual=t['actual_ts'],confirm_point=t['confirm_point_ts'],knowledge=t['source_event_ts'],
                    source_channel=t['source_channel'],actual_price=t['actual_price'],matched=True))
        sep=load(BASE+'S_C2_status/S_outside_domain_only_NOT_ASSESSMENT.csv')
        sep=sep[sep.ref_reference_candidate.eq(CASE)]
        gates=load(BASE+'S_C2_status/C2_gate_only_NOT_CLUSTER.csv')
        gates=gates[gates.ref_reference_candidate.eq(CASE)]
        price_rows=[]
        for s in IDS:
            k=bars[s].copy(); k['_csv_line']=np.arange(len(k))+2
            sub=k[k.bar_ts.between('2021-05-10 11:00:00',FOLLOW[-1])]
            price_rows.extend(rec(sub.assign(symbol=s)))
        result=dict(invocation_id=INVOCATION,case_ref=CASE,method=METHOD,input_bindings=HASHES,
            management_adoption='R0004; no Case-01 re-adjudication',times=times,
            time_rule='All common bars T0..latest original completion visibility, then inherited 05-14/05-18 10:00',
            case_identity=rec(cand),anchor_turns=rec(anchors),selected_episodes=rec(selected),
            source_checks=source_checks,c1_pair=rec(pr),c1_relations=rec(rr),c1_members=rec(mm),
            baseline_S=rec(sep),baseline_C2=rec(gates),u3_scope=u3_scope,
            case01_unjoined=dict(carrier=SINGLE+'C1/02_case_eight_relations.csv',count=len(old)),
            case02_n_gap=gap,n_efficiency_t0=rec(nh),n_windows_t0=nwindows,n_summary_checks=nchecks,
            original_episode_cuts=original,current_node_cuts=current,current_path_checks=checks,
            common_event_windows=event,knowledge_forward_windows=forward,
            canonical_completed=canonical,maturity_matched_prefixes=maturity,
            i_pre_common=window('i','2021-05-10 11:00:00',COMMON_START),
            time_radius_diagnostic=[dict(bound_bars=h,hc_rb_pass=True,i_with_each_pass=(5<=h),
                qualification='ONLY_TIME_CONDITION_NOT_FORMATION') for h in [0,4,5,8]],
            price_rows=price_rows,
            limitations=['Reference diagnostics only; no new G3/G4/G5 signature',
                'Original recovery counts not consumed or repaired',
                'No Case-02 formal Formation/S/C2/H1/R02/R03 output produced',
                'No native Calendar-duration or formal NormalizationProfile',
                'Price percentages are not risk-adjusted returns or PnL',
                'N history checked against exported C0 metrics, not all raw historical paths',
                'Producer implementation not inspected; numeric export correspondence only',
                'No third Case, Worker execution, I5 execution, independent review or market-wide law'])
        write_json(output_dir/'EVIDENCE.json',result)
        for name,data in [('original_episode_cuts',original),('current_node_cuts',current),
                          ('common_event_windows',event),('knowledge_forward_windows',forward),
                          ('canonical_completed',canonical),('maturity_matched_prefixes',maturity),
                          ('source_checks',source_checks),('n_efficiency_t0',rec(nh))]:
            pd.DataFrame(data).to_csv(output_dir/(name+'.csv'),index=False)
        obs=[]
        for domain,rows in [('ORIGINAL_EPISODE',original),('CURRENT_N',current),('COMMON_EVENT',event),('KNOWLEDGE_FORWARD',forward),('CANONICAL',canonical),('EQUAL_AGE',maturity)]:
            for v in rows:
                obs.append({**{k:v.get(k) for k in ['asof','symbol','start','end','h','direction','P','L','E','counter','retained','progress_pct','counter_pct','episode_id','first_csv_line','last_csv_line']},'domain':domain})
        pd.DataFrame(obs).to_csv(output_dir/'OBSERVATIONS.csv',index=False,float_format='%.12g')
        summary=dict(case_ref=CASE,method=METHOD,asof_count=len(times),
            original_episode_rows=len(original),current_node_rows=len(current),
            current_path_max_error=max(x['max_error'] for x in checks),
            canonical_paths_verified=len(canonical),c1_member_paths_verified=len(mm),
            n_efficiency_summary_rows=len(nchecks),n_summary_values_checked=sum(x['values_checked'] for x in nchecks),
            n_summary_max_error=max(x['max_error'] for x in nchecks),
            source_turns_verified=len(source_checks),all_selected_paths_blank_ohlc=0,
            case02_c1_n_gap=gap,case02_u3_r02_rows=u3_scope['U3/02_movement_r02_objective_facts.csv']['case02_rows'],
            evidence_sha256=sha((output_dir/'EVIDENCE.json').read_bytes()))
        write_json(output_dir/'CHECK_SUMMARY.json',summary)
        print(json.dumps(summary,ensure_ascii=False,indent=2))

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--input-dir',type=Path,required=True)
    p.add_argument('--output-dir',type=Path,required=True)
    args=p.parse_args()
    main(args.input_dir,args.output_dir)
