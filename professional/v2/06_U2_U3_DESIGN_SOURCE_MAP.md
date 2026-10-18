# BI-01 V2：U2/U3 业务叙事、具体设计与本轮实际计算的来源导航

## 0. 为什么需要这些材料

**此次工作要检验现有 U2/U3 设计的价值，而非重新设计或重新验算它们。** 仅凭固定 ZIP 的 CSV 字段，无法知道设计原先承诺了什么、什么被参考验算实现了、还有什么未输出。执行 Pro 在 S1 确定观察图之前，应取得本导航所指的**相关完整正文**；S2 画图和 S3 观察时，遇到业务方法疑问则回到对应的准确 Source/Method 与实际 CSV，不能从标题、字段名、示意图或本索引猜出规则。

本导航是**来源地图，不是算法合同全文、管理验收结论或生产代码证明**。每条历史业务 Source 必须带固定 commit、path 和其自述的版本/资格。原则上按以下层次使用：Owner 已接受的业务职责边界 → 人读 Narrative / Use Case → Source/Metric/Step 设计 → 真实有权的候选 Local Contract/MethodProfile → **本轮固定两份 ZIP 的实际参考输出与状态**。不同层结论冲突、方法漂移或数据缺失时，指出差异，不静默选择“最新”或把候选升为正式。

## 1. U2：共同机会簇在哪里，凭什么组成同一轮机会

以下是已核实存在的、锁定在 `daowei2026/complex-systems-vocabulary@48f55f53e25d04e5b4b59fae1e652dd4b679c9d3` 的设计文件：

