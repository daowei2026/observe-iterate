# BI-01-V2-02 R0004 Reader Binding 格式纠正与有限回交修复决定

work_id: BI-01
run_id: BI-01-V2-02
role: management
invocation_id: BI01-V2-02-R0004-20261018T143706Z-4e789f60
assignment_token: BI01-V2-02-M-START-FORMAT-8e1a9756cfeb4576b703c9cac48fef9d

- 决定状态：`SUBMITTED / AUDIT_BINDING_CORRECTION_AND_ONE_LIMITED_RETURN_REPAIR_AUTHORIZED`
- 连续前项：`BI01-V2-02-R0002-20261018T133550Z-3e483710`
- 实质 Reader：`BI01-V2-02-R0003-20261018T135502Z-2de24e8b`
- 性质：原 M-START 签发责任内的格式纠正；保留已经完成的独立阅读、报告、PASS 及其资格边界，不重做业务审查，不改变 Workmap 候选、专业任务、预算、角色或完整业务后继。

<a id="format-correction"></a>
## 1. 管理亲自核实的问题与裁定

R0003 已完成真实独立只读委派：

- `485a796b1d709be81957f25851e62e8c56ddd688:runs/BI-01-V2-02/reviews/independent/WORKMAP_READER_R0001_INPUT.md::full` 给出狭义 `PASS`，无实质 finding；
- 报告记录了真实 invocation、独立性、冻结输入、18 项 source read、完整业务关系、资格外范围和唯一后继；
- R0003 `ROLE_RETURN.json` 通过既有 schema；
- R0003 `QUESTION_WORK_RETURN.json` 与原 Reader Binding 均只在题号 `WORKMAP-READABILITY` 上违反 `question_work.schema.json`，该字符串既不是 DR12 固定题，也不符合 `CASE-...` 格式；
- `reader_fingerprint=a29852320c44b64cf05e4a9250d86104f878718b10dc14a00fe58d18e036b9f8` 未变，当前不存在被审业务输入漂移。

因此裁定如下：

1. **R0003 的实质报告和狭义 PASS 保留。** 格式错误不推翻已经真实完成的独立阅读，也不要求另一 Reader 重新阅读或重新判断。
2. **题号改用 DR12 已有固定题 `AUDIT`。** 本委派本来就是明确授权的 `INDEPENDENT_REVIEW`；DR12 将 `AUDIT / INDEPENDENT_REVIEW` 作为既有审查题，schema 也直接允许 `AUDIT`。没有业务必要新造 `CASE-WORKMAP-READABILITY`，因此 `question_definitions` 保持空数组。
3. **历史不倒改。** 不修改 R0003 原报告、原回答、原 Return 或 transport provenance；它们继续准确记录当时发生的格式错误。
4. **只允许一次有限回交修复。** 原 Reader 聊天依据纠正后的 Binding，产生一个新 invocation 的完整回答、`ROLE_RETURN` 和 `QUESTION_WORK_RETURN`；仅改正题号/Binding 连接并引用既有报告，不重做审查、不修改 verdict、不生成第二份业务报告。
5. **采用仍未发生。** 修复 Return 真正取得并通过 schema、binding identity、after-return 与 Workmap 输入一致性检查前，`WORKMAP_BINDING.json` 继续保持 `NOT_CONFIGURED`，不得形成 Intake、ADOPTED 或专业首发。

<a id="unchanged-business"></a>
## 2. 不变的完整业务主线

R0001 的完整管理关系继续有效：

```text
U2/U3 Owner Decision、Narrative、Use Case
→ 固定 rb/i/hc 基础 KLine、small Zig、mid 贴近转折自主找真实场景
→ U2 位置、同一机会身份、成员及第三对象边界
→ U3 Progress / Friction / Retention / ObservabilityAndConstraint 的合法 As-Of 辨别力
→ 后续支持、削弱、反证或未知
→ 与 KLine、C0/N、静态分组、简单共同事件比较增量或无增量
→ Owner 可按图与同源数据核查的保留、修订、继续验证或停止行动
```

