from pathlib import Path
import sys,os,json,hashlib,ast,fcntl,errno,datetime,collections
ROOT=Path('/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D003/W003');sys.path.insert(0,str(ROOT/'tools'));import runtime as w
w.guard();A=ROOT/'artifacts';stamp=w.utc();assert not (A/'PUBLICATION_MANIFEST.json').exists() and not (A/'HASHES.sha256').exists() and not (A/'FREEZE_RECEIPT.json').exists()
order=json.loads((ROOT/'input/C0011-remote-work_orders--W003--ORDER.json').read_text());handoff=json.loads((A/'LOCAL_STAGE_HANDOFF.json').read_text());verdict=json.loads((A/'PHASE0_RECOVERY_VERDICT.json').read_text());trace=json.loads((A/'FULL_WRITE_TRACE_REVIEW.json').read_text());confinement=json.loads((A/'WRITE_CONFINEMENT_REPORT.json').read_text());launch=json.loads((ROOT/'receipts/r0a-positive-launcher.json').read_text())
assert handoff['outcome']==verdict['outcome']=='STOP' and verdict['phase0_verdict']=='PREFLIGHT_STOP' and len(handoff['deliverable_mapping'])==len(order['deliverables'])==11
assert order['return_to']==handoff['return_to']=='chatgpt:OI-EAW-WALL-20261114-01:executor:E1'
assert launch['calls']==[] and launch['status']=='LAUNCHER_FAILED' and not confinement['write_confinement_pass']
assert trace['successful_descriptor_write_count']==1 and trace['successful_descriptor_write_bytes']==1214 and trace['successful_outside_descriptor_writes_in_this_trace']==0 and not trace['successful_descriptor_writes_with_unknown_destination']
assert hashlib.sha256((ROOT/'tools/landlock_launcher.py').read_bytes()).hexdigest()==launch['script_sha256']=='a6586b1622017434ea6c27592d79ccd0a80735016939d0a3f532a6496bbe2479'
assert hashlib.sha256((ROOT/'tools/runtime.py').read_bytes()).hexdigest()=='30f268d6e6a144405dd4fba5d067924f71ba92170cf94313cd0ba24de17419b5'
for entry in handoff['deliverable_mapping']:
 if entry['index']==9:
  for name in entry['conditional_filenames_not_created']:assert not (A/name).exists()
assert not (A/'WORKER_RETURN.json').exists() and not (ROOT/'WORKER_RETURN.json').exists()
checks=[]
for old in json.loads((ROOT/'audit/READONLY_INPUTS_BEFORE.json').read_text()):
 now=w.filefact(old['path']);ok=all(now[k]==old[k] for k in ['bytes','sha256','mtime_ns','inode','dev']);assert ok;checks.append({'before':old,'after':now,'unchanged':ok})
w.save('audit/READONLY_INPUTS_AFTER.json',{'utc':stamp,'scope':'22 exact supplied input paths only; includes named W002 frozen inputs, not an all-files/global immutability proof.','count':len(checks),'all_unchanged':True,'checks':checks})
copychecks=[]
for item in json.loads((ROOT/'receipts/INPUT_HASH_AND_COPY_VERIFICATION.json').read_text())['items']:
 old=item['copy'];path=Path(old['local_path']);source=Path(item['source_path'] if 'source_path' in item else item['source']['local_readonly_path']);current=w.filefact(path);sf=w.filefact(source);ok=current['sha256']==sf['sha256']==old['sha256'] and current['bytes']==sf['bytes']==old['bytes'];assert ok;copychecks.append({'source':str(source),'copy':str(path),'sha256':current['sha256'],'bytes':current['bytes'],'current_source_matches_copy':ok})
owner=json.loads((ROOT/'input/RUN_BINDING.json').read_text());assert order['worker'] in owner['workers'] and order['grant'] in owner['grants']
for label,src in [('RUN_BINDING.json',Path('/dwdhome/fy/cgpterm/artifacts/oi-eaw-wall/OI-EAW-WALL-20261114-01/observe-iterate/longrun/runs/OI-EAW-WALL-20261114-01/RUN_BINDING.json')),('W003-worker-loaded-context.json',Path('/dwdhome/fy/cgpterm/artifacts/oi-eaw-wall/OI-EAW-WALL-20261114-01/W003-worker-loaded-context.json'))]:
 local=ROOT/'input'/label;lf=w.filefact(local);entry={'source':str(src),'copy':str(local),'sha256':lf['sha256'],'bytes':lf['bytes'],'source_available_at_final_check':src.is_file()}
 if src.is_file():sf=w.filefact(src);entry['current_source_matches_copy']=sf['sha256']==lf['sha256'] and sf['bytes']==lf['bytes']
 copychecks.append(entry)
