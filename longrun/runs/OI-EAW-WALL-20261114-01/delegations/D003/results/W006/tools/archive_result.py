"""R0-A1停止后只读审阅与结果归档；不重跑/调整任何准备或kernel/probe。"""
from pathlib import Path
import collections, json, os, re, sys
sys.path.insert(0,str(Path(__file__).resolve().parent))
from common import ROOT,binding,fact,guard,save,utc
STOP='STOP_PROBE_HOLDER_FDINFO_READ_EACCES'
guard()
b=binding();attempt=json.loads((ROOT/'artifacts/R0_A1_EXECUTION_RECEIPT.json').read_bytes())
main=json.loads((ROOT/'receipts/probe-main.json').read_bytes())
launch=json.loads((ROOT/'receipts/r0a1-launcher.json').read_bytes())
assert attempt['attempts']==1 and attempt['result']['exit_code']==1 and main['status']=='FAILED_STOP'
assert main['error']['type']=='PermissionError' and '[Errno 13]' in main['error']['text'] and '/proc/248632/fdinfo/3' in main['error']['text']
assert launch['abi']==6 and launch['status']=='KERNEL_POLICY_INSTALLED_BEFORE_EXEC'
assert all(c['errno']==0 and c['return']>=0 for c in launch['calls'])
for name in ['HISTORICAL_FIOCLEX_PHASE_CLASSIFICATION.json','FIOCLEX_LOCAL_CONSTANT_VERIFICATION.json','SECCOMP_DATA_LAYOUT_VERIFICATION.json','SECCOMP_FILTER_STATIC_EVALUATION.json']:
    assert json.loads((ROOT/'artifacts'/name).read_bytes())['status']=='PASS'
trace_files=sorted((ROOT/'trace').iterdir());assert len(trace_files)==1
trace=trace_files[0];lines=trace.read_text().splitlines();assert len(lines)==2290
install=next(i+1 for i,s in enumerate(lines) if 'prctl(PR_SET_SECCOMP,' in s and s.endswith('= 0'))
syscalls=collections.Counter();parsed=[];noncall=[]
for number,line in enumerate(lines,1):
    match=re.match(r'^(\d+\.\d+) ([A-Za-z0-9_]+)\((.*)\) = (.*)$',line)
    if match:
        timestamp,name,args,returned=match.groups();syscalls[name]+=1
        parsed.append({'line':number,'timestamp':timestamp,'syscall':name,'args':args,'return':returned,'text':line,'post_policy':number>install})
    else:noncall.append({'line':number,'text':line})
known_read_or_process={'execve','brk','mmap','access','openat','fstat','close','readlinkat','read','munmap','mprotect','pread64','arch_prctl','set_tid_address','set_robust_list','rseq','prlimit64','getrandom','uname','shmget','shmat','futex','gettid','readlink','newfstatat','lseek','getdents64','fcntl','ioctl','rt_sigaction','landlock_create_ruleset','prctl','landlock_add_rule','landlock_restrict_self','write','getpid','getppid','shmdt','exit_group'}
unknown_syscalls=sorted(set(syscalls)-known_read_or_process)
writes=[];write_opens=[];unknown_write_paths=[];outside_writes=[]
write_family={'write','writev','pwrite64','pwritev','pwritev2','sendfile','copy_file_range','splice','tee','vmsplice'}
path_mutators={'rename','renameat','renameat2','link','linkat','symlink','symlinkat','unlink','unlinkat','mkdir','mkdirat','mknod','mknodat','truncate','ftruncate','chmod','fchmod','fchmodat','fchmodat2','chown','fchown','lchown','fchownat','utime','utimes','futimesat','utimensat','setxattr','lsetxattr','fsetxattr','removexattr','lremovexattr','fremovexattr','mount','umount2','msync'}
other_mutations=[];shared_writable_mmaps=[]
for row in parsed:
    name=row['syscall'];returned=row['return'];successful=not returned.startswith('-1 ') and not returned.startswith('?')
    if name in write_family and successful:
        target=re.match(r'\d+<([^>]+)>',row['args']) if name in {'write','writev','pwrite64','pwritev','pwritev2','sendfile','vmsplice'} else None
        d={'line':row['line'],'syscall':name,'text':row['text'],'bytes_returned':int(returned.split()[0],0),'target_path':target.group(1) if target else None}
        if target and target.group(1).startswith('/'):
            d['inside_root']=Path(target.group(1)).is_relative_to(ROOT)
            if not d['inside_root']:outside_writes.append(d)
        else:unknown_write_paths.append(d)
        writes.append(d)
    if name in {'open','openat','openat2'} and successful and re.search(r'O_WRONLY|O_RDWR|O_CREAT|O_TRUNC|O_TMPFILE',row['args']):
        target=re.match(r'\d+<([^>]+)>',returned)
        d={'line':row['line'],'text':row['text'],'path':target.group(1) if target else None}
        if not target:unknown_write_paths.append(d)
        elif not Path(target.group(1)).is_relative_to(ROOT):outside_writes.append(d)
        write_opens.append(d)
    if name in path_mutators:other_mutations.append(row)
    if name=='mmap' and 'MAP_SHARED' in row['args'] and 'PROT_WRITE' in row['args']:shared_writable_mmaps.append(row)
