# Observe–Iterate 业务控制面落地计划（讨论候选 V0.1）

- 形成日期：2026-11-13
- 文档性质：**待确认的实施计划，不是已批准的技术合同，也不是仓库已实现状态**
- 目标：在现有长程 Codex 主控—管理/执行 Pro—Worker—GitHub 协作方式之上，建设**一个共用业务控制核心**，组织「观察材料准备」与「合理性分析」两个可循环、可交接的业务 Workflow，使正常授权工作按 Gate 自动接续，异常定向恢复。
- 当前范围：仅纳入 `observe-iterate/main/discuss-materials/观察材料规划与准备Skill_候选V0.1_20261113/`、`observe-iterate/main/discuss-materials/reasonableness-analysis-skills-v0.1/` 与《业务控制面与 Skill 工程规范》；`observe-iterate` 其它历史目录**不视为当前 Agent 体系**。旧长程协议仅用于执行对接边界与兼容性核查。
- 实施边界：**本计划不授权修改现有 Skill、正式特征、参数、数据或长程主控协议**。所有新增设计均需要可追溯、必要时由 Owner 明确批准；实际落地先创建独立候选目录和新代码目录，不覆盖旧目录。

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

**唯一权威**：受信任控制程序及其存储保存正式业务状态；管理 Pro 可以作专业提议、在 Owner 授权范围内复核，但不能凭聊天、角色自填或普通 GitHub 文件直接改正式状态。GitHub 用于跨角色实物和 provenance，不自动等于权威状态数据库。

**角色可合并，权力不可假合并**：同一个 Pro 可以承担管理和专业执行，但有独立性要求的正式接受必须用真实独立复核执行或经 Owner 授权的有权主体；不能通过同一聊天里自称“复核角色”绕过。

**强制力分级**：未具备真实身份验证、隔离的状态写入口与受保护验证器时，只能开展草稿/影子/建议模式；不得声称自动正式采纳。首轮选用一个受控进程和简单事务存储即可，但必须使 Worker 无法直接写入正式状态与验收策略。

## 3. A：管理 Pro 合同

### 3.1 共用职责（新增 N）

管理 Pro 对完整业务目标负责，持续掌握目标、现有证据、当前正式阶段、工作计划、未决专业判断和后继安排。它：

- 读取 `read_business_state` 和已接受计划，而非自行维护另一份权威状态；
- 组织或修订专业工作计划，并说明工作项依赖、激活条件、最小充分结果及成本；
- 在相应 Gate 提交专业 `StageAssessment` 与 `ManagementDecisionProposal`；
- 将问题分为事实缺口、可由专业/证据解决、真正 Owner 取舍、越权或超预算；
- 对新材料需求、旧计划不充分、标定复验等情况形成可执行的定向返修或跨 Workflow 申请；
- 只在有权范围内决定，不自行生效范围变更、工具授权、正式接收或业务状态写入。

建议管理 Pro 的四类结果：`ProfessionalTaskPlan`、`StageAssessment`、`ManagementDecisionProposal`、`ProfessionalChangeProposal`。正常步骤用结构化字段与引用，不强制逐轮长文。

### 3.2 观察材料准备管理合同 A1（S0～S5；新增管理阶段 N，映射现有 Skill S）

| 阶段 | 来自现有 Skill 的专业活动 | 管理 Pro 的输入与工作 | 候选产物 | 转移/门禁 |
|---|---|---|---|---|
| S0 任务接管与调查 | 第 0 步、部分第 1 步；任务单 A | 明确目标、已有图/数据/源码、事实缺口和必要调查 | `AssetAndBindingAssessment` | 基础事实充分方可详细规划；不要求未知数据在首次调查前全部填齐 |
| S1 材料规划 | 第 1～4 步；任务单 B/C | 判断关键输入、实质阶段、预期/实现输出是否覆盖；每项材料必要性、来源、取数方式、依赖 | `MaterialPlan`/工作项提案 | **G-PLAN**：结构检查＋专业充分性复核 |
| S2 执行准备 | 第 4～5 步；取数参考 | 核实真实入口、版本、是否重算、预算、工具授权 | `ExecutionPlan`/前置调查 | **G-RUN**：针对有成本或副作用的动作授权；可逐次触发，不强制每个只读动作复核 |
| S3 实际材料取得 | 第 5 步；任务单 D | 监督逐项取得数据/图，处理技术异常和必要补查 | `MaterialItemResult`＋实际回执和证据 | 工作项级检查，符合条件的自动继续 |
| S4 整体核验 | 第 6 步；CAEGraph 最小验收 | 判断来源、身份、时间、源/显示阶段、缺项及可用范围 | `MaterialReview` | **G-MATERIAL**：全量/限定范围接受与未解决事项；不得自行降低原必需范围 |
| S5 接收与交付 | 第 7 步；任务单 F | 汇总可回答/不能回答的问题和材料包 | `AcceptedObservationMaterialPackage` 候选 | 受保护正式提交与回执；任务完成条件另行核对 |

每项材料计划记录 `material_id / necessity / business_question / processing_stage / source / data_stage / identity_and_time / dependencies / activation_condition / completion_evidence / cost_estimate / current_unknowns`。专业字段来自 Skill，`id/依赖/触发/验收可追踪性` 为控制面新增 N。条件材料仅在触发事实与专业决定成立时激活。

