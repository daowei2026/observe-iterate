# D003 Executor Progress｜C0013 消费 W004 STOP 并签发 W005

## 0. 身份与当前状态

- `run_id`：`OI-EAW-WALL-20261114-01`
- `call_id`：`C0013`
- `delegation_id`：`D003`
- executor：`chatgpt:OI-EAW-WALL-20261114-01:executor:E1`
- return_to：`chatgpt:OI-EAW-WALL-20261114-01:manager`
- 本轮新增接受：W004 formal STOP Return
- 既有接受：W002、W003 formal STOP Returns（均限域）
- 本轮新签：W005
- `professional_state`：**IN_PROGRESS**
- D003：**NOT COMPLETE**
- `G-RUN`：**NOT PASSED**
- H3：**NOT AVAILABLE**
- 三个父 Q：**OPEN**
- 父任务完成：**NOT CLAIMED**

本报告完成 C0013 当前可真实完成的专业工作：消费 W004、限定证据资格、更新 Phase-0/EP 状态、把新停止点收敛为精确的 seccomp `ioctl(FIOCLEX)` compatibility 问题，并签发独立 W005。它不把 W005 ORDER 发布写成物理派发、执行或回交。

## 1. 正式输入与运输

- C0013 Invocation：`daowei2026/observe-iterate@581de363c1a461457259e3fc602203a87deb1702:longrun/runs/OI-EAW-WALL-20261114-01/calls/C0013/INVOCATION.json`
- C0013 FULL_ASSIGNMENT：`daowei2026/observe-iterate@1793a1e7781210a8eb54a0da4440afe10e8f88d1:longrun/runs/OI-EAW-WALL-20261114-01/calls/C0013/FULL_ASSIGNMENT.md`
- W004 formal Return：`daowei2026/observe-iterate@348c61629eced6597f765b8af92c464bc1e56080:longrun/runs/OI-EAW-WALL-20261114-01/worker_results/W004/WORKER_RETURN.json`
- W004 evidence commit：`23b4070f171af4442ddc83b663814f3349739c67`
- 当前 D003：`daowei2026/observe-iterate@b7200816f86395cd1475ea3a482fc2e63086b967:longrun/runs/OI-EAW-WALL-20261114-01/delegations/D003/DELEGATION.json`

主控已核71份冻结原件、5份正式文件、81项manifest、原W1身份、Return route和锁终态；E1独立完成专业接受。

## 2. W004 专业结论

### 2.1 Decision

```text
ACCEPT_STOP_EVIDENCE_WITH_STRICT_LIMITS
```

W004 的 `STOP/PREFLIGHT_STOP` 合法有效；不返修、不重开、不在W004目录重试。

完整审查：

`daowei2026/observe-iterate@6b6ad47b3b72d88f849ca76c32ab4cfcc9c8fc5c:longrun/runs/OI-EAW-WALL-20261114-01/delegations/D003/results/D003_W004_PROFESSIONAL_REVIEW_C0013.md`

### 2.2 W004 已关闭的前置

W004 已真实完成并可接受：

- 原W1/fresh W004 binding与lock；
- parent显式`O_RDONLY /dev/null` stdin与child fd0只读；
- controller outside sentinel只读不存在回执；
- actual HOME/CODEX_HOME未重设；
- ABI6 query；
- `PR_SET_NO_NEW_PRIVS`；
- Landlock ruleset create、W004-only PATH_BENEATH add、restrict_self；
- seccomp filter安装；
- 第二Python exec成功；
- probe脚本O_RDONLY open/read成功；
- 失败链1518行full trace的路径映射。

这些事项不应在后继中再写成“未执行”。

### 2.3 精确停止点

W004 seccomp把syscall 16 `ioctl`整体拒绝。第二Python bootstrap在脚本O_RDONLY open/read之后调用：

```text
ioctl(fd, FIOCLEX) = -1 EPERM
```

probe主体尚未运行，exit2。准确分类：

```text
SECCOMP_IOCTL_POLICY_COMPATIBILITY_STOP
```

不是Landlock/kernel不支持，也不是confinement PASS。

`FIOCLEX`只设置descriptor close-on-exec，不改文件内容、目录、metadata或设备状态；因此存在不放宽零外写合同的最小request级修复。

### 2.4 Trace边界

该失败链中两个successful write共4628 bytes，均映射W004 root；successful outside write=0、unknown path=0。只能接受该失败链范围，不能外推全W/后继/global zero writes。

## 3. 三类 Phase-0 blocker

| blocker | C0013状态 | 已取得 | 仍缺 |
|---|---|---|---|
| write confinement / zero outside writes | **未解除、已收窄** | stdin/sentinel/kernel setup成功，精确FIOCLEX stop | bootstrap兼容、九项probe、full probe trace、global zero writes |
| single compatible offline closure | **未解除/未进入** | 无新增 | 只选一套resolver/compiler/packageDB/transitive deps/rebuild set |
| four budgets + monitors | **未解除/未进入** | 无新增 | 非空disk/RSS/wall/files上界、可比依据、continuous monitors/kill receipts |

Phase-0四项：

```text
WRITE_CONFINEMENT_PASS             = false
OFFLINE_CLOSURE_PASS               = false / not attempted
FOUR_BUDGETS_KNOWN_WITHIN_CAP      = false / not attempted
CONTINUOUS_MONITORS_PASS           = false / not attempted
```

## 4. 八 EP 当前状态

```text
SATISFIED      = 0
PARTIAL        = 1  (旧 EP-SCENARIO-04 static ledger subset)
UNSATISFIED    = 1  (EP-WALL-SHARED-03)
NOT_ATTEMPTED  = 6
W004 new EP satisfied = 0
```

