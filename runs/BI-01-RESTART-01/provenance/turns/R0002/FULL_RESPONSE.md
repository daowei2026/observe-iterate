[BI01-RESTART-01-R0002-c19efdc130c1995d4660ca4907747429]

<a id="r0002-repair-completed"></a>
# R0002 原 M-START 交付修复完成

本轮仅完成 Owner 授权的 R0001 管理交付机器接线窄修复；没有重新执行 M-START，没有增加业务范围，没有派发专业任务，没有签 G4，也没有宣称 Workmap `ADOPTED` 或 Overlay12 PASS。

<a id="r0002-decisions"></a>
## 六项决定

1. `task_id: BI01-RESTART-01-I4-EXECUTION-01`。
2. R0001 ROLE_RETURN 新增 exact `question_work_ref`；原 exact-commit 文件继续保留。
3. `professional_mode: OBSERVATION_I4`。
4. Binding 中所有 `answer_ref` 已改为 exact Git locator；规范载体是 R0001 exact commit 的地图、任务和 FULL_RESPONSE。
5. 所有 management route 回到 `chatgpt-project:细节叙事生成_金标/chat:BI01-R01-管理`；专业 route 仍是未来独立新专业聊天。
6. README、地图和 Workmap Binding Candidate 只同步当前运行位置，不改 R0001 业务判断。

<a id="r0002-material-use"></a>
## 材料使用

- Owner 授权：`daowei2026/observe-iterate@b6b837e4f8368f07afb4f1eaf6f6648080a6933e:runs/BI-01-RESTART-01/OWNER_AUTHORIZED_MANUAL_REPAIR_R0002.md::full`
- 修复要求：`daowei2026/observe-iterate@46119a8e0030b4c3597634735cbe5d22ad3a0ac7:runs/BI-01-RESTART-01/reviews/MANAGEMENT_DELIVERY_REPAIR_REQUIRED_R0001.md::full`
- 原 R0001 树：`daowei2026/observe-iterate@46119a8e0030b4c3597634735cbe5d22ad3a0ac7:runs/BI-01-RESTART-01/provenance/turns/R0001/::tree`
- 锁定 mode 配置：`daowei2026/observe-iterate@46119a8e0030b4c3597634735cbe5d22ad3a0ac7:runtime/config/COORDINATOR_DISPATCH.json::full`
- workmap task_id 解析规则：`daowei2026/observe-iterate@46119a8e0030b4c3597634735cbe5d22ad3a0ac7:runtime/overlay/tools/workmap_gate.py::dispatch task_id block`

<a id="r0002-current-task"></a>
## 修正版当前任务（完整）

````markdown
# BI-01-RESTART-01 当前任务：I4 真实业务观察，含定向 I3 核查

task_id: BI01-RESTART-01-I4-EXECUTION-01

## 0. 角色与任务性质

recipient：BI-01 执行 Pro。  
当前阶段：I4；其中只有具名承重事实需要定向返回 I3/G3 核查。  
你不是管理 Pro、Owner、Worker Codex 或操作端。你提交专业自查和 Gate 依据，但不自行签 G4。

<a id="issued-task-full-scope"></a>
## 1. 完整范围

持续完成当前 I4 阶段全部约定工作：

- 从 G3 合法范围内的真实结果出发；
- 形成可追溯事实过程；
- 比较单品种、静态板块、U2、U2+U3 的新增认识或无增量；
- 主动挑战 Working/Completed、时间、单位、方法、证据重叠、选择偏差和替代解释；
- 在需要时定向取得图/数据/复算；
- 继续到形成可供管理判断 G4 的成果，或出现具名 Source/Method/Owner 阻塞。

当前重点只决定顺序，不把 Case A、一个文件、一次修复或一组 finding 设为停点。

<a id="issued-task-current-focus"></a>
## 2. 当前第一重点

围绕 HC/RB/I 的共同 Trough Case：

- actual turn：2021-04-30 15:00；
- knowledge/source occurrence：从 2021-05-06 10:00 开始；
- As-Of：2021-05-06、05-07、05-11、05-14、05-18 10:00；
- 问题：成员在 Progress、Friction、Retention 和生命周期上怎样分化，U2/U3 相比单品种和静态板块究竟增加了什么。

先完成必要 I3 定向核查，再立即进入 I4；不等待完整 Runner、全仓审计或正式 H1。

## 3. 已由管理决定，不再重判

1. 旧 I4 试跑结果、Gate、聊天和在途任务不继承。
2. 当前下游只可称 Reference/Shadow，不是正式 OpportunityCluster、H1 或 U3 Quality。
3. 当前上游包采用实际 SHA-256  
   `4fd1af4e7b34af6fc099e6289ffdd5d83125412fc16d2a9902af4fd9741b3987`  
   作为本次候选新 DataBinding；不得称为历史 `ff3215...` 原件。
4. 不要求恢复历史原件或重建完整 Runner 才能观察。
5. S 的 `outside_count=0` 不能支持“优于组外”。
6. A/B/C 不是固定配额；B/C 只在能区分重要解释时进入。
7. 正式 H1、Quality 校准、扩 Universe、平台重构不是当前任务。
8. 没有业务增量是合法结论。

<a id="current-inputs"></a>
## 4. 输入

### 附件 A：下游结果

`steel_U2_U3_执行结果_20261010.zip`  
SHA-256：`7bebbee3fd7d425eb85116f33c5d0e01ae2163e6849818515fe3824a82b9a46c`

首要成员：

- `baseline_U2_C0_N_C1/C0/02_turn_occurrences.csv`
- `baseline_U2_C0_N_C1/C0/04_segment_episodes.csv`
- `baseline_U2_C0_N_C1/C0/05_completed_episode_metrics.csv`
- `baseline_U2_C0_N_C1/C0/06_episode_and_working_cuts_30m.csv`
- `baseline_U2_C0_N_C1/N/01_node_behavior_cuts.csv`
- `baseline_U2_C0_N_C1/N/02_node_behavior_metrics.csv`
- `baseline_U2_C0_N_C1/C1/03_eight_relation_raw_observations.csv`
- `baseline_U2_C0_N_C1/C1/04_member_post_turn_at_common_cut.csv`
- `single_scale_U2_C1_S_C2_U3/C1/02_case_eight_relations.csv`
- `single_scale_U2_C1_S_C2_U3/C1/03_case_formation_and_three_assessments.csv`
- `single_scale_U2_C1_S_C2_U3/S/01_case_external_separation_v0.csv`
- `single_scale_U2_C1_S_C2_U3/C2/01_case_opportunity_cluster_gates_v0.csv`
- `single_scale_U2_C1_S_C2_U3/U3/01_single_scale_shadow_bridge.csv`
- `single_scale_U2_C1_S_C2_U3/U3/02_movement_r02_objective_facts.csv`
- `single_scale_U2_C1_S_C2_U3/U3/03_r03_quality_withholding.csv`

### 附件 B：上游候选 DataBinding

`rb_hc_i_mid贴近转折_zig_small_K线_20210101_20240229.zip`  
实际 SHA-256：`4fd1af4e7b34af6fc099e6289ffdd5d83125412fc16d2a9902af4fd9741b3987`

使用每品种：

- `*_kline_30m.csv`
- `*_mid_scaleturn_value1_value2.csv`
- 必要时 `*_mid_input_zig_small_*`
- `manifest.json`
- `数据说明.md`

原始空 OHLC 占位不得插值或删除；若承重范围命中空值，明确说明影响。

<a id="allowed-use"></a>
## 5. 可消费资格

### 可直接使用

