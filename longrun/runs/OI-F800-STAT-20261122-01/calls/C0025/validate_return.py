"""原schema/gate函数与本C真实I/D/Binding/已发布专业对象核验；不伪造controller。"""
from pathlib import Path
from hashlib import sha256
from datetime import datetime,timezone
import json
import runpy
import subprocess
RECORD=Path(__file__).resolve().parents[5]
RUN='OI-F800-STAT-20261122-01';CALL=RECORD/'longrun/runs'/RUN/'calls/C0025'
LOCAL=Path('/dwdhome/fy/BASE_E6_2_copy/artifacts')/RUN/'D011'
ADOPTED=Path('/dwdhome/fy/cgpterm/artifacts/wall-f-closure-20261122/adopted-observe-iterate')
PIN='87b951bbd15078a2d6353bdd24afe0d8f19c845c';RESULT='c19db65f5b7e228d1db4be61d06e361c16bafa33'
def git(*a):return subprocess.check_output(['git',*a],cwd=RECORD)
def load(p):return json.loads(p.read_text())
assert git('branch','--show-current').decode().strip()=='codex/oi-f800-stat-20261122-01'
gate=ADOPTED/'longrun/tools/longrun_gate.py';schema=ADOPTED/'longrun/contracts/longrun_schema_v2.json'
gate_bytes=git('show',PIN+':longrun/tools/longrun_gate.py')
assert gate.read_bytes()==gate_bytes and sha256(gate_bytes).hexdigest()=='3355372ef1d9cbe3c4440bd6c3908a64827859d59bbdfe6bb9f9624c36aac7a7'
assert schema.read_bytes()==git('show',PIN+':longrun/contracts/longrun_schema_v2.json')
native=runpy.run_path(str(gate),run_name='pinned_return_contract')
packet=load(Path('/dwdhome/fy/cgpterm/artifacts/wall-f-closure-20261122')/RUN/'C0025-dispatch-packet.json')
d=load(Path(packet['delegation_json_path']));i=load(CALL/'INVOCATION.json');p=load(CALL/'PRO_RETURN.json')
binding=load(RECORD/'longrun/runs'/RUN/'RUN_BINDING.json')
assert git('show','3dc11a9dbf39e181b3c6a3051419a90e46b92aac:longrun/runs/'+RUN+'/RUN_BINDING.json')==(RECORD/'longrun/runs'/RUN/'RUN_BINDING.json').read_bytes()
for kind,value in [('binding',binding),('delegation',d),('invocation',i),('professional_return',p)]:native['validated'](kind,value)
native['pro_state'](p);native['object_ref_fields'](p)
assert p['run_id']==i['run_id']==d['run_id']==RUN and p['call_id']==i['call_id']=='C0025'
assert d==packet['delegation'] and i==packet['invocation'] and d['delegation_id']=='D011'
assert p['role']=='executor' and p['sender']==i['recipient']==d['recipient']
assert p['sender'] in binding['executors'] and p['return_to']==d['return_to']==d['issuer']==binding['manager']
assert p['delegation_ref']==packet['delegation_ref']==i['assignment_ref']
assert i['token']=='d81f7b4a5f754457a062ebbf1a162cb9'
assert d['permitted_operations']==['run_result_statistics_analysis_write','run_record_write']
assert set(d['permitted_operations'])<=set(g['operation'] for g in binding['grants'])
assert p['professional_state']=='REPORTED_COMPLETE' and all(p[k] is None for k in ['remaining_scope_ref','continuation_ref','owner_request_ref'])
assert not p['issued_delegation_refs'] and not p['issued_order_refs'] and not p['accepted_worker_refs'] and binding['workers']==[]
repo,commit,path=native['ref_parts'](p['result_ref'])
assert repo=='daowei2026/observe-iterate' and commit==RESULT and path=='longrun/runs/'+RUN+'/professional/D011/EXECUTOR_REPORT.md'
assert git('cat-file','-t',commit+':'+path).decode().strip()=='blob'
published=load(CALL/'PROFESSIONAL_PUBLICATION_READBACK.json')
assert published['commit']==RESULT and len(published['files'])==4 and all(x['local_git_blob_match'] for x in published['files'])
manifest=json.loads(git('show',RESULT+':longrun/runs/'+RUN+'/professional/D011/PROFESSIONAL_MANIFEST.json'))
for row in manifest['files']:
    raw=git('show',RESULT+':'+row['record_path'])
    assert sha256(raw).hexdigest()==row['sha256'] and Path(row['local_path']).read_bytes()==raw
