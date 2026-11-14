from pathlib import Path
import sys,os,json,hashlib,ast,fcntl,errno,re,collections
R=Path('/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D003/W004');sys.path.insert(0,str(R/'tools'));import runtime as w
w.guard();A=R/'artifacts';stamp=w.utc();assert not (A/'PUBLICATION_MANIFEST.json').exists() and not (A/'HASHES.sha256').exists() and not (A/'FREEZE_RECEIPT.json').exists();order=json.loads((R/'input/C0012-remote-work_orders--W004--ORDER.json').read_text());handoff=json.loads((A/'LOCAL_STAGE_HANDOFF.json').read_text());verdict=json.loads((A/'PHASE0_RECOVERY_VERDICT.json').read_text());review=json.loads((A/'FULL_WRITE_TRACE_REVIEW.json').read_text());delta=json.loads((A/'PARENT_LAUNCHER_WIRING_DELTA.json').read_text());launch=json.loads((R/'receipts/r0a1-launcher.json').read_text());cmds=[json.loads(line) for line in (R/'logs/COMMAND_LOG.jsonl').read_text().splitlines()]
assert handoff['outcome']==verdict['outcome']=='STOP' and verdict['verdict']=='PREFLIGHT_STOP' and verdict['specific_stop']=='PROBE_BOOTSTRAP_IOCTL_FIOCLEX_EPERM';assert len(cmds)==1 and cmds[0]['exit_code']==2 and cmds[0]['id']=='r0a1';assert len(order['deliverables'])==len(handoff['deliverable_mapping'])==12;assert launch['abi']==6 and len(launch['calls'])==6 and all(c['errno']==0 and c['return']>=0 for c in launch['calls']);assert launch['stdio_fds'][0]['access_mode']==0 and launch['stdio_fds'][0]['path']=='/dev/null';assert not (R/'receipts/r0a1-main.json').exists();assert w.filefact(R/'tools/runtime.py')['sha256']==delta['new_runtime_sha256'] and w.filefact(R/'tools/landlock_launcher.py')['sha256']==delta['new_launcher_sha256']
assert w.filefact(A/'CONTROLLER_SENTINEL_PRECONFIRMATION.json')['sha256']=='d56b0541daeb37e39978b88ecafbc8fa3e562f882b46d8042b3ad669b3e5bc4a'
raw=(R/'trace/r0a1.244050').read_text().splitlines();assert not [line for line in raw if re.search(r'\bmprotect\(.*PROT_WRITE|\bmsync\(',line)]
review['mprotect_write_upgrade_or_msync_observed']=False;review['memory_write_scope_note']='所有实际MAP_SHARED文件映射均PROT_READ；无mprotect PROT_WRITE升级或msync调用，匿名/private mapping不计文件写。';w.save('artifacts/FULL_WRITE_TRACE_REVIEW.json',review)
# Only exact named inputs are checked; no full W003/BASE/HOME traversal.
before=json.loads((R/'audit/READONLY_INPUTS_BEFORE.json').read_text());extra=json.loads((R/'audit/CURRENT_QUALIFICATION_ADDITIONAL.json').read_text());before.append(extra['source']);checks=[]
for old in before:
 now=w.filefact(old['path']);same=all(now[k]==old[k] for k in ['bytes','sha256','mtime_ns','inode','dev']);assert same;checks.append({'before':old,'after':now,'unchanged':same})
w.save('audit/READONLY_INPUTS_AFTER.json',{'utc':stamp,'exact_named_input_count':len(checks),'all_unchanged':True,'scope':'22 indexed file mirrors＋10 dispatch/ORDER/binding files＋sentinel/Owner binding＋predispatch state，共35具名输入。不是旧W003全目录或全系统证明。','checks':checks})
context=json.loads((A/'W004_BINDING.json').read_text())['actual_context'];turn=context['turn_id'];session=Path('/home/dw/.codex/sessions/2026/11/14/rollout-2026-11-14T21-53-08-01a1da55-5881-7590-94a1-0661f0236977.jsonl');assert session.stat().st_size<16*1024*1024;rows={}
with session.open() as f:
 for line in f:
  o=json.loads(line);d=o.get('payload',{});item=d.get('item',{})
  if o.get('type')=='event_msg' and d.get('type')=='item_completed' and d.get('turn_id')==turn and item.get('type')=='CommandExecution':rows[item['id']]={'record_type':'NATIVE_COMMAND_COMPLETION','timestamp':o.get('timestamp'),'thread_id':d.get('thread_id'),'turn_id':turn,'started_at_ms':d.get('started_at_ms'),'completed_at_ms':d.get('completed_at_ms'),'item':item}
