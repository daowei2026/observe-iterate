import pathlib,os,re
B=pathlib.Path('/dwdhome/fy/BASE_E6_2')
for rel in ('m3sof/settings','mquant','cae','bestpractice','params','edh-universe/frp/frp/test-data/eaw','edh-universe/frp/frp/poc','edh-universe/bin','.migration/records'):
 p=B/rel;print('DIR',p,'REAL',p.resolve(),'EXISTS',p.exists(),'LINK',p.is_symlink())
 if p.is_dir():print('TOP',[(x.name,x.is_dir(),x.is_symlink()) for x in sorted(p.iterdir())[:90]])
for rel in ('config.yml','m3sof/settings/__init__.py','edh-universe/stack.yaml','edh-universe/frp/frp/dbaw/Main.hs','edh-universe/frp/frp/frp.cabal'):
 p=B/rel;print('FILE',p,'SIZE',p.stat().st_size if p.exists() else None)
 if p.exists():
  for n,line in enumerate(p.read_text().splitlines(),1):
   if re.search('dba|store|data|path|dir|tis|frp|OnlyRead|Cal|Wall|^library|^executable|main-is|source-dirs|location|\.\./',line,re.I) and not re.search('password|passwd|secret|token|uri|host|port|database|username|user:',line,re.I): print(f'{n}: {line}')
for d in ('/m3c3/py-prod/tis','/m3c3/Linux/apps/anaconda3/bin/python','/m3c3/Linux/apps/anaconda3/lib','/m3varK/workspace/zx_mquant6.2_test/tis'):
 p=pathlib.Path(d);print('CONFIG_POINTED_PATH',d,'EXISTS',p.exists(),'REAL',p.resolve())
