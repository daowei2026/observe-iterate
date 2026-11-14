# D001｜EawP1WallLifecycleFrp 真实资产绑定、材料计划与最小预期基线

## 0. 运输身份

- `run_id`：`OI-EAW-WALL-20261114-01`
- `delegation_id`：`D001`
- `issuer_call_id`：`C0002`
- `issuer`：`chatgpt:OI-EAW-WALL-20261114-01:manager`
- `recipient`：`chatgpt:OI-EAW-WALL-20261114-01:executor:E1`
- `return_to`：`chatgpt:OI-EAW-WALL-20261114-01:manager`
- 父任务：对 `EawP1WallLifecycleFrp` 开展观察材料准备和业务合理性分析。
- 本 D 的管理决定：`daowei2026/observe-iterate@0dd8a0cb3e243fa6915d07523a17ca5feaca13d3:longrun/runs/OI-EAW-WALL-20261114-01/business_control/decisions/MD-C0001-001.md`
- 被替代的未派发候选：
  - `daowei2026/observe-iterate@27b8ca60903cfd722f875d7b40edcc887a96abac:longrun/runs/OI-EAW-WALL-20261114-01/delegations/D001/DELEGATION.md`
  - `daowei2026/observe-iterate@7b3b75d2f03b520b62a3fecfead1a978c3bb91ae:longrun/runs/OI-EAW-WALL-20261114-01/delegations/D001/DELEGATION.json`

本修订由 C0002 对同一未派发 `D001` 重签，是当前唯一可派发版本；C0001 所签旧版本仅保留为精确历史，不得再派发。除运输身份一致性修复外，D001 的专业目标、输入、产出、接收标准和权限边界均不改变。

本 D 是正式专业子任务，不是测试。executor 对本 D 的专业方法选择、事实核对、Worker 结果审查和交付质量负责；不得把本 D 继续扩为新的父任务。

## 1. 当前业务问题和 Workflow 位置

本 D 同时服务以下三个问题，但只完成它们的**事实/材料/预期基线**，不提前给最终合理性结论：

1. `Q-WALL-IDENTITY-LIFECYCLE`：真实 run-local Wall 身份及 Start、BandUpdate、Present↔Dormant、End、重复/冲突/非法/迟到变化如何对应。
2. `Q-WALL-PUBLICATION-STATE`：`wall_occurrences`、`wall_current_view`、`wall_diagnostics` 与 DSU active map 的真实关系，尤其 current-update、End 和整批事务语义。
3. `Q-WALL-BUSINESS-SUITABILITY`：这些语义是否适合“本次运行内维护上游认出的同一 Wall 生命周期”这一业务目的。

- `stage_view / control_nodes`：M 的 `S0/S1`（`M01～M04`）＋ R 的 `R0/R1`（`R01～R02`）。这是导航视图，不要求机械逐节点独立调用。
- `stage_instance_id`：`M-BASELINE-001`、`R-BASELINE-001`
- `work_item_id`：`WI-WALL-BASELINE-001`
- `analysis_round_id`：`AR-WALL-001`
- 当前消费者：manager 将据本 D 的真实成果决定 G-PLAN、是否需要最小 W/重算、是否具备预期冻结和后续正式对照资格。

## 2. 为什么现在做这项工作

当前只有需求、旧源码和历史运行线索；尚未核实 Linux 工作区的真实 checkout、代码/参数/数据/日历/读取入口、物化产物和可用时间范围，也没有本 Run 的真实材料包或冻结预期。直接对“合理/不合理”下结论会把实现事实循环解释为业务依据；直接全量重算则可能重复已有材料并触发旧报告中出现过的高成本。

本 D 要把两条轨道同时推进到可接续状态：

- **事实/材料轨道**：查清真实 tuple、已有资产和最小材料路径；
- **业务判断轨道**：把 Owner 目标、业务推导和实现行为分开，形成可支持、可反驳、允许未决的 WORKING 预期和场景。

## 3. 必须读取和采用的精确输入