### 3.3 合理性分析管理合同 A2（R0～R5；新增管理阶段 N，专业方法仍来自 Skill S）

| 阶段 | 对应现有 Skill | 专业活动与管理重点 | 关键控制/转移 |
|---|---|---|---|
| R0 接管与证据资格 | 四 Skill 的共同入口及 README 双轨 | 核对业务目标、判断对象、已有材料包及最低可用信息 | 可进入探索，不代表可以进入正式对照；必要时并行请求事实准备 |
| R1 预期推导与冻结 | `business-expectation-derivation` | 区分 `OWNER_EXPLICIT / BUSINESS_INFERRED / IMPLEMENTATION_DERIVED`，提出最小可检验预期和场景 | **正式冻结** `FrozenExpectationSet`，有版本/摘要/适用范围和接受记录；`WORKING` 可用于探索 |
| R2 证据对照 | `business-evidence-comparison` | 按冻结预期比较 `SUPPORTS/COUNTERS/MISSING/AMBIGUOUS/NOT_APPLICABLE/PENDING`，形成效果对照与偏差队列 | 正式对照须绑定已冻结版本、数据口径和来源；新证据诱发新候选预期，不回写旧版 |
| R3 偏差诊断 | `business-discrepancy-diagnosis` | 区分数据/时间/输入/处理/预期等原因，定位最早分歧，形成最小区分性实验 | 证据缺口→补证；预期问题→R1；实现问题→外部实现修正；真正取舍→Owner；参数初筛→条件进入 R4 |
| R4 实例参数标定（有条件） | `feature-instance-calibration` | 合法自由参数、可行域、多位置交集、少量试验、上游耦合与完整实例复验 | 启动/高成本试验需要授权；标定后回 R2 复验；初次实例化可按 Skill 条件直接进入，不强制先 R3 |
| R5 分析结果接收与后继 | 汇集四 Skill 输出 | 明确支持/反证/未决、适用范围、后继及未解决问题 | 依据本轮完成定义正式接受；不能把“已诊断”或“候选实例合理”当作生产参数已改 |

**非瀑布**：README 允许先用少量事实和样本形成 `WORKING` 预期，正式支持/反证前才冻结。R2 发现新场景可生成 R1 新版本；R3 缺证据可返回事实准备/R2；R4 后回 R2，仍有偏差返回 R3。工作流需在 `workflow.yaml` 里明示合法分支，不能只用阶段数字线性推进。

### 3.4 Gate 的专业语义及责任

- **G-PLAN**：针对材料规划，验证是否遗漏关键业务输入/实质中间阶段/最终输出，必要性和取数路径是否合理。程序只做字段、来源、依赖、版本等机械检查；专业充分性需授权复核。
- **G-RUN**：针对具体高成本取数/重放/图构建动作，核对是否需要、是否已用更低成本方法、资源许可、当前版本和剩余预算；一般只读和已授权低成本操作不用默认重复审批。
- **G-MATERIAL**：材料真实取得、数据阶段与身份/时间一致、必要性覆盖、缺口影响；允许限定范围接受，但不得把核心必需项无授权降为可选，也不得无权结束整个任务。
- **G-EXPECTATION-FREEZE（新增）**：最小预期包有来源、可证伪、适用/不适用条件、范围与版本；完成正式冻结后不可无痕改写。
- **G-COMPARISON（新增）**：冻结版本、证据资格、时间口径与反例依据；对照产物明确支持、反证、缺失、歧义，不用源码正确冒充业务合理。
- **G-DIAGNOSIS（新增）**：偏差是否定位、有无排除竞争解释、后继指向是否受证据支持；是否有必要补证/返预期/移交实现/Owner。
- **G-CALIBRATION（新增）**：入口可修复性或初次实例化依据、合法参数自由度、实验权限、成本上限、基线、完整实例复验；试验成功不等于生产采纳。
- **G-ANALYSIS-DELIVERY（新增）**：本轮证据与结论是否充分、未决是否如实保留，是否满足该轮定义的完成标准。

各 Gate 的 `AUTO / REVIEW / FORBIDDEN` 资格和接受者权限**不能凭本计划擅自设定**；在工作包 W2 经 Owner 或已授权治理者批准。自动程序性检查必须与专业语义复核分开，必须检查 `PASS/FAIL/UNKNOWN/NOT_RUN`。

## 4. C：观察材料准备与合理性分析的衔接（新增 N）

### 4.1 父子任务

- `ParentBusinessTask`：一次完整观察—分析业务目的；可以有多个业务子任务与分析轮次。其是否完成不同于任何 Pro/Worker Return 完成。
- `MaterialPreparationTask`：按本轮材料计划准备并验收材料；可有后继补证子任务，不改写已接受原包。
- `ReasonablenessTask / AnalysisRound`：按某轮冻结预期、数据版本与场景形成判断；可能多轮修订。
- `AdditionalEvidenceRequest`：由合理性分析对指定场景和偏差提出可核查的材料缺口，关联原分析轮次、证据与回交目标。
- `CalibrationRun`：可作为 ReasonablenessTask 的受控工作项或子执行，不能自动升级为生产修改任务。

