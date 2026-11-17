# D003｜EAW P1 冻结 v1 限域正式证据对照

## 0. 正式身份

- `run_id`：`OI-EAW-P1-20261116-01`
- `delegation_id`：`D003`
- `issuer_call_id`：`C0007`
- `issuer`：`chatgpt:OI-EAW-P1-20261116-01:manager`
- `recipient`：`chatgpt:OI-EAW-P1-20261116-01:executor:E1`
- `return_to`：`chatgpt:OI-EAW-P1-20261116-01:manager`
- `work_item_id`：`WI-D003-P1-FORMAL-COMPARISON`
- `stage_instance_id`：`R-P1-COMPARISON-001`
- `analysis_round_id`：`AR-P1-001`
- `frozen_expectation_set_id`：`FZ-EAW-P1-AR-P1-001`
- 专业节点：`R06 / R2 正式证据对照`

本 D 只有在主控真实派发并核实原独立 E1 物理接收后才开始。它不是 D001/D002 返工，不是新补证 D，不修改 frozen v1，也不预设 `G-COMPARISON` 结果。

## 1. 当前业务问题

### Q-EAW-P1-REASONABLENESS-001

在 `FZ-EAW-P1-AR-P1-001` 已冻结的 12 条业务预期与 14 个场景下，将当前冻结 Project Source、D001/D002 已接受事实和真实限制正式绑定，逐条形成：

```text
SUPPORTS
COUNTERS
MISSING
AMBIGUOUS
NOT_APPLICABLE
PENDING
```

本 D 的目标不是强行证明八类产品合理或不合理，而是给出当前证据真正允许的正式结果、适用边界与未决原因。

### Q-EAW-P1-BOUNDARY-001

把已证明不可得、局部可用、含义不清和方法 anti-gold 转成问题级正式证据状态，区分：

- 当前冻结源已经能够回答的内容；
- 只能限域回答的内容；
- 当前源下正式 `MISSING` 的内容；
- 真正值得进入 R3 的业务偏差；
- 只应作为未来需求／实现候选而非本轮诊断的问题。

## 2. 已接受上游 Gate 与本 D 的准确位置

1. D001 WorkQuality 已接受；M 步骤 1～7 和 R0/R1 不重做。
2. H1 已 `ACCEPTED_WITH_LIMITS`。
3. `FZ-EAW-P1-AR-P1-001` 已冻结并保持不可无痕修改。
4. D002 WorkQuality 已接受；H2 已 `ACCEPTED_WITH_PRODUCT_AND_PURPOSE_LIMITS`。
5. R05 EvidencePreflight 已接受。
6. 完整八产品 integrated business-effect comparison 仍不具无条件输入资格。
7. manager 已批准本 D 的**限域正式 R06**：允许以 `MISSING/AMBIGUOUS/...` 形成正式结果；不允许把输入缺口偷换成业务 `COUNTERS`。
8. `G-COMPARISON = NOT_RUN`；只有本 D 回交并经 manager 验收后才能判断。

管理依据：

- `daowei2026/observe-iterate@df0fa015e6b9b7e6d1174b308c1519ddcca2fd8b:longrun/runs/OI-EAW-P1-20261116-01/calls/C0007/MANAGER_REPORT.md`
- `daowei2026/observe-iterate@22861d672b0ead9a78c75faa4111b4985af6cd89:longrun/runs/OI-EAW-P1-20261116-01/business_control/decisions/MD-0003.md`

## 3. 必须亲自使用的固定输入

### 3.1 冻结比较合同

- `daowei2026/observe-iterate@c88c4836269e8412e88e9ea6e7e871c0ad44f96e:longrun/runs/OI-EAW-P1-20261116-01/business_control/frozen_expectations/FZ-EAW-P1-AR-P1-001.yaml`
- 原命题文本、适用条件、反例与场景：
  `daowei2026/observe-iterate@0fff57bcc2cb85907586704a67389c038cf5ffa3:longrun/runs/OI-EAW-P1-20261116-01/calls/C0003/D001_EXPECTATION_REGISTER.yaml`

必须比较的 12 条冻结预期：

```text
E-OWN-WALL-001..004
E-BIZ-P1-001..008
```

必须覆盖的 14 个场景：

```text
S-WALL-001
S-DECOUPLE-002
S-SWITCH-003
S-DIRECTION-004
S-DORMANT-005
S-ATTACK-006
S-F4-007
S-F3F4-008
S-MISSING-009
S-GRAPH-010
S-SCOPE-011
S-REPLAY-012
S-ABSORB-013
S-TIME-014
```

