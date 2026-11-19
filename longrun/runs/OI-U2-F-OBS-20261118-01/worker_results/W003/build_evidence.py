from pathlib import Path
import hashlib
import json
import os
import subprocess

RUN = Path(__file__).resolve().parent
SOURCE = RUN/'source/observe-iterate'
RUN_ID = 'OI-U2-F-OBS-20261118-01'
COMMIT = 'f4f0e4b276b1118b779473c1fbe462bc7a64b358'
WORKER = f'codex:{RUN_ID}:worker:W1'
RETURN_TO = f'chatgpt:{RUN_ID}:executor:E1'
ORDER_REF = f'daowei2026/observe-iterate@dd919cca7df1203f7962888b4ecf8b7d24048c43:longrun/runs/{RUN_ID}/work_orders/W003/ORDER.json'
D_REL = f'longrun/runs/{RUN_ID}/artifacts/D/u2_f_caegraph_definition.py'
C_REL = f'longrun/runs/{RUN_ID}/artifacts/C/caegraph_display.py'
ENV = os.environ.copy()
ENV['GIT_OPTIONAL_LOCKS'] = '0'
ENV['PYTHONDONTWRITEBYTECODE'] = '1'


def git(*args):
    return subprocess.check_output(['git','-C',str(SOURCE),*args],env=ENV)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def save_json(relative,value):
    with (RUN/relative).open('x',encoding='utf8') as stream:
        stream.write(json.dumps(value,ensure_ascii=False,indent=2)+'\n')


order = json.loads((RUN/'inputs/ORDER.json').read_bytes())
directory = RUN/'inputs/referenced'
directory.mkdir(exist_ok=False)
refs = list(order['input_refs']) + [
    'daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:longrun/contracts/longrun_schema_v2.json',
    'daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:longrun/contracts/LONGRUN_PROTOCOL_V2.md',
]
referenced = []
for index,ref in enumerate(refs,1):
    repository_commit,relative = ref.split(':',1)
    repository,commit = repository_commit.split('@',1)
    assert repository == 'daowei2026/observe-iterate'
    raw = git('show',commit+':'+relative)
    path = directory/(f'{index:02d}_'+Path(relative).name)
    with path.open('xb') as stream:
        stream.write(raw)
    referenced.append({'ref':ref,'path':str(path),'bytes':len(raw),'sha256':sha(raw)})
    if relative == 'longrun/contracts/longrun_schema_v2.json':
        with (RUN/'inputs/longrun_schema_v2.json').open('xb') as stream:
            stream.write(raw)
save_json('inputs/referenced_input_manifest.json',referenced)
baseline = next(item for item in referenced if item['ref']==order['input_refs'][0])
assert Path(baseline['path']).read_bytes() == (RUN/'inputs/C0019_BASELINE.md').read_bytes()
signed = json.loads((RUN/'inputs/C0019_PRO_RETURN.json').read_bytes())
repository_commit,relative = signed['result_ref'].split(':',1)
repository,commit = repository_commit.split('@',1)
assert repository == 'daowei2026/observe-iterate'
assert git('show',commit+':'+relative) == (RUN/'inputs/C0019_REPORT.md').read_bytes()

head = git('rev-parse','HEAD').decode().strip()
diff = git('diff','--binary','HEAD')
status = git('status','--porcelain=v1','--untracked-files=all')
assert head == COMMIT and not diff and not status
for name,raw in (('repair.diff',diff),('final_git_status.txt',status),('final_head.txt',(head+'\n').encode())):
    with (RUN/name).open('xb') as stream:
        stream.write(raw)
sources = {}
for key,relative,commit in (
    ('final_script',D_REL,COMMIT),
    ('c3_script',C_REL,'508d494c964d5dabeaa1e7ea17bef908f749e9c8'),
):
    raw = (SOURCE/relative).read_bytes()
    assert raw == git('show',commit+':'+relative)
    sources[key] = {'path':str(SOURCE/relative),'ref':f'daowei2026/observe-iterate@{commit}:{relative}','bytes':len(raw),'sha256':sha(raw),'modified':False}