w.save('audit/INPUT_COPY_FINAL_CHECK.json',{'utc':stamp,'32_initial_copies_match_current_sources':True,'additional_copies':2,'items':copychecks,'note':'原始22项镜像的 before/after metadata 另见 READONLY_INPUTS_AFTER；额外绑定/加载快照若主控更新，只保留时间点，不冒充未变。'})
# Capture only this turn's actual shell completions; no reasoning/session wholesale copy.
session=Path('/home/dw/.codex/sessions/2026/11/14/rollout-2026-11-14T21-53-08-01a1da55-5881-7590-94a1-0661f0236977.jsonl');assert session.stat().st_size<=16*1024*1024
turn='01a1dbbd-01ac-7d03-983d-2f655359abf4';thread='01a1da55-5881-7590-94a1-0661f0236977';completed={};contexts=[];numlines=0
with session.open() as f:
 for line in f:
  numlines+=1;o=json.loads(line);d=o.get('payload',{});item=d.get('item',{})
  if o.get('type')=='turn_context' and d.get('turn_id')==turn:contexts.append({'timestamp':o.get('timestamp'),**{k:d.get(k) for k in ['turn_id','cwd','model','effort','reasoning_effort']}})
  if o.get('type')=='event_msg' and d.get('type')=='item_completed' and d.get('turn_id')==turn and item.get('type')=='CommandExecution':completed[item['id']]={'timestamp':o.get('timestamp'),'thread_id':thread,'turn_id':turn,'started_at_ms':d.get('started_at_ms'),'completed_at_ms':d.get('completed_at_ms'),'item':item}
rows=sorted(completed.values(),key=lambda o:o.get('started_at_ms') or 0);assert rows and contexts[-1]['model']=='gpt-6.1-sol' and contexts[-1]['effort']=='max'
(ROOT/'audit/NATIVE_COMMAND_COMPLETIONS.jsonl').write_text(''.join(json.dumps(row,ensure_ascii=False)+'\n' for row in rows))
w.save('audit/NATIVE_COMMAND_CAPTURE.json',{'utc':w.utc(),'source':str(session),'exact_file_read_limit_bytes':16*1024*1024,'session_bytes_at_capture':session.stat().st_size,'lines_examined':numlines,'thread_id':thread,'turn_id':turn,'completed_commands':len(rows),'earliest':rows[0]['timestamp'],'latest':rows[-1]['timestamp'],'current_context':contexts[-1],'capture_scope':'当前 W003 turn 的实际已完成 CommandExecution，保留 command/cwd/status/exit/duration/aggregated_output。当前封存命令另记原 argv 及日志关闭点，封存校验结果见外层 receipt；不伪造尚未返回 exit code。','no_reasoning_or_other_turns_copied':True})
childrows=[json.loads(line) for line in (ROOT/'logs/COMMAND_LOG.jsonl').read_text().splitlines()];assert len(childrows)==2 and [row['id'] for row in childrows]==['strace-supported-options','r0a-positive']
logrows=[{'record_type':'NATIVE_CONTROL_COMMAND_COMPLETION',**row} for row in rows]+[{'record_type':'EXPLICIT_CHILD_COMMAND_WITH_FULL_OUTPUT_FILES',**row} for row in childrows]
logrows.append({'record_type':'FINALIZATION_COMMAND_LOG_CLOSE','utc':w.utc(),'pid':os.getpid(),'argv':sys.orig_argv,'cwd':str(Path.cwd()),'HOME':os.environ['HOME'],'CODEX_HOME':os.environ['CODEX_HOME'],'HOME_or_CODEX_HOME_reset':False,'status':'RUNNING_AT_LOG_CLOSE_BEFORE_HASH_SEAL','exit_code':None,'remaining_operations':'根内一致性校验、manifest/HASHES 生成并逐字节复核、外层 FREEZE_RECEIPT；完整执行源码 tools/finalize_archive.py 已归档，实际结果存 FREEZE_RECEIPT，不将未知未来 exit code 写成0。'})
(A/'COMMAND_LOG.jsonl').write_text(''.join(json.dumps(row,ensure_ascii=False)+'\n' for row in logrows))
fd=os.open(w.LOCK,os.O_RDWR|os.O_NOFOLLOW)
try:
 try:fcntl.flock(fd,fcntl.LOCK_EX|fcntl.LOCK_NB)
 except BlockingIOError as exc:competition={'errno':exc.errno,'result':'FAILED_AS_REQUIRED','inode':os.fstat(fd).st_ino}
 else:raise RuntimeError('STOP unexpected lock acquisition')