fioclex=[{'line':r['line'],'text':r['text'],'post_policy':r['post_policy']} for r in parsed if r['syscall']=='ioctl' and 'FIOCLEX' in r['args']]
post_FIOCLEX=[r for r in fioclex if r['post_policy']]
assert len(post_FIOCLEX)==1 and post_FIOCLEX[0]['line']==1508 and post_FIOCLEX[0]['text'].endswith('= 0')
denied_ioctl=[{'line':r['line'],'text':r['text']} for r in parsed if r['syscall']=='ioctl' and r['post_policy'] and r['return'].startswith('-1 EPERM')]
denied_ioctl_names=collections.Counter(re.search(r'>, ([A-Za-z0-9_]+)',r['text']).group(1) for r in denied_ioctl)
post_getfd=[{'line':r['line'],'text':r['text']} for r in parsed if r['syscall']=='fcntl' and r['post_policy'] and 'F_GETFD' in r['args']]
stop_rows=[{'line':r['line'],'text':r['text']} for r in parsed if r['syscall']=='openat' and '"/proc/248632/fdinfo/3"' in r['args']]
assert len(stop_rows)==1 and stop_rows[0]['line']==2240 and 'O_RDONLY|O_CLOEXEC) = -1 EACCES' in stop_rows[0]['text']
proc_comm=[{'line':i+1,'text':s} for i,s in enumerate(lines) if re.search(r'/proc/[^\"]*/comm|PR_SET_NAME',s)]
ipc=[r for r in parsed if r['syscall'] in {'shmget','shmat','shmdt','shmctl'}]
assert len(writes)==3 and sum(r['bytes_returned'] for r in writes)==6594
assert not outside_writes and not unknown_write_paths and not unknown_syscalls and not other_mutations and not shared_writable_mmaps and not proc_comm
assert not any(name in syscalls for name in ['clone','clone3','fork','vfork'])
review={'status':'PATH_COMPLETE_FOR_SINGLE_FAILED_TRACE_ONLY','at':utc(),'scope':'完整审阅这一失败链，非整个W/后继/global zero writes证明。','trace_files':[fact(trace)],'trace_lines':len(lines),'syscall_counts':dict(syscalls),'unparsed_noncall_rows':noncall,'unknown_syscall_names':unknown_syscalls,'policy_install_line':install,'successful_descriptor_writes':writes,'successful_descriptor_write_count':len(writes),'successful_descriptor_write_bytes':6594,'successful_write_open_rows':write_opens,'successful_outside_file_writes_in_this_trace':len(outside_writes),'unknown_write_paths_in_this_trace':len(unknown_write_paths),'other_path_mutation_calls':other_mutations,'shared_writable_file_mmaps':shared_writable_mmaps,'proc_comm_open_or_write_rows':proc_comm,'current_trace_pre_and_post_policy_FIOCLEX_rows':fioclex,'post_policy_denied_other_ioctls':{'counts':dict(denied_ioctl_names),'rows':denied_ioctl,'scope':'TCGETS/TIOCGWINSZ按其余ioctl默认拒绝，解释器继续进入probe；不扩大allowlist，也不将其写成主停止因。'},'post_policy_F_GETFD_rows':post_getfd,'explicit_test_FIOCLEX_F_GETFD_pair_reached':False,'exact_failure_open':stop_rows[0],'IPC_rows':ipc,'IPC_scope_note':'trace中IPC_CREAT|IPC_EXCL均EEXIST，随后既有segment lookup和SHM_RDONLY attach；只记录实际调用，不作为文件写或全局可用性PASS。','trace_target_processes':1,'trace_target_execve_count':syscalls['execve'],'probe_child_grandchild_count':0,'global_zero_outside_writes_PASS':False,'current_trace_payload_reads_raw':True}
save('artifacts/FULL_WRITE_TRACE_REVIEW.json',review)
save('artifacts/FIOCLEX_KERNEL_OBSERVATION.json',{'phase':'P4','status':'BOOTSTRAP_FIOCLEX_SUCCEEDED_EXPLICIT_EFFECT_PROBE_NOT_REACHED','trace':fact(trace),'policy_install_line':install,'post_policy_FIOCLEX':post_FIOCLEX,'same_descriptor_F_GETFD_after_FIOCLEX_proof':False,'explicit_inside_fd_clear_FIOCLEX_GETFD_effect_test':'NOT_REACHED_AFTER_HOLDER_FDINFO_EACCES','unrelated_post_policy_F_GETFD_rows':post_getfd,'current_vs_history_separate':True})
lock_end=guard()
save('artifacts/WRITE_CONFINEMENT_REPORT.json',{'phase':'P4','status':'STOP_PROBE_HOLDER_FDINFO_READ_EACCES','WRITE_CONFINEMENT_PASS':False,'attempts':1,'kernel_abi':launch['abi'],'kernel_install_calls':launch['calls'],'handled_filesystem_rights':launch['handled_filesystem_rights'],'handled_access_fs':launch['handled_access_fs'],'only_write_allow_root':str(ROOT),'second_Python_bootstrap_success':True,'post_policy_FIOCLEX_return':0,'explicit_F_GETFD_CLOEXEC_effect_test':'NOT_REACHED','probe_body_entered':True,'passed_probe_checks':main['checks'],'probe_failure':main['error'],'exact_trace_failure':stop_rows[0],'failure_layer_attribution':'受限probe只读openat主控holder /proc fdinfo返回EACCES；本工单未进一步区分具体procfs/LSM机制，不称kernel不支持或FIOCLEX失败。','parent_readonly_stdin':json.loads((ROOT/'receipts/r0a1-parent-stdin.json').read_bytes()),'launcher_stdio_and_inherited_FD':{'stdio':launch['stdio_fds'],'closed_nonstdio':launch['inherited_nonstdio_fds_closed']},'holder_lock_independently_intact_outside_restricted_child':lock_end,'nine_probe_status':[{'name':'inside create/write/rename/remove','status':'NOT_REACHED'},{'name':'OUTSIDE create/write denial','status':'NOT_REACHED'},{'name':'SHARED create denial','status':'NOT_REACHED'},{'name':'actual HOME/CODEX read allowed new create denied','status':'ENV_VALUES_PASS_CREATE_READ_PROBES_NOT_REACHED'},{'name':'child/grandchild inheritance','status':'NOT_REACHED'},{'name':'symlink escape denial','status':'NOT_REACHED'},{'name':'inherited writable FD closed + holder lock','status':'INHERITED_FD_CLOSED_PASS_PARENT_HOLDER_PASS_CHILD_HOLDER_READ_EACCES'},{'name':'network socket/connect denial','status':'NOT_REACHED'},{'name':'full trace path mapping','status':'COMPLETE_FAILED_CHAIN_SCOPE_ONLY'}],'policy_or_probe_modified_after_attempt':False,'retry_count':0,'global_zero_outside_writes_PASS':False})
save('artifacts/OFFLINE_CLOSURE_REPORT.json',{'status':'NOT_ATTEMPTED_R0_A_STOP','OFFLINE_CLOSURE_PASS':False,'R0_B_attempts':0,'selected_complete_closure':None,'candidate_E':'exact frp lts-18.28 NOT_EVALUATED','candidate_B':'BASE overlay lts-22.24 historicalGHC9.4.8 NOT_EVALUATED','both_candidates_failed_claimed':False,'resolver_compiler_tool_hashes_current_closure':None,'package_DB_transitive_IDs_minimum_rebuild_set':None,'missing_dependencies_empty_proven':False,'exact_FRP_Git_objects_read':0,'exact_git_object_mappings_deferred':8,'build_compile_test_download_install':0})
save('artifacts/RESOURCE_BUDGET_REPORT.json',{'status':'NOT_ATTEMPTED_R0_A_B_BLOCKED','FOUR_BUDGETS_KNOWN_WITHIN_CAP':False,'CONTINUOUS_MONITORS_PASS':False,'R0_C_attempts':0,'budgets':[{'name':name,'cap':cap,'predicted_value_or_upper_bound':None,'same_compiler_closure_comparable_measurement':None,'status':'NOT_ATTEMPTED'} for name,cap in [('new_disk_bytes',2147483648),('peak_RSS_bytes',4294967296),('post_preflight_seconds',1500),('new_files',50000)]],'continuous_monitors':{'monotonic_deadline_verified':False,'whole_process_group_RSS_verified':False,'root_disk_files_verified':False,'descendants_threshold_kill_receipt_verified':False,'global_kernel_trace_outside_writes_verified':False,'HOME_CODEX_new_writes_coverage_verified':False},'single_failed_command_elapsed_seconds':attempt['result']['elapsed_seconds'],'single_command_timeout_seconds':45,'single_command_timeout_is_engineering_budget_proof':False})
save('artifacts/PHASE0_RECOVERY_VERDICT.json',{'outcome':'STOP','gate':'PREFLIGHT_STOP','stop_code':STOP,'preparation_stages':{'P0':'PASS','P1':'PASS','P2':'PASS','P3':'PASS','P4':'STOP_HOLDER_FDINFO_OPEN_EACCES'},'WRITE_CONFINEMENT_PASS':False,'OFFLINE_CLOSURE_PASS':False,'FOUR_BUDGETS_KNOWN_WITHIN_CAP':False,'CONTINUOUS_MONITORS_PASS':False,'R0_A1_attempts':1,'R0_A1_exit_code':1,'R0_B_attempts':0,'R0_C_attempts':0,'automatic_retry':False,'policy_guard_or_probe_adjusted_after_attempt':False,'conditional_EP_entered':False,'scenario_runs':0,'normal_runs':0,'build_compile_serialization_current_material_runs':0,'professional_acceptance_or_parent_completion_decided':False})

