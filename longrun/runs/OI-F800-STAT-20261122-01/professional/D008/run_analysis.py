"""D008生产后独立OnlyRead、原Skill全量G和原生AsOf复验。"""
from pathlib import Path
from datetime import datetime,timezone
import os,subprocess,json,time,sys
ROOT=Path(__file__).resolve().parent;BASE=ROOT.parents[2]
CLI='/home/dw/.agents/skills/long-task-status/scripts/task_status.py';TASK='oi-f800-stat-20261122-01-d008-e1'
def now():return datetime.now(timezone.utc).isoformat()
def status(*args):
 cp=subprocess.run(['python3',CLI,*args,'--root',str(BASE),'--task-id',TASK],capture_output=True,text=True)
 assert cp.returncode==0,cp.stderr
state=dict(started_at=now(),supervisor_pid=os.getpid(),completed=False,operations=[])
def save():(ROOT/'ANALYSIS_EXECUTION.json').write_text(json.dumps(state,ensure_ascii=False,indent=2)+'\n')
def command(name,*args,native=False):
 cmd=['bash','run-python.sh',str(ROOT/'run_in_runtime.py'),str(ROOT/(name+'.py')),*args] if native else ['python3',str(ROOT/(name+'.py')),*args]
 log=ROOT/(name+'.log'); stream=log.open('w')
 env=os.environ.copy();env['PYTHONDONTWRITEBYTECODE']='1'
 cp=subprocess.Popen(cmd,cwd=BASE,env=env,stdout=stream,stderr=subprocess.STDOUT)
 op=dict(script=name,command=cmd,pid=cp.pid,started_at=now(),log=str(log));state['operations'].append(op);save()
 return cp,op,stream
def wait(entries):
 last=time.monotonic()
 while any(p.poll() is None for p,op,f in entries):
  if time.monotonic()-last>=60:
   status('heartbeat','--action','独立读回或G脚本实际运行，PID和日志已记录','--next-action','当前子进程退出后核原生输出并接续')
   last=time.monotonic()
  time.sleep(0.5)
 for cp,op,f in entries:
  f.close();op.update(exit_code=cp.returncode,finished_at=now());save()
  assert cp.returncode==0,(op['script'],op['log'])
def run(name,*args,native=False):
 entry=command(name,*args,native=native);wait([entry])
try:
 prod=json.loads((ROOT/'PRODUCTION_PROCESS.json').read_text());assert prod['completed'] and prod['exit_code']==0
 status('update','--status','waiting_external','--action','新X已退出0，独立OnlyRead 31表及15表上游读回','--next-action','核全部身份和范围后进入G')
 wait([command('run_formal','--mode','read',native=True),command('extract_upstream',native=True)])
 status('update','--status','running','--clear-blocker','--action','独立读回进程退出0，绑定新结果','--next-action','G1-G8全量剖面')
 run('bind_result');state['g_workflow_started_at']=now();save();run('prepare_g_readiness')
 state['global_profile_started_at']=now();save()
 run('perform_global_profile');run('compare_versions','D005')
 # 同脚本第二次保留独立日志，不覆盖第一基线执行原件。
 (ROOT/'compare_versions.log').rename(ROOT/'compare_versions_be57.log');state['operations'][-1]['log']=str(ROOT/'compare_versions_be57.log');save()
 run('compare_versions','D002');(ROOT/'compare_versions.log').rename(ROOT/'compare_versions_ac.log');state['operations'][-1]['log']=str(ROOT/'compare_versions_ac.log');save()
 run('validate_missing_windows')
 status('update','--status','waiting_external','--action','全量剖面与双基线对照已生成，独立原生Life/AsOf复验','--next-action','核GF001/002及38个历史位置')
 run('verify_native_retest',native=True)
 status('update','--status','running','--clear-blocker','--action','原生AsOf复验完成，整理原Skill G原生合同和Gate','--next-action','验收全部剖面和回交')
 run('build_profile_package');run('validate_delivery')
 state.update(completed=True,global_profile_finished_at=now(),finished_at=now());save()
 status('step-complete','--step-id','profile','--evidence',str(ROOT/'WORKFLOW_COMPLETION.json'))
 status('step-start','--step-id','return','--action','D008新X/全量G已验收，准备发布专业结果和原V2 Return','--next-action','专业结果先发布读回，再发布C0019 Return')
except Exception as e:
 state.update(error=repr(e),failed_at=now());save()
 status('update','--status','running','--clear-blocker','--action','读回或G子步骤有失败，保留原件并核实','--next-action','修正分析脚本或如实报告真实阻断')
 raise
print('ANALYSIS_COMPLETED',now(),flush=True)
