continuation_id: BI01-CO-04-PROFESSIONAL-CONTINUATION-QUERY-ASOF-01
work_id: BI-01
run_id: BI-01-CO-04
role: professional
professional_mode: CASE_OBSERVATION
recipient_ref: chatgpt:BI-01-CO-04:professional
issued_by: chatgpt:BI-01-CO-04:management
issued_from_invocation: BI01-CO-04-R0008-REPLAY-INTAKE-82bb0b60
status: ISSUED_NOT_SENT

# BI-01-CO-04｜同一业务问题的 query-completion as-of continuation

<a id="continuation-purpose"></a>
## 1. 继续目的

继续当前正式任务 `BI-01-CO-04-CASE-INITIAL-ASOF` 与问题 `CASE-FIRST-ASOF-CROSS-SYMBOL-SELECTION`，直接形成首个可管理消费的业务循环。

R0005 已完成输入资格边界；R0007／R0008 已完成旧 run、恢复包和 replay 的技术裁定。本轮不得再做来源搜索、event-level first-seen 证明、第三次 Worker 请求或重复解释缺文件。你要消费现有冻结 prefix query 结果，形成明确的跨品种业务判断、未来评价和方法反馈。

<a id="continuation-authority"></a>
## 2. 管理采用与输入合同

- 原任务：`runs/BI-01-CO-04/01_当前任务.md`
- 管理采用：`c286238462c07f15d9ebfe3cac06edc6a2da29d4:runs/BI-01-CO-04/reviews/management-R0008/DECISION.md::#professional-release`
- operational contract：`QUERY_COMPLETION_ASOF_V1`
- replay package：`e25e585779152aa670d54c87efecba984af4b7e3:runs/BI-01-CO-04/artifacts/worker-BI01CO04-ASOF-VISIBILITY-REPLAY-01/`
- prior recovery baseline：`dfdf843b47c03c0121fd7151b72f24adb5d986c0:runs/BI-01-CO-04/artifacts/worker-BI01CO04-INPUT-RECOVERY-01/`

`QUERY_COMPLETION_ASOF_V1` 的含义：只把截至 cutoff T 的物理行情前缀送入冻结 batch 引擎；查询完成后返回的 big／mid 对象集合与截至 T 行情，是本次决策可用信息。它不声称旧系统在历史当时逐对象实时发布，也不赋予 event-level first-seen 或 revision 生命周期。

<a id="fixed-decision"></a>
## 3. 已预先锁定的决策条件

以下条件不得因未来走势或对象形态改变：

- symbols：rb、hc、i
- frequency：30m
- scales：big、mid
- `T_bar_cutoff`：`2021-09-30 15:00:00 Asia/Shanghai`
- `T_decision`：六组 frozen-prefix query 全部完成后
- future evaluation：`2021-09-30 15:00:00` 之后至 `2021-10-15 15:00:00 Asia/Shanghai`
- parameters／binary／entrypoint：以 replay manifest 和 source snapshot 冻结字节为准

不得改 T、补看 10 月走势后换候选、调参、换品种或扩展全市场。若 snapshot 不能支持可比状态，交“固定 query snapshot 下无可比候选”，不要另找窗口。

<a id="state-semantics"></a>
## 4. 状态语义

### 4.1 允许使用

- replay batch 返回的 big／mid 对象行；
- actual coordinates／price、confirm coordinates／price、event_ts、source key、replay-local occurrence key；
- 截至 T 的正式 30m 行情；
- frozen query receipt、input prefix hash、执行结果与 baseline comparison；
- 由固定公式得到的 `derived_geometric_turn_type`：
  - `LOW_CONFIRMED_PROXY`：`yConfirm > y`
  - `HIGH_CONFIRMED_PROXY`：`yConfirm < y`
  - `FLAT_OR_UNRESOLVED_PROXY`：相等或缺失

### 4.2 必须标注