verified=json.loads((ROOT/'input/VERIFIED_INPUTS.json').read_bytes());input_checks=[];extra_checks=[]
for row in verified['local_inputs']:
    before=row['source'];after=fact(before['path']);assert before==after and fact(row['mirror']['path'])['sha256']==before['sha256']
    input_checks.append({'before':before,'after':after,'same_bytes_hash_mtime_inode_dev':True})
for row in verified['extra_inputs']:
    before=row['source'];after=fact(before['path'])
    extra_checks.append({'before':before,'after':after,'same_bytes_hash_mtime_inode_dev':before==after,'scope':'控制器原件若后续更新，区分该运输来源变化与本W保存镜像；本Worker未写source。'})
save('audit/INPUT_IMMUTABILITY_CHECK.json',{'at':utc(),'local_input_count':26,'all26_local_input_originals_unchanged':True,'local_inputs':input_checks,'extra_controller_contract_sources':extra_checks,'scope':'仅逐项具名检查，非全部BASE/HOME扫描。','eight_Git_objects_not_read':verified['exact_git_inputs_deferred']})
post=[]
for label,path in b['negative_targets'].items():
    try:os.lstat(path)
    except FileNotFoundError as e:assert e.errno==2;post.append({'label':label,'path':path,'readonly_lstat_absent':True,'errno':2})
    else:raise RuntimeError('STOP unexpected outside target exists; do not delete')
