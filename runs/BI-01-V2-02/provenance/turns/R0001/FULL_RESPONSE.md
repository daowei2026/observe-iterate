# BI-01-V2-02 R0001 M-START 完整管理回交

[BI01-V2-02-R0001-20261018T130131Z-7f26abeb]

- `work_id`: `BI-01`
- `run_id`: `BI-01-V2-02`
- `assignment_token`: `BI01-V2-02-M-START-a6b833b62eac4a0fa8c23b037a4bac05`
- `role`: `management`
- 回交状态：`SUBMITTED`
- 当前运行状态：管理实质交付已发布；首次 Workmap Reader 已签发但尚未实际调用；Workmap 仍 `NOT_CONFIGURED`；专业任务尚未发送；本 run 尚无 S1/S2/S3 专业结果。

<a id="management-decision"></a>
## 1. 管理决定

本轮的完整业务链已经重建并签发：

```text
U2/U3 原 Owner 业务问题
→ 固定 rb/i/hc 基础 KLine/Zig/mid 自主发现真实场景
→ U2 位置、机会身份、成员和第三对象边界
→ U3 四个 Movement Evidence Bundles 在合法 As-Of 的辨别力
→ 合法 Outcome 或明确标注的探索性后续路径
→ 与 KLine/C0/N/静态组/简单共同事件比较增量或无增量
→ Owner 可按图核查的保留、修订、继续验证或停止行动
```

管理已裁定：

1. **S1 场景发现先行。** 不再从 304 个 C1 raw、方便字段、旧 Case 或异常列表倒推市场场景。
2. **两个证据面互补而不混同。** 广域基础行情+C0/N/C1 raw 检验位置与成员；一个完整参考 Case×五 As-Of 检验 Current/Working/Completed/R02，可判范围不同。
3. **U2 与 U3 责任分开。** U2 组织同一机会身份和重复暴露边界；U3 评价运动质量。四方面采用 Progress/Friction/Retention/ObservabilityAndConstraint，不是四类 Allocation Evidence。
4. **不预填赢家或场景配额。** 整组都弱、成员难分、当时无法判断和设计无增量都是合法结果。
5. **固定两包不重算。** 不等待正式 Feature，不替换数据源，不把 R03 Withheld、C2 Shadow 或 N 层升格成正式 U3/Cluster/H1。
6. **图与数据同口径。** Owner 看 aidata 真实图；执行 Pro 读同源结构化数据，不声称像素识图。
7. **完整阶段不以局部停。** 首图、单 Case、脚本成功、字段齐全或局部修复均不结案。

已撤销且不列为 deferred required：旧 `BI-01-V2-01` 的任务、Workmap、Reader、Gate、R10、在途、F01—F14、旧选样分类、主 Case 优先及完成说法；预设类型/阈值/赢家/配额；以 raw 候选、单 Case或图数为停点；开工前重算 U2/U3、全仓审计、重测既有环境、建设视觉链、改 aidata 现有分支或在观察仓另造图工具。

正确业务、原数据、actual/confirm/known/As-Of、Working/Completed、Reference/Shadow/Withheld、C0/N 基线、U2/U3 原设计和消费者均完整保留。

<a id="plan"></a>
## 2. 实际工作安排

### S1：基础行情自主发现

执行 Pro 完整读取 Owner Decision、U2/U3 Narrative/Use Case，直接消费固定 KLine/Zig/mid 数据，记录真实搜索覆盖、具名位置、选择理由、后验地位、要检验的成员强弱问题和主要反例。首个有价值位置立即进入 S2/S3，同时继续固定范围内的 S1。

### S2：先基础图，再有目的叠加

执行 Pro 在窗口明确后签 Worker 工单。Worker 用 `/dwdhome/fy/BASE_E6_2` 的 aidata 和 `/dwdhome/fy/资金管理` 的固定原件，先画 KLine/Zig/mid，再按场景问题叠加 U2/N/合法 U3；交真实可打开图、同 `run/node/timespan` 数据与读图定位。普通依赖可连续修通；真正通用缺口只在 aidata 新独立分支处理。

