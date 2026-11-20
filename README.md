# 观察—分析业务控制面三层 Workflow（候选 V0.1）

**本分支用途**：L0 管完整任务及材料准备／合理性分析两条专业 Workflow 的衔接；材料准备 L1 采用 A～E 外层 Workflow，并由五个阶段 Skill 分别定义专业工作；R 与管理 I/O、Gate、完成全景仍保留独立文档。控制程序和真实长程 Run 的采纳须另核，不因本分支更新自动改写历史 Run。

## 目录与阅读顺序

| 目录 | 内容 | 性质 |
|---|---|---|
| [control/01 · L0 完整业务任务](control/01_L0_完整业务任务与双向衔接.md) | 材料准备 ↔ 合理性分析、总输入／输出、补证与任务收束 | 控制流程主体 |
| [control/02 · L1-M 材料准备外层 Workflow](control/02_L1_观察材料准备流程.md) | **A occurrence 理解 → B 观察位置／C 展示方式 → D CAEGraph 定义集成 → E 执行、核图和取数** | M 外层阶段与 I/O 权威来源 |
| [control/03 · L1-R 合理性分析](control/03_L1_合理性分析流程.md) | R0～R5、预期冻结、对照、诊断与标定循环 | 控制流程主体 |
| [control/04 · L2 工作成果 I/O](control/04_L2_节点输入输出登记表.md) | M 的 A～E 阶段成果和 R 节点的真实输入输出、消费资格和后继 | 管理安排、验收与进度对照 |
| [control/05 · 三级 Gate](control/05_三级Gate及后继路由.md) | L0/L1/L2 Gate、阻断与定向返修 | 控制流程主体 |
| [control/06 · 业务完成全景](control/06_业务完成全景与更新协议.md) | 阶段／工作实例→M/R→业务问题→父任务的完成情况、阻断与恢复 | 跨三层共用控制机制（候选） |
| [review/06 · 缺环审查](review/06_接口对齐与缺环审查.md) | 逐边对齐、潜在失效与尚未确认规则 | 审查记录，不是已生效流程 |
| [review/07 · 控制判断与路径走查](review/07_待确认的控制判断与运行路径.md) | 管理判断候选、模拟路径与待确认事项 | 讨论和验证资料 |
| [longrun/ · 长程协作](longrun/README.md) | C/D/W 协议、多 Run 主控合同、独立 Linux 工作区和跨 Run 校验 | V2 + 多 Run 候选运行层 |

**业务完成全景是持续视图，不是只在最终交付时汇总。** 每当阶段结果被接收、Gate 形成结论或补证／失效改变进展，必须基于已核实事实刷新受影响范围，详情见 [control/06](control/06_业务完成全景与更新协议.md)。

## 观察材料准备：外层 Workflow 与五个 Skill

### 外层 Workflow

```text
外层输入：特征名称、特征代码版本、特征实例

A 特征事件级 occurrence 理解
    ├─→ B 观察位置准备
    └─→ C 展示方式准备
A + B + C
    → D CAEGraph 定义集成
    → E CAEGraph 执行／运行
    → 最终脚本、HTML、图数据和核对结果
```

A～E 各阶段都有独立专业 Skill。B 当前只沉淀普通默认和高频多尺度两种经验性用法；D 当前只有一个集成动作，不设置内部 Workflow。

### 总入口与阶段 Skill

| 类别 | 入口 | 作用 |
|---|---|---|
| **M 总入口** | [observation-material-preparation/SKILL.md](skills/observation-material-preparation/SKILL.md) | 索引外层 Workflow、五个阶段 Skill、技术参考和模板 |
| **A occurrence 理解** | [feature-occurrence-understanding](skills/observation-material-preparation/feature-occurrence-understanding/SKILL.md) | 输入／输出 occurrence、各事件发生位置、业务主输出／中间处理结果和处理关系 |
| **B 观察位置** | [observation-position-preparation](skills/observation-material-preparation/observation-position-preparation/SKILL.md) | 普通特征沿用固定 SOF，默认钢铁板块和 2021-01-01～2022-12-31；高频特征复用 1d→30m→1m→5s→tick 位置层级 |
| **C 展示方式** | [caegraph-display-preparation](skills/observation-material-preparation/caegraph-display-preparation/SKILL.md) | C1 待展示信息；C2 形成并循环更新展示预期和唯一预期 HTML；C3 整理可注入展示代码 |
| **D 定义集成** | [caegraph-definition-integration](skills/observation-material-preparation/caegraph-definition-integration/SKILL.md) | 理解锁定 CAEGraph 仓库后，一次性集成外层输入和 A／B／C；确定性上游缺项可直接纠正并留痕 |
| **E 执行／运行** | [caegraph-execution](skills/observation-material-preparation/caegraph-execution/SKILL.md) | 同一个 Codex executor 完整执行 E1～E6，连续运行/修复、核图并在接受后取数 |

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

- B 的 `WORKFLOW.md` 只记录当前两种经验性用法；
- D 不设 `WORKFLOW.md`，只有 `SKILL.md + IO_SPEC.md`；
- E 的 `WORKFLOW.md` 统一安排直接运行、专业核图与接受后正式取数；旧 W1/W2 文件仅供历史 Run 追溯。

## C 的三部分

