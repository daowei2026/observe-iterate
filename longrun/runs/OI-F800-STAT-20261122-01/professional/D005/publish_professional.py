"""将已验收本次原生专业产物复制到允许的Run记录子树；不运行Feature。"""
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
import shutil
import json
import subprocess

ROOT=Path(__file__).resolve().parent
RECORD=Path('/dwdhome/fy/cgpterm/artifacts/wall-f-closure-20261122/OI-F800-STAT-20261122-01/executor-records')
RUN='OI-F800-STAT-20261122-01'
TARGET=RECORD/'longrun/runs'/RUN/'professional/D005'
assert json.loads((ROOT/'VALIDATION.json').read_text())['completed']
assert not TARGET.exists(),'禁止覆盖已发布专业原件'
assert subprocess.check_output(['git','branch','--show-current'],cwd=RECORD,text=True).strip()=='codex/oi-f800-stat-20261122-01'
assert not subprocess.check_output(['git','status','--porcelain'],cwd=RECORD,text=True)
items=[]
def copy(path):
    relative=path.relative_to(ROOT);to=TARGET/relative
    to.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(path,to)
    items.append(dict(record_relative_path=str(to.relative_to(RECORD)),local_source=str(path),
        sha256=sha256(path.read_bytes()).hexdigest(),bytes=path.stat().st_size))
for path in sorted(ROOT.iterdir()):
    if path.is_file() and path.suffix in ('.json','.py','.md') and path.name not in ('task-plan.json','status-last.json','FINAL_DELIVERY.json'):copy(path)
for folder in ('preflight','produced','readback','profile','comparison'):
    for path in sorted((ROOT/folder).rglob('*')):
        if path.is_file() and path.suffix in ('.json','.csv'):copy(path)
for name in ('preflight.log','produce.log','readback.log','upstream.log','profile.log','comparison.log','native-retest.log','validation.log'):copy(ROOT/name)
catalog=dict(archived_at=datetime.now(timezone.utc).isoformat(),workspace_artifact_root=str(ROOT),files=items,
    execution_instruction='脚本归档供审阅，执行位置仅限Owner授权BASE原工作区；不可直接在记录checkout运行。',
    local_only=['store/**原生dba','upstream/**完整源输入CSV','platform-app/**','logs/**','__pycache__/**','task-status ledgers'],
    evidence='31张公开表已归档；原生输出与15张上游导出由NATIVE_OUTPUT_MANIFEST及UPSTREAM_EXTRACTION保存真实路径/规模/SHA。')
(TARGET/'ARTIFACT_CATALOG.json').write_text(json.dumps(catalog,ensure_ascii=False,indent=2)+'\n')
call=RECORD/'longrun/runs'/RUN/'calls/C0012'
(call/'EXECUTOR_REPORT.md').write_text('''# C0012｜原E1对D005的回交

已完成be57新版本F-only rb/hc/i、5m、2021—2023完整正式生产、独立31表读回及原Skill G1–G8。480个候选Life、1534次Revision，原22次错误flag及8次cold对照经独立原生Life/AsOf复验30/30通过，F800-GF-001已在最新完整剖面关闭。

最终GlobalProfileGate=DIAGNOSIS_REQUIRED。新识别F800-GF-002：8次观点/5个Life/6个时刻的完整覆盖标志与同窗公开OHLC缺值并存；旧版同位置也存在，尚未诊断缺值/Calendar/覆盖语义，不宣称新增回归。一个诊断适配包、四项场景问题和候选索引已形成。

原生报告见[professional/D005/EXECUTOR_REPORT.md](../../professional/D005/EXECUTOR_REPORT.md)，绑定与Gate见同目录。D005已完成专业职责，后继由原manager按原Workflow进入business-discrepancy-diagnosis；未修改正式行为、未启动Q/V、未替父Run出释放结论。专业产物先发布，PRO_RETURN随后引用已有exact提交。
''')
print(json.dumps(dict(copied_files=len(items)+1,total_bytes=sum(r['bytes'] for r in items),target=str(TARGET)),ensure_ascii=False))
