"""记录实际命令、退出码和进程归属；不使用 shell 拼接。"""
import argparse
import json
import os
import subprocess
import time
from support import OUT, BASE, now, lease

p = argparse.ArgumentParser()
p.add_argument('--id', required=True)
p.add_argument('--timeout', type=int, default=180)
p.add_argument('command', nargs=argparse.REMAINDER)
a = p.parse_args()
command = a.command[1:] if a.command[:1] == ['--'] else a.command
proof = lease()
(OUT / 'logs').mkdir(exist_ok=True)
log = OUT / 'logs' / (a.id + '.log')
record = dict(id=a.id, started_at_utc=now(), command=command, cwd=str(BASE),
              owner='codex:OI-EAW-WALL-20261116-01:worker:W1', lease=proof,
              stdout_stderr=str(log), timeout_seconds=a.timeout)
started = time.monotonic()
env = os.environ.copy()
env['PYTHONDONTWRITEBYTECODE'] = '1'
env['LONG_TASK_CONTROL_REGISTER_HELPER'] = ''
(OUT / 'tmp').mkdir(exist_ok=True)
env['TMPDIR'] = str(OUT / 'tmp')
record['temporary_directory'] = env['TMPDIR']
with log.open('w') as output:
    child = subprocess.Popen(command, cwd=str(BASE), env=env, stdout=output, stderr=subprocess.STDOUT, start_new_session=True)
    record['pid'] = child.pid
    try:
        record['exit_code'] = child.wait(timeout=a.timeout)
    except subprocess.TimeoutExpired:
        import signal
        os.killpg(child.pid, signal.SIGTERM)
        try:
            child.wait(timeout=5)
        except subprocess.TimeoutExpired:
            os.killpg(child.pid, signal.SIGKILL)
            child.wait()
        record.update(exit_code=child.returncode, timed_out=True)
record.update(ended_at_utc=now(), elapsed_seconds=round(time.monotonic()-started, 6), in_flight=False)
with (OUT / 'COMMANDS.jsonl').open('a') as f:
    f.write(json.dumps(record, ensure_ascii=False) + '\n')
print(json.dumps(record, ensure_ascii=False, indent=2))
preview = log.read_bytes()
if b'\x7fELF' in preview:
    preview = preview[:preview.index(b'\x7fELF')] + b'\n[ELF binary bytes omitted from preview]\n'
print(preview.decode('utf-8', errors='replace')[-18000:])
raise SystemExit(record['exit_code'] if record['exit_code'] >= 0 else 1)

