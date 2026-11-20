# 合理性分析 V0.2｜实施摘要与审阅顺序

> 实施分支：`feat/reasonableness-analysis-v0.2-20261120`  
> 基线分支：`feat/observe-iterate-multirun-controller-v1-20261116`  
> 目标：先让 EAW 与 FQA 的合理性分析形成可运行闭环，再用 EAW Wall 真跑一轮迭代 Skill。

## 1. 本轮已确定的设计

### 1.1 严格串行，不做双线并行

```text
共享 Feature 理解
→ 运行 Feature
→ 全量行为统计
→ Skill 3 诊断
→ 参数／实现／设计／数据问题闭环
→ Feature 重跑
→ 全量统计重跑
→ GlobalProfileGate = PASS_TO_SCENARIO_REVIEW
→ 为最新实例准备宽范围图与图数据
→ Skill 1 从图中选真实场景并冻结预期
→ Skill 2 逐场景过程对照
→ 新疑点进入 Skill 3
→ 行为一旦变化，重新回到 Feature 重跑与全量统计
```

线一发现的所有**已被确认**参数、实现、设计或数据问题必须先闭环；仅靠统计不能判断业务对错的问题进入 `ScenarioQuestionQueue`，在线二通过图和真实过程判断。

### 1.2 线二不直接消费完整全量运行结果

Skill 1／2 消费：

```text
FeatureUnderstandingPackage
CurrentReviewTarget
ObservationMaterialPackage
ScenarioQuestionQueue／CandidateCaseIndex
```

它们使用的图和图数据必须来自通过全量 Gate 的最新 Feature 运行，但不另把完整运行结果作为并列输入。

### 1.3 共享 Feature 理解移出观察材料准备

原观察材料 A 与旧合理性 Skill 1 中重复的“对象／状态／事件／处理链／实现行为理解”合并为共享 Skill：

```text
skills/feature-understanding/
```

核心产物：

```text
FeatureUnderstandingPackage
```

观察材料准备改为 B～E。

### 1.4 暂不建设影响分级 Skill

V0.2 采用保守重跑：

- 参数、实现、设计或数据修改改变 Feature 行为后，重跑 Feature 与全量统计；
- 通过 Gate 后重新准备观察材料和场景分析；
- 暂不做跨问题依赖图、局部跳过或自动并行调度。

## 2. 新增内容

### 2.1 共享 Feature 理解 Skill

```text
skills/feature-understanding/
├── SKILL.md
├── WORKFLOW.md
└── IO_SPEC.md
```

新增能力：

- 业务对象与身份；
- 状态与合法转换；
- occurrence；
- 业务主输出与中间结果；
- 关键中间判断；
- 处理关系；
- 参数定义、派生和消费；
- 运行结果字段映射；
- 未确认项。

明确不做：运行、全量统计、选场景、画图、合理性判断。

### 2.2 全量行为统计 Skill

```text
skills/reasonableness-analysis/feature-global-behavior-profiling/
├── SKILL.md
├── WORKFLOW.md
└── IO_SPEC.md
```

主要输出：

```text
StatisticsInputReadiness
GlobalBehaviorProfile
GlobalFindingCandidates
ScenarioQuestionQueue
CandidateCaseIndex
DiagnosisInputAdapters
GlobalProfileGate
```

Gate：

```text
BLOCKED
DIAGNOSIS_REQUIRED
RERUN_REQUIRED
PASS_TO_SCENARIO_REVIEW
```

为兼容暂不修改的 Skill 3，新增 `DiagnosisInputAdapter`。

## 3. 迁移内容

原目录：

```text
skills/observation-material-preparation/feature-occurrence-understanding/
```

三份旧专业定义已删除，并保留 `README.md` 指向新共享 Skill。历史提交和历史 Run 不回写。

## 4. Skill 1／2 的修改

### 4.1 Skill 1

原路径和 `name` 保持：

```text
skills/reasonableness-analysis/business-expectation-derivation/SKILL.md
name: business-expectation-derivation
```

V0.2 新职责：

- 在观察材料已经完成后，从真实图和图数据中挑场景；
- 强制考虑：
  - `CLEAR_POSITIVE`
  - `CLEAR_NEGATIVE`
  - `OUTPUT_FALSE_POSITIVE_CANDIDATE`
  - `POTENTIAL_FALSE_NEGATIVE`
  - `PARAMETER_BOUNDARY`
  - `OUTSIDE_CURRENT_COVERAGE`
- 为每个案例写具体过程预期；
- 冻结 `CaseReviewSet`、`ScenarioExpectationSet` 和兼容 `FrozenExpectationSet`；
- 材料不足时返回观察材料准备。

删除／移出：

- 重复查代码；
- 重复定义对象、状态和处理链；
- 把当前实现行为称作业务预期；
- 在没有真实图和位置时凭空构造正式场景。

### 4.2 Skill 2

原路径和 `name` 保持：

```text
skills/reasonableness-analysis/business-evidence-comparison/SKILL.md
name: business-evidence-comparison
```

