"""只将本Run已验收产物复制到授权记录根；不提交、不推送。"""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
import json
import shutil
import subprocess

ROOT=Path(__file__).resolve().parent
RECORD=Path('/dwdhome/fy/cgpterm/artifacts/wall-f-closure-20261122/OI-F800-STAT-20261122-01/executor-records')
RUN='OI-F800-STAT-20261122-01'
BASE=RECORD/'longrun/runs'/RUN
TARGET=BASE/'professional/D002'
assert json.loads((ROOT/'VALIDATION.json').read_text())['completed']
assert subprocess.check_output(['git','branch','--show-current'],cwd=RECORD,text=True).strip()=='codex/oi-f800-stat-20261122-01'
assert not TARGET.exists(),'避免覆盖已发布的D002成果'
items=[]
def copy(path,relative=None):
    relative=relative or path.relative_to(ROOT)
    to=TARGET/relative
    to.parent.mkdir(parents=True,exist_ok=True)
    shutil.copy2(path,to)
    items.append(dict(record_relative_path=str(to.relative_to(RECORD)),local_source=str(path),
        sha256=sha256(path.read_bytes()).hexdigest(),bytes=path.stat().st_size))
for path in sorted(ROOT.iterdir()):
    if path.is_file() and path.suffix in ['.json','.py','.md']:
        copy(path)
for folder in ['preflight','produced','readback','profile']:
    for path in sorted((ROOT/folder).rglob('*')):
        if path.is_file() and path.suffix in ['.json','.csv']:
            copy(path)
for name in ['produce.log','readback.log','upstream.log','profile.log','validation.log','supervisor-tool-result.txt']:
    copy(ROOT/name)
catalog=dict(archived_at=datetime.now(timezone.utc).isoformat(),workspace_artifact_root=str(ROOT),
    execution_instruction='归档脚本供审阅；真实执行位置为local_source所示Owner工作区，不能直接在记录checkout执行。OnlyRead也会写导出/报告，需使用原工作区。',
    local_only=['store/**原生dba','upstream/**完整源输入CSV','platform-app/**平台配置和任务JSON','logs/**平台日志'],
    immutable_evidence='NATIVE_OUTPUT_MANIFEST.json、UPSTREAM_EXTRACTION.json分别保存原生结果与输入导出的准确路径、规模及SHA-256；31张F公开表CSV已归档。',files=items)
(TARGET/'ARTIFACT_CATALOG.json').write_text(json.dumps(catalog,ensure_ascii=False,indent=2)+'\n')
call=BASE/'calls/C0005'
call.mkdir(parents=True,exist_ok=True)
(call/'EXECUTOR_REPORT.md').write_text('''# C0005｜E1对D002的专业回交报告

原D002已完成正式X及原Skill G1–G8：新生产rb/hc/i三年F800，独立回读31表一致，480个候选Life、1546次观点。

完整专业报告：[D002/EXECUTOR_REPORT.md](../../professional/D002/EXECUTOR_REPORT.md)。原生输出：[FeatureRunResultBinding.json](../../professional/D002/FeatureRunResultBinding.json)、[FeatureGlobalBehaviorProfilingResult.json](../../professional/D002/FeatureGlobalBehaviorProfilingResult.json)。

GlobalProfileGate=DIAGNOSIS_REQUIRED。覆盖标志与连续输入对照冲突22次观点/12个Life，一项结构疑点和诊断适配包均已交付；另4项场景问题、10个候选案例。未做根因诊断、调参或Feature释放。D002无尚未满足的原Skill工作，后继专业步骤由原manager签发。

没有Worker或新委派。本报告与专业产物先行发布，C0005 PRO_RETURN随后引用该已发布提交；不把executor自述完成当作manager已消费。
''')
print(json.dumps(dict(copied_files=len(items),total_bytes=sum(x['bytes'] for x in items),target=str(TARGET)),ensure_ascii=False))
