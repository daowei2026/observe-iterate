# D004｜EAW P1 R5 问题级分析交付与完成记录

## 0. 正式身份

- `run_id`：`OI-EAW-P1-20261116-01`
- `delegation_id`：`D004`
- `issuer_call_id`：`C0009`
- `issuer`：`chatgpt:OI-EAW-P1-20261116-01:manager`
- `recipient`：`chatgpt:OI-EAW-P1-20261116-01:executor:E1`
- `return_to`：`chatgpt:OI-EAW-P1-20261116-01:manager`
- `work_item_id`：`WI-D004-P1-ANALYSIS-DELIVERY`
- `stage_instance_id`：`R-P1-DELIVERY-001`
- `analysis_round_id`：`AR-P1-001`
- `frozen_expectation_set_id`：`FZ-EAW-P1-AR-P1-001`
- 专业节点：`R5 分析结果交接`

本 D 只有在主控真实派发并核实原独立 E1 物理接收后才开始。它不是新分析轮次，不是 D001/D002/D003 返工，不产生新证据，不预先宣布 `G-ANALYSIS-DELIVERY` 或 H3。

## 1. 当前业务目标

把已经被 manager 接受的 R0～R2 成果转成一份可由 L0/H3 消费的问题级正式交付：

1. 对四个 `question_id` 分别说明原本要求回答什么；
2. 当前实际回答到什么深度；
3. 哪些是正式 `SUPPORTS/AMBIGUOUS/MISSING`，哪些只是 artifact/material/scope 事实；
4. 哪些限制属于当前 frozen source 的合法终点；
5. 是否仍存在本 Run 必须执行的专业工作；
6. 哪些只是未来新输入、产品工程或新 expectation version 的提案；
7. 给 manager 提供 `G-ANALYSIS-DELIVERY/H3` 的完整判断输入。

本 D 不要求把缺失产品补齐，也不要求把所有结果修到合理。

## 2. 四个问题

### `Q-EAW-P1-COVERAGE-001`

现成 CAEGraph 脚本与 frozen Project Source 实际覆盖哪些 P1 产品、阶段、对象、时间尺度和字段？哪些可进入分析，哪些只能限域使用或有据不可得？

### `Q-EAW-P1-EXPECTATION-001`

针对本 Run 实际纳入的 P1 产品，Owner 原始设计、run-local 业务推导与实现事实分别形成哪些可检验预期和场景？怎样保持来源、版本和永久 Owner 接受边界？

### `Q-EAW-P1-REASONABLENESS-001`

在 frozen v1 与合格证据下，12 条预期、14 场景和八产品分别得到哪些正式支持、反证、缺失、歧义、不适用或未决结果？

### `Q-EAW-P1-BOUNDARY-001`

哪些问题已经形成当前 Run 的业务交付，哪些只能限域回答，哪些因正式证据缺失而不能回答，哪些需要 R3/R4，哪些只属于未来新产品／新数据／新版本提案？

## 3. 已接受的上游 Gate 和结果

1. H0：`ACCEPT_FOR_BOUNDED_WORK`。
2. D001 WorkQuality：`ACCEPTED`；H1：`ACCEPTED_WITH_LIMITS`。
3. `FZ-EAW-P1-AR-P1-001`：`FROZEN_FOR_COMPARISON`，只作本 Run working comparison contract，不表示永久 Owner 接受。
4. D002 WorkQuality：`ACCEPTED`；H2：`ACCEPTED_WITH_PRODUCT_AND_PURPOSE_LIMITS`；R05：`ACCEPTED`。
5. D003 WorkQuality：`ACCEPTED`。
6. `G-COMPARISON = PASSED_WITH_BOUNDED_RESULTS`。
7. R3：`NOT_TRIGGERED`；R4：`NOT_APPLICABLE_FOR_AR-P1-001`。
8. 父任务尚未关闭；R5 与 manager 的 `G-ANALYSIS-DELIVERY/H3` 尚未完成。

管理依据：

- `daowei2026/observe-iterate@690d94c4c87d1a271486bbef3912fe957fc1a7cb:longrun/runs/OI-EAW-P1-20261116-01/calls/C0009/MANAGER_REPORT.md`
- `daowei2026/observe-iterate@ea0697f436e7986a5c4b996a532f09be7013252b:longrun/runs/OI-EAW-P1-20261116-01/business_control/decisions/MD-0004.md`

## 4. 必须亲自使用的固定输入

### 4.1 任务、Owner 和冻结合同

- `daowei2026/observe-iterate@6a2d0abd34d44fd20fe7119035a8227e6b019625:longrun/runs/OI-EAW-P1-20261116-01/OWNER_START.md`
- `daowei2026/observe-iterate@1a04ea440f395026491036d405d82e653a5fecbd:longrun/runs/OI-EAW-P1-20261116-01/RUN_BINDING.json`
- `daowei2026/observe-iterate@c88c4836269e8412e88e9ea6e7e871c0ad44f96e:longrun/runs/OI-EAW-P1-20261116-01/business_control/frozen_expectations/FZ-EAW-P1-AR-P1-001.yaml`
- `daowei2026/observe-iterate@0fff57bcc2cb85907586704a67389c038cf5ffa3:longrun/runs/OI-EAW-P1-20261116-01/calls/C0003/D001_EXPECTATION_REGISTER.yaml`