```text
C1：列出待展示信息
C2：形成并迭代展示预期
    C2A：直接阅读锁定版本 CAEGraph 使用手册
    C2B：形成第一版展示预期和第一版 HTML
    C2C：从当前 HTML 列出复杂展示点
    C2D：循环核实现有能力，并同步更新展示预期和 HTML
C3：整理可注入展示代码
    C3A：整理位置、实例和字段可注入的代码
    C3B：核对代码与 C2 当前预期
```

C2 循环结束时的当前 HTML 就是唯一预期 HTML；C3 不再另生成第二份预期 HTML。若 C3 整理代码时必须改变展示预期，返回 C2D 更新预期和 HTML。

C 不维护本仓二手展示速查，而是直接阅读：

- [`daowei2026/uplot@e6.2/CAEGraph使用手册.md`](https://github.com/daowei2026/uplot/blob/e6.2/CAEGraph使用手册.md)

复杂点不能仅靠手册判断时，再查锁定版本对应源码。

## 技术参考、模板和候选方法

| 类别 | 入口 | 作用与边界 |
|---|---|---|
| **D 仓库集成参考** | [CAEGraph 仓库结构与定义集成参考](skills/observation-material-preparation/references/CAEGraph仓库结构与定义集成参考.md) | uplot 仓库文件地图、实例／位置／字段到 PlotCtx、CDS、数据树和动态链的真实集成边界 |
| **B 高频位置参考** | [高频多尺度观察位置参考](skills/observation-material-preparation/observation-position-preparation/MULTISCALE_POSITION_REFERENCE.md) | 只复用既有脚本的 1d→30m→1m→5s→tick 位置层级和父子关系，不复用图内容 |
| **E 技术参考** | [CAEGraph 执行、核图与取数](skills/observation-material-preparation/references/CAEGraph执行取数与验证.md) | 构图／视窗／源值等数据阶段、最终图核对、核图后正式取数和一致性验证 |
| **E 旧 Worker 资料** | [Worker 派单合同](skills/observation-material-preparation/caegraph-execution/WORKER_DELEGATION.md) | 历史 Web executor + W1/W2 参考，不是当前 Codex E 默认路径 |
| **任务记录模板** | [观察材料准备任务记录](skills/observation-material-preparation/templates/观察材料准备任务单.md) | 汇总 A～E 产物和最终交付；字段细节以各 `IO_SPEC.md` 为准 |
| **候选方法组索引** | [S1～S4、E1～E4 方法索引](skills/observation-method-candidates/README.md) | 候选观察方法的触发条件、跨用例对应关系和成熟度；不是固定流程 |
| **合理性分析** | [四个合理性分析 Skill](skills/reasonableness-analysis/README.md) | 预期、对照、诊断、标定的专业方法 |

## A～E 的关键边界

- A 的“事件发生位置”说明每类 Event 自己在哪里发生以及 occurrence 携带哪些位置；B 的“观察位置”给最终图提供普通默认位置或高频多尺度位置。
- B 当前是经验性用法，不从 occurrence 中强行挑选“典型案例”；高频参考只借位置层级，不借图层和展示逻辑。
- C 可只读使用外层特征实例理解数据形状或生成预览 HTML，但 C3 代码必须保留实例注入接口。
- D 是单一集成动作。修法唯一且不改变位置选择／展示预期时，可直接纠正 B／C 缺项并留痕；拿不准或需要业务选择时返回 B／C。
- E 默认由独立 Codex Skill executor 直接完成 E1～E6；运行、核图与正式取数无需跨 Chat 的 W1/W2 必经派单。
- E 必须用 D 核对最终脚本、用 C2 当前预期／HTML 核对最终图；图被接受后才形成正式取数准入。
- `PLAN_READY` 不能冒充 `DATA_READY`。语法检查、静态定义、少量预览和未核对 HTML 都不等于真实观察材料已完成。

## L0 与 R 的边界

**一份任务总输入**：`BusinessTaskInput` 记录完整业务任务的目标、对象和约束；M 自身的外层输入由 `control/02` 规定。阶段产物作为后继输入，不与总任务输入混称。

**L0 只负责材料交接**：M 交付实际图、数据、来源、版本、范围、核对和限制。R 按自身用途检查消费资格；M 不替 R 判断合理性，也不预选 R 的探索／正式分支。

## 用例资料与历史记录

`task-inputs/` 下文件是具体用例输入，不替代 A～E 的通用 Workflow 和 Skill。历史 `longrun/runs/`、旧报告或聊天中出现旧结构，属于当时事实，不回写历史；新工作以本分支当前规则为准。

## 来源与状态

- 【S-M】[当前材料准备外层 Workflow](control/02_L1_观察材料准备流程.md)及 A～E 五个阶段 Skill。
- 【S-R】[合理性分析 Skill README](skills/reasonableness-analysis/README.md)及四个 Skill。
- 【N】本分支三层控制逻辑、A～E 细分、输入输出和 Gate 候选；仍需通过真实用例验证。

后续仍应逐边检查“上游产物 → 下游最低输入”。`control/` 不自行分配管理 Pro、执行 Pro、程序、Worker 或 Owner 的最终权限；[longrun/professional/](longrun/professional/README.md) 是角色适配指南，不改变专业源文档。
