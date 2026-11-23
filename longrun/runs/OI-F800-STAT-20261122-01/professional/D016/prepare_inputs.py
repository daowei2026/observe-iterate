from common import *
p=json.loads(PACKET.read_text());d=p['delegation'];i=p['invocation']
assert d['delegation_id']=='D016' and i['call_id']=='C0036'
assert i['token']=='3ece25e1b3a7456eb883723a7517b5d3'
assert p['professional_control_commit']==LOCKED
assert subprocess.check_output(['git','rev-parse','HEAD'],cwd=RECORD).decode().strip()==INITIAL
assert subprocess.check_output(['git','status','--porcelain'],cwd=RECORD)==b''
assert subprocess.check_output(['git','branch','--show-current'],cwd=RECORD).decode().strip()==p['record_branch']
assert json.loads(Path(p['delegation_json_path']).read_text())==d
assert json.loads(git_bytes(INITIAL,PREFIX+'/calls/C0036/INVOCATION.json'))==i
assert d['permitted_operations']==['run_result_statistics_analysis_write','run_record_write']
sources=list(dict.fromkeys([p['delegation_ref'],p['invocation_ref']]+d['input_refs']+i['source_refs']))
entries=[]
for n,s in enumerate(sources,1):
 repo,rest=s.split('@',1);commit,path=rest.split(':',1)
 assert repo=='daowei2026/observe-iterate' and len(commit)==40
 raw=git_bytes(commit,path);dest=ROOT/'inputs'/f'{n:02}-{Path(path).name}'
 dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(raw)
 physical=Path(p['adopted_source_root'])/path if commit==LOCKED else RECORD/path
 assert physical.read_bytes()==raw
 obj=json.loads(raw) if path.endswith('.json') else None
 entries.append(dict(source_ref=s,bytes=len(raw),sha256=sha(raw),local_copy=str(dest),physical_source=str(physical),exact_git_object_match=True,json_top_fields=list(obj) if isinstance(obj,dict) else None))
owner=Path(p['owner_latest_original_path']).read_bytes()
assert sha(owner)==p['professional_control_adoption']['owner_original_sha256']
assert owner==git_bytes('4bf46f3fbe402915e3272e49a71dc94eac787c15',PREFIX+'/owner-decisions/CONTINUE-20261123/OWNER_CONTINUE.original.txt')
adoption=json.loads(git_bytes('4bf46f3fbe402915e3272e49a71dc94eac787c15',PREFIX+'/PROFESSIONAL_CONTROL_ADOPTION.json'))
assert all(p['professional_control_adoption'][k]==v for k,v in adoption.items())
save('SOURCE_REF_AUDIT.json',dict(run_id=RUN,call_id='C0036',delegation_id='D016',audited_at=now(),professional_control_commit=LOCKED,count=len(entries),exact_sources=entries,all_git_objects_match=True,authoritative_adoption_shared_fields_match=True,latest_owner_original_sha256=sha(owner),workers=[]))
save('INPUT_BINDING.json',dict(professional_control_commit=LOCKED,feature_run_result_binding=pro_ref('FeatureRunResultBinding.json'),frp_commit=FRP,tis_commit='2f460d663d821cf2ba25555eda13e78b697d0767',configuration_sha256='b72095ff100da926474701b74bff7586a74b9770bc81cadc34c23cfe223e5cb3',current_G=pro_ref('EXECUTOR_REPORT.md','D015'),finding_id='F-LIFE-PEAK-CONCURRENCY',new_production=False,feature_behavior_changed=False,valid_history_reused=['U','X','D008_G','31_table_readback','D015_G','S1','S2']))
save('RESOURCE_SCOPE.json',dict(scope='DIAGNOSTIC_ONLY_READ_EXISTING_RESULTS_AND_EXACT_SOURCE',writes=[str(ROOT),PREFIX+'/professional/D016',PREFIX+'/calls/C0036'],shared_cache_write=False,production=False,production_lock_required=False,workers=[],source_policy=p['resource_policy_path']))
save('plan.json',dict(schema_version=1,project=dict(id='oi-f800-stat-20261122-01',title='F800统计闭环 Run'),task=dict(id='oi-f800-stat-20261122-01-d016-e1',title='D016 E1：Life峰值36原偏差诊断',type='engineering',owner='agent',monitoring=dict(scope='general'),completion_gate='先定位责任逻辑并核全部36Life、原生诊断及有证据的处理类型完成；专业结果及原V2 Return真实发布回读。'),phases=[dict(id='d',title='原D诊断与回交',steps=[dict(id='preflight',title='准确来源与输入绑定',acceptance='锁定Control/Skill/Owner/输入实际读取，精确对象/权限核验',weight=1),dict(id='localize',title='全部36Life与责任逻辑定位',acceptance='口径、每Life时序身份期限及create/revision/end/current对账，精确源码责任点',weight=4),dict(id='diagnose',title='原生诊断与后续类型',acceptance='事实与竞争解释排除、符合性与合理性分开、业务影响及必要后续材料',weight=3),dict(id='return',title='验证发布与原V2回交',acceptance='专业对象先行及C0036 Return发布原授权分支、远端对象字节核验',weight=1)])]))
print(json.dumps(dict(exact_sources=len(entries),professional_control_commit=LOCKED,initial_head=INITIAL)))
