# 第二阶段专业适配状态（进行中）

本分支以CYF完整保真复制 `4760638c2ebaa18c4501925499cc4fce95994b73` 为可追溯原始基线，未直接修改或删除该历史快照。当前为迁移工作分支候选，**禁止作为可运行BI-01正式Release**；不得发送手机消息、启动专业Agent或假称Gate已通过。

## 本批已改

- DR00：角色入口和专业方法选择改成BI-01的P00–P07，保留协调者／管理／承办者通用职责。
- DR06：保留完整目标管理、剩余工作、优先级、管理纠偏、预算和后继，改专业合同来源。
- DR12：CYF A/B/C专业题及S01–S25源替换为BI-01既有I1–I6与P00–P07准确来源；未形成的专业Router/独立审查标记缺失。
- DR13：保留管理题M-START/M-REASSESS/M-CLOSE及§6上下文、§8–10触发与处理；CYF A/B/C专属工作组合替换为BI-01 I1–I6、Worker与审查来源。
- DR14：保留BOOTSTRAP、BINDING、RETURN、routes、triggers、持续复看和主控顺序；替换固定Feature地图及C_WORK专属要求。
- Overlay13：保留原有角色回交、去重、权限和持续责任；将A/B/C具体交付义务改为BI-01专业来源引用。

## 连接中断后已恢复的第二批（2026-10-15）

- Overlay08：消息固定正文改为BI-01已存在的专业引用和BI01角色标记；原通用运输、Owner目标、工作身份、准确来源、回交和材料使用规则保留。对CYF专属正文的删除不等于BI-01专业能力已齐。
- `runtime/overlay/tools/management_prompt.py`：策略文件位置改为本仓实际路径；通用stage不再只允许A/B/C；同工作继续和新有权任务不再依赖CURRENT_C_WORK特殊标记；机械验签、指令来源和recipient核验保持。
- Overlay12：原有`workmap`、`prepare/verify`、去重及路由说明保留；命令入口改成`O=runtime/overlay`、`CONFIG=runtime/config/COORDINATOR_DISPATCH.json`；旧U2/U3配置和状态不作为BI-01授权。
- 固定Dispatch配置：将旧候选占位结构与现有脚本合同`coordinator-dispatch/v3`对齐，提供`BI-01`技术工作标识和`BI01`模板stage及候选mode；目标/数据来源来自`professional/`，但没有实际BOOTSTRAP/BINDING、接收者和合法任务前不得发送。采用边界见`runtime/config/ADOPTION_STATUS.md`。
- 第二批文件只在本PR工作分支提交，不动`main`和第一阶段保真提交；不做手机/Pro/业务试跑。

## 本次中断恢复与静态检查（2026-10-15）

