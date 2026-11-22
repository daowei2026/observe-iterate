"""G：仅统计独立读回通过的正式品种；请求范围不缩减，缺失品种使整体 Gate 阻断。"""
import json
from pathlib import Path
from datetime import datetime, timezone
import numpy as np
import pandas as pd

OUT = Path(__file__).resolve().parent
DEST = OUT / "profile"
DEST.mkdir(exist_ok=False)
readback = json.loads((OUT / "readback-summary.json").read_text())
preflight = json.loads((OUT / "preflight.json").read_text())
specification = json.loads((OUT / "statistics-specification.json").read_text())
available = [symbol for symbol, entry in readback["symbols"].items() if entry["status"] == "VERIFIED"]
missing = [symbol for symbol in ("rb", "m") if symbol not in available]
assert available, "没有可靠的正式结果，不能形成数值剖面"
binding = dict(feature_name="mquant.tis.hf.prel0.wall_assembler.WallAssembler",
               code_version="daowei2026/tis@6618d4d147d6ebbe634e61facddf2c9a0b996982",
               parameter_instance_ref=str(OUT / "preflight.json"), parameter_version="wall-default-at-6618d4d",
               run_id="OI-WALL-STAT-20261122-01",
               data_scope=dict(symbols=["rb", "m"], start_time="2021-01-01", end_time="2021-12-31",
                               calendar="night_end_at_2300", sessions="正式日历中的输入；自然钟分箱单独声明"),
               artifact_refs=[], run_result_tables=[], known_data_limits=[],
               verified_symbols=available, missing_symbols=missing,
               status="PARTIAL" if missing else "VALID")
for symbol in available:
    record = json.loads((OUT / "results" / symbol / "result.json").read_text())
    assert record["ppdict"] == preflight["symbols"][symbol]["ppdict"]
    assert readback["symbols"][symbol]["code_fingerprint"] == preflight["symbols"][symbol]["code_fingerprint"]
    for key, value in record["tables"].items():
        binding["run_result_tables"].append(dict(symbol=symbol, key=key, **value))
    binding["artifact_refs"].append(dict(symbol=symbol, full_dir=record["full_dir"],
                                         fields_sha256=record["native_fields_sha256"],
                                         receipt_sha256=record["native_receipt_sha256"]))
if missing:
    binding["known_data_limits"].append("m 的锁定正式入口失败；未把 m 缺失统计成零，也未改变 rb/m 全年请求范围。")
readiness = dict(binding_match=dict(code_version="MATCH", parameter_version="MATCH",
                                   data_scope="PARTIAL" if missing else "CONFIRMED"),
                 core_object_keys=["source_result_namespace", "symbol", "wall_id"],
                 core_time_keys=["native timestamp", "uti", "occurrence_ordinal"],
                 available_items=["已验证品种的 sparse/packed lifecycle occurrences、逐拍 trace 与 receipt"],
                 partial_items=["整体 rb/m 范围：m 尚无有效结果"] if missing else [],
                 not_exposed_items=specification["not_exposed_items"],
                 data_quality_findings=binding["known_data_limits"],
                 readiness_status="PARTIAL" if missing else "READY", verified_symbols=available,
                 statistics_scope_note="只对同版本且独立读回通过的分层形成剖面；整体请求范围和缺失项保留，未将部分结果作为全量完成。")
profile = dict(profile_id="GBP-WALL-STAT-20261122-D002", feature_ref=binding["feature_name"], run_binding=binding,
               statistics_definitions=specification["statistics_definitions"],
               candidate_profile=[dict(status="NOT_EXPOSED", items=specification["not_exposed_items"])],
               object_profile=[], event_profile=[], state_occupancy_profile=[], transition_profile=[],
               lifecycle_profile=[], branch_reachability_profile=[], density_profile=[], reason_profile=[],
               reference_integrity_profile=[], same_tick_order_profile=[], cross_symbol_profile=[],
               cross_period_profile=[], cross_session_profile=[], limits=list(binding["known_data_limits"]),
               known_finding_reviews=[])
findings, questions, cases, adapters = [], [], [], []
profile["limits"].append("F1/F6 转化及逐拍 far/support 不在 WALL 最终结果；未用内部变量或旧 Run 插桩冒充本轮统计。")
profile["limits"].append("钟时分箱是原生 timestamp 的 [06:00,18:00) 与其余时刻，不冒充官方 SessionID。")
profile["coverage_status"] = "PARTIAL" if missing else "FULL_REQUESTED_SCOPE"


