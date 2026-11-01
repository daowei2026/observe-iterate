"""同一原引擎/数学/固定前缀完成其余5组基线对照；不把batch输出当first-seen。"""
from finite_probe import *
marker=OUT/'.runtime/REMAINING_PREFIX_MATRIX_STARTED'
fd=os.open(marker,os.O_CREAT|os.O_EXCL|os.O_WRONLY,0o600);os.close(fd)
prior=json.loads((OUT/'NATIVE_PREFIX_ROUTE_EXECUTION.json').read_text());assert prior['native_success']
m=json.loads((OUT/'REPLAY_MANIFEST.json').read_text())
results=[]
for sym in SYMS:
 for role in ['big','mid']:
  if (sym,role)==('rb','big'):continue
  command=[str(OUT/'frozen/bin/ts'),'--f='+str(OUT/'frozen/entrypoint/one.edh'),'--jp='+str(OUT/f'execution/tasks/{sym}__{role}.json')]
  receipt={'command':command,'cwd':str(WORK),'environment_allowlist':prior['environment_allowlist'],
           'symbol':sym,'scale':role,'started_at':NOW(),'input_bars':2160,
           'purpose':'完整冻结前缀原生对照，不赋first_seen或发布资格'}
  start=time.monotonic()
  with (OUT/f'logs/matrix_{sym}_{role}.stdout').open('wb') as stdout,(OUT/f'logs/matrix_{sym}_{role}.stderr').open('wb') as stderr:
   p=subprocess.Popen(command,cwd=WORK,env=receipt['environment_allowlist'],stdout=stdout,stderr=stderr,stdin=subprocess.DEVNULL,preexec_fn=guard_writes,start_new_session=True)
   try:receipt['returncode']=p.wait(timeout=180)
   except subprocess.TimeoutExpired:p.terminate();receipt['returncode']=p.wait(timeout=10);receipt['timed_out']=True
  text=(OUT/f'logs/matrix_{sym}_{role}.stdout').read_text(errors='replace')+(OUT/f'logs/matrix_{sym}_{role}.stderr').read_text(errors='replace')
  receipt.update(finished_at=NOW(),elapsed_seconds=time.monotonic()-start)
  receipt['native_success']=receipt['returncode']==0 and 'time used:' in text and 'Edh program crashed with an error:' not in text
  results.append(receipt);js('MATRIX_EXECUTION_RECEIPTS.json',results)
  if not receipt['native_success']:break
  print(json.dumps({'symbol':sym,'scale':role,'success':True,'elapsed_seconds':receipt['elapsed_seconds']},ensure_ascii=False),flush=True)
 else:continue
 break
m['engine_runs']+=results;m['native_process_invocations']=4+len(results);m['exit']='PENDING_FINAL_NATIVE_OBSERVABILITY_ASSESSMENT'
js('REPLAY_MANIFEST.json',m)
