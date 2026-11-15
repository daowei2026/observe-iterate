# 观察—分析业务控制面三层 Workflow（候选 V0.1）

**本分支用途**：L0 管完整任务及两条专业 Workflow 衔接；**材料准备 L1 已恢复为原专业 Skill 0～7 步的唯一正文**；R 与管理 I/O、Gate、完成全景仍保留独立文档。原先为 M 新设的 S0～S5 执行链、独立 S2/M05 和统一 G-RUN 门槛均不再适用。控制程序和真实长程 Run 的采纳须另核，不因本分支更新而自动改变历史 Run。

## 目录与阅读顺序

| 目录 | 内容 | 性质 |
|---|---|---|
| [control/01 · L0 完整业务任务](control/01_L0_完整业务任务与双向衔接.md) | 材料准备 ↔ 合理性分析、总输入/输出、补证与任务收束 | 控制流程主体 |
| [control/02 · 材料准备专业方法正文](control/02_L1_观察材料准备流程.md) | **原上位 Skill 的完整执行步骤 0～7**：调查→处理骨架→材料取舍→方法→最小落地→真实取数→核验→交接 | **M 唯一专业执行来源** |
| [control/03 · L1 合理性分析](control/03_L1_合理性分析流程.md) | R0～R5、预期冻结、对照、诊断与标定循环 | 控制流程主体 |
| [control/04 · L2 工作成果 I/O](control/04_L2_节点输入输出登记表.md) | **M 原 Skill 0～7 步与 R 节点的真实输入输出、消费资格和准确后继**；旧 Mxx 仅用于历史回溯 | 管理 Pro 安排、验收与进度对照，不另定义专业方法 |
| [control/05 · 三级 Gate](control/05_三级Gate及后继路由.md) | L0/L1/L2 Gate、阻断与定向返修 | 控制流程主体 |
| [control/06 · 业务完成全景](control/06_业务完成全景与更新协议.md) | 节点→阶段→M/R→业务问题→父任务的当前完成情况、更新触发、阻断与恢复 | **跨三层共用控制机制（候选）** |
| [review/06 · 缺环审查](review/06_接口对齐与缺环审查.md) | 逐边对齐、潜在失效与尚未确认规则 | **审查记录**，不是已生效流程 |
| [review/07 · 控制判断与路径走查](review/07_待确认的控制判断与运行路径.md) | 管理判断候选、模拟路径与待确认事项 | **讨论和验证资料**，不是已生效规则 |
| [longrun/ · 长程协作](longrun/README.md) | C/D/W 运行合同、机械校验、负责人/执行人专业角色指南 | **V2 候选运行层**，尚未完成真实联调；角色指南亦是本次候选适配 |

**业务完成全景是任务的持续视图，而不是只在最终交付时汇总。** 每当节点结果被合法接收、阶段 Gate 形成结论或补证/失效改变进展，必须基于已核实事实刷新受影响范围，详情见 [control/06](control/06_业务完成全景与更新协议.md)。当前只是规则候选，没有创建运行期状态或程序。

**已删除合订版。** 规则以各自独立文档为准，避免一套内容复制两份、修订不一致。06/07 与主体流程分目录管理。

## 专业 Skill、候选方法与技术资料归档

| 类别 | 入口 | 作用与保留理由 |
|---|---|---|
| **M 专业正文唯一来源** | [control/02 · 观察材料规划与准备](control/02_L1_观察材料准备流程.md) | **从原 Skill 完整迁入 0～7 步**；只修迁移后的相对链接，不另增步骤 |
| **兼容 Skill 入口** | [observation-material-preparation/SKILL.md](skills/observation-material-preparation/SKILL.md) | 仅索引到 control/02 及技术参考/模板，**不再重复专业正文** |
| **执行技术参考** | [CAEGraph 真实取数与核验](skills/observation-material-preparation/references/CAEGraph执行取数与验证.md) | 构图/视窗/源值等不同数据阶段、执行接口和质量验证；不是具体候选观察方法 |
| **任务产物模板** | [观察材料准备任务单](skills/observation-material-preparation/templates/观察材料准备任务单.md) | 记录业务处理阶段、材料必要性、取数、缺口与交接；保留 |
| **候选方法组索引** | [S1～S4、E1～E4 方法索引](skills/observation-method-candidates/README.md) | 唯一的触发条件、跨用例对应关系及成熟度目录；从上位 Skill 的 references 移出 |
| **高频候选 Skill 初稿** | [标准化高频四候选](skills/observation-method-candidates/四个候选观察准备Skill_标准化高频用例落地与复用边界_20261112.md) | S1～S4 的专业方法、落地证据、复用限制；是候选 Skill 研究稿，不是普通案例 |
| **EAW 候选 Skill 初稿** | [EAW CAEGraph 候选](skills/observation-method-candidates/EAW_CAEGraph观察准备Skill候选_原图落地与复用边界_20261112.md) | E1/E3 新候选及 E2/E4 对 S3/S4 的复用核查；同样是候选 Skill 研究稿 |
| **合理性分析** | [四个合理性分析 Skill](skills/reasonableness-analysis/README.md) | 已迁入的四个专业 Skill 及协作协议，本轮不改动 |

