"""对本次真实交付作数值、可追溯性及原生合同一致性验收。"""
from pathlib import Path
from hashlib import sha256
from collections import Counter
from bisect import bisect_left, bisect_right
from datetime import datetime, timezone
import csv
import json
import math

ROOT=Path(__file__).resolve().parent
def load(name):return json.loads((ROOT/name).read_text())
def rows(name):
    with (ROOT/name).open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))
def n(v):return int(float(v))
def digest(path):return sha256(path.read_bytes()).hexdigest()
checks=[]
def passed(name,evidence):checks.append(dict(check=name,status='PASS',evidence=evidence))

b=load('FeatureRunResultBinding.json');g=load('FeatureGlobalBehaviorProfilingResult.json');s=load('profile/SUMMARY.json')
assert b['readback_validation']['all_31_tables_equal'] and len(b['run_result_tables'])==31
assert b['parameter_version']==digest(ROOT/'configuration.json')=='b72095ff100da926474701b74bff7586a74b9770bc81cadc34c23cfe223e5cb3'
cfg=load('configuration.json');old=load('preflight/baseline-configuration.json')
assert cfg['profile'].pop('observation_multiple')==800 and cfg==old and cfg['profile']['method']['revision']=='1'
assert load('FRP_SOURCE_BINDING.json')['checked_source_files']==778 and not load('FRP_SOURCE_BINDING.json')['mismatches']
assert all(x['current_match'] for x in load('TIS_SOURCE_RECHECK.json')['source_checks'])
assert digest(Path(b['actual_loading']['engine']))==b['actual_loading']['engine_sha256']
assert load('PRODUCTION_RECONCILIATION.json')['feature_production_completed'] and not load('PRODUCTION_PROCESS.json')['native_process_observed']
passed('X准确配置/代码/实际加载与独立回读','FeatureRunResultBinding.json; PRODUCTION_RECONCILIATION.json; 独立真实ts快照；原监控失败记录保留')

required_top=['statistics_input_readiness','global_behavior_profile','global_finding_candidates','scenario_question_queue','candidate_case_index','diagnosis_input_adapters','gate']
assert all(k in g for k in required_top)
assert g['statistics_input_readiness']['readiness_status']=='PARTIAL'
profile=g['global_behavior_profile'];defs={x['statistic_id']:x for x in profile['statistics_definitions']}
def_fields=['statistic_id','name','business_item_ref','count_unit','object_group_key','time_basis','denominator','deduplication_rule','same_tick_rule','strata','source_fields']
assert len(defs)==17 and all(all(k in x and x[k] for k in def_fields) for x in defs.values())
categories=['candidate_profile','object_profile','event_profile','state_occupancy_profile','transition_profile','lifecycle_profile','branch_reachability_profile','density_profile','reason_profile','reference_integrity_profile','same_tick_order_profile','cross_symbol_profile','cross_period_profile','cross_session_profile']
for name in categories:
    assert profile[name],name
    for item in profile[name]:
        assert item['statistic_id'] in defs
        assert all(k in item for k in ['stratum_id','value_or_distribution','sample_size','denominator_value','source_location','notes'])
passed('G原生字段合同与全部14类可支持剖面','FeatureGlobalBehaviorProfilingResult.json; 17项StatisticDefinition')

tt=rows('profile/scale_turns.csv');rr=rows('profile/raw_turns.csv');rev=rows('profile/candidate_revisions.csv');bb=rows('profile/candidate_births.csv')
assert len(tt)==s['upstream_scale_positions']==1859 and len(rr)==s['upstream_raw_positions']==10073
assert len({t['turn_id'] for t in tt})==len(tt) and sum(t['initial_anchor']=='True' for t in tt)==3
assert sum(t['used_by_f800']=='True' for t in tt)==s['used_distinct_scale_positions']==875
assert len(bb)==len({r['life'] for r in rev})==480 and len(rev)==1546
assert len({(r['life'],r['revision']) for r in rev})==1546
assert all(n(r['original_deadline'])-n(r['original_anchor'])==480000 and n(r['original_revision_end'])-n(r['original_deadline'])==3600 for r in rev)
assert sum(n(x['count']) for x in rows('profile/state_transitions.csv'))==len(rev)-len(bb)==1066
assert sum(n(x['count']) for x in rows('profile/first_block_reference_by_symbol.csv'))==len(tt)
assert sum(n(x['candidate_lives']) for x in rows('profile/counts_by_symbol_year.csv') if x['symbol']=='ALL_DISTINCT')==480
assert sum(n(x['revision_occurrences']) for x in rows('profile/counts_by_session.csv'))==1546
near=rows('profile/near_actual_pair_screen.csv')
assert Counter(p['decision'] for p in near)==dict(Positive=624,Unresolved=3,Veto=21)
assert s['potential_eligible_pairs_unseen']==0
direction=rows('profile/counts_by_direction.csv')
assert sum(n(x['scale_turn_positions']) for x in direction if x['symbol']=='ALL_DISTINCT')==1859
assert sum(n(x['candidate_lives']) for x in direction if x['symbol']=='ALL_DISTINCT')==480
passed('业务单位/总量/分层/转换/独立候选守恒','原始10073、尺度1859含3锚点、参加875、Life480、观点1546、转换1066；pair624/3/21')