`E-IMP-DATA-001..004` 不是冻结业务预期；它们可以作为 DataBinding／实现事实引用，不得被计入业务预期的支持票。

### 3.2 D001 已接受成果

- `daowei2026/observe-iterate@3d3b3b9c568f9b17037b747fc1ca44a76f847ddf:longrun/runs/OI-EAW-P1-20261116-01/calls/C0003/EXECUTOR_REPORT.md`
- `daowei2026/observe-iterate@624dd0dfb2deed97bf57c573ccbd63f9f636b6d7:longrun/runs/OI-EAW-P1-20261116-01/calls/C0003/D001_DATA_AUDIT.json`

### 3.3 D002 已接受成果

- `daowei2026/observe-iterate@03515f51c397650f11a1df4c01f8f623ec5d9479:longrun/runs/OI-EAW-P1-20261116-01/calls/C0006/D002_EVIDENCE_RETURN.md`
- `daowei2026/observe-iterate@242a60e2d2b0b3320a753f1db6f5c7c6282051d6:longrun/runs/OI-EAW-P1-20261116-01/calls/C0006/D002_EVIDENCE_AUDIT.json`
- `daowei2026/observe-iterate@750084b1d4bf177d0bb71e743655ab95b3b81ee2:longrun/runs/OI-EAW-P1-20261116-01/calls/C0006/D002_R2_PREFLIGHT.yaml`
- `daowei2026/observe-iterate@6bc4808db0fbb631f5a345dcfb55e6087f0013bf:longrun/runs/OI-EAW-P1-20261116-01/calls/C0006/D002_REVIEW_ONLY_AUDIT_BUNDLE.zip`

D002 的 `PARTIAL/PROVEN_UNAVAILABLE/ELIGIBLE` 是 preflight 状态，不可直接复制成 R2 业务证据状态；必须按本 D 的映射规则正式判断。

### 3.4 固定专业方法

采用 `daowei2026/observe-iterate@7e240b650b6ba6274b0263e34f5b0616a9a8ff1c`：

- `control/03_L1_合理性分析流程.md`
- `control/04_L2_节点输入输出登记表.md`
- `control/05_三级Gate及后继路由.md`
- `skills/reasonableness-analysis/business-evidence-comparison/SKILL.md`
- `longrun/professional/PRO_EXECUTOR_GUIDE.md`

## 4. 正式证据状态的使用规则

### 4.1 `SUPPORTS`

只有同时满足以下条件才可使用：

- 冻结命题的适用条件成立；
- evidence item 数据有效；
- 业务含义清楚；
- 对当前判断目的适用；
- 替代解释未占主导；
- actual/confirm/time/version 足以支持该判断。

“有一张图”“有同名字段”“current code 有合同”本身不足以形成 frozen product 的 `SUPPORTS`。

### 4.2 `COUNTERS`

只有在适用条件成立、证据充分，且明显的数据、导出阶段、身份、时间和实现问题已被排除时使用。

以下不得写成业务 `COUNTERS`：

- 缺 product/field/receipt；
- Attack timestamp binding 异常；
- canonical F4 不存在；
- direct Formation/Barrier/F3 不存在；
- Absorb level 或 typed identity 缺失；
- graph glyph 与 product contract 不一致；
- current producer 与 frozen source 无 receipt 绑定。

它们应分别进入 `InputAssessment`、`MISSING` 或 `AMBIGUOUS`。

### 4.3 `MISSING`

D002 已有据证明以下正式证据在当前冻结源不可得时，必须正式登记 `MISSING`，不再循环补查：

- P1RunManifest、source_run_ref、frozen receipt 和完整 replay/correction fixture；
- corrected complete AttackSegment、`closed_at` 和权威 TimeBasisContract；
- canonical public F4 union；
- frozen direct FormationEvidence、WallRelationBarrier、F3 artifact；
- 完整 availability/missingness；
- Absorb milestone `level` 与 run-scoped typed identity。

### 4.4 `AMBIGUOUS`

同一真实证据存在多个仍合理的解释、当前材料不能区分时使用。例如：

- Absorb resolve-only 是 quote-track termination 还是正式 interaction 边界；
- 同 UTI milestone 在 frozen product 中缺 level 后的业务身份；
- local ID join 能定位但不能建立 run-scoped typed identity。

### 4.5 `NOT_APPLICABLE / PENDING`

只有场景确实不满足适用条件或业务过程尚未确认结束时使用。不得用来掩盖缺产品、缺历史或数据不可得。