### 4.2 D001、D002、D003 原生专业成果

- D001：
  - `daowei2026/observe-iterate@3d3b3b9c568f9b17037b747fc1ca44a76f847ddf:longrun/runs/OI-EAW-P1-20261116-01/calls/C0003/EXECUTOR_REPORT.md`
  - `daowei2026/observe-iterate@624dd0dfb2deed97bf57c573ccbd63f9f636b6d7:longrun/runs/OI-EAW-P1-20261116-01/calls/C0003/D001_DATA_AUDIT.json`
- D002：
  - `daowei2026/observe-iterate@03515f51c397650f11a1df4c01f8f623ec5d9479:longrun/runs/OI-EAW-P1-20261116-01/calls/C0006/D002_EVIDENCE_RETURN.md`
  - `daowei2026/observe-iterate@242a60e2d2b0b3320a753f1db6f5c7c6282051d6:longrun/runs/OI-EAW-P1-20261116-01/calls/C0006/D002_EVIDENCE_AUDIT.json`
  - `daowei2026/observe-iterate@750084b1d4bf177d0bb71e743655ab95b3b81ee2:longrun/runs/OI-EAW-P1-20261116-01/calls/C0006/D002_R2_PREFLIGHT.yaml`
- D003：
  - `daowei2026/observe-iterate@9a4e567fc90509b43ecce6e380870f0ddd6025ef:longrun/runs/OI-EAW-P1-20261116-01/calls/C0008/D003_EVIDENCE_COMPARISON.md`
  - `daowei2026/observe-iterate@2f6e8ba82581129c98f47992bbc0164194768a50:longrun/runs/OI-EAW-P1-20261116-01/calls/C0008/D003_EVIDENCE_COMPARISON.yaml`

不得用本 D 的摘要替换这些原生结果；统一封面必须引用而不是重写其证据细节。

### 4.3 固定专业方法

采用 `daowei2026/observe-iterate@7e240b650b6ba6274b0263e34f5b0616a9a8ff1c`：

- `control/01_L0_完整业务任务与双向衔接.md`
- `control/03_L1_合理性分析流程.md`
- `control/05_三级Gate及后继路由.md`
- `control/06_业务完成全景与更新协议.md`
- `longrun/professional/PRO_EXECUTOR_GUIDE.md`

## 5. `AnalysisDelivery` 要求

形成统一封面，但不把全部原生报告再复制一遍。至少包含：

```yaml
run_id
business_task_id
analysis_delivery_id
analysis_round_id
frozen_expectation_set_id
expected_outcome
actual_finding
covered_question_ids
covered_expectation_refs
used_material_refs
evidence_and_result_refs
product_result_summary
scenario_and_expectation_summary
r3_r4_evaluation
missing_or_limited
future_question_proposals
completion_evaluation
manager_gate_recommendation
```

### 5.1 必须保留的正式结果

```text
expectations: SUPPORTS 2 / AMBIGUOUS 4 / MISSING 6 / COUNTERS 0
scenarios:    SUPPORTS 3 / AMBIGUOUS 4 / MISSING 7 / COUNTERS 0
```

必须说明：

- 两条 expectation `SUPPORTS` 只限 Wall local lifecycle/identity；
- `S-GRAPH-010` 是 `MATERIAL_METHOD` anti-gold；
- `S-SCOPE-011` 是 applicability boundary；
- Build/Absorb 的歧义不是 partial support 或反证；
- Attack/F4/Formation/Barrier/F3 等 `MISSING` 不是产品错误；
- 没有正式业务 `COUNTERS`，也没有八产品整体合理/不合理总判定。

### 5.2 R3/R4

明确：

```text
R3 = NOT_TRIGGERED
R4 = NOT_APPLICABLE_FOR_AR-P1-001
```

原因必须引用 accepted D003 `DiscrepancyQueue=EMPTY` 及 manager MD-0004；不另做诊断或标定。

## 6. `QuestionCompletionRecord[]` 要求

为四个 question_id 各形成一条独立记录。每条至少包含：

```yaml
question_id
analysis_round_id
expectation_version_or_set
expected_outcome
actual_finding
accepted_result_refs
covered_scope
excluded_scope
missing_or_limited
completion_evaluation
remaining_mandatory_work_in_this_run
future_question_proposals
recommended_parent_task_effect
```

### 6.1 Q-COVERAGE

至少记录：

- 当前 frozen source 的产品、字段、阶段、时间、identity、availability 和材料用途已核至有据退出；
- Wall/Build/Attack/Absorb/F4-lanes 有不同程度直接材料；Formation/Barrier/F3 无 frozen direct product；
- future producer run / receipt-bound package 是新输入版本，不是本轮继续查找；
- 不得把“调查完成”写成“所有产品数据满足”。

### 6.2 Q-EXPECTATION

