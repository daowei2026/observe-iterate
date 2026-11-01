# 启动 BI-01-CO-02 长程任务

现在由 Owner 正式授权启动并持续运行新的长程任务 `BI-01-CO-02`。

**本条是新 Run 的正式 Owner GO，不是准备、离线测试，也不是旧 Run 的接续。**

本次任务围绕既有特征开展业务用例探索。当前仍处于业务用例形成方法的摸索阶段，需要通过多轮真实专业工作逐渐形成有效的业务研究方式。不要提前将当前设想固化成专业规范或固定 Agent。

## 一、运行身份与版本

**操作仓库**

- 仓库：`daowei2026/cgpterm`
- 分支：`fy/observation-iteration-agent-longrun-20261015`
- 采用提交：`86dec991abb27a927c1b5c22af1e51b3f39b918b`

**专业及运行仓库**

- 仓库：`daowei2026/observe-iterate`
- 分支：`fy/feature-based-case-observation`
- 采用提交：`b6ccf766dac055a793e75f76b77a73f4cfc74064`

`work_id=BI-01`，`run_id=BI-01-CO-02`，从 `R0001` 开始。

本次运行成果提交到上述专业及运行仓库的指定分支，不另建分支。

旧运行 `BI-01-CO-01` 保留在原分支，不复制其管理决定、历史授权、R序列、未完成事项或运行状态，也不将其视为已经完成。

## 二、完整任务来源与首次启动

本次业务目标采用专业仓当前版本中的：

`professional/exploration/00_BUSINESS_OBJECTIVE.md`

首次管理需要理解以下完整探索背景：

- `professional/exploration/01_EXISTING_FEATURES_AND_CAPABILITIES.md`
- `professional/exploration/02_CURRENT_WORKING_IDEAS.md`
- `professional/exploration/03_TOOLING_AND_DATA_USAGE.md`
- `professional/exploration/04_EXISTING_BUSINESS_REFERENCES.md`
- `professional/exploration/05_OWNER_PROCESS_EXPLANATION.md`

其中，**`05_OWNER_PROCESS_EXPLANATION.md` 是 Owner 提供的完整做事过程原文，必须完整读取和理解，不能只依据02摘要进行管理。**

另外，`03_TOOLING_AND_DATA_USAGE.md` 已经整理了此前通过 aidata、uplot、CAEGraph/PlotSet 开展数据和画图工作的操作知识。需要实际使用工具时，直接参考，不要重新摸索已经明确的操作方式。

本次工具实践案例位于：

`professional/exploration/tooling_examples/2026-11-01_30m_multi_symbol_turn_chart.md`

这是一次已经走通的特定绘图实践，可以复用其中的接口组合、图层绑定和实际操作经验，但不能把其中的品种、时间范围、30m频率及small/mid/big参数直接作为本次默认配置。

首先按照现有 **M-START BOOTSTRAP** 机制建立新运行，保存本条真实 Owner GO，派发首次 Management Pro，由其理解完整探索背景和实际输入，建立本Run的长程推进地图、当前任务、Binding及必要管理记录，并安排第一项专业工作。

完成真实管理采用后，按原有机制持续运行本次长程任务。

## 三、本次长程任务的性质与管理职责

本次任务不是让专业Pro按照已经确定的专业方法，机械地反复生产业务用例。

当前仍在探索：

- 什么样的初始业务用例真正具有投资业务价值；
- 怎样利用既有贴近转折特征、线段、属性及多对象关系形成用例；
- 怎样通过实际特征观察发现现象和候选规律；
- 怎样利用判断时点之前已经能够取得的信息，提前判断后续品种走势好坏、机会和反向风险；
- 怎样组织专业工作，才能持续形成真实业务成果。

**Management Pro负责整个探索过程的实质管理。**

具体职责：

1. 理解Owner整体业务目标、完整做事过程和已有探索材料。
2. 理解当前已经具备的特征能力、数据及工具使用基础。
3. 结合真实输入和当前业务认识，判断本轮最值得推进的专业工作。
4. 将具体工作派发给Professional Pro。
5. 接收和理解实际业务研究成果，判断取得了什么实质进展。
6. 根据结果更新整体认识，判断当前设想是否需要修正。
7. 安排下一项专业工作，持续迭代。

**当前两层观察过程和同向大尺度背景下观察中尺度差异，只是当前提出的工作设想，不是必须遵循的固定方法或两个正式Gate。**

实际运行中可以发现原设想不成立、需要调整，也可以根据业务发现改变研究范围。不要为了维护原先设想而无限增加细节工作，也不要因为第一层出现困难就直接扩展成全面场景分类研究。

多轮实践之后，再考虑哪些做法值得固定成专业规范或专用Agent。

## 四、动态管理产出与GitHub交付

所有动态管理产出统一放在：

