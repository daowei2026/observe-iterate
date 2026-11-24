# D001｜首轮 U：理解 AttackFlowAssembler

本 D 绑定一项原 Skill 工作，专业输出与完成条件直接采用锁定 Skill 原文。

## 身份与回交

- run_id：`OI-EAW-P1-ATTACK-STAT-20261124-01`
- work_id：`OI-EAW-P1-ATTACK-STAT`；business_case_id：`EAW-P1-ATTACKSEGMENT`
- work_item_id：`OI-EAW-P1-ATTACK-STAT-U-R01`；阶段：首轮 U
- delegation_id：`D001`；issuer_call_id：`C0001`
- issuer / return_to：`codex:OI-EAW-P1-ATTACK-STAT-20261124-01:manager`
- recipient：`codex:OI-EAW-P1-ATTACK-STAT-20261124-01:executor:E1`
- profile：`CODEX_NATIVE_DIRECT`；`workers=[]`

## 准确 Skill 与适用补充

- Skill：`daowei2026/observe-iterate@9877826236e0995e7255e6cbfedc2d1b89dea6da:skills/feature-understanding/SKILL.md`
- 业务对象判别补充：`daowei2026/observe-iterate@9877826236e0995e7255e6cbfedc2d1b89dea6da:skills/feature-understanding/BUSINESS_OBJECT_QUALIFICATION_GUIDE.md`
- 内部 Workflow：`daowei2026/observe-iterate@9877826236e0995e7255e6cbfedc2d1b89dea6da:skills/feature-understanding/WORKFLOW.md`
- 字段级 IO：`daowei2026/observe-iterate@9877826236e0995e7255e6cbfedc2d1b89dea6da:skills/feature-understanding/IO_SPEC.md`
- 已采用 L0：`daowei2026/observe-iterate@9877826236e0995e7255e6cbfedc2d1b89dea6da:control/01_L0_统计驱动的单特征闭环.md`
- executor 指南：`daowei2026/observe-iterate@9877826236e0995e7255e6cbfedc2d1b89dea6da:longrun/professional/PRO_EXECUTOR_GUIDE.md`
- 全 Run 专业控制 commit：`9877826236e0995e7255e6cbfedc2d1b89dea6da`

## 当前真实输入

唯一业务输入：`daowei2026/observe-iterate@9877826236e0995e7255e6cbfedc2d1b89dea6da:task-inputs/eaw-p1-attack-stat-20261124/ATTACK_RUN_INPUT.md`。Feature、正式实例、业务原文与合同来源、技术上游、数据范围及修改边界均由此原件及 Owner GO 确定。

目标为 `mquant.tis.hf.prel0.attack_flow_assembler.AttackFlowAssembler` 当前默认实例 `attack-default`：

- `daowei2026/tis@179016111ed0394f92025313e46bd13534932a74:hf/prel0/attack_flow_assembler.py`
- `daowei2026/tis@179016111ed0394f92025313e46bd13534932a74:hf/prel0/attack_flow_assembler_core.py`

当前尚无本 Run 的 FeatureUnderstandingPackage、正式运行绑定、统计、诊断或 Release；exact Wall、F4 tactical/structural 的 receipts、完整参数及正式结果读回尚未核实。工作区核验原件为 `daowei2026/observe-iterate@16a40c67ee5c63db853a9f27a8a210a13bb6526b:longrun/runs/OI-EAW-P1-ATTACK-STAT-20261124-01/WORKSPACE_VERIFICATION.md`。未将 Build 的线程、结果或完成状态作为本 D 输入。

## 原生输出

`FeatureUnderstandingPackage` 及其完成状态直接遵循 Skill、WORKFLOW、IO_SPEC 和适用补充；本 D 不另设专业方法或验收条件。

## 已覆盖的权限来源

- Owner GO：`daowei2026/observe-iterate@b912f85368fed916c45603c81aa8ef304bc146b6:longrun/runs/OI-EAW-P1-ATTACK-STAT-20261124-01/OWNER_START.md`
- Binding：`daowei2026/observe-iterate@723d65a2ca4fbcf691e9a82eb153a21faae18390:longrun/runs/OI-EAW-P1-ATTACK-STAT-20261124-01/RUN_BINDING.json`
- 资源和写面：`daowei2026/observe-iterate@723d65a2ca4fbcf691e9a82eb153a21faae18390:longrun/runs/OI-EAW-P1-ATTACK-STAT-20261124-01/RUN_RESOURCE_BINDING.json`

本 D 机读权限使用 Binding 已有的 `eaw-attack-execute-and-profile`、`eaw-attack-repair-and-publish`，写面为 copy 工作区与本 Run 记录分支；具体工作仍为上述单项 U Skill。controller 的 Chat 归档授权不属于本 D。D 的发布不表示 E1 已创建或已物理接收；物理线程、模型、工作区、权限和派达由 controller 核实。
