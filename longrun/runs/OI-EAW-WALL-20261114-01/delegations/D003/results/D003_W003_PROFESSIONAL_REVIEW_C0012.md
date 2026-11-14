# D003｜C0012 对 W003 正式 STOP 的专业消费

## 0. 身份、决定与边界

- `run_id`：`OI-EAW-WALL-20261114-01`
- `call_id`：`C0012`
- `delegation_id`：`D003`
- executor：`chatgpt:OI-EAW-WALL-20261114-01:executor:E1`
- reviewed Worker Return：`daowei2026/observe-iterate@e124f5662e4c683ee6abe572b78c6a8de15d4d3e:longrun/runs/OI-EAW-WALL-20261114-01/worker_results/W003/WORKER_RETURN.json`
- professional disposition：**`ACCEPT_STOP_EVIDENCE_WITH_STRICT_LIMITS`**
- D003 professional state：**`IN_PROGRESS`**
- `G-RUN`：**NOT PASSED**
- H3：**NOT AVAILABLE**
- 三个父 Q：**OPEN**
- 父任务完成：**NOT CLAIMED**

W003 的 STOP 被接受为真实、合规、可审计的工程停止；不接受为 kernel confinement、offline closure、预算、monitor、八 EP、current evidence 或 action eligibility 已通过。

## 1. 正式运输与原件资格

主控已逐字出版、远端回读并机械核验：

- 72 份冻结证据原件；
- 正式 W003 Return 与新增校验/回执；
- 81 项 Return manifest（72 个唯一文件源 + 9 个逐字交付别名）；
- V2 schema、原 W1、原 ORDER、return-to 原 E1 和路由。

E1 接受其运输资格。冻结报告中的 publication-pending 是当时历史，现已由真实 publication refs 解决；该运输缺口的解决不改变下面 16 项 substantive missing。

关键来源：

- `WORKER_EXECUTION_REPORT.md`：`daowei2026/observe-iterate@9aaaf4a3b322333b46f33b9e55c916b4cea1b1e3:longrun/runs/OI-EAW-WALL-20261114-01/delegations/D003/results/W003/WORKER_EXECUTION_REPORT.md`
- `ENGINEERING_STOP_REPORT.md`：同 commit 同目录
- `PHASE0_RECOVERY_VERDICT.json`：同 commit 同目录
- `WRITE_CONFINEMENT_REPORT.json`：同 commit 同目录
- `FULL_WRITE_TRACE_REVIEW.json`：同 commit 同目录
- `W003_BINDING.json`：同 commit 同目录
- `OFFLINE_CLOSURE_REPORT.json`：同 commit 同目录
- `RESOURCE_BUDGET_REPORT.json`：同 commit 同目录

## 2. W003 真实执行链

### 2.1 Binding 合格范围

接受：

- 沿用原 W1 物理聊天；
- 本 W actual turn、`gpt-6.1-sol/max`、cwd `/dwdhome/fy/BASE_E6_2`；
- W003 fresh lock 的 holder PID/startticks/inode 与竞争 EAGAIN；
- 旧 W002 writer/lock 已结束；
- actual `HOME=/home/dw`、`CODEX_HOME=/home/dw/.codex` 未重设；
- W003 actual root 为 `/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D003/W003`；
- 22 项指定只读输入的 hash/bytes/mtime/inode/dev 在 W003 命名覆盖内保持不变。

不外推：

- 命名路径不变不等于全系统零写；
- W003 的 thread/lock/资格不延续给任何后继 W；
- 原生平台会话写入不是本任务业务产物，但也不能据此证明全局 filesystem 零写。

### 2.2 唯一 R0-A 尝试

唯一 launcher 尝试：

```text
start   2026-11-14T20:47:17.517414Z
end     2026-11-14T20:47:18.196755Z
elapsed 0.679316 s
exit    73
```

父 `runtime.py` 使用：

```python
subprocess.Popen(..., stdin=subprocess.DEVNULL, ...)
```

Python 因而把 fd0 连接到 `O_RDWR /dev/null`。launcher 在 pre-enforcement inherited-FD inspection 执行：

```python
if fd == 0:
    assert not writable
```

并 fail-closed。直接 trace：

```text
fcntl(0</dev/null>, F_GETFL) = O_RDWR|O_LARGEFILE
```

此时：

```text
PR_SET_NO_NEW_PRIVS            未调用
Landlock ABI query             未调用
ruleset create/add/restrict    未调用
seccomp install                未调用
probe exec                     未发生
child/grandchild               无
```

专业定性：**W003 runtime-to-launcher integration wiring failure**。它不是 Landlock 内核不支持，也不是 kernel policy failure，更不是 confinement PASS。

### 2.3 Trace 可接受范围

完整 `strace -ff -yy -ttt -s128 -e trace=all` 覆盖该失败 launcher 的 execve→exit73，共 1071 行。

接受：

- 唯一成功 descriptor write 为 W003 root 内 launcher failure receipt，1214 bytes；
- 该 trace 内成功 outside write=0；
- 该 trace 内 unknown write destination=0；
- 无 probe、无 descendant、无 network syscall、无 `/proc/*/comm` open/write；
- startup SysV `IPC_CREAT|IPC_EXCL` 返回 EEXIST，随后只读 attach；没有实际新 IPC object 或 writable shared mapping。

不接受：

- 该单进程失败 trace不能证明后继命令、父控制面或整个 W 的全局零外写；
- 没有安装 policy，不能证明 outside/shared/HOME/CODEX/child/symlink/network 被拒绝；
- fd0 未观察到 write不等于 writable inherited fd 已被安全处理。

