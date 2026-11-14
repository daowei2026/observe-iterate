from pathlib import Path
import sys,json,os,hashlib
ROOT=Path('/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D003/W003');sys.path.insert(0,str(ROOT/'tools'));import runtime as w
w.guard();stamp=w.utc();A=ROOT/'artifacts';order=json.loads((ROOT/'input/C0011-remote-work_orders--W003--ORDER.json').read_text());launch=json.loads((ROOT/'receipts/r0a-positive-launcher.json').read_text());trace=json.loads((A/'FULL_WRITE_TRACE_REVIEW.json').read_text());commands=[json.loads(s) for s in (ROOT/'logs/COMMAND_LOG.jsonl').read_text().splitlines()];run=next(o for o in commands if o['id']=='r0a-positive');assert run['exit_code']==73 and launch['calls']==[] and launch['status']=='LAUNCHER_FAILED'
assert hashlib.sha256((ROOT/'tools/landlock_launcher.py').read_bytes()).hexdigest()==launch['script_sha256']
def doc(name,text):p=A/name;assert not p.exists();p.write_text(text)
failed_line=next(i for i,line in enumerate((ROOT/'tools/landlock_launcher.py').read_text().splitlines(),1) if 'if fd==0:assert not writable' in line)
probes=[{'number':i,'requirement':name,'status':'NOT_EXECUTED_LAUNCHER_REJECTED_BEFORE_POLICY'} for i,name in enumerate(['inside-root create/write/rename/remove','outside nonexistent sentinel kernel rejection','shared FRP nonexistent temp create denied at open','actual HOME/CODEX unchanged and readable; new create denied','child/grandchild inheritance','symlink escape rejection','inherited writable FD handling verified','network socket/connect denied or full offline proof','all probes covered by complete trace'],1)]
probes[6]['status']='FAIL_BEFORE_KERNEL_POLICY';probes[6]['detail']='fd0 is writable /dev/null (O_RDWR); launcher required read-only stdin and rejected it. It did not finish enumerating/closing other inherited FDs.'
probes[8]['detail']='Full trace covers the attempted launcher only; probe was never execed.'
confinement={'record_type':'W003_WRITE_CONFINEMENT_REPORT','utc':stamp,'outcome':'STOP','status':'RECOVERY_STOP_WRITE_CONFINEMENT','write_confinement_pass':False,'attempts':1,'automatic_retry_or_parameter_change':False,'failure':{'stage':'pre-enforcement inherited-FD inspection','launcher_exit_code':73,'type':'AssertionError','source':str(ROOT/'tools/landlock_launcher.py'),'line':failed_line,'expression':'if fd==0:assert not writable','fd':0,'path':'/dev/null','actual_F_GETFL':'O_RDWR|O_LARGEFILE','actual_trace_line':1055,'integration_cause':'runtime.py subprocess.Popen(stdin=subprocess.DEVNULL) supplied a writable /dev/null FD. The launcher deliberately required stdin read-only and failed closed.','worker_implementation_integration_issue':True},'kernel_policy':{'candidate':'Python -I -S -B/ctypes Landlock ABI6 plus seccomp','expected_ABI':6,'ABI_observed_this_W003':None,'PR_SET_NO_NEW_PRIVS_called':False,'landlock_ruleset_created':False,'landlock_rule_added':False,'landlock_restrict_self_called':False,'seccomp_installed':False,'recorded_kernel_policy_calls':launch['calls'],'write_allow_root_candidate':str(ROOT),'write_exceptions':[],'candidate_code_executed_to_installation':False},'HOME':'/home/dw','CODEX_HOME':'/home/dw/.codex','HOME_or_CODEX_HOME_reset':False,'explicit_task_directories':launch['explicit_task_directories'],'probes':probes,'outside_sentinel_controller_preconfirmation':{'path':'/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D003/.W003-deny-outside-240810-46501758','required_by':'PHASE0_RECOVERY_PLAN_C0010.md §2.2','requested_in_original_chat':True,'received_before_terminal_STOP':False,'dependent_negative_probe_executed':False,'role_in_outcome':'Additional unfulfilled negative-probe prerequisite; not substituted for the earlier observed fd0 failure.'},'raw_launcher_receipt':w.filefact(ROOT/'receipts/r0a-positive-launcher.json'),'full_trace_review':str(A/'FULL_WRITE_TRACE_REVIEW.json'),'observed_successful_outside_writes_in_failed_launch_trace':0,'global_or_future_zero_external_writes_proven':False,'downstream_R0B_R0C_entered':False,'conclusion_zh':'当前尝试尚未安装 kernel restriction。拒绝 writable fd0 是实测失败终点；不可把 fail-closed 当 confinement PASS，不修改 launcher/runtime 后重试。'}
w.save('artifacts/WRITE_CONFINEMENT_REPORT.json',confinement)
closure={'record_type':'W003_OFFLINE_CLOSURE_REPORT','utc':stamp,'status':'NOT_ATTEMPTED_R0A_GATE','offline_closure_pass':False,'selected_candidate':None,'reason':'R0-A 在安装 kernel restriction 前终止；ORDER 禁止进入 R0-B。','candidates':[{'id':'E','declaration':'exact frp stack.yaml / lts-18.28','status':'NOT_INVESTIGATED_THIS_W003'},{'id':'B','declaration':'BASE overlay / lts-22.24 / historical observed GHC9.4.8','status':'NOT_INVESTIGATED_THIS_W003'}],'current_compiler_or_package_db_commands':0,'current_package_db_paths_hashes_sizes':None,'current_transitive_package_ids_versions':None,'current_missing_dependencies':None,'minimum_rebuild_set':None,'exact_base_compatibility_proven':False,'offline_no_network_proven_for_future_closure':False,'historical_W002_facts_reused_as_current_measurements':False,'candidate_environments_mixed':False,'deferred_exact_git_inputs':{'count':8,'source':'input/W003-input-mirror-index.json','read_this_W003':False,'reason':'未进入允许的 confined closure/staging 阶段；未运行 git 或读取这八个源码 blob。'},'missing':['兼容的单一 resolver/compiler/工具哈希','snapshot/global/local package DB 与传递依赖完整映射','local packages exact HEAD/tree/cabal 与最小 rebuild set','缺失依赖为空及真正离线的证明'],'classification':'R0-A 阻断后的未尝试；不声称两候选已被本 W 实测证明失败。'}
w.save('artifacts/OFFLINE_CLOSURE_REPORT.json',closure)
metrics=[]
for name,unit,cap in [('new_disk','bytes',2*1024**3),('peak_RSS','bytes',4*1024**3),('post_preflight_wall','seconds',25*60),('new_files','files',50000)]:metrics.append({'name':name,'unit':unit,'cap':cap,'predicted_value':None,'predicted_upper_bound':None,'evidence':None,'monitor_verified':False,'stop_threshold':cap,'status':'NOT_ATTEMPTED_R0A_GATE'})
resources={'record_type':'W003_RESOURCE_BUDGET_REPORT','utc':stamp,'status':'NOT_ATTEMPTED_R0A_GATE','four_budgets_known_within_cap':False,'continuous_monitors_pass':False,'metrics':metrics,'comparable_build_artifacts_or_logs_read':False,'same_compiler_closure_target_comparability_proven':False,'dry_run_rebuild_set_available':False,'verified_continuous_monitors':{'single_post_preflight_monotonic_deadline':False,'whole_process_group_RSS':False,'root_disk_files':False,'all_children_included':False,'threshold_kill_and_receipt':False},'actual_failed_launcher_duration_seconds':run['elapsed_seconds'],'actual_failed_launcher_per_command_timeout_seconds':45,'timeout_triggered':run['timeout'],'per_command_timeout_is_post_preflight_budget_or_monitor_proof':False,'reason':'R0-A 失败，R0-B/C 未进入。命令的短超时与实际持续时间不能推导 compile/serialization 的四预算或持续监测 PASS。','missing':['同 compiler/closure/可比 target 的真实 artifact/build/time 依据','四项非空保守预测与上界','全进程组/子孙进程连续监测和阈值杀停回执'],'budget_values_inferred_from_version_commands':False}
w.save('artifacts/RESOURCE_BUDGET_REPORT.json',resources)
verdict={'record_type':'W003_PHASE0_RECOVERY_VERDICT','utc':stamp,'run_id':order['run_id'],'work_order_id':'W003','outcome':'STOP','phase0_verdict':'PREFLIGHT_STOP','primary_stop_reason':'RECOVERY_STOP_WRITE_CONFINEMENT','primary_evidence':'Inherited fd0 /dev/null is O_RDWR; pre-enforcement assertion failed; launcher exit73; no Landlock/seccomp installation calls.','four_independent_requirements':{'WRITE_CONFINEMENT_PASS':{'pass':False,'status':'FAIL_BEFORE_POLICY','evidence':'WRITE_CONFINEMENT_REPORT.json'},'OFFLINE_CLOSURE_PASS':{'pass':False,'status':'NOT_ATTEMPTED_R0A_GATE','evidence':'OFFLINE_CLOSURE_REPORT.json'},'FOUR_BUDGETS_KNOWN_WITHIN_CAP':{'pass':False,'status':'NOT_ATTEMPTED_R0A_GATE','evidence':'RESOURCE_BUDGET_REPORT.json'},'CONTINUOUS_MONITORS_PASS':{'pass':False,'status':'NOT_ATTEMPTED_R0A_GATE','evidence':'RESOURCE_BUDGET_REPORT.json'}},'independent_successful_subfacts':['派发任务原件 5210 bytes/hash 完全一致；22 项文件镜像 hash 校验与只读复制','原 W1 当前实际 turn_context 的 Sol/max/cwd、owner PID/startticks、原 thread/session 及新锁实核','主控 lock PID240810/startticks46501758/inode14806399 存活持有、同 inode 非阻塞竞争失败，未替换/释放主控锁','完整 -ff -yy trace 覆盖唯一失败 launcher：1 个成功 descriptor write，1214 bytes，路径在 W003 内；本 trace 未见成功外写或未知 write 路径','22 项指定输入 hash/bytes/mtime/inode/dev 未变'], 'no_confinement_pass_inferred_from_subfacts':True,'R0B_entered':False,'R0C_entered':False,'Phase1_or_Phase2_entered':False,'scenario_evidence_runs':0,'compile_runs':0,'serialization_runs':0,'automatic_retry':False,'local_goal_completion_scope':'仅本地原件交付；不表示 W/E1 专业接受、D003、G-RUN 或父任务完成。'}
w.save('artifacts/PHASE0_RECOVERY_VERDICT.json',verdict)
missing=[{'id':'M-CONFINEMENT','detail':'当前 R0-A 失败，kernel policy 未安装；继承 writable fd、外写拒绝、HOME/CODEX 新写拒绝、子孙继承、symlink 和网络等 probe 未通过。不得声称零外写合同已证明。'},{'id':'M-SENTINEL-PRECONFIRMATION','detail':'恢复计划要求主控预确认外部 sentinel 不存在；本聊天已请求，停止前未收到确认；未运行该负向探针。主阻断仍是先发生的 fd0 失败。'},{'id':'M-CLOSURE','detail':'R0-B 未进入，单一兼容离线 closure 及完整依赖/工具/package DB/rebuild set 未固定。'},{'id':'M-BUDGETS-MONITORS','detail':'R0-C 未进入；四项预测上界与可比实测依据、连续监测/杀停回执均缺。固定 cap 不是预测。'},{'id':'M-CONDITIONAL-EP','detail':'Phase1/2 未进入，八 EP 未实施。无 staged source/patch/schema/fixture/compile/serialization/local commit；不生成空替代文件。'},{'id':'M-E1-STATIC-LEDGER','detail':'只保留 C0010 E1 对旧 EP-SCENARIO-04 的 PARTIAL 静态子集输入，不冒充当前 target manifest 或当前业务实测。'},{'id':'M-EVIDENCE-PUBLICATION','detail':'当前 W003 本地证据尚无真实 GitHub 出版 commit/refs；需主控逐字运输本清单后回传准确 refs/sha256。'},{'id':'M-FORMAL-RETURN','detail':'同一 W1/W003 取得真实已出版证据 refs 后才生成正式 V2 Return，仅回原 E1；Return 自身需第二次主控出版，不能提前引用未来文件或伪造自 hash。'}]
conditional=['SOURCE_BASELINE_AND_STAGING_REPORT.md','SOURCE_CHANGE_MANIFEST.json','PREREQUISITE_PATCHSET.diff','PRECONDITION_REPORT.md','D003_BINDING_CANDIDATE.json','FIXTURE_SCHEMA_AND_PROVENANCE.md','FX_WALL_SCENARIO_001.schema.json','FX_WALL_SCENARIO_001.json','KNOWN_CONTRACT_CONFLICTS.md','COMPILE_ONLY_REPORT.json','SERIALIZATION_TEST_REPORT.json','STAGED_LOCAL_COMMIT_REPORT.json']
maps=[['WORKER_EXECUTION_REPORT.md'],['W003_BINDING.json'],['WRITE_CONFINEMENT_REPORT.json'],['FULL_WRITE_TRACE_REVIEW.json'],['OFFLINE_CLOSURE_REPORT.json'],['RESOURCE_BUDGET_REPORT.json'],['PHASE0_RECOVERY_VERDICT.json'],['COMMAND_LOG.jsonl','WRITE_SURFACE_AUDIT.json','EP_ACCEPTANCE_MATRIX.md','PUBLICATION_MANIFEST.json','HASHES.sha256'],[],['ENGINEERING_STOP_REPORT.md'],[]]
deliverables=[]
for i,(literal,names) in enumerate(zip(order['deliverables'],maps),1):
 item={'index':i,'literal_ORDER_deliverable':literal,'status':'LOCAL_FILE_READY','local_files':[str(A/name) for name in names]}
 if i==9:item.update(status='NOT_APPLICABLE_PHASE0_STOP',missing='Recovery 未 PASS；未进入 Phase1/2。',conditional_filenames_not_created=conditional)
 if i==11:item.update(status='DEFERRED_TWO_STAGE_REAL_PUBLICATION_CONTRACT',missing='先由主控真实出版本地证据，再由同一 W1 同 W003 生成正式 Return。',future_transport_target='longrun/runs/OI-EAW-WALL-20261114-01/worker_results/W003/WORKER_RETURN.json',return_to=order['return_to'],real_ref=None)
 deliverables.append(item)
