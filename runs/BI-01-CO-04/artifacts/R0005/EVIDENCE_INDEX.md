# BI-01-CO-04 R0005 可追溯输入／证据清单

- `invocation_id`: `BI01-CO-04-R0005-PROFESSIONAL-678c6b83`
- 用途：支持 `REPORT.md` 中的输入资格裁定；不用于证明任何市场候选或收益结论。
- 状态术语：
  - `READ_FORMAL_SOURCE`：已按固定 commit 读取，可支持其声明范围。
  - `DOCUMENTED_LOCATOR_ONLY`：只在正式文档中看到定位或摘要，未取得目标字节。
  - `UNAVAILABLE_IN_EXECUTION_CHANNEL`：本执行通道无法读取。
  - `NOT_PROVIDED_AS_FORMAL_INPUT`：当前派发／工作面未提供为本 Run 正式输入。
  - `NOT_USED`：为防止误用而明确排除。

<a id="formal-sources"></a>
## 1. 已读取正式来源

| ID | 状态 | 精确来源 | 本轮用途 |
|---|---|---|---|
| S01 | READ_FORMAL_SOURCE | `daowei2026/observe-iterate@2c2c7cc72718ab6baaf0907f290baa9cd2b26484:runs/BI-01-CO-04/provenance/turns/R0005/FULL_ASSIGNMENT.md::full` | 本轮完整授权、优先级、交付与运输 |
| S02 | READ_FORMAL_SOURCE | `daowei2026/observe-iterate@d5758f119c82b07236b1d0041c5febcbb1b12273:runs/BI-01-CO-04/01_当前任务.md::full` | 正式问题、范围、完成条件、路由、触发、Binding |
| S03 | READ_FORMAL_SOURCE | `daowei2026/observe-iterate@56ad93f138b6f62fb8435a8c667018f2ce701805:runs/BI-01-CO-04/reviews/management-R0004/DECISION.md::full` | Reader 接收范围、立即执行 Professional、调用计数 |
| S04 | READ_FORMAL_SOURCE | `daowei2026/observe-iterate@b6ccf766dac055a793e75f76b77a73f4cfc74064:professional/README.md::full` | 探索阶段边界 |
| S05 | READ_FORMAL_SOURCE | `daowei2026/observe-iterate@b6ccf766dac055a793e75f76b77a73f4cfc74064:professional/exploration/00_BUSINESS_OBJECTIVE.md::full` | 业务目标及合法无候选边界 |
| S06 | READ_FORMAL_SOURCE | `daowei2026/observe-iterate@b6ccf766dac055a793e75f76b77a73f4cfc74064:professional/exploration/01_EXISTING_FEATURES_AND_CAPABILITIES.md::full` | 大中小、方向、实际／确认时间边界 |
| S07 | READ_FORMAL_SOURCE | `daowei2026/observe-iterate@b6ccf766dac055a793e75f76b77a73f4cfc74064:professional/exploration/02_CURRENT_WORKING_IDEAS.md::full` | 当前待检验工作设想 |
| S08 | READ_FORMAL_SOURCE | `daowei2026/observe-iterate@b6ccf766dac055a793e75f76b77a73f4cfc74064:professional/exploration/03_TOOLING_AND_DATA_USAGE.md::full` | 正式交付、aidata、图面、数据和时间语义 |
| S09 | READ_FORMAL_SOURCE | `daowei2026/observe-iterate@b6ccf766dac055a793e75f76b77a73f4cfc74064:professional/exploration/04_EXISTING_BUSINESS_REFERENCES.md::full` | 旧运行只作来源事实 |
| S10 | READ_FORMAL_SOURCE | `daowei2026/observe-iterate@b6ccf766dac055a793e75f76b77a73f4cfc74064:professional/exploration/05_OWNER_PROCESS_EXPLANATION.md::full` | Owner 实际观察过程与自然挑战 |
| S11 | READ_FORMAL_SOURCE | `daowei2026/observe-iterate@b6ccf766dac055a793e75f76b77a73f4cfc74064:professional/exploration/tooling_examples/2026-11-01_30m_multi_symbol_turn_chart.md::full` | 历史候选 run/page/root/参数/时间字段 locator |
| S12 | READ_FORMAL_SOURCE | `daowei2026/observe-iterate@b6ccf766dac055a793e75f76b77a73f4cfc74064:runtime/operations/CASE_OBSERVATION_RUN_GUIDE.md::full` | Run 与 Worker 边界 |
| S13 | READ_FORMAL_SOURCE | `daowei2026/observe-iterate@e28be2f92522064c146ffe28166350b39a7ae7ca:runs/BI-01-CO-04/OWNER_START.md::full` | Owner GO、分支、职责与 Worker 线程 |
| S14 | READ_FORMAL_SOURCE | `daowei2026/observe-iterate@b6ccf766dac055a793e75f76b77a73f4cfc74064:overlay/tools/question_work.schema.json::full` | `QUESTION_WORK_RETURN.json` 结构 |
| S15 | READ_FORMAL_SOURCE | `daowei2026/observe-iterate@b6ccf766dac055a793e75f76b77a73f4cfc74064:overlay/tools/longrun_handoff.schema.json::full` | `ROLE_RETURN.json` 结构 |
| S16 | READ_FORMAL_SOURCE | `daowei2026/observe-iterate@b68e72a047567e8aced40042b81b8eb58719cb74:runs/BI-01-CO-04/provenance/turns/R0005/INVOCATION.json::full` | 身份与派发元数据；未改写其 transport 记录 |

