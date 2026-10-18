# BI-01 V2-02 新轮次与真实成果交付

## 1. 新 run 与 R 身份

- `work_id=BI-01`；`run_id=BI-01-V2-02`。每个真实 Pro 调用单独记录 `BI01-V2-02-Rnnnn-<unique>`，消息首行 `[invocation_id]`；`runs/BI-01-V2-02/provenance/turns/Rnnnn/` 为准确轮次目录。手机 Episode、Worker 操作和 Git commit 不计入 R。
- Owner 将来真正 GO 后才能生成新 `OWNER_START.md`、首次 `M-START BOOTSTRAP` 和真实角色调用。管理实际签新地图/任务/Binding/reader/Intake前，不进行普通专业派发。旧 `BI-01-V2-01` 已暂停，其 Owner GO、R、管理决定、R10 SUBMITTED、首次 R2 reader 授权、Workmap Gate/预算和在途全部**不继承**。
- 每轮在真实提交/远端核验后持久化 `INVOCATION.json`、字节完全相同 `PROMPT.md`、合法收件者和未发送检查，才能实际发；后续保存真实 `SEND_RECEIPT.json`、`FULL_RESPONSE.md`、`ROLE_RETURN.json`、需要的 `QUESTION_WORK_RETURN.json`及准确实物/source_refs，做现有 after-return、管理接收/续作。S1/S2/S3 不是三轮上限，Operator 不代签业务。

## 2. GitHub-first 与 ZIP 备用

Pro 无法实际向 GitHub 提交时，操作端先核 **新分支远端**是否已有相同 invocation/round marker（有 token 时亦核）发布成果；有实际同轮 GitHub commit 则该实物优先，不能重复应用 ZIP。确无远端同轮实物，才按真实 MCP 可写能力创建当轮完整 ZIP。Owner 报告下列双机路径读写已做过基础检查，**不能由此宣称未来每份 ZIP 也已交付**：

- MCP server / Pro 侧可写：`H:\fy\observe-iterate-share`
- 操作 Codex 侧可读：`/dwdhome/fy/observe-iterate-share`

同一 ZIP 实际核身份、路径、长度/SHA、内容包含完整专业成果、回复和两份适用 Return；禁止伪造软件 API、包空结果、凭据、绝对路径、上跳、符号链接、`.git`、超写权文件或其他轮材料。Codex 重新查远端、验证 ZIP 原件、只恢复有权路径、应用相应检查，向新运行分支非 force 提交并 fresh readback，之后按现行 Return/Workmap 继续。**ZIP_STAGED 不是 GitHub 发布，也不是管理接受**。不能建立额外调度器/状态机、因传输失败重做专业分析。

若已有通用手机 ZIP 附件取回合法同轮原件，直接复用，不重复生成。两份**业务固定 ZIP** 另在 `/dwdhome/fy/资金管理`，aidata工作区 `/dwdhome/fy/BASE_E6_2`，与共享交付目录绝不混同。
