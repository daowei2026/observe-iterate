# BI-01 V2：首次 Workmap 只读接收入口的定向工程工作单

task_id: BI01-V2-WORKMAP-FIRST-READER-FIX-01
work_id: BI-01
run_id: BI-01-V2-01
issued_by_invocation: BI01-V2-01-R0002-b2c88771267c2530631a43db
recipient: codex-thread:01a14a59-7f26-7921-b549-3e7cd9be5119
execution_capacity: Worker Codex（本单明确受派技术职责）；完成后接回原操作职责
status: ISSUED_NOT_EXECUTED

<a id="authority"></a>
## 1. 实际授权和完整目标

授权正文是同目录 [R0002 DECISION](DECISION.md) 的 #decision、#reader-pre-adoption、#adoption；原 Owner GO 与完整 S1—S3 始终不变。本单是管理为真实运行前置生产者签发的本地技术工作，不是从尚未采用的业务地图自行认领，不需为 Worker 新建手机 Pro R 或伪造其角色 Binding。

完成当前 gate 的同根依赖修复和真实直接消费者回用，使管理签发的首次独立地图阅读在尚未 ADOPTED 时能够接受完整前置检查，随后由原操作职责真实送读者、收报告、采用并发原完整 S1—S3。代码提交或某个单测通过不是本单主动停点；技术结果回仓后，只要无新实质冲突，连续执行已签明确后继，不等 Owner 或多开一轮 Pro 来批准普通工程。

<a id="sources"></a>
## 2. 精确起点与已有能力

当前已核源码基线 `daowei2026/observe-iterate@9c2751d0785897ad17e2944680edfbe66dbff861`：
- `runtime/tools/bi01_run_gate.py`：`pre_dispatch`、`active_binding`、`invocation`、`send_state`、`locator`，blob `1c5c5d1b71159833182413a6325c4e764d3a8b97`。
- `runtime/tests/test_bi01_run_gate.py`：现成 unittest + 临时 local Git fixtures；不另建测试框架。
- `runtime/overlay/tools/workmap_gate.py`：`snapshot`、`check`、dispatch 分支、首次 base 的处理，blob `c3d1cdd50300473eb4d9db76f8c53a1b8dcc4972`。
- `runtime/config/COORDINATOR_DISPATCH.json`：INDEPENDENT_REVIEW 已有 purpose=read_only_reception，不需新增角色或另建调度器。
- `runtime/operations/ADOPTION_HANDOFF_CHECKLIST.md`、`BI01_V2_RUN_GUIDE.md`、`V2_ROUND_RECORD_CONTRACT.md`：读取其直接适用的派发/采用合同，采用本次有权修正，不加载无关旧 run。

controller 原证据：`b96ab3ee8d9d0ac7dff44f8e17d7b6dd12bdc7fc:runs/BI-01-V2-01/provenance/controller/WORKMAP_FIRST_READER_GATE_ISSUE.md::full`。Overlay12 已能 prepare/verify；JSON 所在行可用现有 Lx-Ly selector，不能固定复制旧 L91-L134 到改版正文。按实际交付文件重新定位，再由既有接口验证，不改解析器解决已经解决的事。

本工作单与本次读者任务的最终发布 commit 由 R0002 完整回交准确引用。工程取实际远端普通快进增量，先确认没有其他活动写者或冲突；不把本文源码起点当作允许覆盖后来 controller 事实的 base。

<a id="contract"></a>
## 3. 已由管理决定的行为合同

在现有 BI01 gate/调用路径内区分“首次采用证据的只读生产者”与“消费已采用任务的专业工作”。受限只读路径同时满足：BI-01-V2-01、管理当前签发的 BI01-V2-WORKMAP-READER-01、正确的 READER_TASK 完整 task/Binding/exact 采用来源、role=review、INDEPENDENT_REVIEW/read_only_reception、对应的独立接收者及已冻结的被审输入。manager 签发和角色/来源关联用原协议读取核验，不仅看某个可随意自报的布尔值；不新建授权台账或签名基础设施。

仅该用途不调用要求 ADOPTED/既有 Intake 的 `active_binding` 消费检查，也不在读者发送之前误用 `workmap_gate dispatch`。仍执行现有 invocation/真实新R/marker/token/prompt digest、exact source locators、完整 task、send-state 和外部 Overlay12/手机真实检查。已有独立性、report、read snapshot 等义务完整保留，只是由读者产生后供采用消费，不在读者自身开始前反向要求其产物。

普通 professional 的 S1—S3、无此具体授权的 review/receiver、其他 run、错 task/Binding/来源/接收者都不获该例外。不得把 role 改为 management 偷走 BOOTSTRAP，不能为了通过写 ADOPTED、RECORDED 或假 Intake，不能增加全局 skip gate 开关、全 role=review 白名单或放松 UNKNOWN/COMMITTED 的非重复发送边界。续作是同一受托 reader 任务时，沿其真实 continuation，不靠强制一次 PASS 解决。

