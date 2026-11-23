"""使用当前未改V2 schema/gate函数及真实I/D/授权/专业发布核验。"""
from pathlib import Path
from hashlib import sha256
from datetime import datetime,timezone
import json,runpy,subprocess
RECORD=Path(__file__).resolve().parents[5]
RUN='OI-F800-STAT-20261122-01';PREFIX='longrun/runs/'+RUN
CALL=RECORD/PREFIX/'calls/C0036'
LOCAL=Path('/dwdhome/fy/BASE_E6_2_copy/artifacts')/RUN/'D016'
ADOPTED=Path('/dwdhome/fy/cgpterm/artifacts/wall-f-closure-20261122/adopted-observe-iterate-b8c2b513')
PIN='b8c2b513f0b08be6a1fa6782b71bf74a07faff0d';RESULT='__RESULT__'
INITIAL='48d6f7813670fdbdc3576410683f7ed3473c079d'
def git(*a):return subprocess.check_output(['git',*a],cwd=RECORD)
def load(p):return json.loads(p.read_text())
assert git('branch','--show-current').decode().strip()=='codex/oi-f800-stat-20261122-01'
gate=ADOPTED/'longrun/tools/longrun_gate.py';schema=ADOPTED/'longrun/contracts/longrun_schema_v2.json'
raw=git('show',PIN+':longrun/tools/longrun_gate.py')
assert gate.read_bytes()==raw and sha256(raw).hexdigest()=='3355372ef1d9cbe3c4440bd6c3908a64827859d59bbdfe6bb9f9624c36aac7a7'
assert schema.read_bytes()==git('show',PIN+':longrun/contracts/longrun_schema_v2.json')
native=runpy.run_path(str(gate),run_name='pinned_return_contract')
packet=load(Path('/dwdhome/fy/cgpterm/artifacts/wall-f-closure-20261122')/RUN/'C0036-dispatch-packet.json')
d=load(Path(packet['delegation_json_path']));i=load(CALL/'INVOCATION.json');p=load(CALL/'PRO_RETURN.json')
binding=load(RECORD/PREFIX/'RUN_BINDING.json')
assert git('show','3dc11a9dbf39e181b3c6a3051419a90e46b92aac:'+PREFIX+'/RUN_BINDING.json')==(RECORD/PREFIX/'RUN_BINDING.json').read_bytes()
assert git('show',INITIAL+':'+PREFIX+'/calls/C0036/INVOCATION.json')==(CALL/'INVOCATION.json').read_bytes()
for kind,value in [('binding',binding),('delegation',d),('invocation',i),('professional_return',p)]:native['validated'](kind,value)
native['pro_state'](p);native['object_ref_fields'](p)
assert p['run_id']==i['run_id']==d['run_id']==RUN and p['call_id']==i['call_id']=='C0036'
assert d==packet['delegation'] and i==packet['invocation'] and d['delegation_id']=='D016'
assert p['role']=='executor' and p['sender']==i['recipient']==d['recipient']
assert p['sender'] in binding['executors'] and p['return_to']==d['return_to']==d['issuer']==binding['manager']
assert p['delegation_ref']==packet['delegation_ref']==i['assignment_ref']
assert i['token']=='3ece25e1b3a7456eb883723a7517b5d3'
assert packet['professional_control_commit']==PIN and d['task_ref'].startswith('daowei2026/observe-iterate@'+PIN+':')
assert d['permitted_operations']==['run_result_statistics_analysis_write','run_record_write']
assert set(d['permitted_operations'])<=set(g['operation'] for g in binding['grants'])
assert p['professional_state']=='REPORTED_COMPLETE' and all(p[k] is None for k in ['remaining_scope_ref','continuation_ref','owner_request_ref'])
assert not p['issued_delegation_refs'] and not p['issued_order_refs'] and not p['accepted_worker_refs'] and binding['workers']==[]
orepo,ocommit,opath=native['ref_parts'](i['origin_ref']);manager=json.loads(git('show',ocommit+':'+opath));native['validated']('professional_return',manager)
assert orepo=='daowei2026/observe-iterate' and manager['sender']==d['issuer'] and manager['call_id']=='C0035'
assert packet['delegation_ref'] in manager['issued_delegation_refs']
repo,commit,path=native['ref_parts'](p['result_ref'])
assert repo=='daowei2026/observe-iterate' and commit==RESULT and path==PREFIX+'/professional/D016/EXECUTOR_REPORT.md'
report=git('show',commit+':'+path).decode();assert PIN in report
published=load(CALL/'PROFESSIONAL_PUBLICATION_READBACK.json')
assert published['commit']==RESULT and len(published['files'])==4 and all(x['local_git_blob_match'] and x['byte_equal'] for x in published['files'])
manifest=json.loads(git('show',RESULT+':'+PREFIX+'/professional/D016/PROFESSIONAL_MANIFEST.json'))
for row in manifest['files']:
 content=git('show',RESULT+':'+row['record_path'])
 assert sha256(content).hexdigest()==row['sha256'] and Path(row['local_path']).read_bytes()==content
