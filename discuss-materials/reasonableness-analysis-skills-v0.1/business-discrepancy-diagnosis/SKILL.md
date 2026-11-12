---
name: business-discrepancy-diagnosis
description: 当真实数据与业务预期不一致或证据存在多种解释时，沿数据—特征—处理—输出—效果链定位问题来源，设计低成本区分性检查，并形成可交给 Owner 或后续专业角色的诊断材料。
version: 0.1.0
status: draft
---

# 业务偏差诊断与 Owner 决策材料

## 1. 何时使用

在以下情况使用：

- 某个输入或输出明显不符合被冻结预期；
- 同一现象有数据、实现、算法和业务定义等多种解释；
- 改动前需要判断真正的问题发生在哪一层；
- 需要找最小实验区分两个或多个原因；
- 需要把真正的业务取舍整理给 Owner。

不用于：

- 只列“可能原因清单”而不继续排查；
- 未确认问题来源就直接调参数；
- 把所有偏差都归为“需求不清楚”；
- 替 Owner 决定价值取舍。

---

## 2. 核心目标

把：

```text
这里看起来不对
```

推进到：

```text
偏差发生在哪个处理阶段
哪些事实已确认
哪些解释仍竞争
用什么低成本检查可以区分
哪些属于技术事实
哪些属于业务取舍
下一步由谁处理
```

---

## 3. 输入要求

至少需要：

```text
FrozenExpectation
EvidenceComparisonPackage
BusinessIntent
ProcessingChain
RelevantCodeOrRequirementRefs
DataBindingAndTimeBasis
```

若连字段含义和实现事实都不清楚，先归入第一类不确定性并自行补查。

---

## 4. 不确定性三分类与强制路由

| 不确定性来源 | 处理方式 |
|---|---|
| 缺少数据、字段含义或实现事实 | AI 优先自行查代码、补数据或做最小实验 |
| 可以通过真实样本、反例和进一步对照判断 | AI 继续分析，并给出有证据的候选结论 |
| 存在不同的业务目标取舍，无法仅靠数据确定 | 提交 Owner 决定 |

### 4.1 第一类：事实缺口

典型问题：

- 字段究竟是 actual 还是 confirm；
- 参数组何时生效；
- 是否发生过滤、重置或覆盖；
- JSON 是否来自同一版本；
- 数据是否缺失或错位。

处理：查代码、配置、运行记录或做最小复现。

### 4.2 第二类：可由证据解决

典型问题：

- 偏差是否只出现在特定 Session；
- 是否由极端样本主导；
- 两种代表规则哪种更接近目标位置；
- 方案历史适合但后续失效是否重复发生。

处理：构造正例、反例和区分性对照。

### 4.3 第三类：真正的业务取舍

典型问题：

- 优先保留活动最强事件，还是最接近拐头的事件；
- 宁可多保留避免漏掉，还是更强地去重；
- 更重视实时性，还是更重视最终准确性。

处理：形成 OwnerDecisionPacket，不替 Owner 选择。

---

## 5. 偏差来源分类

诊断至少区分以下层次：

```text
A. 数据与来源
B. 时间、对象和参数绑定
C. 输入特征业务含义
D. 输入对当前目的的适用性
E. 处理规则／算法
F. 选择、应用、状态和确认
G. 输出表达／代表性规则
H. 业务预期本身
I. 后续效果与环境变化
```

不能把所有问题压成“算法问题”或“参数问题”。

---

## 6. 执行步骤

### 步骤 1：复述偏差，避免模糊命名

用以下结构表达：

```text
在什么输入条件下
依据哪一版预期
实际观察到什么
与预期具体冲突在哪里
业务影响是什么
```

错误示例：

> 高频标准化效果不好。

正确示例：

> 在存在可解释候选高频的小转折场景中，某些局部的最终 merged 代表事件距离目标实际转折明显更远；当前预期是合并应减少重复而不显著损失目标位置表达。

### 步骤 2：建立处理链

列出从原始证据到最终输出的所有可能丢失、改变或延迟信息的阶段。

每个阶段记录：

```text
Input
Rule
State
Output
ActualTime
ConfirmTime
Version
PossibleInformationLoss
```

### 步骤 3：事实与解释分开

建立两栏：

```text
ConfirmedFacts
CompetingExplanations
```

不允许把“可能因为”写成已定位结论。

### 步骤 4：构造诊断树

对每个竞争解释问：

- 若它成立，还应看到什么？
- 若它不成立，应看到什么？
- 现有证据能否区分？
- 最小新增证据是什么？
- 检查成本和业务价值如何？

### 步骤 5：设计低成本区分性检查

优先级：