### 3.1 运行与专业合同

- `daowei2026/observe-iterate@1e00424349ce8a5d72c9fccf74585d18630b62b8:longrun/runs/OI-EAW-WALL-20261114-01/BusinessTaskInput.md`
- `daowei2026/observe-iterate@ca7fdae84f65265332e3a53865724a2615508766:longrun/professional/PRO_EXECUTOR_GUIDE.md`
- `daowei2026/observe-iterate@ca7fdae84f65265332e3a53865724a2615508766:skills/observation-material-preparation/SKILL.md`
- `daowei2026/observe-iterate@ca7fdae84f65265332e3a53865724a2615508766:skills/reasonableness-analysis/README.md`
- `daowei2026/observe-iterate@ca7fdae84f65265332e3a53865724a2615508766:skills/reasonableness-analysis/business-expectation-derivation/SKILL.md`
- 只有实际进入正式证据映射或探索样本对账时，再采用：`daowei2026/observe-iterate@ca7fdae84f65265332e3a53865724a2615508766:skills/reasonableness-analysis/business-evidence-comparison/SKILL.md`

### 3.2 特征资料、需求和旧代码调查起点

- `daowei2026/observe-iterate@ca7fdae84f65265332e3a53865724a2615508766:task-inputs/eaw-p1-wall-lifecycle/FEATURE_CONTEXT.md`
- `daowei2026/feature-refinement-implementation-agent-evolution@8d58ddd3392a3e67ef5ba44adf2c4cd0c9077f9f:candidate_gold_cases/eaw/taskpacks_and_checkpoints/p1/EAW_P1_PREL0_BASE_PRODUCTS_ENGINEERING_DESIGN_AND_VCC_V1_6_1_20260818/01_EFFECTIVE_SCOPE_AND_REQUIREMENT_CORRECTIONS.md`
- `daowei2026/feature-refinement-implementation-agent-evolution@8d58ddd3392a3e67ef5ba44adf2c4cd0c9077f9f:candidate_gold_cases/eaw/taskpacks_and_checkpoints/p1/EAW_P1_PREL0_BASE_PRODUCTS_ENGINEERING_DESIGN_AND_VCC_V1_6_1_20260818/02_FINAL_P1_ARCHITECTURE.md`
- `daowei2026/feature-refinement-implementation-agent-evolution@8d58ddd3392a3e67ef5ba44adf2c4cd0c9077f9f:candidate_gold_cases/eaw/taskpacks_and_checkpoints/p1/EAW_P1_PREL0_BASE_PRODUCTS_ENGINEERING_DESIGN_AND_VCC_V1_6_1_20260818/dsu/P1-DSU-01_Wall_生命周期_DSU.md`
- `daowei2026/feature-refinement-implementation-agent-evolution@8d58ddd3392a3e67ef5ba44adf2c4cd0c9077f9f:candidate_gold_cases/eaw/taskpacks_and_checkpoints/p1/EAW_P1_PREL0_BASE_PRODUCTS_ENGINEERING_DESIGN_AND_VCC_V1_6_1_20260818/tables/PYTHON_PROJECTION_TABLES.csv`
- `daowei2026/tis@ef887396e0a06d6e75be47efee0f1985ad7988a3:frp/EawBattleP.py`
- `daowei2026/tis@ef887396e0a06d6e75be47efee0f1985ad7988a3:hf/prel0/wall_assembler.py`
- `daowei2026/frp@cac6c912dd65a14acbd591ca57e0afd8ddb4ef13:src/Frp/Instance/ISL/Eaw/P1.hs`
- `daowei2026/frp@cac6c912dd65a14acbd591ca57e0afd8ddb4ef13:src/Frp/Instance/ISL/Eaw/P1/WallLifecycle.hs`
- `daowei2026/frp@cac6c912dd65a14acbd591ca57e0afd8ddb4ef13:src/Frp/Instance/ISL/Eaw/P1/Products.hs`
- `daowei2026/frp@cac6c912dd65a14acbd591ca57e0afd8ddb4ef13:src/Frp/Instance/ISL/Eaw/P1/Publication.hs`
- `daowei2026/frp@cac6c912dd65a14acbd591ca57e0afd8ddb4ef13:src/Frp/Instance/ISL/Eaw/P1/FaoIngress.hs`

