import pathlib,re
B=pathlib.Path('/dwdhome/fy/BASE_E6_2')
for rel,lo,hi in [('mquant/frame/reload/cls.py',1,100),('mquant/tis/lib3.py',1,100),('mquant/worker/beat.py',1,100),('edh-universe/frp/frp-core/src/Frp/Apt/Time.hs',1,90),('edh-universe/frp/frp/dbaw/Main.hs',75,110),('mquant/tis/hf/prel0/p1_product_receipt.py',97,158)]:
 p=B/rel;print('FILE',p,'EXISTS',p.exists())
 if p.is_file():
  for n,line in enumerate(p.read_text().splitlines(),1):
   if lo<=n<=hi:print(f'{n}: {line}')
for rel in ('mquant/tis/ufrp','mquant/frame/reload','mquant/frame/lang/internal/impl'):
 p=B/rel;print('DIR',p,[q.name for q in sorted(p.iterdir())[:70]] if p.is_dir() else None)
