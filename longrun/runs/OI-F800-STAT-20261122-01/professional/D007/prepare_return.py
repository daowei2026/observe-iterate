"""D007专业结果已发布读回后，形成C0017原V2 Return及不改原gate的校验脚本。"""
from pathlib import Path
import argparse,json

ROOT=Path(__file__).resolve().parent
RECORD=Path('/dwdhome/fy/cgpterm/artifacts/wall-f-closure-20261122/OI-F800-STAT-20261122-01/executor-records')
RUN='OI-F800-STAT-20261122-01'
CALL=RECORD/'longrun/runs'/RUN/'calls/C0017'
parser=argparse.ArgumentParser();parser.add_argument('--result-commit',required=True);args=parser.parse_args()
RESULT=args.result_commit;assert len(RESULT)==40
published=json.loads((CALL/'PROFESSIONAL_PUBLICATION_READBACK.json').read_text())
assert published['commit']==RESULT and len(published['files'])==4 and all(x['local_git_blob_match'] for x in published['files'])
value=dict(schema='longrun-professional-return/v2',run_id=RUN,call_id='C0017',role='executor',
 sender='codex:'+RUN+':executor:E1',
 delegation_ref='daowei2026/observe-iterate@714087ecaf03dbed1854a603bd390ad95a166a82:longrun/runs/'+RUN+'/delegations/D007/DELEGATION.json',
 return_to='codex:'+RUN+':manager',
 result_ref='daowei2026/observe-iterate@'+RESULT+':longrun/runs/'+RUN+'/professional/D007/EXECUTOR_REPORT.md',
 issued_delegation_refs=[],issued_order_refs=[],accepted_worker_refs=[],professional_state='REPORTED_COMPLETE',
 remaining_scope_ref=None,continuation_ref=None,owner_request_ref=None)