- 下游包实际导出了什么；
- 各状态、Reference/Shadow/Withheld 边界；
- 五个 As-Of 的客观字段；
- C2 未正式 commit、H1 未发布、R03 Withheld；
- 当前方法标签与限制。

### 定向核后使用

- Case anchor 的 source occurrence、actual/confirm/knowledge 对应；
- R02 关键路径字段与当前上游 KLine；
- 同成熟度/共同前缀比较；
- 跨包结论。

### 当前禁止

- 正式 OpportunityCluster、正式 H1、正式 Quality、资金结论；
- 以原始价格点直接跨品种强弱排名；
- 把后来才知道的 completed end 回填旧 As-Of；
- 把 ValidEmpty/Pending 当负面或优势；
- 把共享 Episode/Geometry/路径字段计作独立多票。

<a id="actual-work"></a>
## 6. 连续专业工作

### A. 定向 I3 核查

1. 核附件真实 hash、成员、字段和 Case identity。
2. 对 Case-01 的三条 anchor，核：
   - actual turn；
   - source occurrence/knowledge time；
   - episode id；
   - Working/Completed 边界；
   - R02 start/end/path 关键值；
   - 当前上游 KLine 能否复算承重路径。
3. 形成 G3 范围建议：
   - Pass；
   - NeedsRepair；
   - 只限制哪些 claim。
4. 不进行全量 Runner 重建、全历史关系审计或无业务影响的逐字段清点。

### B. 重建真实时间线

对五个 As-Of 同时形成：

1. 当时可知的状态；
2. 后来确认的 canonical completed 状态；
3. 不能回填的未来信息；
4. 组候选/资格/Shadow bridge 状态；
5. 每个成员 Movement objective facts。

必须特别处理：

- HC 2021-05-11 10:00 Working 38 bar，而 10:30 才可见 canonical Completed 33 bar；
- I 的 Working/Completed 回定；
- RB 的完成可见性；
- completed Episode 不再延长。

### C. 公平比较

至少保留三种比较域：

1. As-Of lifecycle-true；
2. canonical completed；
3. common-horizon / maturity-matched prefix。

解释每种比较回答什么、不能回答什么。原始价格点只在同品种路径内使用；跨品种要使用合法无量纲量、相对变化或明确说明不可比。

### D. 四层增量/无增量

逐层回答：

| 层 | 必须回答 |
|---|---|
| 单品种 | 原 KLine、Episode、N 已经知道什么 |
| 静态板块 | 固定 HC/RB/I 身份增加了什么，缺什么 |
| U2 | 同轮形成、资格、边界、身份/生命周期是否新增信息，还是只重包装 |
| U2+U3 | 在同轮语境中，Movement facts 是否改变判断；哪些字段只是复述 C0/N |

不得以“字段更多、图更复杂、文件更长”证明增量。

### E. 主动挑战

至少检验：

- Working/Completed 和 late confirmation；
- As-Of 选择；
- 价格单位与归一化；
- Reference Δ/bar proxy、兼容矩阵和方法敏感性；
- Formation 与 Quality/Separation 的证据循环；
- N 与 U3 的同源/重复事实；
- 单 Case 选择偏差；
- 第三成员排除究竟是业务事实还是 Pending/DataUnavailable；
- 单品种是否已经足够。

### F. 持续后继

Case A 初步结果形成后：

- 若已经足以形成 G4 候选或有据无增量，触发管理接收；
- 若关键解释仍不可区分，从现有数据中按事先声明的规则选择下一真实反例/重复样本；
- 若需要 B/C，先写入选条件，不事后挑最好看的 Case；
- 不因 Case A、图、文件或局部修复完成而主动停止。

<a id="issued-task-deliverables"></a>
## 7. 交付

1. Case-01 五切面的事实时间线。
2. 定向 G3 核查表及可消费范围。
3. 公平比较域与结果。
4. 四层增量/无增量矩阵。
5. 至少一条：
   - BusinessFinding；
   - 有据 NoIncrementFinding；
   - DesignFinding / MethodFinding。
6. 每条 finding 的：
   - raw facts / result refs / method revision；
   - support / counter / missing；
   - evidence dependency；
   - alternative explanations；
   - sensitivity / invalidation；
   - what remains unknown；
   - next probe。
7. 必要的图/数据处理工单与 Worker 回交（如发生）。
8. G4 自查及完整未完。
9. 一致的 ROLE_RETURN 与 QUESTION_WORK_RETURN。

<a id="issued-task-completion"></a>
## 8. 完成条件

本阶段只有在下列条件同时满足时，才申请 G4：

- 真实回答 Q-01，而非只报告数据或公式；
- 四层比较形成增量或有据无增量；
- 时间/成熟度/单位/方法/证据重叠得到必要挑战；
- 事实、CaseFinding、Hypothesis、DesignFinding 分开；
- 结论范围不超过 G3 资格；
- 材料足以进入 I5，而 Owner 无需自行倒推 CSV；
- 全部重要未完和下一问题清楚。

局部数据修通、完成一张图或观察一个 Case 不构成阶段完成。

<a id="worker-authority"></a>
## 9. Worker Codex 授权边界

执行 Pro 可在当前任务内签发有界 Worker 工单，用于：

- 定向复算；
- 时间线切片；
- 可复跑图；
- 字段核验；
- 结果渲染。

每份工单必须写清：业务问题、冻结输入、hash、成员、Case、As-Of、Method、字段、视觉/计算规则、输出、核验和禁止推论。Worker 不选业务结论、不改正式方法、不签 Gate。普通工程选择在工单范围内自行完成，不逐错误回 Pro。

<a id="withdrawn-work"></a>
## 10. 已撤技术/专业工作

下列内容从当前任务、前置、验收和后继退出，不列 deferred required：

- 恢复旧 I4 试跑结果；
- 全仓审计或完整 Runner 重建；
- 正式 C2/H1 发布；
- R03 Quality 校准；
- 扩充完整钢铁 Universe；
- A/B/C 固定配额；
- FGL/WSPD/通用网络平台；
- 新建控制表、平行状态机或额外角色；
- 以图数、文件数、测试数结算业务。

<a id="budget-and-review"></a>
## 11. 投入预期与复看

- 第一段：预计 1 次有效执行 Pro 调用可完成定向 G3 与 Case A 的首轮实质观察。
- 当前 I4 达到 G4 候选：预计 2～4 次有效执行 Pro 调用；是否需要 Worker 取决于事实，预期 0～2 个有界工单。
- 以上不是轮次配额或停点。
- 连续 2 次有效调用仍只停留在来源/工具/格式/运行准备，触发管理复看；无关专业工作继续。
- G4 候选、承重资格冲突、Owner/方法变化立即触发管理。

<a id="route-same-work"></a>
## 12. 同工作续作正文

继续本任务。完整范围与权限仍按本文件；采用最新完整 RETURN 的 continuation_ref，保留已成、全部未完、方法与输入。朝完整完成 I4 全部约定工作推进，当前重点只决定顺序，禁止单 Case、局部修复或图完成即停；不重做无新依据成果；重要变化具名返回。

<a id="route-accept"></a>
## 13. 管理接收正文

向 BI-01 管理 Pro 提交完整专业结果、G3/G4 自查、证据、限制、全部重要未完和建议后继。管理按完整目标、I4/G4 和当前可消费范围判断，不把执行者自评或技术完成当 Gate。

<a id="route-decide"></a>
## 14. 管理裁定正文

仅在承重 Source/Method 冲突、Owner/正式方向变化、超授权投入或 G4 候选形成时请求管理裁定。写清受影响 claim、可继续主体、准确证据和需要的具体决定；不以“全面检查”转交管理。

