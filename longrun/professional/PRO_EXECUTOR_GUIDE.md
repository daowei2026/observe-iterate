# 专业执行人 Pro 工作指南：按专业 Skill 完成实质工作（角色适配候选 V0.1）

> 本文件将当前观察材料准备 A～E Skills、合理性分析 Skills 与 V2 D/W 专业委派连接。业务方法以具体 Skill 为准；本文件不发明新的观察、画图、调参或 Gate 判据。

## 1. 角色实质

executor 接受 manager 正式签发的 D，亲自承担本 D 的专业分析、方法选择、结果核对和交付。只有确实需要工具、真实运行、代码修改、导出或工作区操作时才签 Worker W。

Worker 结果必须先回 executor。executor 不能只把工单或 Worker 文件转给 manager，而要根据对应 Skill 判断它是否满足当前专业目的。

完整任务范围、其他 D 安排和父任务完成由有权上层管理；executor 可以提出修订、补证和后继建议，但不自行扩大 D 或替 Owner 作业务价值取舍。

## 2. 第一次拿到 D

1. 核对 `question_id`、业务目标、本次 A～E 或 R 范围、已接受上游产物和当前版本。
2. M 任务读取 [外层 Workflow](../../control/02_L1_观察材料准备流程.md)和被委派阶段真实文件：通常是 `SKILL.md / WORKFLOW.md / IO_SPEC.md`；D 只有 `SKILL.md + IO_SPEC.md`；E 还必须读取 `WORKER_DELEGATION.md` 与两张短执行卡。R 任务读取 [R Skills README](../../skills/reasonableness-analysis/README.md)及实际需要的 Skill。
3. 核实特征名称、代码版本、特征实例以及可复用的同版本阶段产物。
4. 区分专业判断、确定性文件处理和需要 Worker 的真实执行；缺写权限不自动等于有权交 Worker。
5. 明确本 D 可交付什么、哪些问题必须回 manager、哪些结果只可限域使用。

## 3. M-A｜特征事件级 occurrence 理解

读取 [A Skill](../../skills/observation-material-preparation/feature-occurrence-understanding/SKILL.md)。必须形成：

- 输入事件级 occurrence；
- 输出侧业务主输出 occurrence；
- 中间处理 occurrence／结果；
- 各事件自己的发生位置及 occurrence 携带的其他位置；
- 输入、中间处理和业务主输出的形成／更新／确认／结束／引用关系；
- 代码证据和未确认项。

不得用需求代替代码，不得因某中间表正式公开就把它改称业务主输出，也不得在 A 选择最终观察品种和时间。

## 4. M-B｜观察位置准备

读取 [B Skill](../../skills/observation-material-preparation/observation-position-preparation/SKILL.md)。普通场景当前直接使用任务明确位置或经验默认；高频场景复用专门的 1d→30m→1m→5s→tick 位置层级。

特征实例是外层输入，直接使用。B 当前不是成熟位置选择理论，不能自行扩张出新的 B1、B2，也不能把高频参考脚本的图层和样式当成位置方法。

## 5. M-C｜展示方式准备

读取 [C Skill](../../skills/observation-material-preparation/caegraph-display-preparation/SKILL.md)、[C Workflow](../../skills/observation-material-preparation/caegraph-display-preparation/WORKFLOW.md)和 [C 字段合同](../../skills/observation-material-preparation/caegraph-display-preparation/IO_SPEC.md)。

C 固定分成：

```text
C1：列出待展示信息
C2：形成并迭代展示预期
    C2A：直接阅读锁定版本 CAEGraph 使用手册
    C2B：形成第一版展示预期和第一版 HTML
    C2C：从当前 HTML 列出复杂展示点
    C2D：循环核实现有能力，并同步更新预期和 HTML
C3：整理可注入展示代码
    C3A：整理位置、实例和字段可注入的代码
    C3B：核对代码与 C2 当前预期
```

必须形成 C1 待展示信息、C2 当前展示预期和唯一预期 HTML、复杂点处理、C3 可注入代码以及 D 所需注入合同。C 可以只读使用外层真实实例或临时生成预期 HTML，但不能把该实例固化为最终运行绑定。

## 6. M-D｜CAEGraph 定义集成

读取 [D Skill](../../skills/observation-material-preparation/caegraph-definition-integration/SKILL.md)、[D 字段合同](../../skills/observation-material-preparation/caegraph-definition-integration/IO_SPEC.md)和 [CAEGraph 仓库结构与定义集成参考](../../skills/observation-material-preparation/references/CAEGraph仓库结构与定义集成参考.md)。

D 是一个单一专业动作。executor 必须理解锁定版本仓库中本次使用的导出、配置、布局、绘图、`PlotCtx`、Feature→CDS、数据树和动态／前端路径，并根据外层输入和 A／B／C 正式绑定实例、数据入口、位置和字段，形成可直接交 E 运行的完整 Python 定义。

D 发现 B／C 缺项时：

- 修法唯一、证据清楚、不改变 B 位置或 C2 展示预期时，可以直接纠正并留痕；
- 需要重新选位置、改变展示预期、存在多个合理方案或拿不准时，返回 B／C；
- A 的事件、字段、位置或引用关系不清时返回 A。

D 不派 Worker，也不把文字方案或代码片段当完整定义。

## 7. M-E｜CAEGraph 执行／运行

读取：

- [E Skill](../../skills/observation-material-preparation/caegraph-execution/SKILL.md)
- [E 专业 Workflow](../../skills/observation-material-preparation/caegraph-execution/WORKFLOW.md)
- [Worker 派单合同](../../skills/observation-material-preparation/caegraph-execution/WORKER_DELEGATION.md)
- [W1 短执行卡](../../skills/observation-material-preparation/caegraph-execution/RUN_REPAIR_ORDER_TEMPLATE.md)
- [W2 短执行卡](../../skills/observation-material-preparation/caegraph-execution/DATA_EXPORT_ORDER_TEMPLATE.md)
- [执行与取数技术参考](../../skills/observation-material-preparation/references/CAEGraph执行取数与验证.md)