finally:os.close(fd)
assert competition['inode']==14806399
existing=[]
for directory,dirs,files in os.walk(ROOT,followlinks=False):
 for name in dirs+files:assert not (Path(directory)/name).is_symlink()
 for name in files:existing.append(Path(directory)/name)
assert len(existing)<2000
surface={'record_type':'W003_WRITE_SURFACE_AUDIT','utc':w.utc(),'actual_new_business_write_root':str(ROOT),'canonical_root':str(ROOT.resolve()),'scope':'本 W 原生控制命令和新根文件、唯一失败 launcher 的完整 trace；没有全系统写审计或未执行后继 kernel confinement 的证明。','HOME':'/home/dw','CODEX_HOME':'/home/dw/.codex','HOME_or_CODEX_HOME_reset':False,'task_tmp_cache_config_log':{k:str(ROOT/k) for k in ['tmp','cache','config','logs','trace','audit','receipts','artifacts']},'traced_successful_descriptor_writes':1,'traced_successful_descriptor_write_bytes':1214,'traced_outside_successful_writes':0,'traced_unknown_write_paths':0,'traced_proc_comm_open_or_write':0,'global_business_outside_writes_proven_zero':False,'kernel_enforcement_established':False,'outside_inherited_FD_issue':{'fd0':'/dev/null O_RDWR rejected before enforcement, no write observed','fd3':'Separate contending lock FD; no lock acquired or write; parent finally close. Holder FD/lock untouched.'},'negative_probe_invocations':0,'no_external_negative_probe_created_files_claim_scope':'未执行任何负向 create/open，不能把未确认 sentinel 的当前存在性写为已知。','readonly_22_named_inputs_unchanged':True,'initial_32_input_copies_match_sources':True,'frozen_W002_scope':'从不回写、清理或补写 W002；这里只核指定输入子集，未扫描全299原件。','source_checkout_or_production_writes_by_requested_commands':0,'scenario_runs':0,'compile_runs':0,'serialization_runs':0,'network_download_install_calls_requested':0,'native_platform_session':'平台沿既有执行器写原生会话；Worker 仅读取精确 session 的本 turn CommandExecution/turn_context。未将 HOME/CODEX_HOME 用作业务写面，也未据此宣称全局零外写。','snapshot_before_index_seal':{'files':len(existing),'logical_bytes':sum(p.stat().st_size for p in existing),'allocated_bytes':sum(p.stat().st_blocks*512 for p in existing)},'fresh_controller_lock':{'holder_pid':240810,'startticks':'46501758','inode':14806399,'fdinfo':Path('/proc/240810/fdinfo/3').read_text(),'competition':competition,'replaced_released_or_acquired':False},'whole_new_root_small_enumeration_limit':2000,'no_BASE_HOME_cache_recursive_search':True}
w.save('artifacts/WRITE_SURFACE_AUDIT.json',surface)
minimum=['WORKER_EXECUTION_REPORT.md','W003_BINDING.json','WRITE_CONFINEMENT_REPORT.json','FULL_WRITE_TRACE_REVIEW.json','OFFLINE_CLOSURE_REPORT.json','RESOURCE_BUDGET_REPORT.json','PHASE0_RECOVERY_VERDICT.json','COMMAND_LOG.jsonl','WRITE_SURFACE_AUDIT.json','EP_ACCEPTANCE_MATRIX.md','ENGINEERING_STOP_REPORT.md','LOCAL_STAGE_HANDOFF.json']
assert all((A/name).is_file() for name in minimum)
for m in handoff['deliverable_mapping']:
 if m['index'] not in (9,11):
  for path in m['local_files']:
   if Path(path).name not in ['PUBLICATION_MANIFEST.json','HASHES.sha256']:assert Path(path).is_file()
