"""只将本D清单内容提交到Owner指定Run分支；发布后另做远端核验。"""
from common import *
import shutil

def git(*args):return subprocess.check_output(['git',*args],cwd=RECORD)
assert git('branch','--show-current').decode().strip()=='codex/oi-f800-stat-20261122-01'
assert git('rev-parse','HEAD').decode().strip()=='8d1b3b0048dbee8f916d8bf16bf1e4122ee6540a'
assert git('status','--porcelain')==b''
assert json.loads((ROOT/'VALIDATION.json').read_text())['checks_passed']
ignored={'plan.json','PROFESSIONAL_MANIFEST.json','PROFESSIONAL_PUBLICATION_READBACK.json',
         'RETURN_PUBLICATION_READBACK.json','FINAL_DELIVERY.json','SESSION_STATE.json'}
files=[]
for path in sorted(ROOT.rglob('*')):
    if not path.is_file() or '__pycache__' in path.parts or path.name in ignored:continue
    rel=path.relative_to(ROOT).as_posix();raw=path.read_bytes()
    files.append(dict(file=rel,local_path=str(path),record_path=f'{PREFIX}/professional/D014/{rel}',
        bytes=len(raw),sha256=sha(raw)))
manifest=dict(run_id=RUN,delegation_id='D014',call_id='C0031',created_at=now(),files=files,
    file_count=len(files),total_payload_bytes=sum(r['bytes'] for r in files),
    scope='只含本D原S2产物/来源原件/原值回读/实际截图及核验脚本；冻结v1与代码/CAEGraph输入不改。',
    manifest_self_excluded=True,workers=[])
save('PROFESSIONAL_MANIFEST.json',manifest)
target=RECORD/PREFIX/'professional/D014'
assert not target.exists()
for row in files:
    dest=RECORD/row['record_path'];dest.parent.mkdir(parents=True,exist_ok=True)
    shutil.copyfile(row['local_path'],dest)
    assert sha(dest.read_bytes())==row['sha256']
shutil.copyfile(ROOT/'PROFESSIONAL_MANIFEST.json',target/'PROFESSIONAL_MANIFEST.json')
subprocess.run(['git','add','--',f'{PREFIX}/professional/D014'],cwd=RECORD,check=True)
staged=git('diff','--cached','--name-only','-z').decode().rstrip('\0').split('\0')
assert staged and all(s.startswith(f'{PREFIX}/professional/D014/') for s in staged)
# 输入逐字保留，不重写上游原件空白；本D编写文件均检查。
own=[s for s in staged if '/inputs/' not in s and '/locked_skill/' not in s]
subprocess.run(['git','diff','--cached','--check','--',*own],cwd=RECORD,check=True)
subprocess.run(['git','commit','--quiet','-m',f'{RUN} D014: complete frozen-case S2 evidence comparison'],cwd=RECORD,check=True)
commit=git('rev-parse','HEAD').decode().strip()
assert git('status','--porcelain')==b''
subprocess.run(['git','push','origin','HEAD:refs/heads/codex/oi-f800-stat-20261122-01'],cwd=RECORD,check=True)
remote=git('ls-remote','origin','refs/heads/codex/oi-f800-stat-20261122-01').decode().split()[0]
assert remote==commit
print(json.dumps(dict(commit=commit,files=len(staged),payload_bytes=manifest['total_payload_bytes'],remote_head=remote,clean=True),ensure_ascii=False))
