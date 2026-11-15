from pathlib import Path
import datetime, errno, fcntl, hashlib, json, os, sys
ROOT=Path('/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D003/W006')
BASE=Path('/dwdhome/fy/BASE_E6_2')
def utc():return datetime.datetime.now(datetime.timezone.utc).isoformat()
def fact(p):
    p=Path(p);b=p.read_bytes();s=p.lstat()
    return {'path':str(p),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'mtime_ns':s.st_mtime_ns,'mtime_ns_exact':str(s.st_mtime_ns),'inode':s.st_ino,'dev':s.st_dev}
def save(rel,obj):
    p=ROOT/rel;assert p.resolve().is_relative_to(ROOT) and p.parent.is_dir()
    with p.open('x') as f:f.write(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
    return p
def binding():return json.loads((ROOT/'artifacts/W006_BINDING.json').read_bytes())
def guard():
    b=binding();lock=b['fresh_lock'];pid=lock['holder_pid'];path=Path(lock['path'])
    assert Path.cwd()==BASE and ROOT.resolve()==ROOT and not any(p.is_symlink() for p in [ROOT,*ROOT.parents])
    assert b['write_root']==str(ROOT) and b['work_order_id']=='W006'
    assert os.environ['HOME']==b['HOME']=='/home/dw' and os.environ['CODEX_HOME']==b['CODEX_HOME']=='/home/dw/.codex' and sys.dont_write_bytecode
    t=Path('/proc/'+str(pid)+'/stat').read_text();assert t[t.rfind(')')+2:].split()[19]==lock['startticks']
    info=Path('/proc/'+str(pid)+'/fdinfo/'+str(lock['fd'])).read_text()
    assert 'FLOCK' in info and 'WRITE '+str(pid) in info and path.lstat().st_ino==lock['inode']
    fd=os.open(path,os.O_RDWR|os.O_NOFOLLOW)
    try:
        assert os.fstat(fd).st_ino==lock['inode']
        try:fcntl.flock(fd,fcntl.LOCK_EX|fcntl.LOCK_NB)
        except BlockingIOError as e:competition=e.errno;assert e.errno in (errno.EAGAIN,errno.EACCES)
        else:raise RuntimeError('STOP unexpected writer lock acquisition')
    finally:os.close(fd)
    return {'at':utc(),'holder_pid':pid,'startticks':lock['startticks'],'inode':lock['inode'],'fdinfo':info,'same_inode_independent_competition_errno':competition,'only_own_contender_closed':True,'holder_untouched':True}
