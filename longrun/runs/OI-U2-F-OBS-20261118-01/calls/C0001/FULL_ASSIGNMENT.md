[OI-U2-F-OBS-20261118-01-C0001]

你是本 Run 的多层 Workflow 运行协调 Chat（V2 manager）。这是 Owner 已正式 GO 的新 Run 首次实际调用。请实际建立任务完成全景，并首先签发 A Skill 工作，按既定 Workflow 持续推进。

身份：work_id=OI-U2-F-OBS；business_case_id=U2-FQV-F；run_id=OI-U2-F-OBS-20261118-01；call_id=C0001；invocation_token=3d02efa91ad3abb2a973c6c71fe2f39f。
manager=chatgpt:OI-U2-F-OBS-20261118-01:manager；本次可用 Skill 执行身份=chatgpt:OI-U2-F-OBS-20261118-01:executor:E1；回交主控=codex:OI-U2-F-OBS-20261118-01:controller。

请亲自完整读取并采用下列精确原件：
1. Owner GO 与本聊天后续工作区更正：daowei2026/observe-iterate@74ed0b11552f73b03e55e3e324f8325889730b52:longrun/runs/OI-U2-F-OBS-20261118-01/OWNER_START.md
2. 正式 Binding 与资源：daowei2026/observe-iterate@b6fcc3dd824b6e28fffd5b8d464989289dd4d97d:longrun/runs/OI-U2-F-OBS-20261118-01/RUN_BINDING.json 与同提交同目录 RUN_RESOURCE_BINDING.json。
3. 唯一业务输入：daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:task-inputs/u2-fqv-observation/F_OBSERVATION_RUN_INPUT.md 。输入中“草案”标记已由本次 Owner GO 明确转为正式采用；其中观察材料 Workflow 版本占位取本次锁定的 f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288。外层构造/实例原件按该文件亲自读取，不用摘要代替。
4. 职责与流程：daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:longrun/professional/PRO_MANAGER_GUIDE.md；同提交 longrun/contracts/LONGRUN_PROTOCOL_V2.md、longrun/contracts/longrun_schema_v2.json、longrun/CONTROL_PLANE_ADAPTER.md、control/02_L1_观察材料准备流程.md、control/06_业务完成全景与更新协议.md、longrun/templates/PRO_DELEGATION.md 和 longrun/templates/TASK_PROGRESS.md。其余 control/review 是按当前正式版本理解的上下文，不以历史控制设计覆盖当前 A～E 或新增 Gate。

本次唯一对象 CommonPriceTurnGroupCandidatesFrp（F），只取 make_features(...) 返回的 f。完整执行 A～E，以 E 观察材料交付结束；不纳入 Q/V、不做合理性分析、不把历史产物当本 Run 已完成结果、不执行输入排除的全历史 producer 重跑。Owner 已将实际 Linux 工作区更正为 /dwdhome/fy/BASE_E6_2_copy；原始输入文件保持原文，现场以这条更正为准。

本次先调用 A：daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:skills/observation-material-preparation/feature-occurrence-understanding/SKILL.md。请按 V2 签发默认一项 Skill 工作的 D001 给 E1，准确引用该 Skill 及适用原始文件、当前输入和回交对象。不要在 D 正文另加专业执行约束、专业方法、业务预期、展示方案、Worker 返回处理或额外验收条件；专业工作由 E1 亲读完整 Skill 自己执行。A 完成后 B/C 按实际独立性和资源安排，D 消费当前有效 A/B/C 后再进入 E；一次 C 未完成 Skill 则接续原 D/工作项。

请持续维护 longrun/runs/OI-U2-F-OBS-20261118-01/business_control/TASK_PROGRESS.md：整体目标、工作项和阶段、真实执行 Chat、有效成果与版本依赖、未完成/在途/阻断及下一合法动作。当前没有已完成 A～E，也没有已发 W；不要把准备文件视为发送或专业完成。物理操作授权和 Worker 派发前校验由主控单独核实。

本 Run 的运行原件只写 daowei2026/observe-iterate 的 runs/OI-U2-F-OBS-20261118-01 分支下 longrun/runs/OI-U2-F-OBS-20261118-01/**。先发布 D001 的 DELEGATION.md/json，再发布引用其准确提交的 C0001 专业报告和 PRO_RETURN.json；Return 使用 longrun-professional-return/v2、role=manager、call_id=C0001，并在 issued_delegation_refs 引用实际发布的 D。不得引用未来 Return。若当前工具不能写 GitHub，原样完整回传所需文件内容及路径，由主控按此顺序照原文保存，不捏造提交或发送。

请于本次调用完成时提供准确文件/提交引用；最终提交消息包含 turn complete 与 [OI-U2-F-OBS-20261118-01-C0001] 及本次 invocation_token，以便主控核实真实回交。若写 GitHub 不可用，可附完整结果包并给出原生返回；当前调用不足以完成时，明确原工作接续引用。主控将依据真实返回实际派发 A，不要求为正常 Skill 工作逐项再请 Owner 批准。