以上旧 SHA 是阅读基线，不是现役运行 tuple。实际工作区与其不一致时，以新查明事实为准，登记差异，不为保住 `FEATURE_CONTEXT` 的说法而改写事实。

## 4. 已知事实、候选解释和必须查明的未知项

### 已知起点

- 需求要求 run-local identity，不要求跨运行重认墙或 source correction。
- 旧实现区分 occurrence、current update 和 diagnostics；current writer 不是全量快照。
- 旧实现存在具名状态错误、重复 occurrence 处理、End 删除 active map、End current update，以及 firing 内事务式处理。
- TIS `Cache`/直接 `to_df` 限制与 FRP `Cal` 的角色表面不一致。

### 只能作为 `IMPLEMENTATION_DERIVED` 候选的判断

- 整批事务拒绝是否是当前正式运行行为及其业务影响；
- occurrence local number 是否在实际 receipt/stream 绑定下始终无歧义；
- End update 与 active-map 删除是否被下游/读取端正确解释；
- diagnostics 为空究竟表示没有异常、异常分支没出现、还是材料不可得。

### 本 D 必须查明或明确不可得

- `/dwdhome/fy/BASE_E6_2` 中实际 checkout/repo/ref/worktree，不能只报目录名；
- 真实 `EawP1WallLifecycleFrp` 配置、`WallAssembler` 参数、目标对象、日历、time range、source scope、schema/code version；
- generated wrapper、FrpDbaDao/DBA 或其他真实读取入口，以及 `Cache`/`Cal` 在该 tuple 中的含义；
- 已有物化目录、receipt、fields、三路结果、上游 sparse events/state trace 是否存在，分别覆盖什么范围；
- 是否已有可以直接复用的 CAEGraph/Notebook/纯数据；下游旧图不得冒充 Wall Lifecycle 已完成材料；
- 读取现成材料的预计成本与安全边界；若无材料，最小真实运行窗口、入口、内存/时间风险和前置条件。

## 5. 必做专业工作

### A. AssetAndBindingAssessment（M01 / R01）

1. 在实际 Linux BASE 中只读核实仓库和 worktree；记录 `git status`、分支/commit、相关文件是否存在及与旧 SHA 的差异。
2. 查现有物化数据、receipt/fields/manifest、三路 writer 输出和上游 WallAssembler 产物；记录精确路径、大小、对象/时间、生成版本和读取方式。不得只给五行预览或文件名。
3. 分开报告：源代码可读、生成包装存在、数据物化存在、数据可解码、数据适合本问题。任何一项不能由上一项自动推出。
4. 核实 `Cache`、`Cal`、OnlyRead、`to_df`、generated wrapper/FrpDbaDao 的实际组合；无法确定时列竞争解释和最小查证，不凭旧源码拼接结论。
5. 对历史报告或旧数据只判复用资格，不把“曾经成功”写成“当前可读”。

### B. ProcessingSkeleton（M02）

至少还原：

```text
WallAssembler receipt / sparse events / 必要 state trace
→ WallOccurrenceFao packed typed ingress 与 ingress diagnostics
→ WallLifecycleP 的 occurrence ledger、状态转移、active map、current update batch
→ wall_occurrences / wall_current_view / wall_diagnostics
→ 本轮用于解释的 band/core/price 等参照（只取必要项）
```

逐阶段列业务输入、实质状态变化、输出角色、actual/confirm/known time（如能确定）、身份、ValidEmpty/NoOccurrence/DataUnavailable/Pending/diagnostic 的区别。业务预期与实现事实分栏；不按函数个数机械拆材料。

### C. MaterialRequirementSet 与 MaterialPlan（M03/M04）

