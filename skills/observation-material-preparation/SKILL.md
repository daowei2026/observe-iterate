---
name: observation-material-planning-and-preparation
description: 当需要为给定特征实例准备并实际取得 CAEGraph 观察材料时使用。共享 FeatureUnderstandingPackage 是外部前置；本目录负责 B～E：位置、展示、定义集成和实际执行。
---

# 观察材料准备｜总入口

## 1. 共享前置

观察材料准备不再拥有“特征事件级 occurrence 理解”子 Skill。执行本 Workflow 前，必须取得：

- [`FeatureUnderstandingPackage`](../feature-understanding/SKILL.md)；
- 与该 Package 一致的特征名称、代码版本和实例引用。

共享 Package 提供：

```text
业务对象与身份
状态与合法转换
事件级 occurrence 与位置
业务主输出／中间处理结果
关键中间判断
处理关系
参数与运行结果字段映射
```

若 B～E 发现这些事实不清，返回共享特征理解 Skill，不在观察材料流程中重新解释代码。

## 2. 唯一外层 Workflow

完整外层阶段、阶段输入输出和回流关系见：

- [control/02 · 观察材料准备外层 Workflow](../../control/02_L1_观察材料准备流程.md)

本入口不重复 B～E 流程正文。

## 3. 四个阶段 Skill

| 阶段 | Skill | 主要成果 |
|---|---|---|
| B 观察位置准备 | [observation-position-preparation](observation-position-preparation/SKILL.md) | 普通场景的当前默认位置，或高频 1d→30m→1m→5s→tick 多尺度位置路径 |
| C 展示方式准备 | [caegraph-display-preparation](caegraph-display-preparation/SKILL.md) | C1 待展示信息；C2 展示预期、复杂点循环和唯一预期 HTML；C3 位置与实例可注入展示代码及注入合同 |
| D CAEGraph 定义集成 | [caegraph-definition-integration](caegraph-definition-integration/SKILL.md) | 充分理解锁定 CAEGraph 仓库后，把外层输入、共享理解包和 B／C 产物集成为完整定义；拿得准的 B／C 确定性缺项可直接纠正并留痕 |
| E CAEGraph 执行／运行 | [caegraph-execution](caegraph-execution/SKILL.md) | 独立 Codex executor 连续 E1～E6：真实运行/修复、核图接受、图接受后正式取数、同版本图数据与一致性核对 |

## 4. 文件阅读规则

有真实内部步骤的阶段通常采用：

```text
SKILL.md
    阶段定位、边界、输入输出概览、完成条件和禁止事项

WORKFLOW.md
    内部步骤、步骤目标和专业判断方法

IO_SPEC.md
    字段级输入输出
```

当前例外：

- **B**：方法沉淀还不足，`WORKFLOW.md` 只记录普通默认和高频多尺度两种当前用法，不冒充成熟通用 Workflow；
- **D**：只有一个集成动作，不设置 `WORKFLOW.md`，直接读取 `SKILL.md + IO_SPEC.md`；
- **E**：新版 [E Skill](caegraph-execution/SKILL.md) 在独立 Codex executor 同线程完成专业判断及直接运行、取数；旧 W1/W2 工单仅供历史 Run 按原版本追溯。

## 5. 外层输入与专业知识的边界

本 Workflow 当前外层输入为：

- 特征名称；
- 特征代码版本；
- 特征实例；
- 与上述三项一致的 `FeatureUnderstandingPackage`；
- 任务明确指定的品种／时间（如有）。

这些是本次用例事实。位置默认、多尺度层级、展示规则、CAEGraph 仓库理解和 E 工程修复授权边界属于 Skill／Reference 中的专业知识，不要求每次运行重新填写。

特征实例的职责边界：

```text
C：只读理解或临时预览；C3 正式代码保留实例注入接口
D：把外层真实特征实例正式绑定进完整定义
```

## 6. C 的三部分

```text
C1：根据 FeatureUnderstandingPackage 列出待展示信息
C2：理解 CAEGraph，形成并循环更新展示预期和同一份 HTML
C3：把 C2 当前实现整理为位置、实例和字段可注入代码
```

C2 循环结束时的当前 HTML 就是唯一预期 HTML；C3 不再另造第二份预期 HTML。若 C3 整理代码时必须改变展示预期，应返回 C2 同步更新预期与 HTML。

C 直接阅读锁定版本原使用手册：

- [`daowei2026/uplot@e6.2/CAEGraph使用手册.md`](https://github.com/daowei2026/uplot/blob/e6.2/CAEGraph使用手册.md)

复杂展示点若不能仅靠手册判断，再查锁定版本源码。

## 7. D 的直接纠正边界

D 发现 B／C 缺项或错误时：

- 修法唯一、证据清楚、不改变 B 的位置选择或 C2 展示语义时，可以直接纠正并记录修改前后和依据；
- 需要重新选择位置、改变展示预期、存在多个合理方案或涉及业务判断时，必须返回 B／C；
- 共享理解包中的对象、事件、字段或关系事实不清时，返回 `skills/feature-understanding/`。

D 不得无痕改写上游产物。

## 8. E：Codex executor 连续执行，先拿真实反馈

E 是一项完整专业 Skill，默认在本 Run 独立 Codex executor 线程中直接执行：

~~~text
建立最小 D/C2/FeatureUnderstandingPackage 与真实运行入口基准
→ 运行 D、连续诊断与授权范围内修复
→ E2 分类并按需返回共享理解／B／C／D
→ E3 核对并接受最终脚本和真实图
→ E4 确定正式取数清单（必须在核图接受后）
→ Codex 直接导出同一已接受运行的图数据
→ E5 核对一致性
→ E6 交付
~~~

不必为正常工程诊断和取数另签 W1/W2。保留“先做实事，异常再展开”、日志与 diff、真实核图证据、Owner/D 授权及不改变业务语义的边界。

## 9. 最终交付：`ObservationMaterialPackage`

最终至少交付：

```text
FeatureUnderstandingPackage 引用
B／C／D 当前有效产物引用
最终 CAEGraph 脚本
被接受的最终 HTML
正式导出的图数据与元信息
图、数据、Feature 版本和参数实例的一致性核对
已知限制和未解决问题
```

该 Package 供合理性 Skill 1/2 使用；它不代替合理性分析挑选场景或宣布 Feature 合理／不合理。

## 10. 总体完成边界

- B～D 完成但 E 尚未实际运行，只能是 `PLAN_READY`；
- E 必须通过真实运行取得候选图，完成 D/C2 核图接受后才能直接正式取数；
- 最终脚本、HTML、数据、Feature 版本和参数实例必须一致；
- `DATA_READY`：最终图通过核对，正式图数据已取得并通过 E5 一致性检查；
- `PARTIAL_WITH_LIMITS`：只完成部分位置、图层或数据，限制已明确；
- `BLOCKED`：核心图或核心数据无法取得，原因和解除条件已记录。

不得用静态定义、语法检查、少量预览或未核对 HTML 冒充 `DATA_READY`。
