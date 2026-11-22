# Owner 意图与两线运行计划

> Owner 直接意图和纠偏的完整提炼见 [`OWNER_PROMPT_EXTRACT.md`](OWNER_PROMPT_EXTRACT.md)。本文件只保存本次 Campaign 的可执行摘要，不另加新的业务目标。

## 1. 已明确的业务意图

当前重点是：

- 在 Owner 已指定的用例、品种、时间、尺度和工作区上取得完整结果；
- 根据完整统计发现明显不合理问题；
- 把每个问题的现象、业务冲突、责任逻辑和证据分析清楚；
- 对改法明确、值得处理的问题，先形成具体修改方案并回 Owner 确认；
- 只有 Owner 确认后才修改正式代码、参数、配置、业务规则或数据处理；
- 修改后的正式实例继续运行、统计和发现问题；
- 暂时不把时间主要花在复杂、改法不确定、发生比例较低的规则重构上；
- WALL 与 F 两条基础线并行安排；
- 两条基础线达到当前深度后，再进入下游 Feature；
- manager 和 Skill executor 都在 Codex 运行，不使用 Worker。

AI 不把“暂缓复杂问题”改写为“复杂问题已经消失”，也不把自己的流程补充改写为 Owner 新要求。

## 2. Owner 锁定的正式运行范围

```yaml
wall:
  use_case: EAW P1 integrated / WALL
  symbols: [rb, m]
  start_time: 2021-01-01
  end_time: 2021-12-31
  sides: [bid, ask]
  workspace: /dwdhome/fy/BASE_E6_2

f:
  use_case: U2/U3 F-Q-V use case / F only
  symbols: [rb, hc, i]
  sampling: 5m
  start_time: 2021-01-01
  end_time: 2023-12-31
  workspace: /dwdhome/fy/BASE_E6_2_copy
```

正式范围不由 AI 自行调整。临时诊断可使用范围内的少量位置或短窗口，但不改变正式范围，也不能替代最终全量结果。

## 3. Campaign 结构

```text
BASE-WALL ─┐
            ├─ 两条基础线均达到本轮允许释放的状态
BASE-F ────┘
                 ├─ WALL downstream graph
                 └─ Q → V
```

基础 Run 是两个独立 Run，不建立跨 Run 专业 manager。“联合 Barrier”只是控制实现名称，不增加第三套专业判断。

## 4. 两条线的 CurrentReviewTarget

### WALL

```yaml
current_goal:
  在问题1、2、4最终修正版上按锁定 EAW 用例、rb/m、2021 全年范围重新形成完整统计，确认旧问题状态，并继续发现明显结构不合理点。
intended_coverage:
  Owner prompt 要求的业务对象、相关属性、上下游处理和时序逻辑、正式输出字段、对象发生次数、上游转化、发生位置、bid/ask 分侧以及已知 finding 复验。
explicit_non_goals:
  本轮不强制完成问题3所需的复杂生命周期规则重构；不证明所有复杂多价位场景均合理。
owner_constraints:
  问题3保留为已知限制；新发现逐项诊断；具体新修改先回 Owner 确认。
current_acceptance_level:
  最新完整统计已完成；已知问题已核实；没有仍属本轮范围且未经处理／暂缓决定的已确认问题。
```

### F

```yaml
current_goal:
  使用 Owner 提供并锁定的新参数实例，按 U2/U3 F 用例、rb/hc/i、5m、2021—2023 范围完整重跑 F，检查候选组及上游转化结构，继续发现明显合理性问题。
intended_coverage:
  Owner prompt 要求的业务对象与属性层次、实际/确认/选择时间、每品种上游转折、相容关系、准入阻断、候选组创建与修订及其发生位置。
explicit_non_goals:
  不重复把“为什么最终选这个参数”作为必做标定；不把候选组数量增加当作修复充分条件；不优先展开复杂新规则设计。
owner_constraints:
  新参数实例由 Owner 提供并锁定；AI 不再自行改参数；新 finding 逐项诊断，具体修改先回 Owner 确认。
current_acceptance_level:
  最新完整统计已完成；原迟确认准入问题在新实例上的实际影响已说明；没有仍属本轮范围且未经处理／暂缓决定的已确认问题。
```

## 5. 修改确认路由

AI 可以直接做：

```text
读取与核对
→ 按锁定范围运行
→ 统计和合理性分析
→ 局部诊断／隔离实验
→ 形成复现、ModificationProposal、影响分析和验证计划
```

任何新的正式行为改变必须：

```text
ModificationProposal
→ Owner 确认／修订／暂缓
→ 确认后实施
→ 完整重跑和重统计
```

未确认时状态为 `WAITING_OWNER_MODIFICATION_CONFIRMATION`，不得把临时 patch、候选参数或诊断性干预当作本 Run 正式版本。

## 6. Feature 理解复用

- Owner 不需要手工整理上一次运行的 FeatureUnderstanding；
- WALL 复用现有 `WALL_FEATURE_UNDERSTANDING_PACKAGE.md` 并只核对 D1、D2、D4 影响的部分；
- F 从归档 Chat、旧实例材料和当前代码形成最小当前理解；
- 只有当前统计确实需要且旧材料缺失的事实才补齐；
- 不为形式完整重新查一遍全部代码，不把完整理解包重写设为运行前提。

## 7. 并行和等待

- WALL 与 F 可同时运行；
- 一条线返修、等待参数或等待 Owner 修改确认，不阻断另一条非冲突工作；
- 一条线先通过时，保存其 ReleasePackage，不重复跑；
- 两条基础线都达到 `PASS` 或 `PASS_WITH_ACCEPTED_LIMITATIONS` 后，才满足当前 Campaign 的基础释放条件。

## 8. 当前深度的停止条件

单条基础线可以结束本轮，当且仅当：

1. 最新锁定代码、参数、数据和正式范围已完整运行或经过同等严格的复用验证；
2. 最新全量统计已完成；
3. 原已知问题在最新版本上的状态已核实；
4. 新 finding 已关闭、转场景线、由 Owner 暂缓，或在形成修改方案后得到 Owner 明确处理决定；
5. 没有仍属本轮范围的 `OPEN_CONFIRMED_DEFECT`；
6. ReleasePackage 已形成。

这不是 Feature 全场景最终合理性的声明。
