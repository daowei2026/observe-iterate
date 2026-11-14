import pathlib
b=pathlib.Path('/dwdhome/fy/BASE_E6_2')
for rel,lo,hi in [('edh-universe/frp/frp/src/Frp/Instance/ISL/Eaw/P1/FaoIngress.hs',90,240),('edh-universe/frp/frp-core/src/Frp/Core/Fao/Class.hs',595,687),('edh-universe/frp/frp-core/src/Frp/Core/Fao/Class.hs',744,815),('edh-universe/frp/frp-core/src/Frp/Core/Fao/Store/Class.hs',160,215),('edh-universe/frp/frp-core/src/Frp/Core/Fao/Store/Class.hs',250,305)]:
 p=b/rel;print('FILE',p,'LINES',lo,hi)
 for n,line in enumerate(p.read_text().splitlines(),1):
  if lo<=n<=hi:print(f'{n}: {line}')
