import pathlib
B=pathlib.Path('/dwdhome/fy/BASE_E6_2')
for rel,spans in [('pydim/dim/rt.py',[(65,180)]),('pydim/dim/dbas.py',[(1,154)]),('mquant/frame/core/store.py',[(1,85),(470,530)]),('edh-universe/frp/frp-core/src/Frp/DbaStore/Internal.hs',[(100,160)]),('edh-universe/frp/frp/src/Frp/Instance/ISL/Eaw/P1/Products.hs',[(75,190)]),('edh-universe/frp/frp/src/Frp/Instance/ISL/Eaw/P1/Publication.hs',[(608,628)])]:
 p=B/rel;print('FILE',p)
 lines=p.read_text().splitlines()
 for lo,hi in spans:
  for n in range(lo,min(hi,len(lines))+1):print(f'{n}: {lines[n-1]}')
