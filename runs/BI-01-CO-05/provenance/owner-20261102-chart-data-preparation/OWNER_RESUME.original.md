# 接续 BI-01-CO-05：定向纠正图数准备 Worker 工单

现在由 Owner 明确授权，在**现有 `BI-01-CO-05` Run 内**接续执行本次图数准备工单纠正。

**这不是新 Run 的 Owner GO，不重新开始 R0001，不重新进行 M-START，也不默认要求 Management Pro 重新规划整个专业任务。**

## 一、采用本次新增材料

专业及运行仓库：

- 仓库：\`daowei2026/observe-iterate\`
- 分支：\`fy/owner-led-case-exploration-optional-reader-20261102\`
- 本次新增材料提交：\`d2ec75bcc9744569198ff100969fd5a1236dc5ac\`

本次 Owner 纠正：

`runs/BI-01-CO-05/OWNER_CHANGE_20261102_CHART_DATA_PREPARATION.md`

本次新工单约定：

`professional/exploration/07_图数准备工单约定.md`

上述两份文件须从准确提交取得原文并按其实际适用范围使用。

原 CO-05 的业务目标、正式专业任务、Question Work Binding、Manager 已完成的业务安排和既有控制面继续有效。本次没有授权主控重新设计专业任务。

操作 Controller 仍采用本 Run 已锁定的版本，不因本次专业文件提交而自行升级。

## 二、先核当前真实在途

目前仓库已有：

- R0002 Professional 业务回交及 Worker 工单 `BI01CO05-AIDATA-EVIDENCE-01`；
- R0003 `return_repair` 的派发准备记录。

先核实 R0003 是否实际发送、回交修复是否已经完成，以及旧 Worker 工单是否实际投递、正在执行或已经形成技术结果。

R0003 只处理原来的 Return 关联缺件，不把本次实质纠正塞进 R0003 冒充字段修复。

旧 Worker 工单不应按原范围重新投递。已在途或状态未知时先按现有机制对账并处理受影响操作；不重复派发，不覆盖历史，不丢失已经形成的有效结果。

只处理当前真正影响接续的事项，不重新扫描全部历史 Run 或进行全仓检查。

## 三、优先直接接续原 Professional Pro

本次 Owner 已明确决定：以后同类图数准备工作，应当由 Professional Pro 先形成具体 Python 执行脚本和图数交付要求，Codex Worker 主要按脚本执行、核验和交付。

这一变化只涉及原专业任务内部的技术派工方式，**不改变当前具名业务问题、专业任务完整范围及原管理授权**。

在完成必要的在途对账后，优先使用当前 Question Work Binding 已有的 `same_work` 路线，向原 Professional 聊天：

`chatgpt:BI-01-CO-05:professional`

派发新的合法 Professional 调用。

组装本次派发时：

1. 保留当前有效的专业任务和原有 Binding。
2. 保留最新合法 Professional Return、continuation 和真实累计投入。
3. 将本次 Owner 纠正文件及 07 工单约定作为准确 GitHub 来源，通过当前支持的 `evidence_refs` 等既有方式交给 Professional。
4. 明确要求 Professional 全文读取本次纠正及 07，并按其要求重新准备图数 Worker 工单。
5. 按现有正常派发生成、提交、回读、校验并发送准确消息，不手写绕过控制面的提示。

**不要仅为了让 Professional 重签这张图数工单而额外调用一次 Management Pro。**

如果实际检查发现这条直接续作路线存在具体的授权、来源或机械校验阻断，则按现有权力处理受影响部分；确需管理时只申请定向处理，不自行绕过控制面，也不重新执行完整 M-START。

## 四、Professional 本次需要完成的工作

Professional 继续承担原 `CASE-OWNER-PROCESS-PRACTICE-01` 业务任务。

本次优先修正图数准备安排：

- 自己确定本轮所需的具体图和正式数据；
- 按 07 约定提供完整可执行的 aidata Python 脚本，或准确引用现有可执行脚本并给出本次明确修改；
- 采用已有固定运行环境，不重新安排版本；
- 不把历史 first-visible/revision 恢复、事件账本设计、全面字段审计或额外平台调查作为图数准备的默认内容；
- 形成新的正式 Worker 工单，并明确图、对应正式数据和简短执行回交。

由 Professional 正式签发新工单。主控不得替它选择参数、编写脚本或直接把原工单改名重发。

新 Worker 工单仍须通过现有 `worker-order` 检查与实际合法派发，技术结果返回原 Professional。

图数到位后，Professional 直接消费这些材料，继续原 Owner 初版业务用例形成过程的市场观察，不因技术工单完成就停止整个专业工作。

## 五、资料迁移暂不执行

本次不修改：

- `professional/exploration/05_OWNER_PROCESS_EXPLANATION.md`
- `professional/exploration/03_TOOLING_AND_DATA_USAGE.md`
- `professional/exploration/README.md`
- 当前正式 `01_当前任务.md`
- Workmap Binding、Intake

旧绘图材料的转折参数迁移、原文件删除、导航清理和新约定的正式来源采用，留到下一次本来就需要的合法 Management 复看时一并处理。

这部分**不是当前 Professional 重签图数工单的前置**。

## 六、持续运行要求

本次是同一 Run 内的局部纠正，不清零原专业投入、不丢失原任务全部未完，也不取消原有 RESULT、CHANGE、EFFORT 触发。

若正常管理触发确实到期，按原机制处理；但不得把一次普通图数派工纠正自动升级为重新规划业务的管理任务。

完成当前必要纠正后，继续按原长程任务机制运行。

**本次优先目标是尽快让原 Professional 签发真正可执行的图数准备工单，让 Worker 准备图和对应数据，再回到真实业务观察。**

主控只负责有权任务的准确接续、运输、核验及状态管理，不代行 Professional 或 Management 的实质判断。
