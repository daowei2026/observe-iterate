# D004｜W007 证据保留与旧锁释放合同

## 0. 当前状态

```text
W007 execution       = PHYSICAL STOP
formal Worker Return = ABSENT
resume/redispatch    = FORBIDDEN
local evidence root  = PRESERVE READ-ONLY
old reservation lock= PENDING SAFE RELEASE WITH RECEIPT
```

本文件是 D004 的资源与证据收束合同，不是 W007 Return，也不改写 W007 的历史时点。

## 1. 本地证据根

精确根：

```text
/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D003/W007
```

已知冻结规模：

```text
85 files
2,075,599 bytes
all 85 named SHA256 independently checked by controller
```

不得删除、清理、覆盖、重命名或在该根继续运行命令。

## 2. 最小长期保留集合

至少保留并可由 manifest/hash 回溯：

### Binding / transport / freeze

- `W007_BINDING.json`
- `CONTROLLER_SENTINEL_PRECONFIRMATION.json`
- `PUBLICATION_MANIFEST.json`
- `HASHES.sha256`
- `FREEZE_RECEIPT.json`
- `LOCAL_STAGE_HANDOFF.json`
- local stage report 的真实 GitHub ref

### Carry-forward / fresh program / evaluator

- `W006_ACCEPTED_SUBFACT_CARRY_FORWARD.json`
- `FRESH_PROGRAM_EQUIVALENCE.json`
- `SECCOMP_FILTER_STATIC_EVALUATION.json`
- `PROBE_PROOF_DECOMPOSITION.json`

### Lock / FIOCLEX / R0-A

- `HOLDER_LOCK_PRE.json`
- `HOLDER_LOCK_POST.json`
- `HOLDER_LOCK_COMPOSITE_PROOF.json`
- `FIOCLEX_KERNEL_OBSERVATION.json`
- `WRITE_CONFINEMENT_REPORT.json`
- R0-A command receipt and full trace/review

### R0-B STOP

- R0-B command receipt
- exact Git command and stderr
- trace line containing `openat("/dev/null", O_RDWR) = -1 EACCES`
- `OFFLINE_CLOSURE_REPORT.json`
- `PHASE0_RECOVERY_VERDICT.json`
- `RESOURCE_BUDGET_REPORT.json`

### Audit

- `COMMAND_LOG.jsonl`
- `WRITE_SURFACE_AUDIT.json`
- `EP_ACCEPTANCE_MATRIX.md`
- full file inventory with bytes/hash/path

不要求把 85 项全部复制进 GitHub；GitHub 保留具名 status report、精确本地根、总量、hash 验证结论和新 closeout receipts 即可。

## 3. 证据资格

| 类别 | 资格 |
|---|---|
| controller audit | 主控物理状态与独立 hash 核验 |
| W007 local stage report | Worker 本地执行事实来源；非 formal Return |
| local frozen files | 可在 D004 新动作中只读复核；不得冒充已专业接受结果 |
| C0015 reports | W002～W006 限域专业接受；不覆盖后来 W007 事实 |
| W007 formal Return | 不存在；不得补造 |

## 4. 旧锁对象

历史审计值：

```text
lock path   = /dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/.D003-writer.lock
holder PID  = 251010
startticks  = 48763578
inode       = 14806399
session     = 7861
```

这些值只绑定最后审计时点。实际释放前必须重新读取当前 PID/startticks/inode/flock/queue/writer 状态。

## 5. 释放前置

控制侧必须先确认并保存 `W007_LOCK_RELEASE_PRE.json`：

1. W007 physical turn 已 completed；
2. 原 W1 当前 Goal 为空、queue 为空；
3. 没有 W007 运行命令或写者；
4. 85 项冻结证据及关键 hash 仍可读；
5. holder PID/startticks、lock inode与当前 FLOCK owner一致；
6. 同 inode 独立 nonblocking competition 仍被拒绝；
7. 本次动作不会删除 W007 evidence root；
8. 没有新 W 使用旧 D003 lock 身份。

任一未知时不得强行 kill、unlink 或覆盖。

## 6. 安全释放动作

释放必须由真实持有该锁的控制侧完成：

- 优先在原 lockkeeper/session 中正常关闭 holder FD／终止 lockkeeper；
- 不让 Worker 声称自己持有或释放；
- 不杀无关进程；
- 不删除 W007 evidence root；
- 锁文件本身可保留为历史 inode/path，核心要求是 kernel FLOCK 已释放；
- 若必须结束旧 PTY/session，先确认其只承担该 reservation keeper。

该动作属于 D004 resource closeout，不是 W007 resume。

## 7. 释放后核验

保存 `W007_LOCK_RELEASE_POST.json`，至少包含：

```text
checked_at
old path/inode
old holder PID/startticks existence
kernel FLOCK state
same-inode independent competition result
W007 evidence root existence
85-file inventory/hash spot/full verification result
queue/goal state
release method
side effects
```

成功标准：

```text
old holder no longer owns FLOCK
independent contender can acquire and release the same lock safely
W007 evidence root remains intact
no Worker resumed
no old command rerun
```

若锁已在本次前自然释放，记录 `ALREADY_RELEASED_AT_CURRENT_CHECK`，仍需 post receipt；不得伪造本次主动释放。

## 8. 新 D004 writer

旧锁释放完成后，主控才为新 W008 建立 fresh D004 writer lock：

```text
/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/.D004-writer.lock
```

需记录 fresh holder PID/startticks/inode/session及独立竞争失败。它不继承 W007 的 holder、turn、thread eligibility 或 command authority。

## 9. 分流

- **释放成功**：W008 可继续 closeout只读复核和直接 BASE 取材。
- **已自然释放**：记录事实后继续。
- **安全释放受阻**：不破坏性处理；报告精确阻断。若不竞争同一 writer 资源，其他只读调查可继续，但任何新写动作需主控重新判单写者。
- **证据根损坏/身份不一致**：停止 closeout写动作，保存现状并回原 E1；不得补造历史文件。
