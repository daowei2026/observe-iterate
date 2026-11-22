from pathlib import Path
from hashlib import sha256
from datetime import datetime,timezone
import json,shutil,subprocess
R=Path(__file__).resolve().parent
RECORD=Path('/dwdhome/fy/cgpterm/artifacts/wall-f-closure-20261122/OI-F800-STAT-20261122-01/executor-records')
RUN='OI-F800-STAT-20261122-01';REL=Path('longrun/runs')/RUN/'professional/D012';target=RECORD/REL
get=lambda *a:subprocess.check_output(['git',*a],cwd=RECORD,text=True).strip()
assert json.loads((R/'VALIDATION.json').read_text())['completed']
assert json.loads((R/'ObservationMaterialPackage.json').read_text())['status']=='DATA_READY'
assert get('branch','--show-current')=='codex/oi-f800-stat-20261122-01' and get('rev-parse','HEAD')=='df7184295277c8dfa60f4664635d32194437e87b'
assert not get('status','--porcelain') and not target.exists()
exclude={'status-last.json','task-plan.json','SESSION_STATE.json','FINAL_DELIVERY.json','PROFESSIONAL_MANIFEST.json','PROFESSIONAL_PUBLICATION_READBACK.json','RETURN_PUBLICATION_READBACK.json','prepare_return.py','return_validation_template.py'}
folders={'final_script','formal_data','screenshots','html','attempts'};files=[]
for p in sorted(R.rglob('*')):
 rel=p.relative_to(R)
 if not p.is_file() or any(x in rel.parts for x in ['__pycache__','runtime-logs']) or p.name in exclude or p.suffix=='.html':continue
 if len(rel.parts)>1 and rel.parts[0] not in folders:continue
 if len(rel.parts)==1 and p.suffix not in ('.json','.md','.py','.log','.diff'):continue
 dst=target/rel;dst.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,dst)
 files.append(dict(name=str(rel),local_path=str(p.resolve()),record_path=str(REL/rel),bytes=p.stat().st_size,sha256=sha256(p.read_bytes()).hexdigest()))
manifest=dict(run_id=RUN,call_id='C0027',delegation_id='D012',prepared_at=datetime.now(timezone.utc).isoformat(),scope='原M-E连续真实运行/修复/核图/E3接受后E4正式取数/E5一致/E6材料DATA_READY；非业务场景预期或Feature释放。',files=files,
 current_validation='VALIDATION.json',material='ObservationMaterialPackage.json',final_HTML='html/f800.html.gz；HTML_ARCHIVES记录解压前后原字节哈希，授权BASE保留可打开原件',formal_graph_data='FORMAL_GRAPH_DATA.json + formal_data/21份construction_snapshot；不是调试表或截图反推。',
 immutable_inputs='原D011完整包/C2-v4原件/U/X/G/B保持，最终运行副本只有有据的刻度显示修复；原C3及20文件uplot快照字节保持。',
 local_only=['task-plan/status/session/final-delivery','live ledger','runtime-logs','未压缩首版HTML（gzip无损副本已发布）','Return构造模板（实际校验脚本另发布calls/C0027）'],
 execution_instruction='在Owner授权BASE运行final_script/run_definition.py，复现须指定新的HTML输出路径，不能覆盖已接受原件；原E4准入仅绑定现有已接受HTML/脚本/运行哈希。')
for dest in (R,target):(dest/'PROFESSIONAL_MANIFEST.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(files_with_manifest=len(files)+1,bytes=sum(f['bytes'] for f in files),target=str(target)),ensure_ascii=False))
