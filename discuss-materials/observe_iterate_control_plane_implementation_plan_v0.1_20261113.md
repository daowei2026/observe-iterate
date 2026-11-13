# Observe–Iterate 业务控制面落地计划（反馈审查修订候选 V0.2）

- 形成日期：2026-11-13
- 修订基线：`discuss-materials/observe_iterate_control_plane_implementation_plan_v0.1_20261113.md`（完整历史原文单独保留）
- 修订来源：新上传的《修改建议》（审查 V0.1 §1～7.2）及之后已明确的 GitHub 持久化、一次性落地、暂缓外部长程接线、统一 `advance` 入口的讨论。详见 §13 的逐项采纳记录。
- 文档性质：**待确认的实施计划，不是已批准的技术合同，也不是仓库已实现状态**
- 目标：在现有长程 Codex 主控—管理/执行 Pro—Worker—GitHub 协作方式之上，建设**一个共用业务控制核心**，组织「观察材料准备」与「合理性分析」两个可循环、可交接的业务 Workflow，使正常授权工作按 Gate 自动接续，异常定向恢复。
- 当前范围：仅纳入 `observe-iterate/main/discuss-materials/观察材料规划与准备Skill_候选V0.1_20261113/`、`observe-iterate/main/discuss-materials/reasonableness-analysis-skills-v0.1/` 与《业务控制面与 Skill 工程规范》；`observe-iterate` 其它历史目录**不视为当前 Agent 体系**。旧长程协议仅用于执行对接边界与兼容性核查。
- 实施边界：**本计划不授权修改现有 Skill、正式特征、参数、数据或长程主控协议**。只在设计确认后一次性落地本轮文件和控制程序，随后立即试跑；本轮不改外部长程主控代码。所有新增设计均需可追溯，涉及权限、Gate 权限与正式接收的未决事项不得由实现者自作决定。
- 持久化约束：本轮按 Owner 已表达的意图，**控制状态、交接、证据及运行记录都存放 GitHub**；运行代码可在受控 Codex/Actions 环境执行，本地临时文件不构成第二权威状态。GitHub 存储、受保护写入与真实可执行环境的资格尚须实测和授权。

## 1. 来源、继承与新增的识别规则

在一切管理合同和工程文件中使用三种来源标识：

- `S`：来自当前专业 Skill 的规则。引用原件的准确路径、章节、版本；专业语义不改写。若当前 Skill 的两条约束冲突，标记冲突而不自行裁决。
- `C`：来自上传的《业务控制面与 Skill 工程规范》（CP-SKILL-001 v0.1，工程评审稿）。该规范提出强制边界，但不是现有系统已实现的证明，也不是 Owner 自动授权。
- `N`：本轮新增业务控制面设计。保留提出原因、假设、替代选择、受影响的源规则、需要谁决定和实施成熟度。

正式规则只允许在一个受保护位置生效。说明文档、管理 Pro Prompt、Skill 只能**引用**生效规则，不得复制出三套相互独立的可执行状态与权限定义。

### 1.1 已有内容保持不变

1. 材料准备 Skill 第 0～7 步的专业方法：识别入口、还原业务骨架、材料取舍、处理方法、落地设计、真实取数、质量检查、交接。
2. 材料准备候选交付标签：`PLAN_READY / DATA_READY / PARTIAL_WITH_LIMITS / BLOCKED`；它们不是正式业务 `DomainState`。
3. 材料必要性：必需、有条件需要、可选建议、暂不准备；不强制所有候选观察方法和 CAEGraph 图层都运行。
4. 合理性分析四个 Skill：`business-expectation-derivation`、`business-evidence-comparison`、`business-discrepancy-diagnosis`、`feature-instance-calibration`；渐进预期、事实准备轨道、正式对照前冻结、新预期形成新版本、诊断后有条件标定与复验、首次实例化可直接标定。
5. 具体长程运行分工：Owner 授权；Codex 主控只处理发送、工单来源、去重、监控、合法回交和接续；专业 Pro 决定专业下一步与签 Worker Order；Worker 按授权实际执行。`R`、`W` 与业务 Stage/WorkItem 不混用。

### 1.2 新增内容分三组

- `A`：一个管理 Pro 的**共用管理职责**＋两套不同的**专业 Workflow 管理合同**。
- `B`：一个**共用受保护控制程序**：权威状态、工作项、调度、动作授权、Gate、接收、恢复、审计；不为两条 Workflow 各建一套程序。
- `C（衔接）`：父业务任务、材料准备与合理性分析之间的正式材料接收、探索性材料使用、补证请求、定向返工和恢复原分析轮次。

## 2. 总体架构与权威分工

```text
Owner（定义业务目的、边界、预算、必要取舍）
  ↓
ParentBusinessTask（一次观察—分析目标；不等于一次长程 Run）
  ↓
共用业务控制核心 B（唯一权威业务状态、合法后继、权限、Gate、正式提交、恢复）
  ├── MaterialPreparation Workflow（S0～S5；G-PLAN/G-RUN/G-MATERIAL）
  ├── Reasonableness Workflow（R0～R5；允许循环、快速路径和条件分支）
  └── Cross-Workflow Handoff（MaterialPackage / AdditionalEvidenceRequest）
            ↕ 定向专业判断/复核
       管理 Pro（A，共用专业管理职责；必要时另设独立复核）
            ↓ 已获授权的业务工作动作
现有 Codex 长程主控（跨端物理派发与回交，不重做业务 Gate）
            ↓
执行 Pro（按 Skill 执行和正式签 Worker Order）
            ↓
Worker Codex / 数据与 CAEGraph 工具
            ↓ GitHub 精确提交引用 + 真实执行回执
长程主控核实运输事实 → 业务控制核心登记候选/验证/Gate/接续
```

**唯一权威**：受信任控制程序和经受保护的 GitHub 正式状态分支保存业务状态；管理 Pro 可以作专业提议、在 Owner 授权范围内复核，但不能凭聊天、角色自填或普通 GitHub 文件直接改正式状态。GitHub 用于跨角色实物、provenance 和受保护的权威状态分支；普通提交文件不自动构成正式业务接受。

**角色可合并，权力不可假合并**：同一个 Pro 可以承担管理和专业执行，但有独立性要求的正式接受必须用真实独立复核执行或经 Owner 授权的有权主体；不能通过同一聊天里自称“复核角色”绕过。

**强制力分级**：未具备真实身份验证、隔离的状态写入口与受保护验证器时，只能开展草稿/影子/建议模式；不得声称自动正式采纳。本轮按 GitHub-only 设计受保护写入、版本比较与提交回执；只有真实隔离 Worker/Pro 写权、验证器与接受策略时才可称强制型控制面。

## 3. A：管理 Pro 合同

### 3.1 共用职责与专业决定生效协议（S + C + N）

管理 Pro 对当前授权的**整体业务目标**负责，掌握目标、当前正式状态、专业工作安排、证据、业务未决项和完成边界；它读取权威业务状态，不在聊天中维护第二份「最新状态」。可以组织或修订专业计划、提交专业 Gate 复核意见、判断可复用材料以及定向返修；不能以自己的口述直接变更权威状态或扩充授权。

管理 Pro 的回交类型仍采用 V0.1 四类：`ProfessionalTaskPlan`、`StageAssessment`、`ManagementDecisionProposal`、`ProfessionalChangeProposal`。**四类是按需提交的内容类型，不是每轮必须独立编写四份文件。**

**N-新增：专业决定到可执行状态的转换。** 有权专业判断必须归结为受控、可核的结构化结果，程序不通过自然语言重新推断业务后继：

