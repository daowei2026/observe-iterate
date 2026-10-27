# W02 原签发工单的规范定位补登记（R0007）

order_id: BI01-CO-01-W02-FULL-HISTORY-1D
work_order_id: BI01-CO-01-W02-FULL-HISTORY-1D
parent_task_id: BI01-CO-01-CASE-RESEARCH-01
work_id: BI-01
run_id: BI-01-CO-01
issuer_role: professional
issuer_ref: chatgpt:BI-01-CO-01:professional
issuer_invocation_id: BI01-CO-01-R0006-f352c5b081
issuer_assignment_token: a21908ab367a401eb0f50d0c5a94f0a0
return_to: chatgpt:BI-01-CO-01:professional

registration_invocation_id: BI01-CO-01-R0007-07762a4ea7
registration_assignment_token: df887e83eb05fe25f83750f0ff0e837c
registered_by: chatgpt:BI-01-CO-01:professional
registered_at_utc: 2026-10-27T21:48:31.411878Z
record_kind: CURRENT_METADATA_SUPPLEMENT_TO_EXISTING_ORDER

## 原单、权限和本次登记分别定位

本文件由原签发专业者在 **R0007 当前补件**中新增，是同一 W02 的机械定位记录，**不是新工单、重新派发或补造历史签发**。上述 `issuer_*` 指向 R0006 已真实发生的签发身份；`registration_*` 才是本次新增文件的身份。目录名 professional-R0006 只与原签发轮对应，不表示此路径在 R0006 时已经存在。实际新增历史以本文件 Git 提交为准。

原 W02 全文及授权范围仍是唯一任务正文，未修改、缩写或替换：

`daowei2026/observe-iterate@c5955c2e562ca0f318cf08278b81ff56d6479d4e:runs/BI-01-CO-01/artifacts/batch-01/aidata/W02_WORK_ORDER.md::full`

原调用身份及已承诺发送的核对来源分别为：

`daowei2026/observe-iterate@370693e25f18348fa48c85fbb85d8a928b6eb978:runs/BI-01-CO-01/provenance/turns/R0006/INVOCATION.json::full`

`daowei2026/observe-iterate@370693e25f18348fa48c85fbb85d8a928b6eb978:runs/BI-01-CO-01/provenance/turns/R0006/SEND_RECEIPT.json::full`

原 R0006 完整回交为 `703f9fc1213002619aa651ee1fbbeed7f84f819d:runs/BI-01-CO-01/provenance/turns/R0006/ROLE_RETURN.json::full`。本次补登记依据为 `b93febc60cd30aed51436e22f5b8ae4e02748941:runs/BI-01-CO-01/provenance/turns/R0007/FULL_ASSIGNMENT.md::full` 和 `cf024eca9cda73c07c422f886d6fd40bf1e66b72:runs/BI-01-CO-01/provenance/turns/R0007/DELIVERY_ISSUE.md::full`。

## 仅修机械对应，不再执行取数

原 `work_order_id` 与本记录 `order_id` 是同一 ID；原 `issued_by` 的角色和收件人分别在此明确为 `issuer_role`、`issuer_ref`。没有改变对象、日期、方法、工具写权、Worker 身份或返回责任人。

原 Worker 实质报告保留于：

`daowei2026/observe-iterate@3a761c4ebf4a203ec39cabbd1e9d25413b204f5a:runs/BI-01-CO-01/artifacts/worker-BI01-CO-01-W02-FULL-HISTORY-1D/FULL_RESPONSE.md::full`

其当前同路径仅另附具名 R0007 专业者的 `order_id` 对应说明，不把该附注算作 Worker 新执行或新回交。原报告、VALIDATION、INPUT_AND_CALLS、三份完整 CSV、manifest、调用及页面证据继续有效；未知和缺行情仍按原件保留。

Worker 已完成 W02；**不得因为新增这个规范路径而再次派发 W02、唤醒 Worker 或重跑 aidata**。机械复核仅把已有技术结果送回本原签发 Pro 消费，不更新 Intake，不签管理接受，不关闭父任务。通过后沿原 CASE_OBSERVATION 同工作继续全部 3–5 例、回看、方式二和统一交付；本登记不新增任何业务或工程权限。
