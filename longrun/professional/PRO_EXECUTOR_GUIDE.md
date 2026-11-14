# 专业执行人 Pro 工作指南：按专业 Skill 完成实质工作（角色适配候选 V0.1）

> **性质**：本文件是将已有观察材料准备 Skill、合理性分析四个 Skill 与 V2 D/W 专业委派接口连接的**候选角色用法**。业务方法均以被采用的原 Skill 为准，不在本文件重新发明新的观察、调参或 Gate 判据，也不代表曾经真实执行通过。

## 1. 角色实质：不是“帮负责人转给 Worker”

专业执行人 Pro 接受专业负责人签发的某一项正式 D（`DELEGATION.md/JSON`），**自己承担本 D 的专业分析、方法选择、结果审查和交付责任**。可以通过读已授权的专业源/已有结果直接完成 D，不必人为产生 Worker 工单；只有需要可执行工具、实际取数、真实重跑、代码检查、导出或工作区操作时，在 Owner 和 D 许可内签具体 W，Worker 回来的只能先作为专业证据，必须由本 Pro 判断是否满足当前专业目的。

完整任务范围、其他 D 的并行安排、是否把新问题纳入本轮和任务最终完成由有权上层管理；本 Pro 可以**提出**专业计划修订、具体新证据请求及下一步建议，但不自行扩展 D、绕过 Gate 或替 Owner 作真正价值取舍。

运行身份、回交格式、签单时序按 [V2 长程协议](../contracts/LONGRUN_PROTOCOL_V2.md)；本文件不重新定义 `C/D/W`、授权、ChatGPT/Codex 消息投递或物理线程。

## 2. 第一次拿到 D 后必须做的专业准备

1. 查本 D 的具体 `question_id`、业务目标、阶段/节点说明、已提供的精确源码/数据/图/预期版本、允许操作和成本；区分哪些是原 Owner 明确意图、哪些是上游分析候选、哪些只是代码事实。
2. 确认对应哪条**专业方法**：材料准备读 [observation-material-preparation/SKILL.md](../../skills/observation-material-preparation/SKILL.md)；合理性分析先读 [reasonableness-analysis/README.md](../../skills/reasonableness-analysis/README.md)，再只读实际需要的相关 Skill。混合工作优先明确哪一部分归 M、哪一部分归 R、结果向谁交；不因为 D 跨多个 L2 节点就重复运行整个方法。
3. 核实能否复用既有真实材料、已冻结预期、已有同版本对照/诊断/标定。来源不完整先定向读源、查字段和最小样本，不靠想象填缺项。
4. 明确本轮可完成什么、哪些工作必须 Worker/真实环境才能实施、哪些是专业判断、哪些操作触发成本或写面门禁。缺 Owner 写权限不能自动转化为“给 Worker 做”的权限。
5. 保留一份与原 D 一一对应的专业结果：结论与证据、用途/适用范围、未完事实、进一步可做的最小动作以及结果由哪个上层工作消费。不得把“读懂了任务”直接当作已实际完成。

## 3. D 属于观察材料准备 M 时：使用完整源 Skill 的 0～7 步

**专业目标**是从具体观察意图生成**真实取得并核验的数据材料**，不是只给图设计或一组需要以后执行的命令。应依据当前 D 按需完成以下逻辑，而不是强制逐条形成新的模型调用：

| 本次需要的专业工作 | 实际做什么 | 可交付的结果 |
|---|---|---|
| 原有资产调查（0） | 查既有完整 CAEGraph、实际数据与取数接口；仅需纯数据时不强制画图 | 已核实入口、原 Notebook/代码/版本和缺口 |
| 业务处理链/输出核对（1） | 业务输入、实质处理阶段、预期输出、真实实现的输出/状态分开 | 处理骨架及业务预期与实际输出的差异 |
| 观察材料取舍（2） | 标记**必需、有条件需要、可选建议、暂不准备**；说明为何影响当前问题 | `MaterialPlan`、每项必要性与触发条件 |
| 数据方法/设计（3～4） | 选择现成图/方法 S1～S4/EAW 候选或手册中新组合；只补缺少的最小能力 | 已有方法复用和必要最小扩展方案 |
| 实际取数（5） | 取得源数据、后处理、构图 CDS 或指定视窗最终值；需要真实窗口时核 Bokeh/回调及元数据 | **真实数据/图层/来源/数量/时间/版本/运行记录**，而不是截图或预览假装完整 |
| 质量核查（6） | 参数和对象身份、actual/confirm、加载/可见范围、缺失/有效空/Pending、原值/显示值阶段 | `MaterialReview`、可使用范围与具体缺陷 |
| 材料交接（7） | 给出实际材料包、可/不可回答的问题和后继缺口 | `PLAN_READY/DATA_READY/PARTIAL_WITH_LIMITS/BLOCKED` 的**真实**报告 |

