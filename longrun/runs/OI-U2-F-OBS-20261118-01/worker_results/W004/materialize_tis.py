from pathlib import Path
import datetime,hashlib,json,os,subprocess,time
r=Path(__file__).resolve().parent;tis=r/'source/mquant/tis'
def save(name,value):(r/name).write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n')
def inventory():
 result={}
 for root,dirs,files in os.walk(tis,topdown=True):
  dirs[:]=[d for d in dirs if not d.startswith(('.', '__'))]
  if '__init__.py' in files:
   p=Path(root)/'__init__.py';b=p.read_bytes();result[str(p.relative_to(tis))]={'path':str(p),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
 return result
assert json.loads((r/'tis_source_stage_report.json').read_text())['verification_passed']
assert not (r/'logs/tis_seed_inits.dispatch.json').exists(),'EFFECT_UNKNOWN: seeder dispatch already exists'
before=inventory();save('diagnostics/tis_inits.before.json',before)
seed=tis/'seed_inits.py';seed_hash=hashlib.sha256(seed.read_bytes()).hexdigest();assert seed_hash==next(x['sha256'] for x in json.loads((r/'tis_source_stage_report.json').read_text())['files'] if x['relative_path']=='seed_inits.py')
dispatch={'started_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'argv':['bash',str(r/'seed_tis.sh')],'cwd':str(tis),'seed_sha256':seed_hash}
with (r/'logs/tis_seed_inits.dispatch.json').open('x') as f:json.dump(dispatch,f,ensure_ascii=False,indent=2);f.write('\n')
env=os.environ.copy();env['PYTHONDONTWRITEBYTECODE']='1';tick=time.monotonic()
with (r/'logs/tis_seed_environment.log').open('xb') as log:p=subprocess.run(dispatch['argv'],cwd=tis,env=env,stdout=log,stderr=subprocess.STDOUT)
(r/'logs/tis_seed_inits.exit_code').write_text(str(p.returncode)+'\n')
after=inventory();save('diagnostics/tis_inits.after.json',after)
generated=[{'relative_path':name,**after[name]} for name in sorted(after.keys()-before.keys())]
existing_unchanged=all(name in after and after[name]==value for name,value in before.items())
diff=subprocess.check_output(['git','-C',str(tis),'diff','--binary','HEAD'],env=env);(r/'tis_business_source.diff').write_bytes(diff)
status=subprocess.check_output(['git','-C',str(tis),'status','--short'],env=env);(r/'logs/tis_after_seed_git_status.txt').write_bytes(status)
ok=p.returncode==0 and existing_unchanged and not diff and all(x['bytes']==0 and x['sha256']==hashlib.sha256(b'').hexdigest() for x in generated)
report={'run_id':'OI-U2-F-OBS-20261118-01','work_order_id':'W004','tis_commit':'2f460d663d821cf2ba25555eda13e78b697d0767','source_root':str(tis),'seeder':{'path':str(seed),'sha256':seed_hash,'exit_code':p.returncode,'attempt_count':1},'generated_count':len(generated),'generated':generated,'preexisting_init_count':len(before),'preexisting_inits_unchanged':existing_unchanged,'tracked_diff_bytes':len(diff),'only_missing_empty_inits_created':ok,'pretty_exports_executed':False,'elapsed_seconds':time.monotonic()-tick,'ended_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'status':'SUCCESS' if ok else 'BLOCKED'}
save('tis_generated_inits.json',report)
receipt=json.loads((r/'execution_receipt.json').read_text());receipt['phase']='TIS_PACKAGE_BOUNDARY_READY' if ok else 'TIS_PACKAGE_BOUNDARY_BLOCKED';save('execution_receipt.json',receipt)
print(json.dumps({'status':report['status'],'generated_count':len(generated),'seeder_exit_code':p.returncode,'tracked_diff_bytes':len(diff)},ensure_ascii=False))
raise SystemExit(0 if ok else 1)
