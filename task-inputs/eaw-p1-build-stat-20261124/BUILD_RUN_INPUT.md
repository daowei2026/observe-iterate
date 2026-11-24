# EAW P1 Build｜统计驱动单 Feature 闭环输入

> **输入准备稿，不是 Run 已启动的事实。** 本文件只规定目标、正式实例和业务边界。工作流程、专业方法、派送及恢复直接按本次精确采用的 Control／Skills／longrun，不再在这里复制。

## 1. 目标 Feature

```yaml
use_case: EAW P1
feature: BuildAssembler
business_name: Build｜一堵 exact Wall 周围的加固活动
target_tis: daowei2026/tis@179016111ed0394f92025313e46bd13534932a74
target_branch_at_start: codex/wall-output-consistency-20261121
code: hf/prel0/build_assembler.py
core: hf/prel0/build_assembler_core.py
constructor: mquant.tis.hf.prel0.build_assembler.BuildAssembler
parameter_instance: build-default  # 当前代码默认实例，运行前核完整 ppdict／ppid
formal_product_kind: build_activity
```

正式观察和闭环对象是 **BuildAssembler 及其当前公开产物**，包括一轮 Build 的 Start、Milestone、Stop、对应 wall_ref、状态和 receipt。Build 内部使用 transient active flow 等输入，不单独启动 Attack、Absorb、F3/F4 的其他 Feature Run。对应的 `EawP1BuildActivityFrp / BuildActivityDSU` 提供可核对的业务合同，不因此自动扩为另一个独立 FRP 运行任务。

## 2. 正式市场实例

```yaml
sof_name: TA_updto20240229_DBA
symbols: [rb, m]
requested_start_time: 2021-01-01
requested_end_time: 2021-12-31
calendar: night_end_at_2300
parameters: BuildAssembler 当前代码默认值；不凭输入草案重写具体参数
workspace: /dwdhome/fy/BASE_E6_2
```

数据范围沿用此前 EAW WALL／Absorb Run 的正式 rb/m、2021 全年实例。真实运行前核定实际模块路径、版本、参数序列化、数据范围、完整结果与公开表读回；局部窗口只能用于 `DIAGNOSTIC_ONLY`，不能代替全年正式 X/G。既有产物必须通过同版本／同实例／同范围／receipt／读回一致性验证后才可复用。

## 3. 上游和业务来源

**准确技术上游**：本 TIS commit 下的 `WallAssembler` 当前默认实例；相同 SOF、品种、全年范围、Calendar；核对 `wall_lifecycle` receipt、Wall 状态轨迹与 Build receipt 对上游的 exact 引用。Build 的 `_impl` 实际调用 `self.P.wall.run().F`，若匹配结果尚未物化，可在本 Run 内以不改变 Wall 业务行为为前提，合法物化并核验一次。旧 WALL 合理性 Run 终止、没有 WALL 完整合理性 Release；此技术消费不代表 WALL 业务已通过。

需直接阅读的原始业务来源（不以现有代码自动取代业务预期）：

- P1 六 Feature 与真实依赖：`daowei2026/feature-refinement-implementation-agent-evolution@8d58ddd3392a3e67ef5ba44adf2c4cd0c9077f9f:candidate_gold_cases/eaw/taskpacks_and_checkpoints/p1/EAW_P1_PREL0_BASE_PRODUCTS_ENGINEERING_DESIGN_AND_VCC_V1_6_1_20260818/02_FINAL_P1_ARCHITECTURE.md`
- Build DSU：`daowei2026/feature-refinement-implementation-agent-evolution@8d58ddd3392a3e67ef5ba44adf2c4cd0c9077f9f:candidate_gold_cases/eaw/taskpacks_and_checkpoints/p1/EAW_P1_PREL0_BASE_PRODUCTS_ENGINEERING_DESIGN_AND_VCC_V1_6_1_20260818/dsu/P1-DSU-02_Build_活动_DSU.md`
- Wall/Build/Absorb 生命周期：`daowei2026/feature-refinement-implementation-agent-evolution@8d58ddd3392a3e67ef5ba44adf2c4cd0c9077f9f:candidate_gold_cases/eaw/taskpacks_and_checkpoints/p1/EAW_P1_EXISTING_PREL0_BASE_PRODUCTS_AND_SPARSE_OCCURRENCE_V0_6_20260813/03_WALL_BUILD_ABSORB_LIFECYCLE_CONTRACTS.md`
- 原始 Build 组装器方法：`daowei2026/feature-refinement-implementation-agent-evolution@8d58ddd3392a3e67ef5ba44adf2c4cd0c9077f9f:candidate_gold_cases/eaw/preL0_source_materials_20261102/原文快照/mquant/ssot/eaw/03_assemblers_Wall_Build_Absorb_Attack_Exhaustion.md`
- FRP P1 合同参考（不预判已执行）：`daowei2026/frp@cac6c912dd65a14acbd591ca57e0afd8ddb4ef13:src/Frp/Instance/ISL/Eaw/P1/BuildActivity.hs`

## 4. 当前业务目标及修改边界

在现行统计驱动单 Feature Workflow 下，先完成 U 理解、X 正式运行、G 全量统计并发现高置信不合理现象；有 finding 时按 D Skill 定位最早责任逻辑，必要时修正并在后续轮次重跑、重统计。具体分析方法和输出合同以 Skills 为准，不在本输入给出固定统计指标、预判结论或新的专业 Gate。

**允许修改：** Build 自己的专属实现 `build_assembler.py`、`build_assembler_core.py`、与其直接对应的测试及本 Feature 参数／业务常量（需要实际诊断证据）。**禁止修改：** Wall、F3/F4、Attack、Absorb、共享处理模块、上游市场数据、FRP 其他 Feature 或上游业务规则／参数。发现上游错误只形成有据 `UpstreamFinding`，注明 Build 影响、缺口和恢复条件；不在本 Run 修复上游，也不以改坏 Build 来绕过错误。

工作区必须在首次 GO 前由主控核实为**没有其它活跃 Run 写者**的 `/dwdhome/fy/BASE_E6_2`；此前 Absorb Run 也绑定此目录，GitHub 上仍缺终结证据。主控不得强行结束旧 Run、覆盖修改或假定目录已释放。Build Run 只启动一个；不注册 Attack／Absorb 新 Run。

完成时由本 Run 依据最新有效的 X/G/finding 证据形成 `FeatureReleaseGate` 及必要的精确 `UpstreamReleasePackage`，并维护 `BUSINESS_PROGRESS.md` 与 `TASK_PROGRESS.md`。不把未修复的本轮高置信问题自行改称已接受限制。