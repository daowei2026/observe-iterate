# BI-01-V2-02 R0001 首次实质管理决定

- `invocation_id`: `BI01-V2-02-R0001-20261018T130131Z-7f26abeb`
- `assignment_token`: `BI01-V2-02-M-START-a6b833b62eac4a0fa8c23b037a4bac05`
- 决定角色：`management`
- 决定状态：`SUBMITTED / PENDING_WORKMAP_READER_AND_INTAKE`
- 旧运行关系：`BI-01-V2-01` 仅为暂停历史，不是 parent，不继承其业务结果或权限。

<a id="authority"></a>
## 1. 权力与采用来源

本决定依据：

- `daowei2026/observe-iterate@04fea2ae48eb6bb50144e2b8b2e3fccca17ec7ea:runs/BI-01-V2-02/OWNER_START.md::full`
- `daowei2026/observe-iterate@30d6cd28ca4cc52eb201f0aa474f9f4c93b74080:professional/v2/00_PURPOSE_AND_THREE_STEP_FLOW.md::full`
- 同 commit 的 `01/02/03/04/05/06/07` 及 DR06/08/12/13/14、运行与 Workmap 合同
- `daowei2026/complex-systems-vocabulary@48f55f53e25d04e5b4b59fae1e652dd4b679c9d3` 的 U2/U3 Owner Decision、U2 Narrative/Use Case、U3 Narrative/Use Case
- 本次项目附件两份固定 ZIP 的实际成员与关键 CSV 核查

候选 Local Contract 和历史实现可以按具体方法问题追溯，但不取得正式方法或生产资格。

<a id="business-relationship"></a>
## 2. 管理对完整业务的判断

Owner 真正要检验的是：在基础行情里有意义的共同方向运动中，U2 是否给出了有用的同一机会身份和成员边界，U3 当时可知的四类 Movement Evidence 是否增加了对成员后续运动质量的辨别；如果没有，具体是设计无增量、参考输出未覆盖、可比性不足，还是观察范围不合法。

因此本轮不能被下面任一局部对象接管：

- C1 raw 候选数量；
- 单 Case 五个 As-Of；
- 某个字段缺失或可视化错误；
- 已存在的旧图；
- 一份完整 schema；
- 工具是否能运行。

这些都只是证据或施工状态。业务完成必须回到“市场过程—U2 身份—U3 当时差异—后续支持/反证—基线增量—行动”链。

<a id="verified-input"></a>
## 3. 管理亲自核实的承重事实

1. 上游包中 rb/hc/i 各 9,080 根 30m KLine；贴近转折 1,457 条。
2. 广域 C1 raw 有 304 个 exact-actual-UTI 参考候选：205 个两成员、99 个三成员，全部未正式 Formation/Assessment。它们提供广域入口和第三对象挑战，不是正式簇。
3. 完整参考链只有一个 Case、五个 As-Of。C2 无 official commit/H1；S 的 outside_count 为 0；R03 全部 Withheld。
4. R02 的 15 行可以作为客观路径事实，但成员处在不同 lifecycle 和观察长度，且 raw movement 是各自价格单位。不能直接横向排名。
5. 当前上游 ZIP 外层哈希与历史记录不一致，但内部 CSV 与本包 manifest 一致。它限制“与历史 ZIP 字节同一”的主张，不足以冻结全部观察。
6. cgpterm 指定分支仍锁定 `1e28be8e361babadb3ef4b5e647c53ce625ef778`；observe-iterate 业务源锁定 `30d6cd...`。未发现需要改变 Owner 的版本锁。

<a id="management-decision"></a>
## 4. 采用、撤销与未定事项

### 4.1 直接采用

- 业务方向：共同方向机会、U2 机会组织、U3 成员质量辨别。
- 方法顺序：先基础行情，再 U2，再 U3/限制，再后续事实和基线增量。
- 输入范围：固定 rb/i/hc 与两份 ZIP，不重算、不换源。
- 资格边界：actual/confirm/As-Of、Working/Completed、Reference/Shadow/Withheld 分开。
- 四方面：`ProgressBundle`、`FrictionBundle`、`RetentionBundle`、`ObservabilityAndConstraintBundle`。
- 基线：原 KLine、C0/N 单品种画像、静态三品种、简单共同事件关联。
- 工具与消费：aidata 是统一图工具；Owner 看图，AI 读同源数据。

### 4.2 直接撤销

以下不再作为另一份“当前完整任务”，也不列为 deferred required：

- 旧 V2-01 的任务、Gate、Workmap、Reader、R10、在途、样本分类、主 Case 和完成状态。
- 由 raw 候选、字段易取性或旧 F01—F14 分类决定本轮场景。
- 预设场景类型、阈值、赢家和配额。
- 把单 Case、五个 As-Of、首图、图数、字段问题数作为停点。
- 把 C2 Shadow/R03 Withheld/N 层升格成正式 Cluster、Quality 或 U3。
- 先重算整套 U2/U3、全面审计仓库、建设视觉链、修改 aidata 现有分支或另建图工具。
- 为已经取消的工作保留专属实现、检查或“未来必须完成”的表述。

