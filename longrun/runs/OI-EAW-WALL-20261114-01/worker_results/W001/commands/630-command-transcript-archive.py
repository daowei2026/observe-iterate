import pathlib,json,os,datetime
W=pathlib.Path(__file__).resolve().parents[1];tid=os.environ['CODEX_THREAD_ID'];p=next(pathlib.Path('/home/dw/.codex/sessions/2026/11/14').glob('*'+tid+'*.jsonl'));assert p.stat().st_size<16*1024*1024
rows=[];patches=[]
for line in p.open():
 x=json.loads(line);v=x.get('payload',{})
 if x.get('type')=='event_msg' and isinstance(v,dict) and v.get('type')=='item_completed' and v.get('item',{}).get('type')=='CommandExecution':rows.append(x)
 if x.get('type')=='response_item' and isinstance(v,dict) and v.get('type')=='custom_tool_call' and 'tools.apply_patch(' in v.get('input',''):patches.append({'timestamp':x['timestamp'],'type':'file_mutation_tool_call','call_id':v.get('call_id'),'input':v['input']})
with (W/'evidence/ALL_SHELL_COMMAND_EVENTS.jsonl').open('x') as f:
 for x in rows:f.write(json.dumps(x,ensure_ascii=False)+'\n')
with (W/'evidence/FILE_MUTATION_TOOL_CALLS.jsonl').open('x') as f:
 for x in patches:f.write(json.dumps(x,ensure_ascii=False)+'\n')
with (W/'COMMAND_LOG.txt').open('a') as f:
 f.write('\nCOMPLETE_SHELL_TOOL_ARCHIVE '+str(W/'evidence/ALL_SHELL_COMMAND_EVENTS.jsonl')+'\n')
 for i,x in enumerate(rows):
  v=x['payload'];item=v['item'];f.write('TOOL_COMMAND '+json.dumps({'archive_row':i,'started_at_ms':v.get('started_at_ms'),'completed_at_ms':v.get('completed_at_ms'),'command':item.get('command'),'cwd':item.get('cwd'),'exit_code':item.get('exit_code'),'status':item.get('status'),'duration':item.get('duration')},ensure_ascii=False)+'\n')
 f.write('FILE_MUTATION_TOOL_ARCHIVE '+str(W/'evidence/FILE_MUTATION_TOOL_CALLS.jsonl')+'\nOnly command/file tool evidence copied; no reasoning, credentials or unrelated chat bodies. Commands after archive cutoff have runner receipts; final sealing command has its own explicit receipt.\n')
print(json.dumps({'shell_events':len(rows),'file_tool_calls':len(patches),'session_bytes_read':p.stat().st_size,'scope':'only this physical thread; tool command/file-write evidence, no reasoning copied'},ensure_ascii=False))
