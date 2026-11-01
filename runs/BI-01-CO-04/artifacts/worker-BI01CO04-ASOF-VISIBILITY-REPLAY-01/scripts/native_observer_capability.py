"""同一原入口/参数/前缀，关闭strace并查看原生类公开能力；记录neutrality对照。"""
from finite_probe import *
marker=OUT/'.runtime/OBSERVER_CAPABILITY_STARTED'
fd=os.open(marker,os.O_CREAT|os.O_EXCL|os.O_WRONLY,0o600);os.close(fd)
original=OUT/'frozen/entrypoint/one.edh'
wrapper=OUT/'frozen/entrypoint/one_with_scope_observation.edh'
wrapper.write_bytes(original.read_bytes()+b"\nimport * 'batteries/root/debug'\nconsole.print$ 'NATIVE_OBJECT_CAPABILITY_BEGIN'\nprintDir$ task.object\nprintDir$ FrpUtil.getClass('ScaleTurnCalendar')\nconsole.print$ 'NATIVE_OBJECT_CAPABILITY_END'\n")
prior=json.loads((OUT/'NATIVE_PREFIX_ROUTE_EXECUTION.json').read_text());assert prior['native_success']
command=[str(OUT/'frozen/bin/ts'),'--f='+str(wrapper),'--jp='+str(OUT/'execution/tasks/rb__big.json')]
receipt={'command':command,'cwd':str(WORK),'environment_allowlist':prior['environment_allowlist'],'started_at':NOW(),
         'input_bars':2160,'instrumentation':'strace off; original entry followed only by scope() inspection after task completion',
         'parameters_unchanged':True,'source_prefix_unchanged':True}
start=time.monotonic()
with (OUT/'logs/observer_capability.stdout').open('wb') as stdout,(OUT/'logs/observer_capability.stderr').open('wb') as stderr:
 p=subprocess.Popen(command,cwd=WORK,env=receipt['environment_allowlist'],stdout=stdout,stderr=stderr,stdin=subprocess.DEVNULL,preexec_fn=guard_writes,start_new_session=True)
 try:receipt['returncode']=p.wait(timeout=180)
 except subprocess.TimeoutExpired:p.terminate();receipt['returncode']=p.wait(timeout=10);receipt['timed_out']=True
receipt.update(finished_at=NOW(),elapsed_seconds=time.monotonic()-start)
text=(OUT/'logs/observer_capability.stdout').read_text(errors='replace')+(OUT/'logs/observer_capability.stderr').read_text(errors='replace')
receipt['native_success']='time used:' in text and 'Edh program crashed with an error:' not in text
receipt['scope_inspection_complete']='NATIVE_OBJECT_CAPABILITY_END' in text
js('OBSERVER_CAPABILITY_EXECUTION.json',receipt)
m=json.loads((OUT/'REPLAY_MANIFEST.json').read_text());m['engine_runs'].append(receipt);m['native_process_invocations']=4
js('REPLAY_MANIFEST.json',m)
print(json.dumps(receipt,ensure_ascii=False))