def distribution(values):
    series = pd.Series(values).dropna()
    if not len(series):
        return dict(n=0, min=None, p25=None, p50=None, p90=None, p95=None, p99=None, max=None)
    result = {name: float(series.quantile(q)) for name, q in
              [("min", 0), ("p25", .25), ("p50", .5), ("p90", .9), ("p95", .95), ("p99", .99), ("max", 1)]}
    return dict(n=len(series), **result)


def add_profile(section, statistic_id, stratum, value, sample_size, denominator, source, notes=""):
    profile[section].append(dict(statistic_id=statistic_id, stratum_id=stratum, value_or_distribution=value,
                                 sample_size=int(sample_size), denominator_value=denominator,
                                 source_location=source, notes=notes))


def add_finding(kind, symbol, hits, denominator, statement, object_count, unit="occurrence"):
    if not len(hits):
        return
    hits = hits.copy()
    path = DEST / (symbol + "-" + kind + ".parquet")
    hits.to_parquet(path, compression="zstd", index=True)
    finding_id = "GF-" + symbol.upper() + "-" + kind.upper()
    affected = int(hits["wall_id"].nunique()) if "wall_id" in hits else len(hits)
    representatives = []
    grouping = hits.groupby("side_code", sort=True) if "side_code" in hits else [(None, hits)]
    for side, group in grouping:
        row = group.iloc[0]
        location = dict(symbol=symbol, time=str(group.index[0]), wall_id=int(row["wall_id"]) if "wall_id" in row else None,
                        side_code=int(side) if side is not None else None,
                        uti=int(row["uti"]) if "uti" in row and pd.notna(row["uti"]) else None)
        representatives.append(location)
        cases.append(dict(case_candidate_id=finding_id+"-"+str(side), source_finding_or_question_id=finding_id,
                          symbol=symbol, start_time=location["time"], end_time=location["time"],
                          object_ids=[location["wall_id"]], related_events=[], selection_reason=statement,
                          required_fields=["wall_id", "uti", "event_type_code", "state_trace"]))
    invariant = "当前理解包 BO-C1、ST-C0..3、OC-C1..4、ID-D1/D2 及 PR-C2..8 的明确身份/顺序/输出合同"
    adapter_id = "DA-" + finding_id
    findings.append(dict(finding_id=finding_id, finding_type="STRUCTURAL_FINDING_CANDIDATE",
                         feature_ref=binding["feature_name"], run_binding="FeatureRunResultBinding.json",
                         reasonableness_unit_ref=kind, business_object_ref="BO-C1", observation=statement,
                         structural_invariant_ref=invariant, evidence_scope=symbol+" 2021全年已验证结果",
                         repeat_count=len(hits), affected_count=affected,
                         affected_ratio=affected/object_count if object_count else None,
                         count_unit=unit, applicable_denominator=int(denominator),
                         representative_locations=representatives,
                         alternative_non_error_explanations=["复核发生时间、同刻 ordinal 与 relocation 旧身份豁免；未在 G 中写根因。"],
                         current_confidence="可复现的结构证据，待原诊断Skill确认", next_route="BUSINESS_DISCREPANCY_DIAGNOSIS",
                         diagnosis_input_adapter_ref=adapter_id))
    adapters.append(dict(adapter_id=adapter_id, finding_id=finding_id,
                         frozen_expectation=dict(expectation_id="INV-"+kind, version="6618d4d-FUP-D001",
                                                 statement=statement, origin=invariant,
                                                 applicable_conditions="同一正式结果namespace和对象，遵守当前包同刻及身份边界",
                                                 falsifier_or_counterevidence="若两个载体实际不是同一身份/发生时间，应据来源纠正统计绑定。"),
                         evidence_comparison_package=dict(comparison_id=finding_id, scenario_id="GLOBAL_PROFILE",
                                                          data_binding="FeatureRunResultBinding.json", time_basis="native timestamp/uti/ordinal",
                                                          parameter_version="wall-default-at-6618d4d", evidence_items=[str(path)],
                                                          judgment="STRUCTURAL_FINDING_CANDIDATE"),
                         business_intent_ref="WALL_BASE_RUN_INPUT.md §7", processing_chain_ref="FUP D001 §5",
                         relevant_code_or_requirement_refs=[binding["code_version"]+":hf/prel0/wall_assembler_core.py"],
                         data_binding_and_time_basis="FeatureRunResultBinding.json；源结果namespace、symbol、wall_id与原生uti/ordinal"))