| 决定类型 | 必须给出的内容 | 控制程序动作 | 无足够内容时 |
|---|---|---|---|
| `PROPOSE_WORK_DELTA` | 增删/修改的具名工作，必要性、输入、输出、责任角色、依赖条件、预算和分支 | 验证计划修订并提交新计划版本；受影响工作项待重验 | 返回 `NEEDS_SPECIFICATION`，要求原 Pro 补具体化，不自行翻译自然语言 |
| `PROPOSE_GATE_RESULT` | 具体 Gate、候选摘要、所据事实、结论与适用范围 | 核验复核身份和权限，结合硬检查形成正式 Gate 决定 | 进入具名复核/补证，不能自称通过 |
| `PROPOSE_CHANGE` | 旧/新范围、原因、影响、预算、所需授权 | 保留变更申请；有权批准后才更新任务/计划 | `WAIT_OWNER` 或原授权复核者 |
| `REQUEST_FACT_CHECK` | 事实缺项、具体位置、预期检查结果与最小动作 | 在现有计划/授权内登记局部续作或适当调用 | 事实目标不清则补具体问题 |
| `NO_CHANGE` / `COMPLETE_ASSESSMENT` | 当前专业工作已无新增行动、已回答的问题和未决项 | 按本轮完成定义验证并决定继续/接收/结束 | 不把「值得继续研究」无边界地加入必做范围 |

例如管理 Pro 判断「先核对 BP-09 的 actual/confirm，若未错位再调查参数」时，应输出一个核对工作项，以及 `TIME_MISMATCH_FOUND`／`TIME_BASIS_VERIFIED` 两条有据可判的后继条件；控制程序只验证、登记和调度，不再让第二个模型猜该做什么。

**N-新增：管理 Pro 的调用边界。** 控制面可以安排任务；管理 Pro 在已有计划可直接继续时不应每轮再决定。确实出现未覆盖的新业务问题时才提交 `ProfessionalChangeProposal`。同一未决问题与同一候选摘要未产生新事实前不得反复调用同一管理判断。

### 3.2 观察材料准备管理合同 A1：阶段不是调用单位（S + N）

保留 V0.1 的 **S0～S5 业务阶段**，仅作为业务进展与 Gate 的管理视图，不新增六个独立专业 Skill，也不要求每次调用完整 Skill 从头重做。现有 [观察材料准备 Skill] 的第 0～7 步仍是唯一专业方法来源。

| 阶段 | 现有 Skill 对应 | 专业工作和候选产物 | 调用边界与 Gate |
|---|---|---|---|
| S0 接管调查 | 第 0、部分第 1 步；任务单 A | 确认观察目的、源/图/版本线索、缺口，`AssetAndBindingAssessment` | 允许调查未知事实；可沿用已证实的历史调查；关键资产未定位时不得虚构版本 |
| S1 材料规划 | 第 1～4 步；任务单 B/C | `MaterialPlan`：实质阶段、必需/条件/建议材料、处理与取数路径 | `G-PLAN` 管规划覆盖和可执行性；允许已授权的**小范围接口探查**，但不得偷偷启动需 G-RUN 的完整重算 |
| S2 执行准备 | 第 4～5 步及 CAEGraph 说明 | `ExecutionPlan`、版本、运行入口、成本/资源前置检查 | `G-RUN` **作用于具体高成本动作**，不是所有调查的统一人工门禁 |
| S3 实际取数 | 第 5 步；任务单 D | 可分批产生多项材料、执行证据、不可得说明 | 只对被授权工作运行；可用中间产物按依赖就绪资格继续加工，未必等待整包接受 |
| S4 材料核验 | 第 6 步及 CAEGraph 最小验收 | 质量核对、部分/不可得/适用范围与 `MaterialReview` | `G-MATERIAL` 评价材料真实和可交付资格，缺口精确影响对应问题 |
| S5 交付接收 | 第 7 步；任务单 F | 受控接收的 `AcceptedObservationMaterialPackage`；或明确未完与阻断 | 按原任务完成条件结束；部分接受本身不降级必需范围 |

**N-新增：一次专业调用的固定封面 `ProfessionalCallSpec`**，包含 `business_task_id, stage_view, call_id, work_item_ids, purpose, already_accepted_inputs, permitted_local_actions, forbidden_actions, expected_outputs, stop_boundary, escalation_rule, skill_ref`。该调用可覆盖多个 Skill 步骤、多个材料项，也可只用于一轮补查，不得仅用「执行 S1」代替完整工作边界。

**N-新增：三个不能互相替代的单位。**

- `MaterialRequirement`：最终需要交付什么（例如 BP-07、BP-09、K 线和图层身份映射）。源自现有任务单，不能默认每项单独执行。
- `WorkItem`：某项可安排的专业工作，如运行已有完整 CAEGraph 并取得全部需要的图层与源表；可产出多个材料，亦可组合多次执行。
- `ExecutionAction`：一次实际工具/模型/脚本调用的授权与回执。一个 WorkItem 可有多个 Action，也可一次运行满足多个 WorkItem。

映射是多对多，显式记录 `produces`、`consumes`、`execution_group_key` 和可复用产物，**不按材料项数量机械生成 WorkItem**。若已有完整 CAEGraph 同一次构图覆盖四项交付，程序不得无依据派四次完整构图。

每条材料要求继续沿用 `必需 / 有条件需要 / 可选建议 / 暂不准备`；条件材料只在真实触发条件满足后激活。专业方法怎样执行仍由 Skill 决定，控制面只管可执行范围、成果依赖和正式接收。

### 3.3 合理性分析管理合同 A2：专业调用模式与循环身份（S + N）

仍保留 V0.1 的 **R0～R5 业务视图**和现有四个 Skill；不按编号固定顺序派发，不强制把每个 R 作为一次独立 Pro 调用。

| 阶段视图 | 唯一专业方法来源 | 合法调用模式（N） | 有效成果/门禁 |
|---|---|---|---|
| R0 分析接管 | README 的事实/业务双轨 | `FACT_PREP`、`MINIMAL_INTAKE` | 目的、来源、可用材料和最低分析范围明确；可在预期未冻结时查事实 |
| R1 预期推导 | `business-expectation-derivation` | `WORKING_EXPECTATION`、`FREEZE_REQUEST` | 有来源、可证伪的最小预期；正式对照前独立冻结版本 |
| R2 证据对照 | `business-evidence-comparison` | `EXPLORE`、`FORMAL_COMPARE`、`TARGETED_RECHECK`、`INSTANCE_REVALIDATION` | 探索不冒充正式反证；正式对照锁定预期与证据版本 |
| R3 偏差诊断 | `business-discrepancy-diagnosis` | `DIAGNOSE`、`LOCAL_FACT_CHECK`、`PARAMETER_REPAIRABILITY` | 追最早分歧；结论可为已定位、尚存替代解释或不可由参数修复 |
| R4 实例标定（条件） | `feature-instance-calibration` | `FEASIBILITY_SOLVE`、`BOUNDED_TRIAL`、`REQUEST_INSTANCE_COMPARISON` | 试验授权、可行域与完整实例新旧对照；首次实例化可合法直接进入 |
| R5 结果接收 | 汇集四 Skill 正式成果 | `ANALYSIS_DELIVERY` | 分开接收分析质量、业务支持/反证/未决和后继，不要求最终特征必然合理 |

每次调用除 `ProfessionalCallSpec` 外必须携带 `analysis_round_id, question_id, expectation_id/version/digest, data/code/parameter/material_binding, proposal_id, call_mode` 中与当前目的相关的字段；若尚无冻结预期，明确 `exploratory`，不得填造冻结版本。

**N-新增：同一次完整实例复验只执行一次。** 当前标定 Skill 第 4 步已经要求调用证据对照 Skill；控制面应创建/复用一个有唯一 `comparison_work_item_id` 的 `INSTANCE_REVALIDATION` 工作。R4 对该工作形成等待依赖，R2 的专业能力产出被 R4 `CalibrationResult` 和整体分析共同引用，禁止 R4 完成后机械重复派发另一轮同目的 R2。必须在结果回来后再验收 R4 的完整实例合理性判断；有现成同版本、同窗口、同目的的合格对照则复用。对上游对象可能重分段的参数，绑定**原始业务窗口、旧/新实例身份与参数**，不能只依赖旧事件 ID。

