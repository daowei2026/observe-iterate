"""执行未修改的同版schema/pro_state，并核对本Run真实身份与先行结果提交。"""
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
import json
import runpy
import subprocess

RECORD=Path(__file__).resolve().parents[5]
RUN='OI-F800-STAT-20261122-01'
CALL=RECORD/'longrun/runs'/RUN/'calls/C0005'
LOCAL=Path('/dwdhome/fy/BASE_E6_2_copy/artifacts')/RUN/'D002'
ADOPTED=Path('/dwdhome/fy/cgpterm/artifacts/wall-f-closure-20261122/adopted-observe-iterate')
PIN='87b951bbd15078a2d6353bdd24afe0d8f19c845c'
RESULT='3169703e769340200b183dad7675a1d22ecc1850'
def git(*args):return subprocess.check_output(['git',*args],cwd=RECORD)
def load(path):return json.loads(path.read_text())

assert git('branch','--show-current').decode().strip()=='codex/oi-f800-stat-20261122-01'
gate=ADOPTED/'longrun/tools/longrun_gate.py'
gate_bytes=git('show',PIN+':longrun/tools/longrun_gate.py')
assert gate.read_bytes()==gate_bytes and sha256(gate_bytes).hexdigest()=='3355372ef1d9cbe3c4440bd6c3908a64827859d59bbdfe6bb9f9624c36aac7a7'
schema=ADOPTED/'longrun/contracts/longrun_schema_v2.json'
assert schema.read_bytes()==git('show',PIN+':longrun/contracts/longrun_schema_v2.json')
native=runpy.run_path(str(gate),run_name='pinned_return_contract')
packet=load(Path('/dwdhome/fy/cgpterm/artifacts/wall-f-closure-20261122')/RUN/'C0005-dispatch-packet.json')
d=packet['delegation'];i=load(CALL/'INVOCATION.json');p=load(CALL/'PRO_RETURN.json')
binding=load(RECORD/'longrun/runs'/RUN/'RUN_BINDING.json')
native['validated']('professional_return',p)
native['pro_state'](p)
native['object_ref_fields'](p)
assert p['run_id']==i['run_id']==d['run_id']==RUN and p['call_id']==i['call_id']=='C0005'
assert p['role']=='executor' and p['sender']==i['recipient']==d['recipient']
assert p['sender'] in binding['executors'] and p['return_to']==d['return_to']==d['issuer']==binding['manager']
assert p['delegation_ref']==packet['delegation_ref']==i['assignment_ref']
assert i==packet['invocation'] and i['token']==packet['invocation']['token']
assert p['professional_state']=='REPORTED_COMPLETE' and all(p[k] is None for k in ['remaining_scope_ref','continuation_ref','owner_request_ref'])
assert not p['issued_delegation_refs'] and not p['issued_order_refs'] and not p['accepted_worker_refs'] and binding['workers']==[]
repo,commit,path=native['ref_parts'](p['result_ref'])
assert repo=='daowei2026/observe-iterate' and commit==RESULT
assert path=='longrun/runs/'+RUN+'/professional/D002/EXECUTOR_REPORT.md'
assert git('cat-file','-t',commit+':'+path).decode().strip()=='blob'
published=load(CALL/'PROFESSIONAL_PUBLICATION_READBACK.json')
assert published['commit']==RESULT and len(published['files'])==3 and all(x['local_git_blob_match'] for x in published['files'])
assert all(x['completed'] for x in load(LOCAL/'WORKFLOW_COMPLETION.json')['steps'])
assert load(LOCAL/'VALIDATION.json')['completed']
audit=dict(verified_at=datetime.now(timezone.utc).isoformat(),schema_pass=True,pro_state_pass=True,immutable_refs_pass=True,
    actual_invocation_delegation_binding_pass=True,workers_empty=True,professional_state=p['professional_state'],
    result_ref=p['result_ref'],result_published_before_return=True,professional_publication=published,
    pinned_gate_ref='daowei2026/observe-iterate@'+PIN+':longrun/tools/longrun_gate.py',gate_sha256=sha256(gate_bytes).hexdigest(),
    pinned_schema_sha256=sha256(schema.read_bytes()).hexdigest(),return_sha256=sha256((CALL/'PRO_RETURN.json').read_bytes()).hexdigest(),
    validated_functions=["validated('professional_return')",'pro_state','object_ref_fields'],
    full_cli_validation='未运行完整validate-executor-return：该版binding()将manager硬编码为chatgpt，与本Run采用Codex manager不兼容。原gate未修改，未伪造独立controller receipt。',
    completion_boundary='D002 X/G原Skill职责已完成；GlobalProfileGate=DIAGNOSIS_REQUIRED为后继专业路由，不是本D未完成项；manager尚未消费。')
(CALL/'RETURN_VALIDATION.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(schema_pass=True,pro_state_pass=True,actual_binding_pass=True,result_published_before_return=True),ensure_ascii=False))
