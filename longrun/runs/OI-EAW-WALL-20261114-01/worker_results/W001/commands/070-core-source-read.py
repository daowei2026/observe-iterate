import pathlib
B=pathlib.Path('/dwdhome/fy/BASE_E6_2')
items=[('edh-universe/frp/frp/src/Frp/Instance/ISL/Eaw/P1.hs',1,205),('edh-universe/frp/frp/src/Frp/Instance/ISL/Eaw/P1/FaoIngress.hs',220,365),('edh-universe/frp/frp/src/Frp/Instance/ISL/Eaw/P1/Publication.hs',1,85),('edh-universe/frp/frp/src/Frp/Instance/ISL/Eaw/P1/Publication.hs',170,350),('edh-universe/frp/frp/src/Frp/Instance/ISL/Eaw/P1/Publication.hs',665,700),('edh-universe/mpds/host.py/mpds/task/frp.py',1,180),('settings/__init__.py',1,160),('params/tis/__init__.py',1,160),('run-python.sh',1,100)]
for rel,lo,hi in items:
 p=B/rel;print('FILE',str(p),'LINES',lo,hi)
 if p.exists():
  for n,line in enumerate(p.read_text().splitlines(),1):
   if lo<=n<=hi: print(f'{n}: {line}')