save('audit/NEGATIVE_TARGET_POSTCHECK.json',{'at':utc(),'results':post,'negative_create_probes_entered':False,'created_written_deleted_or_cleanup':False,'scope':'absence only, not kernel denial evidence'})

matrix='''# W006 EP状态交接（Worker事实）

P0–P3已PASS，唯一P4在holder fdinfo只读open EACCES停止；四PASS未成立，未进入条件八EP建设。

| EP | C0014状态 | W006新增事实及剩余缺口 |
|---|---|---|
| EP-WALL-SHARED-01 | NOT_ATTEMPTED | snapshot/accessor/patch/typecheck未做 |
| EP-WALL-SHARED-02 | NOT_ATTEMPTED | DTO/schema/canonical serialization未做 |
| EP-WALL-SHARED-03 | UNSATISFIED | 历史分层/常量/layout/fresh filter/pure evaluator通过，kernel安装和bootstrap FIOCLEX成功；holder读EACCES，完整probe/closure/四预算/monitor未证 |
| EP-SCENARIO-01 | NOT_ATTEMPTED | dedicated target与compile-only未建设 |
| EP-SCENARIO-02 | NOT_ATTEMPTED | exact error synthetic records未建设 |
| EP-SCENARIO-03 | NOT_ATTEMPTED | transaction DTO/rejected post=pre/O/C空未建设 |
| EP-SCENARIO-04 | PARTIAL | 仅沿用C0014旧静态conflict ledger范围，未新增实现或当前结果 |
| EP-SCENARIO-05 | NOT_ATTEMPTED | 9/18/22 fixture未物化，静态parse/count/hash未做 |

SATISFIED=0，PARTIAL=1，UNSATISFIED=1，NOT_ATTEMPTED=6。W006新增EP满足0。scenario/normal/current材料0。
以上不替代原E1专业接受，不通过G-RUN/H3或父任务。
'''
with (ROOT/'artifacts/EP_ACCEPTANCE_MATRIX.md').open('x') as out:out.write(matrix)
missing=[
 '唯一R0-A1在受限probe只读openat /proc/248632/fdinfo/3返回EACCES/PermissionError，exit1；未改guard/policy/probe重试；具体procfs/LSM机制未在本W另行调查。',
 'bootstrap FIOCLEX实际成功，但inside descriptor清FD_CLOEXEC→FIOCLEX→F_GETFD效果测试未达；其他descriptor的F_GETFD不能冒充该配对证明。',
 'inside create/write/rename/remove完整positive probe未达；失败回执写入根内不替代该完整probe。',
 'OUTSIDE/SHARED/HOME/CODEX新文件创建、只读目录打开与symlink escape的实际kernel negative probes未达；具名lstat不存在不是kernel拒绝PASS。',
 'child/grandchild未生成，restriction继承未测；inherited writable FD关闭已实证，holder锁在父侧独立复核完整，但受限子域holder只读复核失败。',
 'socket/connect实际negative probe未达；静态socket拒绝与filter安装不替代当前网络probe。',
 '完整2290行失败链已审阅，3次成功write/6594bytes均根内，failed-chain outside file writes0/unknown paths0；不能外推全任务、后继或global zero writes/confinement PASS。',
 'R0-B未进入，E/B两个closure候选均未评估，不称二者均失败；缺唯一兼容offline resolver/compiler/packageDB/transitive IDs/rebuild set与missing deps空证明。',
 '8个exact FRP Git对象仅保留已核映射，本W因前置停止未读；无exact-base源码调查、staging或patch。',
 'R0-C未进入，disk/RSS/wall/files预测上界、同closure可比测量与continuous monitors/kill receipt未证；1.277822秒失败命令及45秒timeout不构成预算PASS。',
 '四PASS未成立，条件八EP与snapshot/DTO/target/error/transaction、9/18/22 fixture、compile-only/synthetic serialization/local commit均未实施，不造空条件成果。',
 '具名26输入收尾一致和任务写路径审阅有限域，未扫描全BASE/HOME/CODEX或验证其全局零新增写。',
 '全部本地证据尚待主控逐字出版至W006成果路径，真实commit/result_ref/manifest refs待回传；Worker无GitHub写授权，不造future/self ref。',
 '正式v2 WORKER_RETURN须主控出版证据并回传真实refs后，由同原W1同W006仅在final-return生成；主控再出版worker_results/W006/WORKER_RETURN.json，仅回原E1。',
 '专业接受、action eligibility、G-RUN/H3、父Q和父任务完成仍归E1/manager，Worker未作决定。'
]
report='''# W006 本地执行报告

outcome=`STOP`，gate=`PREFLIGHT_STOP`，stop_code=`STOP_PROBE_HOLDER_FDINFO_READ_EACCES`。
这是本W本地证据交付，不表示W/D003/父任务完成；正式Return待真实出版refs后同单生成，仅回原E1。

## 绑定与范围

完整WORKER_TASK-W006.md已核7117bytes/SHA256 `0ced124a17365b9c0a83298a8fe817015ab9ffc8bed10d7ad4dd525db3ffada4`；完整读取C0014 ORDER MD/JSON、签单Return、专业review、决定、EP及进度。34输入中26个本地原件逐份bytes/hash核验并镜像；8个exact Git对象保留真实映射但本W未读。
原W1 thread `01a1da55-5881-7590-94a1-0661f0236977`，当前turn `01a1dcc1-192d-7003-ac02-e8e3f6648415`，actual gpt-6.1-sol/max、cwd BASE，真实HOME=/home/dw、CODEX_HOME=/home/dw/.codex未重设。fresh预派发idle/canAccept、Goalnull/queue空、旧W5 turn完成/holder gone来源原件保存，并独立核当前原生context与owner PID2890/startticks20139。
新锁holder PID248632/startticks48206357/inode14806399/session91789，现场fdinfo FLOCK WRITE及同inode独立O_RDWR NB竞争EAGAIN；全程只关闭自身FD，未重取/释放/替换holder。root先核不存在再建；所有新增业务原件仅D003/W006。主控609bytes sentinel回执逐字保留，五个具名负目标事前/事后只读ENOENT，无预建/删除/清理。旧W1–W5/shared源码/配置/生产材料未写，HOME/CODEX保持业务只读。

## P0–P3 独立实际结果

- P0 PASS：W004 trace exact SHA `b2bcd39ff8886fa65815107bd95f333abef1bcb0a1ea69bb20010abc24b2c959`。line312为HISTORICAL_PRE_POLICY_SUCCESS，line1509为HISTORICAL_POST_POLICY_DENIAL，policy install line1190；保存两条原文，不要求同结果，不执行旧W5准备器。
- P1 PASS：termios/header两个来源FIOCLEX=21585/0x5451、FIONCLEX=21584/0x5450一致；x86_64/little-endian，header+ctypes seccomp_data=64bytes，nr0/arch4/instruction_pointer8/args16，请求low32=24/high32=28。本阶段无kernel安装。
- P2 PASS：新runtime读本W真实绑定，common/runtime/launcher已扫描无旧W4/W5 root/PID/startticks。保留显式O_RDONLY stdin、single-link根内stdio与inherited-FD关闭规则。新launcher相对授权W004只读baseline仅增加精确FIOCLEX request分支；其他arch/x32/PR_SET_NAME/network/metadata/Landlock rights源码保持。baseline121→candidate126 instructions，逐instruction/offset/jump/source diff保存。
- P3 PASS：11个mandatory+extra case，24,240组语义比较，61个jump target及所有路径显式终止通过。仅4组正确arch、ioctl16且request恰为FIOCLEX的参数组合产生预期ALLOW差异；其余与baseline等价。pure evaluator无kernel安装/probe。

## P4 唯一 R0-A1 及精确停止

唯一命令UTC 2026-11-15T01:21:38.944026+00:00 至01:21:40.221839+00:00，耗时1.277822054秒，exit1，无timeout。tracer PID248962，target PID248966，同一target有两次Python exec，probe child/grandchild=0。
当前实际ABI6、NNP、ruleset create/add/restrict与126-instruction seccomp安装全部成功。parent stdin O_RDONLY /dev/null、launcher fd0只读、fd1/2根内single-link regular、独立writable lock fd关闭均实证。第二Python bootstrap成功；current trace line1508 `ioctl(...confinement_probe.py, FIOCLEX)=0`。其他TCGETS/TIOCGWINSZ继续EPERM，未扩大allowlist；程序继续进入probe主体。
probe完成6项初始检查：inherited lock FD EBADF、真实HOME/CODEX不变、只读stdin、stdout/stderr根内、NoNewPrivs1/Seccomp2。随后tools/confinement_probe.py line41读取主控holder `/proc/248632/fdinfo/3`。trace line2240 `openat(..., O_RDONLY|O_CLOEXEC)=-1 EACCES`，PermissionError触发STOP/exit1。
这是受限probe对另一个holder进程fdinfo的只读访问失败。未在本W进一步区分procfs/LSM机制，不写成kernel不支持、静态filter失败或FIOCLEX失败；未调整/重试。父runtime前后独立读holder/竞争仍成立，但这不抹去受限域内该检查失败。
指定inside FD的FIOCLEX→F_GETFD效果测试尚未到达，不能用早先不同descriptor的F_GETFD代替。inside创建/rename/remove、全部negative create/readonly-home-dir、child/grandchild、symlink、socket/connect未达。当前bootstrap FIOCLEX成功是独立子事实，不是confinement PASS。

## Trace 与未执行边界

单个完整full trace：trace/r0a1.248966，2290行，SHA256 `f03fdd32f65a06a9973da446c20b352e955cd4c4167380c8d19953e79f84fbf8`。3次successful write共6594bytes：launcher receipt4472、probe-main失败receipt1977、stdout145，全部映射本W根内；两个成功write-open亦根内，unknown write path0，成功外部文件write0，无proc comm open/write，无shared writable file mmap。stdout/stderr和全部trace原文保留，0byte stderr为真实执行日志，不是空条件产物。IPC既有只读attach及默认ioctl拒绝均显式纳入审阅。
上述只覆盖失败链；不外推全W或global zero outside writes。R0-A未PASS，R0-B/C未进入，不判两个closure都失败，四预算/continuous monitors未证，条件八EP未建设。新增EP满足0，仅继承C0014 SCENARIO04 PARTIAL，SHARED03 UNSATISFIED，其余六NOT_ATTEMPTED。
所有single/partial/full场景、normal、DBA/wrapper/native-reader、current/production材料、build/compile/serialization、dependency install/download、shared source写/push均0。未生成空patch/fixture/commit。具名输入immutability审阅不冒充全BASE/HOME扫描。

## 交付与正式Return接续

LOCAL_STAGE_HANDOFF.json逐字映射16项ORDER deliverables、列真实missing；PUBLICATION_MANIFEST.json列全部实际文件的绝对路径、bytes/SHA256/精确出版目标，HASHES与外层FREEZE_RECEIPT封存并避免自hash循环。完整本turn命令与FileChange原文保存，封存命令未发生终态不虚构，实际exit由执行器回执给出。
主控逐字运输到longrun/runs/OI-EAW-WALL-20261114-01/delegations/D003/results/W006/。当前无真实出版commit/ref，result_ref保持null；Worker不写GitHub。主控出版/远端回读核对后回传真实refs，同原W1同W006仅在final-return新写正式v2 Return/validation，由主控出版到worker_results/W006/，只回原E1。E1/manager负责专业接受/后继/父任务。本地有限Goal结束后自然停止，不常驻轮询。
'''
with (ROOT/'artifacts/WORKER_EXECUTION_REPORT.md').open('x') as out:out.write(report)
stop='''# W006 工程停止报告

outcome STOP / PREFLIGHT_STOP / STOP_PROBE_HOLDER_FDINFO_READ_EACCES。
P0/P1/P2/P3全部实际PASS；唯一P4 kernel安装和第二Python/bootstrap FIOCLEX成功，probe主体已进入。
tools/confinement_probe.py line41只读打开/proc/248632/fdinfo/3返回EACCES（trace/r0a1.248966 line2240），PermissionError/exit1。未更改policy/guard/probe，没有重试。具体procfs/LSM归因未进一步调查；不笼统称Linux不支持。
inherited writable FD关闭与父侧holder锁完整为独立已证事实；受限域内holder只读检查未完成，后续inside/negative/child/network/F_GETFD effect probes未达。current FIOCLEX=0不能升级confinement PASS。
完整2290行失败链3次成功write/6594bytes均根内，仅该范围outside文件write0/unknown路径0，不作全局证明。
严格未进入R0-B/C和条件八EP，不跑场景/normal/current生产动作，不扩allowlist、不修改W1–W5/shared。完整真实缺口与逐项交付见LOCAL_STAGE_HANDOFF.json；真实refs尚待主控出版，同单正式Return稍后仅回原E1。
'''
with (ROOT/'artifacts/ENGINEERING_STOP_REPORT.md').open('x') as out:out.write(stop)