W004未进入R0-B/C或Phase1/2，没有staged source、patch、snapshot、DTO/schema、fixture、compile、serialization、local commit或current material。

完整矩阵：

`daowei2026/observe-iterate@c220411b1ef95ce093cfaaa4df09c3dffdb2c5a7:longrun/runs/OI-EAW-WALL-20261114-01/delegations/D003/results/EP_ACCEPTANCE_MATRIX_C0013.md`

## 5. 为什么签发 W005

W004停止点同时满足：

- 有直接trace；
- 位于probe bootstrap；
- 不要求改变Owner/D003 grant；
- 不要求删除inherited-FD检查；
- 不要求放宽Landlock write rights、cap或业务禁令；
- 可以用request级seccomp分支直接验收；
- 可严格保持“除verified FIOCLEX外其他ioctl全部拒绝”。

因此D003尚未达到无合法下一动作的有界停止条件。W005是新root/new lock/single attempt的最小后继，不是W004隐形重跑。

后继决定：

`daowei2026/observe-iterate@8a056068b09d32b06dbba8a6700249ee303f2ac2:longrun/runs/OI-EAW-WALL-20261114-01/delegations/D003/results/W005_SUCCESSOR_DECISION_C0013.md`

## 6. W005 正式原件

### ORDER MD

`daowei2026/observe-iterate@41ad8bddce5d9d3a44f1378b52b320725bfebc89:longrun/runs/OI-EAW-WALL-20261114-01/work_orders/W005/ORDER.md`

### ORDER JSON

`daowei2026/observe-iterate@bf5a28e7afe8ef87280d3c37fd40b81c5f5ea804:longrun/runs/OI-EAW-WALL-20261114-01/work_orders/W005/ORDER.json`

运输身份：

```text
issuer_call_id = C0013
issuer          = original E1
worker          = original bound W1
return_to       = original E1
delegation_ref  = current C8 D003
```

## 7. W005 的唯一 policy delta

W005在本机核实`FIOCLEX` constant与W004 trace后，seccomp只按request精确允许：

```text
ioctl(FIOCLEX)        -> ALLOW
all other ioctl       -> EPERM
```

必须检查`seccomp_data.args[1]`高/低32位；不能把整个ioctl syscall放行。预期constant可记录为`0x5451`，但本地stdlib/header核对值为权威。

launcher实际执行前，pure evaluator必须验证：FIOCLEX allow、FIONCLEX deny、arbitrary ioctl deny、upper32 nonzero deny、socket deny、ordinary syscall allow、x32 deny、wrong arch kill。若静态结果不符，不启动launcher。

通过静态验收后只允许一次实际R0-A1。遇到另一bootstrap ioctl或compatibility缺口，STOP，不扩大allowlist、不自动重试。

## 8. W005 fresh binding 与 sentinel

独立root：

```text
/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D003/W005
```

沿用原W1物理聊天，但fresh核owner/thread/model/effort/cwd/idle/no-writer并取得新锁；W004资格/root/lock不继承。HOME/CODEX_HOME保持真实值，本任务新增写入只在W005 root。

主控派发前只读确认：

```text
/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D003/.W005-deny-outside-C0013-b6e58ef8
```

事前不存在；不创建、不写、不删。receipt进入W005 binding。

## 9. Gate、cap与禁令不变

四PASS同时成立才进入staged construction：

```text
WRITE_CONFINEMENT_PASS
OFFLINE_CLOSURE_PASS
FOUR_BUDGETS_KNOWN_WITHIN_CAP
CONTINUOUS_MONITORS_PASS
```

cap：

```text
new disk       <= 2 GiB
peak RSS       <= 4 GiB
post-preflight <= 25 min
new files      <= 50,000
outside writes = 0
scenario runs  = 0
```

禁止任何single/partial/full scenario、normal、DBA、wrapper、native reader、current/production material、shared source write/push及production lifecycle语义修改。

## 10. 当前尚未发生

截至C0013 Return：

- W005仅发布ORDER MD/JSON；
- 主控未在本调用回报W005 sentinel preconfirmation、物理派发或receipt；
- 没有创建W005 root/lock/chat；
- 没有执行constant/BPF static evaluation、launcher、probe、closure、budget或monitor；
- 没有staging/patch/compile/serialization；
- 没有scenario/normal/current evidence；
- W005 Worker Return不存在；
- `G-RUN`/H3未通过。

## 11. 剩余专业责任

W005正式Return先回原E1。E1随后：

1. 核运输、binding、sentinel、manifest与hash；
2. 核FIOCLEX local constant、BPF delta和static evaluator；
3. 核其他ioctl仍拒绝且无安全断言放宽；
4. 判断R0-A/B/C四PASS；
5. 若STOP，接受可用子集并决定manager回交、有界收束或唯一合法后继；
6. 若四PASS，审查八EP patch/schema/9-18-22 fixture未执行/compile/serialization；
7. 更新EP矩阵和action eligibility；
8. 完成D003最终或部分专业回交；
9. 不自行通过G-RUN/H3或关闭父Q。

## 12. 当前准确终态

```text
D003 professional state       = IN_PROGRESS
accepted Worker Returns       = W002 + W003 + W004
W004 disposition              = ACCEPT_STOP_EVIDENCE_WITH_STRICT_LIMITS
issued successor              = W005
W005 physical dispatch        = NOT CONFIRMED IN C0013
W005 Return                   = NONE
remaining scope               = consume W005 and finish D003 judgment
continuation                  = W005 ORDER.json
G-RUN                         = NOT PASSED
H3                            = NOT AVAILABLE
parent questions              = OPEN
parent task completion        = NOT CLAIMED
```
