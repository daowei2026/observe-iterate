# W003 工程停止原件

本地 outcome 为 **STOP**，Phase0 verdict 为 **PREFLIGHT_STOP**，主原因是 `RECOVERY_STOP_WRITE_CONFINEMENT`。

唯一真实尝试在 2026-11-14T20:47:17.517414+00:00 启动，2026-11-14T20:47:18.196755+00:00 结束，launcher PID241337，退出码73，未超时。`runtime.py` 的 `subprocess.Popen(stdin=subprocess.DEVNULL)` 传入以 `O_RDWR` 打开的 `/dev/null`。launcher 第 26 行在继承 fd 检查中要求 fd0 只读，触发 AssertionError。该接线问题属于本 W 实现；拒绝发生于 `PR_SET_NO_NEW_PRIVS`、Landlock ABI 查询/规则创建/restrict 和 seccomp 安装之前。不能把它描述成 Landlock 内核不支持，也不能把拒绝本身描述成 kernel confinement PASS。

`receipts/r0a-positive-launcher.json` 中 `calls=[]`。`trace/r0a-positive.241337` 的第1055行记录 `fcntl(0</dev/null>, F_GETFL) = O_RDWR|O_LARGEFILE`，第1058/1063行记录 W003 内 receipt 的创建和唯一成功 write（1214 bytes）。共1071行完整 trace，无子孙进程和 probe exec。未见成功外写或无法映射的 descriptor write，但范围仅为这个失败 launcher；整个后继零外写合同未被证明。

按 ORDER §5/8/12，不调整 stdin/参数、不修改 launcher 后重试，不改用另一方法继续，不进入 R0-B/C，不进入 staged source construction。正反 probe、closure、四项预测和连续监测均缺；场景、normal、DBA、wrapper、native-reader、compile、serialization、生产材料生成和源码 push 均未执行。实际 HOME/CODEX_HOME 未重设。未获得外部 sentinel 的主控预确认，该负向 probe 未执行；它是额外缺项，不能掩盖已发生的 fd0 主阻断。

成功子事实保留：精确任务与22项镜像 hash 校验、原 W1 实际配置/新锁核验、唯一失败 launcher 完整 trace 和限定范围的 write 路径映射。22项指定只读输入的 bytes/hash/mtime/inode/dev 复核不变；不把命名子集不变扩展成全局零外写证明。主控锁始终保留，Worker 未重取、替换或释放；W002 没有回写。

本地阶段不造空 patch、fixture、compile/serialization/local commit 报告，不生成声称真实未出版 refs 的正式 Return。后续由原 E1 根据真实 STOP 原件决定修唯一阻断或有界收束；Worker 不自行新建工单或作专业接受/父任务完成决定。先交主控逐字出版证据，再同一 W1/W003 以真实 refs 生成正式 V2 Return，仅回原 E1。
