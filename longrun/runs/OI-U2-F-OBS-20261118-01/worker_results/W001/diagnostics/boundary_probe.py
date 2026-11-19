import ctypes, json, os, platform, runpy, sys
from pathlib import Path
run=Path(__file__).resolve().parent.parent
target=Path(sys.argv[1]).resolve()
args=sys.argv[2:]
runtime={'python_executable':sys.executable,'python_realpath':str(Path(sys.executable).resolve()),'python_version':sys.version,'cwd':os.getcwd(),'target':str(target),'target_args':args,'pythonpath':os.environ.get('PYTHONPATH'),'equivalent_entry':'existing run-python.sh environment; no writes to its .migration logs'}
libc=ctypes.CDLL(None,use_errno=True)
abi=libc.syscall(444,0,0,1)
runtime['landlock_abi']=abi
if abi>=1:
    handled=(1<<1)|sum(1<<bit for bit in range(4,13))
    if abi>=2: handled|=1<<13
    if abi>=3: handled|=1<<14
    class Ruleset(ctypes.Structure): _fields_=[('handled_access_fs',ctypes.c_uint64)]
    class Beneath(ctypes.Structure):
        _pack_=1
        _fields_=[('allowed_access',ctypes.c_uint64),('parent_fd',ctypes.c_int32)]
    ruleset=Ruleset(handled)
    fd=libc.syscall(444,ctypes.byref(ruleset),ctypes.sizeof(ruleset),0)
    if fd<0: raise OSError(ctypes.get_errno(),'landlock_create_ruleset')
    rootfd=os.open(run,os.O_PATH|os.O_CLOEXEC)
    rule=Beneath(handled,rootfd)
    if libc.syscall(445,fd,1,ctypes.byref(rule),0)<0: raise OSError(ctypes.get_errno(),'landlock_add_rule')
    if libc.prctl(38,1,0,0,0)<0: raise OSError(ctypes.get_errno(),'PR_SET_NO_NEW_PRIVS')
    if libc.syscall(446,fd,0)<0: raise OSError(ctypes.get_errno(),'landlock_restrict_self')
    os.close(rootfd); os.close(fd)
    runtime['write_boundary']='kernel Landlock: writes only under W001; reads retain existing access'
else:
    runtime['write_boundary']='Python audit guard (kernel Landlock unavailable)'
    def audit(event, event_args):
        path=None
        if event=='open':
            name,mode,flags=event_args
            if isinstance(name,(str,bytes,os.PathLike)) and (flags & (os.O_WRONLY|os.O_RDWR|os.O_CREAT|os.O_TRUNC|os.O_APPEND)):
                path=Path(os.fsdecode(name)).resolve()
        elif event in ('os.mkdir','os.remove','os.rmdir','os.truncate','os.chmod','os.chown','os.utime'):
            if isinstance(event_args[0],(str,bytes,os.PathLike)): path=Path(os.fsdecode(event_args[0])).resolve()
        if path is not None and not path.is_relative_to(run):
            raise PermissionError('W001 allowed_writes boundary: '+str(path))
    sys.addaudithook(audit)
(run/'logs/semlock_probe_runtime.json').write_text(json.dumps(runtime,ensure_ascii=False,indent=2)+'\n')
sys.argv=[str(target),*args]
sys.path[0]=str(target.parent)
runpy.run_path(str(target),run_name='__main__')
