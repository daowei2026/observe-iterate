order_id: BI01CO04-ASOF-VISIBILITY-REPLAY-01
work_id: BI-01
run_id: BI-01-CO-04
issuer_role: management
issuer_ref: chatgpt:BI-01-CO-04:management
issuer_invocation_id: BI01-CO-04-R0007-WORKER-INTAKE-c149d108
issuer_assignment_token: ade995cbba55556272c158e396739c9f75ebf796a3a23282
return_to: chatgpt:BI-01-CO-04:management
continuation_thread_id: 01a19881-cebf-73f3-a4d3-76c57bce0fe4
owner_authorized_original_thread_id: 01a17dd7-5033-7e63-b7a2-edd90b691c33
expected_workspace: /dwdhome/fy/cgpterm
status: ISSUED_NOT_SENT

# BI-01-CO-04｜三品种 as-of 可知性顺序重放工单

<a id="worker-purpose"></a>
## 1. 技术目的

为当前正式业务任务 `BI-01-CO-04-CASE-INITIAL-ASOF` 生成一个**新命名、字节冻结、逐事件可知性可审计**的最小重放包，使 Professional 可以只使用 T 时已知状态进行 rb／hc／i 的跨品种比较。

本工单不是修饰旧 run，也不把旧 slice 重新命名为合格输入。它以 `BI01CO04-INPUT-RECOVERY-01` 已恢复的真实行情、参数、正式对象和冲突证据为基线，在三品种、30m、同一历史窗口内执行一次严格顺序重放，记录每个对象何时首次出现、何时改变或消失，以及该时刻实际读到的最大输入时间。

Worker 不选择业务 T，不排序品种，不判断候选／无候选，不修改管理工作面或续发 Professional。

<a id="worker-authority"></a>
## 2. 授权、线程与边界

- 实际 continuation thread：`01a19881-cebf-73f3-a4d3-76c57bce0fe4`
- Owner 原始授权 thread：`01a17dd7-5033-7e63-b7a2-edd90b691c33`
- workspace：`/dwdhome/fy/cgpterm`
- 仓库／分支：`daowei2026/observe-iterate@fy/feature-based-case-observation`
- 管理采用：`956ae5891409e0092dd453d1379017486dca0d76:runs/BI-01-CO-04/reviews/management-R0007/DECISION.md`
- 输入基线：`dfdf843b47c03c0121fd7151b72f24adb5d986c0:runs/BI-01-CO-04/artifacts/worker-BI01CO04-INPUT-RECOVERY-01/`

只管理本工单 Goal。禁止启动无关聊天、递归审计旧 runs、扩大到全市场、改变特征数学或参数寻优。当前历史 run 仅作源字节和对照，新的结果必须使用独立 replay identity。

<a id="worker-required-reads"></a>
## 3. 必须先读

1. `runs/BI-01-CO-04/reviews/management-R0007/DECISION.md`
2. `runs/BI-01-CO-04/reviews/management-R0006/WORKER_ORDER.md`
3. `runs/BI-01-CO-04/artifacts/worker-BI01CO04-INPUT-RECOVERY-01/FULL_RESPONSE.md`
4. `.../BLOCKER_REPORT.md`
5. `.../FIELD_DICTIONARY.md`
6. `.../SOURCE_AND_REPRODUCTION.md`
7. `.../DATA_MANIFEST.json`
8. `.../PACKAGE_RECEIPT.json`
9. `.../evidence/VALIDATION.json`
10. `.../evidence/INDEPENDENT_VALIDATION.json`
11. `.../evidence/OBJECT_COVERAGE.json`
12. 当前业务任务 `runs/BI-01-CO-04/01_当前任务.md`

省略号均指上一条完整输入基线路径。只额外读取完成本工单所必需的源文件、配置、依赖、缓存和日志。

<a id="worker-output"></a>
## 4. 唯一输出位置

全部新实物写入：

`runs/BI-01-CO-04/artifacts/worker-BI01CO04-ASOF-VISIBILITY-REPLAY-01/`

至少包含：

