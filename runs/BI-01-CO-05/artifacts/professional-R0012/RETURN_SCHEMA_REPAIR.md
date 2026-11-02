# BI-01-CO-05 R0012：R0011 ROLE_RETURN schema 精确补交

- `work_id`: `BI-01`
- `repair_invocation_id`: `BI01-CO-05-R0012-ae98959b9146`
- `repair_assignment_token`: `88bf3c93f32347b6ac848e36cafc`
- `repair_route`: `return_repair`
- `counts_as_effective_professional_call`: `false`
- `target_invocation_id`: `BI01-CO-05-R0011-e186238bf811`
- `target_assignment_token`: `ade5d48ee39949aa99991f4b0a39`
- `target_role`: `professional`
- `repair_status`: `COMPLETE`

## 1. 本轮唯一范围

本轮只修复 R0011 `ROLE_RETURN.json` 的 schema 附加属性错误，不重做业务分析，不扩大输入或结果资格，不重签/改写 Worker 工单，不重放 Management 或 Worker 路线，也不倒签 R0011 历史文件。

依据：

- 原调用：`daowei2026/observe-iterate@43a1ce02ca5e7c17ddcb27e43df97a766f90bbb9:runs/BI-01-CO-05/provenance/turns/R0011/PROMPT.md::full`
- 缺件检查：`daowei2026/observe-iterate@51d727705eb65e3885a6792494bc617ca7da6d4a:runs/BI-01-CO-05/provenance/turns/R0011/RETURN_SCHEMA_CHECK.json::full`
- 补交路线：`daowei2026/observe-iterate@a6a8acf7fa65665218d0f2163598d434fb921b24:runs/BI-01-CO-05/01_当前任务.md::#task-route-return-repair`
- 原 ROLE_RETURN：`daowei2026/observe-iterate@da52023ad7f2512687c36f0c602286b681c01505:runs/BI-01-CO-05/provenance/turns/R0011/ROLE_RETURN.json::full`
- 原 QUESTION_WORK_RETURN：`daowei2026/observe-iterate@00f204b40d9d0477412389eb7ba847fbd8b74ce2:runs/BI-01-CO-05/provenance/turns/R0011/QUESTION_WORK_RETURN.json::full`

运行记录：观察时间 `2026-11-02T19:16:07.944098+00:00`；有效回交数 `5`。

## 2. 精确修复

失败位置：

```text
/role_outputs/professional
```

从原 R0011 ROLE_RETURN 删除且只删除：

```json
"worker_order_ref"
"worker_order_state"
```

修复后 `role_outputs.professional` 仅保留当前 schema 允许的三个字段：

```json
{
  "mode": "CASE_OBSERVATION",
  "result_ref": "...#decision-summary",
  "continuation_ref": "...#continuation"
}
```

## 3. 保留不变

以下内容全部按原 R0011 回交保留：

- `schema`、`work_id`、原 `invocation_id`、原 `assignment_token`；
- `question_work_ref`、`work_status`、完成范围和未完范围；
- 全部 `artifact_refs`，其中仍明确包含 `WORKER_ORDER.md`；
- `delivery`、`materials`、`unavailable_required`；
- `handoff.kind`、`route_key`、`instructions_ref`；
- `role_outputs.professional.mode/result_ref/continuation_ref`；
- R0011 报告、工单、签发回执、证据索引、manifest、FULL_RESPONSE 和 QUESTION_WORK_RETURN；
- R0011 的所有业务未完、Worker preflight/派发/回交未完和后继关系。

因此删除两个不受 schema 支持的便利字段，不会删除工单实物，也不会改变其原签发状态；该状态仍由 R0011 正式报告、工单和签发回执承载。

## 4. 对应产物与校验

- R0012 `QUESTION_WORK_RETURN.json`：原 R0011 QUESTION_WORK_RETURN 原样复用，Git blob `eaf7b595c36de8ac139df492aabb87dabfcc3aec`。
- R0012 `ROLE_RETURN.json`：原 R0011 ROLE_RETURN 仅删除上述两个字段。
- 原 R0011 ROLE_RETURN 历史 blob `2399c8d64a4f84b5d462f75b8331a9e77098ebef` 保留未覆盖。

静态复核结果：

```yaml
json_structure: valid
schema_pointer: /role_outputs/professional
actual_keys: [mode, result_ref, continuation_ref]
allowed_keys: [mode, result_ref, continuation_ref]
unexpected_fields: []
question_work_association: unchanged
business_substance_changed: false
```

## 5. 范围边界

本轮没有：

- 形成新的有效 Professional 调用；
- 重新分析市场、图数、脚本、输入或 Owner 过程；
- 新签、修改、校验或派发 Worker 工单；
- 消费 R0011 后续产生的 Worker 技术结果；
- 把原分析未完包装成完成；
- 修改原 R0011 路径上的历史文件。

## 6. 结果

`FAIL_ADDITIONAL_PROPERTIES` 所列两个不支持字段已精确移除。R0011 的实质成果、身份、工单实物、未完范围与接续关系继续有效；后续仍按原 R0011 `same_work_after_worker_result_returns_to_issuer` 关系处理，不因本次 Return 修复发生业务、资格、状态或方法升级。
