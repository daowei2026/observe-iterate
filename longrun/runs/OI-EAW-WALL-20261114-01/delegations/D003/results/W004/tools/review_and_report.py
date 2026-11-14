from pathlib import Path
import sys,json,re,collections,hashlib,os
R=Path('/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D003/W004');sys.path.insert(0,str(R/'tools'));import runtime as w
w.guard();A=R/'artifacts';stamp=w.utc();order=json.loads((R/'input/C0012-remote-work_orders--W004--ORDER.json').read_text());launcher=json.loads((R/'receipts/r0a1-launcher.json').read_text());parent=json.loads((R/'receipts/r0a1-parent-stdin.json').read_text());delta=json.loads((A/'PARENT_LAUNCHER_WIRING_DELTA.json').read_text());command=json.loads((R/'logs/COMMAND_LOG.jsonl').read_text().strip());assert command['id']=='r0a1' and command['exit_code']==2 and not command['timeout'];assert launcher['status']=='KERNEL_POLICY_INSTALLED_BEFORE_EXEC' and launcher['abi']==6 and all(c['errno']==0 and c['return']>=0 for c in launcher['calls']);assert len(launcher['calls'])==6 and launcher['stdio_fds'][0]['access_mode']==0 and launcher['stdio_fds'][0]['path']=='/dev/null';assert parent['access_mode']=='O_RDONLY' and parent['parent_close_result']=='CLOSED_OWN_COPY_SUCCESS';assert launcher['seccomp_denied_syscalls']['ioctl']==16
assert w.filefact(R/'tools/runtime.py')['sha256']==delta['new_runtime_sha256'] and w.filefact(R/'tools/landlock_launcher.py')['sha256']==delta['new_launcher_sha256'];assert not list((R/'receipts').glob('r0a1-main.json'))
traces=sorted((R/'trace').glob('r0a1.*'));assert len(traces)==1;hist=collections.Counter();writes=[];opens=[];maps=[];mutations=[];ipc=[];denials=[];executions=[];unknown=[];comm=[];evidence=[];unparsed=[]
write_names={'write','writev','pwrite64','pwritev','pwritev2','sendfile','copy_file_range','splice','vmsplice','tee'};mut_names={'truncate','ftruncate','rename','renameat','renameat2','link','linkat','symlink','symlinkat','unlink','unlinkat','mkdir','mkdirat','rmdir','mknod','mknodat','chmod','fchmod','fchmodat','fchmodat2','chown','fchown','lchown','fchownat','utime','utimes','futimesat','utimensat','setxattr','lsetxattr','fsetxattr','removexattr','lremovexattr','fremovexattr','msync','fallocate'}
for p in traces:
 lines=p.read_text().splitlines();assert lines[-1].endswith('+++ exited with 2 +++');evidence.append({**w.filefact(p),'lines':len(lines),'normal_terminal_exit':2})
 for n,line in enumerate(lines,1):
  m=re.match(r'^[\d.]+\s+(\w+)\((.*)\)\s+=\s+(.*)$',line)
  if not m:
   if '+++ exited with ' not in line:unparsed.append({'line':n,'raw':line})
   continue
  name,args,ret=m.groups();hist[name]+=1;v=re.match(r'(-?(?:0x[0-9a-f]+|\d+))',ret);value=int(v.group(1),0) if v else None;success=value is not None and value>=0;ev={'trace':str(p),'line':n,'syscall':name,'raw':line,'return_text':ret}
  if name in write_names and success:
   dest=re.match(r'\d+<([^>]+)>',args);dest=dest.group(1) if dest else None;ev={**ev,'destination':dest,'actual_return_bytes':value,'inside_WORK_ROOT':bool(dest and Path(dest).is_absolute() and Path(dest).is_relative_to(R))};writes.append(ev)
   if dest is None:unknown.append(ev)
  if name in {'open','openat','openat2','creat'} and success and any(s in args for s in ['O_WRONLY','O_RDWR','O_CREAT','O_TRUNC']):
   dest=re.match(r'\d+<([^>]+)>',ret);dest=dest.group(1) if dest else None;opens.append({**ev,'destination':dest,'inside_WORK_ROOT':bool(dest and Path(dest).is_relative_to(R))})
   if dest is None:unknown.append(ev)
  if name in mut_names:mutations.append({**ev,'success':success})
  if name=='mmap' and 'MAP_SHARED' in args:maps.append({**ev,'success':success,'writable':'PROT_WRITE' in args})
  if name in {'shmget','shmat','shmdt','shmctl'}:ipc.append({**ev,'success':success})
  if name=='ioctl' and 'EPERM' in ret:denials.append(ev)
  if name=='execve':executions.append(ev)
  if '/proc/' in args and '/comm' in args:comm.append(ev)