### S3：按场景形成业务认识

逐项交：市场事实、设计承诺、当时判断、后续支持/反证、基线比较、结论与行动。必须处理不同 lifecycle、观察 bar 数、单位、确认时效和同源证据；广域没有完整 U3 时准确标明，不补算、不把 N 改名 U3。

### 管理复看

首个完整“基础行情→U2→U3/限制→后续→增量”闭环触发非阻塞 M-REASSESS；重要前提冲突或连续两次只在来源/工具/格式循环亦触发；每四个有效结果做 EFFORT 复看；完整条件满足后 M-CLOSE。

<a id="completed"></a>
## 3. 本次已完成

1. 实际读取 Owner 完整目标、V2 00—07、运行/管理/交接合同及 U2/U3 Owner Decision、Narrative、Use Case 承重原文。
2. 直接核查两份固定 ZIP 的文件身份、成员、关键 CSV 行数、状态、一个完整 Case 与五 As-Of 的真实关系。
3. 独立形成当前业务关系图、采用/撤销决定、全部重要剩余、优先级和真实后继。
4. 发布：
   - `runs/BI-01-V2-02/00_长程推进地图.md`
   - `runs/BI-01-V2-02/01_当前任务.md`
   - `runs/BI-01-V2-02/reviews/management-R0001/DECISION.md`
   - `runs/BI-01-V2-02/reviews/management-R0001/READER_TASK.md`
5. 在当前任务中签发连续 S1/S2/S3 `question-work/v2` Binding、专业 recipient、路由和 RESULT/CHANGE/EFFORT 触发。
6. 更新 README、PROGRESS 和 Workmap config 说明，使 config 保持真实 `NOT_CONFIGURED`，不预造 Reader PASS、Intake 或 ADOPTED。

本次没有把“已签发 Reader/专业任务”写成“已发送或已完成”。

<a id="material-use"></a>
## 4. 材料使用记录

### 完整读取并用于实质判断

- `daowei2026/observe-iterate@30d6cd28ca4cc52eb201f0aa474f9f4c93b74080`
  - `professional/v2/00_PURPOSE_AND_THREE_STEP_FLOW.md`
  - `professional/v2/01_AIDATA_CHART_AND_DATA.md`
  - `professional/v2/02_OBSERVATION_IDEAS_AND_VALIDATION.md`
  - `professional/v2/03_EXECUTION_HANDOFF.md`
  - `professional/v2/04_BI01_BUSINESS_BASELINE.md`
  - `professional/v2/05_BI01_FIXED_INPUT_DATA.md`
  - `professional/v2/06_U2_U3_DESIGN_SOURCE_MAP.md`
  - `professional/v2/07_BUSINESS_SCENE_OBSERVATION_METHOD.md`
  - DR06/08/12/13/14、Management Harness、Run Guide、Round Record、Adoption Checklist、Workmap/Question Work schema。
- `daowei2026/complex-systems-vocabulary@48f55f53e25d04e5b4b59fae1e652dd4b679c9d3`
  - U2/U3 Owner Decision
  - U2 Narrative/Use Case
  - U3 Narrative/Use Case。
- 两份本轮固定 ZIP：
  - `steel_U2_U3_执行结果_20261010.zip`，SHA-256 `7bebbee3fd7d425eb85116f33c5d0e01ae2163e6849818515fe3824a82b9a46c`
  - `rb_hc_i_mid贴近转折_zig_small_K线_20210101_20240229.zip`，SHA-256 `4fd1af4e7b34af6fc099e6289ffdd5d83125412fc16d2a9902af4fd9741b3987`。

### 关键恢复事实

