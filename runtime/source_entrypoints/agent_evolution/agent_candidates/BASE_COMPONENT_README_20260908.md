# 长程任务产出的候选 Agent 包

本目录保存 Mission A、Mission B、Mission C 的当前完整候选包，以及只负责三者长程连接的运行覆层和生成式 Project runtime 投影。它们仍是候选：`runtime_maturity: human_led_candidate`、`validated_runnable: false`、`owner_acceptance: pending`。进入仓库、静态校验通过或成功构包，都不等于已可部署或已获 Owner 接受。

## 优先入口：本轮自存与必要材料补齐（2026-09-08）

先读 [11：本轮问答与实质材料入库](runtime_overlay_candidates/agent_owned_long_horizon_overlay_v0_3/11_本轮问答与实质材料入库.md)。Pro 每次交付自行提交本轮实际提示和完整回答；不补历史问答，不等外部采集器。必要任务正文与有效修订必须真实可读，总包成员被多处讲解或链接只存一次。

继续已有长程、专门补 GitHub 材料时，使用 [08 的 MATERIAL_CATCHUP 启动段](runtime_overlay_candidates/agent_owned_long_horizon_overlay_v0_3/08_自然语言运行提示_v0.3.md)，默认 2–3 轮、可提前结束：直接导入重要正文，补齐剩余依赖，再从远端核验；不只生成清单，不重做业务，不把材料入库误作业务审查通过。原位复用既有任务目录和地图，实际运行进展以该任务当前正文为准。

此修订只更新通用运行材料及其投影，未替任何用例执行补齐，也未部署本地 routine。双路实现分工和更大的管理角色建设不在本次改动中。

## 新开或继续长程：先接持续工作面

自 `2026-09-07` 执行修订起，先读 [GitHub 持续工作面](runtime_overlay_candidates/agent_owned_long_horizon_overlay_v0_3/09_GitHub持续工作面与版本管理.md) 和 [独立审查与下一问题选择](runtime_overlay_candidates/agent_owned_long_horizon_overlay_v0_3/10_独立审查与下一轮问题选择.md)。使用 [启动／中途接续提示](runtime_overlay_candidates/agent_owned_long_horizon_overlay_v0_3/08_自然语言运行提示_v0.3.md) 实例化本任务，不把本仓具体用例写入通用规则。

在 Owner 指定目录创建或接续已有推进地图，正文稳定路径原位更新；独立审查先核实产物，再结合实际进展和全图决定下一轮应思考的问题。Builder 的 NEXT_ACTION 只作建议，不能自动发送。日常不复制多套版本目录，下游以 exact commit 冻结所消费版本；按需才导出 ZIP。

本次只改候选运行规则和生成投影，不迁移任何既有用例、不替其填写进度，不改变 A/B/C 业务方法或成熟度。目录名暂保留以兼容旧引用，使用时同时核对执行修订和 exact commit。

## 当前唯一活动版本

|Mission|当前完整候选|本轮补回的主体|
|---|---|---|
|A|[`market_process_modeling_contract_pro_candidate_v0_2/`](market_process_modeling_contract_pro_candidate_v0_2/README.md)|Feature 正面叙事、Feature→Action、方法／参数／模糊控制器、业务回看与状态、最低充分运行复杂度、正式产品资格、实现者探针|
|B|[`repo-aware-engineering-agent-candidate-v0.2/`](repo-aware-engineering-agent-candidate-v0.2/README.md)|把 A 的 Feature／Action／state／method／product 与 frozen RepoFact 编译成真实宿主 realization、最低充分表达、writer/readback/consumer 和可回开的 VCC|
|C|[`mission-c-host-implementation-system-candidate-v0.2/`](mission-c-host-implementation-system-candidate-v0.2/README.md)|把 Implementation Judgment 恢复为 normal path，加入四个实施前沿、主体优先、状态物理三分、method activation proof 和四类再判断|

三份 v0.2 均由锁定的 v0.1 原始 ZIP 生成，并完整承接父包中应沿用的内容；它们不是增量补丁，也不需要运行时再读取旧目录。旧版已移入 [`../archive/superseded_agent_candidates_20260904/`](../archive/superseded_agent_candidates_20260904/README.md)，只用于审计来源，禁止与当前版本混读。

构建来源、父包身份、输出成员数、校验结果，以及 Mission C 构建源的两处机械问题，统一记录在 [`refinement_wave_reports/20260904/INTEGRATION_REPORT.md`](refinement_wave_reports/20260904/INTEGRATION_REPORT.md)。

## 让 Pro 调整既有成果时的必读链

Pro 已经给出了“更新了什么”以及“旧成果怎样处理”的承重材料，不需要 Codex 临场发明业务判断：