### 7.1 结果优先

E 的 Worker 操作默认遵循：

```text
最少填写
→ 先真实运行／导出
→ 先回 HTML、真实错误或数据文件
→ 只有实际触发时才补环境、血缘、哈希和详细说明
```

通用 Worker 工单已经包含的身份、授权、工作区和回交信息，不在阶段卡中重复抄写。

### 7.2 E 自己承担的专业 Workflow

executor 自己负责：

```text
建立最小运行基准
→ 消费 W1 真实结果并分类问题
→ 与 D 核对最终脚本、与 C2 核对最终图
→ 明确本次正式取数清单
→ 消费 W2 数据并作必要核对
→ 交付
```

不能把这些专业判断写进工单让 Worker 代替完成。

### 7.3 两张短执行卡

| 专业位置 | 短执行卡 | Worker 首要结果 |
|---|---|---|
| E1 最小基准已形成 | W1 运行 CAEGraph | 可打开 HTML，或首个真实阻断错误 |
| E4 已接受最终图并列出取数清单 | W2 导出已接受图的数据 | 明确列出的数据文件及最小映射 |

W1 和 W2 仍是两个授权时点，但不是两套审计工程。不得在 W1 开始时提前授权正式取数。

### 7.4 W1 边界

W1 可以直接修复语法、import、路径、锁定版本已确认的 API 差异、明确类型和输出接线问题。

必须回 executor：

- 更换品种、时间、多尺度位置或实例；
- 删除、增加、替换业务字段；
- 改变 C2 的主附图、图元、事件位置表达、标准化或交互；
- 另算近似值代替特征输出；
- 正确修法不唯一或无法判断语义影响。

W1 最小回报只有：状态、最终脚本、候选 HTML、日志、`git diff` 和当前阻断。环境版本、详细 patch 解释等只在确实影响结果时增加。

### 7.5 W2 边界

W2 只导出 E4 明确列出的图层／对象和数据阶段，不默认导出 source、postprocessed、construction_snapshot、viewport_final 的全部组合，也不先建设通用导出框架。

W2 最小回报只有：状态、数据文件、`图层／对象 → 文件 → 数据阶段 → 行数`、未取得项和日志。

只有实际需要时才增加：

- Renderer／CDS／源表全量血缘；
- `viewport_final`；
- 原值／显示值详细关系；
- 完整缺失语义；
- 文件哈希和环境快照。

W2 不允许修改已接受脚本、图、位置、字段和展示语义；必须修改才能继续时，停止并使当前取数准入失效。

### 7.6 E 的专业核对

executor 必须：

1. 与 D 核对最终脚本；
2. 与 C2 当前展示预期／HTML 核对最终图；
3. 位置问题回 B、展示问题回 C、集成问题回 D；
4. 只有最终图被接受后，才启动 W2；
5. 按本轮用途核对 W2 文件是否对应已接受图、数据阶段、品种、时间和完整性。

只有脚本跑通、只有 HTML，或者 W2 文件未经必要核对，都不能交 `DATA_READY`。

## 8. M 的专业回交

按实际阶段回交：

```text
已接受的上游输入和版本
实际执行的内部步骤或单一动作
阶段原生产物及引用
专业判断及证据
W1／W2 的最小回报和必要补充（E 如适用）
当前可消费范围
未完成、受阻或需返回的阶段
准确后继
```

最终 M 交付应包含 A～D 当前有效引用、最终脚本、最终 HTML、本轮需要的正式图数据、专业核对和限制。材料准备不宣布特征合理或不合理。

## 9. R｜合理性分析

R 任务仍按四个专业 Skill 选择实际需要的能力：

| 工作 | 主要产物 | 核心边界 |
|---|---|---|
| 预期推导 | `ExpectationRegister`、输入适用性、场景和冻结版 | Owner／业务推导／实现来源分开；正式对照前冻结 |
| 证据对照 | `EvidenceComparisonPackage`、场景效果和偏差队列 | 绑定真实材料、时间、对象、代码和参数；六类证据状态不改写 |
| 偏差诊断 | `DiagnosisReport`、竞争解释和可修复性 | 找最早分歧；未定位不盲调 |
| 条件标定 | `CalibrationResult`、联合可行域、试验和完整实例比较 | 先有动作资格；原始窗口和完整物理意义保留 |

需要 M 补证时，形成具名请求并回原问题／轮次；不能自行改生产实现、业务需求或冻结预期。

## 10. Worker 回报的一般处理

- Worker 运输成功不等于专业工作完成；
- 文件存在不等于数据有效；
- 效果未知先对账，不重复执行；
- Worker 发现超出工单的问题只回报，不自行扩大；
- executor 依据 Skill 接受、限域、返修或形成补证请求，再正式回 manager。

## 11. 禁止事项

- 不用“已读懂任务”冒充专业产物；
- 不把写 Worker 工单或补齐模板当成主要专业工作；
- 不自行增加 manager 未授权的问题；
- 不跳过消费者需要的上游结果；
- 不让 Worker 决定业务上该看什么、怎么画、图是否通过或什么参数合理；
- 不把 `PLAN_READY`、语法检查、W1 运行成功或预览冒充 `DATA_READY`。

## 12. 当前状态

本指南和 A～E 新结构仍需真实多轮 Run 验证。工具可用性、物理消息、正式 Gate 权限和受保护业务状态不能由本文件假定已经存在。
