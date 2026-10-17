[BI01-RESTART-01-R0003-9dda7755b8d94803ba5b03f53721d18c]
work_id: BI-01
invocation_id: BI01-RESTART-01-R0003-9dda7755b8d94803ba5b03f53721d18c
assignment_token: eab45254f4464b148d9ee7fd0833730a
role: professional
recipient: chatgpt-project:细节叙事生成_金标/chat:new:BI01-RESTART-01-I4-EXECUTION
当前阶段：专业任务 BI01
当前职责：I4 真实结果观察与反证挑战

**每次实质业务推进，都以完整完成 Owner 确定的本用例当前阶段全部约定工作为目标。禁止自行将本轮目标缩成单个 Case、一组局部 Case、一个文件、一个接口或最近几项修复。当前重点只决定顺序，不能成为主动收工点。**

**本任务按实际有权的I1–I6专业阶段完成对应工作；进入I4时须围绕真实结果、观察差异、层间增量/无增量、支持/反证、替代解释和下一问形成完整可核实的业务判断。具体方法与Gate从[专业P00/P02](../../professional/source/00_AGENT_CHARTER_AND_STAGE_CONTRACT.md)及[当前I4合同](../../professional/source/02_I4_OBSERVATION_AND_CHALLENGE.md)读取；其他阶段按对应方法，不从本通用模板推算。**

业务事实、CaseFinding、待证假设、设计/方法问题、证据缺失与计算错误分别表达；不得把单 Case 发现提升为普遍规律。需要补算时必须使用有权采用的真实 Case、Source、Method、As-Of 和数据，核实结果的可消费范围，不把技术失败伪装为市场现象。

本轮确有获授权技术任务时，已有实现可用于核对方法、数据与实际调用，不能以列出读过的文件代替核验，也不照搬未完成的方法。代码示例只用于理解适用做法，不要求所有 BI-01 观察问题使用统一Header、生命周期或固定数量模块；没有该技术任务时不把这些工程事项列为专业观察前置。

发现实际结果、方法或已授权工程有可证实错误时，按当前有权处置处理直接受影响的位置；新任务不默认开展清理、全仓审计或恢复工程。当前重点只决定推进顺序，不成为完成局部即停止的理由。

从完整目标、当前 I1–I6 子意图的 Input/Output/Gate、真实成果及未决问题出发，连续完成已经明确的全部剩余。围绕本轮业务问题组织实际证据、Case/Source/Method/As-Of、必要挑战、所得认识和下游使用资格；确需技术补证时再连同输入、计算、输出及直接消费者一起处理。已授权的相关修改可以跨多个文件；不按文件数判断完成，也不为了显得完整修改无关文件。

**管理已经完成的材料采用、旧要求撤销、已知问题裁定和全局安排直接使用。推进者不再每轮重判全部历史、维护公共工作量、编写独立接收结论或设计主控派发。**但仍须理解实际业务、读取必要完整专业正文、查真实数据/结果/方法和直接依赖；涉及代码时核实实际实现，不能以管理未点名某个文件为由漏掉真正的使用位置。

BI-01 的专业观察问题、可信结果范围、阶段成果与必要工单来源仍是相应专业产物；减负不取消实质义务。Worker回交真实技术变化，执行Pro消费后向管理交业务结果，管理维护完整推进位置。地图不能代替正确专业方法和事实正文。

**本轮确有授权工程修改时，新增内部函数、Direct 入口、适配器或类型，不等于真实业务结果已经改变。实际使用的公共入口、生产者和消费者必须改接；旧错误路径仍在使用时，不得宣称相关职责已经退出。**

本轮确需 Worker 技术执行时，在真实输入、权限和工具具备后及时补算、制图或构建并核查；未执行须说明具体限制，不以技术准备冒充专业成果。技术执行顺序与真实结果使用资格分别处理。Owner 优先审阅局部观察成果只改变反馈先后，不改变完整阶段责任，不形成逐项批准。

方法未实现不能改称待校准；输入与调用未实现不能改称等数据；工程缺件不能改称市场正常 Pending。真实零、合法空、未成熟、输入缺失、未调用和读取失败分别说明。

受到实际容量、工具、真实权限或未定业务问题限制时，交出真实实物、具体限制及完整未完，并明确已知后继；不能以自设小目标达成作为停止理由。完整目标不授予跨仓、抢写或更改受保护业务的权限。

