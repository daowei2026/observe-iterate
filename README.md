# 观察—分析业务控制面三层 Workflow（候选 V0.1）

**本分支用途**：L0 管完整任务及材料准备／合理性分析两条专业 Workflow 的衔接；材料准备 L1 采用 A～E 外层 Workflow，并由五个阶段 Skill 分别定义专业工作；R 与管理 I/O、Gate、完成全景仍保留独立文档。控制程序和真实长程 Run 的采纳须另核，不因本分支更新自动改写历史 Run。

## 目录与阅读顺序

| 目录 | 内容 | 性质 |
|---|---|---|
| [control/01 · L0 完整业务任务](control/01_L0_完整业务任务与双向衔接.md) | 材料准备 ↔ 合理性分析、总输入/输出、补证与任务收束 | 控制流程主体 |
| [control/02 · L1-M 材料准备外层 Workflow](control/02_L1_观察材料准备流程.md) | **A 特征 occurrence 理解 → B 观察位置／C 展示方式 → D CAEGraph 定义集成 → E 执行、核图和取数** | M 外层阶段与 I/O 权威来源 |
| [control/03 · L1-R 合理性分析](control/03_L1_合理性分析流程.md) | R0～R5、预期冻结、对照、诊断与标定循环 | 控制流程主体 |
| [control/04 · L2 工作成果 I/O](control/04_L2_节点输入输出登记表.md) | M 的 A～E 阶段成果和 R 节点的真实输入输出、消费资格和准确后继 | 管理安排、验收与进度对照 |
| [control/05 · 三级 Gate](control/05_三级Gate及后继路由.md) | L0/L1/L2 Gate、阻断与定向返修 | 控制流程主体 |
| [control/06 · 业务完成全景](control/06_业务完成全景与更新协议.md) | 阶段／工作实例→M/R→业务问题→父任务的当前完成情况、阻断与恢复 | 跨三层共用控制机制（候选） |
| [review/06 · 缺环审查](review/06_接口对齐与缺环审查.md) | 逐边对齐、潜在失效与尚未确认规则 | 审查记录，不是已生效流程 |
| [review/07 · 控制判断与路径走查](review/07_待确认的控制判断与运行路径.md) | 管理判断候选、模拟路径与待确认事项 | 讨论和验证资料 |
| [longrun/ · 长程协作](longrun/README.md) | C/D/W 单 Run 协议、多 Run 主控合同、独立 Linux 工作区和跨 Run 校验 | V2 + 多 Run 候选运行层 |

**业务完成全景是持续视图，不是只在最终交付时汇总。** 每当阶段结果被接收、Gate 形成结论或补证／失效改变进展，必须基于已核实事实刷新受影响范围，详情见 [control/06](control/06_业务完成全景与更新协议.md)。

## 观察材料准备：外层 Workflow 与五个 Skill

### 外层 Workflow

[control/02](control/02_L1_观察材料准备流程.md) 只规定：

```text
外层输入：特征名称、特征代码版本、特征实例

A 特征事件级 occurrence 理解
    ├─→ B 观察位置准备
    └─→ C 展示方式准备
B + C + A
    → D CAEGraph 定义集成
    → E CAEGraph 执行／运行
    → 最终脚本、HTML、图数据和核对结果
```

A～E 各阶段都有独立专业 Skill。B 当前只沉淀了普通默认和高频多尺度两种经验性用法，不冒充成熟通用 Workflow；D 当前只有一个集成动作，不再设置内部 Workflow。

### 总入口与阶段 Skill

| 类别 | 入口 | 作用 |
|---|---|---|
| **M 总入口** | [observation-material-preparation/SKILL.md](skills/observation-material-preparation/SKILL.md) | 索引外层 Workflow、五个阶段 Skill、技术参考和模板 |
| **A occurrence 理解** | [feature-occurrence-understanding](skills/observation-material-preparation/feature-occurrence-understanding/SKILL.md) | 输入／输出事件级 occurrence、各事件发生位置、业务主输出／中间处理结果、处理关系 |
| **B 观察位置** | [observation-position-preparation](skills/observation-material-preparation/observation-position-preparation/SKILL.md) | 普通特征沿用固定 SOF，默认钢铁板块和 2021-01-01～2022-12-31；高频特征复用 1d→30m→1m→5s→tick 位置层级 |
| **C 展示方式** | [caegraph-display-preparation](skills/observation-material-preparation/caegraph-display-preparation/SKILL.md) | 先理解 CAEGraph，再形成展示预期；复杂点循环求解；最后产出位置与实例可注入代码、实例注入合同和预期 HTML |
| **D 定义集成** | [caegraph-definition-integration](skills/observation-material-preparation/caegraph-definition-integration/SKILL.md) | 充分理解锁定 CAEGraph 仓库后，根据外层输入和 A／B／C 输出一次性形成完整定义 |
| **E 执行／运行** | [caegraph-execution](skills/observation-material-preparation/caegraph-execution/SKILL.md) | E 自己完成专业判断；真实运行／有限修复用 W1，核图接受后的正式取数用 W2 |

### 阶段目录结构

有真实内部步骤的阶段通常采用：

```text
SKILL.md
    阶段定位、边界、输入输出概览、完成条件和禁止事项
WORKFLOW.md
    内部步骤、步骤目标和步骤内的专业判断方法
IO_SPEC.md
    字段级输入输出
```

当前例外：

- B 的 `WORKFLOW.md` 只记录当前两种经验性用法，不构造没有实际意义的 B1、B2；
- D 不设 `WORKFLOW.md`，只有 `SKILL.md + IO_SPEC.md`；
- E 除专业 `WORKFLOW.md` 外，另有 [Worker 派单合同](skills/observation-material-preparation/caegraph-execution/WORKER_DELEGATION.md)和两份工单模板。

