"""验收后仅复制本D原件至授权Run记录子树，先专业发布后Return。"""
from pathlib import Path
from hashlib import sha256
from datetime import datetime,timezone
import json,shutil,subprocess
ROOT=Path(__file__).resolve().parent
RECORD=Path('/dwdhome/fy/cgpterm/artifacts/wall-f-closure-20261122/OI-F800-STAT-20261122-01/executor-records')
RUN='OI-F800-STAT-20261122-01';REL=Path('longrun/runs')/RUN/'professional/D009';TARGET=RECORD/REL
assert json.loads((ROOT/'VALIDATION.json').read_text())['completed']
assert json.loads((ROOT/'ObservationPositionPreparationResult.json').read_text())['阶段状态']=='完整'
def git(*a):return subprocess.check_output(['git',*a],cwd=RECORD,text=True).strip()
assert git('branch','--show-current')=='codex/oi-f800-stat-20261122-01'
assert git('rev-parse','HEAD')=='073edebe66bdc1592fdb62e47ca34c1258447403'
assert not git('status','--porcelain') and not TARGET.exists()
exclude={'status-last.json','task-plan.json','SESSION_STATE.json','FINAL_DELIVERY.json','PROFESSIONAL_MANIFEST.json','PROFESSIONAL_PUBLICATION_READBACK.json','RETURN_PUBLICATION_READBACK.json'}
files=[]
def copy(p):
 rel=p.relative_to(ROOT);target=TARGET/rel;target.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,target)
 files.append(dict(name=str(rel),local_path=str(p),record_path=str(REL/rel),bytes=p.stat().st_size,sha256=sha256(p.read_bytes()).hexdigest()))
for p in sorted(ROOT.iterdir()):
 if p.is_file() and p.name not in exclude and p.suffix in ('.json','.md','.py','.log'):copy(p)
manifest=dict(run_id=RUN,call_id='C0021',delegation_id='D009',prepared_at=datetime.now(timezone.utc).isoformat(),
 scope='当前39f实例的M-B观察位置准备：原任务明确rb/hc/i三年普通位置、SOF/当前U引用、四问题和七候选来源保留及坐标对齐；只完成B。',files=files,
 local_only=['__pycache__','task-plan/status-last/SESSION_STATE','task-status live ledgers'],
 upstream_artifacts='引用已发布D008 exact对象，不复制或更改原Feature、G、候选或共享理解。',
 current_validation='VALIDATION.json',execution_instruction='归档脚本供审阅，执行位置仅限原Owner授权BASE；不得在记录checkout直接运行生产或分析。')
(TARGET/'PROFESSIONAL_MANIFEST.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
(ROOT/'PROFESSIONAL_MANIFEST.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(target=str(TARGET),files=len(files)+1,bytes=sum(x['bytes'] for x in files)),ensure_ascii=False))
