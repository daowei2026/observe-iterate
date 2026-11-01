"""记录本单准确 argv、cwd、环境白名单、开始/结束、退出码和输出。"""
import argparse
import hashlib
import json
import os
import platform
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

OUT = Path(__file__).resolve().parents[1]


def main():
    p = argparse.ArgumentParser()
    p.add_argument('label')
    p.add_argument('command', nargs=argparse.REMAINDER)
    a = p.parse_args()
    assert a.label.replace('-', '').replace('_', '').isalnum()
    assert a.command and a.command[0] == sys.executable
    assert not (OUT / f'logs/{a.label}.json').exists(), '不覆盖已有真实调用回执'
    env = {'PATH': os.environ['PATH'], 'LANG': 'C.UTF-8', 'LC_ALL': 'C.UTF-8',
           'TZ': 'Asia/Shanghai', 'PYTHONDONTWRITEBYTECODE': '1'}
    receipt = {'command': a.command, 'cwd': str(Path.cwd()), 'environment': env,
               'python': platform.python_version(), 'python_executable': sys.executable,
               'started_at': datetime.now(timezone.utc).isoformat(),
               'stdout': f'logs/{a.label}.stdout', 'stderr': f'logs/{a.label}.stderr'}
    start = time.monotonic()
    with (OUT / receipt['stdout']).open('xb') as stdout, (OUT / receipt['stderr']).open('xb') as stderr:
        completed = subprocess.run(a.command, env=env, stdin=subprocess.DEVNULL,
                                   stdout=stdout, stderr=stderr, timeout=120)
    receipt.update(returncode=completed.returncode,
                   finished_at=datetime.now(timezone.utc).isoformat(),
                   elapsed_seconds=time.monotonic() - start)
    for field in ['stdout', 'stderr']:
        data = (OUT / receipt[field]).read_bytes()
        receipt[field + '_bytes'] = len(data)
        receipt[field + '_sha256'] = hashlib.sha256(data).hexdigest()
    (OUT / f'logs/{a.label}.json').write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps(receipt, ensure_ascii=False))
    sys.exit(completed.returncode)


if __name__ == '__main__':
    main()