<a id="route-return-repair"></a>
## 15. 回交修复正文

只修复确切的 ROLE_RETURN / QUESTION_WORK_RETURN 字段、引用或两份续作不一致。保留原实质与资格；若缺的是专业分析，继续原工作并如实保持未完，不为过格式检查制造业务决定。
````

<a id="r0002-binding"></a>
## 修正版 Question Work Binding（完整）

````json
{
  "schema": "question-work/v2",
  "kind": "BINDING",
  "work_id": "BI-01",
  "goal_ref": {
    "repo": "daowei2026/observe-iterate",
    "commit": "75d42776a78cd4cbdf3b61bbf86ec93701d06b84",
    "path": "professional/source/00_AGENT_CHARTER_AND_STAGE_CONTRACT.md",
    "selector": "full"
  },
  "plan_ref": {
    "repo": "daowei2026/observe-iterate",
    "commit": "46119a8e0030b4c3597634735cbe5d22ad3a0ac7",
    "path": "runs/BI-01-RESTART-01/00_长程推进地图.md",
    "selector": "full"
  },
  "full_scope_ref": {
    "repo": "daowei2026/observe-iterate",
    "commit": "46119a8e0030b4c3597634735cbe5d22ad3a0ac7",
    "path": "runs/BI-01-RESTART-01/01_当前任务.md",
    "selector": "#issued-task-full-scope"
  },
  "batch_result": "先完成Case-01承重G3核查、五切面时间线和四层增量首轮结果；未触发管理条件时连续推进其余I4，不以Case A为停点。",
  "question_ids": [
    "I3",
    "I4"
  ],
  "professional_mode": "OBSERVATION_I4",
  "focus_ref": {
    "repo": "daowei2026/observe-iterate",
    "commit": "46119a8e0030b4c3597634735cbe5d22ad3a0ac7",
    "path": "runs/BI-01-RESTART-01/01_当前任务.md",
    "selector": "#issued-task-current-focus"
  },
  "coverage_ref": {
    "repo": "daowei2026/observe-iterate",
    "commit": "46119a8e0030b4c3597634735cbe5d22ad3a0ac7",
    "path": "runs/BI-01-RESTART-01/00_长程推进地图.md",
    "selector": "full"
  },
  "source_reads": [
    {
      "source": {
        "repo": "daowei2026/observe-iterate",
        "commit": "caccf69993b6f0c184fc89194476bcd542acb1e0",
        "path": "runs/BI-01-RESTART-01/OWNER_START.md",
        "selector": "full"
      },
      "requirement": "MODE_FULL",
      "purpose": "本次新run授权、旧I4不继承、连续真实业务推进要求",
      "reuse_evidence": null
    },
    {
      "source": {
        "repo": "daowei2026/observe-iterate",
        "commit": "75d42776a78cd4cbdf3b61bbf86ec93701d06b84",
        "path": "professional/source/00_AGENT_CHARTER_AND_STAGE_CONTRACT.md",
        "selector": "full"
      },
      "requirement": "MODE_FULL",
      "purpose": "完整总意图、I1-I6 Input/Output/Gate、角色权限",
      "reuse_evidence": null
    },
    {
      "source": {
        "repo": "daowei2026/observe-iterate",
        "commit": "75d42776a78cd4cbdf3b61bbf86ec93701d06b84",
        "path": "professional/source/01_I1_I3_PROFESSIONAL_CONTRACT.md",
        "selector": "full"
      },
      "requirement": "BOUNDARY",
      "purpose": "定向G3核查、局部返I2/I3和不冻结无关I4的边界",
      "reuse_evidence": null
    },
    {
      "source": {
        "repo": "daowei2026/observe-iterate",
        "commit": "75d42776a78cd4cbdf3b61bbf86ec93701d06b84",
        "path": "professional/source/02_I4_OBSERVATION_AND_CHALLENGE.md",
        "selector": "full"
      },
      "requirement": "FOCUS_FULL",
      "purpose": "I4事实、增量/无增量、挑战、G4要求",
      "reuse_evidence": null
    },
    {
      "source": {
        "repo": "daowei2026/observe-iterate",
        "commit": "75d42776a78cd4cbdf3b61bbf86ec93701d06b84",
        "path": "professional/source/03_STAGE_HANDOFF_AND_READINESS.md",
        "selector": "full"
      },
      "requirement": "BOUNDARY",
      "purpose": "G4到I5、定向补修和后继边界",
      "reuse_evidence": null
    },
    {
      "source": {
        "repo": "daowei2026/observe-iterate",
        "commit": "75d42776a78cd4cbdf3b61bbf86ec93701d06b84",
        "path": "professional/source/04_PRO_WORKER_CODEX_HANDOFF.md",
        "selector": "full"
      },
      "requirement": "BOUNDARY",
      "purpose": "必要复算/制图工单与Worker回交边界",
      "reuse_evidence": null
    },
    {
      "source": {
        "repo": "daowei2026/observe-iterate",
        "commit": "75d42776a78cd4cbdf3b61bbf86ec93701d06b84",
        "path": "professional/source/05_ROLE_GATE_AND_HANDOFF_CONTRACT.md",
        "selector": "full"
      },
      "requirement": "BOUNDARY",
      "purpose": "执行Pro自查、管理Gate、Owner权限",
      "reuse_evidence": null
    },
    {
      "source": {
        "repo": "daowei2026/complex-systems-vocabulary",
        "commit": "fe9656349c8f0aefeeef41c323bec81a688a2d70",
        "path": "docs/network-dynamic-ceps-factory/capital-management-purpose/discuss-materials/U2U3首轮业务观察实例上下文_20261010/01_首轮实例及子意图1至3上下文.md",
        "selector": "full"
      },
      "requirement": "FOCUS_FULL",
      "purpose": "Q-01、Case身份、U2/U3计算链、方法与As-Of历史来源；不采用旧执行结论",
      "reuse_evidence": null
    },
    {
      "source": {
        "repo": "daowei2026/complex-systems-vocabulary",
        "commit": "fe9656349c8f0aefeeef41c323bec81a688a2d70",
        "path": "docs/network-dynamic-ceps-factory/capital-management-purpose/discuss-materials/U2U3首轮业务观察实例上下文_20261010/02_子意图4三类观察情形与挑战.md",
        "selector": "full"
      },
      "requirement": "FOCUS_FULL",
      "purpose": "四层增量、A/B/C关系、主动挑战和最低结果合同",
      "reuse_evidence": null
    },
    {
      "source": {
        "repo": "daowei2026/feature-refinement-implementation-agent-evolution",
        "commit": "ed62cd716cd603f0bcc566368c62caec7cdba554",
        "path": "agent_evolution/pilot_cases/network-dynamic-ceps-factory-u2-u3/runs/u2-retrofit-20260907/artifacts/material_catchup/current_inputs/source_to_behavior/U2_SOURCE_OCCURRENCE_EPISODE_NODE_BEHAVIOR_LOCAL_CONTRACT_RETROFIT_0.1.0-candidate.1.md",
        "selector": "full"
      },
      "requirement": "PROVENANCE_TRIGGER",
      "purpose": "C0/N actual-confirm、Episode和NodeBehavior方法边界",
      "reuse_evidence": null
    },
    {
      "source": {
        "repo": "daowei2026/feature-refinement-implementation-agent-evolution",
        "commit": "ed62cd716cd603f0bcc566368c62caec7cdba554",
        "path": "agent_evolution/pilot_cases/network-dynamic-ceps-factory-u2-u3/runs/u2-retrofit-20260907/artifacts/material_catchup/current_inputs/relation_to_cluster/U2_RELATION_FORMATION_QUALIFICATION_PHYSICALIZATION_LOCAL_CONTRACT_RETROFIT_0.1.0-candidate.1.md",
        "selector": "full"
      },
      "requirement": "PROVENANCE_TRIGGER",
      "purpose": "Formation、Qualification、Validity、ExternalSeparation、Commit分责",
      "reuse_evidence": null
    },
    {
      "source": {
        "repo": "daowei2026/feature-refinement-implementation-agent-evolution",
        "commit": "ed62cd716cd603f0bcc566368c62caec7cdba554",
        "path": "agent_evolution/pilot_cases/network-dynamic-ceps-factory-u2-u3/runs/u3-retrofit-20260907/artifacts/material_catchup/effective_mission_a/04_movement_current/02_U3_MA_LOCAL_CONTRACT_MOVEMENT_01.md",
        "selector": "full"
      },
      "requirement": "PROVENANCE_TRIGGER",
      "purpose": "U3 Movement objective facts、Working/Completed、质量非主张",
      "reuse_evidence": null
    },
    {
      "source": {
        "source_kind": "ATTACHMENT",
        "attachment_id": "file_0000000035c481fdbbfb82af5e57a96c",
        "filename": "steel_U2_U3_执行结果_20261010.zip",
        "selector": "full archive; primary members listed in current task",
        "sha256": "7bebbee3fd7d425eb85116f33c5d0e01ae2163e6849818515fe3824a82b9a46c"
      },
      "requirement": "FOCUS_FULL",
      "purpose": "当前Reference/Shadow结果、状态边界和五个As-Of切面",
      "reuse_evidence": null
    },
    {
      "source": {
        "source_kind": "ATTACHMENT",
        "attachment_id": "file_000000008c7481fd8604a79973ec5951",
        "filename": "rb_hc_i_mid贴近转折_zig_small_K线_20210101_20240229.zip",
        "selector": "full archive; bind to actual current hash, not historical expected hash",
        "sha256": "4fd1af4e7b34af6fc099e6289ffdd5d83125412fc16d2a9902af4fd9741b3987"
      },
      "requirement": "FOCUS_FULL",
      "purpose": "当前重启的候选DataBinding、Case anchor与路径核查",
      "reuse_evidence": null
    }
  ],
  "deliverables_ref": {
    "repo": "daowei2026/observe-iterate",
    "commit": "46119a8e0030b4c3597634735cbe5d22ad3a0ac7",
    "path": "runs/BI-01-RESTART-01/01_当前任务.md",
    "selector": "#issued-task-deliverables"
  },
  "completion_ref": {
    "repo": "daowei2026/observe-iterate",
    "commit": "46119a8e0030b4c3597634735cbe5d22ad3a0ac7",
    "path": "runs/BI-01-RESTART-01/01_当前任务.md",
    "selector": "#issued-task-completion"
  },
  "budget_ref": {
    "repo": "daowei2026/observe-iterate",
    "commit": "46119a8e0030b4c3597634735cbe5d22ad3a0ac7",
    "path": "runs/BI-01-RESTART-01/01_当前任务.md",
    "selector": "#budget-and-review"
  },
  "routes": {
    "same_work": {
      "recipient_role": "professional",
      "recipient_ref": "chatgpt-project:细节叙事生成_金标/chat:new:BI01-RESTART-01-I4-EXECUTION",
      "instructions_ref": {
        "repo": "daowei2026/observe-iterate",
        "commit": "46119a8e0030b4c3597634735cbe5d22ad3a0ac7",
        "path": "runs/BI-01-RESTART-01/01_当前任务.md",
        "selector": "#route-same-work"
      }
    },
    "accept": {
      "recipient_role": "management",
      "recipient_ref": "chatgpt-project:细节叙事生成_金标/chat:BI01-R01-管理",
      "instructions_ref": {
        "repo": "daowei2026/observe-iterate",
        "commit": "46119a8e0030b4c3597634735cbe5d22ad3a0ac7",
        "path": "runs/BI-01-RESTART-01/01_当前任务.md",
        "selector": "#route-accept"
      }
    },
    "decide": {
      "recipient_role": "management",
      "recipient_ref": "chatgpt-project:细节叙事生成_金标/chat:BI01-R01-管理",
      "instructions_ref": {
        "repo": "daowei2026/observe-iterate",
        "commit": "46119a8e0030b4c3597634735cbe5d22ad3a0ac7",
        "path": "runs/BI-01-RESTART-01/01_当前任务.md",
        "selector": "#route-decide"
      }
    },
    "return_repair": {
      "recipient_role": "professional",
      "recipient_ref": "chatgpt-project:细节叙事生成_金标/chat:new:BI01-RESTART-01-I4-EXECUTION",
      "instructions_ref": {
        "repo": "daowei2026/observe-iterate",
        "commit": "46119a8e0030b4c3597634735cbe5d22ad3a0ac7",
        "path": "runs/BI-01-RESTART-01/01_当前任务.md",
        "selector": "#route-return-repair"
      }
    }
  },
  "triggers": [
    {
      "trigger_id": "BI01-I4-G4-CANDIDATE",
      "kind": "RESULT",
      "condition_ref": {
        "repo": "daowei2026/observe-iterate",
        "commit": "46119a8e0030b4c3597634735cbe5d22ad3a0ac7",
        "path": "runs/BI-01-RESTART-01/provenance/turns/R0001/FULL_RESPONSE.md",
        "selector": "#trigger-g4"
      },
      "signal_key": "bi01.i4.g4_candidate",
      "route": {
        "recipient_role": "management",
        "recipient_ref": "chatgpt-project:细节叙事生成_金标/chat:BI01-R01-管理",
        "instructions_ref": {
          "repo": "daowei2026/observe-iterate",
          "commit": "46119a8e0030b4c3597634735cbe5d22ad3a0ac7",
          "path": "runs/BI-01-RESTART-01/01_当前任务.md",
          "selector": "#route-accept"
        }
      },
      "blocking": false,
      "effort_limit": null,
      "obligation_id": "BI01-I4-GATE-REVIEW",
      "cycle_id": "BI01-RESTART-01-I4-GATE-01",
      "rearm_ref": null,
      "repeat": "ONCE"
    },
    {
      "trigger_id": "BI01-I3-CONSUMPTION-CONFLICT",
      "kind": "RESULT",
      "condition_ref": {
        "repo": "daowei2026/observe-iterate",
        "commit": "46119a8e0030b4c3597634735cbe5d22ad3a0ac7",
        "path": "runs/BI-01-RESTART-01/provenance/turns/R0001/FULL_RESPONSE.md",
        "selector": "#trigger-g3-conflict"
      },
      "signal_key": "bi01.i3.consumption_conflict",
      "route": {
        "recipient_role": "management",
        "recipient_ref": "chatgpt-project:细节叙事生成_金标/chat:BI01-R01-管理",
        "instructions_ref": {
          "repo": "daowei2026/observe-iterate",
          "commit": "46119a8e0030b4c3597634735cbe5d22ad3a0ac7",
          "path": "runs/BI-01-RESTART-01/01_当前任务.md",
          "selector": "#route-decide"
        }
      },
      "blocking": true,
      "effort_limit": null,
      "obligation_id": "BI01-I3-QUALIFICATION-REVIEW",
      "cycle_id": "BI01-RESTART-01-I3-QUAL-01",
      "rearm_ref": null,
      "repeat": "ONCE"
    },
    {
      "trigger_id": "BI01-OWNER-METHOD-CHANGE",
      "kind": "CHANGE",
      "condition_ref": {
        "repo": "daowei2026/observe-iterate",
        "commit": "46119a8e0030b4c3597634735cbe5d22ad3a0ac7",
        "path": "runs/BI-01-RESTART-01/provenance/turns/R0001/FULL_RESPONSE.md",
        "selector": "#trigger-change"
      },
      "signal_key": "bi01.owner_method_change",
      "route": {
        "recipient_role": "management",
        "recipient_ref": "chatgpt-project:细节叙事生成_金标/chat:BI01-R01-管理",
        "instructions_ref": {
          "repo": "daowei2026/observe-iterate",
          "commit": "46119a8e0030b4c3597634735cbe5d22ad3a0ac7",
          "path": "runs/BI-01-RESTART-01/01_当前任务.md",
          "selector": "#route-decide"
        }
      },
      "blocking": true,
      "effort_limit": null,
      "obligation_id": "BI01-CURRENT-ASSUMPTION-REVIEW",
      "cycle_id": "BI01-RESTART-01-ASSUMPTION-01",
      "rearm_ref": null,
      "repeat": "ONCE"
    },
    {
      "trigger_id": "BI01-I4-STAGNATION-REVIEW",
      "kind": "EFFORT",
      "condition_ref": {
        "repo": "daowei2026/observe-iterate",
        "commit": "46119a8e0030b4c3597634735cbe5d22ad3a0ac7",
        "path": "runs/BI-01-RESTART-01/provenance/turns/R0001/FULL_RESPONSE.md",
        "selector": "#trigger-effort"
      },
      "signal_key": "bi01.i4.stagnation_review",
      "route": {
        "recipient_role": "management",
        "recipient_ref": "chatgpt-project:细节叙事生成_金标/chat:BI01-R01-管理",
        "instructions_ref": {
          "repo": "daowei2026/observe-iterate",
          "commit": "46119a8e0030b4c3597634735cbe5d22ad3a0ac7",
          "path": "runs/BI-01-RESTART-01/01_当前任务.md",
          "selector": "#route-decide"
        }
      },
      "blocking": false,
      "effort_limit": {
        "unit": "EFFECTIVE_CALLS",
        "limit": 2,
        "count_from_ref": {
          "repo": "daowei2026/observe-iterate",
          "commit": "46119a8e0030b4c3597634735cbe5d22ad3a0ac7",
          "path": "runs/BI-01-RESTART-01/01_当前任务.md",
          "selector": "#budget-and-review"
        }
      },
      "obligation_id": "BI01-I4-MANAGEMENT-OVERSIGHT",
      "cycle_id": "BI01-RESTART-01-I4-OVERSIGHT-01",
      "rearm_ref": null,
      "repeat": "WHILE_WORK_ACTIVE"
    }
  ],
  "explicit_no_trigger_reason_ref": null,
  "parent": {
    "status": "NOT_APPLICABLE_NEW_CASE",
    "ref": null,
    "reason_ref": {
      "repo": "daowei2026/observe-iterate",
      "commit": "46119a8e0030b4c3597634735cbe5d22ad3a0ac7",
      "path": "runs/BI-01-RESTART-01/provenance/turns/R0001/FULL_RESPONSE.md",
      "selector": "#parent-decision"
    }
  },
  "question_definitions": []
}
````

