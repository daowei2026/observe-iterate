# 长程专业角色指南（候选 V0.1）

本目录回答“专业负责人 Pro / 专业执行人 Pro 的**专业工作**到底做什么”；它不是第二套长程运行协议，也不是一套独立的观察/合理性分析 Skill。正式 C/D/W 派发和 Return 以 [长程 V2 协议](../contracts/LONGRUN_PROTOCOL_V2.md) 为准。

## 按角色读取

| 角色 | 文件 | 业务工作 |
|---|---|---|
| 专业负责人 Pro（manager） | [PRO_MANAGER_GUIDE.md](PRO_MANAGER_GUIDE.md) | 完整问题、材料准备 ↔ 合理性分析的工作组织和结果接收、具名补证、受限返修、逐问题收束；不当作普通消息转发员 |
| 专业执行人 Pro（executor） | [PRO_EXECUTOR_GUIDE.md](PRO_EXECUTOR_GUIDE.md) | 根据当前 D，使用**已有**观察材料准备 Skill 或合理性分析 Skills 进行实际专业工作；必要时签 W 并审查 Worker 实物，完整回交专业成果 |

**一次实际专业调用不等于一个 S/R 阶段、一个 M/R 节点或一个业务材料要求。** manager 负责组织 D，executor 可以在授权的一个 D 内跨若干相邻工作步骤、调用零个或多个 W，均要清楚表明实际成果。

## 必须仍以原业务源为准

- [观察材料准备 Skill](../../skills/observation-material-preparation/SKILL.md)：从业务骨架规划输入/关键中间阶段/输出，选择必要材料、真实取数和核验、分四类状态交付。
- [合理性分析 Skills README](../../skills/reasonableness-analysis/README.md)：最小预期与探索、冻结后正式对照、值得才诊断、可调才标定、必要的结果反馈；四个各自的 Skill 是专业方法原件。
- [L0 完整业务任务](../../control/01_L0_完整业务任务与双向衔接.md)、[L1-M](../../control/02_L1_观察材料准备流程.md)、[L1-R](../../control/03_L1_合理性分析流程.md)、[L2 I/O](../../control/04_L2_节点输入输出登记表.md)、[Gate](../../control/05_三级Gate及后继路由.md)：目前是**候选控制设计**，专业角色指南不能把它们升级为正式权限。
- [审查与未决](../../review/06_接口对齐与缺环审查.md)、[运行路径走查](../../review/07_待确认的控制判断与运行路径.md)：尚缺真实任务范围、用途资格、补证退出、重复复验身份及正式 Gate 接受等决定。
- **历史设计参考**：`main/discuss-materials/observe_iterate_control_plane_implementation_plan_v0.2_20261113.md` 的管理 Pro 合同。它是历史候选方案，不能覆盖上述当前分支的修订边界，也不能把其中建议的控制核心或 `advance` 声称为已实现。

## 哪些属于“已有业务源”，哪些是这次新增的角色适配

**直接继承**：材料准备 0～7 步、可复用图优先、实际取数/验证、材料四种交付状态；合理性分析四 Skill 及预期三种来源、冻结协议、证据六种状态、参数可修复性状态；L0 补证回原问题和逐问题收束等候选 I/O。

**本次新增、待角色层验证**：把完整业务任务及跨阶段工作组织定位给 manager；把真实专业分析及 Worker 工单专业接收定位给 executor；规定 D 应当携带何种专业最小任务信息、manager 怎样以有限专业复核结果组织后继。该分配符合用户新增双 Pro 的意图，但**当前三层业务控制面没有预先将每一个 Gate 正式授权给某个角色**。

## 最小使用方式

1. 主控根据**同一 Run 已锁定的精确提交**，把本目录 manager 指南引用放进首轮 manager 的完整任务来源；executor 首轮完整任务含 D 正文、executor 指南、适用的具体专业 Skill 和现有证据。
2. manager 只签具名专业 D；executor 自己读专业 Skill 并判断需要什么真实工作，必要时签 W；Worker 结果先回 executor，再由 executor 按 D 的专业标准交 manager。
3. 交回必须引用真实的专业原生结果、限制和未决，不能用两份角色指南代替 Gate、授权、数据或结果。
4. 专业指南变更不能静默更新既有 Run；采用时固定 commit。Skill 文档本身不产生新 Run、真实专业决定或后台自动执行。

## 明确未完成

当前新指南没有经过真实 manager→executor→worker→executor→manager 多轮验证；cgpterm 的物理消息、专业执行侧工具可用性、受保护业务状态/独立复核及正式 Gate 权限仍需实测和有权确定。
