from pathlib import Path
import os,sys,json,errno,ctypes,argparse,datetime
assert sys.flags.isolated and sys.flags.no_site and sys.dont_write_bytecode
p=argparse.ArgumentParser();p.add_argument('--root',required=True);p.add_argument('--stage',choices=['positive','negative'],required=True);p.add_argument('--role',choices=['main','child','grandchild'],default='main');p.add_argument('--forbidden-fd',type=int,required=True);p.add_argument('--confirmed-outside')
a=p.parse_args();root=Path(a.root);checks=[];state={'record_type':'W003_CONFINEMENT_PROBE','stage':a.stage,'role':a.role,'pid':os.getpid(),'ppid':os.getppid(),'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'checks':checks,'HOME':os.environ.get('HOME'),'CODEX_HOME':os.environ.get('CODEX_HOME')}
def check(name,condition,**detail):
 checks.append({'name':name,'pass':bool(condition),**detail})
 if not condition:raise RuntimeError(name)
def absent(path):
 try:os.lstat(path)
 except FileNotFoundError:return True
 return False
def denied_create(name,path):
 check(name+'_absent_before',absent(path),path=str(path))
 try:fd=os.open(path,os.O_WRONLY|os.O_CREAT|os.O_EXCL|os.O_CLOEXEC,0o600)
 except OSError as e:
  check(name+'_kernel_denial',e.errno in (errno.EPERM,errno.EACCES),path=str(path),errno=e.errno,error=str(e))
 else:
  os.close(fd)
  check(name+'_kernel_denial',False,path=str(path),unexpected_external_file_preserved=True)
 check(name+'_absent_after',absent(path),path=str(path))
def spawn(role):
 args=['/usr/bin/python3.12','-I','-S','-B',str(Path(__file__).absolute()),'--root',str(root),'--stage',a.stage,'--role',role,'--forbidden-fd',str(a.forbidden_fd)]
 if a.confirmed_outside:args+=['--confirmed-outside',a.confirmed_outside]
 pid=os.fork()
 if pid==0:
  try:os.execve(args[0],args,os.environ.copy())
  except BaseException:os._exit(74)
 got,status=os.waitpid(pid,0)
 check('inherited_'+role+'_exit',got==pid and os.waitstatus_to_exitcode(status)==0,pid=pid,wait_status=status)
try:
 try:os.fstat(a.forbidden_fd)
 except OSError as e:check('preopened_external_writable_fd_closed',e.errno==errno.EBADF,fd=a.forbidden_fd,errno=e.errno)
 else:check('preopened_external_writable_fd_closed',False,fd=a.forbidden_fd)
 check('actual_HOME_unchanged',os.environ.get('HOME')=='/home/dw')
 check('actual_CODEX_HOME_unchanged',os.environ.get('CODEX_HOME')=='/home/dw/.codex')
 status=Path('/proc/self/status').read_text();selected={s.split(':',1)[0]:s.split(':',1)[1].strip() for s in status.splitlines() if s.startswith(('NoNewPrivs:','Seccomp:','Seccomp_filters:'))};state['kernel_status']=selected
 check('no_new_privs_and_seccomp_filter',selected.get('NoNewPrivs')=='1' and selected.get('Seccomp')=='2')
 for label,path in [('HOME','/home/dw'),('CODEX_HOME','/home/dw/.codex')]:
  fd=os.open(path,os.O_RDONLY|os.O_DIRECTORY|os.O_CLOEXEC);fs=os.fstat(fd);os.close(fd);check(label+'_readonly_directory_open',True,inode=fs.st_ino,dev=fs.st_dev)
 if a.stage=='positive':
  directory=root/'probes'/('positive-'+a.role);os.mkdir(directory,0o700)
  before=directory/'created';after=directory/'renamed';payload=('W003-inside-'+a.role+'\n').encode()
  fd=os.open(before,os.O_WRONLY|os.O_CREAT|os.O_EXCL|os.O_CLOEXEC,0o600)
  amount=os.write(fd,payload);os.close(fd);check('inside_create_write',amount==len(payload),path=str(before),written=amount)
  os.rename(before,after);check('inside_rename',not before.exists() and after.read_bytes()==payload,path=str(after))
  fd=os.open(after,os.O_WRONLY|os.O_CLOEXEC);os.ftruncate(fd,4);os.close(fd);check('inside_ftruncate',after.stat().st_size==4)
  os.unlink(after);os.rmdir(directory);check('inside_remove',not directory.exists())
  libc=ctypes.CDLL(None,use_errno=True);libc.syscall.restype=ctypes.c_long
  ctypes.set_errno(0);rc=libc.syscall(ctypes.c_long(41),ctypes.c_long(2),ctypes.c_long(1),ctypes.c_long(0));err=ctypes.get_errno();check('network_socket_denied_without_destination',rc==-1 and err==errno.EPERM,return_value=rc,errno=err)
  ctypes.set_errno(0);rc=libc.syscall(ctypes.c_long(42),ctypes.c_long(-1),ctypes.c_void_p(),ctypes.c_long(0));err=ctypes.get_errno();check('network_connect_denied_before_fd_validation',rc==-1 and err==errno.EPERM,return_value=rc,errno=err)
 else:
  outside=Path(a.confirmed_outside or '')
  check('controller_confirmation_path_matches_plan',str(outside)=='/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D003/.W003-deny-outside-240810-46501758')
  denied_create('outside_sentinel',outside)
  if a.role=='main':
   for label,path in [('shared','/dwdhome/fy/BASE_E6_2/edh-universe/frp/frp/.W003-deny-shared-240810-46501758'),('HOME','/home/dw/.W003-deny-home-240810-46501758'),('CODEX_HOME','/home/dw/.codex/.W003-deny-codex-240810-46501758')]:denied_create(label,Path(path))
   target=Path('/dwdhome/fy/BASE_E6_2/edh-universe/frp/frp/.W003-deny-symlink-240810-46501758');check('symlink_target_absent_before',absent(target),path=str(target))
   link=root/'probes'/'escape-link';os.symlink(str(target.parent),link);denied_create('symlink_escape',link/target.name);check('symlink_target_absent_after',absent(target));os.unlink(link)
 if a.role=='main':spawn('child')
 elif a.role=='child':spawn('grandchild')
 state['status']='SUBSTAGE_PASS'
except BaseException as e:
 state['status']='SUBSTAGE_FAIL';state['error']={'type':type(e).__name__,'text':str(e)}
 finally_status=1
else:finally_status=0
report=root/'receipts'/('r0a-'+a.stage+'-'+a.role+'.json');report.write_text(json.dumps(state,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'stage':a.stage,'role':a.role,'status':state['status'],'report':str(report)},ensure_ascii=False),flush=True)
raise SystemExit(finally_status)