R2 发现新场景→R1 新候选预期；R3 缺证→当前授权内局部查证或跨工作流补证；R3 可调→受控 R4；R4 发现旧定位错误→R3；首次实例化可直接 R4。每条返回都绑定原 `question_id + analysis_round_id + expectation_version`，不是只按「当前 R2」定位。

### 3.4 Gate 的验收对象必须分清（S + C + N）

本版保留 G-PLAN/G-RUN/G-MATERIAL/G-EXPECTATION-FREEZE/G-COMPARISON/G-DIAGNOSIS/G-CALIBRATION/G-ANALYSIS-DELIVERY，但**不默认每个 Gate 都是独立 Pro 调用**；相同已验证证据可在同一版本与适用范围内复用。Gate 应明确区分下列三种判定：

1. `WorkQualityGate`：本次专业工作和证据是否达到合同要求？例如真实对照得出 `COUNTERS` 或诊断证明 `PROVEN_NOT_ADJUSTABLE`，仍可属于 **合格专业工作**。
2. `BusinessFinding`：被分析特征到底支持、反证、不适用、歧义、未决或不可调？这些是**领域结论**，不等于 Gate PASS/FAIL。
3. `NextActionEligibility`：在当前授权和事实下，能否启动新实验、补证、实现修正或下一轮判断？不因工作通过就自动授权修改生产参数。

| Gate | 验收对象（非“必须业务合理”） | 专业与硬检查重点 | 后继 |
|---|---|---|---|
| G-PLAN | 本轮材料规划的覆盖和可执行性 | Skill 第 1～4 步、必要性和来源 | 合格→取数准备；不充分→返修 |
| G-RUN | 本次成本/副作用动作资格 | 版本、依赖、授权和预算；小探查按已授权能力直接做 | 合法动作放行，超界等待授权 |
| G-MATERIAL | 真正取得材料及适用范围 | Skill 第 5～7 步，数据阶段、时间、身份、有效空/缺失 | 接收完整/限定材料，或记录不可得 |
| G-EXPECTATION-FREEZE | 冻结命题可对照性 | 预期来源、反例、适用条件、已看探索证据和版本 | 锁定本轮版本，而不是冻结所有未来想法 |
| G-COMPARISON | 对照执行和证据是否合格 | 真实场景、冻结版本、支持/反证/缺失的对应关系 | `COUNTERS` 可以是通过 Gate 的分析结果 |
| G-DIAGNOSIS | 诊断是否沿证据追因、给出有据后继 | 已排除竞争解释、尚存未知、必要实验 | 已定位/不可调/有界未决都可以合格交付 |
| G-CALIBRATION | 标定准入、试验动作、完整实例判定的各自资格 | 有效自由度、预算、原始窗口、新旧实例和复验 | `PROVEN_NOT_ADJUSTABLE` 可被接受，不强迫产生候选实例 |
| G-ANALYSIS-DELIVERY | 本轮约定问题是否合格交付 | 支持/反证/未决与适用范围、完整性和后继 | 接受分析成果不代表生产特征已修好 |

规范 CP-013 的 `FAIL / UNKNOWN / NOT_RUN` 不可当作**必需硬检查**通过，但已经完成检查后形成 `MISSING/AMBIGUOUS/PENDING` 等**业务结果**，在本轮已批准完成条件允许时仍可被如实接收。`AUTO/REVIEW/FORBIDDEN` 和各 Gate 接受权仍为待授权决定，不由本计划给默认权。

## 4. C：观察材料准备与合理性分析的衔接（新增 N）

### 4.1 父子任务、问题及分析轮次的身份（S + N）

- `ParentBusinessTask`：一次观察—分析目的及本轮必须回答的问题、允许的分析深度、退出条件；不等于一个长程 Run。
- `MaterialPreparationTask`：准备、验收指定材料；可包含补证工作，不重写旧版本。
- `ReasonablenessTask / AnalysisRound`：某个问题针对某版预期、数据、参数形成一轮判断；保留当前轮和旧轮的关联。
- `AdditionalEvidenceRequest`：关联具体原问题/轮次的事实缺口和原回交点。
- `CalibrationRun`：有界专业工作，不等于正式生产修改任务。

`production_run_id`、`business_task_id`、`question_id`、`analysis_round_id`、`expectation_id/version`、`material_package_id/version`、`work_item_id`、`proposal_id/attempt` 与长程 R/W 分开。每次计划、Gate、补证、标定比较都绑定当时读取的相关摘要及版本（不适用的字段可为空而不得伪造）。补证迟到时只能先回到原 `question_id + analysis_round_id + request_id`，不能自动附到新的 v2 对照；如 v2 也需要此材料，单独核验其适用范围和依赖。

**N-新增：父任务按业务问题收束。** 任务创建时须区分本轮目标是「完成材料准备」「对指定预期作合理性判断」「定位偏差」还是「取得候选实例」，记 `required_questions`、`authorized_depth`、`completion_evidence`、`acceptable_unresolved_conditions`、`future_work_boundary`。发现有价值的新问题，只登记 `FutureQuestionProposal`；未获授权不自动升为本轮必做。反证本身可能是合格终点；不能以「必须将特征修到合理」替代原任务定义。

### 4.2 中间就绪、探索使用与正式接收（S + C + N）

保留 V0.1 的**探索用途**与**正式对照用途**两种业务资格，同时新增工作依赖所需的中间就绪等级，解决循环等待：

| 就绪等级 | 允许的用途 | 不能宣称 |
|---|---|---|
| `PRODUCED` | 文件/对象实际产出，能够按源位置查询；仅供后续最小核查 | 不能证明质量或直接正式交付 |
| `CHECKED_FOR_PROCESSING` | 来源、身份、版本、关键字段及当前加工需要的检查已通过；可以作为同一受控工作链的上游输入 | 不等于整个材料包 G-MATERIAL 已接受 |
| `EXPLORABLE` | 有明确来源、风险和限制的少量真实样本，可形成 `WORKING` 预期或定位问题 | 不得作正式支持/反证结论 |
| `ACCEPTED_FOR_SCOPE` | 已获得受保护接收，声明对象/窗口/用途/版本及证据资格 | 不自动保证对任意新预期均适用 |

等级不是新增的全局 RunState，也不是所有工作必须线性经过四道 Gate。每条工作依赖显式说明 `required_readiness` 和 `required_scope`。例如 `源表导出 A→视图加工 B→整体核验 C→G-MATERIAL`，B 只要求 A 的 `CHECKED_FOR_PROCESSING`，不等待整体 G-MATERIAL；正式交给分析阶段则需要限定范围接收或专门的正式证据准入检查。这样内部加工不会因等待未来整包验收而死锁。

已接受部分材料若足以支撑某个**不依赖其余材料**的分析问题，可以按限定范围启动；任务整体完成仍按最初必要范围判断，不能为推进而擅自降级。

### 4.3 `AcceptedObservationMaterialPackage`（S + N）

沿用任务单 D/F 与 CAEGraph manifest：`package_id, material_task_id, parent_business_task_id, purpose_id, material_plan_version, accepted_artifact_refs/digests, code/data/parameter/skill bindings, object/time/window/data_stage, data_quality, answerable_questions, limitations, unresolved_questions, acceptance_decision_ref, commit_receipt_ref`。额外提供 `question_scope`、每项材料的 `readiness` 和已接受用途，确保同一包可供后继局部分析使用，但不能自动得到任何新预期的业务适用资格。

材料计划中的 `MaterialRequirement` 与实际执行 `WorkItem/ExecutionAction` 分离，多对多的 `produced_by / depends_on` 引用保持可追踪，不为每份输出重复构图。

### 4.4 `AdditionalEvidenceRequest`：局部查证和跨 Workflow 补证不能混同（S + N）

先判断：

