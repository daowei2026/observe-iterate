# EVIDENCE_INDEX — BI-01-CO-05 Professional R0002

## 1. 证据等级

- `FORMAL_FACT`：当前有权 Git 版本或正式 run/core 实物直接提供。
- `DOCUMENTED_REFERENCE`：正式方法/工具文档记录，但本轮未回读对应运行实物。
- `EXECUTION_OBSERVATION`：本次工具通道直接观察，已在 `REPORT.md` 固化。
- `HYPOTHESIS_ONLY`：待正式数据检验，不能支撑业务结论。
- `UNAVAILABLE`：承重实物当前不可读。
- `EXCLUDED`：按任务边界明确不用于当前 Case。

## 2. 当前任务与身份

| ID | 等级 | 精确引用 | 本轮用途 |
|---|---|---|---|
| E01 | `FORMAL_FACT` | `daowei2026/observe-iterate@a6a8acf7fa65665218d0f2163598d434fb921b24:runs/BI-01-CO-05/01_当前任务.md::full` | 当前正式任务、触发、路线、Worker 边界 |
| E02 | `FORMAL_FACT` | `daowei2026/observe-iterate@767aae2fa6291265a12512589dcd5aaa7277adb6:runs/BI-01-CO-05/provenance/turns/R0002/FULL_ASSIGNMENT.md::full` | 本轮完整派发 |
| E03 | `FORMAL_FACT` | `daowei2026/observe-iterate@a7f9c4cf261a751989a2cda6857176a33acca037:runs/BI-01-CO-05/provenance/turns/R0002/INVOCATION.json::full` | invocation/token/role/recipient |
| E04 | `FORMAL_FACT` | `daowei2026/observe-iterate@a7f9c4cf261a751989a2cda6857176a33acca037:runs/BI-01-CO-05/provenance/turns/R0002/SEND_RECEIPT.json::full` | `state=COMMITTED`；Worker 工单身份前提 |
| E05 | `FORMAL_FACT` | `daowei2026/observe-iterate@0a2347e93ef66fcc1165ed5ac31960b59813f6c8:runs/BI-01-CO-05/reviews/management-R0001/DECISION.md::#current-task-decision` | 当前任务采用依据 |

## 3. 方法与 Owner 来源

| ID | 等级 | 精确引用 | 使用点 |
|---|---|---|---|
| M01 | `FORMAL_FACT` | `daowei2026/observe-iterate@b6b344ef0dbd5bc5596c8ec726aad39474254fc4:professional/README.md::full` | 探索期角色边界 |
| M02 | `FORMAL_FACT` | `daowei2026/observe-iterate@b6b344ef0dbd5bc5596c8ec726aad39474254fc4:professional/exploration/06_EXPLORATION_STAGE_GOAL.md::full` | 当前探索目标 |
| M03 | `FORMAL_FACT` | `daowei2026/observe-iterate@b6b344ef0dbd5bc5596c8ec726aad39474254fc4:professional/exploration/00_BUSINESS_OBJECTIVE.md::full` | 投资业务目的 |
| M04 | `FORMAL_FACT` | `daowei2026/observe-iterate@b6b344ef0dbd5bc5596c8ec726aad39474254fc4:professional/exploration/01_EXISTING_FEATURES_AND_CAPABILITIES.md::full` | 对象、尺度、方向、actual/confirm |
| M05 | `FORMAL_FACT` | `daowei2026/observe-iterate@b6b344ef0dbd5bc5596c8ec726aad39474254fc4:professional/exploration/02_CURRENT_WORKING_IDEAS.md::full` | 当前设想摘要 |
| M06 | `FORMAL_FACT` | `daowei2026/observe-iterate@b6b344ef0dbd5bc5596c8ec726aad39474254fc4:professional/exploration/03_TOOLING_AND_DATA_USAGE.md::full` | aidata 正式链路、图/数据区分 |
| M07 | `FORMAL_FACT` | `daowei2026/observe-iterate@b6b344ef0dbd5bc5596c8ec726aad39474254fc4:professional/exploration/04_EXISTING_BUSINESS_REFERENCES.md::full` | 旧 Case 边界 |
| M08 | `FORMAL_FACT` | `daowei2026/observe-iterate@b6b344ef0dbd5bc5596c8ec726aad39474254fc4:professional/exploration/05_OWNER_PROCESS_EXPLANATION.md::full` | 两层实践、关键 T、挑战 |
| M09 | `FORMAL_FACT` | `daowei2026/observe-iterate@85febea03631aef7757412c20533ff536dbf51d9:runs/BI-01-CO-05/OWNER_START.md::full` | Owner 当前设想 |
| M10 | `FORMAL_FACT` | `daowei2026/observe-iterate@b6b344ef0dbd5bc5596c8ec726aad39474254fc4:runtime/operations/CASE_OBSERVATION_RUN_GUIDE.md::full` | Run 接线和不继承旧 Run |
| M11 | `FORMAL_FACT` | `daowei2026/observe-iterate@a7f9c4cf261a751989a2cda6857176a33acca037:overlay/12_管理接收与地图校验.md::#worker-order-contract` | Worker 工单签发前提 |

