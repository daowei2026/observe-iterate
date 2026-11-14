import pathlib,json,sys,bisect,datetime,hashlib
W=pathlib.Path(__file__).resolve().parents[1];sys.path.insert(0,str(W));from bounded_dba_reader import BudgetReader
j=json.loads((W/'evidence/WALL_ASSET_METADATA.json').read_text());prod=next(a for a in j['assets'] if a['feature']=='EawP1WallLifecycleFrp' and '2020-12-01' in a['path']);leaf=pathlib.Path(prod['leaf_parents'][0]);up=next(a for a in j['assets'] if a['feature']=='WallAssembler' and '2020-12-01' in a['path']);up_leaf=pathlib.Path(up['leaf_parents'][0]);receipt=next(f['json'] for f in up['files'] if f['path']==str(up_leaf/'p1_receipts/wall_lifecycle.json'));fields=next(f['json'] for f in up['files'] if f['path']==str(up_leaf/'fields.json'));r=BudgetReader(byte_limit=4*1024*1024,seconds=18,file_limit=90)
def iso(v):
 q,ns=divmod(v,10**9);return datetime.datetime.fromtimestamp(q,datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%S')+f'.{ns:09d}Z'
def event_rows(ev,record,localkey):
 root=leaf/ev;ids=r.array(root/('['+record+']')/(localkey+'::Int64.dba'));anchors=r.array(root/('['+record+']')/'anchor.dba');tss=r.array(leaf/(ev+'.__ts__.dba'),'Q');assert len(anchors)==len(tss) and anchors[-1]==len(ids) and all(x<=y for x,y in zip(anchors,anchors[1:]));return root,ids,anchors,tss
oroot,oids,oa,ots=event_rows('wall_occurrences','P1WallOccurrenceStorage','p1WallOccurrenceLocalNo');croot,cids,ca,cts=event_rows('wall_current_view','P1WallCurrentStorage','p1WallCurrentLocalNo');dtss=r.array(leaf/'wall_diagnostics.__ts__.dba','Q');assert all(x<=y for x,y in zip(ots,ots[1:])) and all(x<=y for x,y in zip(cts,cts[1:]))
local_no=oids[0];selected=[i for i,x in enumerate(oids) if x==local_no];assert 1<=len(selected)<=12
sparse_id=r.array(up_leaf/'wall_assembler_sparse_events.wall_id.dba');sparse_indices=[i for i,v in enumerate(sparse_id) if v==local_no];assert len(sparse_indices)<=24
sparse=[]
for idx in sparse_indices:
 row={'physical_row':idx,'result_key':'wall_assembler_sparse_events','source_directory':str(up_leaf),'payload':{}}
 for col,dt in fields['wall_assembler_sparse_events'].items():
  fmt='b' if dt in ('i1','int8') else 'd' if dt in ('f8','float64') else 'q';value=r.scalar(up_leaf/('wall_assembler_sparse_events.'+col+'.dba'),idx,fmt);row['payload'][col]=value
 sparse.append(row)
records=[]
for i in selected:
 eidx=bisect.bisect_right(oa,i);assert eidx<len(ots);timestamp=ots[eidx];vals={}
 for f in prod['files']:
  p=pathlib.Path(f['path'])
  if p.parent==oroot/'[P1WallOccurrenceStorage]' and p.name!='anchor.dba':
   key=p.name.split('::')[0];fmt='d' if '::Double' in p.name else 'q';v=r.scalar(p,i,fmt);vals[key]=r.text(oroot,v) if '::Text$Data.Text' in p.name else v
 curr=[]
 for ci in range(bisect.bisect_left(cts,timestamp),bisect.bisect_right(cts,timestamp)):
  lo=ca[ci-1] if ci else 0;hi=ca[ci]
  for vi in range(lo,hi):
   if cids[vi]==local_no:
    v=r.scalar(croot/'[P1WallCurrentStorage]/p1WallCurrentState::Text$Data.Text.dba',vi);curr.append({'physical_value_row':vi,'physical_firing_row':ci,'p1WallCurrentLocalNo':cids[vi],'p1WallCurrentState':r.text(croot,v),'writer_trigger_epoch_ns':timestamp})
 matching=[x for x in sparse if x['payload'].get('uti')==vals['p1WallLifecycleOccurredAt']]
 packed=[]
 for stream in ('wall__stream','wall__stream__occ0001','wall__stream__occ0002'):
  if stream not in fields:continue
  upath=up_leaf/(stream+'.uti.dba');uv=r.array(upath);locs=[k for k,x in enumerate(uv) if x==vals['p1WallLifecycleOccurredAt']]
  for pi in locs:
   if r.scalar(up_leaf/(stream+'.wall_id.dba'),pi)==local_no:
    pay={}
    for col,dt in fields[stream].items():
     fmt='b' if dt in ('i1','int8') else 'd' if dt in ('f8','float64') else 'q';pay[col]=r.scalar(up_leaf/(stream+'.'+col+'.dba'),pi,fmt)
    packed.append({'result_key':stream,'physical_row':pi,'payload':pay})
 # Exact seeks in upstream trace; binary-search result accepted only after equality check.
 trace_path=up_leaf/'wall_assembler_state_trace.uti.dba';h=r.file(trace_path);left=0;right=h['n'];target=vals['p1WallLifecycleOccurredAt']
 for _ in range(48):
  if left>=right:break
  mid=(left+right)//2;v=r.scalar(trace_path,mid)
  if v<target:left=mid+1
  else:right=mid
 trace=None
 if left<h['n'] and r.scalar(trace_path,left)==target:
  pay={}
  for col,dt in fields['wall_assembler_state_trace'].items():
   fmt='b' if dt in ('i1','int8') else 'd' if dt in ('f8','float64') else 'q';pay[col]=r.scalar(up_leaf/('wall_assembler_state_trace.'+col+'.dba'),left,fmt)
  trace={'physical_row':left,'source_directory':str(up_leaf),'result_key':'wall_assembler_state_trace','payload':pay,'lookup_method':'bounded binary seek then exact uti equality; no absence claim from failed seek'}
 record={'sample_status':'REAL_LOCAL_LEGACY_PHYSICAL_SAMPLE','source_partition':str(leaf),'source_fields_sha256':next(f['sha256'] for f in prod['files'] if f['path']==str(leaf/'fields.json')),'identity':{'upstream_artifact_location':str(up_leaf),'local_wall_no_observed':local_no,'target':receipt['source_scope']['target'],'calendar':receipt['source_scope']['calendar_or_session'],'canonical_current_FeatureRunIdentity':None,'reason':'legacy stored shape lacks current canonical run identity; no business identity fabricated'},'version':{'upstream_receipt_code_version':receipt['code_version'],'upstream_receipt_schema_version':receipt['schema_version'],'product_shape':'MulWrap P1WallOccurrenceStorage / P1WallCurrentStorage / P1DiagnosticStorage','product_generation_code_version':None,'reason':'product receipt/manifests not found in this leaf; current HEAD not assigned as generation version'},'physical_firing_row':eidx,'physical_value_row':i,'writer_trigger_epoch_ns':timestamp,'writer_trigger_epoch_iso_z':iso(timestamp),'occurrence_payload':vals,'current_updates_at_same_firing':curr,'diagnostics_at_same_firing':{'count':dtss.count(timestamp),'identity_specific':False,'reason':'legacy diagnostics have no direct Wall identity field; only firing equality checked'},'upstream_sparse_rows':matching,'upstream_packed_rows':packed,'upstream_state_trace':trace,'frp_active_map':None,'frp_active_map_reason':'not persisted in the three writer files; upstream WallAssembler trace is distinct','actual_time':None,'confirm_time':None,'known_time':None,'time_role_reason':'stored trigger and uti retained; no distinct roles inferred'}
 records.append(record);print('CHAIN_RECORD',i,'UTI',target,'KIND',vals.get('p1WallLifecycleChangeKind'),'CURRENT',curr,'SPARSE',len(matching),'PACKED',len(packed),'TRACE',trace is not None)
budget=r.summary();assert all(x['unchanged_size_and_mtime'] for x in budget['files']);r.close()
with (W/'SAMPLE_CHAIN.jsonl').open('x') as f:
 for v in records:f.write(json.dumps(v,ensure_ascii=False,allow_nan=False)+'\n')
(W/'evidence/SAMPLE_CHAIN_EXTRACTION.json').write_text(json.dumps({'records':len(records),'local_no':local_no,'selected_indices':selected,'upstream_sparse_matching_wall_rows':len(sparse),'read_budget':budget,'real_data_only':True},ensure_ascii=False,indent=2)+'\n')
print('READ_BYTES',budget['bytes_read'],'SAMPLE_RECORDS',len(records))