V=load(LOCAL/'VALIDATION.json');H=load(LOCAL/'D_HANDOFF.json');I=load(LOCAL/'INPUT_BINDING.json')
assert V['checks_passed'] and V['professional_control_commit']==PIN and V['all_original_D_native_fields_present']
assert V['all_36_lives_reviewed'] and V['peak_life_count']==36 and V['all_36_revision_history_occurrences']==118
assert H['professional_state']=='REPORTED_COMPLETE' and H['workers']==[] and H['remaining_D016_authorized_items']==[]
assert not H['FeatureRelease'] and not H['parent_run_completed'] and not H['manager_consumed']
assert I['professional_control_commit']==PIN and not I['new_production'] and not I['feature_behavior_changed']
F=load(LOCAL/'FindingDisposition.json');D=load(LOCAL/'DiagnosisReport.json')
assert F['status']=='DIAGNOSIS_IN_PROGRESS' and not F['REJECTED_AS_NON_ISSUE'] and not F['confirmed_code_defect']
assert D['logic_localization_ref']=='LogicLocalization.json' and D['professional_scope_completed'] and not D['feature_release_allowed']
adoption=load(RECORD/PREFIX/'PROFESSIONAL_CONTROL_ADOPTION.json')
assert all(packet['professional_control_adoption'].get(k)==v for k,v in adoption.items()) and adoption['professional_control_commit']==PIN
assert (RECORD/PREFIX/'PROFESSIONAL_CONTROL_ADOPTION.json').read_bytes()==git('show','4bf46f3fbe402915e3272e49a71dc94eac787c15:'+PREFIX+'/PROFESSIONAL_CONTROL_ADOPTION.json')
sources=load(LOCAL/'SOURCE_REF_AUDIT.json');assert sources['count']==71 and sources['all_git_objects_match']
changes=git('diff','--name-only','-z',INITIAL,RESULT).decode().rstrip('\0').split('\0')
assert changes and all(x.startswith(PREFIX+'/professional/D016/') for x in changes)
audit=dict(verified_at=datetime.now(timezone.utc).isoformat(),schema_pass=True,pro_state_pass=True,immutable_refs_pass=True,actual_invocation_delegation_binding_pass=True,origin_manager_issued_delegation_pass=True,workers_empty=True,professional_control_commit=PIN,professional_control_adoption_pass=True,professional_state=p['professional_state'],result_ref=p['result_ref'],result_published_before_return=True,professional_publication=published,published_manifest_files_verified=len(manifest['files']),all_36_native_diagnosis_completed=True,finding_status=F['status'],business_tradeoff_open=True,FeatureRelease=False,pinned_gate_ref='daowei2026/observe-iterate@'+PIN+':longrun/tools/longrun_gate.py',gate_sha256=sha256(raw).hexdigest(),pinned_schema_sha256=sha256(schema.read_bytes()).hexdigest(),return_sha256=sha256((CALL/'PRO_RETURN.json').read_bytes()).hexdigest(),validated_functions=['validated(binding/delegation/invocation/professional_return)','pro_state','object_ref_fields'],full_cli_validation='b8c2b513原binding()仍硬编码ChatGPT manager，与本Run Codex manager不兼容；未声称完整CLI通过，原gate/schema未改，未伪造controller物理receipt。',completion_boundary='D016原生诊断及全部36责任定位完成；finding用途取舍未决，不等于关闭或F完成。无新生产、正式行为修改、标定或Release。')
(CALL/'RETURN_VALIDATION.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(schema_pass=True,pro_state_pass=True,actual_binding_pass=True,control_adoption_pass=True,result_published_before_return=True,published_files=len(manifest['files'])),ensure_ascii=False))
