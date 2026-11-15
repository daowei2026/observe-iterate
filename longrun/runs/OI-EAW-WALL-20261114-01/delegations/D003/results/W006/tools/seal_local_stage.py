"""W006本地STOP封存，不执行或重试任何P0–P4/closure/预算/EP。"""
from pathlib import Path
import json, os, re, stat, sys
sys.path.insert(0,str(Path(__file__).resolve().parent))
from common import ROOT,binding,fact,guard,save,utc

TURN='01a1dcc1-192d-7003-ac02-e8e3f6648415'
SESSION=Path('/home/dw/.codex/sessions/2026/11/14/rollout-2026-11-14T21-53-08-01a1da55-5881-7590-94a1-0661f0236977.jsonl')
PREFIX='longrun/runs/OI-EAW-WALL-20261114-01/delegations/D003/results/W006/'
MANIFEST=ROOT/'artifacts/PUBLICATION_MANIFEST.json'
HASHES=ROOT/'artifacts/HASHES.sha256'
FREEZE=ROOT/'artifacts/FREEZE_RECEIPT.json'
STOP='STOP_PROBE_HOLDER_FDINFO_READ_EACCES'
def inventory():
    files=[]
    for parent,dirs,names in os.walk(ROOT,followlinks=False):
        assert len(dirs)+len(names)<2000
        for name in dirs:assert not (Path(parent)/name).is_symlink()
        for name in names:
            path=Path(parent)/name;s=path.lstat()
            assert stat.S_ISREG(s.st_mode) and s.st_nlink==1 and not path.is_symlink()
            files.append(path);assert len(files)<2000
    return sorted(files)
def target(p):
    rel=p.relative_to(ROOT)
    if rel.parts[0]=='artifacts':rel=Path(*rel.parts[1:])
    return PREFIX+rel.as_posix()
lock_start=guard()
assert not any(p.exists() for p in [MANIFEST,HASHES,FREEZE])
assert SESSION.stat().st_size<30000000
commands={};changes={};context=None
for number,line in enumerate(SESSION.open(),1):
    j=json.loads(line);p=j.get('payload',{})
    if j.get('type')=='turn_context' and p.get('turn_id')==TURN:context={k:p.get(k) for k in ['turn_id','cwd','model','effort']}
    if j.get('type')!='event_msg' or not isinstance(p,dict) or p.get('turn_id')!=TURN or p.get('type')!='item_completed':continue
    item=p['item'];r={'native_session_source':str(SESSION),'native_session_line':number,'timestamp':j.get('timestamp'),'turn_id':TURN,'item':item}
    if item.get('type')=='CommandExecution':commands[item['id']]=r
    if item.get('type')=='FileChange':changes[item['id']]=r
assert context=={'turn_id':TURN,'cwd':'/dwdhome/fy/BASE_E6_2','model':'gpt-6.1-sol','effort':'max'}
phase_commands={}
for filename in ['p0_history.py','p1_constants_layout.py','p2_generate.py','p3_evaluate.py','p4_single_attempt.py','archive_result.py']:
    suffix='/usr/bin/python3.12 -I -S -B '+str(ROOT/'tools'/filename)
    found=[]
    for r in commands.values():
        argv=r['item'].get('command',[])
        shell=argv[-1] if isinstance(argv,list) else argv
        if isinstance(shell,str) and shell.endswith(suffix):found.append(r)
    assert len(found)==1
    expected=1 if filename=='p4_single_attempt.py' else 0
    assert found[0]['item']['exit_code']==expected
    phase_commands[filename]={'native_id':found[0]['item']['id'],'actual_exit_code':expected,'attempts':1}
for name,records in [('NATIVE_COMMAND_COMPLETIONS.jsonl',commands),('NATIVE_FILE_CHANGES.jsonl',changes)]:
    with (ROOT/'audit'/name).open('x') as out:
        for r in records.values():out.write(json.dumps(r,ensure_ascii=False)+'\n')
