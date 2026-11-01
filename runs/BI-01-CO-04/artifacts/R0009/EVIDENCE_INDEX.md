# BI-01-CO-04 R0009｜证据、材料与使用边界索引

- `work_id`: `BI-01`
- `run_id`: `BI-01-CO-04`
- `round_id`: `R0009`
- `invocation_id`: `BI01-CO-04-R0009-PROFESSIONAL-QUERY-ASOF-8d6fcf14`
- `contract`: `QUERY_COMPLETION_ASOF_V1`
- 本索引只说明本轮实际消费的材料、证据角色及不能推出的内容；不把路径名、技术 PASS 或未运输 source-root 冒充业务事实。

<a id="governing-materials"></a>
## 1. 有权任务与管理采用

| ID | 精确来源 | 使用范围 |
|---|---|---|
| G01 | `daowei2026/observe-iterate@279e2925156031a5951f852e84911b88d035caf0:runs/BI-01-CO-04/provenance/turns/R0009/FULL_ASSIGNMENT.md::full` | 本轮身份、完整目标、当前工作、交付、Return 与运输要求 |
| G02 | `daowei2026/observe-iterate@d5758f119c82b07236b1d0041c5febcbb1b12273:runs/BI-01-CO-04/01_当前任务.md::full` | 正式问题、完整范围、触发、Binding 与路线 |
| G03 | `daowei2026/observe-iterate@216a83a9594e8ce65681f51c48ca10a607d5aa84:runs/BI-01-CO-04/reviews/management-R0008/PROFESSIONAL_CONTINUATION.md::full` | `QUERY_COMPLETION_ASOF_V1`、固定 T、先冻结后评价、必交付及停止条件 |
| G04 | `daowei2026/observe-iterate@c286238462c07f15d9ebfe3cac06edc6a2da29d4:runs/BI-01-CO-04/reviews/management-R0008/DECISION.md::#operational-contract` | 管理对 replay 的业务采用与旧 event-level 阻断边界 |
| G05 | `daowei2026/observe-iterate@b6ccf766dac055a793e75f76b77a73f4cfc74064:professional/README.md::full` | 探索阶段而非定型方法的边界 |
| G06 | `daowei2026/observe-iterate@b6ccf766dac055a793e75f76b77a73f4cfc74064:professional/exploration/00_BUSINESS_OBJECTIVE.md::full` | 前瞻选择目标及允许无候选 |
| G07 | `daowei2026/observe-iterate@b6ccf766dac055a793e75f76b77a73f4cfc74064:professional/exploration/01_EXISTING_FEATURES_AND_CAPABILITIES.md::full` | 尺度、实际／确认位置与能力边界 |
| G08 | `daowei2026/observe-iterate@b6ccf766dac055a793e75f76b77a73f4cfc74064:professional/exploration/02_CURRENT_WORKING_IDEAS.md::full` | “大背景＋中差异”为待检验设想，不是固定 Gate |
| G09 | `daowei2026/observe-iterate@b6ccf766dac055a793e75f76b77a73f4cfc74064:professional/exploration/03_TOOLING_AND_DATA_USAGE.md::full` | 正式交付、时间字段、图面／数据使用边界 |
| G10 | `daowei2026/observe-iterate@b6ccf766dac055a793e75f76b77a73f4cfc74064:professional/exploration/04_EXISTING_BUSINESS_REFERENCES.md::full` | 旧运行只作来源事实，不继承结论 |
| G11 | `daowei2026/observe-iterate@b6ccf766dac055a793e75f76b77a73f4cfc74064:professional/exploration/05_OWNER_PROCESS_EXPLANATION.md::full` | as-of 比较、自然挑战和反馈方法 |
| G12 | `daowei2026/observe-iterate@b6ccf766dac055a793e75f76b77a73f4cfc74064:professional/exploration/tooling_examples/2026-11-01_30m_multi_symbol_turn_chart.md::full` | 历史 rb／hc／i 入口背景；未作为本轮 snapshot 数据替代 |
| G13 | `daowei2026/observe-iterate@b6ccf766dac055a793e75f76b77a73f4cfc74064:runtime/operations/CASE_OBSERVATION_RUN_GUIDE.md::full` | Run、Worker 与动态工作面边界 |
| G14 | `daowei2026/observe-iterate@e28be2f92522064c146ffe28166350b39a7ae7ca:runs/BI-01-CO-04/OWNER_START.md::full` | Owner GO、职责和写面 |

<a id="snapshot-evidence"></a>
## 2. query snapshot 承重实物

