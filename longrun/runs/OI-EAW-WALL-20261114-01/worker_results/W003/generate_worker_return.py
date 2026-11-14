from pathlib import Path
import os,sys,json,hashlib,fcntl,errno,datetime,runpy,ast
BASE=Path('/dwdhome/fy/BASE_E6_2');ROOT=BASE/'.oi-runs/OI-EAW-WALL-20261114-01/D003/W003';FINAL=ROOT/'final-return';CONTROL=Path('/dwdhome/fy/cgpterm/artifacts/oi-eaw-wall/OI-EAW-WALL-20261114-01');LOCK=ROOT.parents[1]/'.D003-writer.lock'
ORDER_REF='daowei2026/observe-iterate@3afc8e9eedb34ac3b25ba69e383c778c37622c30:longrun/runs/OI-EAW-WALL-20261114-01/work_orders/W003/ORDER.json';COMMIT='9aaaf4a3b322333b46f33b9e55c916b4cea1b1e3';PREFIX='longrun/runs/OI-EAW-WALL-20261114-01/delegations/D003/results/W003/'
def utc():return datetime.datetime.now(datetime.timezone.utc).isoformat()
def fact(p):
 p=Path(p);b=p.read_bytes();s=p.stat();return {'path':str(p),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'mtime_ns':s.st_mtime_ns,'inode':s.st_ino,'dev':s.st_dev}
def load(p):return json.loads(Path(p).read_text())
def save(name,value):
 p=FINAL/name;assert p.parent==FINAL and p.resolve().is_relative_to(FINAL);p.write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n');return p

def guard():
 assert Path.cwd()==BASE and FINAL.resolve()==FINAL and not any(p.is_symlink() for p in [FINAL,*FINAL.parents]);assert sys.dont_write_bytecode and sys.flags.isolated;assert os.environ['HOME']=='/home/dw' and os.environ['CODEX_HOME']=='/home/dw/.codex'
 s=Path('/proc/240810/stat').read_text();assert s[s.rfind(')')+2:].split()[19]=='46501758' and LOCK.lstat().st_ino==14806399
 info=Path('/proc/240810/fdinfo/3').read_text();assert 'FLOCK' in info and 'WRITE 240810' in info
 fd=os.open(LOCK,os.O_RDWR|os.O_NOFOLLOW)
 try:
  assert os.fstat(fd).st_ino==14806399
  try:fcntl.flock(fd,fcntl.LOCK_EX|fcntl.LOCK_NB)
  except BlockingIOError as e:assert e.errno in (errno.EAGAIN,errno.EACCES);denial=e.errno
  else:raise RuntimeError('STOP unexpected lock acquisition')
 finally:os.close(fd)
 return {'utc':utc(),'holder_pid':240810,'startticks':'46501758','inode':14806399,'controller_session':30931,'fdinfo':info,'same_inode_competition_errno':denial,'holder_lock_modified':False}

def verify_frozen(publication,baseline):
 assert publication['state']=='PUBLISHED_REMOTE_BYTE_VERIFIED' and publication['commit']==COMMIT and publication['repository']=='daowei2026/observe-iterate' and publication['all_72_byte_equal'] and publication['only_allowed_new_paths'] and publication['outcome']=='STOP'
 assert len(publication['files'])==len(baseline['frozen_files'])==72 and publication['bytes']==1585202
 before={f['path']:f for f in baseline['frozen_files']};verified=[]
 for item in publication['files']:
  p=Path(item['local_path']);assert p.resolve()==p and p.is_relative_to(ROOT) and not p.is_relative_to(FINAL) and not p.is_symlink();now=fact(p);old=before[str(p)]
  assert all(now[k]==old[k] for k in ['bytes','sha256','mtime_ns','inode','dev']);assert now['bytes']==item['bytes'] and now['sha256']==item['sha256'];blob=hashlib.sha1(('blob '+str(now['bytes'])+'\0').encode()+p.read_bytes()).hexdigest();assert blob==item['git_blob_sha']==item['remote_blob_sha'] and item['byte_equal'] is True
  assert item['path'].startswith(PREFIX) and item['ref']=='daowei2026/observe-iterate@'+COMMIT+':'+item['path'];verified.append({'local_path':str(p),'ref':item['ref'],'before':old,'after':now,'git_blob_sha':blob,'publication_receipt_match':True,'content_and_metadata_unchanged':True})
 assert len({v['local_path'] for v in verified})==len({v['ref'] for v in verified})==72 and sum(v['after']['bytes'] for v in verified)==1585202
 return verified

