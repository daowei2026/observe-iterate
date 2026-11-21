# V0.2 Gate：验收对象、输入、输出与失败后继

> 本文件规定共享理解、Feature 执行、全量行为统计、观察材料、场景分析和问题处理之间的消费资格。专业判断仍由对应 Skill 完成；Gate 不把业务反证判成工作失败，也不把“文件存在”当作“可被下游消费”。

## 1. Gate 判断的四类对象

| 判定对象 | 示例 | 禁止混淆 |
|---|---|---|
| `WorkQuality` | 共享理解是否准确；全量统计是否按真实对象计数；图与数据是否一致 | 业务反证不等于专业工作失败 |
| `UseEligibility` | 最新运行结果能否做统计；材料能否支持指定案例 | 文件存在不等于用途合格 |
| `ActionEligibility` | Feature 重跑、实现修改、参数试验、E 直接运行／正式取数（或历史 W1/W2）是否有权限与成本资格 | 一次授权不等于所有后续动作授权 |
| `TaskCompletion` | 本轮是否达到原完成条件 | 不要求 Feature “修到完全合理”才可交付有据结果 |

硬检查可记录：

```text
PASS / FAIL / UNKNOWN / NOT_RUN / NOT_APPLICABLE
```

必需硬检查为 `UNKNOWN` 或 `NOT_RUN` 时不能算通过。

## 2. L0 主要 Gate

| Gate | 输入与验收对象 | 通过后继 | 未通过后继 |
|---|---|---|---|
| **H0 TASK-ENTRY** | `BusinessTaskInput`：Feature、版本、实例、运行入口、数据范围、当前目标 | U 共享理解 | 目标／对象不明则具名补充，不猜测扩大范围 |
| **H1 UNDERSTANDING-HANDOFF** | `FeatureUnderstandingPackage` | X；并可供 G/M/S1/S2/D 引用 | 核心对象／状态／事件／字段不清则返回 U |
| **H2 GLOBAL-PROFILE** | 最新运行绑定、全量剖面、疑点和 Gate | 按 `GlobalProfileGate` 路由 | 见第 3 节 |
| **H3 MATERIAL-HANDOFF** | `ObservationMaterialPackage`、图、正式图数据、版本与限制 | S1 | `PLAN_READY` 或仅有 HTML 不能作为正式场景材料 |
| **H4 SCENARIO-FREEZE** | 真实案例、具体位置、场景预期、材料引用 | S2 | 案例不具体、预期不可反驳或版本不一致则回 S1／M |
| **H5 PARENT-CLOSE** | 本轮所有有效原生产物、未决和完成评价 | `ParentTaskOutcome` | 仍有原任务必需工作时回准确节点；新增问题不自动扩大本轮 |

## 3. 全量行为统计 Gate

### `BLOCKED`

必要事实之一不可靠：

- 理解包与运行结果版本不一致；
- 参数实例或数据范围不明；
- 对象键、时间键或核心事件字段不能可靠读取；
- 运行结果不足以形成主要剖面。

后继：修正 U、X 或数据绑定。不得进入 M/S1/S2。

### `DIAGNOSIS_REQUIRED`

存在结构疑点，例如：

- 生命周期起点／终点不闭合；
- 终结后继续更新；
- 非法状态转换；
- 中间状态系统性零时长；
- 同拍顺序违背既定生命周期；
- 引用对象大量悬空；
- 稀疏输出近似逐 Tick。

后继：使用 Skill 0 的 `DiagnosisInputAdapter` 进入现有 Skill 3。

### `RERUN_REQUIRED`

参数、实现、设计或数据修正改变了 Feature 行为，旧运行与旧全量剖面失效。

后继：X → G。旧 M/S1/S2 只能作为历史对照。

### `PASS_TO_SCENARIO_REVIEW`

- 当前统计绑定最新运行；
- 已确认参数问题完成 Skill 4、重跑并复验；
- 已确认实现问题完成外部修正、重跑并复验；
- 已确认设计问题完成决策、实现、重跑并复验；
- 剩余问题只能靠真实场景解释，或仅是描述性分布。

后继：M。该状态不等于 Feature 合理。

## 4. 问题诊断与处理 Gate

### `G-DIAGNOSIS`

**输入**：统计或场景疑点、冻结预期／结构不变量、证据包、共享处理链、版本与时间基础。

**应核对**：

- 偏差陈述具体；
- 事实和解释分开；
- 竞争解释有可区分预测；
- 最小责任阶段有证据；
- 参数可修复性不是凭猜测。

**后继**：

| 诊断结果 | 后继 |
|---|---|
| `POSSIBLY_ADJUSTABLE` | Skill 4 |
| `COUPLED_UNRESOLVED` | Skill 4 深入可行性 |
| `PROVEN_NOT_ADJUSTABLE` 且属设计能力 | 外部设计接口 |
| 实现与既有规则不一致 | 外部实现接口 |
| 数据／绑定问题 | 数据或 U/X 修正 |
| 需真实场景才能判断 | `ScenarioQuestionQueue`，等待全量 Gate 允许后进入 M/S1/S2 |
| 证据不足 | 定向补证，不直接调参 |