rows=sorted(rows.values(),key=lambda x:x.get('started_at_ms') or 0);assert rows
(R/'audit/NATIVE_COMMAND_COMPLETIONS.jsonl').write_text(''.join(json.dumps(row,ensure_ascii=False)+'\n' for row in rows))
w.save('audit/NATIVE_COMMAND_CAPTURE.json',{'utc':w.utc(),'source':str(session),'single_file_limit_bytes':16*1024*1024,'actual_session_bytes_at_capture':session.stat().st_size,'thread_id':'01a1da55-5881-7590-94a1-0661f0236977','turn_id':turn,'command_completions':len(rows),'first':rows[0]['timestamp'],'last':rows[-1]['timestamp'],'scope':'只复制本W004 turn的CommandExecution完成原件，保留command/cwd/status/output/exit/duration，不复制reasoning或其他turn。当前封存命令自身另记argv与关闭点；后续实际hash校验见FREEZE_RECEIPT。'})
closure={'record_type':'ARCHIVE_COMMAND_LOG_CLOSE','utc':w.utc(),'argv':sys.orig_argv,'pid':os.getpid(),'cwd':str(Path.cwd()),'status':'RUNNING_AT_LOG_CLOSE_BEFORE_HASH_SEAL','exit_code':None,'remaining_operations':'仅W004根内审计/结构校验、manifest/hash生成与实际复核、FREEZE_RECEIPT；源码tools/seal_archive.py归档，最终结果不伪造尚未返回exit。'}
(A/'COMMAND_LOG.jsonl').write_text(''.join(json.dumps(row,ensure_ascii=False)+'\n' for row in rows+[{'record_type':'EXPLICIT_SINGLE_R0A1_CHILD_COMMAND',**cmds[0]},closure]))
fd=os.open(w.LOCK,os.O_RDWR|os.O_NOFOLLOW)
try:
 try:fcntl.flock(fd,fcntl.LOCK_EX|fcntl.LOCK_NB)
 except BlockingIOError as e:assert e.errno in (errno.EAGAIN,errno.EACCES);competition={'errno':e.errno,'inode':os.fstat(fd).st_ino,'result':'FAILED_AS_REQUIRED'}
 else:raise RuntimeError('STOP unexpected lock acquisition')
finally:os.close(fd)
lock={'utc':w.utc(),'path':str(w.LOCK),'holder_pid':243622,'startticks':'47124402','inode':14806399,'controller_session':90041,'fdinfo':Path('/proc/243622/fdinfo/3').read_text(),'fresh_same_inode_competition':competition,'holder_modified_replaced_released':False};assert competition['inode']==14806399
binding=json.loads((A/'W004_BINDING.json').read_text());binding['additional_no_writer_evidence']={'predispatch_queue_empty':extra['queue']['data']==[],'predispatch_Goal_null':extra['goal']['goal'] is None,'prior_formal_W003_turn_completed':extra['turns'],'source':'input/W004-worker-pre-dispatch-state.json'};binding['post_attempt_lock']=lock;binding['actual_parent_stdin_receipt']='receipts/r0a1-parent-stdin.json';binding['actual_launcher_fd0']=launch['stdio_fds'][0];binding['inherited_competing_FD_closed']=launch['inherited_nonstdio_fds_closed'];binding['kernel_setup_succeeded_but_R0A_probe_not_PASS']=True;binding['global_zero_outside_writes_proven']=False;w.save('artifacts/W004_BINDING.json',binding)
files=[]
for directory,dirs,names in os.walk(R,followlinks=False):
 for name in dirs+names:assert not (Path(directory)/name).is_symlink()
 for name in names:files.append(Path(directory)/name)
