"""D009：只消费锁定当前输入，按原B Skill承接任务明确位置。"""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import csv,io,json,subprocess,uuid
ROOT=Path(__file__).resolve().parent
RECORD=Path('/dwdhome/fy/cgpterm/artifacts/wall-f-closure-20261122/OI-F800-STAT-20261122-01/executor-records')
RUN='OI-F800-STAT-20261122-01';COMMIT='d4f9fefaa67f9f22f540fa35a7da79cbbdf831ca'
PREFIX='longrun/runs/'+RUN+'/professional/D008/'
REF='daowei2026/observe-iterate@'+COMMIT+':'+PREFIX
SKILL='daowei2026/observe-iterate@87b951bbd15078a2d6353bdd24afe0d8f19c845c:skills/observation-material-preparation/observation-position-preparation/'
DREF='daowei2026/observe-iterate@fca115e5b5d128b08a79f10899d8412f9c8d36c6:longrun/runs/'+RUN+'/delegations/D009/DELEGATION.json'
BASEINPUT='daowei2026/observe-iterate@87b951bbd15078a2d6353bdd24afe0d8f19c845c:task-inputs/wall-f-parallel-closure-20261122/F_BASE_RUN_INPUT.md'
def raw(n):return subprocess.check_output(['git','show',COMMIT+':'+PREFIX+n],cwd=RECORD)
def load(n):return json.loads(raw(n))
def rows(n):return list(csv.DictReader(io.StringIO(raw(n).decode('utf-8-sig'))))
def write(n,v):(ROOT/n).write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
def exact(r,p):
 if int(r[p+'_idForm'])==1:return str(uuid.UUID(int=(int(r[p+'_idHigh'])<<64)|int(r[p+'_idLow'])))
 return r[p+'_idText']
B=load('FeatureRunResultBinding.json');U=load('CurrentFeatureUnderstandingPackage.json');cfg=load('configuration.json')
G=load('GlobalProfileGate.json');questions=load('ScenarioQuestionQueue.json');candidates=load('CandidateCaseIndex.json')
assert G['status']=='PASS_TO_SCENARIO_REVIEW'
assert B['code_version']['frp']=='daowei2026/frp@'+U['feature_ref']['code_version']['frp']=='daowei2026/frp@39f02ec4548e68ba8dbd30061afc870546000994'
assert B['code_version']['tis']=='daowei2026/tis@'+U['feature_ref']['code_version']['tis']=='daowei2026/tis@2f460d663d821cf2ba25555eda13e78b697d0767'
assert U['current_applicability']['current_code']==B['code_version']['frp']
assert B['parameter_version']==U['current_applicability']['parameter_version']==sha256(raw('configuration.json')).hexdigest()=='b72095ff100da926474701b74bff7586a74b9770bc81cadc34c23cfe223e5cb3'
scope=B['data_scope'];assert scope['symbols']==cfg['domain']['objects']==['rb','hc','i']
assert scope['start_time']=='2021-01-01' and scope['end_time']=='2023-12-31' and scope['freq']=='5m'
assert scope['sof']=='TA_updto20240229_DBA' and scope['stk_tlist']=='steel' and scope['calendar']=='night_end_at_2300'
assert cfg['profile']['observation_multiple']==800 and cfg['profile']['delta']==600 and cfg['profile']['unit']=='CalendarUTITick'
assert B['readback_validation']['all_31_tables_equal'] and B['readback_validation']['independent_process']
assert U['completion_status']=='PARTIAL'
sof=dict(sof_name=scope['sof'],stk_tlist=scope['stk_tlist'],calendar=scope['calendar'],sampling=scope['freq'],
 instance_ref=REF+'FeatureRunResultBinding.json',sof_ref=REF+'FeatureRunResultBinding.json#data_scope',
 parameter_instance_ref=REF+'configuration.json',parameter_version=B['parameter_version'],code_version=B['code_version'],
 full_result_dir=B['result_identity']['full_dir'],fields_sha256=B['result_identity']['fields_sha256'])
limits=['开始/结束保留原任务日期粒度，结束边界解释由后续D的日历/PlotSet绑定确定；B未改成新的时间边界。',
 '原CandidateCaseIndex的点/段及相关对象保持来源身份，尚非图上正式案例；不在B追加典型位置算法或扩窗。',
 '继承PARTIAL共享理解：内部逐Tick全部轨迹未暴露及800的业务场景解释边界保留；不妨碍本B明确品种/范围。',
 'Q共享适配影响及其独立数值边界限制仍由原输入传递，本B不运行或放行Q/V。']
position={'position_id':'F800-MB-D009-P001','SOF 引用':sof['sof_ref'],'品种集':scope['symbols'],
 '开始时间':scope['start_time'],'结束时间':scope['end_time'],'位置来源':'任务明确指定','采样':scope['freq'],
 '日历引用':REF+'FeatureRunResultBinding.json#data_scope/calendar','缺口与限制':limits}