### `G-CALIBRATION`

**输入**：Skill 3 可调结论、冻结预期、原始业务窗口、参数关系、运行入口。

**应核对**：

- 合法自由参数和派生参数已区分；
- 联合可行域而非机械单参区间；
- 少量候选有业务依据；
- 改上游对象时回到原始窗口评价；
- 局部复算没有冒充完整实例通过。

**通过后继**：形成新实例 → X → G。Skill 4 的局部成功不能跳过全量统计。

### 外部实现／设计返回 Gate

| 返回 | 最低要求 | 后继 |
|---|---|---|
| `ImplementationFixReturn` | 对应 diagnosis、commit、改动文件、行为变化、测试、新 Feature 版本 | 结构合同改变→U；否则→X；随后 G |
| `DesignDecisionReturn` | 对应 diagnosis、业务定义、实现要求、验收条件、决策版本；且实现已完成 | U→X→G |

## 5. 观察材料 B～E Gate

> 只有 `PASS_TO_SCENARIO_REVIEW` 才能正式进入。

| 阶段 | 必需检查 | 通过后继 | 返回 |
|---|---|---|---|
| **B 位置** | 属于当前实例；任务指定或当前经验规则可解释；D 能绑定 | D | 位置无数据／无效回 B |
| **C1 信息清单** | 共享理解中的主输出、必要输入／状态／中间判断已映射 | C2 | 语义事实不清回 U |
| **C2 展示与 HTML** | 已读原手册；第一版即有 HTML；复杂点循环同步更新同一预期与 HTML | C3 | 展示问题留 C2；真实能力缺口具名 |
| **C3 可注入代码** | 未固化最终实例或位置；保持 C2 语义；字段注入完整 | D | 需改展示语义回 C2 |
| **D 定义集成** | 真实实例、共享字段和 B 位置已绑定；仓库调用链已核；无无痕语义修改 | E | 语义／位置／展示问题分别回 U／B／C |
| **E 图与数据** | 真实运行/修复日志；E3 专业核图接受；E4 准入；正式图数据；E5 一致性核对 | `ObservationMaterialPackage` | 只运行成功或只有 HTML 不算 `DATA_READY` |

## 6. 场景选择与过程分析 Gate

### `G-SCENARIO-FREEZE`

至少核对：

- 案例来自当前 `ObservationMaterialPackage`；
- 品种、开始／结束时间和材料引用明确；
- 不只从已有输出反选案例，已考虑潜在漏报；
- case type 属于约定六类之一；
- 当前 intended coverage 与 explicit non-goals 清楚；
- 过程预期可被真实证据反驳；
- `CaseReviewSet` 和 `FrozenExpectationSet` 已冻结。

通过→S2；缺图层／字段→M；目标取舍不清→Owner。

### `G-SCENARIO-COMPARISON`

至少核对：

- `RawMarketProcess` 不由 Feature 输出定义；
- `ExpectedFeatureProcess` 来自冻结预期；
- `ObservedFeatureProcess` 来自真实图数据；
- 对象身份、时间和中间判断对齐；
- `EarliestBusinessDivergence` 已定位或限制明确；
- 覆盖外案例没有被当成当前版本失败；
- 材料缺口、业务反证和待确认分开。

有值得诊断的疑点→Skill 3；无→综合交付；新预期→S1 新版本。

## 7. 行为改变后的失效 Gate

| 变化 | 失效范围 | 必经后继 |
|---|---|---|
| 参数实例变化 | X、G、M、S1、S2 旧结果 | X→G；通过后重做 M/S1/S2 |
| 对象／状态／事件／处理中间结构变化 | U 及其所有下游 | U→X→G→M→S1→S2 |
| 业务实现规则变化 | X 及其所有行为结果；U 需核对 | U 核对→X→G→M→S1→S2 |
| 数据／时间对齐变化 | X、G、M、S1、S2 | X→G→M→S1→S2 |
| 只补结果字段、不改行为 | 共享字段映射和相关统计／材料 | U 字段映射→相关 G/M；不自动重跑业务逻辑 |
| 只改展示 | M 的 C～E 与依赖案例 | C→D→E→S1/S2 |
| 只改案例／预期 | S1/S2 | S1→S2 |

## 8. 当前不设置的 Gate

V0.2 暂不设置：

- 跨问题影响分级 Gate；
- 多问题并行优先级 Gate；
- 局部复验替代全量重跑 Gate；
- 场景反向驱动画图的自动 Gate。

这些在 EAW Wall 与一个 FQA Feature 实跑后再判断必要性。
