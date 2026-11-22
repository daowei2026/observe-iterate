"""D004 隔离输出、FRP/trade缓存；不启动正式Feature，不覆盖D002结果/源/二进制。
未变依赖沿既有构建源；其构建缓存写入同样受实际资源锁保护。
"""
from pathlib import Path
from datetime import datetime, timezone
import fcntl
import hashlib
import json
import os
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parent
BASE = Path('/dwdhome/fy/BASE_E6_2_copy')
OLD = BASE / '.runtime/f-wide-observation-20261122/runtime'
NEW = BASE / '.runtime/f800-exact-uti-20261122/runtime'
FRP = BASE / '.runtime/f-observation-multiple-github-20261122/frp'
LOCK = Path('/dwdhome/fy/cgpterm/artifacts/wall-f-closure-20261122/FORMAL_PRODUCTION.lock')
STATUS = ROOT / 'BUILD_STATUS.json'
def stamp(): return datetime.now(timezone.utc).isoformat()
def sha(p):
    h = hashlib.sha256()
    with p.open('rb') as f:
        for chunk in iter(lambda: f.read(1024*1024), b''): h.update(chunk)
    return h.hexdigest()
def write(): STATUS.write_text(json.dumps(state, ensure_ascii=False, indent=2)+'\n')
state = {'run_id':'OI-F800-STAT-20261122-01', 'delegation_id':'D004', 'pid':os.getpid(),
         'started_at':stamp(), 'formal_feature_run':False, 'runtime':str(NEW), 'completed':False}
resume = sys.argv[1:] == ['--resume']
assert not sys.argv[1:] or resume
if resume:
    prior=json.loads(STATUS.read_text())
    assert prior['phase']=='compiling' and not prior['completed']
    assert not Path('/proc').joinpath(str(prior['build_pid'])).exists(), 'previous build still running'
    (ROOT/'BUILD_ATTEMPT1_MONITOR_FAILURE.json').write_text(json.dumps({
        'prior_status':prior,'monitor_exit_code':1,'build_exit_code':None,
        'cause':'ps returned 1 with no child rows; observer treated it as an exception',
        'previous_build_not_running_at_resume':True,'formal_feature_run':False},ensure_ascii=False,indent=2)+'\n')
    (ROOT/'build-attempt1.log').write_bytes((ROOT/'build.log').read_bytes())
    state['attempt']=2
state['baseline_binary_sha256'] = {name:sha(OLD/'edh-universe/bin'/name)
    for name in ['ts','dbaw','u2-observation-window-check']}
source = Path('src/Frp/Instance/ISL/Opportunity/U2/GroupCandidateKLineInput.hs')
state['baseline_source_sha256'] = sha(OLD/'edh-universe/frp/frp'/source)
write()
with LOCK.open('a+') as lock:
    while True:
        try:
            fcntl.flock(lock, fcntl.LOCK_EX|fcntl.LOCK_NB)
            break
        except BlockingIOError:
            state['phase']='waiting_resource_lock'; write(); time.sleep(10)
    state.update(lock_acquired_at=stamp(), lock_path=str(LOCK), lock_owner_pid=os.getpid(), phase='isolated_runtime_copy')
    write()
    oldedh=OLD/'edh-universe'; edh=NEW/'edh-universe'
    if resume:
        assert (edh/'frp/frp').resolve()==FRP and (edh/'stack.yaml').is_file()
        assert str(edh/'bin') in (edh/'stack.yaml').read_text()
    else:
        assert not NEW.exists(), 'Do not overwrite an existing runtime'
        NEW.mkdir(parents=True); edh.mkdir()
        for path in OLD.iterdir():
            if path.name != 'edh-universe': (NEW/path.name).symlink_to(path, target_is_directory=path.is_dir())
        for path in oldedh.iterdir():
            if path.name not in ['.stack-work','stack.yaml','stack.yaml.lock','bin','frp']:
                (edh/path.name).symlink_to(path, target_is_directory=path.is_dir())
        (edh/'bin').mkdir(); (edh/'frp').mkdir()
        for path in (oldedh/'frp').iterdir():
            if path.name=='frp': (edh/'frp/frp').symlink_to(FRP, target_is_directory=True)
            elif path.name=='trade-poc':
                subprocess.run(['cp','-a','--reflink=auto',str(path.resolve()),str(edh/'frp/trade-poc')], check=True)
            else: (edh/'frp'/path.name).symlink_to(path, target_is_directory=path.is_dir())
        for src,dst in [(oldedh/'.stack-work',edh/'.stack-work'),
                        (oldedh/'frp/frp/.stack-work',FRP/'.stack-work')]:
            assert not dst.exists()
            subprocess.run(['cp','-a','--reflink=auto',str(src),str(dst)], check=True)
        (edh/'stack.yaml.lock').write_bytes((oldedh/'stack.yaml.lock').read_bytes())
        text=(oldedh/'stack.yaml').read_text().replace(str(oldedh/'bin'),str(edh/'bin'))
        (edh/'stack.yaml').write_text(text)
    command=['stack','--stack-yaml',str(edh/'stack.yaml'),'build',
        'frp:exe:dbaw','frp:exe:u2-observation-window-check','trade-poc:exe:ts',
        '--copy-bins','--ghc-options=-O0','--ghc-options=-j2','--jobs=2']
    state.update(phase='compiling', command=command, build_started_at=stamp()); write()
    with (ROOT/'build.log').open('w') as log:
        process=subprocess.Popen(command,cwd=edh,stdout=log,stderr=subprocess.STDOUT)
        state['build_pid']=process.pid; write()
        while process.poll() is None:
            state['heartbeat_at']=stamp()
            observation=subprocess.run(['ps','-o','pid,ppid,args','--ppid',str(process.pid)],text=True,capture_output=True)
            state['build_children']=observation.stdout.splitlines()
            state['child_observation_exit_code']=observation.returncode
            write(); time.sleep(10)
        code=process.returncode
    after={name:sha(OLD/'edh-universe/bin'/name) for name in state['baseline_binary_sha256']}
    state.update(exit_code=code, build_finished_at=stamp(),
        baseline_binaries_unchanged=after==state['baseline_binary_sha256'],
        baseline_source_unchanged=sha(OLD/'edh-universe/frp/frp'/source)==state['baseline_source_sha256'])
    assert state['baseline_binaries_unchanged'] and state['baseline_source_unchanged']
    if code==0:
        state['binaries']={name:{'path':str(edh/'bin'/name),'sha256':sha(edh/'bin'/name)}
            for name in state['baseline_binary_sha256']}
    state.update(completed=code==0, phase='completed' if code==0 else 'failed',lock_released_at=stamp())
    write(); fcntl.flock(lock,fcntl.LOCK_UN)
print(json.dumps(state,ensure_ascii=False,indent=2))
raise SystemExit(state['exit_code'])
