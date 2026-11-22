"""原schema/gate函数与本C真实I/D/Binding/已发布专业对象核验；不伪造controller。"""
from pathlib import Path
from hashlib import sha256
from datetime import datetime,timezone
import json
import runpy
import subprocess
RECORD=Path(__file__).resolve().parents[5]
RUN='OI-F800-STAT-20261122-01';CALL=RECORD/'longrun/runs'/RUN/'calls/C0027'
LOCAL=Path('/dwdhome/fy/BASE_E6_2_copy/artifacts')/RUN/'D012'
ADOPTED=Path('/dwdhome/fy/cgpterm/artifacts/wall-f-closure-20261122/adopted-observe-iterate')
PIN='87b951bbd15078a2d6353bdd24afe0d8f19c845c';RESULT='dfbc647030890fc8af80ac04a4d12a734d99f6dc'
def git(*a):return subprocess.check_output(['git',*a],cwd=RECORD)
def load(p):return json.loads(p.read_text())
assert git('branch','--show-current').decode().strip()=='codex/oi-f800-stat-20261122-01'
gate=ADOPTED/'longrun/tools/longrun_gate.py';schema=ADOPTED/'longrun/contracts/longrun_schema_v2.json'
gate_bytes=git('show',PIN+':longrun/tools/longrun_gate.py')
assert gate.read_bytes()==gate_bytes and sha256(gate_bytes).hexdigest()=='3355372ef1d9cbe3c4440bd6c3908a64827859d59bbdfe6bb9f9624c36aac7a7'
assert schema.read_bytes()==git('show',PIN+':longrun/contracts/longrun_schema_v2.json')
native=runpy.run_path(str(gate),run_name='pinned_return_contract')
packet=load(Path('/dwdhome/fy/cgpterm/artifacts/wall-f-closure-20261122')/RUN/'C0027-dispatch-packet.json')
d=load(Path(packet['delegation_json_path']));i=load(CALL/'INVOCATION.json');p=load(CALL/'PRO_RETURN.json')
binding=load(RECORD/'longrun/runs'/RUN/'RUN_BINDING.json')
assert git('show','3dc11a9dbf39e181b3c6a3051419a90e46b92aac:longrun/runs/'+RUN+'/RUN_BINDING.json')==(RECORD/'longrun/runs'/RUN/'RUN_BINDING.json').read_bytes()
for kind,value in [('binding',binding),('delegation',d),('invocation',i),('professional_return',p)]:native['validated'](kind,value)
native['pro_state'](p);native['object_ref_fields'](p)
assert p['run_id']==i['run_id']==d['run_id']==RUN and p['call_id']==i['call_id']=='C0027'
assert d==packet['delegation'] and i==packet['invocation'] and d['delegation_id']=='D012'
assert p['role']=='executor' and p['sender']==i['recipient']==d['recipient']
assert p['sender'] in binding['executors'] and p['return_to']==d['return_to']==d['issuer']==binding['manager']
assert p['delegation_ref']==packet['delegation_ref']==i['assignment_ref']
assert i['token']=='94493f76479c421d9e613ada8504c1f8'
assert d['permitted_operations']==['run_result_statistics_analysis_write','run_record_write']
assert set(d['permitted_operations'])<=set(g['operation'] for g in binding['grants'])
assert p['professional_state']=='REPORTED_COMPLETE' and all(p[k] is None for k in ['remaining_scope_ref','continuation_ref','owner_request_ref'])
assert not p['issued_delegation_refs'] and not p['issued_order_refs'] and not p['accepted_worker_refs'] and binding['workers']==[]
repo,commit,path=native['ref_parts'](p['result_ref'])
assert repo=='daowei2026/observe-iterate' and commit==RESULT and path=='longrun/runs/'+RUN+'/professional/D012/EXECUTOR_REPORT.md'
assert git('cat-file','-t',commit+':'+path).decode().strip()=='blob'
published=load(CALL/'PROFESSIONAL_PUBLICATION_READBACK.json')
assert published['commit']==RESULT and len(published['files'])==4 and all(x['local_git_blob_match'] for x in published['files'])
manifest=json.loads(git('show',RESULT+':longrun/runs/'+RUN+'/professional/D012/PROFESSIONAL_MANIFEST.json'))
for row in manifest['files']:
    raw=git('show',RESULT+':'+row['record_path'])
    assert sha256(raw).hexdigest()==row['sha256'] and Path(row['local_path']).read_bytes()==raw
