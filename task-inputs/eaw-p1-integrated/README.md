# EAW P1 整体观察与合理性分析｜全新 Run 业务输入准备

> 状态：**待补 CAEGraph 脚本/真实数据引用；尚非 OWNER GO，也未启动或注册新 Run**。整理日期：2026-11-16。本文件只整理本次 Owner 已明确的**任务输入及例外**，不改写 L0/L1/L2、原专业 Skill、V2 长程运行协议或其他 Run 的业务进度。正式启动时须以实际 Git commit 锁定本文件及采用的各项来源。

## 一、本次业务目标与范围

- **全新 Run**：重新发起 EAW 观察材料准备与业务合理性分析；不继承旧 `OI-EAW-WALL-20261116-01` 的 D/W/C、Gate、工作完成、材料接受或分析结论。
- **预期分析对象**：EAW **P1 多个相互关联的特征，作为一个整体**，不是先验只包含 `EawP1WallLifecycleFrp`。哪些 P1 Feature、产品及相关中间量实际纳入本轮，待 Owner 随后提供的 CAEGraph 脚本/数据与需求资料联合核定，不能凭某一历史 P1 包自行扩写为全部对象。
- 任务仍是原 `observe-iterate` 的 M（真实材料准备）→ R（合理性分析）父业务任务，由原专业 Skill 和控制面决定实质专业判断、证据资格及后继，不另创建专业工作流。
- **`work_id`、`business_case_id`、`run_id`、`question_id`**：待正式新 GO 确定；本准备稿不占用运行身份、也不创建 `longrun/runs/<run_id>/`。

## 二、设计预期｜直接使用 Owner 指定原文，不重新撰写

**Owner 指定的设计预期阅读位置**：

