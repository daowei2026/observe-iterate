"""按锁定B原合同核对位置、来源、当前适用绑定和本D完成边界。"""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import json,subprocess
ROOT=Path(__file__).resolve().parent
RECORD=Path('/dwdhome/fy/cgpterm/artifacts/wall-f-closure-20261122/OI-F800-STAT-20261122-01/executor-records')
def load(n):return json.loads((ROOT/n).read_text())
result=load('ObservationPositionPreparationResult.json');ordinary=load('OrdinaryPositions.json');inp=load('INPUT_BINDING.json');align=load('PositionSourceAlignment.json')
assert all(k in result for k in ['位置用法','普通位置或多尺度位置路径','特征实例与 SOF 引用','FeatureUnderstandingPackage 引用','来源说明','未完成位置','阶段状态'])
assert result['stage_code']=='M-B' and result['阶段状态']=='完整' and result['未完成位置']==[]
assert result['位置用法']=='任务明确指定'
pos=result['普通位置或多尺度位置路径']['普通位置'];assert len(pos)==1 and ordinary['位置定义']==pos
p=pos[0]
assert all(k in p for k in ['SOF 引用','品种集','开始时间','结束时间','位置来源','缺口与限制'])
assert p['品种集']==['rb','hc','i'] and p['开始时间']=='2021-01-01' and p['结束时间']=='2023-12-31' and p['位置来源']=='任务明确指定'
assert result['特征实例与 SOF 引用']==ordinary['特征实例与 SOF 引用']==inp['feature_instance']
assert inp['feature_instance']['sof_name']=='TA_updto20240229_DBA' and inp['feature_instance']['calendar']=='night_end_at_2300' and inp['feature_instance']['sampling']=='5m'
assert result['FeatureUnderstandingPackage 引用']==inp['understanding_ref'] and inp['current_applicability_match']
assert inp['understanding_status']=='PARTIAL' and inp['global_profile_gate']=='PASS_TO_SCENARIO_REVIEW'
assert inp['formal_feature_run_in_D009'] is False and inp['global_statistics_rerun_in_D009'] is False and inp['feature_semantics_reinvestigated'] is False
assert align['source_candidates']==len(align['candidates'])==7 and align['source_questions']==len(align['questions'])==4
assert {x['question_id']:x['priority'] for x in align['questions']}=={'F800-SQ-001':'HIGH','F800-SQ-002':'MEDIUM','F800-SQ-003':'HIGH','F800-SQ-004':'MEDIUM'}
assert len({x['source_candidate_id'] for x in align['candidates']})==7
for x in align['candidates']:
 assert x['object_scope_match'] and x['time_scope_match'] and x['location_source_match'] and x['checks']
 assert x['remains_candidate_only'] and x['not_a_formal_selected_case'] and x['start_time']<=x['end_time']
 assert x['within_position_id']==p['position_id'] and x['source_candidate_ref'].startswith('daowei2026/observe-iterate@d4f9fefaa67f9f22f540fa35a7da79cbbdf831ca:')
audit=load('SOURCE_REF_AUDIT.json');assert audit['exact_objects_available'] and audit['packet_invocation_equal'] and audit['owner_original_byte_equal'] and all(x['local_current_equal'] for x in audit['rows'])
remote=load('REMOTE_DISPATCH_READBACK.json');assert remote['completed'] and all(x['byte_equal'] for x in remote['rows'])
# 当前绑定依据精确原件；不重新加载Feature、重跑X/G或重做语义。
for path in ['CurrentFeatureUnderstandingPackage.json','FeatureRunResultBinding.json','GlobalProfileGate.json','ScenarioQuestionQueue.json','CandidateCaseIndex.json','FindingDisposition.json']:
 rel='longrun/runs/OI-F800-STAT-20261122-01/professional/D008/'+path
 data=subprocess.check_output(['git','show','d4f9fefaa67f9f22f540fa35a7da79cbbdf831ca:'+rel],cwd=RECORD)
 assert data==(RECORD/rel).read_bytes()
checks=[dict(item='原IO阶段最终输出字段',result='PASS',evidence='ObservationPositionPreparationResult.json'),
 dict(item='沿明确任务位置、原SOF和当前实例版本；未以默认2021—2022缩短',result='PASS',evidence='OrdinaryPositions.json; INPUT_BINDING.json'),
 dict(item='与当前U对象范围及事件位置一致；四问题/七候选原来源对齐',result='PASS',evidence='PositionSourceAlignment.json'),
 dict(item='候选只保留来源，不替代图上正式场景选择或冻结预期',result='PASS',evidence='PositionSourceAlignment.json; 原B Skill定位'),
 dict(item='D008有效U/X/G及历史原件未更改；本D未重新生产/统计/查Feature语义',result='PASS',evidence='SOURCE_REF_AUDIT.json; INPUT_BINDING.json')]
validation=dict(completed=True,verified_at=datetime.now(timezone.utc).isoformat(),stage_code='M-B',stage_status='完整',
 checks=checks,uncompleted_positions=[],source_candidates_preserved=7,ordinary_positions=1,workers=[],
 original_io_field_mapping={'位置用法':'ObservationPositionPreparationResult.json#位置用法','普通位置或多尺度位置路径':'OrdinaryPositions.json#位置定义',
 '特征实例与 SOF 引用':'INPUT_BINDING.json#feature_instance','FeatureUnderstandingPackage 引用':'INPUT_BINDING.json#understanding_ref','来源说明':'ObservationPositionPreparationResult.json#来源说明','未完成位置':'ObservationPositionPreparationResult.json#未完成位置','阶段状态':'ObservationPositionPreparationResult.json#阶段状态'},
 completion_boundary='只完成M-B普通任务明确位置。未形成M-C展示、M-D完整定义、M-E图/正式图数据或ObservationMaterialPackage；未选择正式CaseReviewSet、未冻结预期，未签FeatureReleaseGate/ReleasePackage或启动Q/V/WALL。',
 next_route='原manager消费B后，按既有M-C/M-D/M-E依赖衔接；B可供D绑定不表示C或D已委派或PLAN_READY/DATA_READY。')
(ROOT/'VALIDATION.json').write_text(json.dumps(validation,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(completed=True,stage_status='完整',ordinary_positions=1,source_candidates_preserved=7,checks=len(checks)),ensure_ascii=False))
