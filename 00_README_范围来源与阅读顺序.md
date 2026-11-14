# 观察—分析业务控制面：三层 Workflow、输入输出与闭环审查（候选 V0.1）

**日期**：2026-11-14。**性质**：可供后续讨论、确认和实施的控制逻辑设计稿；不是已获批准的执行合同，不代表代码或真实运行已经完成。**本包只梳理控制面的业务流程、节点、I/O、Gate、异常和缺环，不分配管理 Pro／程序／专业 Skill／Owner 的具体执行职责，也不实现代码或修改现有 Skill。**

## 1. 首先确定三层，不从执行者开始设计

| 层次 | 管理对象 | 最重要的问题 | 文档 |
|---|---|---|---|
| L0 完整业务任务 | 观察材料准备 ↔ 合理性分析，以及整体目标、任务完成 | 上游怎样交给下游？下游缺证怎样回上游？什么算整体交付？ | `01_L0_完整业务任务与双向衔接.md` |
| L1 两条内部 Workflow | 材料准备 S0～S5；合理性分析 R0～R5（均为管理视图） | 各阶段真正消费和产出什么？各阶段在什么条件下推进／返修？ | `02_L1_观察材料准备流程.md`、`03_L1_合理性分析流程.md` |
| L2 阶段内部工作节点 | 可命名的调查、规划、取数、核验、预期、对照、诊断、标定等工作 | 工作节点的前置条件、业务产物、局部门禁和失效后继是什么？ | `04_L2_节点输入输出登记表.md` |

横贯三层的验收和闭环审查：`05_三级Gate及后继路由.md`、`06_接口对齐与缺环审查.md`、`07_待确认的控制判断与运行路径.md`。

**阶段不是一次模型调用的单位，材料项也不等于执行工作项。** 例如一次完整 CAEGraph 运行可能同时覆盖多个材料项；R4 标定中的完整实例复验可以使用 R2 对照能力，不必为 R4、R2 复制两轮相同计算。本文的 L2 是需要管理其输入输出的逻辑工作节点，不强制每个节点独立派发 Prompt 或新增 Gate。

## 2. 来源及非来源；准确划线

- 【S-M】[观察材料规划与准备 Skill 候选 V0.1](https://github.com/daowei2026/observe-iterate/blob/main/discuss-materials/观察材料规划与准备Skill_候选V0.1_20261113/SKILL.md)，以及[观察材料准备任务单](https://github.com/daowei2026/observe-iterate/blob/main/discuss-materials/观察材料规划与准备Skill_候选V0.1_20261113/templates/观察材料准备任务单.md)。读取时源码 blob SHA 分别为 `bd8698014ddf0feda273804ace336494ecba04b9`、`b571063fdd91e8b0818d64d25a403db037995580`。源定义专业方法、必需/条件/建议材料、数据阶段和交付标签。
- 【S-R】[合理性分析 Skills V0.1 README](https://github.com/daowei2026/observe-iterate/blob/main/discuss-materials/reasonableness-analysis-skills-v0.1/README.md)，含四个 Skill：`business-expectation-derivation`、`business-evidence-comparison`、`business-discrepancy-diagnosis`、`feature-instance-calibration`。README blob SHA `8bd8c861317f4a66d3002b56eb0e9eee6f17b243`。其来源、冻结、六种证据状态、参数路由及多轮循环应原样保留；具体见上述四个各自的 `SKILL.md`。
- 【P】[当前控制面落地计划（路径沿用 V0.1，内容标题为修订候选 V0.2）](https://github.com/daowei2026/observe-iterate/blob/main/discuss-materials/observe_iterate_control_plane_implementation_plan_v0.1_20261113.md)。读取时 blob SHA `99186485e78d8ba1dc9289d6e4deb5cda2b3ddce`。它提出的 S0～S5/R0～R5、三级就绪、交接与补证、真实回执等是**候选控制设计**，不是专业 Skill 的已有状态。
- 【N】本包新增的 L0/L1/L2 边、控制判断点、I/O 适配封面、Gate 结果路径、退出条件和缺环审查。这些是**待确认控制面设计**，不能倒写成源 Skill 已经规定。

**刻意不做**：不检查或采用 `observe-iterate` 的旧 `professional/`、`runtime/`、`runs/` 作为现行系统；不改外部长程 Codex 主控；不分析管理 Pro、控制程序、专业执行者、Owner 的职责分配；不展开 CAEGraph 实际算法和合理性分析的专业判断方法；不代替业务方决定真实项目的观察问题与完成范围。

## 3. 控制层必须统一的基本语义（【N】）

- **业务任务** `ParentTask`：本轮要回答的一组具名问题，明确 `required_questions / allowed_depth / accepted_unresolved / future_questions_boundary`。不应因为遇到新问题而无上限扩充任务。
- **阶段视图** `StageView`：S0～S5 或 R0～R5，用于进展表达；一个专业调用可跨多个相邻步骤、一个阶段可有若干调用。
- **节点** `ControlNode`：具有触发、输入、产出及后继的工作边界；不是技术函数分解。
- **材料要求** `MaterialRequirement`：本轮需要哪些可观察数据；**工作项** `WorkItem`：怎样组织一次具体调查/加工/对照工作；**执行动作** `ExecutionAction`：某次实际运行或调用。三者非一一对应。
- **候选结果与正式接受**：Skill 的 `PLAN_READY/DATA_READY/PARTIAL_WITH_LIMITS/BLOCKED` 是其交付标签；不是控制面 Gate 的正式决定。证据 `SUPPORTS/COUNTERS/MISSING/AMBIGUOUS/NOT_APPLICABLE/PENDING` 是领域结果，不是 Gate PASS/FAIL。
- **Gate**：对某个明确对象的进入/接受资格进行判定；如果规则不足，则产出具名待判决问题，而不是默默选择下一步。并非所有节点都需要单独 Gate。
- **闭环**：每个节点/阶段在成功、部分、失败、不可得、超范围、等待等情况下，必须有明确的结果对象、目标接收方、下一步资格、重新启动条件和结束路径；允许如实阻断，但不能无解释地悬空等待。

## 4. 本包与后续实施的关系

本包是**上游业务控制逻辑**，应该先检查每条边和 Gate 是否完备。确认后，才将其中可确定的规则转为 Workflow/状态/验证配置，将确实需要非确定性管理判断的点转为专门的管理任务。**本轮不做这一步划分。**

建议后续审核顺序：先读 L0，确认两个业务部分之间的可达路径；再逐一核对 L1 阶段是否有输入来源和输出消费者；然后对 L2 的每个节点按 `输入是否可得 → 输出是否有定义 → 下一步是否有人消费 → 失败是否能收束` 检查；最后审查 Gate 与缺环表。对每个尚待确认的关键判断，见 `07_待确认的控制判断与运行路径.md`。
