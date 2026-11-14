import pathlib,json,re
B=pathlib.Path('/dwdhome/fy/BASE_E6_2');w=pathlib.Path(__file__).resolve().parents[1]
r=json.loads((w/'WORKSPACE_BINDING.json').read_text())
for x in r['repos']:print('REPO_SUMMARY',x['name'],x['commands']['head']['stdout'].strip(),x['commands']['status']['stdout'].strip(),x['commands']['toplevel']['stderr'].strip())
for rel in ('m3rc','m3sof/__init__.py','python_modules/tis_auto/__init__.py','edh-universe/frp/frp/src/Frp/Instance/ISL/Eaw/P1.hs','edh-universe/frp/frp/src/Frp/Instance/ISL/Eaw/P1/FaoIngress.hs'):
 p=B/rel;print('FILE',p)
 if p.exists():
  for n,line in enumerate(p.read_text().splitlines(),1):
   ok=(rel=='m3rc' and re.search('PYTHON|tis|source|venv|anaconda|^export PATH|^M3',line)) or (rel.endswith('P1.hs') and 65<=n<=185) or (rel.endswith('FaoIngress.hs') and (240<=n<=340 or 1295<=n<=1382)) or rel in ('m3sof/__init__.py','python_modules/tis_auto/__init__.py')
   if ok:print(f'{n}: {line}')
for rel in ('m3sof','tis_auto','edh-universe/frp/frp/dbaw','edh-universe/frp/frp-core/dbas','edh-universe/frp/frp/test-data','edh-universe/frp/frp/test'):
 p=B/rel;print('DIRECTORY',p)
 if p.is_dir():print([(q.name,q.is_dir(),q.is_symlink()) for q in sorted(p.iterdir())[:90]])
