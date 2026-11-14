# D003｜C0011 W003 最小执行绑定修签报告

## 0. 身份与状态

- `run_id`：`OI-EAW-WALL-20261114-01`
- `call_id`：`C0011`
- `delegation_id`：`D003`
- executor：`chatgpt:OI-EAW-WALL-20261114-01:executor:E1`
- return_to：`chatgpt:OI-EAW-WALL-20261114-01:manager`
- 当前 `professional_state`：**IN_PROGRESS**
- accepted Worker Return：W002 formal STOP Return
- 本轮实际派发/执行 Worker：**NONE**
- W003 当前状态：**REPAIRED_ORDER_PUBLISHED / NOT_YET_DISPATCHED**
- `G-RUN`：**NOT PASSED**
- H3：**NOT AVAILABLE**
- 三个父 Q：**OPEN**
- 父任务完成：**NOT CLAIMED**

本轮只修复 W003 的两处执行绑定冲突及对应运输签认，不改变 C0010 已合法形成的 Phase-0 恢复后继、业务范围、专业判断或任何 Gate。

## 1. 正式输入

- C0011 FULL_ASSIGNMENT：`daowei2026/observe-iterate@84551f72b3a5dda03b4fb98434cb854168518fa6:longrun/runs/OI-EAW-WALL-20261114-01/calls/C0011/FULL_ASSIGNMENT.md`
- C0011 Invocation：`daowei2026/observe-iterate@32684eb7a9a65e494d2f8853b1110fff6d37a74e:longrun/runs/OI-EAW-WALL-20261114-01/calls/C0011/INVOCATION.json`
- 具名反馈：`daowei2026/observe-iterate@9ca270a900560993a176e864b5a3841e54fe332d:longrun/runs/OI-EAW-WALL-20261114-01/calls/C0011/W003_EXECUTION_BINDING_FEEDBACK.json`
- C0010 真 Return：`daowei2026/observe-iterate@62f4c2feca9cf0922522a1c05a8cc1695d062395:longrun/runs/OI-EAW-WALL-20261114-01/calls/C0010/PRO_RETURN.json`
- 当前 D003：`daowei2026/observe-iterate@b7200816f86395cd1475ea3a482fc2e63086b967:longrun/runs/OI-EAW-WALL-20261114-01/delegations/D003/DELEGATION.json`

原 C0010 W003 候选：

- MD：`daowei2026/observe-iterate@f3d4b60ee499875c02b1fa7ebe8d15666a4951c2:longrun/runs/OI-EAW-WALL-20261114-01/work_orders/W003/ORDER.md`
- JSON：`daowei2026/observe-iterate@35eeb0414cf71963938bcbf97afc744bff72ef8c:longrun/runs/OI-EAW-WALL-20261114-01/work_orders/W003/ORDER.json`

该候选从未送达 Worker、从未建立 W003 锁、从未新建聊天、从未执行任何恢复命令；本轮可以在同一 W003 上做最小一致修签。

## 2. 修签一｜原 W1 物理聊天与 fresh W003 资格分开

原文“W002 原件、锁、thread、命令资格和本地目录均不复用”把物理聊天也排除了，与当前 Run 必须沿用已绑定原 W1 聊天的执行约束冲突。

修签后合同为：

```text
沿用本 Run 已绑定的原 W1 物理聊天
不创建或重建 Worker 聊天
但对 W003 重新实核：
  owner
  thread/session
  model/effort
  cwd
  no old writer
  new single-writer lock
```

同时明确不继承：

```text
W002 lock session
W002 execution eligibility
W002 command eligibility
W002 engineering directory
W002 frozen originals
```

因此，“沿用物理聊天”与“W003 fresh actual exclusive”不再混同。

## 3. 修签二｜保持真实 HOME/CODEX_HOME，不允许任务新增写入

原文要求 HOME 本身位于 W003 根，与实际执行绑定不兼容。

修签后合同为：

```text
HOME/CODEX_HOME 保持真实值不变
不得重设、迁移或伪装成 WORK_ROOT
二者只按既有执行绑定读取
不得承载本任务新增业务文件、tmp、cache、config、log或结果
```

所有本任务新增内容仍必须位于：

```text
/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D003/W003
```

工具必须使用其支持的显式任务目录选项，把新增 tmp/cache/config/log 定向 W003 根。若工具无法同时满足真实 HOME/CODEX_HOME 与零外写，准确 STOP；不得：

