"""D002 首轮X。仅当前代码正式实例/技术上游；同一指定flock，独立P1存储。"""
import datetime
import fcntl
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import time
import traceback

BASE=Path('/dwdhome/fy/BASE_E6_2_copy/artifacts/OI-EAW-P1-ATTACK-STAT-20261124-01/D002/C0007')
ATTEMPT=BASE.parent/'formal-attempt-A03'
STORE=ATTEMPT/'store'
LOCK=Path('/dwdhome/fy/cgpterm/artifacts/wall-f-closure-20261122/FORMAL_PRODUCTION.lock')
HEAD='179016111ed0394f92025313e46bd13534932a74'
ATTEMPT.mkdir(parents=True,exist_ok=False)
PROGRESS=ATTEMPT/'execution_progress.json'
EVENTS=ATTEMPT/'execution_events.jsonl'
state={'run_id':'OI-EAW-P1-ATTACK-STAT-20261124-01','call_id':'C0007','delegation_id':'D002','attempt_id':'A03','scope':'FORMAL_2021_RB_M','started_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'lock_path':str(LOCK),'lock_acquired':False,'lock_released':False,'feature_execution_started':False,'formal_complete':False,'feature_results':[],'errors':[],'store_root':str(STORE)}
state['sys_executable']=sys.executable
state['actual_cwd']=str(Path.cwd().resolve())
state['invocation_ref']='daowei2026/observe-iterate@127585f808552a18094a873cf7cf9d80b511d186:longrun/runs/OI-EAW-P1-ATTACK-STAT-20261124-01/calls/C0007/INVOCATION.json'
state['origin_ref']='daowei2026/observe-iterate@0d2137442b76f872f2b38eb4e3cf3d16d98303f2:longrun/runs/OI-EAW-P1-ATTACK-STAT-20261124-01/calls/C0006/PRO_RETURN.json'

def now():return datetime.datetime.now(datetime.timezone.utc).isoformat()
def write_json(path,value):
 path.parent.mkdir(parents=True,exist_ok=True)
 temp=path.with_name(path.name+'.tmp')
 temp.write_text(json.dumps(value,ensure_ascii=False,indent=2,default=str)+'\n')
 os.replace(temp,path)
def event(stage,**extra):
 row={'at':now(),'stage':stage,**extra}
 with EVENTS.open('a') as f:f.write(json.dumps(row,ensure_ascii=False,default=str)+'\n')
 state.update({'last_update':row['at'],'current_stage':stage,**extra})
 write_json(PROGRESS,state)
 print(json.dumps(row,ensure_ascii=False,default=str),flush=True)
def task_update(status,action,next_action,blocker=None):
 args=['python','/home/dw/.agents/skills/long-task-status/scripts/task_status.py','update','--root','/dwdhome/fy/BASE_E6_2_copy/mquant/tis','--task-id','oi-eaw-p1-attack-d002-x-20261124','--status',status,'--action',action,'--next-action',next_action]
 if blocker:args+=['--blocker',blocker]
 elif status=='running':args+=['--clear-blocker']
 result=subprocess.run(args,capture_output=True,text=True)
 if result.returncode:event('STATUS_CLI_WARNING',error=result.stderr[-1000:])
def encode(v):
 if v is None or isinstance(v,(str,int,float,bool)):return v
 if hasattr(v,'items'):return {str(k):encode(x) for k,x in v.items()}
 if isinstance(v,(list,tuple)):return [encode(x) for x in v]
 if hasattr(v,'val'):return encode(v.val)
 if hasattr(v,'P'):return {'type':type(v).__module__+'.'+type(v).__name__,'parameters':encode(v.P)}
 return str(v)

fd=None
try:
 if STORE.exists():raise RuntimeError('ATTEMPT_STORE_ALREADY_EXISTS_DO_NOT_OVERWRITE')
 fd=os.open(LOCK,os.O_RDWR)
 st=os.fstat(fd)
 preflight=json.loads((BASE/'evidence/x_preflight-A03.json').read_text())
 assert st.st_dev==preflight['lock']['device'] and st.st_ino==preflight['lock']['inode']
 state['lock_identity']={'device':st.st_dev,'inode':st.st_ino,'bytes_before':st.st_size,'sha256_before':hashlib.sha256(LOCK.read_bytes()).hexdigest()}
 event('WAITING_SHARED_PRODUCTION_LOCK')
 task_update('waiting_external','等待原FORMAL_PRODUCTION.lock；未运行Feature','原锁释放后实际获取，再开始生产','SharedProductionLock_HELD')
 wait_start=time.monotonic()
 deadline=wait_start+600
 last_notice=wait_start
 while True:
  try:
   fcntl.flock(fd,fcntl.LOCK_EX|fcntl.LOCK_NB)
   break
  except BlockingIOError:
   if time.monotonic()>=deadline:raise TimeoutError('SHARED_PRODUCTION_LOCK_STILL_HELD_AFTER_600_SECONDS')
   if time.monotonic()-last_notice>=30:
    event('WAITING_SHARED_PRODUCTION_LOCK',lock_wait_seconds=round(time.monotonic()-wait_start,3))
    task_update('waiting_external','原生产锁仍由其它生产者持有；未写共享结果','等原锁释放，不中断持有者','SharedProductionLock_HELD')
    last_notice=time.monotonic()
   time.sleep(2)
 state['lock_acquired']=True
 state['lock_acquired_at']=now()
 state['lock_wait_seconds']=round(time.monotonic()-wait_start,3)
 assert LOCK.stat().st_ino==st.st_ino and LOCK.stat().st_dev==st.st_dev
 assert subprocess.check_output(['git','-C','/dwdhome/fy/BASE_E6_2_copy/mquant/tis','rev-parse','HEAD'],text=True).strip()==HEAD
 assert not subprocess.check_output(['git','-C','/dwdhome/fy/BASE_E6_2_copy/mquant/tis','status','--short','--untracked-files=no'],text=True).strip()
 event('SHARED_PRODUCTION_LOCK_ACQUIRED')
 task_update('running','已取得指定flock，执行当前版本正式X','物化当前exact技术上游并运行Attack')

 import numpy as np
 import pandas as pd
 from mquant.quant import OptContext
 from m3tt import CurrTradeSet,CurrSymbol
 from mquant.frame import CurrCalendar,TmpStoreEnv,CurrCalType,CurrFaoCache,CalType
 from mquant.frame.core.app.env import StraEnv
 from mquant.frame.lang.general import OptStoreRule
 from mquant.tis.hf.prel0.p1_dba_export import P1DbaExportMixin
 from mquant.tis.hf.prel0.p1_product_receipt import load_p1_product_receipt,feature_code_fingerprint,validate_product_artifact
 import mquant.tis.hf.prel0.attack_flow_assembler as am
 import mquant.tis.hf.prel0.wall_assembler as wm
 import mquant.tis.hf.prel0.pressure_big_deal as fm
 from mquant.tis.t0.gen.cc import SubContinuousContract,AmountThreshold
 from mquant.tis.hf.qt import VolQuant
 assert OptStoreRule.get(required=False) is None
 expected_code={'wall':feature_code_fingerprint(wm.__file__,wm.run_wall_assembler_replay),'tactical':feature_code_fingerprint(fm.__file__,fm.compute_pressure_big_deal_chunk),'structural':feature_code_fingerprint(fm.__file__,fm.compute_pressure_big_deal_chunk),'attack':feature_code_fingerprint(am.__file__,am.run_attack_flow_assembler_replay)}
 for module in (am,wm,fm):assert Path(module.__file__).resolve().is_relative_to(Path('/dwdhome/fy/BASE_E6_2_copy/mquant/tis'))
 state['actual_module_files']={module.__name__:str(Path(module.__file__).resolve()) for module in (am,wm,fm)}
 source_features=[SubContinuousContract(),AmountThreshold(n=30),VolQuant(freq='1d',n=30,quantile=0.997)]
 cal_overrides={x.__class__.__name__:'cal' for x in source_features}
 state['source_feature_cal_type_overrides']=cal_overrides
 state['expected_code_fingerprints']=expected_code
 context=OptContext({'sof_name':'TA_updto20240229_DBA','startDay':'2021-01-01','endDay':'2021-12-31'})
 kinds={'wall':['wall_lifecycle'],'tactical':['directed_large_deal_stream'],'structural':['directed_large_deal_stream'],'attack':['attack_segment','attack_formation_evidence','wall_relation_barrier']}

 def digest_frame(frame):
  result={}
  for field,values in [('__index__',frame.index.values)]+[(str(name),frame[name].values) for name in frame.columns]:
   ar=np.asarray(values)
   if ar.dtype.hasobject:raise TypeError('Formal artifact contains object dtype: '+field)
   digest=hashlib.sha256()
   digest.update(str(ar.dtype).encode());digest.update(str(ar.shape).encode())
   for start in range(0,ar.size,262144):digest.update(np.ascontiguousarray(ar[start:start+262144]).tobytes())
   result[field]=digest.hexdigest()
  return result

 for symbol in ('rb','m'):
  with CurrFaoCache(),CurrTradeSet(context.sof),CurrSymbol(symbol),CurrCalendar('night_end_at_2300'),TmpStoreEnv(rule=P1DbaExportMixin,store_dir=str(STORE)),CurrCalType(cal_overrides):
   for source in source_features:assert StraEnv.rcal_type(source)==CalType.Cal
   attack=am.AttackFlowAssembler()
   features={'wall':attack.P.wall,'tactical':attack.P.directed_large_deal_tactical,'structural':attack.P.directed_large_deal_structural,'attack':attack}
   symbol_success={}
   for name,feature in features.items():
    location=Path(feature.full_dir).resolve()
    rec={'symbol':symbol,'feature':name,'constructor_parameters':encode(feature.P),'ppdict':encode(feature.ppdict),'ppid':str(feature.ppid),'full_dir':str(location),'expected_code_version':expected_code[name],'started_at':now(),'status':'NOT_STARTED'}
    state['feature_results'].append(rec)
    if not location.is_relative_to(STORE.resolve()) or feature.backup_full_dirs:raise RuntimeError('UNEXPECTED_P1_WRITE_SURFACE')
    if location.exists():raise RuntimeError('EXISTING_TARGET_DO_NOT_OVERWRITE:'+str(location))
    if name=='attack':
     if not all(k in symbol_success for k in ('wall','tactical','structural')):
      rec.update(status='BLOCKED_MISSING_CURRENT_UPSTREAM',finished_at=now());event('ATTACK_NOT_RUN_MISSING_UPSTREAM',symbol=symbol,feature=name);continue
     scopes=[symbol_success[k]['receipts'][0]['source_scope'] for k in ('wall','tactical','structural')]
     if any(scope!=scopes[0] for scope in scopes[1:]):
      rec.update(status='BLOCKED_EXACT_UPSTREAM_SOURCE_SCOPE_MISMATCH',upstream_source_scopes=dict(zip(('wall','tactical','structural'),scopes)),finished_at=now())
      event('ATTACK_NOT_RUN_EXACT_SOURCE_SCOPE_MISMATCH',symbol=symbol,feature=name);continue
    state['feature_execution_started']=True
    event('FEATURE_RUN_STARTED',symbol=symbol,feature=name)
    run_started=time.monotonic()
    try:
     output=feature.run(CalType.Gen).F
     rec['feature_elapsed_seconds']=round(time.monotonic()-run_started,3)
     rec['receipts']=[]
     for kind in kinds[name]:
      receipt=load_p1_product_receipt(feature,kind)
      assert receipt['status']=='success'
      assert receipt['code_version']==expected_code[name]
      assert Path(receipt['artifact_location']).resolve()==location
      rec['receipts'].append(receipt)
      write_json(ATTEMPT/'receipts'/symbol/name/(kind+'.json'),receipt)
     loaded=feature.Dao.loadWith(str(location))
     assert loaded is not None and set(loaded)==set(output)
     rec['tables']=[]
     for key in sorted(loaded):
      before=output[key];after=loaded[key]
      assert before.shape==after.shape and before.index.equals(after.index)
      assert list(before.columns)==list(after.columns)
      assert list(map(str,before.dtypes))==list(map(str,after.dtypes))
      expected_digest=digest_frame(before)
      actual_digest=digest_frame(after)
      assert expected_digest==actual_digest
      rec['tables'].append({'key':key,'rows':int(after.shape[0]),'columns':list(map(str,after.columns)),'dtypes':dict(zip(map(str,after.columns),map(str,after.dtypes))),'first_index':None if after.empty else str(after.index[0]),'last_index':None if after.empty else str(after.index[-1]),'full_readback_digest':actual_digest,'matches_returned_result':True})
     for receipt in rec['receipts']:validate_product_artifact(receipt,dict(loaded))
     rec.update(status='EXECUTED_AND_FULL_READBACK_VERIFIED',finished_at=now())
     symbol_success[name]=rec
     event('FEATURE_RUN_AND_READBACK_COMPLETE',symbol=symbol,feature=name,table_count=len(rec['tables']))
    except Exception as exc:
     chain=[];error=exc
     while error is not None:
      chain.append({'type':type(error).__name__,'message':str(error)[:4000]});error=error.__cause__
     rec.update(status='EXECUTION_OR_READBACK_FAILED',finished_at=now(),exception_chain=chain)
     state['errors'].append({'symbol':symbol,'feature':name,'exception_chain':chain})
     (ATTEMPT/(symbol+'-'+name+'-traceback.txt')).write_text(traceback.format_exc())
     event('FEATURE_RUN_FAILED',symbol=symbol,feature=name,error=chain[-1])
 state['formal_complete']=all(any(x['symbol']==symbol and x['feature']=='attack' and x['status']=='EXECUTED_AND_FULL_READBACK_VERIFIED' for x in state['feature_results']) for symbol in ('rb','m'))
 event('FORMAL_X_COMPLETE' if state['formal_complete'] else 'FORMAL_X_INCOMPLETE')
except Exception as exc:
 state['errors'].append({'stage':state.get('current_stage'),'type':type(exc).__name__,'message':str(exc)[:4000]})
 (ATTEMPT/'runner-traceback.txt').write_text(traceback.format_exc())
 event('RUNNER_STOPPED_WITH_RECORDED_GAP',error_type=type(exc).__name__,error_message=str(exc)[:4000])
finally:
 if fd is not None:
  if state['lock_acquired']:
   state['lock_identity']['bytes_after']=LOCK.stat().st_size
   state['lock_identity']['sha256_after']=hashlib.sha256(LOCK.read_bytes()).hexdigest()
   fcntl.flock(fd,fcntl.LOCK_UN)
   state['lock_released']=True
   state['lock_released_at']=now()
  os.close(fd)
 state['finished_at']=now()
 write_json(ATTEMPT/'execution_result.json',state)
 event('RUNNER_FINISHED',formal_complete=state['formal_complete'],lock_released=state['lock_released'])
 if not state['formal_complete']:
  if state['feature_execution_started']:task_update('blocked','正式X有真实未完成项，保留全部当前结果与错误','原manager消费准确绑定与恢复条件','FormalXIncomplete')
  elif any(x.get('type')=='TimeoutError' for x in state['errors']):task_update('waiting_external','本次未取得原生产锁，未运行Feature','原锁释放后续接同D002生产','SharedProductionLock_HELD')
  else:task_update('blocked','正式X工程前检或运行环境有记录的缺口','核对真实错误后在原D002续接','FormalXEngineeringGap')