V0.2 新职责：

- 消费 Skill 1 已冻结案例；
- 对齐：
  - `RawMarketProcess`
  - `ExpectedFeatureProcess`
  - `ObservedFeatureProcess`
- 找 `EarliestBusinessDivergence`；
- 输出 `ScenarioProcessCasebook`、兼容 `EvidenceComparisonPackage` 和 `DiscrepancyQueue`；
- 不选场景、不做全量统计、不查根因、不调参。

## 5. 明确未修改的内容

以下专业正文未改：

```text
skills/reasonableness-analysis/business-discrepancy-diagnosis/SKILL.md
skills/reasonableness-analysis/feature-instance-calibration/SKILL.md
```

因此：

- Skill 3 仍负责根因诊断、竞争解释、最小检查、参数可修复性初筛和路由；
- Skill 4 仍负责参数可行域、跨位置共同范围、少量候选和完整实例验证；
- V0.2 的闭环通过外层控制和 Skill 0 的兼容适配实现，不在本轮改 Skill 3／4 内部。

## 6. 观察材料准备的修改

观察材料准备改为：

```text
FeatureUnderstandingPackage
        ↓
B 观察位置 ─┐
             ├→ D 定义集成 → E 执行／核图／正式取数
C 展示方式 ─┘
        ↓
ObservationMaterialPackage
```

边界：

- B 准备宽范围位置，不挑合理性场景；
- C 根据共享 Package 展示主输出、状态和必要中间判断；
- D 绑定真实实例、位置和共享字段；
- E 形成同版本脚本、HTML 和图数据；
- 正例／反例／漏报等由 Skill 1 在图完成后选择。

## 7. 控制面同步

已同步：

```text
README.md
control/01_L0_完整业务任务与双向衔接.md
control/02_L1_观察材料准备流程.md
control/03_L1_合理性分析流程.md
control/04_L2_节点输入输出登记表.md
control/05_三级Gate及后继路由.md
control/06_业务完成全景与更新协议.md
```

以及观察材料 B／C／D 的 Skill、Workflow、IO 和任务模板。

## 8. 建议审阅顺序

不需要从头逐字审所有文件。建议：

### 第一组：先审总关系

1. [`skills/reasonableness-analysis/README.md`](../../skills/reasonableness-analysis/README.md)
2. [`control/03_L1_合理性分析流程.md`](../../control/03_L1_合理性分析流程.md)

重点确认：

- 是否接受严格串行；
- 全量 Gate 的边界是否正确；
- 线二是否只消费图和图数据；
- 行为变化后是否统一回 Feature 重跑与全量统计。

### 第二组：审真正新增的 Skill

3. [`skills/feature-understanding/SKILL.md`](../../skills/feature-understanding/SKILL.md)
4. [`skills/feature-understanding/WORKFLOW.md`](../../skills/feature-understanding/WORKFLOW.md)
5. [`feature-global-behavior-profiling/SKILL.md`](../../skills/reasonableness-analysis/feature-global-behavior-profiling/SKILL.md)
6. [`feature-global-behavior-profiling/WORKFLOW.md`](../../skills/reasonableness-analysis/feature-global-behavior-profiling/WORKFLOW.md)

### 第三组：只审 Skill 1／2 的职责变化

7. [`business-expectation-derivation/SKILL.md`](../../skills/reasonableness-analysis/business-expectation-derivation/SKILL.md)
8. [`business-evidence-comparison/SKILL.md`](../../skills/reasonableness-analysis/business-evidence-comparison/SKILL.md)

建议重点看：

- 输入；
- “何时使用／不用于”；
- 执行步骤；
- 输出合同；
- 强制约束。

Skill 3／4 无需重复审，因为未改。

### 第四组：需要时再审材料准备与控制面适配

9. `control/02` 和观察材料入口；
10. B／C／D 及任务模板；
11. L0／L2／Gate／完成全景。

## 9. EAW Wall 首轮试运行建议

```text
1. 生成 Wall FeatureUnderstandingPackage；
2. 绑定当前 Wall 代码、默认参数和全量运行结果；
3. 执行全量行为统计；
4. 将 D1 等结构疑点通过适配包交 Skill 3；
5. 参数问题走 Skill 4，重跑 Wall 和全量统计；
6. 实现／设计问题走外部接口后重跑；
7. 全量 Gate 通过；
8. 对最新实例准备宽范围 Wall 图与中间数据；
9. Skill 1 从图中选正例、负例、误报、漏报、边界和覆盖外案例；
10. Skill 2 做逐过程对照；
11. 新疑点进入 Skill 3；
12. 根据实际摩擦迭代 V0.3。
```

## 10. 本轮有意延后的内容

- Skill 1／2 重命名；
- Skill 3／4 内部返回合同；
- 跨问题影响分级；
- 多问题并行调度；
- 局部重跑替代全量重跑；
- 场景分析反向驱动画图的自动化；
- main 分支同步与正式采用。
