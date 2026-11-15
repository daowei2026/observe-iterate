"""仅归档已发生的W005停止，不执行/修复/重试准备器、evaluator或launcher。"""
from pathlib import Path
import datetime, errno, fcntl, hashlib, json, os, re, sys, termios

BASE=Path('/dwdhome/fy/BASE_E6_2')
ROOT=BASE/'.oi-runs/OI-EAW-WALL-20261114-01/D003/W005'
LOCK=ROOT.parents[1]/'.D003-writer.lock'
SESSION=Path('/home/dw/.codex/sessions/2026/11/14/rollout-2026-11-14T21-53-08-01a1da55-5881-7590-94a1-0661f0236977.jsonl')
TURN='01a1dc6f-c611-7ba1-8301-f0bef1f0eef0'
STOP='STOP_SECCOMP_STATIC_PREPARATION_ASSERTION'

def utc():return datetime.datetime.now(datetime.timezone.utc).isoformat()
def fact(p):
    p=Path(p);b=p.read_bytes();s=p.lstat()
    return {'path':str(p),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'mtime_ns':s.st_mtime_ns,'inode':s.st_ino,'dev':s.st_dev}
def save(n,o):
    p=ROOT/n;assert p.resolve().is_relative_to(ROOT)
    with p.open('x') as f:f.write(json.dumps(o,ensure_ascii=False,indent=2)+'\n')
def text(n,s):
    with (ROOT/n).open('x') as f:f.write(s)
def guard():
    assert Path.cwd()==BASE and ROOT.resolve()==ROOT and not any(p.is_symlink() for p in [ROOT,*ROOT.parents])
    assert os.environ['HOME']=='/home/dw' and os.environ['CODEX_HOME']=='/home/dw/.codex' and sys.dont_write_bytecode
    t=Path('/proc/246047/stat').read_text();assert t[t.rfind(')')+2:].split()[19]=='47679582'
    info=Path('/proc/246047/fdinfo/3').read_text();assert 'FLOCK' in info and 'WRITE 246047' in info and LOCK.lstat().st_ino==14806399
    fd=os.open(LOCK,os.O_RDWR|os.O_NOFOLLOW)
    try:
        assert os.fstat(fd).st_ino==14806399
        try:fcntl.flock(fd,fcntl.LOCK_EX|fcntl.LOCK_NB)
        except BlockingIOError as e:assert e.errno in [11,13]
        else:raise RuntimeError('STOP lock unexpectedly acquired')
    finally:os.close(fd)
    return {'at':utc(),'holder_pid':246047,'startticks':'47679582','inode':14806399,'fdinfo':info,'independent_same_inode_competition':'EAGAIN_OR_EACCES','holder_not_modified':True}

lock=guard()
assert SESSION.stat().st_size<25000000
commands={};changes={};context=None
with SESSION.open() as stream:
    for lineno,line in enumerate(stream,1):
        j=json.loads(line);p=j.get('payload',{})
        if j.get('type')=='turn_context' and p.get('turn_id')==TURN:
            context={k:p.get(k) for k in ['turn_id','cwd','model','effort']}
        if j.get('type')!='event_msg' or not isinstance(p,dict) or p.get('turn_id')!=TURN or p.get('type')!='item_completed':continue
        item=p['item'];record={'session_source':str(SESSION),'session_line':lineno,'timestamp':j.get('timestamp'),'turn_id':TURN,'item':item}
        if item.get('type')=='CommandExecution':commands[item['id']]=record
        if item.get('type')=='FileChange':changes[item['id']]=record
assert context=={'turn_id':TURN,'cwd':str(BASE),'model':'gpt-6.1-sol','effort':'max'}
attempts=[r for r in commands.values() if ' -B '+str(ROOT/'tools/prepare_static.py') in str(r['item'].get('command'))]
assert len(attempts)==1 and attempts[0]['item']['exit_code']==1
attempt=attempts[0]
output=attempt['item']['aggregated_output']
assert 'line 32' in output and "all('EPERM' in x['text'] for x in trace_lines)" in output and 'AssertionError' in output
assert not (ROOT/'tools/runtime.py').exists() and not (ROOT/'tools/landlock_launcher.py').exists()
assert not any((ROOT/'trace').iterdir()) and not any((ROOT/'probes').iterdir())
with (ROOT/'audit/NATIVE_COMMAND_COMPLETIONS.jsonl').open('x') as f:
    for r in commands.values():f.write(json.dumps(r,ensure_ascii=False)+'\n')
