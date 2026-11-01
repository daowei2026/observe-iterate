# BI-01-CO-04 R0008｜Replay 技术接收、目标取舍与 Professional 再放行

- `work_id`: `BI-01`
- `run_id`: `BI-01-CO-04`
- `invocation_id`: `BI01-CO-04-R0008-REPLAY-INTAKE-82bb0b60`
- `assignment_token`: `c12f9a5ebbffc8935b4966455a2854163c0e6aa00bd18b33`
- `role`: `management`
- `recipient`: `chatgpt:BI-01-CO-04:management`
- `decision`: `ACCEPT_BLOCKED_REPLAY_CLOSE_NATIVE_VISIBILITY_ROUTE_ADOPT_QUERY_COMPLETION_ASOF_AND_RELEASE_SAME_WORK`
- `accepted_worker_order`: `BI01CO04-ASOF-VISIBILITY-REPLAY-01`
- `accepted_worker_exit`: `BLOCKED_NO_LOOKAHEAD_PROOF`
- `operational_contract`: `QUERY_COMPLETION_ASOF_V1`
- `professional_task`: `BI-01-CO-04-CASE-INITIAL-ASOF`
- `professional_task_status`: `ACTIVE_RELEASED_AFTER_CURRENT_SNAPSHOT_AND_PREFLIGHT`

<a id="decision-summary"></a>
## 1. 管理决定

管理接收 `BI01CO04-ASOF-VISIBILITY-REPLAY-01` 的真实回交，准确接收范围是：

> 对 rb／hc／i、30m、冻结至 `2021-09-30 15:00:00 Asia/Shanghai` 的物理输入前缀，Worker 已形成新 replay 身份、冻结源码／二进制／参数／输入、六组原生 batch 执行、逐文件 receipt、边界审计、失败注入和独立 validator；但原生引擎没有暴露逐事件对象状态、首次出现、撤回／重现或消费者 publish／known-time，因此不能在不改变算法或发明语义的条件下证明 event-level `first_seen_at` 与对象生命周期。

由此管理接收出口 `BLOCKED_NO_LOOKAHEAD_PROOF`，并拒绝把 batch 输入边界 PASS 升级为 native event-level visibility PASS。R0007 规定的同类技术路线至此关闭：不再继续搜索旧文件、补历史聊天、做第三次可知性重放或要求 Worker 发明生命周期。

同时，管理不把这一技术阻断升级为“现有特征没有业务价值”。完整业务目标允许在当时可执行的工具条件下形成前瞻选择判断；当前原生系统是 batch 查询器而非发布事件流。因此本轮作出明确目标取舍：

- **放弃当前 Case 对“历史生产系统逐对象原生首次发布时间”的要求；**
- **采用 `QUERY_COMPLETION_ASOF_V1`：决策者在固定 cutoff T 后，只把截至 T 的物理行情前缀送入冻结 batch 引擎；查询完成后得到的对象集合，是该次决策可用状态。**

这是一个新的、范围受限的 operational contract，不是对旧 run publish 语义的修复。它支持验证“以当时数据运行现有特征后，能否形成跨品种选择认识”，但不能证明旧生产页面在历史当时已实时发布同一对象。

为避免事后挑 T，本轮把唯一主判断 cutoff 预先锁定为：

- `T_bar_cutoff = 2021-09-30 15:00:00 Asia/Shanghai`
- `T_decision = frozen-prefix query completion`
- `future_evaluation_window = T_bar_cutoff 之后至 2021-10-15 15:00:00 Asia/Shanghai`，只在判断冻结后读取。

该 cutoff 来自 R0007 预先固定的 decision-window 终点和已完成六组矩阵，不因未来涨跌或对象形态选择。原 Professional 现在按同一任务继续第二次有效调用；不增加 Worker、不增加 Reader、不重做 R0005 输入资格分析。

<a id="replay-evidence"></a>
## 2. Replay 身份、实物与独立核验

### 2.1 真实 Worker 结果

