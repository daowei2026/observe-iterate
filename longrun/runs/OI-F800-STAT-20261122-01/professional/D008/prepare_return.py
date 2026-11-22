"""D008专业结果已发布读回后，形成C0019原V2 Return及不改原gate的校验脚本。"""
from pathlib import Path
import argparse,json

ROOT=Path(__file__).resolve().parent
RECORD=Path('/dwdhome/fy/cgpterm/artifacts/wall-f-closure-20261122/OI-F800-STAT-20261122-01/executor-records')
RUN='OI-F800-STAT-20261122-01'
CALL=RECORD/'longrun/runs'/RUN/'calls/C0019'
parser=argparse.ArgumentParser();parser.add_argument('--result-commit',required=True);args=parser.parse_args()
RESULT=args.result_commit;assert len(RESULT)==40
published=json.loads((CALL/'PROFESSIONAL_PUBLICATION_READBACK.json').read_text())
assert published['commit']==RESULT and len(published['files'])==4 and all(x['local_git_blob_match'] for x in published['files'])
value=dict(schema='longrun-professional-return/v2',run_id=RUN,call_id='C0019',role='executor',
 sender='codex:'+RUN+':executor:E1',
 delegation_ref='daowei2026/observe-iterate@c1b79ff6c6e5b103920ccb2fc9b946ca8dec7eac:longrun/runs/'+RUN+'/delegations/D008/DELEGATION.json',
 return_to='codex:'+RUN+':manager',
 result_ref='daowei2026/observe-iterate@'+RESULT+':longrun/runs/'+RUN+'/professional/D008/EXECUTOR_REPORT.md',
 issued_delegation_refs=[],issued_order_refs=[],accepted_worker_refs=[],professional_state='REPORTED_COMPLETE',
 remaining_scope_ref=None,continuation_ref=None,owner_request_ref=None)
(CALL/'PRO_RETURN.json').write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n')
template='''"""未改锁定schema/gate函数 + C0019真实I/D/Binding及已发布D008结果核对。"""
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
RESULT='__RESULT__'
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
(CALL/'RETURN_VALIDATION.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\\n')
print(json.dumps(dict(schema_pass=True,pro_state_pass=True,actual_binding_pass=True,result_published_before_return=True,published_files=len(manifest['files'])),ensure_ascii=False))
'''
(CALL/'validate_return.py').write_text(template.replace('__RESULT__',RESULT))
(CALL/'EXECUTOR_REPORT.md').write_text(f"""# C0019｜D008原executor正式回交

D008当前委派已完成。原生专业结果已先发布并远端读回：
`daowei2026/observe-iterate@{RESULT}:longrun/runs/{RUN}/professional/D008/EXECUTOR_REPORT.md`。

采用已批准FRP39f完整生产F-only rb/hc/i、5m、2021—2023，31表独立OnlyRead与G1—G8已完成；完整结果/配置/范围/Calendar/代码/二进制/加载/真实flock与实际进程均有证据。原GF001的22+8控制与GF002的8观点由独立原生Life/AsOf复验，共38项；finding状态、当前全量检查与原生GlobalProfileGate见已发布专业原件。新be57/ac两组历史对照均按自然对象/知识时点比较，实际Revision/发行/UUID/exact变化已记录；历史产物保留。

首个尝试因本地平台少store_dir.json退出且无F结果，补齐正常空存储覆盖配置后第二次真实持锁生产成功，原日志保留。完整业务配置、PNV、范围和正式代码未在D008修改。Current U只合并D007 delta与当前新X绑定，未重做完整理解。四项场景问题及Q共享适配/独立数值边界限制继续传递。

本V2 REPORTED_COMPLETE只表示D008当前X/G职责完成；本E1没有签FeatureReleaseGate/ReleasePackage、下游Q/V或WALL变更，不代表manager已经消费或父Run闭环。原manager沿原生Gate与既有Workflow处理后继。

未修改锁定schema或gate。调用原validated/pro_state/object_ref_fields并核真实I/D/最新Binding、权限与全部已发布产物；完整CLI的Codex manager硬编码兼容限制如实记录在RETURN_VALIDATION，未伪造controller receipt。
""")
print(CALL/'PRO_RETURN.json')