## 4. 候选输入证据

| ID | 等级 | 精确位置 | 已知 | 未知/不可主张 |
|---|---|---|---|---|
| C01 | `DOCUMENTED_REFERENCE` | `daowei2026/observe-iterate@b6b344ef0dbd5bc5596c8ec726aad39474254fc4:professional/exploration/tooling_examples/2026-11-01_30m_multi_symbol_turn_chart.md::full` | run_id、page、symbols、30m、展示窗口、参数族线索、run/core/board 路径线索 | 当前 run 是否完整、字段/覆盖/版本/哈希、关键 T |
| C02 | `DOCUMENTED_REFERENCE` | `run_id=GTQH_C001_three_turns_20261101_162005` | 精确候选标识 | 正式 manifest 未回读 |
| C03 | `DOCUMENTED_REFERENCE` | `http://192.168.11.40:5006/cae?node_id=6153` | 精确页面位置 | 本轮未实际打开，图面不通过 |
| C04 | `UNAVAILABLE` | `/dwdhome/fy/BASE_E6_2/mquant/aidata/test_runs/fy_owner_1d_30m_20261027/storage_migration_20261101/three_turn_plot/GTQH_C001_three_turns_20261101_162005/` | 文档给出路径族 | 当前执行通道未挂载 |
| C05 | `UNAVAILABLE` | `/m3varF/BaseData/futures/GTQH_L1_20210104_20240208` | 文档给出数据源 | 当前执行通道未挂载 |
| C06 | `UNAVAILABLE` | same-run `DELIVERY_MANIFEST / FILE_INDEX / feature slices / KLine / zig mapping` | 无 | 所有市场对象和关键 T |

## 5. 本轮执行观察

| ID | 等级 | 观察 | 影响 |
|---|---|---|---|
| X01 | `EXECUTION_OBSERVATION` | 连接浏览器工具没有 originating browser context | 未实际查看页面 |
| X02 | `EXECUTION_OBSERVATION` | GitHub 当前 Run 与 conversation/library 可读面未发现候选 run 的正式 manifest、FILE_INDEX 或切片 | 输入不能采纳 |
| X03 | `EXECUTION_OBSERVATION` | 本地执行容器无 `/dwdhome`、`/m3varF` 或 workspace 挂载 | 不能程序读取正式数据 |
| X04 | `EXECUTION_OBSERVATION` | 初始观察的 `NOT_SENT` 已被控制面提交 `a7f9c4cf…` 更新为 `COMMITTED` | 允许按当前合同签 1 份窄 Worker 工单 |

X01—X04 的耐久化陈述位于本包 `REPORT.md`；它们不替代缺失的正式市场实物。

## 6. 业务主张—证据映射

| 主张 | 证据 | 状态 |
|---|---|---|
| 当前存在一个最低成本候选输入 | C01—C03 | 支持“候选”，不支持“已采纳” |
| 当前合格市场 T 为 0 | C04—C06、X01—X03 | 支持 |
| 不能形成大尺度共同背景 | 无 | **不作此主张** |
| 不能形成市场候选 | 无 | **不作此主张** |
| 当前不得形成候选规律 | C04—C06 | 支持，属于证据资格裁定 |
| Worker 身份前提已满足、可签窄工单 | E03、E04、M11、X04 | 支持；不等于已验证或投递 |
| Owner 主过程应被替换 | 无 | **不作此主张** |
| 增加薄的证据平面检查 | 本轮实际阻断 + M06/M08 | 局部过程建议，待后续验证 |

## 7. 排除项

| 项目 | 状态 | 理由 |
|---|---|---|
| CO-01—CO-04 业务结果 | `EXCLUDED` | 新 Case 无父任务继承 |
| 旧 2024 small/mid 运行叙述 | `EXCLUDED` | 非当前 run、缺大尺度和当前正式实物 |
| 外部网络/行情 | `EXCLUDED` | 非任务正式链路 |
| 截图反造数据 | `EXCLUDED` | 违反工具与数据边界 |
| 最终历史交集倒选 | `EXCLUDED` | 违反 as-of 要求 |

## 8. 本包实物

- `REPORT.md`
- `INPUT_QUALIFICATION.json`
- `KEY_T_STATE_TABLE.csv`
- `USE_CASE_AND_CHALLENGE.md`
- `OWNER_PROCESS_FEEDBACK.md`
- `WORKER_ORDER.md`
- `ARTIFACT_MANIFEST.json`
- canonical returns: `runs/BI-01-CO-05/provenance/turns/R0002/QUESTION_WORK_RETURN.json` 与 `ROLE_RETURN.json`
