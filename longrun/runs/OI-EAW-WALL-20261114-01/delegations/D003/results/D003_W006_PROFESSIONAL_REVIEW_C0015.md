# D003｜C0015 对 W006 正式 STOP 的专业消费

## 0. 身份、决定与边界

- `run_id`：`OI-EAW-WALL-20261114-01`
- `call_id`：`C0015`
- `delegation_id`：`D003`
- executor：`chatgpt:OI-EAW-WALL-20261114-01:executor:E1`
- reviewed Worker Return：`daowei2026/observe-iterate@34e7fed4d771e37d9890980e368304ae73ffb3c2:longrun/runs/OI-EAW-WALL-20261114-01/worker_results/W006/WORKER_RETURN.json`
- professional disposition：**`ACCEPT_STOP_EVIDENCE_WITH_STRICT_LIMITS`**
- D003 professional state：**`IN_PROGRESS`**
- `G-RUN`：**NOT PASSED**
- H3：**NOT AVAILABLE**
- 三个父 Q：**OPEN**
- 父任务完成：**NOT CLAIMED**

W006 的 `STOP / PREFLIGHT_STOP` 被接受为真实、合规、可审计的 R0-A 局部停止。W006 真实完成 P0～P3，且在唯一当前 kernel 尝试中完成 NNP、Landlock、seccomp 安装、第二 Python bootstrap 和当前 `FIOCLEX=0`；随后受限 probe 对另一个进程的 holder fdinfo 做只读 `openat` 时得到 `EACCES` 并停止。

这不构成 kernel 不支持、static evaluator 失败、FIOCLEX 失败、write confinement PASS、全局零外写、offline closure、预算/monitor、八 EP 或业务 evidence。

## 1. 运输与原件资格

主控已完成：

- 93 份冻结原件、1,805,193 bytes 的逐字出版和远端 hash/Git blob 核验；
- 正式 W006 Return、validation、命令日志、生成器和资格原件 5 文件的逐字出版；
- 107 项 manifest 中 93 个真实原件与 14 个交付标签别名映射；
- V2 schema、原 W1、原 W006 ORDER、return-to 原 E1 与 route Gate；
- 全部写者终态后释放 W006 锁，原 inode 保持、旧 holder PID gone、kernel FLOCK gone、同 inode 独立竞争成功。

E1 接受其运输资格。冻结原件中的 publication-pending 是冻结时点历史；正式 Return 和新增正式文件现已真实出版。该运输完成不消除 Return 中保留的 14 项 substantive missing。

关键来源：

- `daowei2026/observe-iterate@e9f4e0c569caa2939f3c5bfc2f882df6842f915f:longrun/runs/OI-EAW-WALL-20261114-01/delegations/D003/results/W006/WORKER_EXECUTION_REPORT.md`
- 同 commit 的 `ENGINEERING_STOP_REPORT.md`
- 同 commit 的 `HISTORICAL_FIOCLEX_PHASE_CLASSIFICATION.json`
- 同 commit 的 `FIOCLEX_LOCAL_CONSTANT_VERIFICATION.json`
- 同 commit 的 `SECCOMP_DATA_LAYOUT_VERIFICATION.json`
- 同 commit 的 `PARENT_RUNTIME_BINDING_DELTA.json`
- 同 commit 的 `SECCOMP_IOCTL_FILTER_DELTA.json`
- 同 commit 的 `SECCOMP_FILTER_STATIC_EVALUATION.json`
- 同 commit 的 `FIOCLEX_KERNEL_OBSERVATION.json`
- 同 commit 的 `WRITE_CONFINEMENT_REPORT.json`
- 同 commit 的 `FULL_WRITE_TRACE_REVIEW.json`
- 同 commit 的 `PHASE0_RECOVERY_VERDICT.json`
- 同 commit 的 `OFFLINE_CLOSURE_REPORT.json`
- 同 commit 的 `RESOURCE_BUDGET_REPORT.json`
- 同 commit 的 `EP_ACCEPTANCE_MATRIX.md`
- 同 commit 的 `tools/confinement_probe.py`
- 同 commit 的 `trace/r0a1.248966`

## 2. W006 的真实执行链

### 2.1 Binding 与写面

接受以下具名范围事实：

