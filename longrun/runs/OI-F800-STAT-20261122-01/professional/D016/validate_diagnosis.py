"""交叉核验：独立既有profile与本D原生表解码，检查原Skill合同与不扩大结论。"""
from common import *
from decimal import Decimal
from collections import Counter
num=lambda s:int(Decimal(s))
def load(n):return json.loads((ROOT/n).read_text())
S=load('Peak36Summary.json');details=load('Peak36LifeDetails.json')['life_details'];hist=load('Peak36RevisionHistory.json')['revisions'];window=load('PeakWindowReconciliation.json');diag=load('DiagnosisReport.json')
births=rows('profile/candidate_births.csv');revisions=rows('profile/candidate_revisions.csv')
profiles={r['life']:[] for r in births}
for r in revisions:profiles[r['life']].append(r)
for rs in profiles.values():rs.sort(key=lambda r:(num(r['known']),num(r['occurrence']),num(r['record_id']),num(r['child_id_2'])))
u=80426999;expected={b['life'] for b in births if num(b['known'])<=u<=num(b['original_revision_end'])}
assert expected=={x['life'] for x in details} and len(expected)==36
for x in details:
 rs=profiles[x['life']];current=[r for r in rs if num(r['known'])<=u][-1]
 assert current['revision']==x['current_revision'] and current['timestamp']==x['current_revision_time']
 assert current['observation']==x['observation'] and current['local_basis']==x['local_basis']
 assert num(current['revision_end'])==x['current_question']['revision_end']
 assert (u-num(current['original_anchor']))/120==x['age_open_minutes']
 assert {m['locator'] for m in x['members']}==set(current['members'].split(';'))
 assert len(rs)==x['revisions_full_sample']
 closers=[r for r in rs if num(r['duty_closed'])]
 assert len(closers)==1 and num(closers[0]['known'])==num(rs[-1]['known'])==x['first_duty_close_known']
 assert num(rs[-1]['known'])==num(rs[-1]['revision_end'])
for snap in window['snapshots']:
 at=snap['uti'];inclusive={l for l,rs in profiles.items() if num(rs[0]['known'])<=at<=num(rs[0]['original_revision_end'])}
 current={l:[r for r in rs if num(r['known'])<=at][-1] for l,rs in profiles.items() if num(rs[0]['known'])<=at}
 duty={l for l,r in current.items() if not num(r['duty_closed'])}
 assert inclusive==set(snap['responsibility_lives']) and duty==set(snap['source_reconstructed_active_lives'])
assert len(hist)==118 and sum(x['revisions_to_peak'] for x in details)==45
assert sum(len(x['members']) for x in details)==86 and sum(len(x['required_pairs']) for x in details)==64
assert Counter(x['observation'] for x in details)=={'Open':27,'Subsumed':9}
assert Counter(s['source_reconstructed_active_count'] for s in window['snapshots'])=={36:59,35:1}
assert len({(x['life'],x['revision']) for x in hist})==118
assert all(c['conflicts']==0 for c in S['checks'])
# D原生输出合同，不把未决finding洗成Release或代码缺陷。
required=['diagnosis_id','expectation_id','expectation_version','discrepancy_statement','business_impact','confirmed_facts','processing_chain','competing_explanations','ruled_out_explanations','remaining_explanations','discriminating_checks','current_localization','parameter_repairability','confidence','next_route']
assert all(diag[k] for k in required)
assert all(diag['parameter_repairability'].get(k) for k in ['suspected_parameters','parameter_consumers','earliest_business_divergence','feasibility_status','feasibility_evidence','upstream_dependency','unresolved_constraints','next_route'])
assert diag['parameter_repairability']['feasibility_status']=='EVIDENCE_INSUFFICIENT'
assert diag['professional_control_commit']==LOCKED and 'ImplementationConformance' in diag and 'BusinessReasonableness' in diag
L=load('LogicLocalization.json');assert all(L.get(k) for k in ['finding_id','observed_anomaly','business_processing_chain','responsible_logic','source_refs','why_this_is_the_responsible_logic'])
owner=load('OwnerDecisionPacket.json');assert all(owner.get(k) for k in ['decision_id','business_question','why_data_cannot_decide_alone','option_a','option_b','common_facts','uncertain_facts','implementation_implications','recommended_observation_cases','owner_decision_needed'])
for k in ['option_a','option_b']:assert all(owner[k].get(f) for f in ['preserves','sacrifices','supporting_cases','counter_cases'])
handoff=load('D_HANDOFF.json');f=load('FindingDisposition.json')
assert f['status']=='DIAGNOSIS_IN_PROGRESS' and not f['REJECTED_AS_NON_ISSUE'] and not f['confirmed_code_defect']
assert handoff['remaining_D016_authorized_items']==[] and handoff['workers']==[] and handoff['professional_state']=='REPORTED_COMPLETE'
assert not any(handoff[k] for k in ['manager_consumed','parent_run_completed','FeatureRelease','new_production','formal_behavior_changed'])
assert not diag['feature_release_allowed']
assert not any((ROOT/n).exists() for n in ['FeatureReleaseGate.json','UpstreamReleasePackage.json'])
assert load('SOURCE_REF_AUDIT.json')['count']==71 and load('REUSE_EVIDENCE_READBACK.json')['native_tables']==31
for entry in load('CURRENT_SOURCE_AUDIT.json')['files']:
 raw=Path(entry['local_copy']).read_bytes();assert sha(raw)==entry['sha256'] and entry['source_ref'].startswith('daowei2026/frp@'+FRP+':')
# 原生报告采用完整commit；不是只在机器Return增加自造字段。
report=(ROOT/'EXECUTOR_REPORT.md').read_text();assert LOCKED in report and '36' in report and 'OwnerDecisionPacket' in report
save('VALIDATION.json',dict(checked_at=now(),checks_passed=True,professional_control_commit=LOCKED,exact_input_sources=71,exact_reused_files=load('REUSE_EVIDENCE_READBACK.json')['count'],reused_native_tables=31,exact_current_frp_files=len(load('CURRENT_SOURCE_AUDIT.json')['files']),independent_profile_native_roster_match=True,all_36_lives_reviewed=True,peak_life_count=36,peak_member_rows=86,peak_required_pairs=64,all_36_revision_history_occurrences=118,peak_first36_revisions_to_date=45,peak_window_samples_checked=60,source_reconstructed_current_counts={'36':59,'35':1},native_internal_trace_measured=False,all_original_D_native_fields_present=True,LogicLocalization_created_before_diagnosis=True,finding_status=f['status'],business_tradeoff_open=True,formal_behavior_changed=False,FeatureRelease=False,validation_boundary='核准确来源、全部36逐项原生事实/独立profile交叉对照及原D合同；不把SOURCE_RULE_RECONSTRUCTION叫内部trace，不把结构合法性叫业务合理性，也未声称原gate完整CLI通过。'))
print(json.dumps(dict(checks_passed=True,all_36_lives=True,revisions=118,independent_profiles_match=True,FeatureRelease=False),ensure_ascii=False))
