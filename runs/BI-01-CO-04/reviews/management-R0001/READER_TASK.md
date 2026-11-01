task_id: BI01-CO-04-WORKMAP-READER-01
status: ISSUED
work_id: BI-01
run_id: BI-01-CO-04
role: review
professional_mode: INDEPENDENT_REVIEW
recipient_ref: chatgpt:BI-01-CO-04:workmap-reader-01
issued_by: chatgpt:BI-01-CO-04:management
issued_from_invocation: BI01-CO-04-R0002-MSTART-HANDOFF-518040c2

# BI-01-CO-04 首次 Workmap 独立 Reader 任务

<a id="reader-goal"></a>
## 1. 目标

对固定在 `ed9a32badf4077c25534184da28b0ad41db396ec` 的本 Run 工作面做一次具名、独立、只读的派发前审查。核验 Owner GO、完整业务目标、地图、当前正式专业任务、Workmap Binding 和真实方法入口是否一致地支持下一步 Professional 执行，并识别足以阻断派发的具体断裂。

本任务不形成市场观察，不接收 `CASE_OBSERVATION` 业务结果，不替管理作下一专业问题裁定，也不因结构完整而自动给出业务 PASS。

<a id="reader-full-scope"></a>
## 2. 完整审查范围

Reader 必须全文读取 Binding 所列全部材料，并核：

1. Run、work、角色、Owner GO 与当前任务身份是否一致；
2. 完整业务目标是否仍可从当前工作面恢复，地图是否保留重要未完；
3. 当前专业任务是否具备明确问题、范围、输入资格、完成条件、触发和回交关系；
4. `source_reads` 是否覆盖任务实际依赖的 Owner／方法正文，且未以摘要、hash 或旧 Run 权力替代；
5. 当前任务、地图、Binding、Intake 与管理采用是否存在实质冲突；
6. Reader 与 Professional 的身份、输出、接收、发送和资格是否分离；
7. 是否存在足以阻止当前 Professional 派发的具体断裂，以及哪些仅属非阻断限制。

不得递归审计全仓、重做 R0001 业务分析、审查尚未产生的专业结果，或把旧 Run 事实升级为当前资格。

<a id="reader-focus"></a>
## 3. 集中问题

> 固定输入是否把 Owner GO、完整业务目标、当前任务、专业方法入口、证据资格、未完与真实派发关系连成一个可由 Professional 继续的工作面；是否存在足以阻止当前专业派发的具体断裂、矛盾、遗漏或越权？

重点区分：

- **阻断项：**会使 Professional 收到错误任务、错误权力、不可恢复的承重正文或错误输入身份；
- **非阻断限制：**需要在专业执行中继续核验，但不应由 Reader 先做业务研究；
- **未来事项：**只有专业结果形成后才可能触发的独立专业审查、管理接收或 Owner 反馈。

<a id="reader-coverage"></a>
## 4. 证据与独立性边界

- `input_commit`: `ed9a32badf4077c25534184da28b0ad41db396ec`
- `workmap_snapshot`: `5f24d63895be9d5f52182fd8e4fa94a901667e8bdfda0fc4529f9addcecf19b2`
- `reader_fingerprint`: `b5f0c9826e1b7f639e39f64276e31d26a834e8ffcbd855497c6be628a63fc06b`
- `scope`: `bi01`
- `output_root`: `runs/BI-01-CO-04/reviews/independent/workmap-01`

Reader 必须独立于 R0001 地图／任务构建者。主控本地检查、管理 R0002、本地未提交报告和旧 Run Reader 均不能替代本调用。对未实际读取、不可取得或无法恢复的正文须如实记录。

<a id="reader-deliverables"></a>
## 5. 必交付

在专属输出目录提交：

1. `REPORT.md`：输入身份、实际材料使用、逐项核验、阻断项、非阻断限制、未审范围和结论；
2. 结论只能是 `PASS`、`REPAIR_REQUIRED` 或 `INSUFFICIENT_EVIDENCE`，并给出可追溯理由；
3. `QUESTION_WORK_RETURN.json` 与 `ROLE_RETURN.json`，身份、Binding、continuation 和 remaining 必须一致；
4. 准确记录 input commit、reader fingerprint、invocation 和 assignment token；
5. 明确不能推出的内容：Reader PASS 不等于业务结果通过，也不等于 Professional 已发送。

<a id="reader-completion"></a>
## 6. 完成条件

只有全文读取全部 source_reads、对集中问题给出有证据的结论、区分阻断与非阻断事项、交完整报告与两份一致 Return，才可回管理接收。发现输入变化时不得沿用旧 fingerprint；应报告受影响范围和新的最小恢复条件。

<a id="reader-budget"></a>
## 7. 投入边界

当前仅授权一次真实 Reader Pro 调用。若出现确切阻断，可在管理定向修复后复核受影响部分；不得扩成全仓审计、业务方法再设计或历史 Run 重审。Reader 调用不计入首项 Professional 专业任务的有效调用预算。

<a id="reader-no-trigger"></a>
## 8. 无额外触发说明

