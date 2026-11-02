# EVIDENCE_INDEX — BI-01-CO-05 Professional R0011

## 1. 身份与签发资格

| ID | 类型 | 精确引用 | 本轮用途 |
|---|---|---|---|
| I01 | `FORMAL_FACT` | `daowei2026/observe-iterate@a47c53c2dafab48480c2f93e147b9b1b0e950c82:runs/BI-01-CO-05/provenance/turns/R0011/FULL_ASSIGNMENT.md::full` | 本轮完整派发 |
| I02 | `FORMAL_FACT` | `daowei2026/observe-iterate@4699c3c947753f65d0a3f3ff044f5c74d68fdc3b:runs/BI-01-CO-05/provenance/turns/R0011/INVOCATION.json::full` | invocation、token、recipient、route、计数 |
| I03 | `FORMAL_FACT` | `daowei2026/observe-iterate@4699c3c947753f65d0a3f3ff044f5c74d68fdc3b:runs/BI-01-CO-05/provenance/turns/R0011/SEND_RECEIPT.json::full` | 同身份 `state=COMMITTED` |
| I04 | `FORMAL_FACT` | `daowei2026/observe-iterate@4699c3c947753f65d0a3f3ff044f5c74d68fdc3b:runs/BI-01-CO-05/provenance/turns/R0011/DISPATCH.json::full` | same_work、采用依据和本轮 evidence refs |
| I05 | `FORMAL_FACT` | `daowei2026/observe-iterate@4699c3c947753f65d0a3f3ff044f5c74d68fdc3b:overlay/12_管理接收与地图校验.md::#worker-order-contract` | 工单字段、COMMITTED 前提、controller preflight 与回原 Pro 机制 |

## 2. 管理采用与业务任务

| ID | 类型 | 精确引用 | 采用内容 |
|---|---|---|---|
| M01 | `MANAGEMENT_ADOPTED` | `daowei2026/observe-iterate@0776c5645be4bf1d38c7151baa8662def243e26b:runs/BI-01-CO-05/reviews/management-R0010/DECISION.md::#reentry` | 新的一次性条件重入 order；探针通过即原脚本全量执行 |
| M02 | `MANAGEMENT_ADOPTED` | `daowei2026/observe-iterate@0776c5645be4bf1d38c7151baa8662def243e26b:runs/BI-01-CO-05/provenance/turns/R0010/FULL_RESPONSE.md::#reentry-decision` | 精确工单身份、执行分支、禁止变化和退出条件 |
| M03 | `FORMAL_FACT` | `daowei2026/observe-iterate@a6a8acf7fa65665218d0f2163598d434fb921b24:runs/BI-01-CO-05/01_当前任务.md::full` | 完整业务问题、输入资格、两层实践与 Worker 边界 |
| M04 | `FORMAL_FACT` | `daowei2026/observe-iterate@85febea03631aef7757412c20533ff536dbf51d9:runs/BI-01-CO-05/OWNER_START.md::full` | Owner GO、分支、Worker 线程和初始实践责任 |

## 3. 原脚本、旧执行与新 order 的关系

