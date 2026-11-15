# D003｜C0014 对 W005 正式 STOP 的专业消费

## 0. 身份、决定与边界

- `run_id`：`OI-EAW-WALL-20261114-01`
- `call_id`：`C0014`
- `delegation_id`：`D003`
- executor：`chatgpt:OI-EAW-WALL-20261114-01:executor:E1`
- reviewed Worker Return：`daowei2026/observe-iterate@597d813d7c7cc4a8e619326544915131e7bc46c7:longrun/runs/OI-EAW-WALL-20261114-01/worker_results/W005/WORKER_RETURN.json`
- professional disposition：**`ACCEPT_STOP_EVIDENCE_WITH_STRICT_LIMITS`**
- D003 professional state：**`IN_PROGRESS`**
- `G-RUN`：**NOT PASSED**
- H3：**NOT AVAILABLE**
- 三个父 Q：**OPEN**
- 父任务完成：**NOT CLAIMED**

W005 的 `STOP / PREFLIGHT_STOP` 被接受为真实、合规、可审计的准备阶段停止。它只证明本机 `FIOCLEX` 定义一致、W005 binding/sentinel与准备器失败事实；不证明 seccomp filter 已生成或静态通过，不证明 R0-A1、confinement、offline closure、预算/monitor、八 EP 或 current evidence 已通过。

## 1. 运输与原件资格

主控已完成：

- 67 份冻结原件逐字出版与 hash 核验；
- 正式 W005 Return、validation 与正式运输文件出版；
- 78 项 manifest 的真实原件与交付别名映射；
- V2 schema、原 W1、原 W005、return-to 原 E1 与路由核验；
- W005 全部写者终态、队列空、旧 holder PID 消失、原 inode 保持且锁已释放。

E1 接受运输资格。冻结原件中的 publication-pending 是冻结时点事实，正式 Return 已真实出版；该运输待办的解决不消除 Return 中保留的 13 项 substantive missing。

关键来源：

- `daowei2026/observe-iterate@10e9433477db333ed5d7bf7ac4a1feee508dce44:longrun/runs/OI-EAW-WALL-20261114-01/delegations/D003/results/W005/WORKER_EXECUTION_REPORT.md`
- 同 commit 的 `ENGINEERING_STOP_REPORT.md`
- 同 commit 的 `FIOCLEX_LOCAL_CONSTANT_VERIFICATION.json`
- 同 commit 的 `SECCOMP_IOCTL_FILTER_DELTA.json`
- 同 commit 的 `SECCOMP_FILTER_STATIC_EVALUATION.json`
- 同 commit 的 `receipts/STATIC_PREPARATION_FAILURE.json`
- 同 commit 的 `tools/prepare_static.py`
- 同 commit 的 `PHASE0_RECOVERY_VERDICT.json`
- 同 commit 的 `WRITE_CONFINEMENT_REPORT.json`
- 同 commit 的 `OFFLINE_CLOSURE_REPORT.json`
- 同 commit 的 `RESOURCE_BUDGET_REPORT.json`
- 同 commit 的 `EP_ACCEPTANCE_MATRIX.md`

## 2. W005 的实际执行链

### 2.1 Binding 与只读前置

接受以下具名范围事实：

- 沿用原 W1 物理聊天，并对 W005 fresh 核 actual turn、`gpt-6.1-sol/max`、cwd、owner、idle/no-writer；
- W005 fresh lock 的 holder PID/startticks/inode 与竞争 `EAGAIN`；
- W005 独立根为 `/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D003/W005`；
- actual `HOME=/home/dw`、`CODEX_HOME=/home/dw/.codex` 未重设；
- controller outside sentinel 与 SHARED/HOME/CODEX_HOME/SYMLINK 五个具名负向目标在准备前后只读核为 `ENOENT`；
- 23 个本地输入与额外控制器原件在具名 bytes/hash/mtime/inode/dev 覆盖内收尾一致；
- W005 没有 build/test/download/install/push，没有运行 scenario/normal/DBA/wrapper/native-reader。

