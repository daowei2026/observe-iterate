import pathlib,sys,json,subprocess,hashlib,re
W=pathlib.Path(__file__).resolve().parents[1];sys.path.insert(0,str(W));import runner
B=runner.BASE;doc=json.loads((W/'WORKSPACE_BINDING.json').read_text())
for name,rel,files in [('frame','mquant/frame',['lang/frp/base.py','lang/internal/base.py','lang/internal/dao/frp/dba.py','core/store.py']),('worker','mquant/worker',['adt/dbaw.py','adt/__init__.py'])]:
 p=B/rel;x={'name':name,'path':str(p),'realpath':str(p.resolve()),'old_baseline':None,'old_baseline_reason':'ORDER 未为此依赖指定旧 SHA','commands':{},'files':[]};assert (p/'.git').exists()
 for key,args in [('toplevel',['rev-parse','--show-toplevel']),('head',['rev-parse','HEAD']),('branch',['symbolic-ref','--quiet','--short','HEAD']),('status',['status','--short','--branch']),('worktrees',['worktree','list','--porcelain']),('remotes',['remote','-v'])]:
  cmd=['git','--no-optional-locks','-C',str(p),*args];st=runner.utc();r=subprocess.run(cmd,env=runner.environment(),capture_output=True,text=True,timeout=10);v={'command':cmd,'start':st,'end':runner.utc(),'exit_code':r.returncode,'stdout':re.sub(r'(https?://)[^/\s@]+@',r'\1[REDACTED]@',r.stdout),'stderr':r.stderr};x['commands'][key]=v
  with (W/'COMMAND_LOG.txt').open('a') as f:f.write('\nGIT_SUBCOMMAND '+json.dumps(v,ensure_ascii=False)+'\n')
 for rf in files:
  p1=p/rf;data=p1.read_bytes();x['files'].append({'path':str(p1),'relative_path':rf,'exists':True,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),'git_blob_sha1':hashlib.sha1(b'blob '+str(len(data)).encode()+b'\x00'+data).hexdigest()})
 doc['repos'].append(x);print('REPO',name,x['commands']['head']['stdout'].strip(),x['commands']['status']['stdout'].strip())
# Pin copies of the two professional inputs to exact local Git objects when available, never fetch.
oi=pathlib.Path('/dwdhome/fy/cgpterm/artifacts/oi-eaw-wall/OI-EAW-WALL-20261114-01/observe-iterate');pins=[]
for sha,rel,name in [('cdec293a4bfdac85ca4ab3171f9eeb083a338493','longrun/runs/OI-EAW-WALL-20261114-01/delegations/D001/DELEGATION.md','DELEGATION.md'),('ca7fdae84f65265332e3a53865724a2615508766','task-inputs/eaw-p1-wall-lifecycle/FEATURE_CONTEXT.md','FEATURE_CONTEXT.md')]:
 cmd=['git','--no-optional-locks','-C',str(oi),'show',sha+':'+rel];st=runner.utc();r=subprocess.run(cmd,env=runner.environment(),capture_output=True,timeout=10);h=hashlib.sha256(r.stdout).hexdigest() if r.returncode==0 else None;copy=W/'inputs'/name;v={'command':cmd,'start':st,'end':runner.utc(),'exit_code':r.returncode,'sha256':h,'matches_local_mirror':r.returncode==0 and r.stdout==copy.read_bytes(),'reason':None if r.returncode==0 else 'UNAVAILABLE_LOCALLY; no fetch','stderr':r.stderr.decode(errors='replace')};pins.append(v)
 with (W/'COMMAND_LOG.txt').open('a') as f:f.write('\nPINNED_INPUT_SUBCOMMAND '+json.dumps(v,ensure_ascii=False)+'\n')
 print('PIN',json.dumps(v,ensure_ascii=False))
doc['pinned_input_checks']=pins;doc['runtime_tuple']=None;doc['runtime_tuple_reason']='checkout 已查明；现有物化为 P1Wall*Storage 历史 schema，产品 code receipt 缺失、generated wrapper 缺类型；未运行、未把现有二进制绑定到 HEAD'
(W/'WORKSPACE_BINDING.json').write_text(json.dumps(doc,ensure_ascii=False,indent=2)+'\n')
runner.run('571-current-wall-field-lines',['rg','-n','--max-count','28','data Wall|wall.* ::|WallIdentity|FeatureRunIdentity|wallLifecycleCurrent|WallOccurrenceRef|WallLifecycleOccurrence|WallCurrentView','edh-universe/frp/frp/src/Frp/Instance/ISL/Eaw/P1/Products.hs','edh-universe/frp/frp/src/Frp/Instance/ISL/Eaw/P1/WallLifecycle.hs'])
