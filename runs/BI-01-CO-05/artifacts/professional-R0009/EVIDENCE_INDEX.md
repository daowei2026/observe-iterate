# EVIDENCE_INDEX — BI-01-CO-05 Professional R0009

## 1. 证据等级

- `FORMAL_FACT`：当前有权 Git/控制面实物直接提供。
- `WORKER_OBSERVATION`：获授权 Worker 在目标环境真实执行并回交。
- `PROFESSIONAL_CLASSIFICATION`：Professional 对事实的业务资格与影响裁定。
- `UNKNOWN`：本次执行未到达或未取得。
- `EXCLUDED`：不得用于本轮主张。

## 2. 调用、Binding 与控制面

| ID | 等级 | 精确引用 | 用途 |
|---|---|---|---|
| I01 | `FORMAL_FACT` | `daowei2026/observe-iterate@41aa20f82c087210d8e99ef1adb14e97e56ac161:runs/BI-01-CO-05/provenance/turns/R0009/FULL_ASSIGNMENT.md::full` | 本轮完整派发 |
| I02 | `FORMAL_FACT` | `daowei2026/observe-iterate@d1a1568583631cee4fda84a5be37824af2c85322:runs/BI-01-CO-05/provenance/turns/R0009/INVOCATION.json::full` | invocation、token、计数、worker result ref |
| I03 | `FORMAL_FACT` | `daowei2026/observe-iterate@d1a1568583631cee4fda84a5be37824af2c85322:runs/BI-01-CO-05/provenance/turns/R0009/SEND_RECEIPT.json::full` | 当前调用真实 `COMMITTED` 发送记录 |
| I04 | `FORMAL_FACT` | `daowei2026/observe-iterate@a6a8acf7fa65665218d0f2163598d434fb921b24:runs/BI-01-CO-05/01_当前任务.md::full` | 完整任务、触发与 Worker 边界 |
| I05 | `FORMAL_FACT` | `daowei2026/observe-iterate@15f05a4dac02984592767b403cc3c61cfec83f9d:runs/BI-01-CO-05/reviews/management-R0006/DECISION.md::full` | 全段采用、投入重置、R0008 接续 |
| I06 | `FORMAL_FACT` | `daowei2026/observe-iterate@1d38a58132e9a8f3a83668aac79be3726109c442:runs/BI-01-CO-05/provenance/turns/R0009/WORKER_RESULT_TRANSPORT_CHECK.json::full` | Worker 结果回原签发 Pro 的机械 PASS |

## 3. 原工单与业务输入

| ID | 等级 | 精确引用 | 已固定内容 |
|---|---|---|---|
| O01 | `FORMAL_FACT` | `daowei2026/observe-iterate@34198df6d4435feaa089baeae73e934559bd8b19:runs/BI-01-CO-05/artifacts/professional-R0008/WORKER_ORDER.md::full` | order identity、写权、停止条件、图数验收 |
| O02 | `FORMAL_FACT` | `daowei2026/observe-iterate@afd596a021f96c9f381b64faf6a266465671e776:runs/BI-01-CO-05/artifacts/professional-R0008/REPORT.md::full` | 全段方案与接续 |
| O03 | `FORMAL_FACT` | `daowei2026/observe-iterate@e03e184b06fb058c36fe18c28bc0dc52701b803f:runs/BI-01-CO-05/OWNER_CHANGE_20261102_R0005_TIME_COVERAGE.md::full` | `[2021-01-04, 2024-03-01)` 全段纠正 |
| O04 | `FORMAL_FACT` | R0008 script SHA `5571cad70d5c519d9e0c5260564346837833eb147d7c4fafb40afb0505a3df16` | Worker 实测同字节 |

## 4. Worker 执行事实

