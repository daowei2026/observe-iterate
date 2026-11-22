from pathlib import Path
from datetime import datetime,timezone
import json,os,subprocess
R=Path(__file__).resolve().parent;BASE=Path('/dwdhome/fy/BASE_E6_2_copy')
command=['bash',str(BASE/'run-python.sh'),str(R/'final_script/run_definition.py'),'--output-html',str(R.parent/'caegraph-E/f800.html')]
state=dict(run_id='OI-F800-STAT-20261122-01',call_id='C0027',delegation_id='D012',attempt=2,command=command,cwd=str(BASE),env_override={'PYTHONDONTWRITEBYTECODE':'1'},started_at=datetime.now(timezone.utc).isoformat(),supervisor_pid=os.getpid(),status='STARTED',formal_feature_production_authorized=False)
def save():(R/'RUN_ATTEMPT02.json').write_text(json.dumps(state,ensure_ascii=False,indent=2)+'\n')
with (R/'RUN_ATTEMPT02.log').open('wb') as log:
 env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1');child=subprocess.Popen(command,cwd=BASE,env=env,stdout=log,stderr=subprocess.STDOUT);state['python_pid']=child.pid;save();code=child.wait()
state.update(exit_code=code,finished_at=datetime.now(timezone.utc).isoformat(),status='SUCCESS' if code==0 else 'FAILED');save();print(json.dumps(state,ensure_ascii=False));raise SystemExit(code)
