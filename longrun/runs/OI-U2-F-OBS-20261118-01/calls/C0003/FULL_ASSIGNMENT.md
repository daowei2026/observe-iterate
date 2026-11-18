[OI-U2-F-OBS-20261118-01-C0003]

你是本 Run 独立的 Skill 执行 Chat（V2 executor:E1）。本次实际调用原 manager 已签发的 A Skill 工作 D001。请亲自完整读取指定 Skill 的原始文件和内部 Workflow，并执行本项专业工作；专业完成判断及 Worker 结果处理完全按该 Skill。

run_id=OI-U2-F-OBS-20261118-01；work_id=OI-U2-F-OBS；business_case_id=U2-FQV-F；call_id=C0003；invocation_token=f3d3b2a9eaf264370bbfdd496f6d5342。
recipient=chatgpt:OI-U2-F-OBS-20261118-01:executor:E1；原委派及回交身份=chatgpt:OI-U2-F-OBS-20261118-01:manager。

正式 D 原件（必须全文阅读，不用本消息摘要代替）：
- daowei2026/observe-iterate@d1ef9eda82e6dd536959fde76e445d635430ded9:longrun/runs/OI-U2-F-OBS-20261118-01/delegations/D001/DELEGATION.json
- daowei2026/observe-iterate@4b0ff19b1bb9cf8e77cdbf41fcca96b88ac82c57:longrun/runs/OI-U2-F-OBS-20261118-01/delegations/D001/DELEGATION.md

本次 Skill 的正式原文：
- daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:skills/observation-material-preparation/feature-occurrence-understanding/SKILL.md
- 同一提交同目录 WORKFLOW.md、IO_SPEC.md，以及 Skill 实际要求的适用文件。
职责及机器回交合同：同一提交的 longrun/professional/PRO_EXECUTOR_GUIDE.md、longrun/contracts/LONGRUN_PROTOCOL_V2.md、longrun/contracts/longrun_schema_v2.json。

唯一业务输入为该提交 task-inputs/u2-fqv-observation/F_OBSERVATION_RUN_INPUT.md。Owner 本次 GO 已将其草案标记正式采用，版本占位取 f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288。请亲读 D001 所列全部适用实例、构造、参数和源码原件。唯一被观察对象是 make_features(...) 返回的 f（CommonPriceTurnGroupCandidatesFrp）；完整任务 A～E，E 交付终点。Q/V、合理性分析、历史产物预接受和输入排除的全历史 producer 重跑不在本 Run 范围。Owner 已将实际 Linux 工作区更正为 /dwdhome/fy/BASE_E6_2_copy；原输入文件与授权原文均保留在 OWNER_START，现场采用更正。

当前没有本 Run A 已完成产物；本次保持原 D001、work_item_id=OI-U2-F-OBS-20261118-01-WI-A、stage_instance_id=OI-U2-F-OBS-20261118-01-M-A。专业工作、原生输出、自检和完成条件直接依 A Skill，不以本调用封面另设方法或验收。一次 C 未完成时，保留同一 D/工作项与真实产物，并给出原工作续接点。

运行原件和专业结果写 daowei2026/observe-iterate 的 runs/OI-U2-F-OBS-20261118-01 分支，仅 longrun/runs/OI-U2-F-OBS-20261118-01/**。按 V2 先发布专业报告/产物；如 Skill 确需 W，先发布正式 W 并由当前 Return 引用，主控独立核操作权限并实际派发。最后发布本 C0003 的 longrun-professional-return/v2：role=executor、sender 为本 E1、delegation_ref 精确指原 D001 JSON、return_to 为原 manager。专业状态及剩余/接续引用按真实 Skill 结果填写；文件或单次回复不等于专业完成。若 GitHub 工具不可写，原样完整回传所需文件内容与路径供主控照原文发布，不捏造提交。

最终提交消息请包含 turn complete [OI-U2-F-OBS-20261118-01-C0003] invocation_token=f3d3b2a9eaf264370bbfdd496f6d5342，并回交实际产物的准确提交引用和仍未满足的本项工作。不要执行未调用的 B/C/D/E；主控将把本项真实回交送原 manager 沿既定 Workflow 推进。
