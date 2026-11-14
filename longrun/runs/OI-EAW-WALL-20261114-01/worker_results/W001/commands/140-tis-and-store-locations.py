import pathlib,json
B=pathlib.Path('/dwdhome/fy/BASE_E6_2')
for root in (B/'mquant/tis',pathlib.Path('/m3c3/py-prod/tis'),pathlib.Path('/m3varK/workspace/zx_mquant6.2_test/tis'),B/'edh-universe/frp/frp/test/Frp/Instance/ISL/Eaw/P1',B/'m3sof/settings/sof',B/'m3sof/settings/env'):
 print('CANDIDATE',root,'GIT', (root/'.git').exists(),'REAL',root.resolve())
 print('TOP',[(p.name,p.is_dir(),p.is_symlink()) for p in sorted(root.iterdir())[:90]] if root.is_dir() else None)
 for rel in ('frp/EawBattleP.py','hf/prel0/wall_assembler.py','dao/FrpDbaDao.py','__init__.py','frp/__init__.py','AGENTS.md'):
  p=root/rel
  if p.is_file():print('EXACT',p,'BYTES',p.stat().st_size)
for rel,lo,hi in [('edh-universe/frp/frp-core/src/Frp/Core/Fao/Class.hs',420,530),('m3sof/settings/app.py',1,120),('m3sof/settings/env/default.py',1,45),('m3sof/settings/env/dev.py',1,35),('m3sof/core/sof.py',1,100),('config.yml',1,30)]:
 p=B/rel;print('FILE',p,'LINES',lo,hi)
 for n,line in enumerate(p.read_text().splitlines(),1):
  if lo<=n<=hi and not any(x in line.lower() for x in ('password','secret','token','dsn','postgres','mongo_uri','user:')):print(f'{n}: {line}')