- **当前 Skill 局部续作**：查字段、源码、已有中间结果、少量已授权对照，不更换正式事实基线、不需要专门交付，仍在本 WorkItem 内继续；留证据即可，不走完整 G-PLAN/G-RUN/G-MATERIAL。
- **跨 Workflow 补证**：需要另一专业能力、另取材料/trace、实质性数据基线或计算成本变更、或需要正式独立交付；由原分析问题提出受控请求，由材料准备侧处理并原路返回。

`AdditionalEvidenceRequest` 维持 V0.1 字段，并新增 `question_id, originating_analysis_round_id, expectation_version/digest, material_readiness_required, request_fingerprint, return_to, requested_completion_definition`。请求 ID、业务目的、场景/字段、代码/数据/参数版本及未决原因相同，不得无依据反复新建同一请求。

**N-新增：完整返回结果**（`EvidenceRequestOutcome` 作为请求的结案记录，非伪造数据）：

| 结果 | 材料侧交付 | 分析侧合法后继 |
|---|---|---|
| `OBTAINED` | 已核验证据及适用范围 | 解除原问题对应等待，复验受影响对照/诊断 |
| `PARTIAL` | 部分证据、真实限制、剩余缺口 | 判断哪些原问题可以继续、哪些仍未决，允许有界局部继续 |
| `PROVEN_UNAVAILABLE` | 已调查且不可可靠取得的证据与理由 | 接受「当前条件不可得」事实，考虑替代证据、未决交付或新授权；不得伪装证据齐全 |
| `NOT_APPLICABLE` | 证据请求的对象/字段/时间条件不成立的事实 | 返回请求专业方修订需求，不重复无效取数 |
| `CANCELLED / SUPERSEDED` | 撤销或后继版本依据 | 关闭对应等待；迟到回交保留历史但不得解锁新轮次 |

所有返回都先匹配**原请求、原问题、原分析轮次和原预期版本**；若新轮也需要数据，由独立用途验证决定复用，而不是自动迁移。一次补证出结果后，无论成功、部分还是不可得，都必须产生可验证的关闭/续作决定，不能永远卡在 `WAITING_EVIDENCE`。

控制过程：发现需要补证→先检查同版本可复用材料→选择合法局部续作或受控材料子任务→记录请求和授权→派发实际调查/取数→分别验收「证据」或「不可得事实」→绑定原轮次→决定定向复验、受限交付、重新申请授权或关闭。不得把材料调查失败自动理解为可无限重算。

### 4.5 上游变更与受影响范围（C + N）

记录完整 `read_set`：源代码、数据、时间口径、参数、预期、材料包、候选和已验证摘要。若发生修订，旧产物保留；沿已登记的 `consumes/produces` 和适用范围判断哪些下游结果须重验。**补充独立证据不自动推翻所有既有结果；关键上游基线改变不允许仅改版本号而沿用旧结论。**

复验目标要保留 `question_id + analysis_round_id + frozen_expectation_ref + original_business_window + old/new_parameter_instance`。对校准造成的对象分段变化，回到固定原始业务窗口进行新旧比较，不用已变更的局部对象 ID 作为唯一对照锚点。

## 5. B：共用业务控制程序设计

### 5.1 状态维度及本轮问题完成标准（C + N）

- `DomainState`：已接收材料、冻结预期、分析结论、当前受保护业务版本；只有正式提交更新。
- `RunState`：任务/阶段 `NEW/READY/RUNNING/SUBMITTED/VALIDATING/ACCEPTED/REPAIR_REQUIRED/WAITING_REVIEW/REJECTED` 等执行过程状态；不得将流程状态冒充领域结论。
- `WorkItemState`：`PLANNED/READY/IN_FLIGHT/SUBMITTED/VALIDATING/ACCEPTED/REPAIR_REQUIRED/BLOCKED/SUPERSEDED` 等；实质上另记局部 `readiness`，不是必须等最终阶段 ACCEPTED 才允许所有下游加工。
- `ActionState`：`REQUESTED/AUTHORIZED/DISPATCHED/CONFIRMED/FAILED/EFFECT_UNKNOWN`；长程实际消息执行仍来自已核实回执。

每次阶段或任务完成检查还需要本轮的 `QuestionCompletionRecord`：`question_id, required_deliverable, authorized_depth, result_type (SUPPORT/COUNTER/LOCALIZED/UNRESOLVED/NOT_APPLICABLE等领域事实), evidence_refs, missing_required_checks, still_required_work, optional_future_questions, completion_eligible`。`completion_eligible` 不能由结果正负决定，只根据原任务完成合同和必要验证决定。

**任务终止不得依赖所有子任务都成功或每次发现的新问题都解决。** 若分析结果可信但找到了明确反证或不可调结论，该业务问题可被合格交付；未决能否收束取决于本轮预先允许的有界未决规则。不允许以「研究还有价值」自动扩充本轮必做范围。

### 5.2 共用与领域对象及其消费者（C + N）

保留 V0.1 的通用：`TaskContract/WorkPlanProposal/ResultProposal/ArtifactRef/EvidenceRef/ExecutionReceipt/ValidationReport/ReviewRecord/DecisionRecord/CommitReceipt/ActionRequest/ActionReceipt/Blocker/AuditEvent/SourceDependency`；另增显式：`ProfessionalCallSpec`、`ProfessionalDecisionEffect`、`QuestionCompletionRecord`、`EvidenceRequestOutcome`、`ComparisonWorkRef`，并将 `MaterialRequirement`、`WorkItem`、`ExecutionAction` 分开。

业务原产物仍由现有 Skill 定义：`MaterialPlan/MaterialItemResult/AcceptedObservationMaterialPackage/FrozenExpectationSet/EvidenceComparisonPackage/DiagnosisReport/CalibrationResult/AdditionalEvidenceRequest`。新增统一 Envelope 只封装 `task/round/question/source/version/digest/role/receipt` 等控制信息，不再次定义专业内容。

**文件／配置存在的必要条件：必须有真实运行消费者。** 新增或保留任何受保护配置、合同或管理材料，应注明 `consumed_by_operation`、`enforced_at`、`change_of_behavior`、`verification_case`。仅有一条「检查合理性」但无真实检查器/复核任务的 Gate 文本，不计作可运行能力。

### 5.3 控制程序接口与统一驱动入口（C + N）

对长程主控**只暴露一个固定驱动入口**：`advance(task_ref, event_ref, idempotency_key)`（CLI 可为 `oi-control advance`）。触发条件是新业务 GO、真实 Pro Return 已核验、Worker Return 已核验、派发/回交回执、取消/超时或恢复等**固定运输事件**；主控不判断应调用哪个内部程序。控制程序在一次调用内部处理事件去重、关联工作、必要验证、Gate 资格、正式提交、依赖和调度，输出**一个或若干已经准备好的、有权的外部动作**，或具名 `WAIT/RECONCILE/REQUEST_OWNER/COMPLETE`。无新事件及无可推进工作时必须幂等返回等待，不能凭空生成新工作。

内部接口仍保留、但**不要求主控调用其每一个**：