本次格式修复不恢复旧 `BI-01-V2-01`，不重算固定包，不新增场景类型、阈值、赢家或配额，不修改 aidata 边界，不缩减连续 S1/S2/S3 专业责任，也不把 Reader PASS 升格为 U2/U3 业务 PASS。

<a id="reader-pre-adoption"></a>
## 3. Reader 有限修复的采用前置与预算

管理现签发同一 Reader 的一次性有限修复：

- 角色：`review`；
- recipient：`chatgpt:细节叙事生成_金标:BI01-V202-地图只读接收-01`；
- mode：`INDEPENDENT_REVIEW`；
- 固定题：`AUDIT`；
- 原实质报告：`485a796b1d709be81957f25851e62e8c56ddd688:runs/BI-01-V2-02/reviews/independent/WORKMAP_READER_R0001_INPUT.md::full`；
- 原格式失败：`f0bb3089da99bf9664c1f0c45fb058a292cb5f9f:runs/BI-01-V2-02/provenance/turns/R0003/BINDING_FORMAT_CORRECTION_REQUIRED.md::full`；
- 原 transport：同 commit 的 `TRANSPORT_PROVENANCE.json::full`；
- 冻结 Workmap 业务输入仍为 `5e8e4c1bb184a97bfe47bc40493c667bb7b8185d`，不得重选或更新；
- 预算：一次有效有限回交；不重复读取 18 项未变正文，不重新写报告，不强制改变原 verdict。

完成标准：

1. 当前 Reader task 中唯一 `question-work/v2 BINDING` 通过锁定 schema，`question_ids=["AUDIT"]`，`question_definitions=[]`；
2. 新有限修复回答明确引用既有报告和原错误，不把格式修复说成第二次独立审查；
3. 新 `ROLE_RETURN` 使用新 invocation/token，artifact 指向既有独立报告，review verdict 仍为原 `PASS`，并准确声明没有重做审查；
4. 新 `QUESTION_WORK_RETURN` 使用当前纠正 Binding，`focus_results[0].question_id="AUDIT"`，其完成项只指向格式连接修复与既有报告；
5. 两份 Return 与新 invocation 一致并通过真实 schema/after-return 检查；
6. exact reader input 和 reader fingerprint 未变。

本修复不另设 RESULT/CHANGE/EFFORT 触发。它是一个已知、封闭、一次性的交付格式修复；主业务的持续触发仍由专业 S1/S2/S3 Binding 和管理责任承担。

<a id="reader-return-repair"></a>
## 4. 给原 Reader 的有限修复指令

只处理 R0003 的 Question Work 格式连接：

1. 读取本决定、纠正后的 Reader Binding、R0003 独立报告、`BINDING_FORMAT_CORRECTION_REQUIRED.md`、`TRANSPORT_PROVENANCE.json` 和原两份 Return；
2. 复用原报告已经记录的 18 项 source reads、独立性和实质判断，不重新阅读或重写未变业务输入；
3. 不修改或覆盖 `WORKMAP_READER_R0001_INPUT.md`、R0003 原回答或原 Return；
4. 形成本次新 invocation 的简短但完整回答，明确“原实质 PASS 保留，本次只修合法题号和 Binding/Return 连接”；
5. 交新 `ROLE_RETURN` 与 `QUESTION_WORK_RETURN`；新 QWR 的题号只能是 `AUDIT`，Binding 必须指向当前 Reader task 中唯一 JSON block；
6. affected refs 至少包括既有独立报告、原格式失败事实和纠正后的 Binding；
7. 若发现冻结业务输入、报告 blob、独立性或 verdict 发生实质变化，停止有限修复并按 `decide` 回管理，不自行改判。

<a id="repair-deliverables"></a>
## 5. 有限修复交付

交付仅包括：

- 新 invocation 的完整回答；
- 新 `ROLE_RETURN.json`；
- 新 `QUESTION_WORK_RETURN.json`；
- 对既有独立报告的准确引用；
- 对未重做内容、未改变资格和完整 BI-01 剩余的准确说明。

不交付：第二份 Workmap 业务报告、新 finding、新业务判断、Intake、ADOPTED、专业首发或 S1/S2/S3 结果。

<a id="repair-completion"></a>
## 6. 有限修复完成条件