- 改写 HOME/CODEX_HOME；
- 为 HOME/CODEX_HOME 增加外写例外；
- 放宽 `outside writes = 0`；
- 放宽任何 cap；
- 以工具默认目录静默写出。

Landlock／等价 confinement 仍只允许 W003 根新增写入；真实 HOME/CODEX_HOME 不成为 write allow path。

## 4. 保持不变的合同

以下全部保持原样：

- Owner/D003 字面 grant 与 W003 独立实际子根；
- R0-A kernel confinement + full write trace；
- procfs 不豁免，实际外写必须为0；
- R0-B 只选一套 compatible offline closure，不拼接 resolver；
- R0-C 四项非空预算与 continuous monitors；
- 四项 PASS 后才能 staged construction；
- 全部 caps：2 GiB、4 GiB、25 min、50,000 files、outside writes 0、scenario runs 0；
- 条件性八 EP；
- 禁止任何 single/partial/full scenario execution；
- 禁止 normal、DBA、wrapper、native reader；
- 禁止共享源码写入、production lifecycle 语义修改或 push；
- W002 有效 STOP 与 E1 限域接受；
- G-RUN 未通过、H3 不具备、三个父 Q OPEN。

## 5. 修订后正式 W003 原件

### 5.1 先发布的 ORDER MD

`daowei2026/observe-iterate@ab216297916d708d977f67005ced922a6df1c12c:longrun/runs/OI-EAW-WALL-20261114-01/work_orders/W003/ORDER.md`

核对项：

- `issuer_call_id=C0011`；
- 原 E1／原 W1 逻辑身份／return_to 原 E1；
- 原 W1 物理聊天沿用与 W003 fresh verification 同时写明；
- HOME/CODEX_HOME 真实绑定与 W003-only new writes 同时写明；
- 旧 C0010 候选被标为从未派发的历史；
- 其余方法、cap、EP、禁令未放宽。

### 5.2 后发布的 ORDER JSON

`daowei2026/observe-iterate@3afc8e9eedb34ac3b25ba69e383c778c37622c30:longrun/runs/OI-EAW-WALL-20261114-01/work_orders/W003/ORDER.json`

核对项：

```text
issuer_call_id = C0011
instructions_ref = 新MD真实先行ref ab216297...
issuer = 原E1
worker = 原W1逻辑身份
return_to = 原E1
delegation_ref = 当前C8 D003
```

机读 grant 仍逐字使用 Owner 根 token，没有把实际子根误写成 Owner grant，也没有扩大 allowed_writes。

## 6. 当前没有发生的事项

截至本报告：

- 修订 W003 尚未实际派发；
- 没有新建或重建 Worker 聊天；
- 没有建立 W003 锁；
- 没有运行 Landlock、closure、budget 或 monitor probe；
- 没有 Linux staged source、patch、compile、serialization；
- 没有 scenario/normal/DBA/wrapper/native-reader；
- 没有 current O/C/A/D 业务 evidence；
- 没有新的 Worker Return；
- 没有通过 G-RUN 或 H3。

## 7. 剩余专业责任

主控对修订 W003 完成字面、物理聊天、HOME/CODEX_HOME、model/effort/cwd/no-writer/new-lock 和 V2 Gate 核验后，才可在原 W1 聊天中实际派发。

W003 正式 Return 必须先回原 E1。E1 后续仍需：

1. 核实运输、manifest、hash与actual binding；
2. 核原 W1 聊天沿用但 W003资格/new-lock为fresh；
3. 核真实 HOME/CODEX_HOME未改变且任务新增写入为0；
4. 判断 W002 三 blocker是否解除；
5. 若Phase0 PASS，审查八EP、patch、9/18/22 fixture未执行、compile/serialization与cap；
6. 更新D003专业矩阵并回原manager；
7. 不自行通过G-RUN、H3或关闭父Q。

## 8. 准确终态

```text
D003 professional state:       IN_PROGRESS
accepted_worker_refs:          [W002 formal Return]
issued_order_ref this call:     repaired W003 JSON @3afc8e9...
old C0010 W003 candidate:       NEVER DISPATCHED / SUPERSEDED FOR BINDING ONLY
repaired W003 dispatch:         NOT YET CONFIRMED
W003 Worker Return:             NONE
remaining scope:               consume repaired W003 and finish D003 judgment
continuation:                  repaired W003 ORDER.json
G-RUN:                         NOT PASSED
H3:                            NOT AVAILABLE
parent questions:              OPEN
parent task completion:        NOT CLAIMED
```
