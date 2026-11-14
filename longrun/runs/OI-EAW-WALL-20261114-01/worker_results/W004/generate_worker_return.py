from pathlib import Path
import os,sys,json,hashlib,fcntl,errno,datetime,runpy,ast
BASE=Path('/dwdhome/fy/BASE_E6_2');ROOT=BASE/'.oi-runs/OI-EAW-WALL-20261114-01/D003/W004';FINAL=ROOT/'final-return';C=Path('/dwdhome/fy/cgpterm/artifacts/oi-eaw-wall/OI-EAW-WALL-20261114-01');LOCK=ROOT.parents[1]/'.D003-writer.lock';COMMIT='23b4070f171af4442ddc83b663814f3349739c67';PREFIX='longrun/runs/OI-EAW-WALL-20261114-01/delegations/D003/results/W004/';ORDER_REF='daowei2026/observe-iterate@347e4b2322ff2401aca21333cd3118f93d490baf:longrun/runs/OI-EAW-WALL-20261114-01/work_orders/W004/ORDER.json'
def utc():return datetime.datetime.now(datetime.timezone.utc).isoformat()
def load(path):return json.loads(Path(path).read_text())
def fact(path):
 p=Path(path);b=p.read_bytes();s=p.stat();return {'path':str(p),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'mtime_ns':s.st_mtime_ns,'inode':s.st_ino,'dev':s.st_dev}
def save(name,value):
 p=FINAL/name;assert p.parent==FINAL and p.resolve().is_relative_to(FINAL);p.write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n');return p

def guard():
 assert Path.cwd()==BASE and FINAL.resolve()==FINAL and not any(p.is_symlink() for p in [FINAL,*FINAL.parents]);assert sys.flags.isolated and sys.dont_write_bytecode;assert os.environ['HOME']=='/home/dw' and os.environ['CODEX_HOME']=='/home/dw/.codex'
 s=Path('/proc/243622/stat').read_text();assert s[s.rfind(')')+2:].split()[19]=='47124402' and LOCK.lstat().st_ino==14806399;info=Path('/proc/243622/fdinfo/3').read_text();assert 'FLOCK' in info and 'WRITE 243622' in info
 fd=os.open(LOCK,os.O_RDWR|os.O_NOFOLLOW)
 try:
  assert os.fstat(fd).st_ino==14806399
  try:fcntl.flock(fd,fcntl.LOCK_EX|fcntl.LOCK_NB)
  except BlockingIOError as e:assert e.errno in (errno.EAGAIN,errno.EACCES);denial=e.errno
  else:raise RuntimeError('STOP unexpected acquisition')
 finally:os.close(fd)
 return {'utc':utc(),'path':str(LOCK),'holder_pid':243622,'startticks':'47124402','inode':14806399,'controller_session':90041,'fdinfo':info,'same_inode_competition_errno':denial,'holder_modified_replaced_released':False}

def verify_publication(publication):
 assert publication['state']=='PUBLISHED_REMOTE_BYTE_VERIFIED' and publication['commit']==COMMIT and publication['repository']=='daowei2026/observe-iterate' and publication['branch']=='runs/OI-EAW-WALL-20261114-01' and publication['all_71_byte_equal'] and publication['only_allowed_new_paths'] and publication['originals_frozen_unchanged'] and publication['outcome']=='STOP'
 assert len(publication['files'])==71 and publication['bytes']==1267664
 assert len({e['ref'] for e in publication['files']})==len({e['path'] for e in publication['files']})==len({e['local_path'] for e in publication['files']})==71
 for e in publication['files']:
  p=Path(e['local_path']);assert p.resolve()==p and p.is_relative_to(ROOT) and not p.is_relative_to(FINAL) and not p.is_symlink();assert e['path'].startswith(PREFIX) and e['ref']=='daowei2026/observe-iterate@'+COMMIT+':'+e['path'];assert e['byte_equal'] and e['verified'] and e['error'] is None and e['remote_blob_sha']==e['git_blob_sha']

