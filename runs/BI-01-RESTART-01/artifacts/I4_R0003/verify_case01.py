#!/usr/bin/env python3
"""BI-01 R0003: bounded Case-01 evidence verification; NOT a U2/U3 runner.
Reads immutable supplied ZIPs, preserves all raw rows, and writes diagnostic
evidence. It does not publish a cluster, H1, Quality, trading signal or Gate.
Usage: python verify_case01.py --input-dir /path/to/zips --output-dir ./evidence
Requires Python 3.10+, numpy and pandas.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import zipfile
from pathlib import Path
import numpy as np
import pandas as pd

A_NAME = "steel_U2_U3_执行结果_20261010.zip"
B_NAME = "rb_hc_i_mid贴近转折_zig_small_K线_20210101_20240229.zip"
A_HASH = "7bebbee3fd7d425eb85116f33c5d0e01ae2163e6849818515fe3824a82b9a46c"
B_HASH = "4fd1af4e7b34af6fc099e6289ffdd5d83125412fc16d2a9902af4fd9741b3987"
BASE = "baseline_U2_C0_N_C1/"
SINGLE = "single_scale_U2_C1_S_C2_U3/"
CASE = "refonly-ad8824a52552d7bffa91"
METHOD = "BI01-I4-DIAGNOSTIC-R0003-v1"
INVOCATION = "BI01-RESTART-01-R0003-9dda7755b8d94803ba5b03f53721d18c"
TIMES = [f"2021-05-{d} 10:00:00" for d in ["06","07","11","14","18"]]
SYMS = ["hc","rb","i"]
TOL = 1e-10  # numerical comparison tolerance, NOT a market price epsilon

def require(condition: bool, reason: str) -> None:
    if not condition:
        raise ValueError(reason)

def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def records(df: pd.DataFrame) -> list[dict]:
    # pandas JSON turns NaN into null; no fake zero for unavailable ratios.
    return json.loads(df.to_json(orient="records", double_precision=15))

def stats(close) -> dict:
    p = np.asarray(close, dtype=float)
    require(len(p)>0 and np.isfinite(p).all(), "Unavailable selected close path")
    x = p-p[0]  # All three anchor Episodes are Up; no general direction inference.
    best = np.maximum.accumulate(x)
    length = float(np.abs(np.diff(p)).sum())
    return dict(raw_progress=float(x[-1]), raw_amplitude=float(abs(x[-1])),
        path_length=length,
        path_efficiency=float(abs(x[-1])/length) if length else None,
        max_counter_move=float((best-x).max()), achieved_peak=float(best[-1]),
        retained_fraction=float(x[-1]/best[-1]) if best[-1]>0 else None,
        return_to_origin_progress=float(x[-1]),
        extreme_count=int((x[1:]>best[:-1]).sum()))

def runs_and_recovery(path: pd.DataFrame) -> dict:
    p = path.close.to_numpy(float)
    sign = np.sign(np.diff(p)).astype(int)
    runs = sign[np.r_[True, sign[1:]!=sign[:-1]]] if len(sign) else np.array([],int)
    nz = sign[sign!=0]
    events = []
    peak = p[0]; peak_ts = str(path.bar_ts.iloc[0]); below = False; start = None
    for row in path.iloc[1:].itertuples():
        value = float(row.close)
        if value < peak:
            if not below: start = row.bar_ts; below = True
        else:
            if below:
                events.append(dict(prior_peak_ts=peak_ts, prior_peak=float(peak),
                    excursion_start=start, recovered_at=row.bar_ts,
                    recovered_price=value, equality_touch=bool(value==peak)))
                below = False
            if value > peak: peak = value; peak_ts = row.bar_ts
    # Separate diagnostic alternative. Matching it does NOT prove producer code.
    peak = p[0]; below = False; strict = 0
    for value in p[1:]:
        if value < peak: below = True
        elif value > peak:
            if below: strict += 1; below = False
            peak = value
    return dict(advance_runs=int((runs==1).sum()),counter_runs=int((runs==-1).sum()),
        flat_runs=int((runs==0).sum()),sign_change_count=int((nz[1:]!=nz[:-1]).sum()),
        recovery_touch_count=len(events), recovery_strict_new_high_count=strict,
        recovery_touch_events=events)

def main(input_dir: Path, output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    archive_meta=[]
    for name,expected in [(A_NAME,A_HASH),(B_NAME,B_HASH)]:
        data=(input_dir/name).read_bytes()
        require(sha(data)==expected, f"Wrong DataBinding bytes: {name}")
        archive_meta.append(dict(filename=name,sha256=expected,bytes=len(data)))
    with zipfile.ZipFile(input_dir/A_NAME) as a, zipfile.ZipFile(input_dir/B_NAME) as b:
        require(a.testzip() is None and b.testzip() is None,"ZIP CRC failure")
        pref = next(n for n in b.namelist() if n.endswith("manifest.json"))[:-len("manifest.json")]
        manifest=json.loads(b.read(pref+"manifest.json"))
        members=[]
        for sym in manifest["symbols"]:
            for meta in sym["files"].values():
                data=b.read(pref+meta["file"])
                require(sha(data)==meta["sha256"] and len(data)==meta["bytes"],
                        f"Manifest member mismatch: {meta['file']}")
                members.append(dict(member=pref+meta["file"],sha256=sha(data),bytes=len(data)))
        rd=lambda name: pd.read_csv(a.open(BASE+name))
        one=lambda name: pd.read_csv(a.open(SINGLE+name))
        r=one("U3/02_movement_r02_objective_facts.csv")
        require(set(r.case_ref)=={CASE} and len(r)==15,"Unexpected Case set")
        require(set(r["asof"])==set(TIMES) and set(r.symbol)==set(SYMS),"Wrong cuts")
        turns=rd("C0/02_turn_occurrences.csv")
        episodes=rd("C0/04_segment_episodes.csv")
        metrics=rd("C0/05_completed_episode_metrics.csv")
        cuts=rd("C0/06_episode_and_working_cuts_30m.csv")
        nodes=rd("N/01_node_behavior_cuts.csv")
        nodes=nodes[nodes.asof_event_ts_proxy.isin(TIMES)].copy()
        nm=pd.concat([x[x.asof_event_ts_proxy.isin(TIMES)]
            for x in pd.read_csv(a.open(BASE+"N/02_node_behavior_metrics.csv"),chunksize=50000)],
            ignore_index=True)
        bars={s:pd.read_csv(b.open(pref+s+"_kline_30m.csv")) for s in SYMS}
        for s,k in bars.items():
            require(k.bar_ts.is_monotonic_increasing and k.bar_ts.is_unique,
                    f"Bad KLine index: {s}")
        anchors=turns[turns.ref_turn_id.isin(r.anchor_turn_id)].copy()
        eps=episodes[episodes.ref_episode_id.isin(r.ref_episode_id)].copy()
        require(len(anchors)==3 and len(eps)==3,"Anchor/Episode identity conflict")
        source_checks=[]
        selected_turns=turns[turns.ref_turn_id.isin(
            list(anchors.ref_turn_id)+list(eps.end_turn_id))]
        for t in selected_turns.itertuples():
            raw=pd.read_csv(b.open(pref+t.symbol+"_mid_scaleturn_value1_value2.csv"))
            src=raw.iloc[int(t.source_csv_row)-1]  # 1-based data row, excludes header
            require(float(src.actual_uti)==t.actual_uti and
                    float(src.actual_value)==t.actual_price and
                    float(src.confirm_uti)==t.confirm_uti and
                    float(src.confirm_value)==t.confirm_price and
                    str(src.iloc[0])==t.source_event_ts,
                    f"Turn source mismatch: {t.ref_turn_id}")
            zig=pd.read_csv(b.open(pref+t.symbol+"_mid_input_zig_small_confirmed.csv"))
            z=zig.iloc[int(t.zig_confirmed_csv_row)-1]
            require(float(z.lastPosUTI)==t.actual_uti and
                    float(z.lastPrice)==t.actual_price and
                    str(z.iloc[0])==t.zig_confirm_event_ts,
                    f"Zig exact-row mismatch: {t.ref_turn_id}")
            source_checks.append(dict(symbol=t.symbol,turn_id=t.ref_turn_id,
                source_physical_csv_line=int(t.source_csv_row)+1,
                zig_physical_csv_line=int(t.zig_confirmed_csv_row)+1,
                actual_ts=t.actual_ts,confirm_point_ts=t.confirm_point_ts,
                source_event_ts=t.source_event_ts,actual_price=t.actual_price,
                source_channel=t.source_channel,all_selected_checks_match=True))
        path_checks=[]; duplicate_checks=[]; recovery_checks=[]
        for index,row in r.iterrows():
            s=row.symbol; at=row["asof"]; ep=eps[eps.ref_episode_id==row.ref_episode_id].iloc[0]
            require(ep.source_expected_direction=="Up","Unexpected direction")
            completed=at>=ep.completed_visible_from_proxy
            require((row.episode_stage_at_cut=="Completed")==completed,"Lifecycle mismatch")
            k=bars[s]; start=int(row.anchor_bar_index)
            match=k.index[k.closeUti==int(row.observed_end_uti)]
            require(len(match)==1,"Ambiguous observed endpoint")
            end=int(match[0]); p=k.iloc[start:end+1]
            missing=int(p[["open","high","low","close"]].isna().any(axis=1).sum())
            require(missing==0,"Selected path has original blank OHLC; do not fill or drop")
            require(end-start==row.observed_bar_elapsed and
                    p.close.iloc[0]==row.start_price and
                    p.close.iloc[-1]==row.observed_end_price,"Endpoint mismatch")
            require(str(p.bar_ts.iloc[-1])==row.observed_end_ts,"Endpoint time mismatch")
            if completed:
                require(int(row.observed_end_uti)==int(ep.actual_end_uti),"Completed path extended")
            else:
                require(row.observed_end_ts==at,"Working cutoff mismatch")
            actual=stats(p.close)
            error=max(abs(float(actual[key])-float(row[key])) for key in actual)
            require(error<TOL,"R02 key path field mismatch")
            path_checks.append(dict(r02_physical_csv_line=int(index)+2,symbol=s,asof=at,
                path_first_physical_csv_line=start+2,path_last_physical_csv_line=end+2,
                price_points=len(p),intervals=end-start,blank_ohlc=missing,max_error=error,
                stage=row.episode_stage_at_cut))
            sup=runs_and_recovery(p)
            for key in ["advance_runs","counter_runs","flat_runs","sign_change_count"]:
                require(int(row[key])==sup[key],f"Run-count mismatch: {key}")
            recovery_checks.append(dict(symbol=s,asof=at,reported=int(row.completed_recovery_events),
                **sup,touch_matches_report=int(row.completed_recovery_events)==sup["recovery_touch_count"],
                producer_code_verified=False))
            if not completed:
                n=nodes[(nodes.symbol==s)&(nodes.asof_event_ts_proxy==at)].iloc[0]
                require(n.working_episode_ref==row.ref_episode_id,"Wrong N overlay")
                pairs={"raw_progress":"working_prefix_progress",
                    "path_efficiency":"working_prefix_efficiency",
                    "max_counter_move":"working_prefix_counter","extreme_count":"working_prefix_extreme_updates"}
                origin=n; file="N/01_node_behavior_cuts.csv"
            else:
                origin=metrics[metrics.ref_episode_id==row.ref_episode_id].iloc[0]
                pairs={"raw_progress":"raw_progress","raw_amplitude":"raw_amplitude",
                    "path_length":"path_length","path_efficiency":"path_efficiency",
                    "max_counter_move":"raw_counter_move","extreme_count":"extreme_update_count"}
                file="C0/05_completed_episode_metrics.csv"
            err=max(abs(float(row[x])-float(origin[y])) for x,y in pairs.items())
            require(err<TOL,"Baseline overlap mismatch")
            duplicate_checks.append(dict(symbol=s,asof=at,episode_id=row.ref_episode_id,
                baseline=file,fields=list(pairs),max_error=err))
        n_checks=[]
        for n in nodes.itertuples():
            recent=n.recent_exact_6_ids.split("|"); previous=n.previous_exact_6_ids.split("|")
            require(len(set(recent))==6 and len(set(previous))==6 and
                    not set(recent)&set(previous),"N exact windows overlap/size mismatch")
            epvec=episodes.set_index("ref_episode_id").loc[recent+previous]
            require((epvec.completed_visible_from_proxy<=n.asof_event_ts_proxy).all(),
                    "Future Episode in exported N window")
            subset=nm[(nm.symbol==n.symbol)&(nm.asof_event_ts_proxy==n.asof_event_ts_proxy)]
            for m in subset.itertuples():
                if m.metric not in metrics.columns or m.metric_knownness!="AvailableReference": continue
                v=metrics.set_index("ref_episode_id").loc[recent,m.metric].to_numpy(float)
                w=metrics.set_index("ref_episode_id").loc[previous,m.metric].to_numpy(float)
                level=np.median(v)
                vals=[level,np.median(w),level-np.median(w),np.median(abs(v-level)),
                      max(abs(level-np.median(np.delete(v,j))) for j in range(6))]
                cols=["current_level_median","previous_level_median","recent_change","recent_dispersion_MAD","LOO_max_shift"]
                err=max(abs(float(getattr(m,c))-float(z)) for c,z in zip(cols,vals))
                require(err<TOL,"N summary mismatch")
                n_checks.append(dict(symbol=n.symbol,asof=n.asof_event_ts_proxy,metric=m.metric,max_error=err))
        common=[]
        # Rules selected from task cuts / canonical boundaries, not metric rankings.
        for horizon in [1,2,14,33,38,74,98]:
            for s in SYMS:
                an=anchors[anchors.symbol==s].iloc[0]; ep=eps[eps.symbol==s].iloc[0]
                k=bars[s]; start=int(k.index[k.closeUti==int(an.actual_uti)][0])
                p=k.iloc[start:start+horizon+1]; vals=stats(p.close)
                require(p[["open","high","low","close"]].notna().all().all(),"Blank in common window")
                crosses=int(p.closeUti.iloc[-1])>int(ep.actual_end_uti)
                common.append(dict(symbol=s,horizon=horizon,end_ts=str(p.bar_ts.iloc[-1]),
                    end_price=float(p.close.iloc[-1]),crosses_canonical_end=bool(crosses),
                    domain="ANCHOR_EVENT_WINDOW" if crosses else "CANONICAL_PREFIX_RETROSPECTIVE_BOUNDARY",
                    anchor_known_from=an.source_event_ts,method=METHOD,
                    progress_pct=100*vals["raw_progress"]/float(p.close.iloc[0]),
                    counter_pct=100*vals["max_counter_move"]/float(p.close.iloc[0]),
                    efficiency=vals["path_efficiency"],retained=vals["retained_fraction"],
                    path_length=vals["path_length"],max_counter=vals["max_counter_move"]))
        for h in [1,2,14,33,38,74,98]:
            require(len({x["end_ts"] for x in common if x["horizon"]==h})==1,"Noncommon horizon")
        knowledge=[]
        for at in TIMES:
            for s in SYMS:
                k=bars[s]; p=k[(k.bar_ts>=TIMES[0])&(k.bar_ts<=at)]
                require(p[["open","high","low","close"]].notna().all().all(),"Blank in knowledge window")
                vals=stats(p.close)
                knowledge.append(dict(symbol=s,asof=at,horizon=len(p)-1,
                    domain="KNOWLEDGE_ORIGIN_EVENT_WINDOW_NOT_EPISODE_OR_PNL",
                    progress_pct=100*vals["raw_progress"]/float(p.close.iloc[0]),
                    efficiency=vals["path_efficiency"],
                    counter_pct=100*vals["max_counter_move"]/float(p.close.iloc[0]),
                    retained=vals["retained_fraction"]))
        assessed=one("C1/03_case_formation_and_three_assessments.csv")
        separation=one("S/01_case_external_separation_v0.csv")
        sensitivity=[]
        for d in [1,2,4]:
            for row in assessed.itertuples():
                at=row.asof
                se=separation[separation["asof"]==at].iloc[0]
                rr=r[r["asof"]==at]
                epoch=int(row.epoch_processed_bars)>=6*d
                working=all(x.episode_stage_at_cut=="Completed" or x.observed_bar_elapsed>=2*d
                            for x in rr.itertuples())
                persistence=int(se.evidence_count_reference)>=3 and int(se.elapsed_reference_bar_positions)>=4*d
                sensitivity.append(dict(delta_ref_bars=d,asof=at,zero_actual_lag_condition=True,
                    epoch_age=int(row.epoch_processed_bars),epoch_required=6*d,
                    epoch_condition=epoch,working_extent_condition=working,
                    S_elapsed_required=4*d,S_persistence_conditions=persistence,
                    necessary_conditions_all=bool(epoch and working and persistence),
                    scope="CONDITIONS_ONLY_NOT_A_C1_REEXECUTION"))
        boundary_times={"hc":["2021-05-11 10:00:00","2021-05-11 10:30:00"],
                        "rb":["2021-05-10 23:00:00","2021-05-11 09:30:00"],
                        "i":["2021-05-06 10:30:00","2021-05-06 11:00:00"]}
        boundaries=pd.concat([cuts[(cuts.symbol==s)&cuts.asof_event_ts_proxy.isin(ts)]
                              for s,ts in boundary_times.items()])
        current=nodes.merge(episodes[["ref_episode_id","source_expected_direction","actual_start_ts"]],
                            left_on="working_episode_ref",right_on="ref_episode_id",validate="many_to_one")
        data=dict(invocation_id=INVOCATION,case_ref=CASE,diagnostic_method=METHOD,
            qualification="EXECUTION_PRO_SELF_CHECK_REFERENCE_SHADOW_ONLY_NO_GATE_SIGNATURE",
            archives=archive_meta,upstream_manifest_members=members,
            raw_blank_ohlc_total={s:int(k[["open","high","low","close"]].isna().any(axis=1).sum())
                                  for s,k in bars.items()},
            anchors=records(anchors),canonical_episodes=records(eps),source_checks=source_checks,
            r02_reported=records(r),r02_key_path_checks=path_checks,baseline_overlap_checks=duplicate_checks,
            n_summary_checks=n_checks,n_metrics=records(nm),n_current=records(current),
            lifecycle_boundaries=records(boundaries),common_horizons=common,
            knowledge_origin_windows=knowledge,delta_condition_sensitivity=sensitivity,
            recovery_method_comparison=recovery_checks,
            c1_assessments=records(assessed),c1_relations=records(one("C1/02_case_eight_relations.csv")),
            compatibility_matrix=records(one("C1/01_compatibility_method_matrix.csv")),
            separation=records(separation),c2_gates=records(one("C2/01_case_opportunity_cluster_gates_v0.csv")),
            shadow_bridge=records(one("U3/01_single_scale_shadow_bridge.csv")),
            r03_withholding=records(one("U3/03_r03_quality_withholding.csv")),
            limitations=["No original Runner or producer code verified",
                "No native Calendar duration or formal NormalizationProfile",
                "Recovery touch mismatch isolated: HC 2021-05-07 10:00 reported 3 vs touch 4",
                "N summary checks use exported C0 metrics, not all historical raw paths",
                "Event windows never extend a completed Episode or constitute formal Outcome",
                "No formal cluster/H1/Quality/capital/independent audit/management Gate"])
        # Write complete machine evidence; preserve actual IDs and exact methods in original records.
        (output_dir/"EVIDENCE.json").write_text(json.dumps(data,ensure_ascii=False,indent=2,allow_nan=False)+"\n",encoding="utf-8")
        for key in ["r02_reported","r02_key_path_checks","common_horizons","knowledge_origin_windows",
                    "delta_condition_sensitivity","n_summary_checks","baseline_overlap_checks"]:
            pd.DataFrame(data[key]).to_csv(output_dir/(key+".csv"),index=False)
        summary=dict(path_rows_verified=len(path_checks),n_metric_rows_checked=len(n_checks),
            baseline_rows_checked=len(duplicate_checks),
            recovery_touch_mismatches=sum(not x["touch_matches_report"] for x in recovery_checks),
            evidence_sha256=sha((output_dir/"EVIDENCE.json").read_bytes()))
        (output_dir/"CHECK_SUMMARY.json").write_text(json.dumps(summary,indent=2)+"\n",encoding="utf-8")
        print(json.dumps(summary,ensure_ascii=False))

if __name__=="__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input-dir",type=Path,required=True)
    parser.add_argument("--output-dir",type=Path,required=True)
    args=parser.parse_args()
    main(args.input_dir,args.output_dir)
