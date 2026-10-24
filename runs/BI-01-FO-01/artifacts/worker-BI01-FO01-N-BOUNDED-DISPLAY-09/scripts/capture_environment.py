"""白名单环境/ignored读写证据，不输出环境变量或连接配置。"""
from pathlib import Path
import datetime,hashlib,json,subprocess
OUT=Path(__file__).resolve().parents[1]
RT=Path('/dwdhome/fy/cgpterm/artifacts/bi01-worker09-runtime')
aidata=Path('/dwdhome/fy/BASE_E6_2/mquant/aidata-bi01-fo01-n-bounded-display-r0035')
uplot=aidata.parent/'uplot'
def git(root,*args):return subprocess.check_output(['git','-C',str(root),*args],text=True).strip()
probe=RT/'RW_PROBE.txt'
assert hashlib.sha256(probe.read_bytes()).hexdigest()=='827d6b83e1272fac7826597f0064013ecd45aa9dbd48585721bd2fe03d1868b0'
ignored=subprocess.run(['git','-C','/dwdhome/fy/cgpterm','check-ignore','--quiet',str(probe)])
assert ignored.returncode==0
result={'observed_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'actual_turn_preflight':{'thread':'01a12557-eb30-74b3-b394-99c45b97c2b9','turn':'01a16f62-bfd4-7123-9c77-c6e7673bdd5d',
   'source':'本turn actual runtime/rollout上下文，非仅持久config推断',
   'sandbox':'danger-full-access','approval_policy':'never','reasoning_effort':'xhigh',
   'ignored_probe_readback':True,'probe_sha256':hashlib.sha256(probe.read_bytes()).hexdigest(),
   'probe_gitignored':True,'goal_created':False},
 'aidata':{'worktree':str(aidata),'branch':git(aidata,'branch','--show-current'),'head':git(aidata,'rev-parse','HEAD'),
   'worktree_status':git(aidata,'status','--short'),'base':'cbd0a1f9bf92d9d65e0ad00bfd1a9e3afb7c2cf0',
   'shared_origin_configuration_changed':False},
 'protected_uplot':{'path':str(uplot),'head':git(uplot,'rev-parse','HEAD'),
   'preexisting_tracked_dirty':['pfw.py'],'effective_pfw_sha256':hashlib.sha256((uplot/'pfw.py').read_bytes()).hexdigest(),
   'same_pfw_hash_as_start':hashlib.sha256((uplot/'pfw.py').read_bytes()).hexdigest()=='d8d42b9a27078262d157ece595eb195c29fa6c764a797484520c3e333cb2a2f6',
   'worker_writes':False,'clean_checkout_claimed':False},
 'runtime':'evidence/EXECUTION_RUNTIME.json',
 'reader_and_producer_qualification':'本单复用W02/W03锁定正常导出；未实例化/调用生产N，未fresh调用TIS N读者。原TIS3ff/FRP5154/workerADT cd5及原生成者身份沿原来源，不冒称本次新生产或仅凭checkout HEAD证明有效N读回。',
 'temporary_overlay':'/tmp/bi01-fo01-w03-runtime-20261022（只读）',
 'protected_sources_written':False,'shared_services_changed':False,'authentication_changed':False}
(OUT/'evidence/ENVIRONMENT.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'aidata_head':result['aidata']['head'],'ignored_readback':True,'protected_pfw_unchanged':result['protected_uplot']['same_pfw_hash_as_start']}))
