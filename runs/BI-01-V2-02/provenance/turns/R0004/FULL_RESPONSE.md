# BI-01-V2-02 R0004 M-START 格式纠正完整管理回交

[BI01-V2-02-R0004-20261018T143706Z-4e789f60]

- `work_id`: `BI-01`
- `run_id`: `BI-01-V2-02`
- `invocation_id`: `BI01-V2-02-R0004-20261018T143706Z-4e789f60`
- `assignment_token`: `BI01-V2-02-M-START-FORMAT-8e1a9756cfeb4576b703c9cac48fef9d`
- `role`: `management`
- 连续前项：`BI01-V2-02-R0002-20261018T133550Z-3e483710`
- 实质 Reader：`BI01-V2-02-R0003-20261018T135502Z-2de24e8b`
- 回交状态：`SUBMITTED`
- 当前准确状态：R0003 独立报告的狭义 PASS 保留；Reader Binding 已纠正为固定题 `AUDIT`；一次有限 Return repair 已签发但尚未建立/发送；Workmap 仍 `NOT_CONFIGURED`，尚无 Intake、ADOPTED、专业首发或 S1/S2/S3 结果。

<a id="management-decision"></a>
## 1. 管理决定

### 1.1 已核实的实际问题

操作端保存的真实证据显示：

- `485a796b1d709be81957f25851e62e8c56ddd688:runs/BI-01-V2-02/reviews/independent/WORKMAP_READER_R0001_INPUT.md::full` 已完成一次真实、独立、完整的 Workmap 只读审查；verdict 为狭义 `PASS`，无实质 finding；
- R0003 `ROLE_RETURN.json` 通过 schema；
- R0003 `QUESTION_WORK_RETURN.json` 在 `focus_results[0].question_id` 处失败，因为使用了 `WORKMAP-READABILITY`；
- 当时 Reader Binding 的 `question_ids[0]` 也因同一字符串失败；
- `WORKMAP-READABILITY` 既不在 DR12/schema 的固定题集合，也不满足 `CASE-...` 正则；
- R0003 报告记录的 frozen reader input 未变，`reader_fingerprint=a29852320c44b64cf05e4a9250d86104f878718b10dc14a00fe58d18e036b9f8`；
- 当前 config 仍为 `NOT_CONFIGURED`，没有 Intake、ADOPTED 或专业首发。

因此，这不是 Reader 业务判断失败，也不是被审输入漂移；它是原管理签发中一个明确、局部、可定向修复的 Question Work 题号格式错误。

### 1.2 题号裁定

管理选择 **DR12 既有固定题 `AUDIT`**，不创建 `CASE-WORKMAP-READABILITY`。

理由：本次委派本来就是有明确权限的 `AUDIT / INDEPENDENT_REVIEW`。DR12 已把它列为固定审查题，`question_work.schema.json` 也直接允许 `AUDIT`。新造 CASE 不增加业务信息，反而会增加定义、授权和后继维护成本。

### 1.3 历史和实质成果处置

- R0003 原报告、原回答、原两份 Return、transport provenance 和格式失败记录全部保留，不倒改；
- R0003 的独立性、实质阅读、狭义 PASS、无 finding 和资格边界保留；
- 不要求原 Reader 重新阅读 18 项正文、重写报告、重新判断或生成第二份 PASS；
- 只允许原 Reader 聊天基于纠正 Binding，产生一个**新 invocation** 的完整回答和两份合法 Return；
- 本修复不创建新业务审查，不改变 Workmap 候选、专业任务、预算、角色或完整业务后继。

<a id="plan"></a>
## 2. 已执行的实际处置

### 2.1 R0004 管理决定

已发布：

`daowei2026/observe-iterate@af50358f6de756d56759bc004baacf7ed596a2d0:runs/BI-01-V2-02/reviews/management-R0004/DECISION.md::full`

其中：

- `#format-correction` 给出问题性质和题号裁定；
- `#reader-pre-adoption` 给出一次有限 repair 的角色、recipient、预算、完成条件和无独立触发理由；
- `#reader-return-repair` 给原 Reader 明确“不重读、不重写、不重判”的有限指令；
- `#repair-deliverables/#repair-completion` 固定交付和真实完成条件；
- `#adoption` 授权运行端把该决定作为有限 repair 的 `task_adoption_ref`；
- `#accept-after-repair/#decide` 规定成功消费和异常路由。

### 2.2 原 Reader task 的 Binding 纠正

已更新：