assert len(files)<2000
surface={'record_type':'W004_WRITE_SURFACE_AUDIT','utc':w.utc(),'actual_new_business_root':str(R),'root_canonical':R.resolve()==R,'HOME':os.environ['HOME'],'CODEX_HOME':os.environ['CODEX_HOME'],'HOME_or_CODEX_HOME_reset':False,'explicit_task_directories':{n:str(R/n) for n in ['tmp','cache','config','logs','trace','audit','receipts','artifacts','probes']},'current_kernel_setup_for_single_attempt':{'ABI':6,'NNP_Landlock_seccomp_installed':True,'probe_body_ran':False,'bootstrap_exit_code':2},'single_trace_scope':{'process':244050,'lines':1518,'write_count':2,'write_bytes':4628,'success_outside_writes':0,'unknown_write_destinations':0,'proc_comm_open_write':0,'network_syscalls_or_destinations_requested_by_probe':0},'whole_W_or_future_global_zero_outside_writes_proven':False,'parent_control_scope':'原生控制命令写入均显式W004 root，未受本次trace的kernel restriction；原生平台会话按原执行器续写，不能据限定trace宣称全系统零写。','outside_probe_create_invocations':0,'negative_probes_body_executed':False,'controller_outside_preconfirmation':'656bytes回执已逐字复制；policy前Worker只复核回执，未尝试该外部create。','other4_negative_targets':'仅具名只读lstat ENOENT，未创建/写入/清理。','exact_input_after_checks':len(checks),'all_named_inputs_unchanged':True,'frozen_W003_no_mutations':True,'frozen_W003_verification_scope':'仅索引具名输入hash/mtime/inode；未广扫所有旧W3原件。','new_scene_normal_DBA_wrapper_reader_production_actions':0,'build_compile_serialization':0,'github_or_other_chat_writes':False,'fresh_lock_after_attempt':lock,'root_snapshot_before_outer_indexes':{'files':len(files),'logical_bytes':sum(p.stat().st_size for p in files),'allocated_bytes':sum(p.stat().st_blocks*512 for p in files)},'recursive_enumeration_scope':'仅W004新小根，file limit2000；不扫描BASE/HOME/cache，/m3varK/production完全未访问。'}
w.save('artifacts/WRITE_SURFACE_AUDIT.json',surface)
minimum=['WORKER_EXECUTION_REPORT.md','W004_BINDING.json','CONTROLLER_SENTINEL_PRECONFIRMATION.json','PARENT_LAUNCHER_WIRING_DELTA.json','WRITE_CONFINEMENT_REPORT.json','FULL_WRITE_TRACE_REVIEW.json','OFFLINE_CLOSURE_REPORT.json','RESOURCE_BUDGET_REPORT.json','PHASE0_RECOVERY_VERDICT.json','COMMAND_LOG.jsonl','WRITE_SURFACE_AUDIT.json','EP_ACCEPTANCE_MATRIX.md','ENGINEERING_STOP_REPORT.md','LOCAL_STAGE_HANDOFF.json'];assert all((A/n).is_file() for n in minimum)
for entry in handoff['deliverable_mapping']:
 assert entry['literal_ORDER_deliverable']==order['deliverables'][entry['index']-1]
 if entry['index']==10:
  for n in entry['conditional_files_not_created']:assert not (A/n).exists()
 elif entry['index']!=12:
  for p in entry['local_files']:
   if Path(p).name not in ['PUBLICATION_MANIFEST.json','HASHES.sha256']:assert Path(p).is_file()
