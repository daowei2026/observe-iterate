# R0001 管理交付定向修复要求

## 处置

保留 R0001 已完成的管理业务判断、地图、当前任务正文、证据边界与专业后继意图；不重做 M-START，不重发 R0001，不继承旧 I4 结果。当前只允许原管理角色对下列确切交付／机器接线缺项作窄修复。

## 已通过

- R0001 手机发送仅一次且为 `COMMITTED`。
- 完整回答已关联保存，SHA-256 为 `1e3f425d2da67a3f597fe6f913c9d303fda3f3d0b988fecd53307aef545b37e2`。
- 管理 ZIP 大小 `20156` 字节，SHA-256 为 `3c5a921c3ff321be804e1a027894bb1c4fc8679ce8527f490ad0c441c1fd6f54`；MANIFEST 八项全部一致。
- 地图、任务、管理决定、Question Work Binding Candidate 已在 `e1838ebb2753a7f2e5b1efa94e9a7b62c754561a` 发布并完成远端读回。
- Workmap snapshot 为 `5ac344eaa7dc4e6a68455d5aed2de4cc0b893e5df6366ab848a34f4c7399e348`；独立 reader 对应输入为 `34a8fb16006c812818a4e098dbac4c9cbbdd9412b70ca2f9521dcd6c17f7bab2`，判定 `READABLE_WITH_BLOCKERS`。

## 必须由原管理角色修复

1. R0001 `ROLE_RETURN` 缺少 `question_work_ref`；`bi01_run_gate.py after-return` 的准确错误为 `ROLE_RETURN_QUESTION_WORK_REF_MISSING`。
2. `01_当前任务.md` 缺少合同要求的准确 `task_id:` 行，因而不能与 Workmap intake 的 `dispatch.task_id` 机械绑定。
3. `QUESTION_WORK_BINDING_I4.json` 的 `professional_mode` 为 `BI01_EXECUTION_PRO_I4_WITH_TARGETED_I3`，但锁定的 `COORDINATOR_DISPATCH.json` 没有该 mode；准备消息准确失败为 `BINDING_STAGE_OR_MODE_MISMATCH`。需由管理在已发布 mode 中选择与其真实授权一致的一项，不由操作端代选。
4. Binding 中的 `answer_ref` 会以 Binding 自身文件为 carrier 解析；该文件没有 `#route-same-work` 等锚点，准确失败为 `ANCHOR_MISSING_OR_DUPLICATE:#route-same-work`。需要交付可被现行 Overlay12 解析的有权 Binding／carrier 或准确 Git locators，不能由操作端改写业务签发物。
5. Binding 的管理路线仍指向 `chat:new:BI01-RESTART-01-M-START`，而 R0001 的真实管理聊天已重命名并唯一核验为 `BI01-R01-管理`。修复必须保留同一原管理角色和实际聊天，不得把补交误派到新的管理聊天。
6. 新接收者视角的 README 与地图下一步仍有 M-START 前状态残留；管理需明确哪些管理面正文需要更新，操作端只维护 Owner 事实投影。

## 当前机制边界

- 锁定版本用原 BOOTSTRAP 准备 `DELIVERY_REPAIR` 会准确拒绝为 `BOOTSTRAP_MANAGEMENT_ROUTE_REQUIRED`。
- 用当前签发 Binding 准备普通管理路线会先因未配置 mode 拒绝；即使只检查 route carrier，仍因锚点不在 Binding 文件中拒绝。
- 因而当前没有通过现行 Overlay12 prepare/verify 的管理补交载荷；在有权修复入口形成前，不得手写短消息、不提升 Workmap 为 `ADOPTED`、不创建或发送专业 R0002。

## 准确恢复条件

原管理角色以同一 R0001 实质为基础补交：有效 `ROLE_RETURN`、带准确 `task_id:` 的当前任务、可由锁定配置和 carrier 解析的 BINDING，并确认管理路线仍回到真实 `BI01-R01-管理`。其后重新物化、提交、远端读回、snapshot/intake/check/dispatch；只在所有发送 Gate 通过且现场仍为未发送时，才生成首个专业轮次。
