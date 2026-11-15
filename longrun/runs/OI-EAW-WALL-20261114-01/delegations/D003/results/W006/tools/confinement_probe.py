from pathlib import Path
import argparse, ctypes, errno, fcntl, json, os, stat, sys, traceback

p=argparse.ArgumentParser()
p.add_argument('--root',required=True);p.add_argument('--blocked-inherited-fd',required=True,type=int)
p.add_argument('--role',choices=['main','child','grandchild'],default='main')
a=p.parse_args();root=Path(a.root)
assert root==root.resolve() and root.name=='W006'
report=root/'receipts'/('probe-'+a.role+'.json')
result={'role':a.role,'pid':os.getpid(),'ppid':os.getppid(),'root':str(root),'status':'STARTING','checks':[]}
def check(name,value,**details):
    result['checks'].append({'name':name,'PASS':bool(value),**details})
    if not value:raise RuntimeError('PROBE_FAILED '+name)
def absent(path):
    try:os.lstat(path)
    except FileNotFoundError as e:return e.errno==errno.ENOENT
    return False
def deny_create(name,open_path,negative_target,follow_symlink=False):
    check(name+'_target_absent_before',absent(negative_target),path=str(negative_target))
    flags=os.O_WRONLY|os.O_CREAT|os.O_CLOEXEC
    if not follow_symlink:flags|=os.O_EXCL
    try:fd=os.open(open_path,flags,0o600)
    except OSError as e:check(name+'_kernel_open_denied',e.errno in [errno.EACCES,errno.EPERM],path=str(open_path),target=str(negative_target),errno=e.errno)
    else:
        os.close(fd)
        check(name+'_unexpected_outside_open',False,path=str(open_path),target=str(negative_target),created_file_preserved_no_cleanup=True)
    check(name+'_target_absent_after',absent(negative_target),path=str(negative_target))