# 使用独立窗口切片核验finding，不复用累计连续区间实现。
inputs={symbol:rows('upstream/'+symbol+'_kline.csv') for symbol in ['rb','hc','i']}
utis={s:[n(x['closeUti']) for x in rs] for s,rs in inputs.items()}
conflicts=rows('profile/violations_coverage_flag_vs_continuous_input.csv')
byexact={(x['life'],x['revision']):x for x in rev}
for cf in conflicts:
    u=n(cf['known']);a=u-480000
    for symbol,data in inputs.items():
        index=utis[symbol];start=bisect_left(index,a);end=bisect_right(index,u)
        window=data[start:end]
        assert len(window)==801 and index[start]==a and index[end-1]==u
        assert all(n(y['closeUti'])-n(x['closeUti'])==600 for x,y in zip(window,window[1:]))
        assert all(x['close'] and math.isfinite(float(x['close'])) for x in window)
    assert byexact[(cf['life'],cf['revision'])]['coverage_incomplete']=='1'
assert len(conflicts)==22 and len({x['life'] for x in conflicts})==12 and len({x['timestamp'] for x in conflicts})==18
struct=load('profile/STRUCTURAL_CHECKS.json')
assert len(struct)==24 and {x['check_id']:x['repeat_count'] for x in struct if x['repeat_count']}=={'coverage_flag_vs_continuous_input':22}
passed('finding的22×三对象×801行独立窗口反核','所有窗口实际有效且600UTI连续；18时刻、12Life；其余23项结构检查为零')

findings=g['global_finding_candidates'];adapters=g['diagnosis_input_adapters'];questions=g['scenario_question_queue'];cases=g['candidate_case_index']
assert len(findings)==len(adapters)==1 and len(questions)==4 and len(cases)==10
f=findings[0];a=adapters[0]
assert all(k in f for k in ['finding_id','finding_type','feature_ref','run_binding','reasonableness_unit_ref','business_object_ref','observation','structural_invariant_ref','evidence_scope','repeat_count','affected_count','affected_ratio','representative_locations','alternative_non_error_explanations','current_confidence','next_route','diagnosis_input_adapter_ref'])
assert f['finding_type']=='STRUCTURAL_FINDING_CANDIDATE' and f['repeat_count']==22 and f['affected_ratio']==22/1546
assert a['finding_id']==f['finding_id'] and a['evidence_comparison_package']['scenario_id']=='GLOBAL_PROFILE'
assert all(k in a['frozen_expectation'] for k in ['expectation_id','version','statement','origin','applicable_conditions','falsifier_or_counterevidence'])
ids={f['finding_id']}|{q['question_id'] for q in questions}
assert all(c['source_finding_or_question_id'] in ids and c['candidate_only'] and c['start_time']<=c['end_time'] for c in cases)
assert g['gate']['status']=='DIAGNOSIS_REQUIRED' and all(x['completed'] for x in load('WORKFLOW_COMPLETION.json')['steps'])
passed('疑点/场景问题/适配/案例/Gate闭合','一项结构finding与一个Adapter；4个场景问题，10个候选案例；没有将Gate诊断要求改写为释放通过')

audit=dict(completed=True,verified_at=datetime.now(timezone.utc).isoformat(),checks=checks,
    feature_behavior_changed=False,additional_formal_instances=0,diagnosis_performed=False,workers=[],
    validation_limit='这是原生专业交付与证据一致性验收；不是manager消费、后继诊断、标定或FeatureRelease验收')
(ROOT/'VALIDATION.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(completed=True,checks=len(checks),gate=g['gate']['status']),ensure_ascii=False))