def generate():
 first_lock=guard();pref=load(FINAL/'FINALIZE_PREFLIGHT.json');publication=load(C/'W004-published-refs.json');verify_publication(publication);assert fact(C/'W004-published-refs.json')['sha256']==pref['publication_receipt']['sha256']=='08c9327d26b1817bde92dd1661cc71c85c7626b334932f09d480cf74a9a90fb3';assert len(pref['frozen_files'])==71
 expected={'WORKER_FINALIZE_TASK-W004.md':'6af422a43ab56644810ad237cf826f0758694dfbb1f72fae62acc1be7adc16c5','C0012-remote-work_orders--W004--ORDER.json':'0cf827e6790ef8a6a8ee36f158138df69b1590fefd0a3fe4683078ce07ea301a','C0012-remote-work_orders--W004--ORDER.md':'a30fcf2db5a8bf02dc98544b689ae0dfb5d8d3fed40811e13ed62ee9244b8b94','observe-iterate/longrun/contracts/LONGRUN_PROTOCOL_V2.md':'86ad342ca0aef9f28449dd9ec9168bba465f60a4ef552634b553573491a38c39','observe-iterate/longrun/contracts/longrun_schema_v2.json':'32c1e2409ff4936a87d688848736bb9af71fe0415d338ba66dd031e3149243d3','observe-iterate/longrun/tools/longrun_gate.py':'0bb6bdceadcb52f7697b52de2b3356664a9d381570f791e62d6d2b3ae2d8d680'}
 for name,digest in expected.items():assert fact(C/name)['sha256']==digest
 order=load(C/'C0012-remote-work_orders--W004--ORDER.json');binding=load(ROOT/'input/RUN_BINDING.json');handoff=load(ROOT/'artifacts/LOCAL_STAGE_HANDOFF.json');verdict=load(ROOT/'artifacts/PHASE0_RECOVERY_VERDICT.json');confinement=load(ROOT/'artifacts/WRITE_CONFINEMENT_REPORT.json');trace=load(ROOT/'artifacts/FULL_WRITE_TRACE_REVIEW.json')
 assert order['run_id']==handoff['run_id']=='OI-EAW-WALL-20261114-01' and order['work_order_id']=='W004' and order['issuer_call_id']=='C0012' and handoff['order_ref']==ORDER_REF;assert order['worker']==handoff['worker']=='codex:OI-EAW-WALL-20261114-01:worker:W1' and order['return_to']==order['issuer']==handoff['return_to']=='chatgpt:OI-EAW-WALL-20261114-01:executor:E1'
 assert handoff['outcome']==verdict['outcome']=='STOP' and verdict['verdict']=='PREFLIGHT_STOP' and verdict['specific_stop']=='PROBE_BOOTSTRAP_IOCTL_FIOCLEX_EPERM';assert not verdict['R0_B_entered'] and not verdict['R0_C_entered'] and not verdict['Phase1_2_entered'] and not verdict['automatic_retry'] and verdict['scenario_runs']==verdict['build_compile_serialization_runs']==0
 assert confinement['kernel_policy_setup_calls_success'] and confinement['ABI_observed']==6 and confinement['parent_child_readonly_stdin_wiring_pass'] and confinement['controller_sentinel_preconfirmation_pass'];assert len(confinement['kernel_calls'])==6 and all(c['errno']==0 and c['return']>=0 for c in confinement['kernel_calls']);assert confinement['single_attempt']['count']==1 and confinement['single_attempt']['exit_code']==2 and not confinement['single_attempt']['probe_script_body_entered'] and not confinement['single_attempt']['automatic_retry_or_parameter_change'];assert not confinement['WRITE_CONFINEMENT_PASS'] and not confinement['global_or_future_zero_outside_writes_proven'];assert trace['successful_descriptor_write_count']==2 and trace['successful_descriptor_write_bytes']==4628 and trace['successful_outside_descriptor_writes_in_this_trace']==0 and trace['fatal_script_bootstrap_ioctl']['line']==1509
 by_local={e['local_path']:e for e in publication['files']};by_ref={e['ref']:e for e in publication['files']};manifest={e['path']:{'ref':e['ref'],'sha256':e['sha256']} for e in publication['files']};aliases=[];deferred=[]
 assert len(order['deliverables'])==len(handoff['deliverable_mapping'])==12
 for literal,entry in zip(order['deliverables'],handoff['deliverable_mapping']):
  assert literal==entry['literal_ORDER_deliverable'];index=entry['index']
  if index in (10,12):deferred.append({'index':index,'literal':literal,'reason':'四PASS未满足，未产出条件工程文件。' if index==10 else '本阶段正式Return本地生成，其本身尚无真实出版ref；不能自引用。'});continue
  paths=entry['local_files'];assert paths and all(p in by_local for p in paths);selected=next((p for p in paths if p.endswith('/PUBLICATION_MANIFEST.json')),paths[0]);e=by_local[selected];assert literal not in manifest;manifest[literal]={'ref':e['ref'],'sha256':e['sha256']};aliases.append({'literal_ORDER_label':literal,'index':index,'selected_real_file':selected,'ref':e['ref'],'sha256':e['sha256'],'all_actual_members':[{'local_path':p,'ref':by_local[p]['ref'],'sha256':by_local[p]['sha256']} for p in paths],'group_mapping_note':'组合标签仅用一个真实报告/索引作别名，全部成员同时以完整target相对名分别列入manifest；未伪造多文件hash。' if len(paths)>1 else '逐字标签对应实际单文件。'})
 assert len(manifest)==81 and len(aliases)==10
 missing=[]
 for item in handoff['missing']:
  if item['id'] in ('M-PUBLICATION','M-FORMAL-RETURN'):continue
  detail=item['detail']
  if item['id']=='M-R0A1-BOOTSTRAP':detail+=' 显式O_RDONLY父子接线和主控sentinel回执已补齐；第二execve以及脚本O_RDONLY open/read成功。fatal是其后FIOCLEX ioctl被候选seccomp整体ioctl禁令拒绝，不是Landlock不支持或script open/read被拒。本次收尾没有重新调查/运行R0。'
  if item['id']=='M-REQUIRED-PROBES':detail+=' 1518行唯一trace内两个成功write共4628bytes均在W004，只能接受该限域映射，不能扩成全局零外写或业务PASS。'
  missing.append(item['id']+'：'+detail)
 ep_gaps=[('EP-WALL-SHARED-01','NOT_ATTEMPTED；无新snapshot/accessor、patch/typecheck/只读性质测试'),('EP-WALL-SHARED-02','NOT_ATTEMPTED；无新one-record-per-firing DTO/schema/canonical bytes/roundtrip/stable hash'),('EP-WALL-SHARED-03','UNSATISFIED；只有接线/sentinel/kernel setup成功子事实，必需probe/单一closure/四预算/monitor未证'),('EP-SCENARIO-01','NOT_ATTEMPTED；无新dedicated target/component/main/manifest/compile-only'),('EP-SCENARIO-02','NOT_ATTEMPTED；无exact-error constructor/payload adapter及direct synthetic serialization'),('EP-SCENARIO-03','NOT_ATTEMPTED；无transaction DTO、pre/post A和committed/uncommitted限定serialization验证'),('EP-SCENARIO-04','仅继承C0012 E1对旧ledger的PARTIAL静态子集；无新target manifest或current result，不冒充本W专业接受'),('EP-SCENARIO-05','NOT_ATTEMPTED；未物化完整9/18/22 fixture，无schema/input/static count/order/hash，fixture执行0')]
 missing.extend(name+'：'+text for name,text in ep_gaps)
 missing.append(order['deliverables'][9]+'：四PASS未成立，Phase1/2未进入；未产出 '+', '.join(handoff['deliverable_mapping'][9]['conditional_files_not_created'])+'，不造空文件/ref。')
 missing.append(order['deliverables'][11]+'：本阶段已生成正式V2 Return本地文件；新增Return/validation/generator/COMMAND_LOG/PREFLIGHT尚未出版，不能列出未来或self ref。主控须逐字运输至longrun/runs/OI-EAW-WALL-20261114-01/worker_results/W004/WORKER_RETURN.json及同目录validation等，再以真实Return ref/独立receipt做完整validate-worker-return并送原E1。71份证据出版已解决，旧冻结pending为历史不回写；不冒称业务接受。')
 assert len(missing)==len(set(missing))==16
 report=by_local[str(ROOT/'artifacts/WORKER_EXECUTION_REPORT.md')];assert report['sha256']=='fe9fcab560df1cdb792d77996beb2c69754534a1cd91a864e2154ef5bfb5da6b'
 result={'schema':'longrun-worker-return/v2','run_id':order['run_id'],'work_order_id':'W004','order_ref':ORDER_REF,'worker':order['worker'],'return_to':order['issuer'],'outcome':'STOP','result_ref':report['ref'],'missing':missing,'manifest':manifest}
 gate=runpy.run_path(str(C/'observe-iterate/longrun/tools/longrun_gate.py'));gate['validated']('worker_return',result);gate['validated']('order',order);gate['validated']('binding',binding);gate['exact_path'](ORDER_REF,order['run_id'],'work_orders/W004/ORDER.json');assert result['worker'] in binding['workers'] and result['return_to'] in binding['executors'] and any(gate['grant_covers'](g,order['grant']) for g in binding['grants'])
 manifest_checks=[]
 for key,value in manifest.items():
  assert set(value)=={'ref','sha256'};gate['ref_parts'](value['ref']);e=by_ref[value['ref']];assert e['sha256']==value['sha256'];assert not e['path'].startswith('longrun/runs/OI-EAW-WALL-20261114-01/worker_results/W004/');manifest_checks.append({'key':key,**value,'source_local_path':e['local_path'],'matches_actual_publication_receipt':True})
 output=FINAL/'WORKER_RETURN.json';assert not output.exists();save('WORKER_RETURN.json',result);gate['validated']('worker_return',load(output))
 # After generation, verify the exact 71 frozen original files against preflight and publication metadata.
 before={e['path']:e for e in pref['frozen_files']};unchanged=[]
 for e in publication['files']:
  p=Path(e['local_path']);after=fact(p);old=before[str(p)];assert all(after[k]==old[k]==e[k] for k in ['bytes','sha256','mtime_ns','inode','dev']);blob=hashlib.sha1(('blob '+str(after['bytes'])+'\0').encode()+p.read_bytes()).hexdigest();assert blob==e['git_blob_sha']==e['remote_blob_sha'];unchanged.append({'local_path':str(p),'ref':e['ref'],'before':old,'after':after,'git_blob_sha':blob,'content_and_metadata_unchanged':True})
 assert len(unchanged)==71 and sum(e['after']['bytes'] for e in unchanged)==1267664
 validation={'record_type':'W004_FORMAL_RETURN_LOCAL_VALIDATION','utc':utc(),'status':'PASS_FOR_SCHEMA_IDENTITY_MANIFEST_AND_LOCAL_TRANSPORT_ONLY','outcome':'STOP','return_to':result['return_to'],'run_id':result['run_id'],'work_order_id':'W004','order_ref':ORDER_REF,'worker_return':fact(output),'result_ref':result['result_ref'],'result_sha256':report['sha256'],'actual_context':pref['actual_context'],'current_owner_pid':pref['owner_pid'],'current_owner_startticks':pref['owner_startticks'],'schema_validation':{'pass':True,'method':'官方longrun_gate.py validated(worker_return/order/binding)，Draft202012Validator，Python-I-B，不联网、不写pycache。','source':fact(C/'observe-iterate/longrun/tools/longrun_gate.py'),'schema':fact(C/'observe-iterate/longrun/contracts/longrun_schema_v2.json'),'protocol':fact(C/'observe-iterate/longrun/contracts/LONGRUN_PROTOCOL_V2.md')},'full_validate_worker_return_gate':{'status':'NOT_INVOKED_AWAITING_REAL_RETURN_REF_AND_RECEIPT','reason':'当前Return自身尚未出版；官方完整Gate需要真实worker_return_ref/独立worker_receipt及主控可信快照，不伪造future/self ref或receipt。主控出版后核真再调用。'},'publication_receipt':fact(C/'W004-published-refs.json'),'finalize_task':fact(C/'WORKER_FINALIZE_TASK-W004.md'),'publication_verification_scope':'使用主控真远端逐字/Gitblob回执，本Worker核全部本地bytes/hash/Gitblob/mtime/inode/dev；未联网再读。','resolved_missing':[{'id':'M-PUBLICATION','status':'RESOLVED','commit':COMMIT,'files':71,'bytes':1267664,'historical_pending_in_frozen_files':'保持原件不回写'}],'substantive_missing_preserved':True,'missing_count':len(missing),'missing':missing,'manifest_total':81,'unique_published_file_entries':71,'applicable_literal_deliverable_aliases':10,'manifest_entries':manifest_checks,'deliverable_alias_mappings':aliases,'deliverables_without_self_or_conditional_alias':deferred,'no_future_or_self_refs':True,'kernel_installed_in_original_attempt':True,'original_Landlock_ABI':6,'original_setup_API_errno_zero':True,'readonly_stdin_and_sentinel_preconditions_resolved':True,'original_attempts':1,'original_bootstrap_exit_code':2,'original_retry':False,'probe_body_executed':False,'original_trace_scope':{'lines':1518,'successful_write_count':2,'successful_write_bytes':4628,'scope_only_outside_write0_not_global':True},'confinement_or_business_PASS_claim':False,'new_investigation_R0_build_compile_serialization_scenario_production_actions':0,'8_exact_git_source_objects_read_this_W004':False,'frozen_originals':{'count':71,'bytes':1267664,'all_bytes_sha256_gitblob_mtime_inode_dev_unchanged':True,'checks':unchanged},'HOME':os.environ['HOME'],'CODEX_HOME':os.environ['CODEX_HOME'],'HOME_or_CODEX_HOME_reset':False,'new_business_write_root':str(FINAL),'exclusive_lock_before':first_lock,'exclusive_lock_after':guard(),'github_or_other_chat_writes':False,'formal_return_transport_target':'longrun/runs/OI-EAW-WALL-20261114-01/worker_results/W004/WORKER_RETURN.json','validation_transport_target':'longrun/runs/OI-EAW-WALL-20261114-01/worker_results/W004/WORKER_RETURN_VALIDATION.json','business_acceptance_D3_H3_G_RUN_parent_Q_or_completion_decision':False,'command_log_status':'待本生成命令真实退出后封存当前turn的完整CommandExecution和封存argv，不伪造exit。'}
 save('WORKER_RETURN_VALIDATION.json',validation);print(json.dumps({'outcome':'STOP','schema_local_validation':'PASS','manifest_total':81,'files':71,'aliases':10,'missing':16,'frozen71_bytes_hash_mtime_inode_unchanged':True,'outputs':[fact(output),fact(FINAL/'WORKER_RETURN_VALIDATION.json')]},ensure_ascii=False,indent=2))