assert not unparsed and not unknown and len(writes)==2 and sum(e['actual_return_bytes'] for e in writes)==4628 and all(e['inside_WORK_ROOT'] for e in writes+opens);assert not any(e['success'] and e['writable'] for e in maps);assert len(executions)==2
failure=next(e for e in denials if 'FIOCLEX' in e['raw']);assert failure['line']==1509
trace_report={'record_type':'W004_FULL_WRITE_TRACE_REVIEW','utc':stamp,'status':'COMPLETE_FOR_SINGLE_POLICY_INSTALLED_BOOTSTRAP_FAILURE','scope':'唯一PID244050：launcher execve、policy安装、同PID execve新Python、脚本fopen bootstrap失败至exit2。未执行probe脚本主体，未fork child/grandchild；父控制面/原生平台不在此trace内。','trace_configuration':{'absolute_tool':'/usr/bin/strace','flags':['--kill-on-exit','-ff','-yy','-ttt','-s128','-e trace=all'],'raw_read_payloads':'read/pread/readv/recv payload不复制，syscall仍完整覆盖；write-family保持FD/path/return解码。','displayed_buffer_limit':'-s128仅截显示字节缓冲，不截FD/path、返回写字节数或syscall列表。'},'trace_files':evidence,'histogram':dict(hist),'unparsed_records':unparsed,'successful_descriptor_writes':writes,'successful_descriptor_write_count':2,'successful_descriptor_write_bytes':4628,'successful_outside_descriptor_writes_in_this_trace':0,'unknown_write_paths':unknown,'successful_writable_or_creating_opens':opens,'other_file_mutation_calls':mutations,'shared_maps':maps,'SysV_IPC_calls':ipc,'SysV_IPC_note':'两次启动的IPC_CREAT|IPC_EXCL均EEXIST；取得既有shmid0后SHM_RDONLY attach。未见成功新IPC对象或writable shared mapping。','all_execve_events':executions,'post_policy_ioctl_EPERM':denials,'fatal_script_bootstrap_ioctl':failure,'proc_comm_events':comm,'proc_comm_status':'NO_OPEN_OR_WRITE_OBSERVED','kernel_setup_trace_lines':{'ABI':1182,'NNP':1183,'create':1184,'add':1186,'restrict':1187,'seccomp':1190,'own_contending_lock_FD_close':1180,'next_Python_execve':1198},'script_read_correction':'openat(script,O_RDONLY)在1508行成功；1509行ioctl(FIOCLEX)返回EPERM；先前O_CLOEXEC路径还成功读取5069字节用于启动。不能把报错简化为Landlock拒绝openat或脚本不可读。','no_global_or_future_zero_external_write_claim':True,'WRITE_CONFINEMENT_PASS':False}
w.save('artifacts/FULL_WRITE_TRACE_REVIEW.json',trace_report)
requirements=['inside-root create/write/rename/remove','OUTSIDE create/write kernel denial and no file','SHARED new-file open denied','HOME/CODEX unchanged, readable and new-create denied','child/grandchild inherit restriction','symlink escape denial','preopened writable FD closed and holder intact','network socket/connect denial or equivalent offline','full trace for all required probes']
probes=[{'index':i,'requirement':name,'status':'NOT_EXECUTED_PROBE_SCRIPT_BOOTSTRAP_FAILURE'} for i,name in enumerate(requirements,1)];probes[6].update(status='LAUNCHER_FD_CLOSE_AND_PARENT_POST_LOCK_CHECK_VERIFIED_ONLY',detail='独立O_RDWR锁FD3在1180行关闭；父runtime结束后的guard仍同inode竞争EAGAIN。probe内fstat EBADF和子孙继承未执行。');probes[8]['detail']='本次实际launcher/第二Python启动被全trace覆盖；probe主体未执行，不能算九项probe全PASS。'
confinement={'record_type':'W004_WRITE_CONFINEMENT_REPORT','utc':stamp,'outcome':'STOP','status':'RECOVERY_STOP_WRITE_CONFINEMENT','specific_stop':'PROBE_BOOTSTRAP_IOCTL_FIOCLEX_EPERM','R0_A0_static_review':delta['status'],'actual_parent_stdin':parent,'actual_launcher_stdio':launcher['stdio_fds'],'parent_child_readonly_stdin_wiring_pass':True,'controller_sentinel_preconfirmation_pass':True,'sentinel_preconfirmation':w.filefact(A/'CONTROLLER_SENTINEL_PRECONFIRMATION.json'),'kernel_policy_setup_calls_success':True,'ABI_observed':launcher['abi'],'kernel_calls':launcher['calls'],'policy_rights':launcher['handled_filesystem_rights'],'only_write_allow_root':str(R),'filesystem_write_exceptions':launcher['filesystem_write_exceptions'],'seccomp_denied_syscalls':launcher['seccomp_denied_syscalls'],'inherited_FDs_closed':launcher['inherited_nonstdio_fds_closed'],'launcher_receipt':w.filefact(R/'receipts/r0a1-launcher.json'),'single_attempt':{'count':1,'started_at':command['started_at'],'completed_at':command['completed_at'],'elapsed_seconds':command['elapsed_seconds'],'exit_code':2,'timeout':False,'parent_Popen_child_strace_pid':command['pid'],'tracee_launcher_then_interpreter_pid':244050,'probe_script_body_entered':False,'child_grandchild_spawned':0,'automatic_retry_or_parameter_change':False},'actual_failure':failure,'cause_zh':'候选seccomp按syscall号整体拒绝ioctl(16)，已安装后Python脚本fopen所用FIOCLEX ioctl返回EPERM。脚本O_RDONLY open/read可成功，probe主体未运行。保留该兼容性停止点，不调整policy到成功。','not_a_Landlock_ABI_right_or_create_add_restrict_failure':True,'probes':probes,'WRITE_CONFINEMENT_PASS':False,'actual_successful_write_scope':'本trace仅两个成功write，4462字节launcher receipt和166字节stderr，均在W004。','outside_successful_writes_observed_in_trace':0,'global_or_future_zero_outside_writes_proven':False,'R0_B_C_or_EP_entered':False,'HOME':launcher['HOME'],'CODEX_HOME':launcher['CODEX_HOME'],'HOME_or_CODEX_HOME_reset':False}
w.save('artifacts/WRITE_CONFINEMENT_REPORT.json',confinement)
closure={'record_type':'W004_OFFLINE_CLOSURE_REPORT','utc':stamp,'status':'NOT_ATTEMPTED_R0A_GATE','OFFLINE_CLOSURE_PASS':False,'selected_environment':None,'candidates':[{'id':'E','declaration':'exact frp stack.yaml/lts18.28','status':'NOT_INVESTIGATED_THIS_W004'},{'id':'B','declaration':'BASE overlay/lts22.24/historical GHC9.4.8','status':'NOT_INVESTIGATED_THIS_W004'}],'compiler_tool_hashes_packageDB_dependency_mapping':None,'transitive_package_ids':None,'missing_dependencies':None,'minimum_rebuild_set':None,'exact_base_compatibility_proven':False,'no_network_proof_for_future_closure':False,'environments_mixed':False,'Haskell_Stack_Cabal_GHC_metadata_invocations':0,'8_exact_git_objects_read_this_W004':False,'reason':'R0-A必需probe尚未运行且解释器bootstrap退出2；禁止进入R0-B。未把两候选未调查改写成已实测失败；未复用旧W3资料冒充本W closure事实。'}
w.save('artifacts/OFFLINE_CLOSURE_REPORT.json',closure)
budgets=[{'metric':n,'unit':u,'cap':c,'predicted_value':None,'predicted_upper_bound':None,'comparable_measured_evidence':None,'monitor_verified':False,'stop_threshold':c,'status':'NOT_ATTEMPTED_R0A_GATE'} for n,u,c in [('new_disk','bytes',2*1024**3),('peak_RSS','bytes',4*1024**3),('post_preflight_wall','seconds',1500),('new_files','files',50000)]]
resources={'record_type':'W004_RESOURCE_BUDGET_REPORT','utc':stamp,'status':'NOT_ATTEMPTED_R0A_GATE','FOUR_BUDGETS_KNOWN_WITHIN_CAP':False,'CONTINUOUS_MONITORS_PASS':False,'metrics':budgets,'continuous_monitor_verification':{'monotonic_post_preflight_deadline':False,'whole_process_group_RSS':False,'root_disk_files':False,'all_descendants':False,'threshold_kill_receipt':False},'existing_comparable_artifact_build_logs_read':False,'actual_single_R0A1_elapsed_seconds':command['elapsed_seconds'],'actual_R0A1_command_timeout_seconds':45,'timeout_triggered':False,'command_timeout_not_budget_monitor_proof':True,'reason':'R0-A必需probe未通过，R0-B/C均未进入。固定cap和小命令耗时不能代替同compiler/closure/target可比实测的工程预测。'}
w.save('artifacts/RESOURCE_BUDGET_REPORT.json',resources)
verdict={'record_type':'W004_PHASE0_RECOVERY_VERDICT','utc':stamp,'run_id':order['run_id'],'work_order_id':'W004','outcome':'STOP','verdict':'PREFLIGHT_STOP','stop_reason':'RECOVERY_STOP_WRITE_CONFINEMENT','specific_stop':'PROBE_BOOTSTRAP_IOCTL_FIOCLEX_EPERM','R0_A0_stdin_wiring':'PASS_STATIC_AND_ACTUAL_PARENT_CHILD','controller_sentinel_preconfirmation':'PASS_READONLY_ENOENT_RECEIPT_COPIED','kernel_setup':'ABI6_NNP_LANDLOCK_CREATE_ADD_RESTRICT_AND_SECCOMP_SUCCESS','four_requirements':{'WRITE_CONFINEMENT_PASS':{'pass':False,'status':'PROBE_BOOTSTRAP_FAILED_EXIT2'},'OFFLINE_CLOSURE_PASS':{'pass':False,'status':'NOT_ATTEMPTED_R0A_GATE'},'FOUR_BUDGETS_KNOWN_WITHIN_CAP':{'pass':False,'status':'NOT_ATTEMPTED_R0A_GATE'},'CONTINUOUS_MONITORS_PASS':{'pass':False,'status':'NOT_ATTEMPTED_R0A_GATE'}},'independent_successful_subfacts':['任务7209 bytes/hash、22文件镜像hash和Owner/D003/W004字面子集校验','原W1实际Sol/max/cwd/owner/current turn及fresh锁PID243622/startticks47124402/inode14806399和竞争EAGAIN','主控sentinel只读ENOENT回执656bytes/hash完全匹配，逐字复制；其余4目标只读ENOENT','只修stdin/receipt/new-root/binding的逐行delta；父fd6与launcher fd0为O_RDONLY /dev/null，父关闭自己副本','独立writable lock FD3在policy前关闭，holder仍在并竞争失败','当前ABI6和六个setup API均errno0；policy在exec前成功安装，后继exec成功并观察ioctl拒绝','1518行完整trace的两个实际write均映射W004内路径，无未知write路径'], 'R0_B_entered':False,'R0_C_entered':False,'Phase1_2_entered':False,'scenario_runs':0,'build_compile_serialization_runs':0,'automatic_retry':False,'global_zero_outside_writes_proven':False,'local_terminal_scope':'仅本地停止原件交付；不作W专业接受、D003、action、H3、G-RUN或父任务完成决定。'}
w.save('artifacts/PHASE0_RECOVERY_VERDICT.json',verdict)
conditional=['SOURCE_BASELINE_AND_STAGING_REPORT.md','SOURCE_CHANGE_MANIFEST.json','PREREQUISITE_PATCHSET.diff','PRECONDITION_REPORT.md','D003_BINDING_CANDIDATE.json','FIXTURE_SCHEMA_AND_PROVENANCE.md','FX_WALL_SCENARIO_001.schema.json','FX_WALL_SCENARIO_001.json','KNOWN_CONTRACT_CONFLICTS.md','COMPILE_ONLY_REPORT.json','SERIALIZATION_TEST_REPORT.json','STAGED_LOCAL_COMMIT_REPORT.json']
missing=[{'id':'M-R0A1-BOOTSTRAP','detail':'NNP/Landlock ABI6 create/add/restrict/seccomp均已成功，后继Python启动以ioctl(FIOCLEX) EPERM/exit2停止；probe主体未运行，WRITE_CONFINEMENT_PASS=false。保留原policy，不自动重试。'},{'id':'M-REQUIRED-PROBES','detail':'inside/outside/shared/HOME/CODEX新写拒绝、child/grandchild、symlink和network等实测缺；已有stdin只读、锁FD关闭、policy安装和限域trace不能替代九项probe。'},{'id':'M-CLOSURE','detail':'R0-B未进入；单一兼容offline resolver/compiler/tools/packageDB/传递依赖/rebuild set和missing deps为空未证。8个exact git source对象未在本W读取。'},{'id':'M-BUDGETS-MONITORS','detail':'R0-C未进入；四项非空预测/可比依据及连续监测/阈值kill receipt缺。'},{'id':'M-CONDITIONAL-EP','detail':'四PASS未成立，Phase1/2和八EP未实施；未产出staged source/patch/DTO/schema/9-18-22 fixture/compile/serialization/local commit，不造空文件。'},{'id':'M-STATIC-LEDGER','detail':'只继承C0012 E1对旧SCENARIO-04的PARTIAL静态输入；无新target manifest或current result，不能冒充本W新增EP满足。'},{'id':'M-PUBLICATION','detail':'本地W004原件尚未真实出版，无真实新commit/ref；待主控按清单逐字运输并回传真refs/bytes/hash。'},{'id':'M-FORMAL-RETURN','detail':'本地阶段不生成正式Return；同一原W1同W004取得真实已出版证据refs后再生成V2，仅回原E1，正式Return自身再由主控出版至worker_results/W004/WORKER_RETURN.json。'}]
names=[['WORKER_EXECUTION_REPORT.md'],['W004_BINDING.json'],['CONTROLLER_SENTINEL_PRECONFIRMATION.json'],['PARENT_LAUNCHER_WIRING_DELTA.json'],['WRITE_CONFINEMENT_REPORT.json','FULL_WRITE_TRACE_REVIEW.json'],['OFFLINE_CLOSURE_REPORT.json'],['RESOURCE_BUDGET_REPORT.json'],['PHASE0_RECOVERY_VERDICT.json'],['COMMAND_LOG.jsonl','WRITE_SURFACE_AUDIT.json','EP_ACCEPTANCE_MATRIX.md','PUBLICATION_MANIFEST.json','HASHES.sha256'],[],['ENGINEERING_STOP_REPORT.md'],[]];mapping=[]
for i,(literal,files) in enumerate(zip(order['deliverables'],names),1):
 e={'index':i,'literal_ORDER_deliverable':literal,'local_files':[str(A/n) for n in files],'status':'LOCAL_READY'}
 if i==10:e.update(status='NOT_APPLICABLE_FOUR_PASS_NOT_MET',conditional_files_not_created=conditional,reason='PREFLIGHT_STOP；不得进入条件工程。')
 if i==12:e.update(status='DEFERRED_UNTIL_REAL_PUBLICATION_REFS',reason='两阶段出版合同；不造future/self ref。',return_to=order['return_to'],transport_target='longrun/runs/OI-EAW-WALL-20261114-01/worker_results/W004/WORKER_RETURN.json',real_ref=None)
 mapping.append(e)
