# D002｜legacy 正常链正式对照与 current 高价值证据动作设计

## 0. 运输身份

- `run_id`：`OI-EAW-WALL-20261114-01`
- `delegation_id`：`D002`
- `issuer_call_id`：`C0005`
- `issuer`：`chatgpt:OI-EAW-WALL-20261114-01:manager`
- `recipient`：`chatgpt:OI-EAW-WALL-20261114-01:executor:E1`
- `return_to`：`chatgpt:OI-EAW-WALL-20261114-01:manager`
- 管理决定：`daowei2026/observe-iterate@9ce476e26079b10a5806a9a20fb63db1abe5d02d:longrun/runs/OI-EAW-WALL-20261114-01/business_control/decisions/MD-C0005-001.md`

本 D 是 D001 被接受后的下一项独立专业任务，不是 D001 返修，不重新扫描同一边界，也不把 D001 的 `PARTIAL_WITH_LIMITS` 改写为失败。

本 D 有两个互不互相阻断的 lane：

1. **R lane**：对已经冻结的 historical legacy normal-chain 子集开展正式证据对照；
2. **M/action-design lane**：把 current 高价值证据候选做成可以独立判定 G-RUN 的精确动作合同。

任一 lane 局部受阻，不得停止另一 lane 的合法工作。

## 1. 业务问题、阶段和工作实例

### 1.1 R lane

- `question_id`：
  - `Q-WALL-IDENTITY-LIFECYCLE`
  - `Q-WALL-PUBLICATION-STATE`
  - `Q-WALL-BUSINESS-SUITABILITY`（仅限 historical normal-chain 的局部适用性）
- `stage_instance_id`：`R-NORMAL-COMP-001`
- `work_item_id`：`WI-WALL-LEGACY-NORMAL-COMP-001`
- `analysis_round_id`：`AR-WALL-002`
- `stage_view / control_nodes`：R04 冻结版消费、R05 EvidencePreflight、R06 正式对照、R13 限域发现整理。
- 当前 Gate：`EV-WALL-LEGACY-NORMAL-v1.0` 已由 manager 冻结；`G-COMPARISON` 尚未通过，等待本 D 产生正式结果后由 manager 判断。

### 1.2 M/action-design lane

- `question_id`：三个原 Q，重点是 publication/state、terminal identity 和 transaction/replay 边界。
- `stage_instance_id`：`M-CURRENT-ACTION-001`
- `work_item_id`：`WI-WALL-CURRENT-ACTION-DESIGN-001`
- `stage_view / control_nodes`：M05 ActionPreflight 细化；不进入 M06/M07 实际运行。
- 当前 Gate：`G-PLAN=PASS_WITH_SCOPE`；`G-RUN=NOT PASSED`。

## 2. 必须采用的精确输入

### 2.1 任务与管理决定

- `daowei2026/observe-iterate@1e00424349ce8a5d72c9fccf74585d18630b62b8:longrun/runs/OI-EAW-WALL-20261114-01/BusinessTaskInput.md`
- `daowei2026/observe-iterate@9ce476e26079b10a5806a9a20fb63db1abe5d02d:longrun/runs/OI-EAW-WALL-20261114-01/business_control/decisions/MD-C0005-001.md`
- 专业与控制合同统一采用 `daowei2026/observe-iterate@ca7fdae84f65265332e3a53865724a2615508766`，尤其：
  - `longrun/professional/PRO_EXECUTOR_GUIDE.md`
  - `skills/reasonableness-analysis/business-evidence-comparison/SKILL.md`
  - `skills/reasonableness-analysis/business-expectation-derivation/SKILL.md`
  - `skills/observation-material-preparation/SKILL.md`
  - `control/02_L1_观察材料准备流程.md`
  - `control/03_L1_合理性分析流程.md`
  - `control/05_三级Gate及后继路由.md`

### 2.2 D001 正式结果

- E1 总报告：`daowei2026/observe-iterate@b03a3b43497fce8c10f9dd539a4f623225dce237:longrun/runs/OI-EAW-WALL-20261114-01/delegations/D001/results/D001_EXECUTOR_REPORT.md`
- 同一结果提交 `2b4d60f868ef715d12ba14131871227ba95517ea` 下：
  - `ASSET_AND_BINDING_ASSESSMENT.md`
  - `PROCESSING_SKELETON_AND_MATERIAL_PLAN.md`
  - `WORKING_EXPECTATIONS_AND_SCENARIOS.md`
  - `MATERIAL_REVIEW.md`
  - `MATERIAL_MANIFEST.json`
  - `ACTION_PREFLIGHT.md`
  - `ADDITIONAL_EVIDENCE_REQUEST_CANDIDATE.md`

D001 中 current/legacy、static/runtime、exploratory/formal 的限制全部继续有效。本 D 不允许用 current source HEAD 补写 legacy product generation version。

## 3. Lane A｜formal legacy normal-chain comparison

### 3.1 固定比较输入

冻结版本仅来自 `MD-C0005-001` 第 4 节：

```text
EV-WALL-LEGACY-NORMAL-v1.0
FN-IDENTITY-01
FN-START-01
FN-BAND-01
FN-END-01
```