| 材料 | 直接使用目的 |
|---|---|
| [Owner U2/U3 资金价值与修订决定](https://github.com/daowei2026/complex-systems-vocabulary/blob/48f55f53e25d04e5b4b59fae1e652dd4b679c9d3/docs/network-dynamic-ceps-factory/OD_U2_U3_CAPITAL_VALUE_AND_ITERATION_DECISIONS_V0.1.0.md) | **权威业务职责与增量门槛**：U2 负责 OpportunityCluster、RepeatedExposure 和不确定性，不能变成品种质量/仓位；最低增量价值 Gate 在 §7 |
| [U2 人读叙事 V0.3.0](https://github.com/daowei2026/complex-systems-vocabulary/blob/48f55f53e25d04e5b4b59fae1e652dd4b679c9d3/docs/network-dynamic-ceps-factory/U2_OPPORTUNITY_CLUSTER_SCALE_TURN_NARRATIVE_SPEC_V0.3.0.md) | **先读** §1、§2、§3 了解实际转折、Episode、NodeBehavior → Formation → OpportunityCluster → 后续边界；研究转折/形成/分组争议时读 §4–§5 |
| [U2 具体用例卡 V0.4.0](https://github.com/daowei2026/complex-systems-vocabulary/blob/48f55f53e25d04e5b4b59fae1e652dd4b679c9d3/docs/network-dynamic-ceps-factory/U2_OPPORTUNITY_CLUSTER_SCALE_TURN_USE_CASE_CARD_V0.4.0.md) | **详细设计**：§3 领域对象/字段关系、§4 U2-A/B/C、§5 Formation/Physicalization/Validity/Separation、§10 Case 选择、§11 测试 |
| [U2 Source / Metric / Step Witness V0.1.0](https://github.com/daowei2026/complex-systems-vocabulary/blob/48f55f53e25d04e5b4b59fae1e652dd4b679c9d3/docs/network-dynamic-ceps-factory/U2_SCALE_TURN_SOURCE_METRIC_STEP_WITNESS_V0.1.0.md) | 为实际转折、线段、行为、关系、Group 和跨尺度的来源与计算步骤提供 **设计层 witness**；按 §1/§2/§3 的具体 Metric/Step 追溯，不能冒称当前已跑生产版本 |

在 `feature-refinement-implementation-agent-evolution` 的 **Mission A 候选/Local Contract** 中进一步查方法，而不是由观察 Agent 发明：

- [U2 C0/N Source→Occurrence→Episode→Behavior Local Contract](https://github.com/daowei2026/feature-refinement-implementation-agent-evolution/blob/ed62cd716cd603f0bcc566368c62caec7cdba554/agent_evolution/pilot_cases/network-dynamic-ceps-factory-u2-u3/runs/u2-retrofit-20260907/artifacts/material_catchup/current_inputs/source_to_behavior/U2_SOURCE_OCCURRENCE_EPISODE_NODE_BEHAVIOR_LOCAL_CONTRACT_RETROFIT_0.1.0-candidate.1.md)
- [U2 C0/N Method-State Matrix](https://github.com/daowei2026/feature-refinement-implementation-agent-evolution/blob/ed62cd716cd603f0bcc566368c62caec7cdba554/agent_evolution/pilot_cases/network-dynamic-ceps-factory-u2-u3/runs/u2-retrofit-20260907/artifacts/material_catchup/current_inputs/source_to_behavior/U2_SOURCE_TO_BEHAVIOR_METHOD_STATE_REALIZATION_MATRIX_0.1.0-candidate.1.md)
- [U2 C1/S/C2 Typed Relation / Formation / Qualification / Physicalization Local Contract](https://github.com/daowei2026/feature-refinement-implementation-agent-evolution/blob/ed62cd716cd603f0bcc566368c62caec7cdba554/agent_evolution/pilot_cases/network-dynamic-ceps-factory-u2-u3/runs/u2-retrofit-20260907/artifacts/material_catchup/current_inputs/relation_to_cluster/U2_RELATION_FORMATION_QUALIFICATION_PHYSICALIZATION_LOCAL_CONTRACT_RETROFIT_0.1.0-candidate.1.md)
- [原候选 Upstream First Edition Profile（另一个 exact commit）](https://github.com/daowei2026/feature-refinement-implementation-agent-evolution/blob/ea126840aa68701135491572a453bf88e96ca58d/agent_evolution/pilot_cases/network-dynamic-ceps-factory-u2-u3/runs/u2-retrofit-20260907/artifacts/mission_a_r28_role_domain_20260917/UPSTREAM_FIRST_EDITION_PROFILE.md)

**权限与方法状态：** 上述 EAW Local Contract 的文件头显示 candidate/owner_accepted=false，Upstream First Edition Profile 也显示 `current_application=NOT_APPLIED`。本轮对照其业务语义和候选算法，**不可把这些文件当成已经正式生效且运行过本次 ZIP 的生产实现**。最终采用哪种单尺度参考兼容、时间窗、Δ、Shadow 处理，由本次固定输出与其明确来源查实；细节见 [04 原 I1–I3 业务底稿](04_BI01_BUSINESS_BASELINE.md) 和原始对话 §3.4。

本轮固定 ZIP 中的 U2 结果路径见 [05](05_BI01_FIXED_INPUT_DATA.md)，包括全范围的 C0/N、C1 raw，以及少量单尺度 C1/S/C2 **参考** Case。OpportunityCluster 位置/成员、正式 Commit 和 H1 必须区分；图上可以展示参考候选，不得写成正式已 Commit 的簇。

## 2. U3：这些位置的品种是否好做，具体怎样判断

同样在上述 `complex-systems-vocabulary@48f55f53…`：

| 材料 | 直接使用目的 |
|---|---|
| [U3 人读叙事 V0.3.0](https://github.com/daowei2026/complex-systems-vocabulary/blob/48f55f53e25d04e5b4b59fae1e652dd4b679c9d3/docs/network-dynamic-ceps-factory/U3_MOVEMENT_QUALITY_ACTIVITY_CONVERSION_ALLOCATION_NARRATIVE_SPEC_V0.3.0.md) | **先读** §1–§3：U3-A Movement Quality / U3-B Activity Conversion、四个 Movement Bundles、Current/Outcome；§4/§5 解释运动过程、活动转化及四类资金依据 |
| [U3 具体用例卡 V0.4.0](https://github.com/daowei2026/complex-systems-vocabulary/blob/48f55f53e25d04e5b4b59fae1e652dd4b679c9d3/docs/network-dynamic-ceps-factory/U3_MOVEMENT_QUALITY_ACTIVITY_CONVERSION_ALLOCATION_USE_CASE_CARD_V0.4.0.md) | **详细设计**：§3 Current/Outcome，§4.2 四个 Movement Bundles，§5 Movement，§6 Activity Conversion，§7 Evidence Dependency，§8 四类 Allocation Evidence，§13–14 反例和终止条件 |
| [U3 Source / Metric / Step Witness V0.1.0](https://github.com/daowei2026/complex-systems-vocabulary/blob/48f55f53e25d04e5b4b59fae1e652dd4b679c9d3/docs/network-dynamic-ceps-factory/U3_SOURCE_METRIC_STEP_WITNESS_V0.1.0.md) | **设计层字段/步骤**：§1–3 原行情 Episode → 运动指标与 Current/Outcome，§4–5 Activity/Conversion，§6–7 证据依赖与资金依据；不能把设计 Witness 视为已执行输出 |

EAW 中更细的候选方法：
- [U3 Movement Local Contract 0.2（candidate）](https://github.com/daowei2026/feature-refinement-implementation-agent-evolution/blob/ed62cd716cd603f0bcc566368c62caec7cdba554/agent_evolution/pilot_cases/network-dynamic-ceps-factory-u2-u3/runs/u3-retrofit-20260907/artifacts/material_catchup/effective_mission_a/04_movement_current/02_U3_MA_LOCAL_CONTRACT_MOVEMENT_01.md)
- [U3 Movement Audit 02](https://github.com/daowei2026/feature-refinement-implementation-agent-evolution/blob/ed62cd716cd603f0bcc566368c62caec7cdba554/agent_evolution/pilot_cases/network-dynamic-ceps-factory-u2-u3/runs/u3-retrofit-20260907/artifacts/material_catchup/effective_mission_a/05_movement_current_audit/02_U3_MA_LOCAL_CONTRACT_MOVEMENT_AUDIT_02.md)

**注意**：即使路径名含 `effective_mission_a`，上述合同/审计文件的实际正文仍说明 `ownerAccepted: false`、未运行生产，本轮不能从目录名推断已正式应用或成功运行。

### “四个方面”的业务歧义，须在首次 S1 讲清

U3 设计里同时存在 **两套不同的“四”**：

| 四个 Movement Evidence Bundles（U3 叙事 §3.2、用例卡 §4.2） | 四类 Allocation Evidence（用例卡 §1.2 / §8） |
|---|---|
| `ProgressBundle`：方向推进、持续、极值更新和连贯性 | `OpportunityGroupBudgetEvidence`：组级预算依据 |
| `FrictionBundle`：路径效率、反向运动、回吐和快速反转 | `MemberRelativeAllocationEvidence`：组内成员相对依据 |
| `RetentionBundle`：运动保持、返回原点、恢复及承接 | `RepeatedExposureEvidence`：重复机会表达与去重依据 |
| `ObservabilityAndConstraintBundle`：样本、确认延迟、数据质量、容量/成本等约束 | `UncertaintyHoldbackEvidence`：Pending、未知、冲突等不确定性扣减 |

这两套并不是同一业务输出。“能否辨别品种好不好做”在字面上更接近 Movement Bundle，但**本轮并未由 Owner 逐字段定义“四方面”**。S1 应结合真实 Owner 观察目的、上列业务原文和固定输出，列出一张“业务方面 → 原设计字段 → ZIP 中实际字段 → 有数据/无数据 → 能下何种判断”的对应表。如仍存在会实质改变目标的歧义，再请 Owner 选择，不能自己把四个资金接口当成四个运动指标，亦不能为凑四类自动新算数据。

## 3. 以已冻结的真实 ZIP 确定这次究竟有哪些输出

**唯一预计算数据输入仍是 [05](05_BI01_FIXED_INPUT_DATA.md) 指向的两份 ZIP**，实际 Codex 目录 `/dwdhome/fy/资金管理`；工作区 `/dwdhome/fy/BASE_E6_2` 不是数据目录。按原包保留正式/Reference/Shadow/Withheld 区别。

就本轮实际提供的 ZIP 结构而言：

- **全观察范围参考事实**：C0 TurnOccurrence 1,457 行、N 的逐时切片与 metrics、C1 raw 同实际时间候选/Pair/八类关系。全范围的 `S_C2_status` 带 `NOT_CLUSTER`/`NOT_ASSESSMENT` 限定，不能据此说有全范围正式簇。
- **单尺度有界演示：5 行 = 同一个 Case 在 5 个 As-Of，而不是 5 个机会簇。** `single_scale_U2_C1_S_C2_U3/C1/03_case_formation_and_three_assessments.csv` 的 5 行都是 `case_ref=refonly-ad8824a52552d7bffa91`，成员均为 `hc|i|rb`，同一实际转折时间 `2021-04-30 15:00:00`；`C2/` Gate 与 `S/` 参考 Separation 对应相同范围。5 个 As-Of 在 2021-05-06、05-07、05-11、05-14、05-18（均为 10:00）。不能把它当成 2021–2024 全范围五个正式 U2 OpportunityCluster。
- **U3 的真实可用部分**：`U3/02_movement_r02_objective_facts.csv` 是 15 行（**同一个参考 Case** × 5 个 As-Of × 3 成员）的 Movement 路径事实，含 `raw_progress`、`path_efficiency`、`max_counter_move`、`retained_fraction`、`completed_recovery_events`、`path_status` 等；它不是完整四个 Bundle 的已校准 Current。其 `market_quality_judgement` 表明 Withheld/无正式 H1/校准。
- **未形成的质量结论**：`U3/03_r03_quality_withholding.csv` 15 行，`progress_axis/friction_axis/retention_axis=CalibrationPending`，`quality_judgement=WITHHELD`，不能当成正式“哪个品种好做”。`C2/01_case_opportunity_cluster_gates_v0.csv` 5 行中 `official_cluster_committed=NO`。
- 当前 ZIP 中没有证明 U3-B Activity Conversion、四类 Allocation Evidence 或更广泛 U3 Relation/Group 已按正式合同算出。**缺失要如实作为本次设计价值观察的边界**，不为补齐业务叙事而改动预计算结果。

这些是对**附件里的 CSV 结构和行数/状态**的核对，不是重新运行 U2/U3 算法。若未来 `/dwdhome/fy/资金管理` 的实际文件与此次附件不一致，必须明确差异，而不能默认是同一字节。

## 4. 开始 S1/S2/S3 时具体怎么读

1. **S1 要定义观察目标与业务依据**：本导航 + 原 [04](04_BI01_BUSINESS_BASELINE.md) 中 OP-01/Q-01、已接受的 Owner Decision、U2/U3 人读叙事、与本次问题有关的用例卡章节；明确 U3 所说“四方面”与固定数据的实际覆盖。
2. **S2 要确定具体画法**：`05` 中固定 ZIP 成员和时间、U2 的具体 Formation/Group 合同与必要 Source witness、U3 的 Movement 字段含义；在 aidata 中画实际能产生的图和同源数据。不让 aidata 默认自动节点重新定义本轮业务 Case。
3. **S3 要给可证伪的业务认识**：先看实际图所对应的时间/数据，再按 U2/U3 设计的承诺和已算出的实际字段比较单品种、静态组、U2、U2+U3 哪些判断变了、哪些未变。利用 Contradiction、Pending、NoIncrement 解释设计不足，而不是因形式完整宣称四方面已验证。
4. **有具体方法冲突时**回到上面列出的 Local Contract/MethodProfile/真实 CSV，区分业务设计是否要求了某项行为、参考数据实际怎么算、缺失是否属于已知 Withheld。导航页不代替全文 Source，候选合同不能代替正式批准。

**本导航及其来源不改变固定两份 ZIP、rb/i/hc 范围、S1–S3 业务目标、AI 暂不视觉看图、aidata 尽量不修改和旧 run 不继承的既有决定。**

## 5. V2-02：先读业务叙事后做真实市场场景观察

原以上各设计 Source 的职责边界继续真实有效，但**业务 Source 导航本身不是选样规则**。专业者按 [07 场景观察方法](07_BUSINESS_SCENE_OBSERVATION_METHOD.md) 先读 U2 `DirectionalReleaseIntent` 中共同方向机会组织、U3 组内成员推进/摩擦/保持/可知性及后续 Outcome/Feedback 的实际业务问题，再以基础行情找值得分析的位置，必要时才查候选 Local Contract 及原 CSV 字段。旧 `BI-01-V2-01` 的 raw 分层抽样、已知 F01—F14 与主 Case 是有出处的历史观察，不能当作新 S1 必须采用的分类、样本或已证实的四束辨别力。固定 U3 广域结果不足时报告能做的局部验证与不能判断的真实缺项，不从设计文档想象已运行的输出。
