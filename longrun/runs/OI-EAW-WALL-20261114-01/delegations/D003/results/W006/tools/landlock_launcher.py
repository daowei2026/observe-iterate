from pathlib import Path
import os,sys,ctypes,fcntl,errno,json,hashlib,argparse,stat,datetime,traceback
assert sys.flags.isolated and sys.flags.no_site and sys.dont_write_bytecode
p=argparse.ArgumentParser();p.add_argument('--root',required=True);p.add_argument('--report',required=True);p.add_argument('--blocked-inherited-fd',type=int,required=True)
for n in ['tmp','cache','config']:p.add_argument('--task-'+n,required=True)
p.add_argument('command',nargs=argparse.REMAINDER);a=p.parse_args();root=Path(a.root);report=Path(a.report)
assert root==root.resolve() and root.is_dir() and report.resolve().is_relative_to(root) and not report.exists()
assert not any(q.is_symlink() for q in [root,*root.parents]) and os.uname().machine=='x86_64'
assert os.environ.get('HOME')=='/home/dw' and os.environ.get('CODEX_HOME')=='/home/dw/.codex'
for n in ['tmp','cache','config']:assert Path(getattr(a,'task_'+n)).resolve().is_relative_to(root)
command=a.command[1:] if a.command[:1]==['--'] else a.command;assert command and Path(command[0]).is_absolute()
libc=ctypes.CDLL(None,use_errno=True);libc.syscall.restype=ctypes.c_long;libc.prctl.restype=ctypes.c_int
calls=[];info={'record_type':'W006_LANDLOCK_AND_SECCOMP_LAUNCHER','utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'root':str(root),'root_realpath':str(root.resolve()),'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'HOME':os.environ['HOME'],'CODEX_HOME':os.environ['CODEX_HOME'],'HOME_or_CODEX_HOME_reset':False,'explicit_task_directories':{n:getattr(a,'task_'+n) for n in ['tmp','cache','config']},'filesystem_write_exceptions':[],'calls':calls,'command':command}
def invoke(name,fn,*args):
 ctypes.set_errno(0);rc=fn(*args);err=ctypes.get_errno();calls.append({'operation':name,'return':int(rc),'errno':err});return rc
