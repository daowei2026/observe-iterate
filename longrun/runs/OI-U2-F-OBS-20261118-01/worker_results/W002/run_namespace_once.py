from pathlib import Path
import datetime,json,os,shutil,subprocess,time
run=Path(__file__).resolve().parent
if (run/'logs/private_shm_mount.started.json').exists(): raise SystemExit('EFFECT_UNKNOWN: namespace action already has a receipt; no repeat')
for name in ('tmp','xdg','numba','matplotlib'):
 (run/'runtime'/name).mkdir(exist_ok=True)
versions={}
for tool in ('unshare','mount','findmnt'):
 executable=shutil.which(tool)
 result=subprocess.run([executable,'--version'],stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True) if executable else None
 versions[tool]={'executable':executable,'exit_code':result.returncode if result else None,'version_output':result.stdout if result else None}
(run/'tool_versions.json').write_text(json.dumps(versions,ensure_ascii=False,indent=2)+'\n')
command=[versions['unshare']['executable'],'--user','--map-root-user','--mount','--fork','/bin/bash',str(run/'private_shm_episode.sh'),str(run)]
assert '--pid' not in command
started=datetime.datetime.now(datetime.timezone.utc).isoformat(); tick=time.monotonic()
receipt={'run_id':'OI-U2-F-OBS-20261118-01','work_order_id':'W002','started_at':started,'argv':command,'namespace_attempt':1,'uses_pid_namespace':False,'cwd':str(run/'source/observe-iterate')}
with (run/'logs/private_shm_mount.started.json').open('x') as stream: json.dump(receipt,stream,ensure_ascii=False,indent=2)
env=os.environ.copy(); env['PYTHONDONTWRITEBYTECODE']='1'
with (run/'logs/private_shm_mount.log').open('xb') as log:
 result=subprocess.run(command,cwd=run/'source/observe-iterate',env=env,stdout=log,stderr=subprocess.STDOUT)
finished={'finished_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-tick,'exit_code':result.returncode,'time_precision':'exact'}
(run/'logs/private_shm_mount.finished.json').write_text(json.dumps(finished,indent=2)+'\n')
(run/'logs/private_shm_mount.exit_code').write_text(str(result.returncode)+'\n')
alias=run/'logs/private_shm_mount.alias_report.json'
probe_exit=run/'logs/semlock_probe.exit_code'
d_started=run/'logs/w2_run.started.json'
entered=(run/'logs/private_shm_mount.inner_entered').exists()
report={'run_id':'OI-U2-F-OBS-20261118-01','work_order_id':'W002','status':'SUCCESS' if result.returncode==0 else 'BLOCKED','argv':command,'namespace_attempt_count':1,'uses_pid_namespace':False,'namespace_inner_entered':entered,'requested_alias':'/dev/shm','requested_backing':str(run/'runtime/shm'),'alias_proven':json.loads(alias.read_text())['verified'] if alias.exists() else False,'mount_log':str(run/'logs/private_shm_mount.log'),'namespace_exit_code':result.returncode,'started_at':started,**finished,'semlock_probe_attempt_count':1 if probe_exit.exists() else 0,'semlock_probe_exit_code':int(probe_exit.read_text()) if probe_exit.exists() else None,'D_attempt_count':1 if d_started.exists() else 0,'D_exit_code':int((run/'logs/w2_run.exit_code').read_text()) if (run/'logs/w2_run.exit_code').exists() else None,'host_shm_write_fallback':False,'platform_patched':False}
if result.returncode and not entered:
 report['first_blocker']='Private user + mount namespace creation failed before inner script entry: '+(run/'logs/private_shm_mount.log').read_text().strip()
elif result.returncode:
 report['first_blocker']='See exact inner episode log and last completed receipt; D/probe counts are recorded separately'
(run/'private_shm_report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(report,ensure_ascii=False,indent=2),flush=True)
print('PRIVATE_SHM_LOG_BODY:',flush=True)
print((run/'logs/private_shm_mount.log').read_text(),flush=True)
raise SystemExit(result.returncode)
