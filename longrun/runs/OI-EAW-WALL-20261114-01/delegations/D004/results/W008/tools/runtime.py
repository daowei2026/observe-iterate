import os,json,time,datetime,subprocess,signal,hashlib,fcntl
from pathlib import Path
B=Path('/dwdhome/fy/BASE_E6_2')
R=B/'.oi-runs/OI-EAW-WALL-20261114-01/D004/W008'
def now():return datetime.datetime.now(datetime.timezone.utc).isoformat()
def save(p,o):
 p=Path(p);p.write_text(json.dumps(o,ensure_ascii=False,indent=2)+'\n')
def desc(p):
 p=Path(p);s=p.stat();b=p.read_bytes();return {'path':str(p),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'mtime_ns':s.st_mtime_ns,'mtime_ns_decimal':str(s.st_mtime_ns),'inode':s.st_ino,'dev':s.st_dev}
def guard():
 assert Path.cwd()==B
 assert os.environ['HOME']=='/home/dw' and os.environ['CODEX_HOME']=='/home/dw/.codex'
 p=Path('/proc/255320');assert p.joinpath('stat').read_text().rsplit(')',1)[1].split()[19]=='49586940'
 lp=B/'.oi-runs/OI-EAW-WALL-20261114-01/.D004-writer.lock';s=lp.stat();fs=p.joinpath('fd/3').stat();assert s.st_ino==fs.st_ino==14866078 and s.st_dev==fs.st_dev
 assert 'FLOCK' in p.joinpath('fdinfo/3').read_text()
 f=os.open(lp,os.O_RDWR|os.O_NOFOLLOW|os.O_CLOEXEC)
 try:
  assert os.fstat(f).st_ino==14866078
  try:fcntl.flock(f,fcntl.LOCK_EX|fcntl.LOCK_NB);raise RuntimeError('unexpected free D004 lock')
  except BlockingIOError as e:assert e.errno==11
 finally:os.close(f)
 return {'at':now(),'pid':255320,'startticks':'49586940','inode':14866078,'competition_errno':11}
def env(extra=None):
 e=dict(os.environ);e.update(PYTHONDONTWRITEBYTECODE='1',TMPDIR=str(R/'tmp'),TMP=str(R/'tmp'),TEMP=str(R/'tmp'),XDG_CACHE_HOME=str(R/'cache'),GIT_OPTIONAL_LOCKS='0')
 if extra:e.update(extra)
 assert e['HOME']==os.environ['HOME'] and e['CODEX_HOME']==os.environ['CODEX_HOME']
 return e
def run(label,argv,scope,expected_writes,timeout=120,cwd=B,extra_env=None):
 assert 0<timeout<=1800
 out=R/'logs'/(label+'.stdout');err=R/'logs'/(label+'.stderr');receipt=R/'receipts'/(label+'.json')
 assert not out.exists() and not err.exists() and not receipt.exists()
 pre={'label':label,'at':now(),'argv':argv,'cwd':str(cwd),'input_scope':scope,'expected_writes':expected_writes,'timeout_seconds':timeout,'stop_method':'private process group TERM then KILL after 5s on timeout or stdout/stderr >5GiB; no automatic retry','output_paths':[str(out),str(err)],'env_overrides':{k:env(extra_env)[k] for k in ['PYTHONDONTWRITEBYTECODE','TMPDIR','TMP','TEMP','XDG_CACHE_HOME','GIT_OPTIONAL_LOCKS']},'lock':guard()}
 save(R/'receipts'/(label+'.pre.json'),pre);t=time.monotonic();stop=None
 with out.open('xb') as so,err.open('xb') as se:
  p=subprocess.Popen(argv,cwd=cwd,env=env(extra_env),stdin=subprocess.DEVNULL,stdout=so,stderr=se,start_new_session=True)
  while p.poll() is None:
   if time.monotonic()-t>timeout:stop='TIMEOUT'
   elif out.stat().st_size+err.stat().st_size>5*1024**3:stop='OUTPUT_SIZE_LIMIT'
   if stop:
    os.killpg(p.pid,signal.SIGTERM)
    try:p.wait(timeout=5)
    except subprocess.TimeoutExpired:os.killpg(p.pid,signal.SIGKILL);p.wait()
    break
   time.sleep(.05)
  rc=p.wait()
 post={**pre,'ended_at':now(),'exit_code':rc,'elapsed_seconds':time.monotonic()-t,'stop_reason':stop,'stdout':desc(out),'stderr':desc(err)};save(receipt,post)
 with (R/'logs/COMMAND_EXECUTIONS.jsonl').open('a') as f:f.write(json.dumps(post,ensure_ascii=False)+'\n')
 print(json.dumps({'label':label,'exit':rc,'elapsed_seconds':post['elapsed_seconds'],'stdout_bytes':post['stdout']['bytes'],'stderr_bytes':post['stderr']['bytes'],'receipt':str(receipt)},ensure_ascii=False),flush=True)
 return post
