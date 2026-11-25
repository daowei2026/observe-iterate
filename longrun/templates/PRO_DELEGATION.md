# 具名专业工作委派（V2 D，manager 签发）

- Run / D：run_id / Dxxx；issuer_call_id：
- issuer / recipient / return_to：
- 工作项身份及本次工作范围（阶段、轮次、候选等按实际适用）：
- task_ref：准确 repo@40位commit:path；具体章节/工作范围：
- 其他适用专业来源（Workflow/Skill/任务书按实际采用；可以没有 Skill）：
- business_context_ref：
- input_refs：当前有效任务实例、已存在上游产物、版本及限制：
- expected_outputs：依据任务原件本项应实际产生的成果及完成条件：
- 本 D 合法操作和写面：引用真实 Owner GO grants；不得自行补充权限。
- 同一 D 续接时：原 D、当前实际产物、未完成范围与 continuation_ref：
- 实际回交：原 manager，原工作身份。

本正文只定位已采用任务中的专业工作与输入，不新增专业方法、验收、审批或 Worker 处理规则。机器字段继续使用原 longrun-delegation/v2，无需 skill_ref 或新增 schema。task_ref 不限定文件名。实际工作依据及其他原件通过精确引用传递。
