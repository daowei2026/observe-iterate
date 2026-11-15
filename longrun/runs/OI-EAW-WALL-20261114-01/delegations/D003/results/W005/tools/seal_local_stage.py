"""封存既有STOP证据；不调用preparer、evaluator、launcher或任何工程验证。"""
from pathlib import Path
import ast, datetime, errno, fcntl, hashlib, json, os, stat, sys

BASE=Path('/dwdhome/fy/BASE_E6_2')
ROOT=BASE/'.oi-runs/OI-EAW-WALL-20261114-01/D003/W005'
LOCK=ROOT.parents[1]/'.D003-writer.lock'
SESSION=Path('/home/dw/.codex/sessions/2026/11/14/rollout-2026-11-14T21-53-08-01a1da55-5881-7590-94a1-0661f0236977.jsonl')
TURN='01a1dc6f-c611-7ba1-8301-f0bef1f0eef0'
TARGET='longrun/runs/OI-EAW-WALL-20261114-01/delegations/D003/results/W005/'
MANIFEST=ROOT/'artifacts/PUBLICATION_MANIFEST.json'
HASHES=ROOT/'artifacts/HASHES.sha256'
FREEZE=ROOT/'artifacts/FREEZE_RECEIPT.json'
STOP='STOP_SECCOMP_STATIC_PREPARATION_ASSERTION'

def utc():return datetime.datetime.now(datetime.timezone.utc).isoformat()
def fact(p):
    p=Path(p);b=p.read_bytes();s=p.lstat()
    return {'path':str(p),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'mtime_ns':s.st_mtime_ns,'inode':s.st_ino,'dev':s.st_dev}
def target(p):
    rel=p.relative_to(ROOT)
    if rel.parts[0]=='artifacts':rel=Path(*rel.parts[1:])
    return TARGET+rel.as_posix()
def save(p,o,exclusive=True):
    assert p.resolve().is_relative_to(ROOT)
    with p.open('x' if exclusive else 'w') as f:f.write(json.dumps(o,ensure_ascii=False,indent=2)+'\n')
def inventory():
    paths=[]
    for parent,dirs,names in os.walk(ROOT,followlinks=False):
        assert len(dirs)+len(names)<2000
        for name in dirs:assert not (Path(parent)/name).is_symlink()
        for name in names:
            p=Path(parent)/name;s=p.lstat()
            assert stat.S_ISREG(s.st_mode) and s.st_nlink==1 and not p.is_symlink()
            paths.append(p);assert len(paths)<2000
    return sorted(paths)
def guard():
    assert Path.cwd()==BASE and ROOT.resolve()==ROOT and not any(p.is_symlink() for p in [ROOT,*ROOT.parents])
    assert os.environ['HOME']=='/home/dw' and os.environ['CODEX_HOME']=='/home/dw/.codex' and sys.dont_write_bytecode
    t=Path('/proc/246047/stat').read_text();assert t[t.rfind(')')+2:].split()[19]=='47679582'
    info=Path('/proc/246047/fdinfo/3').read_text();assert 'FLOCK' in info and 'WRITE 246047' in info and LOCK.lstat().st_ino==14806399
    fd=os.open(LOCK,os.O_RDWR|os.O_NOFOLLOW)
    try:
        assert os.fstat(fd).st_ino==14806399
        try:fcntl.flock(fd,fcntl.LOCK_EX|fcntl.LOCK_NB)
        except BlockingIOError as e:competition_errno=e.errno;assert e.errno in (11,13)
        else:raise RuntimeError('STOP unexpected lock acquisition')
    finally:os.close(fd)
    return {'at':utc(),'path':str(LOCK),'holder_pid':246047,'startticks':'47679582','inode':14806399,'fdinfo':info,'competition_errno':competition_errno,'own_contender_closed':True,'holder_lock_replaced_released':False}