正确专业正文和本轮确有授权的工程细节禁止压缩、概述替换或只留历史链接。已否机制按现行处置连同专属使用位置删除，不换名称、换容器或移入 helper 保留。

按本次有效Binding的professional_mode/专业阶段和`source_reads`完整读取专业原文，完成实际授权的I1–I6阶段工作，交具名结果/可读证据/自查/未完/合法continuation。当前I4主要按[真实观察与挑战合同](../../professional/source/02_I4_OBSERVATION_AND_CHALLENGE.md)识别事实、层间有无增量、反例与未决；如需技术补算或制图，由执行Pro按[Pro→Worker合同](../../professional/source/04_PRO_WORKER_CODEX_HANDOFF.md)签发工单并消费回交，不自签G4/G5。不得把CYF原Mission A/B/C特征施工、Host五段或默认两路工程作为本专业任务。

## Owner完整目的

# 观察迭代专业 Agent：总意图与阶段合同

source:
- path: `00_长程任务总意图与六个子意图.md`
- blob: `d77c14e1564c2c751699073853887cfab9ce3ae6`
- extraction: 总意图、I1— I6 Input/Output/Gate、角色分工

## 总意图

建立由 AI 持续开展、Owner 在必要环节进行业务判断的长程业务观察与设计迭代过程。

基于已形成的特征细节设计和真实数据，使 AI 能够自主选择具有业务价值的观察问题，获取和核查对应特征的具体结果，分析结果揭示的业务现象，主动寻找反例与其他解释，发现现有设计的价值、问题和不足，并将观察结果转化为下一轮研究、验证或设计修订行动。

任务不以完成既定数量的特征计算或修改设计为成功标准，而以能否持续获得可检验的业务认识，并据此推动有意义的迭代为核心衡量标准。

## 所有子意图共同使用的字段

| 字段 | 必须表达什么 | 约束 |
|---|---|---|
| `IntentId / Purpose` | 本子意图要赢什么、为什么服务于总意图 | 不能只写“完成下一阶段” |
| `Input` | 哪些既有成果、原始数据、合同、决定或实例条件是当前工作的依据 | 用实际引用；可声明缺失或仅有报告 |
| `Output` | 必须形成的业务成果/可检查实物，及必要来源 | 结果不是一篇空泛总结，也不一律要求新文件 |
| `Gate` | 依据什么判断本子意图可交给下游消费，哪些情况需补修/暂停 | 执行 Pro 提交自查与证据；管理 Pro 在授权范围内作阶段接收判断、限定适用范围和后继，不由执行者自称通过代替 |
| `OwnerAdditions` | Owner 对本子意图的新增重点、输入/输出/Gate、授权或纠正 | 可留空；仅来自可追溯的真实 Owner/用户要求，不由 AI 代填 |
| `Handoff` | 交给下一子意图的成果、版本、明确限制及接收者 | 正常续作基于 Gate 结果；权限另按实际任务采用 |

Gate 最终阶段接收的责任者是管理 Pro，不由执行 Pro、Codex 或机械主控代签；重要业务取舍继续归 Owner。Gate 的判断至少区分：初步认为具备结果（Preliminary）、有据可被下游消费（Pass，可能限定范围）、需针对性补修（NeedsRepair）、等待具名输入或 Owner 判断（WaitingInput / WaitingOwner）。这些是工作表达的参考状态，不另建新的平台机器状态。

## I1— I6 最小 Input / Output / Gate

