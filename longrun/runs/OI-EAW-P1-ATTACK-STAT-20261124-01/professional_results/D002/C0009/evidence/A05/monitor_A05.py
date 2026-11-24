"""只观察本次进程与本地 journal，以 CLI 续写状态心跳。"""
import datetime
import json
from pathlib import Path
import subprocess
import time

base = Path(__file__).resolve().parent
attempt = base.parent / 'formal-attempt-A05'
pid = json.loads((attempt/'execution_progress.json').read_text())['runner_pid']
while True:
    current = json.loads((attempt / 'execution_progress.json').read_text())
    row = {'at': datetime.datetime.now(datetime.timezone.utc).isoformat(), 'pid': pid,
           'stage': current.get('current_stage'), 'symbol': current.get('symbol'),
           'feature': current.get('feature'), 'runner_result_exists': (attempt / 'execution_result.json').exists()}
    try:
        status = dict(line.split(':', 1) for line in Path(f'/proc/{pid}/status').read_text().splitlines() if ':' in line)
        row.update(process_state=status.get('State', '').strip(), rss=status.get('VmRSS', '').strip())
    except FileNotFoundError:
        row['process_state'] = 'PROCESS_ENDED'
    with (base / 'evidence/A05_process_observations.jsonl').open('a') as f:
        f.write(json.dumps(row, ensure_ascii=False) + '\n')
    print(json.dumps(row, ensure_ascii=False), flush=True)
    if row['runner_result_exists'] or row['process_state'] == 'PROCESS_ENDED':
        break
    action = f"C0009/A05 原锁内运行 {row['symbol'] or ''} {row['feature'] or ''}；实际进程仍在"
    subprocess.run(['python', '/home/dw/.agents/skills/long-task-status/scripts/task_status.py',
                    'update', '--root', '/dwdhome/fy/BASE_E6_2_copy/mquant/tis',
                    '--task-id', 'oi-eaw-p1-attack-d002-x-20261124', '--status', 'running',
                    '--clear-blocker', '--action', action, '--next-action',
                    '按真实运行、receipt及完整读回推进；未完成不标成功'], stdout=subprocess.DEVNULL, check=True)
    time.sleep(60)