**旧观察准备文件夹的保留理由**：`skills/observation-material-preparation/SKILL.md` 仅是**兼容调用入口**，指向 control/02，不再复制专业步骤；同目录 `references/CAEGraph执行取数与验证.md` 和 `templates/观察材料准备任务单.md` 是仍有实际用途的技术参考与成果模板。整体删除会损失依赖文件及现有 Pro/主控的 SKILL 路径。此前已经删除的 examples/、reference-cases/ 和重复导航 README 保持不恢复。

**性质边界**：高频、EAW 两份稿原文都明确是初版候选、未证明跨真实用例稳定复用，不能因重新归档就冒充正式可直接执行的独立 `SKILL.md`。保留原稿的研究和来源信息，必要的改动仅用于修复本分支相对链接。当前 control/02 专业正文仍通过索引选用方法，不要求拆开已有完整 CAEGraph 重做。

技术上仍可能需要引用 `viewer`、`uplot` 等外部源码或手册；它们是外部技术依赖，不是旧版观察材料 Skill 的地址。本分支内的专业资料互相引用均转为本地相对路径。

## EAW Wall 任务资料（非通用 Skill）

下列三份是本分支 `task-inputs/eaw-p1-wall-lifecycle/` 中现有的**用例资料**，不代替 Owner 任务目标或原专业方法；其中脚本绑定的是一个具名默认实例，实际能否在新运行工作区取得并读取数据需要按运行结果核实。

- [无二义性需求和实现文件](task-inputs/eaw-p1-wall-lifecycle/无二义性需求和实现文件.md)：沿输入链区分需求、实现事实及待确认项。
- [设计文件](task-inputs/eaw-p1-wall-lifecycle/设计文件.md)：原设计依据和差异线索。
- [实例运行脚本](task-inputs/eaw-p1-wall-lifecycle/实例运行脚本.py)：已写明运行上下文、既有产物命中前置、正式 `.run()` / `.F` 读取和输出报告；不能仅因脚本存在而宣称本轮取数成功。

## 本轮讨论确认的三处边界

**一份任务总输入**：`BusinessTaskInput` 记录已有业务目的、对象和约束；分析深度、完成条件中的未知项在任务开展中逐步明确，不要求额外再填一份 `TaskBoundary`。所谓“过程输入”就是上游节点的产物作为下游节点的输入，不在 L0 总输入表并列定义。

**L0 只负责材料交接**：材料准备交付真实数据、来源、版本、范围和限制。合理性分析在 R03 对探索样本、在 R05 对正式证据进行各自的输入检查；不把“可探索”和“正式使用”画成 M 的两个出口，也不取消正式对照需要冻结预期的专业约束。

**缺环不是已发生的运行故障**：`L0-D01`、`Cxx`、`Dxx` 是设计审查中发现的问题或待明确判断。需要区分：已发现、已提出候选规则、规则已确认、真实验证通过。**只有“提出了候选处理方式”不代表已经闭环**。

## 来源与状态

- 【S-M】[原 Skill 0～7 步专业正文现址](control/02_L1_观察材料准备流程.md)，本次从旧 [Skill 入口](skills/observation-material-preparation/SKILL.md) 原专业正文原样迁移（仅三条相对链接调整）；[任务单](skills/observation-material-preparation/templates/观察材料准备任务单.md)，原件 `b571063fdd91e8b0818d64d25a403db037995580`。
- 【S-R】[合理性分析 Skill README](skills/reasonableness-analysis/README.md)，原件 Git Blob `8bd8c861317f4a66d3002b56eb0e9eee6f17b243`，四个 Skill 的原生状态和产物不由控制面改写。
- 【P】以往控制面落地计划提出的阶段/Gate 候选，**不是本分支外部文件的运行依赖**。
- 【N】本分支新增的三层控制逻辑、输入输出、交接和 Gate 候选；尚需确认与具体业务路径验证。

后续先检查每条“上游产物 → 下游最低输入”，再决定哪些判断可以被确定性实现、哪些需要专门控制判断。**本目录的 control/ 流程本身不分配管理 Pro／程序／专业 Skill／Owner 的正式 Gate 权限**；[longrun/professional/](longrun/professional/README.md) 仅提供针对新版双 Pro 的**候选角色工作指南**，不改变上述控制源与未决权限。
