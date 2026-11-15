[BI01-RESTART-01-R0005-427e020c096844a98f9f46148fce405c]
work_id: BI-01
invocation_id: BI01-RESTART-01-R0005-427e020c096844a98f9f46148fce405c
assignment_token: 8f4678dd01714eb8bc3a9d7f7cfcfe69
role: professional
recipient: chatgpt-project:细节叙事生成_金标/chat:BI01-RESTART-01-I4-EXECUTION
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

# BI-01-RESTART-01 当前任务：I4 成员选择增量检验

task_id: BI01-RESTART-01-I4-EXECUTION-01

## 0. 角色与任务性质

recipient：BI-01 执行 Pro，原物理专业会话 `BI01-RESTART-01-I4-EXECUTION`。  
professional_mode：`OBSERVATION_I4`。  
当前阶段：I4；只有本任务明确指出的承重事实冲突才定向返回 I2/I3。  
你不是管理 Pro、Owner、Worker Codex 或操作端。你提交专业结果、自查和 Gate 依据，但不自行签 G4/G5。

<a id="full-scope"></a>
## 1. 完整范围

继续完成当前 I4 阶段全部约定工作：

- 从管理已限定接收的 G3 结果出发；
- 对真实 Case 形成可追溯事实和业务解释；
- 比较单品种、静态集合、U2 组织和 U2+U3；
- 形成增量或有据无增量；
- 主动挑战时间、成熟度、方法、证据依赖和选择偏差；
- 明确哪些发现可以进入 I5、哪些仍需补证；
- 形成结果后回管理接收。

当前 focus 只决定顺序。不得把一个字段、一个文件或一次复算作为主动停点；也不得未经管理再发散到第三 Case、I5 或正式方法工程。

<a id="accepted-input"></a>
## 2. 管理已接收的输入，直接采用

管理决定：

`runs/BI-01-RESTART-01/reviews/MANAGEMENT_GATE_DECISION_R0004.md::full`

以下结果不再重做：

1. 两个 ZIP 的实际 hash、CRC 和必要成员身份；
2. Case-01 anchor/end、五个 As-Of、15 条 R02 路径、N exact-6 基线；
3. HC/RB h33、h38 公平范围；
4. I h1 Completed 的解释边界；
5. R02 与 C0/N 的承重字段重合；
6. Case-01 的 G3/G4 ScopedPass；
7. U2 的同轮身份/可追溯性增量；
8. 当前 U3 尚未证明独立 Quality 增量的 Case-01 限定结果；
9. 旧 Episode 结果与当前市场状态必须分域。

如新证据与上述事实冲突，必须给出 exact 行、方法和受影响结论；不能笼统重开整套历史。

<a id="withheld-input"></a>
## 3. 当前禁用与已撤工作

### 禁用 claim

`completed_recovery_events` 暂不得按“重新触及 prior peak”消费。它不进入本任务的支持、反证、评分或完成条件。

### 已撤/非目标

- 恢复旧 I4；
- 完整 Runner 或全仓审计；
- 正式 Formation/C2/H1；
- R03 Quality 校准；
- 扩 Universe；
- A/B/C 固定配额；
- 平台、通用 UI、FGL/WSPD 或 Ontology；
- 修复 MF-01；
- 新建 Worker 工单作为任务前置；
- I5、I6 或 Owner Pack；
- 第三个 Case。

<a id="current-focus"></a>
## 4. 当前 focus：Case-02 成员选择增量

### 4.1 管理冻结的 Case

```yaml
case_ref: refonly-671359b4c10f73db5c
case_kind: SAME_ACTUAL_DIAGNOSTIC_NOT_FORMAL_FORMATION
actual_uti: 75344399
actual_ts: 2021-05-10 21:30:00
common_visible_asof: 2021-05-11 10:30:00
members: hc|rb
turn_type: Peak
expected_direction: Down
actual_lag_uti: 0
formal_formation_candidate_status: NOT_ISSUED_SCOPE_MATRIX_DELTA_AND_EPOCH_NOT_EVALUATED
formal_assessment_status: NOT_EVALUATED_F29_BC30_BC31
```