save_json('source_hashes.json',sources)

definition_path = RUN/'output/u2_f_caegraph/definition_run_report.json'
definition = json.loads(definition_path.read_bytes())
exit_code = int((RUN/'logs/w003_run.exit_code').read_text())
attempts = int((RUN/'logs/w003_run.attempt_count').read_text())
platform = json.loads((RUN/'logs/platform_entry.finished.json').read_bytes())
path_check = json.loads((RUN/'diagnostics/module_path_check.json').read_bytes())
assert definition['completed'] is False and definition['error_type'] == 'ModuleNotFoundError'
assert definition['error'] == "No module named 'mquant.tis.frp.fqv_kline_example'"
assert exit_code == 1 and attempts == 1

before_raw = (RUN/'logs/dev_shm_sem.before.tsv').read_bytes()
after_raw = (RUN/'logs/dev_shm_sem.after.tsv').read_bytes()
before = {line.split('\t',1)[0]:line for line in before_raw.decode().splitlines()}
after = {line.split('\t',1)[0]:line for line in after_raw.decode().splitlines()}
audit = {
    'run_id':RUN_ID,'work_order_id':'W003',
    'before_path':str(RUN/'logs/dev_shm_sem.before.tsv'),'after_path':str(RUN/'logs/dev_shm_sem.after.tsv'),
    'before_snapshot_exit_code':int((RUN/'logs/dev_shm_sem.before.exit_code').read_text()),
    'after_snapshot_exit_code':int((RUN/'logs/dev_shm_sem.after.exit_code').read_text()),
    'before_count':len(before),'after_count':len(after),
    'names_new_at_after_snapshot':sorted(after.keys()-before.keys()),
    'names_missing_at_after_snapshot':sorted(before.keys()-after.keys()),
    'same_names_with_changed_metadata':[name for name in sorted(before.keys() & after.keys()) if before[name]!=after[name]],
    'creation_or_deletion_events_during_D':'NOT_MEASURED',
    'attributable_residue':'No sem.* entries were observed in either snapshot; there is no observed residue to attribute.',
    'manual_semaphore_test_or_cleanup':False,
    'observation_limit':'Empty endpoint snapshots do not prove that no semaphores were created and removed during the D process lifetime.',
}
assert audit['before_snapshot_exit_code'] == audit['after_snapshot_exit_code'] == 0
assert not before_raw and not after_raw
save_json('semaphore_audit.json',audit)

blocker = {
    'run_id':RUN_ID,'work_order_id':'W003','parent_delegation_id':'D005',
    'factual_status':'BLOCKED','proposed_outcome_after_transport':'STOP',
    'blocking_stage':'D.main at line 677: declared make_features constructor import',
    'exception_type':definition['error_type'],'error_exact':definition['error'],'traceback':definition['traceback'],
    'D_attempt_count':attempts,'D_exit_code':exit_code,
    'actual_python_entry':(RUN/'logs/python_entry.txt').read_text().strip(),
    'actual_python_version':(RUN/'logs/python_version.txt').read_text().strip(),
    'normal_direct_entry':True,'standalone_SemLock_probe_attempt_count':0,
    'Landlock_used':False,'namespace_used':False,'sudo_used':False,'platform_patch':False,
    'finite_path_check':str(RUN/'diagnostics/module_path_check.json'),
    'unique_import_path_repair_established':False,
    'stop_basis':'No already configured replacement constructor path with proven identical semantics was established in the limited check. W003 section 9 requires returning to E when a unique mechanical repair is not established or would require platform/version changes.',
    'scope_limit':'The finite package check is not an exhaustive workspace or host search; no claim is made that the constructor or an F product is globally absent.',
    'F_constructed':False,'fields_json_existence':'NOT_CHECKED','f_rerun_called':False,'producer_called':False,'Q_or_V_read':False,
}
save_json('first_blocker.json',blocker)