order=json.loads((ROOT/'input/C0014-remote-work_orders--W006--ORDER.json').read_bytes())
groups=[['WORKER_EXECUTION_REPORT.md'],['W006_BINDING.json'],['CONTROLLER_SENTINEL_PRECONFIRMATION.json'],['HISTORICAL_FIOCLEX_PHASE_CLASSIFICATION.json'],['FIOCLEX_LOCAL_CONSTANT_VERIFICATION.json','SECCOMP_DATA_LAYOUT_VERIFICATION.json'],['PARENT_RUNTIME_BINDING_DELTA.json'],['SECCOMP_IOCTL_FILTER_DELTA.json'],['SECCOMP_FILTER_STATIC_EVALUATION.json'],['WRITE_CONFINEMENT_REPORT.json','FULL_WRITE_TRACE_REVIEW.json'],['OFFLINE_CLOSURE_REPORT.json'],['RESOURCE_BUDGET_REPORT.json'],['PHASE0_RECOVERY_VERDICT.json'],['COMMAND_LOG.jsonl','WRITE_SURFACE_AUDIT.json','EP_ACCEPTANCE_MATRIX.md','PUBLICATION_MANIFEST.json','HASHES.sha256'],[],['ENGINEERING_STOP_REPORT.md'],[]]
assert len(groups)==len(order['deliverables'])==16
mapping=[]
for i,(literal,files) in enumerate(zip(order['deliverables'],groups)):
    mapping.append({'deliverable_literal':literal,'local_files':[str(ROOT/'artifacts'/n) for n in files],'status':'LOCAL_FACTUAL_STOP_PACKAGE' if files else 'CONDITIONAL_NOT_ENTERED' if i==13 else 'PENDING_TRUE_PUBLISHED_REFS_THEN_FORMAL_RETURN','note':'真实报告/成功子事实/未完成缺口；不把证明式标签当作实质PASS。' if files else '无四PASS，不造空条件产物。' if i==13 else '未来自身尚无ref，不伪造。'})
