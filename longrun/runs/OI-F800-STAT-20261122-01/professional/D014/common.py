"""S2只读准确输入和本D产物的辅助函数；不调用Feature/CAEGraph构造。"""
import gzip
import hashlib
import json
import subprocess
from pathlib import Path
from datetime import datetime, timezone

BASE = Path('/dwdhome/fy/BASE_E6_2_copy')
RUN = 'OI-F800-STAT-20261122-01'
ROOT = BASE / 'artifacts' / RUN / 'D014'
RECORD = Path('/dwdhome/fy/cgpterm/artifacts/wall-f-closure-20261122') / RUN / 'executor-records'
PREFIX = f'longrun/runs/{RUN}'
LOCKED = '87b951bbd15078a2d6353bdd24afe0d8f19c845c'
MATERIAL = 'dfbc647030890fc8af80ac04a4d12a734d99f6dc'
U = 'd4f9fefaa67f9f22f540fa35a7da79cbbdf831ca'

def now():
    return datetime.now(timezone.utc).isoformat()

def git_bytes(commit, path):
    return subprocess.check_output(['git', 'show', f'{commit}:{path}'], cwd=RECORD)

def read_json(commit, path):
    return json.loads(git_bytes(commit, path))

def ref(commit, path):
    return f'daowei2026/observe-iterate@{commit}:{path}'

def pro_ref(d, name, commit=MATERIAL):
    return ref(commit, f'{PREFIX}/professional/{d}/{name}')

def save(name, obj):
    p = ROOT / name
    p.parent.mkdir(exist_ok=True, parents=True)
    p.write_text(json.dumps(obj, ensure_ascii=False, indent=2, allow_nan=False) + '\n')
    return p

def sha(raw):
    return hashlib.sha256(raw).hexdigest()

def formal_all():
    mapping = read_json(MATERIAL, f'{PREFIX}/professional/D012/FORMAL_GRAPH_DATA.json')
    result = {}
    for m in mapping['formal_files']:
        path = f"{PREFIX}/professional/D012/{m['file']}"
        raw = git_bytes(MATERIAL, path)
        assert sha(raw) == m['gzip_sha256'], path
        unzipped = gzip.decompress(raw)
        assert sha(unzipped) == m['json_sha256'], path
        result[m['source_id']] = json.loads(unzipped)
    return mapping, result

FROZEN = '266c34e5d7d75a05677e7969d528090d37cac44e'
