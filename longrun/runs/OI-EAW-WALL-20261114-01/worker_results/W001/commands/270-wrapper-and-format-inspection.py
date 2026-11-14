import pathlib,json,re
W=pathlib.Path(__file__).resolve().parents[1];B=pathlib.Path('/dwdhome/fy/BASE_E6_2')
print((W/'evidence/261-reader-types-symbols.stdout.txt').read_text())
for rel in ('mquant/frame/core','mquant/frame/lang/internal','pydim/dim','mquant/tis/hf/prel0'):
 p=B/rel;print('LAYOUT',rel,[q.name for q in sorted(p.iterdir()) if q.is_file()][:65])
for a in json.loads((W/'evidence/WALL_ASSET_METADATA.json').read_text())['assets']:
 if a['feature']=='EawP1WallLifecycleFrp' and '2020-12-01' in a['path']:
  for f in a['files']:
   if f['path'].endswith('/type'):
    p=pathlib.Path(f['path']);print('TYPE_FILE',p,repr(p.read_text()))
  for f in a['files'][:4]:
   p=pathlib.Path(f['path'])
   if p.suffix=='.dba':
    with p.open('rb') as r:b=r.read(128)
    print('DBA_HEADER_BYTES',p,len(b),b.hex())
for rel in ('pydim/dim/__init__.py','mquant/frame/lang/internal/dao/util.py','mquant/tis/hf/prel0/p1_dba_export.py'):
 p=B/rel;print('FILE',p)
 if p.is_file():
  for n,line in enumerate(p.read_text().splitlines(),1):
   if n<=125:print(f'{n}: {line}')
