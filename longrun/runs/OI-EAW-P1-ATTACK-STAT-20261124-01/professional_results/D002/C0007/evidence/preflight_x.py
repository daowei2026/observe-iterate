"""D002 只读运行配置核验；禁止任何Feature.run，不取得长期生产锁。"""
import contextlib
import datetime
import fcntl
import hashlib
import io
import json
import os
from pathlib import Path
import subprocess

BASE=Path('/dwdhome/fy/BASE_E6_2_copy/artifacts/OI-EAW-P1-ATTACK-STAT-20261124-01/D002/C0007')
STORE=BASE.parent/'formal-attempt-A03'/'store'
result={'call_id':'C0007','attempt_id':'A03','probe_kind':'X_READONLY_PREFLIGHT','feature_executed':False,'verified_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'cwd':str(Path.cwd().resolve()),'store_root':str(STORE),'symbols':{},'errors':[]}
with contextlib.redirect_stdout(io.StringIO()),contextlib.redirect_stderr(io.StringIO()):
 from mquant.frame.lang.internal.base import AbsFao
 def forbidden(*args,**kwargs):raise RuntimeError('READ_ONLY_PREFLIGHT_FORBIDS_FEATURE_RUN')
 AbsFao.run=forbidden
 AbsFao.rerun=forbidden
 from mquant.quant import OptContext
 from m3tt import CurrTradeSet,CurrSymbol
 from mquant.frame import CurrCalendar,TmpStoreEnv,CalType,CurrCalType
 from mquant.frame.lang.general import OptStoreRule
 from mquant.frame.core.app.env import StraEnv
 from mquant.tis.hf.prel0.p1_dba_export import P1DbaExportMixin
 import mquant.tis.hf.prel0.attack_flow_assembler as attack_module
 from mquant.tis.t0.gen.cc import SubContinuousContract,AmountThreshold
 from mquant.tis.hf.qt import VolQuant
 context=OptContext({'sof_name':'TA_updto20240229_DBA','startDay':'2021-01-01','endDay':'2021-12-31'})
 attack=attack_module.AttackFlowAssembler()
 sources={'SubContinuousContract':SubContinuousContract(),'AmountThreshold':AmountThreshold(n=30),'VolQuant':VolQuant(freq='1d',n=30,quantile=0.997)}
 result['market_source_cal_type_overrides']={v.__class__.__name__:'cal' for v in sources.values()}
 result['p1_readonly_safe_storage_mechanism']='TmpStoreEnv(rule=P1DbaExportMixin, store_dir=本Run A03/store)，仅改产物位置，不改实例参数或代码'
 result['opt_store_rule_active']=OptStoreRule.get(required=False) is not None
 for symbol in ('rb','m'):
  with CurrTradeSet(context.sof),CurrSymbol(symbol),CurrCalendar('night_end_at_2300'):
   row={'source_sof_ori_dir':str(context.sof.ori_dir),'resolved_start':str(context.sof.startDay),'resolved_end':str(context.sof.endDay),'calendar':'night_end_at_2300','p1':{},'source_features':{}}
   features={'wall':attack.P.wall,'tactical':attack.P.directed_large_deal_tactical,'structural':attack.P.directed_large_deal_structural,'attack':attack}
   for name,feature in features.items():
    default=str(feature.full_dir)
    with TmpStoreEnv(rule=P1DbaExportMixin,store_dir=str(STORE)):
     isolated=Path(feature.full_dir).resolve()
     backups=list(feature.backup_full_dirs)
     row['p1'][name]={'ppid':str(feature.ppid),'type':type(feature).__module__+'.'+type(feature).__name__,'default_full_dir':default,'isolated_full_dir':str(isolated),'backup_full_dirs':backups,'gfull_dir':feature.gfull_dir,'isolated_target_exists':isolated.exists(),'isolated_within_run':isolated.is_relative_to(STORE.resolve())}
     assert isolated.is_relative_to(STORE.resolve())
     assert not backups,'未获准覆盖外部备份结果'
   for name,feature in sources.items():
    row['source_features'][name]={'type':type(feature).__name__,'ppid':str(feature.ppid),'full_dir':str(feature.full_dir),'cal_type_during_run':'cal：只计算读取，不保存市场基础Feature缓存'}
   result['symbols'][symbol]=row
 result['attack_ppdict']=attack.ppdict
 with CurrCalType({v.__class__.__name__:CalType.Cal for v in sources.values()}):
  resolved={}
  for name,source in sources.items():
   with StraEnv(attack,CalType.Gen),StraEnv(source,None):
    actual=StraEnv.rcal_type(source)
    assert actual==CalType.Cal,(name,actual)
    resolved[name]={'proxy_class':type(source).__name__,'resolved_class':source.__class__.__name__,'cal_type':actual.value}
  result['verified_nested_market_source_cal_types']=resolved
result['tis_head']=subprocess.check_output(['git','-C','/dwdhome/fy/BASE_E6_2_copy/mquant/tis','rev-parse','HEAD'],text=True).strip()
assert result['tis_head']=='179016111ed0394f92025313e46bd13534932a74'
lock='/dwdhome/fy/cgpterm/artifacts/wall-f-closure-20261122/FORMAL_PRODUCTION.lock'
fd=os.open(lock,os.O_RDWR)
try:
 st=os.fstat(fd);result['lock']={'path':lock,'device':st.st_dev,'inode':st.st_ino,'bytes_before':st.st_size}
 try:
  fcntl.flock(fd,fcntl.LOCK_EX|fcntl.LOCK_NB);result['lock']['state']='AVAILABLE_PROBE_RELEASED';fcntl.flock(fd,fcntl.LOCK_UN)
 except BlockingIOError:result['lock']['state']='HELD'
finally:os.close(fd)
(BASE/'evidence').mkdir(parents=True,exist_ok=True)
(BASE/'evidence/x_preflight-A03.json').write_text(json.dumps(result,ensure_ascii=False,indent=2,default=str)+'\n')
print(json.dumps({'evidence':str(BASE/'evidence/x_preflight-A03.json'),'lock':result['lock'],'all_targets_isolated':all(v['isolated_within_run'] for s in result['symbols'].values() for v in s['p1'].values()),'feature_executed':False},ensure_ascii=False))