成员 turn：

```text
HC refonly-d5b779f4ad88a8a276
RB refonly-910213b3cc62a71bdf
```

第三成员 I 的比较事实：

```yaml
turn_id: refonly-4af5fd6260f29a3c68
actual_ts: 2021-05-10 11:00:00
source_visible: 2021-05-10 21:30:00
turn_type: Peak
expected_direction: Down
distance_from_hc_rb_actual: 5 common 30m bars
```

在 `2021-05-11 10:30:00`，HC/RB/I 均有可读 Down Working 路径。I 不是因数据缺失被排除。

### 4.2 核心问题

> 当静态集合中的三个品种都处于可观察的 Down 运动时，HC/RB exact-same-actual 组织把 I 排除在该轮之外，是否改变了业务认识；这个改变是否超出单品种路径和时间戳已经能直接给出的信息？

<a id="inputs"></a>
## 5. 输入

### 5.1 下游结果包

`steel_U2_U3_执行结果_20261010.zip`  
SHA-256：`7bebbee3fd7d425eb85116f33c5d0e01ae2163e6849818515fe3824a82b9a46c`

本段首要成员：

```text
baseline_U2_C0_N_C1/C0/02_turn_occurrences.csv
baseline_U2_C0_N_C1/C0/04_segment_episodes.csv
baseline_U2_C0_N_C1/C0/05_completed_episode_metrics.csv
baseline_U2_C0_N_C1/C0/06_episode_and_working_cuts_30m.csv
baseline_U2_C0_N_C1/N/01_node_behavior_cuts.csv
baseline_U2_C0_N_C1/N/02_node_behavior_metrics.csv
baseline_U2_C0_N_C1/C1/01_equal_actual_uti_candidate_facts.csv
baseline_U2_C0_N_C1/C1/02_pair_input_facts.csv
baseline_U2_C0_N_C1/C1/03_eight_relation_raw_observations.csv
baseline_U2_C0_N_C1/C1/04_member_post_turn_at_common_cut.csv
```

### 5.2 上游候选 DataBinding

`rb_hc_i_mid贴近转折_zig_small_K线_20210101_20240229.zip`  
SHA-256：`4fd1af4e7b34af6fc099e6289ffdd5d83125412fc16d2a9902af4fd9741b3987`

使用 HC/RB/I 的 KLine、mid ScaleTurn、exact confirmed Zig、manifest 和数据说明。保留原始空 OHLC；本 Case 若命中空值，明确限制，不填补。

### 5.3 已接收的专业结果

```text
R0003 REPORT.md
R0003 verify_case01.py
R0003 CHECK_SUMMARY.json
R0004 MANAGEMENT_GATE_DECISION_R0004.md
```

<a id="work"></a>
## 6. 连续专业工作

### A. Case 身份与资格

1. 核 HC/RB exact actual、Peak/Down、各自 source visibility；
2. 核 I 的早 5 bar Peak/Down 与 source visibility；
3. 明确 `same-actual diagnostic`、正式 Formation、静态集合和当前 N 状态四者不是同一个对象；
4. 不因 formal status 未发就把已存在的诊断事实写成 DataUnavailable；
5. 不因诊断事实存在就升级为正式 U2 Candidate。

### B. 三视图事实过程

在 `2021-05-11 10:30` 及必要后继切面，分别重建：

1. HC/RB exact-same-actual 两成员视图；
2. HC/RB/I 静态三成员视图；
3. 三个单品种/N 当前状态视图。

保留：

- actual / confirm / knowledge；
- Working / Completed；
- 原 Episode 与当前 Episode；
- common cut；
- 同成熟度或共同观察范围；
- 不可用和 Pending 的真实原因。

### C. 成员选择增量

逐项回答：

| 问题 | 必须形成的结果 |
|---|---|
| 为什么是 HC/RB，不是 I | 事实条件、方法条件、缺失条件分账 |
| 组织以后多知道什么 | 具体改变的业务命题，而不是“多了一组” |
| 静态集合能否得到同样认识 | 明确 baseline 和差分 |
| N 是否已足够 | 哪些判断已由单品种/N 给出 |
| C1 未 join N 的影响 | 具体阻断的 claim 和消费者 |
| U3 是否必要 | 只有实际改变判断时才算增量 |
| 对 Case-01 的影响 | 支持、缩窄、反证或不相关 |