(CALL/'PRO_RETURN.json').write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n')
template='''"""未改锁定schema/gate函数 + C0017真实I/D/Binding及已发布D007结果核对。"""
from pathlib import Path
from hashlib import sha256
from datetime import datetime,timezone
import json,runpy,subprocess
RECORD=Path(__file__).resolve().parents[5]
RUN='OI-F800-STAT-20261122-01'
CALL=RECORD/'longrun/runs'/RUN/'calls/C0017'
LOCAL=Path('/dwdhome/fy/BASE_E6_2_copy/artifacts')/RUN/'D007'
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
packet=load(Path('/dwdhome/fy/cgpterm/artifacts/wall-f-closure-20261122')/RUN/'C0017-dispatch-packet.json')
d=load(Path(packet['delegation_json_path']));i=load(CALL/'INVOCATION.json');p=load(CALL/'PRO_RETURN.json')
binding=load(RECORD/'longrun/runs'/RUN/'RUN_BINDING.json')
assert git('show','3dc11a9dbf39e181b3c6a3051419a90e46b92aac:longrun/runs/'+RUN+'/RUN_BINDING.json')==(RECORD/'longrun/runs'/RUN/'RUN_BINDING.json').read_bytes()
for kind,value in [('binding',binding),('delegation',d),('invocation',i),('professional_return',p)]:native['validated'](kind,value)
native['pro_state'](p);native['object_ref_fields'](p)
assert p['run_id']==i['run_id']==d['run_id']==RUN and p['call_id']==i['call_id']=='C0017'
assert d==packet['delegation'] and i==packet['invocation'] and d['delegation_id']=='D007'
assert p['role']=='executor' and p['sender']==i['recipient']==d['recipient']
assert p['sender'] in binding['executors'] and p['return_to']==d['return_to']==d['issuer']==binding['manager']
assert p['delegation_ref']==packet['delegation_ref']==i['assignment_ref']
assert set(d['permitted_operations'])<=set(g['operation'] for g in binding['grants'])
assert d['permitted_operations']==['feature_behavior_implementation','feature_code_commit_push_adopt','run_result_statistics_analysis_write','run_record_write']
assert all(any(g['operation']==op and 'F800-MP-002' in g['authority_quote'] for g in binding['grants']) for op in ['feature_behavior_implementation','feature_code_commit_push_adopt'])
assert p['professional_state']=='REPORTED_COMPLETE' and all(p[k] is None for k in ['remaining_scope_ref','continuation_ref','owner_request_ref'])
assert not p['issued_delegation_refs'] and not p['issued_order_refs'] and not p['accepted_worker_refs'] and binding['workers']==[]
repo,commit,path=native['ref_parts'](p['result_ref'])
assert repo=='daowei2026/observe-iterate' and commit==RESULT and path=='longrun/runs/'+RUN+'/professional/D007/EXECUTOR_REPORT.md'
assert git('cat-file','-t',commit+':'+path).decode().strip()=='blob'
published=load(CALL/'PROFESSIONAL_PUBLICATION_READBACK.json')
assert published['commit']==RESULT and len(published['files'])==4 and all(x['local_git_blob_match'] for x in published['files'])
manifest=json.loads(git('show',RESULT+':longrun/runs/'+RUN+'/professional/D007/PROFESSIONAL_MANIFEST.json'))
for row in manifest['files']:
    raw=git('show',RESULT+':'+row['record_path'])
    assert sha256(raw).hexdigest()==row['sha256'] and Path(row['local_path']).read_bytes()==raw
fi=load(LOCAL/'ImplementationFixReturn.json');adoption=load(LOCAL/'CodeVersionAdoption.json')
assert all(k in fi for k in ['diagnosis_ref','code_commit','changed_files','changed_behavior','tests','new_feature_version','ready_for_feature_rerun'])
assert fi['ready_for_feature_rerun'] and fi['code_commit']==adoption['new_frp']
assert fi['diagnosis_ref'].startswith('daowei2026/observe-iterate@46de903caa04be60a5600ef9f416445f5a6366cd:')
assert all(x['result'].startswith('PASS') for x in fi['tests'])
assert load(LOCAL/'VALIDATION.json')['completed'] and load(LOCAL/'VALIDATION.json')['no_formal_F_run_in_D007']
assert load(LOCAL/'FindingDisposition.json')['status']=='FIXED_PENDING_RERUN' and not load(LOCAL/'FindingDisposition.json')['closed']
assert load(LOCAL/'RERUN_HANDOFF.json')['workflow_status']=='RERUN_REQUIRED'
assert load(LOCAL/'REGRESSION_COMPARISON.json')['actual_adapter_graph']
assert load(LOCAL/'APPROVED_DIFF_CONFORMANCE.json')['implemented_diff_content_exact']
changes=git('diff','--name-only','6ff5ce2e5ad9cc92f887df46b677554de2fd4316',RESULT).decode().splitlines()
assert changes and all(x.startswith('longrun/runs/'+RUN+'/professional/D007/') for x in changes)
for name in ['FeatureRunResultBinding.json','GlobalProfileGate.json','FindingDisposition.json','GlobalFindingCandidates.json']:
    oldpath='longrun/runs/'+RUN+'/professional/D005/'+name
    assert git('show','38e2af72be826a1e98fd7f5d4522c50d218750f3:'+oldpath)==(RECORD/oldpath).read_bytes()
src=Path('/dwdhome/fy/BASE_E6_2_copy/.runtime/f-observation-multiple-github-20261122/frp')
assert subprocess.check_output(['git','rev-parse','HEAD'],cwd=src,text=True).strip()==adoption['new_frp']
assert not subprocess.check_output(['git','status','--porcelain'],cwd=src)
audit=dict(verified_at=datetime.now(timezone.utc).isoformat(),schema_pass=True,pro_state_pass=True,immutable_refs_pass=True,
 actual_invocation_delegation_binding_pass=True,workers_empty=True,professional_state=p['professional_state'],
 result_ref=p['result_ref'],result_published_before_return=True,professional_publication=published,published_manifest_files_verified=len(manifest['files']),
 pinned_gate_ref='daowei2026/observe-iterate@'+PIN+':longrun/tools/longrun_gate.py',gate_sha256=sha256(gate_bytes).hexdigest(),
 pinned_schema_sha256=sha256(schema.read_bytes()).hexdigest(),return_sha256=sha256((CALL/'PRO_RETURN.json').read_bytes()).hexdigest(),
 validated_functions=['validated(binding/delegation/invocation/professional_return)','pro_state','object_ref_fields'],
 full_cli_validation='未运行完整validate-executor-return：该版binding()将manager硬编码为chatgpt，与本Run采用Codex manager不兼容。原gate未修改，未伪造独立controller receipt。',
 completion_boundary='D007已批准MP002 FI完成：原diff实施，真实adapter13项/窗口64项/覆盖8控制和隔离构建通过，新FRP已推送采用；GF002为FIXED_PENDING_RERUN，新完整X/G待原manager签后继，Feature未释放，manager尚未消费。')
(CALL/'RETURN_VALIDATION.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\\n')
print(json.dumps(dict(schema_pass=True,pro_state_pass=True,actual_binding_pass=True,result_published_before_return=True,published_files=len(manifest['files'])),ensure_ascii=False))
'''
(CALL/'validate_return.py').write_text(template.replace('__RESULT__',RESULT))
(CALL/'EXECUTOR_REPORT.md').write_text(f"""# C0017｜D007原executor FI回交

D007已批准MP002 FI完成，专业结果已先发布并远端回读：
`daowei2026/observe-iterate@{RESULT}:longrun/runs/{RUN}/professional/D007/EXECUTOR_REPORT.md`。

生产变更及上下文与原批准具体diff一致。真实正常KLine适配13项、既有窗口64项、Material覆盖8控制及四目标隔离构建通过；旧be57在同一真实适配测试上产生预期缺价断言失败。实际新FRP已提交、推送和采用，准确commit/runtime/binary/config/TIS/依赖绑定与原生ImplementationFixReturn见专业提交；ready_for_feature_rerun=true。

GF002=FIXED_PENDING_RERUN，未关闭；本D无新正式F X/G或释放。D005原件与GF001闭环事实保留为旧版本对照，当前新代码须完整新attempt/store X、31表独立读回及原Skill全量G，保护原8缺价位置及GF001原22+8控制，并实测Revision/发行/UUID和exact链变化。新后继已获Owner批准，由原manager消费FI后签发，无需重复请示本提案范围；本E1不代manager签后继，不运行Q/V或改WALL。

原V2 REPORTED_COMPLETE只表示本D007 FI交付完成，不代表manager已消费或业务Run闭环。先发布专业结果再引用已有exact提交；schema/pro_state/真实I/D/最新Binding/MP002权限及清单产物核对见RETURN_VALIDATION。完整CLI的Codex manager兼容限制如实记录，未改gate、未伪造controller receipt。
""")
print(CALL/'PRO_RETURN.json')