checks = {
    'order_md_matches_dispatch_hash':sha((RUN/'inputs/ORDER.md').read_bytes())=='5a9582385a255a83ad1c3424677272a38c6ec17b1c42646933f07e75fa97b842',
    'order_json_matches_dispatch_hash':sha((RUN/'inputs/ORDER.json').read_bytes())=='5c37f421bd59568de87450408a154b619cceeaa25880b8e948a23eea724e8b73',
    'order_mirrors_match_exact_git_blobs':(RUN/'inputs/ORDER.md').read_bytes()==(RUN/'inputs/ACTIVE_ORDER_REMOTE.md').read_bytes() and (RUN/'inputs/ORDER.json').read_bytes()==(RUN/'inputs/ACTIVE_ORDER_REMOTE.json').read_bytes(),
    'baseline_and_report_mirrors_match_exact_git_blobs':True,
    'grant_matches_new_binding':json.loads((RUN/'authority_validation.json').read_bytes())['grant_matches_current_binding'] is True,
    'source_stage_success_at_D_commit':head==COMMIT and json.loads((RUN/'source_stage_report.json').read_bytes())['verification_passed'] is True,
    'source_worktree_clean':not diff and not status,
    'D_and_C3_original_bytes_preserved':all(item['modified'] is False for item in sources.values()),
    'one_direct_D_attempt':attempts==1,
    'actual_D_exit_code_is_1':exit_code==1,
    'definition_report_preserves_exact_import_failure':definition['completed'] is False and definition['error']==blocker['error_exact'],
    'same_failure_in_D_log':definition['error'] in (RUN/'logs/w003_run.log').read_text(),
    'no_unique_import_path_fix_established':path_check['unique_existing_import_path_repair_established'] is False,
    'semaphore_snapshots_succeeded_and_empty':audit['before_snapshot_exit_code']==0 and audit['after_snapshot_exit_code']==0 and not before_raw and not after_raw,
    'no_candidate_HTML':not (RUN/'output/u2_f_caegraph/u2_f_caegraph.html').exists(),
    'no_prepared_tables_or_plot_data':not (RUN/'output/u2_f_caegraph/prepared_tables').exists() and not (RUN/'output/u2_f_caegraph/plot_data').exists(),
}
assert all(checks.values())
save_json('evidence_checks.json',checks)

missing = [
    "运行时声明的 mquant.tis.frp.fqv_kline_example 构造模块无法导入；尚未确认语义一致的既有替代路径",
    'F 未构造，精确 fields.json 存在性与真实 F 表未检查',
    '候选 u2_f_caegraph.html 未生成；definition_run_report.json 已生成但 completed=false',
    'prepared_tables 与 plot_data 未生成',
    'E3 核图接受与正式数据导出准入尚未发生',
]
facts = {
    'run_id':RUN_ID,'work_order_id':'W003','parent_delegation_id':'D005','issuer_call_id':'C0019',
    'worker':WORKER,'return_to':RETURN_TO,'order_ref':ORDER_REF,
    'factual_status':'BLOCKED','proposed_outcome_after_transport':'STOP',
    'source_stage_report':str(RUN/'source_stage_report.json'),'source_root':str(SOURCE),'HEAD':head,
    'final_script':sources['final_script'],'candidate_html':None,
    'D_run_log':str(RUN/'logs/w003_run.log'),'D_attempt_count':attempts,'D_exit_code':exit_code,
    'D_started_at':(RUN/'logs/w003_run.started_at').read_text().strip(),'D_finished_at':(RUN/'logs/w003_run.finished_at').read_text().strip(),
    'D_independent_elapsed_precision':'NOT_MEASURED; timestamps bracket the command',
    'platform_entry_elapsed_seconds':platform['elapsed_seconds'],'platform_entry_timing_scope':platform['timing_scope'],
    'end_to_end_exact_duration':'UNKNOWN; preparation and evidence preservation are outside the platform entry timer',
    'actual_python_entry':blocker['actual_python_entry'],'actual_python_version':blocker['actual_python_version'],
    'definition_run_report':str(definition_path),'definition_completed':False,
    'repair_diff':str(RUN/'repair.diff'),'repair_diff_bytes':0,'D_C3_changed':False,
    'first_blocker':str(RUN/'first_blocker.json'),'finite_path_check':str(RUN/'diagnostics/module_path_check.json'),
    'semaphore_audit':str(RUN/'semaphore_audit.json'),'semaphore_before_count':0,'semaphore_after_count':0,
    'standalone_SemLock_probe_attempt_count':0,'manual_semaphore_creation_or_cleanup':False,
    'Landlock_used':False,'namespace_used':False,'sudo_used':False,'platform_patch':False,
    'F_constructed':False,'fields_json_existence':'NOT_CHECKED','f_rerun_called':False,'producer_called':False,'Q_or_V_read':False,
    'prepared_tables':None,'plot_data':None,'DATA_READY':False,
    'W001_or_W002_write_operations':False,'remote_push_performed':False,'Goal_created':False,'wake_or_new_executor_created':False,
    'formal_worker_return_signed':False,'transport_state':'AWAITING_CONTROLLER_PUBLICATION_AND_EXACT_REFS','missing':missing,
}
save_json('facts.json',facts)

