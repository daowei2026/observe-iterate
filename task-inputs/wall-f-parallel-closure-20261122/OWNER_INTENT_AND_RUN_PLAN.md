# Owner 意图与两线运行计划

## 1. 已明确的业务意图

当前重点是：

- 根据完整统计发现明显不合理问题；
- 把改法明确、成本合理的问题先处理；
- 修改后继续统计和发现问题；
- 暂时不把时间主要花在复杂、改法不确定、发生比例较低的规则重构上；
- WALL 与 F 两条基础线并行安排；
- 本特征达到当前深度后，再进入下游 Feature；
- manager 和 Skill executor 都在 Codex 运行，不使用 Worker。

该意图来自 Owner 当前消息及归档 Chat。AI 不把“暂缓复杂问题”改写为“复杂问题已经消失”。

## 2. Campaign 结构

```text
BASE-WALL ─┐
            ├─ JOINT_BASE_BARRIER
BASE-F ────┘
                 ├─ WALL downstream graph
                 └─ Q → V
```

基础 Run 是两个独立 Run，不建立跨 Run 专业 manager。

## 3. 两条线的 CurrentReviewTarget

### WALL

```yaml
current_goal:
  在问题1、2、4最终修正版上重新形成完整统计，确认旧问题状态，并继续发现明显结构不合理点。
intended_coverage:
  当前 WALL 业务对象链、正式输出一致性、身份、状态、生命周期、结束原因及关键分层。
explicit_non_goals:
  本轮不强制完成问题3所需的复杂生命周期规则重构；不证明所有复杂多价位场景均合理。
owner_constraints:
  问题3保留为已知限制；新发现仍按证据诊断，不因赶下游而忽略。
current_acceptance_level:
  最新完整统计中没有新的高置信结构 finding；已知问题已关闭或有明确 Owner 暂缓记录。
```

### F

```yaml
current_goal:
  使用 Owner 提供的新参数实例重跑 F，检查候选组及上游转化结构，继续发现明显合理性问题。
intended_coverage:
  输入转折、实际/确认/选择时间、相容关系、准入阻断、候选组创建与修订、品种和时期分层。
explicit_non_goals:
  本 Run 不重新证明新参数是最终最优标定；不把候选组数量增加当作修复充分条件；不优先展开复杂新规则设计。
owner_constraints:
  新参数实例由 Owner 提供并锁定；若统计出现新问题，逐项诊断。
current_acceptance_level:
  最新完整统计中没有新的高置信结构 finding；原迟确认准入问题在新实例上的实际结果已说明。
```

## 4. 并行和等待

- WALL 与 F 可同时运行；
- 一条线返修或等待，不阻断另一条非冲突工作；
- 一条线先通过时，保存其 ReleasePackage，不重复跑；
- 只有两条基础线都达到 `PASS` 或 `PASS_WITH_ACCEPTED_LIMITATIONS`，才满足本 Campaign 的联合 Barrier。

## 5. 当前深度的停止条件

单条基础线可以结束本轮，当且仅当：

1. 最新代码、参数、数据已完整运行或经过同等严格的复用验证；
2. 最新全量统计已完成；
3. 原已知问题在最新版本上的状态已核实；
4. 新 finding 已关闭、转场景线，或由 Owner 明确暂缓；
5. 没有仍属本轮范围的 `OPEN_CONFIRMED_DEFECT`；
6. ReleasePackage 已形成。

这不是 Feature 全场景最终合理性的声明。
