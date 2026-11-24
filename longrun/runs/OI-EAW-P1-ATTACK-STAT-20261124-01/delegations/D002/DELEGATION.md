# D002｜首轮 X：运行正式 AttackFlowAssembler

## 身份与原 Workflow

- run_id：`OI-EAW-P1-ATTACK-STAT-20261124-01`；work_id：`OI-EAW-P1-ATTACK-STAT`；business_case_id：`EAW-P1-ATTACKSEGMENT`
- delegation_id：`D002`；issuer_call_id：`C0004`
- work_item_id：`OI-EAW-P1-ATTACK-STAT-X-R01`；阶段：首轮 X
- issuer / return_to：`codex:OI-EAW-P1-ATTACK-STAT-20261124-01:manager`
- recipient：本 Run 原 `codex:OI-EAW-P1-ATTACK-STAT-20261124-01:executor:E1`，复用原 E1
- execution_profile：`CODEX_NATIVE_DIRECT`；`workers=[]`
- 全 Run 专业控制 commit：`9877826236e0995e7255e6cbfedc2d1b89dea6da`
- 原 Workflow：`daowei2026/observe-iterate@9877826236e0995e7255e6cbfedc2d1b89dea6da:control/01_L0_统计驱动的单特征闭环.md` 的「X｜运行正式 Feature」。X 是原 L0 的实际工程操作，不是独立 Skill。

## 已有真实输入

- 唯一业务输入／当前正式实例：`daowei2026/observe-iterate@9877826236e0995e7255e6cbfedc2d1b89dea6da:task-inputs/eaw-p1-attack-stat-20261124/ATTACK_RUN_INPUT.md`
- 原 Owner GO：`daowei2026/observe-iterate@b912f85368fed916c45603c81aa8ef304bc146b6:longrun/runs/OI-EAW-P1-ATTACK-STAT-20261124-01/OWNER_START.md`
- 已消费的 D001 原生 U 包：`daowei2026/observe-iterate@758c77a566672a4514cbff6d3f26236769d17b59:longrun/runs/OI-EAW-P1-ATTACK-STAT-20261124-01/professional_results/D001/FeatureUnderstandingPackage.json`
- 阅读版：`daowei2026/observe-iterate@758c77a566672a4514cbff6d3f26236769d17b59:longrun/runs/OI-EAW-P1-ATTACK-STAT-20261124-01/professional_results/D001/FeatureUnderstandingPackage.md`
- U 的未完成范围及下游使用资格：`daowei2026/observe-iterate@758c77a566672a4514cbff6d3f26236769d17b59:longrun/runs/OI-EAW-P1-ATTACK-STAT-20261124-01/professional_results/D001/REMAINING_SCOPE.md`
- 原执行报告：`daowei2026/observe-iterate@758c77a566672a4514cbff6d3f26236769d17b59:longrun/runs/OI-EAW-P1-ATTACK-STAT-20261124-01/calls/C0002/EXECUTOR_REPORT.md`
- 有效补正 Return：`daowei2026/observe-iterate@72f33ce96e78653cfd94ae9fba0579fe50548848:longrun/runs/OI-EAW-P1-ATTACK-STAT-20261124-01/calls/C0003/PRO_RETURN.json`

原 U 的 `completion_status=PARTIAL`，原生产物明确允许 X 继续；本 D 保留其缺口，没有将 U 改为 COMPLETE。C0003 仅补正原 D001 的机器回交，不是重做 U。当前没有本 Run 的正式 X 结果或 G。

目标、代码、构造参数、数据范围、技术上游及业务来源沿唯一输入和原 U 原件。产品字段可读性、exact Wall/F4 receipts 与运行事实的待核范围沿原 U 的未完成记录；未把历史候选或 Build 成果采纳为本次正式结果。

## 原生输出与后继

本项输出 `FeatureRunResultBinding`，工作内容、输入输出与进入后继的条件直接采用原 L0 的 X 定义、唯一业务输入及 Owner GO；不另写专业方法、实现步骤或验收清单。U 的保留缺口继续按其原件追踪。

回交对象为原 manager。D002 的发布不表示已物理派达或 Feature 已运行。

## 已覆盖的操作权限来源

- Binding：`daowei2026/observe-iterate@723d65a2ca4fbcf691e9a82eb153a21faae18390:longrun/runs/OI-EAW-P1-ATTACK-STAT-20261124-01/RUN_BINDING.json`
- Resource Binding：`daowei2026/observe-iterate@723d65a2ca4fbcf691e9a82eb153a21faae18390:longrun/runs/OI-EAW-P1-ATTACK-STAT-20261124-01/RUN_RESOURCE_BINDING.json`
- 当前调用任务：`daowei2026/observe-iterate@8125d58f976f7c4faa049f2777e835d7ffef4889:longrun/runs/OI-EAW-P1-ATTACK-STAT-20261124-01/calls/C0004/FULL_ASSIGNMENT.md`

机读权限沿 Owner/Binding 已有 `eaw-attack-execute-and-profile`、`eaw-attack-repair-and-publish`，写面为 copy 工作区和本 Run 记录分支。controller 的 Chat 归档与 Registry 维护权限不属于本 D。

controller 负责本 Run 原 E1 的实际派达及原有权限、工作区、物理审批与共享写面核验；准确协调事实见当前调用任务。本 manager 只签发与协调，不操作生产。