with (ROOT/'audit/NATIVE_FILE_CHANGES.jsonl').open('x') as f:
    for r in changes.values():f.write(json.dumps(r,ensure_ascii=False)+'\n')
save('receipts/STATIC_PREPARATION_FAILURE.json',{'status':'FAILED_STOP_NO_RETRY','stop_code':STOP,'attempts':1,'native_command_record':attempt,'stdout':'','stderr':output,'stdout_stderr_attribution':'该命令唯一输出为Python traceback；原生完整aggregated_output一并保留。','runtime_created':False,'launcher_created':False,'BPF_evaluator_entered':False,'kernel_policy_installed':False,'R0_A1_attempts':0,'preparer_source':fact(ROOT/'tools/prepare_static.py')})

verified=json.loads((ROOT/'input/VERIFIED_INPUTS.json').read_bytes())
checks=[]
for entry in [*verified['verified_local_inputs'],*verified['extra']]:
    before=entry['source'];after=fact(before['path'])
    assert before==after
    assert fact(entry['mirror']['path'])['sha256']==before['sha256']
    checks.append({'before':before,'after':after,'same_bytes_hash_mtime_inode_dev':True})
save('audit/INPUT_IMMUTABILITY_CHECK.json',{'status':'PASS_FOR_ENUMERATED_INPUTS','at':utc(),'checks':checks,'W004_originals_and_scripts_not_modified':True,'eight_git_objects_not_read_due_to_stop':verified['deferred_exact_git_objects'],'scope':'具名输入逐项；不声称扫描全部旧W/BASE/HOME。'})

old_trace=ROOT.parent/'W004/trace/r0a1.244050'
trace_lines=[{'line':i+1,'text':line} for i,line in enumerate(old_trace.read_text().splitlines()) if 'ioctl(' in line and 'FIOCLEX' in line]
assert len(trace_lines)==2 and '= 0' in trace_lines[0]['text'] and 'EPERM' in trace_lines[1]['text']
header=Path('/usr/include/asm-generic/ioctls.h')
header_value=int(re.search(r'^#define\s+FIOCLEX\s+(0x[0-9A-Fa-f]+)',header.read_text(),re.M).group(1),16)
assert header_value==termios.FIOCLEX==21585 and sys.byteorder=='little' and os.uname().machine=='x86_64'
save('artifacts/FIOCLEX_LOCAL_CONSTANT_VERIFICATION.json',{'status':'LOCAL_DEFINITIONS_AGREE_STATIC_PREPARER_STOPPED','symbol':'FIOCLEX','integer_decimal':termios.FIOCLEX,'integer_hex':hex(termios.FIOCLEX),'architecture':os.uname().machine,'endianness':sys.byteorder,'sources':[dict(fact(termios.__file__),module='termios',value=termios.FIOCLEX),dict(fact(header),value=header_value,definition='#define FIOCLEX 0x5451'),dict(fact('/usr/include/x86_64-linux-gnu/asm/ioctls.h'),include='<asm-generic/ioctls.h>')],'FIONCLEX':termios.FIONCLEX,'local_definitions_agree':True,'historical_trace_source':fact(old_trace),'historical_trace_matches':trace_lines,'preparation_failure':'错误的all(EPERM)断言把安装前成功调用与安装后拒绝调用混在一起。定义本身一致；不是发现另一个FIOCLEX常量。','verification_scope':'只读常量与既有trace；不是当前W005 kernel FIOCLEX结果。','preparer_not_fixed_or_rerun':True})
save('artifacts/SECCOMP_IOCTL_FILTER_DELTA.json',{'status':'NOT_PRODUCED_PREPARATION_FAILED','stop_code':STOP,'preparer_source':fact(ROOT/'tools/prepare_static.py'),'failure_receipt':'receipts/STATIC_PREPARATION_FAILURE.json','new_runtime_exists':False,'new_launcher_exists':False,'candidate_BPF_generated':False,'instruction_comparison_executed':False,'intended_delta_only':'verified FIOCLEX low32 and upper32==0 allow; all other ioctl deny; this intent was not executed/verified','old_W004_launcher_source':fact(ROOT.parent/'W004/tools/landlock_launcher.py'),'old_W004_runtime_source':fact(ROOT.parent/'W004/tools/runtime.py'),'old_sources_frozen':True,'no_claim_of_filter_acceptance':True})
case_names=['x86_64 ioctl(FIOCLEX)','x86_64 ioctl(FIONCLEX)','arbitrary ioctl','request upper32!=0','existing denied socket','ordinary allowed syscall','x32 syscall bit','wrong arch','jump bounds / no unintended fallthrough','non-ioctl legacy policy equivalence']
save('artifacts/SECCOMP_FILTER_STATIC_EVALUATION.json',{'status':'NOT_RUN_BLOCKED_BY_PREPARATION_ASSERTION','stop_code':STOP,'preparer_attempts':1,'evaluator_attempts':0,'mandatory_cases':[{'case':n,'status':'NOT_RUN','actual_result':None} for n in case_names],'program_installed':False,'static_PASS':False,'failure_receipt':'receipts/STATIC_PREPARATION_FAILURE.json','no_retry':True})

