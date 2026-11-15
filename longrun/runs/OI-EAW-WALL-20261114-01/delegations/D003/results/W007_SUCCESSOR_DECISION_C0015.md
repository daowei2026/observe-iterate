# D003｜C0015 W007 有据后继决定

## 0. Decision

```text
W006 disposition = ACCEPT_STOP_EVIDENCE_WITH_STRICT_LIMITS
W006 reopen       = NO
new successor     = W007
D003              = IN_PROGRESS
```

W007 只处理 W006 直接证实的 probe proof-orchestration 问题：受限 child 已证明不再持有 inherited writable lock FD，而 controller holder 的持续有效性应由不受该 sandbox 限制的 parent/control 侧在执行前后核验；不再要求受限 child 读取另一个进程的 `/proc/<pid>/fdinfo/<fd>`。

这不取消 holder-lock 完整性，不扩大 Landlock/seccomp 权限，不放宽零外写、资源 cap、八 EP、场景禁令或 Gate。

## 1. 为什么 child 跨进程 fdinfo 读取不是必要安全前提

W006 原 probe 在进入实际 filesystem/network probes 前，顺序执行：

1. `fstat(blocked_inherited_fd) → EBADF`；
2. child读取 `/proc/<holder_pid>/fdinfo/<holder_fd>`；
3. 后续 inside/negative/child/network probes。

步骤1已经回答：

> restricted child 是否仍继承了具名可写 lock FD？

parent runtime 的 `guard()` 在 child 前后回答：

> controller holder 是否仍是同一 PID/startticks、同一 inode、同一 FLOCK WRITE owner，且同 inode independent NB competition仍失败？

步骤2要求 restricted child 具备读取另一个进程 procfs fdinfo 的能力。该权限不是 filesystem write confinement 的组成部分，也不是证明 child 未继承 FD 的必要条件；其 EACCES 可能来自 procfs/LSM/ptrace access policy，W006没有进一步归因，不能通过放宽 sandbox 来解决。

因此采用证据组合：

```text
ChildNonInheritance
AND ControllerLockPre
AND ControllerLockPost
→ HolderLockCompositeProof
```

而不是：

```text
restricted child must read controller process fdinfo
```

## 2. W007 唯一 probe delta

### 2.1 Restricted child

必须：

- 对具名 `blocked_inherited_fd` 执行 `fstat` 并得到 `EBADF`；
- 不打开、不读取、不 stat `/proc/<controller-holder>/fdinfo/*`；
- 不以任何其他procfs路径替代该跨进程检查；
- 继续执行 same-descriptor `clear FD_CLOEXEC → ioctl(FIOCLEX) → F_GETFD`；
- 继续执行inside、negative、child/grandchild、symlink、network与full trace。

### 2.2 Parent runtime PRE

在 spawn restricted child 前，parent必须：

- 核 holder PID存在且startticks匹配；
- 读取 exact holder fdinfo；
- 核 lock path inode与binding一致；
- 核 fdinfo含该holder `FLOCK WRITE`；
- 独立打开同inode并做`LOCK_EX|LOCK_NB`，得到EAGAIN/EACCES；
- 只关闭contender自身FD；
- 保存不可覆盖 `HOLDER_LOCK_PRE.json`。

### 2.3 Parent runtime POST

无论 child PASS、STOP、timeout或nonzero，必须在 `finally` 中重复相同检查，保存：

```text
HOLDER_LOCK_POST.json
```

POST失败必须使整体R0-A失败；不得因child已PASS而忽略。

### 2.4 Composite proof

生成：

```text
HOLDER_LOCK_COMPOSITE_PROOF.json
```

只有以下全部成立才PASS：

```text
PRE exact holder check = PASS
restricted child inherited FD EBADF = PASS
POST exact holder check = PASS
same PID/startticks/inode/fd across PRE/POST
independent competition denied PRE/POST
holder untouched by parent/child
```

该产物必须引用PRE、POST、child report、binding与trace hash。不得把控制面口头状态写成证据。

## 3. W006 accepted P0-P3 的使用方式

W007 不重跑 W004/W005/W006 的旧失败链。它必须：

1. 按 exact ref/hash读取 W006 accepted artifacts；
2. 核本机constant/layout source hash未变化；
3. 在fresh W007 root生成fresh runtime/launcher/probe；
4. candidate seccomp program与W006 accepted 126-instruction语义等价，唯独record/root/binding元数据变化；
5. 对fresh candidate运行pure evaluator；
6. evaluator仍须覆盖W006 mandatory cases、jump bounds、explicit termination和non-ioctl equivalence；
7. 只有fresh evaluator PASS才允许一次kernel attempt。

