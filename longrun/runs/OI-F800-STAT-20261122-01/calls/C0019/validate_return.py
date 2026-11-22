"""未改锁定schema/gate函数 + C0019真实I/D/Binding及已发布D008结果核对。"""
from pathlib import Path
from hashlib import sha256
from datetime import datetime,timezone
import json,runpy,subprocess
RECORD=Path(__file__).resolve().parents[5]
RUN='OI-F800-STAT-20261122-01'
CALL=RECORD/'longrun/runs'/RUN/'calls/C0019'
LOCAL=Path('/dwdhome/fy/BASE_E6_2_copy/artifacts')/RUN/'D008'
ADOPTED=Path('/dwdhome/fy/cgpterm/artifacts/wall-f-closure-20261122/adopted-observe-iterate')
PIN='87b951bbd15078a2d6353bdd24afe0d8f19c845c'
RESULT='d4f9fefaa67f9f22f540fa35a7da79cbbdf831ca'
def git(*args):return subprocess.check_output(['git',*args],cwd=RECORD)
def load(p):return json.loads(p.read_text())
assert git('branch','--show-current').decode().strip()=='codex/oi-f800-stat-20261122-01'
gate=ADOPTED/'longrun/tools/longrun_gate.py';schema=ADOPTED/'longrun/contracts/longrun_schema_v2.json'
gate_bytes=git('show',PIN+':longrun/tools/longrun_gate.py')
assert gate.read_bytes()==gate_bytes and sha256(gate_bytes).hexdigest()=='3355372ef1d9cbe3c4440bd6c3908a64827859d59bbdfe6bb9f9624c36aac7a7'
assert schema.read_bytes()==git('show',PIN+':longrun/contracts/longrun_schema_v2.json')
native=runpy.run_path(str(gate),run_name='pinned_return_contract')
packet=load(Path('/dwdhome/fy/cgpterm/artifacts/wall-f-closure-20261122')/RUN/'C0019-dispatch-packet.json')
d=load(Path(packet['delegation_json_path']));i=load(CALL/'INVOCATION.json');p=load(CALL/'PRO_RETURN.json')
binding=load(RECORD/'longrun/runs'/RUN/'RUN_BINDING.json')
assert git('show','3dc11a9dbf39e181b3c6a3051419a90e46b92aac:longrun/runs/'+RUN+'/RUN_BINDING.json')==(RECORD/'longrun/runs'/RUN/'RUN_BINDING.json').read_bytes()
for kind,value in [('binding',binding),('delegation',d),('invocation',i),('professional_return',p)]:native['validated'](kind,value)
native['pro_state'](p);native['object_ref_fields'](p)
assert p['run_id']==i['run_id']==d['run_id']==RUN and p['call_id']==i['call_id']=='C0019'
assert d==packet['delegation'] and i==packet['invocation'] and d['delegation_id']=='D008'
assert p['role']=='executor' and p['sender']==i['recipient']==d['recipient']
assert p['sender'] in binding['executors'] and p['return_to']==d['return_to']==d['issuer']==binding['manager']
assert p['delegation_ref']==packet['delegation_ref']==i['assignment_ref']
assert set(d['permitted_operations'])<=set(g['operation'] for g in binding['grants'])
assert d['permitted_operations']==['formal_feature_run','run_result_statistics_analysis_write','run_record_write']
assert p['professional_state']=='REPORTED_COMPLETE' and all(p[k] is None for k in ['remaining_scope_ref','continuation_ref','owner_request_ref'])
assert not p['issued_delegation_refs'] and not p['issued_order_refs'] and not p['accepted_worker_refs'] and binding['workers']==[]
repo,commit,path=native['ref_parts'](p['result_ref'])
assert repo=='daowei2026/observe-iterate' and commit==RESULT and path=='longrun/runs/'+RUN+'/professional/D008/EXECUTOR_REPORT.md'
assert git('cat-file','-t',commit+':'+path).decode().strip()=='blob'
published=load(CALL/'PROFESSIONAL_PUBLICATION_READBACK.json')
assert published['commit']==RESULT and len(published['files'])==4 and all(x['local_git_blob_match'] for x in published['files'])
manifest=json.loads(git('show',RESULT+':longrun/runs/'+RUN+'/professional/D008/PROFESSIONAL_MANIFEST.json'))
for row in manifest['files']:
    raw=git('show',RESULT+':'+row['record_path'])
    assert sha256(raw).hexdigest()==row['sha256'] and Path(row['local_path']).read_bytes()==raw
