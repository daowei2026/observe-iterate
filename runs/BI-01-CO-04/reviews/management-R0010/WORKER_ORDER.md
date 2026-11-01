order_id: BI01CO04-FROZEN-TAIL-TRANSPORT-01
work_id: BI-01
run_id: BI-01-CO-04
issuer_role: management
issuer_ref: chatgpt:BI-01-CO-04:management
issuer_invocation_id: BI01-CO-04-R0010-EFFORT-REASSESS-cad9dec8
issuer_assignment_token: f39e59c7341d2d123bc0154738924760204bc2d6766fd5d5
return_to: chatgpt:BI-01-CO-04:management
continuation_thread_id: 01a19881-cebf-73f3-a4d3-76c57bce0fe4
owner_authorized_original_thread_id: 01a17dd7-5033-7e63-b7a2-edd90b691c33
expected_workspace: /dwdhome/fy/cgpterm
status: ISSUED_NOT_SENT

# BI-01-CO-04｜冻结 Case 的 held-out 行情尾部运输工单

<a id="worker-purpose"></a>
## 1. 唯一技术目的

把 R0009 已经预先冻结、但尚未进入 GitHub 工作面的 held-out 30m 行情尾部，从**已经核实的同一 GTQH source snapshot**精确截取、封口并提交，使原 Professional 能套用既定指标闭合当前 Case。

本工单不是第三次 feature／known-time／visibility 研究，也不是新 Case。禁止重算特征、运行 big／mid 引擎、搜索替代数据源、改 cutoff、改品种、改频率、改阈值或作市场解释。

<a id="worker-authority"></a>
## 2. 授权与准确依赖

- 管理决定：`daowei2026/observe-iterate@c8c6f05442f4e2111528cb3ac7c925dfba60e9a2:runs/BI-01-CO-04/reviews/management-R0010/DECISION.md::#tail-order`
- 冻结决定：`daowei2026/observe-iterate@593641a2d26356ecb86cac8903ff02012cebd66c:runs/BI-01-CO-04/artifacts/R0009/DECISION_FREEZE.json::full`
- 专业评价缺口：`daowei2026/observe-iterate@b635b0db1dbd38c2b8a4869cf9bc7e70c379d8a7:runs/BI-01-CO-04/artifacts/R0009/FUTURE_EVALUATION.md::#minimum-recovery`
- 已核 source manifest：`daowei2026/observe-iterate@dfdf843b47c03c0121fd7151b72f24adb5d986c0:runs/BI-01-CO-04/artifacts/worker-BI01CO04-INPUT-RECOVERY-01/DATA_MANIFEST.json::full`
- 已核来源／复现：`daowei2026/observe-iterate@dfdf843b47c03c0121fd7151b72f24adb5d986c0:runs/BI-01-CO-04/artifacts/worker-BI01CO04-INPUT-RECOVERY-01/SOURCE_AND_REPRODUCTION.md::full`
- source data root：`/m3varF/BaseData/futures/GTQH_L1_20210104_20240208`
- 原 recovery source root：`/dwdhome/fy/BASE_E6_2/mquant/aidata/test_runs/fy_owner_1d_30m_20261027/storage_migration_20261101`
- source run：`GTQH_C001_three_turns_20261101_162005`

使用既有实际 Worker thread `01a19881-cebf-73f3-a4d3-76c57bce0fe4` 与 workspace `/dwdhome/fy/cgpterm`。若该现场不能读取上述已核 source，按本单出口 B 停止；不得切换第三方、公开网页、另一连续合约口径或新数据库。

<a id="worker-required-reads"></a>
## 3. 必须先读

