import pathlib,os,json
base=pathlib.Path('/dwdhome/fy/BASE_E6_2')
for d in (base/'edh-universe',base/'feature-production-agent',base/'params/tis',base/'settings',pathlib.Path('/dwdhome/fy/cgpterm/artifacts/oi-eaw-wall/OI-EAW-WALL-20261114-01')):
 print('DIR',str(d),'exists',d.exists(),'symlink',d.is_symlink())
 if d.is_dir():
  a=list(d.iterdir());print('COUNT',len(a));print(json.dumps([{'name':p.name,'dir':p.is_dir(),'link':p.is_symlink(),'git':(p/'.git').exists() if p.is_dir() else False} for p in sorted(a)[:140]],ensure_ascii=False))
for rel in ('edh-universe/frp','edh-universe/e-wrks','edh-universe/mpds','edh-universe/e-wrks/hasdim','params/tis','tis/tti'):
 p=base/rel
 if p.is_dir():
  print('SUBDIR',str(p),[(q.name,q.is_dir(),(q/'.git').exists() if q.is_dir() else False) for q in sorted(p.iterdir())[:70]])
