import pathlib,json,os,itertools,datetime,hashlib,collections,time
W=pathlib.Path(__file__).resolve().parents[1];candidates=json.loads((W/'evidence/CLASS_CANDIDATES.json').read_text());roots=[x for x in candidates if x['exists'] and x['feature'] in ('WallAssembler','EawP1WallLifecycleFrp','WallOccurrenceFao')]
limits={'max_directories':320,'max_entries_per_directory':160,'max_files':2200,'max_depth':13,'small_hash_threshold':65536,'max_hash_bytes':8388608,'elapsed_stop_seconds':22};started=time.monotonic();dcount=0;fcount=0;hashed=0;results=[];stops=[]
for root in roots:
 tree={'path':root['path'],'feature':root['feature'],'time_range_path':root['time_range_path'],'source_root':root['source_root'],'files':[],'directories':[],'stopped':False};q=collections.deque([(pathlib.Path(root['path']),0)])
 while q:
  p,depth=q.popleft()
  if dcount>=limits['max_directories'] or fcount>=limits['max_files'] or time.monotonic()-started>limits['elapsed_stop_seconds']:
   stops.append({'path':str(p),'reason':'global metadata cost limit','queued':len(q)+1});tree['stopped']=True;break
  with os.scandir(p) as it:entries=list(itertools.islice(it,limits['max_entries_per_directory']+1))
  dcount+=1;tree['directories'].append({'path':str(p),'entry_count_observed':min(len(entries),160),'complete':len(entries)<=160})
  if len(entries)>160:stops.append({'path':str(p),'reason':'per-directory cap'});tree['stopped']=True
  for e in entries[:160]:
   ep=pathlib.Path(e.path);s=e.stat(follow_symlinks=False)
   if e.is_symlink():stops.append({'path':str(ep),'reason':'symlink not followed'});continue
   if e.is_dir(follow_symlinks=False):
    if depth<limits['max_depth']:q.append((ep,depth+1))
    else:stops.append({'path':str(ep),'reason':'depth cap'});tree['stopped']=True
   elif e.is_file(follow_symlinks=False):
    fcount+=1;r={'path':str(ep),'bytes':s.st_size,'allocated_bytes':s.st_blocks*512,'mtime_utc':datetime.datetime.fromtimestamp(s.st_mtime,datetime.timezone.utc).isoformat(),'suffix':ep.suffix,'sha256':None,'hash_reason':'metadata only; over small-file threshold or budget','decoded':False}
    if s.st_size<=65536 and hashed+s.st_size<=8388608:
     data=ep.read_bytes();hashed+=len(data);r['sha256']=hashlib.sha256(data).hexdigest();r['hash_reason']='small-file full sha256'
    if ep.name.endswith('.json') and s.st_size<=1048576:
     data=ep.read_bytes()
     try:r['json']=json.loads(data);r['decoded']=True;r['sha256']=hashlib.sha256(data).hexdigest();r['hash_reason']='small metadata JSON full sha256'
     except (ValueError,UnicodeDecodeError) as exc:r['json_error']=type(exc).__name__
    tree['files'].append(r)
 tree['file_count']=len(tree['files']);tree['total_file_bytes']=sum(x['bytes'] for x in tree['files']);tree['directory_count']=len(tree['directories']);tree['leaf_parents']=sorted(set(str(pathlib.Path(x['path']).parent) for x in tree['files'] if pathlib.Path(x['path']).name=='fields.json'))
 print('ASSET_TREE',json.dumps({k:v for k,v in tree.items() if k not in ('directories','files')},ensure_ascii=False))
 for f in tree['files']:
  if f.get('json') is not None:print('METADATA_JSON',json.dumps(f,ensure_ascii=False))
 results.append(tree)
result={'limits':limits,'elapsed_seconds':time.monotonic()-started,'directories_visited':dcount,'files_observed':fcount,'small_bytes_hashed':hashed,'stops':stops,'assets':results}
(W/'evidence/WALL_ASSET_METADATA.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n');print('TOTAL',json.dumps({k:v for k,v in result.items() if k!='assets'},ensure_ascii=False))
