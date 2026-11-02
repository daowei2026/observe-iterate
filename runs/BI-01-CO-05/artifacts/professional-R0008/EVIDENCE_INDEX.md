# EVIDENCE_INDEX — BI-01-CO-05 Professional R0008

## 1. 证据等级

- `FORMAL_FACT`：当前有权 Git 版本或控制面实物直接提供。
- `OWNER_DIRECTED_CHANGE`：Owner 已明确授权并被 R0006 管理采用的局部纠正。
- `MANAGEMENT_ADOPTED`：R0006 已接收/否定并形成当前 same-work 接续的内容。
- `PROFESSIONAL_SELECTION`：本轮 Professional 在授权范围内固定的图数方案。
- `STATIC_VALIDATION`：本地静态检查，只证明语法/结构，不证明目标运行时。
- `PENDING_EXECUTION`：必须由合法 Worker 在目标环境执行并回交。
- `EXCLUDED`：已明确退出本轮或不得继承的范围。

## 2. 身份、任务与控制面

| ID | 等级 | 精确引用 | 本轮用途 |
|---|---|---|---|
| I01 | `FORMAL_FACT` | `daowei2026/observe-iterate@38d056d7acc73939398c30a341b4a84333420feb:runs/BI-01-CO-05/provenance/turns/R0008/FULL_ASSIGNMENT.md::full` | 本轮完整派发 |
| I02 | `FORMAL_FACT` | `daowei2026/observe-iterate@14de6df13c7303fe2bf390638be40011d7f20226:runs/BI-01-CO-05/provenance/turns/R0008/INVOCATION.json::full` | invocation、token、route、调用计数 |
| I03 | `FORMAL_FACT` | `daowei2026/observe-iterate@4f688c6185ea22cabcafc62af9572c05822f0386:runs/BI-01-CO-05/provenance/turns/R0008/SEND_RECEIPT.json::full` | 当前发送状态与工单签发前提 |
| I04 | `FORMAL_FACT` | `daowei2026/observe-iterate@a6a8acf7fa65665218d0f2163598d434fb921b24:runs/BI-01-CO-05/01_当前任务.md::full` | 正式任务与 Question Work Binding |
| I05 | `FORMAL_FACT` | `daowei2026/observe-iterate@4f688c6185ea22cabcafc62af9572c05822f0386:overlay/12_管理接收与地图校验.md::#worker-order-contract` | Worker 工单字段、COMMITTED 前提和 preflight |

## 3. Owner 纠正与管理采用

| ID | 等级 | 精确引用 | 本轮采用内容 |
|---|---|---|---|
| O01 | `OWNER_DIRECTED_CHANGE` | `daowei2026/observe-iterate@e03e184b06fb058c36fe18c28bc0dc52701b803f:runs/BI-01-CO-05/OWNER_CHANGE_20261102_R0005_TIME_COVERAGE.md::full` | 主图/正式数据固定全段；原 Professional 新脚本、新 order；旧身份不得改写 |
| O02 | `MANAGEMENT_ADOPTED` | `daowei2026/observe-iterate@15f05a4dac02984592767b403cc3c61cfec83f9d:runs/BI-01-CO-05/reviews/management-R0006/DECISION.md::#continuation` | 下一有效 Professional 的八项必交与 same-work |
| O03 | `MANAGEMENT_ADOPTED` | `daowei2026/observe-iterate@15f05a4dac02984592767b403cc3c61cfec83f9d:runs/BI-01-CO-05/provenance/turns/R0006/FULL_RESPONSE.md::#owner-correction` | 全段、同 run/core、辅助图边界 |
| O04 | `FORMAL_FACT` | `daowei2026/observe-iterate@efc39e200cce3c94905f9dd35377a42371743ed2:runs/BI-01-CO-05/provenance/turns/R0007/FULL_RESPONSE.md::full` | R0006 交付关联补齐，不改变业务决定 |

## 4. 业务/工具方法来源