for symbol in available:
    target = OUT / "results" / symbol
    events = pd.read_parquet(target / "wall_events.parquet")
    trace = pd.read_parquet(target / "tables/wall_assembler_state_trace.parquet")
    assert trace.index.is_unique and trace.index.is_monotonic_increasing
    events["_event_time"] = events.index
    object_count = int(events.wall_id.nunique())
    source = str(target / "wall_events.parquet")
    first_start = events.loc[events.event_type_code.eq(4)].drop_duplicates("wall_id").set_index("wall_id")
    last_end = events.loc[events.event_type_code.eq(7)].drop_duplicates("wall_id", keep="last").set_index("wall_id")
    lives = pd.DataFrame(index=pd.Index(sorted(events.wall_id.unique()), name="wall_id"))
    for name in ["uti", "_event_time", "side_code", "core_price", "band_lo", "band_hi"]:
        lives["start_"+name] = first_start[name]
        lives["end_"+name] = last_end[name]
    lives["lifetime_uti"] = lives.end_uti-lives.start_uti
    lives["lifetime_wall_clock_seconds"] = (lives.end__event_time-lives.start__event_time).dt.total_seconds()
    lives["right_censored"] = lives.start_uti.notna() & lives.end_uti.isna()
    lives.to_parquet(DEST/(symbol+"-lifecycles.parquet"), compression="zstd")
    add_profile("object_profile", "BO-01", symbol,
                dict(unique_objects=object_count, start_occurrences=int(events.event_type_code.eq(4).sum()),
                     objects_with_start=int(lives.start_uti.notna().sum()), objects_with_end=int(lives.end_uti.notna().sum()),
                     right_censored=int(lives.right_censored.sum()), events_per_object=distribution(events.groupby("wall_id").size())),
                len(events), object_count, source)
    for side in [1, 2]:
        group = events.loc[events.side_code.eq(side)]
        side_name = "bid" if side == 1 else "ask"
        stratum = symbol+"/"+side_name
        add_profile("event_profile", "EV-01", stratum,
                    {str(code): int(group.event_type_code.eq(code).sum()) for code in [4,5,6,7]}, len(group), len(group), source,
                    "按packed occurrence并集；同刻ordinal保留，不与sparse重复计数。")
        add_profile("density_profile", "EV-01", stratum, dict(events_per_million_trace_samples=len(group)/len(trace)*1e6),
                    len(group), len(trace), source)
        statuses = trace["wall_status_code_"+side_name]
        add_profile("state_occupancy_profile", "ST-01", stratum,
                    {str(code): dict(samples=int(statuses.eq(code).sum()), fraction=float(statuses.eq(code).mean())) for code in range(4)},
                    len(trace), len(trace), str(target/"tables/wall_assembler_state_trace.parquet"), "状态样本拍；Ended重复样本不是End事件。")
        statechanges = group.loc[group.event_type_code.eq(6)]
        add_profile("transition_profile", "ST-02", stratum,
                    dict(enter_dormant=int(statechanges.status_code.eq(2).sum()), recover_alive=int(statechanges.status_code.eq(1).sum())),
                    len(statechanges), len(statechanges), source)
        id_array = trace["wall_id_"+side_name].to_numpy()
        state_array = statuses.to_numpy()
        boundaries = np.flatnonzero(np.r_[True, (id_array[1:] != id_array[:-1]) | (state_array[1:] != state_array[:-1])])
        stops = np.r_[boundaries[1:], len(trace)]
        segments = pd.DataFrame(dict(wall_id=id_array[boundaries], status_code=state_array[boundaries],
                                     start_uti=trace.uti.to_numpy()[boundaries],
                                     last_sample_uti=trace.uti.to_numpy()[stops-1],
                                     sample_count=stops-boundaries, right_censored=stops==len(trace)))
        segments["uti_span_last_minus_first"] = segments.last_sample_uti-segments.start_uti
        segments.to_parquet(DEST/(symbol+"-"+side_name+"-state-segments.parquet"), compression="zstd", index=False)
        for status_code in [1,2]:
            active_segments = segments.loc[segments.status_code.eq(status_code)]
            add_profile("transition_profile", "ST-02", stratum+"/state-"+str(status_code),
                        dict(continuous_segments=len(active_segments), sample_run_length=distribution(active_segments.sample_count),
                             uti_span_last_minus_first=distribution(active_segments.uti_span_last_minus_first),
                             right_censored=int(active_segments.right_censored.sum())),
                        len(active_segments), len(active_segments), str(DEST/(symbol+"-"+side_name+"-state-segments.parquet")),
                        "连续同身份同末态段；样本长度和首末UTI差分别报告，不伪造事件中间状态的逐拍持续。")
        selected_lives = lives.loc[lives.start_side_code.eq(side)]
        complete = selected_lives.loc[selected_lives.end_uti.notna()]
        add_profile("lifecycle_profile", "LC-01", stratum,
                    dict(complete_lives=len(complete), right_censored=int(selected_lives.right_censored.sum()),
                         lifetime_uti=distribution(complete.lifetime_uti), wall_clock_seconds=distribution(complete.lifetime_wall_clock_seconds),
                         zero_uti_lives=int(complete.lifetime_uti.eq(0).sum()),
                         up_to_3_uti=int(complete.lifetime_uti.le(3).sum()), up_to_12_uti=int(complete.lifetime_uti.le(12).sum())),
                    len(selected_lives), len(complete), str(DEST/(symbol+"-lifecycles.parquet")), "UTI差、墙钟时间差和样本拍分别解释。")
        ends = group.loc[group.event_type_code.eq(7)]
        add_profile("reason_profile", "RS-01", stratum,
                    {str(reason): dict(count=int(ends.reason_code.eq(reason).sum()), fraction=float(ends.reason_code.eq(reason).mean()) if len(ends) else None) for reason in range(1,6)},
                    len(ends), len(ends), source)
        add_profile("branch_reachability_profile", "RS-01", stratum,
                    dict(breakthrough_ends=int(ends.reason_code.eq(3).sum()), default_absorb_input="NOT_WIRED"), len(ends), len(ends), source,
                    "无Absorb接线时零breakthrough不自动形成不可达缺陷。")
        for month in sorted(trace.index.month.unique()):
            ticks = int((trace.index.month == month).sum())
            ev = group.loc[group.index.month == month]
            add_profile("cross_period_profile", "EV-01", stratum+"/2021-"+str(month).zfill(2),
                        dict(event_occurrences=len(ev), starts=int(ev.event_type_code.eq(4).sum()), events_per_million_samples=len(ev)/ticks*1e6),
                        len(ev), ticks, source)
        for label, is_day in [("DAY_CLOCK_BIN", True), ("OTHER_CLOCK_BIN", False)]:
            trace_day = (trace.index.hour >= 6) & (trace.index.hour < 18)
            event_day = (group.index.hour >= 6) & (group.index.hour < 18)
            ticks = int((trace_day if is_day else ~trace_day).sum())
            ev = group.loc[event_day if is_day else ~event_day]
            add_profile("cross_session_profile", "EV-01", stratum+"/"+label,
                        dict(event_occurrences=len(ev), events_per_million_samples=len(ev)/ticks*1e6 if ticks else None), len(ev), ticks, source,
                        "自然钟分箱代理，不声明官方SessionID。")
        aligned = trace.reindex(group.index)
        match_id = group.wall_id.to_numpy() == aligned["wall_id_"+side_name].to_numpy()
        geometry_bad = np.zeros(len(group), dtype=bool)
        for short, trace_name in [("band_lo","wall_band_lo_"),("band_hi","wall_band_hi_"),("core_price","wall_core_price_")]:
            geometry_bad |= group[short].to_numpy() != aligned[trace_name+side_name].to_numpy()
        add_finding("event-trace-geometry",symbol,group.loc[match_id & geometry_bad],int(match_id.sum()),
                    "同一对象同一发生拍的正式事件几何应与该侧trace末位置一致；已豁免relocation旧End。",object_count)
        add_profile("same_tick_order_profile", "REG-D1", stratum,
                    dict(applicable_events=int(match_id.sum()), geometry_conflicts=int((match_id & geometry_bad).sum()),
                         non_final_identity_events=int((~match_id).sum())), len(group), int(match_id.sum()), source)
        add_finding("event-time-not-in-trace",symbol,group.loc[~group.index.isin(trace.index)],len(group),
                    "正式事件发生时点应能在同输入范围的trace找到；不能把不同时间轴混为同一对象拍。",object_count)
        last_current = group.loc[match_id].groupby(["wall_id","uti"],sort=False).tail(1)
        final_trace = trace.reindex(last_current.index)
        status_bad = last_current.status_code.to_numpy() != final_trace["wall_status_code_"+side_name].to_numpy()
        add_finding("event-trace-final-status",symbol,last_current.loc[status_bad],len(last_current),
                    "同对象同拍最后一条生命周期事件状态应与该侧trace末态一致；较早事件状态不要求等于末态。",object_count)
    previous_code = events.groupby("wall_id",sort=False).event_type_code.shift()
    previous_status = events.groupby("wall_id",sort=False).status_code.shift()
    add_finding("missing-start",symbol,events.loc[previous_code.isna() & ~events.event_type_code.eq(4)],object_count,
                "新source范围从空slot开始，每个对象的首条生命周期occurrence应为Start。",object_count)
    add_finding("duplicate-start",symbol,events.loc[events.event_type_code.eq(4) & previous_code.notna()],object_count,
                "同一source-local身份只能由一次Start创建。",object_count)
    after_end = previous_code.eq(7).groupby(events.wall_id).cummax()
    add_finding("after-end-update",symbol,events.loc[after_end],len(events),
                "Ended身份不能再接受业务更新或复用；后续新墙应分配新编号。",object_count)
    bad_transition = ((events.event_type_code.eq(4) & ~events.status_code.eq(1)) |
                      (events.event_type_code.eq(7) & ~events.status_code.eq(3)) |
                      (events.event_type_code.eq(5) & events.status_code.ne(previous_status)) |
                      (events.event_type_code.eq(6) & (~events.status_code.isin([1,2]) | events.status_code.eq(previous_status))))
    add_finding("illegal-transition",symbol,events.loc[bad_transition],len(events),
                "Start为Alive，End为Ended，BandUpdate不改变presence，StateChange切换Alive/Dormant。",object_count)
    end_keys = pd.MultiIndex.from_frame(events.loc[events.event_type_code.eq(7),["wall_id","uti"]])
    dormant = events.loc[events.event_type_code.eq(6) & events.status_code.eq(2)]
    overlap = dormant.loc[pd.MultiIndex.from_frame(dormant[["wall_id","uti"]]).isin(end_keys)].drop_duplicates(["wall_id","uti"])
    add_finding("dormant-end-overlap",symbol,overlap,len(end_keys),
                "D2已采用：本拍End成立时不再发布进入Dormant；恢复Alive与End同拍不属于该冲突。",object_count,"object_tick_group")
    add_profile("same_tick_order_profile", "REG-D2", symbol,dict(dormant_end_overlap_groups=len(overlap)),len(events),len(end_keys),source)
    add_profile("reference_integrity_profile", "INV-01", symbol,
                dict(side_mutating_objects=int(events.groupby("wall_id").side_code.nunique().gt(1).sum()), explicit_parent_reference="NOT_APPLICABLE"),
                len(events), object_count, source)
    changed_sides = events.groupby("wall_id").side_code.nunique()
    add_finding("identity-side-change",symbol,events.loc[events.wall_id.isin(changed_sides.index[changed_sides.gt(1)])],
                object_count,"Wall侧别是持续身份属性，同一source-local身份不能跨bid/ask变换。",object_count)
    # D3只重新量化薄触End后的同侧相邻Start模式；Owner暂缓，不在G定位规则原因或改参数。
    d3_rows = []
    for side in [1,2]:
        sequence = events.loc[events.side_code.eq(side) & events.event_type_code.isin([4,7])].copy()
        previous = sequence.shift()
        match = (sequence.event_type_code.eq(4) & previous.event_type_code.eq(7) & previous.reason_code.eq(2) &
                 sequence.core_price.eq(previous.core_price) & sequence.band_lo.eq(previous.band_lo) & sequence.band_hi.eq(previous.band_hi))
        pairs = sequence.loc[match].copy()
        pairs["previous_wall_id"] = previous.loc[match,"wall_id"].to_numpy()
        pairs["gap_uti"] = pairs.uti.to_numpy()-previous.loc[match,"uti"].to_numpy()
        pairs["gap_wall_clock_seconds"] = (pairs._event_time.to_numpy()-previous.loc[match,"_event_time"].to_numpy())/np.timedelta64(1,"s")
        d3_rows.append(pairs)
    d3 = pd.concat(d3_rows).sort_index()
    d3.to_parquet(DEST/(symbol+"-D3-thin-end-same-position-restart.parquet"),compression="zstd")
    profile["known_finding_reviews"].append(dict(finding_id="D3",status="DEFERRED_BY_OWNER",symbol=symbol,
                                                observed_pattern_count=len(d3),gap_uti=distribution(d3.gap_uti),
                                                applicable_thin_ends=int((events.event_type_code.eq(7)&events.reason_code.eq(2)).sum()),
                                                scope_limit="严格使用已发布 band/core 相等的可读子模式；缺少thin/support逐拍量，不能等同全部D3或确认业务错误。"))
    profile["known_finding_reviews"].append(dict(finding_id="D4",symbol=symbol,fixed_fixture_regression="PASS",
                                                full_per_tick_support_far_regression="NOT_EXPOSED",status="NO_GLOBAL_CLOSE_CLAIM"))
    if len(lives.dropna(subset=["lifetime_uti"])):
        question_id="SQ-"+symbol.upper()+"-LIFETIME"
        longest=lives.lifetime_uti.idxmax()
        row=lives.loc[longest]
        location=dict(symbol=symbol,start_time=str(row.start__event_time),end_time=str(row.end__event_time),wall_id=int(longest))
        questions.append(dict(question_id=question_id,finding_type="SCENARIO_INTERPRETATION_QUESTION",feature_ref=binding["feature_name"],
                              reasonableness_unit_ref="BO-C1",statistical_pattern=distribution(lives.lifetime_uti),
                              why_statistics_cannot_decide="寿命与密度本身不足以判断墙是否符合真实市场过程。",
                              recommended_visual_evidence="原始盘口、同身份生命周期与band/core；候选不是已冻结正式场景。",
                              representative_locations=[location],priority="NORMAL",next_route="BUSINESS_EXPECTATION_DERIVATION"))
        cases.append(dict(case_candidate_id=question_id+"-LONGEST",source_finding_or_question_id=question_id,symbol=symbol,
                          start_time=location["start_time"],end_time=location["end_time"],object_ids=[int(longest)],
                          related_events=["Start","BandUpdate","End"],selection_reason="最长完整寿命，用于解释真实过程，不能直接判错。",
                          required_fields=["quote input","events","state_trace"]))
    profile["cross_symbol_profile"].append(dict(symbol=symbol,status="PROFILED",objects=object_count,event_occurrences=len(events),trace_samples=len(trace)))
    print(symbol,"全量可读分层剖面完成",object_count,"objects",len(events),"occurrences",flush=True)
    del trace,events
