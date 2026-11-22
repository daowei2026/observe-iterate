"""仅发布本D验收原件至授权Run子树，先专业结果后Return。"""
from pathlib import Path
from hashlib import sha256
from datetime import datetime,timezone
import json
import shutil
import subprocess
R=Path(__file__).resolve().parent
RECORD=Path('/dwdhome/fy/cgpterm/artifacts/wall-f-closure-20261122/OI-F800-STAT-20261122-01/executor-records')
RUN='OI-F800-STAT-20261122-01';REL=Path('longrun/runs')/RUN/'professional/D010';target=RECORD/REL
def git(*a):return subprocess.check_output(['git',*a],cwd=RECORD,text=True).strip()
assert json.loads((R/'VALIDATION.json').read_text())['completed']
assert json.loads((R/'CAEGraphDisplayPreparationResult.json').read_text())['阶段状态']=='完整'
assert git('branch','--show-current')=='codex/oi-f800-stat-20261122-01'
assert git('rev-parse','HEAD')=='ef32a9bed08ad7396b8b91cf0a71330b22ee9103'
assert not git('status','--porcelain') and not target.exists()
exclude={'status-last.json','task-plan.json','SESSION_STATE.json','FINAL_DELIVERY.json','PROFESSIONAL_MANIFEST.json',
 'PROFESSIONAL_PUBLICATION_READBACK.json','RETURN_PUBLICATION_READBACK.json','prepare_return.py','return_validation_template.py'}
folders={'archive','html','screenshots','display_code','source'}
files=[]
for p in sorted(R.rglob('*')):
    rel=p.relative_to(R)
    if not p.is_file() or '__pycache__' in rel.parts or p.name in exclude or p.name.startswith('smoke'):continue
    if len(rel.parts)>1 and rel.parts[0] not in folders:continue
    if len(rel.parts)==1 and p.suffix not in ('.json','.md','.py','.log'):continue
    dst=target/rel;dst.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,dst)
    files.append(dict(name=str(rel),local_path=str(p),record_path=str(REL/rel),bytes=p.stat().st_size,sha256=sha256(p.read_bytes()).hexdigest()))
manifest=dict(run_id=RUN,call_id='C0023',delegation_id='D010',prepared_at=datetime.now(timezone.utc).isoformat(),
 scope='原M-C C1/C2A/真实C2 HTML迭代及C3可注入具体代码；当前唯一HTML为html/current.html。档案和早期失败不当作当前预期。',
 files=files,current_validation='VALIDATION.json',immutable_inputs='已接受D008 U/X/G及D009 B按exact引用保留，不复制重跑或更改。',
 uplot_snapshot='source/uplot为0a4精确原件只读快照，20个文件逐字核哈希，非工具修改/发布。',
 local_only=['task-plan/status/session/final-delivery','live ledger','smoke API临时诊断','Return构造模板（校验脚本另发布C0023）'],
 execution_instruction='复现脚本只在原Owner授权BASE运行；C3正式context/实例/位置/字段由后续D注入，不在记录checkout运行Feature生产。')
for d in (R,target):(d/'PROFESSIONAL_MANIFEST.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'files_with_manifest':len(files)+1,'bytes':sum(f['bytes'] for f in files),'target':str(target)},ensure_ascii=False))
