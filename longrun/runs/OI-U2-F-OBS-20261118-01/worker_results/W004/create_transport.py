from pathlib import Path
import datetime,hashlib,json,os,subprocess
r=Path(__file__).resolve().parent;rid='OI-U2-F-OBS-20261118-01';prefix='longrun/runs/'+rid+'/worker_results/W004/'
def read(name):return json.loads((r/name).read_text())
def raw_hash(data):return hashlib.sha256(data).hexdigest()
def blob_hash(data):return hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
def save_new(name,value):
 with (r/name).open('x',encoding='utf-8') as f:json.dump(value,f,ensure_ascii=False,indent=2);f.write('\n')
assert not (r/'MANIFEST.local.json').exists() and not (r/'TRANSPORT_PAYLOAD.json').exists()
assert not (r/'WORKER_RETURN.json').exists()
prep=read('RETURN_PREPARATION.json');facts=read('facts.json');assert facts['fact_state']=='BLOCKED' and prep['fixed_fields']['outcome']=='STOP'
paths=set()
excluded_root={'MANIFEST.local.json','TRANSPORT_PAYLOAD.json','SHA256SUMS','WORKER_RETURN.json','WORKER_RETURN.validation.json'}
for p in r.iterdir():
 if p.is_file() and p.name not in excluded_root:paths.add(p)
for directory in ['inputs','logs','diagnostics','output/u2_f_caegraph']:
 for p in (r/directory).iterdir():
  if p.is_file() and p.name!='task_status_cli.log':paths.add(p)
existing={}
for name,repo,commit in [('observe_iterate','daowei2026/observe-iterate','f4f0e4b276b1118b779473c1fbe462bc7a64b358'),('tis','daowei2026/tis','2f460d663d821cf2ba25555eda13e78b697d0767')]:
 stage=read(name+'_source_stage_report.json');root=Path(stage['source_root'])
 for x in stage['files']:
  p=Path(x['path']);paths.add(p);ref=repo+'@'+commit+':'+x['relative_path']
  if x['relative_path'].endswith('/C/caegraph_display.py'):ref='daowei2026/observe-iterate@508d494c964d5dabeaa1e7ea17bef908f749e9c8:'+x['relative_path']
  if x['relative_path'].endswith('/C/caegraph_display_preview.html'):ref='daowei2026/observe-iterate@56eef30b28c928255329f77798fb46b9adbbc71a:'+x['relative_path']
  existing[p]=ref
 if name=='tis':
  for rel in ['blk/gen.py','.exportignore']:
   p=root/rel
   if p.is_file():paths.add(p);existing[p]=repo+'@'+commit+':'+rel
for x in read('tis_generated_inits.json')['generated']:paths.add(Path(x['path']))
for p in paths:assert p.resolve().is_relative_to(r) and not p.is_symlink()
def entry(p):
 data=p.read_bytes();rel=str(p.relative_to(r));return {'relative_path':rel,'local_path':str(p),'bytes':len(data),'sha256':raw_hash(data),'git_blob_sha1':blob_hash(data),'existing_ref':existing.get(p),'suggested_publication_path':None if p in existing else prefix+rel}
