from pathlib import Path
import sys,os,json,hashlib,re,ctypes,platform
sys.path.insert(0,str(Path(__file__).parent));import runner as w
w.guard();R=w.ROOT;B=w.BASE
G=['/usr/bin/git','--no-optional-locks'];BASE_COMMIT='cac6c912dd65a14acbd591ca57e0afd8ddb4ef13'
def readgit(label,repo,*args):
 result=w.run(label,G+['-C',str(repo),*args],limit=35)
 if result['exit_code']!=0:raise RuntimeError(label)
 return Path(result['stdout']['path']).read_bytes()
def fact(p):
 p=Path(p);s=p.lstat();d={'path':str(p),'realpath':str(p.resolve()),'symlink':p.is_symlink(),'mode':s.st_mode,'dev':s.st_dev,'inode':s.st_ino,'size':s.st_size,'mtime_ns':s.st_mtime_ns}
 if p.is_file():d['sha256']=hashlib.sha256(p.read_bytes()).hexdigest()
 return d
paths=[B/'edh-universe/frp/frp',B/'mquant/tis',B/'mquant/worker'];snap={}
for i,repo in enumerate(paths):
 top=readgit(f'before-{i}-root',repo,'rev-parse','--show-toplevel').decode().strip();assert top==str(repo.resolve())
 info={'path':str(repo),'realpath':str(repo.resolve()),'repo_root':top,'head':readgit(f'before-{i}-head',repo,'rev-parse','HEAD').decode().strip(),'branch':readgit(f'before-{i}-branch',repo,'branch','--show-current').decode().strip(),'status':readgit(f'before-{i}-status',repo,'status','--porcelain=v1','--untracked-files=normal').decode(),'files':[]}
 names=['.git/HEAD','.git/index']
 if i==0:names+=['src/Frp/Instance/ISL/Eaw/P1/WallLifecycle.hs','src/Frp/Instance/ISL/Eaw/P1/FaoIngress.hs','src/Frp/Instance/ISL/Eaw/P1/Products.hs','src/Frp/Instance/ISL/Eaw/P1/Publication.hs','src/Frp/Instance/ISL/Eaw/P1/Internal/OccurrenceLedger.hs','test/Frp/Instance/ISL/Eaw/P1/P1EndToEndSpec.hs','frp.cabal','stack.yaml','src/Frp/Instance/BussinessUtils.hs']
 if i==1:names+=['frpExample/STCalendar.py']
 if i==2:names+=['adt/dbaw.py']
 dirty=[line[3:] for line in info['status'].splitlines() if len(line)>3 and not line.startswith('??') and ' -> ' not in line]
 for name in dict.fromkeys(names+dirty):
  p=repo/name
  if p.is_file():info['files'].append(fact(p))
 snap[str(repo)]=info
w.save('audit/SHARED_BEFORE.json',{'utc':w.utc(),'repos':snap,'scope':'three exact repositories; no production data path accessed'})
repo=paths[0];assert snap[str(repo)]['head']==BASE_COMMIT
basefiles={}
for i,name in enumerate(['src/Frp/Instance/ISL/Eaw/P1/WallLifecycle.hs','src/Frp/Instance/ISL/Eaw/P1/FaoIngress.hs','src/Frp/Instance/ISL/Eaw/P1/Products.hs','src/Frp/Instance/ISL/Eaw/P1/Publication.hs','src/Frp/Instance/ISL/Eaw/P1/Internal/OccurrenceLedger.hs','test/Frp/Instance/ISL/Eaw/P1/P1EndToEndSpec.hs','frp.cabal','stack.yaml']):
 b=readgit('base-blob-'+str(i),repo,'show',BASE_COMMIT+':'+name);p=R/'input/exact-base'/name;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(b)
 basefiles[name]={'source_ref':'daowei2026/frp@'+BASE_COMMIT+':'+name,'receipt_path':str(p),'sha256':hashlib.sha256(b).hexdigest(),'bytes':len(b),'matches_working_copy':(repo/name).read_bytes()==b,'imports':[l for l in b.decode().splitlines() if l.startswith('import ')]}
w.save('audit/EXACT_SOURCE_BLOBS.json',basefiles)
w.save('audit/FRP_BASE_TREE.json',{'commit':BASE_COMMIT,'tree':readgit('base-tree',repo,'rev-parse',BASE_COMMIT+'^{tree}').decode().strip(),'staged':False})
for name in ['stack.yaml','stack.yaml.lock']:
 (R/'input'/('BASE-'+name)).write_bytes((B/name).read_bytes())