- result commit：`e25e585779152aa670d54c87efecba984af4b7e3`
- output root：`runs/BI-01-CO-04/artifacts/worker-BI01CO04-ASOF-VISIBILITY-REPLAY-01/`
- replay run：`BI01CO04_ASOF_REPLAY_20261101T203232Z_f4a75f64`
- Worker exit：`BLOCKED_NO_LOOKAHEAD_PROOF`
- result check：`45557c7f6ae9d932c463e9cbae12e361dd3910ad:runs/BI-01-CO-04/provenance/worker-BI01CO04-ASOF-VISIBILITY-REPLAY-01/RESULT_CHECK.json`

管理实际检查了 `FULL_RESPONSE.md`、`BLOCKER_REPORT.md`、`REPLAY_MANIFEST.json`、`SOURCE_SNAPSHOT.json`、`TIME_CONTRACT.md`、`NATIVE_OBSERVABILITY_ASSESSMENT.json`、`BATCH_INPUT_BOUNDARY_AUDIT.json`、`MATRIX_EXECUTION_RECEIPTS.json`、`NO_LOOKAHEAD_VALIDATION.json`、`FORMAL_BASELINE_COMPARISON.json`、`VISIBILITY_LEDGER.csv`、`OBJECT_LIFECYCLE_LEDGER.csv`、`FAILURE_INJECTION_RESULTS.json`、`INDEPENDENT_VALIDATION.json`、`PACKAGE_RECEIPT.json` 和 `SHA256SUMS`。

### 2.2 接受的事实

1. 三品种、big／mid 六组冻结 batch 执行均返回成功，输入均为同一 2160-bar 物理前缀；
2. OS 级边界审计没有发现执行时打开前缀外正式行情，`physical_prefix_bound_passed=true`；
3. `canonical_upper_bound=2021-09-30T15:00:00+08:00`，PNV 行情文件在引擎执行后保持不变；
4. frozen source、entrypoint、binary、参数、环境、任务、stdout／stderr 和输出均有逐文件 hash；
5. 旧正式对象与新 batch 输出的重叠／差异已逐行保留，没有把不匹配行静默丢弃；
6. validator 能拒绝未来数据、错时轴、空状态、乱序、缺方向和伪生命周期等坏包；
7. Worker 没有把缺失的 first-seen、upstream direction、撤回／重现状态伪造成正式字段。

### 2.3 阻断的事实

1. 原生入口一次性执行完整 prefix 后返回最终 batch 对象集合，没有事件回调或每个 bar 后的对象快照；
2. `VISIBILITY_LEDGER` 和 `OBJECT_LIFECYCLE_LEDGER` 只能如实记录 UNKNOWN／BLOCKED，不能证明逐对象 first-seen；
3. `xConfirm`、`event_ts`、bar close time 与 calendar alternate 均没有权威消费者 publish 合同；
4. batch prefix 的物理无未来边界，不等于每个对象在 prefix 内何时首次可见；
5. 要得到 event-level 生命周期，必须新增 observer、逐前缀重复执行或改变系统能力；这超出“只记录、不改算法”的工单边界。

管理因此不接受 `QUALIFIED_FOR_PROFESSIONAL_ASOF` 的旧定义；但接受 batch query 在完成后形成一个可见快照的客观事实。

<a id="operational-contract"></a>
## 3. `QUERY_COMPLETION_ASOF_V1` 合同

### 3.1 决策对象

本轮 Professional 只能使用以下状态：

> 对固定 `T_bar_cutoff`，物理隔离所有 T 后行情，运行冻结参数和冻结引擎；引擎完成后返回的 big／mid 对象集合与截至 T 行情，共同构成 `T_decision` 时可用信息。

`known_time` 在本合同中指**本次 query completion**，而不是对象原生首次发布。每条状态必须带 replay run、symbol、scale、prefix hash、query receipt 和 source key。

### 3.2 固定 cutoff 与禁止挑选

主路径只允许：

- `T_bar_cutoff = 2021-09-30 15:00:00 Asia/Shanghai`
- 三品种：rb／hc／i
- 频率：30m
- 尺度：big／mid
- 参数：replay manifest 冻结参数

不得在看到 10 月行情后改 T，不得从多个 cutoff 中挑表现最好者，不得改品种、参数或窗口。若该 cutoff 不能形成可比较状态，合法结论是“在本固定 query snapshot 下没有可比候选”，不是另找 T。

### 3.3 方向与对象语义