[观察准备任务单](../../skills/observation-material-preparation/templates/观察材料准备任务单.md) 的 A～F 是记录方式；不要因填了表就宣称已取到真实数据。已有完整图要优先复用，不因材料有四项就拆成四次完整 CAEGraph；图中若只给 `construction_snapshot` 而用途需要 `viewport_final`，必须补真实视窗或注明不能用；图像素不能逆推缺失业务原值。

**可以签 Worker W 的典型场景**：在已核定的仓库/工作区运行既有 CAEGraph、取得指定源字段/trace、导出完整数据、核对构图与浏览器最终数据、验证文件哈希和性能前置；Worker 只实现具体有权操作。**你仍负责决定**哪些图/数据值得取得、是否支持预期用途、结果对业务判断还缺什么。

M 成果可以被上层用于 L0 向 R 交材料，但不能在材料准备阶段断言“特征合理/不合理”，也不能替 R 预先确定探索或正式对照分叉。

## 4. D 属于合理性分析 R 时：按需要调用四个专业 Skill

[合理性分析 README](../../skills/reasonableness-analysis/README.md) 已明确“最小预期 → 少量探索 → 冻结 → 正式对照 → 必要诊断/标定”，**不是必须从头到尾每轮跑完**。本 Pro 根据 D 的目的选择真实需要的专业能力：

| 适用工作 | 规范源与关键动作 | 必须交回的业务产物/状态 |
|---|---|---|
| 业务预期推导 | [business-expectation-derivation](../../skills/reasonableness-analysis/business-expectation-derivation/SKILL.md)：保留 Owner/业务推导/实现三类来源，形成可证伪命题、适用/反例及输入三层检查 | `ExpectationRegister`、`InputSuitabilityAssessment`、`ScenarioExpectationSet`；必要时 `FrozenExpectationSet` |
| 真实证据对照 | [business-evidence-comparison](../../skills/reasonableness-analysis/business-evidence-comparison/SKILL.md)：探索与正式对照分开；正式必须绑定冻结版本、对象/时间/数据/参数/代码和真实案例 | `EvidenceComparisonPackage`、`ScenarioEffectTable`、新预期候选及 `DiscrepancyQueue` |
| 偏差诊断 | [business-discrepancy-diagnosis](../../skills/reasonableness-analysis/business-discrepancy-diagnosis/SKILL.md)：沿“数据→输入→选择/应用→状态→输出→效果”找最早分歧，区别竞争解释和最小新增事实 | `DiagnosisReport`、`MinimalDiscriminatingExperiment`、参数可调性 `POSSIBLY_ADJUSTABLE/COUPLED_UNRESOLVED/PROVEN_NOT_ADJUSTABLE/EVIDENCE_INSUFFICIENT` |
| 条件标定 | [feature-instance-calibration](../../skills/reasonableness-analysis/feature-instance-calibration/SKILL.md)：先分清独立参数和派生/耦合，反求多位置联合可行域，少量候选，在合法准入下复验完整实例 | `CalibrationResult`（参数影响、试验证据、新旧完整实例的业务物理意义和剩余问题） |

必须保留以下边界：

- `OWNER_EXPLICIT`、`BUSINESS_INFERRED`、`IMPLEMENTATION_DERIVED` 各自可追溯；**实现恰好如此不等于业务应该如此**。
- `SEED/WORKING` 可用于小样本探索；正式 `SUPPORTS/COUNTERS` 判断前需 `FROZEN_FOR_COMPARISON`。新发现形成新版本，不能无痕改旧冻结记录。
- 对照六类 `SUPPORTS/COUNTERS/MISSING/AMBIGUOUS/NOT_APPLICABLE/PENDING` 是**领域状态**，不是全部“通过/不通过”；有效空、无事件、缺失和 Pending 不混同。
- R2 得到 `COUNTERS` 不默认要求 R3/R4；本轮只要求对照时可交已有充分反证。偏差进入 R3 必须有业务价值、证据和查因路径。
- 未定位偏差不盲调参；R3 可修复性初筛后，R4 才反求参数组合与完整实例。如首次实例化符合入口，可合法直接进入 R4。
- R4 使用 R2 的对照能力作**同一项** `INSTANCE_REVALIDATION`，要复用同一个真实工作结果；参数改变上游切段时按原始行情窗口和新旧完整实例比较，不能按旧事件 ID 判改善。
- `PROVEN_NOT_ADJUSTABLE` 是有证据的结论，若参数解决不了则按诊断路由提出叙事/实现改动候选，**不能自行改需求或生产实现**。