jsoncount=jsonlcount=pycount=0
for directory,dirs,files in os.walk(ROOT,followlinks=False):
 for name in files:
  p=Path(directory)/name
  if p.suffix=='.json':json.loads(p.read_text());jsoncount+=1
  elif p.suffix=='.jsonl':
   for line in p.read_text().splitlines():json.loads(line)
   jsonlcount+=1
  elif p.suffix=='.py':ast.parse(p.read_text());pycount+=1
validation={'record_type':'W003_LOCAL_ARCHIVE_VALIDATION','utc':w.utc(),'status':'PASS_FOR_LOCAL_STOP_ARCHIVE_ONLY','project_build_or_test_run':False,'work_order_identity_and_return_to_match':True,'outcome_STOP_and_phase0_PREFLIGHT_STOP':True,'four_recovery_requirements_not_PASS':True,'11_literal_order_deliverables_mapped':True,'required_STOP_payload_files_present':minimum,'conditional_artifacts_or_formal_Return_fabricated':False,'launcher_and_runtime_hashes_unchanged_after_failure':True,'input22_hash_metadata_unchanged':True,'initial32_copies_match_sources':True,'helper_Python_files_AST_parsed':pycount,'JSON_files_parsed_before_seal':jsoncount,'JSONL_files_parsed_before_seal':jsonlcount,'completed_native_commands_captured':len(rows),'explicit_child_commands':len(childrows),'nonengineering_archival_preparation_errors_preserved':['写报告脚本外层引号造成 SyntaxError，首次未写文件；随后一次执行找不到该脚本。只恢复报告脚本文本并完成归档，没有重跑 R0-A。','write_reports stdout reports_generated=9 是辅助计数错误，实际该脚本新写8个报告文件；实际完整文件数以本封存清单为准。'],'hash_seal_validation':'实际逐文件结果在外层 FREEZE_RECEIPT。该本地一致性 PASS 不等于 confinement/closure/预算/EP/业务 PASS。'}
w.save('artifacts/LOCAL_ARCHIVE_VALIDATION.json',validation)
# Acyclic publication catalogs: payload -> manifest -> HASHES -> outer receipt.
payload=[]
for directory,dirs,files in os.walk(ROOT,followlinks=False):
 for name in files:
  p=Path(directory)/name;assert not p.is_symlink();payload.append(p)
payload.sort();assert len(payload)<2000
prefix='longrun/runs/OI-EAW-WALL-20261114-01/delegations/D003/results/W003/'
def target(p):
 rel=p.relative_to(ROOT);parts=rel.parts
 return prefix+str(Path(*parts[1:]) if parts[0]=='artifacts' else rel)
entries=[]
for p in payload:
 fact=w.filefact(p);entries.append({'local_path':str(p),'relative_path':str(p.relative_to(ROOT)),'target_path':target(p),'bytes':fact['bytes'],'sha256':fact['sha256'],'ref':None})
assert len({entry['target_path'] for entry in entries})==len(entries)
outer_names=['PUBLICATION_MANIFEST.json','HASHES.sha256','FREEZE_RECEIPT.json']
manifest={'schema':'w003-local-publication-manifest/v1','utc':w.utc(),'run_id':order['run_id'],'work_order_id':'W003','outcome':'STOP','phase0_verdict':'PREFLIGHT_STOP','target_repo':'daowei2026/observe-iterate','target_branch':'runs/OI-EAW-WALL-20261114-01','target_prefix':prefix,'github_publication_performed_by_worker':False,'real_publication_commit':None,'payload_file_count':len(entries),'payload_bytes':sum(x['bytes'] for x in entries),'files':entries,'outer_catalogs_to_transport':[{'local_path':str(A/name),'target_path':prefix+name,'sha256_source':'PUBLICATION_MANIFEST 的 hash 在 HASHES 和 FREEZE_RECEIPT；HASHES 的 hash 在 FREEZE_RECEIPT；FREEZE_RECEIPT 自 hash 从本聊天最终交付读取，避免循环自 hash。'} for name in outer_names],'deliverables':handoff['deliverable_mapping'],'missing':handoff['missing'],'formal_Return_ref':None,'formal_Return_transport_target':'longrun/runs/OI-EAW-WALL-20261114-01/worker_results/W003/WORKER_RETURN.json','return_to':order['return_to'],'transport_instructions_zh':'payload 与3个外层目录文件全部逐字运输。artifacts 文件映射到目标根同名；其他相对路径保留。出版后真实回读对照 bytes/SHA256，再回传真实 refs 给原W1同W003。不要把本地路径/未存在 commit 当精确 GitHub ref。'}
w.save('artifacts/PUBLICATION_MANIFEST.json',manifest)
hashed=payload+[A/'PUBLICATION_MANIFEST.json'];hashed.sort();(A/'HASHES.sha256').write_text(''.join(hashlib.sha256(p.read_bytes()).hexdigest()+'  '+str(p)+'\n' for p in hashed))
for entry in entries:
 p=Path(entry['local_path']);b=p.read_bytes();assert len(b)==entry['bytes'] and hashlib.sha256(b).hexdigest()==entry['sha256']