- 恢复前最后有效提交：`d593d0a93b74c68be957699bb3a7c956728d860f`，不重复修改其中6份已完成DR/Overlay规则。
- 第二批恢复提交：`417141e3b9578761fc383e9503d6121a49147dbb`。文件范围仅Overlay08、Overlay12、`management_prompt.py`、Dispatch候选配置、采用状态与本页说明。
- 一次性静态检查：[Actions run 38736886419](https://github.com/daowei2026/observe-iterate/actions/runs/38736886419)；Python `ast.parse`、JSON配置结构、阶段/role模板标记、已有链接、工具与命令路径、`DO_NOT_DISPATCH`均PASS。
- 本轮没有调用`prepare_dispatch`派发业务任务，没有调用手机/模型，也没有运行依赖CYF A/B/C情形的旧端到端测试。一次性静态验证工作流完成后从分支删除，不作为常驻运行服务。
- 远端Git没有其他并发提交，且本分支Actions均已完成；但外部Codex本地工作树及未提交修改不能由GitHub远端证明，未冒称已检查。

## 尚待适配

DR01–05、07–11及管理Harness其他专业段落；Overlay01–07、11及未逐项核查部分可能保留的CYF专业绑定；其余程序／Schema／旧测试的BI-01完整场景覆盖、Release和生成视图、全库跨目录引用。已定点调整Overlay00、08、09、10、13和CURRENT_EXECUTION及cgpterm个人入口，不代表全仓适配完成。配置虽已对齐消息组装工具的静态合同，但真实管理/专业Binding和路由尚未采用，不能声称端到端可运行。不得将当前文档已通用化等同整套系统已通用化。

## 方法

保留通用运行段落全文；只在真正的CYF专业段落换成BI-01准确专业引用，缺原文不得补造；每批复核Git diff和身份/授权/Return边界。已复制的`runtime/release/`继续视为CYF旧发布候选，不能成为本次正式Release。

本批仅静态文件变更，**没有运行手机、Pro任务或长程试跑**。


## 试跑门槛核查与补缺（2026-10-15）

结论：**OFFLINE_SYNTHETIC_DISPATCH_PASS；REAL_LONGRUN_PILOT_NOT_READY；DO_NOT_DISPATCH 仍有效。** 这是试跑准备检查，不是 BI-01 Release、实际管理采用或业务 Gate。

已补的确定性缺口：

- cgpterm 用户分支 fy/observation-iteration-agent-longrun-20261015 的观察迭代 controller Skill / README 已改为本仓真实的 Overlay08、Overlay12 路径；见其提交 874d3c07ea6e4e2b764d0720607c6d03a325801b。该分支未因此被认定为通用 main 已发布版本。
- 增加 runtime/overlay/tests/test_bi01_pilot_smoke.py 和分支专属轻量 Actions 检查，合成 Git 记录下验证 BI-01 首次 M-START BOOTSTRAP、I4 专业派发、只读审查路由、准确来源以及消息/发送状态的拒绝条件。GitHub Actions run [38740292499](https://github.com/daowei2026/observe-iterate/actions/runs/38740292499) 为 success。这是脱机机械测试，无真实模型、手机、授权或回交验证。
- DR14 修正搬迁后的两处测试/工具相对引用及残留的 C 专属正常消息描述；更新后 run [38740855167](https://github.com/daowei2026/observe-iterate/actions/runs/38740855167) 为 success。

真实受控试跑前的阻断项（不得以离线 PASS 越过）：

1. **已明确发现的活动入口旧业务要求已定点清理，但未全量验收**：本轮更新 Overlay08 的共同 MANAGEMENT_DUTY/TASK_DUTY 及 Overlay00、CURRENT_EXECUTION、09、10、13 中已点名的 A/B/C、C 五段、Feature/Reflex/CEPS 专业默认要求；保留通用管理、回交与权限。其它 DR/Overlay 和旧测试未系统改造；本轮未回归、未运行，不能据此宣称所有消息都已适配或整套运行可用。
2. **尚未真实采用工作与接收者**：runtime/config/WORKMAP_BINDING.json 为 NOT_CONFIGURED；尚无依据真实 Owner 输入形成并签发的 BI-01 BOOTSTRAP/BINDING、chat recipient、采用任务全文、既有在途对账及发送状态。不得用合成测试记录填入 runs/，也不得把旧 CYF/U2/U3 在途作为当前事实。
3. **多轮回交接续未获得实测证据**：ROLE_RETURN、QUESTION_WORK_RETURN 的真实收取、原始回答归档、去重、续作/管理 Gate 转交和中断恢复尚未通过 BI-01 角色实测；receive_return / decide_next_action / apply_transition 尚无完整已测试自动实现。首轮可明确由主控按 Overlay13 协议人工监督处理，但不能称自动闭环或无人值守。
4. **专业与发布边界**：professional/TASK_ROUTER.md 为 MISSING、独立审查 Harness 为 PARTIAL；真实 I4 需要可消费的 G3 结果与准确 Case/Source/Method/As-Of，不存在时管理 M-START 应先判定缺口而非虚报 G3。runtime/release/ 仍为 CYF 锁定发行副本，不得作为 BI-01 正式版本使用。
5. **手机现场**：本次未获得 cgpterm MCP、设备控制权、目标聊天身份、实际 payload 送达及可恢复性证据；只读远端 GitHub 无法确认 Codex 本地未提交工作。

最小后继：由操作端在真实启动时先核旧 BI-01-IT-01 的管理决定、实际 I4 回交、最新在途和聊天身份；不要默认从零 BOOTSTRAP，也不把旧运行态自动移入新仓。锁定本仓 exact commit 后，只有取得实际授权、已采用任务、可取得接收者及未发送证据时才用真实 prepare/verify 并发送；身份/权限/证据不可核即 NO_SEND。首个真实回交继续按 Overlay13 由主控按协议处理，不冒称自动引擎已部署；不合并 PR、不推广 Release、不改写历史。

## 2026-10-15 定点修正及现实接续来源

本轮只修改可确认的旧业务正文/入口、保留完整通用机制；**没有运行测试、回归、手机、专业 Pro 或长程试跑**。此前离线成功记录属于前序提交，不能当本次修改的测试结果。为遵守本轮不运行要求，已将临时 `bi01-offline-smoke.yml` 从 push 自动触发改为手动触发。

另确认旧业务仓 `daowei2026/complex-systems-vocabulary` 的 `docs/network-dynamic-ceps-factory/capital-management-purpose/observation-iteration-runs/BI-01-IT-01/` 保留真实 `CURRENT.md`、`PROGRESS.md`、`ROUTES.md`、tasks 与 returns；在所读分支中截至 2026-10-13，I4 rerun 已有第三段完整回交，原路线为 CONTINUE、下一消息待发，G4 未获管理接收。这些是**旧仓历史快照**，不是本仓已采用的在途或今日手机事实；实际操作前须 fresh 对账，不能创建第二个管理/执行任务或盲目重发。


## 旧试跑停止后的下一次清洁运行准备（2026-10-15）

Owner 已明确停止此前 BI-01/I4 试跑，希望运行机制符合预期后从实际任务重新运行。此前所读历史和第四段完整回交仍存在于旧业务 Git 历史中，但不迁移为新 run 的业务成果、Gate、聊天、在途、预算或运行状态；不删除远端 Git 历史，也不凭过去有成果断言新运行已启动。

- 新预备工作面：runs/BI-01-RESTART-01/README.md（PREPARED_NOT_STARTED）；00 管理地图、01 当前任务、真实 R0001、管理审查/绑定尚未产生，不能预造。
- 运行合同：runtime/operations/BI01_REAL_RUN_V1.md、ROUND_RECORD_CONTRACT.md、ADOPTION_HANDOFF_CHECKLIST.md。独立的新 run_id 和 chat/root/invocation/token；固定配置 work_id 为 BI-01，不能擅自把 run ID 当工作路由 ID。
- CYF 预期机制的落地差异：CYF_MECHANISM_RUNTIME_GAP_AUDIT.md。已给出实际角色 Pro Rnnnn、管理者 00 地图与 01 任务、真实 review、v2 Workmap A/B 提交、Owner PROGRESS、输入/消费版本与本地调度状态的边界。默认日常生效规则已对齐 Overlay/DR 管理及 cgpterm 观察迭代控制 Skill；源 CYF Release 和未适配专业段不得自动装入本次任务。
- 执行硬门修复：v3 消息首行 [invocation_id] 与 cgpterm scheduler 的 bracket round marker 精确绑定；v2 Schema 增加 I1— I6 正式问题 ID，保留旧 v1 原样兼容；派发配置补管理 M-REASSESS/M-CLOSE、I1— I6 modes（不是自动 Router）；BI-01 gate 检查首行、准确 SHA、源身份、未采用地图保护、真实双 Return；Workmap 模板不将每轮 pre-send provenance/turns 放入 watched business result trees，防止自过期，实质 artifacts 和独立复核仍能触发接收。
- cgpterm 个人观察迭代控制 Skill 已同步新运行入口、首次管理前的真实 Owner START/BOOTSTRAP、准确 round marker、GitHub 预发送基线、Workmap/两份回交、角色分工与现场错误隔离；通用手机/调度器代码未重写。
- 离线 CI 证据：[BI-01 mechanical-gates run 38763497170](https://github.com/daowei2026/observe-iterate/actions/runs/38763497170) 与 [Workmap 自过期场景 run 38764028763](https://github.com/daowei2026/observe-iterate/actions/runs/38764028763) 均为 success。测试只使用合成 Git/静态规范，无业务 ZIP、Pro、真实手机或新长期任务，因此**不能标记真实运行闭环通过**。

仍须真实环境才能证实或形成的义务：下一次 Owner 明确 GO、首次管理业务地图/任务真实交付与管理接收、Workmap 的实际授权采用/reader、专业题 Router 缺失的可用范围、真正专业独立审查 Harness（仍 PARTIAL）、实际唯一手机聊天与消息发送收取、每 R 回交和动态管理触发、外部 timer/继续唤醒能力，以及没有程序级强制实现的 receive_return/decide_next_action/apply_transition。上述缺口不得用文档或合成 PASS 代替；暂不运行手机、不发 Pro、不合并 PR、不升级 Release。历史的试跑已发生，不可将之前“从未试跑”的旧段理解为现在的全局状态。