- upstream direction 仍为 null 时不得补称正式方向；
- 可使用新字段 `derived_geometric_turn_type`：
  - `LOW_CONFIRMED_PROXY` 当 `yConfirm > y`；
  - `HIGH_CONFIRMED_PROXY` 当 `yConfirm < y`；
  - `FLAT_OR_UNRESOLVED_PROXY` 当二者相等或任一缺失；
- 该字段只能描述返回对象的几何关系，必须标记 `DERIVED_NOT_UPSTREAM_DIRECTION`；
- replay-local occurrence key 不能冒充旧系统 object id 或 revision 链；
- Professional 应以“query snapshot 中返回的最近 confirmed geometry／line relation”表述，不得写成“该对象在历史生产中于某时首次出现”。

### 3.4 前瞻目标与挑战

Professional 必须在读取 T 后行情前先冻结：

1. 候选／排序／无候选；
2. 明确后续市场过程，例如相对延续、相对回撤、同背景下强弱分化或无法比较；
3. 评价时段和反例条件。

随后只读 `2021-09-30 15:00:00` 之后至 `2021-10-15 15:00:00` 的 bounded tail，检查最近自然挑战、失败候选或合法无候选。未来行情只用于评价，不能回写 snapshot 或更换判断。

### 3.5 能推出与不能推出

可以检验：

- 在固定数据前缀上运行现有 big／mid 特征后，query snapshot 是否提供跨品种差异；
- 这种差异能否支持一个预先冻结的后续市场判断；
- 当前“大尺度背景＋中尺度差异”设想在该 operational workflow 下是否有初步业务增量。

不能检验：

- 旧历史系统是否逐 bar 实时发布同一对象；
- `event_ts`／`xConfirm` 是否等于原生产消费者 known time；
- event-level revision、撤回与重现；
- 该单 Case 是否足以发布稳定方法或通用 Agent。

<a id="professional-release"></a>
## 4. Professional continuation 放行

正式 continuation：`runs/BI-01-CO-04/reviews/management-R0008/PROFESSIONAL_CONTINUATION.md`

- recipient：`chatgpt:BI-01-CO-04:professional`
- kind：`EXISTING_AUTHORIZED_REPAIR / SAME_WORK`
- task：沿用 `runs/BI-01-CO-04/01_当前任务.md`
- question：沿用 `CASE-FIRST-ASOF-CROSS-SYMBOL-SELECTION`
- input contract：`QUERY_COMPLETION_ASOF_V1`
- effective Professional call：续发后为第 2 次
- Reader：不新增；业务问题和 task blob 未改变，变化已由管理显式消费
- Worker：不新增；现有 replay package 已包含 frozen prefix、六组输出、行情、对象与 bounded tail 来源

主控须先基于当前 README、地图、任务、Binding、Intake 和 R0008 决定计算新的 Workmap snapshot，并运行适用 dispatch preflight。通过后直接发送 continuation；机械失败只修直接字段，不再返回管理重做业务取舍。

<a id="trigger-assessment"></a>
## 5. 触发与投入裁定

| 触发 | 本轮状态 | 管理解释 |
|---|---|---|
| `FIRST_USABLE_ASOF_LOOP` | `NOT_YET` | 技术包尚未被 Professional 转成冻结判断、未来评价和方法反馈 |
| `MATERIAL_INPUT_OR_METHOD_CHANGE` | `SATISFIED_AND_CONSUMED` | event-level native visibility 路线关闭，改用 query-completion operational contract |
| `ACTIVE_WORK_EFFORT_REVIEW` | `NOT_YET` | 有效 Professional 调用仍为 1；Worker 调用不计入 |

第二次 Professional 调用必须直接形成业务主体或明确给出固定 snapshot 下不可比较的业务结论。若仍停留在来源／资格循环，`ACTIVE_WORK_EFFORT_REVIEW` 到期，管理必须停止继续技术加厚并改变问题范围或向 Owner 提交目标取舍。

<a id="independent-review"></a>
## 6. 独立审查裁定

当前仍不签独立业务审查：尚无候选、排序或方法增量可复做。Replay 自带的独立 validator 只覆盖技术包和失败注入，不等于业务审查。第二次 Professional 形成承重业务结论后，管理按影响决定是否签具名独立专业审查。

<a id="completed-scope"></a>
## 7. 本轮完成范围

