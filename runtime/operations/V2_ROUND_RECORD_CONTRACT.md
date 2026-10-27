# BI-01 GitHub Pro 轮次与真实发送记录

文件路径保留 V2 名称只为既有引用兼容；正文不再选择某个历史 run 或专业方法。手机发送/回复/Return/调度义务不因专业方法替换而放松。真实 Pro 调用逐一记录 R0001/R0002……，手机 Episode、Worker 操作和 Git commit 不算 R。

- `work_id=BI-01` 是稳定路由键。
- `run_id` 取本次真实授权的新运行或原有权续作，不设历史默认值。
- 轮次目录为 `runs/<本次run_id>/provenance/turns/Rnnnn/`。
- invocation 前缀按该 run 的实际约定生成；既有 BI-01 工具将 run_id 开头的 `BI-01-` 映射为 `BI01-`，再接 `-Rnnnn-<唯一ID>`。
- scheduler round_marker 严格为 `[` + invocation_id + `]`，亦为真实要发送 UTF-8 载荷第一行。
- 专业 mode、question_ids 与业务内容由本次实际配置/Binding 确定，本合同不预置 S1/S2/S3 或四项专业工作。管理模式沿 M-START/M-REASSESS/M-CLOSE。

每轮依原流程写 INVOCATION.json、精确 PROMPT.md、真实 SEND_RECEIPT.json、完整 FULL_RESPONSE.md、有效 ROLE_RETURN.json 和实际要求的 QUESTION_WORK_RETURN.json 与检查结果；发送前 commit+remote readback+pre-dispatch+NOT_SENT，收到后按真实完整回答与角色 Return 核验证据。首次 BOOTSTRAP 的 binding/current task 可引用实际新 Owner 启动；后续用本次管理签发的 map/task/Binding/intake，不借另一 run。

新 run 若确需首次地图 Reader，必须由本次管理重新签发具名授权和相应前置采用规则，核完整任务、Binding、管理依据、输入及方法；不能从历史 Reader 特例取得权限。Reader 属于真实 Pro 新 R，保存原样载荷、NOT_SENT 和实际回交，不预填 PASS。

历史 R、token、Owner 决定、Gate 和业务结论不翻译成新运行事实。专业文件不负责发送，机械操作端不自行签业务结果。

## GitHub 回交失败时：共享 ZIP 备用交付

本轮有真实授权的 Pro 优先按 GitHub 原有流程提交。若无法实际提交，不丢失已有成果，也不把“已生成 ZIP”当成“已提交 GitHub”。

### 共享目录（按角色选路径）

| 使用者 | 实际路径 | 用途 |
| --- | --- | --- |
| MCP server / Pro 侧可写 | `H:\fy\observe-iterate-share` | 存放当轮 Pro 产生的 ZIP |
| 操作 Codex 侧可读 | `/dwdhome/fy/observe-iterate-share` | 读取同一 ZIP，核对后合法发布 |

以上为 Owner 提供的路径映射，适用时沿用。Owner 已报告基础读写和互见通过，不因换方法重复同一预检；这不是本轮 ZIP 已产生的证据。每轮仍确认真实文件、大小/字节/SHA-256、一致的 invocation/成员/来源和发布结果。共享路径不是业务数据入口，也不是 aidata 工作区 `/dwdhome/fy/BASE_E6_2`。

### 正常判断和交接顺序

1. **先核是否真未提交**：Pro 报告不可写时，操作 Codex 核本次有权目标分支的派发前 base 和当前远端；已有匹配 invocation/round_marker 及实际 token 的提交时，fresh 回读实物，以 GitHub 为准，不再应用同轮 ZIP。手机说法作为矛盾证据保留。
2. **有真实 ZIP 才接收**：确无对应提交时，Pro 可按实际 MCP 文件能力，在共享目录下按本次 run/invocation 分开存放唯一 ZIP，提供真实路径、名称、打包范围、工作身份及能取得的 bytes/hash。不规定不存在的 MCP API，不伪造写入成功。
3. **交付内容**：保留原本要提交的全部真实成果及仓库相对路径，包括完整回答、有效 Return、专业/管理正文及实际要求的实物；不能用摘要、空 ZIP、假数据或另一轮材料替代。按原写权打包，不含凭据、设备私密状态、整个工作区或无关附件。
4. **实际取包与发布**：操作端定位同一 ZIP，记录 bytes/SHA-256 和 invocation；检查成员路径、..、绝对路径、符号链接、嵌入 .git、凭据及越权范围，禁止直接覆盖。再次核远端同轮状态后，只在本次合法分支恢复实际文件，校验完整 Return/成果、做适用检查，非 force 提交并 fresh readback。
5. **回到原机制**：发布后以真实 exact commit/blob、轮次和证据继续既有 Return、管理接收及接续。共享文件不改变发消息/去重/授权流程；未发布时只能说明 ZIP_STAGED / PENDING_GITHUB_PUBLICATION，不伪造机器状态或 Gate。
6. **无法转运**：实际不能生成、写、读、互见或发布时，记录真实错误、受阻位置和恢复条件，不把运输失败当作业务没做，不重做已完成的分析。

通用手机附件回收链已取得同轮真实 ZIP 时复用，不重复收两份；共享路径只是备用承运位置，不绕过既有 github_or_zip_1h 核实顺序。
