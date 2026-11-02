# EVIDENCE_INDEX — BI-01-CO-05 Professional R0013

## 1. 证据等级

- `FORMAL_FACT`：当前有权 Git、任务或控制面实物直接提供。
- `WORKER_OBSERVATION`：获授权 Worker 在目标环境真实执行并回交。
- `MANAGEMENT_ADOPTED`：R0010 已正式采用的决定与退出边界。
- `PROFESSIONAL_CLASSIFICATION`：本轮对技术事实的业务资格、受影响结论和路线裁定。
- `UNKNOWN`：本次没有到达、没有读取或没有证明。
- `EXCLUDED`：按现行决定不得作为后继或事实来源。

## 2. 本轮身份、Binding 与运输

| ID | 等级 | 精确引用 | 用途 |
|---|---|---|---|
| I01 | `FORMAL_FACT` | `daowei2026/observe-iterate@b31486dc586985baadabaa9151cef4eeb509b497:runs/BI-01-CO-05/provenance/turns/R0013/FULL_ASSIGNMENT.md::full` | 本轮完整派发与 source_reads |
| I02 | `FORMAL_FACT` | `daowei2026/observe-iterate@601c05b92fe3debf8ce3e5e6ae83d5a27f3365b5:runs/BI-01-CO-05/provenance/turns/R0013/INVOCATION.json::full` | invocation、token、route、有效调用计数与 worker_result_commit |
| I03 | `FORMAL_FACT` | `daowei2026/observe-iterate@601c05b92fe3debf8ce3e5e6ae83d5a27f3365b5:runs/BI-01-CO-05/provenance/turns/R0013/DISPATCH.json::full` | 采用依据、完整 evidence refs 与 route |
| I04 | `FORMAL_FACT` | `daowei2026/observe-iterate@509ac0894a1c492846bc8c6b0e7d1ba7a2fa6eb5:runs/BI-01-CO-05/provenance/turns/R0013/SEND_RECEIPT.json::full` | 本轮真实发送记录，`state=COMMITTED`；不构成 Worker 业务认可 |
| I05 | `FORMAL_FACT` | `daowei2026/observe-iterate@2e34c004458e30d4bb02863def47514beb3a7ed7:runs/BI-01-CO-05/provenance/turns/R0013/WORKER_RESULT_TRANSPORT_CHECK.json::full` | 结果回原签发 Pro、18 文件哈希、无 pending queue |
| I06 | `FORMAL_FACT` | `daowei2026/observe-iterate@a6a8acf7fa65665218d0f2163598d434fb921b24:runs/BI-01-CO-05/01_当前任务.md::full` | 完整业务任务、触发、证据资格与两层过程 |

## 3. 管理采用与原工单

| ID | 等级 | 精确引用 | 采用内容 |
|---|---|---|---|
| M01 | `MANAGEMENT_ADOPTED` | `daowei2026/observe-iterate@0776c5645be4bf1d38c7151baa8662def243e26b:runs/BI-01-CO-05/reviews/management-R0010/DECISION.md::#reentry` | 只允许一次同路径条件重入；失败后回管理二选一 |
| M02 | `MANAGEMENT_ADOPTED` | 同文件 `#decision-summary` | 原 R0008 order 终态、无市场结论、成功后立即进业务观察 |
| M03 | `FORMAL_FACT` | `daowei2026/observe-iterate@ed0da9d0ff8974ac34ebbb290c859627bfdd6137:runs/BI-01-CO-05/artifacts/professional-R0011/WORKER_ORDER.md::full` | 新 order 身份、探针通过/失败分支、一次性额度与回交边界 |
| M04 | `FORMAL_FACT` | `daowei2026/observe-iterate@34198df6d4435feaa089baeae73e934559bd8b19:runs/BI-01-CO-05/artifacts/professional-R0008/build_bi01_co05_r0008_fullrange_chart_data.py::full` | 原全段脚本与固定业务参数 |
| M05 | `FORMAL_FACT` | `daowei2026/observe-iterate@b2b0883e54c0e8118f55357b82e3c79765a5c05e:runs/BI-01-CO-05/provenance/turns/R0012/ROLE_RETURN.json::full` | R0011 schema-valid Role Return；R0012 不计有效调用 |

## 4. Worker 真实执行证据