- 沿用原 W1 物理聊天，并为 W006 fresh 核 actual turn、`gpt-6.1-sol/max`、cwd、owner、idle/no-writer；
- W006 fresh lock 的 holder PID/startticks/inode、fdinfo FLOCK WRITE 与独立 `LOCK_EX|LOCK_NB → EAGAIN`；
- W006 独立根为 `/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D003/W006`；
- actual `HOME=/home/dw`、`CODEX_HOME=/home/dw/.codex` 未重设；
- controller outside sentinel 及 SHARED/HOME/CODEX_HOME/SYMLINK 具名目标在事前/事后只读检查中为 `ENOENT`；
- 26 个具名输入与 93 个冻结原件在 Worker 声明的 bytes/hash/mtime/inode/dev 覆盖内收尾一致；
- W006 没有 scenario、normal、DBA、wrapper、native-reader、production/current material、build、compile、serialization、download、install 或 source push。

不外推：

- 具名输入不变不等于全 BASE/HOME/CODEX_HOME 不变；
- sentinel 仍不存在不等于 kernel negative probe 已通过；
- W006 thread/lock/资格不延续给后继 W；
- failed-chain trace 内零 outside write 不等于全任务或后继全局零外写。

### 2.2 P0｜历史 FIOCLEX 分层

接受 `PASS`：

```text
W004 trace SHA256 = b2bcd39ff8886fa65815107bd95f333abef1bcb0a1ea69bb20010abc24b2c959
line 312  = HISTORICAL_PRE_POLICY_SUCCESS / FIOCLEX=0
line 1190 = historical seccomp install
line 1509 = HISTORICAL_POST_POLICY_DENIAL / FIOCLEX=EPERM
```

两阶段事实被分别保存，没有再次使用“所有 FIOCLEX 都应 EPERM”的错误断言。该结论只解释 W004 历史，不是 W006 current kernel 结果。

### 2.3 P1｜本机常量和 `seccomp_data` layout

接受 `PASS`：

```text
architecture       = x86_64
endianness         = little
termios FIOCLEX    = 21585 / 0x5451
header FIOCLEX     = 0x5451
FIONCLEX           = 21584 / 0x5450
seccomp_data size  = 64 bytes
nr/arch/ip/args    = 0/4/8/16
args[1] low/high32 = offsets 24/28
```

这是本机静态定义核验，不是 filter 安装或业务 evidence。

### 2.4 P2｜fresh W006 runtime/launcher/filter

接受 `PASS` 到生成和静态 binding 范围：

- runtime 从 fresh W006 binding 读取 root、holder PID/startticks/inode；
- source scan 未发现 W004/W005 旧 root/PID/startticks；
- parent 继续使用显式 `O_RDONLY|O_CLOEXEC /dev/null` stdin；
- launcher 保留 root 内 single-link stdout/stderr、inherited writable FD 关闭规则和 HOME/CODEX_HOME 约束；
- baseline 121 → candidate 126 instructions；
- 唯一策略差异是：正确 arch、非 x32、`ioctl` request high32=0 且 low32=`FIOCLEX` 时 ALLOW；其他 `ioctl` 保持 EPERM；
- non-ioctl、network、metadata、`PR_SET_NAME`、Landlock handled rights 与 only-W006-root write allowance 未放宽。

### 2.5 P3｜pure evaluator

接受 `PASS` 到纯静态范围：

```text
mandatory/extra cases = 11
semantic comparisons  = 24,240
jump targets checked  = 61
all paths explicit terminal = true
```

FIOCLEX allow、FIONCLEX/arbitrary/high32 deny、socket deny、read allow、x32 deny、wrong arch kill、`PR_SET_NAME` deny、other prctl allow均与预期一致。仅 4 个“正确 arch + ioctl16 + verified FIOCLEX”组合相对 baseline 发生预期 ALLOW 差异。

该 PASS 不替代 current kernel 或 probe 结果。

## 3. 唯一 R0-A1 的专业接受范围

### 3.1 实际执行

```text
start   = 2026-11-15T01:21:38.944026Z
end     = 2026-11-15T01:21:40.221839Z
elapsed = 1.277822054 s
exit    = 1
attempt = 1
retry   = 0
```

接受以下 current kernel 子事实：