只有当纠正后的 Binding 与新 QWR 均通过锁定 `question_work.schema.json`，新两份 Return 与新 invocation 一致，且既有报告和 reader fingerprint 未变时，本格式修复才完成。纯文本声称“已改为 AUDIT”不足以完成。

相同格式错误若在这一次有限补交后仍失败，停止继续调用 Reader，回本管理责任直接处理，不无限重发。

<a id="adoption"></a>
## 7. Reader 修复任务采用决定

本锚点授权运行端把本决定作为这一次有限 Reader return-repair 调用的 `task_adoption_ref`，并把当前 `READER_TASK.md` 的唯一、已纠正 `question-work/v2 BINDING` 作为 `binding_ref`。

运行端只有在以下条件同时满足时才可准备并发送：

1. current task 和 binding 来自同一个当前 Reader task commit；
2. Binding `plan_ref` 精确指向本决定 `#reader-pre-adoption`；
3. Binding 通过锁定 schema，题号为固定 `AUDIT`；
4. 本 R0004 invocation、决定、`ROLE_RETURN` 和真实 send receipt 能证明 management 身份与签发；
5. frozen Workmap `reader_fingerprint` 与 R0003 报告记录一致；
6. 当前没有同一有限修复在途、已发送未收取或未知发送需要先对账；
7. dispatcher prepare/verify、recipient 核验和 `bi01_run_gate.py pre-dispatch` 真实通过。

该采用只允许有限 return repair，不等于 Workmap `ADOPTED`、Reader 新 PASS、专业 Gate 或 Owner 接收。

<a id="accept-after-repair"></a>
## 8. 修复后的合法消费

新修复回交通过后，操作端/管理可将：

- R0003 的真实独立报告和原 `ROLE_RETURN`；
- 新 repair invocation 的合法 Binding、`ROLE_RETURN` 与 `QUESTION_WORK_RETURN`；
- 未变的 reader fingerprint；

共同作为首次 Reader 证据链。不得删除或覆盖原失败记录。

随后才可按 R0001 `DECISION.md#reader-decision`、R0002/R0004 决定及既有 Workmap 工具形成真实 Intake，并在 snapshot/check/dispatch 通过后转为 `ADOPTED`。只有 Workmap 真正采用后，才向新执行 Pro 聊天发送完整 S1/S2/S3 任务。

<a id="decide"></a>
## 9. 变化、冲突或再次失败

以下任一情况回 `chatgpt:细节叙事生成_金标:BI01-V202-管理`：

- frozen Workmap 输入或 reader fingerprint 改变；
- 原独立报告、独立性或 verdict 发生实质冲突；
- 纠正后的 Binding 或有限修复 Return 再次不通过；
- 需要改变专业业务任务、完成条件、预算或角色。

只限制 Reader/Intake/专业首发依赖；已经完成且未受影响的业务管理成果继续有效。

<a id="parent"></a>
## 10. 连续关系

本格式修复的 parent 是 R0003 已完成的独立报告，不是新 Case，也不是第二次审查。旧 `BI-01-V2-01` 仍不是 parent。

<a id="remaining"></a>
## 11. 本决定后的真实未完

1. 将原 Reader task 中非法题号改为固定 `AUDIT`，并把 Binding 连接到本决定；
2. 发布本次完整管理回交和两份 Return；
3. 操作端创建一次有限 review return-repair invocation，真实发送并收取合法 Return；
4. 修复通过后形成首次 Workmap Intake/ADOPTED；
5. 再首发完整 S1/S2/S3 专业任务并继续 R0001 的 RESULT/CHANGE/EFFORT 管理责任。

<a id="continuation"></a>
## 12. 精确后继

本轮 Return 发布后，主控应 fresh 读取当前 Reader task，取得唯一纠正 Binding 的准确 line selector，以该任务全文为 `current_task_ref`、该 JSON block 为 `binding_ref`、本决定 `#adoption` 为 `task_adoption_ref`，沿 `return_repair` 路线建立一个新的 `review / INDEPENDENT_REVIEW` invocation。该调用只做本决定 §4 的有限格式修复；未真实发送前保持 `NOT_SENT`。