report = f'''# W003 最小事实报告

run_id：{RUN_ID}
work_order_id：W003
parent_delegation_id：D005（当前 C0018 修订）
issuer_call_id：C0019
worker：{WORKER}
return_to：{RETURN_TO}
order_ref：{ORDER_REF}

状态：BLOCKED。正常入口直接运行 D 一次，得到新的真实构造模块导入阻断；未建立唯一可直接采用的机械修法，按原停止条件回 E。正式 Return 待运输后拟签认 outcome=STOP。
source staging：{RUN/'source_stage_report.json'}；SUCCESS，独立 detached HEAD={head}，D/C3 原件一致。
最终脚本：{SOURCE/D_REL}；HEAD={head}。
候选 HTML：无。
运行日志：{RUN/'logs/w003_run.log'}；环境入口完整输出另存 {RUN/'logs/environment.log'}。
D attempt count：1。
D 退出码：1，原值保存在 {RUN/'logs/w003_run.exit_code'}。
实际修改：D/C3 无；{RUN/'repair.diff'} 为 0 字节，{RUN/'final_git_status.txt'} 为空。
definition_run_report：{definition_path}；已生成，completed=false。
semaphore 事实：{RUN/'logs/dev_shm_sem.before.tsv'} 与 {RUN/'logs/dev_shm_sem.after.tsv'}；快照命令均退出 0，两份文件均为空。汇总见 {RUN/'semaphore_audit.json'}。

首个真实阻断：

```text
ModuleNotFoundError: No module named 'mquant.tis.frp.fqv_kline_example'
```

完整 D traceback：

```text
{definition['traceback'].rstrip()}
```

实际 D 命令：

```text
python longrun/runs/{RUN_ID}/artifacts/D/u2_f_caegraph_definition.py --output-dir {RUN/'output/u2_f_caegraph'}
```

实际 cwd={SOURCE}；Python={blocker['actual_python_entry']}，版本 {blocker['actual_python_version']}。运行复用原工单指定的 m3rc、已有 .runtime/python-deps、TLS 库和 W003 cache 重定向，直接启动原 D；没有 Landlock、boundary_runner、unshare、任何 namespace、sudo、mount、平台 patch 或独立 SemLock probe，没有安装依赖、新建环境或切换平台版本。环境入口的 nif2 DNS 输出与回退过程完整留在 environment.log；D 确已启动，因此该环境输出不是本轮最终致命阻断。

有限静态路径核对只涉及当前 mquant/tis/frp 包、声明的构造模块及对应类文件路径、包直接 13 个条目和 __init__.py；没有执行额外平台模块或递归搜索整个工作区。当前检查路径未发现 fqv_kline_example.py 或同名包，包初始化文件不提供 make_features；同范围也未发现 CommonPriceTurnGroupCandidates 的所查文件/目录。证据见 {RUN/'diagnostics/module_path_check.json'} 与 initializer 原样快照。这不是全工作区或全主机不存在相关代码的断言，也不是精确 F 产品不存在的证据。

未确认一个已配置且语义一致的替代导入路径。Worker 未从远端补装构造模块、未引入另一 TIS/平台版本、未修改平台源码，也没有用其他构造器或近似值替换 F。按照 W003 第九节“正确修法不唯一，或无法判断语义影响”的边界，停止并回原 E1；没有第二次 D 运行。

D 已到达 make_features 的 import，但在函数可用之前失败；F 未构造、fields.json 未检查、真实 F 表未读取。没有调用 f.rerun 或全历史 producer，没有读取 Q/V，没有生成 prepared_tables、plot_data 或候选 HTML，没有 DATA_READY 或正式取数准入。

本轮未由 wrapper 手工创建测试 semaphore 或删除任何 sem.*。两次端点快照均未观察到 sem.*，没有观察到可归属残留；这不证明进程存续期间未创建并正常删除 semaphore，也不构成逐次 IPC 创建/删除审计。没有读写非 sem.* 的 /dev/shm 对象，没有扩大清理动作。

D 命令时间边界为 {facts['D_started_at']} 至 {facts['D_finished_at']}；没有独立测量 D 单独 elapsed。平台入口（包含环境初始化、D 和审计快照）墙钟 {platform['elapsed_seconds']:.6f} 秒为独立实测，不能把它称为纯 D 耗时；此前准备、staging、输入核对和之后封存的完整端到端精确总成本未知。

未写 W001/W002、其他 Run、平台源码、生产数据或外部 symlink 目标；未推送 source checkout；未创建 Goal、计划休眠、后台唤醒或新执行器。W001/W002 历史保留。

完整本地事实、日志、报告、源码状态、有限路径核对和 semaphore 记录均将在正文运输包中逐项保存路径、字节数与 SHA-256。正式 result_ref 和新增 manifest.ref 待主控原样发布后提供真实 commit；D/C3 可复用既有精确 refs。当前准备稿不是正式 worker_return。收到真实 refs 后，在同一 W003 下核验并签认，回原 executor:E1，续接 D005 / WI-E / M-E；本 Worker 不替 E 作专业分类或图接受判断。
'''
with (RUN/'FACT_REPORT.md').open('x',encoding='utf8') as stream:
    stream.write(report)