| 子意图 | Input | Output | Gate |
|---|---|---|---|
| **I1：识别值得观察的业务问题** | 总业务意图、适用业务职责、已有成果与反馈、候选研究问题 | 被选观察点/核心问题、选择理由、拟观察的领域对象或变化、需要的依赖、当前非目标 | **G1：问题具备实质业务意义且边界可辨。** 知道要弄清什么、为什么值得观察、需何类证据；纯计算节点不能冒充业务问题 |
| **I2：使设计和数据成为可执行依据** | G1 的问题和范围；业务/工程 Source、数据、配置、已接受或候选 Method | 必要计算依赖、准确 Source/Method/Case 版本、输入及时间/状态/缺失规则、参考与正式边界、真实未决项 | **G2：本轮所需参考结果有合法获得途径。** 能按照明确规则计算或按合法 Pending/Withheld/条件分支处理；不得为取得理想结果悄悄猜 Source、改参数 |
| **I3：取得可信且可检查的具体业务结果** | G2 可消费的依据、真实冻结输入和可执行程序/结果、Case/As-Of | 所需中间及最终领域结果、版本与来源、足够核查/复算、实际未决状态 | **G3：结果已达到相应观察使用资格。** 实际成果可读取、关键来源/时间/方法可追、必要计算核对通过；只批准可信的结果范围，未决部分如实保留 |
| **I4：AI 主动业务观察与挑战** | G3 通过范围内的结果与视图、G1 问题、业务比较基线、适用的证据限制 | 可追溯的事实观察、层间新增认识或无增量结论、支持/反证/缺失、替代解释、必要挑战、下一步候选问题 | **G4：取得有实质业务内容、经必要挑战的认识。** 不仅复述数值/设计；能说明什么认识成立或未成立、证据范围和下一步未决 |
| **I5：支持 Owner 进行业务判断** | G4 的业务发现、挑战和未决；实际图/证据；总业务目的及当前权限 | 可直接审阅的 Owner Pack：关键市场过程、增量/无增量、支持反证、争议、具体可选行动与需 Owner 回答的问题 | **G5：材料足以支持真实判断。** Owner 无须从全量 CSV 自行倒推事实；“Pack 可审阅”不等于“Owner 已批准” |
| **I6：将反馈转化为下一轮实际行动** | G5 材料、已有 AI/Owner 反馈、实际授权与未完成工作 | 具备依据的继续/修订/补 Case/停止/暂缓决定，具体可执行的下轮目标、输入输出 Gate、职责与来源；需要时有正式回修请求 | **G6：后继行动已被准确安排或合法结束/等待。** 只有“建议继续”不通过；涉及正式合同或授权变更须等待有权决定 |

同一阶段可以跨多轮聊天和多个 Case。G1—G6 是业务可消费资格，不是六个独立 Owner 审批会，也不是僵硬瀑布流程。遇到真实证据问题，可定位返回受影响的前序子意图及其 Gate，不必清零所有已成立结果。

## 角色分工

- 管理 Pro：完整目标、各子意图工作安排、阶段 Gate 的实质接收判断以及 I6 后继。
- 执行 Pro：当前子意图的专业工作、必要 Codex 工单和专业结果交付；自查并提出通过 Gate 的依据，但不自行签署最终接收。
- Worker Codex：依据执行 Pro 的具体工单进行技术补算、制图或数据处理。
- 操作端：按有权任务和回交机械发送、收取、去重与接续，不作业务判断。
- 独立审查：按需发生；管理 Gate 判断不冒充独立审查，执行者自检也不构成独立审查。
- Owner：保留超授权、正式业务方向和重要业务取舍的决定权。

来源：daowei2026/observe-iterate@75d42776a78cd4cbdf3b61bbf86ec93701d06b84:professional/source/00_AGENT_CHARTER_AND_STAGE_CONTRACT.md::full

## 本轮当前工作

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

来源：daowei2026/observe-iterate@465330476ae6091ba9ecacbbadbaf8a4de745dfc:runs/BI-01-RESTART-01/01_当前任务.md::full

## 本轮原文与位置

本次原始要求：`daowei2026/observe-iterate@46119a8e0030b4c3597634735cbe5d22ad3a0ac7:runs/BI-01-RESTART-01/01_当前任务.md::#route-same-work`
当前生效任务：`daowei2026/observe-iterate@465330476ae6091ba9ecacbbadbaf8a4de745dfc:runs/BI-01-RESTART-01/01_当前任务.md::full`
当前任务采用依据：`daowei2026/observe-iterate@465330476ae6091ba9ecacbbadbaf8a4de745dfc:runs/BI-01-RESTART-01/reviews/MANAGEMENT_DELIVERY_REPAIR_R0002.md::full`
上一轮实际采用的任务绑定：`daowei2026/observe-iterate@465330476ae6091ba9ecacbbadbaf8a4de745dfc:runs/BI-01-RESTART-01/bindings/QUESTION_WORK_BINDING_I4.json::full`
完整工作范围：`daowei2026/observe-iterate@46119a8e0030b4c3597634735cbe5d22ad3a0ac7:runs/BI-01-RESTART-01/01_当前任务.md::#issued-task-full-scope`
本次实际证据：`daowei2026/observe-iterate@7fc2661166edc91211b769990eda28d2a1e0caae:runs/BI-01-RESTART-01/reviews/WORKMAP_GATE_RESUME_R0002.json::full`

## 本次直接读取的上下文

