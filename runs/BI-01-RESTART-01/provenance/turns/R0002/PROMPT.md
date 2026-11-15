[BI01-RESTART-01-R0002-c19efdc130c1995d4660ca4907747429]
work_id: BI-01
invocation_id: BI01-RESTART-01-R0002-c19efdc130c1995d4660ca4907747429
assignment_token: dc5df7008bbcb41665e37aea084c100e
role: management
recipient: chatgpt-project:细节叙事生成_金标/chat:BI01-R01-管理
dispatch_authority: OWNER_AUTHORIZED_MANUAL_REPAIR
overlay12_status: NOT_RUN_NOT_PASS

你是本次 BI-01-RESTART-01 的原管理 Pro。本消息只在同一个原物理管理会话 `BI01-R01-管理` 中修复你在 R0001 已形成管理交付的确切机器接线缺项；它是新的 R0002 管理修复 invocation，不是重新执行 M-START，不是专业任务轮次，也不授权新的业务范围。

## Owner 一次性授权与冻结边界

Owner 已明确批准一次性 `OWNER_AUTHORIZED_MANUAL_REPAIR`，仅解决当前锁定机制不能为 BOOTSTRAP-origin 管理补交准备消息的问题。通用 Overlay12/runtime 没有因此修改或通过；本次消息也没有 Overlay12 prepare/verify PASS。

准确授权原文：

`daowei2026/observe-iterate@b6b837e4f8368f07afb4f1eaf6f6648080a6933e:runs/BI-01-RESTART-01/OWNER_AUTHORIZED_MANUAL_REPAIR_R0002.md::full`

准确缺项清单：

`daowei2026/observe-iterate@46119a8e0030b4c3597634735cbe5d22ad3a0ac7:runs/BI-01-RESTART-01/reviews/MANAGEMENT_DELIVERY_REPAIR_REQUIRED_R0001.md::full`

原始 R0001 回答、Return、提示、receipt 和管理包原件均保留在：

`daowei2026/observe-iterate@46119a8e0030b4c3597634735cbe5d22ad3a0ac7:runs/BI-01-RESTART-01/provenance/turns/R0001/::tree`

禁止覆盖、伪造或改写这些历史记录；禁止重发或重做 R0001；禁止把修复轮说成专业工作或 Gate PASS。

## 本轮唯一任务

检查 R0001 已交付内容，并只决定、交付以下修正：

1. 为当前任务补充合法、明确且可由 `workmap_gate.py` 识别的 `task_id:` 行。该值必须由你作为原管理角色选择；操作 Codex 不代填。
2. 为 R0001 `ROLE_RETURN` 提供保留原始历史的修正版或补充件，其中含可追溯、可解析到 R0001 `QUESTION_WORK_RETURN` 的非空 `question_work_ref`，并明确原件、修复件及采用关系。
3. 从当前锁定配置 `runtime/config/COORDINATOR_DISPATCH.json` 已允许的 mode 中选择一个与你已签发的真实 I4（含定向 I3 核查）授权相符的合法 `professional_mode`；不得要求操作 Codex代选或新增通用 mode。
4. 修正 Question Work Binding 的引用承载方式：所有 `answer_ref` 必须有能够被现行解析器定位和校验的实际 carrier，或改为准确 Git locator；不得继续让 detached JSON 中的 `answer_ref` 指向该 JSON 内不存在的锚点。请明确 Binding 的规范载体与 exact selector。
5. 把所有回到管理角色的 route 修正为实际存在的同一物理管理会话 `BI01-R01-管理`，不再指向 `chat:new:*`。专业执行 route 是否仍指向未来新的专业聊天，应按原管理授权保持或由你明确说明，不得借修复扩大范围。
6. 如果这些修复使管理地图、当前任务、Binding、Workmap Binding Candidate 或相关签发物必须同步更新，请只给出必要修正版，并明确每份修正版与 R0001 原件的关系；不重做既有业务判断。

## 必须交付的可落库证据

请在完整回复中：

- 逐项说明以上六项的决定、修复结果和仍未满足项；
- 明确 `R0001` 原始历史继续保留，本轮修复件如何被后续 intake／dispatch 使用；
- 给出修正版当前任务、Question Work Binding、R0001 ROLE_RETURN 修复件及任何必要同步文件的完整内容；
- 生成一个可下载的最新完整修复 ZIP，包含 `MANIFEST.json`、说明文件、所有修正版文件及各项 SHA-256；建议文件名 `BI01_RESTART_01_R0002_MANUAL_REPAIR_package.zip`；
- 不声称 GitHub 已写入，除非你确有可核验写入证据；操作 Codex 将负责下载、验哈、落库、提交和远端读回；
- 不派发专业任务，不生成专业分析，不签 G4，不宣布 Workmap 已 `ADOPTED`。

本轮完整回答末尾还必须提供：

1. 本轮 R0002 自身的一个 `ROLE_RETURN`，身份严格使用本消息的 work/invocation/token，并以非空 `question_work_ref` 指向同一回答中的 R0002 `QUESTION_WORK_RETURN`；
2. 本轮 R0002 自身的一个 `QUESTION_WORK_RETURN`，`binding_ref` 严格保持原 R0001 BOOTSTRAP locator：
   `daowei2026/observe-iterate@003d6700e20c7feed7a9d30147e673f39380d082:runs/BI-01-RESTART-01/BOOTSTRAP.json::full`；其结果只陈述“原 M-START 交付修复”，不得声称重新执行 M-START；
3. 单独的 R0001 `ROLE_RETURN` 修复件，保留 R0001 原 invocation/token/work 身份，并说明其不会覆盖 Git 历史中的原始文件。

如果你无法在该窄范围内形成一致修复，返回 `BLOCKED`、逐项剩余缺口和准确所需输入；不要用猜测值让 Gate 表面通过。
