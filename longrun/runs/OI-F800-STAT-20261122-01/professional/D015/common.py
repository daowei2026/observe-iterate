"""D015原G补充：只读锁定来源与当前D008结果，写本D分析。"""
import json,hashlib,subprocess
from pathlib import Path
from datetime import datetime,timezone
BASE=Path('/dwdhome/fy/BASE_E6_2_copy')
RUN='OI-F800-STAT-20261122-01'
ROOT=BASE/'artifacts'/RUN/'D015'
PACKET=Path('/dwdhome/fy/cgpterm/artifacts/wall-f-closure-20261122')/RUN/'C0034-dispatch-packet.json'
RECORD=PACKET.parent/'executor-records'
PREFIX='longrun/runs/'+RUN
LOCKED='b8c2b513f0b08be6a1fa6782b71bf74a07faff0d'
U='d4f9fefaa67f9f22f540fa35a7da79cbbdf831ca'
INITIAL='0d6d288fc0be2f1c7c67f182ab4be96eddc43fc1'
D008=BASE/'artifacts'/RUN/'D008'
def now():return datetime.now(timezone.utc).isoformat()
def sha(raw):return hashlib.sha256(raw).hexdigest()
def git_bytes(commit,path):return subprocess.check_output(['git','show',commit+':'+path],cwd=RECORD)
def read_json(commit,path):return json.loads(git_bytes(commit,path))
def ref(commit,path):return 'daowei2026/observe-iterate@'+commit+':'+path
def pro_ref(name):return ref(U,PREFIX+'/professional/D008/'+name)
def save(name,obj):
    p=ROOT/name;p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(obj,ensure_ascii=False,indent=2,allow_nan=False)+'\n');return p
