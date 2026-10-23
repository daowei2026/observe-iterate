# BI-01 V2 业务起点：复用原 I1/I2/I3 已积累的业务认识

> **历史参考资料（非现行执行合同）**：本文件原属于 V2 S1–S3 方法；当前仅按具体特征需要参考其中的业务知识。旧固定数据、阶段目标、操作方式及 GO/Gate 不能直接适用于 BI-01-FO-01；现行任务以已采用的 `professional/feature_observation/` 与 FO-01 Binding 为准。

## 0. 本文的来源与权限

**本文件保存的是已积累的业务内容、Source 和方法背景，不是旧版运行状态的迁移。** 当前新运行准备为 `BI-01-V2-02`，需未来真实 Owner GO；上一 `BI-01-V2-01` 已由 Owner 暂停，原 `BI-01-RESTART-01` 亦是更早的历史。旧运行的 Gate、聊天、Owner 授权、已采用 Task/Workmap、在途、预算或执行结果不自动进入新运行；仅可将明确来源的业务知识、原图和真实数据作为历史证据核实后使用。

首要完整来源（旧版原始讨论而非后来精简的运行摘录）：
- `daowei2026/complex-systems-vocabulary@fix/work-order-boundary-part-a-20260909`
- `docs/network-dynamic-ceps-factory/capital-management-purpose/discuss-materials/U2U3首轮业务观察实例上下文_20261010/01_首轮实例及子意图1至3上下文.md`，源 blob `5bd81ef05dce01ac36704085d71221c958907b93`。
- 对应 `00_长程任务总意图与六个子意图.md` 源 blob `d77c14e1564c2c751699073853887cfab9ce3ae6`，此文件的 **AI/Owner 角色导向总意图已经被 V2 重新表述**，旧六阶段不再生效。
- 具体 U2/U3 原业务决策与设计从 `daowei2026/complex-systems-vocabulary@48f55f53e25d04e5b4b59fae1e652dd4b679c9d3` 的 `docs/network-dynamic-ceps-factory/` 读取；需核原文件正文，不由此摘要取代方法。

这些旧业务底稿保留的是**原本为什么要观察、对象关系、方法边界和数据事实**；原文写的“G1/G2/G3 初步完成”不能自动移作本次 V2 Gate 通过。

## 1. 原 I1：观察问题为什么选这里

- 业务实例：`BI-01`（观察 U2 单尺度机会组织及 U3 成员差异，不等于某个 Case 或 run）。
- 首轮研究点 `OP-01`：U2 从实际转折/NodeBehavior 走向 Same-Round Formation、Post-Turn Organization 和 OpportunityCluster 的首次多对象机会边界，再观察 U3 对成员差异的解释。
- 核心问题 `Q-01`：同一轮转折或相近位置的成员在方向推进、路径摩擦、保留和 Episode 生命周期上如何分化？U2/U3 是否比只看单品种或静态板块多提供了有用认识？
- 选择依据：U2 应回答哪些对象实际上属于同一机会及重复暴露边界，不应把同轮发生本身当作好做；U3 再评估运动质量/后续结果及可用证据；rb/hc/i 有完整的真实上游样本和事先验算的参考 CSV，可直接入手。
- 有价值的结果包括识别错组、未达到机会资格、U3 增量不足、重复表达或不确定性，而不只期待肯定 U2/U3。
- 原首轮曾优先 U3-A Movement，**本次 Owner 已将业务问题扩展为“这些位置 U3 四方面能否辨别品种好不好做”**；不得用旧 OP-01 优先顺序擅自取消新范围，也不得把未产生的数据说成已具备。

## 2. 原 I2：已有的业务设计、处理依赖和方法边界

基本依赖关系：

```text
真实 rb/hc/i 30m KLine、Zig、小尺度转折来源
    ↓
U2 C0：Source Confirmation、TurnOccurrence、SegmentEpisode、Episode Metrics
    ├─ N：NodeScaleTurnBehavior
    ↓
U2 C1：同轮/成对 Typed Relation 与 Formation、Qualification、Validity
    ├─ S：External Separation/组外、持续性参考
    ↓
U2 C2：OpportunityCluster 候选 Gate、正式 Commit 资格（不可自动混同）
    ↓
单尺度 U2→U3 ReferenceOnly/Shadow 桥（**不是正式 H1**）
    ↓
U3 R02：各 As-Of 成员 Movement 的 Progress/Friction/Retention 等客观事实
    ↓
U3 R03：Quality / Allocation 的可用或 Withheld 状态
```

基本立场：

1. **原业务职责**由 Owner 决定与 U2/U3 用例、叙事合同约束，不能由某个 CSV 名字反推完整业务定义。U2 与 U3 责任分层，不能把机会簇身份等同于运动质量排序。
2. **正式 Source 与参考方法分开**。原 U2 First Edition 候选采用名义 Δ 相关约束，原第 14 轮单尺度 Shadow Reference 为尽快验算而暂取 Δ=2 根实际 30m bar，并定义转折邻域 4 bar、Epoch 12 bar、Working 4 bar、S K=3、持续观察 8 bar 等参考处理。它不能冒充正式 Mission C 生效参数；几何/类别同源不算独立共证。
3. **时间语义分开**：actual turn、确认/知识时间、As-Of，WorkingSoFar/Completed 与结果可见性；不能把事后走势反馈写回历史 Current。
4. **增量价值基线**：只看单品种事实 → 静态品种分类/同属板块 → 加 U2 真实组织 → 再加 U3 质量证据，比较究竟改善了哪个业务判断。
5. U3 有两套容易混淆的“四”：U3 用例卡 §4.2 的四个 Movement Evidence Bundles（Progress、Friction、Retention、Observability/Constraint）以及 §1.2 的四类 Allocation Evidence（Group Budget、Member Relative、Repeated Exposure、Uncertainty Holdback）。本轮要辨别“品种好不好做”的具体四方面，应在 S1 依据 Owner 目标、正式定义及**这两份固定输入实际上计算出的字段**建立明确映射；两套“四”不可无声替换。

