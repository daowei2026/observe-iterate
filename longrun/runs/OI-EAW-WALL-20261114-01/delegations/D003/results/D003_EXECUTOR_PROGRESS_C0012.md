# D003 Executor Progress｜C0012 消费 W003 STOP 并签发 W004

## 0. 身份与当前状态

- `run_id`：`OI-EAW-WALL-20261114-01`
- `call_id`：`C0012`
- `delegation_id`：`D003`
- executor：`chatgpt:OI-EAW-WALL-20261114-01:executor:E1`
- return_to：`chatgpt:OI-EAW-WALL-20261114-01:manager`
- 本轮新增接受：W003 formal STOP Return
- 既有接受：W002 formal STOP Return（限域）
- 本轮新签：W004
- `professional_state`：**IN_PROGRESS**
- D003：**NOT COMPLETE**
- `G-RUN`：**NOT PASSED**
- H3：**NOT AVAILABLE**
- 三个父 Q：**OPEN**
- 父任务完成：**NOT CLAIMED**

本报告完成 C0012 当前可真实完成的专业工作：消费 W003、限定其证据资格、更新 EP 矩阵、把停止点收敛为明确的父子进程 stdin 接线问题，并签发具有新 root/lock/资格的 W004。它不把 W004 ORDER 发布写成物理派发、执行或回交。

## 1. 正式输入与运输

- C0012 FULL_ASSIGNMENT：`daowei2026/observe-iterate@9076e41ad5beeb09a0cdd84b57794f2664162716:longrun/runs/OI-EAW-WALL-20261114-01/calls/C0012/FULL_ASSIGNMENT.md`
- C0012 Invocation：`daowei2026/observe-iterate@9c8ec64ccbd02dc90a828482d7ae6337cc605659:longrun/runs/OI-EAW-WALL-20261114-01/calls/C0012/INVOCATION.json`
- W003 formal Return：`daowei2026/observe-iterate@e124f5662e4c683ee6abe572b78c6a8de15d4d3e:longrun/runs/OI-EAW-WALL-20261114-01/worker_results/W003/WORKER_RETURN.json`
- W003 evidence commit：`9aaaf4a3b322333b46f33b9e55c916b4cea1b1e3`
- 当前 D003：`daowei2026/observe-iterate@b7200816f86395cd1475ea3a482fc2e63086b967:longrun/runs/OI-EAW-WALL-20261114-01/delegations/D003/DELEGATION.json`

主控已核72份冻结文件、正式Return/validation、81项manifest、原W1身份和return-to路由；E1没有把运输PASS替代专业接受。

## 2. W003 专业结论

### 2.1 Decision

```text
ACCEPT_STOP_EVIDENCE_WITH_STRICT_LIMITS
```

W003 的 STOP 合法有效，不返修、不重开、不在其目录重试。

### 2.2 唯一实际尝试

父runtime使用：

```python
stdin=subprocess.DEVNULL
```

child fd0 实测为：

```text
/dev/null
O_RDWR|O_LARGEFILE
```

launcher在pre-enforcement inherited-FD inspection要求fd0不可写，fail-closed并exit73。此时NNP、Landlock ABI/rules/restrict、seccomp均未调用，probe/child均未执行。

专业定性：

```text
runtime-to-launcher stdin wiring failure
```

不是：

```text
Landlock kernel unsupported
kernel policy failure
write confinement pass
```

### 2.3 Trace范围

完整failed-launch trace共1071行。唯一成功descriptor write为W003 root内failure receipt 1214 bytes；该trace内successful outside write=0、unknown path=0。

限制：只覆盖失败launcher，不能证明后继、parent/control或全W零外写。

### 2.4 未进入范围

```text
R0-B closure                 = NOT ATTEMPTED
R0-C budgets/monitors        = NOT ATTEMPTED
Phase1/2                     = NOT ENTERED
staged source/patch/schema   = 0
fixture materialization      = 0
compile/serialization        = 0
scenario/normal/current data = 0
```

完整专业审查：

`daowei2026/observe-iterate@d883c9fd7b430d991b7bef9c5f303aa46071d062:longrun/runs/OI-EAW-WALL-20261114-01/delegations/D003/results/D003_W003_PROFESSIONAL_REVIEW_C0012.md`

## 3. Phase-0 blocker状态

| blocker | W003后状态 | 说明 |
|---|---|---|
| write confinement / zero outside writes | **未解除** | 本次停止于policy前；新增价值是定位stdin wiring |
| single compatible offline closure | **未解除/未尝试** | R0-A Gate阻断 |
| four budgets + monitors | **未解除/未尝试** | 四预测仍null，monitor未验证 |

四项 PASS：

```text
WRITE_CONFINEMENT_PASS             = false
OFFLINE_CLOSURE_PASS               = false / not attempted
FOUR_BUDGETS_KNOWN_WITHIN_CAP      = false / not attempted
CONTINUOUS_MONITORS_PASS           = false / not attempted
```

