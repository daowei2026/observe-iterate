# D003｜C0013 对 W004 正式 STOP 的专业消费

## 0. 身份、决定与边界

- `run_id`：`OI-EAW-WALL-20261114-01`
- `call_id`：`C0013`
- `delegation_id`：`D003`
- executor：`chatgpt:OI-EAW-WALL-20261114-01:executor:E1`
- reviewed Worker Return：`daowei2026/observe-iterate@348c61629eced6597f765b8af92c464bc1e56080:longrun/runs/OI-EAW-WALL-20261114-01/worker_results/W004/WORKER_RETURN.json`
- professional disposition：**`ACCEPT_STOP_EVIDENCE_WITH_STRICT_LIMITS`**
- D003 professional state：**`IN_PROGRESS`**
- `G-RUN`：**NOT PASSED**
- H3：**NOT AVAILABLE**
- 三个父 Q：**OPEN**
- 父任务完成：**NOT CLAIMED**

W004 的 STOP 被接受为真实、合规、可审计的工程停止。W004 已把 W003 的父子 stdin 接线问题修复，并证明 NNP、Landlock ABI6 ruleset 与候选 seccomp filter 可以实际安装；但 probe bootstrap 被候选 seccomp 对全部 `ioctl` 的过宽拒绝阻断。因此不能接受为 `WRITE_CONFINEMENT_PASS`、全局零外写、offline closure、预算/monitor、八 EP 或 current evidence 已通过。

## 1. 运输与原件资格

主控已完成：

- 71 份冻结原件逐字出版与 hash 核验；
- 正式 W004 Return、validation 和新增正式文件出版；
- 81 项 manifest 的 71 个唯一文件与交付别名映射；
- V2 schema、原 W1、原 W004、return-to 原 E1 与路由核验；
- W004 写者终态、队列空、旧 holder PID 消失、原锁 inode 保持且锁已释放。

E1 接受该运输资格。冻结原件中的 publication-pending 是冻结时点事实，已由正式 publication refs 解决；这不消除 Return 中保留的 16 项 substantive missing。

关键证据：

- `daowei2026/observe-iterate@23b4070f171af4442ddc83b663814f3349739c67:longrun/runs/OI-EAW-WALL-20261114-01/delegations/D003/results/W004/WORKER_EXECUTION_REPORT.md`
- 同 commit 的 `ENGINEERING_STOP_REPORT.md`
- 同 commit 的 `PHASE0_RECOVERY_VERDICT.json`
- 同 commit 的 `WRITE_CONFINEMENT_REPORT.json`
- 同 commit 的 `FULL_WRITE_TRACE_REVIEW.json`
- 同 commit 的 `PARENT_LAUNCHER_WIRING_DELTA.json`
- 同 commit 的 `W004_BINDING.json`
- 同 commit 的 `OFFLINE_CLOSURE_REPORT.json`
- 同 commit 的 `RESOURCE_BUDGET_REPORT.json`

## 2. W004 的实际执行链

### 2.1 Binding 与接线

接受以下具名范围事实：

- 沿用原 W1 物理聊天，并为 W004 fresh 核 actual turn、`gpt-6.1-sol/max`、cwd、owner、idle/no-writer；
- W004 fresh lock 的 holder PID/startticks/inode 与竞争 `EAGAIN`；
- W004 独立根为 `/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D003/W004`；
- actual `HOME=/home/dw`、`CODEX_HOME=/home/dw/.codex` 未重设；
- 父 runtime 以 `os.open('/dev/null', O_RDONLY|O_CLOEXEC)` 打开 stdin，`F_GETFL` 验证为 `O_RDONLY`，传给 child 后关闭父副本；
- launcher 实测 fd0=`/dev/null` 且只读；fd1/2 为 W004 根内单链接日志文件；
- 独立 writable lock FD 在 policy 前关闭，主控 holder lock 仍保持；
- 主控 outside sentinel 的只读 `ENOENT` 回执与其他四个具名负向目标的只读不存在检查完成。

这些事实关闭了 C0012 指定的两个接线前置：read-only stdin 与 controller sentinel preconfirmation。它们不得在后继中再次写成“未执行”。

