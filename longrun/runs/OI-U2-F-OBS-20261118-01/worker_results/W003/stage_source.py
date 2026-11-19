from pathlib import Path
import datetime,json,os,subprocess,time
run=Path(__file__).resolve().parent; source=run/'source/observe-iterate'
commit='f4f0e4b276b1118b779473c1fbe462bc7a64b358'; remote='https://github.com/daowei2026/observe-iterate.git'
d=source/'longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/D/u2_f_caegraph_definition.py'
c=source/'longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/C/caegraph_display.py'
if source.exists(): raise SystemExit('EFFECT_UNKNOWN: existing W003 source; no repeat staging')
report={'run_id':'OI-U2-F-OBS-20261118-01','work_order_id':'W003','remote_url':remote,'requested_commit':commit,'actual_head':None,'source_root':str(source),'D_script_path':str(d),'C3_path':str(c),'created_or_reused':'created','started_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'steps':[]}
env=os.environ.copy(); env['GIT_TERMINAL_PROMPT']='0'; env['PYTHONDONTWRITEBYTECODE']='1'
commands=[['git','init',str(source)],['git','-C',str(source),'remote','add','origin',remote],['git','-C',str(source),'-c','protocol.version=2','fetch','--filter=blob:none','--no-tags','origin','refs/heads/runs/OI-U2-F-OBS-20261118-01:refs/remotes/origin/run'],['git','-C',str(source),'checkout','--detach',commit]]
code=0
with (run/'logs/source_stage.log').open('xb') as log:
 for command in commands:
  started=datetime.datetime.now(datetime.timezone.utc).isoformat(); tick=time.monotonic()
  log.write(('COMMAND '+json.dumps(command)+'\n').encode()); log.flush()
  result=subprocess.run(command,env=env,cwd=run,stdout=log,stderr=subprocess.STDOUT)
  item={'argv':command,'started_at':started,'ended_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-tick,'exit_code':result.returncode}
  report['steps'].append(item); print(json.dumps(item),flush=True)
  if result.returncode: code=result.returncode; report['blocker']='Git command failed: '+json.dumps(command); break
 if code==0:
  report['actual_head']=subprocess.check_output(['git','-C',str(source),'rev-parse','HEAD'],env=env,text=True).strip()
  symbolic=subprocess.run(['git','-C',str(source),'symbolic-ref','-q','HEAD'],env=env,stdout=log,stderr=subprocess.STDOUT)
  report['detached_head']=symbolic.returncode==1; report['D_exists']=d.is_file(); report['C3_exists']=c.is_file()
  report['verification_passed']=report['actual_head']==commit and report['detached_head'] and report['D_exists'] and report['C3_exists']
  if not report['verification_passed']: code=1; report['blocker']='Source staging verification failed'
report['status']='SUCCESS' if code==0 else 'BLOCKED'; report['ended_at']=datetime.datetime.now(datetime.timezone.utc).isoformat()
(run/'source_stage_report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
(run/'logs/source_stage.exit_code').write_text(str(code)+'\n')
print('SOURCE_STAGE_STATUS='+report['status'],flush=True)
raise SystemExit(code)
