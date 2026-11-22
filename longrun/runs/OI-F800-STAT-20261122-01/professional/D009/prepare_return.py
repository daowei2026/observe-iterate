"""D009专业结果已发布读回后，形成C0021原V2 Return及不改原gate的校验脚本。"""
from pathlib import Path
import argparse,json

ROOT=Path(__file__).resolve().parent
RECORD=Path('/dwdhome/fy/cgpterm/artifacts/wall-f-closure-20261122/OI-F800-STAT-20261122-01/executor-records')
RUN='OI-F800-STAT-20261122-01'
CALL=RECORD/'longrun/runs'/RUN/'calls/C0021'
parser=argparse.ArgumentParser();parser.add_argument('--result-commit',required=True);args=parser.parse_args()
RESULT=args.result_commit;assert len(RESULT)==40
published=json.loads((CALL/'PROFESSIONAL_PUBLICATION_READBACK.json').read_text())
assert published['commit']==RESULT and len(published['files'])==4 and all(x['local_git_blob_match'] for x in published['files'])
value=dict(schema='longrun-professional-return/v2',run_id=RUN,call_id='C0021',role='executor',
 sender='codex:'+RUN+':executor:E1',
 delegation_ref='daowei2026/observe-iterate@fca115e5b5d128b08a79f10899d8412f9c8d36c6:longrun/runs/'+RUN+'/delegations/D009/DELEGATION.json',
 return_to='codex:'+RUN+':manager',
 result_ref='daowei2026/observe-iterate@'+RESULT+':longrun/runs/'+RUN+'/professional/D009/EXECUTOR_REPORT.md',
 issued_delegation_refs=[],issued_order_refs=[],accepted_worker_refs=[],professional_state='REPORTED_COMPLETE',
 remaining_scope_ref=None,continuation_ref=None,owner_request_ref=None)