binding=json.loads((ROOT/'artifacts/W005_BINDING.json').read_bytes())
post_targets=[]
for x in binding['negative_prechecks']:
    try:os.lstat(x['path'])
    except FileNotFoundError as e:assert e.errno==2;post_targets.append({'path':x['path'],'label':x['label'],'operation':'os.lstat','absent':True,'errno':e.errno})
    else:raise RuntimeError('unexpected target now exists; do not delete')
save('audit/NEGATIVE_TARGET_POSTCHECK.json',{'at':utc(),'results':post_targets,'kernel_negative_probe_attempts':0,'writes_or_cleanup_to_targets':0,'scope':'readonly absence checks only'})
save('artifacts/WRITE_CONFINEMENT_REPORT.json',{'status':'NOT_ATTEMPTED_STATIC_PREPARATION_STOP','WRITE_CONFINEMENT_PASS':False,'R0_A1_attempts':0,'parent_child_runtime_instantiated':False,'read_only_stdin_wiring_exercised_in_W005':False,'inherited_FD_probe_exercised':False,'NNP_installs':0,'Landlock_installs':0,'seccomp_installs':0,'FIOCLEX_actual_kernel_result_W005':None,'F_GETFD_CLOEXEC_evidence':None,'nine_probes':[{'number':i+1,'name':n,'status':'NOT_RUN'} for i,n in enumerate(['inside create/write/rename/remove','OUTSIDE create/write deny','SHARED create deny','HOME/CODEX read allowed create deny','child/grandchild inheritance','symlink escape deny','inherited writable FD closed and holder intact','socket/connect deny','full trace covers all probes'])],'controller_sentinel_receipt_preserved':'CONTROLLER_SENTINEL_PRECONFIRMATION.json','negative_targets_pre_and_post_absent':True,'actual_HOME':'/home/dw','actual_CODEX_HOME':'/home/dw/.codex','HOME_CODEX_reset':False,'new_failure':STOP,'W004_facts_preserved_not_reexecuted':'W004 ABI6/NNP/Landlock/seccomp installed; second Python FIOCLEX EPERM before probe body. Those historical successes do not constitute W005 enforcement.','confinement_or_global_zero_write_PASS_claimed':False})
save('artifacts/FULL_WRITE_TRACE_REVIEW.json',{'status':'NO_W005_KERNEL_PROBE_TRACE','stop_code':STOP,'W005_trace_files':[],'W005_R0_A1_processes':0,'probe_children':0,'probe_grandchildren':0,'successful_descriptor_write_path_complete_proof':False,'outside_write_count_from_kernel_trace':None,'unknown_write_paths_from_kernel_trace':None,'proc_comm_writes_from_kernel_trace':None,'kernel_trace_absent_reason':'静态准备失败，按合同未启动launcher/strace/probe。','historical_W004_trace_mirror':'input/mirrors/17-r0a1.244050','historical_trace_is_current_measurement':False,'command_source_for_local_writes':'audit/NATIVE_COMMAND_COMPLETIONS.jsonl','no_global_zero_write_claim':True})
save('artifacts/OFFLINE_CLOSURE_REPORT.json',{'status':'NOT_ATTEMPTED_R0_A_BLOCKED','OFFLINE_CLOSURE_PASS':False,'selected_closure':None,'candidates':[{'id':'E','description':'exact frp stack.yaml / lts-18.28','current_evaluation':'NOT_ATTEMPTED'},{'id':'B','description':'BASE overlay / lts-22.24 / historical GHC9.4.8','current_evaluation':'NOT_ATTEMPTED'}],'resolver_or_compiler_or_package_DB_current_proof':None,'transitive_ids':None,'minimum_rebuild_set':None,'missing_dependencies':None,'missing_dependencies_empty_proven':False,'exact_git_objects_read':0,'git_objects_deferred':8,'stop_reason':STOP,'build_compile_test_download_install_executed':False,'no_claim_both_candidates_failed':True})
save('artifacts/RESOURCE_BUDGET_REPORT.json',{'status':'NOT_ATTEMPTED_R0_A_B_BLOCKED','FOUR_BUDGETS_KNOWN_WITHIN_CAP':False,'CONTINUOUS_MONITORS_PASS':False,'budgets':[{'name':n,'cap':cap,'predicted_upper_bound':None,'comparable_compiler_closure_measurement':None,'status':'NOT_ATTEMPTED'} for n,cap in [('new_disk_bytes',2147483648),('peak_RSS_bytes',4294967296),('post_preflight_wall_seconds',1500),('new_files',50000)]],'monitor_proof':{'monotonic_deadline':False,'whole_group_RSS':False,'root_disk_files':False,'descendants':False,'threshold_kill_receipt':False,'kernel_trace_outside_write_coverage':False,'HOME_CODEX_new_write_coverage':False},'local_readonly_preparation_elapsed_is_budget_proof':False,'phase1_2_entered':False,'stop_reason':STOP})
save('artifacts/PHASE0_RECOVERY_VERDICT.json',{'outcome':'STOP','gate':'PREFLIGHT_STOP','stop_code':STOP,'stop_phase':'R0-A0 static preparation, before BPF generation/evaluator','WRITE_CONFINEMENT_PASS':False,'OFFLINE_CLOSURE_PASS':False,'FOUR_BUDGETS_KNOWN_WITHIN_CAP':False,'CONTINUOUS_MONITORS_PASS':False,'local_FIOCLEX_definitions_agree':True,'BPF_static_acceptance_PASS':False,'R0_A1_attempts':0,'R0_B_attempts':0,'R0_C_attempts':0,'new_preparer_attempts':1,'automatic_retry':False,'policy_tuning_after_failure':False,'conditional_EP_entered':False,'scenario_runs':0,'normal_runs':0,'production_current_material_generated':False,'professional_acceptance_or_parent_completion_decided':False})