根目录：

`daowei2026/observe-iterate@e25e585779152aa670d54c87efecba984af4b7e3:runs/BI-01-CO-04/artifacts/worker-BI01CO04-ASOF-VISIBILITY-REPLAY-01/`

| ID | 文件／定位 | 本轮实际用途 | 关键边界 |
|---|---|---|---|
| S01 | `FULL_RESPONSE.md::full` | 核 replay 身份、六组调用、对象行数、tail 未消费 | Worker 的 `BLOCKED_NO_LOOKAHEAD_PROOF` 不被改写；管理另行采用 query-completion 合同 |
| S02 | `REPLAY_MANIFEST.json::full` | replay id、symbols、frequency、scales、参数与包结构 | 不推出 event-level first-seen |
| S03 | `RECOMPUTED_OBJECT_ROWS.csv::full` | 选择每个 symbol／scale 的 rightmost returned occurrence；读取 x/y/xConfirm/yConfirm/event_ts/source key/replay key | final batch occurrence 不等于 active object、首次出现、撤回或重现 |
| S04 | `MATRIX_EXECUTION_RECEIPTS.json::full` | 六组 query completion time 与结果计数 | completion 是本轮 operational known time，不是历史 publish time |
| S05 | `BATCH_INPUT_BOUNDARY_AUDIT.json::full` | 物理 prefix 边界和实际输入文件打开范围 | 只支持该 fixed prefix，不支持 cutoff 后行情 |
| S06 | `PNV_PREFIX_ROUTE_RECEIPT.json::full` | 原生 PNV 路由、无 F 盘行情 fallback | 不把路由 PASS 当业务判断 |
| S07 | `OBSERVER_CAPABILITY_EXECUTION.json::full` | 核 old engine 没有逐事件生命周期观察入口 | 解释部署限制，不阻止管理采用的 query snapshot 业务读法 |
| S08 | `TIME_CONTRACT.md::full` | actual／confirm／event_ts 与 known-time 禁止混同 | 本轮 known time 由六组 query 全部完成定义 |
| S09 | `SHA256SUMS::full` | 包内文件封口 | 只对列出的字节有效 |

承重哈希：

| 文件 | sha256 |
|---|---|
| `RECOMPUTED_OBJECT_ROWS.csv` | `9dc2fda0f7ed729c28b1d77c1d631acfa37429376586408d8729a45fb357b54c` |
| `REPLAY_MANIFEST.json` | `72af57a0e33dd419ec15aa7dbb3543ee07ba967597a1ef4f13e1c29ebc585e33` |
| `TIME_CONTRACT.md` | `051dcf2d05db9306b7709fcc29f0d65d5ba8be9d910317766701317309573eeb` |
| `MATRIX_EXECUTION_RECEIPTS.json` | `c3d1b42019bb4132e32df82745ed51cdc45a4cfde1645460e9b88a75bb6f5e2` |
| `BATCH_INPUT_BOUNDARY_AUDIT.json` | `66dc56941830ad7b25f3488eb1a1758aa8516b6f7be353aecac3b6aa0b82ad73` |
| `PNV_PREFIX_ROUTE_RECEIPT.json` | `06d3bd1ce912c247768243ce65f5feda696c7a4ab11ec33f1a7c2fc0b59dde08` |

<a id="prior-recovery"></a>
## 3. prior recovery 的限定使用

根目录：

`daowei2026/observe-iterate@dfdf843b47c03c0121fd7151b72f24adb5d986c0:runs/BI-01-CO-04/artifacts/worker-BI01CO04-INPUT-RECOVERY-01/`

| ID | 文件／定位 | 使用 | 不能推出 |
|---|---|---|---|
| P01 | `DATA_MANIFEST.json::full` | 核 exported rows 的首末时间、source input 覆盖声明、recovery export end-exclusive | source input 覆盖到 2024 不等于本轮已交付 10 月 tail |
| P02 | `copied/formal_slices/rb/gtqh_kline_30m.csv::full` | 核可读 formal slice 实际止于 Sep 30 | 不能从缺行推断 10 月走势 |
| P03 | `copied/formal_slices/hc/gtqh_kline_30m.csv::full` | 同上 | 同上 |
| P04 | `copied/formal_slices/i/gtqh_kline_30m.csv::full` | 同上 | 同上 |

`DATA_MANIFEST.json` 记录：三品种 exported slice 的 `last_business_time` 均为 `2021-09-30 15:00:00`；recovery export `end_exclusive=2021-10-01 00:00:00`；source input last 虽为 `2024-02-08 15:00:00`，但 cutoff 后实际行、哈希与 receipt 未在交付中。

