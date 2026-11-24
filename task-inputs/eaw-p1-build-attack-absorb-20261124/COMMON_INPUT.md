# 共同业务输入｜EAW P1 三个独立 Feature

## 1. 本次共同 ReviewTarget

对 Build 活动、AttackSegment 攻势段、Absorb 交互**分别**开展当前统计驱动单 Feature 闭环：

```text
核实当前代码／实例语义 → 运行真实正式实例 → 对正式结果全量统计并发现明显不合理现象
→ 对各 finding 追溯责任逻辑 → 在初始授权内必要修改 → 重跑重统计直到本轮完成判断
```

此处只定义业务目标，具体节点、轮次和专业完成方法由现行 `control/01_L0_统计驱动的单特征闭环.md`、`skills/feature-understanding/`、`feature-global-behavior-profiling`、`business-discrepancy-diagnosis` 及适用实践补充决定。**不要求预先列出一套固定统计清单或先验问题结论。**

三线相互独立，但必须与同一准确 Wall 实例保持版本、参数、源范围和业务身份一致。每线独立形成理解、X、G、findings、Gate、必要 Release；一线阻断不阻断其它合法工作。

## 2. 真实产品结构与原始业务来源

正式 P1 架构：`daowei2026/feature-refinement-implementation-agent-evolution@8d58ddd3392a3e67ef5ba44adf2c4cd0c9077f9f:candidate_gold_cases/eaw/taskpacks_and_checkpoints/p1/EAW_P1_PREL0_BASE_PRODUCTS_ENGINEERING_DESIGN_AND_VCC_V1_6_1_20260818/02_FINAL_P1_ARCHITECTURE.md`

```text
exact Wall artifact → BuildAssembler
                   → AttackFlowAssembler (+ selected DirectedBigDealTick/F4)
                   → AbsorbAssembler

Build 内部计算 transient active flow；Absorb 还需要自己的 track / quote 输入。
三个下游 Feature 不消费彼此的正式产物。
```

其它业务定义按实际目标分别从以下原件读取，不能用当前代码行为替代原设计：

- Build：`daowei2026/feature-refinement-implementation-agent-evolution@8d58ddd3392a3e67ef5ba44adf2c4cd0c9077f9f:candidate_gold_cases/eaw/taskpacks_and_checkpoints/p1/EAW_P1_PREL0_BASE_PRODUCTS_ENGINEERING_DESIGN_AND_VCC_V1_6_1_20260818/dsu/P1-DSU-02_Build_活动_DSU.md`
- AttackSegment：`daowei2026/feature-refinement-implementation-agent-evolution@8d58ddd3392a3e67ef5ba44adf2c4cd0c9077f9f:candidate_gold_cases/eaw/taskpacks_and_checkpoints/p1/EAW_P1_PREL0_BASE_PRODUCTS_ENGINEERING_DESIGN_AND_VCC_V1_6_1_20260818/dsu/P1-DSU-03_贴墙攻势段簿_DSU.md`
- Absorb：`daowei2026/feature-refinement-implementation-agent-evolution@8d58ddd3392a3e67ef5ba44adf2c4cd0c9077f9f:candidate_gold_cases/eaw/taskpacks_and_checkpoints/p1/EAW_P1_PREL0_BASE_PRODUCTS_ENGINEERING_DESIGN_AND_VCC_V1_6_1_20260818/dsu/P1-DSU-04_Absorb_交互_DSU.md`
- 原设计和组装器：`daowei2026/feature-refinement-implementation-agent-evolution@8d58ddd3392a3e67ef5ba44adf2c4cd0c9077f9f:candidate_gold_cases/eaw/preL0_source_materials_20261102/原文快照/mquant/ssot/eaw/03_assemblers_Wall_Build_Absorb_Attack_Exhaustion.md`
- Build／Absorb 生命周期：`daowei2026/feature-refinement-implementation-agent-evolution@8d58ddd3392a3e67ef5ba44adf2c4cd0c9077f9f:candidate_gold_cases/eaw/taskpacks_and_checkpoints/p1/EAW_P1_EXISTING_PREL0_BASE_PRODUCTS_AND_SPARSE_OCCURRENCE_V0_6_20260813/03_WALL_BUILD_ABSORB_LIFECYCLE_CONTRACTS.md`

## 3. 锁定的代码起点

