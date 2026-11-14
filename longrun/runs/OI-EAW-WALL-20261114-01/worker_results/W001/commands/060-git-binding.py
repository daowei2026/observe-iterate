import os,sys,pathlib,json,subprocess,datetime,re,hashlib
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[1]));import runner
B=runner.BASE;W=runner.W
repos=[('frp',B/'edh-universe/frp/frp','cac6c912dd65a14acbd591ca57e0afd8ddb4ef13',['src/Frp/Instance.hs','src/Frp/Instance/ISL/Eaw/P1.hs','src/Frp/Instance/ISL/Eaw/P1/WallLifecycle.hs','src/Frp/Instance/ISL/Eaw/P1/Products.hs','src/Frp/Instance/ISL/Eaw/P1/Publication.hs','src/Frp/Instance/ISL/Eaw/P1/FaoIngress.hs']),('frp-core',B/'edh-universe/frp/frp-core',None,['src/Frp/DbaStore.hs','src/Frp/Core/Fao.hs']),('mpds',B/'edh-universe/mpds',None,['host.py/mpds/task/frp.py']),('hasdim',B/'edh-universe/e-wrks/hasdim',None,['host.py/hasdim/rt.py']),('m3',B/'m3',None,['hpath.py']),('pydim',B/'pydim',None,['__init__.py']),('tis_path',B/'tis','ef887396e0a06d6e75be47efee0f1985ad7988a3',['frp/EawBattleP.py','hf/prel0/wall_assembler.py'])]
def clean(t):
 t=re.sub(r'(https?://)[^/\s@]+@',r'\1[REDACTED]@',t);t=re.sub(r'([?&](?:token|access_token|auth|password)=)[^&\s]+',r'\1[REDACTED]',t,flags=re.I);return t
def git(p,*a):
 cmd=['git','--no-optional-locks','-C',str(p),*a];st=runner.utc()
 try:r=subprocess.run(cmd,env=runner.environment(),capture_output=True,text=True,timeout=15);code=r.returncode;out=clean(r.stdout);err=clean(r.stderr)
 except subprocess.TimeoutExpired:code=124;out='';err='bounded timeout'
 row={'command':cmd,'start':st,'end':runner.utc(),'exit_code':code,'stdout':out,'stderr':err}
 with (W/'COMMAND_LOG.txt').open('a') as f:f.write('\nGIT_SUBCOMMAND '+json.dumps(row,ensure_ascii=False)+'\n')
 return row
R=[]
for name,p,old,paths in repos:
 entry={'name':name,'path':str(p),'realpath':str(p.resolve()),'old_baseline':old,'commands':{},'files':[]}
 for k,a in [('toplevel',['rev-parse','--show-toplevel']),('head',['rev-parse','HEAD']),('branch',['symbolic-ref','--quiet','--short','HEAD']),('status',['status','--short','--branch']),('worktrees',['worktree','list','--porcelain']),('remotes',['remote','-v'])]:entry['commands'][k]=git(p,*a)
 if old:
  ck=git(p,'cat-file','-e',old+'^{commit}');entry['old_commit_present']=ck['exit_code']==0;entry['baseline_probe']=ck
  if ck['exit_code']==0:entry['baseline_related_diff']=git(p,'diff','--stat',old,'HEAD','--',*paths)
  else:entry['baseline_status']='UNAVAILABLE_LOCALLY'
 for rel in paths:
  f=p/rel;d={'path':str(f),'exists':f.exists(),'relative_path':rel}
  if f.exists() and f.is_file() and f.stat().st_size<=2*1024*1024:
   data=f.read_bytes();d.update({'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),'git_blob':git(p,'hash-object','--',rel)})
  entry['files'].append(d)
 R.append(entry);print(json.dumps(entry,ensure_ascii=False,indent=2))
physical=json.loads((W/'evidence/PHYSICAL_BINDING.json').read_text());physical.update({'schema':'w001-workspace-binding/local-v1','run_id':'OI-EAW-WALL-20261114-01','work_order_id':'W001','repos':R,'base_is_repo':None,'base_is_repo_reason':'尚未直接执行根目录 git 探测；toplevel 以每项真实命令为准','runtime_tuple':None,'runtime_tuple_reason':'静态 checkout 与运行 receipt/二进制/配置尚未绑定'})
(W/'WORKSPACE_BINDING.json').write_text(json.dumps(physical,ensure_ascii=False,indent=2)+'\n')