- Landlock ABI query=6；
- `PR_SET_NO_NEW_PRIVS` 成功；
- ruleset create、only-W006-root PATH_BENEATH add、`restrict_self` 成功；
- 126-instruction seccomp filter 安装成功；
- parent stdin `O_RDONLY /dev/null`，launcher fd0只读；
- stdout/stderr为W006根内single-link regular files；
- 独立 writable lock FD 在 restrict/exec 前关闭；
- 第二 Python bootstrap 成功；
- current trace line1508 `FIOCLEX=0`；
- TCGETS/TIOCGWINSZ 等其他 ioctl 仍 EPERM；
- probe 主体进入并完成：inherited fd EBADF、HOME/CODEX_HOME值保持、stdin只读、stdout/stderr根内、NoNewPrivs=1、Seccomp=2。

### 3.2 精确停止点

`tools/confinement_probe.py` line41 在受限子进程内读取：

```text
/proc/248632/fdinfo/3
```

current trace line2240：

```text
openat(..., O_RDONLY|O_CLOEXEC) = -1 EACCES
```

随后 `PermissionError`，probe exit1。W006 没有调整 guard/policy/probe 或重试，也没有自行确定 procfs/LSM 的具体原因。

准确分类：

```text
STOP_PROBE_HOLDER_FDINFO_READ_EACCES
```

不是：

```text
kernel / Landlock 不支持
P0-P3失败
current seccomp安装失败
current FIOCLEX失败
write confinement PASS
```

### 3.3 锁完整性已有的独立证据

W006 同时存在三个彼此不同的事实：

1. **受限子域**：具名 inherited writable lock FD `fstat → EBADF`，证明 child 未继承该可写 FD；
2. **parent runtime / ordinary executor**：在 restricted child 外读取 holder PID/startticks/fdinfo，核同 inode FLOCK WRITE，并独立竞争得到 EAGAIN；
3. **执行后复核**：holder PID/startticks/inode/fdinfo和独立竞争仍成立，且只关闭 contender 自身 FD。

因此，受限 child 再读取另一个进程的 `/proc/<pid>/fdinfo/<fd>` 是一项重复且环境敏感的交叉证明位置。它失败不反证 holder 锁实际完整；但由于原 probe 把它设为硬前置，后续真正 confinement probes 未执行，R0-A 仍不得判 PASS。

这里的专业判断是：**后继应把“child 未继承 lock FD”和“controller holder 在执行前后保持 lock”拆成组合证明，而不是要求受限 child 获得另一个进程 procfs 的可读权限。** 这不是删除锁完整性要求，也不是放宽 confinement；它把证明放回各自有权、可审计的执行域。

### 3.4 尚未完成的 R0-A 事实

- 对同一 inside descriptor 做 clear `FD_CLOEXEC → FIOCLEX → F_GETFD` 的效果配对；
- inside create/write/truncate/rename/remove；
- OUTSIDE/SHARED/HOME/CODEX negative create；
- HOME/CODEX read-only directory open；
- symlink escape denial；
- child/grandchild restriction inheritance；
- socket/connect denial；
- 完整 probe full trace 与 global zero outside writes。

不能用 bootstrap 的另一 descriptor `FIOCLEX=0` 或无关 descriptor 的 `F_GETFD` 代替第一项。

## 4. Trace 接受范围

接受：

```text
trace file        = r0a1.248966
trace lines       = 2290
successful writes = 3 / 6594 bytes
write-open rows   = 2
unknown paths     = 0
successful outside file writes in failed chain = 0
```

三次写入均映射 W006 根内 launcher receipt、probe failure receipt和stdout。无 proc comm write、无 shared writable mmap。

限制：只覆盖该失败链；不能证明完整 W006、R0-B/C、后继命令或全局零外写。

## 5. 三类 Phase-0 blocker

### B1｜write confinement / global zero outside writes

状态：**未解除，但已收敛到 probe 证明编排。**

已实证：P0-P3、kernel policy安装、bootstrap、current FIOCLEX、受限 child inherited FD关闭、parent-side holder完整性。

仍缺：组合证明的正式产物、同descriptor FIOCLEX效果、完整九项probe、child/grandchild与full trace/global zero writes。

### B2｜single compatible offline closure

