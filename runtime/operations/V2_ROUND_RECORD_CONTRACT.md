# BI-01 V2 GitHub Pro 轮次与真实发送记录

本文件只改变旧 Rnnnn 记录合同中的 **run 作用域和 V2 专业标识**；原来的手机发送/回复/Return/调度器义务不因改版而放松。真实 Pro 调用逐一记录 R0001/R0002……，手机 Episode、Worker 操作和 Git commit 不算 R。

- `work_id=BI-01`
- `run_id=BI-01-V2-01`
- 轮次目录：`runs/BI-01-V2-01/provenance/turns/Rnnnn/`
- 唯一 invocation 前缀：`BI01-V2-01-Rnnnn-<independent-unique-id>`
- scheduler `round_marker`：严格为 `[` + invocation_id + `]`，亦为真实要发送 UTF-8 载荷第一行。
- 当前专业工作标识：`S1`（对象）、`S2`（图和数据）、`S3`（观察想法）；调度 mode 分别由当前正式 dispatch 配置确定。管理模式保留 M-START/M-REASSESS/M-CLOSE。

每轮依原流程写 `INVOCATION.json`、精确 `PROMPT.md`、真实 `SEND_RECEIPT.json`、完整 `FULL_RESPONSE.md`、有效 `ROLE_RETURN.json` 和必要的 `QUESTION_WORK_RETURN.json` 与 Gate 检查；发送前 commit+remote readback+pre-dispatch+NOT_SENT，收到后按真实完整回答与角色 Return 核验证据。首次 BOOTSTRAP 的 binding/current task 可引用实际新 Owner 启动，不可引用旧 run；后续必须用新管理签发的 map/task/Binding/intake。

首次采用的具名地图 reader 是 Intake 阅读证据的生产者，其采用前派发按 [R0002 已签用途修正](../../runs/BI-01-V2-01/reviews/management-R0002/DECISION.md#reader-pre-adoption)核当前完整受托任务、Binding、管理依据和冻结输入，不先要求尚待该读者产出的 Intake／ADOPTED。它仍是独立真实 Pro 新 R，照常保存原样载荷、NOT_SENT 与实际回交；不预填 PASS，不把整个 review 角色免检。普通专业任务仍在真实采用后派发。

不可把历史 V1 的 R、token、Owner 决定、G1–G6 或 I4/I5/I6 回交翻译为 V2 的当前任务事实。专业文件不负责发送，机械操作端不自行签业务结果。


## GitHub 回交失败时：共享 ZIP 备用交付

本轮有真实授权的 Pro **优先按 GitHub 原有流程提交**。当其 GitHub 写入不可用时，不因不能提交就丢失已有专业成果，也不把“已生成 ZIP”当成“已提交 GitHub”。

### 共享目录（按角色选路径）

| 使用者 | 实际路径 | 用途 |
| --- | --- | --- |
| MCP server / Pro 侧可写 | `H:\fy\observe-iterate-share` | 存放当轮 Pro 产生的 ZIP 交付 |
| 操作 Codex 侧可读 | `/dwdhome/fy/observe-iterate-share` | 读取同一 ZIP，核对后代为合法发布 |

以上是 Owner 提供的**路径映射**，尚非本版已验证的两机器互通记录。首次真实使用时确认目录存在、MCP 写入权限、Codex 读取权限、文件字节和 SHA-256 一致。它们不是固定数据 ZIP 的所在位置，也不是 aidata 执行工作区 `/dwdhome/fy/BASE_E6_2`。

### 正常判断和交接顺序

1. **先核是否真未提交**：Pro 报告 GitHub 不可写时，操作 Codex 检查本轮派发前的目标仓库/分支 base 和当前远端；若已有匹配 `invocation_id/round_marker`（及实际有记录时的 assignment token）的提交，回读相关文件，以 GitHub 实物为准，**不要再应用同轮 ZIP**。
2. **有真实 ZIP 才接收**：若确无对应 GitHub 提交，Pro 可按 MCP server 当前可用写文件能力，在 `H:\fy\observe-iterate-share` 下按 `BI-01-V2-01`、当轮 invocation 分开存放唯一名称 ZIP；提供确切完整路径、文件名、实际打包范围、工作身份/轮次、能取得时的大小和 SHA-256。不规定一个不存在的专用 MCP API，也不假称共享目录自动创建或已写入成功。
3. **交付内容**：尽可能保留原本要提交到 `observe-iterate` 的**全部真实成果**及仓库相对路径，包括完整可见回答、`ROLE_RETURN`、实际要求的 `QUESTION_WORK_RETURN`、相关专业 artifact/管理正文或 Worker 实物；不可用摘要、伪造数据、空 ZIP 或另一轮材料代替。与原指令中的写权和允许路径一一对应，不打包凭据、私有设备状态、整个工作区或无关附件。
4. **操作 Codex 实际取包**：从 `/dwdhome/fy/observe-iterate-share` 定位相同 ZIP，记录真实 bytes/SHA-256 和关联 invocation；先检查 ZIP 成员路径、`..`/绝对路径/符号链接/嵌入 `.git`/凭据/超出授权范围等，禁止不经检查直接覆盖工作树。与 GitHub 远端同轮状态再对账后，才在合法 V2 工作分支恢复仓库相对路径、校验完整 Return/实际成果，做适用测试与审阅，**非 force 提交并远端回读**。
5. **回到原机制**：发布后引用新的 exact commit/blob、轮次和完成证据，继续原 `ROLE_RETURN/QUESTION_WORK_RETURN` 校验、管理接收与接续。共享文件并不改变原来的发消息/去重/授权/管理流程；未实际提交时标记为 `ZIP_STAGED / PENDING_GITHUB_PUBLICATION` 等**说明性文字**，不伪造既有机器状态或 Gate。
6. **无法转运时**：若 Pro 无法生成 ZIP、MCP server 无法写、共享路径不能互见、Codex 无法读取或发布，则记下受阻位置、真实错误和恢复条件，不让 ZIP 看起来像已完成 GitHub 交付，不因传输失败重做已完成的业务分析。

若通用手机附件的 ZIP 回收链已经成功提供同轮实物，可继续按照现成通用 Skill 运送与核验，不重复回收两份同轮成果；本共享路径只是一种明确的备用承运位置，不能绕过已存在的 `github_or_zip_1h` 核实顺序。
