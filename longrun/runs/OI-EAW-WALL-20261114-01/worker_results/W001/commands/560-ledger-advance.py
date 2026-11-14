import sys,pathlib
W=pathlib.Path(__file__).resolve().parents[1];sys.path.insert(0,str(W));import runner
s='/home/dw/.agents/skills/long-task-status/scripts/task_status.py';common=['--root',str(W),'--task-id','w001-local']
for label,args in [('561-binding-complete',['step-complete',*common,'--step-id','binding-code','--evidence',str(W/'WORKSPACE_BINDING.json')]),('562-assets-start',['step-start',*common,'--step-id','assets','--action','读取真实短窗 DBA 局部链并登记 schema/version 缺口','--next-action','完成库存、预检和样本说明']),('563-assets-complete',['step-complete',*common,'--step-id','assets','--evidence',str(W/'evidence/WALL_ASSET_METADATA.json'),'--evidence',str(W/'SAMPLE_CHAIN.jsonl')]),('564-delivery-start',['step-start',*common,'--step-id','delivery','--action','编制完整报告、库存、发布映射和哈希；只结束本地阶段','--next-action','验证原件后交主控发布，待真实 refs 再生成正式 Return'])]:
 assert runner.run(label,[sys.executable,'-B',s,*args])==0