```yaml
tis_repository: daowei2026/tis
tis_branch: codex/wall-output-consistency-20261121
tis_commit: 179016111ed0394f92025313e46bd13534932a74
frp_reference_repository: daowei2026/frp
frp_reference_commit: cac6c912dd65a14acbd591ca57e0afd8ddb4ef13
frp_reference_branch: eaw/p123-integration-20260820
```

**TIS commit 是三线正式 producer 起点；不得回退到 6618d4d 或旧 Wall 计算。** 该提交包含 2026-11-23 的 Wall 开盘全空半秒占位过滤修复。FRP commit 是 P1 typed ingress/DSU 合同的参考版本，真实 FRP 包装和运行依赖如实际启用必须核加载的代码与版本；不得仅因 TIS Python wrapper 存在就声称已成功执行 Haskell DSU。

代码入口：

```text
mquant.tis.hf.prel0.wall_assembler.WallAssembler
mquant.tis.hf.prel0.build_assembler.BuildAssembler
mquant.tis.hf.prel0.attack_flow_assembler.AttackFlowAssembler
mquant.tis.hf.prel0.absorb_assembler.AbsorbAssembler
mquant.tis.frp.EawBattleP  # 对应 P1 typed Fao/DSU 包装来源，仅供核合同
```

## 4. 共同正式实例范围（本批建议，随初始 GO 固定）

```yaml
sof_name: TA_updto20240229_DBA
symbols: [rb, m]
requested_start_time: 2021-01-01
requested_end_time: 2021-12-31
calendar: night_end_at_2300
parameters: 代码起点当前各 Feature 的默认正式实例；运行前保存完整 ppdict / ppid
```

来源是上一批 Absorb Run 的正式输入，而不是新发明的时间或品种。初始 GO 采用后不得静默缩短范围、切换到旧结果、改日历或改为人工构造输入。少量位置可以作 `DIAGNOSTIC_ONLY`，不能代替正式全年 X/G。

## 5. 共同 Wall 技术前置

三条线使用该 TIS commit 下的 **WallAssembler 默认正式实例**，与目标 Feature 完全相同的 SOF、rb/m、2021 全年及 Calendar。必须取得并验证确切的 `wall_lifecycle` receipt、产物与 `wall_assembler_state_trace`，并让下游 result receipts 明确引用准确 Wall 身份。

此前 WALL 合理性 Run 由 Owner 停止，没有 WALL 全面合理性 Release。**本次 GO 允许三线把修复后的 exact Wall 当作技术输入，但不得虚构其 FeatureReleaseGate，也不解除其业务限制**。旧 rb 部分结果或旧代码版本不可冒充当前 Wall。

如该 exact Wall artifact 不存在，先在已授权的单写者现场物化并验证一次；其余 Run 可以并行推进 U／代码与业务分析，但在 Wall 身份确定前不能启动依赖它的正式 X。多个 `_impl` 内会调用 `self.P.wall.run()`，不能由并行三个首次生产同时抢写相同 Wall 目录。所有共享缓存、DBA、输出和修复用的 Git 分支需要在写前核单写者；共同上游共享只读，不共享三个目标 Feature 的正式写面。

## 6. 范围边界

本次三个目标不需要互相的 FeatureReleaseGate；各自的 Release 只由当前本 Feature 的真实证据和当前 ReviewTarget 决定。输出结果及可能修改不可不标版本地跨 Run 混用。历史分析、CAEGraph 数据和归档 Chat 可以作为线索，不能冒充本轮 X/G。

Owner 本次明确把**正式修改权限限制为本 Run 所负责的目标 Feature 自身**：Build 只修 Build，Attack 只修 AttackSegment，Absorb 只修 Absorb。允许目标 Feature 自己的源码、默认参数和本 Feature 专属业务常量、测试与自身结果修正；**不允许修改 Wall、F3/F4、市场数据、公共处理器或其他 Feature 的源码、参数、业务规则和输出合同**，也不允许为修自己的问题顺带改这些共享实现。

技术上必须读取或者一次性物化已锁定的 Wall/F4 等上游结果时，允许按原实例运行／读回（不可改其算法和参数）；若诊断确认真实问题位于上游，形成准确 `UpstreamFinding`，记录证据、受影响本 Feature 结果与需未来单独处理的来源，不执行上游修改、不把上游缺陷冒充本 Feature 修复成功。不能在本次任务中自行扩大修改范围。Manager 只依据既定 Workflow 和 Skill Return 协调；超范围动作只局部阻断，不引入运行中 Owner 确认。
