"""仅复制本D原件至授权Run子树；实际commit/push单独执行。"""
from pathlib import Path
from hashlib import sha256
from datetime import datetime,timezone
import json,shutil,subprocess
R=Path(__file__).resolve().parent
RECORD=Path('/dwdhome/fy/cgpterm/artifacts/wall-f-closure-20261122/OI-F800-STAT-20261122-01/executor-records')
RUN='OI-F800-STAT-20261122-01';REL=Path('longrun/runs')/RUN/'professional/D011';target=RECORD/REL
def git(*a):return subprocess.check_output(['git',*a],cwd=RECORD,text=True).strip()
assert json.loads((R/'VALIDATION.json').read_text())['completed']
assert json.loads((R/'CAEGraphDefinitionIntegrationResult.json').read_text())['阶段状态']=='完整'
assert git('branch','--show-current')=='codex/oi-f800-stat-20261122-01'
assert git('rev-parse','HEAD')=='9cd294ffc80bba7ebdbe8bb2889eb1bb77e826d2'
assert not git('status','--porcelain') and not target.exists()
exclude={'status-last.json','task-plan.json','SESSION_STATE.json','FINAL_DELIVERY.json','PROFESSIONAL_MANIFEST.json','PROFESSIONAL_PUBLICATION_READBACK.json','RETURN_PUBLICATION_READBACK.json','prepare_return.py','return_validation_template.py'}
folders={'definition','source','inputs','attempts'}
files=[]
for p in sorted(R.rglob('*')):
 rel=p.relative_to(R)
 if not p.is_file() or '__pycache__' in rel.parts or p.name in exclude:continue
 if len(rel.parts)>1 and rel.parts[0] not in folders:continue
 if len(rel.parts)==1 and p.suffix not in ('.json','.md','.py','.log'):continue
 dst=target/rel;dst.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,dst)
 files.append(dict(name=str(rel),local_path=str(p),record_path=str(REL/rel),bytes=p.stat().st_size,sha256=sha256(p.read_bytes()).hexdigest()))
manifest=dict(run_id=RUN,call_id='C0025',delegation_id='D011',prepared_at=datetime.now(timezone.utc).isoformat(),
 scope='原M-D单一集成：真实实例/数据入口、完整B三年位置、共享字段进入完整CAEGraph定义；仓库理解、纠正、差异和定义检查。未运行E/HTML/正式取图数据。',
 files=files,current_validation='VALIDATION.json',immutable_inputs='已接受D008 U/X/G、D009 B、D010 C保持原件；inputs是准确副本，base_parameters是原D001正常构造形参抽取。',
 C3_renderer='definition/caegraph_display.py与原C3-v1逐字一致，SHA e5d6a235…，展示沿C2-v4唯一预期。',
 uplot_snapshot='source/uplot=0a4准确20文件快照，原始字节保留，不是工具修改/发布。',
 local_only=['task-plan/status/session/final-delivery','live ledger','runtime-logs','Return构造模板（本C校验脚本另发布calls/C0025）'],
 execution_instruction='后继E在Owner授权BASE按原生结果E运行命令执行run_definition.py；D定义检查不构图、不调用Feature.run。正式图数据必须E3接受后E4从同运行meta.roots取得。')
for dest in (R,target):(dest/'PROFESSIONAL_MANIFEST.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(files_with_manifest=len(files)+1,bytes=sum(f['bytes'] for f in files),target=str(target)),ensure_ascii=False))