不外推：

- 具名输入不变不等于全 BASE/HOME/CODEX_HOME 不变；
- sentinel 仍不存在不等于 kernel policy 已拒绝写入；
- W005 的 thread/lock/资格不延续给后继 W；
- 没有 W005 kernel trace，不能声称全局零外写或 confinement PASS。

### 2.2 本机常量核验的独立成功事实

接受：

```text
architecture        = x86_64
endianness          = little
termios.FIOCLEX     = 21585 / 0x5451
asm-generic header  = #define FIOCLEX 0x5451
FIONCLEX            = 21584 / 0x5450
local definitions   = agree
```

W004 冻结 trace 中存在两个不同阶段的 `FIOCLEX`：

```text
line 312  : policy安装前，FIOCLEX = 0
line 1509 : policy安装后，FIOCLEX = -1 EPERM
```

二者并存符合 W004 执行顺序；不能要求所有 FIOCLEX 都是 EPERM，也不能把 line312 的成功解释为 W005 当前 policy 已放行。

### 2.3 精确停止点

W005 的唯一准备器命令：

```text
prepare_static.py
attempts = 1
exit     = 1
failure  = AssertionError at line 32
```

错误代码：

```python
trace_lines = [all W004 FIOCLEX lines]
assert trace_lines and all('EPERM' in line for line in trace_lines)
```

它把：

- W004 policy 安装前成功的 `FIOCLEX=0`；
- W004 policy 安装后的 `FIOCLEX=EPERM`

错误地要求为同一种结果。准确分类：

```text
STOP_SECCOMP_STATIC_PREPARATION_ASSERTION
```

这是 **Worker 准备器对历史 trace 的阶段分类错误**，不是：

```text
本机FIOCLEX常量失败
BPF static evaluator失败
新的seccomp filter安装失败
新的kernel/ioctl兼容性失败
Landlock/kernel不支持
write confinement PASS
```

W005 按“任一新失败即停”停止，没有修改脚本重跑，也没有扩大 allowlist。

### 2.4 严格未执行范围

W005 在失败前尚未物化：

```text
new runtime
new launcher
candidate BPF
instruction comparison
pure static evaluator
```

并且：

```text
R0-A1 attempts                = 0
NNP/Landlock/seccomp installs = 0
current FIOCLEX/F_GETFD proof = none
nine probes                   = 0
child/grandchild              = 0
W005 full kernel trace        = none
R0-B/R0-C                     = not entered
Phase1/2                      = not entered
```

`SECCOMP_IOCTL_FILTER_DELTA.json` 与 `SECCOMP_FILTER_STATIC_EVALUATION.json` 是准确的 `NOT_PRODUCED/NOT_RUN` 记录，不是失败的 filter/evaluator 结果。

## 3. 三类 Phase-0 blocker 的当前状态

### B1｜write confinement / zero outside writes

状态：**未解除；W005没有推进到当前policy。**

已保留的历史事实：

- W004 read-only stdin、sentinel、NNP、Landlock ABI6、ruleset/restrict、seccomp安装成功；
- W004 安装后 `FIOCLEX` 被 blanket-ioctl policy 拒绝。

W005 新增：

- 本机 `FIOCLEX=0x5451` 两个本地来源一致；
- intended request-level filter的准备器在历史trace检查处过早停止。

仍缺：

- candidate BPF 的生成与纯静态评价；
- 当前 request-level filter 的 kernel 安装；
- `FIOCLEX` 成功与 `F_GETFD_CLOEXEC`；
- 九项 probe、child/grandchild、full trace；
- global zero outside writes。

`WRITE_CONFINEMENT_PASS=false`。

### B2｜single compatible offline closure

状态：**未解除 / 未进入。**

R0-B attempts=0；不能说 exact lts-18.28 或 BASE lts-22.24 任一候选已成功，也不能说两者均失败。8 个 exact FRP Git 对象未在 W005 读取。

### B3｜four budgets + continuous monitors

状态：**未解除 / 未进入。**