本任务本身就是 R0001 承诺的单次派发前证据生产；完成后直接按 `accept` 回管理，不再建立 RESULT／CHANGE／EFFORT 触发。输入发生变化或证据不足按 `decide` 回管理，不自行重签新任务。

<a id="reader-parent"></a>
## 9. Parent

这是本 Run 首次正式 Workmap Reader，`NOT_APPLICABLE_NEW_CASE`。旧 Run Reader、本地主控检查和未提交报告不构成 parent，也不取得当前输入资格。

<a id="reader-same-work"></a>
## 10. same_work

在输入仍与冻结 fingerprint 一致时，继续完成本任务全部只读审查范围，不以找到一项问题或核完一份文件为停点。不得修改地图、任务、Binding、Intake 或业务 artifacts。

<a id="reader-accept"></a>
## 11. accept

将完整报告与两份 Return 交 `chatgpt:BI-01-CO-04:management`。管理按 R0002 决定的 `#reader-accept` 核独立性、输入一致性、证据和结论，再决定是否记录 Intake 及放行适用 preflight。

<a id="reader-decide"></a>
## 12. decide

若冻结输入已变化、必要正文不可取得、角色独立性不成立，或发现超出只读审查授权的真实冲突，准确说明受影响范围并回管理。不得自行修改工作面、扩大审查或代发 Professional。

<a id="reader-return-repair"></a>
## 13. return_repair

只修补两份 Return 的确切结构、引用或一致性缺件，保留原审查实质与资格。缺少实际读取、证据或完整审查时继续原 Reader 工作，不用 metadata 冒充完成。

<a id="question-work-binding"></a>
## 14. QUESTION_WORK_BINDING

