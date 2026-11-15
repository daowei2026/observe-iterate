from pathlib import Path
import os,sys,json,hashlib,datetime,time,fcntl,errno,subprocess,signal
ROOT=Path('/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D003/W004');BASE=Path('/dwdhome/fy/BASE_E6_2');LOCK=ROOT.parents[1]/'.D003-writer.lock'
def utc():return datetime.datetime.now(datetime.timezone.utc).isoformat()
def guard():
 assert Path.cwd()==BASE and ROOT.resolve()==ROOT and not any(p.is_symlink() for p in ROOT.parents)
 assert os.environ['HOME']=='/home/dw' and os.environ['CODEX_HOME']=='/home/dw/.codex'
 t=Path('/proc/243622/stat').read_text();assert t[t.rfind(')')+2:].split()[19]=='47124402';assert LOCK.lstat().st_ino==14806399
 info=Path('/proc/243622/fdinfo/3').read_text();assert 'FLOCK' in info and 'WRITE 243622' in info
 fd=os.open(LOCK,os.O_RDWR|os.O_NOFOLLOW)
 try:
  try:fcntl.flock(fd,fcntl.LOCK_EX|fcntl.LOCK_NB)
  except BlockingIOError as e:assert e.errno in (errno.EACCES,errno.EAGAIN)
  else:raise RuntimeError('STOP unexpected lock acquisition')
 finally:os.close(fd)
def save(rel,obj):
 p=ROOT/rel;assert p.resolve().is_relative_to(ROOT);p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n');return p
def filefact(p):
 p=Path(p);b=p.read_bytes();s=p.lstat();return {'path':str(p),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'mtime_ns':s.st_mtime_ns,'inode':s.st_ino,'dev':s.st_dev}
def run(label,argv,limit=45,pass_fds=()):
 guard();assert Path(argv[0]).is_absolute();out=ROOT/'logs'/(label+'.stdout');err=ROOT/'logs'/(label+'.stderr');assert not out.exists() and not err.exists()
 start=utc();tick=time.monotonic();timed=False
 with out.open('xb') as so,err.open('xb') as se:
  stdin_fd=os.open('/dev/null',os.O_RDONLY|os.O_CLOEXEC)
  flags=fcntl.fcntl(stdin_fd,fcntl.F_GETFL)
  assert (flags & os.O_ACCMODE)==os.O_RDONLY
  stdin_record={'opened_path':'/dev/null','F_GETFL_raw':flags,'access_mode':'O_RDONLY','parent_fd':stdin_fd,'parent_pid':os.getpid(),'opened_at':utc(),'child_pid':None}
  try:
   child=subprocess.Popen(argv,cwd=BASE,env=os.environ.copy(),stdin=stdin_fd,stdout=so,stderr=se,pass_fds=pass_fds,start_new_session=True)
   stdin_record['child_pid']=child.pid
  finally:
   os.close(stdin_fd)
   stdin_record['parent_close_timestamp']=utc()
   stdin_record['parent_close_result']='CLOSED_OWN_COPY_SUCCESS'
   save('receipts/'+label+'-parent-stdin.json',stdin_record)
  try:rc=child.wait(timeout=limit)
  except subprocess.TimeoutExpired:
   timed=True;os.killpg(child.pid,signal.SIGKILL);rc=child.wait()
 record={'id':label,'argv':argv,'cwd':str(BASE),'started_at':start,'completed_at':utc(),'elapsed_seconds':time.monotonic()-tick,'pid':child.pid,'new_process_group':child.pid,'exit_code':rc,'timeout_seconds':limit,'timeout':timed,'HOME':os.environ['HOME'],'CODEX_HOME':os.environ['CODEX_HOME'],'environment_preserved':True,'pass_fds':list(pass_fds),'stdout':filefact(out),'stderr':filefact(err)}
 with (ROOT/'logs/COMMAND_LOG.jsonl').open('a') as f:f.write(json.dumps(record,ensure_ascii=False)+'\n')
 print(json.dumps({'id':label,'exit_code':rc,'elapsed_seconds':record['elapsed_seconds'],'stdout':record['stdout'],'stderr':record['stderr']},ensure_ascii=False));print(out.read_text(errors='replace')[:2000]);print(err.read_text(errors='replace')[:2000]);guard();return record
