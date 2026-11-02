# BI-01-CO-05：Owner 初版用例形成过程的真实实践

<a id="common"></a>
## 共同状态

- **Run**：`BI-01-CO-05`
- **Work**：`BI-01`
- **当前专业 mode**：`CASE_OBSERVATION`
- **当前状态**：已完成两次有效 Professional 调用和 R0006 到期投入复看。R0005 的品种、频率、large+mid、Context、同 run/core 图数链和脚本化准备被有限接收；旧 45 天主范围及旧 Worker 工单已停止新投递。当前等待原 Professional 按 Owner 指定全段修订新脚本并重新签发新工单。
- **有权分支**：`fy/owner-led-case-exploration-optional-reader-20261102`
- **Owner GO**：[OWNER_START.md](OWNER_START.md)
- **Owner 最新时间纠正**：[OWNER_CHANGE_20261102_R0005_TIME_COVERAGE.md](OWNER_CHANGE_20261102_R0005_TIME_COVERAGE.md)
- **最终投资目的**：[00_BUSINESS_OBJECTIVE.md](../../professional/exploration/00_BUSINESS_OBJECTIVE.md)
- **当前探索直接目标**：[06_EXPLORATION_STAGE_GOAL.md](../../professional/exploration/06_EXPLORATION_STAGE_GOAL.md)
- **Owner 完整初版过程**：[05_OWNER_PROCESS_EXPLANATION.md](../../professional/exploration/05_OWNER_PROCESS_EXPLANATION.md)

本 Run 不继承 CO-01—CO-04 的任务、地图、Reader、预算、在途、Gate 或业务结论。旧运行仅在当前具体问题确有需要时作为历史事实或工具经验定向引用。当前业务目标不是证明旧图、旧参数或旧 Case 正确，而是用真实特征与市场过程实践并迭代 Owner 的初版用例形成方式。

<a id="bi01"></a>
## BI-01 当前入口

### 当前业务关系

`Owner 初版过程与当前问题 → 本 Run 同身份全段图/正式数据 → 证据资格核对 → 沿当时可知信息观察大尺度背景形成/改变 → 检查中尺度结构 → 形成并更新具体用例/前瞻判断 → 管理接收与方法反馈 → Owner 校准或下一轮专业实践`

### 当前已成

1. R0002 完成输入资格 fail-closed：没有正式数据时不制造市场结论；合格市场 T 为 0。
2. R0005 固定 `rb/hc/i`、`30m`、`ScaleTurnCalendar("large") + ("mid")`、`GTQH_L1_20210104_20240229 / gtqh_four`，形成同 run/core 图—正式数据脚本和具名工单；静态语法通过，但没有目标环境运行、图或正式数据。
3. Owner 指出 45 天局部范围不能承担第一层主观察，固定主图和正式数据范围为 `[2021-01-04 00:00:00, 2024-03-01 00:00:00)`。
4. R0006 有限接收可复用技术准备，停止旧工单 `BI01CO05-CHART-DATA-R0005-01` 的任何新投递，并消费第二次有效调用的 EFFORT 复看。

### 当前未成

尚未取得本 Run 的新全段脚本/新工单、实际 run/core、可打开全段主图、正式 KLine/large/mid 切片、manifest/FILE_INDEX、字段语义核实、合格关键 T、第一层连续市场过程、中尺度用例、候选/排序/无候选、自然挑战或方法有效性结论。首个过程实践包未被接收。

### 当前正式工作面

- [长程推进地图](00_长程推进地图.md)
- [当前正式专业任务](01_当前任务.md)
- [R0006 阶段接收与投入复看](reviews/management-R0006/DECISION.md)
- [当前 Workmap Intake](reviews/WORKMAP_INTAKE_CURRENT.json)
- [运行采用状态](../../runtime/config/ADOPTION_STATUS.md)

### 下一实际动作

协调者在同一 exact commit 上核更新后的 Intake 和 unchanged formal task，运行 routine Professional dispatch preflight；通过后向 `chatgpt:BI-01-CO-05:professional` 发送当前完整任务、Owner 时间纠正与 R0006 决定。原 Professional 必须创建全段新脚本和新的正式 Worker 工单；旧 R0005 工单不得派发。新单合法执行后，技术结果回原 Professional，并立即进入真实第一层业务观察。

### 当前不能声称

本入口不证明全段脚本/工单已形成、Worker 已派发或执行、图数已取得、字段语义已核、当时可知状态可还原、共同背景或中尺度结构存在、候选规律成立、市场无候选、独立业务审查通过、Owner 已接受新增业务分析，或当前探索阶段完成。
