import pathlib,json,sys,hashlib,subprocess,datetime
W=pathlib.Path(__file__).resolve().parents[1];sys.path.insert(0,str(W));import runner
binding=json.loads((W/'WORKSPACE_BINDING.json').read_text());audit=[]
for x in binding['repos']:
 if x['name']=='tis_path':continue
 p=pathlib.Path(x['path']);assert (p/'.git').exists()
 current={}
 for key,args in [('head',['rev-parse','HEAD']),('status',['status','--short','--branch'])]:
  cmd=['git','--no-optional-locks','-C',str(p),*args];st=runner.utc();r=subprocess.run(cmd,capture_output=True,text=True,env=runner.environment(),timeout=8);v={'command':cmd,'start':st,'end':runner.utc(),'exit_code':r.returncode,'stdout':r.stdout,'stderr':r.stderr};current[key]=v
  with (W/'COMMAND_LOG.txt').open('a') as f:f.write('\nFINAL_GIT_READONLY_AUDIT '+json.dumps(v,ensure_ascii=False)+'\n')
 same=all(current[k]['exit_code']==0 and current[k]['stdout']==x['commands'][k]['stdout'] for k in current);audit.append({'repo':x['name'],'path':str(p),'head_and_status_unchanged':same,'current':current});assert same
extra=[]
for x in binding['repos']:
 if x['name']=='tis_path':continue
 p=pathlib.Path(x['path'])
 for f in x['files']:
  fp=pathlib.Path(f['path'])
  if f.get('sha256') and fp.is_file():assert hashlib.sha256(fp.read_bytes()).hexdigest()==f['sha256']
for rel in ['pydim/dim/rt.py','pydim/dim/dbas.py','mquant/tis/hf/prel0/p1_product_receipt.py','mquant/tis/hf/prel0/p1_dba_export.py','mquant/tis/hf/prel0/wall_assembler_core.py','mquant/tis/test/integration/verify_eaw_p1_real_run.py','mquant/tis/test/integration/fixtures/eaw_p1_real_run.example.json','edh-universe/frp/frp/dbaw/Main.hs','edh-universe/frp/frp-core/src/Frp/Core/Fao/Class.hs','edh-universe/frp/frp-core/src/Frp/Core/Fao/Store/Class.hs','edh-universe/frp/frp-core/src/Frp/Apt/Time.hs','m3sof/settings/json.py','m3sof/settings/lib3.py','config.yml','run-python.sh','m3rc']:
 p=runner.BASE/rel;b=p.read_bytes();extra.append({'path':str(p),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'git_blob_sha1_of_worktree_bytes':hashlib.sha1(b'blob '+str(len(b)).encode()+b'\x00'+b).hexdigest()})
binding['additional_related_file_hashes']=extra;binding['final_readonly_audit']={'checked_at_utc':runner.utc(),'all_relevant_heads_and_statuses_unchanged':True,'source_file_hashes_unchanged':True,'repos':audit};(W/'WORKSPACE_BINDING.json').write_text(json.dumps(binding,ensure_ascii=False,indent=2)+'\n')
recs=[json.loads(line) for line in (W/'SAMPLE_CHAIN.jsonl').open()];end=recs[-1];print('END_SOURCE_BAND',{k:end['upstream_sparse_rows'][0]['payload'][k] for k in ('band_lo','band_hi','core_price')},'END_PRODUCT_BAND',{k:end['occurrence_payload'][k] for k in ('p1WallBandLow','p1WallBandHigh','p1WallCore')})
print('AUDIT',len(audit),'REPOS_UNCHANGED',True,'EXTRA_SOURCE_HASHES',len(extra));runner.guard()