M=load(LOCAL/'ObservationMaterialPackage.json');E=load(LOCAL/'CAEGraphExecutionResult.json');I=load(LOCAL/'INPUT_BINDING.json')
assert load(LOCAL/'VALIDATION.json')['completed'] and M['status']==E['阶段状态']=='DATA_READY'
assert E['stage_code']=='M-E' and E['未完成项']==E['阻塞项']==[]
assert load(LOCAL/'E3_ACCEPTANCE.json')['结果']=='接受' and load(LOCAL/'E5_DATA_CHECK.json')['结果']=='一致'
assert load(LOCAL/'E5_DATA_CHECK.json')['file_count']==21 and len(load(LOCAL/'FORMAL_GRAPH_DATA.json')['formal_files'])==21
assert load(LOCAL/'E4_ADMISSION.json')['E3_acceptance_sha256']==sha256((LOCAL/'E3_ACCEPTANCE.json').read_bytes()).hexdigest()
assert load(LOCAL/'RUN_ATTEMPT01.json')['exit_code']==load(LOCAL/'RUN_ATTEMPT02.json')['exit_code']==0
assert I['frp']=='39f02ec4548e68ba8dbd30061afc870546000994' and I['tis']=='2f460d663d821cf2ba25555eda13e78b697d0767'
assert I['configuration_sha256']=='b72095ff100da926474701b74bff7586a74b9770bc81cadc34c23cfe223e5cb3' and I['exact_source_count']==73
assert I['permitted_operations']==d['permitted_operations'] and not I['formal_feature_production']
assert not M['business_expectation_frozen'] and not M['FeatureReleaseGate_or_ReleasePackage'] and M['workers']==[]
assert sha256(Path(M['final_html_local_path']).read_bytes()).hexdigest()==M['final_html_sha256']
for f in load(LOCAL/'FORMAL_GRAPH_DATA.json')['formal_files']:assert sha256((LOCAL/f['file']).read_bytes()).hexdigest()==f['gzip_sha256']
changes=git('diff','--name-only','-z','df7184295277c8dfa60f4664635d32194437e87b',RESULT).decode().rstrip('\0').split('\0')
assert changes and all(x.startswith('longrun/runs/'+RUN+'/professional/D012/') for x in changes)
for old_d,old_commit,names in [('D008','d4f9fefaa67f9f22f540fa35a7da79cbbdf831ca',
    ['CurrentFeatureUnderstandingPackage.json','FeatureRunResultBinding.json','GlobalProfileGate.json','FindingDisposition.json','ScenarioQuestionQueue.json','CandidateCaseIndex.json']),
  ('D009','4d429ccb310452467b78b09802c48c9adbc47be5',['ObservationPositionPreparationResult.json','OrdinaryPositions.json','PositionSourceAlignment.json']),
  ('D010','ec747f4d460956bd1a91f59d0dcbaba6722ce750',['CAEGraphDisplayPreparationResult.json','C2_CURRENT_EXPECTATION.json','html/current.html','display_code/caegraph_display.py']),
  ('D011','c19db65f5b7e228d1db4be61d06e361c16bafa33',['CAEGraphDefinitionIntegrationResult.json','PROFESSIONAL_MANIFEST.json','run_definition.py','definition/f800_definition.py','definition/caegraph_display.py'])]:
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
 completion_boundary='仅D012原M-E E1至E6完整：真实最终图接受、E3之后E4导出21份同次CDS构图快照，E5一致，ObservationMaterialPackage DATA_READY。未重做U/X/G/B/C/D，未启动正式生产、未冻结场景预期或签Feature释放；原manager尚未消费，父Run未完成。')
(CALL/'RETURN_VALIDATION.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(schema_pass=True,pro_state_pass=True,actual_binding_pass=True,result_published_before_return=True,published_files=len(manifest['files'])),ensure_ascii=False))