### 2.2 Kernel setup 的独立成功子事实

唯一 R0-A1：

```text
start   2026-11-14T22:21:27.970491Z
end     2026-11-14T22:21:28.799738Z
elapsed 0.829199 s
exit    2
```

接受：

```text
Landlock ABI query = 6
PR_SET_NO_NEW_PRIVS = success
ruleset create = success
PATH_BENEATH add for W004 root = success
restrict_self = success
seccomp filter install = success
second Python execve = success
probe script O_RDONLY open/read = success before fatal ioctl
```

这些是 kernel/API 安装链成功的直接事实。它们不是负向 probe 通过，也不是 confinement 或全局零外写通过。

### 2.3 精确停止点

W004 seccomp candidate 将 syscall 16 `ioctl` 整体列入 deny set。第二 Python 启动后：

```text
trace line 1508: O_RDONLY open succeeds
trace line 1509: ioctl(fd, FIOCLEX) = -1 EPERM
```

`FIOCLEX` 只改变该文件描述符的 close-on-exec 标志；本次阻断来自 seccomp 规则粒度过粗，把 interpreter bootstrap 所需的 descriptor-control request 与潜在设备 ioctl 一并拒绝。

专业定性：

```text
SECCOMP_IOCTL_POLICY_COMPATIBILITY_STOP
```

不是：

```text
Landlock unsupported
Landlock rights failure
script open/read denied by Landlock
write-confinement PASS
```

probe 主体未进入，child/grandchild 未生成。W004 遵守单次尝试、未调整 policy、未重试。

### 2.4 Trace 的接受范围

接受：

- 1518 行完整 trace 覆盖 launcher、policy 安装、第二 Python bootstrap 和 exit；
- 两个实际成功 write 共 4628 bytes，均映射 W004 根内 launcher receipt/stderr；
- 该 trace 中 successful outside write=0、unknown write path=0；
- 无 `/proc/*/comm` open/write；
- 无 probe descendant、无 scenario/build/compile/serialization。

不接受：

- 该失败链不能证明完整 probe、R0-B/C、后继 command 或整个 W004 的全局零外写；
- policy 安装成功不能代替 inside/outside/shared/HOME/CODEX/child/symlink/network probes；
- 不能从本 trace 推导八 EP 或 business action 可运行。

## 3. 三类 Phase-0 blocker 的当前状态

### B1｜write confinement / zero outside writes

状态：**未解除，但已显著收窄。**

已关闭：

- W003 的 writable fd0 接线；
- 主控 outside sentinel 预确认；
- NNP/Landlock/seccomp 安装可达性。

仍缺：

- probe bootstrap 兼容性；
- inside/outside/shared/HOME/CODEX/child/grandchild/symlink/network 的真实结果；
- probe 全 trace；
- global zero outside writes。

`WRITE_CONFINEMENT_PASS=false`。

### B2｜single compatible offline closure

状态：**未解除 / 未进入。**

R0-B 未执行；不能说 exact lts-18.28 或 BASE lts-22.24 任一候选已成功，也不能说二者均已失败。8 个 exact Git source objects 未在 W004 读取。

### B3｜four budgets + continuous monitors

状态：**未解除 / 未进入。**

new disk、peak RSS、post-preflight wall、new files 的 predicted upper bound、可比实测与连续 monitor 仍缺。0.829 秒单命令和 45 秒 timeout 不能替代后继工程预算。

## 4. 八项 EP 的接受范围

W004 未进入 Phase1/2：

```text
staged source = 0
patch/local commit = 0
snapshot/accessor = 0
DTO/schema = 0
fixture materialization = 0
compile-only = 0
synthetic serialization = 0
scenario/normal/current material = 0
```

因此：

```text
SATISFIED      = 0
PARTIAL        = 1  (仅继承旧 EP-SCENARIO-04 静态 conflict ledger)
UNSATISFIED    = 1  (EP-WALL-SHARED-03)
NOT_ATTEMPTED  = 6
W004 new EP satisfied = 0
```

Kernel setup 成功是 Phase-0 子事实，不升级为 EP 满足。

## 5. 专业接受决定

