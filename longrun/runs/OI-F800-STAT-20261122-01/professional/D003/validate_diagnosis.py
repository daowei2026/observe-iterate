"""有证据的诊断交付验收；不是正式修复或Feature释放验收。"""
from pathlib import Path
from hashlib import sha256
from datetime import datetime,timezone
import json,csv,subprocess,re
ROOT=Path(__file__).resolve().parent;PREV=ROOT.parent/'D002'
def load(name):return json.loads((ROOT/name).read_text())
def rows(name):
    with (ROOT/name).open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))
def n(x):return int(float(x))
checks=[]
def ok(name,evidence):checks.append(dict(check=name,status='PASS',evidence=evidence))

adapter=json.loads((PREV/'DiagnosisInputAdapters.json').read_text())[0]
assert load('FrozenExpectation.json')==adapter['frozen_expectation']
assert load('EvidenceComparisonPackage.json')==adapter['evidence_comparison_package']
assert len(load('SOURCE_AUDIT.json')['sources'])==37
assert all(x['exact_git_match'] for x in load('SOURCE_AUDIT.json')['sources'])
assert sha256((PREV/'configuration.json').read_bytes()).hexdigest()=='b72095ff100da926474701b74bff7586a74b9770bc81cadc34c23cfe223e5cb3'
ok('被冻结输入、准确版本与原D绑定','37项来源；原Expectation/ComparisonPackage逐结构不变；配置SHA保持')

diag=load('DiagnosisReport.json')
fields=['diagnosis_id','expectation_id','expectation_version','discrepancy_statement','business_impact','confirmed_facts','processing_chain',
    'competing_explanations','ruled_out_explanations','remaining_explanations','discriminating_checks','current_localization','parameter_repairability','confidence','next_route']
assert all(x in diag for x in fields)
assert diag['expectation_id']==adapter['frozen_expectation']['expectation_id']
assert len(diag['processing_chain'])==6
assert all(all(k in p for k in ['Input','Rule','State','Output','ActualTime','ConfirmTime','Version','PossibleInformationLoss']) for p in diag['processing_chain'])
assert diag['current_localization']['category']=='ImplementationMismatch' and diag['remaining_explanations']==[]
assert diag['parameter_repairability']['feasibility_status']=='PROVEN_NOT_ADJUSTABLE'
assert all(k in diag['parameter_repairability'] for k in ['suspected_parameters','parameter_consumers','earliest_business_divergence','feasibility_evidence','upstream_dependency','unresolved_constraints','next_route'])
assert diag['ImplementationConformance'] and diag['BusinessReasonableness']['value_tradeoff_required'] is False
ok('原生DiagnosisReport字段及不确定性路由','六阶段链、六竞争解释逐项检查；实现事实与业务合理性分别报告；非盲目标定')

e=load('EXPERIMENT_RESULTS.json');replay=rows('PUBLISHED_FLAG_RECONCILIATION.csv');changed=rows('DIAGNOSTIC_COUNTERFACTUAL_AT_PUBLISHED_LOCATIONS.csv')
assert len(replay)==1546 and all(n(r['published_flag'])==n(r['native_derived_flag']) for r in replay)
assert len(changed)==22 and len({r['life'] for r in changed})==12 and len({r['timestamp'] for r in changed})==18
assert sum(n(r['integer_diagnostic_flag']) for r in replay)==8
old=[]
with (PREV/'profile/violations_coverage_flag_vs_continuous_input.csv').open(encoding='utf-8-sig') as f:old=list(csv.DictReader(f))
assert {(r['life'],r['revision']) for r in changed}=={(r['life'],r['revision']) for r in old}
breaks=rows('SOURCE_FALSE_BREAKS.csv');assert len(breaks)==3
assert all(n(r['integer_delta'])==600 and float(r['position_delta'])!=1 and n(r['new_accumulated_start'])==78643799 for r in breaks)
assert e['diagnostic_only'] and not e['formal_feature_run'] and not e['source_behavior_changed']
ok('派生重放与全体正式finding位置闭合','1546/1546、0差异；22观点/12Life/18时刻与D002逐exact相等，8冷启动保留')

h=load('HASKELL_PROBE_VALIDATION.json');assert h['completed'] and h['exit_code']==0
assert sha256((ROOT/'DoubleGuardProbe.hs').read_bytes()).hexdigest()==h['source_sha256']
assert sha256((ROOT/'HASKELL_DOUBLE_GUARD_PROBE.csv').read_bytes()).hexdigest()==h['output_sha256']
probe={x['name']:x for x in rows('HASKELL_DOUBLE_GUARD_PROBE.csv')}
assert probe['real_boundary']['source_guard']=='False' and probe['real_boundary']['integer_diagnostic_guard']=='True'
assert probe['true_gap_control']['source_guard']==probe['true_gap_control']['integer_diagnostic_guard']=='False'
assert all(probe[x]['source_guard']==probe[x]['integer_diagnostic_guard']=='True' for x in ['normal_before','normal_after'])
ok('独立Haskell四对照真实执行','Double真实边界误拒绝可复现；真实跳过一根不被连接；前后正常边通过')

mp=load('ModificationProposal.json');issue=load('RequirementOrImplementationIssue.json')
assert all(k in mp for k in ['finding_ref','current_behavior','proposed_change','why_this_stage','alternatives','expected_effect','possible_side_effects','validation_plan','files_or_parameters_to_change'])
assert not mp['formal_change_applied'] and not mp['formal_patch_prepared'] and not diag['formal_repair_applied']
assert issue['issue_type']=='ImplementationMismatch' and issue['status']=='CONFIRMED_NOT_REPAIRED'
assert load('OWNER_DECISION_APPLICABILITY.json')['owner_decision_packet_required'] is False
assert not (ROOT/'OwnerDecisionPacket.json').exists()
assert all(x['completed'] for x in load('WORKFLOW_COMPLETION.json')['steps'])
for source in load('CODE_AUDIT.json')['sources']:
    path=source['ref'].split(':',1)[1]
    approved=Path('/dwdhome/fy/BASE_E6_2_copy/.runtime/f-observation-multiple-github-20261122/frp')/path
    runtime=Path('/dwdhome/fy/BASE_E6_2_copy/.runtime/f-wide-observation-20261122/runtime/edh-universe/frp/frp')/path
    assert sha256(approved.read_bytes()).hexdigest()==sha256(runtime.read_bytes()).hexdigest()==source['sha256']
ok('具体提案、未实施状态与专业完成边界','Owner确认前不改正式代码；六源文件与实际加载runtime哈希均保持；无第三类业务取舍不造OwnerDecisionPacket')

audit=dict(completed=True,verified_at=datetime.now(timezone.utc).isoformat(),checks=checks,
    diagnosis_scope_complete=True,implementation_applied=False,formal_feature_run=False,global_profiling_rerun=False,
    feature_release=False,workers=[],completion_boundary='本D诊断及提案交付；Owner确认/实施/XG复验/释放由原manager沿既定流程接续')
(ROOT/'VALIDATION.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(completed=True,checks=len(checks),classification=issue['issue_type'],formal_repair=False),ensure_ascii=False))
