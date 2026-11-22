"""持controller指定flock运行本Run生产，记录实际子进程与锁证据。"""
from pathlib import Path
from datetime import datetime, timezone
import fcntl
import json
import os
import signal
import subprocess
import sys
import time

BASE = Path('/dwdhome/fy/BASE_E6_2_copy')
ROOT = Path(__file__).resolve().parent
LOCK = Path('/dwdhome/fy/cgpterm/artifacts/wall-f-closure-20261122/FORMAL_PRODUCTION.lock')
RUN = 'OI-F800-STAT-20261122-01'
CLI = '/home/dw/.agents/skills/long-task-status/scripts/task_status.py'
TASK = 'oi-f800-stat-20261122-01-d002-e1'


def now():
    return datetime.now(timezone.utc).isoformat()


def write(name, value):
    (ROOT / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')


def status(*args):
    result = subprocess.run(['python', CLI, *args, '--root', str(BASE), '--task-id', TASK], capture_output=True, text=True)
    if result.returncode:
        print('STATUS_ERROR ' + result.stderr, flush=True)


def processes():
    result = {}
    for path in Path('/proc').iterdir():
        if not path.name.isdigit():
            continue
        try:
            if path.stat().st_uid != os.getuid():
                continue
            raw = (path / 'stat').read_text()
            parent = int(raw[raw.rfind(')') + 2:].split()[1])
            result[int(path.name)] = parent
        except (OSError, ValueError):
            continue
    return result


def details(pid):
    path = Path('/proc') / str(pid)
    try:
        exe = os.readlink(path / 'exe')
        cwd = os.readlink(path / 'cwd')
        command = (path / 'cmdline').read_bytes().replace(b'\0', b' ').decode(errors='replace')
        return dict(pid=pid, executable=exe, cwd=cwd, command=command, observed_at=now())
    except OSError:
        return None


def store_writers():
    writers, denied = [], []
    for pid in processes():
        path = Path('/proc') / str(pid)
        try:
            for fd in (path / 'fd').iterdir():
                try:
                    target = os.readlink(fd)
                    if not target.startswith(str(ROOT / 'store') + '/'):
                        continue
                    info = (path / 'fdinfo' / fd.name).read_text()
                    flags = int(next(line.split()[1] for line in info.splitlines() if line.startswith('flags:')), 8)
                    if flags & 3:
                        writers.append(dict(pid=pid, path=target))
                except (OSError, StopIteration):
                    continue
        except OSError:
            denied.append(pid)
    return dict(checked_at=now(), writers=writers, inaccessible_processes=denied,
                scope='本Run新建独立store的同UID可见写fd；与真实flock、独立路径及配置证据共同使用')


def main():
    preflight = json.loads((ROOT / 'preflight/report.json').read_text())
    assert preflight['completed'] and not preflight['fields_existed_before']
    expected = preflight['engine_executable']
    result = dict(run_id=RUN, call_id='C0005', delegation_id='D002', supervisor_pid=os.getpid(),
                  lock_path=str(LOCK), requested_at=now(), completed=False, children=[], native_process_observed=False)
    with LOCK.open('a+') as lock:
        while True:
            try:
                fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
                break
            except BlockingIOError:
                status('update', '--status', 'waiting_external', '--action', '等待另一Run释放共享正式生产锁', '--next-action', '获锁后生产F800')
                result['waiting_at'] = now()
                write('PRODUCTION_PROCESS.json', result)
                print('WAITING_FORMAL_LOCK ' + now(), flush=True)
                time.sleep(30)
        result['lock_acquired_at'] = now()
        result['lock_inode'] = os.fstat(lock.fileno()).st_ino
        locks = Path('/proc/locks').read_text()
        result['kernel_lock_lines'] = [line for line in locks.splitlines() if str(os.getpid()) in line.split()]
        probe = subprocess.run([sys.executable, '-c',
            'import fcntl,sys; f=open(sys.argv[1],"r+");\ntry: fcntl.flock(f,fcntl.LOCK_EX|fcntl.LOCK_NB)\nexcept BlockingIOError: sys.exit(73)\nsys.exit(0)', str(LOCK)])
        assert probe.returncode == 73, '独立进程未能证明flock排他'
        result['independent_lock_probe_exit'] = probe.returncode
        audit = store_writers()
        write('STORE_WRITER_AUDIT.json', audit)
        assert not audit['writers'], audit['writers']
        assert not (Path(preflight['full_dir']) / 'fields.json').exists()
        status('update', '--status', 'running', '--clear-blocker', '--action', '已核独立写面并取得共享正式生产锁', '--next-action', '运行准确F800三年实例')
        status('step-complete', '--step-id', 'preflight', '--evidence', str(ROOT / 'preflight/report.json'))
        status('step-start', '--step-id', 'production', '--action', '持共享锁正式生产rb/hc/i三年F800', '--next-action', '完成原生生产后独立进程读回31表')
        env = os.environ.copy()
        env['PYTHONDONTWRITEBYTECODE'] = '1'
        env['OI_FORMAL_LOCK_HELD'] = RUN
        command = ['bash', 'run-python.sh', '.runtime/f-wide-observation-20261122/run_in_runtime.py',
                   str(ROOT / 'run_formal.py'), '--mode', 'produce']
        with (ROOT / 'produce.log').open('w') as logfile:
            child = subprocess.Popen(command, cwd=BASE, env=env, stdout=logfile, stderr=subprocess.STDOUT,
                                     start_new_session=True)
            result.update(python_pid=child.pid, child_started_at=now(), command=command)
            write('PRODUCTION_PROCESS.json', result)
            print('FORMAL_PRODUCTION_WRAPPER_PID ' + str(child.pid), flush=True)
            observed = set()
            last_heartbeat = time.monotonic()
            while child.poll() is None:
                mapping = processes()
                descendants = {child.pid}
                while True:
                    expanded = descendants | {pid for pid, parent in mapping.items() if parent in descendants}
                    if expanded == descendants:
                        break
                    descendants = expanded
                for pid in descendants - observed:
                    record = details(pid)
                    if record is None:
                        continue
                    observed.add(pid)
                    result['children'].append(record)
                    if Path(record['executable']).name == 'ts':
                        if Path(record['executable']).resolve() != Path(expected).resolve():
                            os.killpg(child.pid, signal.SIGTERM)
                            raise RuntimeError('实际加载了非锁定runtime的ts，已停止本次进程组')
                        result['native_process_observed'] = True
                        result['native_pid'] = pid
                        print('NATIVE_TS_PID ' + str(pid), flush=True)
                    write('PRODUCTION_PROCESS.json', result)
                if time.monotonic() - last_heartbeat >= 60:
                    status('heartbeat', '--action', '共享锁内F800正式进程运行，日志持续保存', '--next-action', '生产结束后独立读回')
                    last_heartbeat = time.monotonic()
                    print('PRODUCTION_ALIVE ' + now(), flush=True)
                time.sleep(0.25)
            result['exit_code'] = child.returncode
            result['process_finished_at'] = now()
        assert child.returncode == 0, '正式运行失败，见produce.log'
        assert result['native_process_observed'], '没有实际ts进程证据，禁止宣称正式加载验收'
        produced = json.loads((ROOT / 'produced/report.json').read_text())
        assert produced['completed'] and produced['producer_executed'] and produced['public_read_completed']
        result['completed'] = True
        result['lock_release_at'] = now()
        write('PRODUCTION_PROCESS.json', result)
        fcntl.flock(lock, fcntl.LOCK_UN)
        status('step-complete', '--step-id', 'production', '--evidence', str(ROOT / 'PRODUCTION_PROCESS.json'))
        status('step-start', '--step-id', 'readback', '--action', '正式F800生产已完成，准备独立进程31表读回', '--next-action', '形成FeatureRunResultBinding后执行G')
        print('PRODUCTION_COMPLETED_AND_LOCK_RELEASED ' + now(), flush=True)


if __name__ == '__main__':
    main()