### D. 反向挑战

至少覆盖：

- exact same actual 是否只是过强的时间筛选；
- I 早 5 bar 是否仍属于同一经济过程；
- common visible 时点是否让不同开始时间产生不公平成熟度；
- 三品种同方向是否只是静态板块共同运动；
- N 和 C1/U3 是否共享相同路径证据；
- 当前诊断候选 formal status 未发，能否合法支持当前命题；
- 端点选择是否改变成员差异；
- 是否存在“组织更清楚但没有新业务判断”的结果。

### E. I5 就绪判断

形成一张明确表：

```text
可进入 I5 的发现
仍只是 CaseFinding 的内容
仍是 Hypothesis 的内容
因具名 Source/Method 缺件不可判断的内容
当前是否存在需要 Owner 回答的问题
```

不得代管理启动 I5。

<a id="deliverables"></a>
## 7. 交付

1. Case-02 exact 身份与资格表；
2. HC/RB 两成员与 HC/RB/I 三成员的可知时间线；
3. 同成熟度/共同范围比较；
4. 静态集合 → same-actual 组织 → 必要时 U3 的增量/无增量矩阵；
5. 至少一条具名 CaseFinding 或 NoIncrementFinding；
6. 对 `RawNWindowAvailableButNotJoined` 的具体业务影响判断；
7. 对 Case-01 NI-01 的支持/缩窄/反证关系；
8. I5 就绪表；
9. 完整限制、替代解释和下一行动候选；
10. 一致的 ROLE_RETURN 与 QUESTION_WORK_RETURN。

<a id="completion"></a>
## 8. 本段完成条件

本段不是要求证明 U2/U3 有用。完成条件是：

- exact Case 合法；
- 三视图事实可追；
- 成员选择是否改变认识得到有据回答，或具名说明为何不可判断；
- 结论经过时间、成熟度、证据重叠和方法资格挑战；
- 不把诊断候选升级为正式结果；
- 不依赖 MF-01；
- 不外推市场普遍规律；
- I5 就绪边界清楚；
- 回管理作下一阶段决定。

完成后必须提交管理，不自行继续第三 Case。

<a id="worker"></a>
## 9. Worker Codex

当前没有已签 Worker 工单。执行 Pro可使用现有冻结数据做有界读取和复算；若确有无法在当前专业环境完成的技术缺件，先写清：

```text
业务问题
冻结输入
exact Case
所需输出
禁止推论
为什么现有数据读取不足
```

再决定是否发工单。不得把画图、代码或 Runner 当本段默认前置。

<a id="budget"></a>
## 10. 投入与复看

- 预计 1 次有效执行 Pro 调用；
- 结果完成、出现具名消费冲突，或 1 次有效调用结束，均触发管理；
- 本次不采用固定图数、文件数或 Case 数；
- 下一次管理必须决定进入 I5、定向补证或有据停止/修订。

<a id="trigger-selection-result"></a>
## 11. RESULT 触发

当成员选择增量、限定无增量或具名不可判断结果形成时，触发管理接收。

<a id="trigger-consumption-conflict"></a>
## 12. I2/I3 消费冲突触发

只有新的 Source/Method/Case 身份冲突会触发；明确受影响 claim。MF-01 已经隔离，不重复触发。

<a id="trigger-change"></a>
## 13. CHANGE 触发

Owner、正式方法、业务前提或 DataBinding 发生实质变化时触发，只限制受影响工作。

<a id="route-same-work"></a>
## 14. 同工作续作正文

继续本任务。直接采用 R0004 管理已接收结果；不要重做 Case-01。完成 Case-02 成员选择增量检验和 I5 就绪判断，形成结果后提交管理。完整 I4 范围、证据边界和禁止事项仍有效。

<a id="route-accept"></a>
## 15. 管理接收正文