D=load(LOCAL/'CAEGraphDefinitionIntegrationResult.json');I=load(LOCAL/'INPUT_BINDING.json')
assert load(LOCAL/'VALIDATION.json')['completed'] and D['阶段状态']=='完整' and D['未完成项']==D['阻塞项']==[]
assert D['阶段']=='M-D' and D['定义编号与版本']=='F800-D-v1'
checks=load(LOCAL/'DEFINITION_CHECKS.json')
assert checks['all_passed'] and len(checks['checks'])==10 and checks['native_feature_run_calls']==0
assert not checks['final_graph_built'] and not checks['html_generated'] and not checks['formal_graph_data_extracted']
assert I['current_frp']=='39f02ec4548e68ba8dbd30061afc870546000994' and I['current_tis']=='2f460d663d821cf2ba25555eda13e78b697d0767'
assert I['configuration_sha256']=='b72095ff100da926474701b74bff7586a74b9770bc81cadc34c23cfe223e5cb3'
assert I['permitted_operations']==d['permitted_operations'] and I['source_count']==64
assert load(LOCAL/'DEFINITION_INTEGRATION_RECORD.json')['C3→D代码差异']['C3_renderer_byte_equal']
assert load(LOCAL/'UPSTREAM_CORRECTIONS.json')['返回共享理解问题']==[]
assert load(LOCAL/'UPSTREAM_CORRECTIONS.json')['返回B问题']==load(LOCAL/'UPSTREAM_CORRECTIONS.json')['返回C问题']==[]
assert not Path(D['预期输出HTML路径']).exists()
changes=git('diff','--name-only','-z','9cd294ffc80bba7ebdbe8bb2889eb1bb77e826d2',RESULT).decode().rstrip('\0').split('\0')
assert changes and all(x.startswith('longrun/runs/'+RUN+'/professional/D011/') for x in changes)
for old_d,old_commit,names in [('D008','d4f9fefaa67f9f22f540fa35a7da79cbbdf831ca',
    ['CurrentFeatureUnderstandingPackage.json','FeatureRunResultBinding.json','GlobalProfileGate.json','FindingDisposition.json','ScenarioQuestionQueue.json','CandidateCaseIndex.json']),
  ('D009','4d429ccb310452467b78b09802c48c9adbc47be5',['ObservationPositionPreparationResult.json','OrdinaryPositions.json','PositionSourceAlignment.json']),
  ('D010','ec747f4d460956bd1a91f59d0dcbaba6722ce750',['CAEGraphDisplayPreparationResult.json','C2_CURRENT_EXPECTATION.json','html/current.html','display_code/caegraph_display.py'])]:
    for name in names:
        oldpath='longrun/runs/'+RUN+'/professional/'+old_d+'/'+name
        assert git('show',old_commit+':'+oldpath)==(RECORD/oldpath).read_bytes()
audit=dict(verified_at=datetime.now(timezone.utc).isoformat(),schema_pass=True,pro_state_pass=True,immutable_refs_pass=True,
 actual_invocation_delegation_binding_pass=True,workers_empty=True,professional_state=p['professional_state'],
 result_ref=p['result_ref'],result_published_before_return=True,professional_publication=published,published_manifest_files_verified=len(manifest['files']),
 pinned_gate_ref='daowei2026/observe-iterate@'+PIN+':longrun/tools/longrun_gate.py',gate_sha256=sha256(gate_bytes).hexdigest(),
 pinned_schema_sha256=sha256(schema.read_bytes()).hexdigest(),return_sha256=sha256((CALL/'PRO_RETURN.json').read_bytes()).hexdigest(),
 validated_functions=['validated(binding/delegation/invocation/professional_return)','pro_state','object_ref_fields'],
 full_cli_validation='未运行完整validate-executor-return：该版binding()将manager硬编码为chatgpt，与本Run采用Codex manager不兼容。原gate未修改，未伪造独立controller receipt。',
 completion_boundary='仅D011原M-D单一集成职责完整：真实实例/完整B位置/字段进入完整定义，10项定义检查通过；C3与C2语义保持，三项确定性补齐留痕。未重做U/X/G/B/C，未运行最终图/原生reader/HTML或正式图数据，未代E/S1/S2、未签材料DATA_READY或Feature释放；原manager尚未消费。')
(CALL/'RETURN_VALIDATION.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(schema_pass=True,pro_state_pass=True,actual_binding_pass=True,result_published_before_return=True,published_files=len(manifest['files'])),ensure_ascii=False))
