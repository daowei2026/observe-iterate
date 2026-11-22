"""原V2函数及本C真实I/D/Binding/授权/专业发布原件核验；不改原gate。"""
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
import json, runpy, subprocess

RECORD=Path(__file__).resolve().parents[5]
RUN='OI-F800-STAT-20261122-01';PREFIX='longrun/runs/'+RUN
CALL=RECORD/PREFIX/'calls/C0029'
LOCAL=Path('/dwdhome/fy/BASE_E6_2_copy/artifacts')/RUN/'D013'
ADOPTED=Path('/dwdhome/fy/cgpterm/artifacts/wall-f-closure-20261122/adopted-observe-iterate')
PIN='87b951bbd15078a2d6353bdd24afe0d8f19c845c';RESULT='266c34e5d7d75a05677e7969d528090d37cac44e'
def git(*a):return subprocess.check_output(['git',*a],cwd=RECORD)
def load(p):return json.loads(p.read_text())
assert git('branch','--show-current').decode().strip()=='codex/oi-f800-stat-20261122-01'
gate=ADOPTED/'longrun/tools/longrun_gate.py';schema=ADOPTED/'longrun/contracts/longrun_schema_v2.json'
gate_bytes=git('show',PIN+':longrun/tools/longrun_gate.py')
assert gate.read_bytes()==gate_bytes and sha256(gate_bytes).hexdigest()=='3355372ef1d9cbe3c4440bd6c3908a64827859d59bbdfe6bb9f9624c36aac7a7'
assert schema.read_bytes()==git('show',PIN+':longrun/contracts/longrun_schema_v2.json')
native=runpy.run_path(str(gate),run_name='pinned_return_contract')
packet=load(Path('/dwdhome/fy/cgpterm/artifacts/wall-f-closure-20261122')/RUN/'C0029-dispatch-packet.json')
d=load(Path(packet['delegation_json_path']));i=load(CALL/'INVOCATION.json');p=load(CALL/'PRO_RETURN.json')
binding=load(RECORD/PREFIX/'RUN_BINDING.json')
assert git('show','3dc11a9dbf39e181b3c6a3051419a90e46b92aac:'+PREFIX+'/RUN_BINDING.json')==(RECORD/PREFIX/'RUN_BINDING.json').read_bytes()
for kind,value in [('binding',binding),('delegation',d),('invocation',i),('professional_return',p)]:native['validated'](kind,value)
native['pro_state'](p);native['object_ref_fields'](p)
assert p['run_id']==i['run_id']==d['run_id']==RUN and p['call_id']==i['call_id']=='C0029'
assert d==packet['delegation'] and i==packet['invocation'] and d['delegation_id']=='D013'
assert p['role']=='executor' and p['sender']==i['recipient']==d['recipient']
assert p['sender'] in binding['executors'] and p['return_to']==d['return_to']==d['issuer']==binding['manager']
assert p['delegation_ref']==packet['delegation_ref']==i['assignment_ref']
assert i['token']=='bc49cbb4b48541eeb1615f591475c145'
assert d['permitted_operations']==['run_result_statistics_analysis_write','run_record_write']
assert set(d['permitted_operations'])<=set(g['operation'] for g in binding['grants'])
assert p['professional_state']=='REPORTED_COMPLETE' and all(p[k] is None for k in ['remaining_scope_ref','continuation_ref','owner_request_ref'])
assert not p['issued_delegation_refs'] and not p['issued_order_refs'] and not p['accepted_worker_refs'] and binding['workers']==[]
repo,commit,path=native['ref_parts'](p['result_ref'])
assert repo=='daowei2026/observe-iterate' and commit==RESULT and path==PREFIX+'/professional/D013/EXECUTOR_REPORT.md'
assert git('cat-file','-t',commit+':'+path).decode().strip()=='blob'
published=load(CALL/'PROFESSIONAL_PUBLICATION_READBACK.json')
assert published['commit']==RESULT and len(published['files'])==4 and all(x['local_git_blob_match'] and x['byte_equal'] for x in published['files'])
manifest=json.loads(git('show',RESULT+':'+PREFIX+'/professional/D013/PROFESSIONAL_MANIFEST.json'))
for row in manifest['files']:
    raw=git('show',RESULT+':'+row['record_path'])
    assert sha256(raw).hexdigest()==row['sha256'] and Path(row['local_path']).read_bytes()==raw
