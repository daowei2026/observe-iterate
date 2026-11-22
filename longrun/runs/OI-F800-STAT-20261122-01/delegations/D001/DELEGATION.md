# D001｜F800 最小当前理解核对（U）

- run_id：`OI-F800-STAT-20261122-01`；work_id：`OI-F800-STAT-20261122`；business_case_id：`F-STATISTICS-CLOSURE`。
- parent_task_id：`OI-F800-STAT-20261122`；work_item_id：`F800-U-001`；stage_instance_id：`F800-U-001`；签发调用：`C0001`。
- issuer / return_to：`codex:OI-F800-STAT-20261122-01:manager`；recipient：`codex:OI-F800-STAT-20261122-01:executor:E1`。
- execution profile：`CODEX_NATIVE_DIRECT`；workers=[]。E1 是接收逻辑身份，controller 在正式 D 发布后创建独立物理线程；本 D 尚未发送。

## Skill 与本项任务

本次只委派 `feature-structure-and-behavior-understanding`：

`daowei2026/observe-iterate@87b951bbd15078a2d6353bdd24afe0d8f19c845c:skills/feature-understanding/SKILL.md`

必要 WORKFLOW、IO_SPEC 依 Skill 原文；适用补充：`daowei2026/observe-iterate@87b951bbd15078a2d6353bdd24afe0d8f19c845c:skills/feature-understanding/BUSINESS_OBJECT_QUALIFICATION_GUIDE.md`。
外层 Workflow 为 `daowei2026/observe-iterate@87b951bbd15078a2d6353bdd24afe0d8f19c845c:control-v0.3/01_L0_统计驱动的单特征闭环.md` 的 §2 U；本项深度沿用该节与 BusinessTaskInput §6 的既有理解复用和最小当前核对规则。专业内容、原生产物与完成条件直接遵循上述已采用原件。

## 有效输入

BusinessTaskInput：`daowei2026/observe-iterate@87b951bbd15078a2d6353bdd24afe0d8f19c845c:task-inputs/wall-f-parallel-closure-20261122/F_BASE_RUN_INPUT.md`。Owner GO：`daowei2026/observe-iterate@43a13e14129984d6f3a142c6eb64397a43c3ca79:longrun/runs/OI-F800-STAT-20261122-01/OWNER_START.md`。

外层已锁定 Feature 为 `CommonPriceTurnGroupCandidatesFrp`，即 `frp/fqv_kline_example.py::make_features` 返回的 f；只 F，不运行或分析 Q/V 专业产物。

- FRP：`daowei2026/frp@ac1927518ad6105f15ffbe37fea45e4be91ba574`，输入声明分支 `codex/f-observation-multiple-20261122`。
- TIS：`daowei2026/tis@2f460d663d821cf2ba25555eda13e78b697d0767`。
- 参数与实例：BusinessTaskInput §1—3 的 U2/U3 基线及唯一已批准 override `profile.observation_multiple=800`；`delta=600`、`unit=CalendarUTITick`。
- 正式范围：`rb/hc/i`、`5m`、`night_end_at_2300`、`TA_updto20240229_DBA`、`steel`、`2021-01-01` 至 `2023-12-31`。
- Linux 工作区：`/dwdhome/fy/BASE_E6_2_copy`。

已有理解线索和基线来源均列于 DELEGATION.json.input_refs，沿 BusinessTaskInput §5—6 使用。它们尚未被本 Run executor 核验或接受，不是本 Run 已完成的 U、X、G 或 Release 成果；F800 结果身份尚无本 Run 合格绑定。

## 原生输出与回交

输出按 Skill 原文，适用上述 L0 §2 与 BusinessTaskInput §6。由 executor 作真实的 COMPLETE / PARTIAL / BLOCKED 判断并保留未确认项；不增加本 D 自拟的专业检查表。按原 V2 协议发布专业报告和 PRO_RETURN，回交 `codex:OI-F800-STAT-20261122-01:manager`，绑定本 D 的实际发布 exact ref。没有 Worker，issued_order_refs=[]、accepted_worker_refs=[]。

## Owner 操作授权

Binding：`daowei2026/observe-iterate@2665f0cbabff0439fe8d361c2ad545bf922e1792:longrun/runs/OI-F800-STAT-20261122-01/RUN_BINDING.json`；资源绑定：`daowei2026/observe-iterate@2665f0cbabff0439fe8d361c2ad545bf922e1792:longrun/runs/OI-F800-STAT-20261122-01/RUN_RESOURCE_BINDING.json`。本 D 机读权限仅采用 Binding 内 `run_result_statistics_analysis_write` 与 `run_record_write`；写面为本 Run 记录路径及所绑定 Linux 工作区，具体原授权引用以 Binding.grants.authority_quote 与真实 Owner 原文为准。Skill 自身的工作边界继续有效。

Owner 已锁定的代码与 F800 实例作为本次输入；任何进一步正式行为、参数、常量、期限、数据处理或输出合同改变，依真实 GO 和已采用 L0 §7 的 ModificationProposal → Owner 确认链处理。