def generate():
 lock_before=guard();baseline=load(FINAL/'FINALIZE_PREFLIGHT.json');publication=load(CONTROL/'W003-published-refs.json');verified_before=verify_frozen(publication,baseline)
 order=load(CONTROL/'C0011-remote-work_orders--W003--ORDER.json');binding=load(ROOT/'input/RUN_BINDING.json');handoff=load(ROOT/'artifacts/LOCAL_STAGE_HANDOFF.json');verdict=load(ROOT/'artifacts/PHASE0_RECOVERY_VERDICT.json');confinement=load(ROOT/'artifacts/WRITE_CONFINEMENT_REPORT.json');trace=load(ROOT/'artifacts/FULL_WRITE_TRACE_REVIEW.json');launch=load(ROOT/'receipts/r0a-positive-launcher.json')
 assert fact(CONTROL/'WORKER_FINALIZE_TASK-W003.md')['sha256']=='5ba3bbbcf323970c517f7a6a398759317d5b9c368037175b20f60c404a1d1b7a';assert fact(CONTROL/'C0011-remote-work_orders--W003--ORDER.json')['sha256']=='c0906a7cabcf970d51f052d9747592ad9e66b015080d4ff48fd5b6f39e32effb';assert fact(CONTROL/'C0011-remote-work_orders--W003--ORDER.md')['sha256']=='c6bf89c9a2c4c8b477e8e81458123ac7c69f7e0194545b5257312781ca1c05c7'
 assert handoff['order_ref']==ORDER_REF and order['run_id']=='OI-EAW-WALL-20261114-01' and order['work_order_id']=='W003' and order['issuer_call_id']=='C0011' and order['worker']==handoff['worker']=='codex:OI-EAW-WALL-20261114-01:worker:W1' and order['issuer']==order['return_to']==handoff['return_to']=='chatgpt:OI-EAW-WALL-20261114-01:executor:E1'
 assert verdict['outcome']==handoff['outcome']=='STOP' and verdict['phase0_verdict']=='PREFLIGHT_STOP' and verdict['primary_stop_reason']=='RECOVERY_STOP_WRITE_CONFINEMENT'
 assert launch['calls']==[] and launch['status']=='LAUNCHER_FAILED' and confinement['failure']['launcher_exit_code']==73 and not confinement['write_confinement_pass'];assert not verdict['automatic_retry'] and not verdict['R0B_entered'] and not verdict['R0C_entered'] and not verdict['Phase1_or_Phase2_entered'];assert verdict['scenario_evidence_runs']==verdict['compile_runs']==verdict['serialization_runs']==0
 assert not trace['global_or_future_zero_outside_write_proof'] and trace['successful_outside_descriptor_writes_in_this_trace']==0
 by_local={e['local_path']:e for e in publication['files']};manifest={e['path']:{'ref':e['ref'],'sha256':e['sha256']} for e in publication['files']};aliases=[];deferred=[]
 assert len(order['deliverables'])==len(handoff['deliverable_mapping'])==11
 for literal,entry in zip(order['deliverables'],handoff['deliverable_mapping']):
  assert literal==entry['literal_ORDER_deliverable'];index=entry['index']
  if index in (9,11):deferred.append({'index':index,'literal':literal,'reason':'未进入条件工程阶段，无产物' if index==9 else '当前生成正式 Return 本地文件，尚无真实自出版 ref；不得自引用。'});continue
  locals=entry['local_files'];assert locals and all(path in by_local for path in locals)
  selected=next((p for p in locals if p.endswith('/PUBLICATION_MANIFEST.json')),locals[0]);chosen=by_local[selected];assert literal not in manifest;manifest[literal]={'ref':chosen['ref'],'sha256':chosen['sha256']};aliases.append({'literal':literal,'index':index,'alias_ref':chosen['ref'],'alias_sha256':chosen['sha256'],'actual_files':[{'local_path':p,'ref':by_local[p]['ref'],'sha256':by_local[p]['sha256']} for p in locals],'group_alias_note':'逐字标签8引用真实出版索引文件；五个实际成员亦分别完整列入 manifest。' if len(locals)>1 else '逐字标签指向该实际报告原件。'})
 assert len(manifest)==81 and len(aliases)==9
 missing=[]
 for entry in handoff['missing']:
  if entry['id'] in ('M-EVIDENCE-PUBLICATION','M-FORMAL-RETURN'):continue
  detail=entry['detail']
  if entry['id']=='M-CONFINEMENT':detail+=' 唯一旧 launcher 因 fd0 O_RDWR /dev/null 接线问题在安装 NNP/Landlock/seccomp 前退出73，calls=[]，没有重试；这不是本 W 证明 Landlock 不支持。唯一失败 trace 的1071行中仅有 W003 内1214 bytes成功write；scope内外写0不能外推为全局零外写。当前收尾阶段未运行任何 R0/调查。'
  missing.append(entry['id']+'：'+detail)
 ep_gaps=[('EP-WALL-SHARED-01','NOT_ATTEMPTED；无新 snapshot/accessor/patch/typecheck'),('EP-WALL-SHARED-02','NOT_ATTEMPTED；无 versioned DTO/schema/canonical roundtrip/stable hash'),('EP-WALL-SHARED-03','UNSATISFIED；新 confinement未建立，兼容离线closure/四预算/持续监测缺证'),('EP-SCENARIO-01','NOT_ATTEMPTED；无 dedicated target/component/main/manifest/compile-only'),('EP-SCENARIO-02','NOT_ATTEMPTED；无 exact-error constructor/payload synthetic serialization'),('EP-SCENARIO-03','NOT_ATTEMPTED；无 transaction DTO/pre-post A/committed-uncommitted serialization验证'),('EP-SCENARIO-04','仅继承 C0010 E1 已认定的旧 PARTIAL静态子集；无新 target manifest或actual result，不冒充本 W专业接受'),('EP-SCENARIO-05','NOT_ATTEMPTED；未物化完整9/18/22 fixture，无schema/input/static parse-count-order-hash验证，fixture执行0')]
 missing.extend(ep+'：'+detail for ep,detail in ep_gaps)
 conditional=handoff['deliverable_mapping'][8]
 missing.append(order['deliverables'][8]+'：Phase0 PREFLIGHT_STOP，条件未成立；未产出 '+', '.join(conditional['conditional_filenames_not_created'])+'，不造空文件/ref。')
 missing.append(order['deliverables'][10]+'：本阶段已生成正式V2 Return本地原件；其自身及新增validation/generator/COMMAND_LOG/PREFLIGHT尚未出版，缺真实self ref和独立回交receipt，不列入本manifest。由主控逐字出版至longrun/runs/OI-EAW-WALL-20261114-01/worker_results/W003/WORKER_RETURN.json，并在有真实ref/receipt后完成validate-worker-return和送原E1。72份证据出版缺口已解决；旧冻结报告中的pending为当时历史，不回写。')
 assert len(missing)==len(set(missing))==16
 report=by_local[str(ROOT/'artifacts/WORKER_EXECUTION_REPORT.md')];assert report['sha256']=='839c7c62302dd1b07cca3da7115364702a89d6290a2f11014a8cb9e28a1f7357'
 returned={'schema':'longrun-worker-return/v2','run_id':order['run_id'],'work_order_id':'W003','order_ref':ORDER_REF,'worker':order['worker'],'return_to':order['issuer'],'outcome':'STOP','result_ref':report['ref'],'missing':missing,'manifest':manifest}
 gate_path=CONTROL/'observe-iterate/longrun/tools/longrun_gate.py';schema_path=CONTROL/'observe-iterate/longrun/contracts/longrun_schema_v2.json';assert fact(schema_path)['sha256']=='32c1e2409ff4936a87d688848736bb9af71fe0415d338ba66dd031e3149243d3'
 gate=runpy.run_path(str(gate_path));gate['validated']('worker_return',returned);gate['validated']('order',order);gate['validated']('binding',binding)
 assert returned['worker'] in binding['workers'] and returned['return_to'] in binding['executors'] and any(gate['grant_covers'](grant,order['grant']) for grant in binding['grants']);gate['exact_path'](ORDER_REF,order['run_id'],'work_orders/W003/ORDER.json')
 evidence={e['ref']:e for e in publication['files']};manifest_checks=[]
 for key,value in manifest.items():
  assert set(value)=={'ref','sha256'};gate['ref_parts'](value['ref']);real=evidence[value['ref']];assert real['sha256']==value['sha256'];assert not real['path'].startswith('longrun/runs/OI-EAW-WALL-20261114-01/worker_results/W003/');manifest_checks.append({'key':key,'ref':value['ref'],'sha256':value['sha256'],'source_local_path':real['local_path'],'publication_receipt_match':True})
 assert returned['result_ref'] in evidence
 output=FINAL/'WORKER_RETURN.json';assert not output.exists();save('WORKER_RETURN.json',returned);gate['validated']('worker_return',load(output));verified_after=verify_frozen(publication,baseline);lock_after=guard()
 validation={'record_type':'W003_FORMAL_RETURN_LOCAL_VALIDATION','utc':utc(),'status':'PASS_FOR_SCHEMA_BINDING_MANIFEST_AND_LOCAL_TRANSPORT_ONLY','run_id':order['run_id'],'work_order_id':'W003','outcome':'STOP','return_to':order['issuer'],'current_turn_context':baseline['actual_context'],'scope_zh':'只核正式Return结构/原W1身份/原ORDER路由/真实refs与本地文件一致性；未重跑原调查/R0/工程/生产动作。不作专业接受或父任务完成决定。','schema_validation':{'method':'原仓longrun_gate.py validated(worker_return/order/binding)，Draft202012Validator，-I -B禁止写pycache；无网络ref解析。','pass':True,'schema':fact(schema_path),'gate_source':fact(gate_path)},'full_validate_worker_return_gate':{'status':'NOT_INVOKED_RETURN_NOT_YET_PUBLISHED','reason':'官方全Gate要求真实worker_return_ref和独立worker_receipt；当前正式Return尚未出版，不伪造future/self ref来运行或宣称Gate通过。该步由主控出版并实核receipt后完成。'},'worker_return':fact(output),'result_ref':returned['result_ref'],'result_sha256':report['sha256'],'order_ref':ORDER_REF,'exact_identity_and_binding_match':True,'STOP_missing_preserved':True,'missing_count':len(missing),'missing':missing,'resolved_missing':[{'id':'M-EVIDENCE-PUBLICATION','status':'RESOLVED','commit':COMMIT,'files':72,'bytes':1585202,'proof':'主控真实回执逐字/remote blob验证＋本地72份bytes/SHA256/Git blob复核；不联网重读。'}],'return_publication_pending':True,'publication_receipt':fact(CONTROL/'W003-published-refs.json'),'finalize_task':fact(CONTROL/'WORKER_FINALIZE_TASK-W003.md'),'manifest_total':81,'published_file_entries':72,'literal_deliverable_aliases':9,'manifest_entries':manifest_checks,'applicable_deliverable_aliases':aliases,'deliverables_without_manifest_alias':deferred,'no_future_or_self_refs':True,'old_freeze_historical_pending_not_rewritten':True,'frozen_originals':{'count':72,'bytes':1585202,'before_checked':len(verified_before),'after_checked':len(verified_after),'all_bytes_sha256_git_blob_and_mtime_inode_dev_unchanged':True,'checks':verified_after},'kernel_confinement_established_in_original_attempt':False,'old_attempt_exit_code':73,'old_attempts':1,'old_retry':False,'new_R0_or_investigation_actions':0,'scenario_build_compile_serialization_runs':0,'HOME':os.environ['HOME'],'CODEX_HOME':os.environ['CODEX_HOME'],'HOME_or_CODEX_HOME_reset':False,'exclusive_lock_before':lock_before,'exclusive_lock_after':lock_after,'new_business_write_root':str(FINAL),'github_or_other_chat_writes':False,'formal_return_transport_target':'longrun/runs/OI-EAW-WALL-20261114-01/worker_results/W003/WORKER_RETURN.json','validation_transport_target':'longrun/runs/OI-EAW-WALL-20261114-01/worker_results/W003/WORKER_RETURN_VALIDATION.json','command_log_status':'待本脚本真实完成后从本turn原生命令完成事件封存；不写伪造exit。'}
 save('WORKER_RETURN_VALIDATION.json',validation)
 print(json.dumps({'status':validation['status'],'outcome':'STOP','manifest_total':81,'published_file_entries':72,'deliverable_aliases':9,'missing_count':16,'frozen72_unchanged':True,'files':[fact(output),fact(FINAL/'WORKER_RETURN_VALIDATION.json')]},ensure_ascii=False,indent=2))