localrels=['edh-universe/frp/frp-core','edh-universe/frp/frp','edh-universe/frp/frp-poc','edh-universe/e-wrks/edh/host.hs','edh-universe/e-wrks/edh/elr','edh-universe/e-wrks/eas/host.hs','edh-universe/e-wrks/hasdim/host.hs','edh-universe/e-wrks/edh/lossless-decimal','edh-universe/fis/cfis/host.hs','edh-universe/hsite3/hgeometry/hgeometry','edh-universe/hsite3/hgeometry/hgeometry-combinatorial','edh-universe/e-wrks/nedh/host.hs','edh-universe/e-wrks/haskit/host.hs','edh-universe/e-wrks/sedh/host.hs','edh-universe/e-wrks/els/host.hs']
packages=[]
for i,rel in enumerate(localrels):
 p=B/rel;obj={'path':str(p),'exists':p.is_dir(),'realpath':str(p.resolve())}
 if p.is_dir():
  top=readgit('local-'+str(i)+'-root',p,'rev-parse','--show-toplevel').decode().strip();assert Path(top).is_relative_to(B)
  obj.update({'repo_root':top,'head':readgit('local-'+str(i)+'-head',p,'rev-parse','HEAD').decode().strip(),'declarations':[]})
  cabals=sorted(p.glob('*.cabal'));assert len(cabals)<=5
  for q in cabals:
   b=q.read_bytes();r=q.relative_to(Path(top));exact=readgit('local-'+str(i)+'-'+q.stem+'-cabal',p,'show',obj['head']+':'+str(r));dest=R/'input/local-package-declarations'/rel/q.name;dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(exact)
   obj['declarations'].append({'path':str(q),'head_relative_path':str(r),'working':fact(q),'exact_head_sha256':hashlib.sha256(exact).hexdigest(),'matches_head':b==exact,'receipt_path':str(dest),'declared_fields':[l.strip() for l in exact.decode().splitlines() if re.match(r'^\s*(name|version|build-type|hs-source-dirs|build-depends|cabal-version|custom-setup)\s*:',l)]})
 packages.append(obj)
w.save('audit/LOCAL_PACKAGE_CLOSURE.json',{'packages':packages,'no_source_staged':True,'method':'only explicitly named local roots, top-level cabal and exact git HEAD metadata','dependency_closure_complete':False})
toolnames=['/usr/bin/python3.12','/usr/bin/git','/usr/bin/bash','/usr/bin/true','/usr/bin/bwrap','/usr/bin/strace','/usr/bin/timeout','/usr/bin/time','/usr/bin/prlimit','/usr/bin/tar','/usr/bin/cp','/usr/bin/rsync','/usr/bin/find','/usr/bin/du','/usr/bin/stat','/usr/bin/sha256sum','/home/dw/.local/bin/stack','/nix/.ghcup/bin/stack','/nix/.ghcup/bin/cabal','/nix/.ghcup/ghc/9.4.8/bin/ghc-9.4.8','/nix/.ghcup/ghc/9.4.8/bin/ghc-pkg-9.4.8','/nix/.ghcup/ghc/9.4.8/lib/ghc-9.4.8/bin/ghc-9.4.8','/nix/.ghcup/ghc/9.4.8/lib/ghc-9.4.8/bin/ghc-pkg-9.4.8','/home/dw/.agents/skills/long-task-status/scripts/task_status.py']
tools={}
for name in toolnames:
 p=Path(name);tools[name]={'exists':p.exists()}
 if p.exists():tools[name].update(fact(p.resolve()));tools[name]['invocation_path']=str(p);tools[name]['invocation_is_symlink']=p.is_symlink()
w.save('audit/TOOL_BINDINGS.json',tools)
cache={}
for p in [Path('/home/dw/.stack/snapshots'),Path('/home/dw/.stack/pantry'),Path('/home/dw/.stack/programs'),B/'.stack-work',repo/'.stack-work',Path('/nix/.ghcup/ghc/9.4.8/lib/ghc-9.4.8/lib/package.conf.d'),Path('/nix/.ghcup/ghc/8.10.7/lib/ghc-8.10.7/package.conf.d')]:
 obj={'exists':p.exists(),'scope':'single directory level; no recursive cache/source/artifact scan'}
 if p.is_dir():
  children=list(p.iterdir());assert len(children)<=1000;obj['entries']=[{'name':q.name,'dir':q.is_dir(),'symlink':q.is_symlink(),'size':q.lstat().st_size} for q in sorted(children)]
 cache[str(p)]=obj
w.save('audit/BOUNDED_CACHE_INDEX.json',cache)
print('COLLECTED',len(basefiles),'base files',len(packages),'local roots',len(tools),'tools; source untouched; source staging absent')
