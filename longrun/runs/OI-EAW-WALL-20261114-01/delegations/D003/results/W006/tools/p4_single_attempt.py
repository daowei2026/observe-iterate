from pathlib import Path
import ast, errno, fcntl, json, os, sys
sys.path.insert(0,str(Path(__file__).resolve().parent))
from common import ROOT,binding,fact,guard,save,utc
from runtime import run
guard()
required={'HISTORICAL_FIOCLEX_PHASE_CLASSIFICATION.json':'PASS','FIOCLEX_LOCAL_CONSTANT_VERIFICATION.json':'PASS','SECCOMP_DATA_LAYOUT_VERIFICATION.json':'PASS','PARENT_RUNTIME_BINDING_DELTA.json':'PASS_STATIC_BINDING','SECCOMP_IOCTL_FILTER_DELTA.json':'PASS_GENERATION_ONLY_PENDING_P3','SECCOMP_FILTER_STATIC_EVALUATION.json':'PASS'}
for name,status in required.items():assert json.loads((ROOT/'artifacts'/name).read_bytes())['status']==status
static=json.loads((ROOT/'artifacts/SECCOMP_FILTER_STATIC_EVALUATION.json').read_bytes())
assert static['candidate_launcher']==fact(ROOT/'tools/landlock_launcher.py')
for name in ['runtime.py','common.py','landlock_launcher.py','confinement_probe.py']:ast.parse((ROOT/'tools'/name).read_text())
b=binding();lock=b['fresh_lock'];negative_checks=[]
for label,path in b['negative_targets'].items():
    try:os.lstat(path)
    except FileNotFoundError as e:assert e.errno==2;negative_checks.append({'label':label,'path':path,'absent':True,'errno':2,'readonly':True})
    else:raise RuntimeError('STOP negative target now exists')
tool_facts=[fact('/usr/bin/python3.12'),fact('/usr/bin/strace')]
assert tool_facts[0]['sha256']=='c2c20b4745d447551221ec3d4e70f92c270c4609fe3df34fc52ea6dd46e92273'
assert tool_facts[1]['sha256']=='28f957c227012de0b18d1bd7fff2d396cb693ea60ed8013be68de071e84b5001'
fd=os.open(lock['path'],os.O_RDWR|os.O_NOFOLLOW)
try:
    assert os.fstat(fd).st_ino==lock['inode']
    try:fcntl.flock(fd,fcntl.LOCK_EX|fcntl.LOCK_NB)
    except BlockingIOError as e:assert e.errno in [errno.EAGAIN,errno.EACCES]
    else:raise RuntimeError('STOP unexpected lock acquisition')
    argv=['/usr/bin/strace','--kill-on-exit','-ff','-yy','-ttt','-s','128','-e','trace=all','-e','raw=read,pread64,readv,preadv,preadv2,recvfrom,recvmsg,recvmmsg','-o',str(ROOT/'trace/r0a1'),'/usr/bin/python3.12','-I','-S','-B',str(ROOT/'tools/landlock_launcher.py'),'--root',str(ROOT),'--report',str(ROOT/'receipts/r0a1-launcher.json'),'--blocked-inherited-fd',str(fd),'--task-tmp',str(ROOT/'tmp'),'--task-cache',str(ROOT/'cache'),'--task-config',str(ROOT/'config'),'--','/usr/bin/python3.12','-I','-S','-B',str(ROOT/'tools/confinement_probe.py'),'--root',str(ROOT),'--blocked-inherited-fd',str(fd)]
    save('receipts/R0_A1_ATTEMPT.json',{'at':utc(),'attempt':1,'only_attempt_marker':True,'P0_P3_all_PASS':True,'argv':argv,'tool_facts':tool_facts,'launcher':fact(ROOT/'tools/landlock_launcher.py'),'runtime':fact(ROOT/'tools/runtime.py'),'probe':fact(ROOT/'tools/confinement_probe.py'),'negative_readonly_prechecks':negative_checks,'independent_writable_lock_fd':fd,'holder_lock_untouched':True,'read_payloads_raw_to_avoid_exporting_private_contents':True})
    result=run('r0a1',argv,limit=45,pass_fds=(fd,))
finally:os.close(fd)
save('artifacts/R0_A1_EXECUTION_RECEIPT.json',{'phase':'P4','status':'COMMAND_COMPLETED_PENDING_TRACE_REVIEW' if result['exit_code']==0 else 'KERNEL_OR_PROBE_FAILED_STOP','attempts':1,'result':result,'automatic_retry':False,'policy_adjustment_after_attempt':False})
print(json.dumps({'phase':'P4','attempts':1,'child_exit_code':result['exit_code'],'elapsed_seconds':result['elapsed_seconds'],'stdout':result['stdout'],'stderr':result['stderr']},ensure_ascii=False))
print(Path(result['stdout']['path']).read_text());print(Path(result['stderr']['path']).read_text())
raise SystemExit(0 if result['exit_code']==0 else 1)
