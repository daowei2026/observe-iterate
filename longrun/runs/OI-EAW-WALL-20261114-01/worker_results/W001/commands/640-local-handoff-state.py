import sys,pathlib,json,hashlib,datetime
W=pathlib.Path(__file__).resolve().parents[1];sys.path.insert(0,str(W));import runner
required=['WORKER_EXECUTION_REPORT.md','WORKSPACE_BINDING.json','CODE_AND_READER_ENTRYPOINTS.md','ASSET_INVENTORY.json','SAMPLE_CHAIN.jsonl','SAMPLE_CHAIN_README.md','ACTION_PREFLIGHT_FACTS.md','WORKER_RETURN_PREPARATION.json','VALIDATION_REPORT.json']
for n in required:assert (W/n).is_file() and (W/n).stat().st_size>0
assert json.loads((W/'WORKSPACE_BINDING.json').read_text())['final_readonly_audit']['all_relevant_heads_and_statuses_unchanged']
runner.guard()
s='/home/dw/.agents/skills/long-task-status/scripts/task_status.py';common=['--root',str(W),'--task-id','w001-local']
for label,args in [('641-delivery-complete',['step-complete',*common,'--step-id','delivery','--evidence',str(W/'WORKER_EXECUTION_REPORT.md'),'--evidence',str(W/'VALIDATION_REPORT.json'),'--message','本地原件已齐、物理对账及JSON验证通过；下一条封包命令生成最终映射和hash并核验，不含GitHub或正式Return完成']),('642-local-stage-finish',['finish',*common,'--status','completed','--action','本地原件交付阶段结束；W001本身为PARTIAL，等待主控先发布证据后回准确refs，由原W1补正式Return回E1','--evidence',str(W/'WORKER_RETURN_PREPARATION.json'),'--evidence',str(W/'WORKER_EXECUTION_REPORT.md')])]:
 assert runner.run(label,[sys.executable,'-B',s,*args])==0
print('LOCAL_LEDGER_COMPLETE_ONLY; NEXT: final byte hash seal; NO BUSINESS COMPLETION')