| ID | 等级 | 精确引用 | 使用点 |
|---|---|---|---|
| M01 | `FORMAL_FACT` | `daowei2026/observe-iterate@b6b344ef0dbd5bc5596c8ec726aad39474254fc4:professional/README.md::full` | Professional 探索职责 |
| M02 | `FORMAL_FACT` | `daowei2026/observe-iterate@b6b344ef0dbd5bc5596c8ec726aad39474254fc4:professional/exploration/00_BUSINESS_OBJECTIVE.md::full` | 投资业务目的 |
| M03 | `FORMAL_FACT` | `daowei2026/observe-iterate@b6b344ef0dbd5bc5596c8ec726aad39474254fc4:professional/exploration/01_EXISTING_FEATURES_AND_CAPABILITIES.md::full` | KLine、large/mid、actual/confirm 能力边界 |
| M04 | `FORMAL_FACT` | `daowei2026/observe-iterate@b6b344ef0dbd5bc5596c8ec726aad39474254fc4:professional/exploration/03_TOOLING_AND_DATA_USAGE.md::full` | 图/正式数据同身份及 aidata 调用边界 |
| M05 | `FORMAL_FACT` | `daowei2026/observe-iterate@b6b344ef0dbd5bc5596c8ec726aad39474254fc4:professional/exploration/05_OWNER_PROCESS_EXPLANATION.md::full` | 第一层/第二层与 as-of 业务过程 |
| M06 | `FORMAL_FACT` | `daowei2026/observe-iterate@46563266029a53e46982ea5321c737b987e36335:professional/exploration/07_图数准备工单约定.md::full` | Professional 决定图数/代码、Worker 只执行修通回交 |
| M07 | `FORMAL_FACT` | `daowei2026/observe-iterate@b6b344ef0dbd5bc5596c8ec726aad39474254fc4:professional/exploration/tooling_examples/2026-11-01_30m_multi_symbol_turn_chart.md::full` | 已走通 API/图面参考，不继承旧 SOF 或旧时间窗 |
| M08 | `FORMAL_FACT` | `daowei2026/observe-iterate@b6b344ef0dbd5bc5596c8ec726aad39474254fc4:runtime/operations/CASE_OBSERVATION_RUN_GUIDE.md::full` | 当前 Run 接线与结果回原 Professional |

## 5. 旧实现核对

| ID | 等级 | 精确引用 | 结论 |
|---|---|---|---|
| L01 | `FORMAL_FACT` | `daowei2026/observe-iterate@c0b628e58a2231bc50796e56c153446018fdab5a:runs/BI-01-CO-05/artifacts/professional-R0005/build_bi01_co05_r0005_chart_data.py::full` | 旧脚本把主窗、Context、timespan 和回执锁定为 45 天；不能仅改文字 |
| L02 | `FORMAL_FACT` | `daowei2026/observe-iterate@c0b628e58a2231bc50796e56c153446018fdab5a:runs/BI-01-CO-05/artifacts/professional-R0005/WORKER_ORDER.md::full` | 旧 order 身份保留历史、停止新投 |
| L03 | `EXCLUDED` | `BI01CO05-CHART-DATA-R0005-01` | 不复用、不改名、不重复派发 |

## 6. R0008 专业选择与实物

| ID | 等级 | 实物 | 支持的主张 |
|---|---|---|---|
| P01 | `PROFESSIONAL_SELECTION` | `CHART_DATA_REQUEST.json` | rb/hc/i、30m、全段主窗、large/mid、无 small、半年度辅助图和核验合同已固定 |
| P02 | `PROFESSIONAL_SELECTION` | `build_bi01_co05_r0008_fullrange_chart_data.py` | 业务选择已接入 aidata 调用和同 run/core 图数链 |
| P03 | `STATIC_VALIDATION` | `SCRIPT_STATIC_VALIDATION.json` | Python 编译与 AST 通过；目标 runtime 未执行 |
| P04 | `FORMAL_FACT` | `WORKER_ORDER.md` | 新 order 内容及技术边界；签发状态见控制面 |
| P05 | `FORMAL_FACT` | `REPORT.md` | 当前状态、限制、触发、未完与接续 |

## 7. 主张—证据映射

| 主张 | 证据 | 状态 |
|---|---|---|
| Owner 要求全段主图/正式数据 | O01—O03 | 支持 |
| 旧 45 天单不得继续执行 | O01—O03、L01—L03 | 支持 |
| 本轮已固定新的全段图数方案 | P01、P02 | 支持 |
| 脚本语法有效 | P03 | 仅静态范围支持 |
| 脚本在目标 aidata 环境运行成功 | 无 | 不作主张 |
| 新 Worker 工单正式签发 | I03、I05、P04 | 取决于 `SEND_RECEIPT=COMMITTED`；本包状态 `SIGNED_PENDING_CONTROLLER_VALIDATION_AND_DISPATCH` |
| controller preflight/实际派发完成 | 无 | 不作主张 |
| 新全段图页/正式数据存在 | 无 | 不作主张 |
| 共同背景、候选、排序或无候选 | 无 | 不作主张 |
| 合格市场 T | 无 | `0`，证据未取得 |

## 8. 执行后必须返回的证据

`PENDING_EXECUTION`：

- 实际 command/exit/stdout/stderr/run_id；
- 全段主图及七个辅助图的打开记录和静态证据；
- delivery manifest、feature-slice stats、file index；
- rb/hc/i × KLine/large/mid 的实际首末、行数、空值、重复和缺失；
- feature warm-up / effective start；
- 每个文件路径、字节和 sha256；
- 图与正式数据同 run/core 证据；
- 所有普通兼容修通副本与 diff；
- `FULL_RESPONSE.md` 回原 Professional。

## 9. 明确排除

- R0002 事件账本、全面方向映射、全面输入审计；
- R0004 未采用迁移/任务改写；
- R0005 旧 order/脚本的当前执行资格；
- small 尺度；
- Worker 的市场解释或业务决策；
- 外部行情、网络数据或平行数据库路径；
- 用 URL、退出码或路径存在替代实际开图/读数。
