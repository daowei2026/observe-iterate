# BI-01-CO-04 R0009 Professional｜query-completion as-of 跨品种判断

- `work_id`: `BI-01`
- `run_id`: `BI-01-CO-04`
- `round_id`: `R0009`
- `invocation_id`: `BI01-CO-04-R0009-PROFESSIONAL-QUERY-ASOF-8d6fcf14`
- `assignment_token`: `625dea7ad3106c7bb13e2d923ed4e67f2d3713fcbf25f5a4`
- `role`: `professional`
- `professional_mode`: `CASE_OBSERVATION`
- `question_id`: `CASE-FIRST-ASOF-CROSS-SYMBOL-SELECTION`
- `contract`: `QUERY_COMPLETION_ASOF_V1`
- `assignment`: `daowei2026/observe-iterate@279e2925156031a5951f852e84911b88d035caf0:runs/BI-01-CO-04/provenance/turns/R0009/FULL_ASSIGNMENT.md::full`
- `management_release`: `daowei2026/observe-iterate@c286238462c07f15d9ebfe3cac06edc6a2da29d4:runs/BI-01-CO-04/reviews/management-R0008/DECISION.md::#operational-contract`
- `replay_package`: `daowei2026/observe-iterate@e25e585779152aa670d54c87efecba984af4b7e3:runs/BI-01-CO-04/artifacts/worker-BI01CO04-ASOF-VISIBILITY-REPLAY-01/`

<a id="decision-summary"></a>
## 1. 决定摘要

### 1.1 截至 T 的业务判断

**`NO_CANDIDATE`。**

在固定 `QUERY_COMPLETION_ASOF_V1` snapshot 中：

- rb 与 hc 是唯一具有相同大尺度几何 proxy 的可比 pair：两者均为 `HIGH_CONFIRMED_PROXY`；
- i 的大尺度为 `LOW_CONFIRMED_PROXY`，不属于同背景比较组；
- rb 与 hc 的最新 returned mid occurrence 仍同为浅 `HIGH_CONFIRMED_PROXY`，`(yConfirm-y)/y` 分别约为 `-0.270660%` 与 `-0.196113%`；
- 该差异同号、幅度都很小，不能在不新增规则、不偷看未来的情况下解释为哪一个品种更有相对韧性。

因此本轮没有强行从 rb／hc 中选一个，也没有把 i 放进不相同的大尺度背景。无候选是**合格 snapshot 的业务结果**，不是 snapshot 数据缺失。

### 1.2 完成状态

`SNAPSHOT_DECISION_COMPLETE__BOUNDED_TAIL_NOT_EXECUTABLE`

- query snapshot 状态表已提交；
- 判断已在任何 cutoff 后行情读取前独立冻结；
- 指定 bounded tail 的实际 30m 行没有进入当前可读、封口的 GitHub 交付，因此后续支持／反证和最近市场自然挑战不能计算；
- 冻结判断不因尾部未运输而改写，但首个完整可消费 as-of 循环尚未达到完成条件。

### 1.3 触发

| Trigger | 本轮状态 | 理由 |
|---|---|---|
| `FIRST_USABLE_ASOF_LOOP` | `NOT_YET` | 已完成 snapshot 与先冻结判断；未完成 bounded-tail 市场评价和最近自然挑战 |
| `ACTIVE_WORK_EFFORT_REVIEW` | `SATISFIED` | 本轮是第 2 次有效 Professional 调用；任务仍有一个明确承重输入未完，须管理决定有界运输或停止当前 Case |
| `MATERIAL_INPUT_OR_METHOD_CHANGE` | `NOT_YET` | 没有发现 query contract、参数、source identity 或对象语义发生新冲突；当前是指定 tail 未运输 |

<a id="question-and-contract"></a>
## 2. 问题、as-of 合同与固定范围

正式问题仍是：

> 在本 Run 可核的正式输入中，是否存在一个截至 T 至少两个品种具有可比较大尺度背景、而中尺度已确认状态存在差异的窗口？只用 T 时可知证据，能否对明确的后续市场过程形成候选／排序／无候选判断；后来的确认点、反向对象或失败区间如何支持、否定或限制该判断？本次结果对“用大尺度找背景、用中尺度找差异”的当前设想提出什么保留、修订或反例？

R0008 管理已采用 `QUERY_COMPLETION_ASOF_V1`，其合法 known-time 不是旧系统逐对象的历史 publish time，而是：

1. 只把截至 cutoff T 的物理行情前缀输入冻结 batch 引擎；
2. 六组 rb／hc／i × big／mid query 全部完成；
3. query 返回对象集合与截至 T 行情从此成为本次业务判断可用信息。