for symbol in missing:
    profile["cross_symbol_profile"].append(dict(symbol=symbol,status="MISSING_FORMAL_RESULT",value_or_distribution=None))
gate_status="BLOCKED" if missing else ("DIAGNOSIS_REQUIRED" if findings else "PASS_TO_SCENARIO_REVIEW")
gate=dict(status=gate_status,reasons=binding["known_data_limits"]+(["有结构疑点，需原诊断Skill接续。"] if findings else []),
          valid_profile_ref="GlobalBehaviorProfile.json",next_action="先由Owner确认m正式输入处理，再按采用版本补全/重跑正式范围与G；现有rb结果保留。" if missing else "按结构疑点/场景问题队列进入原生后继。")
result=dict(statistics_input_readiness="StatisticsInputReadiness.json",global_behavior_profile="GlobalBehaviorProfile.json",
            global_finding_candidates=findings,scenario_question_queue=questions,candidate_case_index=cases,
            diagnosis_input_adapters=adapters,gate=gate)
payloads={"FeatureRunResultBinding.json":binding,"StatisticsInputReadiness.json":readiness,
          "GlobalBehaviorProfile.json":profile,"GlobalFindingCandidates.json":findings,
          "ScenarioQuestionQueue.json":questions,"CandidateCaseIndex.json":cases,
          "DiagnosisInputAdapters.json":adapters,"GlobalProfileGate.json":gate,
          "FeatureGlobalBehaviorProfilingResult.json":result}
for name,value in payloads.items():
    (DEST/name).write_text(json.dumps(value,ensure_ascii=False,indent=2,allow_nan=False)+"\n")
print("G Gate",gate_status,"findings",len(findings),"missing",missing,flush=True)