`production_run_id`（长程）、`business_task_id`（业务）、`analysis_round_id`（证据轮次）、`work_item_id` 和 `W/R`（长程工单/轮次）分开；一轮 Pro 可包含多项工作，一项业务工作可经过多轮 Pro/Worker。

### 4.2 两种使用资格

1. **探索用途**：合理性分析可以使用已标明来源和限制的少量真实样本，形成 `WORKING` 候选预期、了解实际字段和场景；不能据此直接给出正式“符合/不符合”结论。
2. **正式对照用途**：必须绑定已冻结 `FrozenExpectationSet`、符合用途的已接受材料或通过专门受保护证据资格检查的原始证据、明确数据/代码/参数/时间版本与适用范围。材料准备内部 Gate 不代替合理性分析的目的适用性检查。

材料准备 G-MATERIAL 负责材料自身是否可交付；合理性分析入口/对照资格负责它是否足以检验具体预期。可复用材料验证，不重复做无意义检查。

### 4.3 `AcceptedObservationMaterialPackage`（由 Skill 任务单 D/F、CAEGraph manifest 提取并加受控字段）

至少包含：`package_id, material_task_id, parent_business_task_id, purpose_id, material_plan_version, accepted_artifact_refs/digests, code/data/parameter/skill bindings, object/time/window/data_stage, data_quality, answerable_questions, limitations, unresolved_questions, acceptance_decision_ref, commit_receipt_ref`。

该包只代表已接受的材料及适用范围，不代表合理性分析结论。

### 4.4 `AdditionalEvidenceRequest`（新增 N）

至少包含：`request_id, parent_business_task_id, requesting_analysis_round_id, purpose_id, missing_question, discriminating_value, needed_evidence, existing_evidence_refs, object/time/field_scope, priority, authorized_cost_boundary, desired_return_to, requesting_proposal_ref`。

控制流程：

```text
R2/R3发现缺失且值得补
→ 提交补证提案
→ 查询是否已有同范围/版本的合格材料
→ 若已有：绑定引用，恢复分析
→ 若无：核权、核预算、专业规划最小工作
→ 建立关联材料子任务/追加工作项
→ 既有长程主控派 Pro/Worker 实际补证
→ G-MATERIAL 核验补证候选
→ 生成新材料包/补充包与提交回执
→ 解除原分析轮次的对应等待
→ 重验受影响的结果，恢复 R2/R3
```

核心条件：不得无限循环同一补证请求；不能把条件材料一律提前全量准备；不能因为新材料出现就无痕改写既有冻结预期；仅重验真正受影响的工作项及结论。

### 4.5 上游变更的失效传播

明确记录 `read_set`（源代码/数据/参数/预期/材料包版本与摘要）。若发生修订：旧产物保留只读；计算依赖图定位受影响的下游提案，标记待重验或产生新轮次，**不能**把旧产物 version 改成新值冒充已验收。

## 5. B：共用业务控制程序设计

### 5.1 四种状态维度

- `DomainState`：`ParentBusinessTask`、材料包、已冻结预期、分析结论等**业务事实**及版本；只在受保护正式提交时更新。
- `RunState`：任务/阶段执行过程（参考规范 `NEW / READY / RUNNING / SUBMITTED / VALIDATING / ACCEPTED / REPAIR_REQUIRED / WAITING_REVIEW / REJECTED` 等），不等于业务版本。
- `WorkItemState`（新增）：例如 `PLANNED / READY / IN_FLIGHT / SUBMITTED / VALIDATING / ACCEPTED / REPAIR_REQUIRED / BLOCKED / SUPERSEDED`；多个工作项可同时处于不同状态。
- `ActionState`：外部实际派发 `REQUESTED / AUTHORIZED / DISPATCHED / CONFIRMED / FAILED / EFFECT_UNKNOWN`；R/W 物理执行状态仍由长程主控负责并提供可信回执。

现有 Skill 的交付标签、合理性分析的预期状态、证据状态、诊断可调性状态均作为**领域内容字段**，不混成一种通用 RunState。

### 5.2 共用数据/协议对象

`TaskContract`、`WorkPlanProposal`、`ResultProposal`、`ArtifactRef`/`EvidenceRef`、`ExecutionReceipt`、`ValidationReport`、`ReviewRecord`、`DecisionRecord`、`CommitReceipt`、`ActionRequest`/`ActionReceipt`、`Blocker`、`AuditEvent`、`SourceDependency`。这些主要由规范 C 定义通用骨架，业务字段与具体业务产物来自 S 或新增 N。

业务专有对象：`MaterialPlan`、`MaterialItemResult`、`AcceptedObservationMaterialPackage`、`FrozenExpectationSet`、`EvidenceComparisonPackage`、`DiagnosisReport`、`CalibrationResult`、`AdditionalEvidenceRequest`。后四个专业包的内容合同**引用既有 Skill**，不要在控制面重复重新定义一套业务含义。

### 5.3 控制程序接口及语义

