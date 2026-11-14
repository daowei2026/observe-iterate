import pathlib,json,hashlib,re,datetime,os
W=pathlib.Path(__file__).resolve().parents[1];checks=[]
required=['WORKER_EXECUTION_REPORT.md','WORKSPACE_BINDING.json','CODE_AND_READER_ENTRYPOINTS.md','ASSET_INVENTORY.json','COMMAND_LOG.txt','SAMPLE_CHAIN.jsonl','SAMPLE_CHAIN_README.md','ACTION_PREFLIGHT_FACTS.md','WORKER_RETURN_PREPARATION.json']
for name in required:
 p=W/name;assert p.is_file() and p.stat().st_size>0;checks.append({'path':str(p),'exists':True,'bytes':p.stat().st_size,'sha256_at_check':hashlib.sha256(p.read_bytes()).hexdigest()})
def strict(p):return json.loads(p.read_text(),parse_constant=lambda v:(_ for _ in ()).throw(ValueError('nonstandard JSON '+v)))
parsed=[]
for p in W.rglob('*.json'):
 if p.is_file():strict(p);parsed.append(str(p))
for p in W.rglob('*.jsonl'):
 if p.is_file():
  for line in p.open():
   if line.strip():json.loads(line,parse_constant=lambda v:(_ for _ in ()).throw(ValueError(v)))
samples=[json.loads(x) for x in (W/'SAMPLE_CHAIN.jsonl').read_text().splitlines()];assert len(samples)==3
ret=strict(W/'WORKER_RETURN_PREPARATION.json');assert ret['return_to']=='chatgpt:OI-EAW-WALL-20261114-01:executor:E1' and ret['outcome']=='PARTIAL' and ret['result_ref'] is None and not (W/'WORKER_RETURN.json').exists()
assert not list(W.rglob('__pycache__'))
for p in W.rglob('*'):assert not p.is_symlink() and p.resolve().is_relative_to(W)
source=pathlib.Path('/dwdhome/fy/cgpterm/artifacts/oi-eaw-wall/OI-EAW-WALL-20261114-01/observe-iterate/longrun/contracts/longrun_schema_v2.json');dest=W/'inputs/longrun_schema_v2.json';dest.write_bytes(source.read_bytes())
commands=sorted(W.glob('evidence/*.command.json'));codes={}
for p in commands:
 row=strict(p);codes.setdefault(str(row['exit_code']),[]).append(row['label'])
# Not a content proof: enumerate credential-shaped strings locally without printing any values.
credential_findings=[]
patterns=[re.compile(r'(?i)https?://[^\s/]+:[^\s/@]+@'),re.compile(r'\bgh[pousr]_[A-Za-z0-9]{20,}\b'),re.compile(r'\bsk-(?:proj-)?[A-Za-z0-9_-]{24,}\b')]
for p in W.rglob('*'):
 if p.is_file() and p.suffix in ('.txt','.json','.jsonl','.md','.py') and p.stat().st_size<5*1024*1024:
  txt=p.read_text(errors='replace')
  if any(q.search(txt) for q in patterns):credential_findings.append(str(p))
assert not credential_findings
validation={'scope':'本地交付文件结构/strict JSON/实际样本物理对账；未运行算法测试或新Run','checked_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'required_files':checks,'json_files_parsed':len(parsed),'sample_records':len(samples),'no_pycache_or_symlink':True,'credential_shaped_findings':credential_findings,'command_exit_codes':codes,'publication_not_performed':True,'formal_return_deferred':True,'hash_index':'由封包命令最终生成并再次逐项校验；本报告哈希快照不替代最终 HASHES.sha256'}
(W/'VALIDATION_REPORT.json').write_text(json.dumps(validation,ensure_ascii=False,indent=2)+'\n');print(json.dumps({'required_core_files':len(checks),'json_files_parsed':len(parsed),'sample_records':3,'command_exit_codes':codes,'credential_shaped_findings_count':len(credential_findings)},ensure_ascii=False,indent=2))