- 核 R0008 管理身份、真实发送与完整派发原文；
- 独立检查 replay package 的源码／参数／输入冻结、六组执行、边界审计、对象输出、ledger、baseline、validator、receipt 和 blocker；
- 接收 `BLOCKED_NO_LOOKAHEAD_PROOF`，拒绝把物理 prefix PASS 冒充 event-level known-time PASS；
- 关闭同类 native visibility 技术搜索，不签第三个 Worker；
- 明确作出目标取舍并采用 `QUERY_COMPLETION_ASOF_V1`；
- 预先锁定唯一 cutoff、方向代理公式、未来评价尾部和禁止挑选规则；
- 保持原业务问题 ACTIVE，签发 same-work Professional continuation；
- 保持 `known_pro_turns=1`，裁定 CHANGE 已消费、RESULT／EFFORT 未满足；
- 未虚报 Professional 已续发、业务 T 已由专业者消费、候选已形成或 Owner 已接收。

<a id="remaining-scope"></a>
## 8. 全部重要剩余

1. 主控尚需记录当前 Workmap snapshot，运行 dispatch preflight，并实际发送 R0008 Professional continuation；
2. Professional 尚需只用固定 query snapshot 形成 rb／hc／i 状态表，冻结候选／排序／无候选与未来过程；
3. Professional 尚需读取 bounded tail，检查最近自然挑战／失败候选，说明替代解释与方法增量；
4. 第二次有效调用结束时必须回管理并触发 RESULT 或 EFFORT；
5. 管理尚需接收首个业务循环，必要时签独立专业审查；
6. 相邻 Case、Owner 可读首版、真实反馈、适用边界和阶段收拢仍未完成。

完整 BI-01 工作保持 ACTIVE。当前不再等待 event-level publish 语义；下一步必须进入业务判断。

<a id="material-use"></a>
## 9. 材料使用记录

本轮实际读取并用于裁定：

- R0008 `FULL_ASSIGNMENT.md`、`INVOCATION.json`、`SEND_RECEIPT.json` 和当前分支身份；
- R0007 `DECISION.md`、`WORKER_ORDER.md`、地图、README、Intake 和 Adoption Status；
- replay `FULL_RESPONSE.md`、`BLOCKER_REPORT.md`、`REPLAY_MANIFEST.json`、`SOURCE_SNAPSHOT.json`、`TIME_CONTRACT.md`、`NATIVE_OBSERVABILITY_ASSESSMENT.json`；
- `BATCH_INPUT_BOUNDARY_AUDIT.json`、`MATRIX_EXECUTION_RECEIPTS.json`、`NATIVE_PREFIX_ROUTE_EXECUTION.json`、`NO_LOOKAHEAD_VALIDATION.json`；
- `FORMAL_BASELINE_COMPARISON.json`、`RECOMPUTED_OBJECT_ROWS.csv`、两份 ledger、failure injection、independent validation、receipt 与 seal；
- Worker `RESULT_CHECK.json`；
- 当前专业任务及 Question Work Binding、Workmap Binding 与 dispatch／snapshot 规则。

`unread_required=[]`。`unavailable_required` 是旧生产系统的 event-level publish／first-seen／revision 合同；该缺口已被准确关闭，不再由管理或 Worker补猜。

<a id="handoff"></a>
## 10. 准确接续

主控下一步：

1. 读取本决定、`PROFESSIONAL_CONTINUATION.md` 和更新后的 Workmap Intake；
2. 计算并记录当前 exact Workmap snapshot；
3. 以现有 `01_当前任务.md` 全文为 `current_task_ref`、本决定 `#professional-release` 为 `task_adoption_ref`、continuation 文件全文为续接约束，建立原 Professional 的新 R；
4. 运行适用 pre-dispatch；通过后向 `chatgpt:BI-01-CO-04:professional` 实际发送；
5. 不再派发 Worker 或第二 Reader，不允许 Professional 重开 native known-time 调查；
6. 第二次有效 Professional 回交后立即回本管理聊天 M-REASSESS，接收业务结果并执行 RESULT／EFFORT 裁定。

本轮结束于“blocked replay 已准确接收、技术路线已关闭、query-completion 业务合同与 Professional continuation 已签发”；实际发送和业务结果仍需后续真实记录证明。
