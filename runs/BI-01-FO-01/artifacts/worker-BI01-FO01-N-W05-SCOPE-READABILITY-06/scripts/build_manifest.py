"""本单有限交付清单；不重验或重传W05整包。"""
from pathlib import Path
import hashlib,json

OUT=Path(__file__).resolve().parents[1]
files=[]
for p in sorted(OUT.rglob('*')):
    if not p.is_file() or any(x in p.relative_to(OUT).parts for x in ('__pycache__','.ipynb_checkpoints','.pytest_cache')):continue
    if p.name in ('DELIVERY_MANIFEST.json','GITHUB_RECEIPT.json'):continue
    b=p.read_bytes();files.append({'path':str(p.relative_to(OUT)),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()})
manifest={'order_id':'BI01-FO01-N-W05-SCOPE-READABILITY-06',
          'issuer_invocation_id':'BI01-FO-01-R0017-20261023T192809Z-edd5489f',
          'qualification':'W06实际增量；W05原整包固定引用b055102，不重新打包。清单不是业务接收。',
          'file_count':len(files),'bytes':sum(x['bytes'] for x in files),'files':files,
          'excluded':['本清单自身','GITHUB_RECEIPT.json（payload后的真实发布回执）','pycache/checkpoints/pytest_cache','本机ignored截图/端口/凭据/现场账本']}
(OUT/'DELIVERY_MANIFEST.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
print(manifest['file_count'],manifest['bytes'])