def seal_log():
 guard();pref=load(FINAL/'FINALIZE_PREFLIGHT.json');turn=pref['actual_context']['turn_id'];session=Path('/home/dw/.codex/sessions/2026/11/14/rollout-2026-11-14T21-53-08-01a1da55-5881-7590-94a1-0661f0236977.jsonl');assert session.stat().st_size<16*1024*1024;records={}
 with session.open() as f:
  for line in f:
   o=json.loads(line);d=o.get('payload',{});item=d.get('item',{})
   if o.get('type')=='event_msg' and d.get('type')=='item_completed' and d.get('turn_id')==turn and item.get('type')=='CommandExecution':records[item['id']]={'record_type':'NATIVE_COMMAND_COMPLETION','timestamp':o.get('timestamp'),'thread_id':d.get('thread_id'),'turn_id':turn,'started_at_ms':d.get('started_at_ms'),'completed_at_ms':d.get('completed_at_ms'),'item':item}
 rows=sorted(records.values(),key=lambda e:e.get('started_at_ms') or 0);generated=[]
 for row in rows:
  cmd=row['item'].get('command');argv=ast.literal_eval(cmd) if isinstance(cmd,str) else cmd
  if isinstance(argv,list) and argv[-1].strip()=='PYTHONDONTWRITEBYTECODE=1 /usr/bin/python3.12 -I -B '+str(FINAL/'generate_worker_return.py'):generated.append(row)
 assert generated and generated[-1]['item']['exit_code']==0
 closing={'record_type':'FINAL_COMMAND_LOG_CLOSE','utc':utc(),'argv':sys.orig_argv,'pid':os.getpid(),'cwd':str(Path.cwd()),'status':'RUNNING_AT_LOG_CLOSE','exit_code':None,'note':'此前所有本turn已完成命令/完整aggregated_output及当前封存argv；后续仅F内日志和validation补记真实生成exit0/日志hash/打印最终文件hash。完整代码已归档，不伪造当前未知exit或未来self ref。'}
 log=FINAL/'COMMAND_LOG.jsonl';assert not log.exists();log.write_text(''.join(json.dumps(row,ensure_ascii=False)+'\n' for row in rows+[closing]))
 validation=load(FINAL/'WORKER_RETURN_VALIDATION.json');validation['command_log_status']='SEALED_NATIVE_COMPLETIONS_PLUS_CURRENT_LOG_CLOSE';validation['command_log']=fact(log);validation['native_completed_commands']=len(rows);validation['actual_generator_completion']=generated[-1];validation['generator_source']=fact(FINAL/'generate_worker_return.py');validation['final_lock_check']=guard();validation['local_phase_completed_at']=utc();save('WORKER_RETURN_VALIDATION.json',validation)
 names=['FINALIZE_PREFLIGHT.json','generate_worker_return.py','WORKER_RETURN.json','WORKER_RETURN_VALIDATION.json','COMMAND_LOG.jsonl'];assert {p.name for p in FINAL.iterdir()}==set(names)
 print(json.dumps({'outcome':'STOP','manifest_total':81,'published_file_entries':71,'literal_aliases':10,'missing_count':16,'frozen71_unchanged':True,'all_new_files':[fact(FINAL/name) for name in names],'return_to':validation['return_to'],'formal_return_transport_target':validation['formal_return_transport_target'],'full_Gate':'NOT_INVOKED_NO_FAKE_RETURN_REF_RECEIPT'},ensure_ascii=False,indent=2))

if __name__=='__main__':
 if sys.argv[1:]==['--seal-log']:seal_log()
 else:assert len(sys.argv)==1;generate()
