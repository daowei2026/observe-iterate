import pathlib,os,itertools,json,datetime
W=pathlib.Path(__file__).resolve().parents[1];results=[]
for root,origin in [('/m3varK/BaseData/futures/TA_updto20240229_DBA/fao/prod','BASE/config.yml:3'),('/m3varK/BaseData/futures/TB/fao/prod','m3sof/settings/env/default.py:13,18,21 + sof/default.py:21'),('/m3varK/BaseData/futures/TA_updto20240229/fao/prod','sof/TA_updto20240229.py candidate;未当作当前默认'),('/m3varK/BaseData/futures/TA_updto20240229_DBA/fao','config.yml 上级仅一层，用于检查环境候选')]:
 p=pathlib.Path(root);r={'path':root,'origin':origin,'exists':p.exists(),'is_dir':p.is_dir(),'realpath':str(p.resolve()),'entries':[],'cap':180}
 if p.is_dir():
  with os.scandir(p) as it:entries=list(itertools.islice(it,181))
  r['truncated']=len(entries)>180
  for e in entries[:180]:
   st=e.stat(follow_symlinks=False);r['entries'].append({'name':e.name,'is_dir':e.is_dir(follow_symlinks=False),'is_link':e.is_symlink(),'size':st.st_size,'mtime_utc':datetime.datetime.fromtimestamp(st.st_mtime,datetime.timezone.utc).isoformat()})
 print(json.dumps(r,ensure_ascii=False,indent=2));results.append(r)
(W/'evidence/STORE_ROOTS.json').write_text(json.dumps(results,ensure_ascii=False,indent=2)+'\n')
