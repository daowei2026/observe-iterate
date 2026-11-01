# 方法探索项目采用状态

当前状态：**BI-01-CO-04 已完成首次实质管理采用；首项 `CASE_OBSERVATION` 任务已签发；独立 Workmap Reader 已由 R0004 管理接收并在 Intake 记录为 `RECORDED`。dispatch preflight、Professional 实际发送和业务执行尚未被证明。**

- 专业及运行仓：`daowei2026/observe-iterate`
- 有权分支：`fy/feature-based-case-observation`
- `work_id`: `BI-01`
- `run_id`: `BI-01-CO-04`
- 首次管理采用：`runs/BI-01-CO-04/reviews/management-R0001/DECISION.md`
- Reader 接收：`runs/BI-01-CO-04/reviews/management-R0004/DECISION.md`
- Reader 报告：`runs/BI-01-CO-04/reviews/independent/workmap-01/REPORT.md`
- Run 入口：`runs/BI-01-CO-04/README.md`
- 长程地图：`runs/BI-01-CO-04/00_长程推进地图.md`
- 当前任务：`runs/BI-01-CO-04/01_当前任务.md`
- 当前 mode：`CASE_OBSERVATION`
- Workmap Binding：`runtime/config/WORKMAP_BINDING.json`
- 当前 Intake：`runs/BI-01-CO-04/reviews/WORKMAP_INTAKE_CURRENT.json`

## 已采用与已接收

Owner GO、探索完整目标、Owner 原过程、现有特征／工具背景、当前 Run 动态工作面、Question Work v2、Workmap v2 和角色回交机制已由 R0001 管理用于签发首项专业任务。R0004 只接收 exact Reader 对固定工作面的派发前 `PASS`：当前工作面无 repair-level blocker，可进入 dispatch preflight；它不提升市场证据等级。

当前任务继续要求先核真实输入与 as-of 时间资格，再形成主多品种判断、最近自然挑战／失败候选／合法无候选及方法反馈。下一实际动作是对既有任务运行适用 preflight，通过后直接发送 Professional，不再增加第二 Reader 或普通管理确认。

## 未被本状态证明

本状态不证明：

- dispatch preflight 已通过或 Professional 已实际发送；
- Professional 已开始、Worker 工单已签发或本 Run 正式数据已取得；
- 已有候选、中尺度具有选择增量、历史 30m 图适用；
- 任何业务判断、后续独立专业审查、管理业务 Gate 或 Owner 接收已经通过。

这些事实分别在派发记录、专业实物、Return 和后续管理决定中记录，不用 `RECORDED` 或 Reader `PASS` 合并。

## 连续性边界

旧 CO Run、U2／U3、I2—I6、历史图、旧聊天、旧预算和旧 Gate 仅按准确来源定向使用，不取得本 Run 当前权力。`professional/` 保存稳定探索背景，不维护平行 current task。Reader 调用不计入首项 Professional 的 1—2 次有效调用预算；当前 `known_pro_turns=0`。