向 `chatgpt-project:细节叙事生成_金标/chat:BI01-R01-管理` 提交完整结果、证据、限制、I5 就绪表和双 Return。不得把执行自查当 G4/G5。

<a id="route-decide"></a>
## 16. 管理裁定正文

只在新消费冲突、Owner/正式方法变化、超授权投入或本段结果形成时进入。写清受影响 claim、可继续主体和需要的具体决定。

<a id="route-return-repair"></a>
## 17. 回交修复正文

只修确切的 Return 字段、引用或续作不一致。缺专业分析则继续原工作，不为过结构检查制造结论。

来源：daowei2026/observe-iterate@0c496004729d58ceb2033a14ba20e636b8979027:runs/BI-01-RESTART-01/01_当前任务.md::full

## 本轮原文与位置

本次原始要求：`daowei2026/observe-iterate@0c496004729d58ceb2033a14ba20e636b8979027:runs/BI-01-RESTART-01/01_当前任务.md::#route-same-work`
当前生效任务：`daowei2026/observe-iterate@0c496004729d58ceb2033a14ba20e636b8979027:runs/BI-01-RESTART-01/01_当前任务.md::full`
当前任务采用依据：`daowei2026/observe-iterate@0c496004729d58ceb2033a14ba20e636b8979027:runs/BI-01-RESTART-01/reviews/MANAGEMENT_GATE_DECISION_R0004.md::full`
上一轮实际采用的任务绑定：`daowei2026/observe-iterate@ae2ac32857628e6a8f03e6bc361a14be2d175df1:runs/BI-01-RESTART-01/bindings/QUESTION_WORK_BINDING_I4.json::full`
完整工作范围：`daowei2026/observe-iterate@0c496004729d58ceb2033a14ba20e636b8979027:runs/BI-01-RESTART-01/01_当前任务.md::#full-scope`
本次实际证据：`daowei2026/observe-iterate@c3fbaf2e5d200f79b49aa85d9a27f0b6bf36e0d5:runs/BI-01-RESTART-01/provenance/turns/R0004/FULL_RESPONSE.md::full`
本次实际证据：`daowei2026/observe-iterate@dc0872e58e193b0b84ff359b33cf78790ddcc6ff:runs/BI-01-RESTART-01/reviews/WORKMAP_READER_R0004.md::full`
本次实际证据：`daowei2026/observe-iterate@dc0872e58e193b0b84ff359b33cf78790ddcc6ff:runs/BI-01-RESTART-01/reviews/WORKMAP_INTAKE_CURRENT.json::full`

## 本次直接读取的上下文

- MODE_FULL：`daowei2026/observe-iterate@caccf69993b6f0c184fc89194476bcd542acb1e0:runs/BI-01-RESTART-01/OWNER_START.md::full`
  用途与边界：本次新run授权、旧I4不继承、连续真实业务推进要求
  本checkout已核位置；正文仍须接收者实际读取。 所给复用依据：{"commit": "34d90874ddc9617a4dfecec1f39cbedf54c23845", "path": "runs/BI-01-RESTART-01/artifacts/I4_R0003/REPORT.md", "repo": "daowei2026/observe-iterate", "selector": "#material-use"}；仍须同一上下文、未变且关键内容可恢复。

- MODE_FULL：`daowei2026/observe-iterate@75d42776a78cd4cbdf3b61bbf86ec93701d06b84:professional/source/00_AGENT_CHARTER_AND_STAGE_CONTRACT.md::full`
  用途与边界：完整总意图、I1-I6 Input/Output/Gate、角色权限
  本checkout已核位置；正文仍须接收者实际读取。 所给复用依据：{"commit": "34d90874ddc9617a4dfecec1f39cbedf54c23845", "path": "runs/BI-01-RESTART-01/artifacts/I4_R0003/REPORT.md", "repo": "daowei2026/observe-iterate", "selector": "#material-use"}；仍须同一上下文、未变且关键内容可恢复。