<a id="r0001-role-return-repair"></a>
## R0001 ROLE_RETURN 修复件（完整）

````json
{
  "schema": "longrun-return/v1",
  "work_id": "BI-01",
  "invocation_id": "BI01-RESTART-01-R0001-42ceb84c3fdf413bae35cbed17fb7078",
  "assignment_token": "c4bfebec3b7748c9993ff60a187b3096",
  "question_work_ref": "github:daowei2026/observe-iterate@46119a8e0030b4c3597634735cbe5d22ad3a0ac7:runs/BI-01-RESTART-01/provenance/turns/R0001/QUESTION_WORK_RETURN.json::full",
  "work_status": "SUBMITTED",
  "completed_scope_ref": "#m-start-complete",
  "remaining_scope_ref": null,
  "artifact_refs": [
    {
      "answer_ref": "#management-decision"
    },
    {
      "answer_ref": "#workmap"
    },
    {
      "answer_ref": "#issued-task"
    },
    {
      "answer_ref": "#question-work-binding"
    }
  ],
  "delivery": {
    "status": "READY",
    "missing_refs": []
  },
  "materials": {
    "use_record_ref": "#material-use",
    "unread_required": [],
    "unavailable_required": [
      "github:daowei2026/observe-iterate@75d42776a78cd4cbdf3b61bbf86ec93701d06b84:professional/CURRENT_EXECUTION.md::完整独立专业审查方法MISSING"
    ]
  },
  "handoff": {
    "kind": "SUBMIT",
    "route_key": "bi01_management_result_to_coordinator",
    "instructions_ref": "#management-handoff"
  },
  "role_outputs": {
    "management": {
      "decision_ref": "#management-decision",
      "plan_ref": "#workmap",
      "issued_work_refs": [
        "#issued-task",
        "#question-work-binding"
      ],
      "delivery_scope_ref": "#management-delivery-scope"
    }
  }
}
````