missing=[
 '静态准备脚本错误地要求旧trace中所有FIOCLEX均EPERM，遇到安装前成功记录后AssertionError/exit1；依新失败即停，未修复或重试。',
 'W005 runtime/launcher/BPF尚未物化；唯一request delta的逐instruction比较未执行。',
 '纯BPF evaluator未进入，arch/x32/FIOCLEX/FIONCLEX/arbitrary/high32/socket/ordinary/jumpbounds与非ioctl等价均未获验收PASS。',
 'R0-A1实际尝试0；NNP/Landlock/seccomp当前安装与FIOCLEX成功及F_GETFD_CLOEXEC证据均无。',
 '九项kernel probe及child/grandchild、read-only stdin/inherited FD接线均未在W005执行。',
 '没有W005完整kernel trace，无法证明成功descriptor write路径完备、confinement或全局零外写；未把shell路径审阅/历史trace代替实测。',
 'R0-B未进入；E与B候选均未评估，没有唯一兼容完整offline closure、package DB/transitive IDs/rebuild set，也不宣称二者均失败。',
 '8个exact FRP Git对象因前置停止未读取；没有源码调查、staging或exact-base工程实现。',
 'R0-C未进入；disk/RSS/wall/files四个非空预测上界、同closure可比依据及持续monitor/kill回执缺失。',
 '四PASS均未成立，条件八EP包未建设；六项NOT_ATTEMPTED、一项SHARED-03 UNSATISFIED、旧SCENARIO-04仅继承PARTIAL，当前新增SATISFIED=0。',
 'snapshot/accessor、DTO/schema、target、exact error/transaction synthetic records、patch/commit、fixture9/18/22、compile-only/serialization均未产生；不造空条件产物。',
 '实际证据尚未由主控出版，准确GitHub result_ref/manifest refs待真实commit回传；本Worker无GitHub写授权。',
 '正式longrun-worker-return/v2尚未生成；须证据先出版、同原W1同W005取得真refs后生成并仅回原E1，再由主控出版worker_results/W005/WORKER_RETURN.json。',
 '专业接受、action eligibility、G-RUN/H3、父Q和父任务完成仍归E1/manager，Worker未作决定。'
]
matrix='''# W005 EP 状态交接（Worker事实，不作专业接受）

W005停于R0-A0静态准备，未进入条件Phase1/2。以下沿用C0013已签专业矩阵的状态，W005没有新增满足EP。

| EP | C0013输入状态 | W005新增实施 | 保留缺口 |
|---|---|---|---|
| EP-WALL-SHARED-01 | NOT_ATTEMPTED | 未实施 | lifecycle snapshot/accessor/patch/typecheck |
| EP-WALL-SHARED-02 | NOT_ATTEMPTED | 未实施 | structured one-record-per-firing DTO/schema/serialization |
| EP-WALL-SHARED-03 | UNSATISFIED | 常量本地定义一致；静态准备失败 | static PASS、R0-A/B/C四PASS与完整隔离离线closure |
| EP-SCENARIO-01 | NOT_ATTEMPTED | 未实施 | dedicated staged target/compile-only |
| EP-SCENARIO-02 | NOT_ATTEMPTED | 未实施 | exact constructor/payload synthetic records |
| EP-SCENARIO-03 | NOT_ATTEMPTED | 未实施 | rejected post=pre、O/C空与transaction DTO |
| EP-SCENARIO-04 | PARTIAL | 未实施；仅继承旧静态ledger范围 | dedicated target引用、unresolved choice/actual result |
| EP-SCENARIO-05 | NOT_ATTEMPTED | 未实施 | 9/18/22 fixture/schema/hash/static validation |

SATISFIED=0，PARTIAL=1，UNSATISFIED=1，NOT_ATTEMPTED=6。scenario/normal/current材料=0。
本地常量、锁、只读sentinel事实不升级为EP满足，不形成业务SUPPORTS/COUNTERS。未运行历史W004脚本。
'''
text('artifacts/EP_ACCEPTANCE_MATRIX.md',matrix)
report='''# W005 本地执行报告

outcome=`STOP`；gate=`PREFLIGHT_STOP`；stop=`STOP_SECCOMP_STATIC_PREPARATION_ASSERTION`。
仅完成本地原件交付，不代表W/D003、G-RUN/H3或父任务完成。正式Return尚未生成，return_to只能原E1。

## 实际完成

完整任务6813 bytes/SHA256 `0cc6d0a55603978822feb80811cfc7eda9945f1620710b525326eb8029398db8`核完全一致；完整读取ORDER MD/JSON、签单Return、决定、专业review、当前EP/进度。31项输入映射中23个本地原件逐份bytes/hash核对并镜像；8个exact Git对象在后续Gate前停止，未读。
原W1 thread=`01a1da55-5881-7590-94a1-0661f0236977`；当前turn=`01a1dc6f-c611-7ba1-8301-f0bef1f0eef0`；实际`gpt-6.1-sol/max`，cwd=`/dwdhome/fy/BASE_E6_2`。当前owner PID2890/startticks20139现场一致；fresh预派发idle/canAccept、旧turn终态、Goal null/queue空有控制器原件，当前原生turn_context复核配置。
fresh holder PID246047/startticks47679582/inode14806399现场fdinfo证实FLOCK WRITE；同inode独立O_RDWR FD的NBflock竞争EAGAIN。只关闭自身竞争FD，未重取/替换/释放主控锁。旧PID243622已消失。W005 root先核不存在再独立创建。
真实HOME=/home/dw、CODEX_HOME=/home/dw/.codex始终未重设。主控650bytes sentinel回执逐字/hash核并保存；五个精确负目标只读lstat事前/事后均ENOENT，无预建/写/删。唯一业务写根为D003/W005，旧W4原件/脚本只读。

## 本机常量与精确新停止点

termios.FIOCLEX=21585 (`0x5451`) 与本机asm-generic/ioctls.h定义一致；x86_64、little-endian。模块/header路径、bytes/hash及本机seccomp_data布局检查源均保存在准备器和常量报告。
我编写的`tools/prepare_static.py`在任何runtime/launcher/BPF生成或evaluator之前，对旧W004 trace提取全部FIOCLEX行，错误断言`all('EPERM' in x['text'] for x in trace_lines)`。旧trace第312行是安装前FIOCLEX成功，第1509行才是安装后FIOCLEX EPERM。二者并存不否定本地常量；失败来自Worker准备脚本过强断言。
唯一准备器命令exit1/AssertionError，原生receipt、完整命令与完整traceback已保存。遵守新失败即停，未改/重跑准备器，未扩大allowlist，未启动R0-A1。该停止不是kernel不支持、不是新的ioctl兼容性实测，也不是BPF case已执行失败。

## 未执行范围

W005新runtime/launcher未产生，pure BPF evaluator=0，静态验收未PASS。R0-A1=0，NNP/Landlock/seccomp安装=0，当前FIOCLEX/F_GETFD证据无，九项probe=0，child/grandchild=0，W005 full kernel trace无。
R0-B/C未进入，不判两套closure均失败；四预算预测上界与continuous monitors未证。四PASS均未成立，条件八EP、source staging/patch/local commit、snapshot/DTO、fixture9/18/22、compile-only与synthetic serialization均未实施。没有scenario/normal/DBA/wrapper/native-reader/current生产材料，也未build/test/download/install/push。
23个本地输入及额外控制器原件收尾逐项复核bytes/hash/mtime/inode/dev一致；不以这项具名检查声称扫描全部BASE/HOME或证明kernel全局零外写。命令与自身新增文件路径可复核；无当前kernel trace，confinement/global zero writes明确未PASS。W004的历史安装成功及FIOCLEX EPERM事实冻结保留。

## 交付与路由

所有真实文件在本W005根内。`LOCAL_STAGE_HANDOFF.json`逐字映射ORDER每项deliverable到本地文件，并列真实missing。`PUBLICATION_MANIFEST.json`给绝对路径/sha256/bytes/逐字出版目标；`HASHES.sha256`和外层`FREEZE_RECEIPT.json`封存hash，明确排除自hash循环。
主控逐字运输到`longrun/runs/OI-EAW-WALL-20261114-01/delegations/D003/results/W005/`；Worker无GitHub写权限。目前真实出版commit/ref不存在，result_ref保持null；不生成future/self ref的正式Return。主控出版并回传真实refs后，同原W1同W005仅生成正式v2 Return与validation，再由主控出版`worker_results/W005/WORKER_RETURN.json`，只回`chatgpt:OI-EAW-WALL-20261114-01:executor:E1`。
E1/manager负责专业消费与后续决定。有限Goal完成只表示本地STOP证据已交付，自然结束、不常驻轮询。
'''
text('artifacts/WORKER_EXECUTION_REPORT.md',report)
text('artifacts/ENGINEERING_STOP_REPORT.md','''# W005 工程停止原件

`STOP_SECCOMP_STATIC_PREPARATION_ASSERTION` / `PREFLIGHT_STOP` / outcome=`STOP`。

唯一准备器执行exit1，未到BPF生成/evaluator；错误是把旧W004安装前FIOCLEX成功与安装后EPERM一并要求EPERM。完整原文在receipts/STATIC_PREPARATION_FAILURE.json，原准备器保留未修。

本机termios/header均为0x5451是独立成功事实；新静态delta/evaluator、当前kernel/probe均无PASS。未启动R0-A1，没有重试、policy调整或进入closure/budgets/八EP。保持旧W004 trace两阶段事实，不把准备器断言错误解释成Linux或FIOCLEX不支持。

依据ORDER静态验收前不得launcher、任一新失败即停的约束停止。未擅自修ORDER或改脚本再跑；只继续日志、不可变核验、报告、hash与运输交接。无需另一个测试Run，Worker不决定专业接受或后继签单。

完整missing、逐项产物映射和后续真实出版/正式Return步骤见LOCAL_STAGE_HANDOFF.json。无实际GitHub refs，不造正式Return。
''')

