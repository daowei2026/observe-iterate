"""核原G字段合同/准确来源及独立计数对账，不替代业务诊断。"""
from common import *
from collections import Counter
from decimal import Decimal
import csv,uuid
def load(n):return json.loads((ROOT/n).read_text())
def read(p):
    with p.open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))
def num(v):return int(Decimal(v))
def uid(row,p):return str(uuid.UUID(int=(int(row[p+'idHigh'])<<64)|int(row[p+'idLow']))) if row[p+'idForm']=='1' else row[p+'idText']
def parent(r):return tuple(r[k] for k in ['timestamp','occurrence','record_id','child_id_2'])
audit=load('SOURCE_REF_AUDIT.json');reuse=load('REUSE_EVIDENCE_READBACK.json')
assert audit['professional_control_commit']==LOCKED and audit['count']==47
for source in audit['exact_sources']:
    repo,rest=source['source_ref'].split('@',1);commit,path=rest.split(':',1)
    raw=git_bytes(commit,path)
    assert sha(raw)==source['sha256'] and Path(source['local_copy']).read_bytes()==raw
for source in reuse['source_refs']:
    raw=Path(source['local_path']).read_bytes();assert sha(raw)==source['sha256']
assert reuse['table_count']==31 and reuse['all_exact_bytes_match']
assert not reuse['new_public_reader_invoked'] and not reuse['native_producer_invoked'] and not reuse['prior_G_script_executed']
binding=read_json(U,PREFIX+'/professional/D008/FeatureRunResultBinding.json')
con=load('ConcurrencyProfile.json');sem=load('IncrementalSemanticChecks.json')
calendar=load('CALENDAR_SOURCE_READBACK.json');rows=read(Path(calendar['local_artifact_path']))
assert sha(Path(calendar['local_artifact_path']).read_bytes())==calendar['sha256']
axis=[num(r['closeUti']) for r in rows]
main=read(D008/'readback/tables/occurrences.csv');parts={parent(r):r for r in read(D008/'readback/tables/occurrences_groupFormationParticipation.csv')}
hist={}
for row in main:
    life=uid(row,'groupReference_referenceLife_');hist.setdefault(life,[]).append(row)
assert len(hist)==480 and len(main)==1538
intervals=[]
for life,values in hist.items():
    values.sort(key=lambda r:(num(r['groupKnownFrom']),parent(r)))
    intervals.append((num(values[0]['groupKnownFrom']),num(values[0]['groupRevisionEnd'])))
# 独立直接枚举每个原Calendar采样点，核增量差分/分段算法的全轴计数及端点。
direct=[sum(start<=u<=stop for start,stop in intervals) for u in axis]
segments=read(ROOT/'incremental/concurrency_segments.csv');expanded=[]
for segment in segments:
    a=int(segment['start_index']);b=int(segment['end_index_exclusive'])
    assert len(expanded)==a and b>a
    expanded.extend([int(segment['d008_responsibility_inclusive'])]*(b-a))
assert expanded==direct and len(expanded)==49683 and max(direct)==36
assert sum(n==36 for n in direct)==con['peak_sample_positions']==60
first=direct.index(36);assert axis[first]==con['first_peak_uti'] and rows[first]['timestamp']==con['first_peak_time']
u=axis[first];latest=[]
for values in hist.values():
    if num(values[0]['groupKnownFrom'])<=u<=num(values[0]['groupRevisionEnd']):
        latest.append(max((r for r in values if num(r['groupKnownFrom'])<=u),key=lambda r:(num(r['groupKnownFrom']),parent(r))))
assert len(latest)==36
assert Counter(r['groupObservation_name'] for r in latest)=={'Open':27,'Subsumed':9}
assert Counter(parts[parent(r)]['participationDutyClosed'] for r in latest)=={'0':36}
assert len({num(r['groupAnchor']) for r in latest})==27
assert all(c['repeat_count']==0 for c in sem['checks']) and [c['denominator'] for c in sem['checks']]==[480,480,242,219]
assert len(read_json(U,PREFIX+'/professional/D008/profile/STRUCTURAL_CHECKS.json'))==27
profile=load('GlobalBehaviorProfile.json')
needed=['candidate_profile','object_profile','current_object_profile','event_profile','state_occupancy_profile','transition_profile',
    'lifecycle_profile','conversion_profile','branch_reachability_profile','density_profile','reason_profile',
    'reference_integrity_profile','same_tick_order_profile','cross_symbol_profile','cross_period_profile','cross_session_profile']
for field in needed:
    assert profile[field]
    for r in profile[field]:
        assert all(k in r for k in ['statistic_id','stratum_id','value_or_distribution','sample_size','denominator_value','source_location','notes'])
assert len(profile['statistics_definitions'])==22 and not profile['prior_values_recomputed']
for d in profile['statistics_definitions']:
    assert all(k in d for k in ['statistic_id','name','business_item_ref','count_unit','object_group_key','time_basis','denominator','deduplication_rule','same_tick_rule','strata','source_fields'])