result={'stage_code':'M-B','run_id':RUN,'call_id':'C0021','delegation_id':'D009','位置用法':'任务明确指定',
 '普通位置或多尺度位置路径':{'类型':'普通位置','普通位置':[position]},'特征实例与 SOF 引用':sof,
 'FeatureUnderstandingPackage 引用':REF+'CurrentFeatureUnderstandingPackage.json',
 '来源说明':{'明确任务位置来源':[BASEINPUT+'#4',DREF,REF+'FeatureRunResultBinding.json#data_scope'],
  '优先级依据':[SKILL+'SKILL.md#输入概览',SKILL+'WORKFLOW.md#2',SKILL+'IO_SPEC.md#1'],
  '默认位置处理':'本任务已经明确rb/hc/i和2021—2023，采用明确输入；不将未指定位置时的2021—2022默认范围覆盖该输入。',
  '多尺度处理':'本任务位置直接按品种集和起止日期承接；没有生成或要求1d→30m→1m→5s→tick节点链，不启用高频多尺度用法。',
  '既有候选来源':{'question_queue_ref':REF+'ScenarioQuestionQueue.json','candidate_index_ref':REF+'CandidateCaseIndex.json',
   'preservation':'四问题和七候选全部保留来源；候选点只作原索引来源和范围对齐，不升级为B选择的新正式案例。',
   'source_alignment_ref':'PositionSourceAlignment.json'}},
 '未完成位置':[],'阶段状态':'完整'}
write('ObservationPositionPreparationResult.json',result)
write('OrdinaryPositions.json',{'位置用法':result['位置用法'],'位置定义':[position],
 '特征实例与 SOF 引用':sof,'FeatureUnderstandingPackage 引用':result['FeatureUnderstandingPackage 引用']})
# 只核现有候选的来源坐标，不重新选点或做业务对照。
qmap={q['question_id']:q for q in questions};assert len(qmap)==4 and len(candidates)==7
fields=['timestamp','occurrence','record_id','child_id_2'];occur={tuple(r[k] for k in fields):r for r in rows('readback/tables/occurrences.csv')}
turns={r['turn_id']:r for r in rows('profile/scale_turns.csv')}
alignment=[]
for c in candidates:
 assert c['source_finding_or_question_id'] in qmap and c['candidate_only'] is True
 assert set(c['symbol'])<=set(scope['symbols']) and scope['start_time']<=c['start_time'][:10]<=c['end_time'][:10]<=scope['end_time']
 checks=[]
 for event in c['related_events']:
  if 'parent_coordinates' in event:
   r=occur[tuple(event['parent_coordinates'][k] for k in fields)]
   assert event['life']==exact(r,'groupReference_referenceLife') and event['revision']==exact(r,'groupReference_referenceRevision')
   assert event['timestamp']==r['timestamp'] and int(event['known_uti'])==int(float(r['groupKnownFrom']))
   checks.append({'kind':'当前F公开观点坐标与exact','source_ref':REF+'readback/tables/occurrences.csv','parent_coordinates':event['parent_coordinates'],'life':event['life'],'revision':event['revision'],'known_uti':event['known_uti']})
  else:
   t=turns[event['turn_id']]
   assert event['actual_ts']==t['actual_ts'] and event['known_ts']==t['known_ts']
   checks.append({'kind':'当前上游指定尺度位置及actual/known','source_ref':REF+'profile/scale_turns.csv','turn_id':event['turn_id'],'actual_ts':event['actual_ts'],'known_ts':event['known_ts']})
 alignment.append(dict(source_candidate_id=c['case_candidate_id'],source_question_id=c['source_finding_or_question_id'],
  priority=qmap[c['source_finding_or_question_id']]['priority'],symbols=c['symbol'],start_time=c['start_time'],end_time=c['end_time'],
  original_object_ids=c['object_ids'],source_candidate_ref=REF+'CandidateCaseIndex.json#'+c['case_candidate_id'],
  source_question_ref=REF+'ScenarioQuestionQueue.json#'+c['source_finding_or_question_id'],
  within_position_id=position['position_id'],object_scope_match=True,time_scope_match=True,location_source_match=True,checks=checks,
  remains_candidate_only=True,not_a_formal_selected_case=True))
write('PositionSourceAlignment.json',dict(binding_ref=REF+'FeatureRunResultBinding.json',question_queue_ref=REF+'ScenarioQuestionQueue.json',
 candidate_index_ref=REF+'CandidateCaseIndex.json',role='输入来源和范围/坐标对齐，非新增案例选择或业务判断',questions=[dict(question_id=q['question_id'],priority=q['priority'],status=q['status']) for q in questions],
 candidates=alignment,source_candidates=7,source_questions=4,all_match=True,same_tick_policy='同刻不同对象/观点保留原exact与父坐标；未合并候选或修改位置关系。'))
write('INPUT_BINDING.json',dict(checked_at=datetime.now(timezone.utc).isoformat(),delegation_ref=DREF,
 feature_instance=sof,understanding_ref=result['FeatureUnderstandingPackage 引用'],understanding_status=U['completion_status'],
 current_applicability_match=True,global_profile_gate_ref=REF+'GlobalProfileGate.json',global_profile_gate=G['status'],
 existing_X_G_valid=True,formal_feature_run_in_D009=False,global_statistics_rerun_in_D009=False,feature_semantics_reinvestigated=False,
 observed_input_refs=[REF+n for n in ['FeatureRunResultBinding.json','CurrentFeatureUnderstandingPackage.json','configuration.json','GlobalProfileGate.json','ScenarioQuestionQueue.json','CandidateCaseIndex.json']],
 bounded_alignment_sources=[REF+'readback/tables/occurrences.csv',REF+'profile/scale_turns.csv'],
 native_result_reuse_scope='只沿用已接受D008结果作B输入，非新X复用验收或重新生产/统计。',
 heavy_resource_policy='本D无重型生产或共享缓存/数据库写入，不请求生产flock、不声称持锁；只写BASE/D009及授权Run记录。'))
print('B explicit ordinary position prepared; 4 questions / 7 existing source candidates aligned; no Feature or G executed')