## 5. 八产品正式对照边界

八类产品全部保留：

| 产品 | 本 D 可以做什么 | 本 D 不能做什么 |
|---|---|---|
| Wall | 对生命周期形态、identity continuity 的局部 evidence item 正式判断；记录 provenance/reason/time/missingness 缺口 | 把 display segment 当独立 source occurrence，或泛化到完整生产合同 |
| Build | 对 Start/Milestone/Stop 形态和 local Wall join 建链；缺参数、milestone/stop 语义处登记状态 | 从行数、图样推断 threshold identity 或 producer 合理性 |
| AttackSegment | 正式记录现有 artifact 的时间/字段有效性和所需产品 `MISSING` | 比较 business_end 与 closed_at 的产品效果，或自行生成 corrected export |
| Absorb | 对生命周期行、multiplicity、resolve-only、zero-wall 建证据链 | 多票计数等价 payload、补造 milestone level、把 quote track 当 interaction |
| F4 | 对两 lane overlap 和 anti-double-counting 建材料事实 | 把 review-only union 当 canonical occurrence，或只留 max grade |
| FormationEvidence | 登记 frozen direct product `MISSING`，并引用 current contract 说明不能用 latent row 替代 | 从 Attack/F4 字段重命名生成产品 |
| WallRelationBarrier | 登记 frozen direct product `MISSING`，并保留 Wall.End 与 migration glyph 的边界 | 从 color/glyph/table order 造 Barrier |
| F3 | 登记 direct artifact `MISSING`，保留 current transient-only 事实 | 用 legacy Thick/Dense/Fight 或每 UTI 行替代正式 F3 |

## 6. 场景选择与证据链

不需要重新看遍所有数据。优先复用 D001/D002 已定位场景和确定性审计：

- `tick_000023 / i / wall_id=57427`：Wall lifecycle；
- `tick_000023 / i` 的 local Wall/Build/Attack/Absorb joins：decoupling；
- `wall_id=57428 -> 57429 / UTI=78266350`：switch/migration；
- `track_id=454496 / UTI=78266204`：Absorb same-UTI milestone；
- Attack 17,856 行及 10,115 mismatch、5 个 session boundary case；
- F4 37,846 overlap、25,116 grade difference；
- 全包 object/window/availability/replay 缺口。

每个 evidence item 至少记录：

```text
evidence_id
expectation_id / version
scenario_id
product
data/source ref
object/location
actual_time / confirm_time（可得时）
validity
business meaning
purpose suitability
formal status
observation
interpretation
alternative explanations
data quality
applicability boundary
```

若 actual/confirm/version 不可得，直接作为 `MISSING` 字段记录，不得猜测。

## 7. 同源证据与阶段边界

必须执行以下去重和边界：

- window snapshot 与 source frame 是同 lineage；
- `wall_segments` 是 Wall lifecycle 的显示派生；
- tactical/structural F4 overlap 是同一 half-second material；
- review-only union 派生自两 lane，不是独立 source，也不是产品；
- current TIS/FRP 只证明 current implementation contract，不证明 frozen run 参数或输出；
- graph/legend/glyph 只可定位和解释，不替代 source product；
- local IDs 只能在明确 symbol/package scope 内使用，不升级为跨 run identity。

## 8. 结果组织

### 8.1 `InputAssessment`

必须分别给出：

```text
DataValidityFinding
InputMeaningFinding
PurposeSuitabilityFinding
```

并按产品说明可用范围、不可用范围和来源版本。

### 8.2 `EvidenceComparisonPackage`

对 12 条冻结预期逐条形成正式 package；每条可以包含多条不同状态的 evidence item，但必须给出一个有依据的当前 judgment 和适用边界。

禁止：

- 用一个总分替代 12 条判断；
- 把多个 `MISSING` 机械汇总成“产品不合理”；
- 把同源派生重复计票；
- 因证据不足而省略冻结预期。

### 8.3 `ScenarioEffectTable`

对 14 个场景逐项记录：

- 场景适用性；
- 支持／反证／缺失／歧义／未决位置；
- 当前可回答和不可回答的问题；
- 产品和证据依赖；
- 下一动作。

### 8.4 `EvidenceInducedCandidates`

至少保留 D002 的三项候选及其来源，不修改 frozen v1。新发现只有在真正超出现有命题时才新增，不能把输入问题换名包装成新业务预期。

### 8.5 `DiscrepancyQueue`

只加入值得进入 R3 的**业务偏差**：