<a id="candidate-locators"></a>
## 2. 历史低成本入口定位

| ID | 状态 | 定位 | 已知／未知 |
|---|---|---|---|
| C01 | DOCUMENTED_LOCATOR_ONLY | 页面 `http://192.168.11.40:5006/cae?node_id=6153` | locator 已知；页面像素、DOM、导出和节点读数未取得 |
| C02 | DOCUMENTED_LOCATOR_ONLY | run `GTQH_C001_three_turns_20261101_162005` | 名称已知；run manifest、文件表、哈希、实际行数未取得 |
| C03 | DOCUMENTED_LOCATOR_ONLY | 本地根 `/dwdhome/fy/BASE_E6_2/.../storage_migration_20261101` | 文档定位已知；目录未挂载 |
| C04 | DOCUMENTED_LOCATOR_ONLY | `selected_turn_parameters.json` | 文件名已知；实际 JSON 未读取 |
| C05 | DOCUMENTED_LOCATOR_ONLY | `build_three_turn_plot.py` | 文件名已知；代码字节和版本未读取 |
| C06 | DOCUMENTED_LOCATOR_ONLY | 行情源 `/m3varF/BaseData/futures/GTQH_L1_20210104_20240208` | 文档定位已知；源未挂载 |
| C07 | DOCUMENTED_LOCATOR_ONLY | `rb/hc/i`、`30m`、`2021-08-15..2021-09-30` | 文档摘要已知；实际数据范围、终点包含性和缺失未核 |
| C08 | DOCUMENTED_LOCATOR_ONLY | 图点 `x/y` 为实际位置，`xConfirm/yConfirm` 分离，另有 `event_ts` | 语义摘要已知；逐对象实例值未取得 |

<a id="execution-probes"></a>
## 3. 本执行通道核验

| ID | 状态 | 核验 | 结果及边界 |
|---|---|---|---|
| P01 | NOT_PROVIDED_AS_FORMAL_INPUT | 当前 GitHub Run 工作面 | 在本轮读取到的派发、任务与工作树中，没有随派发提供本 Run 正式 manifest／board 文件、K 线切片、feature slice 或静态图；这不等于它们在别处不存在 |
| P02 | UNAVAILABLE_IN_EXECUTION_CHANNEL | `/dwdhome` | 当前容器中路径不存在／未挂载；不能读历史 run 根 |
| P03 | UNAVAILABLE_IN_EXECUTION_CHANNEL | `/m3varF` | 当前容器中路径不存在／未挂载；不能读行情源 |
| P04 | UNAVAILABLE_IN_EXECUTION_CHANNEL | 局域网页面 | 当前执行通道没有可用的来源浏览器上下文，也没有页面导出；未看图 |
| P05 | UNAVAILABLE_IN_EXECUTION_CHANNEL | Worker 线程 `01a17dd7-5033-7e63-b7a2-edd90b691c33` | 没有可验证的发送／回交接口；未创建假工单 |
| P06 | READ_FORMAL_SOURCE | 分支头 `b68e72a047567e8aced40042b81b8eb58719cb74` | 该提交只补 R0005 transport 记录；未把业务数据包加入工作面 |

<a id="missing-inputs"></a>
## 4. 缺失输入与受阻结论

| ID | 缺失输入 | 受阻结论 |
|---|---|---|
| M01 | 正式 run/board manifest 与文件哈希 | 无法建立输入身份、版本和正式消费关系 |
| M02 | 实际参数 JSON 与 override | 无法核大中小参数是否真由该 run 使用 |
| M03 | rb/hc/i 30m K 线切片 | 无法界定 T 时价格状态、后续目标或自然挑战 |
| M04 | 大／中对象逐行切片 | 无法确定可比背景、中尺度差异、方向和对象存在性 |
| M05 | `x/xConfirm/event_ts` 等实例值 | 无法构造截至 T 已知集 |
| M06 | object id、revision、status | 无法排除最终修订倒填 |
| M07 | 日历、时区、UTI 映射 | 无法跨品种对齐同一 T |
| M08 | 缺失／故障／无信号状态 | 无法把市场无候选与计算问题分开 |
| M09 | 静态图或可读页面 | 无法核视觉对象与结构化数据对应，但即使补图也不能替代 M01—M08 |

<a id="not-evidence"></a>
## 5. 明确不是证据的内容

- 历史 run 名本身不是本 Run 正式输入身份。
- 页面 URL 本身不证明页面可读、对象完整或时间无泄漏。
- 参数摘要不等于参数文件字节。
- 最终图上的实际转折位置不等于当时已知。
- 本地路径在文档中出现不等于本执行通道已读取。
- 输入不可读不等于市场没有候选。
- 本清单不含任何价格结论、收益结论或品种偏好。

<a id="recovery-package"></a>
## 6. 最小恢复定位

恢复要求见 `REPORT.md#minimum-recovery`。最低需要：

1. manifest／run summary／board FILE_INDEX；
2. 实际参数和代码／构建版本 receipt；
3. timespan、日历、时区、UTI 映射；
4. rb/hc/i 30m K 线；
5. 大／中 feature slices，必要时才补小尺度；
6. 字段字典、方向／zig 映射、确认和 revision 语义；
7. 静态图或页面导出；
8. 每文件 sha256、字节数、行数、首末时间。

只接受可定位到实际字节的恢复包；不接受新的文字摘要替代。