| 接口 | 输入 | 权威结果/副作用 |
|---|---|---|
| `create_or_resume_task` | Owner任务原文及受认证授权、父子任务身份、版本/范围 | 新建（先去重）或恢复同一任务；初始化不代表任意外部动作获准 |
| `read_business_state` | task/parent id、认证调用身份 | 权威状态、已接受计划/材料、候选、阻塞、预算、下一合法工作概览 |
| `submit_work_plan` | 管理/执行 Pro 的计划提案、依赖/激活条件、范围变化 | 保存不可变候选，审核后才可变为已接受计划 |
| `submit_stage_result` | 关联 task/stage/work item 的候选结果及证据 | 保存候选与 attempt，不自动推进或接受 |
| `record_verified_execution_result` | 现有长程主控已核验的 R/W 回交、执行证据和动作身份 | 关联 WorkItem 与真实派发/回交，不把 Worker 口述当工具事实 |
| `validate_stage_result` | 候选摘要、受保护验收配置/验证器版本 | 独立 `ValidationReport`，逐项 PASS/FAIL/UNKNOWN/NOT_RUN |
| `record_gate_decision` | 有权 Gate 身份、证据、ReviewRecord、候选摘要 | 保存有权决定；不只依赖模型自报 role |
| `commit_stage_transition` | 决定、当前 domain version、完整 read_set、幂等键 | 原子登记业务版本/决定/审计/CommitReceipt，触发已批准后继 |
| `get_next_business_action` | 读取权威状态、依赖、授权、预算、现有在途动作 | **只规划**合法下一动作；不直接发送消息或执行工具 |
| `claim_and_dispatch_action`（新增必需） | 合法下一动作、当前版本、资源锁/lease | 原子占用+登记 outbox/派发请求，防止双主控重复发送；由现有长程主控实际发送 |
| `submit_additional_evidence_request`（新增） | R2/R3 提出的缺项/场景/影响/目标轮次 | 查询可复用材料，建补证提案/工作或待授权请求 |
| `register_material_handoff`（新增） | G-MATERIAL 已接受的材料包+用途 | 绑定接收范围与下游分析，不隐含目的适用性已通过 |
| `freeze_expectation`（新增） | 预期提案、来源、范围、冻结准入复核 | 受保护写入冻结版本和摘要；不由 Skill 自改 status 实现 |
| `request_action / reconcile_action / cancel_run` | 动作/授权、外部回执、待取消运行 | 检查实物和未知效果，安全取消/对账；复用长程真实运输状态 |

前面讨论的 `get_next_business_action` 仍是**核心调度决策**，但为了可靠性，要把“查询下一动作”和“原子占用并发派”明确分开。否则两个主控可能同时读取同一 `READY` 项并重复派发。

### 5.4 下一动作决策优先级（新增 N，需回归测试）

```text
1 读取权威状态，若任务 CANCELLED / QUARANTINED / 完成，不再派发
2 若有 EFFECT_UNKNOWN 的动作：先 reconcile，暂停会重放同一效果的路径
3 若有已提交未验证的候选：执行受保护验证
4 若硬检查 PASS 但需语义复核：形成具名 Gate 任务
5 若有合法有权 Gate 决定尚未提交：执行原子提交
6 若有等待的已获批准 WorkItem，依赖齐全且预算/权限满足：派发
7 若需要专业新增计划/明确后继：定向 CALL 管理/执行 Pro 提议
8 若需要补证：关联请求并启动或恢复指定材料子任务
9 若合法阶段完成：自动进入下一阶段/下一 Workflow
10 否则具名 WAIT_INPUT / WAIT_OWNER / BLOCKED，附责任者、解除条件、恢复点
```

绝不让“建议继续研究”在没有新事实、新工作项或阶段推进时构成无限循环。

### 5.5 Gate / 正式提交与权限

- 每个 Gate 配 `entry_condition / required_hard_checks / semantic_review_policy / authority / accepted_scope / failure_route / cost_boundary`；可执行验收配置受保护，不能由候选产物覆盖。
- 必需硬检查为 `FAIL / UNKNOWN / NOT_RUN` 时不能正式通过；语义复核的权限和证据要求必须明确；不使用模型 confidence 自动扩权。
- **接受权与创建权分离**；管理 Pro 拥有多少 Gate 接受权限由 Owner 本轮授权决定。
- `SCOPED_ACCEPT` 是讨论中提出的**扩展业务表达**：可实现为正式 `ACCEPT` 加上不可变的 `accepted_scope/limitations`，但需确定它是否允许结束当前任务；不得擅自扩大通用规范的机器枚举。
- 状态、决定、审计、回执必须同一事务性边界原子提交；同幂等键同载荷返回同一结果，同键异载荷报冲突。
- 新候选引用必须固定版本；GitHub path 或 branch 名单独不构成不可变证据。来源和语义验证不能由哈希单独证明。

### 5.6 恢复与审计

保留：`stage/work_item/attempt`, `what_blocked`, `who_resolves`, `what_is_missing`, `when_to_retry_or_expire`, `resume_from`, `remaining_budget`, `read_set`；崩溃后从正式状态、租约、CommitReceipt 与在途动作恢复，不从模型记忆重建。

`TIMEOUT/EFFECT_UNKNOWN` 先查物理端和外部对象，绝不盲目重发昂贵或有副作用的工作；重复无进展触发 `NO_PROGRESS`；数据/参数/代码变化只使依赖结果待重验；安全或越权进入拒绝/隔离。展示页是正式状态的读模型，非权威状态源。

## 6. 与既有长程主控的接口边界（新增适配，不复制旧协议）

