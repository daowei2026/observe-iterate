---
name: feature-global-behavior-profiling
description: 基于共享 FeatureUnderstandingPackage 和同版本特征运行结果，对业务对象、状态、事件、生命周期与分层分布做全量行为统计，发现结构塌缩、不可达、非法顺序、过密／过稀风险及跨环境失稳疑点；不依赖图，不替代偏差根因诊断。
version: 0.1.0
status: draft
---

# 特征全量行为统计与结构疑点发现

## 1. 何时使用

在以下任务中使用：

- 已取得某个明确 Feature 版本、参数实例和数据范围的运行结果；
- 需要在看图前检查对象、状态、事件和生命周期是否存在系统性异常；
- 需要确认某个现象是个案还是全量重复模式；
- 需要为后续场景观察提供重点问题和候选时间位置；
- 参数、实现或设计修改后，需要重新检查全局行为是否出现新退化。

本 Skill 不负责：

- 画图或从图中挑选正反例；
- 判断某个真实市场过程是否像它声称的业务对象；
- 定位问题根因；
- 决定参数修改、实现修正或业务设计取舍。

## 2. 核心目标

将完整运行结果转成：

```text
可追溯的全量／分层行为剖面
+ 系统性结构疑点
+ 需要通过真实场景解释的问题
+ 可交给现有偏差诊断 Skill 的输入包
+ 是否可以进入场景观察线的 Gate
```

这里的“结构疑点”是问题候选，不自动等于业务不合理。

## 3. 输入

至少需要：

```text
FeatureUnderstandingPackage
FeatureRunResultBinding
  ├─ feature code version
  ├─ parameter instance/version
  ├─ data scope
  ├─ run id / artifact refs
  └─ run result tables/files
StratificationPlan
  ├─ symbol
  ├─ period
  ├─ Session
  └─ other available environment strata
```

若运行结果与 FeatureUnderstandingPackage 的代码／实例版本不一致，必须停止正式统计。

字段级格式见 [IO_SPEC.md](IO_SPEC.md)。

## 4. 统计对象

根据 `FeatureUnderstandingPackage` 中真实存在且可读取的内容，按需统计：

- 候选／中间判断命中；
- 业务对象数量与身份连续性；
- 业务主输出 occurrence；
- 状态占用、状态转换和状态持续时间；
- 生命周期长度、起点／终点完整性；
- 分支和 reason 可达性；
- 同对象同刻 occurrence 顺序；
- 对象间引用完整性；
- 事件、对象和活跃覆盖密度；
- 品种、时期、Session 等分层差异。

运行结果未暴露的中间判断不得用代码内变量冒充已统计结果。

## 5. 疑点分两类

### 5.1 `STRUCTURAL_FINDING_CANDIDATE`

已有事实足以说明结构异常值得进入偏差诊断，例如：

- 生命周期终点存在但起点缺失；
- 非法状态转换；
- 中间状态全部零时长；
- 设计分支在完整样本中不可达；
- 同刻事件顺序系统性违背既定生命周期；
- 同一业务对象在终结后继续更新；
- 对象引用大量悬空；
- 稀疏输出近似逐 Tick 发生。

这类疑点进入 `business-discrepancy-diagnosis`；本 Skill 不解释根因。

### 5.2 `SCENARIO_INTERPRETATION_QUESTION`

统计看起来值得关注，但不能仅凭数量或分布判断业务是否合理，例如：

- 某品种对象数显著更高；
- 某类结束原因很少；
- 活跃覆盖率高；
- 生命周期偏短；
- 某时段 Start 密集。

这类问题进入后续图上场景选择与过程分析，不在本 Skill 中强行判错。

## 6. 全量统计 Gate

本 Skill 输出 `GlobalProfileGate`：

- `BLOCKED`：数据、版本、对象键或核心字段不可靠，统计不能成立；
- `DIAGNOSIS_REQUIRED`：存在结构疑点，需先走现有 Skill 3；
- `RERUN_REQUIRED`：问题处理改变了 Feature 行为，必须重跑 Feature 后重新统计；
- `PASS_TO_SCENARIO_REVIEW`：已确认的参数／实现／设计问题均已闭环或不存在；剩余问题只能靠场景解释，允许进入观察材料与真实场景分析。

`PASS_TO_SCENARIO_REVIEW` 不代表 Feature 已经合理，只代表全量结构检查已完成本轮职责。

## 7. 与现有 Skill 3／4 的关系

### 7.1 进入 Skill 3

每个结构疑点必须生成 `DiagnosisInputAdapter`，将统计事实映射到现有 `business-discrepancy-diagnosis` 所需的：

```text
FrozenExpectation／结构不变量引用
EvidenceComparisonPackage 兼容证据包
BusinessIntent／当前 Feature 目标引用
ProcessingChain 引用
RelevantCodeOrRequirementRefs
DataBindingAndTimeBasis
```

这样无需先修改 Skill 3 内部合同。

### 7.2 进入 Skill 4

只有 Skill 3 判定为 `POSSIBLY_ADJUSTABLE` 或 `COUPLED_UNRESOLVED` 后，才进入 `feature-instance-calibration`。本 Skill 不直接试值。

## 8. 输出

1. `StatisticsInputReadiness`；
2. `GlobalBehaviorProfile`；
3. `GlobalFindingCandidates`；
4. `ScenarioQuestionQueue`；
5. `CandidateCaseIndex`；
6. `DiagnosisInputAdapters`；
7. `GlobalProfileGate`。

详细字段见 [IO_SPEC.md](IO_SPEC.md)。

## 9. 完成条件

- 统计结果绑定明确代码版本、参数实例和数据范围；
- 计数单位、对象键、分母、同刻规则和去重规则来自共享理解包并已说明；
- 对象、事件、状态、生命周期和关键分层中，凡运行结果可支持者均已形成剖面；
- 结构疑点与需要场景解释的问题已分开；
- 所有正式疑点均保留可复现位置、重复次数、影响比例和证据来源；
- Gate 状态及下一步明确。

## 10. 不允许做的事

- 不根据输出数量直接宣布业务合理或不合理；
- 不把低频分支自动判为无用；
- 不把没有 occurrence 自动解释为失败；
- 不将运行结果未暴露的代码内变量当作统计事实；
- 不在此 Skill 内查根因、改实现、改需求或调参数；
- 不用全局平均掩盖品种、时期、Session 和对象条件差异；
- 不因发现一个疑点而停止其他可完成的全量剖面。
