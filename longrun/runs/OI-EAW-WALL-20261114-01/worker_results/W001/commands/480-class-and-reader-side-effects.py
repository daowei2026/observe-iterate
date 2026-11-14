import pathlib
B=pathlib.Path('/dwdhome/fy/BASE_E6_2')
for rel,lo,hi in [('mquant/frame/core/app/env.py',110,215),('mquant/frame/lang/internal/abstract/fao.py',1,45)]:
 p=B/rel;print('FILE',p,'EXISTS',p.exists())
 if p.is_file():
  for n,line in enumerate(p.read_text().splitlines(),1):
   if lo<=n<=hi:print(f'{n}: {line}')
for rel in ('mquant/frame/lang/internal/mixin','mquant/frame/lang/internal/data','mquant/frame/core/app','mquant/frame/lang/internal/abstract'):
 p=B/rel;print('DIR',rel,[(q.name,q.is_dir()) for q in sorted(p.iterdir())[:70]])