**控制面向长程主控发出**：`business_action_id, business_task_id, stage_id, work_item_id, target_role, skill_ref, purpose, assignment_ref, expected_return, allowed_scope, deadline/budget, idempotency_key`；业务控制端不自行发送物理聊天。

**长程主控核实后回交**：`business_action_id, production_run_id, actual_invocation_id, optional_work_order_id, sent/received receipt refs, exact GitHub commit+path refs, action outcome/effect-known status`。

有三个必须保持的旧约束：

1. 由**Pro 签发** Worker Order，业务控制程序不能自己伪造 W；Codex 主控只负责合法派发/监控/回交。
2. R/W 是长程运输与工单编号，不等于业务阶段/工作项；一项业务工作可以多轮 R/W，一个 R 可包含多个工作结果。
3. 旧长程中的 `PRO_CURRENT`、发件和 Return 等不等于业务状态数据库。业务状态只能由 B 的正式提交更新；长程 Gate 也不能证明业务正确。

首先开展接口盘点，确认当前 cgpterm 实际采用版本与 `LONGRUN_PROTOCOL_V1` 的调用契约；尚未接通之前只能做模拟适配测试，不宣称跨端自动运行。

## 7. 推荐文件组织（提议：新增目录；不搬动旧版 Observe Iterate 目录）

### 7.1 讨论/审批资料——存在 `observe-iterate` 已纳入的 `discuss-materials/` 下

```text
observe-iterate/
└─ discuss-materials/
   └─ 观察迭代业务控制面_候选V0.1_20261113/                 [新增]
      ├─ README.md                                       [定位/权威关系/阅读顺序/成熟度]
      ├─ 01_SOURCE_RULE_MATRIX.md                         [逐条：S/C/N、出处、原义、归属、实施状态/冲突]
      ├─ 02_ARCHITECTURE_AND_LONGRUN_BOUNDARY.md           [管理 Pro / 主控 / Worker / GitHub / B 的边界]
      ├─ 03_A_SHARED_MANAGEMENT_PRO_CONTRACT.md            [共用管理职责、授权、四类回交]
      ├─ 04_A1_MATERIAL_MANAGEMENT.md                      [S0-S5、G-PLAN/G-RUN/G-MATERIAL、工作项]
      ├─ 05_A2_REASONABLENESS_MANAGEMENT.md                [R0-R5、四 Skill、冻结/诊断/标定/复验]
      ├─ 06_C_CROSS_WORKFLOW_HANDOFF.md                    [探索/正式使用、材料包/补证/恢复]
      ├─ 07_B_CONTROL_CORE_DESIGN.md                       [状态/接口/权限/调度/提交/审计/恢复]
      ├─ 08_IMPLEMENTATION_WORK_PACKAGES.md                [W0-W7、依赖、验收、证据]
      ├─ 09_TEST_AND_NEGATIVE_CASES.md                     [正常/反例/真实故障/影子与真实区分]
      └─ 10_OPEN_DECISIONS_AND_CHANGELOG.md                [待裁事项、正式决定、任何偏离先提案]
```

**文档职责**：解释为什么以及如何实施，维护来自现有文档的出处；不能再维护另一套会与运行 YAML 冲突的“正式状态真相”。`01_SOURCE_RULE_MATRIX.md` 是差异审计和变更保护的关键。现有两包 Skill 不搬走、不覆盖；只以 commit+path 引用它们。

### 7.2 可执行候选实现——新建独立 `control-plane/`（不是复用旧 `runtime/`）