new disk、peak RSS、post-preflight wall、new files 的非空预测上界、同 closure 可比实测和 continuous monitor/kill receipts 均缺。准备器 0.036 秒失败不能替代后继工程预算。

## 4. 八项 EP 的接受范围

W005 未进入 Phase1/2：

```text
staged source = 0
patch/local commit = 0
snapshot/accessor = 0
DTO/schema = 0
dedicated target = 0
fixture 9/18/22 = 0
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
W005 new EP satisfied = 0
```

本机常量核验、binding、sentinel和准备器错误定位是 Phase-0 工程事实，不升级任何 EP。

## 5. 专业接受决定

```text
Accept W005 formal Return transport:                    YES
Accept STOP / PREFLIGHT_STOP:                            YES
Accept binding/sentinel/named immutability facts:        YES, SCOPED
Accept FIOCLEX local constant agreement:                 YES, STATIC LOCAL SCOPE
Accept exact historical two-phase trace classification:  YES
Accept preparer assertion failure attribution:           YES
Accept intended BPF delta as produced/tested:             NO
Accept pure static evaluator PASS/FAIL:                   NO, NOT RUN
Accept current kernel/request-level result:               NO, NOT RUN
Accept WRITE_CONFINEMENT_PASS/global zero writes:         NO
Accept offline closure / budgets / monitors:              NO
Accept any newly constructed EP:                          NO
Accept current business evidence / G-RUN / H3:            NO
Reopen or rerun W005:                                     NO
```

W005 冻结封存，不修改其准备器、原件、root或Return。

## 6. 合法后继判断

### 6.1 为什么继续仍然有据

本次停止点：

- 是确定的纯准备逻辑错误；
- 发生在runtime/launcher/BPF物化及evaluator之前；
- 不涉及kernel行为的新反例；
- 不需要改变Owner/D003 grant；
- 不需要放宽inherited-FD、Landlock rights、seccomp deny、zero outside writes、cap或scenario禁令；
- 可以通过把历史trace分类从“所有都EPERM”改成“policy前成功、policy后EPERM”直接验收；
- 可以把历史trace分类与candidate BPF/evaluator拆成不同证据层，避免再次相互替代。

因此 D003 尚未达到“无合法下一动作”的有界停止条件。签发 W006 是有直接证据的最小后继，不是 W005 重开或自动重试。

### 6.2 W006 最小修复原则

W006 必须：

1. 精确绑定 W004 trace SHA；
2. 分别记录 line312 的 pre-policy success 与 line1509 的 post-policy EPERM；
3. **不得再使用 `all(FIOCLEX lines contain EPERM)` 或等价断言**；
4. 历史trace只用于上下文与源完整性，不作为candidate filter static PASS的替代；
5. 使用 fresh W006 binding 值生成runtime，不从W005硬编码PID/startticks；
6. 独立生成 candidate launcher/BPF；
7. 在任何kernel尝试前运行pure evaluator与非-ioctl等价检查；
8. static PASS后只允许一次R0-A1；若新失败则STOP，不自动修第二次。

### 6.3 不变 Gate、cap 与禁令

W006 仍须 R0-A→R0-B→R0-C；四PASS同时成立后才可 staged 八EP。固定：

```text
new disk       <= 2 GiB
peak RSS       <= 4 GiB
post-preflight <= 25 min
new files      <= 50,000
outside writes = 0
scenario runs  = 0
```

禁止任何 single/partial/full scenario、normal、DBA、wrapper、native-reader、current/production material、shared source write/push 与 production lifecycle语义修改。

## 7. 当前 D003 状态

```text
professional_state         = IN_PROGRESS
accepted_worker_refs       = W002 + W003 + W004 + W005 formal Returns
issued successor           = W006
EP satisfied               = 0
EP partial                 = 1
EP unsatisfied             = 1
EP not attempted           = 6
G-RUN                       = NOT PASSED
H3                          = NOT AVAILABLE
parent questions            = OPEN
parent task completion      = NOT CLAIMED
```
