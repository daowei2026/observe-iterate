"""补同刻与原位重建剖面，并核对统计守恒；不重算Feature。"""
import json
from pathlib import Path
import numpy as np
import pandas as pd

OUT=Path(__file__).resolve().parent
ROOT=OUT/"profile"
profile=json.loads((ROOT/"GlobalBehaviorProfile.json").read_text())
spec=json.loads((OUT/"statistics-specification.json").read_text())
checks=[]
profile["candidate_profile"]=[]
profile["cross_symbol_profile"]=[]
profile["missing_strata"]=profile["run_binding"]["missing_symbols"]
definition=dict(statistic_id="EV-02",name="同刻 occurrence 基数与同对象事件顺序",
                business_item_ref="OC-C1..4",count_unit="物理timestamp组／对象uti组分别计",
                object_group_key="source namespace + symbol + wall_id + uti",
                time_basis="native timestamp、uti与物理ordinal",denominator="对应已发生事件组数",
                deduplication_rule="packed并集；同类型重复occurrence保留",
                same_tick_rule="按全局物理ordinal保留每条，再按对象分组；不引入业务因果优先级",
                strata=["symbol","side"],source_fields=["wall_id","uti","occurrence_ordinal","event_type_code","side_code"])
spec["statistics_definitions"].append(definition)
profile["statistics_definitions"]=spec["statistics_definitions"]
for symbol in profile["run_binding"]["verified_symbols"]:
    directory=OUT/"results"/symbol
    events=pd.read_parquet(directory/"wall_events.parquet")
    clock=pd.read_parquet(directory/"tables/wall_assembler_state_trace.parquet",columns=["uti"])
    assert events.index.isin(clock.index).all()
    assert np.array_equal(events.uti.to_numpy(),clock.reindex(events.index).uti.to_numpy())
    physical=events.groupby(level=0,sort=False).size()
    object_tick=events.groupby(["wall_id","uti"],sort=False).size()
    multi=object_tick.index[object_tick.gt(1)]
    selected=events.loc[pd.MultiIndex.from_frame(events[["wall_id","uti"]]).isin(multi)]
    combinations=selected.assign(code=selected.event_type_code.astype(int).astype(str)).groupby(["wall_id","uti"],sort=False).code.agg("->".join).value_counts()
    profile["same_tick_order_profile"].append(dict(statistic_id="EV-02",stratum_id=symbol,
        value_or_distribution=dict(physical_timestamp_groups=len(physical),physical_multiplicity={str(int(k)):int(v) for k,v in physical.value_counts().items()},
                                   object_uti_groups=len(object_tick),multiple_object_uti_groups=int(object_tick.gt(1).sum()),
                                   multi_event_type_sequences={str(k):int(v) for k,v in combinations.items()},
                                   same_object_uti_type_extra_occurrences=int(events.duplicated(["wall_id","uti","event_type_code"]).sum())),
        sample_size=len(events),denominator_value=len(object_tick),source_location=str(directory/"wall_events.parquet"),
        notes="物理时间组可能含双侧；对象拍组只含同一身份。同类型同拍多次保留，不盲目去重。"))
    consecutive=[]
    for side,group in events.loc[events.event_type_code.eq(4)].groupby("side_code",sort=True):
        previous=group.shift()
        matched=(group.core_price.eq(previous.core_price)&group.band_lo.eq(previous.band_lo)&group.band_hi.eq(previous.band_hi))
        hit=group.loc[matched].copy();hit["previous_wall_id"]=previous.loc[matched,"wall_id"].to_numpy()
        hit["inter_start_gap_uti"]=hit.uti.to_numpy()-previous.loc[matched,"uti"].to_numpy()
        consecutive.append(hit)
    repeated=pd.concat(consecutive)
    repeated.to_parquet(ROOT/(symbol+"-same-position-consecutive-starts.parquet"),compression="zstd")
    profile["lifecycle_profile"].append(dict(statistic_id="LC-02",stratum_id=symbol,
        value_or_distribution=dict(strict_same_position_consecutive_start_pairs=len(repeated)),sample_size=int(events.event_type_code.eq(4).sum()),
        denominator_value=int(events.event_type_code.eq(4).sum()-events.side_code.nunique()),
        source_location=str(ROOT/(symbol+"-same-position-consecutive-starts.parquet")),
        notes="同侧相邻Start的已发布band/core精确相等子模式；不是同一身份恢复，也不能仅凭数量判错。"))
    count=sum(sum(item["value_or_distribution"].values()) for item in profile["event_profile"] if item["stratum_id"].startswith(symbol+"/"))
    assert count==len(events)
    assert sum(item["sample_size"] for item in profile["cross_period_profile"] if item["stratum_id"].startswith(symbol+"/"))==len(events)
    assert sum(item["sample_size"] for item in profile["cross_session_profile"] if item["stratum_id"].startswith(symbol+"/"))==len(events)
    for side in ["bid","ask"]:
        occupancy=next(item for item in profile["state_occupancy_profile"] if item["stratum_id"]==symbol+"/"+side)
        assert sum(value["samples"] for value in occupancy["value_or_distribution"].values())==len(clock)
        segments=pd.read_parquet(ROOT/(symbol+"-"+side+"-state-segments.parquet"),columns=["sample_count"])
        assert int(segments.sample_count.sum())==len(clock)
    native=json.loads((directory/"result.json").read_text())
    assert native["tables"]["wall_assembler_sparse_events"]["rows"]==len(events)
    assert sum(item["rows"] for key,item in native["tables"].items() if key.startswith("wall__stream"))==len(events)
    profile["cross_symbol_profile"].append(dict(statistic_id="EV-01",stratum_id=symbol,
        value_or_distribution=dict(event_occurrences=len(events),unique_objects=int(events.wall_id.nunique()),trace_samples=len(clock)),
        sample_size=len(events),denominator_value=len(clock),source_location=str(directory/"wall_events.parquet"),
        notes="只有rb可用，未作rb/m数值比较；对象数、occurrence和输入样本拍保持不同单位。"))
    checks.append(dict(symbol=symbol,event_month_clock_bin_counts_conserved=True,state_sample_segment_counts_conserved=True,
                       packed_sparse_row_counts_match=True,event_timestamp_and_uti_match_trace=True,
                       event_rows=len(events),trace_rows=len(clock)))
for section in ["object_profile","event_profile","state_occupancy_profile","transition_profile","lifecycle_profile",
                "branch_reachability_profile","density_profile","reason_profile","reference_integrity_profile",
                "same_tick_order_profile","cross_symbol_profile","cross_period_profile","cross_session_profile"]:
    for item in profile[section]:
        assert all(key in item for key in ["statistic_id","stratum_id","value_or_distribution","sample_size","denominator_value","source_location","notes"])
(OUT/"statistics-specification.json").write_text(json.dumps(spec,ensure_ascii=False,indent=2)+"\n")
(ROOT/"GlobalBehaviorProfile.json").write_text(json.dumps(profile,ensure_ascii=False,indent=2,allow_nan=False)+"\n")
(ROOT/"STATISTICS_SELF_CHECK.json").write_text(json.dumps(dict(checks=checks,requested_scope_preserved=["rb","m"],
    missing_symbol_not_counted_as_zero=profile["missing_strata"],gate_status=json.loads((ROOT/"GlobalProfileGate.json").read_text())["status"]),ensure_ascii=False,indent=2)+"\n")
print("统计口径、守恒与native对象拍时间映射核验通过；整体Gate仍保留缺失品种。",flush=True)
