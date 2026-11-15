# W007本地执行事实与STOP交付

outcome=STOP，gate=PREFLIGHT_STOP，stop_code=STOP_R0_B_GIT_DEV_NULL_O_RDWR_EACCES。
仅回原E1：chatgpt:OI-EAW-WALL-20261114-01:executor:E1。本报告记录当前实测事实；本地交付不代表专业接受、W007或父任务完成。

## 资格、原单与边界

原ORDER：daowei2026/observe-iterate@e788e36c8e4c18e4888f1d8a225950f51c9a695c:longrun/runs/OI-EAW-WALL-20261114-01/work_orders/W007/ORDER.json。
MD：daowei2026/observe-iterate@aafb1ef72b30ad8a9ebab7e89b6b2d15b0d4b58a:longrun/runs/OI-EAW-WALL-20261114-01/work_orders/W007/ORDER.md；C0015签认原件见input/C0015-head-PRO_RETURN.json。
本物理thread=01a1da55-5881-7590-94a1-0661f0236977，turn=01a1dd15-f35a-7892-bca9-6de6721263b5，actual gpt-6.1-sol/max，cwd=/dwdhome/fy/BASE_E6_2。
Owner进程2890/startticks20139/uid501与新锁251010/startticks48763578/inode14806399/fd3/session7861均现场核验。
仅新增业务写根/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D003/W007；HOME=/home/dw、CODEX_HOME=/home/dw/.codex未重设。
主控sentinel ENOENT回执逐字入binding；未由普通Worker重复其预检查。其余4具名负向目标在policy前只读核不存在。
32个当前本地输入核bytes/hash并收尾核精确mtime/inode/dev一致；8个Git对象映射不冒充本W已读取源码。
W006冻结不动，未重跑旧失败链；本W使用fresh root、binding、锁和程序。

## carry-forward与fresh静态结果

W006 accepted P0-P3子事实按exact ref/hash核验。本机termios、ioctl/seccomp/syscall headers及architecture/endianness/layout hash未变。
fresh launcher只变record元数据；seccomp 126条指令与accepted candidate数组相等，Landlock、network、metadata、PR_SET_NAME规则未放宽。
fresh pure evaluator：11 cases、24,240 semantic comparisons、61 jumps，所有路径显式terminal；相对121条baseline仅4个verified FIOCLEX组合出现预期差异。
restricted probe保留具名inherited FD EBADF和全部后续probe；移除跨进程holder fdinfo依赖。parent PRE与finally POST保留完整guard。

## 唯一R0-A1当前实测

开始2026-11-15T02:52:32.961743+00:00，结束2026-11-15T02:52:36.003440+00:00，耗时3.041698381秒，exit0，timeout=false，attempt1/retry0。
NNP、Landlock ABI6/create/add/restrict、126条seccomp安装、只读stdin、根内single-link stdio、继承独立可写lock FD关闭均成功。
main/child/grandchild完整probe PASS，3代进程均实测同一descriptor initial FD_CLOEXEC=1→清0→FIOCLEX=0→F_GETFD=1。
inside create/write/truncate/rename/remove、OUTSIDE/SHARED/HOME/CODEX create拒绝及仍不存在、HOME/CODEX只读目录、symlink escape拒绝、socket/connect拒绝和继承restriction均PASS。
HOLDER_LOCK_PRE/POST均同PID/startticks/fd/inode及FLOCK WRITE，独立NB竞争均errno11；组合证明PASS，无parent/child改变holder。
完整3进程/4次exec的4511行trace审阅完成；10次成功write共15419bytes均根内，成功write-open7、negative write-open7，unknown paths0/outside file writes0。
current post-policy FIOCLEX6次成功，其他ioctl继续EPERM；该结果不改写W006自身STOP或不替代closure/预算。

## R0-B新失败与硬停止

R0-A PASS后进入一次受相同policy限制的离线closure核验，绝非R0-A1重试。
开始2026-11-15T03:04:16.166848+00:00，结束2026-11-15T03:04:17.790886+00:00，耗时1.624022382秒；首个Git命令exit128，受限child/driver exit1，无timeout。
真实命令为/usr/bin/git --no-optional-locks -c core.fsmonitor=false -c gc.auto=0 -C /dwdhome/fy/BASE_E6_2/edh-universe/frp/frp cat-file blob cac6c912dd65a14acbd591ca57e0afd8ddb4ef13:frp.cabal。
Git自身启动路径openat("/dev/null", O_RDWR)=-1 EACCES；stderr为“fatal: could not open '/dev/null' for reading and writing: Permission denied”。Worker提供的stdin仍是显式O_RDONLY。
r0b1.251844 line157直接保存失败open；没有放宽policy、替换guard、改probe或重试。
2进程/3次exec的2561行失败链trace完整审阅；5成功write共9453bytes均根内，outside file writes0、unknown paths0。
parent R0-B PRE/POST均PASS，holder保持；IPC CREATE|EXCL均EEXIST且attach为SHM_RDONLY，无新增segment/可写attach。
input/exact-frp/frp.cabal确为失败命令创建的0字节stdout，保留原证，不是已读取/核hash的11958字节Git对象。
Git成功对象读取=0，E/B两个closure候选尚未实际评估；不得称两者均失败/不兼容，不能给OFFLINE_CLOSURE_PASS。

## 后继未执行与交付

R0-C未进入；四项预测上界、同compiler/closure可比测量、continuous monitor/kill receipt均未知，短命令耗时与timeout不构成工程预算PASS。
四PASS未同时成立，条件八EP、staged源码、patch、local commit、fixture/compile-only/direct synthetic serialization均未进入；所有scenario/normal/DBA/wrapper/native-reader/current材料=0。
EP专业基线保持SATISFIED0/PARTIAL1/UNSATISFIED1/NOT_ATTEMPTED6，新满足0。
全部产物见PUBLICATION_MANIFEST.json、HASHES.sha256及FREEZE_RECEIPT.json的实际路径/bytes/hash/metadata；逐字ORDER deliverable映射与10项missing见LOCAL_STAGE_HANDOFF.json。
现无W007真实出版commit/ref，正式Return未生成。主控逐字运输目标为longrun/runs/OI-EAW-WALL-20261114-01/delegations/D003/results/W007/；真实refs回传后由原W1同W007生成正式Return，运输至worker_results/W007/WORKER_RETURN.json，只回原E1。
审计覆盖具名材料和全部已追踪命令，不作全BASE/HOME/CODEX扫描或未来/global业务零写证明；专业接受、action eligibility、G-RUN/H3、父Q和父任务完成仍由原E1/manager决定。
