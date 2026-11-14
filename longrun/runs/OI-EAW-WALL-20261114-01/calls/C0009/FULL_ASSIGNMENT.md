# C0009｜原E1接管当前D003并推进Run隔离scenario工程前置

run_id OI-EAW-WALL-20261114-01；call_id C0009；marker [OI-EAW-WALL-20261114-01-C0009]；token oiwall-C0009-190d150456e40c72d1d38699。
recipient chatgpt:OI-EAW-WALL-20261114-01:executor:E1，继续原独立E1；issuer/return_to仍为原manager chatgpt:OI-EAW-WALL-20261114-01:manager。

## 完整任务与签发原件

请完整阅读、实际承接并执行 manager C0008 当前签发的 D003，不停留在建议：
- 当前D003正文：daowei2026/observe-iterate@461a420bbacc5d24ee093f9f20f2f86653973041:longrun/runs/OI-EAW-WALL-20261114-01/delegations/D003/DELEGATION.md
- 当前D003 JSON／本调用origin：daowei2026/observe-iterate@b7200816f86395cd1475ea3a482fc2e63086b967:longrun/runs/OI-EAW-WALL-20261114-01/delegations/D003/DELEGATION.json
- 原manager C8 Return：daowei2026/observe-iterate@2b8e745093ee6eec966d89e0a55a2baa5a022249:longrun/runs/OI-EAW-WALL-20261114-01/calls/C0008/PRO_RETURN.json
- C8管理报告：daowei2026/observe-iterate@a0d00577711e9b453cc75cabaf771cd019d5ecb2:longrun/runs/OI-EAW-WALL-20261114-01/calls/C0008/MANAGER_REPORT.md
- C8运输修签决定：daowei2026/observe-iterate@147770cb63bc0de3b9a97eee1c6aa4abd6fbbbff:longrun/runs/OI-EAW-WALL-20261114-01/business_control/decisions/MD-C0008-001.md
- C7原专业决定：daowei2026/observe-iterate@11fce23f543b000425350153d9cb1eda5e78453c:longrun/runs/OI-EAW-WALL-20261114-01/business_control/decisions/MD-C0007-001.md
- 最新全景：daowei2026/observe-iterate@31c35e5a270ae28e9f553934faeec3a583e6ef14:longrun/runs/OI-EAW-WALL-20261114-01/business_control/TASK_PROGRESS.md

业务仓、控制面、专业Skill和长程协议统一采用 daowei2026/observe-iterate@ca7fdae84f65265332e3a53865724a2615508766；主控采用06eda7c9bed88ab1c35de1ff7e9e470bef341bab，不更换版本。D003列出的专业输入、source exact baseline和全部EP acceptance均是完整合同，不由本转交摘要替代。

## 真实业务连续性

你已完成并正式回交D002。原manager已实际接受关闭其两lane，接受三项scoped QCR、通过legacy normal-chain限域comparison（四个SUPPORTS共享一条历史chain，非四份独立证据）。三个父Q继续OPEN、父任务incomplete，current normal/scenario两action均NEEDS_PRECONDITION、G-RUN未通过。没有正式COUNTERS，不触发diagnosis。

原manager选择scenario-first，D003只建设shared + scenario八EP工程前置。C7 D003候选从未送达，现已由C8修订版替代；不得使用旧候选作为当前delegation_ref。C8只修运输token表示，全部专业范围、实际子根、cap、禁令、Gate不变。主控已核六文件及五精确refs逐字/hash一致，validate-manager-return和validate-delegation通过；这不等于Worker已获准或工程已执行。

## 本轮实际推进与工具边界

由你按完整D003自主组织专业安排、预检、实现审查和交付。Linux staged engineering确需工具时，先签合法的新Worker工单，收到真实结果后由你消费再回原manager。当前新order候选W002未被占用，Binding唯一批准Worker逻辑身份 codex:OI-EAW-WALL-20261114-01:worker:W1；旧W001已完成消费、其旧写锁已释放，不重用旧锁或旧单。主控收到合法W、核当前物理chat/model/effort/cwd和真实独占后才实际派发；你不能假定Worker已运行。

新W的issuer_call_id必须为C0009、issuer及return_to为你，delegation_ref指向当前C8 D003 JSON。W.grant逐字沿用对应Owner原授权的operation/execution_context/authority_quote/allowed_writes token；W instructions、输出、执行目录和write audit再严格收窄D003 actual root。不能把空grant或根token当超出D3实际子根写权限。

实际Linux子根仅：
/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D003
D003业务成果实际发布到：
longrun/runs/OI-EAW-WALL-20261114-01/delegations/D003/results
正式C/D/W运输原件依本次采用V2的准确身份/路径签发，不以成果目录替换正式运输路径。若发现真实合同矛盾，具名回交而不自行改D或扩大授权。

保持先dry dependency/write/cost preflight；只有全部可监测且预计不超cap时才做compile-only和限定工程测试。disk<=2GiB，RSS<=4GiB，post-preflight wall<=25min，new files<=50000，D3外写入0，九场景evidence execution0。编译/测试条件未具备时仍交可审查合格子集和最小解除条件，局部问题不让其他合法工作冻结。

禁止九场景证据运行、normal action、DBA/wrapper/native reader、改共享源码或源码repo push、改production生命周期语义；工程测试不能形成current O/C/A/D业务材料或自行G-RUN。staged source/patch/local commit是Run工程artifact，不称上游发布。不得重跑W001调查或重复出版旧313原件。

## 回交

完成当前专业可推进部分并实际发布D003合同要求的最低/条件成果。若签W，先完整ORDER正文+JSON，按V2回交IN_PROGRESS及准确remaining/continuation，issued_order_refs只列真签单；manager不直接签W。零工具同样不能虚称实现、编译、测试或EP满足。

正式PRO_RETURN必须role=executor、sender=你、delegation_ref=当前C8 D3 JSON、return_to=原manager，accepted_worker_refs只可列实际消费且主控验证的Worker Return。REPORTED_COMPLETE仅指D003合同完整交付，不能据此声明父任务或scenario action完成。需要manager决定的后继完整保留，不例行逐项问Owner。

遵守V2一小时GitHub/ZIP完整回交合同。只写Owner授权Run分支；最终calls/C0009/PRO_RETURN.json及最后commit精确含：
turn complete [OI-EAW-WALL-20261114-01-C0009] oiwall-C0009-190d150456e40c72d1d38699
