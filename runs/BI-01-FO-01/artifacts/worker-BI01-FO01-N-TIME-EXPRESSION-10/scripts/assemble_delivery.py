"""白名单证据/精确有序源码运输；不含私密日志、截图、旧整包或平台产物。"""
from pathlib import Path
import datetime,hashlib,json,os,shutil,subprocess
OUT=Path(__file__).resolve().parents[1]
RT=Path(os.environ.get('BI01_W10_RUNTIME','/dwdhome/fy/cgpterm/artifacts/bi01-worker10-runtime'))
def sha(b):return hashlib.sha256(b).hexdigest()
def dump(p,x):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(x,ensure_ascii=False,indent=2,allow_nan=False)+'\n')
for name in ('INPUT_VERIFICATION.json','FRONTEND_EPISODE_LIFECYCLE.json','FINAL_UNIT_TESTS.json','AIDATA_GITHUB_READBACK.json','RUNTIME_BOUNDARIES.json'):
 source=RT/name
 if source.exists():shutil.copy2(source,OUT/'evidence'/name)
nbpath=OUT/'N_time_expression_Worker10.ipynb';raw=nbpath.read_bytes();nb=json.loads(raw)
target=OUT/'notebook_source';target.mkdir(exist_ok=True)
parts=['# Worker10 实际执行Notebook：精确有序源码\n\n',f'主文件 {nbpath.name}；{len(raw)} bytes；SHA256 {sha(raw)}。\n\n',
 '此副本不是完整Notebook：每个cell的source全文逐字保留，大段内嵌JS/widget/图形保存输出不展开，仅列MIME/位置/错误/hash；完整输出仍在主ipynb。\n\n']
indexed=[]
for i,c in enumerate(nb['cells']):
 source=''.join(c['source']);name=f'{i:02d}-{c["id"]}.source.txt';(target/name).write_text(source)
 assert (target/name).read_bytes()==source.encode()
 outputs=[]
 for j,o in enumerate(c.get('outputs',[])):
  encoded=json.dumps(o,ensure_ascii=False,sort_keys=True).encode()
  outputs.append(dict(position=j,output_type=o['output_type'],mime_types=list(o.get('data',{})),ename=o.get('ename'),bytes_json=len(encoded),sha256_json=sha(encoded)))
 indexed.append(dict(position=i,id=c['id'],type=c['cell_type'],execution_count=c.get('execution_count'),metadata=c.get('metadata',{}),
  source_file=name,source_utf8_bytes=len(source.encode()),source_sha256=sha(source.encode()),source_exact_match=True,outputs=outputs))
 parts.extend([f'## {i}. {c["id"]} / {c["cell_type"]} / execution_count={c.get("execution_count")}\n\n',
  'metadata: '+json.dumps(c.get('metadata',{}),ensure_ascii=False)+'\n\n','````'+('python' if c['cell_type']=='code' else 'markdown')+'\n',
  source,'' if source.endswith('\n') else '\n','````\n\n','输出索引：'+json.dumps(outputs,ensure_ascii=False)+'\n\n'])
dump(target/'INDEX.json',dict(notebook_file=nbpath.name,notebook_bytes=len(raw),notebook_sha256=sha(raw),
 notebook_blob=subprocess.check_output(['git','hash-object',str(nbpath)],text=True).strip(),metadata=nb['metadata'],cell_source_exact_match=True,cells=indexed))
(target/'NOTEBOOK_SOURCE.md').write_text(''.join(parts).rstrip()+'\n')
entries=[]
for p in sorted(OUT.rglob('*')):
 if not p.is_file() or any(k in ('.ipynb_checkpoints','__pycache__') for k in p.parts):continue
 name=str(p.relative_to(OUT))
 if name in ('DELIVERY_MANIFEST.json','GITHUB_RECEIPT.json'):continue
 assert not name.endswith(('.png','.private.log','.private.json')),name
 data=p.read_bytes();entries.append(dict(path=name,bytes=len(data),sha256=sha(data),git_blob=subprocess.check_output(['git','hash-object',str(p)],text=True).strip()))
dump(OUT/'DELIVERY_MANIFEST.json',dict(order_id='BI01-FO01-N-TIME-EXPRESSION-10',generated_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),
 qualification='本单新增工作1/2实物；旧包仅准确引用；不代表Pro/管理接收或平台完成',
 excludes=['DELIVERY_MANIFEST.json','GITHUB_RECEIPT.json','.ipynb_checkpoints','__pycache__','private logs/screenshots'],files=entries))
print(json.dumps(dict(notebook_bytes=len(raw),source_cells=len(indexed),manifest_files=len(entries),all_source_exact=True)))
