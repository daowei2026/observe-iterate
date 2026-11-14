import pathlib,re
B=pathlib.Path('/dwdhome/fy/BASE_E6_2')
for rel,spans in [('mquant/tis/frp/EawBattleP.py',[(30,104)]),('mquant/tis/frp/Base.py',[(1,95)]),('mquant/frame/lang/internal/dao/frp/dba.py',[(1,210)]),('mquant/tis/hf/prel0/wall_assembler.py',[(630,712)]),('mquant/tis/hf/prel0/p1_dba_export.py',[(1,85)]),('mquant/tis/hf/prel0/p1_product_receipt.py',[(158,205),(240,307),(360,410)])]:
 p=B/rel;print('FILE',p,'EXISTS',p.exists())
 if p.exists():
  lines=p.read_text().splitlines()
  for lo,hi in spans:
   for n in range(lo,min(hi,len(lines))+1):print(f'{n}: {lines[n-1]}')
