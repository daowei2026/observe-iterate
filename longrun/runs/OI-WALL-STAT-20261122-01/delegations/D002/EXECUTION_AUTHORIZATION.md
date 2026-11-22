# D002｜既定 L0 X 及 G 的实际操作授权

签发者、接收者、原发行 C、操作和写面均使用同目录 `DELEGATION.json` 的原 V2 字段。本文件是该 D 的执行授权说明，不新增 Skill、W 或传输 schema。

授权来源：

- Owner 原 GO：`daowei2026/observe-iterate@6ba49120d4b620b48c93c76bc9dcdbafc3bf357c:longrun/runs/OI-WALL-STAT-20261122-01/OWNER_START.md`
- 最新继续指令的逐字发布原件：`daowei2026/observe-iterate@64469aed9f7205736ac33ea17d38552226c39742:longrun/runs/OI-WALL-STAT-20261122-01/calls/C0003/FULL_ASSIGNMENT.md`
- 原 Binding：`daowei2026/observe-iterate@be01e3ac9e46a046bbe2352d81104cd87b567039:longrun/runs/OI-WALL-STAT-20261122-01/RUN_BINDING.json`
- 同提交的 `RUN_RESOURCE_BINDING.json`；已采用 `87b951bbd15078a2d6353bdd24afe0d8f19c845c` 的 L0 X/G 及 CODEX_NATIVE_DIRECT。

| 原 grant.operation | 原 execution_context | 原 allowed_writes | 在本 D 中的用途 |
|---|---|---|---|
| `formal_feature_run` | `/dwdhome/fy/BASE_E6_2` | `/dwdhome/fy/BASE_E6_2` | 按锁定正式输入完成 L0 X；准确一致才复用，否则正式运行 |
| `run_result_statistics_analysis_write` | `/dwdhome/fy/BASE_E6_2` | `/dwdhome/fy/BASE_E6_2` | 本 Run 独立结果、统计脚本、日志、图表和分析报告 |
| `run_record_write` | `daowei2026/observe-iterate@codex/oi-wall-stat-20261122-01` | `longrun/runs/OI-WALL-STAT-20261122-01/**` | 提交和推送本 Run 专业产物、结果绑定和 V2 回交；executor 使用本 Run 独立记录 checkout |

每项授权 quote 均直接采用上述原 Binding 的 `authority_quote`，其 Owner 原文已存在。operation 编码与本 Run 记录路径是原授权的已确认作用域映射，不是新增权限。

WALL 正式运行的加载版本、默认参数、复用与重跑范围，以最新 Owner 原文第 3、5 项及单份 WALL BusinessTaskInput 为准；无需再次向 Owner 询问是否进入生产。正式 X 的加载／参数／输入／结果身份和资源单写者核验仍依原 GO 与资源绑定，由 controller/executor 按各自职责取得事实。

C0002 已报告的工作树差异及 U-C1..5 是本次输入。既有 wrapper 输入处理差异不因本 D 签发而获准采用；HEAD 一致不等于实际加载一致。现有差异按 X 的原定来源核验对账，不能假称已解除。只有推进确实需要新的正式行为或输入处理改变、超出现有授权或遇到无法消除的真实阻断，才按原控制面形成准确阻断／ModificationProposal 回 Owner；其余合法工作按最新 Owner 指令继续。

取得有效 X 绑定后，依 G 原生 G1/G2 就绪及分层合同进入完整统计；未暴露字段的处理仍服从 G Skill 和实践补充，不以补齐整套 U 代替 X/G。D1/D2/D4 作为既有正式修复输入复验，D3 仍按 Owner 暂缓决定处理。

此 D 是专业与操作派工，不构成真实发送、实际生产进程、共享写面锁、结果复用接受或 ReleaseGate。后继实际调用与物理回执仍由 controller 维护。
