# BI-01-CO-04 R0009｜冻结判断后的 bounded-tail 评价

- `work_id`: `BI-01`
- `run_id`: `BI-01-CO-04`
- `round_id`: `R0009`
- `invocation_id`: `BI01-CO-04-R0009-PROFESSIONAL-QUERY-ASOF-8d6fcf14`
- `contract`: `QUERY_COMPLETION_ASOF_V1`
- `freeze_commit`: `593641a2d26356ecb86cac8903ff02012cebd66c`
- `freeze_decision`: `NO_CANDIDATE`
- `future_evaluation_status`: `NOT_EXECUTABLE_FROM_DELIVERED_BYTES`

<a id="sequence-proof"></a>
## 1. 先冻结、后开启 future evaluation

本轮严格按管理合同执行了顺序隔离：

1. 只读取截至 `2021-09-30 15:00:00 Asia/Shanghai` 的 frozen-prefix query 输出；
2. 将六组 rightmost returned occurrence 写入 `QUERY_SNAPSHOT_STATE_TABLE.csv`，提交为 `c497abf49806a596e34a51a8a35541644ff84215`；
3. 在未读取任何 cutoff 后行情字节的情况下，将 `NO_CANDIDATE`、目标过程、反证条件和固定评价指标写入 `DECISION_FREEZE.json`，提交为 `593641a2d26356ecb86cac8903ff02012cebd66c`；
4. 冻结之后才开始查找管理指定的 `2021-09-30 15:00` 之后至 `2021-10-15 15:00 Asia/Shanghai` bounded tail。

冻结决定没有因后续输入可得性而改写。当前文件也不修改、替换或补充 `DECISION_FREEZE.json` 中的判断。

<a id="frozen-evaluation-plan"></a>
## 2. 冻结时已经确定的评价对象与指标

### 2.1 目标过程

`RELATIVE_RESILIENCE_WITHIN_COMMON_BIG_HIGH_PROXY_PAIR`

- eligible pair：`rb`、`hc`
- `i` 仅作诊断，不进入同背景相对选择，因为其大尺度为 `LOW_CONFIRMED_PROXY`，而 rb／hc 为 `HIGH_CONFIRMED_PROXY`。
- 冻结结论为无候选：rb／hc 的最新中尺度 returned occurrence 同为浅 `HIGH_CONFIRMED_PROXY`，没有足够清楚、可解释且独立于共同大背景的差异。

### 2.2 固定指标

以各品种 cutoff 对应 close 为基准，本应计算：

1. 截至 `2021-10-15 15:00` 的 terminal close return；
2. tail 内 minimum close return；
3. tail 内 maximum close return；
4. rb 减 hc 的标准化 close path 与 terminal gap。

仅供该 Case 的探索性 material-separation 条件已在冻结文件中写定：

- `abs(terminal return gap) >= 5 percentage points`；或
- `abs(difference in minimum tail return) >= 5 percentage points`。

该阈值不是一般业务 Gate，也不能在看到尾部后修改。

<a id="delivered-byte-audit"></a>
## 3. cutoff 后实物审计

### 3.1 已交付实物的时间上界

授权 replay 包 `e25e585779152aa670d54c87efecba984af4b7e3:runs/BI-01-CO-04/artifacts/worker-BI01CO04-ASOF-VISIBILITY-REPLAY-01/` 明确只消费 fixed prefix：

- 每品种 2160 根原生 PNV；
- decision window 截止 `2021-09-30 15:00`；
- Worker 明确记录 `tail删除/扰动：未执行；没有声称通过，未消费tail`；
- six-query 输出与 `RECOMPUTED_OBJECT_ROWS.csv` 是 cutoff snapshot，不含 cutoff 后 close path。

prior recovery package `dfdf843b47c03c0121fd7151b72f24adb5d986c0:runs/BI-01-CO-04/artifacts/worker-BI01CO04-INPUT-RECOVERY-01/` 的 `DATA_MANIFEST.json` 进一步明确：

- recovery export end-exclusive 为 `2021-10-01 00:00:00`；
- rb／hc／i 三个已导出行情切片的 `last_business_time` 均为 `2021-09-30 15:00:00`；
- manifest 虽记录 source input 延伸至 `2024-02-08 15:00:00`，但那只是原始源覆盖声明，不是本轮已运输、已封口的 tail 字节。

### 3.2 对当前 GitHub 工作面的查找

冻结之后，已对当前分支工作树、R0009 provenance、replay package、prior recovery package及其 formal slices 定向核对；没有找到下列任一项：

- rb／hc／i 在 `(2021-09-30 15:00, 2021-10-15 15:00]` 的 30m 行；
- 该区间的行数、首末时间、时区／交易日映射与 sha256；
- future-tail 专用 manifest、receipt 或静态导出；
- 能把原始 source-root 声明转化为本轮实际消费字节的证据。