| ID | 等级 | 精确引用 | 事实 |
|---|---|---|---|
| W01 | `WORKER_OBSERVATION` | `daowei2026/observe-iterate@8c7de6c113f38d24584d73e081d441d85e8a8c4b:runs/BI-01-CO-05/artifacts/worker-BI01CO05-FULLRANGE-CHART-DATA-R0008-01/FULL_RESPONSE.md::full` | 真实一次执行、失败分类、完整未完 |
| W02 | `WORKER_OBSERVATION` | 同提交 `EXECUTION_RECEIPT.json::full` | 命令、时间、耗时、退出码、API 调用顺序 |
| W03 | `WORKER_OBSERVATION` | 同提交 `BLOCKER_EVIDENCE.json::full` | errno 5、精确文件、调用链、NFS mount |
| W04 | `WORKER_OBSERVATION` | 同提交 `PAGE_INDEX.csv::full` | 主图与 7 辅助图均未生成/未打开 |
| W05 | `WORKER_OBSERVATION` | 同提交 `COVERAGE_AND_MISSING.csv::full` | 9 类切片覆盖均 UNKNOWN，不是 0 |
| W06 | `WORKER_OBSERVATION` | 同提交 `PAGE_AND_DATA_IDENTITY.json::full` | actual run/core 未建立，同身份不可证明 |
| W07 | `WORKER_OBSERVATION` | 同提交 `FORMAL_FILE_INDEX.csv::full` | manifest/stats/index/切片均为缺件占位 |
| W08 | `WORKER_OBSERVATION` | 同提交 `DEPENDENCY_BEFORE.json` 与 `DEPENDENCY_AFTER.json` | 依赖快照相同 |
| W09 | `WORKER_OBSERVATION` | 同提交 `COMPATIBILITY_PATCH.diff` | 0 字节；无代码/业务修通 |

## 5. 方法边界来源

| ID | 等级 | 精确引用 | 使用点 |
|---|---|---|---|
| M01 | `FORMAL_FACT` | `professional/exploration/03_TOOLING_AND_DATA_USAGE.md@b6b344ef...::full` | run/core、页面、board、正式数据职责分开 |
| M02 | `FORMAL_FACT` | `professional/exploration/05_OWNER_PROCESS_EXPLANATION.md@b6b344ef...::full` | as-of 第一层与中尺度第二层 |
| M03 | `FORMAL_FACT` | `professional/exploration/01_EXISTING_FEATURES_AND_CAPABILITIES.md@b6b344ef...::full` | large/mid、actual/confirm 与方向边界 |
| M04 | `FORMAL_FACT` | `professional/exploration/00_BUSINESS_OBJECTIVE.md@b6b344ef...::full` | 投资用途与合法无候选边界 |

## 6. 主张—证据映射

| 主张 | 证据 | 状态 |
|---|---|---|
| Worker 按工单真实执行一次 | W01—W03 | 支持 |
| 脚本字节与固定 SHA 一致 | O04、W02 | 支持 |
| 精确日历文件发生一次 errno 5 | W01—W03 | 支持 |
| 故障是永久 NFS 故障 | 无 | **不作主张** |
| 行情源为空或缺失 | 无；行情读取未到达 | **不作主张** |
| core/run 已建立 | W02、W06 | **否定** |
| 图/正式切片已产生 | W04—W07 | **否定** |
| 共同背景存在或不存在 | 无 | **不作主张** |
| 合格市场 T 为 0 | W04—W07 | 支持证据资格状态 |
| 当前应立即重派 | 无恢复证据；任务投入条款 | **否定** |
| 当前应触发投入复看 | I02、I04、I05 | 支持 |
| Owner 两层过程应替换 | 无市场实践 | **不作主张** |

## 7. Professional 本轮实物

- `REPORT.md`
- `WORKER_RESULT_CONSUMPTION.json`
- `BLOCKER_AND_REENTRY_DECISION.md`
- `KEY_T_STATE_TABLE.csv`
- `OWNER_PROCESS_FEEDBACK.md`
- `MANAGEMENT_TRIGGER_NOTICE.md`
- `ARTIFACT_MANIFEST.json`
- canonical `FULL_RESPONSE.md`、`QUESTION_WORK_RETURN.json`、`ROLE_RETURN.json`

## 8. 排除项

- R0005 45 天窗及旧工单执行资格；
- R0002 宽事件账本/全面审计工单；
- 外部行情或平行数据库；
- 以请求合同、路径存在、URL、退出码替代图数交付；
- 把 UNKNOWN、NOT_REACHED 或 NOT_GENERATED 改写为市场零值。
