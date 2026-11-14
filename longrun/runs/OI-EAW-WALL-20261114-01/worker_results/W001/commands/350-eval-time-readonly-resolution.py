import pathlib,json
W=pathlib.Path(__file__).resolve().parents[1];B=pathlib.Path('/dwdhome/fy/BASE_E6_2')
for rel,lo,hi in [('mquant/frame/core/base/json.py',90,165),('mquant/frame/core/store.py',750,820),('mquant/frame/core/base/app.py',1,110),('mquant/frame/lib3.py',1,125),('edh-universe/frp/frp/src/Frp/Instance.hs',30,85),('mquant/frame/__init__.py',1,80)]:
 p=B/rel;print('FILE',p)
 for n,line in enumerate(p.read_text().splitlines(),1):
  if lo<=n<=hi:print(f'{n}: {line}')
p=W/'evidence/340-headers-only.command.json';print('HEADER_COMMAND_COMPLETED',p.exists())
if p.exists():
 print(p.read_text());print((W/'evidence/340-headers-only.stdout.txt').read_text()[-4500:])