<a id="r0009-artifacts"></a>
## 4. 本轮先冻结实物

| ID | commit | path | 作用 |
|---|---|---|---|
| R01 | `c497abf49806a596e34a51a8a35541644ff84215` | `runs/BI-01-CO-04/artifacts/R0009/QUERY_SNAPSHOT_STATE_TABLE.csv` | 六组 snapshot 状态表；提交时间早于 future-tail 查找 |
| R02 | `593641a2d26356ecb86cac8903ff02012cebd66c` | `runs/BI-01-CO-04/artifacts/R0009/DECISION_FREEZE.json` | 冻结 `NO_CANDIDATE`、目标过程、指标和反证条件 |
| R03 | `b635b0db1dbd38c2b8a4869cf9bc7e70c379d8a7` | `runs/BI-01-CO-04/artifacts/R0009/FUTURE_EVALUATION.md` | 冻结后核查 tail；结论为未运输、不可执行 |

R01 内容 sha256：`973e0a4ce080b3e3d354c91c9e9222e4098b682949e05ee2fbcf7a8ee2e01b08`。

R02 中声明 `future_tail_accessed_before_freeze=false`；本轮没有用后续走势修改 R01 或 R02。

<a id="fact-separation"></a>
## 5. 事实类别分离

### 5.1 业务事实

- query completion 后，rb／hc 的 rightmost big occurrence 均为 `HIGH_CONFIRMED_PROXY`；i 为 `LOW_CONFIRMED_PROXY`。
- rb／hc 的 rightmost mid occurrence 也均为浅 `HIGH_CONFIRMED_PROXY`，分别约 `-0.270660%` 与 `-0.196113%` 的 `yConfirm-y` 相对 y。
- 固定 snapshot 没有为 rb 与 hc 提供清楚的中尺度差异，故冻结 `NO_CANDIDATE`。

### 5.2 派生／视觉证据

- `HIGH_CONFIRMED_PROXY`／`LOW_CONFIRMED_PROXY` 是由 y 与 yConfirm 的固定几何关系派生，状态为 `DERIVED_NOT_UPSTREAM_DIRECTION`。
- 本轮没有以图面颜色、形状或最终路径承重。

### 5.3 工程／方法事实

- 六组 frozen-prefix batch query 成功返回 524 行；管理采用 query completion 为 operational known time。
- replay-local key 只是本次 occurrence key，不是正式 object id。
- 旧引擎未提供 event-level first-seen／withdrawal／reappearance 账本；真实部署仍受该限制。

### 5.4 未知

- rb／hc／i 在指定 bounded tail 的 close path；
- 冻结指标是否达到 material separation；
- 最近市场挑战、反向对象或失败区间；
- latest mid occurrence 的负结果究竟是正确无差异，还是特征读法遗漏。

<a id="search-and-gap"></a>
## 6. 冻结后 tail 查找与缺口

冻结后定向检查了：

1. 当前分支递归工作树；
2. R0009 provenance 与 artifacts；
3. replay package；
4. prior recovery package 及 formal slices；
5. 以 `2021-10-15`、`202110`、`tail`、`future`、`held` 等定位词进行路径／内容核对。

未找到 `(2021-09-30 15:00, 2021-10-15 15:00]` 的三品种 30m 行或对应 receipt。该核对发生在 R01、R02 提交之后。结论只适用于当前 GitHub 可读工作面；不声称原始工作站 source-root 没有这些行。

<a id="not-used"></a>
## 7. 明确未使用

- 未使用 cutoff 后外部网页、第三方数据库或公开连续合约数据；
- 未读取或声称读取局域网页面最终路径；
- 未改 T、参数、品种、频率、尺度或目标过程；
- 未重新计算 10 月特征；
- 未从 final batch rows 推断历史 lifecycle；
- 未把 Worker 技术 PASS／BLOCKED 直接替代业务判断；
- 未签发第三次同类 Worker 来源搜索；
- 未扩展到全市场。

<a id="unavailable"></a>
## 8. 必需但不可用

唯一仍承重且不可用的输入：

- 与 frozen source/version 一致的 rb／hc／i 30m 行，区间 `(2021-09-30 15:00:00, 2021-10-15 15:00:00] Asia/Shanghai`；
- 每份切片的 sha256、字节数、行数、首末 timestamp、calendar／timezone／night-session 说明和 source provenance。

恢复规范见 `FUTURE_EVALUATION.md#minimum-recovery`。
