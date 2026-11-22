"""仅准备授权Run记录子树；不执行Feature或更改源代码。"""
from pathlib import Path
from hashlib import sha256
from datetime import datetime,timezone
import json,shutil,subprocess

ROOT=Path(__file__).resolve().parent
RECORD=Path('/dwdhome/fy/cgpterm/artifacts/wall-f-closure-20261122/OI-F800-STAT-20261122-01/executor-records')
RUN='OI-F800-STAT-20261122-01'
REL=Path('longrun/runs')/RUN/'professional/D007'
TARGET=RECORD/REL
def git(*a):return subprocess.check_output(['git',*a],cwd=RECORD,text=True).strip()
assert git('branch','--show-current')=='codex/oi-f800-stat-20261122-01'
assert git('rev-parse','HEAD')=='6ff5ce2e5ad9cc92f887df46b677554de2fd4316'
assert not git('status','--porcelain') and not TARGET.exists()
assert json.loads((ROOT/'VALIDATION.json').read_text())['completed']
exclude={'status-last.json','task-plan.json','build.log','SESSION_STATE.json'}
files=[]
TARGET.mkdir(parents=True)
for p in sorted(ROOT.iterdir()):
    if not p.is_file() or p.name in exclude:continue
    shutil.copy2(p,TARGET/p.name)
    files.append(dict(name=p.name,local_path=str(p),record_path=str(REL/p.name),bytes=p.stat().st_size,sha256=sha256(p.read_bytes()).hexdigest()))
for p in sorted((ROOT/'adapter-fixture-app').rglob('*.json')):
    relative=p.relative_to(ROOT);target=TARGET/relative;target.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,target)
    files.append(dict(name=str(relative),local_path=str(p),record_path=str(REL/relative),bytes=p.stat().st_size,sha256=sha256(p.read_bytes()).hexdigest()))
manifest=dict(run_id=RUN,call_id='C0017',delegation_id='D007',prepared_at=datetime.now(timezone.utc).isoformat(),
    scope='D007 已批准MP002 FI实现/真实adapter回归/新FRP采用；无正式新F X/G或释放',files=files,
    omitted='仅本C操作状态/计划和已gzip归档的raw build.log；真实测试fixture配置随包保留，正式configuration.json不变。',
    current_validation='VALIDATION.json',source_state='CodeVersionAdoption.json')
(TARGET/'PROFESSIONAL_MANIFEST.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
(ROOT/'PROFESSIONAL_MANIFEST.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(target=str(TARGET),files=len(files)+1,bytes=sum(x['bytes'] for x in files)),ensure_ascii=False))
