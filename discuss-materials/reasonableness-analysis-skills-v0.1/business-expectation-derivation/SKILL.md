---
name: business-expectation-derivation
description: 从 Owner 的业务意图、现有需求与实现事实中，推导可被真实数据支持或反驳的输入预期、局部场景预期和输出预期；适用于特征、策略、数据处理链与业务叙事的合理性分析。
version: 0.1.0
status: draft
---

# 业务预期推导与可观察化

## 1. 何时使用

在以下任务中使用本 Skill：

- Owner 给出业务目的，但没有把数据位置上的具体预期讲全；
- 需要分析某个输入特征、处理阶段或输出是否合理；
- 需要把口语化目的转成可由真实数据检验的陈述；
- 需要区分需求预期、AI 推导和代码行为；
- 需要为后续画图、数据处理、效果对照或偏差诊断定义“到底看什么”。

不用于：

- 单纯查字段、修数据格式或运行脚本；
- 在没有业务目的的情况下机械寻找异常；
- 未经证据与 Owner 决定，直接改需求、调参或修改实现。

---

## 2. 核心目标

将含糊的业务意图转化为：

```text
有来源
有适用条件
可被支持
可被反驳
允许未决
能够映射到真实数据
```

的预期命题。

本 Skill 不要求在看数据前一次性形成完整预期。它要求的是：

> 在作出正式“符合／不符合预期”判断前，至少冻结当前一轮的最小可检验预期；新证据产生的新想法必须进入下一版，而不是无痕改写旧预期。

---

## 3. 三种预期来源：必须显式区分

### 3.1 `OWNER_EXPLICIT`：Owner 明确给出的业务预期

例如：

> 希望保留能够覆盖重要拐头的高频。

这属于需求依据。AI 应忠实理解，不随意改写；若语义有多种可能解释，应保留原话并列出解释分支。

### 3.2 `BUSINESS_INFERRED`：由业务目的推导出的候选预期

例如：

> 如果某个拐头周围存在多个时间接近的高频，其中可能存在可以合并的冗余。

它可以很有价值，但不是 Owner 已确认需求。必须标注：

- 推导理由；
- 适用条件；
- 反例；
- 当前成熟度；
- 是否需要 Owner 决定。

### 3.3 `IMPLEMENTATION_DERIVED`：由现有算法或代码定义得到的实现预期

例如：

> 段内事件数量比例满足上下限时，该参数组会被选择；紧密组确认结束后才形成正式合并结果。

这类预期用于理解当前实现“实际上会做什么”，不能自动证明它“业务上就应该这样做”。

### 3.4 禁止的循环论证

禁止：

```text
代码这样实现
→ 所以业务上应该这样
→ 数据符合代码
→ 所以业务设计合理
```

正确做法：

```text
Owner 目的 / 业务推导 / 实现行为分别记录
→ 在真实数据中比较三者是否一致
→ 不一致时进入偏差诊断
```

---

## 4. 输入必须做三层检查

| 层次 | 具体问题 | 性质 |
|---|---|---|
| 输入有效性 | 数据是否缺失、错位、重复、使用了错误的时间或参数 | 数据质量与来源检查 |
| 输入业务合理性 | 当前输入呈现的现象，是否与它声称表达的业务概念相符 | 专业合理性分析 |
| 输入对当前目的的适用性 | 即使输入本身没有错，它是否足以支持本次业务目的 | 业务适用性判断 |

必须保留：

```text
输入不适合当前目的
≠
输入特征本身错误
```

例：Dense 可能正确表达成交活动，但未必足以单独承担“覆盖价格拐头”的目的。

---

## 5. 不确定性三分类与处理路由

| 不确定性来源 | 处理方式 |
|---|---|
| 缺少数据、字段含义或实现事实 | AI 优先自行查代码、补数据或做最小实验 |
| 可以通过真实样本、反例和进一步对照判断 | AI 继续分析，并给出有证据的候选结论 |
| 存在不同的业务目标取舍，无法仅靠数据确定 | 提交 Owner 决定 |

禁止把前两类问题过早抛给 Owner。

提交 Owner 时必须同时提供：

- 真实分歧场景；
- 两种或多种取舍分别保留什么、损失什么；
- 现有材料支持到哪；
- AI 已排除哪些技术或数据原因。

---

## 6. 渐进式执行，而不是一次写完完整预期

### 6.1 先建立最小可检验预期包

至少包括：

```text
BusinessIntent
JudgmentTarget
ExpectationStatement
ExpectationOrigin
ApplicableConditions
KnownUnknowns
FalsifierOrCounterEvidence
EvidenceNeeded
ExpectationVersion
```

有了这份最小包，就可以进入小样本探索。

### 6.2 小样本探索可以反哺预期

探索可以用于：

- 理解字段和时间语义；
- 找到有业务差异的场景；
- 发现原先遗漏的条件；
- 形成新的候选预期。

但不得把证据诱发的新预期伪装成事前已有预期。

### 6.3 进入正式对照前冻结

将当前版本标为：

```text
FROZEN_FOR_COMPARISON
```

后续若修订，创建新版本并保留：