def seal_log():
 guard();baseline=load(FINAL/'FINALIZE_PREFLIGHT.json');turn=baseline['actual_context']['turn_id'];session=Path('/home/dw/.codex/sessions/2026/11/14/rollout-2026-11-14T21-53-08-01a1da55-5881-7590-94a1-0661f0236977.jsonl');assert session.stat().st_size<16*1024*1024
 rows={}
 with session.open() as f:
  for line in f:
   o=json.loads(line);d=o.get('payload',{});item=d.get('item',{})
   if o.get('type')=='event_msg' and d.get('type')=='item_completed' and d.get('turn_id')==turn and item.get('type')=='CommandExecution':rows[item['id']]={'record_type':'NATIVE_COMMAND_COMPLETION','timestamp':o.get('timestamp'),'thread_id':d.get('thread_id'),'turn_id':turn,'started_at_ms':d.get('started_at_ms'),'completed_at_ms':d.get('completed_at_ms'),'item':item}
 records=sorted(rows.values(),key=lambda r:r.get('started_at_ms') or 0);generated=[]
 for record in records:
  command=record['item'].get('command');argv=ast.literal_eval(command) if isinstance(command,str) else command
  if isinstance(argv,list) and str(FINAL/'generate_worker_return.py') in argv[-1] and 'PYTHONDONTWRITEBYTECODE=1 /usr/bin/python3.12 -I -B ' in argv[-1] and '--seal-log' not in argv[-1]:generated.append(record)
 assert generated and generated[-1]['item']['exit_code']==0
 current={'record_type':'FINAL_COMMAND_LOG_SEAL','utc':utc(),'argv':sys.orig_argv,'cwd':str(Path.cwd()),'pid':os.getpid(),'status':'RUNNING_AT_LOG_CLOSE','exit_code':None,'note_zh':'完整记录此前已完成命令及当前封存argv。本记录后的实际操作仅F内COMMAND_LOG写入、validation补记真实生成命令退出0和日志hash、打印最终文件hash；代码已归档。不伪造当前命令尚未返回的exit或自身未来ref。'}
 log=FINAL/'COMMAND_LOG.jsonl';assert not log.exists();log.write_text(''.join(json.dumps(row,ensure_ascii=False)+'\n' for row in records+[current]))
 validation=load(FINAL/'WORKER_RETURN_VALIDATION.json');validation['command_log_status']='SEALED_WITH_NATIVE_COMPLETIONS_AND_CURRENT_CLOSURE_RECORD';validation['command_log']=fact(log);validation['native_completed_commands']=len(records);validation['actual_generator_command_completion']=generated[-1];validation['generator_source']=fact(FINAL/'generate_worker_return.py');validation['final_lock_check']=guard();validation['local_phase_completed_at']=utc();save('WORKER_RETURN_VALIDATION.json',validation)
 names=['FINALIZE_PREFLIGHT.json','generate_worker_return.py','WORKER_RETURN.json','WORKER_RETURN_VALIDATION.json','COMMAND_LOG.jsonl'];assert set(p.name for p in FINAL.iterdir())==set(names)
 print(json.dumps({'outcome':'STOP','manifest_total':81,'published_files':72,'aliases':9,'missing_count':16,'old72_frozen':True,'all_new_files':[fact(FINAL/name) for name in names],'return_to':validation['return_to'],'formal_return_transport_target':validation['formal_return_transport_target'],'full_Gate':'NOT_INVOKED_RETURN_UNPUBLISHED_NO_FAKE_SELF_REF'},ensure_ascii=False,indent=2))

if __name__=='__main__':
 if sys.argv[1:]==['--seal-log']:seal_log()
 else:assert len(sys.argv)==1;generate()