save('artifacts/LOCAL_STAGE_HANDOFF.json',{'schema':'local-worker-stage-handoff/v1','run_id':b['run_id'],'work_order_id':'W006','worker':b['worker'],'return_to':b['return_to'],'outcome':'STOP','gate':'PREFLIGHT_STOP','stop_code':STOP,'missing':missing,'deliverable_mapping':mapping,'publication_target_root':'longrun/runs/OI-EAW-WALL-20261114-01/delegations/D003/results/W006/','real_publication_commit':None,'result_ref':None,'formal_Return_created':False,'formal_Return_later_target':'longrun/runs/OI-EAW-WALL-20261114-01/worker_results/W006/WORKER_RETURN.json','next_steps':['主控逐字出版冻结原件并远端核bytes/hash/Gitblob。','主控回传准确真实refs/hash到同原W1同W006。','本Worker仅final-return新写v2 Return/validation，主控出版，仅回原E1。','E1/manager决定专业接受与后继，本地Goal不代表W/D/父任务完成。']})
save('audit/ARCHIVE_RESULT_RECEIPT.json',{'at':utc(),'source':fact(__file__),'scope':'停止后仅完整trace审阅、日志/输入核对与报告归档','P0_P3':'PASS','P4':'STOP','attempts':1,'evaluator_rerun_after_kernel':False,'kernel_or_probe_retried':False,'closure_budget_EP_entered':False,'new_phase0_gate_PASS':False,'local_input_originals_checked':len(input_checks),'extra_controller_sources_checked':len(extra_checks),'missing_count':len(missing),'trace_review':fact(ROOT/'artifacts/FULL_WRITE_TRACE_REVIEW.json'),'lock_end':guard()})
print(json.dumps({'outcome':'STOP','stop_code':STOP,'P0_P3':'PASS','R0_A1_attempts':1,'R0_A1_exit':1,'trace_lines':len(lines),'successful_write_count':len(writes),'successful_write_bytes':6594,'failed_chain_outside_file_writes':0,'failed_chain_unknown_write_paths':0,'missing_count':len(missing),'report':fact(ROOT/'artifacts/WORKER_EXECUTION_REPORT.md')},ensure_ascii=False))
