from pathlib import Path
import datetime, hashlib, json, os, subprocess, time
run=Path(__file__).resolve().parent
obs=run/'source/observe-iterate';tis=run/'source/mquant/tis'
obs_commit='f4f0e4b276b1118b779473c1fbe462bc7a64b358';tis_commit='2f460d663d821cf2ba25555eda13e78b697d0767'
env=os.environ.copy();env.update({'GIT_TERMINAL_PROMPT':'0','PYTHONDONTWRITEBYTECODE':'1','TMPDIR':str(run/'cache/tmp'),'XDG_CACHE_HOME':str(run/'cache/xdg')})
def now():return datetime.datetime.now(datetime.timezone.utc).isoformat()
def save(name,obj):(run/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
def stage(name,root,remote,commit,fetchspec,required):
 if root.exists():raise RuntimeError('EFFECT_UNKNOWN: source already exists: '+str(root))
 root.parent.mkdir(parents=True,exist_ok=True)
 report={'run_id':'OI-U2-F-OBS-20261118-01','work_order_id':'W004','repository':name,'remote_url':remote,'requested_commit':commit,'actual_head':None,'source_root':str(root),'created_or_reused':'created','started_at':now(),'steps':[],'files':[],'status':'BLOCKED'}
 commands=[['git','init',str(root)],['git','-C',str(root),'remote','add','origin',remote],['git','-C',str(root),'-c','protocol.version=2','fetch','--filter=blob:none','--no-tags','origin',fetchspec],['git','-C',str(root),'checkout','--detach',commit]]
 code=0
 with (run/('logs/'+name+'_source_stage.log')).open('xb') as log:
  for argv in commands:
   at=now();tick=time.monotonic();log.write(('COMMAND '+json.dumps(argv)+'\n').encode());log.flush()
   p=subprocess.run(argv,env=env,cwd=run,stdout=log,stderr=subprocess.STDOUT)
   step={'argv':argv,'started_at':at,'ended_at':now(),'elapsed_seconds':time.monotonic()-tick,'exit_code':p.returncode};report['steps'].append(step);print(json.dumps(step),flush=True)
   if p.returncode:
    code=p.returncode;report['blocker']='Source staging command failed: '+json.dumps(argv);break
  if code==0:
   report['actual_head']=subprocess.check_output(['git','-C',str(root),'rev-parse','HEAD'],text=True,env=env).strip()
   report['detached_head']=subprocess.run(['git','-C',str(root),'symbolic-ref','-q','HEAD'],env=env,stdout=log,stderr=subprocess.STDOUT).returncode==1
   for rel in required:
    p=root/rel;b=p.read_bytes() if p.is_file() else None
    report['files'].append({'relative_path':rel,'path':str(p),'exists':b is not None,'bytes':None if b is None else len(b),'sha256':None if b is None else hashlib.sha256(b).hexdigest()})
   report['verification_passed']=report['actual_head']==commit and report['detached_head'] and all(x['exists'] for x in report['files'])
   if not report['verification_passed']:code=1;report['blocker']='Locked source verification failed'
   status=subprocess.check_output(['git','-C',str(root),'status','--short'],text=True,env=env)
   (run/('logs/'+name+'_initial_git_status.txt')).write_text(status)
   report['initial_git_status_clean']=status==''
 report['status']='SUCCESS' if code==0 else 'BLOCKED';report['ended_at']=now()
 save(name+'_source_stage_report.json',report);(run/('logs/'+name+'_source_stage.exit_code')).write_text(str(code)+'\n')
 if code:raise SystemExit(code)
 return report
stage('observe_iterate',obs,'https://github.com/daowei2026/observe-iterate.git',obs_commit,'refs/heads/runs/OI-U2-F-OBS-20261118-01:refs/remotes/origin/run',['longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/D/u2_f_caegraph_definition.py','longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/C/caegraph_display.py','longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/C/caegraph_display_preview.html'])
stage('tis',tis,'https://github.com/daowei2026/tis.git',tis_commit,tis_commit,['README.md','seed_inits.py','frp/fqv_kline_example.py','frp/CommonPriceTurnGroupCandidates.py','frp/PostTurnGroupDirectionalOrganization.py','frp/CommonTurnGroupValidity.py','frpExample/Wave.py','frpExample/STCalendar.py','frpExample/ScaleTurn.py'])
receipt=json.loads((run/'execution_receipt.json').read_text());receipt['phase']='LOCKED_SOURCES_STAGED';save('execution_receipt.json',receipt)
print('LOCKED_SOURCES_STAGED',flush=True)