采用关系：原件保持在 exact commit `46119a8e0030b4c3597634735cbe5d22ad3a0ac7`；新提交把上述修正版物化到当前规范路径，并同时保存 `ROLE_RETURN_REPAIR_R0002.json` 旁路审计件。不会重写旧 Git 对象。

<a id="r0002-sync-files"></a>
## 必要同步文件（完整）

### run README

````markdown
# BI-01 / RESTART-01 — 首次管理已完成，当前处于窄修复与专业派发门禁

**MANAGEMENT_R0001_RECEIVED / R0002_MANUAL_REPAIR / PROFESSIONAL_NOT_SENT / WORKMAP_NOT_ADOPTED**。

R0001 已完成首次实质管理并形成地图、当前任务和 Question Work Binding；其原始回答、Return、提示、receipt 与管理包继续由 exact commit `46119a8e0030b4c3597634735cbe5d22ad3a0ac7` 保留。R0002 只修复 Owner 授权的机器接线缺项，不重新执行 M-START，不产生专业结果，不签 G4，也不表示 Overlay12 prepare/verify 已通过。

<a id="common"></a>
## 运行身份与历史隔离

- 唯一新运行空间为本目录；业务协调器固定 `work_id=BI-01`，但 `run_id=BI-01-RESTART-01`、新 invocation/token/marker、管理/执行 chat/thread 和 local long-task 身份均与旧试跑隔离。
- 旧业务仓 `complex-systems-vocabulary/.../observation-iteration-runs/BI-01-IT-01/` 仍是已停止试跑的历史，不继承为本 run 的业务成果、当前任务、Gate 或在途。
- R0001 原管理业务判断继续有效；R0002 只修接线。原物理管理会话是 `BI01-R01-管理`。
- 当前没有任何专业执行消息发送证据；不得从地图、任务、Binding、commit 或 intake 准备状态推出专业任务已发送。

<a id="bi01"></a>
## 当前生效管理面与实际恢复顺序

已形成并保留：

- `00_长程推进地图.md`：R0001 的完整业务关系、阶段与后继；R0002 仅同步当前操作位置。
- `01_当前任务.md`：I4 真实业务观察（含定向 I3 核查）；当前 `task_id` 为 `BI01-RESTART-01-I4-EXECUTION-01`。
- `bindings/QUESTION_WORK_BINDING_I4.json`：模式采用 `OBSERVATION_I4`；全部业务引用为 exact Git locator；管理路线回到 `BI01-R01-管理`。
- `reviews/MANAGEMENT_START_R0001.md`：原管理业务决定，不改写。
- `reviews/MANAGEMENT_DELIVERY_REPAIR_R0002.md`：本次窄修复决定和原件／修复件关系。
- `provenance/turns/R0001/`：原始 R0001 历史与明确修复旁路件。
- `provenance/turns/R0002/`：本次管理修复回交；不是专业轮次。