固定范围：

| 项目 | 固定值 |
|---|---|
| symbols | rb、hc、i |
| frequency | 30m |
| scales | big、mid |
| `T_bar_cutoff` | `2021-09-30 15:00:00 Asia/Shanghai` |
| `T_decision` | 六组 frozen-prefix query 全部完成后，即 `2026-11-01T21:01:47.861354+00:00` |
| future interval | `(2021-09-30 15:00:00, 2021-10-15 15:00:00] Asia/Shanghai` |
| parameters／binary／entrypoint | replay manifest 与 frozen source snapshot 字节 |

本合同不授予 event-level first-seen、撤回、重现、revision lifecycle 或历史实时发布语义。

<a id="completed-scope"></a>
## 3. 本轮已完成

1. 全文读取 R0009 完整派发、正式任务、R0008 管理采用与 continuation。
2. 核 replay manifest、六组执行 receipts、物理 prefix audit、PNV route、时间合同、对象总表和封口哈希。
3. 按每个 symbol／scale 的 `MAX_XCONFIRM_RETURNED_OCCURRENCE` 形成固定 snapshot 状态表，同时明确它只是 rightmost returned batch occurrence，不是 active state 或 lifecycle 结论。
4. 使用固定几何公式派生 high／low proxy，全部标注 `DERIVED_NOT_UPSTREAM_DIRECTION`。
5. 先提交状态表 `c497abf49806a596e34a51a8a35541644ff84215`。
6. 在未读取 future tail 前，冻结 `NO_CANDIDATE`、目标过程、固定指标、反证条件和禁止项，提交 `593641a2d26356ecb86cac8903ff02012cebd66c`。
7. 冻结后核管理指定 bounded tail 的已交付字节；确认 replay 和 recovery slice 均止于 cutoff，原始 source-root 覆盖声明不能替代未运输的 10 月行。
8. 写出不可执行的精确范围、不能推出的内容及唯一最小恢复，不改 T、不调参、不换品种、不做第三次同类来源搜索。
9. 形成业务反馈、部署边界、全部未完、触发观察与一致的两份 Return。

<a id="snapshot-state"></a>
## 4. 固定 query snapshot

完整逐行表：

`c497abf49806a596e34a51a8a35541644ff84215:runs/BI-01-CO-04/artifacts/R0009/QUERY_SNAPSHOT_STATE_TABLE.csv`

### 4.1 rightmost returned occurrence

| symbol | scale | event_ts_native | x | y | xConfirm | yConfirm | `(yConfirm-y)/y` | geometric proxy |
|---|---|---:|---:|---:|---:|---:|---:|---|
| rb | big | 2021-09-24 15:00 | 6928199 | 5695.0 | 7279199 | 5437.0 | -4.530290% | `HIGH_CONFIRMED_PROXY` |
| rb | mid | 2021-09-28 10:30 | 7300799 | 5542.0 | 7345799 | 5527.0 | -0.270660% | `HIGH_CONFIRMED_PROXY` |
| hc | big | 2021-09-24 22:00 | 6928199 | 5946.0 | 7286399 | 5415.0 | -8.930373% | `HIGH_CONFIRMED_PROXY` |
| hc | mid | 2021-09-27 22:00 | 7300799 | 5609.0 | 7327799 | 5598.0 | -0.196113% | `HIGH_CONFIRMED_PROXY` |
| i | big | 2021-09-30 11:00 | 7369199 | 662.0 | 7430399 | 740.0 | +11.782477% | `LOW_CONFIRMED_PROXY` |
| i | mid | 2021-09-30 09:30 | 7399799 | 685.5 | 7421399 | 724.5 | +5.689278% | `LOW_CONFIRMED_PROXY` |

公式：

- `LOW_CONFIRMED_PROXY`：`yConfirm > y`；
- `HIGH_CONFIRMED_PROXY`：`yConfirm < y`；
- `FLAT_OR_UNRESOLVED_PROXY`：相等或任一缺失。

以上 proxy 是几何派生，不是 upstream direction。`event_ts_native`、xConfirm 或 bar time 也都不是本合同的 known time；known time 是六组 query 全部完成。

### 4.2 证据角色