1. `runs/BI-01-CO-04/reviews/management-R0010/DECISION.md`
2. `runs/BI-01-CO-04/artifacts/R0009/DECISION_FREEZE.json`
3. `runs/BI-01-CO-04/artifacts/R0009/FUTURE_EVALUATION.md`
4. `runs/BI-01-CO-04/artifacts/R0009/QUERY_SNAPSHOT_STATE_TABLE.csv`
5. prior recovery 的 `DATA_MANIFEST.json`
6. prior recovery 的 `SOURCE_AND_REPRODUCTION.md`
7. prior recovery 的 `PACKAGE_RECEIPT.json` 中三品种行情来源项
8. replay package 的 `SOURCE_SNAPSHOT.json`、`TIME_CONTRACT.md` 与 frozen prefix 行情 receipt

只读取完成 exact extraction、identity matching 和 receipt 所需的文件。不得递归重审旧 runs 或业务报告。

<a id="worker-output"></a>
## 4. 唯一输出位置

全部新实物写入：

`runs/BI-01-CO-04/artifacts/worker-BI01CO04-FROZEN-TAIL-TRANSPORT-01/`

至少包含：

- `FULL_RESPONSE.md`
- `TAIL_MANIFEST.json`
- `TAIL_PACKAGE_RECEIPT.json`
- `TAIL_MECHANICAL_METRICS.json`
- `SOURCE_IDENTITY_CHECK.json`
- `TIME_AND_CALENDAR_CONTRACT.md`
- `rb_30m_tail.csv`
- `hc_30m_tail.csv`
- `i_30m_tail.csv`
- extraction script、命令、stdout／stderr、validator
- `SHA256SUMS`
- 出口 B 时的 `BLOCKER_REPORT.md`

不得修改 R0009 冻结文件、当前业务任务、地图、Intake、Adoption Status 或任何历史管理决定。

<a id="fixed-scope"></a>
## 5. 固定数据范围

### 5.1 品种与频率

- symbols：`rb`、`hc`、`i`
- frequency：`30m`
- timezone：`Asia/Shanghai`，或源真实时区；若源不是该时区，必须保留原字段并给无歧义转换

### 5.2 时间范围

每个文件必须包含：

- 一行 cutoff anchor：`2021-09-30 15:00:00`，标记 `row_role=CUTOFF_ANCHOR`；
- held-out evaluation rows：`(2021-09-30 15:00:00, 2021-10-15 15:00:00]`，标记 `row_role=EVALUATION_TAIL`。

不得包含 `2021-10-15 15:00:00` 之后的行。若源在终点没有 exact 15:00 行，不得自行用更早／更晚行替代；如实标记 `ENDPOINT_MISSING` 并走出口 B，除非 R0009 冻结合同中的 exact endpoint 已由源交易日规则明确等价。

### 5.3 必保留字段

至少：

- symbol
- business timestamp
- close
- source row／source key
- contract／continuous-series／adjustment 标识（源存在时）
- trading day、session／night-session attribution（源存在时）
- `row_role`

OHLC、volume、open interest 可保留但不是承重要求。不得从其他口径补列。

<a id="source-identity"></a>
## 6. 来源身份核对

每个 symbol 必须证明：

1. anchor row 与 replay／prior recovery 的 cutoff close、UTI／timestamp 和 source identity一致；
2. tail 来自 prior manifest 已声明覆盖到 2024-02-08 的同一 source input，不是另一主力、复权或连续化口径；
3. 提取前后源文件 hash／identity、读取路径、行选择规则和输出 hash 可追溯；
4. 如果源文件过大而不做全文件 hash，使用既有已核 source identity 加上本次精确 source path、文件 stat、局部行 hash／range proof，并解释边界；不得虚写完整 hash；
5. 三品种 timestamp 集合是否一致必须报告；不一致时保留真实交集和差异，不做插值。

<a id="mechanical-metrics"></a>
## 7. 机械指标

Worker 可以机械计算，但不得解释支持／反证：

对 symbol `s`，令 cutoff anchor close 为 `C_s(T)`；对尾部每个真实 timestamp `t`：

`r_s(t) = close_s(t) / C_s(T) - 1`

