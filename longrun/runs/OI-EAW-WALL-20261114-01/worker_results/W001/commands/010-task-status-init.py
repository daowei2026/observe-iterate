import sys,pathlib
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[1]));import runner
skill='/home/dw/.agents/skills/long-task-status/scripts/task_status.py';root=str(runner.W)
assert runner.run('011-ledger-init',[sys.executable,'-B',skill,'init','--root',root,'--plan',str(runner.W/'runtime/plan.json')])==0
assert runner.run('012-ledger-binding-start',[sys.executable,'-B',skill,'step-start','--root',root,'--task-id','w001-local','--step-id','binding-code','--action','已核真模型、cwd、thread、主控单写者锁；开始有界静态调查','--next-action','记录相关仓库 HEAD/dirty、精确源码与读取入口'])==0