- BOUNDARY：`daowei2026/observe-iterate@75d42776a78cd4cbdf3b61bbf86ec93701d06b84:professional/source/01_I1_I3_PROFESSIONAL_CONTRACT.md::full`
  用途与边界：G3限定消费和局部返I2/I3边界
  本checkout已核位置；正文仍须接收者实际读取。 所给复用依据：{"commit": "34d90874ddc9617a4dfecec1f39cbedf54c23845", "path": "runs/BI-01-RESTART-01/artifacts/I4_R0003/REPORT.md", "repo": "daowei2026/observe-iterate", "selector": "#material-use"}；仍须同一上下文、未变且关键内容可恢复。

- MODE_FULL：`daowei2026/observe-iterate@75d42776a78cd4cbdf3b61bbf86ec93701d06b84:professional/source/02_I4_OBSERVATION_AND_CHALLENGE.md::full`
  用途与边界：I4事实、增量/无增量、挑战、G4标准
  本checkout已核位置；正文仍须接收者实际读取。 所给复用依据：{"commit": "34d90874ddc9617a4dfecec1f39cbedf54c23845", "path": "runs/BI-01-RESTART-01/artifacts/I4_R0003/REPORT.md", "repo": "daowei2026/observe-iterate", "selector": "#material-use"}；仍须同一上下文、未变且关键内容可恢复。

- BOUNDARY：`daowei2026/observe-iterate@75d42776a78cd4cbdf3b61bbf86ec93701d06b84:professional/source/03_STAGE_HANDOFF_AND_READINESS.md::full`
  用途与边界：G4到I5、阶段继续和定向补修边界
  本checkout已核位置；正文仍须接收者实际读取。 所给复用依据：{"commit": "34d90874ddc9617a4dfecec1f39cbedf54c23845", "path": "runs/BI-01-RESTART-01/artifacts/I4_R0003/REPORT.md", "repo": "daowei2026/observe-iterate", "selector": "#material-use"}；仍须同一上下文、未变且关键内容可恢复。

- BOUNDARY：`daowei2026/observe-iterate@75d42776a78cd4cbdf3b61bbf86ec93701d06b84:professional/source/04_PRO_WORKER_CODEX_HANDOFF.md::full`
  用途与边界：必要技术工单与Worker边界；当前没有签发Worker
  本checkout已核位置；正文仍须接收者实际读取。 所给复用依据：{"commit": "34d90874ddc9617a4dfecec1f39cbedf54c23845", "path": "runs/BI-01-RESTART-01/artifacts/I4_R0003/REPORT.md", "repo": "daowei2026/observe-iterate", "selector": "#material-use"}；仍须同一上下文、未变且关键内容可恢复。

- BOUNDARY：`daowei2026/observe-iterate@75d42776a78cd4cbdf3b61bbf86ec93701d06b84:professional/source/05_ROLE_GATE_AND_HANDOFF_CONTRACT.md::full`
  用途与边界：执行自查、管理Gate、Owner权限和阶段接收
  本checkout已核位置；正文仍须接收者实际读取。 所给复用依据：{"commit": "34d90874ddc9617a4dfecec1f39cbedf54c23845", "path": "runs/BI-01-RESTART-01/artifacts/I4_R0003/REPORT.md", "repo": "daowei2026/observe-iterate", "selector": "#material-use"}；仍须同一上下文、未变且关键内容可恢复。

- FOCUS_FULL：`daowei2026/observe-iterate@34d90874ddc9617a4dfecec1f39cbedf54c23845:runs/BI-01-RESTART-01/artifacts/I4_R0003/REPORT.md::full`
  用途与边界：已管理接收的Case-01事实、findings、限制和预声明选样规则
  本checkout已核位置；正文仍须接收者实际读取。 所给复用依据：{"commit": "34d90874ddc9617a4dfecec1f39cbedf54c23845", "path": "runs/BI-01-RESTART-01/artifacts/I4_R0003/REPORT.md", "repo": "daowei2026/observe-iterate", "selector": "#material-use"}；仍须同一上下文、未变且关键内容可恢复。

