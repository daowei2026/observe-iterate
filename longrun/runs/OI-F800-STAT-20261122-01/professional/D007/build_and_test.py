"""MP002隔离编译和原生回归；持真实资源锁，不启动正式F。"""
from pathlib import Path
from hashlib import sha256
from datetime import datetime,timezone
import fcntl,json,os,subprocess,time

ROOT=Path(__file__).resolve().parent
BASE=ROOT.parents[2]
NEW=BASE/'.runtime/f800-input-missing-20261123/runtime'
OLD=BASE/'.runtime/f800-exact-uti-20261122/runtime'
FRP=BASE/'.runtime/f-observation-multiple-github-20261122/frp'
LOCK=Path('/dwdhome/fy/cgpterm/artifacts/wall-f-closure-20261122/FORMAL_PRODUCTION.lock')
def stamp():return datetime.now(timezone.utc).isoformat()
def digest(p):
 h=sha256()
 with p.open('rb') as f:
  for b in iter(lambda:f.read(1024*1024),b''):h.update(b)
 return h.hexdigest()
pre=json.loads((ROOT/'RUNTIME_PREPARATION.json').read_text());assert pre['completed']
assert json.loads((ROOT/'APPROVED_DIFF_CONFORMANCE.json').read_text())['implemented_diff_content_exact']
assert (NEW/'edh-universe/frp/frp').resolve()==FRP
state=dict(run_id='OI-F800-STAT-20261122-01',delegation_id='D007',pid=os.getpid(),started_at=stamp(),formal_feature_run=False,completed=False,runtime=str(NEW),tests=[])
def save():(ROOT/'BUILD_STATUS.json').write_text(json.dumps(state,ensure_ascii=False,indent=2)+'\n')
def supervised(command,logname):
 with (ROOT/logname).open('w') as log:
  proc=subprocess.Popen(command,cwd=NEW/'edh-universe',stdout=log,stderr=subprocess.STDOUT)
  state.update(active_command=command,active_pid=proc.pid,active_log=logname);save()
  while proc.poll() is None:
   state['heartbeat_at']=stamp()
   observed=subprocess.run(['ps','-o','pid,ppid,args','--ppid',str(proc.pid)],text=True,capture_output=True)
   state.update(active_children=observed.stdout.splitlines(),child_observation_exit_code=observed.returncode);save();time.sleep(5)
  return proc.returncode
save()
with LOCK.open('a+') as lock:
 while True:
  try:fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB);break
  except BlockingIOError:state.update(phase='waiting_resource_lock',heartbeat_at=stamp());save();time.sleep(10)
 state.update(lock_acquired_at=stamp(),lock_path=str(LOCK),lock_owner_pid=os.getpid(),phase='compiling');save()
 edh=NEW/'edh-universe'
 command=['stack','--stack-yaml',str(edh/'stack.yaml'),'build','frp:exe:dbaw','frp:exe:u2-observation-window-check','frp:exe:u2-kline-coverage-adapter-check','trade-poc:exe:ts','--copy-bins','--ghc-options=-O0','--ghc-options=-j2','--jobs=2']
 state['build_command']=command
 code=supervised(command,'build.log');state.update(build_exit_code=code,build_finished_at=stamp());save()
 if code==0:
  state['phase']='native_regressions';save()
  commands=[
   ('real_kline_adapter',[str(edh/'bin/u2-kline-coverage-adapter-check'),str(ROOT.parent/'D005/configuration.json'),str(ROOT/'adapter-fixture-app'),str(ROOT/'fixed-adapter-trace.csv')],'fixed-adapter-check.log'),
   ('existing_observation_window',[str(edh/'bin/u2-observation-window-check'),str(ROOT.parent/'D002/preflight/baseline-configuration.json'),str(ROOT.parent/'D005/configuration.json')],'fixed-window-checks.log'),
   ('existing_material_coverage_controls',['stack','--stack-yaml',str(edh/'stack.yaml'),'exec','--','runghc','-package=frp',str(ROOT.parent/'D006/NativeCoverageControls.hs')],'fixed-coverage-controls.log')]
  for name,cmd,log in commands:
   started=stamp();rc=supervised(cmd,log)
   state['tests'].append(dict(name=name,command=cmd,log=log,started_at=started,finished_at=stamp(),exit_code=rc));save()
   if rc:code=rc;break
 state['baseline_binaries_unchanged']=all(digest(Path(v['path']))==v['sha256'] for v in pre['baseline_binaries'].values())
 assert state['baseline_binaries_unchanged']
 source=Path('src/Frp/Instance/ISL/Opportunity/U2/GroupCandidateKLineInput.hs')
 state['baseline_source_unchanged']=digest(OLD/'edh-universe/frp/frp'/source)==pre['baseline_adapter_sha256'];assert state['baseline_source_unchanged']
 if code==0:
  state['binaries']={n:dict(path=str(edh/'bin'/n),sha256=digest(edh/'bin'/n)) for n in ['ts','dbaw','u2-observation-window-check','u2-kline-coverage-adapter-check']}
 state.update(exit_code=code,completed=code==0,phase='completed' if code==0 else 'failed',finished_at=stamp(),lock_released_at=stamp());save();fcntl.flock(lock,fcntl.LOCK_UN)
print(json.dumps(dict(completed=state['completed'],build_exit_code=state['build_exit_code'],exit_code=code,tests=state['tests']),ensure_ascii=False))
raise SystemExit(code)
