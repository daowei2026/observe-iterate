# W003 本地执行报告

本地 outcome：**STOP**。Phase0：**PREFLIGHT_STOP**。主停止原因：**RECOVERY_STOP_WRITE_CONFINEMENT**。本报告仅交当前 W003 本地事实和原件，不表示 E1 专业接受、D003/G-RUN 或父任务完成。

## 任务、身份和实际写面

按 C0011 正式修签 W003，原 Worker W1、原物理聊天 `01a1da55-5881-7590-94a1-0661f0236977` 执行。准确 ORDER JSON ref 为 `daowei2026/observe-iterate@3afc8e9eedb34ac3b25ba69e383c778c37622c30:longrun/runs/OI-EAW-WALL-20261114-01/work_orders/W003/ORDER.json`。定位任务原件完整读取并核得5210 bytes、SHA256 `f8aae85a8bf268c5f2dd7c48edf7383d810749d6c83094f7ca0d61db9fb3ce87`。指定镜像索引22个文件全部逐字/hash核验；8个 exact Git 源码输入因 R0-A 失败而未进入后续读取/closure 阶段。

当前原生 turn_context 记录 `gpt-6.1-sol/max`、cwd `/dwdhome/fy/BASE_E6_2`；现有执行器 PID2890/startticks20139、UID501/exe 现场只读复核。主控对同 owner 的原 thread/session、旧 turn completed/Goal null/queue 空、加载后 idle/canAccept 的原件保留。旧 keeper PID237355 当前不存在；W003 原根不存在后才由本 W 建立。新独占锁 path `.oi-runs/OI-EAW-WALL-20261114-01/.D003-writer.lock`，PID240810/startticks46501758/inode14806399，主控 session30931；现场 fdinfo 为 FLOCK WRITE，同 inode 新 open-file-description 的 `LOCK_EX|LOCK_NB` 竞争 EAGAIN，未重取、替换或释放主控锁。证据见 `W003_BINDING.json`、input 原件、COMMAND_LOG。

Owner literal grant：

```text
operation=wall-observation-work execution_context=linux:/dwdhome/fy/BASE_E6_2 allowed_writes=/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01
```

本 W 唯一新增业务写根：`/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D003/W003`。HOME=`/home/dw`、CODEX_HOME=`/home/dw/.codex` 保持实际原值，未重设；任务显式 tmp/cache/config/log/report 路径只在本根。Python 使用 `-I -S -B` 和 `PYTHONDONTWRITEBYTECODE=1`，未写外部 pycache；不重新设置 HOME/CODEX_HOME。只读边界包括 shared、W002、cgpterm、实际 HOME/CODEX_HOME；未访问 `/m3varK`/production materials 或生产 wrapper。

## R0-A 的真实结果

创建了 run-local Python/ctypes Landlock+seccomp 候选 launcher、分阶段 probe 和完整审计脚本；均为本 W audit artifact，不是 FRP patch。先把正向/继承FD/网络核验与需主控预确认 sentinel 的负向核验分开。负向 sentinel 主控预确认停止前未收到，因此未运行负向探针。

只实际尝试一次正向 launcher：`2026-11-14T20:47:17.517414+00:00` → `2026-11-14T20:47:18.196755+00:00`，用时 `0.679316` seconds，exit73，timeout=false。完整命令和 stdout/stderr 原件已存。失败发生在 inherited FD inspection：runtime 的 `subprocess.DEVNULL` 使 stdin fd0 为 `O_RDWR /dev/null`；launcher 第26行要求 fd0只读，拒绝并退出。这是本 W 接线问题。当前 Landlock ABI 未查询、NNP/规则/restrict/seccomp 未调用；历史 ABI6 只用于候选设计，未冒充本 W 实测。

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

全部最低 STOP 原件及11项 ORDER deliverable 的逐项映射在 `LOCAL_STAGE_HANDOFF.json`。不适用的条件工程文件不生成空替代品。主控逐字运输目标：`longrun/runs/OI-EAW-WALL-20261114-01/delegations/D003/results/W003/`；本地 artifacts 下文件发布到目标根同名，其余相对路径保留。当前无真实 W003 publication commit/ref，也无 GitHub 写授权。

待主控真实出版并回传逐字回读的 refs/hash/bytes 后，同一原 W1/同 W003 再生成正式 V2 `WORKER_RETURN.json`，`return_to=chatgpt:OI-EAW-WALL-20261114-01:executor:E1`，再由主控出版至 `worker_results/W003/WORKER_RETURN.json`。本地阶段结束自然退出，不常驻轮询、不向其他聊天发消息。不决定 W 专业接受或父任务完成。
