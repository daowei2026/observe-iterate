# W006 本地执行报告

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
