import pathlib,json,sys,datetime
W=pathlib.Path(__file__).resolve().parents[1];sys.path.insert(0,str(W));from bounded_dba_reader import BudgetReader
j=json.loads((W/'evidence/WALL_ASSET_METADATA.json').read_text());a=next(a for a in j['assets'] if a['feature']=='EawP1WallLifecycleFrp' and '2020-12-01' in a['path']);leaf=pathlib.Path(a['leaf_parents'][0]);r=BudgetReader(byte_limit=512*1024,seconds=15);observed=[]
for event,record in [('wall_occurrences','P1WallOccurrenceStorage'),('wall_current_view','P1WallCurrentStorage'),('wall_diagnostics','P1DiagnosticStorage')]:
 root=leaf/event;row={'event':event,'source':str(root),'fields':{},'timestamps_raw':[]}
 ts=leaf/(event+'.__ts__.dba');h=r.file(ts);row['firing_count']=h['n'];row['timestamps_raw']=[r.scalar(ts,i,'Q') for i in range(min(3,h['n']))]
 for f in a['files']:
  p=pathlib.Path(f['path'])
  if str(p.parent)==str(root/('['+record+']')) and p.name!='anchor.dba':
   h=r.file(p);fmt='d' if '::Double' in p.name else 'q';vals=[r.scalar(p,i,fmt) for i in range(min(3,h['n']))]
   if '::Text$Data.Text' in p.name:
    try:vals=[{'text_index':v,'text':r.text(root,v)} for v in vals]
    except Exception as e:vals={'raw':vals,'decode_error':str(e)}
   row['fields'][p.name]={'row_count':h['n'],'first_three':vals}
 print(json.dumps(row,ensure_ascii=False,indent=2));observed.append(row)
result={'source_leaf':str(leaf),'method':'read-only little-endian DBA scalar seeks; no project imports; literal physical field names; time units not inferred','observed':observed,'read_budget':r.summary()};r.close();(W/'evidence/SHORT_WINDOW_PHYSICAL_PROBE.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print('READ_BUDGET',result['read_budget']['bytes_read'])
