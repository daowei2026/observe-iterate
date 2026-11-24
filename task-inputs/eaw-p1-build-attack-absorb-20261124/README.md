# EAW P1｜Build / AttackSegment / Absorb 三线统计闭环输入

> **状态：已准备任务输入与主控 GO 草案，尚未注册／启动新 Run。** 本目录不代表 Linux 工作区已准备、Wall 正式结果已取得、三个 Feature 已运行或 Release 已通过。
>
> 这些文件遵循旧版 `task-inputs/u2-fqv-observation/F_OBSERVATION_RUN_INPUT.md` 的简洁原则：**这里只给本轮 Feature、代码／实例／数据、业务来源、上下游与明确边界**；Workflow、专业执行步骤、机器协议和管理 Chat prompt 不复制到每个 Feature 输入中。

| 文件 | 用途 |
|---|---|
| [COMMON_INPUT.md](COMMON_INPUT.md) | 三线共同的业务范围、上游身份、代码、来源和目标 |
| [BUILD_RUN_INPUT.md](BUILD_RUN_INPUT.md) | Build 的目标实例及独立产物 |
| [ATTACK_RUN_INPUT.md](ATTACK_RUN_INPUT.md) | AttackSegment 的目标实例、F4 资格族及独立产物 |
| [ABSORB_RUN_INPUT.md](ABSORB_RUN_INPUT.md) | Absorb 的目标实例、已有历史与独立产物 |
| [MAIN_CONTROLLER_START_PROMPT.md](MAIN_CONTROLLER_START_PROMPT.md) | 给 cgpterm 主控的一次性 GO，含三个独立 Run、资源和工程授权 |

## 本轮关键决定

- **三个业务 Feature 并列**：共同依赖修复后 TIS 中的 exact Wall，上游还包含各自的附属计算／F4；Build、Attack、Absorb 互不读取对方的正式产物。按 P1 最终架构与现有 TIS `_impl` 核实。
- **不共用同一个可写 Run 工作区**：当前 `longrun/contracts/MULTI_RUN_CONTROLLER.md` 要求不同 run_id 使用不同且不重叠的真实路径。建议共用同一父目录、只读环境和可验证的 Wall artifact，但每 Run 拥有独立工作树、输出和提交分支。
- **基线范围**：建议沿用 11/23 Absorb 原任务的 `TA_updto20240229_DBA / rb,m / 2021 全年 / night_end_at_2300`，并在给主控的首次 GO 中明确采用；这不是从当前三个 Feature 的业务设计自然推导出来的范围。
- **代码修正只允许改本 Feature**：Build／Attack／Absorb 三条工作线不能改 Wall、F3/F4 或公共上游实现；发现上游问题只登记诊断及影响，不在本轮修复。
- **旧 Run 不自动接续**：本次使用新的 Run ID；旧 WALL 合理性 Run 没有 FeatureReleaseGate，旧 Absorb 的真实成果也不冒充新 Run 已完成。
- **当前仅正式运行 TIS P1 Feature producer**：`BuildAssembler`、`AttackFlowAssembler`、`AbsorbAssembler`。对应的 Haskell P1 DSU / Python FRP 包装是对象、身份、下游输出合同的来源，不因存在包装就把另一个完整 FRP Run 算入本轮完成。真实结果的读回与统计依各目标 Feature 的正式结果和 receipt。

本轮不包含重新跑 WALL 的独立合理性 Workflow、CAEGraph 观察图线、Exhaustion、P2/P3 或其它 Feature。必要的 exact Wall 物化只是三线的技术前置，不意味着完成墙的全面业务合理性审查。

**现有 Run 的版本不会随准备文件自动改变。** 新 GO 应统一采用其明确锁定的 observe-iterate 与 cgpterm exact commit。
