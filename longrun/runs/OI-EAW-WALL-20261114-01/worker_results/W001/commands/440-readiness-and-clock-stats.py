import pathlib,sys,json,math,datetime,hashlib
W=pathlib.Path(__file__).resolve().parents[1];sys.path.insert(0,str(W));from bounded_dba_reader import BudgetReader
j=json.loads((W/'evidence/WALL_ASSET_METADATA.json').read_text());r=BudgetReader(byte_limit=3*1024*1024,seconds=18,file_limit=55);out=[]
def iso(v):
 q,ns=divmod(v,10**9);return datetime.datetime.fromtimestamp(q,datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%S')+f'.{ns:09d}Z'
for a in j['assets']:
 if a['feature']!='EawP1WallLifecycleFrp':continue
 leaf=pathlib.Path(a['leaf_parents'][0]);row={'source_leaf':str(leaf),'time_range_path':a['time_range_path'],'mode':'historical materialized physical DBA; not current canonical schema','streams':{}}
 for event,record,local in [('wall_occurrences','P1WallOccurrenceStorage','p1WallOccurrenceLocalNo'),('wall_current_view','P1WallCurrentStorage','p1WallCurrentLocalNo'),('wall_diagnostics','P1DiagnosticStorage',None)]:
  ts=leaf/(event+'.__ts__.dba');h=r.file(ts);root=leaf/event
  if '2020-12-01' in a['path']:
   tss=r.array(ts,'Q');time_fact={'scope':'full short-window physical firing timestamp column','min_raw':min(tss) if tss else None,'max_raw':max(tss) if tss else None,'min_utc':iso(min(tss)) if tss else None,'max_utc':iso(max(tss)) if tss else None,'monotonic_non_decreasing':all(x<=y for x,y in zip(tss,tss[1:])),'zero_timestamps':tss.count(0)}
  else:
   ends=[r.scalar(ts,i,'Q') for i in (0,h['n']-1)] if h['n'] else [];time_fact={'scope':'first/last only; global min/max not asserted','first_utc':iso(ends[0]) if ends else None,'last_utc':iso(ends[-1]) if ends else None,'first_raw':ends[0] if ends else None,'last_raw':ends[-1] if ends else None}
  x={'firing_count':h['n'],'time':time_fact,'actual_time':None,'confirm_time':None,'known_time':None,'time_role_reason':'physical writer trigger timestamps only; distinct actual/confirm/known columns absent in this legacy layout'}
  anchor=root/('['+record+']')/'anchor.dba';ha=r.file(anchor);x['list_record_count']=r.scalar(anchor,ha['n']-1) if ha['n'] else 0;x['anchor_event_count_matches']=ha['n']==h['n']
  if local:
   lp=root/('['+record+']')/(local+'::Int64.dba');hl=r.file(lp);x['numeric_record_count']=hl['n'];x['anchor_last_matches_numeric_records']=x['list_record_count']==hl['n']
   if '2020-12-01' in a['path']:
    ids=r.array(lp);x['local_no_stats']={'min':min(ids),'max':max(ids),'distinct':len(set(ids)),'zero_count':ids.count(0),'negative_count':sum(v<0 for v in ids)}
  if event=='wall_occurrences' and '2020-12-01' in a['path']:
   rp=root/'[P1WallOccurrenceStorage]';vals=r.array(rp/'p1WallLifecycleOccurredAt::Int.dba');x['occurred_at_raw_stats']={'min':min(vals),'max':max(vals),'zero_count':vals.count(0),'reason':'stored Int field; sample joins upstream uti, do not relabel as epoch time'}
   x['float_columns']={}
   for col in ('p1WallCore','p1WallBandLow','p1WallBandHigh'):
    vals=r.array(rp/(col+'::Double.dba'),'d');finite=[v for v in vals if math.isfinite(v)];x['float_columns'][col]={'count':len(vals),'nan_count':sum(math.isnan(v) for v in vals),'infinite_count':sum(math.isinf(v) for v in vals),'min_finite':min(finite) if finite else None,'max_finite':max(finite) if finite else None,'zero_count':vals.count(0.0)}
  row['streams'][event]=x
 out.append(row);print(json.dumps(row,ensure_ascii=False,indent=2))
budget=r.summary();r.close();result={'assets':out,'read_budget':budget,'text_null_scope':'only sampled values in SHORT_WINDOW_PHYSICAL_PROBE; global text null count unknown'};(W/'evidence/PHYSICAL_DATA_STATS.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n');print('READ_BYTES',budget['bytes_read'])