因此当前不是“尾部走势无变化”“无反例”或“无挑战”，而是**指定评价输入未进入已交付字节**。

<a id="evaluation-result"></a>
## 4. 评价结果

`NOT_EXECUTABLE_FROM_DELIVERED_BYTES`

| 项目 | 结果 |
|---|---|
| terminal return | `NOT_COMPUTED` |
| minimum tail return | `NOT_COMPUTED` |
| maximum tail return | `NOT_COMPUTED` |
| rb-minus-hc normalized path | `NOT_COMPUTED` |
| material-separation test | `NOT_TESTED` |
| nearest market challenge | `UNKNOWN_INPUT_NOT_DELIVERED` |
| frozen decision changed | `NO` |

不能用以下替代物填表：

- 公开网页或第三方连续合约数据；
- 仅凭 source-root 覆盖声明推断的价格；
- 另一主力切换、不同复权口径或不同交易日历的序列；
- cutoff 后重新跑特征并倒推选择；
- 最终图形的视觉路径。

这些替代都会破坏 frozen symbols／frequency／calendar／source-version／evaluation-plan 的一致性。

<a id="business-interpretation"></a>
## 5. 对冻结业务判断的影响

### 5.1 仍然成立的部分

- `NO_CANDIDATE` 是合格 query snapshot 下的业务判断，而不是数据缺失判断。
- rb／hc 的大尺度几何 proxy 可比；二者最新中尺度 returned occurrence 同号且都很浅，snapshot 没有提供足以合法排名的中尺度差异。
- i 的大尺度 proxy 相反，不能被硬塞进同背景 pair。
- “不强行选品种”本身是本轮低成本入口的一项有效业务输出。

### 5.2 尚未成立的部分

- 不能说 `NO_CANDIDATE` 得到后续行情支持；
- 不能说它被后续行情反证；
- 不能判断 rb／hc 后来是否出现 material separation；
- 不能判断最新中尺度 proxy 是否漏掉真正有价值的相对韧性差异；
- 不能完成最近自然挑战与替代解释的市场检验。

### 5.3 方法反馈的当前上限

截至 snapshot，只能得到一个**结构性负结果**：在这个 cutoff，当前“共同大尺度背景＋最新中尺度对象差异”的读法没有产生独立选择信息。它可能意味着：

1. 该时点确实没有可用差异；
2. latest returned occurrence 太粗，序列关系而非单个最近对象才有信息；
3. 几何 proxy 只提高组织清晰度，没有新增方向能力；
4. 差异存在于未授权的小尺度或其他属性，但本轮不能事后扩展；
5. 后续本来就没有 material separation。

没有正式 tail，不能在上述解释之间裁定。

<a id="minimum-recovery"></a>
## 6. 唯一最小恢复

不需要第三次特征重算、不需要换窗口、不需要扩全市场。只需运输与 frozen source/version 一致的三份行情切片：

- symbols：rb、hc、i；
- frequency：30m；
- interval：`(2021-09-30 15:00:00, 2021-10-15 15:00:00] Asia/Shanghai`；
- fields：至少 business timestamp、close；若存在合约／复权／连续化标识一并保留；
- receipt：每文件 sha256、字节数、行数、首末 timestamp、时区、交易日／夜盘映射、source snapshot/version；
- provenance：明确由 prior manifest 所述 source input 原字节截取，或如并非原字节，明确转换步骤及其 hash。

恢复后必须直接套用已冻结指标，不能重开 snapshot、改 decision、改阈值或补选候选。

<a id="trigger-impact"></a>
## 7. 触发影响

- `FIRST_USABLE_ASOF_LOOP = NOT_YET`：snapshot 和先冻结判断已完成，但 bounded-tail 自然挑战没有可执行输入。
- `ACTIVE_WORK_EFFORT_REVIEW = SATISFIED`：这是第 2 次有效 Professional 调用，任务仍有明确承重未完，必须回管理决定是否运输这一个有界 tail 或停止当前 Case。
- `MATERIAL_INPUT_OR_METHOD_CHANGE = NOT_YET`：未发现 query contract、参数、source identity 或对象语义发生新冲突；当前是 management-required tail 未运输，不把它冒充方法改变。

<a id="next-question"></a>
## 8. 恢复后的唯一问题

> 在保持 `593641a2d26356ecb86cac8903ff02012cebd66c` 冻结的 `NO_CANDIDATE`、目标过程和评价指标不变时，rb 与 hc 在 `(2021-09-30 15:00, 2021-10-15 15:00]` 的 terminal return、minimum return 与标准化路径是否出现预定义的 material separation；若出现，它是否构成“latest mid occurrence 不足以捕捉相对韧性”的反例，若未出现，它对本 Case 的保守无候选判断提供多大支持？
