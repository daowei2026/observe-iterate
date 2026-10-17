# BI-01 V2 GitHub Pro 轮次与真实发送记录

本文件只改变旧 Rnnnn 记录合同中的 **run 作用域和 V2 专业标识**；原来的手机发送/回复/Return/调度器义务不因改版而放松。真实 Pro 调用逐一记录 R0001/R0002……，手机 Episode、Worker 操作和 Git commit 不算 R。

- `work_id=BI-01`
- `run_id=BI-01-V2-01`
- 轮次目录：`runs/BI-01-V2-01/provenance/turns/Rnnnn/`
- 唯一 invocation 前缀：`BI01-V2-01-Rnnnn-<independent-unique-id>`
- scheduler `round_marker`：严格为 `[` + invocation_id + `]`，亦为真实要发送 UTF-8 载荷第一行。
- 当前专业工作标识：`S1`（对象）、`S2`（图和数据）、`S3`（观察想法）；调度 mode 分别由当前正式 dispatch 配置确定。管理模式保留 M-START/M-REASSESS/M-CLOSE。

每轮依原流程写 `INVOCATION.json`、精确 `PROMPT.md`、真实 `SEND_RECEIPT.json`、完整 `FULL_RESPONSE.md`、有效 `ROLE_RETURN.json` 和必要的 `QUESTION_WORK_RETURN.json` 与 Gate 检查；发送前 commit+remote readback+pre-dispatch+NOT_SENT，收到后按真实完整回答与角色 Return 核验证据。首次 BOOTSTRAP 的 binding/current task 可引用实际新 Owner 启动，不可引用旧 run；后续必须用新管理签发的 map/task/Binding/intake。

不可把历史 V1 的 R、token、Owner 决定、G1–G6 或 I4/I5/I6 回交翻译为 V2 的当前任务事实。专业文件不负责发送，机械操作端不自行签业务结果。