(CALL/'PRO_RETURN.json').write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n')
template='''"""未改锁定schema/gate函数 + C0021真实I/D/Binding及已发布D009结果核对。"""
from pathlib import Path
from hashlib import sha256
from datetime import datetime,timezone
import json,runpy,subprocess
RECORD=Path(__file__).resolve().parents[5]
RUN='OI-F800-STAT-20261122-01'
CALL=RECORD/'longrun/runs'/RUN/'calls/C0021'
LOCAL=Path('/dwdhome/fy/BASE_E6_2_copy/artifacts')/RUN/'D009'
ADOPTED=Path('/dwdhome/fy/cgpterm/artifacts/wall-f-closure-20261122/adopted-observe-iterate')
PIN='87b951bbd15078a2d6353bdd24afe0d8f19c845c'
RESULT='__RESULT__'
def git(*args):return subprocess.check_output(['git',*args],cwd=RECORD)
def load(p):return json.loads(p.read_text())
assert git('branch','--show-current').decode().strip()=='codex/oi-f800-stat-20261122-01'
gate=ADOPTED/'longrun/tools/longrun_gate.py';schema=ADOPTED/'longrun/contracts/longrun_schema_v2.json'
gate_bytes=git('show',PIN+':longrun/tools/longrun_gate.py')
assert gate.read_bytes()==gate_bytes and sha256(gate_bytes).hexdigest()=='3355372ef1d9cbe3c4440bd6c3908a64827859d59bbdfe6bb9f9624c36aac7a7'
assert schema.read_bytes()==git('show',PIN+':longrun/contracts/longrun_schema_v2.json')
native=runpy.run_path(str(gate),run_name='pinned_return_contract')
packet=load(Path('/dwdhome/fy/cgpterm/artifacts/wall-f-closure-20261122')/RUN/'C0021-dispatch-packet.json')
d=load(Path(packet['delegation_json_path']));i=load(CALL/'INVOCATION.json');p=load(CALL/'PRO_RETURN.json')
binding=load(RECORD/'longrun/runs'/RUN/'RUN_BINDING.json')
assert git('show','3dc11a9dbf39e181b3c6a3051419a90e46b92aac:longrun/runs/'+RUN+'/RUN_BINDING.json')==(RECORD/'longrun/runs'/RUN/'RUN_BINDING.json').read_bytes()
for kind,value in [('binding',binding),('delegation',d),('invocation',i),('professional_return',p)]:native['validated'](kind,value)
native['pro_state'](p);native['object_ref_fields'](p)
assert p['run_id']==i['run_id']==d['run_id']==RUN and p['call_id']==i['call_id']=='C0021'
assert d==packet['delegation'] and i==packet['invocation'] and d['delegation_id']=='D009'
assert p['role']=='executor' and p['sender']==i['recipient']==d['recipient']
assert p['sender'] in binding['executors'] and p['return_to']==d['return_to']==d['issuer']==binding['manager']
assert p['delegation_ref']==packet['delegation_ref']==i['assignment_ref']
assert set(d['permitted_operations'])<=set(g['operation'] for g in binding['grants'])
assert d['permitted_operations']==['run_result_statistics_analysis_write','run_record_write']
assert p['professional_state']=='REPORTED_COMPLETE' and all(p[k] is None for k in ['remaining_scope_ref','continuation_ref','owner_request_ref'])
assert not p['issued_delegation_refs'] and not p['issued_order_refs'] and not p['accepted_worker_refs'] and binding['workers']==[]
repo,commit,path=native['ref_parts'](p['result_ref'])
assert repo=='daowei2026/observe-iterate' and commit==RESULT and path=='longrun/runs/'+RUN+'/professional/D009/EXECUTOR_REPORT.md'
assert git('cat-file','-t',commit+':'+path).decode().strip()=='blob'
published=load(CALL/'PROFESSIONAL_PUBLICATION_READBACK.json')
assert published['commit']==RESULT and len(published['files'])==4 and all(x['local_git_blob_match'] for x in published['files'])
manifest=json.loads(git('show',RESULT+':longrun/runs/'+RUN+'/professional/D009/PROFESSIONAL_MANIFEST.json'))
for row in manifest['files']:
    raw=git('show',RESULT+':'+row['record_path'])
    assert sha256(raw).hexdigest()==row['sha256'] and Path(row['local_path']).read_bytes()==raw
B=load(LOCAL/'ObservationPositionPreparationResult.json');I=load(LOCAL/'INPUT_BINDING.json')
assert load(LOCAL/'VALIDATION.json')['completed'] and B['阶段状态']=='完整' and B['未完成位置']==[]
assert B['位置用法']=='任务明确指定' and B['stage_code']=='M-B'
pos=B['普通位置或多尺度位置路径']['普通位置'];assert len(pos)==1
assert pos[0]['品种集']==['rb','hc','i'] and pos[0]['开始时间']=='2021-01-01' and pos[0]['结束时间']=='2023-12-31'
assert I['feature_instance']['code_version']['frp']=='daowei2026/frp@39f02ec4548e68ba8dbd30061afc870546000994'
assert I['current_applicability_match'] and I['understanding_status']=='PARTIAL'
assert not I['formal_feature_run_in_D009'] and not I['global_statistics_rerun_in_D009'] and not I['feature_semantics_reinvestigated']
assert load(LOCAL/'PositionSourceAlignment.json')['all_match']
assert len(load(LOCAL/'PositionSourceAlignment.json')['candidates'])==7
changes=git('diff','--name-only','073edebe66bdc1592fdb62e47ca34c1258447403',RESULT).decode().splitlines()
assert changes and all(x.startswith('longrun/runs/'+RUN+'/professional/D009/') for x in changes)
for name in ['CurrentFeatureUnderstandingPackage.json','FeatureRunResultBinding.json','GlobalProfileGate.json','FindingDisposition.json','ScenarioQuestionQueue.json','CandidateCaseIndex.json']:
    oldpath='longrun/runs/'+RUN+'/professional/D008/'+name
    assert git('show','d4f9fefaa67f9f22f540fa35a7da79cbbdf831ca:'+oldpath)==(RECORD/oldpath).read_bytes()
audit=dict(verified_at=datetime.now(timezone.utc).isoformat(),schema_pass=True,pro_state_pass=True,immutable_refs_pass=True,
 actual_invocation_delegation_binding_pass=True,workers_empty=True,professional_state=p['professional_state'],
 result_ref=p['result_ref'],result_published_before_return=True,professional_publication=published,published_manifest_files_verified=len(manifest['files']),
 pinned_gate_ref='daowei2026/observe-iterate@'+PIN+':longrun/tools/longrun_gate.py',gate_sha256=sha256(gate_bytes).hexdigest(),
 pinned_schema_sha256=sha256(schema.read_bytes()).hexdigest(),return_sha256=sha256((CALL/'PRO_RETURN.json').read_bytes()).hexdigest(),
 validated_functions=['validated(binding/delegation/invocation/professional_return)','pro_state','object_ref_fields'],
 full_cli_validation='未运行完整validate-executor-return：该版binding()将manager硬编码为chatgpt，与本Run采用Codex manager不兼容。原gate未修改，未伪造独立controller receipt。',
 completion_boundary='D009只完成当前39f实例的M-B任务明确位置：rb/hc/i、2021—2023、原SOF/日历及当前U引用，四问题和七候选保留原来源。没有重做U/X/G、没有正式场景选择或冻结预期，没有M-C/D/E或ObservationMaterialPackage，没有Feature释放/Q/V/WALL变更；manager尚未消费本回交。')
(CALL/'RETURN_VALIDATION.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\\n')
print(json.dumps(dict(schema_pass=True,pro_state_pass=True,actual_binding_pass=True,result_published_before_return=True,published_files=len(manifest['files'])),ensure_ascii=False))
'''
(CALL/'validate_return.py').write_text(template.replace('__RESULT__',RESULT))
(CALL/'EXECUTOR_REPORT.md').write_text(f"""# C0021｜D009原executor B位置回交

D009的M-B职责已完成，原生专业结果已先发布并远端读回：
`daowei2026/observe-iterate@{RESULT}:longrun/runs/{RUN}/professional/D009/EXECUTOR_REPORT.md`。

按锁定observation-position-preparation原Skill/WORKFLOW/IO_SPEC，直接采用任务明确rb/hc/i、5m、2021-01-01至2023-12-31及原TA_updto20240229_DBA/steel/night_end_at_2300，沿当前39f实例、参数和D008共享理解引用。原生阶段状态完整、未完成位置为空，普通位置可供后续D绑定，结束边界解释依原IO留D的Calendar/PlotSet。

四项问题和七候选保持原来源/优先级/开放状态，全部范围和对象/事件来源坐标核对匹配，保留同拍不同exact和父坐标；没有把候选索引升级正式场景集。没有新位置算法、多尺度节点、图层或业务预期；没有重做完整理解、有效X/G或改变正式行为。

原manager按既有M-C/M-D/M-E及适用S1/S2依赖衔接。本V2 REPORTED_COMPLETE只代表D009的B职责完成，不表示manager已消费、M材料已PLAN_READY/DATA_READY、Feature已释放或父Run业务完成。未运行/释放Q/V或改WALL，PARTIAL和既有Q限制继续传递。

未改原schema/gate。原validated/pro_state/object_ref_fields与真实I/D/最新Codex Binding、权限子集、先发布exact结果及全部清单产物核验见RETURN_VALIDATION；完整CLI的Codex manager兼容边界如实记录，未伪造controller物理receipt。
""")
print(CALL/'PRO_RETURN.json')