discovery=load('FindingDiscoverySummary.json');queue=load('CandidateFindingQueue.json')
findings=load('GlobalFindingCandidates.json')['candidates'];adapters=load('DiagnosisInputAdapters.json')['adapters']
assert discovery['discovery_pass_complete'] and discovery['first_candidate_did_not_stop_discovery']
assert len(discovery['business_surfaces_reviewed'])==9 and all(s['assessment_complete'] and s['evidence_refs'] for s in discovery['business_surfaces_reviewed'])
assert len(discovery['remaining_unreviewed_surfaces'])==3
assert queue['snapshot_id']==discovery['queue_snapshot_id'] and queue['candidates']==findings
assert queue['parameter_version']==binding['parameter_version'] and queue['feature_ref']==binding['code_version']
assert queue['data_scope']==binding['data_scope'] and queue['new_evidence_may_add_candidates']
assert queue['run_binding']==pro_ref('FeatureRunResultBinding.json') and queue['professional_control_commit']==LOCKED
assert len(findings)==len(adapters)==1
required=['finding_id','finding_type','candidate_origin','feature_ref','run_binding','reasonableness_unit_ref','business_object_ref',
    'observation','candidate_basis','why_high_confidence','confidence_limits','contract_or_business_semantics_ref',
    'evidence_scope','repeat_count','affected_count','affected_ratio','representative_locations','alternative_non_error_explanations',
    'current_confidence','must_assess_before_release','next_route','diagnosis_input_adapter_ref']
for f,a in zip(findings,adapters):
    assert all(k in f for k in required)
    assert f['finding_id']==a['finding_id']=='F-LIFE-PEAK-CONCURRENCY'
    assert f['candidate_origin']=='OWNER_RAISED' and f['status']=='CANDIDATE'
    assert f['current_confidence']=='OWNER_CONCERN' and f['owner_assessment_status']=='PROMOTED'
    assert f['must_assess_before_release'] and f['logic_localization_ref'] is None
    assert f['repeat_count']==60 and f['affected_count']==36
    assert all(k in a for k in ['adapter_id','finding_id','frozen_expectation','evidence_comparison_package','business_intent_ref',
        'processing_chain_ref','relevant_code_or_requirement_refs','data_binding_and_time_basis'])
    assert all(k in a['frozen_expectation'] for k in ['expectation_id','version','statement','origin','applicable_conditions','falsifier_or_counterevidence'])
    ecp=a['evidence_comparison_package']
    assert all(k in ecp for k in ['comparison_id','scenario_id','data_binding','time_basis','parameter_version','evidence_items','judgment'])
    assert ecp['scenario_id']=='GLOBAL_PROFILE' and ecp['parameter_version']==binding['parameter_version']
    assert all(x['evidence_status'] in ['SUPPORTS','AMBIGUOUS','MISSING','NOT_APPLICABLE','PENDING','COUNTERS'] for x in ecp['evidence_items'])
    assert not a['diagnosis_performed']
obs=load('ObservationsNotPromoted.json')['observations']
assert len(obs)==8 and all(all(k in r for k in ['observation_id','feature_ref','run_binding','observation','evidence_refs','why_not_promoted','revisit_condition']) for r in obs)
assert load('GlobalProfileGate.json')['status']=='DIAGNOSIS_REQUIRED'
assert not load('GlobalProfileGate.json')['feature_release_allowed']
assert len(load('CandidateCaseIndex.json')['cases'])==1
closed=load('FindingRegister.json')['closed_findings_reused']
assert closed==read_json(U,PREFIX+'/professional/D008/FindingDisposition.json')['findings']
assert all(f['status']=='CLOSED_ON_LATEST_PROFILE' for f in closed)
assert load('G_WORKFLOW_COMPLETION.json')['discovery_completed'] and not load('G_WORKFLOW_COMPLETION.json')['diagnosis_completed']
assert load('INPUT_BINDING.json')['professional_control_commit']==LOCKED and load('INPUT_BINDING.json')['workers']==[]
save('VALIDATION.json',dict(checked_at=now(),checks_passed=True,exact_source_count=47,reused_exact_files=len(reuse['source_refs']),
    prior_readback_tables_verified=31,new_OnlyRead_or_native_run=False,
    original_G_not_rerun=True,all_native_G_contract_fields_pass=True,discovery_surfaces=9,observations_not_promoted=8,
    owner_candidate_status='CANDIDATE / PROMOTED_TO_D / OWNER_CONCERN',gate='DIAGNOSIS_REQUIRED',
    full_calendar_direct_count_check_positions=len(direct),peak_count=36,peak_positions=60,
    first_peak_public_states={'Open':27,'Subsumed':9},supplemental_semantic_checks=4,
    source_profile_and_closed_findings_preserved=True,professional_control_commit=LOCKED,
    root_cause_localization_or_fix_performed=False,FeatureRelease=False,
    check_boundary='验证准确来源、原G合同与公开增量统计可追溯；不是判定36业务合理/不合理或完成Owner指定D。'))
print(json.dumps(dict(checks_passed=True,direct_calendar_positions=len(direct),candidates=1,gate='DIAGNOSIS_REQUIRED',contract_fields=True),ensure_ascii=False))