[《01.04.01 EAW叙事一个小范围完整的部分-preL0细节》§1.1.2 “墙”的基本思想](https://github.com/daowei2026/feature-refinement-implementation-agent-evolution/blob/8d58ddd3392a3e67ef5ba44adf2c4cd0c9077f9f/candidate_gold_cases/eaw/preL0_source_materials_20261102/%E5%8E%9F%E6%96%87%E5%BF%AB%E7%85%A7/mquant/ssot/eaw/01.04.01%20EAW%E5%8F%99%E4%BA%8B%E4%B8%80%E4%B8%AA%E5%B0%8F%E8%8C%83%E5%9B%B4%E5%AE%8C%E6%95%B4%E7%9A%84%E9%83%A8%E5%88%86-preL0%E7%BB%86%E8%8A%82.md#112-%E5%A2%99%E7%9A%84%E5%9F%BA%E6%9C%AC%E6%80%9D%E6%83%B3)

- 必须**亲自阅读该固定提交的原文**，连同该文 §1.1.1 的数据前提，理解来源范围。**本文件不将 AI 的改写、归纳或新写的一段话当作设计预期替代原文。**
- 这个定位直接指向“墙”的基本思想；P1 其它关联 Feature 的具体设计预期，如本轮确实涉及，按其对应原设计与需求材料查证，注明原文位置/版本。不能凭本链接自动宣称 P1 所有特征都具有一套已经被 Owner 确认的详细预期。
- Reasonableness Analysis Skill 仍负责将被指定的原始业务意图及具体来源组织成可检验预期与场景，区分 Owner 原文、业务推导、实现事实；**不能把现有代码行为当成设计预期**，正式对照前按原 Skill 冻结版本。

## 三、需求、设计、实现来源｜直接查原件，不另造一份“正式需求”

1. **成果／需求／工程包目录**：[EAW taskpacks_and_checkpoints](https://github.com/daowei2026/feature-refinement-implementation-agent-evolution/tree/8d58ddd3392a3e67ef5ba44adf2c4cd0c9077f9f/candidate_gold_cases/eaw/taskpacks_and_checkpoints)。P1 首先查看 `p1/`；`spine/` 提供跨包产品关系；`integration/` 提供当时的代码和运行检查点。目录内 `AUTHORITY_BY_SUBTREE.yaml` 明确 `included_does_not_mean_owner_accepted`，需区分收录、候选、实际采用与已运行。
2. **原始 EAW 业务资料**：[preL0_source_materials_20261102](https://github.com/daowei2026/feature-refinement-implementation-agent-evolution/tree/8d58ddd3392a3e67ef5ba44adf2c4cd0c9077f9f/candidate_gold_cases/eaw/preL0_source_materials_20261102)。其中前节指定的 §1.1.2 是本次 Owner 点名的设计预期入口。
3. **查需求 Chat 的归档**：[EAW 特征成果信息管理与追溯讨论](https://github.com/daowei2026/observe-iterate/blob/feat/observe-iterate-multirun-controller-v1-20261116/ai_chat/EAW%E7%89%B9%E5%BE%81%E6%88%90%E6%9E%9C%E4%BF%A1%E6%81%AF%E7%AE%A1%E7%90%86%E4%B8%8E%E8%BF%BD%E6%BA%AF%E8%AE%A8%E8%AE%BA.md)，作为成果索引/追溯线索；讨论中 AI 对当前有效版本的判断需回到原件验证。
4. 原有 `task-inputs/eaw-p1-wall-lifecycle/` 只反映**旧单 Wall Run** 的范围与输入，不作为新 Run 完成状态或整个 P1 的已冻结任务范围；其中真实代码线索仍可按专业方法独立核实。

## 四、此次特殊输入及直接后继

**Owner 已说明**：CAEGraph 画图/运行脚本已由别处准备，真实数据也可直接提供；相关脚本与数据的**精确路径、提交及实例绑定尚未提供给本次准备稿**，以后补充。

- 本 Run **不重新设计 CAEGraph 画图方案**，不将完成图形布局、显示方式、浏览器交互或建立新的绘图 Skill 作为取数与合理性分析的前置。
- 脚本提供后，以 **Owner 指定的现成 CAEGraph 脚本**作为取数入口：如配套真实数据已经足以满足相应专业消费者的要求，直接消费和核验；缺必需数据时，按已授权入口运行现成脚本或作最小定向补取。不能因为原通用步骤表存在就机械重做已经由现成脚本/数据提供的画图方案设计。
- 专业人员仍须确认所拿到的确为实际市场数据及适用版本、对象、参数、日历、时间和数据阶段。源业务结果、CAEGraph 构图结果、窗口显示结果不能不加区分；**不以人工构造的受控输入替代本次正式市场观察证据**。
- 入口和已有图的**完整重复盘点**不作为本次启动前置，缺必要事实时定向核查。原 M→R 的真实材料质量/使用资格和正式预期冻结条件仍有效；若输入已经具备，应按既有控制面和 Skill **直接安排具备输入资格的后继**。
- 原合理性分析范围不因本例外而被更改；必须由专业 Pro 依现有 Reasonableness Analysis Skill 作业务对照、诊断及必要时标定，不由 CAEGraph 或主控机械判断业务合理性。

**随后补填（暂不猜测）**：

| 输入 | 当前状态 |
| --- | --- |
| CAEGraph 脚本原件（仓库、commit、路径、执行入口） | 待 Owner 提供 |
| 已有数据原件（真实产物路径、对象、时间/日历、参数和数据阶段） | 待 Owner 提供 |
| 脚本实际覆盖的 P1 Feature/产品与本轮观察范围 | 待脚本核实 |
| 新 Run 正式身份、GO、采用来源锁、权限、实际写面 | 尚未 GO，不预填为已授权 |

## 五、多 Run 资源及运行环境输入

- **Owner 指定的本次 Linux 工作区：`/dwdhome/fy/BASE_E6_2`。** 这是待新 GO 采用的路径，不是本次已核实的独占/可运行凭证。
- 按 [MULTI_RUN_CONTROLLER.md](../../longrun/contracts/MULTI_RUN_CONTROLLER.md)，同一时刻活跃的不同 `run_id` 需要不同且不重叠的工作区。旧 Wall Run 也曾绑定该 BASE；**启动新 Run 前主控必须核实它已经释放该路径，若仍被另一活跃 Run 占用，不得在该路径并行派 Worker**。不擅自替 Owner 改用其它路径。
- 专业 Pro 使用 ChatGPT Project `细节叙事生成_金标`，推理档位 `Pro`；Worker 目标配置仍为已指定的 `GPT-6.1 Sol Max`，实际物理端绑定/可用性按本 Run 正式 GO 和主控规则检查。
- 真实 GO 须按 [OWNER_GO 模板](../../longrun/templates/OWNER_GO.md) 确定每 Run 独立身份、精确控制面/主控 Skill 引用、Linux/仓库写入授权和与其它 Run 共享目标的单写者条件。本准备稿**不代替 GO、不创建 Binding/Registry、不派发 C/D/W**。

## 六、不得改变的边界

- 这是**新 Run 的输入准备**，不修改现有 `control/`、原专业 Skill、协议或旧 Run 的事实/结果。
- **设计预期看指定原文**；不要另写一段并当成 Owner 确认的 EAW 预期。
- **现成 CAEGraph 脚本和数据直接往后走**，但“Owner 已准备”与“本 Run 已实际收到、核验并具备分析消费资格”分开。
- P1 具体覆盖边界及脚本/数据 exact refs 等 Owner 后续提供再补；未具备真实 GO 时不假报新 Run 已启动。
