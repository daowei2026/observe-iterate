# 观察—分析业务控制面三层 Workflow（候选 V0.1）

**本分支用途**：先梳理完整业务任务（L0）、两条专业工作流（L1）、阶段内节点（L2）以及必要 Gate，再通过审查材料记录仍未闭合的控制问题。这是待确认的设计资料，**不代表已编写控制程序或完成真实业务试跑**。

## 目录与阅读顺序

| 目录 | 内容 | 性质 |
|---|---|---|
| [control/01 · L0 完整业务任务](control/01_L0_完整业务任务与双向衔接.md) | 材料准备 ↔ 合理性分析、总输入/输出、补证与任务收束 | 控制流程主体 |
| [control/02 · L1 材料准备](control/02_L1_观察材料准备流程.md) | S0～S5 阶段输入输出、运行与核验 | 控制流程主体 |
| [control/03 · L1 合理性分析](control/03_L1_合理性分析流程.md) | R0～R5、预期冻结、对照、诊断与标定循环 | 控制流程主体 |
| [control/04 · L2 工作节点](control/04_L2_节点输入输出登记表.md) | M01～M09、R01～R13 的输入输出与后继 | 控制流程主体 |
| [control/05 · 三级 Gate](control/05_三级Gate及后继路由.md) | L0/L1/L2 Gate、阻断与定向返修 | 控制流程主体 |
| [review/06 · 缺环审查](review/06_接口对齐与缺环审查.md) | 逐边对齐、潜在失效与尚未确认规则 | **审查记录**，不是已生效流程 |
| [review/07 · 控制判断与路径走查](review/07_待确认的控制判断与运行路径.md) | 管理判断候选、模拟路径与待确认事项 | **讨论和验证资料**，不是已生效规则 |

**已删除合订版。** 规则以各自独立文档为准，避免一套内容复制两份、修订不一致。06/07 与主体流程分目录管理。

## 专业 Skill 已纳入本分支

- [skills/observation-material-preparation/](skills/observation-material-preparation/README.md)：观察材料准备候选 Skill，保留专业方法、CAEGraph 引用、候选方法索引、任务单与示例。
- [skills/reasonableness-analysis/](skills/reasonableness-analysis/README.md)：合理性分析四个 Skill 及其协作说明。
- [reference-cases/](reference-cases/)：上述观察材料 Skill 引用的两份早期高频／EAW 方法分析讨论稿，作为案例依据，不当作本轮控制面正式规则。

本分支的专业依据**直接引用上述本地文件**，不再指向旧的 `main/discuss-materials/` Skill 路径。观察材料 Skill 仅对原有案例讨论稿链接改为本地相对路径，专业内容、相对目录结构和候选成熟度不变。引用外部 `uplot`、`viewer` 等实现仓库是技术依赖，不属于本次搬入范围。

## 本轮讨论确认的三处边界

**一份任务总输入**：`BusinessTaskInput` 记录已有业务目的、对象和约束；分析深度、完成条件中的未知项在任务开展中逐步明确，不要求额外再填一份 `TaskBoundary`。所谓“过程输入”就是上游节点的产物作为下游节点的输入，不在 L0 总输入表并列定义。

**L0 只负责材料交接**：材料准备交付真实数据、来源、版本、范围和限制。合理性分析在 R03 对探索样本、在 R05 对正式证据进行各自的输入检查；不把“可探索”和“正式使用”画成 M 的两个出口，也不取消正式对照需要冻结预期的专业约束。

**缺环不是已发生的运行故障**：`L0-D01`、`Cxx`、`Dxx` 是设计审查中发现的问题或待明确判断。需要区分：已发现、已提出候选规则、规则已确认、真实验证通过。**只有“提出了候选处理方式”不代表已经闭环**。

## 来源与状态

- 【S-M】[观察材料准备 Skill](skills/observation-material-preparation/SKILL.md)，原件 Git Blob `bd8698014ddf0feda273804ace336494ecba04b9`；[任务单](skills/observation-material-preparation/templates/观察材料准备任务单.md)，原件 `b571063fdd91e8b0818d64d25a403db037995580`。
- 【S-R】[合理性分析 Skill README](skills/reasonableness-analysis/README.md)，原件 Git Blob `8bd8c861317f4a66d3002b56eb0e9eee6f17b243`，四个 Skill 的原生状态和产物不由控制面改写。
- 【P】以往控制面落地计划提出的阶段/Gate 候选，**不是本分支外部文件的运行依赖**。
- 【N】本分支新增的三层控制逻辑、输入输出、交接和 Gate 候选；尚需确认与具体业务路径验证。

后续先检查每条“上游产物 → 下游最低输入”，再决定哪些判断可以被确定性实现、哪些需要专门控制判断；**本分支不做管理 Pro／程序／专业 Skill／Owner 的执行职责划分**。