lock=guard()
assert not any(p.exists() for p in [MANIFEST,HASHES,FREEZE])
assert SESSION.stat().st_size<25000000
completed={};changes={}
for lineno,line in enumerate(SESSION.open(),1):
    j=json.loads(line);p=j.get('payload',{})
    if j.get('type')!='event_msg' or not isinstance(p,dict) or p.get('turn_id')!=TURN or p.get('type')!='item_completed':continue
    item=p['item'];record={'session_source':str(SESSION),'session_line':lineno,'timestamp':j.get('timestamp'),'turn_id':TURN,'item':item}
    if item.get('type')=='CommandExecution':completed[item['id']]=record
    if item.get('type')=='FileChange':changes[item['id']]=record
assert len([r for r in completed.values() if ' -B '+str(ROOT/'tools/prepare_static.py') in str(r['item'].get('command'))])==1
assert any(' -B '+str(ROOT/'tools/archive_stop.py') in str(r['item'].get('command')) and r['item']['exit_code']==0 for r in completed.values())
for filename,records in [('NATIVE_COMMAND_COMPLETIONS.jsonl',completed),('NATIVE_FILE_CHANGES.jsonl',changes)]:
    with (ROOT/'audit'/filename).open('w') as out:
        for r in records.values():out.write(json.dumps(r,ensure_ascii=False)+'\n')
seal_cmd='PYTHONDONTWRITEBYTECODE=1 TMPDIR='+str(ROOT/'tmp')+' /usr/bin/python3.12 -I -S -B '+str(ROOT/'tools/seal_local_stage.py')
with (ROOT/'artifacts/COMMAND_LOG.jsonl').open('x') as out:
    for r in completed.values():out.write(json.dumps({'record_type':'NATIVE_COMPLETED_COMMAND',**r},ensure_ascii=False)+'\n')
    for r in changes.values():out.write(json.dumps({'record_type':'NATIVE_FILE_CHANGE',**r},ensure_ascii=False)+'\n')
    out.write(json.dumps({'record_type':'SEAL_CURRENT_COMMAND','at':utc(),'pid':os.getpid(),'cwd':str(BASE),'shell_command':seal_cmd,'sys_argv':sys.argv,'status':'RUNNING_AT_LOG_FREEZE','exit_code':None,'scope_note':'完整记录本封存命令输入；尚未发生的终态不伪造。封存命令真实exit由平台原生completed事件和本次执行器回执给出；冻结原件不再回写日志。','HOME':os.environ['HOME'],'CODEX_HOME':os.environ['CODEX_HOME'],'PYTHONDONTWRITEBYTECODE':os.environ.get('PYTHONDONTWRITEBYTECODE'),'TMPDIR':os.environ.get('TMPDIR')},ensure_ascii=False)+'\n')

before_files=inventory()
snapshot=[fact(p) for p in before_files]
save(ROOT/'artifacts/WRITE_SURFACE_AUDIT.json',{'status':'LOCAL_COMMAND_AND_FILE_BOUNDARY_REVIEW_ONLY','stop_code':STOP,'at':utc(),'unique_business_write_root':str(ROOT),'cwd':str(BASE),'HOME':'/home/dw','CODEX_HOME':'/home/dw/.codex','HOME_CODEX_reset':False,'task_tmp':str(ROOT/'tmp'),'business_write_outside_root_in_executed_command_sources_observed':False,'platform_native_session_log_exception':'平台自身沿原执行器记录session；Worker仅只读抽取本turn命令/FileChange，不向HOME/CODEX写业务文件。','current_kernel_confinement_coverage':False,'global_zero_outside_writes_PASS':False,'unknown_paths_from_missing_kernel_trace':'NOT_MEASURED','native_command_log':'COMMAND_LOG.jsonl','native_file_changes':'audit/NATIVE_FILE_CHANGES.jsonl','scope':'审阅实际命令/文件路径；不以此代替full kernel write trace。旧W源码/原件未写，具名输入另有hash/mtime/inode复核。','readonly_input_recheck':'audit/INPUT_IMMUTABILITY_CHECK.json','negative_target_postcheck':'audit/NEGATIVE_TARGET_POSTCHECK.json','R0_A1_attempts':0,'scenario_runs':0,'normal_runs':0,'build_compile_test_install_download':0,'GitHub_or_shared_repo_write':0,'files_at_pre_catalog_boundary':snapshot,'own_final_catalog_writes_only':[str(ROOT/'artifacts/LOCAL_VALIDATION.json'),str(MANIFEST),str(HASHES),str(FREEZE)],'command_log_closure':'封存命令以RUNNING_AT_LOG_FREEZE/null exit真实记录，原生完成回执在执行器；不伪造未来终态。'})