- `FULL_RESPONSE.md`
- `REPLAY_MANIFEST.json`
- `SOURCE_SNAPSHOT.json`
- `TIME_CONTRACT.md`
- `VISIBILITY_LEDGER.csv` 或等价逐事件结构化文件
- `OBJECT_LIFECYCLE_LEDGER.csv`
- `FORMAL_BASELINE_COMPARISON.json`
- `NO_LOOKAHEAD_VALIDATION.json`
- `FAILURE_INJECTION_RESULTS.json`
- `PACKAGE_RECEIPT.json`
- `SHA256SUMS`
- 实际命令、日志、冻结源码／补丁和独立 validator
- 失败时的 `BLOCKER_REPORT.md`

不得修改 R0005／R0006／R0007 历史报告、当前业务任务、地图、Intake 或 Adoption Status。

<a id="worker-input-window"></a>
## 5. 固定范围

- symbols：`rb`、`hc`、`i`
- bar frequency：`30m`
- warm-up：从已恢复实际源起点 `2021-01-04 09:30:00` 开始，或算法严格需要的更晚且有证明的起点
- decision window：`2021-08-15 00:00:00` 至 `2021-09-30 15:00:00`
- bounded evaluation tail：最多至 `2021-10-15 15:00:00`，单独分区，只用于后续挑战；不得用于回写 decision-window 状态
- parameters：以已恢复、已证明实际消费的 big／mid selected 参数为起点；不得调参
- small scale：本单不生产，除非证明它是 big／mid 生命周期审计不可缺的技术依赖；若加入须单列理由，不能成为业务门槛

<a id="worker-source-freeze"></a>
## 6. 新 replay 身份与源冻结

创建唯一 `replay_run_id`，不得沿用旧 `GTQH_C001_three_turns_20261101_162005` 身份。冻结并逐文件 hash：

1. 实际执行入口、所有被 import 的业务源码、二进制／动态库和 instrumentation wrapper；
2. 实际参数、日历／session 配置、Python／系统依赖、环境变量白名单；
3. rb／hc／i 原始行情输入及已恢复正式基线；
4. 命令、cwd、开始／结束时间、返回码、stdout／stderr；
5. 若 workspace dirty，必须把**实际使用的源码字节和 patch**完整装包，不能只写 Git commit；
6. copied、wrapper-only instrumentation、recomputed feature output 分开记录。

Instrumentation 只能记录输入边界与状态变化，不得改变特征计算、排序、阈值、浮点路径或参数。用对照测试证明 instrumentation on/off 在相同前缀上的业务数值输出一致。

<a id="worker-replay-contract"></a>
## 7. 顺序重放与可知性账本

严格按 canonical source bar／event 时间单调追加输入。对每个事件和每个 big／mid 状态记录：

- `replay_run_id`, `symbol`, `scale`, `replay_event_seq`, `replay_event_ts`
- `max_input_bar_ts`, `max_input_source_row`, `input_prefix_hash`
- `source_actual_uti`, `actual_bar_ts`, `actual_price`
- `source_confirm_uti`, `confirm_bar_ts`, `confirm_price`（源正式存在时）
- `first_seen_at`, `last_seen_at`, `state_change_at`
- `present`, `withdrawn`, `reappeared`, `lifecycle_seq`, `state_hash`
- `source_key` 与明确标注为 replay-local 的 `replay_object_key`
- upstream direction 及证明；若不存在，保留 null
- 可另列 `derived_geometric_turn_type`，但必须给固定公式、来源字段和 `DERIVED_NOT_UPSTREAM_DIRECTION` 标签
- `event_ts`, canonical bar time, calendar alternate time 分列
- unknown／missing／calculation failure／no state 的不同状态

`replay_object_key` 仅用于本次生命周期连接，不能冒充旧系统正式 object id。对象首次被增量引擎输出的事件时间才可成为 `first_seen_at`；静态最终切片的 `xConfirm` 或 `event_ts` 不得直接倒填该字段。

<a id="worker-time-contract"></a>
## 8. 时间合同

