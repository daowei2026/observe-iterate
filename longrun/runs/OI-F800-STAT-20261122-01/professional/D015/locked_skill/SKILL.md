---
name: feature-global-behavior-profiling
description: 基于共享 FeatureUnderstandingPackage 和同版本特征运行结果，对业务对象、状态、事件、生命周期与分层分布做全量行为统计；在不停止于第一个问题、也不机械扩大问题面的前提下，发现本轮高置信度的不合理现象候选，并将其交给偏差诊断。
version: 0.1.1
status: draft
---

# 特征全量行为统计与高置信不合理现象发现

## 1. 何时使用

在以下任务中使用：

- 已取得某个明确 Feature 版本、参数实例和数据范围的运行结果；
- 需要在看图前检查对象、状态、事件和生命周期是否存在系统性异常；
- 需要确认某个现象是个案还是全量重复模式；
- 需要在同一轮中先找齐当前结果里明确值得处理的问题，再逐个进入根因诊断；
- 参数、实现或设计修改后，需要重新检查全局行为是否出现新退化。

本 Skill 不负责：

- 画图或从图中挑选正反例；
- 在证据不足时把统计现象直接判成业务错误；
- 定位问题根因；
- 决定参数修改、实现修正或业务设计取舍。

## 2. 核心目标

将完整运行结果转成：

```text
可追溯的全量／分层行为剖面
+ 本轮高置信不合理现象候选队列
+ 发现覆盖与判断边界说明
+ 未升级为 finding 的观察项
+ 可交给现有偏差诊断 Skill 的输入包
+ GlobalProfileGate
```

这里的候选表示“已有充分理由进入诊断”，不自动等于已确认业务缺陷。

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
CurrentReviewTarget
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
- 当前对象、历史对象及其口径差异；
- 状态占用、状态转换和状态持续时间；
- 生命周期长度、起点／终点完整性；
- 分支和 reason 可达性；
- 同对象同刻 occurrence 顺序；
- 对象间引用完整性；
- 事件、对象和活跃覆盖密度；
- 上下游转化、首次阻断与数量级关系；
- 品种、时期、Session 等有业务意义的分层差异。

运行结果未暴露的中间判断不得用代码内变量冒充已统计结果。

## 5. 发现阶段：覆盖面与置信度并重

发现一个候选不构成本轮 G 完成。在进入单个 finding 的深入诊断前，应先对当前正式结果完成一次高置信不合理现象发现：

```text
完成适用业务面的统计与检查
→ 识别执行者判断为明确值得处理的候选
→ 记录未升级观察和未覆盖范围
→ 形成与当前结果绑定的候选队列快照
→ 再由主 Workflow 逐个进入 D
```

这里既不是单纯追求“看得广”，也不是要求穷尽所有可能问题。执行者需要同时判断：

- 现象是否与当前 Feature 的对象语义、生命周期、输出合同或数量关系发生明显冲突；
- 现有全量／分层事实是否足以说明它不是普通波动或纯主观感受；
- 是否值得投入责任逻辑定位和根因诊断；
- 当前证据支持到什么程度，仍有哪些解释未排除。

以下只作为参考视角，包括但不限于：

- 对象身份、状态或生命周期矛盾；
- 与明确业务语义发生强冲突；
- 上下游转化或当前对象数量出现有业务分母支持的数量级异常；
- 多品种、多时期或多对象重复出现的结构异常；
- 正式输出之间不自洽。

这些参考视角不是穷尽清单、固定阈值或自动判错规则。执行者可以提出清单外候选；也可以在证据不足时不把清单内现象升级为 finding。每个升级候选都应说明 `why_high_confidence` 和 `confidence_limits`。

Owner 明确提出的候选必须进入本轮评估，但仍不预设它最终是代码缺陷、业务规则问题、统计口径问题或非问题。

候选队列“冻结”只表示形成当前结果绑定下的可追溯快照，不禁止后续证据产生新候选；不得以此为理由忽略后来发现的明显问题。

## 6. 候选与未升级观察

