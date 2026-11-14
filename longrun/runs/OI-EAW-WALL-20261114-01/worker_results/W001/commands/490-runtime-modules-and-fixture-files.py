import pathlib
B=pathlib.Path('/dwdhome/fy/BASE_E6_2')
for rel in ('mquant/frame','mquant/frame/lang','mquant/frame/DBAS.py','mquant/frame/lang/frp','mquant/tis/tests'):
 p=B/rel;print('PATH',p,'EXISTS',p.exists(),'GIT',(p/'.git').exists() if p.is_dir() else None)
 if p.is_dir():print('CHILDREN',[(q.name,q.is_dir()) for q in sorted(p.iterdir())[:95]])
for rel in ('mquant/frame/lang/__init__.py','mquant/frame/lang/internal/base.py','edh-universe/frp/frp/poc/dbaw.py','edh-universe/bin/dbaw'):
 p=B/rel;print('FILE',p,'BYTES',p.stat().st_size if p.is_file() else None)
 if p.is_file() and p.stat().st_size<40000:
  data=p.read_bytes()
  try:txt=data.decode()
  except UnicodeDecodeError:print('BINARY_NOT_LOADED');continue
  for n,line in enumerate(txt.splitlines(),1):
   if n<=120:print(f'{n}: {line}')
