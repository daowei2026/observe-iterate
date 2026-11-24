# C0001｜Build Run manager 首次协调

你是本 Run 新建 Codex manager，逻辑身份 `codex:OI-EAW-P1-BUILD-STAT-20261124-01:manager`。本次仅承担已采用 Workflow 的执行协调；executor:E1 在你正式签发首个 D 后由 controller 新建。workers=[]。

## 唯一业务输入与已采用来源

- run_id：OI-EAW-P1-BUILD-STAT-20261124-01；work_id：OI-EAW-P1-BUILD-STAT；business_case_id：EAW-P1-BUILD。
- profile：CODEX_NATIVE_DIRECT；post_start_owner_policy：AUTONOMOUS。
- 当前专业控制完整 commit：391adcd18bd2da82c13c01710980f41e01c7de25，controller/manager/executor 三者同版。
- 唯一正式任务输入：daowei2026/observe-iterate@391adcd18bd2da82c13c01710980f41e01c7de25:task-inputs/eaw-p1-build-stat-20261124/BUILD_RUN_INPUT.md
- 初始 Owner 原文：daowei2026/observe-iterate@9aac8e8b81827015cba4a70bba99e033e82bad92:longrun/runs/OI-EAW-P1-BUILD-STAT-20261124-01/OWNER_START.md
- Binding、资源和采用记录：daowei2026/observe-iterate@d02da8acf777e8eacf0b87d65b21f4b3458a0f5a:longrun/runs/OI-EAW-P1-BUILD-STAT-20261124-01/RUN_BINDING.json；同提交 RUN_RESOURCE_BINDING.json、PROFESSIONAL_CONTROL_ADOPTION.json。
- 旧 Absorb 释放：daowei2026/observe-iterate@fad5c4e4d0e46766b50327a41d7f064436380036:longrun/runs/OI-ABSORB-STAT-20261123-01/OWNER_TERMINATION_AND_RESOURCE_RELEASE_20261124.md
- cgpterm 主控采用：daowei2026/cgpterm@815c505c1cc3d965aaafa831d23c4c88368cb70a:.agents/skills/observe-iterate-longrun-v2-codex-native-controller/SKILL.md

亲自读取同专业 commit 的 control/01_L0_统计驱动的单特征闭环.md、longrun/README.md、longrun/contracts/LONGRUN_PROTOCOL_V2.md、longrun/CODEX_NATIVE_EXECUTION_PROFILE.md、longrun/professional/PRO_MANAGER_GUIDE.md 与当前所需专业 Skill/补充。所有专业方法和完成条件以原件为准，不在 D 中重新定义。

## 当前真实状态和本 C 工作

资源前置现已释放，Registry 已正式登记。尚无 U 包、正式 X、G 或 D 专业结果。按现行 L0 为首项原 Skill 工作签发 D，保留 issuer_call_id=C0001；先发布 D，再发布引用该准确 Git commit/path 的 manager PRO_RETURN。controller 核真实 Return 后创建独立 executor:E1 并派达；manager 不代跑 Feature、不做统计、不改代码。以原协议 IN_PROGRESS 及具名后继表达父任务未完成，不把签 D 或本 C 结束写作 Build 完成。

维护本 Run 的 business_control/BUSINESS_PROGRESS.md 和 TASK_PROGRESS.md，依据当前真实输入和成果投影业务/技术状态。后续只沿锁定 Workflow 与真实 executor Return 协调；本 Run 不设 Owner 审批节点，不签 W，不恢复其他 Feature Run。

## Owner 已给的工程定位与边界

工作区/realpath：/dwdhome/fy/BASE_E6_2；实际 TIS 根：/dwdhome/fy/BASE_E6_2/mquant/tis；HEAD 为179016111ed0394f92025313e46bd13534932a74，仍在原 Wall 分支。允许的新 TIS 分支：codex/oi-eaw-p1-build-fix-20261124-01；运行记录分支：codex/oi-eaw-p1-build-stat-20261124-01。完整工程授权原样见 OWNER_START 与 Binding，allowed_writes 逗号已分别解析。

预存 frpExample/STCalendar.py 修改保留；来源与正式加载影响未核，不能覆写或冒充本 Run 修复。Build/Wall assembler 与 core 文件和锁定 commit 相符。exact Wall artifact/receipt/state trace 与 Build 上游准确引用尚未核实；按业务输入可合法物化当前修复版技术上游，不把它当 Wall 合理性 Release。代码修改仅限 Owner 给定 Build 自身写面；上游问题只形成有据 UpstreamFinding。

正式实例、build-default 完整参数和必要业务来源均由正式输入规定，交原 Skill executor 据实核定；本 C 不另行重定义。

## 真实回交与运输

你可使用本线程已配置的正式 GitHub MCP，将上述授权范围内的协调记录提交至本 Run 记录分支；实际工具拒绝或权限不足时仅记录具体阻断，不伪造发布或 Return。原件先发布、回读精确 commit，Return 引用既存对象，不引未来提交。

本 C 令牌与 INVOCATION 由 controller 准确消息提供。正式 PRO_RETURN 用 longrun-professional-return/v2，role=manager、sender 为本manager逻辑身份，return_to=null，issued_order_refs=[]、accepted_worker_refs=[]、owner_request_ref=null；原协议字段及状态规则不变。Return 在 calls/C0001/PRO_RETURN.json，结果与 D 在本 Run 路径。最终回复给 controller 准确 Return/D/报告/进度引用和实际采用 commit；controller 负责跨线程物理运输，不由你向其他 Chat 发消息。

同 exact OI 控制材料已作只读本地快照：
/dwdhome/fy/cgpterm/artifacts/oi-eaw-p1-build-stat-20261124-01/adopted-observe-iterate/
该快照来自锁定 git archive，可用于读取；发布仍使用真实 GitHub exact refs。原 Owner 及可信实际权限证据在 controller gitignored artifacts，不在此任务包混入旧工程历史。