`daowei2026/observe-iterate@4a4c8d9e1a6dd7726ed2147b49313c3fa17729c2:runs/BI-01-V2-02/reviews/management-R0001/READER_TASK.md::#question-work-binding`

纠正后的 Binding：

- `question_ids=["AUDIT"]`；
- `question_definitions=[]`；
- `plan_ref` 指向 R0004 `#reader-pre-adoption`；
- `batch_result` 只要求补交合法 Return，不要求重新审查；
- `focus_ref` 指向 `#reader-return-repair`；
- 原 frozen README/map/专业 task/config 和 Owner GO 仍保留为 exact source；
- R0003 报告作为已完成阅读的 `reuse_evidence`；
- R0003 格式失败、transport 和原 Return 作为 provenance source；
- `parent.status=PRESENT`，parent 为 R0003 实质报告；
- 四条路线分别保持 review repair、management accept/decide 和有限补交责任；
- `triggers=[]`，一次性格式修复不复制主业务触发。

Binding 中题号 `AUDIT` 和空 `question_definitions` 与锁定 schema 的允许结构一致。未来 repair invocation 仍须由操作端实际运行完整 schema、dispatcher prepare/verify、recipient 和 pre-dispatch；本管理回交不伪称未来机械检查已执行。

### 2.3 完整业务决定保持不变

本次没有修改 R0001 的业务主线：

```text
U2/U3 原 Owner 业务问题
→ 固定 rb/i/hc 基础行情自主发现有价值场景
→ U2 位置、机会身份、成员与第三对象边界
→ U3 四个 Movement Evidence Bundles 的合法 As-Of 辨别力
→ 后续支持、削弱、反证或未知
→ 与 KLine、C0/N、静态组、简单共同事件比较增量
→ Owner 可定位图和同源数据核查的设计行动
```

广域 raw 与单一完整 Case×五 As-Of 的证据分层、不同 lifecycle/bar 数/单位的可比性纪律、固定两包不重算、AI 不看像素图、旧 V2-01 暂停、S1/S2/S3 连续责任和业务完成条件均未改变。

<a id="completed"></a>
## 3. 本次已完成

1. 读取并核实 R0003 `BINDING_FORMAT_CORRECTION_REQUIRED.md`、transport provenance、完整回答、两份 Return 和独立报告；
2. 对照 DR12、DR14 和 `question_work.schema.json`，确认唯一格式失败是未受控题号；
3. 裁定采用固定题 `AUDIT`，明确不需要新 CASE；
4. 发布 R0004 真实管理决定，签清有限修复范围、预算、完成、采用与成功/失败路由；
5. 在原 Reader task 中纠正唯一 Binding，并使用 R0003 报告作为未变正文的复用证据；
6. 明确不倒改 R0003 历史，不让 Reader 重做已完成阅读；
7. 保持 `WORKMAP_BINDING.json=NOT_CONFIGURED`，未预造 repair Return、Intake、ADOPTED 或专业结果；
8. 更新真实进展，并形成本轮完整管理回答、`ROLE_RETURN` 和 `QUESTION_WORK_RETURN`。

<a id="material-use"></a>
## 4. 材料使用记录

### 本次重新取得并用于裁定

- `f0bb3089da99bf9664c1f0c45fb058a292cb5f9f:runs/BI-01-V2-02/provenance/turns/R0003/BINDING_FORMAT_CORRECTION_REQUIRED.md::full`
- 同 commit 的 `TRANSPORT_PROVENANCE.json`、`FULL_RESPONSE.md`、`ROLE_RETURN.json`、`QUESTION_WORK_RETURN.json`
- `485a796b1d709be81957f25851e62e8c56ddd688:runs/BI-01-V2-02/reviews/independent/WORKMAP_READER_R0001_INPUT.md::full`
- `ae5826028a8441a6ee018ebfac48eb0568a7be72:runs/BI-01-V2-02/reviews/management-R0002/DECISION.md::full`
- `e3d65aa5131be591416b861343afa9953eaf6661:runs/BI-01-V2-02/reviews/management-R0001/READER_TASK.md::full`
- `30d6cd28ca4cc52eb201f0aa474f9f4c93b74080:runtime/dual_route_execution/DR12_PROFESSIONAL_QUESTION_CATALOG.md::full`
- 同 commit 的 `DR14_QUESTION_WORK_CONTRACT.md` 和 `runtime/overlay/tools/question_work.schema.json`。

### 已读未变并复用