deliverables=json.loads((ROOT/'input/C0013-remote-work_orders--W005--ORDER.json').read_bytes())['deliverables']
files=[['WORKER_EXECUTION_REPORT.md'],['W005_BINDING.json'],['CONTROLLER_SENTINEL_PRECONFIRMATION.json'],['SECCOMP_IOCTL_FILTER_DELTA.json','FIOCLEX_LOCAL_CONSTANT_VERIFICATION.json'],['SECCOMP_FILTER_STATIC_EVALUATION.json'],['WRITE_CONFINEMENT_REPORT.json','FULL_WRITE_TRACE_REVIEW.json'],['OFFLINE_CLOSURE_REPORT.json'],['RESOURCE_BUDGET_REPORT.json'],['PHASE0_RECOVERY_VERDICT.json'],['COMMAND_LOG.jsonl','WRITE_SURFACE_AUDIT.json','EP_ACCEPTANCE_MATRIX.md','PUBLICATION_MANIFEST.json','HASHES.sha256'],[],['ENGINEERING_STOP_REPORT.md'],[]]
assert len(deliverables)==len(files)==13
mapping=[]
for i,(literal,names) in enumerate(zip(deliverables,files)):
    status='LOCAL_STOP_EVIDENCE'
    if i==10:status='NOT_ATTEMPTED_FOUR_PASS_NOT_MET'
    if i==12:status='PENDING_TRUE_PUBLISHED_REFS_THEN_SAME_W1_FORMAL_RETURN'
    mapping.append({'deliverable_literal':literal,'local_files':[str(ROOT/'artifacts'/n) for n in names],'status':status,'note':'只交真实已发生状态，不以停止报告冒充成功工程证明。' if i<10 else ('条件Gate未满足，不造空条件文件。' if i==10 else '正式Return由真实出版refs接续，不引用未来自身。' if i==12 else '原件与索引封存见外层FREEZE_RECEIPT。')})