固定解释规则：

- C 是 update/delta rows，不是 full snapshot；
- 缺行不填造成状态不变；
- legacy product generation version 仍缺；
- End 的 `0 + not_present` 不当真实价格 0；
- current source只作静态解释上下文；
- 本轮不用总体分数。

固定材料：`MATERIAL_MANIFEST.json` 所接受的 exact historical chain、source/upstream join 和必要 evidence refs。不能扩大到全年统计，也不能把 diagnostics 同 firing 为 0 解释为异常机制通过。

### 3.2 必做工作

1. **EvidencePreflight**
   - 逐项核 DataBinding、identity、time role、schema/version gap、read chain、evidence dependency、data quality 和目的适用性；
   - 明确哪些字段来自 upstream、legacy O、legacy C、D、current static source；
   - 任何无法证明的 actual/confirm/known role保持 `MISSING/AMBIGUOUS`。

2. **逐命题正式对照**
   - 对 `FN-IDENTITY-01 / FN-START-01 / FN-BAND-01 / FN-END-01` 分别给：
     `SUPPORTS / COUNTERS / MISSING / AMBIGUOUS / NOT_APPLICABLE / PENDING`；
   - 每项必须列直接证据、反证、缺失、替代解释、适用范围和不能推出什么；
   - 同一三行链和同一 upstream join 不得机械计成多份独立共证；
   - `COUNTERS` 是业务发现，不等于工作失败；样本只有一条链时必须保留覆盖限制。

3. **限域问题完成记录**
   - 为下列子问题给出 `QuestionCompletionRecord` 候选：
     - historical exact-artifact normal identity continuity；
     - historical Start/BandUpdate/End 的 O/C publication；
     - legacy normal-chain 对 current full suitability 的不可外推边界；
   - 明确它们是否已达到本轮限域结案，及为何不关闭三个原 Q。

4. **发现路由**
   - 若正式对照出现 `COUNTERS`，判断其是否值得进入诊断；不得自动修改冻结预期；
   - End measurement loss 继续作为 evidence-induced candidate，不因它已被观察而写成 frozen business defect；
   - 若证据只能支持局部命题，保留局部结果，不把整条链标成总体 PASS。

### 3.3 Lane A 禁止事项

- 不重新派 Worker 读取相同三行链；
- 不把 historical artifact 称为 current runtime；
- 不扩成 Dormant、duplicate、transaction 或 active-map 对照；
- 不无痕修改 `EV-WALL-LEGACY-NORMAL-v1.0`；
- 不宣布父任务完成。

## 4. Lane B｜current evidence action design

### 4.1 目标

把 D001 的 E1～E4 候选收束为两个互相独立、可由 manager 单独判定 G-RUN 的动作合同：

#### `ARUN-WALL-NORMAL-001`｜current normal O/C/A/D

最小区分对象：

```text
Start
→ two legal updates in one firing（若 current contract 可构造）
→ End
```

目标区分：current schema/native read、current update 与 active map、same-firing last update、Ended update + deletion、End measurement contract。

#### `ARUN-WALL-SCENARIO-001`｜controlled lifecycle semantics

优先场景：

1. End→update；
2. End→End；
3. End→Start same local no；
4. same-firing exact duplicate；
5. cross-firing exact duplicate；
6. same-ref different-payload；
7. one legal + one state-invalid same firing；
8. one legal + one decode-invalid same firing；
9. out-of-order UTI。

Dormant/恢复只在 producer/current contract 证明可达时纳入；不可达时提出 `NOT_APPLICABLE` 候选，不强造自然样本。

### 4.2 必做设计调查

1. 查明 current source tree 中是否已有无需修改生产代码的纯逻辑 test、fixture、replay 或 wall-only 入口；给精确文件、函数、build target 和依赖，不能用“应该可以”代替。
2. 查明 active map 在测试/运行中可观察的最小接口；producer trace 不得冒充 FRP active map。
3. 查明 current ADT、generated wrapper/native reader 的生成和读取入口；没有现成路径时，准确标为工程缺口，并说明需要哪一项独立建设，不能自行生成后宣称已就绪。
4. 对 legacy generation provenance，只允许使用已知 task linker、receipt、manifest 索引和精确路径作有界查询；没有新索引时不得重复无界扫描。
5. 查 firing formation contract、upstream ref uniqueness／localNo terminal invariant 的现有来源；找不到时列为动作前置，不用 current source 推测代替。

### 4.3 每个动作合同必须完整给出

- 所区分的 `question_id / expectation_id / scenario_id`；
- 动作类型：pure fixture、wall-only integration、deterministic replay 或其他；
- exact checkout/commit/dirty relevance；
- exact executable/build target/command template；
- target/calendar/source range/warmup/effective params（不适用时说明理由）；
- fixture 每条 ordered input、firing boundary、identity/ref/UTI；
- pre-state、post-state 和预期 O/C/A/D observation surface；
- current ADT/schema/wrapper/reader；
- build/cache/TMP/product/task-linker/log/migration 等全部写面；
- 输出目录、receipt、manifest、hash、command/exit/time/size；
- 成本 metadata、预计输入规模、内存、墙钟、文件数和 stop threshold；
- single-writer/lock/thread/model/effort 要求；
- Owner grant 和未来 manager G-RUN 的对应关系；
- 安全停止点、失败/UNKNOWN 处理和恢复入口。