```text
observe-iterate/
└─ control-plane/                                          [新增、待实现]
   ├─ README.md                                           [如何运行/权限前提/哪些仍为候选]
   ├─ config/
   │  └─ source_bindings.lock.yaml                         [首次经批准锁定两包Skill及规范引用]
   ├─ workflows/                                          [生效的状态与合法路由唯一位置]
   │  ├─ material_preparation.yaml                         [S0-S5 + G-PLAN/G-RUN/G-MATERIAL]
   │  ├─ reasonableness_analysis.yaml                      [R0-R5 + 快速路径/循环/标定分支]
   │  └─ cross_workflow.yaml                               [材料接收/补证/恢复/完成]
   ├─ policy/                                             [仅保护版本可运行]
   │  ├─ role_authority.yaml                               [Owner/管理Pro/执行Pro/Worker/主控/Gate复核]
   │  ├─ capability_budget.yaml                            [动作权限/成本/超限/暂停条件]
   │  └─ acceptance/
   │     ├─ material_plan.yaml                             [G-PLAN]
   │     ├─ material_run.yaml                              [G-RUN]
   │     ├─ material_acceptance.yaml                       [G-MATERIAL]
   │     ├─ handoff.yaml                                   [接收与用途资格]
   │     ├─ expectation_freeze.yaml                        [冻结前检查]
   │     ├─ evidence_comparison.yaml                       [正式证据对照]
   │     ├─ diagnosis.yaml                                 [诊断与后继]
   │     ├─ calibration.yaml                               [标定及实验许可/复验]
   │     └─ analysis_delivery.yaml                         [R5]
   ├─ contracts/
   │  ├─ shared/                                           [通用受保护对象，仅一份定义]
   │  │  ├─ task_contract.schema.json
   │  │  ├─ work_item.schema.json
   │  │  ├─ result_proposal.schema.json
   │  │  ├─ artifact_evidence_ref.schema.json
   │  │  ├─ execution_action_receipt.schema.json
   │  │  ├─ validation_review_decision.schema.json
   │  │  └─ commit_receipt.schema.json
   │  ├─ material/
   │  │  ├─ material_plan.schema.json                       [源自现有任务单A-C]
   │  │  ├─ material_item_result.schema.json               [源自任务单D和CAEGraph清单]
   │  │  └─ accepted_material_package.schema.json          [跨Workflow正式交付N]
   │  └─ analysis/
   │     ├─ expectation_freeze_request.schema.json        [引用原Skill的ExpectationRegister]
   │     ├─ analysis_result_envelope.schema.json           [引用原Skill的对照/诊断/标定包]
   │     └─ additional_evidence_request.schema.json       [跨Workflow请求N]
   ├─ src/oi_control/
   │  ├─ api.py                                            [create/resume/read/submit/commit等接口]
   │  ├─ state_store.py                                    [权威状态、版本、事务、幂等]
   │  ├─ scheduler.py                                      [get_next_business_action]
   │  ├─ action_dispatch.py                                [动作占用/租约/outbox，交长程主控]
   │  ├─ gate_engine.py                                    [hard check + 语义复核请求]
   │  ├─ authorization.py                                 [角色/真实主体/资源操作校验]
   │  ├─ validation.py                                    [受保护执行、产物/回执核对]
   │  ├─ commit.py                                        [Decision/CommitReceipt 原子提交]
   │  ├─ dependencies.py                                  [版本read_set/失效传播]
   │  ├─ recovery.py                                      [失败/NO_PROGRESS/UNKNOWN对账]
   │  └─ audit.py                                         [可查询审计与状态读模型]
   ├─ adapters/
   │  └─ cgpterm_longrun.py                                [只翻译业务动作/已核实的R/W回交]
   └─ tests/
      ├─ fixtures/                                        [模拟用例；不得冒充真实行情验收]
      ├─ unit/                                            [状态/权限/版本/调度等]
      ├─ integration/                                     [控制核与长程适配模拟]
      ├─ fault_injection/                                 [超时/重复/崩溃/迟到/越权]
      └─ real_case/                                       [真实取数、正式接收的证据索引，不存敏感原始数据]
```

注：这棵树是**目标结构，不要求第一工作包立即建完所有文件**。实现中可合并 Python 模块，但不得合并候选、验证、接受与回执的权力和概念。`analysis_result_envelope` 只为接收和版本管理提供统一封面，四个原 Skill 的业务输出合同保持原位。

### 7.3 运行期数据不放在哪里

**不要**把可变数据库、密钥、任务当前状态直接当作 GitHub 讨论文档。运行期推荐独立的受控存储（首轮可用真正隔离写权的轻量事务服务/SQLite 后端）。`GitHub` 只存固定提交可查的候选材料、决定引用和允许公开的审计/结果摘要；源数据和敏感日志按已有授权存放在合适的数据盘或受控制品库。控制程序能根据其正式存储生成只读进度报告。

### 7.4 外部长程代码放在哪里

**先不更改** `cgpterm` 和 `feature-production-agent` 旧协议或主控 Skill。先在新的 `adapters/cgpterm_longrun.py` 做接口适配和模拟；真实接入之前，由拥有对应仓库权限的维护者确认准确入口和必要改动，再按独立变更计划实施。不建立第二套物理消息发送、R/W ID 或 Worker Order 机制。

## 8. 分期实施工作包与验收

| 阶段 | 实施工作包 | 主要交付及来源 | 验收完成定义 |
|---|---|---|---|
| **W0 源约束冻结/盘点** | 取得两 Skill 包精确 Git commit 与完整引用、规范版本；整理 `S/C/N` 来源矩阵，盘点现有长程入口、旧资产仅作兼容核查 | `01_SOURCE_RULE_MATRIX.md`，差异表（已实施/仅文档/缺失/冲突） | 所有拟新增规则能追溯；无未经说明的旧目录复活/Skill改写 |
| **W1 A 管理合同** | 共用管理 Pro、A1 S0–S5、A2 R0–R5、各 Gate 输入/输出/专业判断/返修与Owner升级；明确非瀑布 | 03/04/05 文档；专业源自 S，管理增量 N | 用一个材料案例和一个合理性分析案例可以逐步明确谁做什么、返回什么、何时自动继续 |
| **W2 权限/合同/跨Workflow设计** | 父子任务、两用途资格、材料包/补证请求、版本/读依赖、正式冻结、角色权限、预算、Gate接收人 | 06/07、workflows、contracts、policy 草案 | 对两条 Workflow 都能列出合法/非法转移；Owner 未决项明确且未经批准不得正式生效 |
| **W3 B 最小控制核心** | 受控状态存储、提案、验证、复核、正式提交回执、get_next、原子派发占用、依赖与审计 | `src/oi_control/` 核心，unit tests | 在模拟执行回交下，一次 GO 后自动运行合法后继、Gate 返修、恢复；非法自我接受被程序实际挡住 |
| **W4 长程适配** | 控制动作↔既有长程 Pro R/Worker W 回交的映射，真实收件端验证、幂等派发/UNKNOWN对账 | adapters，integration tests；旧协议作为输入但不改写 | 主控能核实实际派发及回交，再通知业务控制核；不把 W 完成当业务 Gate 通过 |
| **W5 首个真实材料准备闭环** | 选择有实际运行条件的高频或 EAW 用例，真实取数、G-PLAN/G-RUN/G-MATERIAL、交付限定范围 | real_case 实物及回执；源自材料 Skill | 真实数据、来源、图/数据阶段、缺口与可用范围经独立验证；不是只有预览、Notebook定义或模拟 |
| **W6 真正的分析/交接闭环** | 接收材料、渐进探索、冻结最小预期、正式对照、诊断、补证并恢复原轮次 | 四 Skill 原产物＋新 handoff/analysis Gate | 不重复从头取数；补证能原路回交；数据/预期更新只重验受影响部分；证据未充分不冒充结论 |
| **W7 标定分支与故障/发布验收** | 参数首次实例化/诊断后标定资格、受限试验、完整复验；超时、取消、并发、重复、失效、未知动作、越权与恢复 | calibration profile、fault-injection、回归与实测报告 | 无权限不发生正式重算/改生产参数；模拟与真实分开；全部 mandatory Gate 有实际结果与残余风险说明 |

