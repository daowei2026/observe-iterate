order_id: BI01CO04-INPUT-RECOVERY-01
work_id: BI-01
run_id: BI-01-CO-04
issuer_role: management
issuer_ref: chatgpt:BI-01-CO-04:management
issuer_invocation_id: BI01-CO-04-R0006-PROFESSIONAL-INTAKE-6fd91174
issuer_assignment_token: 43645083c9663b83a73077ab4c48cb4815b3221177edc89b
return_to: chatgpt:BI-01-CO-04:management
recipient_thread_id: 01a17dd7-5033-7e63-b7a2-edd90b691c33
expected_workspace: /dwdhome/fy/cgpterm
status: ISSUED_NOT_SENT

# BI-01-CO-04｜最小正式输入恢复工单

<a id="worker-purpose"></a>
## 1. 技术目的

为当前正式专业任务 `BI-01-CO-04-CASE-INITIAL-ASOF` 恢复一个最小、不可变、可追溯的数据包，使 Professional 能够在不使用未来信息的条件下继续同一 `CASE-FIRST-ASOF-CROSS-SYMBOL-SELECTION` 问题。

本工单只做正式实例定位、字节复制、必要的同配置窄范围重生、字段／时间语义整理、静态导出和 receipt。Worker 不选择 T，不比较 rb／hc／i 强弱，不判断候选、无候选、方法有效性或管理 Gate。

<a id="worker-authority"></a>
## 2. 授权与现场

- Owner 指定 Worker thread：`01a17dd7-5033-7e63-b7a2-edd90b691c33`
- 预期聊天工作区：`/dwdhome/fy/cgpterm`
- 专业及运行仓：`daowei2026/observe-iterate`
- 分支：`fy/feature-based-case-observation`
- 技术来源候选：
  - run：`GTQH_C001_three_turns_20261101_162005`
  - 本地根：`/dwdhome/fy/BASE_E6_2/.../storage_migration_20261101`
  - 行情源：`/m3varF/BaseData/futures/GTQH_L1_20210104_20240208`
  - 页面：`http://192.168.11.40:5006/cae?node_id=6153`
  - 参数文件名：`selected_turn_parameters.json`
  - 品种：`rb`、`hc`、`i`
  - K 线频率：`30m`
  - 历史观察窗口：`2021-08-15` 至 `2021-09-30`

这些仅为定位入口。Worker 必须以现场真实文件、run manifest、配置消费记录和数据内容为准；不得因名称相似自行认定同一实例。

<a id="worker-required-reads"></a>
## 3. 必须先读

1. `runs/BI-01-CO-04/artifacts/R0005/REPORT.md`
2. `runs/BI-01-CO-04/artifacts/R0005/EVIDENCE_INDEX.md`
3. `runs/BI-01-CO-04/artifacts/R0005/INPUT_QUALIFICATION.json`
4. `runs/BI-01-CO-04/reviews/management-R0006/DECISION.md`
5. `professional/exploration/03_TOOLING_AND_DATA_USAGE.md`
6. `professional/exploration/tooling_examples/2026-11-01_30m_multi_symbol_turn_chart.md`

只读取完成本工单所需的源码、配置、manifest、日志、数据和现有导出。禁止无明确需要递归读取旧 runs、全仓历史、无关模型或全部 Worker 聊天历史。

<a id="worker-output"></a>
## 4. 唯一输出位置

全部新实物写入：

`runs/BI-01-CO-04/artifacts/worker-BI01CO04-INPUT-RECOVERY-01/`

至少包含：

- `FULL_RESPONSE.md`
- `PACKAGE_RECEIPT.json`
- `DATA_MANIFEST.json`
- `FIELD_DICTIONARY.md`
- `SOURCE_AND_REPRODUCTION.md`
- 正式行情切片文件
- 正式大／中尺度特征对象切片文件
- 参数／配置及 run 消费证明
- 可取得时的静态图面导出
- 发生阻断时的 `BLOCKER_REPORT.md`

不得修改 `README.md`、`00_长程推进地图.md`、`01_当前任务.md`、`WORKMAP_INTAKE_CURRENT.json`、任何管理决定或 R0005 专业报告。

<a id="worker-p0"></a>
## 5. P0 必须恢复

### 5.1 正式实例身份

交 run／board／文件索引或等价 manifest，至少含：

- run id、core／build／代码版本；
- 数据源根、输出根、品种、K 线频率、请求窗口；
- 实际 warm-up 起止和实际输出覆盖；
- 每个交付文件的来源路径、目标路径、SHA-256、bytes；
- copied／regenerated 标记；
- 当前读取到的完成、缺失、失败或部分状态。

