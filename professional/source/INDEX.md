> **V1 历史索引**：本目录 I1–I6 来源是旧版本的提取记录，V2 新 run 的专业方法以 [`professional/v2/`](../v2/README.md) 为准。本文件不得被用作 V2 活动阶段合同。

# 00—08 专业 Agent 内容提取索引

本目录只搬入 `U2U3首轮业务观察实例上下文_20261010/00—08` 中直接约束观察迭代专业 Agent 的内容。

不搬入：

- Network Dynamic、CEPS、FRP 等其它业务资料；
- 两份 ZIP、行情、CSV、运行结果本体；
- BI-01 既有运行工作面 `CURRENT/PROGRESS/ROUTES/ops/returns/tasks`；
- 仅用于手机操作、发送、等待和 GitHub 机械运输的说明；
- 未在 00—08 中形成的专业方法。

提取文件均保留来源仓库、分支、原路径和源 blob SHA。正文只采用原材料中的专业角色、阶段、Gate、观察、审查、Worker 工单与回交要求；为便于运行系统读取，按职责重组，但不把缺失内容补造成正式方法。

| 原文件 | 提取目标 | 提取的专业内容 | 未搬入内容 |
|---|---|---|---|
| `00_长程任务总意图与六个子意图.md` | `00_AGENT_CHARTER_AND_STAGE_CONTRACT.md` | 总意图；I1— I6 Input/Output/Gate；管理/执行/Codex/Owner 分工 | BI-01 后续实例细节与业务资料索引 |
| `01_首轮实例及子意图1至3上下文.md` | `01_I1_I3_PROFESSIONAL_CONTRACT.md` | I1— I3 当前成果、G3 核查责任、I2/I3/I4 分流 | ZIP 文件清单、CSV 明细和大段 U2/U3 业务追溯 |
| `02_子意图4三类观察情形与挑战.md` | `02_I4_OBSERVATION_AND_CHALLENGE.md` | I4 Input/Output/G4；执行 Pro 方法；事实/发现/假设/设计问题区分；挑战要求 | 具体行情数值和 Case 业务结果正文 |
| `03_接续入口与就绪检查.md` | `03_STAGE_HANDOFF_AND_READINESS.md` | 阶段推进、Gate 交接、定向返回前序阶段、I4/G4 工作要求 | 具体 ZIP 运行核验细节与当前运行状态 |
| `04_贴近转折画图背景与Pro_Codex制图交接.md` | `04_PRO_WORKER_CODEX_HANDOFF.md` | 执行 Pro、Worker Codex、管理 Pro 职责；工单最低字段；技术回交和专业接收 | 历史画图系统、颜色、服务、路径和具体数据说明 |
| `05_管理Pro与执行Pro职责_Gate接收和交接.md` | `05_ROLE_GATE_AND_HANDOFF_CONTRACT.md` | 角色权限、G1—G6 接收责任、Pro→Pro 交付、Gate 决定正文、最小闭环 | 当前实例 ZIP 状态与首次运行历史 |
| `06_管理Pro启动提示词与执行Pro派发要求.md` | `06_MANAGEMENT_AND_DISPATCH_REQUIREMENTS.md` | 管理 Pro 首次/后续调用条件、必须交付、执行 Pro 任务形成边界 | 当前聊天、手机设置、ZIP 路径和历史发送状态 |
| `07_操作Codex与GitHub运行交接最小约定.md` | `07_PROFESSIONAL_OPERATION_BOUNDARY.md` | 管理/执行/Worker/操作端的职责边界；UI完成、业务结果、Gate 三种状态不得混同 | 手机 UI、网络、等待、durable-result 和 GitHub 机械细节 |
| `08_操作Codex首次接入与机械接续提示词.md` | 无独立专业正文 | 仅作为操作端模板来源；专业任务仍回到 00—06 | 全文暂不搬入 |

## 精确来源

- repository: `daowei2026/complex-systems-vocabulary`
- ref: `fix/work-order-boundary-part-a-20260909`
- root: `docs/network-dynamic-ceps-factory/capital-management-purpose/discuss-materials/U2U3首轮业务观察实例上下文_20261010/`

| 文件 | blob SHA |
|---|---|
| 00 | `d77c14e1564c2c751699073853887cfab9ce3ae6` |
| 01 | `5bd81ef05dce01ac36704085d71221c958907b93` |
| 02 | `728e0f7e702cc70a0876a0bd1bbbe692ebb5edf6` |
| 03 | `df2872883d14f3c97f66029c61ed625e2694b30c` |
| 04 | `e390f32dca0bb4ccddee9eda5b729ec1b9818fbb` |
| 05 | `4116c27df86a63e40ba7e19b03e971d603df1a07` |
| 06 | `a5cea5c715997a051ebefc4daeb85449ad5ac748` |
| 07 | `41ae31a862272a074a2343a336090c8e111b1a50` |
| 08 | `f146fce892e842e72888e1ad9b2d1f95d670de36` |