这是已定合同。如何复用当前 selector、dispatcher 和 validator，如何组织小 helper/参数与错误信息，由工程师根据实际代码决定；不用逐函数回 Pro，不复制第二套 resolver/gate。必要同根调用点、输入/结果表示、回归、直接使用说明和首次采用兼容一起纳入，不能只改 active_binding 的一处调用后把下游同因问题留下一轮。

<a id="write-surface"></a>
## 4. 写面、版本和保护

本单主要代码/测试进入 observe-iterate 的 `fy/observation-iteration-v2-20261017`，只普通快进，保留现有改动。`runtime/tools`、对应 `runtime/tests` 及实际命中的相邻调用/说明是起点，不是封闭文件白名单；可连续处理该已定用途的依赖、表示、测试和直接消费者。共享通用 runtime 的其他行为、cgpterm 通用手机系统、角色/Owner 权力不得无授权改变；真命中另一平台公共行为时只停该受影响操作，具名回管理。

业务 mapa/task/专业 Binding、Owner/方法正文、固定 ZIP、aidata、市场算法不在技术写面。管理已签 map/reader/采用正文可由操作职责机械发布指定原文，不能由 Worker自行编改业务决定。不要把两个角色的行为混写成“已获独立审查”。

policy_commit 保持原专业方法锁 `11626f64bc64ae21e52108b2e47fafbbc1023615`；记录修补源码 commit、测试代码 commit、真正调用的脚本位置/版本。只 Python gate 的修复不触发 Haskell stack install、Numba 特征重算或缓存清除。不得在 aidata 工作区为此建第二套 gate；在实际 observe-iterate checkout 中修复。

<a id="verification"></a>
## 5. 必要验证与实际回用

先在现有 unittest/临时 Git fixtures 下覆盖真实因果和保护边界；测试记录明确为合成技术输入，不作真实 reader/Owner/Gate 历史。需验证的语义不是数量配额：

- NOT_CONFIGURED、无 Intake 下，完全符合本管理受托条件的首次 review 可完成 gate 前置；结果仍 sent=false、business_gate=false。
- 同样状态下普通 professional、其他 review/receiver、错 task/Binding/采用来源/目标输入/接收者不能借道；单加 review 字符串或冒用 bootstrap 不能通过。
- marker、prompt 字节、exact source 和身份关联破坏仍被阻止；UNKNOWN、COMMITTED 和其他不可安全重发状态仍阻止发送。
- 原 management BOOTSTRAP、正常 ADOPTED 专业路径和 after-return 两份 Return 关联不回归。
- 首次 base `2e817e2e8408b714185be55aa8f443e389b92ddf` 没有旧 map/receipt，不应导致循环重建；在明确合成 fixtures 验首次采用路径，不能生成真实假 reader 或把 current 当旧已接受 base。

已存在的命令入口为 `python -m unittest discover -s runtime/tests -p 'test_bi01*.py'`；按实际环境补充相关既有回归，不为收集测试数扩建框架。若初次执行暴露同因相邻错误，集中修通后继续。

源码提交并远端回读后，从实际选用的新代码，对真正准备的下一 reader R 的完整 Invocation/PROMPT/exact task 做 `bi01_run_gate.py pre-dispatch`，保留实际结果、执行代码身份和接收者/非重复发送证据。没有真实 prepared R 时可先作不计 R 的合成验证，但不能把它写成真实预派发通过。此处应在 NOT_CONFIGURED 下通过合格只读前置，不改状态骗结果。

<a id="return"></a>
## 6. 技术回交和连续后继

技术回交放 `runs/BI-01-V2-01/reviews/management-R0002/WORKER_RETURN.md`，含本工单和 source_invocation、实际执行者/容量、源码 commit/diff、实际命令与结果、测试及调用代码身份、未执行、限制、完整剩余和当前接续位置。必要日志沿既有本地/附件路径，不把大量现场文件或凭据推仓。此报告是受派技术自检，不是独立 reader 或管理接受实质业务。

接续顺序：修补/回归/远端回读/实际 gate 回用 → 原操作职责向真正独立的新上下文发送本轮重新绑定的 READER_TASK → 收真实报告 → 按 R0002 DECISION#adoption 机械 Intake/ADOPTED/专业 dispatch → 原完整 S1—S3 task 首发。管理已经给出这条明确后继，不需等一个新 Owner GO 或先开另一管理 Pro 做普通代码选择。

若工作区/调用权限缺失、核心必要代码无法按合同修通或出现新实质语义冲突，报告已经尝试的具体动作、实际错误、直接受影响输出和有根据的下一步回本管理；不重复提交相同 WORKMAP_NOT_ADOPTED 而不执行本工单。其他清楚且获授权工作继续；未生成图/数据/S3 不能靠技术报告补成完成。

本地 Worker 施工和 Git commit 不计新 R。下次真正 Pro 调用由原操作流程分配实际新 R/token；不要提前把它称 R0003 已发生，也不要重发 R0001/R0002。
