import os,sys,json,hashlib,datetime,time,subprocess,fcntl,pathlib
ROOT=pathlib.Path('/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D003/W002')
BASE=pathlib.Path('/dwdhome/fy/BASE_E6_2')
LOCK=ROOT.parents[1]/'.D003-writer.lock'
def utc():return datetime.datetime.now(datetime.timezone.utc).isoformat()
def guard():
 assert os.getcwd()==str(BASE)
 assert ROOT.resolve()==ROOT and not any(p.is_symlink() for p in [ROOT,*ROOT.parents])
 text=pathlib.Path('/proc/237355/stat').read_text();assert text[text.rfind(')')+2:].split()[19]=='45798445'
 assert LOCK.stat().st_ino==14806399
 fd=os.open(LOCK,os.O_RDWR|os.O_NOFOLLOW)
 try:
  assert os.fstat(fd).st_ino==14806399
  try:fcntl.flock(fd,fcntl.LOCK_EX|fcntl.LOCK_NB)
  except BlockingIOError:pass
  else:raise RuntimeError('STOP: unexpected lock acquisition')
 finally:os.close(fd)
def environment():
 e={'PATH':'/usr/bin:/bin:/nix/.ghcup/ghc/9.4.8/bin','LANG':'C.UTF-8','LC_ALL':'C.UTF-8','USER':'dw','LOGNAME':'dw','PYTHONDONTWRITEBYTECODE':'1','GIT_OPTIONAL_LOCKS':'0','GIT_CONFIG_NOSYSTEM':'1','GIT_CONFIG_GLOBAL':'/dev/null','GIT_NO_REPLACE_OBJECTS':'1','GIT_PAGER':'cat','GHC_ENVIRONMENT':'-','LD_LIBRARY_PATH':'/home/dw/.local/lib','CODEX_THREAD_ID':'01a1da55-5881-7590-94a1-0661f0236977'}
 for k,v in {'HOME':'home','TMPDIR':'tmp','TMP':'tmp','TEMP':'tmp','XDG_CACHE_HOME':'xdg-cache','XDG_CONFIG_HOME':'home/.config','XDG_DATA_HOME':'home/.local/share','XDG_STATE_HOME':'home/.local/state','STACK_ROOT':'stack-root','STACK_WORK':'build/stack-work','CABAL_DIR':'home/.cabal','CABAL_CONFIG':'home/.cabal/config','CABAL_BUILDDIR':'build/cabal','GHCUP_INSTALL_BASE_PREFIX':'home','GHCUP_TMP_DIR':'tmp','GHCUP_LOGS_DIR':'logs/ghcup','PYTHONPYCACHEPREFIX':'xdg-cache/python','PYTHONUSERBASE':'home/.local','MPLCONFIGDIR':'home/.config/matplotlib','PIP_CACHE_DIR':'xdg-cache/pip','NPM_CONFIG_CACHE':'xdg-cache/npm','CARGO_HOME':'home/.cargo','RUSTUP_HOME':'home/.rustup','CCACHE_DIR':'xdg-cache/ccache','SQLITE_TMPDIR':'tmp','GHC_HISTORY':'home/.ghci_history'}.items():e[k]=str(ROOT/v)
 return e
def save(rel,obj):
 p=ROOT/rel;assert p.resolve().is_relative_to(ROOT);p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n');return p
def run(label,argv,limit=40,cwd=None):
 guard();assert pathlib.Path(argv[0]).is_absolute();cwd=cwd or str(BASE)
 assert cwd==str(BASE) or pathlib.Path(cwd).resolve().is_relative_to(ROOT)
 for ch in label:assert ch.isalnum() or ch in '-_.'
 out=ROOT/'logs'/(label+'.stdout');err=ROOT/'logs'/(label+'.stderr');assert not out.exists() and not err.exists()
 env=environment();start=utc();t=time.monotonic();error=None
 with out.open('xb') as so,err.open('xb') as se:
  try:r=subprocess.run(argv,env=env,cwd=cwd,stdout=so,stderr=se,timeout=limit);rc=r.returncode
  except subprocess.TimeoutExpired:rc=124;error='SUBPROCESS_TIMEOUT'
 result={'id':label,'started_at':start,'finished_at':utc(),'elapsed_seconds':time.monotonic()-t,'cwd':cwd,'argv':argv,'environment':env,'timeout_seconds':limit,'exit_code':rc,'error':error,'stdout':{'path':str(out),'bytes':out.stat().st_size,'sha256':hashlib.sha256(out.read_bytes()).hexdigest()},'stderr':{'path':str(err),'bytes':err.stat().st_size,'sha256':hashlib.sha256(err.read_bytes()).hexdigest()}}
 with (ROOT/'logs/COMMAND_LOG.jsonl').open('a') as f:f.write(json.dumps(result,ensure_ascii=False)+'\n')
 print(json.dumps({k:result[k] for k in ['id','exit_code','elapsed_seconds','stdout','stderr']},ensure_ascii=False));print('STDOUT\n'+out.read_text(errors='replace')[:4000]);print('STDERR\n'+err.read_text(errors='replace')[:4000])
 guard();return result
if __name__=='__main__':
 assert len(sys.argv)>=4
 run(sys.argv[1],sys.argv[2:])
