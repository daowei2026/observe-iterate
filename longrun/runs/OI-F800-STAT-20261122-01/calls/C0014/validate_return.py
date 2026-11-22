"""未改锁定schema/gate函数 + C0014真实I/D/Binding及已发布D006结果核对。"""
from pathlib import Path
from hashlib import sha256
from datetime import datetime,timezone
import json,runpy,subprocess
RECORD=Path(__file__).resolve().parents[5]
RUN='OI-F800-STAT-20261122-01'
CALL=RECORD/'longrun/runs'/RUN/'calls/C0014'
LOCAL=Path('/dwdhome/fy/BASE_E6_2_copy/artifacts')/RUN/'D006'
ADOPTED=Path('/dwdhome/fy/cgpterm/artifacts/wall-f-closure-20261122/adopted-observe-iterate')
PIN='87b951bbd15078a2d6353bdd24afe0d8f19c845c'
RESULT='46de903caa04be60a5600ef9f416445f5a6366cd'
def git(*args):return subprocess.check_output(['git',*args],cwd=RECORD)
def load(p):return json.loads(p.read_text())
assert git('branch','--show-current').decode().strip()=='codex/oi-f800-stat-20261122-01'
gate=ADOPTED/'longrun/tools/longrun_gate.py';schema=ADOPTED/'longrun/contracts/longrun_schema_v2.json'
gate_bytes=git('show',PIN+':longrun/tools/longrun_gate.py')
assert gate.read_bytes()==gate_bytes and sha256(gate_bytes).hexdigest()=='3355372ef1d9cbe3c4440bd6c3908a64827859d59bbdfe6bb9f9624c36aac7a7'
assert schema.read_bytes()==git('show',PIN+':longrun/contracts/longrun_schema_v2.json')
native=runpy.run_path(str(gate),run_name='pinned_return_contract')
packet=load(Path('/dwdhome/fy/cgpterm/artifacts/wall-f-closure-20261122')/RUN/'C0014-dispatch-packet.json')
d=load(Path(packet['delegation_json_path']));i=load(CALL/'INVOCATION.json');p=load(CALL/'PRO_RETURN.json')
binding=load(RECORD/'longrun/runs'/RUN/'RUN_BINDING.json')
assert git('show','bff656a28bafbd10919e05a01d799c20d0d25fad:longrun/runs/'+RUN+'/RUN_BINDING.json')==(RECORD/'longrun/runs'/RUN/'RUN_BINDING.json').read_bytes()
for kind,value in [('binding',binding),('delegation',d),('invocation',i),('professional_return',p)]:native['validated'](kind,value)
native['pro_state'](p);native['object_ref_fields'](p)
assert p['run_id']==i['run_id']==d['run_id']==RUN and p['call_id']==i['call_id']=='C0014'
assert d==packet['delegation'] and i==packet['invocation'] and d['delegation_id']=='D006'
assert p['role']=='executor' and p['sender']==i['recipient']==d['recipient']
assert p['sender'] in binding['executors'] and p['return_to']==d['return_to']==d['issuer']==binding['manager']
assert p['delegation_ref']==packet['delegation_ref']==i['assignment_ref']
assert set(d['permitted_operations'])<=set(g['operation'] for g in binding['grants'])
assert d['permitted_operations']==['run_result_statistics_analysis_write','run_record_write']
assert p['professional_state']=='REPORTED_COMPLETE' and all(p[k] is None for k in ['remaining_scope_ref','continuation_ref','owner_request_ref'])
assert not p['issued_delegation_refs'] and not p['issued_order_refs'] and not p['accepted_worker_refs'] and binding['workers']==[]
repo,commit,path=native['ref_parts'](p['result_ref'])
assert repo=='daowei2026/observe-iterate' and commit==RESULT and path=='longrun/runs/'+RUN+'/professional/D006/EXECUTOR_REPORT.md'
assert git('cat-file','-t',commit+':'+path).decode().strip()=='blob'
published=load(CALL/'PROFESSIONAL_PUBLICATION_READBACK.json')
assert published['commit']==RESULT and len(published['files'])==4 and all(x['local_git_blob_match'] for x in published['files'])
manifest=json.loads(git('show',RESULT+':longrun/runs/'+RUN+'/professional/D006/PROFESSIONAL_MANIFEST.json'))
for row in manifest['files']:
    raw=git('show',RESULT+':'+row['record_path'])
    assert sha256(raw).hexdigest()==row['sha256'] and Path(row['local_path']).read_bytes()==raw