| 内部接口 | 输入与前提 | 输出/真实职责 |
|---|---|---|
| `create_or_resume_task` | 经核实 GO、task/purpose/授权/Skill 版本 | 建/恢复正式任务；未知事实可保留待调查 |
| `read_business_state` | task/id 和有权调用方 | 读取权威状态及范围内计划/轮次/材料/在途动作 |
| `submit_work_plan` | 专业计划或 `ProfessionalDecisionEffect` 提案 | 校验后进入计划待接受；不由程序猜新业务意义 |
| `submit_stage_result` | 绑定 question/round/work/call/attempt 的结果 | 仅保存候选；同摘要已失败的验证不能被无限重跑 |
| `record_verified_execution_result` | 与真实 R/W、Action 关联的回交和工具证据 | 登记实际事实；消息运输成功不等于数据合格 |
| `validate_stage_result` | 候选摘要、权威配置和验证器版本 | 按需生成 PASS/FAIL/UNKNOWN/NOT_RUN 的独立验证报告 |
| `record_gate_decision` | 有权复核者、绑定候选/版本/范围 | 登记有权专业决定；不相信自填角色 |
| `commit_stage_transition` | Gate、read_set、版本、幂等键 | 原子接收状态、Decision/Receipt/Audit；冲突拒绝而非覆盖 |
| `get_next_business_action` | 已接受计划、work/readiness、授权、阻塞和在途记录 | 确定性筛选可行动作；纯查询不得直接发消息 |
| `claim_and_dispatch_action` | 候选合法动作、预计版本和资源占用 | 原子登记 outbox/唯一动作 ID；由长程主控实际发送 |
| `submit_additional_evidence_request` | 原问题/轮次/预期/数据范围与请求 | 去重、复用、局部续作或受控跨 Workflow 子工作 |
| `register_material_handoff` | 已接收材料及用途资格 | 绑定分析消费者和限制，不替代目的适用性判断 |
| `freeze_expectation` | 候选预期、授权和冻结复核 | 产生不可变版本、摘要和冻结回执 |
| `request_action/reconcile_action/cancel_run` | 实际动作、回执或撤销授权 | 未知效果先对账；取消不抹掉在途后果 |

**N-新增：`ProfessionalDecisionEffect` 机器合同。** `decision_kind` 必须属于 §3.1 已列的类型；对于 `PROPOSE_WORK_DELTA`，具名 `work_delta.create/update/supersede` 要含 `work_id, purpose, professional_owner, input_refs, expected_outputs, dependencies + required_readiness, condition, authorized_scope, cost_class, completion_predicate`；分支后继由已接受条件驱动。只有经有权同意并落入正式计划的动作才进入 Scheduler。自由文本仅作理由，不能替代 `work_delta`。

**对长程主控输出最小合同**：`business_action_id, task_id, question_id/round_id(如适用), target_role, assignment_ref(完整原件), expected_return, allowed_scope, idempotency_key`；其物理发送/工单协议仍按旧长程规则执行，本轮不改旧代码。结果回交后通知 `advance` 即可。

### 5.4 调度不能只用任务级 `if/elif` 优先级（N 修订）

V0.1 的十条顺序**仅保留作为说明性检查清单，不作为全局调度算法**。本版建议两步：

**第 1 步：逐个 `question_id / work_item / action` 判断资格。** 每个候选动作明确：`trigger_fact, consumed_pending_item, produced_fact, dependency_readiness, scope, blocking_refs, budget/authority, prior_attempt, retry_on_new_fact, idempotency_key`。只被阻断的依赖路径不得封锁其他独立问题；同一候选摘要验证 FAIL 后没有新摘要/新事实，不可再安排相同验证。`EFFECT_UNKNOWN` 仅阻断可能重复同一外部效果的动作路径，其他独立工作可以继续。

**第 2 步：在合格动作集合中确定性排序**（优先保证正式状态必要维护与已接收 Gate 提交，再按已经批准的计划依赖、明确业务优先级和资源预算选择工作；同级稳定排序如 `work_id`）。不得为实现“优先级”临时发明业务价值排序。可授权多个独立动作但需检查资源独占和在途占用；首版即使单线程也不得造成跨问题饥饿。

```
for each pending_business_question:
  enumerate action candidates from accepted WorkPlan and valid events
  check exact identity, dependency readiness, event freshness and blocking scope
  reject unauthorized/over_budget/duplicate/unchanged_failed_proposals
eligible = union of all scoped legal actions
if eligible: choose deterministically; claim action(s) in authoritative storage
else: return named WAIT / REVIEW / OWNER / COMPLETE with unblock condition
```

`CALL_PRO` 只有当计划缺失新专业判断、相关输入已有新事实且存在具体期望回交时才合法；管理 Pro 已提出的补查若尚未执行，应先激活已批准补查而非再问 Pro。一项专业意见只有产生了 `work_delta / gate_decision / blocker / owner_request / completion` 等**可消费状态变化**才算驱动进度，不以写了新报告判定进展。

调度每一轮必须有进展测度：新证据、排除一个竞争解释、工作项验证完成、合法 Gate 转移、消耗一个阻断或发现明确不可得，均可能是实质进展；语义同义复述不是。正常无新事实时返回稳定的 WAIT，不能原地循环调用模型。

### 5.5 Gate、正式提交与权限（C + N）

每个 Gate 的受保护合同必须有 `gate_subject (WORK_QUALITY/BUSINESS_FINDING/NEXT_ACTION_ELIGIBILITY), entry_conditions, hard_checks, semantic_review_policy, authority, accepted_scope, failure_route, cost_boundary`。硬检查的 `UNKNOWN/NOT_RUN` 不得等价 PASS；业务结论 `COUNTERS/PROVEN_NOT_ADJUSTABLE/AMBIGUOUS` 与验证结果分别存储。

创建者与正式接受者在权限上分离；管理 Pro 的 Gate 权限来自真实 Owner 委托，不由同一聊天自称两种角色取得；需要独立复核时使用受控的另一调用。`SCOPED_ACCEPT` 可以建议表达为规范基础决定 `ACCEPT` 加不可变 `accepted_scope/limitations`，**是否允许整项任务结束仍须单独判断**。

状态、正式决定、审计、可查询 CommitReceipt 必须同一受保护原子提交范围；验证后修改产物、计划、数据版本必须重新检查受影响的依赖。同幂等键相同规范载荷返回同一结果，不同载荷冲突；不把 GitHub 普通候选 Markdown 当授权或接收。

### 5.6 恢复、失败和审计（C + N）

保留每个 `question/stage/work/attempt/action` 的版本、前置依赖、阻断范围、责任方、解除条件、重试条件、剩余预算和 `read_set`。崩溃/超时/迟到回交按动作 ID 对账；`EFFECT_UNKNOWN` 先查真实结果，不盲目重算；已证实的材料、失败调查和 `PROVEN_UNAVAILABLE` 不因下次继续而无痕覆盖。

`NO_PROGRESS` 依据新可验证事实和具体问题的未决集合变化，而不是报告篇数或 token 数。同一补证请求在无新事实时不得再次派发；必要条件不再满足或旧轮已被替代时关闭等待并隔离迟到回交。审计至少能回答「为什么触发该调用、为何阻断/放行、谁批准、哪些文件版本被采纳、后续回到了哪个问题/分析轮次」。

## 6. 与既有长程主控的接口边界（只固定业务协议，本次不改外部长程代码）

本轮只定义 `advance(task_ref,event_ref,idempotency_key)` 与外部事件/动作合同，**不实现 `cgpterm` 或 `feature-production-agent` 的调用改造，也不重建 R/W 工单运输**。当 Owner GO、已核验 Pro Return、已核验 Worker Return、动作回执、恢复/超时/取消等固定事件出现时，由未来长程主控按统一规则通知 `advance`，无需判断调用 Scheduler 还是 Gate/Commit；控制面内部决定并输出明确 `SEND_PRO_ASSIGNMENT / ALLOW_WORKER_DISPATCH / REQUEST_OWNER / WAIT / RECONCILE / COMPLETE`。

业务动作引用完整任务原件 `assignment_ref`，不得只返回「下步做 BP-09」让主控重新编业务 Prompt。只有 Pro 按原长程授权签 Worker Order；主控核实实物和收件端后发送；Worker Return 先回原 Pro 作专业消费，运输完成不等于业务 Gate 通过。

**本次实现范围的限制**：控制面代码可用模拟已验证回交和已存在 GitHub 实物做完整业务调度测试，但**跨端真实自动派发**是否已接通依赖后续独立工作；不得据控制面测试 PASS 夸称外部长程集成完成。

## 7. 推荐文件组织（提议：新增目录；不搬动旧版 Observe Iterate 目录）

### 7.1 讨论/审批与管理资料：继续留在已纳入的 `discuss-materials/`

