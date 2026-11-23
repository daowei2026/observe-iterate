"""准确packet/新专业控制及有效D008输入原件审计，不重新运行U/X/G。"""
from common import *
packet=json.loads(PACKET.read_text());d=packet['delegation'];i=packet['invocation']
assert d['delegation_id']=='D015' and i['call_id']=='C0034'
assert i['token']=='c84b79a71bba4cd38459f02ca1ca608a'
assert packet['professional_control_commit']==LOCKED
assert subprocess.check_output(['git','branch','--show-current'],cwd=RECORD).decode().strip()==packet['record_branch']=='codex/oi-f800-stat-20261122-01'
assert subprocess.check_output(['git','rev-parse','HEAD'],cwd=RECORD).decode().strip()==INITIAL
assert subprocess.check_output(['git','status','--porcelain'],cwd=RECORD)==b''
assert json.loads(Path(packet['delegation_json_path']).read_text())==d
assert json.loads((RECORD/PREFIX/'calls/C0034/INVOCATION.json').read_text())==i
assert d['permitted_operations']==['run_result_statistics_analysis_write','run_record_write']
sources=list(dict.fromkeys([packet['delegation_ref'],packet['invocation_ref'],d['task_ref'],d['business_context_ref']]+d['input_refs']+i['source_refs']))
entries=[];adopted=Path(packet['adopted_source_root'])
for n,s in enumerate(sources,1):
    repo,rest=s.split('@',1);commit,path=rest.split(':',1)
    assert repo=='daowei2026/observe-iterate' and len(commit)==40
    raw=git_bytes(commit,path);p=ROOT/'inputs'/f'{n:02}-{Path(path).name}'
    p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(raw)
    physical=None
    if commit==LOCKED:
        assert (adopted/path).read_bytes()==raw;physical=str(adopted/path)
    elif path.startswith(PREFIX+'/'):
        assert (RECORD/path).read_bytes()==raw;physical=str(RECORD/path)
    entries.append(dict(source_ref=s,path=path,commit=commit,bytes=len(raw),sha256=sha(raw),
        local_copy=str(p),physical_source=physical,exact_git_object_match=True))
skill_dir='skills/reasonableness-analysis/feature-global-behavior-profiling'
for name in ['SKILL.md','WORKFLOW.md','IO_SPEC.md']:
    p=ROOT/'locked_skill'/name;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(git_bytes(LOCKED,skill_dir+'/'+name))
owner=git_bytes('4bf46f3fbe402915e3272e49a71dc94eac787c15',PREFIX+'/owner-decisions/CONTINUE-20261123/OWNER_CONTINUE.original.txt')
assert owner==Path(packet['owner_latest_original_path']).read_bytes()
assert sha(owner)==packet['professional_control_adoption']['owner_original_sha256']
for name in ['FeatureRunResultBinding.json','CurrentFeatureUnderstandingPackage.json','GlobalBehaviorProfile.json',
             'StatisticsInputReadiness.json','StratificationPlan.json','StatisticDefinitions.json','PUBLIC_TABLE_SCHEMA.json',
             'NATIVE_OUTPUT_MANIFEST.json','configuration.json','readback/report.json']:
    assert (D008/name).read_bytes()==git_bytes(U,PREFIX+'/professional/D008/'+name)
save('SOURCE_REF_AUDIT.json',dict(run_id=RUN,call_id='C0034',delegation_id='D015',audited_at=now(),
    professional_control_commit=LOCKED,previous_professional_control_commit='87b951bbd15078a2d6353bdd24afe0d8f19c845c',
    physical_controller_commit=packet['professional_control_adoption']['controller_skill_commit'],
    exact_sources=entries,count=len(entries),all_git_objects_match=True,adopted_snapshot_matches=True,
    invocation_and_delegation_match=True,latest_owner_original_sha256=sha(owner),
    latest_owner_overrides_old_joint_barrier=True,valid_D008_inputs_reused=True,workers=[]))
plan=dict(schema_version=1,project=dict(id='oi-f800-stat-20261122-01',title='F800统计闭环 Run'),
    task=dict(id='oi-f800-stat-20261122-01-d015-e1',title='D015 E1：当前正式结果高置信发现补充',type='engineering',
        priority='normal',owner='agent',monitoring=dict(scope='general'),
        completion_gate='原G补充发现覆盖与高置信判断完成，形成当前结果绑定队列/未升级观察/适配包及Gate，采用commit明确；原V2回交发布远端核验。'),
    phases=[dict(id='g',title='原G补充及真实回交',steps=[
        dict(id='preflight',title='新控制/Owner与有效输入绑定',acceptance='准确来源实际读取；复用当前U/X/G及31表有效事实，登记增量口径',weight=1),
        dict(id='discover',title='适用业务面高置信发现',acceptance='复用全量剖面并做必要增量检查，不在首候选停止，不提前诊断根因',weight=4),
        dict(id='package',title='队列快照与原G适配包/Gate',acceptance='逐候选理由/边界、未升级/未检查范围、Owner候选明确状态与诊断输入可追溯',weight=2),
        dict(id='return',title='原V2专业回交',acceptance='先专业结果再C0034 Return发布授权分支，远端字节与对象核验',weight=1)])])
save('plan.json',plan)
print(json.dumps(dict(exact_sources=len(entries),professional_control_commit=LOCKED,valid_D008_inputs_reused=True),ensure_ascii=False))