required=['WORKER_EXECUTION_REPORT.md','W005_BINDING.json','CONTROLLER_SENTINEL_PRECONFIRMATION.json','FIOCLEX_LOCAL_CONSTANT_VERIFICATION.json','SECCOMP_IOCTL_FILTER_DELTA.json','SECCOMP_FILTER_STATIC_EVALUATION.json','WRITE_CONFINEMENT_REPORT.json','FULL_WRITE_TRACE_REVIEW.json','OFFLINE_CLOSURE_REPORT.json','RESOURCE_BUDGET_REPORT.json','PHASE0_RECOVERY_VERDICT.json','COMMAND_LOG.jsonl','WRITE_SURFACE_AUDIT.json','EP_ACCEPTANCE_MATRIX.md','ENGINEERING_STOP_REPORT.md','LOCAL_STAGE_HANDOFF.json']
assert all((ROOT/'artifacts'/n).is_file() for n in required)
json_checked=[];jsonl_checked=[]
for p in inventory():
    if p.suffix=='.json':json.loads(p.read_bytes());json_checked.append(str(p))
    if p.suffix=='.jsonl':
        for line in p.open():json.loads(line)
        jsonl_checked.append(str(p))
handoff=json.loads((ROOT/'artifacts/LOCAL_STAGE_HANDOFF.json').read_bytes())
assert handoff['outcome']=='STOP' and handoff['result_ref'] is None and handoff['true_github_commit'] is None
assert len(handoff['deliverable_mapping'])==13 and len(handoff['missing'])==14
assert not (ROOT/'WORKER_RETURN.json').exists() and not (ROOT/'artifacts/WORKER_RETURN.json').exists() and not (ROOT/'tools/runtime.py').exists() and not (ROOT/'tools/landlock_launcher.py').exists()
assert not any((ROOT/'trace').iterdir()) and not any((ROOT/'probes').iterdir())
failure=json.loads((ROOT/'receipts/STATIC_PREPARATION_FAILURE.json').read_bytes())
assert failure['preparer_source']==fact(ROOT/'tools/prepare_static.py')
current_inputs=[]
inputs=json.loads((ROOT/'input/VERIFIED_INPUTS.json').read_bytes())
for e in [*inputs['verified_local_inputs'],*inputs['extra']]:
    assert e['source']==fact(e['source']['path'])
    current_inputs.append({'path':e['source']['path'],'same_bytes_hash_mtime_inode_dev':True})
save(ROOT/'artifacts/LOCAL_VALIDATION.json',{'at':utc(),'status':'PASS_LOCAL_ARCHIVE_CONSISTENCY_ONLY','professional_or_preflight_acceptance':False,'JSON_files_parsed':json_checked,'JSONL_files_parsed':jsonl_checked,'required_STOP_artifacts_present':required,'original_preparer_unchanged':True,'prepare_attempt_count':1,'evaluator_attempt_count':0,'R0_A1_attempt_count':0,'source_inputs_unchanged':current_inputs,'formal_Return_absent':True,'future_self_refs_or_hashes_created':False,'conditional_empty_artifacts_created':False,'four_PASS_claimed':False,'full_command_outputs_preserved_to_seal_boundary':True,'sealer_current_status':'RUNNING_AT_LOG_FREEZE','future_terminal_record_not_fabricated':True,'preparer_or_project_tests_rerun':False})

