import sys,pathlib,json,subprocess,re,hashlib
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[1]));import runner
W=runner.W;B=runner.BASE;doc=json.loads((W/'WORKSPACE_BINDING.json').read_text())
for name,rel,old,files in [('tis','mquant/tis','ef887396e0a06d6e75be47efee0f1985ad7988a3',['frp/EawBattleP.py','hf/prel0/wall_assembler.py','frp/__init__.py','__init__.py']),('m3sof','m3sof',None,['settings/app.py','settings/env/default.py','settings/env/prod.py','settings/sof/TA_updto20240229_DBA.py'])]:
 p=B/rel;x={'name':name,'path':str(p),'realpath':str(p.resolve()),'old_baseline':old,'commands':{},'files':[]}
 assert (p/'.git').exists()
 def g(key,args):
  cmd=['git','--no-optional-locks','-C',str(p),*args];st=runner.utc();r=subprocess.run(cmd,capture_output=True,text=True,env=runner.environment(),timeout=15);out=re.sub(r'(https?://)[^/\s@]+@',r'\1[REDACTED]@',r.stdout);v={'command':cmd,'start':st,'end':runner.utc(),'exit_code':r.returncode,'stdout':out,'stderr':r.stderr};x['commands'][key]=v
  with (W/'COMMAND_LOG.txt').open('a') as f:f.write('\nGIT_SUBCOMMAND '+json.dumps(v,ensure_ascii=False)+'\n')
  return v
 for k,a in [('toplevel',['rev-parse','--show-toplevel']),('head',['rev-parse','HEAD']),('branch',['symbolic-ref','--quiet','--short','HEAD']),('status',['status','--short','--branch']),('worktrees',['worktree','list','--porcelain']),('remotes',['remote','-v'])]:g(k,a)
 if old:
  r=g('baseline_probe',['cat-file','-e',old+'^{commit}']);x['old_commit_present']=r['exit_code']==0
  if r['exit_code']==0:g('baseline_related_diff',['diff','--stat',old,'HEAD','--',*files]);g('worktree_related_diff',['diff','--stat',old,'--',*files])
  else:x['baseline_status']='UNAVAILABLE_LOCALLY'
 for relf in files:
  f=p/relf;row={'path':str(f),'relative_path':relf,'exists':f.exists()}
  if f.is_file():row.update({'sha256':hashlib.sha256(f.read_bytes()).hexdigest(),'bytes':f.stat().st_size,'blob':g('blob_'+relf.replace('/','_'),['hash-object','--',relf])['stdout'].strip()})
  x['files'].append(row)
 doc['repos'].append(x);print('SUMMARY',name,x['commands']['head']['stdout'],x['commands']['status']['stdout'],'BASELINE',x.get('old_commit_present'))
parent=doc['repos'][6];parent['relevance']='NOT_TIS: 向上发现 /dwdhome/fy 的 uplot 父仓库；不用于 TIS tuple。无关父级 status 已记录但不再扩展。';doc['base_is_repo']=False;doc['base_is_repo_reason']='BASE 无自身 .git；BASE/tis 的 rev-parse 归属 /dwdhome/fy uplot，真实 TIS 是 BASE/mquant/tis';doc['scope_deviation']={'command':'git -C BASE/tis status --short --branch','reason':'未先据 toplevel 拒绝上层无关仓库，意外列出无关父级未跟踪名字；仅元数据、未读内容，无后续扩搜'}
(W/'WORKSPACE_BINDING.json').write_text(json.dumps(doc,ensure_ascii=False,indent=2)+'\n')
