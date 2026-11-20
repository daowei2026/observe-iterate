[OI-U2-V-OBS-20261120-01-C0002]
invocation_token=7c2666356a6e4dbfb4f7614791abed61

你是本Run独立的Skill执行Chat（V2 executor），本次准确执行已由真实manager签发并被主控核验的D001 / WI-A / M-A。不是运行协调Chat；原Skill决定专业方法、内部Workflow、自检和完成条件。

run_id=OI-U2-V-OBS-20261120-01
call_id=C0002
recipient=chatgpt:OI-U2-V-OBS-20261120-01:executor:E1
delegation_id=D001
work_item_id=OI-U2-V-OBS-20261120-01-WI-A
stage_instance_id=OI-U2-V-OBS-20261120-01-M-A
return_to=chatgpt:OI-U2-V-OBS-20261120-01:manager

唯一正式工作来自D001原件（下方保留完整正文）：
- DELEGATION.json：daowei2026/observe-iterate@acccde23c5753ba8b0b98581063a1e857429f4a3:longrun/runs/OI-U2-V-OBS-20261120-01/delegations/D001/DELEGATION.json
- DELEGATION.md：daowei2026/observe-iterate@d8ff75ad2201a8440e7a1d31e68720074eff7c1e:longrun/runs/OI-U2-V-OBS-20261120-01/delegations/D001/DELEGATION.md
- 签发manager Return：daowei2026/observe-iterate@a95c0a89396dc3c9a196d5299b9fb5f336a6e103:longrun/runs/OI-U2-V-OBS-20261120-01/calls/C0001/PRO_RETURN.json
- 原manager报告：daowei2026/observe-iterate@593295b6c070776cdd25f43c57282187e4708645:longrun/runs/OI-U2-V-OBS-20261120-01/calls/C0001/MANAGER_REPORT.md

请亲自完整读取D所引用A原始SKILL.md、WORKFLOW.md、IO_SPEC.md及适用Reference，依原文件实际执行本项Skill。固定专业来源observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288，唯一V输入@3efb2719a66a2fcc1bb86f33b7b0a2258f9bfbf7。原始输入和代码引用以D和Owner GO为准；只针对CommonTurnGroupValidityFrp，即make_features(...)第三项v，f/q仅必要上游。历史F/Q阶段成果没有被接受为V的A成果。工作区的Owner覆盖为/dwdhome/fy/BASE_E6_2_copy，权限仅D与Owner Binding交集，不从旧任务继承。

