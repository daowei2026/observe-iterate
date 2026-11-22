"""验收当前D008的原生数据、业务单位、版本复验和原Skill合同。"""
from pathlib import Path
from collections import Counter
from hashlib import sha256
from datetime import datetime, timezone
import csv
import json
import subprocess

ROOT=Path(__file__).resolve().parent
def load(n): return json.loads((ROOT/n).read_text())
def rows(n):
    with (ROOT/n).open(encoding='utf-8-sig',newline='') as f: return list(csv.DictReader(f))
def iv(x): return int(float(x))
def digest(p): return sha256(p.read_bytes()).hexdigest()
checks=[]
def passed(n,e): checks.append(dict(check=n,status='PASS',evidence=e))
B=load('FeatureRunResultBinding.json'); G=load('FeatureGlobalBehaviorProfilingResult.json'); S=load('profile/SUMMARY.json');C=load('VersionComparison.json')
P=load('PRODUCTION_PROCESS.json'); API=load('NATIVE_RETEST_API.json')
assert P['completed'] and P['exit_code']==0 and P['native_process_observed'] and P['independent_lock_probe_exit']==73
assert B['production']['feature_python_exit_code']==0 and B['production']['supervisor_exit_code']==0
assert B['actual_loading']['native_pid']==P['native_pid']
assert B['readback_validation']['all_31_tables_equal'] and B['readback_validation']['independent_process'] and B['readback_validation']['only_read']
assert len(B['run_result_tables'])==31
assert B['code_version']==dict(frp='daowei2026/frp@39f02ec4548e68ba8dbd30061afc870546000994',tis='daowei2026/tis@2f460d663d821cf2ba25555eda13e78b697d0767')
assert B['parameter_version']==digest(ROOT/'configuration.json')=='b72095ff100da926474701b74bff7586a74b9770bc81cadc34c23cfe223e5cb3'
cfg=load('configuration.json');base=load('preflight/baseline-configuration.json')
assert cfg['profile'].pop('observation_multiple')==800 and cfg==base and cfg['profile']['method']['revision']=='1'
assert cfg['profile']['delta']==600 and cfg['profile']['unit']=='CalendarUTITick'
assert digest(Path(B['actual_loading']['engine']))==B['actual_loading']['engine_sha256']=='4e0e22796bb6b32b6fd9afd1c3b18b5af1eebe1d35df24090fc19585866652f0'
source=load('FRP_SOURCE_BINDING.json');assert not source['mismatches'] and all(r['match'] for r in source['files'])
assert load('TIS_SOURCE_RECHECK.json')['all_match']
for t in B['run_result_tables']: assert digest(Path(t['path']))==t['sha256']
for f in load('NATIVE_OUTPUT_MANIFEST.json')['files']: assert digest(Path(B['result_identity']['full_dir'])/f['relative_path'])==f['sha256']
passed('最新X实际加载/配置/范围/锁及31表独立读回','FeatureRunResultBinding.json; PRODUCTION_PROCESS.json; NATIVE_OUTPUT_MANIFEST.json')

assert G['statistics_input_readiness']['binding_match']==dict(code_version='MATCH',parameter_version='MATCH',data_scope='CONFIRMED')
assert load('CurrentFeatureUnderstandingPackage.json')['feature_ref']['code_version']['frp']=='39f02ec4548e68ba8dbd30061afc870546000994'
profile=G['global_behavior_profile']; defs={r['statistic_id']:r for r in profile['statistics_definitions']}
required=['statistic_id','name','business_item_ref','count_unit','object_group_key','time_basis','denominator','deduplication_rule','same_tick_rule','strata','source_fields']
assert len(defs)==18 and all(all(k in r and r[k] for k in required) for r in defs.values())
categories=['candidate_profile','object_profile','event_profile','state_occupancy_profile','transition_profile','lifecycle_profile','branch_reachability_profile','density_profile','reason_profile','reference_integrity_profile','same_tick_order_profile','cross_symbol_profile','cross_period_profile','cross_session_profile']
for category in categories:
    assert profile[category],category
    for r in profile[category]:
        assert r['statistic_id'] in defs
        assert all(k in r for k in ['stratum_id','value_or_distribution','sample_size','denominator_value','source_location','notes'])
passed('G1当前理解适用绑定与原生字段合同','CurrentFeatureUnderstandingPackage.json; StatisticsInputReadiness.json; 18项定义及14类可支持剖面')

