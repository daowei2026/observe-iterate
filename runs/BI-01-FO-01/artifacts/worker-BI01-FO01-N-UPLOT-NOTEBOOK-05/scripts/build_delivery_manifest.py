"""本次有限技术交付的文件清单，不创建生产/平台身份。"""
from pathlib import Path
import hashlib,json
OUT=Path(__file__).resolve().parents[1]
excluded={'DELIVERY_MANIFEST.json','GITHUB_RECEIPT.json'}
files=[]
for path in sorted(OUT.rglob('*')):
    if not path.is_file() or any(part in ('.ipynb_checkpoints','__pycache__') for part in path.relative_to(OUT).parts):continue
    if path.name in excluded:continue
    raw=path.read_bytes()
    files.append({'path':str(path.relative_to(OUT)),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()})
manifest={'order_id':'BI01-FO01-N-UPLOT-NOTEBOOK-05','issuer_invocation_id':'BI01-FO-01-R0014-20261023T153303Z-57f340f3',
 'qualification':'Worker05实际工作2技术实物；原Pro判断/管理认可另行发生',
 'file_count':len(files),'bytes':sum(p['bytes'] for p in files),'excluded':['本清单自身','GITHUB_RECEIPT.json（提交后发布回执）','Jupyter checkpoints/pycache','本机ignored端口/认证材料及截图'], 'files':files}
(OUT/'DELIVERY_MANIFEST.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
print(manifest['file_count'],manifest['bytes'])
