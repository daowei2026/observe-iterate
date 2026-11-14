import pathlib,json,os,re,itertools
W=pathlib.Path(__file__).resolve().parents[1];roots=json.loads((W/'evidence/STORE_ROOTS.json').read_text());records=[]
for row in roots:
 if not row['path'].endswith('/prod'):continue
 print('ROOT_SUMMARY',row['path'],'observed',len(row['entries']),'truncated',row.get('truncated'))
 names=[x['name'] for x in row['entries'] if x['is_dir'] and not x['is_link'] and '~' in x['name']]
 print('DATE_WINDOWS',names)
 # Exact feature path tests under observed range dirs; no recursive traversal or unrelated class enumeration.
 for sub in ['',*names]:
  for cls in ('WallAssembler','EawP1WallLifecycleFrp','WallOccurrenceFao','EawBattleP'):
   p=pathlib.Path(row['path'])/sub/cls;r={'path':str(p),'source_root':row['path'],'time_range_path':sub or None,'feature':cls,'exists':p.exists(),'is_dir':p.is_dir()}
   if p.is_dir():
    with os.scandir(p) as it:a=list(itertools.islice(it,65))
    r['children']=[{'name':e.name,'is_dir':e.is_dir(follow_symlinks=False),'is_link':e.is_symlink()} for e in a[:64]];r['children_truncated']=len(a)>64
    print('FOUND_CLASS',json.dumps(r,ensure_ascii=False))
   records.append(r)
(W/'evidence/CLASS_CANDIDATES.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n');print('EXACT_PATH_PROBES',len(records),'FOUND',sum(x['exists'] for x in records))