B=load(LOCAL/'FeatureRunResultBinding.json');G=load(LOCAL/'FeatureGlobalBehaviorProfilingResult.json')
assert load(LOCAL/'VALIDATION.json')['completed'] and load(LOCAL/'ANALYSIS_EXECUTION.json')['completed']
assert B['code_version']['frp']=='daowei2026/frp@39f02ec4548e68ba8dbd30061afc870546000994'
assert B['readback_validation']['all_31_tables_equal'] and B['readback_validation']['independent_process']
assert B['production']['native_producer_executed'] and B['production']['feature_python_exit_code']==0
assert all(x['completed'] for x in load(LOCAL/'WORKFLOW_COMPLETION.json')['steps'])
assert G['gate']==load(LOCAL/'GlobalProfileGate.json')
assert load(LOCAL/'NATIVE_RETEST_API.json')['completed']
assert load(LOCAL/'FindingDisposition.json')['all_prior_findings_closed']
changes=git('diff','--name-only','6d7e96322ac942116d0a474de05f7eef839454ef',RESULT).decode().splitlines()
assert changes and all(x.startswith('longrun/runs/'+RUN+'/professional/D008/') for x in changes)
for name in ['FeatureRunResultBinding.json','GlobalProfileGate.json','FindingDisposition.json','GlobalFindingCandidates.json']:
    oldpath='longrun/runs/'+RUN+'/professional/D005/'+name
    assert git('show','38e2af72be826a1e98fd7f5d4522c50d218750f3:'+oldpath)==(RECORD/oldpath).read_bytes()
src=Path('/dwdhome/fy/BASE_E6_2_copy/.runtime/f-observation-multiple-github-20261122/frp')
assert subprocess.check_output(['git','rev-parse','HEAD'],cwd=src,text=True).strip()=='39f02ec4548e68ba8dbd30061afc870546000994'
assert not subprocess.check_output(['git','status','--porcelain'],cwd=src)
audit=dict(verified_at=datetime.now(timezone.utc).isoformat(),schema_pass=True,pro_state_pass=True,immutable_refs_pass=True,
 actual_invocation_delegation_binding_pass=True,workers_empty=True,professional_state=p['professional_state'],
 result_ref=p['result_ref'],result_published_before_return=True,professional_publication=published,published_manifest_files_verified=len(manifest['files']),
 pinned_gate_ref='daowei2026/observe-iterate@'+PIN+':longrun/tools/longrun_gate.py',gate_sha256=sha256(gate_bytes).hexdigest(),
 pinned_schema_sha256=sha256(schema.read_bytes()).hexdigest(),return_sha256=sha256((CALL/'PRO_RETURN.json').read_bytes()).hexdigest(),
 validated_functions=['validated(binding/delegation/invocation/professional_return)','pro_state','object_ref_fields'],
 full_cli_validation='未运行完整validate-executor-return：该版binding()将manager硬编码为chatgpt，与本Run采用Codex manager不兼容。原gate未修改，未伪造独立controller receipt。',
 completion_boundary='D008已完成39f完整正式F-only三年新X、31表独立OnlyRead、全量G1-G8和38个历史位置原生AsOf复验；GF001/002完整复验见原生FindingDisposition与Gate。未代manager签FeatureReleaseGate或启动Q/V，未改WALL；manager尚未消费。')
(CALL/'RETURN_VALIDATION.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(schema_pass=True,pro_state_pass=True,actual_binding_pass=True,result_published_before_return=True,published_files=len(manifest['files'])),ensure_ascii=False))