assert not (A/'WORKER_RETURN.json').exists() and not (R/'WORKER_RETURN.json').exists()
parsed=collections.Counter()
for directory,dirs,names in os.walk(R,followlinks=False):
 for name in names:
  p=Path(directory)/name
  if p.suffix=='.json':json.loads(p.read_text());parsed['JSON']+=1
  elif p.suffix=='.jsonl':
   for line in p.read_text().splitlines():json.loads(line)
   parsed['JSONL']+=1
  elif p.suffix=='.py':ast.parse(p.read_text());parsed['Python_AST']+=1
w.save('artifacts/LOCAL_ARCHIVE_VALIDATION.json',{'utc':w.utc(),'status':'PASS_FOR_LOCAL_STOP_ARCHIVE_ONLY','minimum_STOP_files_present':minimum,'12_ORDER_deliverables_mapped':True,'outcome_STOP_and_PREFLIGHT_STOP':True,'specific_stop_verified':'ioctl(FIOCLEX) EPERM at trace1509 after O_RDONLY open success1508','readonly_parent_child_wiring_verified':True,'kernel6_API_setup_success_verified':True,'required_probes_not_run':True,'only_one_R0A1_no_retry':True,'runtime_launcher_hashes_unchanged_since_attempt':True,'sentinel_original_bytes_hash_preserved':True,'named_inputs_unchanged':len(checks),'parsed_files':dict(parsed),'conditional_or_Return_files_fabricated':False,'project_build_test_or_scenario_run':False,'native_completed_commands':len(rows),'hash_seal_check_result_location':'外层FREEZE_RECEIPT记录随后实际完成的hash复核；本PASS不是业务或四PASS。'})
# Freeze acyclic catalogs: payload -> PUBLICATION_MANIFEST -> HASHES -> receipt.
payload=[]
for directory,dirs,names in os.walk(R,followlinks=False):
 for name in names:payload.append(Path(directory)/name)
payload.sort();assert len(payload)<2000
prefix='longrun/runs/OI-EAW-WALL-20261114-01/delegations/D003/results/W004/'
def target(p):
 rel=p.relative_to(R);return prefix+str(Path(*rel.parts[1:]) if rel.parts[0]=='artifacts' else rel)
entries=[{'local_path':str(p),'relative_path':str(p.relative_to(R)),'target_path':target(p),'bytes':w.filefact(p)['bytes'],'sha256':w.filefact(p)['sha256'],'ref':None,'retention':'FROZEN_RUN_AUDIT_EVIDENCE'} for p in payload];assert len({e['target_path'] for e in entries})==len(entries)
trees=[]
for dirname in ['tools','input','logs','trace','audit','receipts','artifacts','tmp','cache','config','probes']:
 grouped=[e for e in entries if Path(e['local_path']).is_relative_to(R/dirname)];trees.append({'local_tree_path':str(R/dirname),'file_count':len(grouped),'logical_bytes':sum(e['bytes'] for e in grouped),'retention':'retain as frozen audit evidence; no large binary/cache/production export','stage_source_or_fixture':False})
manifest={'schema':'w004-local-publication-manifest/v1','utc':w.utc(),'run_id':order['run_id'],'work_order_id':'W004','outcome':'STOP','phase0_verdict':'PREFLIGHT_STOP','target_repo':'daowei2026/observe-iterate','target_branch':'runs/OI-EAW-WALL-20261114-01','target_prefix':prefix,'worker_github_writes':False,'real_publication_commit':None,'payload_file_count':len(entries),'payload_bytes':sum(e['bytes'] for e in entries),'files':entries,'local_tree_retention':trees,'conditional_source_build_fixture_trees':'NOT_CREATED_FOUR_PASS_NOT_MET','outer_catalogs_to_transport':[{'local_path':str(A/n),'target_path':prefix+n,'sha256_source':'manifest的hash在HASHES及FREEZE_RECEIPT；HASHES的hash在FREEZE_RECEIPT；receipt自hash由本聊天最终回报，避免循环自hash。'} for n in ['PUBLICATION_MANIFEST.json','HASHES.sha256','FREEZE_RECEIPT.json']],'deliverables':handoff['deliverable_mapping'],'missing':handoff['missing'],'formal_Return_ref':None,'formal_Return_transport_target':'longrun/runs/OI-EAW-WALL-20261114-01/worker_results/W004/WORKER_RETURN.json','return_to':order['return_to'],'transport_zh':'全部payload和三个外层目录文件逐字运输。artifacts文件发到目标根同名，其余相对路径保留。真实出版回读后再回传refs给原W1同W004，不伪造future/self ref。'}
w.save('artifacts/PUBLICATION_MANIFEST.json',manifest)
hashed=sorted(payload+[A/'PUBLICATION_MANIFEST.json']);(A/'HASHES.sha256').write_text(''.join(hashlib.sha256(p.read_bytes()).hexdigest()+'  '+str(p)+'\n' for p in hashed))
for e in entries:
 b=Path(e['local_path']).read_bytes();assert len(b)==e['bytes'] and hashlib.sha256(b).hexdigest()==e['sha256']