child_commands=[json.loads(line) for line in (ROOT/'logs/COMMAND_LOG.jsonl').read_text().splitlines()]
assert len(child_commands)==1 and child_commands[0]['id']=='r0a1' and child_commands[0]['exit_code']==1
own_command='PYTHONDONTWRITEBYTECODE=1 TMPDIR='+str(ROOT/'tmp')+' /usr/bin/python3.12 -I -S -B '+str(ROOT/'tools/seal_local_stage.py')
with (ROOT/'artifacts/COMMAND_LOG.jsonl').open('x') as out:
    for r in commands.values():out.write(json.dumps({'record_type':'NATIVE_COMPLETED_COMMAND',**r},ensure_ascii=False)+'\n')
    for r in changes.values():out.write(json.dumps({'record_type':'NATIVE_FILE_CHANGE',**r},ensure_ascii=False)+'\n')
    for r in child_commands:out.write(json.dumps({'record_type':'CONFINED_CHILD_EXECUTION','record':r},ensure_ascii=False)+'\n')
    out.write(json.dumps({'record_type':'CURRENT_SEAL_COMMAND','at':utc(),'pid':os.getpid(),'cwd':str(Path.cwd()),'shell_command':own_command,'sys_argv':sys.argv,'status':'RUNNING_AT_LOG_FREEZE','exit_code':None,'HOME':os.environ['HOME'],'CODEX_HOME':os.environ['CODEX_HOME'],'TMPDIR':os.environ['TMPDIR'],'note':'本封存命令完整输入已列；未来终态不虚构。真实exit由本次执行器terminal result和平台原生completed事件证明；冻结后不回写原件。'},ensure_ascii=False)+'\n')

handoff=json.loads((ROOT/'artifacts/LOCAL_STAGE_HANDOFF.json').read_bytes())
verdict=json.loads((ROOT/'artifacts/PHASE0_RECOVERY_VERDICT.json').read_bytes())
attempt_marker=json.loads((ROOT/'receipts/R0_A1_ATTEMPT.json').read_bytes())
assert handoff['outcome']=='STOP' and len(handoff['missing'])==15 and len(handoff['deliverable_mapping'])==16
assert handoff['real_publication_commit'] is None and handoff['result_ref'] is None and not handoff['formal_Return_created']
assert verdict['stop_code']==STOP and verdict['R0_A1_attempts']==1 and verdict['R0_B_attempts']==verdict['R0_C_attempts']==0
for name in ['launcher','runtime','probe']:assert attempt_marker[name]==fact(attempt_marker[name]['path'])
static=json.loads((ROOT/'artifacts/SECCOMP_FILTER_STATIC_EVALUATION.json').read_bytes())
assert static['status']=='PASS' and static['semantic_comparison_cases']==24240 and static['expected_FIOCLEX_differences']==4
assert static['candidate_launcher']==fact(ROOT/'tools/landlock_launcher.py')
review=json.loads((ROOT/'artifacts/FULL_WRITE_TRACE_REVIEW.json').read_bytes())
assert review['trace_lines']==2290 and review['successful_descriptor_write_count']==3 and review['successful_descriptor_write_bytes']==6594
assert not review['global_zero_outside_writes_PASS']
required=['WORKER_EXECUTION_REPORT.md','W006_BINDING.json','CONTROLLER_SENTINEL_PRECONFIRMATION.json','HISTORICAL_FIOCLEX_PHASE_CLASSIFICATION.json','FIOCLEX_LOCAL_CONSTANT_VERIFICATION.json','SECCOMP_DATA_LAYOUT_VERIFICATION.json','PARENT_RUNTIME_BINDING_DELTA.json','SECCOMP_IOCTL_FILTER_DELTA.json','SECCOMP_FILTER_STATIC_EVALUATION.json','WRITE_CONFINEMENT_REPORT.json','FULL_WRITE_TRACE_REVIEW.json','OFFLINE_CLOSURE_REPORT.json','RESOURCE_BUDGET_REPORT.json','PHASE0_RECOVERY_VERDICT.json','COMMAND_LOG.jsonl','EP_ACCEPTANCE_MATRIX.md','ENGINEERING_STOP_REPORT.md','LOCAL_STAGE_HANDOFF.json']
assert all((ROOT/'artifacts'/n).is_file() for n in required)
assert not (ROOT/'WORKER_RETURN.json').exists() and not (ROOT/'artifacts/WORKER_RETURN.json').exists()
assert not any((ROOT/'probes').iterdir())
inputs=json.loads((ROOT/'input/VERIFIED_INPUTS.json').read_bytes());input_end=[]
for row in inputs['local_inputs']:
    before=row['source'];after=fact(before['path']);assert before==after
    assert fact(row['mirror']['path'])['sha256']==before['sha256']
    input_end.append({'before':before,'after':after,'same_bytes_hash_mtime_inode_dev':True})
