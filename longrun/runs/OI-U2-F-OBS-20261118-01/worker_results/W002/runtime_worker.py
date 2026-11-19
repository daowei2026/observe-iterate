import ctypes
import datetime
import json
import os
from pathlib import Path
import subprocess
import sys
import time
import traceback

run = Path(__file__).resolve().parent
source = run / 'source/observe-iterate'
proof = json.loads((run/'logs/private_shm_mount.alias_report.json').read_text())
assert proof['verified'] is True
assert Path(proof['backing']).resolve() == (run/'runtime/shm').resolve()
alias_stat = Path('/dev/shm').stat()
backing_stat = (run/'runtime/shm').stat()
assert (alias_stat.st_dev,alias_stat.st_ino) == (backing_stat.st_dev,backing_stat.st_ino)

libc = ctypes.CDLL(None,use_errno=True)
abi = libc.syscall(444,0,0,1)
if abi < 1:
    raise RuntimeError('Required run-root write boundary is unavailable; no fallback host shm writes')
handled = (1<<1) | sum(1<<bit for bit in range(4,13))
if abi >= 2:
    handled |= 1<<13
if abi >= 3:
    handled |= 1<<14

class Ruleset(ctypes.Structure):
    _fields_ = [('handled_access_fs',ctypes.c_uint64)]

class Beneath(ctypes.Structure):
    _pack_ = 1
    _fields_ = [('allowed_access',ctypes.c_uint64),('parent_fd',ctypes.c_int32)]

ruleset = Ruleset(handled)
ruleset_fd = libc.syscall(444,ctypes.byref(ruleset),ctypes.sizeof(ruleset),0)
if ruleset_fd < 0:
    raise OSError(ctypes.get_errno(),'landlock_create_ruleset')
for path in (run,Path('/dev/shm')):
    directory_fd = os.open(path,os.O_PATH|os.O_CLOEXEC)
    rule = Beneath(handled,directory_fd)
    if libc.syscall(445,ruleset_fd,1,ctypes.byref(rule),0) < 0:
        raise OSError(ctypes.get_errno(),'landlock_add_rule')
    os.close(directory_fd)
if libc.prctl(38,1,0,0,0) < 0:
    raise OSError(ctypes.get_errno(),'PR_SET_NO_NEW_PRIVS')
if libc.syscall(446,ruleset_fd,0) < 0:
    raise OSError(ctypes.get_errno(),'landlock_restrict_self')
os.close(ruleset_fd)
runtime = {'python_executable':sys.executable,'python_realpath':str(Path(sys.executable).resolve()),'python_version':sys.version,'cwd':os.getcwd(),'landlock_abi':abi,'write_roots':[str(run),'/dev/shm'],'private_shm_backing':str(run/'runtime/shm'),'alias_backing_verified_before_rule':True,'namespace_ids':{name:os.readlink('/proc/self/ns/'+name) for name in ('user','mnt','pid')}}
(run/'logs/python_runtime.json').write_text(json.dumps(runtime,ensure_ascii=False,indent=2)+'\n')

tick = time.monotonic()
started = datetime.datetime.now(datetime.timezone.utc).isoformat()
probe_exit = 0
with (run/'logs/semlock_probe.log').open('x') as log:
    try:
        import multiprocessing as mp
        lock = mp.Lock()
        lock.acquire()
        lock.release()
        log.write('multiprocessing.Lock acquire/release: SUCCESS\n')
    except Exception:
        traceback.print_exc(file=log)
        probe_exit = 1
(run/'logs/semlock_probe.exit_code').write_text(str(probe_exit)+'\n')
(run/'logs/semlock_probe.timing.json').write_text(json.dumps({'started_at':started,'finished_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-tick,'exit_code':probe_exit},indent=2)+'\n')
if probe_exit:
    raise SystemExit(probe_exit)

argv = [sys.executable,'longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/D/u2_f_caegraph_definition.py','--output-dir',str(run/'output/u2_f_caegraph')]
started = datetime.datetime.now(datetime.timezone.utc).isoformat()
tick = time.monotonic()
with (run/'logs/w2_run.started.json').open('x') as stream:
    json.dump({'started_at':started,'argv':argv,'cwd':str(source),'business_attempt':1},stream,indent=2)
with (run/'logs/w2_run.log').open('xb') as log:
    result = subprocess.run(argv,cwd=source,stdout=log,stderr=subprocess.STDOUT)
(run/'logs/w2_run.exit_code').write_text(str(result.returncode)+'\n')
(run/'logs/w2_run.finished.json').write_text(json.dumps({'finished_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-tick,'exit_code':result.returncode},indent=2)+'\n')
raise SystemExit(result.returncode)