`runs/BI-01-CO-02/`

Management Pro按原有机制维护：

- `README.md`：Owner查看当前Run的入口。
- `00_长程推进地图.md`：整体业务目标、实际成果、重要剩余和后续安排。
- `01_当前任务.md`：当前正式专业任务。
- `reviews/management-Rxxxx/DECISION.md`：每轮管理决定。
- `provenance/turns/Rxxxx/`：管理和专业正式回交及身份记录。
- `reviews/WORKMAP_INTAKE_CURRENT.json`：当前管理采用及地图接收状态。

根据真实变化更新推进地图和当前任务，不要求每次管理调用机械修改。

不要在 `professional/` 下另建 `current_work`、`CURRENT_EXECUTION.md`、`TASK_ROUTER.md` 或其他重复的动态管理工作面。

专业背景保留在 `professional/exploration/`，动态管理和实际业务成果统一进入当前Run。

专业工作成果、管理决定、ROLE_RETURN、QUESTION_WORK_RETURN 分别按现有机制提交GitHub。成功后手机只回复准确commit及交付位置，不重复粘贴完整报告或JSON。GitHub不可写时按原备用ZIP运输规则处理。

## 五、主控读取限制

首次只读取以下必要入口：

- `cgpterm/AGENTS.md`（如已自动加载，不重复）
- `cgpterm/.agents/skills/observation-iteration-longrun-controller/SKILL.md`
- `observe-iterate/runtime/overlay/08_自然语言运行提示_v0.3.md`
- `observe-iterate/runtime/config/COORDINATOR_DISPATCH.json`

进行首次管理启动时，再按需要定向读取：

- `runtime/operations/CASE_OBSERVATION_RUN_GUIDE.md`
- `runtime/config/WORKMAP_BINDING.json`
- `runtime/config/ADOPTION_STATUS.md`
- 本次正式管理采用所需的探索背景和管理协议。

主控不需要自行通读全部专业材料，也不代替Management Pro研究业务。

Management Pro应按照自身职责完整读取本次必要的业务背景、Owner原始做事过程说明、实际输入和适用工具材料。

**禁止无明确任务需要而递归读取全仓、历史runs、旧分支、runtime/release、无关专业Source、全部Skill、测试文件及实现源码。**

已经读取且版本未变的规则不重复读取；后续确有具体操作或故障需要时，只定向取得对应材料。

## 六、数据与工具使用

本次以既有贴近转折特征及其衍生对象为业务观察基础。

实际数据到位后，由Management Pro先核对本次真实交付，确认品种、时间范围、大中小尺度配置、特征字段、方向信息、实际转折点、确认信息、线段及其当前发展状态。

数据与图的准备使用：

`professional/exploration/03_TOOLING_AND_DATA_USAGE.md`

以及其中指向的已走通工具实践。

首次观察的画图设想需要注意：

- 1d概览图可能无法自由调整或添加特征，不作为首次主要观察图。
- 优先尝试相对完整时间范围的大尺度图，同时显示大尺度和中尺度贴近转折。
- 贴近转折输出不一定包含完整方向信息，必要时核对上游zig。
- 区分正式带方向的转折点与额外的无方向贴近点。
- 区分实际转折位置和确认信息到达时间。
- 小尺度按实际观察需要使用。

这些是Owner提供的当前操作设想，需要结合实际数据和工具能力核实，不得擅自升级为已验证的固定绘图规范。

复用已有适用的正式数据、Core、图页和工具，不机械重复调用全部接口，不重建整套环境。

## 七、Worker Codex

本次 Worker Codex 使用 Owner 指定的已有聊天：

- `threadId`：`01a17dd7-5033-7e63-b7a2-edd90b691c33`
- 预期聊天工作区：`/dwdhome/fy/cgpterm`

不另建 Worker 聊天，不自行改用其他聊天。

首次出现合法 Worker 技术工单时，核实该threadId对应的真实聊天及其工作区，确认无误后，按既有工程师派工机制向该聊天发送任务。

若聊天不存在、工作区不符或无法正常派工，新建一个聊天。

此目录是Worker聊天工作区，实际技术任务涉及的源码、数据和执行目录仍以具体工单为准。没有Worker技术任务时，不提前读取其历史或进行无关检查。

## 八、运行

完成首次管理采用和合法派发后，持续推进本次完整业务目标。

专业工作、Worker派工、独立审查、GitHub成果、正式回交、管理接收与后继处理，均按仓库已经采用的正常机制执行。

不要将本次探索预先设置成固定两层Gate，也不要因为完成一次局部观察就主动停止。

**本次长程任务的核心责任，是由Management Pro持续管理探索，通过多轮具体专业实践，逐渐形成真正有业务价值的初始用例及其有效形成方式。**

不自行扩大Owner授权范围。