```json
{
  "schema": "question-work/v2",
  "kind": "BINDING",
  "work_id": "BI-01",
  "goal_ref": {
    "repo": "daowei2026/observe-iterate",
    "commit": "ed9a32badf4077c25534184da28b0ad41db396ec",
    "path": "professional/exploration/00_BUSINESS_OBJECTIVE.md",
    "selector": "full"
  },
  "plan_ref": {
    "repo": "daowei2026/observe-iterate",
    "commit": "9f52cbc2e51ca709af6f71a70ff53f8f4d6d3d34",
    "path": "runs/BI-01-CO-04/reviews/management-R0002/DECISION.md",
    "selector": "#reader-pre-adoption"
  },
  "full_scope_ref": {"answer_ref": "#reader-full-scope"},
  "batch_result": "对固定输入完成一次独立只读 Workmap 审查，明确是否存在阻断当前 Professional 派发的具体断裂，并区分非阻断限制；交完整证据、结论和两份一致 Return，不形成市场业务判断或自动通过。",
  "question_ids": ["AUDIT"],
  "professional_mode": "INDEPENDENT_REVIEW",
  "focus_ref": {"answer_ref": "#reader-focus"},
  "coverage_ref": {"answer_ref": "#reader-coverage"},
  "source_reads": [
    {"source":{"repo":"daowei2026/observe-iterate","commit":"ed9a32badf4077c25534184da28b0ad41db396ec","path":"runs/BI-01-CO-04/README.md","selector":"full"},"requirement":"FOCUS_FULL","purpose":"核本Run入口、当前阶段、动态正本与旧Run不继承边界。","reuse_evidence":null},
    {"source":{"repo":"daowei2026/observe-iterate","commit":"ed9a32badf4077c25534184da28b0ad41db396ec","path":"runs/BI-01-CO-04/00_长程推进地图.md","selector":"full"},"requirement":"FOCUS_FULL","purpose":"核完整终点、证据资格、进展、全部重要剩余和直接后继。","reuse_evidence":null},
    {"source":{"repo":"daowei2026/observe-iterate","commit":"ed9a32badf4077c25534184da28b0ad41db396ec","path":"runs/BI-01-CO-04/01_当前任务.md","selector":"full"},"requirement":"MODE_FULL","purpose":"核当前Professional任务、问题、范围、完成条件、触发、Binding和回交路线。","reuse_evidence":null},
    {"source":{"repo":"daowei2026/observe-iterate","commit":"ed9a32badf4077c25534184da28b0ad41db396ec","path":"runtime/config/WORKMAP_BINDING.json","selector":"full"},"requirement":"BOUNDARY","purpose":"核当前Workmap路径、方法入口、监看根与Reader专属输出排除。","reuse_evidence":null},
    {"source":{"repo":"daowei2026/observe-iterate","commit":"ed9a32badf4077c25534184da28b0ad41db396ec","path":"runs/BI-01-CO-04/OWNER_START.md","selector":"full"},"requirement":"MODE_FULL","purpose":"核本Run真实Owner GO、角色分工、写面和授权边界。","reuse_evidence":null},
    {"source":{"repo":"daowei2026/observe-iterate","commit":"ed9a32badf4077c25534184da28b0ad41db396ec","path":"professional/README.md","selector":"full"},"requirement":"BOUNDARY","purpose":"核专业背景与动态任务的权力分离。","reuse_evidence":null},
    {"source":{"repo":"daowei2026/observe-iterate","commit":"ed9a32badf4077c25534184da28b0ad41db396ec","path":"professional/exploration/README.md","selector":"full"},"requirement":"BOUNDARY","purpose":"核探索阶段的材料组织与当前工作面关系。","reuse_evidence":null},
    {"source":{"repo":"daowei2026/observe-iterate","commit":"ed9a32badf4077c25534184da28b0ad41db396ec","path":"professional/exploration/00_BUSINESS_OBJECTIVE.md","selector":"full"},"requirement":"MODE_FULL","purpose":"核完整业务目标、阶段定位和允许无候选的结果。","reuse_evidence":null},
    {"source":{"repo":"daowei2026/observe-iterate","commit":"ed9a32badf4077c25534184da28b0ad41db396ec","path":"professional/exploration/01_EXISTING_FEATURES_AND_CAPABILITIES.md","selector":"full"},"requirement":"FOCUS_FULL","purpose":"核既有特征能力及方向、确认状态等边界。","reuse_evidence":null},
    {"source":{"repo":"daowei2026/observe-iterate","commit":"ed9a32badf4077c25534184da28b0ad41db396ec","path":"professional/exploration/02_CURRENT_WORKING_IDEAS.md","selector":"full"},"requirement":"FOCUS_FULL","purpose":"核候选设想被保留为待实践假设而非固定Gate。","reuse_evidence":null},
    {"source":{"repo":"daowei2026/observe-iterate","commit":"ed9a32badf4077c25534184da28b0ad41db396ec","path":"professional/exploration/03_TOOLING_AND_DATA_USAGE.md","selector":"full"},"requirement":"FOCUS_FULL","purpose":"核正式数据、工具、图面、时间语义与权限边界。","reuse_evidence":null},
    {"source":{"repo":"daowei2026/observe-iterate","commit":"ed9a32badf4077c25534184da28b0ad41db396ec","path":"professional/exploration/04_EXISTING_BUSINESS_REFERENCES.md","selector":"full"},"requirement":"BOUNDARY","purpose":"核历史来源只被定向使用且不继承资格。","reuse_evidence":null},
    {"source":{"repo":"daowei2026/observe-iterate","commit":"ed9a32badf4077c25534184da28b0ad41db396ec","path":"professional/exploration/05_OWNER_PROCESS_EXPLANATION.md","selector":"full"},"requirement":"MODE_FULL","purpose":"核Owner完整观察过程、复杂情况与反馈方式仍可恢复。","reuse_evidence":null},
    {"source":{"repo":"daowei2026/observe-iterate","commit":"ed9a32badf4077c25534184da28b0ad41db396ec","path":"dual_route_execution/DR14_QUESTION_WORK_CONTRACT.md","selector":"full"},"requirement":"BOUNDARY","purpose":"核Binding、Return、触发与路线的现行合同。","reuse_evidence":null},
    {"source":{"repo":"daowei2026/observe-iterate","commit":"ed9a32badf4077c25534184da28b0ad41db396ec","path":"overlay/08_自然语言运行提示_v0.3.md","selector":"full"},"requirement":"PROVENANCE_TRIGGER","purpose":"核实际派发、接续和不可虚报发送的运行边界。","reuse_evidence":null}
  ],
  "deliverables_ref": {"answer_ref": "#reader-deliverables"},
  "completion_ref": {"answer_ref": "#reader-completion"},
  "budget_ref": {
    "repo": "daowei2026/observe-iterate",
    "commit": "9f52cbc2e51ca709af6f71a70ff53f8f4d6d3d34",
    "path": "runs/BI-01-CO-04/reviews/management-R0002/DECISION.md",
    "selector": "#reader-budget"
  },
  "routes": {
    "same_work": {"recipient_role":"review","recipient_ref":"chatgpt:BI-01-CO-04:workmap-reader-01","instructions_ref":{"answer_ref":"#reader-same-work"}},
    "accept": {"recipient_role":"management","recipient_ref":"chatgpt:BI-01-CO-04:management","instructions_ref":{"repo":"daowei2026/observe-iterate","commit":"9f52cbc2e51ca709af6f71a70ff53f8f4d6d3d34","path":"runs/BI-01-CO-04/reviews/management-R0002/DECISION.md","selector":"#reader-accept"}},
    "decide": {"recipient_role":"management","recipient_ref":"chatgpt:BI-01-CO-04:management","instructions_ref":{"answer_ref":"#reader-decide"}},
    "return_repair": {"recipient_role":"review","recipient_ref":"chatgpt:BI-01-CO-04:workmap-reader-01","instructions_ref":{"answer_ref":"#reader-return-repair"}}
  },
  "triggers": [],
  "explicit_no_trigger_reason_ref": {"answer_ref": "#reader-no-trigger"},
  "parent": {"status":"NOT_APPLICABLE_NEW_CASE","ref":null,"reason_ref":{"answer_ref":"#reader-parent"}},
  "question_definitions": []
}
```
