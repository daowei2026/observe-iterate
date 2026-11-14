from pathlib import Path
import sys,os,json,hashlib,errno,fcntl,datetime
ROOT=Path('/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D003/W003');sys.path.insert(0,str(ROOT/'tools'));import runtime as w
w.guard();stamp=w.utc();session=Path('/home/dw/.codex/sessions/2026/11/14/rollout-2026-11-14T21-53-08-01a1da55-5881-7590-94a1-0661f0236977.jsonl');assert session.stat().st_size<=16*1024*1024
thread='01a1da55-5881-7590-94a1-0661f0236977';turn='01a1dbbd-01ac-7d03-983d-2f655359abf4';completed={};contexts=[];total=0
with session.open() as f:
 for line in f:
  total+=1;o=json.loads(line);payload=o.get('payload',{})
  if o.get('type')=='turn_context' and payload.get('turn_id')==turn:contexts.append({'timestamp':o.get('timestamp'),**{k:payload.get(k) for k in ['turn_id','cwd','model','effort','reasoning_effort']}})
  if o.get('type')=='event_msg' and payload.get('type')=='item_completed' and payload.get('turn_id')==turn and payload.get('item',{}).get('type')=='CommandExecution':completed[payload['item']['id']]={'timestamp':o.get('timestamp'),'thread_id':payload.get('thread_id'),'turn_id':turn,'started_at_ms':payload.get('started_at_ms'),'completed_at_ms':payload.get('completed_at_ms'),'item':payload['item']}
rows=sorted(completed.values(),key=lambda o:o.get('started_at_ms') or 0)
p=ROOT/'audit/NATIVE_COMMAND_COMPLETIONS.jsonl';p.write_text(''.join(json.dumps(o,ensure_ascii=False)+'\n' for o in rows))
w.save('audit/NATIVE_COMMAND_CAPTURE.json',{'utc':stamp,'source':str(session),'session_bytes_at_capture':session.stat().st_size,'single_exact_file_read_limit_bytes':16*1024*1024,'lines_examined':total,'thread_id':thread,'turn_id':turn,'command_completions':len(rows),'earliest':rows[0]['timestamp'] if rows else None,'latest':rows[-1]['timestamp'] if rows else None,'capture_scope':'Only completed CommandExecution events for this exact W003 turn; no reasoning/private conversation copied. Current collection and later archive commands are logged by subsequent capture/finalization records.','file':w.filefact(p),'current_contexts':contexts})
assert contexts and contexts[-1]['model']=='gpt-6.1-sol' and contexts[-1]['effort']=='max' and contexts[-1]['cwd']=='/dwdhome/fy/BASE_E6_2'
checks=[]
for old in json.loads((ROOT/'audit/READONLY_INPUTS_BEFORE.json').read_text()):
 current=w.filefact(old['path']);ok=all(current[k]==old[k] for k in ['bytes','sha256','mtime_ns','inode','dev']);checks.append({'before':old,'after':current,'unchanged':ok})
assert all(x['unchanged'] for x in checks)
w.save('audit/READONLY_INPUTS_AFTER.json',{'utc':stamp,'scope':'22 exact supplied input mirrors only; includes named frozen W002 inputs; no broad checkout/HOME/cache traversal and no claim of full global filesystem audit.','count':len(checks),'all_unchanged':True,'checks':checks})
loaded=Path('/dwdhome/fy/cgpterm/artifacts/oi-eaw-wall/OI-EAW-WALL-20261114-01/W003-worker-loaded-context.json');dest=ROOT/'input/W003-worker-loaded-context.json';assert not dest.exists();dest.write_bytes(loaded.read_bytes());assert dest.read_bytes()==loaded.read_bytes()
proc=[]
for pid,ticks in [(2890,'20139'),(240810,'46501758')]:
 q=Path('/proc')/str(pid);s=(q/'stat').read_text();actual=s[s.rfind(')')+2:].split()[19];assert actual==ticks;proc.append({'pid':pid,'startticks':actual,'uid':q.stat().st_uid,'exe':os.readlink(q/'exe')})
fd=os.open(w.LOCK,os.O_RDWR|os.O_NOFOLLOW)
try:
 try:fcntl.flock(fd,fcntl.LOCK_EX|fcntl.LOCK_NB)
 except BlockingIOError as e:competition={'result':'FAILED_AS_REQUIRED','errno':e.errno,'inode':os.fstat(fd).st_ino,'fd_opened_for_competition_only_no_write':True}
 else:raise RuntimeError('STOP unexpected acquisition')
finally:os.close(fd)
assert competition['inode']==14806399
controller=json.loads((ROOT/'input/W003-worker-pre-dispatch-state.json').read_text());owner=controller['owner'];load=json.loads(dest.read_text());assert load['thread']['id']==thread and load['thread']['status']['type']=='idle' and load['thread']['canAcceptDirectInput'] is True
binding={'utc':stamp,'run_id':'OI-EAW-WALL-20261114-01','work_order_id':'W003','worker':'codex:OI-EAW-WALL-20261114-01:worker:W1','issuer_call_id':'C0011','return_to':'chatgpt:OI-EAW-WALL-20261114-01:executor:E1','original_physical_thread_reused':True,'thread_id':thread,'session_id':thread,'actual_turn_id':turn,'cwd':str(Path.cwd()),'model':'gpt-6.1-sol','effort':'max','current_turn_context_evidence':contexts[-1],'actual_processes_read_only_verified':proc,'controller_owner_binding':owner,'owner_binding_evidence':'input/W003-worker-pre-dispatch-state.json; input/W003-worker-loaded-context.json; fresh PID/startticks/uid/exe checks','prior_worker_status':{'controller_old_turn_completed_and_goal_null_queue_empty':True,'controller_evidence':'input/W003-worker-pre-dispatch-state.json','old_lock_holder_pid237355_absent_now':not Path('/proc/237355').exists(),'original_thread_loaded_idle_before_dispatch':True,'new_root_precreation_absent_verified_in_bootstrap_native_command_log':True,'no_other_writer_claim_scope':'Fresh new controller lock plus original-thread idle/queue snapshot and old PID absent; no broad process or HOME scan.'},'new_lock':{'path':str(w.LOCK),'session':30931,'holder_pid':240810,'holder_startticks':'46501758','inode':14806399,'current_holder_fdinfo':Path('/proc/240810/fdinfo/3').read_text(),'competition':competition,'holder_lock_acquired_replaced_or_released_by_worker':False},'HOME':'/home/dw','CODEX_HOME':'/home/dw/.codex','HOME_or_CODEX_HOME_reset':False,'HOME_and_CODEX_HOME_business_new_writes_contract':0,'HOME_and_CODEX_HOME_trace_observed_successful_writes':0,'global_zero_external_writes_proven':False,'actual_write_root':str(ROOT),'root_canonical':ROOT.resolve()==ROOT,'owner_literal_grant':'operation=wall-observation-work execution_context=linux:/dwdhome/fy/BASE_E6_2 allowed_writes=/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01','grant_validation':'Exact Owner RUN_BINDING copy, current D003 and W003 literal grant subset verified in bootstrap; originals in input, command evidence retained.','github_write_authority':False,'no_other_chat_messages':True,'no_new_worker_or_subagent':True}
w.save('artifacts/W003_BINDING.json',binding);w.guard();print(json.dumps({'utc':stamp,'native_commands':len(rows),'input_hashes_unchanged':len(checks),'binding':str(ROOT/'artifacts/W003_BINDING.json')},ensure_ascii=False))