**依赖安排**：W0 → W1/W2 可部分并行 → W3 → W4 → W5/W6（可提前用模拟打通，真实按依赖分步）→ W7。跨 Workflow 数据结构和冻结条件必须在 W3 前定义；不能等材料准备代码全部写完才发现合理性分析的路由不兼容。

**实施节奏约束**：每一工作包结束先形成 source diff（原定内容/实际实现/新增理由/影响/待批准）。不能为“快速成功”自行删减 Gate、改变 Skill 专业判断、把源 `DATA_READY` 写成正式 `ACCEPTED`，或把 `FROZEN_FOR_COMPARISON` 改为模型可编辑的字段。

## 9. 第一轮验收测试清单

> 下列是**待实施**的验收用例，未运行；真实测试必须记录环境、输入、预期、实际证据、状态写入与审核者。

1. 正常链路：一次启动后，S0→S1 材料规划/审核→S2合法动作→S3取数→S4核验→S5正式接收；通过后无需 Owner 再说“继续”。
2. 只找到图定义或 5 行预览时，`DATA_READY` 的候选不得被正式接受。
3. CAEGraph `construction_snapshot` 不得冒充 `viewport_final`；T056、T059、正式看板不得误混。
4. `PARTIAL_WITH_LIMITS` 可登记限定范围使用；必需材料未完成时未经授权不得把整个任务标为完成。
5. G-PLAN 规划漏必要中间阶段：返回定向专业返修，而不是改写任务目的。
6. 未绑定 Skill/代码/数据版本或使用旧基线候选：应拒绝对应正式执行/接收。
7. 管理 Pro/执行 Pro 在同一对话里自行填写 `role: reviewer` 或 `ACCEPTED`：不改变正式状态。
8. 合法下一 WorkItem 自动派发；无进展重复 `CALL_PRO` 被限次；并发两个调度者不产生重复派发。
9. 长程 W Return 已回交但材料未验证：工作项保持待检；长程 R/W 不能直接推动业务 Gate。
10. 事实准备/少量样本探索可在 `WORKING` 预期下进行；正式对照必须绑定 `FrozenExpectationSet`，新证据只能产生新版本。
11. `MISSING / PENDING / ValidEmpty / NoOccurrence / InsufficientHistory` 不被误当业务反证或可忽略的空值。
12. 合理性分析请求已存在的合格材料，控制面直接复用；不存在时生成唯一补证工作并回原 `analysis_round_id`。
13. 补证新增材料不改变旧依赖时，不重跑所有分析；改变冻结相关数据/参数/版本时，受影响对照进入重验。
14. 诊断 `POSSIBLY_ADJUSTABLE / COUPLED_UNRESOLVED` 可提出 R4 资格申请；无实际授权不得开启昂贵试验；首次实例化路径不要求先伪造诊断。
15. 参数局部试验成功但改变上游对象，不能自动称完整实例合理；正式修改生产参数仍为范围外动作。
16. 超时/回执丢失/外部效果未知，先对账；成功的 Worker 动作不可盲目重跑。
17. 崩溃/重复请求/迟到回交/过期租约不会形成双提交、双派发或无痕覆盖。
18. 取消/超预算/越权/安全异常必须停派发、保留现有有效产物、显示明确负责人和恢复条件。
19. 同一人管理/执行场景下，独立接受要求有真实受控复核，而不是同一提示词扮演两种身份。
20. 父任务完成由完整业务完成标准判断；某个 S5、R5、Worker 回交成功不能自动结束父任务。

## 10. 必须公开的缺口和待确认事项（N；不自行填默认值生效）