handoff={'schema':'w004-local-stage-handoff/v1','utc':stamp,'run_id':order['run_id'],'work_order_id':'W004','worker':order['worker'],'return_to':order['return_to'],'order_ref':'daowei2026/observe-iterate@347e4b2322ff2401aca21333cd3118f93d490baf:longrun/runs/OI-EAW-WALL-20261114-01/work_orders/W004/ORDER.json','outcome':'STOP','phase0_verdict':'PREFLIGHT_STOP','specific_stop':verdict['specific_stop'],'resolved_prior_preconditions':['显式只读stdin父子接线','主控sentinel预确认原件已核并逐字复制'],'missing':missing,'deliverable_mapping':mapping,'actual_write_root':str(R),'local_result_path':str(A/'WORKER_EXECUTION_REPORT.md'),'result_ref':None,'real_publication_commit':None,'publication_target_prefix':'longrun/runs/OI-EAW-WALL-20261114-01/delegations/D003/results/W004/','transport_mapping':'W004/artifacts/<name>发布到目标根同名；其余W004/<relative>保留相对路径，逐字运输。','formal_Return_generated':False,'next_steps':['主控按PUBLICATION_MANIFEST/HASHES/FREEZE_RECEIPT逐字出版本地证据并真实回读。','真实commit/ref/hash/bytes回传同原W1同W004。','同单核真后生成正式V2 Return及独立校验，仅回原E1，由主控出版到worker_results/W004/。'],'business_acceptance_or_parent_completion_claim':False,'no_polling_or_other_chat':True}
w.save('artifacts/LOCAL_STAGE_HANDOFF.json',handoff)
EP='''# W004 本地 EP 事实矩阵

R0-A0接线和sentinel前置已修复，kernel setup API成功；R0-A1在Python脚本bootstrap的ioctl(FIOCLEX)被拒后exit2，未进入R0-B/C和Phase1/2。以下继承C0012 E1状态，只记录当前工程事实，不替代专业判断。

| EP | 继承E1状态 | W004事实与缺口 |
|---|---|---|
| EP-WALL-SHARED-01 | NOT_ATTEMPTED | 无新snapshot/accessor、patch/typecheck |
| EP-WALL-SHARED-02 | NOT_ATTEMPTED | 无新DTO/schema/canonical roundtrip/hash |
| EP-WALL-SHARED-03 | UNSATISFIED | 只读stdin和policy安装有新成功子事实；必需probe、closure、预算/monitor仍未证 |
| EP-SCENARIO-01 | NOT_ATTEMPTED | 未构造dedicated target/component/main/manifest |
| EP-SCENARIO-02 | NOT_ATTEMPTED | 未构造exact-error synthetic serialization |
| EP-SCENARIO-03 | NOT_ATTEMPTED | 未构造transaction DTO和committed/uncommitted验证 |
| EP-SCENARIO-04 | PARTIAL（旧静态子集） | 保留旧ledger输入，未进入新target manifest，无current result |
| EP-SCENARIO-05 | NOT_ATTEMPTED | 未物化完整9/18/22 fixture，无static parse/count/order/hash |

SATISFIED=0，PARTIAL=1，UNSATISFIED=1，NOT_ATTEMPTED=6；本W新满足EP=0。所有single/partial/full scenario、normal、build/compile/serialization/current materials均0。来源为input/mirrors中C0012专业矩阵和本W真实回执/trace；不从源码或历史材料推断当前业务事实。
'''
(A/'EP_ACCEPTANCE_MATRIX.md').write_text(EP)
stop=f'''# W004 工程停止原件

outcome=STOP，verdict=PREFLIGHT_STOP，主原因RECOVERY_STOP_WRITE_CONFINEMENT，精确停止点PROBE_BOOTSTRAP_IOCTL_FIOCLEX_EPERM。

唯一R0-A1：{command['started_at']} → {command['completed_at']}，{command['elapsed_seconds']:.6f}秒，exit2，未超时。父Popen启动strace PID{command['pid']}；tracee PID244050先执行launcher，再在同PID execve新Python。父stdin fd6及launcher fd0均为O_RDONLY /dev/null（F_GETFL=32768），父副本已finally关闭。独立open-file-description的writable锁FD3于trace第1180行关闭；主控PID243622/startticks47124402/inode14806399仍持FLOCK，父guard随后竞争EAGAIN。已按原件复制656字节sentinel只读ENOENT回执，其余四目标只读核ENOENT。

本W实测ABI6，NNP、Landlock create/add/restrict和seccomp安装均成功、errno0，安装发生在第二execve之前。第二execve在1198行成功；Python曾成功O_RDONLY open/read脚本。精确fatal为1508行O_RDONLY open成功后，1509行ioctl(fd3,FIOCLEX)=-1 EPERM；候选seccomp原规则整体拒绝ioctl syscall16。脚本主体和九项probe未执行，child/grandchild未产生。它是policy与解释器脚本启动的兼容性停止点，不能描述为fd0再次失败、Landlock ABI/rights不支持、openat/read失败或confinement PASS。

按C0012 ORDER，未调整policy、未加ioctl/dev/null写例外、未修改launcher到成功、未重试。R0-B/C及Phase1/2均未进入；不将未调查的两个resolver候选称已实测失败。没有当前业务证据、场景、normal、DBA、wrapper、native-reader、共享源码写/源码push；未联网、下载或安装。

完整1518行trace保留；唯一两个成功write为W004内launcher receipt4462字节和stderr166字节，共4628字节，未知write路径0，scope内成功外写0。未见/proc/*/comm open/write；不能扩成全W/全系统/后继零外写证明。policy setup成功也不能代替负向probe或八EP满足。

原W003及所有指定输入只读；本W只在{R}新增业务文件，HOME/CODEX_HOME保持真实值，未改变主控锁。完整逐项交付、missing及两阶段出版步骤见LOCAL_STAGE_HANDOFF.json。后续是否形成新修签或有界收束由原E1/manager决定；Worker不自行再开W或作专业接受/父任务完成决定。
'''
(A/'ENGINEERING_STOP_REPORT.md').write_text(stop)
report=f'''# W004 本地执行报告

**outcome=STOP，Phase0=PREFLIGHT_STOP**。R0-A0只读stdin接线和sentinel预确认已有真实成功证据；唯一R0-A1在已安装kernel policy之后，于Python脚本bootstrap的ioctl(FIOCLEX) EPERM处退出2。R0-B/C和条件八EP未进入。

## 工单、当前绑定与输入

原E1 C0012正式W004，ORDER JSON为`{handoff['order_ref']}`，Return只回`{order['return_to']}`。完整定位任务7209 bytes、SHA256 da90f19b6ee5408b208e62efe4beec5f2fae22a677ffaa1a228c5675f68ff25f。30输入ref映射中22文件hash已核并逐字只读复制；8个exact Git对象因R0-A停止尚未进入后继读取。当前D003和Owner literal grant逐字子集已核：

```text
operation=wall-observation-work execution_context=linux:/dwdhome/fy/BASE_E6_2 allowed_writes=/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01
```

沿用原W1物理聊天01a1da55-5881-7590-94a1-0661f0236977。原生当前turn_context实测gpt-6.1-sol/max、cwd=/dwdhome/fy/BASE_E6_2；owner PID2890/startticks20139/UID501现场核实。主控本次predispatch idle/canAccept、Goal null、queue空和旧turn completed记录已归档；旧keeper PID240810已不存在。新lock由PID243622/startticks47124402、session90041持有，inode14806399；同inode/new-open-description非阻塞flock竞争EAGAIN。Worker只关闭自己竞争/探针FD，不重取、替换或释放holder锁。

W004根派发前不存在，核无占用后新建。唯一新增业务写根`{R}`；HOME=/home/dw、CODEX_HOME=/home/dw/.codex未重设且业务只读。显式任务tmp/cache/config/log/trace/audit/receipts/artifacts均在本根。Python使用-I -S -B及PYTHONDONTWRITEBYTECODE=1，不产生外部pycache。W002/W003、shared、cgpterm和其他路径只读，不访问/m3varK或production materials/wrapper。

## R0-A0及sentinel

新runtime由旧脚本只读对照，在新根实现显式os.open('/dev/null',O_RDONLY|O_CLOEXEC)、F_GETFL验证、Popen(stdin=stdin_fd)和finally关闭。PARENT_LAUNCHER_WIRING_DELTA.json保留逐行diff、自hash和静态只读FD检查；未删除launcher fd0只读断言或其他继承FD规则。变化限stdin/receipt/new-root/binding；Landlock rights和seccomp候选规则未放宽。

父实际stdin fd6 flags32768/O_RDONLY，Popen子strace PID{command['pid']}；父关闭时间{parent['parent_close_timestamp']}。launcher实测fd0 /dev/null O_RDONLY、fd1/2为W004内常规单链接log文件。独立writable锁FD3被关闭，holder仍持锁且竞争失败。

主控sentinel精确路径为D003/.W004-deny-outside-C0012-e9ed948d；回执656 bytes、SHA256 d56b0541daeb37e39978b88ecafbc8fa3e562f882b46d8042b3ad669b3e5bc4a已核并逐字复制至CONTROLLER_SENTINEL_PRECONFIRMATION.json。其余SHARED/HOME/CODEX_HOME/SYMLINK_TARGET四个ORDER精确路径仅lstat核ENOENT；未创建/写入/清理。该预确认不是kernel拒绝证明。

## 唯一R0-A1实测与精确停止点

{command['started_at']} → {command['completed_at']}，{command['elapsed_seconds']:.6f}秒，exit2，45秒命令timeout未触发。ABI query返回6；NNP=0、ruleset create=fd3、add=0、restrict=0、seccomp=0，均errno0。唯一W004写allow rule、可用write/create/remove/refer/truncate/IOCTL_DEV rights和网络限制、metadata/syscall过滤的实际内容完整记录于launcher receipt。

trace第1198行第二Python execve成功。脚本曾经O_RDONLY|O_CLOEXEC open/read成功，随后第1508行O_RDONLY open亦成功；第1509行ioctl(FIOCLEX)返回EPERM。原候选seccomp整体拒绝ioctl(16)，Python脚本fopen启动因此报错。probe脚本主体未执行，main/child/grandchild probe receipt均不存在，不能造空文件。当前API安装成功、父子接线修复和内核拒绝是独立子事实，九项probe尚未PASS。

完整trace为trace/r0a1.244050：1518行、187074 bytes、SHA256 b2bcd39ff8886fa65815107bd95f333abef1bcb0a1ea69bb20010abc24b2c959。两个实际成功write均映射W004：launcher receipt4462 bytes、stderr166 bytes，总4628 bytes，未知write路径0、该scope成功外写0。两个execve在同PID，无fork子孙。startup IPC创建尝试均EEXIST、readonly attach，未见writable shared mapping或/proc/*/comm open/write。读payload以raw保留syscall，write-family保持路径及actual return；-s128不截系统调用覆盖。

停止后不调整policy、不改参数/脚本重试、不增外写例外。不能写成Landlock不支持、script open/read被Landlock拒绝或全局零外写已证。

## R0-B/C、四PASS与EP

WRITE_CONFINEMENT_PASS=false（probe bootstrap失败）；其余OFFLINE_CLOSURE_PASS、FOUR_BUDGETS_KNOWN_WITHIN_CAP、CONTINUOUS_MONITORS_PASS均false/NOT_ATTEMPTED_R0A_GATE。未运行Haskell/Stack/Cabal/GHC metadata、dry dependency plan、build/compile/test；未扫描cache、未混合E lts18.28和B lts22.24/historical GHC9.4.8。

四预算预测/可比实测/连续monitor均缺；固定cap仍2GiB disk、4GiB RSS、1500秒post-preflight、50000新files、outside writes0、scenario runs0。单命令0.829秒及45秒timeout不是后继工程预算/持续监测证明。

Phase1/2未进入，staged source、patch、DTO/schema、9/18/22 fixture、compile-only、synthetic serialization和local commit均未产出，不创建空替代文件。继承C0012 E1矩阵SATISFIED0、PARTIAL1（旧SCENARIO-04静态子集）、UNSATISFIED1（SHARED-03）、NOT_ATTEMPTED6；本W新满足EP0。所有single/partial/full scenario、normal、DBA、wrapper、native-reader、production/current材料生成和源码push均0。

## 原件、日志、限制与运输

所有最低STOP文件和12项逐字ORDER deliverable→本地文件映射见LOCAL_STAGE_HANDOFF.json。COMMAND_LOG含当前W004 turn全部已完成原生命令及唯一子命令完整stdout/stderr/trace路径；封存命令自身以argv和日志关闭点记录，不捏造当时未知exit。指定输入before/after hash/bytes/mtime/inode/dev见WRITE_SURFACE_AUDIT与audit；命名输入未变不外推全系统零写。原生平台会话沿原执行器续写，不作为业务写面。

PUBLICATION_MANIFEST列全部真实payload、bytes/hash/明确目标和retention。HASHES与FREEZE_RECEIPT按无环目录层级补齐索引自身hash，不造future/self ref。所有新增业务文件在W004根；仅有界枚举该小根及精确输入，不广搜BASE/HOME/cache、不联网、不安装。

主控逐字出版目标`{handoff['publication_target_prefix']}`，本地artifacts文件映射目标根同名，其余相对路径保留。当前本地阶段没有新GitHub commit/ref、没有正式Return。待主控真实回读refs/hash后同一W1同W004生成V2 Return及独立校验，仅回原E1，由主控运输到worker_results/W004/WORKER_RETURN.json。

本地Goal结束只表示原件交付；不决定W专业接受、D003、action eligibility、G-RUN、H3、父Q或父任务完成。不常驻轮询、不向其他聊天发消息、不自行新开W。
'''
(A/'WORKER_EXECUTION_REPORT.md').write_text(report)
w.guard();print(json.dumps({'outcome':'STOP','phase0':'PREFLIGHT_STOP','specific_stop':verdict['specific_stop'],'stdin_fixed':True,'sentinel_preconfirmed':True,'kernel_setup_success':True,'trace_lines':1518,'trace_successful_writes':2,'trace_write_bytes':4628,'trace_observed_outside_writes':0,'required_probes_executed':0,'R0B_C_or_EP_entered':False,'deliverables_mapped':len(mapping),'missing':len(missing)},ensure_ascii=False,indent=2))