try:
 inherited=[]
 for entry in os.listdir('/proc/self/fd'):
  fd=int(entry)
  try:flags=fcntl.fcntl(fd,fcntl.F_GETFL);path=os.readlink('/proc/self/fd/'+entry);fs=os.fstat(fd)
  except OSError as e:
   if e.errno==errno.EBADF or e.errno==errno.ENOENT:continue
   raise
  access=flags & os.O_ACCMODE;writable=access in (os.O_WRONLY,os.O_RDWR)
  if fd<=2:
   info.setdefault('stdio_fds',[]).append({'fd':fd,'path':path,'flags':flags,'access_mode':access,'writable':writable,'inode':fs.st_ino,'nlink':fs.st_nlink})
   if fd==0:assert not writable
   else:assert writable and stat.S_ISREG(fs.st_mode) and fs.st_nlink==1 and Path(path).resolve().is_relative_to(root)
  else:
   inherited.append({'fd':fd,'path':path,'flags':flags,'writable':writable,'closed_before_restrict_and_exec':True});os.close(fd)
 assert any(x['fd']==a.blocked_inherited_fd and x['writable'] and x['path'].endswith('/.D003-writer.lock') for x in inherited)
 info['inherited_nonstdio_fds_closed']=inherited
 abi=invoke('landlock_create_ruleset_VERSION',libc.syscall,ctypes.c_long(444),ctypes.c_void_p(),ctypes.c_size_t(0),ctypes.c_uint(1));info['abi']=abi;assert abi==6
 # ABI1 write/create/remove rights plus ABI2 REFER, ABI3 TRUNCATE, ABI5 IOCTL_DEV.
 rights={n:(1<<i) for n,i in [('WRITE_FILE',1),('REMOVE_DIR',4),('REMOVE_FILE',5),('MAKE_CHAR',6),('MAKE_DIR',7),('MAKE_REG',8),('MAKE_SOCK',9),('MAKE_FIFO',10),('MAKE_BLOCK',11),('MAKE_SYM',12),('REFER',13),('TRUNCATE',14),('IOCTL_DEV',15)]};handled=sum(rights.values());info['handled_filesystem_rights']=rights;info['handled_access_fs']=handled
 class Ruleset(ctypes.Structure):_fields_=[('handled_access_fs',ctypes.c_uint64),('handled_access_net',ctypes.c_uint64)]
 class Beneath(ctypes.Structure):_pack_=1;_fields_=[('allowed_access',ctypes.c_uint64),('parent_fd',ctypes.c_int32)]
 attr=Ruleset(handled,3)
 assert invoke('prctl_PR_SET_NO_NEW_PRIVS',libc.prctl,ctypes.c_int(38),ctypes.c_ulong(1),ctypes.c_ulong(0),ctypes.c_ulong(0),ctypes.c_ulong(0))==0
 rulesfd=invoke('landlock_create_ruleset',libc.syscall,ctypes.c_long(444),ctypes.byref(attr),ctypes.c_size_t(ctypes.sizeof(attr)),ctypes.c_uint(0));assert rulesfd>=0
 rootfd=os.open(root,os.O_PATH|os.O_DIRECTORY|os.O_CLOEXEC);beneath=Beneath(handled,rootfd)
 assert invoke('landlock_add_rule_PATH_BENEATH_only_WORK_ROOT',libc.syscall,ctypes.c_long(445),ctypes.c_int(rulesfd),ctypes.c_uint(1),ctypes.byref(beneath),ctypes.c_uint(0))==0
 assert invoke('landlock_restrict_self',libc.syscall,ctypes.c_long(446),ctypes.c_int(rulesfd),ctypes.c_uint(0))==0
 os.close(rootfd);os.close(rulesfd)
 # Landlock does not mediate all metadata mutation APIs. Deny these globally,
 # including inside root, rather than creating any external write exception.
 denied={'socket':41,'connect':42,'accept':43,'sendto':44,'recvfrom':45,'sendmsg':46,'recvmsg':47,'shutdown':48,'bind':49,'listen':50,'getsockname':51,'getpeername':52,'socketpair':53,'setsockopt':54,'getsockopt':55,'accept4':288,'recvmmsg':299,'sendmmsg':307,'ioctl':16,'chmod':90,'fchmod':91,'chown':92,'fchown':93,'lchown':94,'utime':132,'utimes':235,'futimesat':261,'utimensat':280,'fchmodat':268,'fchmodat2':452,'fchownat':260,'setxattr':188,'lsetxattr':189,'fsetxattr':190,'removexattr':197,'lremovexattr':198,'fremovexattr':199,'mount':165,'umount2':166,'pivot_root':155,'chroot':161,'open_by_handle_at':304,'ptrace':101,'process_vm_writev':311,'io_uring_setup':425,'io_uring_enter':426,'io_uring_register':427,'acct':163,'quotactl':179,'swapon':167,'swapoff':168,'reboot':169,'sethostname':170,'setdomainname':171,'sync':162}
 class Insn(ctypes.Structure):_fields_=[('code',ctypes.c_ushort),('jt',ctypes.c_ubyte),('jf',ctypes.c_ubyte),('k',ctypes.c_uint)]
 class Prog(ctypes.Structure):_fields_=[('length',ctypes.c_ushort),('filter',ctypes.POINTER(Insn))]
 RET_ERRNO=0x50000|errno.EPERM;program=[(0x20,0,0,4),(0x15,1,0,0xc000003e),(0x06,0,0,0x80000000),(0x20,0,0,0),(0x45,0,1,0x40000000),(0x06,0,0,RET_ERRNO)]
 program.extend([(21, 0, 6, 16), (32, 0, 0, 28), (21, 0, 3, 0), (32, 0, 0, 24), (21, 0, 1, 21585), (6, 0, 0, 2147418112), (6, 0, 0, 327681)])
 for nr in sorted(set(denied.values())-{16}):program.extend([(0x15,0,1,nr),(0x06,0,0,RET_ERRNO)])
 # Deny PR_SET_NAME, which could otherwise mutate the procfs-visible comm.
 program.extend([(0x15,0,3,157),(0x20,0,0,16),(0x15,0,1,15),(0x06,0,0,RET_ERRNO),(0x06,0,0,0x7fff0000)])
 instructions=(Insn*len(program))(*(Insn(*x) for x in program));prog=Prog(len(program),instructions)
 assert invoke('prctl_PR_SET_SECCOMP_FILTER',libc.prctl,ctypes.c_int(22),ctypes.c_ulong(2),ctypes.byref(prog),ctypes.c_ulong(0),ctypes.c_ulong(0))==0
 info['seccomp_denied_syscalls']=denied;info['seccomp_denied_prctl_options']=['PR_SET_NAME'];info['network_policy']='Landlock TCP bind/connect denied plus seccomp all socket/connect/send/recv calls denied; no inherited nonstdio fd survives';info['global_reads_permitted_by_landlock']=True;info['status']='KERNEL_POLICY_INSTALLED_BEFORE_EXEC'
 report.write_text(json.dumps(info,ensure_ascii=False,indent=2)+'\n');os.execve(command[0],command,os.environ.copy())
except BaseException as exc:
 info['status']='LAUNCHER_FAILED';info['error']={'type':type(exc).__name__,'text':str(exc),'traceback':traceback.format_exc()}
 try:report.write_text(json.dumps(info,ensure_ascii=False,indent=2)+'\n')
 except BaseException as nested:print(json.dumps({'launcher_error':info,'report_write_error':str(nested)},ensure_ascii=False),flush=True)
 raise SystemExit(73)
