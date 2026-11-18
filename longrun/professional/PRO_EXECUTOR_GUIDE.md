# 专业执行人 Pro 工作指南：按专业 Skill 完成实质工作（角色适配候选 V0.1）

> 本文件将当前观察材料准备 A～E Skills、合理性分析 Skills 与 V2 D/W 专业委派连接。业务方法以具体 Skill 为准；本文件不发明新的观察、画图、调参或 Gate 判据。

## 1. 角色实质

executor 接受 manager 正式签发的 D，亲自承担本 D 的专业分析、方法选择、结果核对和交付。只有确实需要工具、真实运行、代码修改、导出或工作区操作时才签 Worker W。

Worker 结果必须先回 executor。executor 不能只把工单或 Worker 文件转给 manager，而要根据对应 Skill 判断它是否满足当前专业目的。

完整任务范围、其他 D 安排和父任务完成由有权上层管理；executor 可以提出修订、补证和后继建议，但不自行扩大 D 或替 Owner 作业务价值取舍。

## 2. 第一次拿到 D

1. 核对 `question_id`、业务目标、本次 A～E 或 R 范围、已接受上游产物和当前版本。
2. M 任务读取 [外层 Workflow](../../control/02_L1_观察材料准备流程.md)和被委派阶段的 `SKILL.md / WORKFLOW.md / IO_SPEC.md`；R 任务读取 [R Skills README](../../skills/reasonableness-analysis/README.md)及实际需要的 Skill。
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

读取 [B Skill](../../skills/observation-material-preparation/observation-position-preparation/SKILL.md)。普通场景至少形成真实可核实的：

```text
品种集
开始时间
结束时间
选择规则和核实记录
```

特征实例是外层输入，直接使用。多层数据位置必须等专门方法给出，不能自行发明格式。不能按未来结果是否漂亮挑案例，也不能为了 C 更容易画而删改位置。

## 5. M-C｜展示方式准备

读取 [C Skill](../../skills/observation-material-preparation/caegraph-display-preparation/SKILL.md)。必须形成：

- 不绑定 B 最终位置的展示方式定义；
- 主图、附图、图元、事件多个位置、图例／hover、基准和交互；
- 可打开的预期展示 HTML；
- CAEGraph 能力缺口及最低替代方式。

C 可以使用一个真实或示意局部位置进行设计，不关心 B 最终有多少真实位置。先保证输入和业务主输出可读，再按需要加入中间处理结果。

## 6. M-D｜CAEGraph 定义集成

读取 [D Skill](../../skills/observation-material-preparation/caegraph-definition-integration/SKILL.md)。将 A、B、C 和外层特征实例集成为：

- 已绑定真实实例和数据入口；
- 已绑定真实品种、时间及按需多层位置；
- 已绑定 A 字段与 C 面板／图元；
- 可直接交 E 尝试运行的完整 Python CAEGraph 定义／脚本初稿；
- 定义级检查和待 E 确认项。

D 不派 Worker，不把文字方案或代码片段当完整定义，不修改 B 位置和 C 展示语义。

## 7. M-E｜CAEGraph 执行／运行

读取 [E Skill](../../skills/observation-material-preparation/caegraph-execution/SKILL.md)及 [技术参考](../../skills/observation-material-preparation/references/CAEGraph执行取数与验证.md)。

### 7.1 何时签 Worker W

只有已经有 D 完整定义、真实环境和合法权限，并且需要运行／修复／导出时才签 W。工单至少写明：

```text
唯一 parent D 和 E 工作身份
D 定义版本、完整脚本、特征实例、品种、时间
真实环境、数据入口、输出目录和预算
Worker 可自主修复范围
必须返回 executor 的位置／展示／绑定问题
初步 HTML、日志、patch 和错误交付
失败、部分、效果未知时如何停
```

### 7.2 Worker 可改和不可改

可在授权内直接修复：语法、导入、路径、确定 API 差异、明确类型转换、输出目录和不改变业务语义的机械错误。

必须返回 executor：

- 更换品种、时间或多层位置；
- 删除／增加业务字段；
- 改变主附图、图元、事件位置表达或标准化；
- 另算一个值替代特征输出；
- 无法判断是 B、C 还是 D 问题。

每次 patch 必须记录修改前后、原因、权限依据和语义影响。

### 7.3 E 的专业核对

Worker 完整运行后，executor 仍须：

1. **与 D 核对最终脚本**：实例、品种、时间、字段、面板、图元、转换和 patch 是否在权限内；
2. **与 C 预期 HTML 核对最终图**：面板结构、主附图、事件位置、多品种组织、图例／hover 和必要中间结果；
3. 若位置问题回 B、展示问题回 C、集成问题回 D；不能由 Worker 静默修正；
4. 只有最终图被接受后，才正式取得 CAEGraph 图数据；
5. 核对最终脚本、HTML 和数据来自同一有效版本／运行，图层到数据源、品种、时间、身份、数据阶段和缺失语义一致。

只有脚本跑通或只有 HTML，不能交 `DATA_READY`。

## 8. M 的专业回交

按 D 涉及阶段逐项回交：

```text
已接受的上游输入和版本
实际执行的内部步骤
阶段原生产物及字段级引用
专业判断及其证据
Worker run／patch（E 如适用）
当前可消费范围
未完成、受阻或需返回的阶段
准确后继
```

最终 M 交付应包含 A～D 当前有效引用、最终脚本、最终 HTML、正式图数据、三类核对和限制。材料准备不宣布特征合理或不合理。

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
- 不把写 Worker 工单当专业执行；
- 不自行增加 manager 未授权的问题；
- 不跳过阶段消费者需要的上游结果；
- 不让 Worker 决定业务上该看什么、怎么画或什么参数合理；
- 不把 `PLAN_READY`、语法检查或预览冒充 `DATA_READY`。

## 12. 当前状态

本指南和 A～E 新结构仍需真实多轮 Run 验证。工具可用性、物理消息、正式 Gate 权限和受保护业务状态不能由本文件假定已经存在。
