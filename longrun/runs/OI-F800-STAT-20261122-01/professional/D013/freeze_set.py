from common import *
from copy import deepcopy

assert not (ROOT/'FREEZE_MANIFEST.json').exists(), '冻结后禁止无痕重写v1'
validation=json.loads((ROOT/'DRAFT_VALIDATION.json').read_text())
assert validation['checks_passed'] and validation['mode']=='draft'
cs=json.loads((ROOT/'draft/CaseReviewSet.READY.json').read_text())
es=json.loads((ROOT/'draft/ScenarioExpectationSet.READY.json').read_text())
pool=json.loads((ROOT/'CandidateCasePool.v1.json').read_text())
at=now()
cs['status']=es['status']='FROZEN_FOR_COMPARISON'
cs['frozen_at']=es['frozen_at']=at
for c in cs['cases']:c['status']='FROZEN_FOR_COMPARISON'
for e in es['expectations']:e['status']='FROZEN_FOR_COMPARISON'
save('CaseReviewSet.json',cs)
save('ScenarioExpectationSet.json',es)
frozen=dict(frozen_set_id='F800-S1-D013-FROZEN',version=1,status='FROZEN_FOR_COMPARISON',frozen_at=at,
    feature_ref=cs['feature_ref'],parameter_version=cs['parameter_version'],
    case_set_id=cs['case_set_id'],case_set_version=cs['version'],case_ids=[c['case_id'] for c in cs['cases']],
    case_review_set_ref='CaseReviewSet.json',case_review_set_sha256=sha((ROOT/'CaseReviewSet.json').read_bytes()),
    scenario_expectation_set_ref='ScenarioExpectationSet.json',scenario_expectation_set_sha256=sha((ROOT/'ScenarioExpectationSet.json').read_bytes()),
    observation_material_ref=cs['observation_material_ref'],review_target_ref=cs['review_target_ref'],
    expectations=es['expectations'],case_material_index='CaseMaterialIndex.json',coverage='CaseTypeCoverage.json',
    observation_gap_requests='ObservationGapRequests.json',open_questions='OpenQuestions.json',
    consumer_skill_ref=ref(LOCKED,'skills/reasonableness-analysis/business-evidence-comparison/SKILL.md'),
    compatibility='按当前原S2入口交CaseReviewSet+ScenarioExpectationSet/FrozenExpectationSet、当前U/ReviewTarget及同次材料；未预做ScenarioEvidencePreflight、三过程对照或SUPPORTS/COUNTERS。',
    revision_policy='S2新证据诱发的新预期/适用条件改变另起REVISED版本，保留本v1及修订原因；不得回写原预期。')
save('FrozenExpectationSet.json',frozen)
for p in pool['candidates']:
    used=[c['case_id'] for c in cs['cases'] if p['candidate_id'] in c['candidate_ids']]
    p['case_ids']=used
    p['status']='FROZEN_FOR_COMPARISON' if used else ('READY_FOR_EXPECTATION' if p['candidate_id']=='RAW-01' else 'CANDIDATE')
    p['selection_decision']='USED_IN_FROZEN_SET' if used else 'NOT_FROZEN_CURRENT_SCOPE'
    p['not_frozen_reason']=None if used else ('同类共同谷点已有区分代表；不以增加相似案例数量替代判断。' if p['candidate_id']=='RAW-01' else
        '保留为线索，未要求穷尽时期/分支或强造漏报；不将数据筛查自动提升为正式预期。')
pool['version']=2;pool['updated_at']=at;pool['state']='SELECTED_AND_FROZEN'
pool['previous_pool']='CandidateCasePool.v1.json'
pool['previous_pool_sha256']=sha((ROOT/'CandidateCasePool.v1.json').read_bytes())
save('CandidateCasePool.json',pool)
save('FREEZE_HISTORY.json',dict(case_set_id=cs['case_set_id'],version=1,events=[
    dict(state='CANDIDATE',at=pool['created_at'],source='CandidateCasePool.v1.json'),
    dict(state='READY_FOR_EXPECTATION',at=cs['prepared_at'],source='draft/CaseReviewSet.READY.json',check='DRAFT_VALIDATION.json'),
    dict(state='FROZEN_FOR_COMPARISON',at=at,source='FrozenExpectationSet.json')],
    unchanged_input_policy='原七条candidate-only索引/原问题队列/原HTML及正式21文件均不回写；仅本D候选在真实读取后提升。'))
names=['CaseReviewSet.json','ScenarioExpectationSet.json','FrozenExpectationSet.json','CandidateCasePool.json',
       'CaseMaterialIndex.json','CaseTypeCoverage.json','ObservationGapRequests.json','OpenQuestions.json','FREEZE_HISTORY.json']
save('FREEZE_MANIFEST.json',dict(frozen_set_id=frozen['frozen_set_id'],version=1,frozen_at=at,
    case_ids=frozen['case_ids'],files=[dict(file=n,bytes=(ROOT/n).stat().st_size,sha256=sha((ROOT/n).read_bytes())) for n in names],
    owner_approval_implied=False,evidence_comparison_performed=False))
print(json.dumps(dict(frozen_set=frozen['frozen_set_id'],version=1,cases=len(cs['cases']),expectations=len(es['expectations']),frozen_at=at),ensure_ascii=False))