```text
supersedesExpectationId
revisionReason
evidenceThatTriggeredRevision
```

---

## 7. 执行步骤

### 步骤 1：还原业务目的

回答：

- Owner 想改善或避免什么业务问题？
- 输出将用于观察、筛选、叙事、参数选择、实现还是策略？
- 当前明确不要求输出什么？
- 业务判断发生在什么对象、尺度、时间和参数范围？

输出：`BusinessIntentStatement`。

### 步骤 2：确定判断对象与处理链位置

区分：

```text
原始数据
输入特征
候选事件
选择结果
应用后的事件
中间组或状态
最终输出
后续效果
```

不能只写“这个特征是否合理”。

### 步骤 3：抽取 Owner 明确预期

保留原话、出处和适用范围。不要润色成比原文更强的结论。

### 步骤 4：推导业务候选预期

从以下问题推导：

- 为什么该输入有可能实现业务目的？
- 实现该目的至少需要哪些信息？
- 哪些条件下预期成立？
- 哪些反例会使预期不成立？
- 不同局部场景下是否应有不同输出？

所有推导均标为 `BUSINESS_INFERRED`。

### 步骤 5：抽取实现预期

从需求、代码、配置和运行规则中记录：

- 触发条件；
- 状态维护；
- 选择与应用；
- actualTime／confirmTime；
- Pending／Empty／Missing；
- 结束和重置；
- 参数版本。

所有此类预期均标为 `IMPLEMENTATION_DERIVED`。

### 步骤 6：执行输入三层检查

分别输出：

```text
InputValidityAssessment
InputBusinessReasonablenessAssessment
InputPurposeSuitabilityAssessment
```

三者不得压成一个“输入通过／不通过”。

### 步骤 7：形成场景矩阵

优先从四类变化构造场景：

1. 输入关键性质变化；
2. 多个输入之间关系变化；
3. 时间状态变化；
4. 与预期相反的反例。

每个场景至少写：

```text
ScenarioId
InputCondition
ExpectedBehavior
Why
Counterexample
EvidenceNeeded
ExpectationOrigin
```

### 步骤 8：选择本轮最小对照范围

不追求一次覆盖全部场景。优先选择：

- 能区分不同解释的场景；
- 业务损失风险高的场景；
- 输入清楚、证据容易核验的场景；
- 对后续 Skill 复用价值高的场景。

### 步骤 9：冻结当前预期版本并交接

输出 `ExpectationRegister` 和本轮 `FrozenExpectationSet`，交给 `business-evidence-comparison`。

---

## 8. 输出合同

### 8.1 `ExpectationRegister`

```yaml
expectation_id:
version:
status: SEED | WORKING | FROZEN_FOR_COMPARISON | REVISED | RETIRED
business_intent:
judgment_target:
statement:
origin: OWNER_EXPLICIT | BUSINESS_INFERRED | IMPLEMENTATION_DERIVED
source_ref:
applicable_conditions:
non_applicable_conditions:
rationale:
falsifier_or_counterevidence:
evidence_needed:
known_unknowns:
confidence:
owner_decision_required:
supersedes_expectation_id:
revision_reason:
```

### 8.2 `InputSuitabilityAssessment`

分别给出：

- 输入有效性；
- 输入业务合理性；
- 输入对当前目的的适用性；
- 可继续分析的局部范围；
- 必须隔离的问题范围。

### 8.3 `ScenarioExpectationSet`

保存不同输入条件下的预期，不强求单一统一规则。

### 8.4 `OpenQuestions`

按三类不确定性分组，并给出下一步处理者。

---

## 9. 高频标准化示例

### 9.1 Owner 明确预期

```text
希望保留能够覆盖重要拐头的高频，同时减少冗余。
```

### 9.2 业务候选预期

```text
若同一局部活动由多个参数组重复表达，合并可能降低冗余；
但若不同事件分别对应不同业务过程，则不能仅因时间接近就合并。
```

### 9.3 实现预期

```text
在分段点，根据参照转折与各参数组高频的关系约束选择参数；
将选择结果应用到后续候选流；
选中事件形成紧密组，确认结束后再合并。
```

### 9.4 输入三层检查

- 有效性：事件、UTI、参数组和 actual／confirm 是否对齐；
- 业务合理性：Dense／Fight 是否确实表达它声称的高频活动；
- 目的适用性：这些高频活动是否足以承担覆盖拐头的目的。

### 9.5 第一轮最小场景

```text
A. 小转折附近存在清晰候选高频
B. 小转折附近无候选高频
C. 无明显小转折但候选高频密集
D. 多参数组在同一局部重复发生
```

---

## 10. 强制约束

1. 不把代码行为写成天然业务预期。
2. 不把 AI 推导写成 Owner 已确认需求。
3. 不要求在看任何数据前写完全部预期。
4. 不允许在正式对照中无痕改写被冻结预期。
5. 不把“没有事件”自动解释为反证。
6. 不把数据缺失、样本不足、有效空结果和业务失败混为一类。
7. 不因某种场景暂时无法解释，就强行给出统一结论。
8. 不在尚未定位问题来源时直接建议调参数。