- FOCUS_FULL：`daowei2026/observe-iterate@0c496004729d58ceb2033a14ba20e636b8979027:runs/BI-01-RESTART-01/reviews/MANAGEMENT_GATE_DECISION_R0004.md::full`
  用途与边界：当前G3/G4接收、Case-02身份、已知处置和后继
  本checkout已核位置；正文仍须接收者实际读取。 本次不主张已读复用。

- FOCUS_FULL：`daowei2026/complex-systems-vocabulary@fe9656349c8f0aefeeef41c323bec81a688a2d70:docs/network-dynamic-ceps-factory/capital-management-purpose/discuss-materials/U2U3首轮业务观察实例上下文_20261010/01_首轮实例及子意图1至3上下文.md::full`
  用途与边界：Q-01、Case身份、计算链、方法和As-Of历史来源
  外仓准确定位；本checkout未读取，接收者按原工具取得正文。 所给复用依据：{"commit": "34d90874ddc9617a4dfecec1f39cbedf54c23845", "path": "runs/BI-01-RESTART-01/artifacts/I4_R0003/REPORT.md", "repo": "daowei2026/observe-iterate", "selector": "#material-use"}；仍须同一上下文、未变且关键内容可恢复。

- FOCUS_FULL：`daowei2026/complex-systems-vocabulary@fe9656349c8f0aefeeef41c323bec81a688a2d70:docs/network-dynamic-ceps-factory/capital-management-purpose/discuss-materials/U2U3首轮业务观察实例上下文_20261010/02_子意图4三类观察情形与挑战.md::full`
  用途与边界：四层比较、反向挑战、finding和阶段交界
  外仓准确定位；本checkout未读取，接收者按原工具取得正文。 所给复用依据：{"commit": "34d90874ddc9617a4dfecec1f39cbedf54c23845", "path": "runs/BI-01-RESTART-01/artifacts/I4_R0003/REPORT.md", "repo": "daowei2026/observe-iterate", "selector": "#material-use"}；仍须同一上下文、未变且关键内容可恢复。

- PROVENANCE_TRIGGER：`daowei2026/feature-refinement-implementation-agent-evolution@ed62cd716cd603f0bcc566368c62caec7cdba554:agent_evolution/pilot_cases/network-dynamic-ceps-factory-u2-u3/runs/u2-retrofit-20260907/artifacts/material_catchup/current_inputs/source_to_behavior/U2_SOURCE_OCCURRENCE_EPISODE_NODE_BEHAVIOR_LOCAL_CONTRACT_RETROFIT_0.1.0-candidate.1.md::full`
  用途与边界：C0/N actual-confirm、Episode、N基线和重复证据边界
  外仓准确定位；本checkout未读取，接收者按原工具取得正文。 所给复用依据：{"commit": "34d90874ddc9617a4dfecec1f39cbedf54c23845", "path": "runs/BI-01-RESTART-01/artifacts/I4_R0003/REPORT.md", "repo": "daowei2026/observe-iterate", "selector": "#material-use"}；仍须同一上下文、未变且关键内容可恢复。

- PROVENANCE_TRIGGER：`daowei2026/feature-refinement-implementation-agent-evolution@ed62cd716cd603f0bcc566368c62caec7cdba554:agent_evolution/pilot_cases/network-dynamic-ceps-factory-u2-u3/runs/u2-retrofit-20260907/artifacts/material_catchup/current_inputs/relation_to_cluster/U2_RELATION_FORMATION_QUALIFICATION_PHYSICALIZATION_LOCAL_CONTRACT_RETROFIT_0.1.0-candidate.1.md::full`
  用途与边界：Formation、Qualification、Validity、Separation、Commit和成员边界
  外仓准确定位；本checkout未读取，接收者按原工具取得正文。 所给复用依据：{"commit": "34d90874ddc9617a4dfecec1f39cbedf54c23845", "path": "runs/BI-01-RESTART-01/artifacts/I4_R0003/REPORT.md", "repo": "daowei2026/observe-iterate", "selector": "#material-use"}；仍须同一上下文、未变且关键内容可恢复。