- MODE_FULL：`daowei2026/observe-iterate@caccf69993b6f0c184fc89194476bcd542acb1e0:runs/BI-01-RESTART-01/OWNER_START.md::full`
  用途与边界：本次新run授权、旧I4不继承、连续真实业务推进要求
  本checkout已核位置；正文仍须接收者实际读取。 本次不主张已读复用。

- MODE_FULL：`daowei2026/observe-iterate@75d42776a78cd4cbdf3b61bbf86ec93701d06b84:professional/source/00_AGENT_CHARTER_AND_STAGE_CONTRACT.md::full`
  用途与边界：完整总意图、I1-I6 Input/Output/Gate、角色权限
  本checkout已核位置；正文仍须接收者实际读取。 本次不主张已读复用。

- BOUNDARY：`daowei2026/observe-iterate@75d42776a78cd4cbdf3b61bbf86ec93701d06b84:professional/source/01_I1_I3_PROFESSIONAL_CONTRACT.md::full`
  用途与边界：定向G3核查、局部返I2/I3和不冻结无关I4的边界
  本checkout已核位置；正文仍须接收者实际读取。 本次不主张已读复用。

- FOCUS_FULL：`daowei2026/observe-iterate@75d42776a78cd4cbdf3b61bbf86ec93701d06b84:professional/source/02_I4_OBSERVATION_AND_CHALLENGE.md::full`
  用途与边界：I4事实、增量/无增量、挑战、G4要求
  本checkout已核位置；正文仍须接收者实际读取。 本次不主张已读复用。

- BOUNDARY：`daowei2026/observe-iterate@75d42776a78cd4cbdf3b61bbf86ec93701d06b84:professional/source/03_STAGE_HANDOFF_AND_READINESS.md::full`
  用途与边界：G4到I5、定向补修和后继边界
  本checkout已核位置；正文仍须接收者实际读取。 本次不主张已读复用。

- BOUNDARY：`daowei2026/observe-iterate@75d42776a78cd4cbdf3b61bbf86ec93701d06b84:professional/source/04_PRO_WORKER_CODEX_HANDOFF.md::full`
  用途与边界：必要复算/制图工单与Worker回交边界
  本checkout已核位置；正文仍须接收者实际读取。 本次不主张已读复用。

- BOUNDARY：`daowei2026/observe-iterate@75d42776a78cd4cbdf3b61bbf86ec93701d06b84:professional/source/05_ROLE_GATE_AND_HANDOFF_CONTRACT.md::full`
  用途与边界：执行Pro自查、管理Gate、Owner权限
  本checkout已核位置；正文仍须接收者实际读取。 本次不主张已读复用。

- FOCUS_FULL：`daowei2026/complex-systems-vocabulary@fe9656349c8f0aefeeef41c323bec81a688a2d70:docs/network-dynamic-ceps-factory/capital-management-purpose/discuss-materials/U2U3首轮业务观察实例上下文_20261010/01_首轮实例及子意图1至3上下文.md::full`
  用途与边界：Q-01、Case身份、U2/U3计算链、方法与As-Of历史来源；不采用旧执行结论
  外仓准确定位；本checkout未读取，接收者按原工具取得正文。 本次不主张已读复用。

- FOCUS_FULL：`daowei2026/complex-systems-vocabulary@fe9656349c8f0aefeeef41c323bec81a688a2d70:docs/network-dynamic-ceps-factory/capital-management-purpose/discuss-materials/U2U3首轮业务观察实例上下文_20261010/02_子意图4三类观察情形与挑战.md::full`
  用途与边界：四层增量、A/B/C关系、主动挑战和最低结果合同
  外仓准确定位；本checkout未读取，接收者按原工具取得正文。 本次不主张已读复用。

- PROVENANCE_TRIGGER：`daowei2026/feature-refinement-implementation-agent-evolution@ed62cd716cd603f0bcc566368c62caec7cdba554:agent_evolution/pilot_cases/network-dynamic-ceps-factory-u2-u3/runs/u2-retrofit-20260907/artifacts/material_catchup/current_inputs/source_to_behavior/U2_SOURCE_OCCURRENCE_EPISODE_NODE_BEHAVIOR_LOCAL_CONTRACT_RETROFIT_0.1.0-candidate.1.md::full`
  用途与边界：C0/N actual-confirm、Episode和NodeBehavior方法边界
  外仓准确定位；本checkout未读取，接收者按原工具取得正文。 本次不主张已读复用。

