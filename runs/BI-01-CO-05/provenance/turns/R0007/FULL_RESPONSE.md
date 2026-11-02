# BI-01-CO-05 R0007 原调用交付关联补齐

- `work_id`: `BI-01`
- `repair_invocation_id`: `BI01-CO-05-R0007-769e316967b3`
- `repair_assignment_token`: `218c7ead1f2c40b681f6d8688482`
- `role`: `management`
- `repair_kind`: `RETURN_ASSOCIATION_ONLY`
- `target_original_invocation_id`: `BI01-CO-05-R0006-81bbad74993d`
- `status`: `SUBMITTED`

<a id="repair-result"></a>
## 补齐结果

本轮只修复 R0006 原 `ROLE_RETURN` 的一处既有交付关联错误：

```text
field:
  handoff.instructions_ref
before:
  github:daowei2026/observe-iterate@15f05a4dac02984592767b403cc3c61cfec83f9d:runs/BI-01-CO-05/provenance/turns/R0006/FULL_RESPONSE.md::#controller-handoff
after:
  github:daowei2026/observe-iterate@15f05a4dac02984592767b403cc3c61cfec83f9d:runs/BI-01-CO-05/provenance/turns/R0006/FULL_RESPONSE.md::#continuation
```

修复依据为：

- R0006 `QUESTION_WORK_RETURN.continuation_ref` 已指向原完整回交的 `#continuation`；
- `RETURN_ASSOCIATION_CHECK.json` 的唯一失败项为 `CONTINUATION_MISMATCH`，其 expected locator 即上述 `#continuation`；
- 原完整回交确实存在该锚点，且它承载同工作续作指令。

修复后的原 `ROLE_RETURN` 作为窄补交发布在：

`runs/BI-01-CO-05/provenance/turns/R0007/ROLE_RETURN.json`

对应的既有 `QUESTION_WORK_RETURN` 未修改内容，按原身份原样随本轮发布在：

`runs/BI-01-CO-05/provenance/turns/R0007/QUESTION_WORK_RETURN.json`

<a id="preserved"></a>
## 保持不变

除 `handoff.instructions_ref` 外，修复后的 `ROLE_RETURN` 保留 R0006 原产物的全部身份和内容，包括：

- `work_id = BI-01`；
- `invocation_id = BI01-CO-05-R0006-81bbad74993d`；
- `assignment_token = 0979ffeb0ae94fec8bda685d20fce36`；
- 原 `question_work_ref`、完成/剩余范围、artifact refs、materials、route key 和 management outputs；
- 原 `work_status = SUBMITTED` 及原未完成业务范围。

本轮未修改或倒签：

- R0006 `FULL_RESPONSE.md`；
- R0006 原 `QUESTION_WORK_RETURN.json`；
- R0006 原 `ROLE_RETURN.json` 历史文件；
- 当前正式任务、Question Work Binding、Workmap Binding、Intake、README、长程地图或 Adoption 状态；
- R0006 的有限技术接收、旧工单停投、Owner 全段时间纠正、触发消费、持续责任或任何业务判断。

<a id="remaining"></a>
## 原未完成范围

R0006 已记录的专业业务未完成范围全部保留。本轮补字段不构成全段脚本/工单形成、Worker 派发或执行、图数取得、合格市场 T、第一层/第二层业务观察、候选或无候选、独立审查、Owner 接受或阶段完成。

<a id="validation"></a>
## 补交自查

- 原调用身份与 token：保持；
- 原 QWR 内容：保持；
- 原 ROLE_RETURN 其他字段：保持；
- 唯一修改字段：`handoff.instructions_ref`；
- 修复后 locator 与 QWR `continuation_ref`：一致；
- 历史原文件：未覆盖；
- 业务分析、资格和范围：未扩张；
- 原未完成项：如实保留。