```text
Accept W004 formal Return transport:                 YES
Accept STOP / PREFLIGHT_STOP:                         YES
Accept O_RDONLY parent-child stdin fix:               YES
Accept controller sentinel preconfirmation:           YES
Accept NNP/Landlock ABI6/ruleset/restrict setup:       YES, SCOPED
Accept seccomp installation and exact FIOCLEX stop:    YES, SCOPED
Accept failed-chain trace mapping:                     YES, FAILED-CHAIN SCOPE ONLY
Accept WRITE_CONFINEMENT_PASS:                         NO
Accept global zero outside writes:                     NO
Accept offline closure / budgets / monitors:           NO
Accept any newly constructed EP:                       NO
Accept current business evidence / G-RUN / H3:         NO
Reopen or rerun W004:                                  NO
```

W004 冻结封存，不修改其 scripts、policy、原件或 Return。

## 6. 合法后继判断

### 6.1 继续的依据

W004 新停止点：

- 直接由 trace 定位；
- 位于 probe bootstrap；
- 是一个明确的 seccomp syscall-argument 粒度问题；
- 不要求修改 Owner/D003 grant；
- 不要求放宽 zero-outside-write、resource cap 或 scenario 禁令；
- 可通过仅允许无文件内容写语义的 `FIOCLEX` request、继续拒绝其余 `ioctl` 来区分；
- 可以由新 W/root/lock 的单次尝试验证。

因此 D003 尚未达到“无合法下一动作”的有界停止条件。签发 W005 是有直接证据的最小后继，不是 W004 重跑。

### 6.2 W005 唯一 policy delta

W005 seccomp filter 对 syscall `ioctl` 必须改为按 request 分支：

```text
if syscall != ioctl:
    preserve W004 policy

if syscall == ioctl and request == locally-verified FIOCLEX:
    ALLOW

if syscall == ioctl and request != FIOCLEX:
    EPERM
```

本地验证值应来自当前 x86_64 Linux 的 stdlib/header，并与 W004 trace 的 symbolic `FIOCLEX` 一致；预期值可记录为 `0x5451`，但实际本地验证为权威。BPF 必须检查 request 高位与低位，不允许把任意 ioctl 放行。

理由：`FIOCLEX` 只设置 descriptor `FD_CLOEXEC`，不修改被指向文件内容、目录、metadata 或设备状态。其他 ioctl 保持拒绝；Landlock `IOCTL_DEV` 与原 filesystem rights 不放宽。

### 6.3 防止“连续调到跑通”

W005 在启动 launcher 前必须对 BPF 做静态/纯 evaluator 测试，至少覆盖：

- x86_64 arch；
- x32 syscall number；
- `ioctl(FIOCLEX)` → ALLOW；
- `ioctl(FIONCLEX)` → EPERM；
- arbitrary ioctl → EPERM；
- existing denied socket syscall → EPERM；
- ordinary allowed syscall → ALLOW；
- wrong arch → KILL。

随后只允许一次 R0-A1 实际尝试。若出现另一个未预先允许的 ioctl 或其他 bootstrap incompatibility，准确 STOP，不扩大 allowlist、不自动重试。

### 6.4 其余 Gate、cap 与禁令不变

W005 仍须先完成 R0-A probe/full trace，再进入 R0-B/C；四项 PASS 同时成立后才可 staged 八 EP。固定：

```text
new disk       <= 2 GiB
peak RSS       <= 4 GiB
post-preflight <= 25 min
new files      <= 50,000
outside writes = 0
scenario runs  = 0
```

禁止任何 single/partial/full scenario、normal、DBA、wrapper、native-reader、current/production material、shared source write/push 和 production lifecycle 语义修改。

## 7. 当前 D003 状态

```text
professional_state         = IN_PROGRESS
accepted_worker_refs       = W002 + W003 + W004 formal Returns
issued successor           = W005
EP satisfied               = 0
EP partial                 = 1
EP unsatisfied             = 1
EP not attempted           = 6
G-RUN                       = NOT PASSED
H3                          = NOT AVAILABLE
parent questions            = OPEN
parent task completion      = NOT CLAIMED
```