按“必需 / 有条件需要 / 可选 / 暂不准备”给出材料取舍。首轮至少评估：

- receipt/source scope/参数/版本；
- 上游 sparse event 与 occurrence 对账；
- `wall_occurrences`；
- `wall_current_view` update stream；
- `wall_diagnostics`；
- 能解释 current update 的完整 active map 或可替代 trace；
- 必要价格、band、core 背景；
- duplicate/conflict/invalid transition 的证据来源。

每项写明回答哪个 Q、来源、字段、时间角色、所需数据阶段、转换损失、现有/缺失、取得方式和成本。优先一个真实工作满足多个要求；不为每项材料完整重跑一遍。

若无现成真实材料，输出 `ActionPreflight`：最小窗口、目标对象、执行入口、上游是否会重算、预估数据量/内存/耗时、停止点及为何足以区分当前问题。**本 D 禁止自行启动全年或其他大范围重算。**

### D. WORKING 预期和场景（R02）

严格区分：

- `OWNER_EXPLICIT`：仅保留 Owner 目标原文及明确边界；
- `BUSINESS_INFERRED`：由“维护同一 Wall 生命周期”推导的候选预期；
- `IMPLEMENTATION_DERIVED`：需求/代码当前规定或实现的行为。

每条预期至少包含 statement、origin/source、适用/不适用条件、反例、证据需求、known unknowns、置信度、版本和状态。首轮使用 `AR-WALL-001 / EV-WALL-WORKING-v0.1`，默认状态 `WORKING`；**不得在本 D 中擅自标 `FROZEN_FOR_COMPARISON`，除非实际材料和场景边界足以提交 manager 作冻结 Gate。**

场景集至少覆盖：

1. Start Present；
2. Present 下 BandUpdate 且 presence 不变；
3. Present→Dormant；
4. Dormant 下 BandUpdate；
5. Dormant→Present；
6. Present 或 Dormant→End；
7. 完全重复 occurrence；
8. 同 ref 内容冲突；
9. update/end before start、start twice、Ended 后 update、band update 改 presence、非法 presence transition；
10. 同一 firing 内一条非法 occurrence 与其他合法 occurrence 并存；
11. NoOccurrence、ValidEmpty、DataUnavailable、InsufficientHistory、Pending 的可区别场景。

每个场景说明期望的 occurrence/current update/active map/diagnostics 关系和可反驳条件。没有真实样本的场景仍可作为后续材料需求，不能伪造出现过。

### E. 机会性小样本探索（仅在已有材料真实可用时）

- 优先取得一段含 Start 且至少包含一次非平凡更新、休眠/恢复或 End 的真实链；同时保留同一 Wall 身份、发生时间、ref、payload、三路输出和必要上游背景。
- 对 `wall_current_view` 按 update stream 解释，并在能取得时与完整 active map/trace 对账；不得把缺行填成状态不变的伪全量快照。
- 只输出 `ExploratoryFindings` 或材料事实；未冻结预期前不得标为正式 `SUPPORTS/COUNTERS`。
- 若 diagnostics 为空，只能报告所覆盖范围内未观察到诊断；不能证明错误分支正确。

## 6. 原生交付物及准确路径

所有 GitHub 成果只能发布到：

`longrun/runs/OI-EAW-WALL-20261114-01/delegations/D001/results/`

最低交付：

1. `D001_EXECUTOR_REPORT.md`：本 D 的专业总报告、采用的 Skill、Worker 消费情况、限制和准确后继；
2. `ASSET_AND_BINDING_ASSESSMENT.md`；
3. `PROCESSING_SKELETON_AND_MATERIAL_PLAN.md`；
4. `WORKING_EXPECTATIONS_AND_SCENARIOS.md`。

条件交付：