1. 选择一个 canonical consumer clock，并说明为什么；优先使用实际输入 bar `closeTs`／engine event time，不得静默混合 `natural_tsa`；
2. 时区固定并显式记录为 `Asia/Shanghai` 或现场真实值；记录交易所 session、夜盘归属和端点规则；
3. 原 B01 冲突全部保留为 alternate mapping 和 conflict flag；不得通过取最早／最晚值消失；
4. 只有在 `max_input_bar_ts <= replay_event_ts` 且无未来测试通过时，`first_seen_at` 才可作为 operational known time；
5. evaluation tail 必须物理或逻辑隔离，任何 decision-window ledger hash 不得因 tail 删除、替换或追加而变化。

<a id="worker-validation"></a>
## 9. 无未来信息验证

至少完成以下独立检查：

### 9.1 Monotone input audit

对全部事件验证输入前缀严格单调，且任一状态的 `max_input_bar_ts` 不晚于 `replay_event_ts`。列出所有违反项；存在未解释违反即 BLOCKED。

### 9.2 Prefix invariance

对 decision window 内每次 big／mid 状态变化，在只提供截至该事件前缀的独立执行中重算并与主顺序重放状态比较。至少比较对象集合、actual／confirm 坐标、价格、状态 hash 与 first-seen。不能只抽样成功点。

### 9.3 Future-tail deletion／perturbation

删除 9 月 30 日后输入，及用明显扰动值替换 evaluation tail；验证 decision-window 全部状态、first-seen 和 hash 不变。任何变化即证明未来依赖，必须 BLOCKED。

### 9.4 Instrumentation neutrality

对相同前缀比较 instrumentation on/off 的业务数值结果。wrapper 只允许新增日志／账本，不得改变原状态。

### 9.5 Formal baseline comparison

与 `dfdf843...` 包中正式 slice 和已恢复对象逐项比较。相同语义字段须逐值一致；旧正式行因最终修订、窗口后 event 或时间冲突无法匹配时逐条列明，不得丢弃。

### 9.6 Failure injection

至少覆盖：未来数据泄漏探针、时间轴错配、对象撤回／重现、缺方向、空事件、乱序输入。Validator 必须拒绝被注入的坏包。

<a id="worker-exits"></a>
## 10. 两个合法出口

### A. `QUALIFIED_FOR_PROFESSIONAL_ASOF`

只有同时满足才可给出：

- 新 replay 身份及全部源字节冻结；
- decision-window 全量顺序 ledger 与生命周期账本；
- canonical time 合同和 B01 冲突保留；
- monotone、prefix invariance、tail perturbation、neutrality、baseline、failure injection 全部通过；
- operational known time 可逐对象复核；
- receipt 与独立 validator 全通过。

### B. `BLOCKED_NO_LOOKAHEAD_PROOF`

任何承重条件不能在不改变业务算法下满足时给出。`BLOCKER_REPORT.md` 必须列：已执行命令、失败点、受影响对象／窗口、最小缺件、为何不能通过更多搜索或同类重跑解决，以及仍可保留的真实实物。

不得给第三种含糊“基本可用”出口。技术 qualifier 不等于市场候选或业务 Gate。

<a id="worker-checks"></a>
## 11. 最低自查与停止规则

- 全部三品种／两尺度／固定窗口覆盖；
- 每个 first-seen 都能回到具体 replay event 和 input prefix；
- 每个 receipt hash 可重算；
- copied／instrumented／recomputed 分账；
- 旧 run 与新 replay 身份不可混同；
- 没有用结果好坏选择 T、窗口、参数或品种；
- 没有形成市场判断、修改管理面或触发其他聊天。

本单只允许一次有限执行。若 exact replay 不成立，按出口 B 停止；不得继续递归搜索、调参或另起实现路线。

<a id="worker-return"></a>
## 12. 回交

结果回 `chatgpt:BI-01-CO-04:management`。`FULL_RESPONSE.md` 必须明确：

1. 最终出口 A 或 B；
2. replay identity、实际版本、命令、输入、输出与校验；
3. copied／instrumented／recomputed 的准确范围；
4. 所有失败、冲突、未知和未完；
5. 是否足以交回原 Professional，但不得自行续发；
6. GitHub commit 与唯一输出路径。

Worker 不更新 Workmap Intake，不宣布 T、候选、无候选、方法增量或业务 Gate。管理先做技术接收，再决定原 Professional continuation。