- PROVENANCE_TRIGGER：`daowei2026/feature-refinement-implementation-agent-evolution@ed62cd716cd603f0bcc566368c62caec7cdba554:agent_evolution/pilot_cases/network-dynamic-ceps-factory-u2-u3/runs/u3-retrofit-20260907/artifacts/material_catchup/effective_mission_a/04_movement_current/02_U3_MA_LOCAL_CONTRACT_MOVEMENT_01.md::full`
  用途与边界：Movement objective facts、Working/Completed、恢复语义与no-backfill
  外仓准确定位；本checkout未读取，接收者按原工具取得正文。 所给复用依据：{"commit": "34d90874ddc9617a4dfecec1f39cbedf54c23845", "path": "runs/BI-01-RESTART-01/artifacts/I4_R0003/REPORT.md", "repo": "daowei2026/observe-iterate", "selector": "#material-use"}；仍须同一上下文、未变且关键内容可恢复。

- FOCUS_FULL；用途与边界：Case-02 C0/N/C1诊断事实与当前Reference/Shadow状态
  原始来源：`{"attachment_id": "file_0000000035c481fdbbfb82af5e57a96c", "filename": "steel_U2_U3_执行结果_20261010.zip", "selector": "full archive; Case-01 accepted results and Case-02 diagnostic members", "sha256": "7bebbee3fd7d425eb85116f33c5d0e01ae2163e6849818515fe3824a82b9a46c", "source_kind": "ATTACHMENT"}`
  原件由接收者实际取得；本工具未读取或验证原件。

- FOCUS_FULL；用途与边界：Case-02 actual/source/knowledge与共同范围路径
  原始来源：`{"attachment_id": "file_000000008c7481fd8604a79973ec5951", "filename": "rb_hc_i_mid贴近转折_zig_small_K线_20210101_20240229.zip", "selector": "full archive; current DataBinding hash and HC/RB/I paths", "sha256": "4fd1af4e7b34af6fc099e6289ffdd5d83125412fc16d2a9902af4fd9741b3987", "source_kind": "ATTACHMENT"}`
  原件由接收者实际取得；本工具未读取或验证原件。

读取Owner完整要求、生效完整任务和输入输出地图，不能用最新remaining替全部责任。按source_reads取得准确正文用于判断，已读未变且可恢复者复用；不递归扫无关历史，不用索引/hash/旧回执代正文。

旧包中已被Owner否定的多余任务，必须由原有权责任者从当前正文、任务、前置、接收和后继删除；只为其存在的辅助代码与检查交原实现者删除。禁止继续完善、改名或列为暂缓/未来优化。不能只在顶部写新原则却继续采用相反正文。真实业务方法、时间、身份、状态、正式输出与消费者保留，技术机制替换回正常平台。正确正文禁止任何压缩或摘要替换。历史提交和实际记录不倒改；历史可追溯不授后续派发。通用材料维护不自动取得用例任务写权。

当前执行材料由管理和有权任务责任者明确采用。推进者取得实际需要的正确正文，不能用管理概述替代业务细节；也不要求每轮重读全部历史和已撤完整任务。

发现新的实质冲突时，给出准确位置与受影响结论，按原责任处理。来源不足只限制真正依赖的判断，不用旧快照补造事实，也不冻结无关工作。

方法版本、业务合同版本、源码版本和运行数据分别保持准确，不随一次方法更新全部追 latest。

运行事实（来自现有记录）：
观察时间：2026-10-16T12:36:24.941Z
有效回交数：0

按既有协议交完整实质回答及ROLE_RETURN/QUESTION_WORK_RETURN，来源、未执行和资格如实保留，不新增控制表，不重抄协调者已存提示。完整任务未完成就保留完整责任及连续后继，局部交付不自设停点。要求GitHub提交时普通快进并fresh回读，最后commit message带turn complete及本轮invocation_id，无invocation时简要标明执行身份；不造空提交。

专业者回交实际实物、必要自检／执行结果、具体限制及完整未完，不代写管理接收、全局预算或主控派发。管理回交已完成的判断、实际处置和可执行后继，不以问题目录代替决定。

没有完整完成时，说明真实停止原因及已经明确的下一步；不得以自设局部目标完成作为结束解释。
