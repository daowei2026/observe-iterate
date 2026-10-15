# CYF 长程机制 → BI-01 真实运行接线核对（2026-10-15）

结论：此前成功的是旧业务任务的一次专业续作/原文收取/GitHub 旧工作面归档，不是本仓完整 CYF 式长程运行。Owner 已停止旧试跑并允许未来重跑，因此在本仓准备新 `BI-01-RESTART-01`，**不迁移旧 I4 结果、旧权限状态和旧聊天**。下表是可确认的运行落地缺口及已修/待现场的边界。

| 预期复用的 CYF 机制 | 旧试跑实际缺口 | 本次落地位置 | 哪项仍必须有真实运行证据 |
|---|---|---|---|
| 真实 Pro 轮次 R 与角色 Invocation/Return | 只有“第一/二/三/四段”与手机 episode，缺仓内正式 R | `ROUND_RECORD_CONTRACT.md` + `bi01_run_gate.py` + cgpterm BI-01 Skill 要求逐 Pro 轮保存 | 实际 R0001 发送和完整收取；不能倒填旧四段 |
| 长程 00 业务推进地图、01 当前任务 | 新 observe-iterate/runs 只有 README；旧 PROGRESS 只是投影 | 新 run 唯一目录/两份非活动模板；首次管理必交、由管理 Pro 维护 | 新 M-START 真实业务图和有权任务，不能由主控填 |
| Workmap Binding v2 / management intake | NOT_CONFIGURED、未入真实任务 | `ADOPTION_HANDOFF_CHECKLIST.md`、准确绑定模板、已有 workmap_gate | 管理 Gate/reader 实证、exact A/B 提交和正式 adopted |
| 管理 M-START、M-REASSESS、M-CLOSE | 第四段虽要管理复看，却找不到原管理聊天、无实际管理接收 | 新 run 独立管理聊天/唯一标题与角色身份；写清管理决策与下一交接 | 首次新管理回复及后续实际接收 |
| DR14 两份 Return/稳定触发 EFFORT | 旧 I4 reply 是自由格式，缺新 question-work 双回交，未能证明跨轮管理触发 | 新 run 采用 v2 的真实 BOOTSTRAP/BINDING/Return；主控按`question_work_check.py`核触发、累积与去重 | 真实有效 PRO 回交、已签义务是否实际唤起，非自动语义引擎 |
| 角色/电话投递版本可恢复 | detached HEAD、Skill 找不到、旧工具不暴露、管理聊天重找成本高 | cgpterm Skill 载入 exact 且检查工具可用；通用 Skill 唯一标题/零继承 episode；新 R marker/实际 route | 真机独立聊天身份、发送、收取和恢复 |
| GitHub 与本地运行态对账 | 本地 long-task 状态与 Git 提交分离，新仓无对应 round | 新运行合同明确三个真实状态源；每轮归档后远端读回 | 现场实际长任务和 R/发送证据能对应 |
| 独立专业审查与管理 Gate | 只有管理候选和 I4 结果，专业 Harness PARTIAL | Gate/自检/独立读图/Owner 决定显式分开，缺方法仍报 PARTIAL | 真正独立专业审查前不称 PASS |
| Worker/工程/制图交接 | 旧 Worker 尚未成为新长程标准分路 | 仅由执行 Pro 按 P04 有权 Work Order 激活；未有 READY 不创建 | 实际工单和产物通过专门 Worker 验证 |
| 旧发行副本与生效 source | CYF signed release 仍留在 observe-iterate；部分 DR/Overlay 残留 A/B/C | 当前生效入口明确限制加载；活动 DR00/DR08/Overlay07/08 的确定性残留定点修 | 上线仍需确认实际载荷/上下文未用旧签名 Release |
| 操作主控自动引擎 | prepare/snapshot/check 只计算不写状态，不会主动 choose/send/recover | 新运行合同 + 机械 gate + cgpterm controller 将动作逐一接起来 | 只可称主控**按协议调度**；不能称已实现程序级 receive/decide/apply |

通用 CYF 运行 Skills 已包含手机 episode 隔离、唯一新标题、发送去重、等待/恢复和本地长任务状态，**不应重复实现这些状态机**。旧 I4 试跑停止不意味着通用技能要丢失。真正剩余的是未来真实运行中的现场落地、专业 Router/审查方法完备性与自动处理器尚未实现，不得虚报本轮已解决。
