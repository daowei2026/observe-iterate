# W004 工程停止原件

outcome=STOP，verdict=PREFLIGHT_STOP，主原因RECOVERY_STOP_WRITE_CONFINEMENT，精确停止点PROBE_BOOTSTRAP_IOCTL_FIOCLEX_EPERM。

唯一R0-A1：2026-11-14T22:21:27.970491+00:00 → 2026-11-14T22:21:28.799738+00:00，0.829199秒，exit2，未超时。父Popen启动strace PID244046；tracee PID244050先执行launcher，再在同PID execve新Python。父stdin fd6及launcher fd0均为O_RDONLY /dev/null（F_GETFL=32768），父副本已finally关闭。独立open-file-description的writable锁FD3于trace第1180行关闭；主控PID243622/startticks47124402/inode14806399仍持FLOCK，父guard随后竞争EAGAIN。已按原件复制656字节sentinel只读ENOENT回执，其余四目标只读核ENOENT。

本W实测ABI6，NNP、Landlock create/add/restrict和seccomp安装均成功、errno0，安装发生在第二execve之前。第二execve在1198行成功；Python曾成功O_RDONLY open/read脚本。精确fatal为1508行O_RDONLY open成功后，1509行ioctl(fd3,FIOCLEX)=-1 EPERM；候选seccomp原规则整体拒绝ioctl syscall16。脚本主体和九项probe未执行，child/grandchild未产生。它是policy与解释器脚本启动的兼容性停止点，不能描述为fd0再次失败、Landlock ABI/rights不支持、openat/read失败或confinement PASS。

按C0012 ORDER，未调整policy、未加ioctl/dev/null写例外、未修改launcher到成功、未重试。R0-B/C及Phase1/2均未进入；不将未调查的两个resolver候选称已实测失败。没有当前业务证据、场景、normal、DBA、wrapper、native-reader、共享源码写/源码push；未联网、下载或安装。

完整1518行trace保留；唯一两个成功write为W004内launcher receipt4462字节和stderr166字节，共4628字节，未知write路径0，scope内成功外写0。未见/proc/*/comm open/write；不能扩成全W/全系统/后继零外写证明。policy setup成功也不能代替负向probe或八EP满足。

原W003及所有指定输入只读；本W只在/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D003/W004新增业务文件，HOME/CODEX_HOME保持真实值，未改变主控锁。完整逐项交付、missing及两阶段出版步骤见LOCAL_STAGE_HANDOFF.json。后续是否形成新修签或有界收束由原E1/manager决定；Worker不自行再开W或作专业接受/父任务完成决定。
