# BI-01-RESTART-01｜R0001 已收管理结果后的合法恢复（停止时点记录）

本页是**当前已知恢复事实与顺序**，不自动启动手机、Pro、Codex Goal 或后台定时器；准确 live Send、设备所有权和最近 Git HEAD 仍由下次真正恢复时 fresh 对账。Owner 当前先处理白天运行机制／环境问题，准备之后继续同一个新 run，而不是开始又一个 M-START 或重做 I4。

## 已有事实（GitHub 可直接消费）

- 运行 `runs/BI-01-RESTART-01/` 的管理 R0001 已真实发送且 COMMITTED：`provenance/turns/R0001/SEND_RECEIPT.json`；完整手机回复已归档：`FULL_RESPONSE.md`。原提示、两份结构化回交、失败 Gate 分别在同一 R0001 目录。手机原管理聊天已重命名为 `BI01-R01-管理`。
- `FULL_RESPONSE.md` 包含 `#management-decision`、`#workmap`、`#issued-task`、`#worker-authority`、`#budget-and-review`、`#question-work-binding`、`#role-return`、`#question-work-return`。可用于**精确取回原管理业务决定、地图与任务内容**；但 `#question-work-binding` 仅为摘要，不是完整已校验 JSON；不得由 Codex 猜填。
- 原 R0001 Gate `ROLE_RETURN_QUESTION_WORK_REF_MISSING`：`ROLE_RETURN` 缺少指向同条回答中 `QUESTION_WORK_RETURN` 的 `question_work_ref`；双 Return 文件存在，但整个 after-return 仍 FAIL。只允许原管理角色定向有限补交，原业务决定保持。
- R0001 同一回复附件为管理落地 ZIP，手机可见于 `/sdcard/Download/BI01_RESTART_01_M_START_R0001_package.zip`，Pro 宣称的期望 SHA 与实际 Codex 已取得、已验证不同：此前 `pull_phone_file(local_path,phone_path)` 因 Server 与 Codex 处在不同主机、没有经证实的共享目录而失败。不能拿 CYF 本机 `/dwdhome/cyf/...` 路径当本次已共享；ZIP 的未得到部分仍欠原始字节。
- 原管理回交摘要中的 `professional_mode=BI01_EXECUTION_PRO_I4_WITH_TARGETED_I3` 不在当前固定 `COORDINATOR_DISPATCH.json` 允许列表。应由原管理以实际合法 mode `OBSERVATION_I4` 签 I4 主任务、将定向 I3 工作列为完整 `question_ids`/scope，或由有权材料维护者依原管理真实指令补配置；操作端不得自改专业任务。
- 现有 `runtime/config/WORKMAP_BINDING.json` 仍为 `NOT_CONFIGURED`；本 run 尚无已采用 `00_长程推进地图.md`、`01_当前任务.md` 和 `reviews/WORKMAP_INTAKE_CURRENT.json`。所以执行 Pro R0002 尚未派发。
- 独立的旧 I4 试跑不属于此 run，新旧线程/结果/Gate 不可混用。R0001 的 original `invocation_id` / assignment token 与物理 chat 身份须复用作为原调用关联，不复用已提交的消息作为新发送。

## 白天修运行材料／交付／环境，夜间才能真实恢复

1. **先保证可用交付路径**：正常优先按 CYF 已实行的办法查 GitHub exact remote commit；没有时主控从已归档 `FULL_RESPONSE` **只保真抽取明确完整的正文实物**，作为原管理成果机械入库。原文不完整的正式 Binding 和必要附件则由同一管理聊天`DELIVERY_REPAIR` 有界补全，优先要求提供完整可复制文本，不因此重做 M-START。对于真正非文本或太大只在 ZIP 的文件，必须取得本 run 实际 MCP Server 可写并且 Codex 可读取的目录映射或其它已授权正式传输；找不到即具名等待，不允许猜路径/raw HTTP/ADB。
2. **补真实缺项而非重做管理**：从 `GATE_CHECK` 和原 `FULL_RESPONSE` 定位准确问题，沿当前 BOOTSTRAP 的 `DELIVERY_REPAIR`（`original_dispatch_ref`、`issue_ref`、`missing_output_refs`）编译新、一次性的原管理**同一物理聊天**补交。仅补问 `ROLE_RETURN.question_work_ref`、完整可合法采用的 Binding、当前 mode 及因文件物化确实缺少的原稿。原 R0001 prompt 已 COMMITTED，严禁重发。
3. **Stage 1**：将有权管理的完整地图、`01_当前任务`、decision、Binding 和必要出处按确切字节发布；从 R0001 原文发布时记录原文/提取范围，不让操作端改业务判断、补未知数据或代签 Gate。若还缺必要部分就暂时只发布确实已取得的文件。
4. **Stage 2**：使用实际已提交的 Stage 1 内容与现行 `workmap_gate` 计算 Snapshot，取得真正需要的有权 management/reader 接收，发布 Intake，按真实远端回读结果把 WORKMAP_BINDING 从 NOT_CONFIGURED 改为 ADOPTED。不得先改 status，再回填凭证。
5. **实际恢复同一 run**：管理接收和正式专业 Binding 的机器 mode/来源可用后，才为首次专业执行生成新 R 轮（通常 R0002，仍核当前实际编号），按准确接受者派发；正常 RESULT/CHANGE/EFFORT 回管理，地图/任务由管理维护。此后运行中真实错误走 cgpterm 共用恢复，不因一次 GitHub 归档暂时缺失重新发旧消息。

## 运行能力与诚实边界

当前 ChatGPT Pro 不具备直接 GitHub 写入**是本次 R0001 回复和远端记录的事实**，并非以后所有聊天/插件必然如此；下次按现场实际能力选择。CYF 先直写、不能写才补丁 ZIP，其成功依赖此前实际可读的手机文件落地路径；本次不同主机没有同等路径，必须先改机制/环境或避免把正文全部锁进 ZIP。

不用为这次调整再做一套离线验收任务；后续真运行的自然进展是主要观察反馈。以上文件提交不证明修复效果、不解锁 R0002、不授权手机动作或唤醒已停止 Codex Goal。