后续顺序：

1. 操作端下载并验证 R0002 修复包，按原路径落库；
2. 提交、推送并远端读回；
3. 对修正版 task/binding/map/README 重新生成 snapshot，完成 reader 与 intake；
4. intake 的 `dispatch.task_id` 必须严格等于 `BI01-RESTART-01-I4-EXECUTION-01`；
5. 只有 Candidate intake、reader、binding、dispatch 与发送现场检查全部真实通过后，才可形成 `ADOPTED` 的 Workmap Binding；
6. 之后才能创建首个专业轮次并发送到未来的新专业聊天。当前仍禁止派发。

准确流程：[BI-01 真实运行合同](../../runtime/operations/BI01_REAL_RUN_V1.md)；[轮次合同](../../runtime/operations/ROUND_RECORD_CONTRACT.md)。
````

### 长程推进地图

````markdown
# BI-01-RESTART-01 长程推进地图

<a id="goal"></a>
## 1. 完整目标

建立由 AI 持续开展、Owner 在必要环节进行业务判断的业务观察与设计迭代过程。成功标准不是完成若干文件、图或计算，而是持续取得可检验的业务认识，并据此形成有依据的继续、修订、补 Case、停止或等待行动。

本次全新运行不继承旧 I4 试跑的业务输出、Gate、聊天或在途状态；旧材料只保留历史追溯资格。历史设计、原始数据和方法事实只有在本次重新采用并核清适用边界后，才进入当前证据链。

<a id="business-system"></a>
## 2. 正常系统的业务关系图

```text
Owner 总意图
  ↓
I1 选择值得观察的真实业务问题
  ↓ G1：问题有实质意义、边界可辨
I2 固定合法 Source / Method / Case / As-Of / Missingness
  ↓ G2：结果有合法取得途径
I3 取得并限定可信结果范围
  ↓ G3：哪些结果可以被观察，哪些只可参考/待修
I4 真实业务观察与挑战
  ├─ 事实过程
  ├─ 单品种 → 静态板块 → U2 → U2+U3 的增量/无增量
  ├─ 支持、反证、缺失、证据依赖
  ├─ 替代解释与反例
  └─ 下一项能缩小不确定性的观察
  ↓ G4：形成经挑战的实质业务认识
I5 Owner Pack
  ├─ Owner 可直接看懂的市场过程与图
  ├─ 增量/无增量和证据边界
  ├─ 争议与具体行动选项
  └─ 真正需要 Owner 回答的问题
  ↓ G5：材料足以支持真实判断
Owner 判断（只处理超授权或重要取舍）
  ↓
I6 将反馈转为可执行的下一轮任务
  ↓ G6：下一目标、输入、输出、Gate、责任和来源已准确安排
下一轮 I1～I6（必要时只回到受影响的前序 Gate）
```

本轮业务对象链：

```text
真实 30m KLine / Zig / ScaleTurn
  ↓
U2 C0：TurnOccurrence / SegmentEpisode / Episode Metric
  ├─ U2 N：单品种 NodeScaleTurnBehavior
  ↓
U2 C1：关系、Formation 与三项 assessment 的参考事实
  ├─ U2 S：ExternalSeparation
  ↓
U2 C2：候选资格、Identity、Commit/H1 边界
  ↓
U3 R02：成员 Movement objective facts
  ↓
U3 R03：Progress / Friction / Retention / Quality（当前 Withheld）
  ↓
I4：比较“单品种、静态板块、U2、U2+U3”究竟改变了什么认识
```

<a id="stage"></a>
## 3. 当前阶段与核心业务问题

### 当前阶段

- I1：Pass（本次管理重新采用）
- I2：Pass，限定为“当前冻结的 Reference/Shadow 观察路径”
- I3：分区接收  
  - 下游包的文件身份、导出记录和状态边界：Pass（限定范围）  
  - 当前上游包与承重市场路径：NeedsRepair，但只限制依赖这些事实的结论
- I4：已由管理签发，尚未派发；G4 尚未接收
- I5/I6：尚未开始

### 当前核心问题 Q-01

在 HC、RB、I 这一轮共同 Trough 转折过程中：

1. 三个成员在 Progress、Friction、Retention 和生命周期上怎样真实分化；
2. 这种分化是否只是 Working/Completed、确认延迟、比较时点、原始价格单位或临时方法造成；
3. 单看各品种、看固定钢铁板块、加入 U2 同轮组织、再加入 U3 Movement 后，业务认识分别新增了什么；
4. 若没有新增信息，缺失发生在哪一层，是否应停止或改造相应设计；
5. 下一项什么观察最能缩小不确定性。

本轮不预设 U2/U3 有效；“有据无增量”是合法结果。

<a id="evidence"></a>
## 4. 当前证据地图与资格

### 4.1 当前重新采用的附件

| 输入 | 当前身份 | 允许用途 | 禁止用途 |
|---|---|---|---|
| `steel_U2_U3_执行结果_20261010.zip` | SHA-256 `7bebbee3fd7d425eb85116f33c5d0e01ae2163e6849818515fe3824a82b9a46c`；23 CSV 已读取 | 导出事实、Reference/Shadow 状态、五个 As-Of 切面、定向路径核查 | 冒充正式 OpportunityCluster、正式 H1、U3 Quality 或生产验收 |
| `rb_hc_i_mid贴近转折_zig_small_K线_20210101_20240229.zip` | 当前实际 SHA-256 `4fd1af4e7b34af6fc099e6289ffdd5d83125412fc16d2a9902af4fd9741b3987`；包内 manifest 自洽 | 作为本次重启的新候选 DataBinding，完成 Case 行级/路径级核对后，支持限定市场观察 | 静默等同历史记录中的 `ff3215...` 原件；在未核承重路径前发布强市场结论 |

管理决定：不再把取得历史 `ff3215...` 原件作为全线前置。当前实际包可作为新 DataBinding；但必须保留自己的真实 hash，并完成 Case-01 的定向 C0/R02 核对。不存在必要性去重建全部 Runner 或审计整个仓库。

### 4.2 已确认的下游业务边界

- `official_cluster_committed=NO`
- `official_h1_emitted=NO`
- Shadow 主体为 `ShadowOpportunityClusterNotCanonical`
- H1 authority 为 `NOT_AUTHORIZED_NO_U2_SNAPSHOT_H1`
- R03 的三个轴均 `CalibrationPending`
- `quality_judgement=WITHHELD`
- `capital_use=WITHHELD`
- C1 兼容矩阵来源为 `NEW_REFERENCE_MATRIX_NOT_MISSION_C_APPROVED`
- S 当前 `universe=hc|i|rb`、`outside_count=0`、`EXPLICIT_RESEARCH_UNIVERSE_ONLY`

因此本轮观察主语固定为：

> “Reference/Shadow 同轮转折候选及成员 Movement objective facts”

不得称为：

> “正式 OpportunityCluster 及正式 U3 Quality”。

### 4.3 已发现的承重时间问题

五个切面为 2021-05-06、05-07、05-11、05-14、05-18 10:00。2021-05-11 10:00 的 R02 中：

- HC 是 `WorkingSoFar`，观测 38 bar；
- RB 是 `Completed`，完成段 33 bar；
- I 是 `Completed`，完成段 1 bar。

更关键的是，HC 的完成在 10:30 才可见，却把实际结束回定到 2021-05-10 21:30；I 也存在确认后把实际结束回定到更早时点的情况。因此必须同时保留：