for line in (A/'HASHES.sha256').read_text().splitlines():
 digest,path=line.split('  ',1);assert hashlib.sha256(Path(path).read_bytes()).hexdigest()==digest
assert len((A/'HASHES.sha256').read_text().splitlines())==len(payload)+1
w.guard()
all_except_receipt=sorted(payload+[A/'PUBLICATION_MANIFEST.json',A/'HASHES.sha256']);facts=[w.filefact(p) for p in all_except_receipt]
receipt={'record_type':'W003_FREEZE_RECEIPT','utc':w.utc(),'status':'FROZEN_LOCAL_STOP_ARCHIVE','run_id':order['run_id'],'work_order_id':'W003','outcome':'STOP','phase0_verdict':'PREFLIGHT_STOP','primary_stop_reason':'RECOVERY_STOP_WRITE_CONFINEMENT','payload_files_verified':len(payload),'hashes_entries_verified':len(hashed),'files_to_transport_including_this_receipt':len(all_except_receipt)+1,'payload_plus_manifest_HASHES_bytes':sum(x['bytes'] for x in facts),'all_payload_bytes_and_hashes_rechecked':True,'target_paths_unique':True,'all_minimum_STOP_files_present':True,'deliverable_count':11,'formal_Return_exists':False,'conditional工程_files_exist':False,'return_to':order['return_to'],'publication_commit':None,'transport_target_prefix':prefix,'manifest':w.filefact(A/'PUBLICATION_MANIFEST.json'),'HASHES':w.filefact(A/'HASHES.sha256'),'report':w.filefact(A/'WORKER_EXECUTION_REPORT.md'),'handoff':w.filefact(A/'LOCAL_STAGE_HANDOFF.json'),'all_files_except_this_receipt':[{**fact,'target_path':target(Path(fact['path']))} for fact in facts],'this_receipt':{'path':str(A/'FREEZE_RECEIPT.json'),'target_path':prefix+'FREEZE_RECEIPT.json','self_hash':'不在自身正文内伪造。由本聊天最终回报外层 SHA256。'},'finalization_log_boundary':'COMMAND_LOG 包含此前所有已完成原生命令、本次子命令完整原件和当前封存 argv/关闭点；本 receipt 记录随后实际完成的 hash/seal 校验，不捏造当时尚未知的 shell exit。','freeze_policy':'本阶段到此封存，不回写现有 payload、manifest、HASHES 或旧 W002；未来仅同单真实 refs/正式 Return 续接。','business_acceptance_claim':False}
w.save('artifacts/FREEZE_RECEIPT.json',receipt)
print(json.dumps({'outcome':'STOP','phase0_verdict':'PREFLIGHT_STOP','payload_files':len(payload),'all_files_including_receipt':len(all_except_receipt)+1,'completed_native_commands':len(rows),'files':{name:w.filefact(A/name) for name in ['WORKER_EXECUTION_REPORT.md','LOCAL_STAGE_HANDOFF.json','PUBLICATION_MANIFEST.json','HASHES.sha256','FREEZE_RECEIPT.json','PHASE0_RECOVERY_VERDICT.json','COMMAND_LOG.jsonl']},'missing':handoff['missing']},ensure_ascii=False,indent=2))