cs=load(LOCAL/'CaseReviewSet.json');es=load(LOCAL/'ScenarioExpectationSet.json');fz=load(LOCAL/'FrozenExpectationSet.json')
assert cs['status']==es['status']==fz['status']=='FROZEN_FOR_COMPARISON'
assert fz['expectations']==es['expectations'] and fz['case_ids']==[c['case_id'] for c in cs['cases']]
assert not es['evidence_comparison_performed'] and load(LOCAL/'VALIDATION.json')['checks_passed']
for f in load(LOCAL/'FREEZE_MANIFEST.json')['files']:assert sha256((LOCAL/f['file']).read_bytes()).hexdigest()==f['sha256']
I=load(LOCAL/'INPUT_BINDING.json');H=load(LOCAL/'S1_HANDOFF.json')
assert I['assignment_ref']==packet['delegation_ref'] and I['invocation_ref']==packet['invocation_ref']
assert I['permitted_operations']==d['permitted_operations'] and I['exact_source_count']==83
assert not any(I[k] for k in ['formal_feature_production','global_statistics_rerun','CAEGraph_rebuilt','formal_data_reexported','S2_evidence_comparison','FeatureRelease'])
assert H['uncompleted_S1_items']==H['blocked_items']==[] and H['workers']==[]
assert not H['evidence_comparison_performed'] and not H['parent_run_complete'] and not H['FeatureRelease']
assert load(LOCAL/'OpenQuestions.json')['original_questions_unchanged']==json.loads(git('show','d4f9fefaa67f9f22f540fa35a7da79cbbdf831ca:'+PREFIX+'/professional/D008/ScenarioQuestionQueue.json'))
M=json.loads(git('show','dfbc647030890fc8af80ac04a4d12a734d99f6dc:'+PREFIX+'/professional/D012/ObservationMaterialPackage.json'))
assert M['status']=='DATA_READY' and sha256(Path(M['final_html_local_path']).read_bytes()).hexdigest()==M['final_html_sha256']
assert (RECORD/PREFIX/'professional/D012/ObservationMaterialPackage.json').read_bytes()==git('show','dfbc647030890fc8af80ac04a4d12a734d99f6dc:'+PREFIX+'/professional/D012/ObservationMaterialPackage.json')
changes=git('diff','--name-only','-z','db1b87c6147c283643bdf75cfa9e8516d0d08eec',RESULT).decode().rstrip('\0').split('\0')
assert changes and all(x.startswith(PREFIX+'/professional/D013/') for x in changes)
audit=dict(verified_at=datetime.now(timezone.utc).isoformat(),schema_pass=True,pro_state_pass=True,immutable_refs_pass=True,
    actual_invocation_delegation_binding_pass=True,workers_empty=True,professional_state=p['professional_state'],
    result_ref=p['result_ref'],result_published_before_return=True,professional_publication=published,
    published_manifest_files_verified=len(manifest['files']),frozen_case_count=len(cs['cases']),frozen_expectation_count=len(es['expectations']),
    pinned_gate_ref='daowei2026/observe-iterate@'+PIN+':longrun/tools/longrun_gate.py',gate_sha256=sha256(gate_bytes).hexdigest(),
    pinned_schema_sha256=sha256(schema.read_bytes()).hexdigest(),return_sha256=sha256((CALL/'PRO_RETURN.json').read_bytes()).hexdigest(),
    validated_functions=['validated(binding/delegation/invocation/professional_return)','pro_state','object_ref_fields'],
    full_cli_validation='未运行完整validate-executor-return：该版binding()将manager硬编码为chatgpt，与本Run采用Codex manager不兼容。原gate未修改，未伪造独立controller receipt。',
    completion_boundary='仅D013原S1范围完成：七个真实案例及七条预期v1冻结，六类覆盖明确；潜在漏报NO_CASE_FOUND限有界筛查。当前U/X/G/M复用；没有S2对照、诊断、调参、Feature释放或父Run完成声明。')
(CALL/'RETURN_VALIDATION.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(schema_pass=True,pro_state_pass=True,actual_binding_pass=True,result_published_before_return=True,published_files=len(manifest['files'])),ensure_ascii=False))