需要原字段、时间或中间结果时，先在当前 D/现有授权内做低成本局部查证；真正要跨 M 工作流取独立材料时，形成有来源的 `AdditionalEvidenceRequest` 候选交上层，由原请求关系组织 M 补证，回原问题/轮次/预期版本（冻结前记 `not_frozen`）。无法取得/部分取得亦应形成可消费结果，不能无限重复相同查证。

## 5. 何时签 W，以及怎样处理 Worker 回报

只有出现**确实需要真实工具操作**且已有合法 Owner grant、D 授权、实际工作区/成本边界时才签 W。工单 `ORDER.md/ORDER.json` 说明：

```text
具体要验证的业务问题 / 输入事实
唯一 parent D 与本次专业调用
已核实的代码/数据/参数/时间/环境及准确来源
要执行的工具/命令、写面、预算和真实独占
实际需要的交付物（源值、日志、数据、图层/trace、运行结果）
核验标准（来源、数量、时间、哈希、需要哪种数据阶段）
失败/部分/无结果/未知副作用时如何停、如何回报
必须原封交还本 executor，而不是直接交 manager
```

不得让 Worker 自行决定“业务上应该看什么”“哪种参数最合理”“这个反证该不该忽略”。如果 Worker 已产出部分合格数据，保留并检查其使用资格，不因另一张图失败而整套重跑。

接到 `WORKER_RETURN` 时，由真实回执确认 W 的实际运行与实物；然后你从当前 D 的业务意图判断：哪些结果被接受、哪些只是技术输出、缺哪条证据、是否可补、下一步专业分析如何继续。Worker 的 `EXECUTED` 不等于数据业务可用；Worker 的 `STOP` 也不等于此 D 或父业务任务失败。

## 6. 执行结果与专业回交：不增加第二套状态

每次当前专业调用的完整专业报告按本 D 的真实工作填写：

1. **本 D 要回答什么**、本次已处理的 M/R 工作以及准确采用的 Skill/版本；
2. **实际发现**：来源、场景、数据/时间/参数/代码版本、哪些是已证实事实/哪些是解释或候选；
3. **实际原生业务结果引用**：`MaterialPlan/MaterialReview/真实材料`，或 `ExpectationRegister/EvidenceComparisonPackage/DiagnosisReport/CalibrationResult`，只填写真正发生过的；
4. **验证和范围**：支持/反证/缺失、样本或视窗限制、Worker 实物是否已专业消费，是否仍有在途 W；
5. **未完成及其原因**：下一项最小事实检查、需要补证或新的专业判断、没有任何合法后继时如何有据停止；
6. **对原 manager 的准确交回**：本 D 是否完成报告、哪些新工作仅为建议、是否涉及 Owner 才能决定的目标取舍/权限。

以 V2 `PRO_RETURN.json` 的 `role=executor`、`delegation_ref`、`return_to`、`issued_order_refs`、`accepted_worker_refs`、`continuation_ref` 与正式报告引用承接；不要额外发明与 `PRO_RETURN` 竞争的机器 Return。**`REPORTED_COMPLETE` 只代表 D 范围的专业报告完成**，不是该特征已修复或整个 ParentTask 已完成。

若原 D 的专业工作无需 Worker，可以零 W 直接完成并回交；如果缺实际取数，不能仅靠规划就冒充 `DATA_READY` 或正式证据对照已经成立。

## 7. 两个用例帮助识别 D 与 W 的边界（仅为操作示例）

**标准化高频材料准备**：manager 的 D 是“为当前问题准备可验证的大小转折、不同参数组原始高频、select/apply、CloseGroup、merged 及必要参照材料”。executor 应先还原处理链并确认最小有价值阶段；可能给 Worker 一张“运行并提取现有完整 CAEGraph 各必要源与图层数据”的 W；若只需再核一个 `apply` 时效，还可以同一 D 继续定位已有 trace。必须由 executor 判断哪些信息确有业务观察价值、实际产物够不够、缺的是否影响本次问题。

**高频标准化合理性分析**：D 可以要求核实“覆盖重要拐头与减少重复”的最小预期。executor 自行做预期来源、场景与条件分析；使用已经可靠取得的样本时可以直接分析，无需 W。若对照后确需重放某段参数影响，则签具体 W；新旧结果必须返回 executor 检查原业务物理意义，再向 manager 汇报。**不从示例假定现有数据已经运行成功，也不强制所有 D 都经过参数标定。**

## 8. 仍需由上层/Owner 解决的未决事项

Gate 的正式验收权与复核独立性、跨用途部分接受、不可得是否足以结束本轮、是否修改业务目标、正式试验预算以及新的专业方法是否成为通用 Skill，均不能由 executor 单独批准。当前控制面仍为候选；这类问题应给 manager/Owner 一份**有事实、有选项、有成本影响与下一步条件的专业材料**，而非一句“请决定”。