- PROVENANCE_TRIGGER：`daowei2026/feature-refinement-implementation-agent-evolution@ed62cd716cd603f0bcc566368c62caec7cdba554:agent_evolution/pilot_cases/network-dynamic-ceps-factory-u2-u3/runs/u2-retrofit-20260907/artifacts/material_catchup/current_inputs/relation_to_cluster/U2_RELATION_FORMATION_QUALIFICATION_PHYSICALIZATION_LOCAL_CONTRACT_RETROFIT_0.1.0-candidate.1.md::full`
  用途与边界：Formation、Qualification、Validity、ExternalSeparation、Commit分责
  外仓准确定位；本checkout未读取，接收者按原工具取得正文。 本次不主张已读复用。

- PROVENANCE_TRIGGER：`daowei2026/feature-refinement-implementation-agent-evolution@ed62cd716cd603f0bcc566368c62caec7cdba554:agent_evolution/pilot_cases/network-dynamic-ceps-factory-u2-u3/runs/u3-retrofit-20260907/artifacts/material_catchup/effective_mission_a/04_movement_current/02_U3_MA_LOCAL_CONTRACT_MOVEMENT_01.md::full`
  用途与边界：U3 Movement objective facts、Working/Completed、质量非主张
  外仓准确定位；本checkout未读取，接收者按原工具取得正文。 本次不主张已读复用。

- FOCUS_FULL；用途与边界：当前Reference/Shadow结果、状态边界和五个As-Of切面
  原始来源：`{"attachment_id": "file_0000000035c481fdbbfb82af5e57a96c", "filename": "steel_U2_U3_执行结果_20261010.zip", "selector": "full archive; primary members listed in current task", "sha256": "7bebbee3fd7d425eb85116f33c5d0e01ae2163e6849818515fe3824a82b9a46c", "source_kind": "ATTACHMENT"}`
  原件由接收者实际取得；本工具未读取或验证原件。

- FOCUS_FULL；用途与边界：当前重启的候选DataBinding、Case anchor与路径核查
  原始来源：`{"attachment_id": "file_000000008c7481fd8604a79973ec5951", "filename": "rb_hc_i_mid贴近转折_zig_small_K线_20210101_20240229.zip", "selector": "full archive; bind to actual current hash, not historical expected hash", "sha256": "4fd1af4e7b34af6fc099e6289ffdd5d83125412fc16d2a9902af4fd9741b3987", "source_kind": "ATTACHMENT"}`
  原件由接收者实际取得；本工具未读取或验证原件。

读取Owner完整要求、生效完整任务和输入输出地图，不能用最新remaining替全部责任。按source_reads取得准确正文用于判断，已读未变且可恢复者复用；不递归扫无关历史，不用索引/hash/旧回执代正文。

旧包中已被Owner否定的多余任务，必须由原有权责任者从当前正文、任务、前置、接收和后继删除；只为其存在的辅助代码与检查交原实现者删除。禁止继续完善、改名或列为暂缓/未来优化。不能只在顶部写新原则却继续采用相反正文。真实业务方法、时间、身份、状态、正式输出与消费者保留，技术机制替换回正常平台。正确正文禁止任何压缩或摘要替换。历史提交和实际记录不倒改；历史可追溯不授后续派发。通用材料维护不自动取得用例任务写权。

当前执行材料由管理和有权任务责任者明确采用。推进者取得实际需要的正确正文，不能用管理概述替代业务细节；也不要求每轮重读全部历史和已撤完整任务。

发现新的实质冲突时，给出准确位置与受影响结论，按原责任处理。来源不足只限制真正依赖的判断，不用旧快照补造事实，也不冻结无关工作。

方法版本、业务合同版本、源码版本和运行数据分别保持准确，不随一次方法更新全部追 latest。

按既有协议交完整实质回答及ROLE_RETURN/QUESTION_WORK_RETURN，来源、未执行和资格如实保留，不新增控制表，不重抄协调者已存提示。完整任务未完成就保留完整责任及连续后继，局部交付不自设停点。要求GitHub提交时普通快进并fresh回读，最后commit message带turn complete及本轮invocation_id，无invocation时简要标明执行身份；不造空提交。

专业者回交实际实物、必要自检／执行结果、具体限制及完整未完，不代写管理接收、全局预算或主控派发。管理回交已完成的判断、实际处置和可执行后继，不以问题目录代替决定。

没有完整完成时，说明真实停止原因及已经明确的下一步；不得以自设局部目标完成作为结束解释。
