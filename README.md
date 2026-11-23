# 观察—分析业务控制面

本仓库同时保留两套可显式采用的控制面：

- `control/`：候选 V0.2，覆盖共享 Feature 理解、全量统计、观察材料和场景合理性全链；
- `control-v0.3/`：统计驱动的轻量闭环，优先完成“运行最新实例—做全量统计—关闭明显问题—重跑重统计—释放给下游”。

历史 Run、历史 Chat 和已经锁定 V0.2 的任务不因 V0.3 出现而自动升级。新 Run 必须在 Owner GO 中锁定实际采用的 commit、控制面、Skill 和任务输入。

## 阅读入口

| 入口 | 用途 |
|---|---|
| [control-v0.3/README.md](control-v0.3/README.md) | 当前统计驱动闭环与下游释放 |
| [task-inputs/wall-f-parallel-closure-20261122/](task-inputs/wall-f-parallel-closure-20261122/README.md) | WALL 与 F 两条线的本次任务输入 |
| [skills/feature-understanding/SKILL.md](skills/feature-understanding/SKILL.md) | 共享 Feature 对象、状态、事件、中间判断、参数和结果字段理解 |
| [业务对象判别补充](skills/feature-understanding/BUSINESS_OBJECT_QUALIFICATION_GUIDE.md) | 防止把运行配置、模块和计算步骤误当业务对象 |
| [skills/reasonableness-analysis/README.md](skills/reasonableness-analysis/README.md) | 合理性 Skill 入口 |
| [统计驱动实践补充](skills/reasonableness-analysis/STATISTICS_DRIVEN_PRACTICE.md) | 统计选择、抽样、诊断和标定的轻量通用规则 |
| [control/](control/01_L0_完整业务任务与双向衔接.md) | 原 V0.2 完整控制面 |
| [longrun/](longrun/README.md) | 多 Run、真实派发、独立工作区和 Codex 原生直执行 |

## V0.3 的取舍

V0.3 只增加真正影响业务分析质量或运行效率的内容：

1. 统计沿真实业务对象链比较上游、下游、位置和首次阻断，不只数最终输出；
2. 每个疑点独立诊断，代码符合当前规则与业务规则合理分开判断；
3. 行为变化后，旧运行和旧统计失效；
4. 基础 Feature 形成精确版本释放包后，下游才可以启动；
5. 不把看图和 CAEGraph 设为统计闭环前置；当前 V0.3 也不自动转入 V0.2 场景线，统计和现有证据不能判断的问题先记录为未决。

本轮明确不新增 Feature 执行 Skill、实现修正 Skill、Campaign schema 或自动调度器。Feature 运行是带版本绑定的实际动作；实现修正沿已有诊断结果进入普通工程修改和回归验证；两条线的并行与汇合由现有多 Run 控制器和本次任务输入完成。

## V0.2 继续独立有效

`control/` 仍保留完整路径：

```text
FeatureUnderstandingPackage
→ 运行 Feature
→ 全量行为统计
→ 问题闭环
→ 观察材料 B～E
→ 从图中选择真实场景
→ 场景过程证据对照
→ 新问题继续诊断
```

观察材料准备、CAEGraph 定义集成、真实核图和正式取数继续使用原 B～E Skills。但这些能力当前没有接入 V0.3 的自动后继；以后需要接入时，应另行明确入口、输入输出和采用条件。

## 版本和历史

- `task-inputs/` 只提供具体任务事实和边界，不替代通用 Skill；
- 新控制文件不回写历史 Run 的完成事实；
- 新代码、参数或数据提交不自动升级任何已启动 Run；
- 已启动 Run 仍以其 Owner GO 锁定的精确 commit 为准。
