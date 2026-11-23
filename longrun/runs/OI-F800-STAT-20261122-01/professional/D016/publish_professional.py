"""只发布本D原生诊断到原授权Run分支；先专业对象，后另commit原Return。"""
from common import *
import shutil
def git(*a):return subprocess.check_output(['git',*a],cwd=RECORD)
assert git('branch','--show-current').decode().strip()=='codex/oi-f800-stat-20261122-01'
assert git('rev-parse','HEAD').decode().strip()==INITIAL and git('status','--porcelain')==b''
assert json.loads((ROOT/'VALIDATION.json').read_text())['checks_passed']
ignored={'plan.json','PROFESSIONAL_MANIFEST.json','PROFESSIONAL_PUBLICATION_READBACK.json','RETURN_PUBLICATION_READBACK.json','FINAL_DELIVERY.json','SESSION_STATE.json'}
files=[]
for p in sorted(ROOT.rglob('*')):
 if not p.is_file() or '__pycache__' in p.parts or p.name in ignored:continue
 rel=p.relative_to(ROOT).as_posix();raw=p.read_bytes()
 files.append(dict(file=rel,local_path=str(p),record_path=PREFIX+'/professional/D016/'+rel,bytes=len(raw),sha256=sha(raw)))
manifest=dict(run_id=RUN,call_id='C0036',delegation_id='D016',professional_control_commit=LOCKED,created_at=now(),files=files,file_count=len(files),total_payload_bytes=sum(f['bytes'] for f in files),manifest_self_excluded=True,workers=[],scope='当前单一Owner候选的原生D与完整36项证据；旧专业结果和正式源码只读复用。')
save('PROFESSIONAL_MANIFEST.json',manifest)
target=RECORD/PREFIX/'professional/D016';assert not target.exists()
for f in files:
 p=RECORD/f['record_path'];p.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(f['local_path'],p)
 assert sha(p.read_bytes())==f['sha256']
shutil.copyfile(ROOT/'PROFESSIONAL_MANIFEST.json',target/'PROFESSIONAL_MANIFEST.json')
subprocess.run(['git','add','--',PREFIX+'/professional/D016'],cwd=RECORD,check=True)
staged=git('diff','--cached','--name-only','-z').decode().rstrip('\0').split('\0')
assert staged and all(p.startswith(PREFIX+'/professional/D016/') for p in staged)
own=[p for p in staged if '/inputs/' not in p and '/source/' not in p]
subprocess.run(['git','diff','--cached','--check','--',*own],cwd=RECORD,check=True)
subprocess.run(['git','commit','--quiet','-m',RUN+' D016: localize and diagnose all 36 peak candidate lives'],cwd=RECORD,check=True)
commit=git('rev-parse','HEAD').decode().strip()
subprocess.run(['git','push','origin','HEAD:refs/heads/codex/oi-f800-stat-20261122-01'],cwd=RECORD,check=True)
remote=git('ls-remote','origin','refs/heads/codex/oi-f800-stat-20261122-01').decode().split()[0]
assert commit==remote and git('status','--porcelain')==b''
print(json.dumps(dict(commit=commit,remote_head=remote,files=len(staged),payload_bytes=manifest['total_payload_bytes'],clean=True),ensure_ascii=False))