| ID | 类型 | 精确引用 | 事实 |
|---|---|---|---|
| S01 | `ACCEPTED_TECHNICAL_BASIS` | `daowei2026/observe-iterate@34198df6d4435feaa089baeae73e934559bd8b19:runs/BI-01-CO-05/artifacts/professional-R0008/build_bi01_co05_r0008_fullrange_chart_data.py::full` | 原脚本字节、全段图数配置 |
| S02 | `FORMAL_FACT` | 脚本 Git blob `f84bf86d4bfe1cf5411ee7e35d6c867aa4957d6c`；SHA-256 `5571cad70d5c519d9e0c5260564346837833eb147d7c4fafb40afb0505a3df16` | 本轮未修改，Worker 执行前重核 |
| S03 | `HISTORICAL_TERMINAL` | `daowei2026/observe-iterate@34198df6d4435feaa089baeae73e934559bd8b19:runs/BI-01-CO-05/artifacts/professional-R0008/WORKER_ORDER.md::full` | 旧 order 只保留历史，不重派 |
| S04 | `WORKER_OBSERVATION` | `daowei2026/observe-iterate@8c7de6c113f38d24584d73e081d441d85e8a8c4b:runs/BI-01-CO-05/artifacts/worker-BI01CO05-FULLRANGE-CHART-DATA-R0008-01/EXECUTION_RECEIPT.json::full` | 上次 launcher、Python、脚本 hash、单次 errno 5 与未到页面/board |
| S05 | `PROFESSIONAL_SIGNED` | `runs/BI-01-CO-05/artifacts/professional-R0011/WORKER_ORDER.md` | 新 order 独立身份、一次性探针与条件全量执行 |
| S06 | `PROFESSIONAL_SIGNED` | `runs/BI-01-CO-05/artifacts/professional-R0011/ORDER_SIGNING_RECEIPT.json` | 机器可读签发基础、不可变输入与未声称状态 |

## 4. 专业方法与工具边界

| ID | 类型 | 精确引用 | 使用点 |
|---|---|---|---|
| P01 | `FORMAL_FACT` | `professional/README.md@b6b344ef...::full` | 探索阶段角色和动态工作面 |
| P02 | `FORMAL_FACT` | `professional/exploration/00_BUSINESS_OBJECTIVE.md@b6b344ef...::full` | 投资用途与合法无候选边界 |
| P03 | `FORMAL_FACT` | `professional/exploration/01_EXISTING_FEATURES_AND_CAPABILITIES.md@b6b344ef...::full` | large/mid、方向及 actual/confirm 边界 |
| P04 | `FORMAL_FACT` | `professional/exploration/03_TOOLING_AND_DATA_USAGE.md@b6b344ef...::full` | chart/pages/board、manifest/index、同 run/core 与覆盖边界 |
| P05 | `FORMAL_FACT` | `professional/exploration/05_OWNER_PROCESS_EXPLANATION.md@b6b344ef...::full` | as-of 第一层和中尺度第二层；技术输入不代替业务实践 |
| P06 | `FORMAL_FACT` | `professional/exploration/06_EXPLORATION_STAGE_GOAL.md@b6b344ef...::full` | 当前长程目的与 Professional 职责 |
| P07 | `FORMAL_FACT` | `professional/exploration/07_图数准备工单约定.md@46563266...::full` | Pro 决定图数/代码，Worker 只执行修通并回交 |
| P08 | `FORMAL_FACT` | `runtime/operations/CASE_OBSERVATION_RUN_GUIDE.md@b6b344ef...::full` | 当前 Run 接线和技术 PASS 不等于业务包 |

## 5. 主张—证据映射

| 主张 | 证据 | 状态 |
|---|---|---|
| R0011 具备合法签发身份 | I01—I05 | 支持 |
| 新 order 已由原 Professional 正式签发 | I02、I03、S05、S06 | 支持 |
| 旧 R0008 order 可重派 | M01、M02、S03 | **否定** |
| R0008 原脚本和业务参数改变 | M01、M02、S01、S02 | **否定** |
| controller preflight 已运行 | 无 | **不作主张** |
| Worker 已实际派发或执行 | 无 | **不作主张** |
| 日历读探针通过/失败 | 无当前执行 | `UNKNOWN` |
| 全段图数或正式数据存在 | 无当前执行 | `UNKNOWN` |
| 共同大尺度背景或候选存在 | 无 | **不作主张** |
| 合格 market T | 无图数 | `0`（证据资格状态） |

## 6. 本轮实物

- `REPORT.md`
- `WORKER_ORDER.md`
- `ORDER_SIGNING_RECEIPT.json`
- `EVIDENCE_INDEX.md`
- `ARTIFACT_MANIFEST.json`
- canonical `FULL_RESPONSE.md`
- `QUESTION_WORK_RETURN.json`
- `ROLE_RETURN.json`
