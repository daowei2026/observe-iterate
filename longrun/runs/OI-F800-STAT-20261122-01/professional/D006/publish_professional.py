"""仅准备授权Run记录子树；不执行Feature或更改源代码。"""
from pathlib import Path
from hashlib import sha256
from datetime import datetime,timezone
import json,shutil,subprocess

ROOT=Path(__file__).resolve().parent
RECORD=Path('/dwdhome/fy/cgpterm/artifacts/wall-f-closure-20261122/OI-F800-STAT-20261122-01/executor-records')
RUN='OI-F800-STAT-20261122-01'
REL=Path('longrun/runs')/RUN/'professional/D006'
TARGET=RECORD/REL
def git(*a):return subprocess.check_output(['git',*a],cwd=RECORD,text=True).strip()
assert git('branch','--show-current')=='codex/oi-f800-stat-20261122-01'
assert git('rev-parse','HEAD')=='a791240c2bbf428f79bb86fe01f7ca025fd4a14b'
assert not git('status','--porcelain') and not TARGET.exists()
assert json.loads((ROOT/'VALIDATION.json').read_text())['completed']
exclude={'status-last.json','task-plan.json','native-package-binding.attempt1.txt'}
files=[]
TARGET.mkdir(parents=True)
for p in sorted(ROOT.iterdir()):
    if not p.is_file() or p.name in exclude:continue
    shutil.copy2(p,TARGET/p.name)
    files.append(dict(name=p.name,local_path=str(p),record_path=str(REL/p.name),bytes=p.stat().st_size,sha256=sha256(p.read_bytes()).hexdigest()))
manifest=dict(run_id=RUN,call_id='C0014',delegation_id='D006',prepared_at=datetime.now(timezone.utc).isoformat(),
    scope='D006 GF002单finding原生诊断/证据/未应用MP002；未启动正式Feature，无源提交/采用',files=files,
    omitted='仅本C操作状态和计划、空的失败命令stdout；失败原因和日志保留。平台配置复制件沿D005输入原件，不重复发布。',
    current_validation='VALIDATION.json',source_state='SOURCE_EVIDENCE.json')
(TARGET/'PROFESSIONAL_MANIFEST.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
(ROOT/'PROFESSIONAL_MANIFEST.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(target=str(TARGET),files=len(files)+1,bytes=sum(x['bytes'] for x in files)),ensure_ascii=False))
