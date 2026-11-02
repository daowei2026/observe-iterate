# CO-05 Owner 定向纠正：图数准备工单

- work_id: `BI-01`
- run_id: `BI-01-CO-05`
- change_kind: `OWNER_LOCAL_PROFESSIONAL_WORKER_ORDER_CORRECTION`
- owner_authorization: 本次 Owner 明确要求，将此类高频技术工作限定为图数准备，由 Professional 先给具体脚本，Codex Worker 按既定方案执行
- source: `professional/exploration/07_图数准备工单约定.md`
- historical_order: `runs/BI-01-CO-05/artifacts/professional-R0002/WORKER_ORDER.md`（`BI01CO05-AIDATA-EVIDENCE-01`）

## 一、纠正范围与权力

这是一项**现有 CO-05 专业任务内部的 Owner 定向纠正**，不是新的 Run、新业务研究题、管理 M-START 或对已提交历史的修改。原 `CASE-OWNER-PROCESS-PRACTICE-01` 的业务目标、两层实践和完整未完保留；纠正的是原 Worker 工单过多承担“输入资格/数据语义调查/事件账本”等非图数准备工作的任务边界及交付内容。

自本纠正起，本 Run 后续同类 Worker 技术工单统一按新 `07_图数准备工单约定.md` 形成：**Professional 提前确定具体图和数据、现有固定执行环境中的完整 Python 脚本（或准确的现成可执行脚本引用及已确定变更）、执行命令和交付要求；Worker 主要执行、正常工程修通、核对并交付可供人看的图及供 AI 读的对应正式数据。** 工单不需要单列观察目的，不要求 Worker 重新选择研究范围、设计图面或构造首次可知事件账本。不为交工增加无消费者的专项报告。额外技术调查或能力开发另签工单。

### 本 Run 的图数准备执行环境（既有定位）

这是本 Run 图数准备工单使用的固定工作环境定位，**不要求 Professional 每张工单重新选择环境或软件版本**：

- **Worker Codex 聊天工作区**：`/dwdhome/fy/cgpterm`，是 Worker 聊天的工作区，不是实际 aidata 代码执行根。
- **实际 aidata 执行工作区**：`/dwdhome/fy/BASE_E6_2`。
- **aidata 代码目录**：`/dwdhome/fy/BASE_E6_2/mquant/aidata`。
- **正常执行入口**：在 `/dwdhome/fy/BASE_E6_2` 中使用当前环境现有的 Python 运行 Professional 已给定的脚本。例如 `cd /dwdhome/fy/BASE_E6_2 && python <本次指定脚本路径>`；此处尖括号是待替换的脚本路径，不是可照抄的命令。
- **数据源、脚本和输出位置**：由 Professional 的本次具体 aidata 脚本/brief 指定。已有 `test_runs/fy_owner_1d_30m_20261027` 是历史测试位置，不作为全部后续工单的固定输出根。

**版本核实边界：**目前已提交的资料只确认以上路径，没有提供可独立核实的本地 aidata/关联代码 checkout commit、Python 解释器版本及依赖锁定值。不能凭历史案例声称这些版本已核实。由 Worker 在第一次合法现场执行时读取现有工作区实际版本并报告，**不自行切换、升级或另选版本**；如果发现与现行有权环境要求不一致，报告具体差异和影响，待有权方处理。后续如果固定版本已有真实正式来源，直接按该来源使用，不要求 Professional 逐次重新指定。

上述定位依据既有 `画图.md` 及 R0002 历史 Worker 工单，尚未经本次现场复验；不因补充本段就额外发起环境搭建或平台研究任务。

## 二、R0002 已签工单处理

`BI01CO05-AIDATA-EVIDENCE-01` 已经签发，不能删除、改写或倒签这份历史。**不要继续按该工单的原交付范围新投递**；尤其不自动实施 `KEY_T_EVENT_LEDGER`、全部 first-visible/revision 恢复、方向映射专项调查和十一项交付清单。

协调者必须先核实实际在途和原 Worker 线程。若工单尚未实际投递，停止其待发并保留准确证据；若已经投递、执行或状态不明，先对账并按现有合法停止/接续机制处理，不能重复发送或宣称未执行；正确、已经生成的图数实物可按权限复用。

本次纠正必须交由**原有权 Professional Pro**，由它在原业务任务范围内重新准备符合 07 的实际图数脚本和新工单，不能由操作主控自行编写参数/工单，也不能把旧工单改个名字直接再次发送。

## 三、建议的低成本接续

1. 先核 `R0003` 定向 `return_repair` 的现场发送/回交状态。它只处理 R0002 Return 关联缺件，**不得**把本次实质纠正伪装成其字段修复。
2. 旧 Worker 工单现场状态对账并处理受影响的发送/执行；不影响其他合法专业工作。
3. 在原 `QUESTION_WORK_BINDING` 和 `same_work` 路线仍有效、无新增管理放行要求时，使用新一轮 NORMAL Professional 消息，将**本 Owner 纠正和 07 文件的 exact GitHub 引用**作为 `evidence_refs` 真实交付原 `chatgpt:BI-01-CO-05:professional`；保留最新合法专业 Return/continuation、原任务的全部义务和累计投入。不能只向手机发自由改写文字，也不能让协调者修改原 Task/Binding 来凑校验。
4. Professional 应先产出实际可执行 Python 脚本/脚本引用，再签发一张**新的**图数准备工单，按旧 `overlay/12` 合法校验、派发、回交；有已有图数可直接消费就无需无故重算。
5. 图数结果回原 Professional，继续现有 Owner 初版过程的市场观察。当前纠正本身不强制额外调用 Management Pro；若真实授权、业务任务或已到期管理触发要求管理，则按实际受影响范围办理，不得伪造豁免。

若上述直接 `same_work` 的权力、来源采用或工具校验不成立，应报告**具体阻断**，再由对应有权责任者作**定向**处理；不以节省调用为由绕过身份、来源、旧在途及派发校验。

## 四、延后到正常管理复看的资料整理

为避免当下更改受 Workmap 监控的来源造成 `INTAKE_STALE`，**现在暂不修改** `05_OWNER_PROCESS_EXPLANATION.md`、`03_TOOLING_AND_DATA_USAGE.md`、`professional/exploration/README.md`、正式 `01_当前任务.md`、Workmap Binding 与 Intake。

在本 Run 下一次**本来就应发生的合法管理复看**时，连同实际专业进展一起处理：将旧 `tooling_examples/2026-11-01_30m_multi_symbol_turn_chart.md` 中的 small/mid/large 转折计算参数迁入 `05_OWNER_PROCESS_EXPLANATION.md` 第一节，去掉图形标记等非特征参数；删除旧绘图案例文件及受影响导航/03 引用；正式采用本 07 约定并根据实际变更更新 Workmap/Intake。历史 commit、已签 R0002 工单、原 Owner GO 和业务成果不倒改。**这些资料整理不是本次重新签发图数工单的前置。**