| 层级 | 本轮角色 | 实际结果 | 不能推出 |
|---|---|---|---|
| big | 先过滤可比背景 | rb／hc 同为 high proxy；i 为 low proxy | 不能把 high／low proxy直接写成未来涨跌方向；不能从幅度大小强行排名 |
| mid | 在共同 big 背景中寻找独立差异 | rb／hc 同号且均浅，没有清楚差异 | 不能把 0.07 个百分点左右的 proxy 差硬解释成选择能力 |
| small | 本合同未纳入 | 未使用 | 不能事后补小尺度来救候选或解释尾部 |
| through-T price | anchor／核对 | 仅截至 cutoff | 不能替代 cutoff 后评价 |
| query receipts | operational known-time 与执行证据 | 六组全部完成 | 不能替代特征业务含义 |

### 4.3 为什么不按 big 幅度强行选 hc 或 rb

rb 与 hc 的 big proxy 确认幅度不同，但本题的候选设想是“大尺度用于建立可比背景，中尺度用于形成差异”。若因 hc big 幅度更大就选 hc，等于把背景层改为排序层，并绕过本轮要检验的中尺度独立增量。当前没有预先授权的映射证明“更大的 high-confirmation 幅度”意味着更高相对韧性；这样排名会是事后发明新规则。

<a id="decision-freeze"></a>
## 5. 冻结业务判断

冻结实物：

`593641a2d26356ecb86cac8903ff02012cebd66c:runs/BI-01-CO-04/artifacts/R0009/DECISION_FREEZE.json`

### 5.1 决定

- candidate：`null`
- ranking：`null`
- decision：`NO_CANDIDATE`
- 合格共同背景 pair：rb、hc
- i：因 big proxy 不同而排除在该比较组外

### 5.2 目标后续市场过程

`RELATIVE_RESILIENCE_WITHIN_COMMON_BIG_HIGH_PROXY_PAIR`

如果 snapshot 有合法 mid 差异，本应选出 rb 或 hc 中一个，并在 bounded tail 检查：

- 相对 cutoff 的 close path 是否更高；
- adverse excursion 是否更小；
- terminal return 是否优于另一成员。

本轮 snapshot 没有提供合法选择依据，所以不选成员，但仍冻结评价对象，以检查“无差异”后来是否遭遇明显 ex-post separation。

### 5.3 冻结评价指标与 Case-only 挑战线

- terminal close return；
- minimum close return；
- maximum close return；
- rb-minus-hc normalized close path 与 terminal gap；
- exploratory material separation：terminal gap 绝对值至少 5 percentage points，或 minimum-return 差绝对值至少 5 percentage points。

该 5 个百分点只用于本 Case 的挑战识别，不是一般 Gate，也不能用一个 Case 证明阈值有效。

### 5.4 不能推出

- 不能推出 rb、hc 或 i 的未来方向；
- 不能推出 upstream direction；
- 不能推出 rightmost occurrence 在 cutoff 时仍“active”；
- 不能推出正式 object id、revision 或 lifecycle；
- 不能推出无候选优于随机选择；
- 不能把本次无候选推广为 big＋mid 方法无效。

<a id="future-evaluation"></a>
## 6. 后续评价与自然挑战

完整审计：

`b635b0db1dbd38c2b8a4869cf9bc7e70c379d8a7:runs/BI-01-CO-04/artifacts/R0009/FUTURE_EVALUATION.md`

### 6.1 实际结果

`NOT_EXECUTABLE_FROM_DELIVERED_BYTES`

- replay package 只含每品种 2160 根截至 cutoff 的 PNV；Worker 明确写明未消费 tail；
- prior recovery `DATA_MANIFEST.json` 的 export end-exclusive 为 `2021-10-01 00:00:00`，三品种 exported slice 的 last business time 均为 `2021-09-30 15:00:00`；
- source input last 虽声明为 2024-02-08，但 source-root 不是本执行通道可读、封口的本轮 tail 交付；
- 当前 GitHub 工作面没有指定 10 月 1—15 日行、哈希、行数或 receipt。

因此 terminal／minimum／maximum return、rb-hc path 和 material-separation test 均为 `NOT_COMPUTED`／`NOT_TESTED`。

### 6.2 最近自然挑战的真实状态

不是“没有自然挑战”，而是 `UNKNOWN_INPUT_NOT_DELIVERED`。

不能把未来输入缺失写成：

- 市场支持无候选；
- 市场反证无候选；
- rb 与 hc 没有分化；
- 没有反向对象；
- 该 Case 已完整闭环。

### 6.3 合法替代解释

1. 原始 source-root 很可能实际含该 tail，只是未随授权包运输；这不等于 tail 不存在。
2. 即使后来 rb／hc 明显分化，也不能自动证明 snapshot 应该选其中一个；需要证明该差异在 T 时由允许的 mid 信息可解释。
3. 即使后来没有分化，也只能给本 Case 的保守无候选增加有限支持，不能证明 latest-mid 读法一般有效。
4. rightmost occurrence 可能不是最佳状态摘要；序列关系、对象年龄或此前确认链可能包含信息，但本轮不得在看到未来后新增。
5. event-level observability 缺失不妨碍本次 batch query 业务读法，却限制真实实时部署时的决策时刻与 revision 审计。