diag=load(LOCAL/'DiagnosisReport.json');issue=load(LOCAL/'RequirementOrImplementationIssue.json')
assert diag['finding_id']==issue['finding_id']=='F800-GF-002' and issue['classification']=='ImplementationMismatch'
assert diag['parameter_repairability']['feasibility_status']=='PROVEN_NOT_ADJUSTABLE'
assert load(LOCAL/'ExperimentEvaluation.json')['checks']['both_failure_interventions_incomplete_at_all_8']
assert load(LOCAL/'VALIDATION.json')['completed']
assert all(x['completed'] for x in load(LOCAL/'WORKFLOW_COMPLETION.json')['steps'])
assert not load(LOCAL/'OwnerDecisionApplicability.json')['owner_decision_packet_applicable']
proposal=load(LOCAL/'ModificationProposal.json')
assert proposal['proposal_id']=='F800-MP-002' and not proposal['diff_applied'] and proposal['status']=='PROPOSED_NOT_AUTHORIZED_NOT_APPLIED'
changes=git('diff','--name-only','a791240c2bbf428f79bb86fe01f7ca025fd4a14b',RESULT).decode().splitlines()
assert changes and all(x.startswith('longrun/runs/'+RUN+'/professional/D006/') for x in changes)
for name in ['FeatureRunResultBinding.json','GlobalProfileGate.json','FindingDisposition.json','GlobalFindingCandidates.json']:
    oldpath='longrun/runs/'+RUN+'/professional/D005/'+name
    assert git('show','38e2af72be826a1e98fd7f5d4522c50d218750f3:'+oldpath)==(RECORD/oldpath).read_bytes()
src=Path('/dwdhome/fy/BASE_E6_2_copy/.runtime/f-observation-multiple-github-20261122/frp')
assert subprocess.check_output(['git','rev-parse','HEAD'],cwd=src,text=True).strip()=='be57d6752c9d43d10f1d670e1d2993bb8153ea7c'
assert not subprocess.check_output(['git','status','--porcelain'],cwd=src)
audit=dict(verified_at=datetime.now(timezone.utc).isoformat(),schema_pass=True,pro_state_pass=True,immutable_refs_pass=True,
 actual_invocation_delegation_binding_pass=True,workers_empty=True,professional_state=p['professional_state'],
 result_ref=p['result_ref'],result_published_before_return=True,professional_publication=published,published_manifest_files_verified=len(manifest['files']),
 pinned_gate_ref='daowei2026/observe-iterate@'+PIN+':longrun/tools/longrun_gate.py',gate_sha256=sha256(gate_bytes).hexdigest(),
 pinned_schema_sha256=sha256(schema.read_bytes()).hexdigest(),return_sha256=sha256((CALL/'PRO_RETURN.json').read_bytes()).hexdigest(),
 validated_functions=['validated(binding/delegation/invocation/professional_return)','pro_state','object_ref_fields'],
 full_cli_validation='未运行完整validate-executor-return：该版binding()将manager硬编码为chatgpt，与本Run采用Codex manager不兼容。原gate未修改，未伪造独立controller receipt。',
 completion_boundary='D006原Skill单GF002诊断完成，确认为既存ImplementationMismatch并提出独立MP002；未实施正式修改或新X/G，GF001/D005有效原件保留。新MP待原manager/Owner确认，Feature未释放，manager尚未消费。')
(CALL/'RETURN_VALIDATION.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(schema_pass=True,pro_state_pass=True,actual_binding_pass=True,result_published_before_return=True,published_files=len(manifest['files'])),ensure_ascii=False))
