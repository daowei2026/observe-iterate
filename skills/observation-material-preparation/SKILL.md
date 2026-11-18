---
name: observation-material-planning-and-preparation
description: 当需要为给定特征实例准备并实际取得 CAEGraph 观察材料时使用。外层执行顺序以 control/02 的 A～E Workflow 为准，各阶段专业方法由本目录五个子 Skill 提供。
---

# 观察材料准备｜总入口

## 1. 唯一外层 Workflow

完整外层阶段、阶段输入输出和回流关系见：

- [control/02 · 观察材料准备外层 Workflow](../../control/02_L1_观察材料准备流程.md)

本入口不重复一份 A～E 流程正文。

## 2. 五个阶段 Skill

| 阶段 | Skill | 主要成果 |
|---|---|---|
| A 特征事件级 occurrence 理解 | [feature-occurrence-understanding](feature-occurrence-understanding/SKILL.md) | 事件级 occurrence、事件发生位置、业务主输出／中间处理结果及处理关系 |
| B 观察位置准备 | [observation-position-preparation](observation-position-preparation/SKILL.md) | 普通场景的当前默认位置，或高频 1d→30m→1m→5s→tick 多尺度位置路径 |
| C 展示方式准备 | [caegraph-display-preparation](caegraph-display-preparation/SKILL.md) | 待展示信息、展示预期、复杂点处理、位置与实例可注入展示代码、实例注入合同和预期 HTML |
| D CAEGraph 定义集成 | [caegraph-definition-integration](caegraph-definition-integration/SKILL.md) | 充分理解锁定 CAEGraph 仓库后，把外层输入和 A／B／C 产物一次性集成为完整定义 |
| E CAEGraph 执行／运行 | [caegraph-execution](caegraph-execution/SKILL.md) | E 专业判断、W1 运行修复、核图、W2 正式取数、最终脚本／HTML／图数据和核对结果 |

## 3. 文件阅读规则

有真实内部步骤的阶段通常采用：

```text
SKILL.md
    阶段定位、边界、输入输出概览、完成条件和禁止事项

WORKFLOW.md
    内部步骤、步骤目标和步骤中的专业判断方法

IO_SPEC.md
    字段级输入输出
```

当前例外：

- **B**：方法沉淀还不足，`WORKFLOW.md` 只记录当前普通默认和高频多尺度两种用法，不冒充成熟通用 Workflow；
- **D**：只有一个集成动作，不设置 `WORKFLOW.md`，直接读取 `SKILL.md + IO_SPEC.md`；
- **E**：除 `WORKFLOW.md + IO_SPEC.md` 外，还必须读取 [Worker 派单合同](caegraph-execution/WORKER_DELEGATION.md)以及 W1／W2 两份工单模板。

专业判断方法不是一份独立的平行流程；它写在真正使用该判断的步骤下。篇幅较大的跨步骤方法进入 `references/`。

## 4. 外层输入与专业知识的边界

本 Workflow 当前外层输入为：

- 特征名称；
- 特征代码版本；
- 特征实例。

这些是本次用例信息。Occurrence 分析方法、普通位置默认、高频多尺度位置层级、展示规则、CAEGraph 仓库理解和 Worker 修改权限属于 Skill／Reference 中的专业知识，不要求每次运行重新填写，也不得与本次品种、时间等用例事实混在一起。

特征实例的职责边界为：

```text
C：只读理解或临时预览，正式代码保留实例注入接口
D：把外层真实特征实例正式绑定进完整定义
```

## 5. 保留的技术参考

- [CAEGraph 展示能力与构建速查](references/CAEGraph展示能力与构建速查.md)
- [CAEGraph 仓库结构与定义集成参考](references/CAEGraph仓库结构与定义集成参考.md)
- [CAEGraph 执行、核图与取数参考](references/CAEGraph执行取数与验证.md)
- [高频多尺度观察位置参考](observation-position-preparation/MULTISCALE_POSITION_REFERENCE.md)
- [观察材料准备任务记录模板](templates/观察材料准备任务单.md)
- [候选观察方法索引](../observation-method-candidates/README.md)

候选方法稿不是 A～E 的固定必经步骤。需要时由对应阶段 Skill 按适用条件引用。

## 6. E 的两类 Worker 工单

E 的专业 Workflow 与 Worker 操作分开：

- [W1 运行与有限修复模板](caegraph-execution/RUN_REPAIR_ORDER_TEMPLATE.md)
- [W2 正式取图数据模板](caegraph-execution/DATA_EXPORT_ORDER_TEMPLATE.md)

W2 只能在 E 已接受最终图并形成正式取数准入后签发，不能与 W1 合并为一张提前授权正式取数的工单。

## 7. 总体完成边界

- A～D 完成但尚未实际运行，只能是 `PLAN_READY`。
- E 必须先通过 W1 取得候选图，由 E 对照 D／C 完成专业核图；核图接受后再签 W2 正式取得图数据。
- 最终脚本、HTML 和数据必须来自同一有效版本和运行。
- 材料准备阶段只交付图、数据、来源、核对和限制，不代替合理性分析宣布特征合理或不合理。