原参考方法和具体角色来源：
- U2/U3 资金边界：[Owner Decision](https://github.com/daowei2026/complex-systems-vocabulary/blob/48f55f53e25d04e5b4b59fae1e652dd4b679c9d3/docs/network-dynamic-ceps-factory/OD_U2_U3_CAPITAL_VALUE_AND_ITERATION_DECISIONS_V0.1.0.md)
- [U2 Use Case](https://github.com/daowei2026/complex-systems-vocabulary/blob/48f55f53e25d04e5b4b59fae1e652dd4b679c9d3/docs/network-dynamic-ceps-factory/U2_OPPORTUNITY_CLUSTER_SCALE_TURN_USE_CASE_CARD_V0.4.0.md)
- [U3 Use Case](https://github.com/daowei2026/complex-systems-vocabulary/blob/48f55f53e25d04e5b4b59fae1e652dd4b679c9d3/docs/network-dynamic-ceps-factory/U3_MOVEMENT_QUALITY_ACTIVITY_CONVERSION_ALLOCATION_USE_CASE_CARD_V0.4.0.md)
- [U3 Narrative](https://github.com/daowei2026/complex-systems-vocabulary/blob/48f55f53e25d04e5b4b59fae1e652dd4b679c9d3/docs/network-dynamic-ceps-factory/U3_MOVEMENT_QUALITY_ACTIVITY_CONVERSION_ALLOCATION_NARRATIVE_SPEC_V0.3.0.md)
- **直接的 [06 U2/U3 叙事与具体设计 Source 导航](06_U2_U3_DESIGN_SOURCE_MAP.md)** 汇总了 U2/U3 人读 Narrative、用例详细设计、Source/Metric/Step Witness，以及 C0/N、C1/S/C2、U3 Movement Local Contract 的已核精确来源。S1 判断业务预期时须从其入口进入原文；06 不能替代算法原文，也不能把历史候选当生产结果。

## 3. 原 I3：已经形成的实际业务事实和能/不能使用的范围

本次已提供一对互补数据包：上游原始 KLine/Zig/mid 与下游 **23 份事先参考计算 CSV**。原 I3 数据表的报告事实包括：
- 上游 rb/hc/i 每个品种 9,080 根 30m KLine；mid 转折分别 rb 363、hc 342、i 752，合计 1,457。原文报告 C0 TurnOccurrence 与该来源行级对应，但这不是 V2 已经重新独立核算所有下游数据的证明。
- 参考包有 C0、N、C1，S/C2 的 Reference/Shadow Gate 状态、U3 单尺度 Shadow Bridge、R02 的 15 条（5 个 As-Of × 3 个品种）客观运动事实、R03 的 15 条 Withheld 结果。
- `C2/01_case_opportunity_cluster_gates_v0.csv` 的 `official_cluster_committed` / `official_h1_emitted` 不是已正式获批的 Cluster 或 H1；`U3/03_r03_quality_withholding.csv` 的 `quality_judgement=WITHHELD` 不能被说成正式品种优劣。
- 两包没有独立可执行的完整 U2/U3 Runner 和全链 Trace，不适于自动宣称正式实现/生产资格。**当前 Owner 已固定这批已验算数据作为观察输入，不要求因没有 Runner 而重新计算**；但如发现数据/方法具体矛盾，应指出有疑问的行、源规则及受影响分析，向 Owner 反馈而不默默修改。

以上是可以带入 S1/S2 的**业务背景与输入事实**，不是复用旧 I4/I5/I6 产生的诊断，也不是将上轮 Gate Pass 搬进新 run。数据实际如何取得详见 [05](https://github.com/daowei2026/observe-iterate/blob/c7971cc616e09db47681abc868e77acdc272f84a/professional/v2/05_BI01_FIXED_INPUT_DATA.md)。

## 4. 对本轮的直接使用要求

首个专业任务不应再说“先自行选择数据、找有没有可用正式 Feature、再决定是否小范围验算”，也不应说“既有 I1–I3 业务背景不用理”。应读此文及原 I1–I3 Source，以已固定数据为工作前提，尽快进入 **S1 定图对象 → S2 用 aidata 画图 → S3 给出业务认识**。

完成一次局部观察并不结束 rb/i/hc 的完整 U2/U3 观察意图。找不到图、字段或有效结论时标明准确原因，但不得凭空生成“已看图”“已计算出 Quality”等主张。

## V2-02 方法更新：旧业务依据不是现成选样名单

原 OP-01/Q-01、I1–I3 的设计动机和证据边界继续作为专业 Source。2026-10-18 Owner 指出：新的业务观察应先理解叙事与细节设计要解决的共同方向机会和成员强弱问题，从固定 K 线/贴近转折的基础行情寻找真实位置，再检验 U2 位置/成员和 U3 四方面对后续质量的辨别，而不是先把旧的 raw 候选/某些字段缺项变成研究中心。详见 [07](07_BUSINESS_SCENE_OBSERVATION_METHOD.md)。这不追认旧 run 的业务接收为新 run 的完成，也不先规定场景分类、强弱公式或样本数。