## 4. 八 EP 当前状态

```text
SATISFIED      = 0
PARTIAL        = 1  (EP-SCENARIO-04 old static ledger subset)
UNSATISFIED    = 1  (EP-WALL-SHARED-03)
NOT_ATTEMPTED  = 6
W003 new EP satisfied = 0
```

完整矩阵：

`daowei2026/observe-iterate@a9cc7533b0f131aa5ff1e74eb00f1110c8fb0ca2:longrun/runs/OI-EAW-WALL-20261114-01/delegations/D003/results/EP_ACCEPTANCE_MATRIX_C0012.md`

## 5. 为什么签发 W004

W003停止点具有直接、确定、可验证的最小修复：父runtime为launcher提供显式`O_RDONLY /dev/null`，launcher继续严格拒绝可写fd0。该修复：

- 不改Owner/D003 grant；
- 不放宽inherited-FD规则；
- 不增加write例外；
- 不放宽cap或禁令；
- 不需要scenario或production材料；
- 可以在新root和full trace下直接区分成功/失败。

另一个前置是主控在派发前只读确认外部sentinel不存在；W003停止前该确认未收到。

后继决定：

`daowei2026/observe-iterate@dc28c18212e1549a35b920e2ebdd42668f20b048:longrun/runs/OI-EAW-WALL-20261114-01/delegations/D003/results/W004_SUCCESSOR_DECISION_C0012.md`

## 6. W004 正式原件

### ORDER MD

`daowei2026/observe-iterate@f2fca11e1b5b7fefe5e91afe15bcf346b716caff:longrun/runs/OI-EAW-WALL-20261114-01/work_orders/W004/ORDER.md`

### ORDER JSON

`daowei2026/observe-iterate@347e4b2322ff2401aca21333cd3118f93d490baf:longrun/runs/OI-EAW-WALL-20261114-01/work_orders/W004/ORDER.json`

运输身份：

```text
issuer_call_id = C0012
issuer          = original E1
worker          = original bound W1
return_to       = original E1
delegation_ref  = current C8 D003
```

## 7. W004 的 two explicit deltas

### 7.1 read-only stdin

父runtime必须：

```text
open /dev/null O_RDONLY|O_CLOEXEC
verify access mode O_RDONLY
pass as child stdin
close parent copy after spawn
```

禁止`subprocess.DEVNULL`，禁止删除launcher的fd0 read-only断言。

### 7.2 controller sentinel preconfirmation

主控派发前只读确认不存在：

```text
/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D003/.W004-deny-outside-C0012-e9ed948d
```

不创建、不写、不删除。该receipt进入W004 binding。

## 8. W004不变Gate、cap与禁令

独立root：

```text
/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D003/W004
```

沿用原W1物理聊天，但fresh核资格/idle/cwd/model/effort/no-writer并取得新锁；W003资格/锁/root不继承。真实HOME/CODEX_HOME保持不变，任务新增写入只在W004 root。

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

仍禁止任何single/partial/full scenario、normal、DBA、wrapper、native reader、current/production material、shared source write/push和production lifecycle语义修改。

## 9. 当前没有发生

截至C0012 Return：

- W004只发布MD/JSON；
- 主控尚未在本调用回报W004 sentinel preconfirmation、物理派发或receipt；
- 没有创建W004 root/lock/chat；
- 没有运行read-only stdin launcher、Landlock、probe、closure、budget或monitor；
- 没有staging/patch/compile/serialization；
- 没有scenario/normal/current evidence；
- W004 Worker Return不存在；
- `G-RUN`/H3未通过。

## 10. 剩余专业责任

W004正式Return必须先回原E1。E1随后：

1. 核运输、binding、sentinel receipt、manifest和hash；
2. 核stdin只读接线真实修复且安全断言未放宽；
3. 判断R0-A/B/C四PASS；
4. 若STOP，接受可用子集并决定唯一修复、manager决策或有界收束；
5. 若四PASS，审查八EP patch/schema/fixture/compile/serialization；
6. 核fixture精确9/18/22且scenario run=0；
7. 更新EP矩阵和action eligibility；
8. 完成D003最终/部分专业回交；
9. 不自行通过G-RUN/H3或关闭父Q。

## 11. 当前准确终态

```text
D003 professional state       = IN_PROGRESS
accepted Worker Returns       = W002 + W003
W003 disposition              = ACCEPT_STOP_EVIDENCE_WITH_STRICT_LIMITS
issued successor              = W004
W004 physical dispatch        = NOT CONFIRMED IN C0012
W004 Return                   = NONE
remaining scope               = consume W004 and finish D003 judgment
continuation                  = W004 ORDER.json
G-RUN                         = NOT PASSED
H3                            = NOT AVAILABLE
parent questions              = OPEN
parent task completion        = NOT CLAIMED
```