save_json('RETURN_PREPARATION.json',{
    'preparation_format':'local-only; not a schema-valid formal Worker Return','state':'AWAITING_TRANSPORT_PUBLICATION',
    'target_schema_ref':'daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:longrun/contracts/longrun_schema_v2.json','target_definition':'#/$defs/worker_return',
    'fixed_fields':{'schema':'longrun-worker-return/v2','run_id':RUN_ID,'work_order_id':'W003','order_ref':ORDER_REF,'worker':WORKER,'return_to':RETURN_TO,'outcome':'STOP','missing':missing},
    'existing_manifest_entries':{key:{'ref':value['ref'],'sha256':value['sha256']} for key,value in sources.items()},
    'awaiting_fields':['result_ref','manifest entries for newly published evidence'],'result_local_path':str(RUN/'FACT_REPORT.md'),
    'parent_delegation_id':'D005','delegation_ref':order['delegation_ref'],
    'publication_authority':'主控运输原样证据，Worker 不推送 source checkout。',
    'next_action':'接收真实 ref/hash 映射后核验并签认同一 W003；不重跑 D、producer 或诊断。',
})
print(json.dumps({'factual_status':'BLOCKED','proposed_outcome_after_transport':'STOP','D_attempt_count':attempts,'D_exit_code':exit_code,'first_blocker':definition['error'],'semaphore_before_count':0,'semaphore_after_count':0,'evidence_checks_passed':len(checks),'report_path':str(RUN/'FACT_REPORT.md')},ensure_ascii=False))
