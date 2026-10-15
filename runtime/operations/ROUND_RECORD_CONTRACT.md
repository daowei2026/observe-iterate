# BI-01 GitHub 轮次：Pro Rnnnn 与手机 Episode 分开

这是下一次真实运行的记录合同，并非本次已运行的轮次。每个 ChatGPT Pro 管理/执行/审查的**实际调用**记作 R0001、R0002……；失败但已证实零发送副作用可沿原 R 重试，未知发送不重试。每个 R 有独立 invocation_id、assignment_token、round_marker；同一持久 work_id 可跨多 R。手机 Episode、Codex step、Commit 不算 R。旧 I4 第一至四段不能改成新 run 的 R0001—R0004。

路径：`runs/BI-01-RESTART-01/provenance/turns/Rnnnn/`。

| 文件 | 谁写/何时 | 事实边界 |
|---|---|---|
| INVOCATION.json | 主控在实际发送前 | 真实源任务/Binding/role/recipient/policy/轮次/token 和原始 payload hash；准备不等于发送 |
| PROMPT.md | 主控发送前 | **要真正发送的完整 UTF-8 载荷原样**；不能附加未经签发的任务指令 |
| SEND_RECEIPT.json | 发送后主控 | COMMITTED、NOT_SENT、UNKNOWN 等真实状态及消息证据 |
| FULL_RESPONSE.md | 回复完整后由原角色或操作端代存 | 原完整可见答复/有资格的远端完整回交，含实际局限；未知不造 |
| ROLE_RETURN.json | 有效角色回交后 | 对应原 invocation/token/实际职责，不能由操作端猜字段 |
| QUESTION_WORK_RETURN.json | 确实采用 DR14 时 | 真实 work/trigger/focus/remaining；旧调用不用追造 |
| GATE_CHECK.json | 已真实运行检查器后 | 结构检查器输出，不能称业务 Gate 或已实跑业务 |

INVOCATION.json 最小结构：schema=bi01-invocation/v1；run_id=BI-01-RESTART-01；round_id=R0001 等；work_id、invocation_id、assignment_token、round_marker、role（management / professional / review / receiver）、recipient_ref、policy_commit（40位）、prompt_sha256（64位）、binding_ref、current_task_ref、task_adoption_ref 均为 coordinator-dispatch/v3 所需的完整 Git locator 对象（repo/40位commit/path/selector），不是纯字符串路径。首次 M-START 的 binding_ref 和 bootstrap_ref 同指真实 BOOTSTRAP；current_task_ref/task_adoption_ref 可都指向新 Owner 的真实 OWNER_START.md，不预造管理地图。其它轮引用真实已采用来源；不在 metadata 内填伪造的发出时间或 Gate。

**准入条件：**

- 首次管理：必须有 Owner 的后续实际启动消息、真实 BOOTSTRAP/role/recipient、未发送证据和精确载荷；暂不存在管理 map/task 是正常状态，禁止预造。
- 首次专业及新管理签发路线：必须有真实 00 地图、01 当前任务、管理决定/接收证据、实际采用的 WORKMAP_BINDING；缺一不发送。同任务后续 continuation 不必每轮新管理批准，但原完整 scope/方法/触发不可失联。
- 收到 Pro 回交后存完整答复及 Return/实际附件，更新同一 R，而不是用 STATUS 改成已完成。格式缺件找原角色补，主体未完继续原工作；管理的业务决定必须由管理 Pro 真正签发。
- 每次按已有真实发布写权提交 Git、回读远端；通用 GitHub round marker 相关性从实际 scheduler 取，不猜 commit 是哪个手机聊天导致。手机原始控制状态/设备凭据留在 gitignored 本地。
- 管理 Pro 根据实质结果更新地图和任务，主控只录发送/收取/在途、投影 Owner PROGRESS，不把地图做成机器状态表。

机械检查器：`runtime/tools/bi01_run_gate.py` 的 pre-dispatch / after-return；它不发送消息、不批准专业 Gate，也不自动新建/升级 workmap。读到旧 Repo 的 R 文档不等于本次产生真实新轮。
