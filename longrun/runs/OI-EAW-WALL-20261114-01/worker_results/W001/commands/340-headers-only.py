import pathlib,json,struct
W=pathlib.Path(__file__).resolve().parents[1];j=json.loads((W/'evidence/WALL_ASSET_METADATA.json').read_text());headers=[]
for a in j['assets']:
 for x in a['files']:
  p=pathlib.Path(x['path'])
  if p.suffix!='.dba':continue
  with p.open('rb') as f:b=f.read(24)
  r={'path':str(p),'bytes':x['bytes'],'feature':a['feature'],'time_range_path':a['time_range_path']}
  if len(b)==24:
   version,offset,itemsize,alignment,n=struct.unpack('<iiiiq',b);valid=version==0 and offset==64 and itemsize>0 and alignment>0 and n>=0 and offset+n*itemsize<=x['bytes'];r.update({'layout_version':version,'offset':offset,'item_size':itemsize,'item_align':alignment,'row_count':n,'capacity':(x['bytes']-offset)//itemsize if itemsize>0 else None,'header_valid':valid})
  else:r.update({'header_valid':False,'reason':'short header'})
  headers.append(r)
  if a['feature']=='EawP1WallLifecycleFrp' and ('2020-12-01' in a['path'] or p.name.endswith('__ts__.dba')):print('HEADER',json.dumps(r,ensure_ascii=False))
(W/'evidence/DBA_HEADERS.json').write_text(json.dumps({'method':'24-byte <iiiiq header only, per pydim/dim/rt.py:69-93; no payload import','headers':headers},ensure_ascii=False,indent=2)+'\n')
print('HEADER_TOTAL',len(headers),'INVALID',sum(not x['header_valid'] for x in headers))