1. **As-Of 当时可知的 Working 视图**；
2. **后来可见的 canonical Completed 视图**；
3. **同成熟度/共同前缀的公平比较视图**。

禁止用后来才知道的 Completed 边界回填旧 As-Of，也禁止继续把已完成 Episode 延长。

<a id="current-adoption"></a>
## 5. 当前采用、撤销与保留

### 采用

- Q-01 与真实 HC/RB/I Case A；
- 五个 As-Of 切面，而不是只看 2021-05-11 单点；
- 下游 Reference/Shadow 导出事实；
- 当前上游实际 hash 作为候选新 DataBinding；
- 四层增量比较；
- 必要的定向 I3 核查与 I4 连续推进并行。

### 撤销为当前要求

以下不再是本轮当前任务、前置、验收或未来必做：

- 继承旧 I4 试跑发现、Gate、聊天和在途状态；
- 先完整审计全部仓库、恢复全部 Runner/Trace，再做业务观察；
- 把 A/B/C 三类 Case 当固定配额；
- 先做正式 C2/H1 或 R03 Quality 校准；
- 以图数、文件数、测试数或代码量证明业务增量；
- 让执行 Pro 重新裁定管理已经明确的材料权力与删除决定；
- 让 Worker/操作端判断投资业务；
- 本阶段开展 FGL/WSPD、通用 Ontology、平台重构或全市场扩域。

### 保留

- actual / observed / confirm / As-Of 区分；
- Source、Method、DataBinding、状态、Missingness；
- Formation、Quality、ExternalSeparation 分责；
- 支持、反证、证据重叠和替代解释；
- 正确的历史事实与可追溯记录；
- 正式方法、Reference 方法与 Shadow 方法的边界。

<a id="progress"></a>
## 6. 已完成

1. Owner 已启动新 run，并明确旧 I4 试跑不继承。
2. M-START 的完整目标、阶段合同、角色合同、I4 方法和运行约束已读取。
3. 两个附件已实际读取；下游包 hash/23 CSV、上游包实际 hash/manifest/关键范围已核。
4. 当前正式/参考/Shadow/Withheld 边界已裁定。
5. G1、G2 和分区 G3 已由管理作出当前决定。
6. 当前 I4 的完整范围、第一重点、验收标准、管理触发和执行 Pro 任务已形成。
7. 不需要 Owner 现在补任何业务决定。
8. R0001 原始回答、Return 和管理包已保存在 exact commit；R0002 只修复 task_id、Return 引用、mode、carrier 和实际管理路线，不改变业务判断。

<a id="remaining"></a>
## 7. 全部重要剩余

### 当前 I4 必须完成

- Case-01 的承重 C0/R02 行与原 KLine 路径定向核对；
- actual/confirm/knowledge/As-Of 和 Working/Completed 的完整时间线；
- 单品种、静态板块、U2、U2+U3 四层增量或无增量；
- 对公平比较、证据重叠、临时方法、选择偏差和替代解释的挑战；
- 至少形成一个可复查 BusinessFinding 或有据无增量结论；
- 证据需要时选择下一项真实反例/重复样本，不把 Case A 当正常停点。

### 后继

- G4 候选形成后，由管理接收；
- G4 Pass 后进入 I5 Owner Pack；
- Owner 只在出现正式方法投入、扩 Universe、校准 Quality、改变业务方向等真实取舍时介入；
- I6 将判断转为下一轮明确任务。

### 尚未覆盖

- 独立专业审查方法当前不存在，不能冒称独立 PASS；
- 正式 OpportunityCluster/H1/U3 Quality 未形成；
- 全市场普遍规律未建立。

<a id="management"></a>
## 8. 管理安排与复看

管理在以下条件实际复看：

1. 执行 Pro 形成 G4 候选或有据无增量；
2. 承重 Source/Method 冲突改变可消费范围；
3. Owner/正式方法/业务前提发生变化；
4. 连续两次有效执行 Pro 调用仍只停留在来源、工具、格式或运行准备，没有实质业务观察。

第 4 项按工作 ACTIVE 时每两次有效调用复看，但不强制通过、缩范围或冻结无关工作。

所有管理接收、裁定与复看 route 均回到同一原物理管理会话 `chatgpt-project:细节叙事生成_金标/chat:BI01-R01-管理`；未来专业执行 route 继续指向独立的新专业聊天。

<a id="next"></a>
## 9. 实际下一步

1. 将 R0002 窄修复件按原路径落库，保留 R0001 exact-commit 原件与旁路修复件。
2. 对修正版地图、README、当前任务和 Binding 做提交、远端读回、fresh snapshot、reader 与 workmap intake；intake 的 `dispatch.task_id` 必须为 `BI01-RESTART-01-I4-EXECUTION-01`。
3. 只在 Candidate intake、reader、binding、dispatch 和未发送现场检查全部真实通过后，形成 `ADOPTED` 的 Workmap Binding；R0002 本身不宣称这些 Gate 已通过。
4. 之后才创建首个专业轮次，并把当前任务发送到未来的独立专业聊天；当前仍未派发。
5. 执行 Pro 连续推进 I3 定向核查和 I4，不以单一 Case、图、文件或局部修复结束；管理按上列条件接收、返修或进入 I5。
````

### Workmap Binding Candidate

````json
{
  "schema": "workmap-binding/v2",
  "status": "PENDING_MATERIALIZATION_AND_INTAKE",
  "manager_role": "management",
  "overview": {
    "path": "runs/BI-01-RESTART-01/README.md",
    "anchors": [
      "common",
      "bi01"
    ]
  },
  "shared_overview_anchors": [
    "common"
  ],
  "owner_sources": [
    "runs/BI-01-RESTART-01/OWNER_START.md",
    "professional/source/00_AGENT_CHARTER_AND_STAGE_CONTRACT.md"
  ],
  "rule_paths": [
    "professional/source/00_AGENT_CHARTER_AND_STAGE_CONTRACT.md",
    "professional/source/01_I1_I3_PROFESSIONAL_CONTRACT.md",
    "professional/source/02_I4_OBSERVATION_AND_CHALLENGE.md",
    "professional/source/03_STAGE_HANDOFF_AND_READINESS.md",
    "professional/source/04_PRO_WORKER_CODEX_HANDOFF.md",
    "professional/source/05_ROLE_GATE_AND_HANDOFF_CONTRACT.md",
    "runtime/dual_route_execution/DR13_WORK_ARRANGEMENT_AND_CONTEXT.md",
    "runtime/dual_route_execution/DR14_QUESTION_WORK_CONTRACT.md",
    "runtime/overlay/08_自然语言运行提示_v0.3.md"
  ],
  "receipt_path": "runs/BI-01-RESTART-01/reviews/WORKMAP_INTAKE_CURRENT.json",
  "streams": {
    "bi01": {
      "map": {
        "path": "runs/BI-01-RESTART-01/00_长程推进地图.md",
        "anchors": [
          "goal",
          "stage",
          "evidence",
          "progress",
          "remaining",
          "management",
          "next"
        ]
      },
      "task": "runs/BI-01-RESTART-01/01_当前任务.md",
      "overview_anchors": [
        "bi01"
      ],
      "watch_roots": [
        "runs/BI-01-RESTART-01/artifacts",
        "runs/BI-01-RESTART-01/reviews/independent"
      ]
    }
  },
  "management_decision": "runs/BI-01-RESTART-01/reviews/MANAGEMENT_START_R0001.md",
  "question_work_binding": "runs/BI-01-RESTART-01/bindings/QUESTION_WORK_BINDING_I4.json",
  "note": "R0001 business judgement preserved. R0002 manual repair selects task_id BI01-RESTART-01-I4-EXECUTION-01, professional_mode OBSERVATION_I4, exact Git carriers, and management chat BI01-R01-管理. Candidate only: after repair files are committed, remotely read back, and fresh reader/intake/dispatch checks pass, materialize an exact ADOPTED binding. Do not dispatch professional work before then."
}
````

