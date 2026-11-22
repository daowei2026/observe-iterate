"""为MP002隔离输出/构建缓存，冻结be57旧源码视图；不运行正式Feature。"""
from pathlib import Path
from hashlib import sha256
from datetime import datetime,timezone
import fcntl,json,os,subprocess,time

ROOT=Path(__file__).resolve().parent
BASE=ROOT.parents[2]
OLD=BASE/'.runtime/f800-exact-uti-20261122/runtime'
NEW=BASE/'.runtime/f800-input-missing-20261123/runtime'
FRP=BASE/'.runtime/f-observation-multiple-github-20261122/frp'
SNAP=NEW.parent/'baseline-frp-be57'
LOCK=Path('/dwdhome/fy/cgpterm/artifacts/wall-f-closure-20261122/FORMAL_PRODUCTION.lock')
def stamp():return datetime.now(timezone.utc).isoformat()
def digest(p):
 h=sha256()
 with p.open('rb') as f:
  for b in iter(lambda:f.read(1024*1024),b''):h.update(b)
 return h.hexdigest()
state=dict(run_id='OI-F800-STAT-20261122-01',delegation_id='D007',pid=os.getpid(),started_at=stamp(),formal_feature_run=False,completed=False,old_runtime=str(OLD),new_runtime=str(NEW))
def save(): (ROOT/'RUNTIME_PREPARATION.json').write_text(json.dumps(state,ensure_ascii=False,indent=2)+'\n')
assert subprocess.check_output(['git','rev-parse','HEAD'],cwd=FRP,text=True).strip()=='be57d6752c9d43d10f1d670e1d2993bb8153ea7c'
assert not NEW.exists() and not SNAP.exists()
state['baseline_binaries']={n:dict(path=str(OLD/'edh-universe/bin'/n),sha256=digest(OLD/'edh-universe/bin'/n)) for n in ['ts','dbaw','u2-observation-window-check']}
save()
with LOCK.open('a+') as lock:
 while True:
  try:fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB);break
  except BlockingIOError:state.update(phase='waiting_resource_lock',heartbeat_at=stamp());save();time.sleep(10)
 state.update(lock_acquired_at=stamp(),lock_path=str(LOCK),lock_owner_pid=os.getpid(),phase='freezing_old_source');save()
 SNAP.mkdir(parents=True)
 archive=subprocess.Popen(['git','archive','--format=tar','be57d6752c9d43d10f1d670e1d2993bb8153ea7c'],cwd=FRP,stdout=subprocess.PIPE)
 subprocess.run(['tar','-xf','-','-C',str(SNAP)],stdin=archive.stdout,check=True);archive.stdout.close();assert archive.wait()==0
 source=Path('src/Frp/Instance/ISL/Opportunity/U2/GroupCandidateKLineInput.hs')
 assert (SNAP/source).read_bytes()==(FRP/source).read_bytes()
 old_link=OLD/'edh-universe/frp/frp';assert old_link.is_symlink() and old_link.resolve()==FRP
 pending=old_link.with_name('frp.mp002-freeze');pending.symlink_to(SNAP,target_is_directory=True);os.replace(pending,old_link)
 state.update(baseline_source_snapshot=str(SNAP),old_runtime_source_frozen=True,baseline_adapter_sha256=digest(SNAP/source),phase='isolated_runtime_copy');save()
 NEW.mkdir();oldedh=OLD/'edh-universe';edh=NEW/'edh-universe';edh.mkdir()
 for p in OLD.iterdir():
  if p.name!='edh-universe':(NEW/p.name).symlink_to(p,target_is_directory=p.is_dir())
 for p in oldedh.iterdir():
  if p.name not in ['.stack-work','stack.yaml','stack.yaml.lock','bin','frp']:(edh/p.name).symlink_to(p,target_is_directory=p.is_dir())
 (edh/'bin').mkdir();(edh/'frp').mkdir()
 for p in (oldedh/'frp').iterdir():
  if p.name=='frp':(edh/'frp/frp').symlink_to(FRP,target_is_directory=True)
  elif p.name=='trade-poc':subprocess.run(['cp','-a','--reflink=auto',str(p.resolve()),str(edh/'frp/trade-poc')],check=True)
  else:(edh/'frp'/p.name).symlink_to(p,target_is_directory=p.is_dir())
 subprocess.run(['cp','-a','--reflink=auto',str(oldedh/'.stack-work'),str(edh/'.stack-work')],check=True)
 (edh/'stack.yaml.lock').write_bytes((oldedh/'stack.yaml.lock').read_bytes())
 (edh/'stack.yaml').write_text((oldedh/'stack.yaml').read_text().replace(str(oldedh/'bin'),str(edh/'bin')))
 state.update(completed=True,phase='prepared',finished_at=stamp(),lock_released_at=stamp());save();fcntl.flock(lock,fcntl.LOCK_UN)
print(json.dumps({k:v for k,v in state.items() if k!='baseline_binaries'},ensure_ascii=False))