### 5.2 实际参数与消费证明

复制 `selected_turn_parameters.json` 的真实字节或等价正式配置，并交证明该 run 实际消费它的日志、manifest、命令、配置快照或代码版本关系。不得只抄文档参数或默认值。

### 5.3 正式 30m 行情切片

为 rb／hc／i 交正式 K 线切片，覆盖：

- 该 run 实际需要的 warm-up；
- `2021-08-15` 至 `2021-09-30` 完整观察窗口；
- 若正式 run 输出可核且成本低，继续到足以检查窗口内最近自然挑战的末端，但不得扩大成全历史或全市场复制。

每行至少保留 symbol、business timestamp、open、high、low、close、volume／open interest（若源正式提供）、source key。记录交易所日历、时区、session、夜盘归属和首末业务时间。

### 5.4 大／中尺度对象切片

为 rb／hc／i 交本 run 的大尺度与中尺度正式对象行。每个对象至少保留：

- scale、symbol、object id／source key；
- direction 或可追溯的上游 zig 方向映射；
- actual turn time／position（如 `x/y`）；
- confirm／known time／position（如 `xConfirm/yConfirm`）；
- `event_ts` 及其边界含义；
- revision／version、current status、line／segment 关系（正式存在时）；
- missing、calculation failure、no-signal 的可区分状态。

小尺度当前不必补，除非它是确认上述对象身份／方向所必需；若补，单独说明必要性。

### 5.5 语义字典

交字段词典，明确：

- actual time 与 confirm／publish／known time；
- direction 与 zig 的来源关系；
- revision、撤回、更新和当前状态；
- `event_ts`、UTI、bar timestamp 和交易日边界；
- 缺失、计算失败、未运行、真实无信号的区别。

### 5.6 Receipt

`PACKAGE_RECEIPT.json` 对每个文件记录：

- path、source_path；
- sha256、bytes；
- rows（适用时）；
- first_business_time、last_business_time（适用时）；
- generated_at；
- tool／version；
- copied／regenerated；
- source_run_id；
- verification_status。

Receipt 须能由独立消费者逐文件复核，不得用目录名或一个总说明代替。

<a id="worker-p1"></a>
## 6. P1 图面辅助

尝试导出 node 6153 或同一正式 run 的静态 PNG／PDF／HTML，并记录它与 run、品种、频率、窗口和参数的对应证明。页面无法访问时如实记录；结构化 P0 完整则不因图面缺失停止交付。图面绝不能替代行情／对象字节或确认时间字段。

<a id="worker-reproduction"></a>
## 7. 复制与窄范围重生规则

1. 优先复制现有正式产物，不重算。
2. 若正式切片缺失，但 exact 代码版本、配置、源数据和命令均可核，允许只对 rb／hc／i、30m 和上述窗口执行一次同配置窄范围重生。
3. regenerated 文件必须与 copied 文件分目录或在 receipt 中逐文件明确，保存命令、环境、版本、日志和差异说明。
4. 禁止调参数追求预期图形，禁止改业务算法，禁止用新默认值替代旧运行，禁止全市场／全历史重算。
5. exact 条件不成立时不要猜测；交 `BLOCKER_REPORT.md`，列出已查位置、具体缺件、受阻 P0 项、最小恢复条件和仍已取得的真实实物。

<a id="worker-checks"></a>
## 8. 最低自查

- 三个品种和 30m 频率逐一核对；
- manifest、参数、行情、特征对象之间 run／版本／窗口一致；
- 每个正式对象可追到 actual 与 known／confirm 时间；
- 行情和特征覆盖能支持后续选择首个合法 T，而不是只有最终结果截图；
- 每个 receipt hash 对目标文件重新计算；
- 行数、首末时间和缺失状态与文件内容一致；
- 没有把 Worker 的技术判断写成市场结论。

<a id="worker-return"></a>
## 9. 回交

完整结果回 `chatgpt:BI-01-CO-04:management`，并在 `FULL_RESPONSE.md` 明确：

1. P0 各项 `SATISFIED`／`PARTIAL`／`BLOCKED`；
2. copied 与 regenerated 的准确范围；
3. 实际命令、版本、输入、输出和校验；
4. 全部未完及是否足以交回 Professional；
5. GitHub commit 与输出位置。

Worker 不更新管理 Intake，不续发 Professional，不宣告 as-of 循环或业务 Gate 通过。管理只先接技术包；之后由原 Professional 消费并形成业务判断。