按原Skill形成原生结果和准确引用，使用既有V2报告与PRO_RETURN.json回交原manager；单次调用不足时继续原D001与原工作项。专业状态按原Skill事实，未完成如实列明。所有本Run新记录仅写observe-iterate@runs/OI-U2-V-OBS-20261120-01:longrun/runs/OI-U2-V-OBS-20261120-01/**。不得以文件存在或一次回复结束替代本项专业完成。

跨端协议采用D所引LONGRUN_PROTOCOL_V2.md及longrun_schema_v2.json。机读PRO_RETURN使用longrun-professional-return/v2，role=executor，sender=本recipient，delegation_ref=上述D001 DELEGATION.json，return_to=上述原manager。字段严格依原schema，不添加invocation_token等schema未列字段；完整token保留在专业报告封面、最终commit message及最终回复结尾。D/Return/W引用顺序按V2，正式ref均40位commit。报告或原生结果与机器Return分开，主控不替你决定方法或结果。

完成本次实际交付后，最后commit message包含 turn complete [OI-U2-V-OBS-20261120-01-C0002] invocation_token=7c2666356a6e4dbfb4f7614791abed61。最终回复给出原生结果、报告和Return精确refs，真正结尾保留该marker与完整token。如GitHub工具不能发布，完整原文交回并说明实际未发布，不虚构commit。

以下为原manager签发D001正文，原样传递，不追加专业方法：

# D001｜A Skill 工作委派：CommonTurnGroupValidityFrp occurrence 理解

本 D 仅绑定一次具体 Skill 工作与已经存在的输入，不重新规定专业方法、业务预期、展示方案、Worker 返回处理或专业验收条件。机器身份、操作授权和实际发送状态以本 Run 的 V2 记录及主控核验为准。

## 1. 委派身份

- `run_id`：`OI-U2-V-OBS-20261120-01`
- `delegation_id`：`D001`
- `issuer_call_id`：`C0001`
- `issuer`：`chatgpt:OI-U2-V-OBS-20261120-01:manager`
- `recipient`：`chatgpt:OI-U2-V-OBS-20261120-01:executor:E1`
- `return_to`：`chatgpt:OI-U2-V-OBS-20261120-01:manager`
- `parent_task_id / work_id`：`OI-U2-V-OBS`
- `business_case_id`：`U2-FQV-V`
- `work_item_id`：`OI-U2-V-OBS-20261120-01-WI-A`
- `stage_instance_id`：`OI-U2-V-OBS-20261120-01-M-A`

## 2. 本次 Skill

- Skill：`daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:skills/observation-material-preparation/feature-occurrence-understanding/SKILL.md`
- 内部 Workflow：`daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:skills/observation-material-preparation/feature-occurrence-understanding/WORKFLOW.md`
- 字段级 I/O：`daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:skills/observation-material-preparation/feature-occurrence-understanding/IO_SPEC.md`

本项专业工作由接收者亲自完整读取并采用上述 Skill 原件。

## 3. 外层任务已经提供的事实

- 本次特征名称：`CommonTurnGroupValidityFrp`（V｜共同转折组的局部成立判断）。
- 特征代码版本：`daowei2026/frp@67711c492da909ed0f044f357beb278abf7fc71c`；正常 Python 包装与实例构造版本：`daowei2026/tis@2f460d663d821cf2ba25555eda13e78b697d0767`。
- 本次特征实例：按已给 `make_features(...)` 完整参数构造后，只取返回的第三项 `v`；其类型应为 `CommonTurnGroupValidityFrp`。当前实例上下文为 `TA_updto20240229_DBA / steel / night_end_at_2300 / 5m / rb,hc,i / DirectionUp`，V 方法为 `ClosedFormationLocalValidity`。完整构造、参数和实例身份以下列精确原件为准，不以本段摘要替代。
- `v` 由准确的 `q` 经 `CommonTurnGroupValidityFrp.from_organization(q)` 构造；`q` 又由准确的 `f` 经 `PostTurnGroupDirectionalOrganizationFrp.from_formation(f, ...)` 构造。F、Q 只作为 V 的必要上游依赖；本 Run 不执行 F/Q 的独立 A～E，不把 F/Q 历史交付或阶段成果计入 V 的完成范围，也不把 F/Q 输出冒充 V 主输出。
- Q 当前按 Owner 指令暂停且未完成，历史记录保留；Q 不自动恢复。本次 V 已独占取得 `/dwdhome/fy/BASE_E6_2_copy`，这不改变 F/Q 只作必要上游依赖的业务边界。
- 本 Run 完整范围为 V 的观察材料准备 A～E，并以 V 的 E 交付结束；合理性分析、F/Q 独立 Workflow、S/U2/U3、参数标定、收益判断、资金配置及未经授权的全历史 producer 重跑均不在范围内。
- Owner 确认的本 Run Linux 工作区为 `/dwdhome/fy/BASE_E6_2_copy`。所有本 Run 新业务产物和运行记录写入 `longrun/runs/OI-U2-V-OBS-20261120-01/**`；本 A Skill 当前没有 Worker 工单。

## 4. 当前输入与适用原始文件

### 4.1 Run 与业务输入

- Owner GO：`daowei2026/observe-iterate@14610d4e6dbcf1af5ea024754f9da6eb5a901e8c:longrun/runs/OI-U2-V-OBS-20261120-01/OWNER_START.md`
- Binding：`daowei2026/observe-iterate@a95c6c7a2feae3dcd1e7622a01a509afc4070488:longrun/runs/OI-U2-V-OBS-20261120-01/RUN_BINDING.json`
- 资源绑定：`daowei2026/observe-iterate@a95c6c7a2feae3dcd1e7622a01a509afc4070488:longrun/runs/OI-U2-V-OBS-20261120-01/RUN_RESOURCE_BINDING.json`
- Q 暂停及工作区移交记录：`daowei2026/observe-iterate@d446b94527a61a5f07b47f0470eb6787b7a52274:longrun/runs/OI-U2-V-OBS-20261120-01/Q_PAUSE_HANDOFF_20261120.json`
- C0001 原任务：`daowei2026/observe-iterate@9877e14c749a80ae5494d9d37386e87b723c33a8:longrun/runs/OI-U2-V-OBS-20261120-01/calls/C0001/FULL_ASSIGNMENT.md`
- C0001 Invocation：`daowei2026/observe-iterate@d446b94527a61a5f07b47f0470eb6787b7a52274:longrun/runs/OI-U2-V-OBS-20261120-01/calls/C0001/INVOCATION.json`
- 唯一 V 业务输入：`daowei2026/observe-iterate@3efb2719a66a2fcc1bb86f33b7b0a2258f9bfbf7:task-inputs/u2-fqv-observation/V_OBSERVATION_RUN_INPUT.md`

### 4.2 实例构造、V 实现与 F→Q→V 输入合同原件

- 本批实例读取脚本：`daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:task-inputs/u2-fqv-observation/实例运行脚本.py`
- 需求与实现索引：`daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:task-inputs/u2-fqv-observation/无二义性需求和实现文件.md`
- 正常 `make_features(...)` 构造原件：`daowei2026/tis@2f460d663d821cf2ba25555eda13e78b697d0767:frp/fqv_kline_example.py`
- 完整展开实例参数：`daowei2026/feature-refinement-implementation-agent-evolution@2d3f56a7944c44b2a1c441c15eebf9659835136b:agent_evolution/pilot_cases/network-dynamic-ceps-factory-u2-u3/configurations/fqv-kline-rb-hc-i.json`
- V 的 Haskell 主实现：`daowei2026/frp@67711c492da909ed0f044f357beb278abf7fc71c:src/Frp/Instance/ISL/Opportunity/CommonTurnGroupValidity.hs`
- V 的 Python 包装与正式读取接口：`daowei2026/tis@2f460d663d821cf2ba25555eda13e78b697d0767:frp/CommonTurnGroupValidity.py`
- 必要上游 Q 的 Haskell 主实现：`daowei2026/frp@67711c492da909ed0f044f357beb278abf7fc71c:src/Frp/Instance/ISL/Opportunity/PostTurnGroupDirectionalOrganization.hs`
- 必要上游 Q 的 Python 包装与正式读取接口：`daowei2026/tis@2f460d663d821cf2ba25555eda13e78b697d0767:frp/PostTurnGroupDirectionalOrganization.py`
- 必要上游 F 的 Haskell 主实现：`daowei2026/frp@67711c492da909ed0f044f357beb278abf7fc71c:src/Frp/Instance/ISL/Opportunity/CommonPriceTurnGroupCandidates.hs`
- 必要上游 F 的 Python 包装与正式读取接口：`daowei2026/tis@2f460d663d821cf2ba25555eda13e78b697d0767:frp/CommonPriceTurnGroupCandidates.py`

## 5. 已有上游真实产物

本 Run 的 V A～E 均无已完成专业产物。本 D 是本 Run 首项 Skill 工作；截至签发时，没有 V 的阶段产物，也没有已发 Worker 工单。F/Q 的历史结果、源码及索引仅作为 V 必要上游关系和代码／实例定位来源，不作为 V 的 A 阶段完成结果。Q 的暂停记录也不构成 V 的专业产物。

## 6. 本项专业输出与回交

- 本项专业输出、状态和完成条件直接遵循第 2 节所列 A Skill 的原生合同，不另设最小证据、专业验收或 Worker 返回处理要求。
- 实际回交对象：`chatgpt:OI-U2-V-OBS-20261120-01:manager`；回交时保持 `work_item_id=OI-U2-V-OBS-20261120-01-WI-A`、`stage_instance_id=OI-U2-V-OBS-20261120-01-M-A` 和 `delegation_id=D001`。
- 一次调用不足以完成本项 Skill 时，继续原 `D001` 与原工作项，并引用已经形成的真实产物和当前续接点。
