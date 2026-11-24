# EAW P1 AttackSegment｜统计驱动单 Feature 闭环输入

> **仅为本次 AttackSegment Run 的业务输入，不代表 Run 已注册或执行。** 本文件只确定 Feature、代码／实例／数据来源和业务边界；Workflow、专业方法、角色职责、权限与恢复沿本 Run 实际采用的 Control、Skill 和 `longrun/`，不在输入中重写。

## 1. 目标 Feature

```yaml
use_case: EAW P1
feature: AttackFlowAssembler
business_name: AttackSegment｜围绕 exact Wall 的主动成交攻势段
target_tis: daowei2026/tis@179016111ed0394f92025313e46bd13534932a74
target_branch_at_start: codex/wall-output-consistency-20261121
code: hf/prel0/attack_flow_assembler.py
core: hf/prel0/attack_flow_assembler_core.py
constructor: mquant.tis.hf.prel0.attack_flow_assembler.AttackFlowAssembler
parameter_instance: attack-default  # 当前代码默认值；运行前核完整 ppdict／ppid
formal_products:
  - attack_segment
  - attack_formation_evidence
  - wall_relation_barrier
```

本次完整分析对象是 **`AttackFlowAssembler` 当前实例及其真实输出**。三个产品应区分：完整形成的 AttackSegment、形成过程相关材料、正式 Wall 关系／屏障事件；不要混成同一种业务 occurrence。对应的 `EawP1AttackSegmentBookFrp / AttackSegmentBookDSU` 是业务合同和下游产品结构的阅读来源，**不因此自动启动另一条 FRP／P2 独立流程**。

## 2. 正式市场实例

```yaml
sof_name: TA_updto20240229_DBA
symbols: [rb, m]
requested_start_time: 2021-01-01
requested_end_time: 2021-12-31
calendar: night_end_at_2300
parameters: AttackFlowAssembler 当前代码默认实例（不凭本输入重新发明参数）
workspace: /dwdhome/fy/BASE_E6_2_copy
```

正式品种／时间沿用前一项 Build 任务与 EAW 2021 全年范围。本次单 Run 的业务目标是：在该正式范围运行真实市场数据，对 AttackSegment 产物进行全量统计与高置信不合理现象发现，对 finding 定位最早责任逻辑并在本 Feature 范围内迭代。局部短窗口仅可标记 `DIAGNOSTIC_ONLY`，不能代替全年正式 X/G。旧结果只有同代码、完整参数、源范围、receipt／artifact 身份及公开表读回都一致才允许复用。

## 3. 准确的上游及业务来源

**技术上游**为同 TIS commit、同正式 SOF、品种、期间和 Calendar 的 `WallAssembler` 默认实例（`wall_lifecycle` receipt、`wall_assembler_state_trace` 及 Wall sparse events），以及本 Attack 实例明确选择的两组 `DirectedBigDealTick`／F4：

- tactical：当前默认 `DirectedBigDealTick()`；
- structural：当前默认 `DirectedBigDealTick(parameter_set_id="structural-default", qualification_family="structural", lane_threshold_map={"structural": ["0.997", "0.999"]})`；
- `additional_directed_large_deal_features=()`（默认）。

这些是**当前代码的默认接线线索**，最终以真实 `ppdict`、实际加载模块、两组 F4 的 source scope、receipts 和完整读回为准。下游 Attack 自身不消费 Build 或 Absorb 的正式结果。Wall／F4 已物化的合格结果可复用；缺结果时允许按锁定代码与参数作必要技术物化，但不是重跑它们的业务合理性 Workflow，也不允许修改其实现。

业务原文／合同应由执行者亲自读取（不以实现事实替代设计预期）：

- P1 Feature 及依赖：`daowei2026/feature-refinement-implementation-agent-evolution@8d58ddd3392a3e67ef5ba44adf2c4cd0c9077f9f:candidate_gold_cases/eaw/taskpacks_and_checkpoints/p1/EAW_P1_PREL0_BASE_PRODUCTS_ENGINEERING_DESIGN_AND_VCC_V1_6_1_20260818/02_FINAL_P1_ARCHITECTURE.md`
- AttackSegment DSU：`daowei2026/feature-refinement-implementation-agent-evolution@8d58ddd3392a3e67ef5ba44adf2c4cd0c9077f9f:candidate_gold_cases/eaw/taskpacks_and_checkpoints/p1/EAW_P1_PREL0_BASE_PRODUCTS_ENGINEERING_DESIGN_AND_VCC_V1_6_1_20260818/dsu/P1-DSU-03_贴墙攻势段簿_DSU.md`
- 原始组装器定义：`daowei2026/feature-refinement-implementation-agent-evolution@8d58ddd3392a3e67ef5ba44adf2c4cd0c9077f9f:candidate_gold_cases/eaw/preL0_source_materials_20261102/原文快照/mquant/ssot/eaw/03_assemblers_Wall_Build_Absorb_Attack_Exhaustion.md`
- FRP P1 合同参考（不是已验收运行事实）：`daowei2026/frp@cac6c912dd65a14acbd591ca57e0afd8ddb4ef13:src/Frp/Instance/ISL/Eaw/P1/AttackSegmentBook.hs`

## 4. 本轮修改边界与完成

按现行统计闭环 Control 进行首轮 U、X、G；发现高置信 finding 时由 D Skill 诊断，再在授权范围内处理并进行后续轮次。统计选择、诊断方法、专业完成和结果合同由 Skills 本身规定，不再列固定统计清单或预期 finding 结论。

**仅允许修改 AttackSegment 自己的** `hf/prel0/attack_flow_assembler.py`、`hf/prel0/attack_flow_assembler_core.py`，以及直接针对本 Feature 的测试和本 Feature 专属参数／业务常量。**禁止修改** Wall、DirectedBigDealTick／F4、Build、Absorb、市场数据、共同处理器、其它上游 Feature 或 FRP 相关公共合同。若发现真正问题位于上游，则生成 `UpstreamFinding`，注明真实证据和对 Attack 的影响；不抢改上游，也不错误宣布 Attack 已完成。

工作区 `/dwdhome/fy/BASE_E6_2_copy` **由 Owner 在本次启动前说明已释放**。主控仍需在注册／建角色线程前核实目录存在、realpath、旧 F/Q/V 或其他 Run 确无活跃写者、实际 Git 工作树和外部共享写面。与 Build 使用的 `/dwdhome/fy/BASE_E6_2` 必须实证不重叠；如两者共用外部数据库／缓存写面，仅该具体写入按真实单写者管理，其余独立工作可以并行。

此前 WALL 合理性 Run 已停止、未形成完整 `FeatureReleaseGate`；本次明确允许已修复且有 exact receipt 的 Wall 作为**技术上游**，但不虚构其全面合理性已验收。Attack 当前有效成果满足本轮 ReviewTarget 后，按现行 Workflow 形成 `FeatureReleaseGate` 和必要的 `UpstreamReleasePackage`。业务进展与机器恢复分别维护 `BUSINESS_PROGRESS.md`、`TASK_PROGRESS.md`。