5. `MATERIAL_REVIEW.md`：只有实际取得或复用真实材料时产生；
6. `MATERIAL_MANIFEST.json`：材料文件、路径、大小/哈希、身份/时间/版本和 readiness；
7. `ACTION_PREFLIGHT.md`：需要真实重算但本 D 未获启动资格时产生；
8. `ADDITIONAL_EVIDENCE_REQUEST_CANDIDATE.md`：仅在确需跨 Workflow 的独立材料且当前 D 无法低成本查证时产生。

Linux 侧任何中间/导出只允许写入：

`/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D001/`

不得把敏感原始数据、凭据或未经允许的大文件提交 GitHub；GitHub 只登记允许发布的业务结果、manifest 和精确引用。

## 7. 接收标准与硬停止点

### 可接收完成

- 三份最低原生材料和 executor 报告均有精确来源，不把旧 SHA 当实际 tuple；
- 已有资产/缺口、处理骨架、材料必要性和取得路径能够逐项对应三个 Q；
- WORKING 预期来源、反例、证据和版本齐全；
- 若声称取得真实材料，能核对身份、时间、代码/参数/data binding、数据阶段、数量和读取路径；
- 清楚区分 `PLAN_READY / DATA_READY / PARTIAL_WITH_LIMITS / BLOCKED`；
- 给出 manager 可直接判断的下一步：复用材料、签 W/最小运行、返修计划、冻结预期或有界阻断。

### 部分交付

某些材料不可读或样本不含全部状态时，保留已验证部分，准确列出每个 Q 可继续/不能继续的范围、尝试记录和解除条件。不能因异常样本缺失而丢弃正常生命周期材料。

### 硬停止

- 即将触发上游大范围重算、全年加载、生产写入或越出 Owner/D 写面；
- 实际工作区不是授权 BASE，或发现共享写面冲突/无法证明单写者；
- 需要修改正式需求/现役实现、覆盖数据、访问凭据或改变 Owner 目的；
- 外部动作效果未知、真实执行可能已发生但无回执。此时先对账，禁止猜测重派。

失败、无结果、有效空和不可得均须返回证据与影响，不能只写“没找到”。

## 8. Worker 边界

executor 可零 Worker 完成本 D。只有需要真实命令、读取实际文件、导出或低成本最小运行时，才可在 Owner grant 与本 D 内签 W 给：

`codex:OI-EAW-WALL-20261114-01:worker:W1`

Worker 请求运行配置采用既有 Run 约定的 Linux BASE，并由主控在实际派发前核实请求模型配置 `GPT-6.1 Sol Max`、物理 thread、单写者和真实权限。executor 必须先发布 W，再在正式 Return 中引用；Worker 只交执行事实和实物，不能决定预期、材料必要性或业务合理性。Worker Return 必须回原 executor，由 executor 专业消费后才能交 manager。

允许的操作类别不超过 Owner 已给的：

- `wall-observation-work`：`linux:/dwdhome/fy/BASE_E6_2`，写面 `/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01`；
- `run-record-publish`：`github:daowei2026/observe-iterate:runs/OI-EAW-WALL-20261114-01`，写面 `longrun/runs/OI-EAW-WALL-20261114-01`。

## 9. 结果分流与回交

- **成功/可接收**：提交最低四项结果，必要条件项一并提交，说明哪些已达到 G-PLAN 候选、材料 readiness 和冻结候选资格。
- **部分**：提交合格子集、未满足项、对应问题和最小恢复动作；不得整包标完成。
- **需要 Worker**：先签合法 W，当前 executor Return 标 `IN_PROGRESS` 并引用 W；Worker 回来后由同一 executor 消费。
- **无法执行**：给出真实路径/权限/版本/成本阻断和独立可继续的专业成果；不得把局部阻断扩大为父任务停止。
- **发现新的业务问题**：登记 `FutureQuestionProposal` 或补证候选，不自动纳入本 D 必做。

最终正式 `EXECUTOR_RETURN` 必须引用真实结果原件、D001、已接受 Worker（如有）、剩余范围和准确续作；`REPORTED_COMPLETE` 只表示 D001 合同范围的专业报告完整，不代表三个 Q 或父任务已经完成。