### 6.1 `HIGH_CONFIDENCE_REASONABLENESS_CANDIDATE`

已有事实足以说明该现象值得进入偏差诊断。它可以来自硬结构冲突，也可以来自有明确业务分母和对象语义支持的强数量级矛盾。

进入 `business-discrepancy-diagnosis`；本 Skill 不解释根因。

### 6.2 `OBSERVATION_NOT_PROMOTED`

当前值得记录，但证据不足以升级为高置信候选，例如：

- 单个孤立案例；
- 只有最大值很大，却没有可靠口径或业务比较基准；
- 分层差异存在，但尚不能说明业务冲突；
- 输出数量变化，但没有说明为何偏离 Feature 目标。

这类条目记录“为什么暂不升级”和返回条件；当前 V0.3 不自动路由到场景线。

## 7. 全量统计 Gate

本 Skill 输出 `GlobalProfileGate`：

- `BLOCKED`：数据、版本、对象键或核心字段不可靠，统计不能成立；
- `DIAGNOSIS_REQUIRED`：存在尚未完成评估的高置信候选，或 Owner 指定候选尚未判断；
- `RERUN_REQUIRED`：问题处理改变了 Feature 行为，必须重跑 Feature 后重新统计；
- `PASS_TO_SCENARIO_REVIEW`：当前结果上的高置信发现工作已完成，已确认问题均已闭环或不存在；剩余条目尚不足以升级或超出当前 ReviewTarget。

`PASS_TO_SCENARIO_REVIEW` 不代表 Feature 已经全面合理，也不自动启动另一套 Workflow。

## 8. 与现有 Skill 3／4 的关系

### 8.1 进入 Skill 3

每个高置信候选必须生成 `DiagnosisInputAdapter`，将统计事实映射到现有 `business-discrepancy-diagnosis` 所需的：

```text
FrozenExpectation／对象合同／业务语义引用
EvidenceComparisonPackage 兼容证据包
BusinessIntent／当前 Feature 目标引用
ProcessingChain 引用
RelevantCodeOrRequirementRefs
DataBindingAndTimeBasis
```

适配包不得提前写根因。

### 8.2 进入 Skill 4

只有 Skill 3 判定为 `POSSIBLY_ADJUSTABLE` 或 `COUPLED_UNRESOLVED` 后，才进入 `feature-instance-calibration`。本 Skill 不直接试值。

## 9. 输出

1. `StatisticsInputReadiness`；
2. `GlobalBehaviorProfile`；
3. `FindingDiscoverySummary`；
4. `GlobalFindingCandidates`；
5. `ObservationsNotPromoted`；
6. `CandidateCaseIndex`；
7. `DiagnosisInputAdapters`；
8. `GlobalProfileGate`。

详细字段见 [IO_SPEC.md](IO_SPEC.md)。

## 10. 完成条件

- 统计结果绑定明确代码版本、参数实例和数据范围；
- 计数单位、对象键、分母、同刻规则和去重规则来自共享理解包并已说明；
- 当前 Feature 适用的对象、事件、状态、生命周期、转化与关键分层已形成足以支持判断的剖面；
- 未因发现第一个问题而停止其余适用业务面的检查；
- 已形成 `FindingDiscoverySummary` 和当前结果绑定的候选队列快照；
- 每个高置信候选都说明为何值得进入诊断、影响范围、证据来源和当前边界；
- Owner 指定候选已有明确状态；
- Gate 状态及下一步明确。

## 11. 不允许做的事

- 不根据输出数量直接宣布业务合理或不合理；
- 不把参考类别当作穷尽清单、固定阈值或自动判错器；
- 不把低频分支自动判为无用；
- 不把没有 occurrence 自动解释为失败；
- 不将运行结果未暴露的代码内变量当作统计事实；
- 不在此 Skill 内查根因、改实现、改需求或调参数；
- 不用全局平均掩盖品种、时期、Session 和对象条件差异；
- 不因发现一个候选而停止其他适用的高置信发现工作；
- 也不为了“找全”把所有边角现象都升级成 finding。
