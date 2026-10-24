"""收集本单必要安全元数据/版本/清单；不收原URL、环境或原认证日志。"""
from pathlib import Path
import argparse,ast,datetime,hashlib,json,re,subprocess

p=argparse.ArgumentParser();p.add_argument('--runtime',type=Path,required=True)
args=p.parse_args();rt=args.runtime;out=Path(__file__).resolve().parents[1]
e=out/'evidence'
write=lambda path,value:path.write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n')
read=lambda name:json.loads((rt/name).read_text())
processes=read('ACTIVE_PROCESS_METADATA.private.json')
write(e/'ACTIVE_PROCESS_METADATA.json',[{k:v for k,v in x.items() if k not in ['pid','whitelisted_environment','stdout_kind']} for x in processes])
write(e/'PERMISSIONS.json',read('PERMISSIONS.json'))
active=read('ACTIVE_TRIER_FASON_OBSERVATION.json')
response=read('ACTIVE_ORDINARY_DOC_RESPONSE.private.json')
payload=response.get('data',{})
pp=payload.get('_ppjson_') if isinstance(payload,dict) else None
if isinstance(pp,str):
 expression=ast.parse(pp,mode='eval').body
 mapping={k.value:v for k,v in zip(expression.args[0].keys,expression.args[0].values) if isinstance(k,ast.Constant)}
 active['ppjson_parameter_keys']=sorted(mapping)
 active['sample_fixed_input_manifest_nonempty']=bool(ast.literal_eval(mapping['fixed_input_manifest']))
 active['scope']='existing shared-class legacy fixed_input instance; only observe active parameter contract, not a non-N market-page success'
 active['selection_limit']='selector excludes the new N key; this does not prove the historical sample is a non-N business object'
write(e/'ACTIVE_TRIER_FASON_OBSERVATION.json',active)
write(e/'ACTIVE_TRIER_N_RECOVERY.json',read('ACTIVE_TRIER_N_RECOVERY.json'))
write(e/'LEGACY_ORDINARY_SAMPLE.json',{'node_id':889,'http_status':200,'application_code':3000,
    'unknown_parameter':'bigscale_freq','scope':'只读初筛的历史实例；不归因cbd，不修改节点，后续使用最新合格6126'})
old_log=(rt/'old-library.private.log').read_text()
failure=next((b for b in old_log.split('Traceback (most recent call last):')[1:]
              if "have no param key 'normal_node_behavior_manifest'" in b),None)
if failure:
 frames=[{'file':m[0],'line':int(m[1]),'function':m[2]}
         for m in re.findall(r'File "([^"\n]+)", line (\d+), in ([^\n]+)',failure)]
 write(e/'OLD_RESTORE_FAILURE_FRAMES.json',{'source':'actual isolated old restore traceback',
     'unknown_parameter':'normal_node_behavior_manifest','frames':frames,
     'qualification':'仅保留调用位置，不展开异常参数上下文'})
repo=Path('/dwdhome/fy/BASE_E6_2/mquant/aidata-bi01-fo01-n-platform-board-r0022')
git=lambda *a:subprocess.check_output(['git','-C',str(repo),*a],text=True).strip()
assert Path(git('rev-parse','--show-toplevel'))==repo
refs={'shared':'f58ea95c358b9ac31659c92b7bc20fe9bf7f8264','work2':'8a08300cb70a610401424bedadb42e9dcde13e71','cbd':'cbd0a1f9bf92d9d65e0ad00bfd1a9e3afb7c2cf0'}
files=['feature_configs/__init__.py','feature_configs/u2_normal_node_behavior.py',
 'u2_normal_node_behavior_display.py','normal_node_behavior.py','big_world_chart.py',
 'boardrun.py','delivery.py','run_brief_spec.py','timespan_builder.py',
 'evidence_plot.py','feature_slicer.py','contracts.py','csv_feature.py','README.md']
inventory=[]
for file in files:
 row={'path':file}
 for name,ref in refs.items():
  result=subprocess.run(['git','-C',str(repo),'rev-parse','--verify',f'{ref}:{file}'],text=True,capture_output=True)
  row[name+'_blob']=result.stdout.strip() if result.returncode==0 else None
 inventory.append(row)
base=Path('/dwdhome/fy/BASE_E6_2')
protected=['mquant/frame/lang/internal/base.py','mquant/frame/lang/cae.py',
 'mquant/frame/core/app/env.py','mquant/frame/core/base/json.py',
 'mquant/quant/models/graph/dao/fao.py','insights/trier/web/view/graph/view.py',
 'insights/trier/server/bokeh.py','mquant/uplot/pfw.py']
source_hashes=[{'path':str(base/x),'sha256':hashlib.sha256((base/x).read_bytes()).hexdigest(),
   'qualification':'本次磁盘只读源码；不冒充活动进程模块身份'} for x in protected]
write(e/'SOURCE_INVENTORY.json',{'aidata_fixed_refs':refs,'files':inventory,'readonly_source_hashes':source_hashes,
 'frame_overlay_target':str(Path('/tmp/bi01-fo01-w03-runtime-20261022/mquant/frame').resolve()),
 'no_aidata_source_edits_or_new_branch':True})
selection_path=Path('/dwdhome/fy/observe-iterate-bi01-fo-01/artifacts/bi01-worker07-runs/BI01-FO01-W07-20261024T0028-rb/manifest/normal_node_behavior.json')
selection=json.loads(selection_path.read_text())
write(e/'EXISTING_N_SELECTION.json',{'source_path':str(selection_path),'sha256':hashlib.sha256(selection_path.read_bytes()).hexdigest(),
 'reused_fields':{k:selection[k] for k in ['symbol','as_of','node_life','expected_exact']},
 'scope':'只读原W07 manifest元数据；不新读N表或运行layout'})
findings=[]
patterns={'credential_url':r'\w+://[^\s/]+:[^\s/@]+@',
 'private_ipv4':r'\b(?:10\.\d+\.\d+\.\d+|192\.168\.\d+\.\d+|172\.(?:1[6-9]|2\d|3[01])\.\d+\.\d+)\b'}
for path in out.rglob('*'):
 if path.is_file() and path.suffix in ['.json','.py','.md','.log','.csv']:
  text=path.read_text()
  for kind,pattern in patterns.items():
   if re.search(pattern,text):findings.append({'path':str(path.relative_to(out)),'kind':kind})
write(e/'TRANSPORT_SAFETY_CHECK.json',{'scope':'本单待交付文件的限定凭据URL/私网地址扫描；不关闭历史日志事件','unresolved_candidates':findings})
if findings:raise SystemExit('transport contains a candidate requiring review; values not output')
manifest=[]
for path in sorted(out.rglob('*')):
 if path.is_file() and path.name not in ['DELIVERY_MANIFEST.json','GITHUB_RECEIPT.json']:
  payload=path.read_bytes();manifest.append({'path':str(path.relative_to(out)),'bytes':len(payload),'sha256':hashlib.sha256(payload).hexdigest()})
write(out/'DELIVERY_MANIFEST.json',{'order_id':'BI01-FO01-N-CONSUMER-CONTRACT-08',
 'generated_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'excludes':['DELIVERY_MANIFEST.json','GITHUB_RECEIPT.json'],'files':manifest})
print(json.dumps({'source_inventory_complete':True,'transport_safe_candidates':len(findings),
 'files':len(manifest),'bytes':sum(x['bytes'] for x in manifest)},ensure_ascii=False))