Owner GO、R0001 地图/任务/决定、V2 00—07、U2/U3 Owner Decision/Narrative/Use Case 和两份固定数据的业务判断没有出现新冲突；本次不重复开展场景、算法或数据分析。R0003 报告已经记录其 18 项正文的完整阅读，本次只复用该真实证据。

### 未执行

- 未建立或发送未来有限 repair invocation；
- 未取得新的 Reader FULL_RESPONSE/Return；
- 未运行未来 round 的真实 schema/prepare/verify/pre-dispatch/after-return；
- 未形成 Workmap Intake/ADOPTED；
- 未发送专业任务或产生 S1/S2/S3 结果。

<a id="validation"></a>
## 5. 自检与资格

已 fresh 核：

- R0004 决定 commit 为 `af50358f6de756d56759bc004baacf7ed596a2d0`；
- 当前 Reader task commit 为 `4a4c8d9e1a6dd7726ed2147b49313c3fa17729c2`；
- 当前唯一 Binding 题号为 `AUDIT`，`question_definitions=[]`；
- Binding `plan_ref` 与 R0004 `#reader-pre-adoption` 一致；
- frozen README/map/task/config 仍统一指向 `5e8e4c1...`；
- 原独立报告和 R0003 历史文件未修改；
- Workmap config 尚未采用。

本次只完成有权管理签发和静态合同纠正。操作端必须在真实未来 round 上取得完整机械验证和发送证据。

<a id="delivery-scope"></a>
## 6. 本次交付范围

本轮交付：

- R0004 管理裁定；
- 原 Reader task 上的合法 `AUDIT` Binding；
- 一次有限 Return repair 的采用、交付、完成和路由；
- 真实进展投影；
- 本次完整管理回答和两份 Return。

本轮不交付、不冒称：

- 新 Reader invocation 或实际修复 Return；
- 第二份独立审查报告或新 PASS；
- Workmap Intake/ADOPTED；
- 专业首发；
- S1/S2/S3 结果、U2/U3 业务 Gate 或 Owner 接收。

<a id="remaining"></a>
## 7. 全部真实未完

1. 操作端 fresh 读取当前 Reader task，取得唯一 JSON block 的准确 line selector；
2. 以任务全文为 `current_task_ref`、该 block 为 `binding_ref`、R0004 `DECISION.md#adoption` 为 `task_adoption_ref`，沿 `return_repair` 路线创建一次新的 review invocation；
3. 真实运行 schema、dispatcher prepare/verify、recipient 和 `bi01_run_gate.py pre-dispatch`，并保持 `NOT_SENT` 到检查完成；
4. 原 Reader 只交新 invocation 的完整回答和合法两份 Return，不重做报告；
5. 操作端运行 after-return、Question Work association 和 reader fingerprint 检查；
6. 修复成功后，以 R0003 实质报告和新合法 Return 共同形成 Reader 证据链，生成真实 Workmap Intake/ADOPTED；
7. Workmap 采用后，向新执行 Pro 聊天发送完整 S1/S2/S3 专业任务；
8. 继续 R0001 已签的 RESULT/CHANGE/EFFORT 管理责任和完整业务接收。

<a id="continuation"></a>
## 8. 精确后继

主控下一动作是一次**有限 Reader return-repair**，不是重开 M-START、重做独立审查或直接发专业任务：

```text
fresh 读当前 READER_TASK.md
→ 取得唯一 AUDIT Binding 的准确 selector
→ current_task_ref / binding_ref / R0004#adoption 装配
→ 沿 return_repair 路线创建 review / INDEPENDENT_REVIEW invocation
→ schema + prepare/verify + recipient + pre-dispatch
→ 实际发送同一 Reader 聊天
→ 只补新 invocation 的合法两份 Return
→ after-return 与关联检查
→ 成功后才形成 Intake/ADOPTED
→ 再首发完整 S1/S2/S3 专业任务
```

如果 frozen input、reader fingerprint、原报告、独立性或 verdict 出现实质变化，停止有限修复并回本管理聊天；不得沿用旧 PASS，也不得由操作端自行改判。

GitHub 正常通道本轮可用，因此没有使用备用 ZIP 成果运输。

<a id="question-work-return"></a>
## 9. Return 关系

同目录机器可读回交：

- `ROLE_RETURN.json`
- `QUESTION_WORK_RETURN.json`

`SUBMITTED` 只表示本次有权管理纠正和 repair 签发已经交付，不表示 Reader 格式修复、Workmap 采用或完整 BI-01 业务已经完成。