```text
observe-iterate/
└─ discuss-materials/
   ├─ observe_iterate_control_plane_implementation_plan_v0.1_20261113.md   # 历史原版，不覆盖
   ├─ observe_iterate_control_plane_implementation_plan_v0.2_20261113.md   # 本修订计划
   └─ 观察迭代业务控制面_候选V0.2_20261113/                   # 计划经确认后一次性落地
      ├─ README.md
      ├─ 01_SOURCE_RULE_MATRIX.md
      ├─ 02_ARCHITECTURE_AND_LONGRUN_BOUNDARY.md
      ├─ 03_A_SHARED_MANAGEMENT_PRO_CONTRACT.md
      ├─ 04_A1_MATERIAL_MANAGEMENT.md
      ├─ 05_A2_REASONABLENESS_MANAGEMENT.md
      ├─ 06_C_CROSS_WORKFLOW_HANDOFF.md
      ├─ 07_B_CONTROL_CORE_DESIGN.md
      ├─ 08_IMPLEMENTATION_AND_ONE_SHOT_ACCEPTANCE.md
      ├─ 09_TEST_AND_NEGATIVE_CASES.md
      ├─ 10_OPEN_DECISIONS_AND_CHANGELOG.md
      └─ 11_OPERATIONAL_PATHS.md                # 新增：八种具体运行路径及唯一合法后继
```

每份文件维护其说明/审议职责；**唯一生效 Workflow 和权限定义位于受保护配置/执行入口**，说明文档只引用，不再另立一套状态真相。每新增一个文件或配置需在 `SOURCE_RULE_MATRIX` 登记 `谁读/何时读/改变什么/测试哪条`；没有运行消费者的文件不应强制成为每轮必交材料。当前两 Skill 包不移动或重写。

### 7.2 可执行候选实现：共用 `control-plane/`（本轮只设计，确认后一次性落地）

```text
observe-iterate/
└─ control-plane/
   ├─ README.md                             # 实际启动/advance/影子与正式模式
   ├─ config/source_bindings.lock.yaml      # 精确绑定两 Skill 包和审定控制规则
   ├─ workflows/
   │  ├─ material_preparation.yaml          # S0-S5管理视图和调用模式/合法路由
   │  ├─ reasonableness_analysis.yaml       # R0-R5, 探索/正式/定向重查/实例复验
   │  └─ cross_workflow.yaml                # 补证成功/部分/不可得/不适用/撤销
   ├─ policy/
   │  ├─ role_authority.yaml                # 有权决定谁能复核/放行/正式接收
   │  ├─ capability_budget.yaml             # 各种能力及成本边界
   │  └─ acceptance/                     # Gate 资格/必需检查；不强制每项独立 Pro 轮次
   │     ├─ material_plan.yaml
   │     ├─ material_run.yaml
   │     ├─ material_acceptance.yaml
   │     ├─ handoff.yaml
   │     ├─ expectation_freeze.yaml
   │     ├─ evidence_comparison.yaml
   │     ├─ diagnosis.yaml
   │     ├─ calibration.yaml
   │     └─ analysis_delivery.yaml
   ├─ contracts/
   │  ├─ shared/                           # task, question, call, work, action, proposal, review, receipt
   │  ├─ material/                         # material_requirement, plan, item, accepted_package
   │  └─ analysis/                         # expectation_freeze_request, result_envelope,
   │                                      # additional_evidence_request, evidence_request_outcome
   ├─ src/oi_control/
   │  ├─ cli.py                            # oi-control advance/status/init; 不强迫主控逐个选内部函数
   │  ├─ advance.py                        # 固定事件进入→验证/Gate/提交→返回可执行动作
   │  ├─ github_store.py                   # GitHub 精确读取、条件写入与版本冲突
   │  ├─ scheduler.py                      # 逐作用域资格判定→合格动作确定性排序
   │  ├─ plans.py                          # 管理 Pro 的结构化 work_delta 核验与应用
   │  ├─ gates.py                          # Gate 内部验证和受控语义复核入口
   │  ├─ authorization.py                  # 实际认证身份/操作权限/成本
   │  ├─ commit.py                         # Decision/状态/Audit/Receipt 原子入库
   │  ├─ dependencies.py                   # readiness/版本read_set/最小失效传播
   │  └─ recovery.py                       # 去重、失败不重做、未知效果、原轮次接续
   ├─ tests/
   │  ├─ fixtures/                         # 仅合成/模拟（禁止标为真实行情）
   │  ├─ unit/                             # 合同、就绪、算法、Gate、权限
   │  ├─ integration/                      # advance 与模拟已核验 R/W 回交
   │  ├─ fault_injection/                  # 重复、未知、冲突、迟到、补证不可得
   │  └─ real_case/                        # 真实用例的 GitHub 证据索引
   └─ pyproject.toml                       # 可运行工具及测试配置
```

可按实际代码复杂度合并较小 Python 模块，但**`advance`、权威状态写入、验证/审核、真正可核对的回执不能只有空壳函数**。不为每个材料项建独立绘图任务；不重写原 Skill 的数据操作代码；本轮不创建 `adapters/cgpterm_longrun.py`，只保留未来对接合同。

### 7.3 运行期状态与材料全部存放 GitHub（按用户明确方向修订）

**取消 V0.1 中独立 SQLite/事务数据库为默认运行状态源的建议。** GitHub 是本轮所有正式运行材料、状态、原件和证据的唯一持久化来源；本地计算缓存和临时文件不是第二权威状态。可复用其他 GitHub 仓库既有文件，以 `repo@commit:path + digest` 精确引用；大型历史数据要在真正使用前核实普通 Git、LFS 与权限能否承载，不能无依据假定所有行情文件都适合 Git 对象。

建议控制状态使用独立的、受保护的 GitHub 分支（具体名称与写入身份仍待确认），按 `control-plane-data/tasks/<task_id>/` 保存 `task/current_state, plans, work_items, proposals, validations, reviews, decisions, receipts, actions, dependencies, audit`。`current_state` 是由正式提交导出的查询视图，不能靠最后修改时间裁定最新。候选材料可位于普通提交；正式状态和受保护验收配置须由独立、经授权的入口写入，模型/Worker 不得凭自述改正式结论。

事务边界建议采用 Git commit 固定成组状态变更、分支引用带预期 head 的条件更新（CAS）、业务版本与幂等键核验；冲突后重新读取并核对，不能 `force` 覆盖。`CommitReceipt` 写业务提交 ID、版本与关联摘要，提交成功后向调用方返回 Git commit SHA，避免回执自引用 Git SHA 问题。仅在身份/分支写入权限真实隔离的情况下才称正式自动控制；否则标记草稿/影子模式。凭据绝不入仓。

### 7.4 外部长程代码：本轮不处理

不修改 `cgpterm`、`feature-production-agent` 旧主控协议/Skill/Worker 模式；不建立第二套物理消息发送和 R/W 运输。本轮只交 `advance` 外部事件及动作合同，利用模拟真实身份结构的 fixture 验证控制程序；旧长程代码实际接入另行处理。不将「模拟 R/W 接口通过」写成真实跨端已接通。

## 8. 一次性落地、随后立即试跑（原 W0～W7 为内部实施依赖，不再分批确认）

根据用户已明确的实施意图：**设计与新增控制规则先确认一次，再一并创建本轮文档、Workflow、Schema、Python 控制程序、测试和运行说明，之后直接启动真实业务试跑。** 不要求 W0、W1 等每个工作包结束后重复向 Owner 申请「继续」。工程实施内部仍应遵循先后依赖，以防带着未决规则写死代码：

