from pathlib import Path
import os,sys,json,argparse,errno,fcntl,ctypes,datetime
assert sys.flags.isolated and sys.flags.no_site and sys.dont_write_bytecode
p=argparse.ArgumentParser();p.add_argument('--root',required=True);p.add_argument('--blocked-fd',type=int,required=True);p.add_argument('--role',choices=['main','child','grandchild'],default='main');a=p.parse_args();root=Path(a.root);checks=[];report={'record_type':'W004_R0A1_PROBE','role':a.role,'pid':os.getpid(),'ppid':os.getppid(),'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'checks':checks,'HOME':os.environ.get('HOME'),'CODEX_HOME':os.environ.get('CODEX_HOME')}
def check(name,condition,**details):
 checks.append({'name':name,'pass':bool(condition),**details})
 if not condition:raise RuntimeError(name)
def absent(path):
 try:os.lstat(path)
 except FileNotFoundError:return True
 return False
def deny_create(name,path):
 check(name+'_absent_before',absent(path),path=str(path))
 try:fd=os.open(path,os.O_WRONLY|os.O_CREAT|os.O_EXCL|os.O_CLOEXEC,0o600)
 except OSError as e:check(name+'_denied_at_open',e.errno in (errno.EACCES,errno.EPERM),path=str(path),errno=e.errno,error=str(e))
 else:
  os.close(fd);check(name+'_denied_at_open',False,path=str(path),outside_file_preserved=True)
 check(name+'_absent_after',absent(path),path=str(path))
def spawn(role):
 argv=['/usr/bin/python3.12','-I','-S','-B',str(Path(__file__).absolute()),'--root',str(root),'--blocked-fd',str(a.blocked_fd),'--role',role];pid=os.fork()
 if pid==0:
  try:os.execve(argv[0],argv,os.environ.copy())
  except BaseException:os._exit(74)
 got,status=os.waitpid(pid,0);check('inherited_'+role+'_PASS',got==pid and os.waitstatus_to_exitcode(status)==0,pid=pid,wait_status=status)
try:
 try:os.fstat(a.blocked_fd)
 except OSError as e:check('preopened_writable_external_fd_closed',e.errno==errno.EBADF,fd=a.blocked_fd,errno=e.errno)
 else:check('preopened_writable_external_fd_closed',False,fd=a.blocked_fd)
 flags=fcntl.fcntl(0,fcntl.F_GETFL);check('fd0_readonly_null',(flags&os.O_ACCMODE)==os.O_RDONLY and os.readlink('/proc/self/fd/0')=='/dev/null',F_GETFL_raw=flags,path=os.readlink('/proc/self/fd/0'))
 check('real_HOME_unchanged',os.environ.get('HOME')=='/home/dw');check('real_CODEX_HOME_unchanged',os.environ.get('CODEX_HOME')=='/home/dw/.codex')
 for label,path in [('HOME','/home/dw'),('CODEX_HOME','/home/dw/.codex')]:
  fd=os.open(path,os.O_RDONLY|os.O_DIRECTORY|os.O_CLOEXEC);info=os.fstat(fd);os.close(fd);check(label+'_readable',True,inode=info.st_ino,dev=info.st_dev)
 status=Path('/proc/self/status').read_text();ks={line.split(':',1)[0]:line.split(':',1)[1].strip() for line in status.splitlines() if line.startswith(('NoNewPrivs:','Seccomp:','Seccomp_filters:'))};report['kernel_status']=ks;check('NNP_and_seccomp_inherited',ks.get('NoNewPrivs')=='1' and ks.get('Seccomp')=='2')
 d=root/'probes'/('inside-'+a.role);os.mkdir(d,0o700);p=d/'new';q=d/'renamed';payload=('W004-'+a.role+'\n').encode();fd=os.open(p,os.O_WRONLY|os.O_CREAT|os.O_EXCL|os.O_CLOEXEC,0o600);amount=os.write(fd,payload);os.ftruncate(fd,len(payload));os.close(fd);check('inside_create_write_truncate',amount==len(payload) and p.read_bytes()==payload,path=str(p));os.rename(p,q);check('inside_rename',not p.exists() and q.read_bytes()==payload);os.unlink(q);os.rmdir(d);check('inside_remove',not d.exists())
 outside=root.parent/'.W004-deny-outside-C0012-e9ed948d';deny_create('OUTSIDE',outside)
 if a.role=='main':
  shared=Path('/dwdhome/fy/BASE_E6_2/edh-universe/frp/frp')
  for label,path in [('SHARED',shared/'.W004-deny-shared-C0012-e9ed948d'),('HOME',Path('/home/dw/.W004-deny-home-C0012-e9ed948d')),('CODEX_HOME',Path('/home/dw/.codex/.W004-deny-codex-C0012-e9ed948d'))]:deny_create(label,path)
  target=shared/'.W004-deny-symlink-C0012-e9ed948d';check('SYMLINK_TARGET_absent',absent(target));link=root/'probes'/'escape';os.symlink(str(shared),link);deny_create('SYMLINK_ESCAPE',link/target.name);check('SYMLINK_TARGET_still_absent',absent(target));os.unlink(link)
 libc=ctypes.CDLL(None,use_errno=True);libc.syscall.restype=ctypes.c_long
 for name,nr,args in [('socket',41,[ctypes.c_long(2),ctypes.c_long(1),ctypes.c_long(0)]),('connect',42,[ctypes.c_long(-1),ctypes.c_void_p(),ctypes.c_long(0)])]:
  ctypes.set_errno(0);rc=libc.syscall(ctypes.c_long(nr),*args);err=ctypes.get_errno();check('network_'+name+'_denied',rc==-1 and err==errno.EPERM,return_value=rc,errno=err,no_destination_or_connection=True)
 holder=Path('/proc/243622/fdinfo/3').read_text();check('controller_holder_still_has_FLOCK','FLOCK' in holder and 'WRITE 243622' in holder)
 if a.role=='main':spawn('child')
 elif a.role=='child':spawn('grandchild')
 report['status']='PROBE_PASS';rc=0
except BaseException as e:report['status']='PROBE_FAIL';report['error']={'type':type(e).__name__,'text':str(e)};rc=1
out=root/'receipts'/('r0a1-'+a.role+'.json');out.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n');print(json.dumps({'role':a.role,'status':report['status'],'report':str(out)},ensure_ascii=False),flush=True);raise SystemExit(rc)
