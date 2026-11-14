import pathlib,json
W=pathlib.Path(__file__).resolve().parents[1];B=pathlib.Path('/dwdhome/fy/BASE_E6_2')
p=W/'evidence/340-headers-only.command.json';print('HEADER_COMMAND',p.read_text() if p.exists() else 'RUNNING_OR_NO_RECEIPT')
p=W/'evidence/DBA_HEADERS.json';print('HEADER_JSON_EXISTS',p.exists())
if p.exists():
 j=json.loads(p.read_text());print('TOTAL',len(j['headers']),'INVALID',sum(not x['header_valid'] for x in j['headers']))
 for x in j['headers']:
  if x['feature']=='EawP1WallLifecycleFrp' and ('__ts__' in x['path'] or 'LocalNo' in x['path']):print('KEY_HEADER',json.dumps(x,ensure_ascii=False))
for rel,lo,hi in [('mquant/frame/core/base/json.py',1,90),('mquant/frame/core/__init__.py',1,60)]:
 p=B/rel;print('FILE',p)
 for n,line in enumerate(p.read_text().splitlines(),1):
  if lo<=n<=hi:print(f'{n}: {line}')
for rel in ('mquant/apt','mquant/frame/lang/internal/ext'):
 p=B/rel;print('DIR',p,[q.name for q in sorted(p.iterdir())[:70]])