handoff={'schema':'w003-local-stage-handoff/v1','utc':stamp,'run_id':order['run_id'],'work_order_id':'W003','worker':order['worker'],'return_to':order['return_to'],'outcome':'STOP','phase0_verdict':'PREFLIGHT_STOP','stop_reason':'RECOVERY_STOP_WRITE_CONFINEMENT','order_ref':'daowei2026/observe-iterate@3afc8e9eedb34ac3b25ba69e383c778c37622c30:longrun/runs/OI-EAW-WALL-20261114-01/work_orders/W003/ORDER.json','actual_write_root':str(ROOT),'local_result_path':str(A/'WORKER_EXECUTION_REPORT.md'),'result_ref':None,'github_publication_commit':None,'publication_target_prefix':'longrun/runs/OI-EAW-WALL-20261114-01/delegations/D003/results/W003/','transport_path_mapping':'W003/artifacts/<name> -> publication_target_prefix/<name>; all other W003/<relative> -> publication_target_prefix/<relative>. All payload originals transported verbatim.','deliverable_mapping':deliverables,'missing':missing,'formal_Return_generated':False,'conditional_artifact_files_created':False,'next_steps':['主控按 PUBLICATION_MANIFEST、HASHES 和 FREEZE_RECEIPT 逐字运输本地原件，并从真实出版对象回读。','主控把真实 commit/ref/sha256/bytes 映射交同一原 W1 同 W003。','同一 W1 在续接授权内核真实 refs 后生成 V2 WORKER_RETURN.json，仅回原 E1；再交主控出版至 worker_results/W003/WORKER_RETURN.json。'],'terminal_scope':'本地阶段可终结；不常驻轮询、不自行新建 W、不向其他聊天发送消息。W/D/专业接受和父任务完成由原 E1/manager 决定。','index_self_hash_policy':'完整文件 hash 从 PUBLICATION_MANIFEST/HASHES 的无环层级和最终 FREEZE_RECEIPT/本聊天外层 hash 读取；不捏造 index 自 hash 或 Return 自 ref。'}
w.save('artifacts/LOCAL_STAGE_HANDOFF.json',handoff)
doc('EP_ACCEPTANCE_MATRIX.md','''# W003 本地 EP 事实矩阵

本 W 在 R0-A 的继承 fd 检查失败，未进入 R0-B/C 或 Phase1/2。以下“继承 E1 状态”仅引用只读 C0010 专业矩阵，不代表 Worker 对专业接受的决定，也不是 W003 当前生命周期实测。

| EP | 继承 E1 状态 | W003 新工程事实 | 当前缺口 |
|---|---|---|---|
| EP-WALL-SHARED-01 | NOT_ATTEMPTED | 未构造 accessor/snapshot | 无 patch、typecheck/read-only test |
| EP-WALL-SHARED-02 | NOT_ATTEMPTED | 未构造 DTO/schema | 无 canonical order、roundtrip/stable hash |
| EP-WALL-SHARED-03 | UNSATISFIED | 新 R0-A launcher 在安装 policy 前拒绝 writable fd0，exit73；保留完整 trace | confinement 未通过；closure、预算和持续监测仍无本 W 证明 |
| EP-SCENARIO-01 | NOT_ATTEMPTED | 无 dedicated target/manifest | Phase0 hard gate 未通过 |
| EP-SCENARIO-02 | NOT_ATTEMPTED | 未构造 exact-error serialization | 无 structured constructor/payload 验证 |
| EP-SCENARIO-03 | NOT_ATTEMPTED | 未构造 transaction DTO | 无 pre/post A 和 committed/uncommitted 验证 |
| EP-SCENARIO-04 | PARTIAL（旧静态子集） | 旧 ledger 只作为不可覆盖输入；无新 target | 未进入 target manifest；无 actual result |
| EP-SCENARIO-05 | NOT_ATTEMPTED | 未物化 9/18/22 fixture | 无完整 schema/input/static count/order/hash |

继承 E1 状态合计：SATISFIED=0，PARTIAL=1，UNSATISFIED=1，NOT_ATTEMPTED=6。W003 新满足的 EP=0。`scenario evidence runs=0`，compile-only=0，serialization=0。

来源：`input/mirrors/` 中逐字 C0010 `EP_ACCEPTANCE_MATRIX_C0010.md` 及 W002 frozen 输入；W003 的 `PHASE0_RECOVERY_VERDICT.json` 和 `FULL_WRITE_TRACE_REVIEW.json`。W002 原件不改，不据旧源码/旧证据替代当前实测，不判断 G-RUN 或父任务完成。
''')
doc('ENGINEERING_STOP_REPORT.md',f'''# W003 工程停止原件

本地 outcome 为 **STOP**，Phase0 verdict 为 **PREFLIGHT_STOP**，主原因是 `RECOVERY_STOP_WRITE_CONFINEMENT`。

唯一真实尝试在 {run['started_at']} 启动，{run['completed_at']} 结束，launcher PID241337，退出码73，未超时。`runtime.py` 的 `subprocess.Popen(stdin=subprocess.DEVNULL)` 传入以 `O_RDWR` 打开的 `/dev/null`。launcher 第 {failed_line} 行在继承 fd 检查中要求 fd0 只读，触发 AssertionError。该接线问题属于本 W 实现；拒绝发生于 `PR_SET_NO_NEW_PRIVS`、Landlock ABI 查询/规则创建/restrict 和 seccomp 安装之前。不能把它描述成 Landlock 内核不支持，也不能把拒绝本身描述成 kernel confinement PASS。

`receipts/r0a-positive-launcher.json` 中 `calls=[]`。`trace/r0a-positive.241337` 的第1055行记录 `fcntl(0</dev/null>, F_GETFL) = O_RDWR|O_LARGEFILE`，第1058/1063行记录 W003 内 receipt 的创建和唯一成功 write（1214 bytes）。共1071行完整 trace，无子孙进程和 probe exec。未见成功外写或无法映射的 descriptor write，但范围仅为这个失败 launcher；整个后继零外写合同未被证明。

按 ORDER §5/8/12，不调整 stdin/参数、不修改 launcher 后重试，不改用另一方法继续，不进入 R0-B/C，不进入 staged source construction。正反 probe、closure、四项预测和连续监测均缺；场景、normal、DBA、wrapper、native-reader、compile、serialization、生产材料生成和源码 push 均未执行。实际 HOME/CODEX_HOME 未重设。未获得外部 sentinel 的主控预确认，该负向 probe 未执行；它是额外缺项，不能掩盖已发生的 fd0 主阻断。

成功子事实保留：精确任务与22项镜像 hash 校验、原 W1 实际配置/新锁核验、唯一失败 launcher 完整 trace 和限定范围的 write 路径映射。22项指定只读输入的 bytes/hash/mtime/inode/dev 复核不变；不把命名子集不变扩展成全局零外写证明。主控锁始终保留，Worker 未重取、替换或释放；W002 没有回写。

本地阶段不造空 patch、fixture、compile/serialization/local commit 报告，不生成声称真实未出版 refs 的正式 Return。后续由原 E1 根据真实 STOP 原件决定修唯一阻断或有界收束；Worker 不自行新建工单或作专业接受/父任务完成决定。先交主控逐字出版证据，再同一 W1/W003 以真实 refs 生成正式 V2 Return，仅回原 E1。
''')
doc('WORKER_EXECUTION_REPORT.md',f'''# W003 本地执行报告

本地 outcome：**STOP**。Phase0：**PREFLIGHT_STOP**。主停止原因：**RECOVERY_STOP_WRITE_CONFINEMENT**。本报告仅交当前 W003 本地事实和原件，不表示 E1 专业接受、D003/G-RUN 或父任务完成。

## 任务、身份和实际写面

按 C0011 正式修签 W003，原 Worker W1、原物理聊天 `01a1da55-5881-7590-94a1-0661f0236977` 执行。准确 ORDER JSON ref 为 `{handoff['order_ref']}`。定位任务原件完整读取并核得5210 bytes、SHA256 `f8aae85a8bf268c5f2dd7c48edf7383d810749d6c83094f7ca0d61db9fb3ce87`。指定镜像索引22个文件全部逐字/hash核验；8个 exact Git 源码输入因 R0-A 失败而未进入后续读取/closure 阶段。

当前原生 turn_context 记录 `gpt-6.1-sol/max`、cwd `/dwdhome/fy/BASE_E6_2`；现有执行器 PID2890/startticks20139、UID501/exe 现场只读复核。主控对同 owner 的原 thread/session、旧 turn completed/Goal null/queue 空、加载后 idle/canAccept 的原件保留。旧 keeper PID237355 当前不存在；W003 原根不存在后才由本 W 建立。新独占锁 path `.oi-runs/OI-EAW-WALL-20261114-01/.D003-writer.lock`，PID240810/startticks46501758/inode14806399，主控 session30931；现场 fdinfo 为 FLOCK WRITE，同 inode 新 open-file-description 的 `LOCK_EX|LOCK_NB` 竞争 EAGAIN，未重取、替换或释放主控锁。证据见 `W003_BINDING.json`、input 原件、COMMAND_LOG。

Owner literal grant：

```text
operation=wall-observation-work execution_context=linux:/dwdhome/fy/BASE_E6_2 allowed_writes=/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01
```

本 W 唯一新增业务写根：`{ROOT}`。HOME=`/home/dw`、CODEX_HOME=`/home/dw/.codex` 保持实际原值，未重设；任务显式 tmp/cache/config/log/report 路径只在本根。Python 使用 `-I -S -B` 和 `PYTHONDONTWRITEBYTECODE=1`，未写外部 pycache；不重新设置 HOME/CODEX_HOME。只读边界包括 shared、W002、cgpterm、实际 HOME/CODEX_HOME；未访问 `/m3varK`/production materials 或生产 wrapper。

## R0-A 的真实结果

创建了 run-local Python/ctypes Landlock+seccomp 候选 launcher、分阶段 probe 和完整审计脚本；均为本 W audit artifact，不是 FRP patch。先把正向/继承FD/网络核验与需主控预确认 sentinel 的负向核验分开。负向 sentinel 主控预确认停止前未收到，因此未运行负向探针。

只实际尝试一次正向 launcher：`{run['started_at']}` → `{run['completed_at']}`，用时 `{run['elapsed_seconds']:.6f}` seconds，exit73，timeout=false。完整命令和 stdout/stderr 原件已存。失败发生在 inherited FD inspection：runtime 的 `subprocess.DEVNULL` 使 stdin fd0 为 `O_RDWR /dev/null`；launcher 第{failed_line}行要求 fd0只读，拒绝并退出。这是本 W 接线问题。当前 Landlock ABI 未查询、NNP/规则/restrict/seccomp 未调用；历史 ABI6 只用于候选设计，未冒充本 W 实测。

因此 inside-root 正向操作、外部/shared/HOME/CODEX 拒绝、child/grandchild、symlink escape、完整 inherited FD closure、network denial 等 probe 均未到达 PASS。未改变参数或代码重试。

`strace --kill-on-exit -ff -yy -ttt -s128 -e trace=all` 覆盖唯一 launcher PID241337 从 execve 到 exit73。read-family 的 byte payload 用 raw 格式，仍保留 syscall；write-family 保留 FD/path/actual return。完整原件1071行、133303 bytes、SHA256 `ea4a8881e8a3967196e0b6ef4f904ddb6ad17bd80d866b5e5b2e8bfec51177bb`。唯一成功 descriptor write 为 W003 内失败 receipt 的1214 bytes；成功外写=0、未知 write 路径=0，均仅限本次 trace。无 `/proc/*/comm` open/write。startup SysV IPC 创建尝试 EEXIST，实际 attach 为 SHM_RDONLY；唯一 MAP_SHARED 文件映射 PROT_READ。没有全局/后继 confinement 或零外写证明。

## R0-B、R0-C 与条件工程

| 要求 | W003 真实状态 |
|---|---|
| WRITE_CONFINEMENT_PASS | false：kernel policy 安装前停止 |
| OFFLINE_CLOSURE_PASS | false：R0-A gate 阻断，未尝试 |
| FOUR_BUDGETS_KNOWN_WITHIN_CAP | false：未尝试，四预测上界 unknown |
| CONTINUOUS_MONITORS_PASS | false：未尝试，未验证连续监测/阈值杀停 |

未运行任何 Haskell/Stack/Cabal/GHC metadata、build、compile、test；没有把 E lts18.28 与 B lts22.24/GHC9.4.8 拼接，亦未浅扫 cache 或以版本查询代替预算。固定 cap 保持 new disk≤2GiB、peakRSS≤4GiB、post-preflight≤25min、new files≤50000、outside writes=0、scenario runs=0。45秒单命令 timeout 不代表后继工程预算/连续监测证明。

Phase1/2 未进入，未构造 staged source、patch、schema、fixture、dedicated target、serialization 或 local commit。继承 E1 C0010 矩阵为0 SATISFIED、1 PARTIAL（旧 SCENARIO-04 静态子集）、1 UNSATISFIED（SHARED-03）、6 NOT_ATTEMPTED；本 W 新满足 EP=0。W002 ledger 仍是 frozen input，不能替代当前业务实测。所有单/部分/全场景 evidence、normal、DBA、wrapper、native-reader、当前业务材料生成和源码 push 均为0。

## 日志、限制和交付

`COMMAND_LOG.jsonl` 以当前 W003 turn 的原生命令完成事件及独立受 trace 子命令日志组成；控制命令的完整代码/aggregated output 与业务 raw trace/stdout/stderr 分别归档。最终封存命令记录自身命令及日志关闭点，不伪造尚未返回的 exit code。所有原件路径、bytes、hash 和目标由 `PUBLICATION_MANIFEST.json` / `HASHES.sha256` / 外层 `FREEZE_RECEIPT.json` 给出，无循环自 hash。仅在新 W003 根内做小范围枚举；未广搜 BASE/HOME/cache、未联网或安装。

22项指定原输入的 bytes/hash/mtime/inode/dev 复核未变。该子集和单次 launcher trace 不等于全局 filesystem 零外写证明；本 W 不作此推断。原生平台按现有执行器续写自身会话，不作为本任务业务 tmp/cache/产物写面。

全部最低 STOP 原件及11项 ORDER deliverable 的逐项映射在 `LOCAL_STAGE_HANDOFF.json`。不适用的条件工程文件不生成空替代品。主控逐字运输目标：`{handoff['publication_target_prefix']}`；本地 artifacts 下文件发布到目标根同名，其余相对路径保留。当前无真实 W003 publication commit/ref，也无 GitHub 写授权。

待主控真实出版并回传逐字回读的 refs/hash/bytes 后，同一原 W1/同 W003 再生成正式 V2 `WORKER_RETURN.json`，`return_to={order['return_to']}`，再由主控出版至 `worker_results/W003/WORKER_RETURN.json`。本地阶段结束自然退出，不常驻轮询、不向其他聊天发消息。不决定 W 专业接受或父任务完成。
''')
w.guard();print(json.dumps({'reports_generated':9,'outcome':'STOP','phase0':'PREFLIGHT_STOP','missing_count':len(missing),'deliverables_mapped':len(deliverables),'conditional_files_created':False,'formal_Return_generated':False},ensure_ascii=False))
