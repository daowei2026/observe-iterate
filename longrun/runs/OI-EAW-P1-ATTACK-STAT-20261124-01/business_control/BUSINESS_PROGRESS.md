# BUSINESS_PROGRESS｜AttackSegment 统计驱动闭环

## 当前任务与业务位置

目标仍为 EAW P1 AttackFlowAssembler 当前默认实例，在 rb、m 的 2021 全年正式市场范围完成统计驱动闭环。[唯一业务输入](https://github.com/daowei2026/observe-iterate/blob/9877826236e0995e7255e6cbfedc2d1b89dea6da/task-inputs/eaw-p1-attack-stat-20261124/ATTACK_RUN_INPUT.md)与专业控制 commit `9877826236e0995e7255e6cbfedc2d1b89dea6da` 不变。

原 E1 已形成部分有效 X 成果：**rb 当前三产品的 35 张公开表严格读回有效**；m Wall 已有当前版本 receipt 和 5 张公开表读回。m 两组 F4 与 Attack 在运行上下文补正后仍未执行，最新 A04 未获共享生产锁并已结束。

当前原生绑定为 `INCOMPLETE_WAITING_SHARED_LOCK`，`formal_complete=false`、`eligible_for_G=false`。原 U 保持 PARTIAL；完整 rb/m X、G、finding 诊断和 Feature 释放尚未完成。

## 有效成果与适用范围

| 成果 | 已核事实与当前用途 | 原件 |
|---|---|---|
| Feature 理解 | 主要实现链、业务对象、事件、参数和公开布局已说明；PARTIAL 与全部具名未知保留 | [原 U 包](https://github.com/daowei2026/observe-iterate/blob/758c77a566672a4514cbff6d3f26236769d17b59/longrun/runs/OI-EAW-P1-ATTACK-STAT-20261124-01/professional_results/D001/FeatureUnderstandingPackage.json) |
| rb Attack 三产品 | A03 已生产；R01 用当前代码、默认参数、完整正式范围和本 Run exact 上游作只读完整重算，经原 dump 转换后按列名逐列全量读回，35 表一致；原 artifact／receipt 元数据未变 | [C0007 完整原生绑定](https://github.com/daowei2026/observe-iterate/blob/0837509a7200dcffcfced4113cab22ec575bdcce/longrun/runs/OI-EAW-P1-ATTACK-STAT-20261124-01/professional_results/D002/C0007/FeatureRunResultBinding.json) |
| rb 技术输入 | Wall、tactical F4、structural F4 均有本 Run 当前版本生产及完整读回记录 | 同一原生绑定 |
| m Wall | 当前版本 receipt 及 5 表读回已有记录；A04 计划的补正上下文只读复核尚未执行 | 同一原生绑定及 [执行报告](https://github.com/daowei2026/observe-iterate/blob/0837509a7200dcffcfced4113cab22ec575bdcce/longrun/runs/OI-EAW-P1-ATTACK-STAT-20261124-01/calls/C0007/EXECUTOR_REPORT.md) |
| m F4／Attack | 运行交易集遗漏已在 X 工程内只读核实并完成补正前检；补正后的实际生产与读回仍待资源恢复 | [原剩余范围与恢复](https://github.com/daowei2026/observe-iterate/blob/0837509a7200dcffcfced4113cab22ec575bdcce/longrun/runs/OI-EAW-P1-ATTACK-STAT-20261124-01/professional_results/D002/C0007/REMAINING_SCOPE.md) |

这些是当前版本的运行和读回事实，尚未形成全量行为统计或合理性结论。rb 局部有效成果不代替完整 rb/m 正式 X，也不赋予 G 资格。复用范围沿原生结果及完全同一性核验，不消费 Build 业务成果。

## 工程错误、纠正和保留边界

- A01 未持锁、未执行 Feature；原记录保留。
- A02 实际取得并释放原锁，在任何 Feature 开始前因运行器配置断言结束；原脚本和错误保留。后续运行器框架类名匹配作了工程纠正，未改产品代码、参数或正式范围。
- A03 已生产部分结果。rb 原生产读回的列顺序断言和 journal 保留；R01 的只读补充按列名完整核对既有结果，确认 artifact、receipt 和文件状态未变后，作为 rb 有效读回依据。
- m 两组 F4 的 A03 异常由原 E1 在 X 工程内核实为运行脚本沿用默认 `black` 交易集，未包含正式输入已有的 m。现有原生 `m.csv` 的上下文前检已通过；Feature 默认业务参数、市场数据、正式品种、期间、SOF 和日历均未变。
- A04 未获同一原锁，runner 已结束；未执行补正上下文后的 m Wall 只读复核、两组 F4 或 Attack，m 新目标仍未产生结果。

上述处理是原 X 工程执行和回交事实，没有升级为业务 finding、专业诊断、产品修复或上游修改许可。A01/A02/A03/R01/A04 原件和原错误均保留。

## 业务理解与未决

原 U 说明完整 AttackSegment 在真实闭段时发布，`business_end` 与 `closed_at` 分别保留；形成材料、完整段和正式 Barrier 的角色与计数粒度不同，Barrier 当前来自 exact Wall.End；双 lane overlap 不能直接相加为段总量，物理 chunk 边界不自动形成完整段。

原 U 的 NOT_EXPOSED、分支可达性、参考 TIS/FRP 合同及职责差异、最早信息可得时间等仍按原件保留。部分 X 的有效读回不将 U 自动改为 COMPLETE。尚无正式高置信 finding、DiagnosisReport、FeatureReleaseGate 或 UpstreamReleasePackage；旧 WALL 合理性 Release 的未完成事实不变。

## 当前等待与下一合法动作

同一生产锁最近由另一获准生产者持有，当前不重复强启动新的等待尝试。恢复直接沿 [C0007 原 continuation](https://github.com/daowei2026/observe-iterate/blob/0837509a7200dcffcfced4113cab22ec575bdcce/longrun/runs/OI-EAW-P1-ATTACK-STAT-20261124-01/professional_results/D002/C0007/REMAINING_SCOPE.md)：controller 核原锁自然释放、A04 终态／未持锁／未执行 m 及新目标状态后，以新 C 和新 attempt 在原 E1 续接仍未完成的 m 范围。原 D002 的签发调用保持 C0004，不新增 D、Skill、Gate、Worker 或 Owner 节点。

完全同一性已核的本 Run 结果保留复用；原尝试与既有结果不覆盖，未执行工程继续按原工作处理。实际锁与源工作区由 controller 核实，manager 只协调。Build 按自身 Run 的专业版本和产物独立继续。

- [运行状态、准确版本与恢复](TASK_PROGRESS.md)
- [本次 manager 报告](../calls/C0008/MANAGER_REPORT.md)

快照：2026-11-24，C0008 已消费原 E1 的部分 X，本次报告、双进度与 manager Return 已发布并准确回读，实际发行引用见 TASK_PROGRESS。父 Run IN_PROGRESS，当前等待 m 剩余工程合法恢复。