- 业务影响大；
- 可重复；
- 不能由数据质量／产品不可得解释；
- 有明确可追踪处理阶段；
- 区分原因有现实价值。

若没有满足条件的偏差，返回空队列并说明依据；不要为了产生后继而硬建诊断项。

## 9. Artifact conformance、材料方法与业务合理性必须分开

每个重要发现明确属于以下哪一层：

1. `ARTIFACT_CONFORMANCE`：当前 frozen export 是否满足字段、时间、identity、availability 合同；
2. `MATERIAL_METHOD`：图、窗口、派生视图是否适合承担证据；
3. `BUSINESS_REASONABLENESS`：正式产品行为是否支持或反驳冻结业务预期。

例如：

- Attack timestamp mixed binding 是 `ARTIFACT_CONFORMANCE`；
- 图层不能替代 occurrence 是 `MATERIAL_METHOD`；
- 只有在正式产品身份和语义合格后，产品行为才进入 `BUSINESS_REASONABLENESS`。

不得跨层偷换。

## 10. Worker、工具与写面

D003 预期零 W 完成。你已能直接读取固定 Project Source 和 GitHub 原件；本 D 不要求新数据生产。

若出现未预期、确需 Linux-only 的小范围只读事实动作，你可以在本 D 内签 W，但必须：

- 只限 `/dwdhome/fy/BASE_E6_2`；
- 主控先核本 Run 专用 Worker 的真实物理 thread、cwd、授权和文件可达；
- 不修改业务源码，不宽泛重算，不生成新正式产品；
- Worker Return 先回 E1，由 E1 专业消费后再回 manager。

不得为已证明不存在的产物补造 W；不得把 executor 自写派生物升级为 producer authority。

## 11. 明确非目标和停止点

本 D 不做：

- D001/D002 返工；
- 新的 H2 补证循环；
- 修改 frozen v1；
- R3 根因诊断；
- R4 参数标定；
- 新 producer export、canonical F4、corrected Attack、F3 artifact；
- 业务源码修改或上游重算；
- CAEGraph 新设计；
- P2/P3/P4；
- 最终策略或资金动作；
- 父任务完成判断。

如一个 evidence item 需要上述动作才能判断，当前结果即为 `MISSING` 或准确的 `AMBIGUOUS`，并记录未来解除条件；不要越界执行。

## 12. 预期交付物

1. `D003_EVIDENCE_COMPARISON.md`：完整专业叙事报告；
2. `D003_EVIDENCE_COMPARISON.yaml`：机器可读统一包，至少包含：
   - `input_assessment`
   - `expectation_packages`（12 条）
   - `scenario_effect_table`（14 个）
   - `evidence_induced_candidates`
   - `discrepancy_queue`
   - `product_result_summary`
   - `question_boundary_summary`
3. 如使用 Worker：正式 W、Worker Return、E1 接受意见；
4. 符合 V2 的 executor `PRO_RETURN.json`。

可以在统一 YAML 内承载 Skill 原生子结果，不要求为了文件数量机械拆分；但不能遗漏任何一类输出。

## 13. 完成条件与正式回交

D003 专业范围完成需要：

- 12 条冻结预期全部有正式 evidence package；
- 14 个场景全部有正式 effect/status 记录；
- 八类产品全部出现在 product summary；
- 三层 InputAssessment 完整；
- 每个 `COUNTERS`（如有）明确排除数据/实现缺陷解释；
- 每个 `MISSING/AMBIGUOUS` 有准确缺项、调查来源和解除条件；
- 同源证据未重复计票；
- EIC 与 frozen v1 分离；
- DiscrepancyQueue 只含值得诊断项，允许为空；
- 明确哪些业务问题已回答、哪些只能限域、哪些仍未决。

回交顺序：

1. 先发布专业报告和机器包；
2. 再发布 executor V2 Return；
3. `delegation_ref` 引用 D003 `DELEGATION.json` 精确 commit/path；
4. `return_to=chatgpt:OI-EAW-P1-20261116-01:manager`；
5. D003 报告范围完成可使用 `REPORTED_COMPLETE`，即使结果主要为 `MISSING/AMBIGUOUS`；
6. 完成态 `remaining_scope_ref=null`、`continuation_ref=null`，manager 后继不是 E1 剩余范围；
7. 不新增旧 ROLE_RETURN/FPA 字段；
8. 回报准确 commit 和路径。

D003 的 `REPORTED_COMPLETE` 不表示 `G-COMPARISON` 已通过、R3/R5 已完成或父任务完成。