### 2.4 Sentinel 缺口

W003 要求主控先只读确认外部 sentinel 不存在。停止前未收到确认，所以负向 sentinel probe 未执行。该项是独立缺口；主停止仍是先发生的 fd0 接线失败。

## 3. 四项 Phase-0 requirement

| requirement | W003 事实 | E1 判断 |
|---|---|---|
| `WRITE_CONFINEMENT_PASS` | pre-policy fd0 assertion fail | **FAIL / NOT PASSED** |
| `OFFLINE_CLOSURE_PASS` | R0-B 未进入 | **NOT ATTEMPTED** |
| `FOUR_BUDGETS_KNOWN_WITHIN_CAP` | R0-C 未进入；四项为 null/unknown | **NOT ATTEMPTED** |
| `CONTINUOUS_MONITORS_PASS` | deadline/RSS/disk/files/kill receipt 未验证 | **NOT ATTEMPTED** |

原 W002 三类高层阻断仍在：

```text
confinement / global zero outside writes 未证
single compatible offline closure 未证
four budgets + continuous monitors 未证
```

W003 的新增价值是把第一项的本次实际停止点进一步定位到一个确定的 fd0 接线错误；没有解除任何高层阻断。

## 4. EP 专业接受范围

W003 未进入 R0-B/C 或 Phase1/2：

```text
staged source = 0
patch = 0
schema/DTO = 0
fixture materialization = 0
compile-only = 0
serialization = 0
local commit = 0
scenario/normal/current material = 0
```

所以 W003 新满足 EP 数量为 0。C0010 的旧 `EP-SCENARIO-04` 静态 conflict ledger 仍可作为 `PARTIAL` 输入，但不是 W003 新结果或 current runtime evidence。

## 5. 专业接受决定

```text
Accept W003 formal Return transport:             YES
Accept STOP / PREFLIGHT_STOP:                     YES
Accept binding and failed-launch facts:           YES, SCOPED
Accept fail-closed inherited-FD guard behavior:   YES, SCOPED
Accept failed-launch trace mapping:                YES, FAILED-LAUNCH SCOPE ONLY
Accept WRITE_CONFINEMENT_PASS:                     NO
Accept kernel unsupported conclusion:              NO
Accept outside writes proven zero globally:        NO
Accept offline closure / budgets / monitors:       NO
Accept any newly built EP:                         NO
Accept current business evidence / G-RUN / H3:     NO
Reopen or rerun W003:                              NO
```

W003 冻结封存；不修改其 runtime、launcher、原件或 Return，不在其目录重试。

## 6. 合法后继判断

### 6.1 为什么不是有界结束

fd0 failure 具有以下性质：

- 原因直接、确定、可复现；
- 发生在任何 kernel policy 调用前；
- 不要求改变 Owner/D003 grant；
- 不要求降低 inherited-FD 安全断言；
- 不要求放宽 cap、零外写或禁令；
- 可以通过父 runtime 为 stdin 显式提供 **read-only** `/dev/null` 解决；
- 可以在新 W/root/lock 下保留完整审计并让实际 Landlock/probe 决定后续。

因此，局部 STOP 还不足以证明 D003 不可执行。合法后继是一个新的 W004，而不是重跑 W003。

### 6.2 W004 唯一已知接线修复

父 runtime 必须：

```python
fd = os.open('/dev/null', os.O_RDONLY | os.O_CLOEXEC)
# verify F_GETFL access mode == O_RDONLY
subprocess.Popen(..., stdin=fd, ...)
# parent closes its copy after spawn
```

launcher 保持严格规则：fd0 必须只读；不得把 `O_RDWR /dev/null` 加入例外，也不得删除 inherited-FD 检查。

W004 还必须在派发前取得主控对一个具名 outside sentinel 的**只读不存在确认**；其他 shared/HOME/CODEX sentinel 在本 W 内先只读确认不存在。只有这样负向 probe 才不会把已有文件误当作新建测试目标。

### 6.3 不变条件

W004 仍须：

- 沿用原 W1 物理聊天但 fresh 核 actual owner/thread/model/effort/cwd/no-writer/new lock；
- 使用独立 `/D003/W004` root；
- 真实 HOME/CODEX_HOME 不变，任务新增写入只在 W004 root；
- R0-A→R0-B→R0-C→Phase1/2 严格 Gate；
- 四 PASS 同时成立才进入 staged construction；
- 保留 2 GiB/4 GiB/25 min/50,000 files/outside writes 0/scenario runs 0；
- 禁止 single/partial/full scenario、normal、DBA、wrapper、native-reader、production material、shared source write/push。

### 6.4 再次停止原则

W004 不得自动 retry。若 read-only stdin 修复后仍在 policy 前因其他 wiring defect停止，或 Landlock/probe/closure/budget任一不满足，保存新证据并 STOP；不得连续修改到“跑通”。后续是否再修由 E1/manager依据新证据决定。

## 7. 当前 D003 状态

```text
professional_state         = IN_PROGRESS
accepted_worker_refs       = W002 + W003 formal Returns
issued successor           = W004
EP satisfied               = 0
EP partial                 = 1 (old static conflict ledger only)
EP unsatisfied             = 1 (SHARED-03)
EP not attempted           = 6
G-RUN                       = NOT PASSED
H3                          = NOT AVAILABLE
parent questions            = OPEN
parent task completion      = NOT CLAIMED
```