<a id="method-feedback"></a>
## 7. 对“大尺度背景＋中尺度差异”设想的反馈

### 7.1 是否形成独立业务增量

**本 Case 截至 snapshot 没有形成正向选择增量，但形成了一项可审计的负向增量：合法无候选。**

- big 的确完成了背景分组：rb／hc 可比，i 不可比；
- mid 没有把 rb 与 hc 分开；
- 因而“mid 提供独立选择信息”在这个 cutoff 未观察到，而不是被普遍反证。

### 7.2 哪些来自特征，哪些只是组织改善

来自特征的内容：

- big／mid returned occurrence 的 y 与 yConfirm 几何关系；
- rb／hc 同背景、i 异背景；
- rb／hc mid 没有清楚差异。

来自组织／可追溯性改善的内容：

- fixed prefix；
- 六组 query completion known-time；
- source key、replay key、hash 和先冻结提交；
- 将“不选”与“缺数据”分离。

后者提高可信度，但不等于增加预测能力。

### 7.3 event-level observability 缺失对部署意味着什么

当前低成本入口可用于**离线、批次、query-completion 后**的探索决策；不能直接声称为历史实时或生产增量信号。若部署为真实连续决策，至少还需二选一：

1. 明确按固定批次完成时点重新计算并把它当正式业务时钟，同时定义对象替换和重复判断规则；或
2. 增加同一引擎的 event-level observer／first-seen／revision／withdrawal 合同。

在此之前，无法回答对象首次何时可见、曾否撤回、重复出现是否同一对象，也无法精确审计实时持有状态。

### 7.4 是否值得继续使用该低成本入口

**条件性保留。**

保留理由：

- 能在不扩全市场、不使用最终图倒填的情况下形成清楚的可比组；
- 能给出合法无候选，而不是强制排名；
- 成本低，审计链已明显改善。

限制：

- 尚无一次完成的 held-out outcome；
- geometric proxy 不是 upstream direction；
- latest occurrence 是否是有效状态摘要未知；
- event-level 部署语义不完整。

因此当前只值得继续完成这个 bounded tail，并在其后做一个相邻、预先声明 cutoff 的 Case；不值得固化成 Gate、评分器或专用 Agent。

### 7.5 下一相邻 Case

当前 Case 闭合之后，最有价值的相邻 Case不是换全市场，而是：

- 仍用同一 symbols／frequency／big-mid 参数；
- 在看后续前预先选一个 big 背景相同、mid proxy 真正异号或差异清楚的 cutoff；
- 先冻结选择，再用等长 held-out tail 检验相对韧性；
- 与本次无候选 Case 成对比较。

该相邻 Case 只能在本次 tail 闭合后启动，不能用 10 月结果倒选窗口。

<a id="minimum-recovery"></a>
## 8. 唯一最小恢复

无需再次重算特征，也不需要第三次来源搜索。只需运输与 frozen source/version 一致的：

- rb、hc、i；
- 30m；
- `(2021-09-30 15:00:00, 2021-10-15 15:00:00] Asia/Shanghai`；
- 至少 business timestamp 与 close；
- 每文件 sha256、字节数、行数、首末 timestamp、时区／交易日／夜盘映射、source snapshot/version；
- 若不是原字节截取，附转换步骤及其 hash。

收到后只执行冻结指标，不得重开 snapshot、改阈值、补候选或重新定义目标过程。

<a id="materials-use"></a>
## 9. 材料使用

完整索引：

`e96ad6191ae766372f2874899898473754cbfc6a:runs/BI-01-CO-04/artifacts/R0009/EVIDENCE_INDEX.md`

本轮实际使用：

- R0009 完整派发与现行 Binding；
- R0008 管理决定和 Professional continuation；
- 既有专业目标、能力、工作设想、工具／数据、历史边界、Owner 过程与 Run guide；
- replay package 的 manifest、对象总表、执行 receipts、prefix audit、route receipt、observer assessment、time contract 和 hashes；
- prior recovery manifest 与 formal slice 的时间覆盖；
- 本轮先冻结的状态表和决定文件。

未使用：

- cutoff 后外部行情；
- 局域网页面最终路径；
- 未提供的小尺度；
- 另一窗口、另一参数或全市场扫描；
- Worker 对业务候选的任何替代判断；
- 未签发的第三次工单。