1. 直接查已有中间结果；
2. 查代码或配置事实；
3. 找一对对照场景；
4. 在少量位置重放；
5. 仅在必要时扩大统计范围；
6. 最后才考虑实现新工具或大规模重跑。

### 步骤 6：定位到最小责任阶段

可能结论示例：

```text
已定位：数据时间错位
已定位：原始候选本身不存在，输出阶段无责
已定位：参数选择未包含目标方案
已定位：选择已包含，但应用生效范围不同
已定位：CloseGroup 尚未确认，属于 Pending
已定位：代表性规则导致位置偏移
未定位：业务预期与输入特征目的可能不匹配
```

### 步骤 7：判断是否需要返回预期推导

若发现：

- 原预期适用条件不完整；
- 新场景无法由现有预期覆盖；
- Owner 目的存在多种合理解释；

则创建新的候选预期，不修改旧版本。

### 步骤 8：决定下一步路由

```text
数据问题
    → 数据准备／数据质量角色

实现未照既有规则
    → 实现修正角色

现有规则执行正确但业务效果不合理
    → 叙事／需求迭代角色

证据不足但可继续分析
    → 证据对照 Skill

真正业务取舍
    → Owner
```

---

## 7. 高频标准化诊断链

针对“重要拐头附近缺少最终高频”这一类问题，按以下顺序：

### 7.1 原始候选

所有参数组中是否存在接近该目标位置的 `ThickEnd`？

- 无：检查上游输入、Dense／Fight 定义及当前目的适用性；
- 有：继续。

### 7.2 分段参数选择

`select` 是否包含产生目标事件的参数组？

- 无：检查该分段使用的参照转折、数量关系、样本和选择时点；
- 有：继续。

### 7.3 选择应用

目标事件是否发生在该参数组生效范围内？

- 无：检查“历史选择 → 后续应用”的时间边界；
- 有：继续。

### 7.4 紧密组更新与确认

目标事件是否进入 CloseGroup？

- 未进入：检查临近约束和对象属性；
- 进入但未确认：标记 `PENDING`；
- 已确认：继续。

### 7.5 代表事件

最终是否由其他更强 Dense／Fight 事件代表？

- 是：比较“强度代表性”与“转折位置代表性”的业务取舍；
- 否：检查其他输出转换。

### 7.6 当前数量约束的边界

若参数组数量比例满足，但高频在段内分布与目标拐头明显错位，应形成候选诊断：

> 当前约束能够表达数量关系，但缺乏对事件局部位置关系的充分表达。

这只是待真实数据支持的候选诊断，不能仅从代码结构直接宣布实际问题已发生。

---

## 8. OwnerDecisionPacket

只有真正的业务取舍才提交 Owner。至少包含：

```yaml
decision_id:
business_question:
why_data_cannot_decide_alone:
option_a:
  preserves:
  sacrifices:
  supporting_cases:
  counter_cases:
option_b:
  preserves:
  sacrifices:
  supporting_cases:
  counter_cases:
common_facts:
uncertain_facts:
implementation_implications:
recommended_observation_cases:
owner_decision_needed:
```

示例：

```text
选择紧密组代表事件时：
A. 优先最大 Dense/Fight
B. 优先接近目标拐头或更早确认
```

提交前，AI 应先比较两种规则在哪些真实位置产生不同结果，以及各自保留／损失什么。

---

## 9. 输出合同

### 9.1 `DiagnosisReport`

```yaml
diagnosis_id:
expectation_id:
expectation_version:
discrepancy_statement:
business_impact:
confirmed_facts:
processing_chain:
competing_explanations:
ruled_out_explanations:
remaining_explanations:
discriminating_checks:
current_localization:
confidence:
next_route:
```

### 9.2 `MinimalDiscriminatingExperiment`

描述最小新增数据、样本、重放或代码检查。

### 9.3 `RequirementOrImplementationIssue`

区分：

```text
ImplementationMismatch
BusinessRuleInsufficiency
InputPurposeMismatch
DataQualityIssue
UnresolvedTradeoff
```

### 9.4 `OwnerDecisionPacket`

仅在第三类不确定性下生成。

---

## 10. 强制约束

1. 不只列可能原因，必须尽量排除并排序。
2. 不把实现事实缺口提交给 Owner。
3. 不把可由真实样本区分的问题提交给 Owner。
4. 不在根因未定位前直接调参数。
5. 不把单一异常等同于通用规则失败。
6. 不用后来证据无痕重写旧预期和旧判断。
7. 不把 Pending、缺失和真正反证混为一类。
8. 不替 Owner 决定业务价值取舍。
9. 不把当前算法限制自动解释为业务世界的限制。
10. 不在没有业务影响说明时把所有实现差异都升级为高优先级问题。
