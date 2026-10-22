# 具体特征观察：准备到真实运行的衔接说明

**此文件仅说明衔接，不是 Owner 授权或启动提示词。** 不新建默认 run_id，不代管理签发工作地图，不预填 Intake 或 ADOPTED Binding。

## 1. 新的专业内容

- 专业目标：professional/feature_observation/00_PURPOSE_AND_FOUR_WORKS.md。
- 基本输出：professional/feature_observation/01_OUTPUT_BASE_FORMAT.md。
- 工作细节：professional/feature_observation/02_WORK_DETAILS.md。
- 旧知识复用：professional/feature_observation/03_REUSE_FROM_V2.md。
- aidata 实际使用：professional/feature_observation/04_AIDATA_USE.md。

四项专业工作是可往返的业务活动，不按四个阶段依次签收。U2/U3 仅按当前具名特征需要读取。

## 1.1 相关仓库与工作区：各司其职

CYF 的仓库说明是可参考的**组织方式**，不表示本任务需要在某个 Git 仓库“开 chat”，也不把 CYF 的写面或工作区照搬过来：

| 仓库 | 用途及本任务边界 |
| --- | --- |
| [`cgpterm` 的 CYF Skill 分支](https://github.com/daowei2026/cgpterm/tree/cyf-integration-from-20260924) | CYF 的 ChatGPT Terminal 手机操作 Skill 来源；操作端使用本次实际采用且可用的版本，不因参考链接擅改当前已装 Skill。 |
| [`feature-refinement-implementation-agent-evolution/agent_evolution/agent_candidates`](https://github.com/daowei2026/feature-refinement-implementation-agent-evolution/tree/main/agent_evolution/agent_candidates) | CYF 长程专业 Agent 的材料；其需求/工程细化成果一般进入这个协调仓。本次 `BI-01` 的专业方法、任务地图及分析成果仍归 `observe-iterate` 的有权路径。 |
| [`tis`](https://github.com/daowei2026/tis)、[`frp`](https://github.com/daowei2026/frp) | 具体特征的 Python 侧接口、FRP 计算及实现仓；按目标特征需要读取。改代码需明确技术工单和写权，不因做观察就自动修改。 |
| [`aidata`](https://github.com/daowei2026/aidata) | 本任务制图和同范围数据的工具仓。实际使用前先读 [aidata README](https://github.com/daowei2026/aidata/blob/main/README.md)，再按需要查配置合同和[真实示例](https://github.com/daowei2026/aidata/blob/main/examples/microstructure_review.py)；详细使用见[04](../../professional/feature_observation/04_AIDATA_USE.md)。 |
| [`observe-iterate`](https://github.com/daowei2026/observe-iterate) | 本任务专业方法、长程运行材料和实际业务成果的归属仓。按本次有权分支、路径、版本回交。 |

CYF 本地 Codex 对话开在个人工作区的 `mquant` 目录，只是方便跨目录查代码。**对话工作目录不等于 Git 仓库、任务身份或代码写权**；本次应以实际可访问的工作区和具名仓库源、结果路径为准，不照搬其本机路径。

## 2. 准备 3：修改后再审查

当前完成新方法文档与入口修改后，审查实际改动：
- 专业总目标、工作内容、成果表达是否一致；旧 S1–S3、固定 ZIP、完整 U2/U3 任务要求是否被误继承；
- 角色与 Router/Coordinator modes 是否仍为同一专业目标提供入口；是否错误地以旧 run 的 Owner GO、Binding、Workmap 或已接收成果替代新授权；
- 针对**实际选定特征和运行环境**，已知/高概率会使夜间执行无法推进的重要工具、取数、展示或交付依赖是否已有处理方案与必要验证；
- 发现确定问题则修正；当前没有依据的专业问题留给真实观察和后续迭代，不要求提前穷举。

准备 3 的静态审查、已处理问题和需要现场验证的条件已具名记录在[准备 3 审查记录](FEATURE_OBSERVATION_PREP_REVIEW_20261021.md)。静态检查不冒充真实运行验收。

## 3. 真正开始新长程运行时

1. Owner 另行明确新的 GO、任务范围和相应 run 身份；锁定专业仓、控制仓与实际特征实现/数据的版本与读取方式。
2. 按 runtime 既有协议建立真实管理任务/地图、具体特征与需要做的工作、准确 source_refs、Binding/Intake、角色接收者与后继；不能使用旧 BI-01-V2-02 的已采用配置。
3. 管理 Pro 按四项可往返专业工作安排，而不是使用旧 S1/S2/S3 的强制划分；Worker 根据有权技术工单实际使用 aidata。
4. 操作端在真实身份、准确 payload、前置条件和 Gate 成立后才发送，保存真实回交并依法续作。未满足条件时反馈准确缺项，不能自签 Owner GO。
5. 现有手机操作、Workmap、QUESTION_WORK_RETURN、ROLE_RETURN、Git 提交及备用运输能力优先沿用既有通用机制；本文件不重建平台。
6. **新 run 机械入口的已知限制：**当前 `runtime/tools/bi01_run_gate.py` 仍含旧 `BI-01-V2-02` 的固定 run 路径、记录身份和消息标记，不能直接拿旧检查通过来证明新 run 合法。新 run 身份确定后需按必要最小范围适配相关调用及测试，实际通过有权 Gate 再派发；无法完成时报告阻断，不能跳过检查、借用旧 Binding 或复用旧 run ID。此处不预设新 run ID。


新任务的非活动模板位于 [feature_observation/templates/](feature_observation/templates/)；必须在新 Owner GO 后填成具名的新 run、实际特征、管理地图、当前任务、Binding 与 Intake，模板中 `<NEW_RUN_ID>` 不能用于真实派发。`BI01_V2_RUN_GUIDE.md` 与 `runtime/operations/v2/templates/` 保存的原 V2-02 具体运行内容只作历史参考，不能沿用旧专业职责、数据或已采用资格。