assert len(input_end)==26
save('audit/SEAL_INPUT_AND_CODE_IMMUTABILITY.json',{'at':utc(),'local26_inputs_unchanged':input_end,'actual_attempt_code_unchanged_after_failure':[{'path':attempt_marker[name]['path'],'sha256':attempt_marker[name]['sha256'],'bytes_hash_mtime_inode_dev_unchanged':True} for name in ['launcher','runtime','probe']],'current_candidate_matches_static_PASS':True,'no_preparer_evaluator_kernel_retry':True})
before_catalog=[fact(p) for p in inventory()]
save('artifacts/WRITE_SURFACE_AUDIT.json',{'status':'LOCAL_COMMAND_BOUNDARY_REVIEW_PLUS_SCOPED_FAILED_KERNEL_TRACE','at':utc(),'unique_business_write_root':str(ROOT),'HOME':os.environ['HOME'],'CODEX_HOME':os.environ['CODEX_HOME'],'HOME_CODEX_reset':False,'task_tmp':str(ROOT/'tmp'),'task_cache':str(ROOT/'cache'),'task_config':str(ROOT/'config'),'old_W1_W5_and_shared_written_by_worker':False,'current_kernel_trace_scope':'trace/r0a1.248966 only; not all W/continuation','trace_successful_descriptor_writes':review['successful_descriptor_writes'],'trace_outside_file_write_count':0,'trace_unknown_write_paths':0,'global_zero_outside_writes_PASS':False,'proc_comm_exceptions':[],'native_command_log':'COMMAND_LOG.jsonl','phase_command_execution_counts':phase_commands,'actual_R0_A1_child_commands':child_commands,'local_input_immutability_scope':'26 named local inputs, not whole BASE/HOME','local_input_recheck':'audit/SEAL_INPUT_AND_CODE_IMMUTABILITY.json','actual_post_failure_code_unchanged':True,'negative_targets_readonly_postcheck':'audit/NEGATIVE_TARGET_POSTCHECK.json','scenario_normal_DBA_wrapper_native_reader_current_material_runs':0,'build_compile_serialization_install_download_runs':0,'GitHub_or_shared_push':0,'platform_session_log_exception':'平台沿原执行器日志；Worker只读提取本turn命令/FileChange，不向HOME/CODEX写业务文件。','files_at_pre_catalog_boundary':before_catalog,'final_catalog_additions_only':['artifacts/LOCAL_VALIDATION.json','artifacts/PUBLICATION_MANIFEST.json','artifacts/HASHES.sha256','artifacts/FREEZE_RECEIPT.json'],'seal_current_terminal_status_not_fabricated':True})

parsed_json=[];parsed_jsonl=[]
for p in inventory():
    if p.suffix=='.json':json.loads(p.read_bytes());parsed_json.append(str(p))
    if p.suffix=='.jsonl':
        for line in p.open():json.loads(line)
        parsed_jsonl.append(str(p))
save('artifacts/LOCAL_VALIDATION.json',{'at':utc(),'status':'PASS_LOCAL_ARCHIVE_STRUCTURE_HASH_CONSISTENCY_ONLY','professional_or_business_PASS':False,'phase_commands':phase_commands,'P0_P3_actual_PASS':True,'P4_attempts':1,'P4_actual_exit_code':1,'P4_stop_code':STOP,'four_Phase0_requirements_PASS':False,'current_probe_body_entered':True,'current_bootstrap_FIOCLEX_succeeded':True,'explicit_F_GETFD_effect_test_reached':False,'full_kernel_trace_delivered':True,'trace_path_mapping_scope':'single failed execution chain','closure_budget_EP_or_scenario_entered':False,'JSON_files_parsed':parsed_json,'JSONL_files_parsed':parsed_jsonl,'required_STOP_evidence_files_present':required,'deliverable_mapping_count':16,'missing_count':15,'original_local26_inputs_unchanged':True,'actual_attempt_sources_unchanged':True,'formal_Return_not_created_without_refs':True,'no_future_or_self_refs_or_hashes':True,'real_empty_stderr_retained_as_actual_log_not_conditional_artifact':fact(ROOT/'logs/r0a1.stderr'),'current_seal_command_status':'RUNNING_AT_LOG_FREEZE; actual completion via executor receipt','native_completed_commands':len(commands),'native_file_changes':len(changes)})

