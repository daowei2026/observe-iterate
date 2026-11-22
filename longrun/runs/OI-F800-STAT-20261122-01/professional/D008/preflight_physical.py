"""D008只核本Run来源、限定runtime和当前可见写面，禁止全盘搜索。"""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256,sha1
import json,os,subprocess,shutil,sys
ROOT=Path(__file__).resolve().parent
BASE=ROOT.parents[2]
OLD=ROOT.parent/'D007'
REPO=BASE/'.runtime/f-observation-multiple-github-20261122/frp'
RUNTIME=BASE/'.runtime/f800-input-missing-20261123/runtime'
COMMIT='39f02ec4548e68ba8dbd30061afc870546000994'
def write(n,v): (ROOT/n).write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
def digest(p): return sha256(Path(p).read_bytes()).hexdigest()
def git(*args): return subprocess.check_output(['git',*args],cwd=REPO,text=True).strip()
assert git('rev-parse','HEAD')==COMMIT and not git('status','--porcelain')
assert (RUNTIME/'edh-universe/frp/frp').resolve()==REPO
adopt=json.loads((OLD/'CodeVersionAdoption.json').read_text())
manifest=json.loads((OLD/'BUILD_INPUT_MANIFEST.json').read_text())
files=[];mismatches=[]
for x in manifest['files']:
 p=REPO/x['path']
 actual=digest(p)
 if actual!=x['sha256']: mismatches.append(x['path'])
 files.append(dict(path=x['path'],sha256=actual,match=actual==x['sha256']))
assert not mismatches,mismatches
bins={}
for name,meta in adopt['binaries'].items():
 assert digest(meta['path'])==meta['sha256']
 bins[name]=dict(path=meta['path'],sha256=digest(meta['path']),match=True)
source=dict(checked_at=datetime.now(timezone.utc).isoformat(),frp_commit=COMMIT,source_root=str(REPO),runtime=str(RUNTIME),
 checked_source_files=len(files),mismatches=mismatches,files=files,engine_path=bins['ts']['path'],engine_sha256=bins['ts']['sha256'],
 engine_matches_recorded_build=True,build_completed=True,build_evidence='daowei2026/observe-iterate@08f5d8d4bd6982648fc93ce80b9cf843f183c8fd:longrun/runs/OI-F800-STAT-20261122-01/professional/D007/BUILD_STATUS.json')
write('FRP_SOURCE_BINDING.json',source)
dep=json.loads((OLD/'DEPENDENCY_BINDING.json').read_text())
for x in dep['critical_constructor_files']+dep['native_and_python_input_chain_files']:
 assert digest(x['path'])==x['sha256'],x['path']
dep['checked_at']=datetime.now(timezone.utc).isoformat(); dep['current_f_preflight']=True
write('TIS_SOURCE_RECHECK.json',dep)
config=Path('/m3varE/AppData/mquant/config/prod/sof/TA_updto20240229_DBA.json')
original=json.loads(config.read_text());current=dict(original);current['store_dir']=str(ROOT/'store')
assert not (ROOT/'store').exists()
app=ROOT/'platform-app/mquant/config/prod/sof/TA_updto20240229_DBA.json';app.parent.mkdir(parents=True,exist_ok=True);app.write_text(json.dumps(current,ensure_ascii=False,indent=2)+'\n')
write('PLATFORM_STORAGE_BINDING.json',dict(scope='只改本Run正常平台存储位置，非Feature参数',source_sof_config=str(config),source_sha256=digest(config),app_dir=str(ROOT/'platform-app'),store_dir=str(ROOT/'store'),sof_config_delta=[dict(field='store_dir',before=original['store_dir'],after=current['store_dir'])],input_paths_unchanged=True,special_store_overrides={},all_write_roots_under=str(BASE)))
write('RESULT_REUSE_ASSESSMENT.json',dict(adopted_frp=COMMIT,runtime=str(RUNTIME),new_store=str(ROOT/'store'),new_store_existed_before=False,qualified_new_results=[],decision='NEW_FORMAL_PRODUCTION',basis='D007真实handoff明确没有39f正式结果；D005/更早基线代码版本不同且保留。按D008必须新attempt/store，不作全盘目录搜索。',historical_D005='保留，比较用途；不能当39f当前结果'))
from supervise_production import processes,details,store_writers
procs=[details(pid) for pid in processes()];procs=[p for p in procs if p and Path(p['executable']).name in ['ts','dbaw','u2-kline-coverage-adapter-check','u2-observation-window-check']]
assert not procs,procs
write('PHYSICAL_PREFLIGHT.json',dict(checked_at=datetime.now(timezone.utc).isoformat(),source_commit_clean=True,source_files=len(files),binary_hashes=bins,no_visible_native_feature_process=not procs,native_processes=procs,store_writer_audit=store_writers(),source_root=str(REPO),runtime=str(RUNTIME),not_lock_acquisition_proof=True))
print('Physical source/binary/input/storage preflight passed',len(files),'files')