这属于carry-forward + fresh-equivalence，不是把W006静态PASS冒充W007 kernel PASS。

## 4. Fresh physical binding

W007：

- 沿用原W1物理聊天，不新建聊天；
- 重新核actual owner/thread/session/model/effort/cwd/idle/no-writer；
- 获取fresh D003 writer lock并证明竞争失败；
- 使用独立root：`.../D003/W007`；
- W002～W006 roots与原件只读冻结；
- W006 lock/session/turn/资格/command不延续；
- actual HOME/CODEX_HOME保持不变，本任务新增写入为0；
- 所有任务tmp/cache/config/log/source/build/artifact只在W007 root。

## 5. Controller preconfirmation

派发前只读确认以下精确outside sentinel不存在：

```text
/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D003/.W007-deny-outside-C0015-57a2c396
```

只允许有界`lstat`/等价检查；不得create/write/delete。receipt进入W007 binding。其他SHARED/HOME/CODEX/symlink目标由W007在policy前只读核不存在。

## 6. Single current R0-A1

fresh static equivalence/evaluator PASS后，只允许一次actual launcher/probe：

1. O_RDONLY stdin与root-only stdio；
2. inherited FD guard与composite holder proof；
3. NNP、Landlock、seccomp安装；
4. second Python bootstrap；
5. current FIOCLEX及same-descriptor F_GETFD effect；
6. inside create/write/truncate/rename/remove；
7. OUTSIDE/SHARED/HOME/CODEX negative create与read-only directory；
8. child/grandchild inheritance；
9. symlink escape；
10. socket/connect denial；
11. path-complete full trace。

出现新的kernel/bootstrap/probe问题：STOP，保留trace，不修改后重试。

## 7. Recovery Gate

只有R0-A PASS才进入R0-B；只有R0-A/B PASS才进入R0-C。四项同时PASS才进入staged construction：

```text
WRITE_CONFINEMENT_PASS
OFFLINE_CLOSURE_PASS
FOUR_BUDGETS_KNOWN_WITHIN_CAP
CONTINUOUS_MONITORS_PASS
```

否则：

```text
PREFLIGHT_STOP
```

不自动重试。

## 8. Unchanged caps

```text
new disk       <= 2 GiB
peak RSS       <= 4 GiB
post-preflight <= 25 min
new files      <= 50,000
outside writes = 0
scenario runs  = 0
```

## 9. Unchanged prohibitions

- 不运行single/partial/full scenario；
- 不运行normal；
- 不运行DBA/wrapper/native reader；
- 不生成current/production O/C/A/D业务材料；
- 不访问或修改production material；
- 不写shared checkout；
- 不修改production lifecycle语义或旧test assertion；
- 不联网、下载、安装依赖；
- 不push源码；
- 不把static/kernel/compile结果解释成业务`SUPPORTS/COUNTERS`。

## 10. Conditional eight EP continuation

仅四PASS后，按原D003合同建设：

```text
EP-WALL-SHARED-01..03
EP-SCENARIO-01..05
```

完整9/18/22 fixture只物化和静态parse/count/order/hash；不得送入production decoder/lifecycle。允许的compile-only和direct synthetic serialization须在cap与零外写内。

## 11. Stop routing

| 新事实 | 处理 |
|---|---|
| fresh program/evaluator不等价 | STOP before kernel |
| PRE或POST holder proof失败 | STOP，保留exact receipt；不让child结果覆盖 |
| restricted child仍含跨进程holder fdinfo读取 | STOP before kernel |
| kernel/bootstrap/probe失败 | STOP，保留trace，不改后重试 |
| R0-A PASS但closure不闭合 | STOP，不拼resolver |
| R0-A/B PASS但预算/monitor unknown或超cap | STOP，不进入EP |
| 四PASS后EP局部失败 | 保留独立满足EP，禁止scenario |
| 八EP全部满足 | 回E1消费；仅可建议action `ELIGIBLE_WITH_LIMITS`，G-RUN仍由manager决定 |

## 12. Parent boundary

签发W007不改变：

```text
three parent questions = OPEN
H3                     = NOT AVAILABLE
G-RUN                   = NOT PASSED
parent task             = INCOMPLETE
```

W007正式Return先回原E1；只有E1消费后才能更新D003或向manager作最终/部分回交。