1. **同一次实施的源规则核对**：锁定当前两个 Skill 目录及 CP 规范的可查版本；完成逐条 S/C/N 来源、冲突、受权状态与消费者矩阵，保留原 Skill 的专业内容。
2. **同一次实施的 A/C 管理材料**：共用管理 Pro、A1/A2 调用边界、不同结论与 Gate、跨任务补证全结果、按问题收束；参照 §3～4 和新增 `11_OPERATIONAL_PATHS.md`，不要求每轮重复输出四份文件。
3. **同一次实施的 B 核心实现**：GitHub 权威状态、统一 `advance`、结构化专业决定、按作用域调度、依赖就绪、受保护验证/Gate/提交、幂等和恢复，全部与测试联动，不能只写骨架。
4. **同一次实施的控制面测试**：模拟已核验长程回交、非法动作、缓存/回执冲突、双派发、补证不可得、v1/v2 迟到、不可调结论等；明确 PASS/FAIL/NOT_RUN，保留真实测试证据。
5. **落地后立即试跑**：在授权的真实高频或 EAW 用例，检查材料准备及到合理性分析的正式衔接；必要时试一次定向补证与恢复。若能力/权限不具备，记录准确阻塞和影子模式范围，不假称正式自动运行。

**本次不做**旧长程代码接线。真正 Pro/Worker 物理派发仍取决于后续独立工程，当前一次性交付不能代替它。正式状态写入身份、Gate 权限和高成本试验授权等若仍未确定，必须在真实动作前保持阻断并明确告知，不允许实施者自行批准。

**整体验收**：一套程序同时支持材料与分析两 Workflow；测试至少覆盖 `Skill调用边界/Material–Work–Action多对多/分层就绪/Gate结果与业务反证分离/补证全分支/round精确回归/标定复验单次复用/按依赖调度/问题级完成/advance`，并能追溯每条真实生效规则的消费者与证据。

## 9. 一次性落地的验收测试清单（保留 V0.1 义务、补本轮八类运行路径）

> 全部为拟实施测试，未运行；每个样例记录 `初始状态 → 合法后继 → 输入与证据 → Gate → 状态更新 → 后继`，分别标明模拟/真实、硬检查与专业结果。以下无「模拟运行＝业务实测通过」推断。

1. **正常材料链**：一轮 GO 后 S0/S1 调查规划通过→S2 合法运行→S3 实际取数→S4 验收→S5 交付；固定事件触发 `advance`，无需 Owner 逐步喊继续。
2. **调用边界**：派 S1 时允许小范围接口验证、不允许未经 G-RUN 的昂贵重算；已接受 S0 不被重复调查。
3. **材料与执行非一一对应**：一次完整 CAEGraph 返回 BP-07、BP-09、K线与映射；不得派四次完整计算。
4. **中间就绪无死锁**：源数据已 `CHECKED_FOR_PROCESSING` 但整包未接受；后续视图加工可继续，正式对照仍被限制。
5. **部分独立推进**：BP-07 具备限定用途、BP-09 阻塞；BP-07 合法工作仍可推进，不能暗降整体必需范围。
6. **假完成**：只有图定义/5行预览或仅 `construction_snapshot` 却声称完整/`viewport_final`，硬验收拒绝；T056/T059/正式看板不能混用。
7. **专业决定可落地**：管理 Pro 给出「先核对时间，若无错位再诊断参数」的结构化 work_delta，程序创建准确的工作与两条条件后继；仅自然语言则要求补结构，不擅自推断。
8. **Gate 与反证分离**：有充分证据的 `COUNTERS` 可通过分析工作 Gate；明确 `PROVEN_NOT_ADJUSTABLE` 是可接受的专业结论；不得强迫调到合理。
9. **硬检查与业务未决分离**：mandatory `UNKNOWN/NOT_RUN` 不能 PASS；`AMBIGUOUS/MISSING/PENDING` 经实证和授权完成定义可作受限业务交付。
10. **正式预期冻结**：`WORKING` 可探索；正式对照只用冻结版本，事后诱发的新预期进下一版。
11. **局部查证**：分析 Skill 在既有权限内查一个字段/小样本不新建跨 Workflow 补证任务。
12. **补证全结果**：`OBTAINED/PARTIAL/PROVEN_UNAVAILABLE/NOT_APPLICABLE/CANCELLED/SUPERSEDED` 均能解除或转移原等待，不出现无限 `WAITING_EVIDENCE`。
13. **迟到轮次**：v1 预期的补证在 v2 开始后返回，先回原 question/round/expectation；新轮必须另行验证适用，不能直接接入。
14. **标定复验只一次**：R4 内调用对照 Skill 的完整实例比较被 R2 能力复用为同一 work_id；不重复计算、不出现 R4 与 R2 互等。
15. **上游对象变化**：参数改变导致对象分段变化，必须回原始业务窗口比较新旧实例，不用已消失事件ID冒充同一对象。
16. **调度逐作用域**：一项阻断/效果未知不挡独立工作；同一候选失败且摘要不变不再重复验收；既定补查优先落地而非反复问 Pro。
17. **整体完成边界**：本轮仅授权识别/定位 select 与 merged；新市场环境问题进入后继建议，不能自动扩大必做范围；反证可以是合格交付。
18. **无进展**：重复换词报告不算进展；排除不同竞争解释或得到不可得事实算有效变化。
19. **权限和自我接受**：Agent 自写 `ACCEPTED`/reviewer role 不改变正式状态；无高成本许可不得执行重算。
20. **幂等与恢复**：相同 GO、相同 event/decision 提交与相同外部动作不能双提交/双派发；GitHub CAS 冲突按版本失败而非覆盖。
21. **真实执行回执**：长程 R/W 已回交不等于业务 Gate 通过；模拟运输的测试必须标模拟。
22. **取消、超时、未知效果**：先对账，不重放可能已有副作用的动作；允许受影响范围外已授权工作继续。
23. **限定范围完成**：只有经明确批准的任务完成条件允许时整体才可有界结束；否则局部接受不代表 ParentBusinessTask 完成。
24. **数据与存储安全**：GitHub 受保护状态写入无权者不可替代；过大的敏感原始数据或凭据不得无授权入普通 Git。

## 10. 必须公开的缺口和待确认事项（N；未经 Owner 批准不使权限/业务选择生效）

| ID | 需要确认 | 明确前可以怎样处理 |
|---|---|---|
| D01 | CP-SKILL-001 仍是评审稿，本次正式采用哪些条款？ | 以约束性设计和候选测试推进，不冒充已批准的业务授权 |
| D02 | GitHub 权威状态用哪个分支/路径；哪个经认证独立身份具有唯一写入权、如何隔离 Pro/Worker 直写？ | 可以制作本地/影子模拟；不能宣称正式强制门禁 |
| D03 | G-PLAN/G-MATERIAL/冻结/证据/诊断/标定/分析交付各由谁接受，管理与执行 Pro 同人时如何独立复核？ | 仅保留候选专业意见，无有权复核不正式提交 |
| D04 | `AUTO/REVIEW/FORBIDDEN` 的授权门槛、预算单位及哪些小探查免 G-RUN？ | 默认拒绝尚未授权的高成本动作；允许已有明确授权的只读探查 |
| D05 | 父任务 `required_questions/authorized_depth/acceptable_unresolved` 及材料/分析各自完成定义？ | 不擅自降低必需范围，也不把后继建议强塞本轮 |
| D06 | GitHub 原始数据、LFS/大文件、敏感信息与有效访问范围怎样安排？ | 只提交获准的材料和固定引用，未批准数据不出本地安全现场 |
| D07 | `SCOPED_ACCEPT` 的机器表达及是否允许特定受限问题完成？ | 建议规范基本 `ACCEPT + accepted_scope`，不能自行使父任务结束 |
| D08 | 真实长程主控何时及如何调用 `advance`、返回物理回执？ | **本轮后置**，只做边界合同与模拟，另项处理代码 |
| D09 | 第一条高频或 EAW 真实验证场景的版本、数据权限和运行条件？ | 在权限内做低成本确认；没有真实证据不能声称业务闭环实测 |
| D10 | 预期冻结时已看探索证据与正式样本如何隔离、记录截止/时区？ | 先保留版本与已看证据，未经批准不能无痕覆盖 |
| D11 | 标定可调参数、联合试验/完整重算的预算和候选实例接受权？ | 可以做公式层调查，未经授权不做超成本实验或正式参数修改 |
| D12 | 各候选 Skill 以什么范围试用，跨例推广或正式采纳的门槛？ | 锁定实际版本，报告候选能力，不预先宣称生产级 |
| D13 | 局部续作与跨 Workflow 补证的允许成本、能力、数据基线改变边界？ | 采用 §4.4 的专业判断原则；超出原授权时请求决定 |
| D14 | 调度同级业务优先级/资源独占/可并行范围；如何避免独立 WorkItem 被局部阻断饿死？ | 仅在已经批准的优先级/资源范围按稳定 ID 排序，不发明业务权重 |
| D15 | 各调用模式的停止边界与最小产物如何由当前 Pro/Worker 执行环境保证？ | 用 `ProfessionalCallSpec` 明确载荷，尚未接通物理端时靠模拟验收 |
| D16 | 补证 `PROVEN_UNAVAILABLE` 的调查充分性/是否允许本轮未决收束？ | 接受调查事实不等于证据齐全；需相应 Gate 与完成合同 |
| D17 | R4 内/外的比较工作唯一 ID、复用覆盖范围及实例变化下的原始窗口对齐策略？ | 先按 §3.3 单工作项设计，未验证等价不复用旧对照 |
| D18 | 正式状态写入在 GitHub Git 对象上的 CAS/授权如何工程验收？ | Git 提交/版本策略不能凭文档声明通过，需真实负例测试 |
| D19 | 统一 `advance` 如何让旧主控按固定事件触发，真实传递已验证调用身份？ | 本轮只定义事件/动作 Envelope，不自行接外部代码 |