至少记录：

- frozen set v1、12 条预期、14 场景及来源边界；
- V0.6 是 run-local working comparison contract，不是永久 Owner 接受；
- `EIC-D002-001..003` 是 future candidate，未进入 v1；
- 当前 v1 是否满足本轮问题的完成定义。

### 6.3 Q-REASONABLENESS

至少记录：

- D003 正式状态全景与 G-COMPARISON；
- Wall local lifecycle 的限域支持；
- Build/Absorb 歧义；
- Attack/Formation/Barrier/F3/canonical F4/replay/missingness 的正式缺失；
- 0 个业务 `COUNTERS`；
- 不形成“P1 整体合理”或“不合理”的总判定；
- 本轮允许的有界未决是否已经成为合格结果。

### 6.4 Q-BOUNDARY

至少记录：

- 已回答、限域回答、因缺证未回答的清单；
- 为什么 R3 不触发、R4 不适用；
- future proposals 与本 Run mandatory work 的分离；
- 是否仍存在能在当前 frozen source 和原授权内合法推进、且属于原完成合同的必做工作。

## 7. Future proposals 的边界

允许列为未来独立提案：

- receipt-bound `P1RunManifest` / source_run / typed refs / complete availability；
- corrected authoritative Attack product 与 TimeBasisContract；
- canonical public F4 product；
- frozen FormationEvidence、WallRelationBarrier、F3 direct artifacts；
- receipt-bound Absorb level/typed identity；
- 对 `EIC-D002-001..003` 建新 expectation version 和新 evidence round。

必须明确这些不是 D004、不是当前 R5、也不是本 Run H3 前自动必做。不得写成“由于未来可继续，所以当前问题永远不完成”。

## 8. Manager Gate 建议

你可以给出：

```text
READY_FOR_MANAGER_G_ANALYSIS_DELIVERY_REVIEW
READY_FOR_MANAGER_H3_REVIEW
或
NOT_READY + 准确缺项
```

但不得自行宣布：

- `G-ANALYSIS-DELIVERY` 已通过；
- H3 已通过；
- 父任务已完成。

若认为当前仍缺本 Run 必做工作，必须指出具体 question、原完成合同、缺项和准确返回节点；不能仅因存在未来更完整数据的可能性而判未完成。

## 9. 工具、Worker 与写面

D004 预期且要求零 W：

```text
Worker Orders = 0
Worker Returns = 0
Linux reads/writes = 0
new data = 0
new product = 0
source changes = 0
```

所有必要原件均已在 GitHub 固定提交可读。D004 不授权 Linux 操作、源码修改、数据生产、上游重算、producer export 或新证据抽样。若发现真正输入身份不一致，停止并回报；不得自行签 W 绕过。

允许写入仅为本 Run GitHub 路径中的 R5 专业交付和 Return。

## 10. 明确非目标

本 D 不做：

- D001/D002/D003 返工；
- 新 H2 补证；
- 新 R1 预期版本；
- 新 R2 对照；
- R3 诊断；
- R4 标定；
- 修改 frozen v1；
- 生产 corrected Attack/canonical F4/Formation/Barrier/F3；
- 修改业务源码或原数据；
- Owner 永久需求决定；
- H3 manager 决定。

## 11. 预期交付物

1. `D004_ANALYSIS_DELIVERY.md`：人类可读统一问题级交付；
2. `D004_QUESTION_COMPLETION_RECORDS.yaml`：机器可读 `AnalysisDelivery` 与四条 `QuestionCompletionRecord`；
3. 符合 V2 的 executor `PRO_RETURN.json`；
4. 零 W，不存在 Worker Return。

## 12. 完成条件

D004 专业范围完成需要：

- 四个 question_id 均有独立 completion record；
- 每条记录绑定 `AR-P1-001` 和 frozen v1；
- 原生 D001/D002/D003 结果引用完整；
- 正式状态及其层次、产品、场景、对象/窗口限制准确；
- `G-COMPARISON` 与业务结果分开；
- R3/R4 不触发依据明确；
- future proposal 与 current mandatory work 分开；
- 给出可供 manager 独立判断的 `G-ANALYSIS-DELIVERY/H3` 建议；
- 没有新增业务结论、补证、诊断或实现动作。

## 13. 正式回交

1. 先发布 MD 和 YAML 专业交付；
2. 再发布 executor V2 Return；
3. `delegation_ref` 引用 D004 `DELEGATION.json` 精确 commit/path；
4. `return_to=chatgpt:OI-EAW-P1-20261116-01:manager`；
5. D004 合同范围完成可使用 `REPORTED_COMPLETE`；
6. 完成态 `remaining_scope_ref=null`、`continuation_ref=null`；
7. `issued_delegation_refs=[]`、`issued_order_refs=[]`、`accepted_worker_refs=[]`；
8. 不新增旧 ROLE_RETURN/FPA 字段；
9. 回报准确 commit 和路径。

D004 的 `REPORTED_COMPLETE` 只表示 R5 专业交付完整，不表示 manager Gate 或父任务已经通过。