- 广域 C1 raw 304 行：205 个两成员、99 个三成员；全部未正式 Formation/Assessment。
- 完整链只有 `refonly-ad8824a52552d7bffa91` 一个 Case、五个 As-Of；C2 无 official Cluster/H1，R03 全 Withheld，组外为零。
- `2021-05-11 10:00` 的 hc/rb/i 分别是 Working 38 bars、Completed 33 bars、Completed 1 bar；raw progress 又是各自价格单位，所以不能直接横排赢家。
- 上游外层 ZIP 与历史哈希差异保留为身份限制；本包内部与自身 manifest 一致，不能据此冻结全部业务。

### 未读/不可得

- 无必须材料未读。
- 未把候选 Local Contract 当正式方法；涉及后续具体公式或字段争议时，执行 Pro 按 06 精确指针再读取。

<a id="reader-issued-work"></a>
## 5. 已签发 Reader 工作

已签：`runs/BI-01-V2-02/reviews/management-R0001/READER_TASK.md`。

Reader 只检查 exact 地图、任务、Binding、决定和 overview 是否能让独立执行者恢复完整业务链、撤销/保留边界、完成条件和真实后继。它不改候选、不审算法、不签业务 PASS。

当前事实：Reader 任务已发布到 GitHub，**尚未创建/发送真实 Reader 调用，尚无报告、verdict、Intake 或 ADOPTED**。狭义 PASS 后仍须实际 snapshot/Intake/check/dispatch。

<a id="delivery-scope"></a>
## 6. 本次交付范围与准确资格

本轮交付的是：首次实质管理判断、地图、完整专业任务及 Binding、Reader 任务、完整回答与两份 Return。

本轮不交付也不声称：

- Reader 回交或 Workmap Intake；
- 专业任务实际发送；
- S1 场景、S2 图、S3 观察；
- U2/U3 业务 Gate；
- Owner 接收；
- 正式 Cluster/H1/Quality、资金或交易结论。

<a id="remaining"></a>
## 7. 全部真实未完

1. 操作端按 exact `READER_TASK.md` 建立新的独立 review 调用并取得完整回交。
2. Reader 输入未变且狭义 PASS 后，运行真实 Workmap snapshot，形成 Intake，将 config 合法转为 ADOPTED，再做 check/dispatch。
3. 向新的执行 Pro 聊天实际发送完整 S1/S2/S3 任务；不按摘要或最新 remaining 缩范围。
4. 执行 Pro 完成基础行情场景发现、具体 Worker 工单、真实图/同源数据、U2/U3/后续/基线业务分析。
5. 管理按首个闭环、CHANGE、每四个有效结果与完整交付持续复看并最终接收。

这些未完只限制其依赖步骤；不存在 Reader/Intake 时不虚称专业已开工，也不把管理任务重新交执行 Pro判断。

<a id="continuation"></a>
## 8. 精确后继

主控下一责任不是重做 M-START，也不是直接发专业任务，而是：

1. fresh 核 `daowei2026/observe-iterate@759ba7104f6b9e400d1b872865cf5cf2627c4dd2` 的 reader-input 未漂移；
2. 以新独立 review recipient 发送 `reviews/management-R0001/READER_TASK.md`，按 V2 轮次合同保存 invocation/prompt/send/response/Returns；
3. 取得真实报告后按 verdict 路由：PASS 才走 Intake/ADOPTED；REPAIR_REQUIRED/INSUFFICIENT_EVIDENCE 回本管理聊天 M-REASSESS；
4. Workmap 真实采用后，向 `chatgpt:细节叙事生成_金标:BI01-V202-执行` 发送 `01_当前任务.md` 完整载荷，首发 mode `OBSERVATION_SCOPE`；
5. 继续原管理触发，不因本轮提交清零。

GitHub 正常通道本轮可用，因此没有使用备用 ZIP 成果运输。

<a id="question-work-return"></a>
## 9. Return 关系

机器可读回交见同目录：

- `ROLE_RETURN.json`
- `QUESTION_WORK_RETURN.json`

两者的完成、未完、材料、后继与本正文一致；`SUBMITTED` 只表示本次管理实物已交，不表示完整 BI-01 业务完成。
