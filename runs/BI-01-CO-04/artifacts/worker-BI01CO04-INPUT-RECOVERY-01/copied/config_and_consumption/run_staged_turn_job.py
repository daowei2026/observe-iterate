from pathlib import Path
import json,subprocess,time,os,sys
from datetime import datetime,timezone
root=Path(__file__).resolve().parent;stage=root/"turn_staging"
sym=sys.argv[1];role=sys.argv[2]
assert sym in ['rb','hc','i'] and role in ['small','mid','big']
name=sym+"__"+role;state_path=stage/(name+".state.json");task_path=stage/(name+".task.json")
if state_path.exists():raise RuntimeError('已有执行收据，须先核查状态，禁止重复启动: '+str(state_path))
task=json.loads(task_path.read_text());app=Path(task['task_params']['app']['app_dir']);cfg=json.loads((app/'mquant/config/prod/sof/GTQH_L1_20210104_20240208.json').read_text())
assert all(Path(p).is_relative_to(stage) for p in cfg['store_dir'])
assert task['target']['target']['sym']==sym and task['target']['calendar']=='@'
assert task['task_params']['sof']['sof_name']=='GTQH_L1_20210104_20240208'
engine=json.loads((root/'generation_engine_readiness.json').read_text());assert engine['matches_verified_original_E_binary']
worker='/m3varK/workspace/mquant_e6.2_prod/edh-universe/frp/trade-poc/edh_modules/trade/frp/worker/one.edh'
command=[engine['path'],'--f='+worker,'--jp='+str(task_path)]
env=dict(os.environ,M3WORKS='/dwdhome/fy/BASE_E6_2',OMP_NUM_THREADS='1',OPENBLAS_NUM_THREADS='1',MKL_NUM_THREADS='1')
log=stage/(name+'.engine.log');started=time.monotonic()
with log.open('wb') as output:
 p=subprocess.Popen(command,cwd='/dwdhome/fy/BASE_E6_2',env=env,stdin=subprocess.DEVNULL,stdout=output,stderr=subprocess.STDOUT,start_new_session=True)
 state={'symbol':sym,'role':role,'state':'running','pid':p.pid,'command':command,'started_at':datetime.now(timezone.utc).isoformat(),'log':str(log),'formal_output_modified':False,'staging_cache_root':str(stage/'cache')}
 state_path.write_text(json.dumps(state,ensure_ascii=False,indent=2));print(json.dumps(state,ensure_ascii=False),flush=True)
 try:rc=p.wait(timeout=1800)
 except subprocess.TimeoutExpired:
  p.terminate();rc=p.wait(timeout=15);state['timed_out']=True
text=log.read_text(errors='replace')
state.update(returncode=rc,elapsed_seconds=time.monotonic()-started,state='generated_pending_readback' if rc==0 and 'Edh program crashed with an error:' not in text and 'time used:' in text else 'failed')
state_path.write_text(json.dumps(state,ensure_ascii=False,indent=2));print(json.dumps(state,ensure_ascii=False),flush=True)
if state['state']=='failed':print(text[-6000:],flush=True);sys.exit(1)