| ID | 未决问题 | 影响和需要的决定 | 决定前可以做什么 |
|---|---|---|---|
| D01 | 本次是否正式采纳 CP-SKILL-001 v0.1 的哪些条款？ | 它是工程评审稿，不自动成为现行授权 | 依据其原则做草案和模拟，不宣称强制控制已部署 |
| D02 | 谁是权威状态写入口的持有者，运行环境/认证/存储具体在哪里？ | 若 Pro/Worker 能写状态库或验收程序，强制门禁失效 | 设计保护方案，模拟/影子运行；正式接受暂停 |
| D03 | 谁对 G-PLAN/G-MATERIAL/G-EXPECTATION/G-COMPARISON/G-DIAGNOSIS/G-CALIBRATION/G-ANALYSIS 有接受权？ | 管理 Pro 的委托范围和独立复核要求 | 列 Gate 权限矩阵草案，待授权确认 |
| D04 | AUTO / REVIEW / FORBIDDEN、风险等级及高成本操作的授权阈值？ | 决定是否能够无人介入执行 | 先不自动执行成本/权限未明确的操作 |
| D05 | 父业务任务、材料任务和分析轮次的完成定义是什么？ | 尤其“局部被接受”与“整个任务结束”不能混同 | 首版强制保留剩余项，不擅自缩范围 |
| D06 | 正式接收的材料包存储、数据访问、可保留哪些来源/敏感日志、期限？ | 影响真实交付/复查及安全 | 草案使用无敏感 fixtures，真实数据路径待核 |
| D07 | `SCOPED_ACCEPT` 机器枚举如何表达？ | 规范通用 DecisionRecord 是 `ACCEPT/REPAIR/REVIEW/REJECT`；讨论中希望局部接受 | 建议 `ACCEPT + accepted_scope`，正式决定前保留待裁 |
| D08 | 哪套 `cgpterm` 主控实现和长程协作协议是本次实际采用版本？ | 旧 FPA 合同有具体实现，但不证明现在已接好观察迭代 | W0 盘点真正入口，先模拟兼容 |
| D09 | 第一条真实端到端用例选高频还是 EAW？数据/计算权限是否具备？ | 决定 W5 能否真正执行 | 用现有 Skill 做低成本可行性调查，不伪称实测 |
| D10 | 正式预期冻结怎样处理证据截止时间、已看探索样本与正式反例样本？ | 避免事后调整预期导致循环论证 | 记录已看证据与版本，待制定冻结/对照准入策略 |
| D11 | 参数标定的试验预算、允许变化的参数、正式候选实例接受权，是否授权实际重算？ | 关系到业务与计算风险 | 可以做代码/公式层面的低成本可行性调查，未经授权不大规模重算 |
| D12 | 语义复核是否必须独立 Pro？同一 Pro 同时管理/执行时怎样满足创建者与接受者分离？ | 决定人工成本与真实性 | 先留独立复核任务接口，不以自评直接接收 |
| D13 | 各专业 Skill 当前均是候选/草稿，哪些允许在试用范围使用？ | 不能把测试通过等同正式发布 | 将试用环境和验收结果分离，记录成熟度 |
| D14 | 当前哪些补证或实现修正应由本控制面内部完成，哪些属于新业务任务？ | 防止诊断跨越观察材料/合理性分析授权 | 默认：低成本合法补证内部；正式实现修改/需求迭代只提出交接申请 |

所有 D 项应在 `10_OPEN_DECISIONS_AND_CHANGELOG.md` 中按 `proposed / approved / rejected / deferred` 记录决定主体、时间、版本和影响；不能把表中“建议”直接视为已批准。

## 11. 非目标与停止规则

- 不移动、合并、重写当前两包专业 Skill，也不采纳 `observe-iterate` 其它历史目录的架构。
- 不复制旧长程协议中的 R/W 运输；不新建第二套跨端消息系统；不让 Codex 主控承担专业 Gate 判断。
- 不重建 CAEGraph/uplot/FeatDFProcessor 专业方法；控制面检查材料资格和授权，不能代替专业取数。
- 不将材料准备、预期推导、证据对照、诊断、标定压成一个线性大 Skill；保持事实轨道与业务判断轨道、合理性分析内部循环。
- 不把 Skill 自检、模型 confidence、GitHub Markdown 自写 `ACCEPTED` 当正式采纳，也不把模型扮演两种角色当独立复核。
- 不在版本未锁定、权限缺失、mandatory 验收未执行或有未知外部效果时继续正式提交或高风险自动动作。
- 不先开发通用 DSL、微服务集群、自动 Skill 市场、全局智能路由器，亦不为了轻量化删掉本业务必要的强制门禁。

## 12. 交付/变更管控

本计划对应一轮**先确认设计、再实施**的流程：

1. 先交完整源矩阵、A/B/C 合同、文件组织、待裁事项和测试方案供审阅；审阅后冻结 V0.1 基线。
2. 每个 W 包开始时以冻结基线为依据；发现必要新增/冲突，出具 `ChangeProposal`：原计划条款、实际问题、建议变更、备选方案、影响范围、需谁批准。
3. 未获批准不得以“顺手优化”为由重写阶段、合并/新增 Skill、修改已有验收标准、放宽权限或改变完成定义；不妨碍在授权内作低风险局部技术选择。
4. 每个 W 包结束提供：准确 Git commit/path（如实际提交）、代码与版本、测试 PASS/FAIL/NOT_RUN、实际运行证据、限制与残余风险、下一包进入条件。若未提交仓库，不报假 SHA。
5. 第一轮上线判断以至少一条真实材料准备→正式交接→合理性分析→定向补证→返回分析的闭环和负向门禁实际阻断为核心；调参分支可单列能力验收，但不能声称已完成未经授权的真实标定。

