"""原V2函数与本C真实I/D/Binding/授权/专业发布核验；不改原gate。"""
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
import json, runpy, subprocess

RECORD=Path(__file__).resolve().parents[5]
RUN='OI-F800-STAT-20261122-01';PREFIX='longrun/runs/'+RUN
CALL=RECORD/PREFIX/'calls/C0031'
LOCAL=Path('/dwdhome/fy/BASE_E6_2_copy/artifacts')/RUN/'D014'
ADOPTED=Path('/dwdhome/fy/cgpterm/artifacts/wall-f-closure-20261122/adopted-observe-iterate')
PIN='87b951bbd15078a2d6353bdd24afe0d8f19c845c';RESULT='__RESULT__'
def git(*a):return subprocess.check_output(['git',*a],cwd=RECORD)
def load(p):return json.loads(p.read_text())
assert git('branch','--show-current').decode().strip()=='codex/oi-f800-stat-20261122-01'
gate=ADOPTED/'longrun/tools/longrun_gate.py';schema=ADOPTED/'longrun/contracts/longrun_schema_v2.json'
gate_bytes=git('show',PIN+':longrun/tools/longrun_gate.py')
assert gate.read_bytes()==gate_bytes and sha256(gate_bytes).hexdigest()=='3355372ef1d9cbe3c4440bd6c3908a64827859d59bbdfe6bb9f9624c36aac7a7'
assert schema.read_bytes()==git('show',PIN+':longrun/contracts/longrun_schema_v2.json')
native=runpy.run_path(str(gate),run_name='pinned_return_contract')
packet=load(Path('/dwdhome/fy/cgpterm/artifacts/wall-f-closure-20261122')/RUN/'C0031-dispatch-packet.json')
d=load(Path(packet['delegation_json_path']));i=load(CALL/'INVOCATION.json');p=load(CALL/'PRO_RETURN.json')
binding=load(RECORD/PREFIX/'RUN_BINDING.json')
assert git('show','3dc11a9dbf39e181b3c6a3051419a90e46b92aac:'+PREFIX+'/RUN_BINDING.json')==(RECORD/PREFIX/'RUN_BINDING.json').read_bytes()
assert git('show','8d1b3b0048dbee8f916d8bf16bf1e4122ee6540a:'+PREFIX+'/calls/C0031/INVOCATION.json')==(CALL/'INVOCATION.json').read_bytes()
for kind,value in [('binding',binding),('delegation',d),('invocation',i),('professional_return',p)]:native['validated'](kind,value)
native['pro_state'](p);native['object_ref_fields'](p)
assert p['run_id']==i['run_id']==d['run_id']==RUN and p['call_id']==i['call_id']=='C0031'
assert d==packet['delegation'] and i==packet['invocation'] and d['delegation_id']=='D014'
assert p['role']=='executor' and p['sender']==i['recipient']==d['recipient']
assert p['sender'] in binding['executors'] and p['return_to']==d['return_to']==d['issuer']==binding['manager']
assert p['delegation_ref']==packet['delegation_ref']==i['assignment_ref']
assert i['token']=='b6f19c6b9e1146b3b125a89798ef17ec'
assert d['permitted_operations']==['run_result_statistics_analysis_write','run_record_write']
assert set(d['permitted_operations'])<=set(g['operation'] for g in binding['grants'])
assert p['professional_state']=='REPORTED_COMPLETE' and all(p[k] is None for k in ['remaining_scope_ref','continuation_ref','owner_request_ref'])
assert not p['issued_delegation_refs'] and not p['issued_order_refs'] and not p['accepted_worker_refs'] and binding['workers']==[]
repo,commit,path=native['ref_parts'](p['result_ref'])
assert repo=='daowei2026/observe-iterate' and commit==RESULT and path==PREFIX+'/professional/D014/EXECUTOR_REPORT.md'
assert git('cat-file','-t',commit+':'+path).decode().strip()=='blob'
published=load(CALL/'PROFESSIONAL_PUBLICATION_READBACK.json')
assert published['commit']==RESULT and len(published['files'])==4 and all(x['local_git_blob_match'] and x['byte_equal'] for x in published['files'])
manifest=json.loads(git('show',RESULT+':'+PREFIX+'/professional/D014/PROFESSIONAL_MANIFEST.json'))
for row in manifest['files']:
    raw=git('show',RESULT+':'+row['record_path'])
    assert sha256(raw).hexdigest()==row['sha256'] and Path(row['local_path']).read_bytes()==raw
