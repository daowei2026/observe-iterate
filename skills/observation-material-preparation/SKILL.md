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
| C 展示方式准备 | [caegraph-display-preparation](caegraph-display-preparation/SKILL.md) | 待展示信息、展示预期、复杂点处理、位置独立展示代码和预期 HTML |
| D CAEGraph 定义集成 | [caegraph-definition-integration](caegraph-definition-integration/SKILL.md) | 将 C 代码绑定真实实例、字段、品种和时间后的完整 CAEGraph 定义 |
| E CAEGraph 执行／运行 | [caegraph-execution](caegraph-execution/SKILL.md) | 最终脚本、最终 HTML、图数据、运行与核对结果 |

## 3. 文件阅读规则

每个阶段目录通常采用：

```text
SKILL.md
    阶段定位、边界、输入输出概览、完成条件和禁止事项

WORKFLOW.md
    内部步骤、步骤目标和步骤中的专业判断方法

IO_SPEC.md
    字段级输入输出
```

B 当前是例外：方法沉淀还不足，`WORKFLOW.md` 只记录当前普通默认和高频多尺度两种用法，不冒充成熟通用 Workflow。

专业判断方法不是一份独立的平行流程；它写在 `WORKFLOW.md` 中真正使用该判断的步骤下。篇幅较大的跨步骤方法进入 `references/`。

## 4. 外层输入与专业知识的边界

本 Workflow 当前外层输入为：

- 特征名称；
- 特征代码版本；
- 特征实例。

这些是本次用例信息。Occurrence 分析方法、普通位置默认、高频多尺度位置层级、主附图规则、CAEGraph 能力和 Worker 修改权限属于 Skill／Reference 中的专业知识，不要求每次运行重新填写，也不得与本次品种、时间等用例事实混在一起。

## 5. 保留的技术参考

- [CAEGraph 展示能力与构建速查](references/CAEGraph展示能力与构建速查.md)
- [CAEGraph 执行、核图与取数参考](references/CAEGraph执行取数与验证.md)
- [高频多尺度观察位置参考](observation-position-preparation/MULTISCALE_POSITION_REFERENCE.md)
- [观察材料准备任务记录模板](templates/观察材料准备任务单.md)
- [候选观察方法索引](../observation-method-candidates/README.md)

候选方法稿不是 A～E 的固定必经步骤。需要时由对应阶段 Skill 按适用条件引用。

## 6. 总体完成边界

- A～D 完成但尚未实际运行，只能是 `PLAN_READY`。
- E 必须先核对最终图，再正式取得图的数据；最终脚本、HTML 和数据必须来自同一有效版本。
- 材料准备阶段只交付图、数据、来源、核对和限制，不代替合理性分析宣布特征合理或不合理。
