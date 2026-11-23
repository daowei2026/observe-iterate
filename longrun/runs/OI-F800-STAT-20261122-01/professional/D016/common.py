"""D016只读正式D008结果及锁定源码，写本D诊断和授权Run记录。"""
import json, hashlib, subprocess, csv, uuid
from pathlib import Path
from datetime import datetime, timezone
BASE=Path('/dwdhome/fy/BASE_E6_2_copy')
RUN='OI-F800-STAT-20261122-01'
ROOT=BASE/'artifacts'/RUN/'D016'
PACKET=Path('/dwdhome/fy/cgpterm/artifacts/wall-f-closure-20261122')/RUN/'C0036-dispatch-packet.json'
RECORD=PACKET.parent/'executor-records'
PREFIX='longrun/runs/'+RUN
LOCKED='b8c2b513f0b08be6a1fa6782b71bf74a07faff0d'
U='d4f9fefaa67f9f22f540fa35a7da79cbbdf831ca'
G='6e9521ffc437a307da7413727f80fc2621994d4f'
INITIAL='48d6f7813670fdbdc3576410683f7ed3473c079d'
D008=ROOT.parent/'D008'
D015=ROOT.parent/'D015'
FRP='39f02ec4548e68ba8dbd30061afc870546000994'
def now():return datetime.now(timezone.utc).isoformat()
def sha(raw):return hashlib.sha256(raw).hexdigest()
def git_bytes(commit,path):return subprocess.check_output(['git','show',commit+':'+path],cwd=RECORD)
def ref(commit,path):return 'daowei2026/observe-iterate@'+commit+':'+path
def pro_ref(name,stage='D008'):return ref(U if stage=='D008' else G,PREFIX+'/professional/'+stage+'/'+name)
def save(name,obj):
 p=ROOT/name;p.parent.mkdir(parents=True,exist_ok=True)
 p.write_text(json.dumps(obj,ensure_ascii=False,indent=2,allow_nan=False)+'\n');return p
def rows(name):return list(csv.DictReader((D008/name).open(encoding='utf-8-sig',newline='')))
def uid(r,p):
 if int(r[p+'idForm'])==1:return str(uuid.UUID(int=(int(r[p+'idHigh'])<<64)|int(r[p+'idLow'])))
 return r[p+'idText']
def parent(r):return (r['timestamp'],int(r['occurrence']),int(r['record_id']),int(r['child_id_2']))