V=load(LOCAL/'VALIDATION.json');H=load(LOCAL/'S2_HANDOFF.json');I=load(LOCAL/'INPUT_BINDING.json')
assert V['checks_passed'] and V['frozen_v1_unchanged'] and V['all_7_native_package_contracts_pass']
assert V['exact_native_group_views']==18 and V['actual_browser_windows']==12
assert I['assignment_ref']==packet['delegation_ref'] and I['invocation_ref']==packet['invocation_ref']
assert I['permitted_operations']==d['permitted_operations'] and I['exact_source_count']==83
assert I['S2_evidence_comparison'] and not any(I[k] for k in ['formal_feature_production','global_statistics_rerun','CAEGraph_rebuilt','formal_data_reexported','FeatureRelease','scenario_reselection','S1_expectations_rewritten','diagnosis_performed','parameter_tuning','source_feature_modified'])
assert H['professional_state']=='REPORTED_COMPLETE' and H['workers']==[]
assert not H['feature_release_signed'] and not H['parent_run_completed'] and not H['manager_consumed']
assert H['skill3_candidates']==0 and load(LOCAL/'DiscrepancyQueue.json')['queue']==[]
assert load(LOCAL/'ObservationGapRequests.json')['mandatory_rebuild_requests']==[]
assert len(load(LOCAL/'ScenarioProcessCasebook.json')['cases'])==len(load(LOCAL/'EvidenceComparisonPackage.json')['packages'])==7
FROZEN='266c34e5d7d75a05677e7969d528090d37cac44e'
frozen_manifest=json.loads(git('show',FROZEN+':'+PREFIX+'/professional/D013/FREEZE_MANIFEST.json'))
for row in frozen_manifest['files']:
    raw=git('show',FROZEN+':'+PREFIX+'/professional/D013/'+row['file'])
    assert sha256(raw).hexdigest()==row['sha256'] and raw==(RECORD/PREFIX/'professional/D013'/row['file']).read_bytes()
M=json.loads(git('show','dfbc647030890fc8af80ac04a4d12a734d99f6dc:'+PREFIX+'/professional/D012/ObservationMaterialPackage.json'))
assert M['status']=='DATA_READY' and sha256(Path(M['final_html_local_path']).read_bytes()).hexdigest()==M['final_html_sha256']
changes=git('diff','--name-only','-z','8d1b3b0048dbee8f916d8bf16bf1e4122ee6540a',RESULT).decode().rstrip('\0').split('\0')
assert changes and all(x.startswith(PREFIX+'/professional/D014/') for x in changes)
audit=dict(verified_at=datetime.now(timezone.utc).isoformat(),schema_pass=True,pro_state_pass=True,immutable_refs_pass=True,
    actual_invocation_delegation_binding_pass=True,workers_empty=True,professional_state=p['professional_state'],
    result_ref=p['result_ref'],result_published_before_return=True,professional_publication=published,
    published_manifest_files_verified=len(manifest['files']),frozen_case_count=7,comparison_package_count=7,
    pinned_gate_ref='daowei2026/observe-iterate@'+PIN+':longrun/tools/longrun_gate.py',gate_sha256=sha256(gate_bytes).hexdigest(),
    pinned_schema_sha256=sha256(schema.read_bytes()).hexdigest(),return_sha256=sha256((CALL/'PRO_RETURN.json').read_bytes()).hexdigest(),
    validated_functions=['validated(binding/delegation/invocation/professional_return)','pro_state','object_ref_fields'],
    full_cli_validation='未运行完整validate-executor-return：该版binding()将manager硬编码为chatgpt，与本Run采用Codex manager不兼容。原gate未修改，未伪造独立controller receipt。',
    completion_boundary='仅D014原S2七个冻结案例的三过程与对齐、逐预期判断、首分歧或不可定位原因及后继分流完成。6例有界SUPPORTS、1例当前F层NOT_APPLICABLE；内部/前史缺口和迟到效用歧义保留，无合格S3疑点，不等于全800合理性/FeatureRelease/父Run完成。')
(CALL/'RETURN_VALIDATION.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(schema_pass=True,pro_state_pass=True,actual_binding_pass=True,result_published_before_return=True,published_files=len(manifest['files'])),ensure_ascii=False))