<a id="remaining-scope"></a>
## 10. 全部未完

1. 取得第 8 节 bounded tail 三品种 30m 字节及 receipt。
2. 按冻结指标计算 rb／hc terminal、minimum、maximum return 与标准化路径。
3. 判定是否达到 Case-only material separation。
4. 找最近可定位的状态改变、反向对象、失败候选或无法判定区间。
5. 区分对 frozen no-candidate 的有限支持、反例、噪声或仍不可判定。
6. 完成 `FIRST_USABLE_ASOF_LOOP` 的自然挑战和方法反馈闭环。
7. 由管理决定：运输唯一有界 tail 后继续同一 Case，或在 effort review 下停止／改范围。
8. 只有当前 Case 闭合后，才考虑第 7.5 节相邻 Case。

<a id="next-question"></a>
## 11. 唯一推荐下一专业问题

> 在保持 `593641a2d26356ecb86cac8903ff02012cebd66c` 冻结的 `NO_CANDIDATE`、目标过程和全部评价指标不变时，rb 与 hc 在 `(2021-09-30 15:00, 2021-10-15 15:00]` 的 terminal return、minimum return 与标准化 close path 是否出现预定义 material separation；若出现，它是否构成“latest mid occurrence 不足以捕捉相对韧性”的反例，若未出现，它对本 Case 的保守无候选判断提供多大支持？

<a id="trigger-observations"></a>
## 12. 触发观察

### `FIRST_USABLE_ASOF_LOOP = NOT_YET`

已满足：

- 固定 query snapshot；
- 明确候选／排序／无候选；
- 判断先于 future evaluation 冻结；
- 目标过程、反证条件和不能推出内容。

未满足：

- bounded-tail 后续评价；
- 最近市场自然挑战；
- 基于实际 held-out outcome 的方法裁定。

### `ACTIVE_WORK_EFFORT_REVIEW = SATISFIED`

- R0005 为第 1 次有效 Professional 调用；
- R0009 为第 2 次；
- 任务仍 ACTIVE，但未完已缩到一个有界、可运输、无需重算特征的 tail 输入。

按正式 trigger 应回 management `decide`，由其选择运输或停止／重定范围。

### `MATERIAL_INPUT_OR_METHOD_CHANGE = NOT_YET`

- R0008 采用的 query-completion 合同已被本轮直接使用；
- 没有发现其参数、二进制、source identity 或几何 proxy 定义发生新冲突；
- tail 未运输是承重未完，不据此虚构新方法变化。

<a id="continuation"></a>
## 13. 接续

当前任务、问题、T、snapshot、决定与评价计划全部保持不变。管理若决定继续，只需把第 8 节有界 tail 作为新输入运输到同一 Run 可读工作面；下一 Professional 必须从冻结提交继续，不重读未来后重新选择。

若管理决定停止当前 Case，应明确记录：已经取得一个可审计 snapshot `NO_CANDIDATE`，但没有 held-out outcome，不能计为首个完整可消费 as-of loop，也不能把本次结果用作方法有效或无效的证据。

<a id="handoff"></a>
## 14. 回交路线

`route = decide`

接收方：`chatgpt:BI-01-CO-04:management`。

管理需决定的唯一事项：

- 是否运输第 8 节有界 tail，完成同一 frozen Case；或
- 因 effort review 停止／改范围，并保留 snapshot 冻结结果及其未验证状态。

本回交不请求管理重判 replay 技术合同，不请求第三次来源搜索，不请求改 T、调参或扩全市场。

<a id="self-check"></a>
## 15. 自查

- [x] 使用管理已采用的 `QUERY_COMPLETION_ASOF_V1`，未偷换为 event-level first-seen。
- [x] proxy 全部标注 `DERIVED_NOT_UPSTREAM_DIRECTION`。
- [x] rightmost occurrence 未冒充 active object 或 lifecycle。
- [x] snapshot 表先提交，决定单独冻结，再查 future tail。
- [x] 未在看到未来后改候选、T、参数、阈值、symbols 或目标过程。
- [x] 无候选来自 snapshot，而不是数据缺失。
- [x] cutoff 后评价不可执行已与冻结业务判断分离。
- [x] 未使用外部或未封口 tail 代替正式输入。
- [x] 未把 source-root 覆盖声明写成已消费字节。
- [x] 明确 big、mid、small、price、receipt 的证据角色。
- [x] 回答独立业务增量、组织增量、部署限制、低成本入口和相邻 Case。
- [x] 列出全部未完、材料使用、唯一下一问题与三项 trigger。