### R0002 管理修复决定

````markdown
# BI-01-RESTART-01 R0002 管理交付窄修复决定

- invocation：`BI01-RESTART-01-R0002-c19efdc130c1995d4660ca4907747429`
- assignment token：`dc5df7008bbcb41665e37aea084c100e`
- authority：`OWNER_AUTHORIZED_MANUAL_REPAIR`
- Overlay12：`NOT_RUN_NOT_PASS`
- 原管理会话：`BI01-R01-管理`
- 业务范围：不变；不重新执行 M-START；不派发专业任务；不签 G4；不宣称 Workmap `ADOPTED`

## 六项决定

1. **task_id**：选择 `BI01-RESTART-01-I4-EXECUTION-01`。修正版 `01_当前任务.md` 只新增这一身份行；后续 intake 的 `dispatch.task_id` 必须完全一致。
2. **R0001 ROLE_RETURN**：保留 exact-commit 原件，新增修复旁路件，并将相同修正版物化到当前规范路径供 `after-return` 读取。唯一新增字段是指向原 R0001 `QUESTION_WORK_RETURN.json` 的非空 `question_work_ref`。
3. **professional_mode**：选择 `OBSERVATION_I4`。当前主体是 I4 真实结果观察与反证挑战；定向 I3 是 I4 任务内的证据资格核查，不另造 mode。
4. **Binding carrier**：删除 Binding 中全部 `answer_ref`。规范载体分别为 R0001 exact commit 中的 `00_长程推进地图.md`、`01_当前任务.md` 与 `FULL_RESPONSE.md`；每个引用均带 exact commit/path/selector。
5. **route**：全部 management route 改为 `chatgpt-project:细节叙事生成_金标/chat:BI01-R01-管理`。未来 professional same-work/return-repair route 继续保留 `chatgpt-project:细节叙事生成_金标/chat:new:BI01-RESTART-01-I4-EXECUTION`；这不表示聊天已创建或任务已发送。
6. **同步文件**：修正 run README、地图的当前操作位置与 Workmap Binding Candidate 说明；原 `MANAGEMENT_START_R0001.md` 和业务正文不重写。

## 原件与修复件

- R0001 原始历史：`daowei2026/observe-iterate@46119a8e0030b4c3597634735cbe5d22ad3a0ac7:runs/BI-01-RESTART-01/provenance/turns/R0001/::tree`
- R0001 原 ROLE_RETURN：`daowei2026/observe-iterate@46119a8e0030b4c3597634735cbe5d22ad3a0ac7:runs/BI-01-RESTART-01/provenance/turns/R0001/ROLE_RETURN.json::full`
- R0001 原 QUESTION_WORK_RETURN：`daowei2026/observe-iterate@46119a8e0030b4c3597634735cbe5d22ad3a0ac7:runs/BI-01-RESTART-01/provenance/turns/R0001/QUESTION_WORK_RETURN.json::full`
- R0002 修复件不会改变上述 Git 对象；新提交只形成当前采用修正版和旁路审计件。

## 仍未满足

- 尚未由本回答写入或推送 GitHub；
- 尚未 remote readback；
- 尚未 fresh snapshot/reader/intake；
- 尚未运行修复后的 Candidate/binding/dispatch Gates；
- Workmap 尚未 `ADOPTED`；
- 专业任务尚未派发；
- Overlay12 仍为 `NOT_RUN_NOT_PASS`。
````

<a id="r0002-adoption"></a>
## 采用关系

- R0001 原业务决定与原始证据保持不变。
- 修正版任务只新增 task_id。
- Binding 只改 mode、carrier 与 recipient wiring。
- README、地图与 Candidate 只同步当前机械位置。
- R0002 返回只表示修复交付已形成，不表示已经落库或通过 Gate。

<a id="r0002-delivery-scope"></a>
## 本轮交付范围

交付修正版当前任务、Question Work Binding、R0001 ROLE_RETURN 修复件、同步 README/地图/Candidate、R0002 双 Return、说明和 manifest。没有生成专业分析或新业务工作。

<a id="r0002-handoff"></a>
## 后继

操作端下载、验哈、按路径落库、提交、推送、远端读回，然后重新运行 R0001 after-return、Candidate snapshot/reader/intake、binding/dispatch 与未发送现场检查。只有所有 Gate 真实通过后才可形成 `ADOPTED` 并创建首个专业轮次。

<a id="r0002-role-return"></a>
## ROLE_RETURN

````json
{
  "schema": "longrun-return/v1",
  "work_id": "BI-01",
  "invocation_id": "BI01-RESTART-01-R0002-c19efdc130c1995d4660ca4907747429",
  "assignment_token": "dc5df7008bbcb41665e37aea084c100e",
  "question_work_ref": "#r0002-question-work-return",
  "work_status": "SUBMITTED",
  "completed_scope_ref": "#r0002-repair-completed",
  "remaining_scope_ref": null,
  "artifact_refs": [
    {
      "answer_ref": "#r0002-current-task"
    },
    {
      "answer_ref": "#r0002-binding"
    },
    {
      "answer_ref": "#r0001-role-return-repair"
    },
    {
      "answer_ref": "#r0002-sync-files"
    }
  ],
  "delivery": {
    "status": "READY",
    "missing_refs": []
  },
  "materials": {
    "use_record_ref": "#r0002-material-use",
    "unread_required": [],
    "unavailable_required": []
  },
  "handoff": {
    "kind": "SUBMIT",
    "route_key": "bi01_management_manual_repair_to_coordinator",
    "instructions_ref": "#r0002-handoff"
  },
  "role_outputs": {
    "management": {
      "decision_ref": "#r0002-decisions",
      "plan_ref": "#r0002-adoption",
      "issued_work_refs": [
        "#r0002-current-task",
        "#r0002-binding"
      ],
      "delivery_scope_ref": "#r0002-delivery-scope"
    }
  }
}
````

<a id="r0002-question-work-return"></a>
## QUESTION_WORK_RETURN

````json
{
  "schema": "question-work/v2",
  "kind": "RETURN",
  "work_id": "BI-01",
  "invocation_id": "BI01-RESTART-01-R0002-c19efdc130c1995d4660ca4907747429",
  "binding_ref": {
    "repo": "daowei2026/observe-iterate",
    "commit": "003d6700e20c7feed7a9d30147e673f39380d082",
    "path": "runs/BI-01-RESTART-01/BOOTSTRAP.json",
    "selector": "full"
  },
  "focus_results": [
    {
      "question_id": "M-START",
      "completed_ref": {
        "answer_ref": "#r0002-repair-completed"
      },
      "remaining_ref": null,
      "affected_refs": [
        {
          "answer_ref": "#r0002-decisions"
        },
        {
          "answer_ref": "#r0002-current-task"
        },
        {
          "answer_ref": "#r0002-binding"
        },
        {
          "answer_ref": "#r0001-role-return-repair"
        },
        {
          "answer_ref": "#r0002-sync-files"
        }
      ]
    }
  ],
  "material_use_ref": {
    "answer_ref": "#r0002-material-use"
  },
  "trigger_observations": [],
  "continuation_ref": {
    "answer_ref": "#r0002-handoff"
  },
  "batch_remaining_ref": null
}
````