save('artifacts/LOCAL_STAGE_HANDOFF.json',{'schema':'local-worker-stage-handoff/v1','run_id':'OI-EAW-WALL-20261114-01','work_order_id':'W005','worker':'codex:OI-EAW-WALL-20261114-01:worker:W1','return_to':'chatgpt:OI-EAW-WALL-20261114-01:executor:E1','outcome':'STOP','gate':'PREFLIGHT_STOP','stop_code':STOP,'missing':missing,'deliverable_mapping':mapping,'true_github_commit':None,'result_ref':None,'formal_WORKER_RETURN_created':False,'publication_target_root':'longrun/runs/OI-EAW-WALL-20261114-01/delegations/D003/results/W005/','formal_return_later_target':'longrun/runs/OI-EAW-WALL-20261114-01/worker_results/W005/WORKER_RETURN.json','next_steps':['主控逐字出版全部冻结原件并远端核验bytes/hash。','主控回传真实commit/ref/hash到同原W1同W005。','Worker仅在final-return新写正式v2 Return/validation，仅回原E1；主控出版。','E1/manager执行其余合同Gate和专业接受决定。'],'local_goal_completion_scope':'仅本W本地STOP调查与原件交付；不是W/D3/父任务完成。'})
save('audit/ARCHIVE_STAGE_RECEIPT.json',{'at':utc(),'scope':'停止后仅归档，不是preparer/evaluator/launcher重试','current_context':context,'completed_native_commands_exported':len(commands),'native_file_changes_exported':len(changes),'prepare_attempts':1,'prepare_exit_code':1,'evaluator_attempts':0,'R0_A1_attempts':0,'unchanged_original_inputs_checked':len(checks),'fresh_lock_at_archive':lock,'write_root':str(ROOT),'HOME':os.environ['HOME'],'CODEX_HOME':os.environ['CODEX_HOME'],'archive_source':fact(__file__),'seal_pending':True})
guard()
print(json.dumps({'outcome':'STOP','stop_code':STOP,'preparer_attempts':1,'evaluator_attempts':0,'R0_A1_attempts':0,'completed_command_records':len(commands),'input_immutability_checks':len(checks),'missing_count':len(missing),'report':fact(ROOT/'artifacts/WORKER_EXECUTION_REPORT.md')},ensure_ascii=False))