turns=rows('profile/scale_turns.csv'); raw=rows('profile/raw_turns.csv');revs=rows('profile/candidate_revisions.csv');births=rows('profile/candidate_births.csv')
assert len(turns)==S['upstream_scale_positions'] and len(raw)==S['upstream_raw_positions']
assert len({t['turn_id'] for t in turns})==len(turns)
assert sum(t['used_by_f800']=='True' for t in turns)==S['used_distinct_scale_positions']
assert len(births)==len({r['life'] for r in revs})==S['candidate_lives']
assert len(revs)==len({(r['life'],r['revision']) for r in revs})==S['candidate_revision_occurrences']
assert all(iv(r['original_deadline'])-iv(r['original_anchor'])==480000 and iv(r['original_revision_end'])-iv(r['original_deadline'])==3600 for r in revs)
assert sum(iv(r['count']) for r in rows('profile/state_transitions.csv'))==len(revs)-len(births)
assert sum(iv(r['count']) for r in rows('profile/first_block_reference_by_symbol.csv'))==len(turns)
assert sum(iv(r['candidate_lives']) for r in rows('profile/counts_by_symbol_year.csv') if r['symbol']=='ALL_DISTINCT')==len(births)
assert sum(iv(r['revision_occurrences']) for r in rows('profile/counts_by_session.csv'))==len(revs)
assert sum(iv(r['scale_turn_positions']) for r in rows('profile/counts_by_direction.csv') if r['symbol']=='ALL_DISTINCT')==len(turns)
assert all(float(r['distanceValue'])<=1200 for r in rows('readback/tables/occurrences_groupRequired_pairDistance.csv'))
struct=load('profile/STRUCTURAL_CHECKS.json'); assert len(struct)==27
actual_violations={c['check_id']:c['repeat_count'] for c in struct if c['repeat_count']}
assert actual_violations==C['new_structural_violations']
passed('单位、计数守恒、2Δ及全量分层','profile/SUMMARY.json; 27项结构检查；状态边数=Revision数-Life数；完整方向/年/Session/首阻断守恒')

assert C['same_parameter_version'] and C['all_upstream_equal'] and C['upstream_tables']==C['upstream_tables_byte_equal']
assert len(rows('comparison/all_31_tables.csv'))==31
assert C['matched_lives']+C['old_only_lives']==C['old_lives'] and C['matched_lives']+C['new_only_lives']==C['new_lives']
assert API['completed'] and API['producer_executed'] is False and API['only_read']
AC=load('InitialVersionComparison.json')
assert API['total']==API['passed']==AC['false_flag_retest_total']+AC['cold_control_total']+C['gf002_original_view_retest_total']
assert API['pid']!=B['readback_validation']['producer_pid'] and API['pid']!=B['readback_validation']['reader_pid']
assert AC['false_flag_retest_total']==22 and AC['cold_control_total']==8 and C['gf002_original_view_retest_total']==8
assert AC['all_upstream_equal'] and len(rows('comparison_ac/all_31_tables.csv'))==31
assert all(r['passed'] for r in API['results'])
assert sum(r['retest_kind']=='OLD_FALSE_FLAG' and r['native_flag']==0 for r in API['results'])==22
assert sum(r['retest_kind']=='OLD_COLD_START_CONTROL' and r['native_flag']==1 for r in API['results'])==8
assert sum(r['retest_kind']=='OLD_PRICE_GAP_FLAG' and r['native_flag']==1 for r in API['results'])==8
assert load('MISSING_INPUT_WINDOW_VALIDATION.json')['all_current_affected_views_flagged']
passed('同输入完整两版基线比较及38项独立原生Life/AsOf复验','VersionComparison.json; comparison/*.csv; NATIVE_RETEST_API.json（原reader沿exact链择观点）')

findings=G['global_finding_candidates'];adapters=G['diagnosis_input_adapters'];questions=G['scenario_question_queue'];cases=G['candidate_case_index']
assert len(findings)==len(adapters)
assert all(f['finding_type']=='STRUCTURAL_FINDING_CANDIDATE' and f['next_route']=='BUSINESS_DISCREPANCY_DIAGNOSIS' for f in findings)
assert {f['finding_id'] for f in findings}=={a['finding_id'] for a in adapters}
assert len(questions)==4 and all(q['finding_type']=='SCENARIO_INTERPRETATION_QUESTION' for q in questions)
ids={f['finding_id'] for f in findings}|{q['question_id'] for q in questions}
assert all(c['source_finding_or_question_id'] in ids and c['candidate_only'] and c['start_time']<=c['end_time'] for c in cases)
fd=load('FindingDisposition.json');assert fd['all_prior_findings_closed'] and len(fd['findings'])==2 and all(f['closed'] and f['status']=='CLOSED_ON_LATEST_PROFILE' for f in fd['findings'])
assert G['gate']['status']==('DIAGNOSIS_REQUIRED' if findings else 'PASS_TO_SCENARIO_REVIEW')
assert len(load('WORKFLOW_COMPLETION.json')['steps'])==8 and all(s['completed'] for s in load('WORKFLOW_COMPLETION.json')['steps'])
passed('原finding闭环、四项场景问题及G1–G8原生Gate','FindingDisposition.json; FeatureGlobalBehaviorProfilingResult.json; WORKFLOW_COMPLETION.json')

write=dict(completed=True,verified_at=datetime.now(timezone.utc).isoformat(),checks=checks,workers=[],
    formal_feature_source_changes_in_D008=False,formal_new_instance_count=1,production_attempts=2,failed_initial_attempt='PRODUCTION_ATTEMPT01_FAILURE.json',additional_formal_instances=0,
    gate=G['gate']['status'],native_retest_passed=API['passed'],
    validation_limit='本D原生专业职责验收，非manager已消费、父Run已释放或Q/V已通过。')
(ROOT/'VALIDATION.json').write_text(json.dumps(write,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(completed=True,checks=len(checks),gate=G['gate']['status'],closed_findings=[f['finding_id'] for f in fd['findings']]),ensure_ascii=False))
