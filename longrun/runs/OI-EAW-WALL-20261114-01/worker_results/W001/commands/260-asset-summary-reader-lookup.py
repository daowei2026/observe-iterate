import pathlib,json,sys
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[1]));import runner
W=runner.W;j=json.loads((W/'evidence/WALL_ASSET_METADATA.json').read_text());print('PROBE_TOTALS',{k:v for k,v in j.items() if k!='assets'})
for a in j['assets']:
 print('SUMMARY',a['feature'],a['time_range_path'],'FILES',a['file_count'],'BYTES',a['total_file_bytes'],'STOP',a['stopped'])
 for leaf in a['leaf_parents']:
  fs=[f for f in a['files'] if f['path'].startswith(leaf+'/')];receipts=[f for f in fs if '/p1_receipts/' in f['path']];print('LEAF',leaf,'FILE_COUNT',len(fs),'SIZE',sum(f['bytes'] for f in fs))
  for f in receipts:print('RECEIPT',f['path'],json.dumps(f.get('json'),ensure_ascii=False))
  if a['feature']=='EawP1WallLifecycleFrp':
   for f in fs:print('PRODUCT_FILE',pathlib.Path(f['path']).relative_to(leaf),f['bytes'],f.get('sha256'))
runner.run('261-reader-types-symbols',['rg','-n','--max-count','25','class NormalField|adt_class|class DbaStore|class DbArray|P1WallOccurrenceStorage|P1WallCurrentStorage|MulWrap_P1Wall','mquant/frame/core','mquant/frame/lang/internal','pydim/dim'],timeout=15)
runner.run('262-ledger-heartbeat',[sys.executable,'-B','/home/dw/.agents/skills/long-task-status/scripts/task_status.py','heartbeat','--root',str(W),'--task-id','w001-local','--action','已定位当前 TIS/FRP 和真实旧 schema 物化资产；核验包装、只读解码边界','--next-action','区分版本差异，完成有界资产解码或明确停止'])