专业判断方法不是另一条平行流程；它写在真正使用该判断的内部步骤下。跨多个步骤且篇幅很大的方法才进入 Reference。

## 技术参考、模板和候选方法

| 类别 | 入口 | 作用与边界 |
|---|---|---|
| **C 展示能力参考** | [CAEGraph 展示能力与构建速查](skills/observation-material-preparation/references/CAEGraph展示能力与构建速查.md) | 从锁定版本手册提取构建链、布局类、绘图类和使用／能力缺口区分；不替代原手册 |
| **D 仓库集成参考** | [CAEGraph 仓库结构与定义集成参考](skills/observation-material-preparation/references/CAEGraph仓库结构与定义集成参考.md) | uplot 仓库文件地图、实例／位置／字段到 PlotCtx、CDS、数据树和动态链的真实集成边界 |
| **B 高频位置参考** | [高频多尺度观察位置参考](skills/observation-material-preparation/observation-position-preparation/MULTISCALE_POSITION_REFERENCE.md) | 只复用既有脚本的 1d→30m→1m→5s→tick 位置层级和父子关系，不复用图内容 |
| **E 技术参考** | [CAEGraph 执行、核图与取数](skills/observation-material-preparation/references/CAEGraph执行取数与验证.md) | 构图／视窗／源值等数据阶段、最终图核对、核图后正式取数和一致性验证 |
| **E Worker 派单** | [Worker 派单合同](skills/observation-material-preparation/caegraph-execution/WORKER_DELEGATION.md) | 区分 W1 运行修复与 W2 正式取数，避免提前授权正式数据导出 |
| **任务记录模板** | [观察材料准备任务记录](skills/observation-material-preparation/templates/观察材料准备任务单.md) | 汇总 A～E 产物和最终交付；字段细节仍以各 `IO_SPEC.md` 为准 |
| **候选方法组索引** | [S1～S4、E1～E4 方法索引](skills/observation-method-candidates/README.md) | 候选观察方法的触发条件、跨用例对应关系和成熟度；不是固定必经流程 |
| **高频候选初稿** | [标准化高频四候选](skills/observation-method-candidates/四个候选观察准备Skill_标准化高频用例落地与复用边界_20261112.md) | S1～S4 的研究稿与复用限制 |
| **EAW 候选初稿** | [EAW CAEGraph 候选](skills/observation-method-candidates/EAW_CAEGraph观察准备Skill候选_原图落地与复用边界_20261112.md) | E1/E3 新候选及 E2/E4 复用核查 |
| **合理性分析** | [四个合理性分析 Skill](skills/reasonableness-analysis/README.md) | 预期、对照、诊断、标定的专业方法；本次不改其语义 |

技术上仍可能引用 `viewer`、`uplot` 等外部源码或手册；它们是技术依赖，不是用例输入。具体品种、时间、实例属于用例事实，不进入通用 Skill。

## A～E 的关键边界

- A 的“事件发生位置”说明每类 Event 自己在哪里发生以及 occurrence 携带哪些位置；B 的“观察位置”给最终图提供普通默认位置或高频多尺度位置，二者不能混同。
- B 当前是经验性用法，不从 occurrence 中强行挑选所谓“典型案例”；高频参考只借位置层级，不借图层和展示逻辑。
- C 可以只读使用外层特征实例理解数据形状或生成预览 HTML，但正式代码必须保留实例注入接口；不能固化最终实例。
- D 是一个单一动作：理解本次所需 CAEGraph 仓库调用链，把外层真实实例、A 字段、B 位置注入 C 代码，形成完整定义；D 不派 Worker。
- E 的专业 Workflow 与 Worker 操作分开。W1 负责真实运行和权限内修复；E 专业核图；W2 只在核图接受后正式取数据。
- E 必须用 D 核对最终脚本、用 C 展示预期／HTML 核对最终图；图被接受后才形成正式取数准入。
- `PLAN_READY` 不能冒充 `DATA_READY`。语法检查、静态定义、少量预览和未核对 HTML 都不等于真实观察材料已完成。

## L0 与 R 的边界

**一份任务总输入**：`BusinessTaskInput` 记录完整业务任务的目标、对象和约束；M 自身的外层输入由 `control/02` 规定。阶段产物作为后继输入，不与总任务输入混称。

**L0 只负责材料交接**：M 交付实际图、数据、来源、版本、范围、核对和限制。R 在探索与正式对照节点按自身用途检查消费资格；M 不替 R 判断合理性，也不预选 R 的探索／正式分支。

**缺环不是已发生的运行故障**：review 中的问题和候选规则只有经过确认和真实验证才算闭环。

## 用例资料与历史记录

`task-inputs/` 下文件是具体用例输入，不替代 A～E 的通用 Workflow 和 Skill。历史 `longrun/runs/`、旧报告或聊天中出现“0～7 步”属于当时事实，不回写历史；新工作以本分支当前 A～E 规则为准。

## 来源与状态

- 【S-M】[当前材料准备外层 Workflow](control/02_L1_观察材料准备流程.md)及 A～E 五个阶段 Skill。
- 【S-R】[合理性分析 Skill README](skills/reasonableness-analysis/README.md)及四个 Skill；其原生状态和产物不由 M 控制面改写。
- 【N】本分支三层控制逻辑、A～E 细分、输入输出和 Gate 候选；仍需通过真实用例验证。

后续仍应逐边检查“上游产物 → 下游最低输入”。`control/` 不自行分配管理 Pro、执行 Pro、程序、Worker 或 Owner 的最终权限；[longrun/professional/](longrun/professional/README.md) 是角色适配指南，不改变专业源文档。
