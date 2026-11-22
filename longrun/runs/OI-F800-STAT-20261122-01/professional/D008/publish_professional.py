"""验收后仅复制本D原件至授权Run记录子树，先专业发布后Return。"""
from pathlib import Path
from hashlib import sha256
from datetime import datetime,timezone
import json,shutil,subprocess
ROOT=Path(__file__).resolve().parent
RECORD=Path('/dwdhome/fy/cgpterm/artifacts/wall-f-closure-20261122/OI-F800-STAT-20261122-01/executor-records')
RUN='OI-F800-STAT-20261122-01';REL=Path('longrun/runs')/RUN/'professional/D008';TARGET=RECORD/REL
assert json.loads((ROOT/'VALIDATION.json').read_text())['completed']
assert json.loads((ROOT/'ANALYSIS_EXECUTION.json').read_text())['completed']
def git(*a):return subprocess.check_output(['git',*a],cwd=RECORD,text=True).strip()
assert git('branch','--show-current')=='codex/oi-f800-stat-20261122-01'
assert git('rev-parse','HEAD')=='6d7e96322ac942116d0a474de05f7eef839454ef'
assert not git('status','--porcelain') and not TARGET.exists()
exclude={'status-last.json','task-plan.json','SESSION_STATE.json','FINAL_DELIVERY.json','PROFESSIONAL_MANIFEST.json','PROFESSIONAL_PUBLICATION_READBACK.json','RETURN_PUBLICATION_READBACK.json'}
files=[]
def copy(p):
 rel=p.relative_to(ROOT);target=TARGET/rel;target.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,target)
 files.append(dict(name=str(rel),local_path=str(p),record_path=str(REL/rel),bytes=p.stat().st_size,sha256=sha256(p.read_bytes()).hexdigest()))
for p in sorted(ROOT.iterdir()):
 if p.is_file() and p.name not in exclude and p.suffix in ('.json','.md','.py','.log'):copy(p)
for folder in ['preflight','produced','readback','profile','comparison','comparison_ac','attempts']:
 for p in sorted((ROOT/folder).rglob('*')):
  if p.is_file() and p.suffix in ('.json','.csv','.log'):copy(p)
for name in ['mquant/config/prod/sof/TA_updto20240229_DBA.json','mquant/config/prod/store_dir.json']:
 copy(ROOT/'platform-app'/name)
manifest=dict(run_id=RUN,call_id='C0019',delegation_id='D008',prepared_at=datetime.now(timezone.utc).isoformat(),
 scope='39f完整正式F-only三年X、31表独立OnlyRead、G1-G8、双历史基线比较及38个原位置AsOf复验；不代manager释放。',files=files,
 local_only=['store/**原生dba及全部上游缓存','upstream/**完整15源输入CSV','平台任务/日志缓存','__pycache__','task-status live ledgers'],
 local_only_evidence=['NATIVE_OUTPUT_MANIFEST.json','UPSTREAM_EXTRACTION.json'],
 current_validation='VALIDATION.json',execution_instruction='归档脚本供审阅，执行位置仅限原Owner授权BASE；不得在记录checkout直接运行生产或分析。')
(TARGET/'PROFESSIONAL_MANIFEST.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
(ROOT/'PROFESSIONAL_MANIFEST.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(target=str(TARGET),files=len(files)+1,bytes=sum(x['bytes'] for x in files)),ensure_ascii=False))