payload=[p for p in inventory() if p not in [MANIFEST,HASHES,FREEZE]]
entries=[dict(fact(p),publication_target=target(p),ref=None,normalization='none') for p in payload]
assert len({e['publication_target'] for e in entries})==len(entries)
save('artifacts/PUBLICATION_MANIFEST.json',{'schema':'local-publication-manifest/v1','run_id':'OI-EAW-WALL-20261114-01','work_order_id':'W006','outcome':'STOP','at':utc(),'actual_publisher':'controller; worker has no GitHub write grant','target_root':PREFIX,'real_commit':None,'result_ref':None,'entries':entries,'deliverable_mapping':handoff['deliverable_mapping'],'missing':handoff['missing'],'catalogs':[{'path':str(p),'publication_target':target(p),'own_or_forward_hash_omitted':True} for p in [MANIFEST,HASHES,FREEZE]],'hash_layers':'manifest hashes payload; HASHES hashes payload+manifest; FREEZE hashes all other files; FREEZE own actual hash comes from executor/final handoff. No circular hash/future ref.','formal_Return_later_target':handoff['formal_Return_later_target']})
hashed=sorted([*payload,MANIFEST])
with HASHES.open('x') as out:
    for p in hashed:out.write(fact(p)['sha256']+'  '+p.relative_to(ROOT).as_posix()+'\n')
for e in entries:assert fact(e['path'])=={k:v for k,v in e.items() if k not in ['publication_target','ref','normalization']}
for line in HASHES.read_text().splitlines():
    digest,rel=line.split('  ',1);assert fact(ROOT/rel)['sha256']==digest
all_other=inventory();assert FREEZE not in all_other
size=sum(p.stat().st_size for p in all_other);assert size<2147483648 and len(all_other)+1<50000
lock_end=guard()
save('artifacts/FREEZE_RECEIPT.json',{'schema':'local-freeze-receipt/v1','run_id':'OI-EAW-WALL-20261114-01','work_order_id':'W006','outcome':'STOP','gate':'PREFLIGHT_STOP','stop_code':STOP,'at':utc(),'all_files_except_this_receipt':[dict(fact(p),publication_target=target(p),ref=None) for p in all_other],'file_count_including_this_receipt':len(all_other)+1,'bytes_excluding_this_receipt':size,'this_receipt_path':str(FREEZE),'this_receipt_publication_target':target(FREEZE),'this_receipt_sha256_note':'See actual executor output/final handoff; no self hash embedded.','HASHES_entries_verified':len(hashed),'payload_entries_verified':len(entries),'local_original26_inputs_unchanged':True,'actual_attempt_code_unchanged':True,'phase_counts':phase_commands,'current_context':context,'native_completed_commands_archived':len(commands),'native_file_changes_archived':len(changes),'P0_P3_PASS':True,'P4_once_exit1_no_retry':True,'probe_child_grandchild_count':0,'lock_start':lock_start,'lock_end':lock_end,'HOME':os.environ['HOME'],'CODEX_HOME':os.environ['CODEX_HOME'],'formal_Return_created':False,'real_publication_refs_pending':True,'frozen_after_this_local_stage':True,'last_seal_command':{'shell_command':own_command,'status_at_archive_freeze':'RUNNING','exit_code_at_archive_freeze':None,'actual_terminal_evidence':'execution tool terminal result and original platform completed event; do not rewrite frozen files'},'next':'controller transports verbatim to results/W006; returns exact published refs; same original W1/W006 then final-return only, formal Return to E1','professional_or_parent_completion_claimed':False})
assert inventory()==sorted([*all_other,FREEZE])
for e in json.loads(FREEZE.read_bytes())['all_files_except_this_receipt']:
    assert fact(e['path'])=={k:v for k,v in e.items() if k not in ['publication_target','ref']}
print(json.dumps({'outcome':'STOP','stop_code':STOP,'P0_P3':'PASS','P4_attempts':1,'P4_exit':1,'file_count':len(all_other)+1,'total_bytes':size+FREEZE.stat().st_size,'missing_count':15,'hash_verification':'PASS','all_output_absolute_paths_bytes_hashes_metadata_targets':str(FREEZE),'key_files':[fact(ROOT/'artifacts'/n) for n in ['WORKER_EXECUTION_REPORT.md','LOCAL_STAGE_HANDOFF.json','PUBLICATION_MANIFEST.json','HASHES.sha256','FREEZE_RECEIPT.json','COMMAND_LOG.jsonl','FULL_WRITE_TRACE_REVIEW.json','LOCAL_VALIDATION.json']]},ensure_ascii=False,indent=2))