### 4.3 真正未定

- 基础行情中最终值得深入的场景是什么、数量多少；
- 每个场景 U2 位置/成员是否合理；
- 四束能否产生当时合法差异、差异是否有增量；
- 固定数据不足是局部限制还是足以否定某项设计价值；
- 哪些设计应保留、修改、继续验证或停止。

这些只能由本轮真实观察决定，管理不预填答案。

<a id="plan"></a>
## 5. 实际计划与工作安排

### 第一步：S1 业务场景发现先启动

执行 Pro 完整阅读承重业务原文，直接消费上游 KLine/Zig/mid 结构化数据和必要基础图。先形成：

- 固定范围的实际搜索覆盖；
- 值得研究的位置及选择理由；
- 是否回顾性发现；
- 共同方向运动、成员强弱或“整组都弱/无法判断”的具体问题；
- 主要反例和需要在图上检查的对象。

不得先查 U2/U3 输出来决定“应该选哪里”。首个有价值位置可以立即进入 S2，S1 对固定范围继续。

### 第二步：S2 形成同口径图与数据

执行 Pro 对具名场景签 Worker 技术工单。Worker：

- 先画 KLine/Zig/mid 基础图；
- 再按问题叠加 U2 actual/confirm、成员/第三对象、N 和真实可用 U3；
- 使用固定 ZIP 原件和现有 aidata；
- 核真实浏览器图层、run/node/timespan 与同源结构化数据；
- 只在真实通用缺口且业务推进必需时，于 aidata 新独立分支修通。

工具问题只限制依赖它的图，不冻结可继续的数据阅读、场景发现或其他场景。

### 第三步：S3 随场景循环检验

每个重要场景都按以下顺序给判断：

1. 实际市场过程及选择理由；
2. U2 原设计要表达什么、固定数据实际输出什么；
3. U2 位置、方向、成员、第三对象和及时性是否合理；
4. U3 四束当时能/不能区分什么；
5. 后续合法 Outcome 或探索性路径怎样支持、削弱、反证；
6. 相对 KLine/C0/N/静态组/简单共同事件多了什么，或没有多什么；
7. 设计行动、适用范围和推翻条件。

完整链参考 Case 用于深挖 Current→Outcome；广域场景用于检验位置/成员与基线，不伪装有完整 U3。

### 第四步：管理复看与收拢

- 首个真实闭环：非阻塞 M-REASSESS，检查实际业务是否启动和任务是否需要调整。
- 重要前提冲突或连续两次实质回交仍停留在来源/工具/格式：M-REASSESS，改变实际安排。
- 每四个有效结果：EFFORT 复看。
- 完整阶段满足：M-CLOSE；否则保持连续后继。

<a id="budget"></a>
## 6. 投入预测与触发

这是完成预测，不是 Case 配额或强制用满：

- 专业执行：预计 6—10 个有效 Pro 回交，覆盖场景发现、首图、多个 S2/S3 循环、综合与自查。
- 首次 Workmap 独立只读接收：预计 1 个有效 review 回交。
- 管理：首个结果复看、必要变化复看、阶段收拢预计 2—4 个有效回交。
- Worker 技术执行按实际场景工单发生，不计为 Pro 业务结论。

每四个有效专业/必要管理结果触发一次非阻塞投入复看；新聊天、普通 commit 或局部修复不清零。若固定数据很快精确证明关键问题不可判断，可少于预测；若出现真实反例或图迭代，可超过预测，但必须解释新增业务价值。

<a id="reader-decision"></a>
## 7. 首次 Workmap 只读接收决定

本地图是全新 run 的第一张地图，并实质改变了旧试跑的选场景方法与证据组织。为避免作者自签“别人一定读得懂”，签发一次新的独立只读接收，检查：

- 是否能从 Owner 目标恢复完整业务链；
- 是否清楚区分广域 raw 与单 Case 完整链；
- 是否清楚四束、时间、状态和正式资格；
- 是否无旧 V2-01 任务泄漏、无预分类/配额/单 Case 停点；
- task、Binding、路由、完成条件是否可执行。

读者不修改候选，不审算法正确性，不签业务 PASS，不扩成全仓审计。若 PASS，仅允许在相同输入上机械形成 Workmap Intake；若 REPAIR_REQUIRED，回管理定向修订。

<a id="remaining"></a>
## 8. 管理仍承担的未完

本次管理判断和任务签发已完成；以下责任仍在：

- 接收 reader 的实质歧义或确认；
- 核 Workmap Intake 真正采用后专业首发；
- 消费首个业务闭环、前提变化与投入触发；
- 判断专业结果是否真正回答 U2/U3 业务问题；
- 在完整条件满足时接收或安排下一轮设计行动。

本轮结束不取消这些责任，也不把它们转交给执行 Pro“全面检查”。
