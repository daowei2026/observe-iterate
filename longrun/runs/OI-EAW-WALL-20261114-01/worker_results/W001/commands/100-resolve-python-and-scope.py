import pathlib,json,os,re
w=pathlib.Path(__file__).resolve().parents[1];B=pathlib.Path('/dwdhome/fy/BASE_E6_2');j=json.loads((w/'WORKSPACE_BINDING.json').read_text());t=j['repos'][-1]
for k in ('toplevel','head','worktrees','remotes'):print('TIS_PARENT_GIT',k,t['commands'][k]['stdout'])
print('GIT_ENV',{k:os.environ[k] for k in ('GIT_DIR','GIT_WORK_TREE','GIT_CEILING_DIRECTORIES') if k in os.environ})
for rel in ('m3rc','m3sof/core/__init__.py','m3sof/core/settings.py','m3sof/settings.py','m3sof/core/setting.py'):
 p=B/rel;print('FILE',p,p.exists())
 if p.exists():
  for n,line in enumerate(p.read_text().splitlines(),1):
   if (rel=='m3rc' and n<=82) or (rel!='m3rc' and re.search('sys.path|python_modules|tis|M3WORKS|M3ROOT|FRP|DATA|PATH|DIR',line,re.I)):
    if not re.search('password|passwd|token|secret',line,re.I):print(f'{n}: {line}')
for rel in ('tis_auto','edh-universe/frp/frp/dbaw','edh-universe/frp/frp-core/dbas','edh-universe/frp/frp/test-data','edh-universe/frp/frp/test','m3sof/core'):
 p=B/rel;print('LAYOUT',p,[(q.name,q.is_dir(),q.is_symlink()) for q in sorted(p.iterdir())[:80]] if p.is_dir() else None)
for d in ('/dwdhome/fy/BASE_E6_2/.runtime/python-deps','/dwdhome/fy/BASE_E6_2/python_modules/tis','/dwdhome/fy/BASE_E6_2/tis_auto'):
 p=pathlib.Path(d);print('PATH_META',str(p),p.resolve(),p.exists())