for line in (A/'HASHES.sha256').read_text().splitlines():
 h,p=line.split('  ',1);assert hashlib.sha256(Path(p).read_bytes()).hexdigest()==h
w.guard();all_files=sorted(payload+[A/'PUBLICATION_MANIFEST.json',A/'HASHES.sha256']);facts=[{**w.filefact(p),'target_path':target(p)} for p in all_files]
receipt={'record_type':'W004_FREEZE_RECEIPT','utc':w.utc(),'status':'FROZEN_LOCAL_STOP_ARCHIVE','outcome':'STOP','phase0_verdict':'PREFLIGHT_STOP','specific_stop':'PROBE_BOOTSTRAP_IOCTL_FIOCLEX_EPERM','payload_files_verified':len(payload),'HASHES_entries_verified':len(hashed),'files_to_transport_including_this_receipt':len(all_files)+1,'payload_plus_manifest_HASHES_bytes':sum(f['bytes'] for f in facts),'all_payload_bytes_hashes_rechecked':True,'target_paths_unique':True,'all_minimum_STOP_files_present':True,'12_literal_deliverables_mapped':True,'formal_Return_exists':False,'conditional_source_fixture_compile_files_exist':False,'return_to':order['return_to'],'real_publication_commit':None,'target_prefix':prefix,'manifest':w.filefact(A/'PUBLICATION_MANIFEST.json'),'HASHES':w.filefact(A/'HASHES.sha256'),'report':w.filefact(A/'WORKER_EXECUTION_REPORT.md'),'handoff':w.filefact(A/'LOCAL_STAGE_HANDOFF.json'),'all_files_except_this_receipt':facts,'this_receipt':{'local_path':str(A/'FREEZE_RECEIPT.json'),'target_path':prefix+'FREEZE_RECEIPT.json','self_hash':'正文不写循环自hash，最终由本聊天回报真实SHA256。'},'command_log_boundary':'已完成原生命令和唯一子命令完整日志＋当前封存argv/关闭点；本receipt记录随后实际完成的hash校验，不伪造关闭点尚未知的exit。','freeze_policy':'封存此根全部原件不回写，原W003保持冻结；待真实refs同单正式Return阶段。','business_acceptance_or_parent_completion_claim':False}
w.save('artifacts/FREEZE_RECEIPT.json',receipt)
print(json.dumps({'outcome':'STOP','phase0':'PREFLIGHT_STOP','specific_stop':receipt['specific_stop'],'payload_files':len(payload),'all_files_including_receipt':len(all_files)+1,'named_inputs_unchanged':len(checks),'all_new_files_total_bytes_including_receipt':sum(f['bytes'] for f in facts)+(A/'FREEZE_RECEIPT.json').stat().st_size,'files':{n:w.filefact(A/n) for n in ['WORKER_EXECUTION_REPORT.md','LOCAL_STAGE_HANDOFF.json','PUBLICATION_MANIFEST.json','HASHES.sha256','FREEZE_RECEIPT.json','PHASE0_RECOVERY_VERDICT.json','COMMAND_LOG.jsonl']},'missing':handoff['missing']},ensure_ascii=False,indent=2))
