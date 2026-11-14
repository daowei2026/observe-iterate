# W004 本地执行报告

**outcome=STOP，Phase0=PREFLIGHT_STOP**。R0-A0只读stdin接线和sentinel预确认已有真实成功证据；唯一R0-A1在已安装kernel policy之后，于Python脚本bootstrap的ioctl(FIOCLEX) EPERM处退出2。R0-B/C和条件八EP未进入。

## 工单、当前绑定与输入

原E1 C0012正式W004，ORDER JSON为`daowei2026/observe-iterate@347e4b2322ff2401aca21333cd3118f93d490baf:longrun/runs/OI-EAW-WALL-20261114-01/work_orders/W004/ORDER.json`，Return只回`chatgpt:OI-EAW-WALL-20261114-01:executor:E1`。完整定位任务7209 bytes、SHA256 da90f19b6ee5408b208e62efe4beec5f2fae22a677ffaa1a228c5675f68ff25f。30输入ref映射中22文件hash已核并逐字只读复制；8个exact Git对象因R0-A停止尚未进入后继读取。当前D003和Owner literal grant逐字子集已核：

```text
operation=wall-observation-work execution_context=linux:/dwdhome/fy/BASE_E6_2 allowed_writes=/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01
```

沿用原W1物理聊天01a1da55-5881-7590-94a1-0661f0236977。原生当前turn_context实测gpt-6.1-sol/max、cwd=/dwdhome/fy/BASE_E6_2；owner PID2890/startticks20139/UID501现场核实。主控本次predispatch idle/canAccept、Goal null、queue空和旧turn completed记录已归档；旧keeper PID240810已不存在。新lock由PID243622/startticks47124402、session90041持有，inode14806399；同inode/new-open-description非阻塞flock竞争EAGAIN。Worker只关闭自己竞争/探针FD，不重取、替换或释放holder锁。

W004根派发前不存在，核无占用后新建。唯一新增业务写根`/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D003/W004`；HOME=/home/dw、CODEX_HOME=/home/dw/.codex未重设且业务只读。显式任务tmp/cache/config/log/trace/audit/receipts/artifacts均在本根。Python使用-I -S -B及PYTHONDONTWRITEBYTECODE=1，不产生外部pycache。W002/W003、shared、cgpterm和其他路径只读，不访问/m3varK或production materials/wrapper。

## R0-A0及sentinel

新runtime由旧脚本只读对照，在新根实现显式os.open('/dev/null',O_RDONLY|O_CLOEXEC)、F_GETFL验证、Popen(stdin=stdin_fd)和finally关闭。PARENT_LAUNCHER_WIRING_DELTA.json保留逐行diff、自hash和静态只读FD检查；未删除launcher fd0只读断言或其他继承FD规则。变化限stdin/receipt/new-root/binding；Landlock rights和seccomp候选规则未放宽。

父实际stdin fd6 flags32768/O_RDONLY，Popen子strace PID244046；父关闭时间2026-11-14T22:21:28.006602+00:00。launcher实测fd0 /dev/null O_RDONLY、fd1/2为W004内常规单链接log文件。独立writable锁FD3被关闭，holder仍持锁且竞争失败。

主控sentinel精确路径为D003/.W004-deny-outside-C0012-e9ed948d；回执656 bytes、SHA256 d56b0541daeb37e39978b88ecafbc8fa3e562f882b46d8042b3ad669b3e5bc4a已核并逐字复制至CONTROLLER_SENTINEL_PRECONFIRMATION.json。其余SHARED/HOME/CODEX_HOME/SYMLINK_TARGET四个ORDER精确路径仅lstat核ENOENT；未创建/写入/清理。该预确认不是kernel拒绝证明。

## 唯一R0-A1实测与精确停止点

2026-11-14T22:21:27.970491+00:00 → 2026-11-14T22:21:28.799738+00:00，0.829199秒，exit2，45秒命令timeout未触发。ABI query返回6；NNP=0、ruleset create=fd3、add=0、restrict=0、seccomp=0，均errno0。唯一W004写allow rule、可用write/create/remove/refer/truncate/IOCTL_DEV rights和网络限制、metadata/syscall过滤的实际内容完整记录于launcher receipt。

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

主控逐字出版目标`longrun/runs/OI-EAW-WALL-20261114-01/delegations/D003/results/W004/`，本地artifacts文件映射目标根同名，其余相对路径保留。当前本地阶段没有新GitHub commit/ref、没有正式Return。待主控真实回读refs/hash后同一W1同W004生成V2 Return及独立校验，仅回原E1，由主控运输到worker_results/W004/WORKER_RETURN.json。

本地Goal结束只表示原件交付；不决定W专业接受、D003、action eligibility、G-RUN、H3、父Q或父任务完成。不常驻轮询、不向其他聊天发消息、不自行新开W。
