import pathlib
B=pathlib.Path('/dwdhome/fy/BASE_E6_2')
for rel,lo,hi in [('mquant/tis/frp/EawBattleP.py',1,115),('mquant/tis/frp/__init__.py',1,175),('mquant/tis/hf/prel0/wall_assembler.py',600,730),('mquant/tis/hf/prel0/wall_assembler.py',733,860),('m3sof/settings/sof/TA_updto20240229_DBA.py',1,90),('m3sof/settings/sof/default.py',1,85),('mquant/tis/__init__.py',1,70)]:
 p=B/rel;print('FILE',p,'LINES',lo,hi)
 for n,line in enumerate(p.read_text().splitlines(),1):
  if lo<=n<=hi and not any(x in line.lower() for x in ('password','secret','token','dsn','username','database','host =','host=')):print(f'{n}: {line}')
