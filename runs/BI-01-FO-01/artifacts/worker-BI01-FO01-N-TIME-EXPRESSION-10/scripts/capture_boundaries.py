"""只输出本单必要安全字段；不读取或打印认证/完整环境/服务日志。"""
from pathlib import Path
import datetime,hashlib,json,os,subprocess
import psutil
OUT=Path(__file__).resolve().parents[1]
RT=Path(os.environ.get('BI01_W10_RUNTIME','/dwdhome/fy/cgpterm/artifacts/bi01-worker10-runtime'))
candidate=Path('/dwdhome/fy/BASE_E6_2/mquant/aidata-bi01-fo01-n-time-expression-r0038')
uplot=Path('/dwdhome/fy/BASE_E6_2/mquant/uplot')
def git(repo,*args):return subprocess.check_output(['git','-C',str(repo),*args],text=True).strip()
owned=[]
for p in psutil.process_iter(['pid','cmdline']):
 try:
  cmd=p.info['cmdline'] or []
  if any('ipykernel' in str(a) for a in cmd) and any(str(RT/'jupyter') in str(a) for a in cmd):owned.append(p.pid)
 except psutil.Error:pass
assert not owned,'本单自有kernel未关闭'
life=json.loads((RT/'FRONTEND_EPISODE_LIFECYCLE.json').read_text())
assert life['owned_server_exited'] and life['remaining_owned_kernels']==0
expected_pfw='d8d42b9a27078262d157ece595eb195c29fa6c764a797484520c3e333cb2a2f6'
pfw_hash=hashlib.sha256((uplot/'pfw.py').read_bytes()).hexdigest();assert pfw_hash==expected_pfw
result=dict(at=datetime.datetime.now(datetime.timezone.utc).isoformat(),
 actual_turn='01a17031-7be5-7e62-87c6-adfcd000ad96',actual_access=dict(sandbox='danger-full-access',approval_policy='never',reasoning='xhigh',
 source='本turn原生只读turn_context已核；另有ignored有限写读回，不用旧持久配置替代'),
 ignored_RW_sha256=hashlib.sha256((RT/'RW_PROBE.txt').read_bytes()).hexdigest(),
 aidata=dict(base='25a9fd8b1333aafd4c56fd1b288e7f8d3c8c3113',head=git(candidate,'rev-parse','HEAD'),branch=git(candidate,'branch','--show-current'),
 worktree=str(candidate),status=git(candidate,'status','--short'),github_target='https://github.com/daowei2026/aidata.git',legacy_origin_unchanged=True),
 uplot=dict(head=git(uplot,'rev-parse','HEAD'),preexisting_status=git(uplot,'status','--short'),effective_pfw_sha256=pfw_hash,worker_writes=False),
 protected_repositories_written=False,shared_service_or_DAO_or_auth_write=False,production_read_or_recompute=False,
 old_W09_or_other_service_resumed=False,own_Jupyter_closed=True,remaining_owned_kernels=0,
 newly_created_Goal_timer_daemon_or_future_wake=False,qualification='有限Worker10技术边界；不代签Pro/管理/工作3/4')
(RT/'RUNTIME_BOUNDARIES.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(aidata_head=result['aidata']['head'],uplot_pfw_unchanged=True,own_kernels=0),ensure_ascii=False))