- geometric proxy 必须标注 `DERIVED_NOT_UPSTREAM_DIRECTION`；
- query completion 是本轮 operational known time，不是旧生产 publish time；
- replay-local occurrence key 不是正式 object id；
- final batch snapshot 不证明对象在 prefix 内的首次出现、撤回或重现。

### 4.3 禁止

- 把 `event_ts`、`xConfirm`、bar time 或 calendar alternate 单独写成原生 known time；
- 把几何 proxy 写成正式 direction；
- 从最终对象行推断历史 revision 生命周期；
- 用技术 validator PASS 代替业务判断。

<a id="required-analysis"></a>
## 5. 必做业务分析

### 5.1 固定 snapshot 状态表

对 rb／hc／i 分别列出：

- 截至 T 返回的最近 big 对象及几何 proxy；
- 截至 T 返回的最近 mid 对象及几何 proxy；
- object actual／confirm 坐标与价格；
- query receipt／source key；
- 大尺度背景是否可比；
- 中尺度是否存在清楚差异；
- 哪些字段只是视觉／派生证据。

### 5.2 先冻结判断

在读取 future evaluation 前，明确写出并封存：

1. 候选、排序或无候选；
2. 目标后续市场过程；
3. 判断依据中 big、mid 各自承担的角色；
4. 反证条件；
5. 不能推出的内容。

若三品种没有至少两个可比较 big 背景，或 mid 差异不能合法解释，给出无候选。无候选必须是 snapshot 的业务结论，不是数据缺失。

### 5.3 后续评价与自然挑战

判断冻结后，再读取 bounded tail：

- 检查候选相对表现是否符合预先定义过程；
- 找最近的反向对象、失败候选、状态改变或无法判定区间；
- 区分支持、反证、等待、噪声与输入限制；
- 不因结果不佳改 T、规则或目标。

### 5.4 方法反馈

必须回答：

- 在 query-completion workflow 下，“大尺度背景＋中尺度差异”是否形成独立业务增量；
- 哪部分增量来自特征，哪部分只是把信息组织得更清楚；
- event-level observability 缺失对真实部署意味着什么；
- 下一轮最值得验证的相邻 Case 是什么；
- 当前是否值得继续使用该低成本入口。

<a id="deliverables"></a>
## 6. 必交付

写入新的 Professional R artifacts 目录，至少包含：

1. `REPORT.md`：完整业务循环；
2. `QUERY_SNAPSHOT_STATE_TABLE.csv` 或等价结构化表；
3. `DECISION_FREEZE.json`：T、候选／无候选、目标过程、反证条件、freeze time、使用实物 hash；
4. `FUTURE_EVALUATION.md` 或等价；
5. `EVIDENCE_INDEX.md`；
6. `ROLE_RETURN.json` 与 `QUESTION_WORK_RETURN.json`；
7. 材料使用、全部未完、触发观察和下一专业问题。

所有引用必须定位到真实 commit／path／blob 或行；不得只写“已看图”。

<a id="completion"></a>
## 7. 完成与停止条件

本次是第二次有效 Professional 调用。只有以下之一成立才可结束：

### A. `FIRST_USABLE_ASOF_LOOP=SATISFIED`

固定 query snapshot 已产生候选／排序／市场无候选，判断先于 future evaluation 冻结，并完成最近自然挑战、替代解释和方法反馈。

### B. `ACTIVE_WORK_EFFORT_REVIEW=SATISFIED`

即使使用本轮已授权 operational contract，仍不能形成业务主体。必须精确说明是 snapshot 无可比状态、语义仍不足，还是业务目标本身不适配；不得再请求同类技术搜索。回管理作范围／目标取舍。

若发现新的承重输入或方法冲突，同时报告 `MATERIAL_INPUT_OR_METHOD_CHANGE=SATISFIED`。普通分析困难不构成第三次来源循环。

<a id="handoff"></a>
## 8. 回交

结果回 `chatgpt:BI-01-CO-04:management`。不要自行签独立审查、修改地图／Intake、扩张到全市场或宣布 Owner 接受。管理将按真实业务证据决定接收、独立专业审查和下一 Case。