| ID | 等级 | 精确引用 | 事实 |
|---|---|---|---|
| W01 | `WORKER_OBSERVATION` | `daowei2026/observe-iterate@45e9f33474d8d36f4f9fa07a3f72824c710c0d46:runs/BI-01-CO-05/artifacts/worker-BI01CO05-FULLRANGE-CONDITIONAL-REENTRY-01/FULL_RESPONSE.md::full` | 完整执行叙述、阶段、已成/未成和退出边界 |
| W02 | `WORKER_OBSERVATION` | 同提交 `REENTRY_OUTCOME.json::full` | `FAILED_PROBE_EVIDENCE_INCOMPLETE`、open/read 0、full run false、额度耗尽 |
| W03 | `WORKER_OBSERVATION` | 同提交 `PROBE_RECEIPT.json::full` | launcher 时间、身份、mount、Python probe 未开始、session 143 |
| W04 | `WORKER_OBSERVATION` | 同提交 `EXECUTION_RECEIPT.json::full` | 实际命令、attempt 数、原脚本 hash、无 actual run/core/pages/data |
| W05 | `WORKER_OBSERVATION` | 同提交 `MOUNT_AND_IDENTITY.json::full` | 宿主身份和 `/m3varI` NFS source；非业务 Python 证据 |
| W06 | `WORKER_OBSERVATION` | 同提交 `BLOCKER_EVIDENCE.json::full` | launcher 中断、child wait、目标文件未 open/read、原因未知 |
| W07 | `WORKER_OBSERVATION` | 同提交 `SHA256SUMS::full` | 18 个回交实物的哈希清单 |
| W08 | `WORKER_OBSERVATION` | 同提交 `SESSION_EXIT_OBSERVATION.json::full` | 143、无 probe receipt、相关进程随后不存在 |
| W09 | `WORKER_OBSERVATION` | 同提交 `DEPENDENCY_BEFORE.json` 与 `DEPENDENCY_AFTER.json` | 依赖记录相同，原有差异未改 |

## 5. 专业与 Owner 方法来源

| ID | 等级 | 精确引用 | 使用点 |
|---|---|---|---|
| P01 | `FORMAL_FACT` | `professional/README.md@b6b344ef...::full` | Professional 探索职责与动态工作面 |
| P02 | `FORMAL_FACT` | `professional/exploration/00_BUSINESS_OBJECTIVE.md@b6b344ef...::full` | 投资用途与合法无候选边界 |
| P03 | `FORMAL_FACT` | `professional/exploration/01_EXISTING_FEATURES_AND_CAPABILITIES.md@b6b344ef...::full` | KLine/large/mid、方向、actual/confirm 边界 |
| P04 | `FORMAL_FACT` | `professional/exploration/03_TOOLING_AND_DATA_USAGE.md@b6b344ef...::full` | chart/pages/board、manifest/index、同 run/core 与正式数据 |
| P05 | `FORMAL_FACT` | `professional/exploration/05_OWNER_PROCESS_EXPLANATION.md@b6b344ef...::full` | as-of 第一层、中尺度第二层、更新与挑战 |
| P06 | `FORMAL_FACT` | `professional/exploration/06_EXPLORATION_STAGE_GOAL.md@b6b344ef...::full` | 当前长程目的、职责与新增分析边界 |
| P07 | `FORMAL_FACT` | `professional/exploration/07_图数准备工单约定.md@46563266...::full` | Pro 决定图数，Worker 只执行/修通/回交 |
| P08 | `FORMAL_FACT` | `runtime/operations/CASE_OBSERVATION_RUN_GUIDE.md@b6b344ef...::full` | Run 接线与技术结果回原 Pro |

## 6. 主张—证据映射

| 主张 | 证据 | 状态 |
|---|---|---|
| Worker 结果属于 R0011 新 order 并合法回原 Pro | I05、M03、W01—W04 | 支持 |
| launcher 入口尝试一次并会话返回 143 | W03、W04、W08 | 支持 |
| Python 探针实际开始 | W03、W06、W08 | **否定** |
| 精确日历文件本次被 open/read | W02、W03、W06 | **否定** |
| 本次复现 errno 5 | W03、W06 | **否定；errno 未取得** |
| 文件当前可读或不可读 | 无文件级读 | **不作主张** |
| `/m3varI` host mount 仍指向原 NFS source | W03、W05 | 支持；不等于文件可读 |
| 原 R0008 脚本字节或业务参数改变 | W01、W04、W09 | **否定** |
| full-range script 被运行 | W02、W04 | **否定** |
| actual run/core、图页或正式数据存在 | W01—W04 | **否定** |
| 市场无背景/无候选 | 无市场证据 | **不作主张** |
| 合格 market T 为 0 | W01—W04 | 支持证据资格状态 |
| 同路径重入额度已耗尽 | M01、M03、W01—W03、W06 | 支持 |
| 可签第三个同路径 Worker | M01、M03、W02 | **否定** |
| 当前需 Management 二选一决定 | M01、W02、I02 | 支持 |
| 本段投入复看触发 | I02、M05 | 支持：R0011+R0013 两次有效调用 |
| Owner 两层方法失败 | 无市场实践 | **不作主张** |

## 7. 本轮 Professional 实物

- `REPORT.md`
- `WORKER_RESULT_CONSUMPTION.json`
- `CASE_ROUTE_DECISION.md`
- `KEY_T_STATE_TABLE.csv`
- `OWNER_PROCESS_FEEDBACK.md`
- `MANAGEMENT_TRIGGER_NOTICE.md`
- `EVIDENCE_INDEX.md`
- `ARTIFACT_MANIFEST.json`
- canonical `FULL_RESPONSE.md`、`QUESTION_WORK_RETURN.json`、`ROLE_RETURN.json`

## 8. 排除项

- 第三个同路径 Worker 或旧 order 重派；
- 自动恢复、后台等待或无责任主体的环境修复；
- 复制日历、旧快照、替代 source/resolver 或平行数据入口；
- R0008 errno 5 作为本次文件级事实；
- `bytes_read=0` 作为文件大小；
- host mount 作为业务 Python 文件读取；
- 无图数时的市场或方法结论。