必须输出：

- `terminal_return_s`：exact `2021-10-15 15:00` 的 `r_s(t)`；
- `minimum_tail_return_s`：严格在 `(T, T_end]` 的最小 `r_s(t)`；
- `maximum_tail_return_s`：严格在 `(T, T_end]` 的最大 `r_s(t)`；
- exact common timestamps 上的 `rb_minus_hc_path = r_rb(t) - r_hc(t)`；
- `terminal_gap = terminal_return_rb - terminal_return_hc`；
- `minimum_return_difference = minimum_tail_return_rb - minimum_tail_return_hc`；
- frozen Case-only test：
  - `abs(terminal_gap) >= 0.05`，或
  - `abs(minimum_return_difference) >= 0.05`。

输出 test 的布尔值及原始数值，不写“支持无候选”“反证方法”或任何候选结论。i 指标只作诊断，不进入 rb／hc 同背景 material-separation test。

所有公式和 endpoint 必须与 `DECISION_FREEZE.json` 一致；不得在看到数值后修改。

<a id="receipt-and-validation"></a>
## 8. Receipt 与最低验证

`TAIL_PACKAGE_RECEIPT.json` 对每个交付文件记录：

- path、source_path
- sha256、bytes、rows
- first／last timestamp
- anchor close、tail first／last close（适用时）
- timezone、trading-day／night-session convention
- source snapshot／version、extraction command、tool version
- copied／deterministically_extracted
- verification status

Validator 至少检查：

1. 只有三品种、30m、固定 anchor＋tail；
2. anchor 唯一且与 prior frozen prefix 一致；
3. 尾部严格不含 cutoff 及 end 后行；
4. timestamp 单调、close 非空且数值合法；
5. 三文件 identity／calendar 口径一致或差异显式报告；
6. receipt hash、bytes、rows、首末时间与文件一致；
7. 机械指标可从 CSV 独立重算且逐值一致；
8. extraction script 不运行 feature engine，不读取替代数据源，不修改冻结实物。

<a id="legal-exits"></a>
## 9. 两个合法出口

### A. `TAIL_PACKAGE_READY`

只有三品种 anchor＋完整 tail、identity、receipt、validator 和机械指标全部满足，才可给出。该出口只表示可交管理技术接收，不表示业务 loop 完成。

### B. `TAIL_SOURCE_INACCESSIBLE`

source 不可读、identity 不匹配、anchor 对不上、exact endpoint 缺失、calendar／continuous-series 口径无法与 frozen prefix 对齐，或不能在不换源的条件下完整截取时给出。`BLOCKER_REPORT.md` 必须列已查 exact path、命令、真实错误、受影响 symbol／range 和仍可保留的实物。

不得给第三种“基本可用／部分可用”出口；不得转向公开行情、其他数据商、另一连续合约、插值或人工补点。

<a id="stop-rules"></a>
## 10. 停止规则

- 本单只允许一次确定性提取与必要的同脚本修正；
- 不允许 feature 重算、参数调整、窗口选择、对象分析或业务判断；
- 不允许继续搜索旧聊天、另找数据库、扩时间或扩品种；
- 出口 B 后停止，管理将终止当前 Case 的 outcome 验证；
- 不更新 Intake，不续发 Professional，不宣布 `FIRST_USABLE_ASOF_LOOP`。

<a id="worker-return"></a>
## 11. 回交

结果回 `chatgpt:BI-01-CO-04:management`。`FULL_RESPONSE.md` 必须明确：

1. 最终出口 A 或 B；
2. source identity、实际命令、输入、输出与校验；
3. 三品种行数、首末 timestamp、anchor、tail endpoint；
4. receipt／validator 状态；
5. 机械指标已算或为何不能算；
6. 全部未完、GitHub commit 与唯一输出路径。

Worker 不形成市场候选／排序／无候选，不解释 material separation，不修改冻结判断或管理状态。
