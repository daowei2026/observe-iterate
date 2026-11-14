import pathlib,json,struct,time
W=pathlib.Path(__file__).resolve().parents[1];j=json.loads((W/'evidence/WALL_ASSET_METADATA.json').read_text());rs=[];start=time.monotonic()
selected=[x for a in j['assets'] if a['feature']=='EawP1WallLifecycleFrp' for x in a['files'] if x['path'].endswith('.dba')]
selected += [x for a in j['assets'] if a['feature']=='WallAssembler' and '2020-12-01' in a['path'] for x in a['files'] if 'wall_assembler_sparse_events.' in x['path'] and x['path'].endswith('.dba')]
with (W/'evidence/DBA_HEADERS_BOUNDED.jsonl').open('x') as out:
 for x in selected[:110]:
  if time.monotonic()-start>19:print('STOPPED_FOR_COST 19s');break
  p=pathlib.Path(x['path'])
  with p.open('rb') as f:b=f.read(24)
  v,o,z,a,n=struct.unpack('<iiiiq',b);r={'path':str(p),'bytes':x['bytes'],'layout_version':v,'data_offset':o,'item_size':z,'item_alignment':a,'row_count':n,'capacity':(x['bytes']-o)//z if z>0 else None,'header_valid':v==0 and o==64 and z>0 and n>=0 and o+n*z<=x['bytes']};rs.append(r);out.write(json.dumps(r,ensure_ascii=False)+'\n');out.flush()
  if '.__ts__.' in p.name or 'LocalNo' in p.name or 'anchor.dba'==p.name:print('KEY_HEADER',json.dumps(r,ensure_ascii=False),flush=True)
print('TOTAL',len(rs),'SELECTED',len(selected),'ELAPSED',time.monotonic()-start,'INVALID',sum(not r['header_valid'] for r in rs))