状态：**未解除 / 未进入。**

```text
R0-B attempts = 0
candidate E   = NOT_EVALUATED
candidate B   = NOT_EVALUATED
exact FRP Git objects read = 0
```

不能说二者都失败。

### B3｜four budgets + continuous monitors

状态：**未解除 / 未进入。**

四个 predicted upper bounds、同 compiler/closure 可比实测、deadline/RSS/disk/files/descendant kill receipt 与全流程写面监测均未证。1.277822 秒失败命令和 45 秒 timeout 不构成工程预算。

## 6. 八 EP 的专业接受范围

W006 未进入 Phase1/2：

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
W006 new EP satisfied = 0
```

P0-P3和kernel子事实属于 Phase-0 capability evidence，不升级任何 EP。

## 7. 专业接受决定

```text
Accept W006 formal Return transport:                   YES
Accept STOP / PREFLIGHT_STOP:                           YES
Accept P0 historical phase classification:              YES, SCOPED
Accept P1 constants/layout:                             YES, SCOPED
Accept P2 fresh filter generation:                      YES, SCOPED
Accept P3 pure evaluator PASS:                          YES, STATIC SCOPE
Accept current NNP/Landlock/seccomp/bootstrap/FIOCLEX:  YES, CURRENT ATTEMPT SCOPE
Accept inherited FD EBADF and parent holder checks:     YES, AS SEPARATE FACTS
Accept child cross-process fdinfo read as required:     NO, REDUNDANT PROOF PLACEMENT
Accept WRITE_CONFINEMENT_PASS/global zero writes:       NO
Accept offline closure / budgets / monitors:            NO
Accept any newly constructed EP:                        NO
Accept current business evidence / G-RUN / H3:          NO
Reopen or rerun W006:                                   NO
```

W006 冻结封存，不修改其 probe、policy、root、原件或 Return。

## 8. 合法后继判断

### 8.1 为什么仍有合法下一动作

本次停止点：

- 由 exact source/trace/traceback 定位；
- 出现在真正 filesystem/network probes 之前；
- 不反证 P0-P3 或 current policy 安装；
- 不要求改变 Owner/D003 grant；
- 不要求放宽 seccomp/Landlock、inherited-FD、zero-write、caps或场景禁令；
- holder 完整性已有 parent-side pre/post + 独立竞争证据路径；
- 可在新 W/root/lock 中用“restricted child EBADF + unrestricted parent pre/post holder checks”的组合证明，避开不必要的跨进程procfs读取；
- 可保留 W006 accepted P0-P3，以fresh程序等价核验而非重跑历史错误链。

因此 D003 尚未达到“无合法下一动作”的有界停止条件。签发 W007 是有直接证据的最小后继，不是 W006 重开或自动 retry。

### 8.2 W007 的唯一 proof-orchestration delta

```text
restricted child:
  prove blocked inherited lock FD == EBADF
  do not read /proc/<controller-holder>/fdinfo

parent runtime before child:
  verify holder PID/startticks
  verify exact lock inode and FLOCK WRITE
  independent same-inode NB competition fails
  persist PRE receipt

parent runtime after child, including child failure:
  repeat exact checks in finally
  persist POST receipt

composite result:
  child EBADF PASS
  AND parent PRE PASS
  AND parent POST PASS
  => holder-lock proof PASS
```

任何一项失败都使 R0-A 失败。该拆分不把 procfs EACCES解释成PASS，也不取消锁要求；只取消“受限 child 必须读取另一个进程 fdinfo”这一无必要耦合。

### 8.3 后继不变边界

W007 仍须完成当前 R0-A，随后才可进入 R0-B/C；四PASS同时成立后才可建设八EP。所有caps、scenario/normal/DBA/wrapper/native-reader/current material/shared write/push禁令保持。

## 9. 当前 D003 状态

```text
professional_state         = IN_PROGRESS
accepted_worker_refs       = W002 + W003 + W004 + W005 + W006 formal Returns
issued successor           = W007
EP satisfied               = 0
EP partial                 = 1
EP unsatisfied             = 1
EP not attempted           = 6
G-RUN                       = NOT PASSED
H3                          = NOT AVAILABLE
parent questions            = OPEN
parent task completion      = NOT CLAIMED
```