payload=[p for p in inventory() if p not in [MANIFEST,HASHES,FREEZE]]
entries=[dict(fact(p),publication_target=target(p),ref=None,transport='verbatim bytes; no normalization') for p in payload]
assert len({e['publication_target'] for e in entries})==len(entries)
save(MANIFEST,{'schema':'local-publication-manifest/v1','run_id':'OI-EAW-WALL-20261114-01','work_order_id':'W005','outcome':'STOP','at':utc(),'publisher':'controller; worker has no GitHub write grant','target_root':TARGET,'real_commit':None,'result_ref':None,'entries':entries,'deliverable_mapping':handoff['deliverable_mapping'],'catalog_files':[{'path':str(p),'publication_target':target(p),'self_or_forward_hash_omitted':True} for p in [MANIFEST,HASHES,FREEZE]],'hash_layers':'此manifest仅hash payload；HASHES覆盖payload+manifest；FREEZE覆盖全部其他文件；FREEZE自身hash由执行器与最终交接给出。无自hash或future ref。','formal_return_later_target':handoff['formal_return_later_target'],'missing':handoff['missing']})
hash_paths=sorted([*payload,MANIFEST])
with HASHES.open('x') as out:
    for p in hash_paths:out.write(fact(p)['sha256']+'  '+p.relative_to(ROOT).as_posix()+'\n')
checks=[]
for e in entries:
    assert fact(e['path'])=={k:v for k,v in e.items() if k not in ['publication_target','ref','transport']}
    checks.append({'path':e['path'],'bytes_sha256_metadata_match':True})
for line in HASHES.read_text().splitlines():
    digest,relative=line.split('  ',1);assert fact(ROOT/relative)['sha256']==digest
all_other=inventory();assert FREEZE not in all_other
disk=sum(p.stat().st_size for p in all_other);assert disk<2147483648 and len(all_other)+1<50000
final_lock=guard()
save(FREEZE,{'schema':'local-freeze-receipt/v1','run_id':'OI-EAW-WALL-20261114-01','work_order_id':'W005','outcome':'STOP','gate':'PREFLIGHT_STOP','stop_code':STOP,'at':utc(),'all_files_except_this_receipt':[dict(fact(p),publication_target=target(p),ref=None) for p in all_other],'total_file_count_including_this_receipt':len(all_other)+1,'total_bytes_excluding_this_receipt':disk,'this_receipt_path':str(FREEZE),'this_receipt_publication_target':target(FREEZE),'this_receipt_sha256':'Not embedded: see actual executor output/final handoff; no self-hash','payload_hash_verification_count':len(checks),'HASHES_entries_verified':len(hash_paths),'input_immutability_recheck_count':len(current_inputs),'original_preparer_kept_unchanged':True,'native_completed_commands_archived':len(completed),'native_file_changes_archived':len(changes),'last_seal_command':{'shell_command':seal_cmd,'status_at_manifest_freeze':'RUNNING','exit_code_at_manifest_freeze':None,'completion_evidence':'execution tool actual terminal result, then platform native completed event; no archive rewrite'},'binding_lock_end':final_lock,'HOME':'/home/dw','CODEX_HOME':'/home/dw/.codex','frozen_after_local_stage':True,'formal_RETURN_created':False,'true_published_refs_pending':True,'publisher_next':'controller transports verbatim, returns actual refs/hash; original W1 sameW005 then writes formal Return only to E1','no_professional_or_business_completion_claim':True})
assert inventory()==sorted([*all_other,FREEZE])
for e in json.loads(FREEZE.read_bytes())['all_files_except_this_receipt']:
    assert fact(e['path'])=={k:v for k,v in e.items() if k not in ['publication_target','ref']}
output={'outcome':'STOP','stop_code':STOP,'file_count':len(all_other)+1,'total_bytes':disk+FREEZE.stat().st_size,'missing_count':len(handoff['missing']),'preparer_attempts':1,'evaluator_attempts':0,'R0_A1_attempts':0,'native_completed_commands':len(completed),'hash_verification':'PASS','all_output_absolute_paths_hashes_and_targets':str(FREEZE),'key_files':[fact(ROOT/'artifacts'/n) for n in ['WORKER_EXECUTION_REPORT.md','LOCAL_STAGE_HANDOFF.json','PUBLICATION_MANIFEST.json','HASHES.sha256','FREEZE_RECEIPT.json','LOCAL_VALIDATION.json','COMMAND_LOG.jsonl','ENGINEERING_STOP_REPORT.md','FIOCLEX_LOCAL_CONSTANT_VERIFICATION.json','SECCOMP_IOCTL_FILTER_DELTA.json','SECCOMP_FILTER_STATIC_EVALUATION.json','W005_BINDING.json']]}
print(json.dumps(output,ensure_ascii=False,indent=2))