每项须在 `10_OPEN_DECISIONS_AND_CHANGELOG.md` 标注 `proposed/approved/rejected/deferred`、授权主体、版本和影响。**本 V0.2 提出具体建议不等于自动替 Owner 作出 D 项批准。**

## 11. 非目标、可运行边界和停止规则

- 不搬动/改写现有两包专业 Skill，不利用 Observe Iterate 的其它旧目录作当前架构，不重新实现 CAEGraph/uplot/FeatDFProcessor 专业取数方法。
- 不改 `cgpterm` 或 `feature-production-agent` 旧长程代码；不建设第二套跨端消息、R/W 编号或 Worker 工单体系；物理自动派发未接入时如实说明。
- 不把 S0～S5、R0～R5 强制解释为十二次 Pro 调用，不逐份材料重复跑完整图，不强制每项补字段都走跨 Workflow Gate。
- 不把 Skill `DATA_READY`、模型 `confidence`、Worker 自述或 GitHub 普通文件的 `ACCEPTED` 当受保护正式采纳。
- 不把可信反证或参数不可调等领域结论判作专业工作不合格；不以修到合理为默认任务目标。
- 不以全局优先级遮蔽独立问题；不将新版预期与旧补证无条件混用；同一标定复验不重复计算；无新事实不无限调用 Pro。
- 不先开发任意 Workflow 引擎、微服务平台或通用 Agent 市场；不因精简代码而删除版本锁、必要硬 Gate、权限、幂等和回执。
- GitHub-only 不代表允许泄漏凭据或全部市场原始数据，真实存储资格未确认前拒绝相关敏感写入。

## 12. 一次性交付、审计和变更保护

1. V0.1 独立保存、不可改写；本 V0.2 只作为审查采纳后的**候选修改版**，所有新增 N 规则具有定位与验收目标，但不自动构成 Owner 授权。
2. 在本轮设计确认后，实施者**一次性落地本轮范围内**的管理文件、业务 Workflow、受控合同、可运行 Python 代码与测试；实施过程可按代码依赖编排，但不建立 W0～W7 八次独立确认/发布门槛。
3. 落地若遇本计划未覆盖、互相矛盾或无法真正执行之处，提出精确 `ChangeProposal`（原条款、失败现场、建议、替代方案、影响、所需批准），不能擅自删 Gate、扩权、改 Skill、降低必需范围或改变完成定义。
4. 每项代码和配置必须有具体消费者、受保护入口、读写对象、负例测试和真实执行凭据。GitHub-only 的正式状态需有独立授权身份和 CAS 实测；否则只可称影子/候选模式。
5. 完整落地后直接启动一个获授权真实用例：材料准备→交付→合理性分析→必要的定向补证→原轮次继续；明确模拟测试与真实行情/真实接收测试的证据区别。未授权的真实大规模标定不执行，不能假报 PASS。
6. 后续旧长程代码接线另行处理，只交业务动作协议和验收需求，不把其接线混入本次提交。

## 13. 新上传《修改建议》的逐项裁决与修订追溯

该反馈只审核 V0.1 §1～7.2，其关于第 7.3 及以后没有提出存储和排期结论；GitHub-only、一次性落地、长程代码后置、统一 `advance` 来自本聊天后续已明确的用户反馈，**不是冒称来自该审查文件**。

| 反馈问题/建议 | 本次判断 | 采纳位置 | 边界与保留项 |
|---|---|---|---|
| S/R 阶段与真实 Skill 调用没有一一对应 | **采纳** | §3.2～3.3、§5.3 | 保留阶段管理视图，不拆旧 Skill，不预设十二次调用 |
| 材料项不等于 WorkItem/ExecutionAction | **采纳** | §3.2、§5.2 | 多对多映射，优先复用完整图，避免重复重算 |
| 管理 Pro 决定缺少生效形式 | **采纳** | §3.1、§5.3 | 结构化 `work_delta/conditional successor`；程序不推断新业务价值 |
| 中间工作依赖全部等正式 ACCEPTED 易死锁 | **采纳但限定用途** | §4.2、§5.1 | 中间加工可受控继续，正式对照仍需独立材料/证据准入 |
| Gate 把反证/不可调判成失败 | **采纳** | §3.4、§5.1 | 分清工作合格、领域发现和下一动作资格；硬检查仍不得豁免 |
| 补证没有失败/不适用/取消返回；局部查字段流程过重 | **采纳** | §4.4、§5.6 | 只跨专业边界或独立交付才生成补证任务；不能把不可得当证据充分 |
| 轮次/预期/数据版本不贯穿回交 | **采纳** | §3.3、§4.1、§4.5 | 迟到先回原轮次；新轮复用另行验证 |
| R4 内部对照和外部 R2 重复复验 | **采纳并明确单次工作** | §3.3、§9 | 一个 comparison WorkItem，结果被 R4/R2 逻辑角色复用，正式验收不省略 |
| `get_next` 优先级不能作全局 if/elif | **采纳** | §5.4 | 按问题/WorkItem 判断资格，再确定性排序；局部阻塞不全局停 |
| 新问题无限扩充本轮、无法结束 | **采纳** | §4.1、§5.1 | 问题级 completion + authorized_depth；不偷偷缩小必需范围 |
| 所有管理结果都要四份文件、Gate 都要独立调用 | **采纳减负意见** | §3.1、§3.4、§7 | 四类回交按需存在，Gate 共用验证与受控结果，不增无消费者文件 |
| 用具体八个现场做正反面验证 | **采纳** | §9、目标目录 `11_OPERATIONAL_PATHS.md` | 实施后以真实回交/模拟负例分别证实，不能把文档推演当实测 |

**未采纳为“替代性架构”的做法**：不删除共用控制核心，不退回纯管理 Pro 自律；不取消正式 Gate、身份/版本保护；不要求每份中间产物都先获整体业务接受；不把合理性分析目标强制改成「修到合理」。反馈主张填补运行语义，而非推翻这些已讨论的原则。

**变更摘要**：V0.1 的 A/B/C 分工、两套专业 Skill、S0～S5/R0～R5 管理视图、Gate 核心、长程角色边界保持；V0.2 增强真实调用接口、管理决定生效、分层就绪、Gate 语义、补证退出、轮次身份、标定复验单工作项、按作用域调度和问题级结束。存储/交付/统一入口的修订属于用户后续明确条件，审查反馈原文未涵盖。
