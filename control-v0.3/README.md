# 统计驱动的 Feature 闭环与下游释放｜V0.3

## 1. 用途

V0.3 服务于当前这类工作：

```text
先运行一个明确版本的 Feature
→ 用完整结果发现明显不合理点
→ 诊断并处理
→ 用修改后的完整实例重跑、重统计
→ 当前深度内不再出现新的明显问题
→ 释放精确上游版本给下游 Feature
```

它不替代 V0.2 的 CAEGraph、场景选择和过程证据对照。统计本身不足以判断的业务问题，仍可转入 `control/` 的观察材料与场景线。

## 2. 文件

| 文件 | 内容 |
|---|---|
| [01_L0_统计驱动的单特征闭环.md](01_L0_统计驱动的单特征闭环.md) | 单 Feature 从理解、运行、统计到问题关闭的主流程 |
| [02_L1_本特征释放与下游依赖.md](02_L1_本特征释放与下游依赖.md) | FeatureReleaseGate、已知限制、上游释放包、多 Run 汇合和下游失效 |
| [03_L2_节点输入输出与完成状态.md](03_L2_节点输入输出与完成状态.md) | 节点 I/O、状态和最小进度视图 |

专业方法继续来自现有 Skill：

- `skills/feature-understanding/`；
- `feature-global-behavior-profiling`；
- `business-discrepancy-diagnosis`；
- `feature-instance-calibration`（仅在确有标定任务时）。

V0.3 采用以下两份实践补充：

- `skills/feature-understanding/BUSINESS_OBJECT_QUALIFICATION_GUIDE.md`；
- `skills/reasonableness-analysis/STATISTICS_DRIVEN_PRACTICE.md`。

## 3. 减重原则

1. **不为运行 Feature 新建 Skill。** 运行是受 Owner 授权、带精确版本和结果绑定的实际动作。
2. **不为修代码新建 Skill。** 诊断完成后，按最小修改、反例复现、回归和全量新旧比较执行工程修正。
3. **不为多 Run 新建专业上级。** 各 Run 自己形成专业 Gate；主控只按任务输入中的依赖汇合。
4. **不把 WALL/F 的字段写进通用 Skill。** 通用 Skill 只规定怎样从对象、时间和处理链推导统计；品种、方向、年份和具体门槛由任务输入给出。
5. **不要求每轮都画图。** 只有统计不能判断、需要读取真实市场过程时才进入观察材料线。

## 4. 当前完成深度

每个 Run 必须声明 `CurrentReviewTarget`：

```yaml
current_goal:
intended_coverage:
explicit_non_goals:
owner_constraints:
current_acceptance_level:
```

本控制面允许当前目标只是“发现并关闭明显不合理问题”，不强迫在同一 Run 中完成复杂业务规则重构、全部覆盖证明或最终参数理论。未处理问题必须保留为已知限制，不能改写成不存在。

## 5. 采用方式

Owner GO 至少锁定：

```text
observe-iterate 精确 commit
control-v0.3
适用 Skill 和实践补充
Feature 代码 commit
参数实例
数据范围
独立 Linux 工作区
执行 profile
```

本次 WALL/F 具体输入见 `task-inputs/wall-f-parallel-closure-20261122/`。