动作合同必须使下一轮 manager 可以只看事实就选择：

```text
ELIGIBLE
ELIGIBLE_WITH_LIMITS
NEEDS_PRECONDITION
NOT_EXECUTABLE
```

若仍缺精确入口，不得写成 `ELIGIBLE`；应给最小工程缺项，而不是把同一问题再次交给“继续调查”。

### 4.4 Lane B 本 D 的执行边界

- **禁止实际 build、test、fixture execution、current material generation 或 native readback。**
- 禁止运行现有 multi-product integration runner。
- 禁止修改 TIS/FRP/frp-core/schema/wrapper。
- 允许低成本只读源码、已有 manifest/task-linker/fixture 索引核实。
- 需要 Linux 命令、真实文件核实或导出时，可由 E1 在本 D 内签新的 W；Worker 只做明确只读调查，不取得运行资格。
- 旧 W001 的锁、thread、模型或已通过事项不自动延续；任何新 W 仍须单独真实绑定、单写者和写面核验。

## 5. 原生交付物与准确路径

所有 GitHub 结果只能发布到：

`longrun/runs/OI-EAW-WALL-20261114-01/delegations/D002/results/`

最低交付：

1. `D002_EXECUTOR_REPORT.md`
2. `FORMAL_LEGACY_NORMAL_CHAIN_COMPARISON.md`
3. `QUESTION_COMPLETION_RECORDS.md`
4. `CURRENT_NORMAL_CHAIN_ACTION_DESIGN.md`
5. `CONTROLLED_SCENARIO_ACTION_DESIGN.md`
6. `ACTION_ELIGIBILITY_MATRIX.md`

条件交付：

7. `BOUNDED_PROVENANCE_RECOVERY_RESULT.md`——只有实际做了有界索引核实时产生；
8. `ADDITIONAL_ENGINEERING_PRECONDITION.md`——只有动作合同因缺现成入口而需要独立工程前置时产生；
9. `D002_MATERIAL_MANIFEST.json`——只有产生新的可交接事实材料时产生，不能复制 D001 manifest 冒充新材料。

Linux 中间文件若确需产生，只允许：

`/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D002/`

不得把大型原数据、凭据、cache 或未授权产物提交 GitHub。

## 6. 接收标准

### 6.1 R lane

- 严格使用 frozen v1.0，不改变命题；
- EvidencePreflight 和逐命题状态完整；
- source/current/legacy 与 evidence dependency 不混；
- 明确何种 historical 子问题可限域结案、何种不能；
- 不外推 current/full suitability。

### 6.2 M/action-design lane

- 两个动作合同分别完整、可审计、可停止；
- 精确区分“已有入口”“需建设前置”“不可执行”；
- 不把 command template 当执行事实；
- 写面和成本必须覆盖 build/cache/TMP/task/log 等间接副作用；
- manager 能据结果独立判断未来 G-RUN，而无需再次要求“继续细化”。

### 6.3 部分交付

某个动作合同因真实缺口不能闭合时：

- 保留 formal comparison 和另一动作的可用结果；
- 给出最小工程前置、受影响问题和解除条件；
- 不把整个 D 标成失败；
- 不因 action design 阻断 historical formal comparison。

## 7. Worker 边界

E1 可零 Worker 完成。若签 W：

- 只能签给 Binding 已有获准角色 `codex:OI-EAW-WALL-20261114-01:worker:W1`；
- 只允许 `wall-observation-work` 和 `run-record-publish` 的既有子集；
- Linux 工作区仍为 `/dwdhome/fy/BASE_E6_2`；
- Linux 写面只可为 `/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01`；
- GitHub 写面只可为 `longrun/runs/OI-EAW-WALL-20261114-01`；
- Worker Return 必须先回 E1，经 E1 专业消费后再回 manager；
- Worker 不决定冻结预期、正式比较结论、G-RUN 或父任务完成。

## 8. 结果分流与回交

- **Lane A 完成、Lane B action-ready**：回交逐命题正式结果、限域 completion records 和两个可判定动作合同；manager 决定 G-COMPARISON 和 G-RUN。
- **Lane A 完成、Lane B 需工程前置**：保留正式比较；给出唯一、最小、具名工程前置，不启动运行。
- **Lane A 出现正式 COUNTERS**：保留为业务发现并判断是否值得诊断；不回写冻结预期。
- **无法取得新的 provenance**：如实返回有界查询范围和 `MISSING`，不重复无界扫描。
- **需要 Worker**：先签 W，当前 D Return 按真实状态；Worker 回来后仍由同一 E1 消费。

最终 `EXECUTOR_RETURN` 必须引用 D002 原件、全部真实结果、已接受 Worker（如有）、remaining scope 和准确后继。D002 `REPORTED_COMPLETE` 只表示本 D 合同完整报告，不表示三个原 Q 或父任务完成。