1. 先读 [`refinement_wave_reports/20260904/00_ROUNDS_2_4_EXECUTIVE_CHANGE_REPORT.md`](refinement_wave_reports/20260904/00_ROUNDS_2_4_EXECUTIVE_CHANGE_REPORT.md)，确认 A/B/C/Overlay 的整体变化。
2. Mission A 读 [`provenance/V0_2_CHANGE_AND_EXISTING_ARTIFACT_EFFECT.md`](market_process_modeling_contract_pro_candidate_v0_2/provenance/V0_2_CHANGE_AND_EXISTING_ARTIFACT_EFFECT.md)，再按 [`operations/EXISTING_ARTIFACT_EFFECT_AND_RETROFIT_DECLARATION.md`](market_process_modeling_contract_pro_candidate_v0_2/operations/EXISTING_ARTIFACT_EFFECT_AND_RETROFIT_DECLARATION.md) 对旧工作地图／合同逐项给出 effect 和 disposition。
3. Mission B 读 [`90_provenance/V0_2_CHANGE_AND_EXISTING_ARTIFACT_EFFECT.md`](repo-aware-engineering-agent-candidate-v0.2/90_provenance/V0_2_CHANGE_AND_EXISTING_ARTIFACT_EFFECT.md)，判断旧工程产物需要 `KEEP`、定向重审、回补，还是因 A 的承重变化而 stale。
4. Mission C 读 [`audit_provenance/V0_2_CHANGE_AND_EXISTING_ARTIFACT_EFFECT.md`](mission-c-host-implementation-system-candidate-v0.2/audit_provenance/V0_2_CHANGE_AND_EXISTING_ARTIFACT_EFFECT.md)，判断旧实现、checkpoint 和 handoff 是否满足新的 normal-path Implementation Judgment。
5. 跨 Mission 的回压和 stale 传播，以 Overlay 的 [`06_A_B_C滚动交接_回压与既有产物影响_v0.3.md`](runtime_overlay_candidates/agent_owned_long_horizon_overlay_v0_3/06_A_B_C滚动交接_回压与既有产物影响_v0.3.md) 为准；快速 selector 可读 [`refinement_wave_reports/20260904/01_EXISTING_ARTIFACT_RETROFIT_AND_STALE_MAP.md`](refinement_wave_reports/20260904/01_EXISTING_ARTIFACT_RETROFIT_AND_STALE_MAP.md)。

这套材料没有预先宣布某个 U2／U3 旧产物一定错误。正确做法是把 current accepted artifact、其 parent/source 和当前候选交给相应 Mission 的 Pro，由 Pro 对每个承重单元作 `KEEP`、`REAUDIT_EXISTING`、`RETROFIT_EXISTING` 或 stale/rebase 判断；Codex只负责提供准确路径、原样传递结果和维护版本／状态记录。当前发布明确记录 `existing_artifacts_retrofitted: false`，所以“已有调整方法”不能误写成“旧成果已经调整完”。

## 长程覆层与 Project runtime 投影

- [`runtime_overlay_candidates/`](runtime_overlay_candidates/README.md)：当前唯一入口为 `agent_owned_long_horizon_overlay_v0_3`。它只管理多轮收敛、版本／权限锁、A→B→C 交接、回压、既有产物影响和 continuation，不是第四个 Agent。
- [`runtime_release_candidates/`](runtime_release_candidates/README.md)：保存 A/B/C v0.2 与 Overlay v0.3 的自包含 Project runtime release，以及 `project_upload_core`／`project_upload_optional` 上传视图。它是生成投影，不是 Agent common core 的第二份真源。
- [`refinement_wave_reports/`](refinement_wave_reports/README.md)：保存跨 Agent 的实质变化、既有成果回修／stale 图、验证边界和集成回执；这些报告不取得业务或代码写权。

## 现有 U2／U3 Pilot 的边界

[`../pilot_cases/network-dynamic-ceps-factory-u2-u3/`](../pilot_cases/network-dynamic-ceps-factory-u2-u3/README.md) 中现存的是针对旧组合形成、尚未执行的 task-local 绑定快照。它没有按 A/B/C v0.2＋Overlay v0.3 重新实例化，也没有执行 existing-artifact retrofit，当前身份是 `STALE_PENDING_REBASE`。

不得把旧 U2／U3 绑定与新候选静默拼接，也不得把本次修订包解释为已经修好了既有 U2／U3 产物。后续必须由 Pro 先按上述必读链处理兼容性，再形成新的 task-local packet。

## 当前测试与晋级边界

至少仍需完成：

1. 为 A、B、C 的主要 runtime profile 分别做 fresh-agent pilot，确认入口、按需读取、停止条件和产物合同；
2. 运行各包声明的 Harness、anti-gold、缺口和 fail-closed 场景，而不只检查文件、YAML 或 SHA；
3. 使用 EAW 之外的场景验证 common core 与 case profile 的边界；
4. 验证 A→B→C 的真实 handoff、回压与 stale 传播，不让下游静默补裁上游业务合同；
5. 对真实实现、编译、production、writer、official readback、consumer 和缺陷恢复形成证据；
6. 经 Owner 明确接受后，再决定晋级、拆分、合并或安装形态。

在这些条件完成前，任何包内静态 `PASS`、ZIP 完整性、hash 一致或一次长程成功，都不得改写成“Agent 已验证可运行”。

## Mission B 的语言现状

Mission B v0.2 新增的承重内容已有中文，但继承的顶层 README、front door、runtime profile、Owner surface、repo router 和 maintenance 控制层仍以英文为主。本轮没有完成中文化。后续翻译必须形成新的候选修订并重建 manifest/hash；不得直接改写已经校验的 v0.2 成员后仍声称原校验有效。