try:
    # Before opening any new persistent descriptor, verify inherited writable FD was closed.
    try:os.fstat(a.blocked_inherited_fd)
    except OSError as e:check('inherited_writable_lock_fd_closed',e.errno==errno.EBADF,fd=a.blocked_inherited_fd,errno=e.errno)
    else:check('inherited_writable_lock_fd_closed',False,fd=a.blocked_inherited_fd)
    b=json.loads((root/'artifacts/W006_BINDING.json').read_bytes());negative=b['negative_targets'];holder=b['fresh_lock']
    check('actual_HOME_CODEX_preserved',os.environ['HOME']==b['HOME']=='/home/dw' and os.environ['CODEX_HOME']==b['CODEX_HOME']=='/home/dw/.codex',HOME=os.environ['HOME'],CODEX_HOME=os.environ['CODEX_HOME'])
    check('stdin_readonly',fcntl.fcntl(0,fcntl.F_GETFL)&os.O_ACCMODE==os.O_RDONLY,path=os.readlink('/proc/self/fd/0'))
    for fd in [1,2]:
        fs=os.fstat(fd);path=os.readlink('/proc/self/fd/'+str(fd))
        check('stdio_'+str(fd)+'_inside_single_link_regular',stat.S_ISREG(fs.st_mode) and fs.st_nlink==1 and Path(path).resolve().is_relative_to(root),path=path)
    status=dict(x.split(':',1) for x in Path('/proc/self/status').read_text().splitlines() if ':' in x)
    check('NNP_and_seccomp_inherited',status['NoNewPrivs'].strip()=='1' and status['Seccomp'].strip()=='2',NoNewPrivs=status['NoNewPrivs'].strip(),Seccomp=status['Seccomp'].strip())
    info=Path('/proc/'+str(holder['holder_pid'])+'/fdinfo/'+str(holder['fd'])).read_text()
    check('controller_holder_lock_intact','FLOCK' in info and 'WRITE '+str(holder['holder_pid']) in info and Path(holder['path']).lstat().st_ino==holder['inode'],holder_pid=holder['holder_pid'],inode=holder['inode'],fdinfo=info)
    inside=root/'probes'/('inside-'+a.role);inside.mkdir()
    first=inside/'created.txt';renamed=inside/'renamed.txt'
    fd=os.open(first,os.O_WRONLY|os.O_CREAT|os.O_EXCL|os.O_CLOEXEC,0o600)
    try:
        check('inside_write',os.write(fd,b'W006 engineering confinement probe\n')==35)
        initial=fcntl.fcntl(fd,fcntl.F_GETFD)
        fcntl.fcntl(fd,fcntl.F_SETFD,initial&~fcntl.FD_CLOEXEC)
        before=fcntl.fcntl(fd,fcntl.F_GETFD)
        request=json.loads((root/'artifacts/FIOCLEX_LOCAL_CONSTANT_VERIFICATION.json').read_bytes())['symbols']['FIOCLEX']['decimal']
        rc=fcntl.ioctl(fd,request)
        after=fcntl.fcntl(fd,fcntl.F_GETFD)
        check('FIOCLEX_success_sets_FD_CLOEXEC',rc==0 and not before&fcntl.FD_CLOEXEC and bool(after&fcntl.FD_CLOEXEC),request=request,request_hex=hex(request),ioctl_return=rc,F_GETFD_initial=initial,F_GETFD_before=before,F_GETFD_after=after,fd=fd,path=str(first))
        os.ftruncate(fd,4)
    finally:os.close(fd)
    first.rename(renamed);check('inside_rename',renamed.is_file() and not first.exists())
    renamed.unlink();check('inside_remove',not renamed.exists())
    deny_create('OUTSIDE',negative['OUTSIDE'],negative['OUTSIDE'])
    if a.role=='main':
        deny_create('SHARED',negative['SHARED'],negative['SHARED'])
        for label,env in [('HOME','HOME'),('CODEX_HOME','CODEX_HOME')]:
            fd=os.open(os.environ[env],os.O_RDONLY|os.O_DIRECTORY|os.O_CLOEXEC);os.close(fd)
            check(label+'_readonly_directory_open',True,path=os.environ[env])
            deny_create(label,negative[label],negative[label])
        link=inside/'escape-link';link.symlink_to(negative['SYMLINK_TARGET'])
        deny_create('SYMLINK_ESCAPE',link,negative['SYMLINK_TARGET'],follow_symlink=True)
        link.unlink()
    libc=ctypes.CDLL(None,use_errno=True);libc.syscall.restype=ctypes.c_long
    ctypes.set_errno(0);rc=libc.syscall(ctypes.c_long(41),ctypes.c_int(2),ctypes.c_int(1),ctypes.c_int(0));err=ctypes.get_errno()
    if rc>=0:os.close(rc)
    check('network_socket_denied',rc==-1 and err==errno.EPERM,return_value=rc,errno=err)
    ctypes.set_errno(0);rc=libc.syscall(ctypes.c_long(42),ctypes.c_int(-1),ctypes.c_void_p(),ctypes.c_uint(0));err=ctypes.get_errno()
    check('network_connect_denied_before_badfd',rc==-1 and err==errno.EPERM,return_value=rc,errno=err,no_destination_contacted=True)
    if a.role!='grandchild':
        role='child' if a.role=='main' else 'grandchild'
        pid=os.fork()
        if pid==0:
            try:os.execve('/usr/bin/python3.12',['/usr/bin/python3.12','-I','-S','-B',str(Path(__file__).resolve()),'--root',str(root),'--blocked-inherited-fd',str(a.blocked_inherited_fd),'--role',role],os.environ.copy())
            except BaseException:os._exit(74)
        waited,status=os.waitpid(pid,0)
        check(role+'_restriction_probe_success',waited==pid and os.WIFEXITED(status) and os.WEXITSTATUS(status)==0,pid=pid,wait_status=status)
    result['status']='PASS'
except BaseException as exc:
    result['status']='FAILED_STOP';result['error']={'type':type(exc).__name__,'text':str(exc),'traceback':traceback.format_exc()}
with report.open('x') as f:f.write(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'role':a.role,'status':result['status'],'report':str(report)},ensure_ascii=False),flush=True)
raise SystemExit(0 if result['status']=='PASS' else 1)