files=[entry(p) for p in sorted(paths,key=lambda p:str(p.relative_to(r)))]
assert len({x['relative_path'] for x in files})==len(files)
manifest={'format':'local-worker-evidence-manifest/v2','run_id':rid,'work_order_id':'W004','parent_delegation_id':'D005','worker':prep['fixed_fields']['worker'],'return_to':prep['fixed_fields']['return_to'],'order_ref':prep['fixed_fields']['order_ref'],'fact_state':'BLOCKED','proposed_worker_return_outcome':'STOP','result_local_path':str(r/'FACT_REPORT.md'),'result_ref':None,'new_evidence_commit':None,'created_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'file_count_excluding_manifest_self':len(files),'complete_utf8_bodies_transport_path':str(r/'TRANSPORT_PAYLOAD.json'),'self_hash_rule':'本manifest不递归列自身；TRANSPORT_PAYLOAD另含本manifest完整正文和hash。SHA256SUMS另含transport payload的hash，不递归列SHA256SUMS自身。','missing':prep['fixed_fields']['missing'],'absent_outputs':[{'local_path':str(r/'output/u2_f_caegraph/u2_f_caegraph.html'),'exists':False},{'local_path':str(r/'output/u2_f_caegraph/prepared_tables'),'exists':False},{'local_path':str(r/'output/u2_f_caegraph/plot_data'),'exists':False}],'present_incomplete_report':{'local_path':str(r/'output/u2_f_caegraph/definition_run_report.json'),'completed':False},'excluded_runtime_material':['source checkout .git数据库与非声明源码（源码版本由原精确commit保留）','cache目录','artifacts/task-status实时events/snapshot与logs/task_status_cli.log','TRANSPORT_PAYLOAD与SHA256SUMS递归自身','未来尚不存在的正式WORKER_RETURN.json'],'files':files}
save_new('MANIFEST.local.json',manifest)
files.append(entry(r/'MANIFEST.local.json'));files.sort(key=lambda x:x['relative_path'])
with_bodies=[]
for x in files:
 p=Path(x['local_path']);b=p.read_bytes();assert len(b)==x['bytes'] and raw_hash(b)==x['sha256'] and blob_hash(b)==x['git_blob_sha1']
 body=b.decode('utf-8');assert body.encode('utf-8')==b
 with_bodies.append({**x,'body_utf8':body})
payload={'format':'local-worker-complete-body-transport/v2','run_id':rid,'work_order_id':'W004','parent_delegation_id':'D005','worker':prep['fixed_fields']['worker'],'return_to':prep['fixed_fields']['return_to'],'order_ref':prep['fixed_fields']['order_ref'],'fact_state':'BLOCKED','proposed_worker_return_outcome':'STOP','all_bodies_are_complete':True,'is_formal_worker_return':False,'new_evidence_commit':None,'file_count':len(with_bodies),'new_publication_file_count':sum(x['existing_ref'] is None for x in with_bodies),'reuse_exact_ref_file_count':sum(x['existing_ref'] is not None for x in with_bodies),'transport_instructions':'按各body_utf8原样发布需要新增的正文；已有existing_ref仅复用精确原件。不改body，不伪造未来refs；发布回读/hash通过后给真实映射供同W004正式Return签认。','files':with_bodies}
save_new('TRANSPORT_PAYLOAD.json',payload)
transport_bytes=(r/'TRANSPORT_PAYLOAD.json').read_bytes()
lines=[x['sha256']+'  '+x['relative_path'] for x in files]+[raw_hash(transport_bytes)+'  TRANSPORT_PAYLOAD.json']
with (r/'SHA256SUMS').open('x',encoding='utf-8') as f:f.write('\n'.join(lines)+'\n')
roundtrip=read('TRANSPORT_PAYLOAD.json');assert len(roundtrip['files'])==len(files)
for x in roundtrip['files']:
 b=Path(x['local_path']).read_bytes();assert b==x['body_utf8'].encode('utf-8') and len(b)==x['bytes'] and raw_hash(b)==x['sha256'] and blob_hash(b)==x['git_blob_sha1']
# 仅更新未封存的本地状态投影，不改运输正文。
env=os.environ.copy();env['PYTHONDONTWRITEBYTECODE']='1';env.pop('LONG_TASK_CONTROL_REGISTER_HELPER',None)
cli='/home/dw/.agents/skills/long-task-status/scripts/task_status.py';tid='oi-u2-f-obs-20261118-01-w004'
for a in [['step-complete','--root',str(r),'--task-id',tid,'--step-id','transport','--evidence',str(r/'FACT_REPORT.md'),'--evidence',str(r/'MANIFEST.local.json'),'--evidence',str(r/'TRANSPORT_PAYLOAD.json')],['update','--root',str(r),'--task-id',tid,'--status','waiting_external','--action','本地执行事实BLOCKED：D一次exit1，mquant.tis.t1缺失；完整运输包封存，尚未正式Return或业务完成','--next-action','主控原样发布并回读证据，给真实ref/hash映射后同W004签认Return回原E1']]:
 p=subprocess.run(['/usr/bin/python',cli]+a,env=env,cwd=r,capture_output=True,text=True)
 with (r/'logs/task_status_cli.log').open('a') as log:log.write(json.dumps(a,ensure_ascii=False)+'\n'+p.stdout+p.stderr)
 assert p.returncode==0,p.stderr
for x in roundtrip['files']:
 b=Path(x['local_path']).read_bytes();assert b==x['body_utf8'].encode('utf-8') and raw_hash(b)==x['sha256']
assert (r/'TRANSPORT_PAYLOAD.json').read_bytes()==transport_bytes
summary={'fact_state':'BLOCKED','proposed_outcome':'STOP','D_attempt_count':1,'D_exit_code':1,'module_overlay_ok':True,'origin_checks_passed':7,'generated_empty_inits':18,'seeder_exit_code':0,'first_blocker':facts['first_blocker']['error'],'file_count':len(files),'new_publication_file_count':payload['new_publication_file_count'],'reuse_exact_ref_file_count':payload['reuse_exact_ref_file_count'],'complete_body_roundtrip':'PASS','business_source_diff_bytes':0,'local_status':'waiting_external','formal_worker_return_exists':(r/'WORKER_RETURN.json').exists(),'files':[]}
for n in ['FACT_REPORT.md','MANIFEST.local.json','TRANSPORT_PAYLOAD.json','SHA256SUMS','RETURN_PREPARATION.json']:
 p=r/n;b=p.read_bytes();summary['files'].append({'path':str(p),'bytes':len(b),'sha256':raw_hash(b)})
print(json.dumps(summary,ensure_ascii=False,indent=2))
