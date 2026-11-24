# EAW P1 Build / Attack / Absorb｜三 Run 并行启动主控提示词（待 Owner 发送）

> **这是可复制发送的 GO 草案，不是已真实发送的 GO。** 发送前须在真实 Linux 主机准备下面三个互不重叠的工作区。若任何目录尚不存在，主控必须如实报告，不得擅自创建或以旧 BASE 代替。
>
> 三个独立 Run 共享业务输入和修复后的 Wall 技术上游，但**不能共用同一个可写目录**。这遵守现有多 Run 协议，不改造主控工作模式。
>
> 本提示词的 Control 和五份业务输入精确采用 `observe-iterate@8e76ac7e33bea17ad4ef1792173986a5e123c198`（三个 Feature 仅可修改自身的约束已包含）。本提示词文件是在该输入版本之后单独提交的 GO 草案；发送时必须保留下面的精确采用版本，不能让浮动 branch HEAD 自动替换。

---

请作为现有 `observe-iterate` V2 主控，**正式启动 EAW P1 Build、AttackSegment、Absorb 三个相互独立、允许并行的统计驱动 Feature 闭环 Run**。本消息为三个新 Run 的统一初始 Owner GO 与一次性授权；不是接续旧 Absorb/WALL Run。

## 一、专业来源及边界

三类角色（controller／各 Run manager／各 Run executor）共同采用：

```text
observe-iterate: daowei2026/observe-iterate@8e76ac7e33bea17ad4ef1792173986a5e123c198
controller-skill: daowei2026/cgpterm@815c505c1cc3d965aaafa831d23c4c88368cb70a:.agents/skills/observe-iterate-longrun-v2-codex-native-controller/SKILL.md
business-control: control/01_L0_统计驱动的单特征闭环.md
common-input: task-inputs/eaw-p1-build-attack-absorb-20261124/COMMON_INPUT.md
TIS: daowei2026/tis@179016111ed0394f92025313e46bd13534932a74
FRP P1 DSU reference: daowei2026/frp@cac6c912dd65a14acbd591ca57e0afd8ddb4ef13
```

必须按精确 commit 读 Control、Skill、实践补充、专业角色指南、任务输入和原始业务来源；不得恢复旧 V0.2 观察 A～E，也不自动要求 CAEGraph。当前业务输入精确文件：

- Build：`task-inputs/eaw-p1-build-attack-absorb-20261124/BUILD_RUN_INPUT.md`
- AttackSegment：`task-inputs/eaw-p1-build-attack-absorb-20261124/ATTACK_RUN_INPUT.md`
- Absorb：`task-inputs/eaw-p1-build-attack-absorb-20261124/ABSORB_RUN_INPUT.md`

本次三个目标严格是 `BuildAssembler`、`AttackFlowAssembler`、`AbsorbAssembler` 的**实际正式代码与输出**；对应 P1 FRP wrapper/DSU 是业务合同和必要读回的依据，不将其它 FRP 产品或下游 Feature 自动算入三个 Run 的独立交付。

三个 Run 的正式 SOF、品种、期间、Calendar 统一锁定为：`TA_updto20240229_DBA`、`rb/m`、`2021-01-01..2021-12-31`、`night_end_at_2300`，当前 TIS 代码的各自默认正式参数。运行前由 executor 保存并核实序列化实例身份和实际加载模块；不能将旧代码、旧 cache、人工构造输入或诊断局部窗口冒充正式全年数据。

## 二、三个 Run、资源与输出分支

本次 Run 独立拥有 manager、executor、状态和 Gate，不共用物理 threadId 或在途 C/D：

| 目标 | run_id | Owner 准备的工作区 | 运行记录 Git 分支 | 目标 TIS 修正 Git 分支 |
|---|---|---|---|---|
| Build | `OI-EAW-P1-BUILD-STAT-20261124-01` | `/dwdhome/fy/EAW_P1_PARALLEL/build` | `codex/oi-eaw-p1-build-stat-20261124-01` | `codex/oi-eaw-p1-build-fix-20261124-01` |
| AttackSegment | `OI-EAW-P1-ATTACK-STAT-20261124-01` | `/dwdhome/fy/EAW_P1_PARALLEL/attack` | `codex/oi-eaw-p1-attack-stat-20261124-01` | `codex/oi-eaw-p1-attack-fix-20261124-01` |
| Absorb | `OI-EAW-P1-ABSORB-STAT-20261124-01` | `/dwdhome/fy/EAW_P1_PARALLEL/absorb` | `codex/oi-eaw-p1-absorb-stat-20261124-01` | `codex/oi-eaw-p1-absorb-fix-20261124-01` |

`work_id` 分别为 `OI-EAW-P1-BUILD-STAT`、`OI-EAW-P1-ATTACK-STAT`、`OI-EAW-P1-ABSORB-STAT`；`business_case_id` 为 `EAW-P1-BUILD`、`EAW-P1-ATTACKSEGMENT`、`EAW-P1-ABSORB`。

这里的三个目录应优先是**同一个基础 TIS 仓库的三个轻量 Git worktree**：共用 Git 对象存储、安装环境、只读基础数据及核实后的 Wall artifact，**不需要复制三套完整 TIS 工程和数据**；但各 Run 的实际可写 Git checkout／运行记录必须隔离。上述目录只是待真实 Linux 核实的三个路径，不是已经存在的现场。主控首次注册前必须按 V2 核目录、realpath、实际加载的 TIS 版本、工作树和只读数据挂载；必须检查与旧未结束的 `OI-ABSORB-STAT-20261123-01` 等 Run 是否争用路径／共享 DB。若路径不存在，不自动 mkdir/clone/symlink 或借旧工作区；只将该 Run 保留为待准备，其他具备全部条件的 Run 可继续。

三个 Run 从**同一个已核实** `tis@179016...` 提交创建本 Run 专用开发分支；修正只写自己的 TIS 分支，不直接推送 `codex/wall-output-consistency-20261121`。本轮**禁止修改任何上游 Feature 的代码／参数／业务规则**（包括 Wall、F3/F4、FRP 相关上游产品及共用处理模块）；若定位出上游问题只登记具名 finding 和对本 Run 的影响，不能擅改上游，也不得误称当前 Feature 已修复。不改历史 FRP 基线，不跨 Run 覆盖彼此的源码结果。observe-iterate 的运行记录各提交到本 Run 自己的分支，不能让三个 Run 并行修改本任务输入分支。

## 三、共用 Wall 的前置处理

本次**允许**三个 Feature 使用已修复的 exact Wall 作为技术上游，尽管旧 WALL 合理性 Run 未完成 FeatureReleaseGate；必须在每个 Feature 的来源和限制中如实保留，不得虚构 WALL 已全面合理。

三条 Run 分别可以先并行完成 U、准备业务证据与实例核查。但在真正 X 前：

1. 先核 `WallAssembler` 是否已有匹配当前 TIS commit、默认参数、rb/m 全年、日历的完整正式 `wall_lifecycle` receipt、state trace 与读回；旧版结果不算。
2. 若没有合格 Wall artifact，指定**Build Run 的 executor** 为本次共同 Wall 技术前置的唯一生产者（不新建 WALL 专业 Run），先完成真实物化／验证。其他两线等待这个**具体共享写面**，仍可继续独立 U／文档核查。
3. 只有在真实运行环境确定读到**同一份** Wall receipt 与数据产物且共享目标处于只读状态后，才允许三个目标 Feature 的正式 X 并行。
4. TIS 的各目标 `_impl` 仍会调用 `self.P.wall.run()`；主控要核实它们是否只是合法读回，不能把相同 full_dir 的首次创建交给三个并发进程碰运气。共享 DBA、缓存、QT、F4 和结果目录若存在冲突，先按真实写面隔离或让受影响操作串行，不能因为逻辑上无业务依赖就伪称物理写入安全。
5. 只允许真实市场正式输入，不能用人工构造的受控数据包替代 X/G；临时诊断必须标 `DIAGNOSTIC_ONLY`。

这不把 Wall 的生产或 F4 的独立运行算作三个目标 Feature 的额外完成 Gate。允许为绑定既定参数和代码完成必要技术物化，但不允许利用物化过程改变上游 Feature 实现或业务含义。

## 四、执行 profile 和一次性授权

```yaml
execution_profile: CODEX_NATIVE_DIRECT
post_start_owner_policy: AUTONOMOUS
model: gpt-6.1-sol
reasoning_effort: max
roles_each_run:
  manager: fresh Codex thread
  executor_E1: fresh different Codex thread
  workers: []
```

主控依实际 App Server 回读上述模型、强度、身份、cwd、状态与审批沙箱政策；不能因 GO 书面给了工程权限，就把需要人工批准的物理命令虚构成自动批准成功。若现有审批设置使本 Run 无法自主执行常规 Git 提交／运行，必须在实际派达前记录准确技术阻断，不让三个 Run 反复进入未知提交等待。不会在运行过程中向 Owner 询问。

本次我作为 Owner **一次性授权**三个 Run 在各自独立工作区内真实运行、查看源码、统计、定位 finding、**仅修改各自目标 Feature 的专属实现、参数及业务常量**、跑回归、正式重跑、形成结果，以及对下列**具名且仅具名的分支**进行普通 commit/push；允许 Build Run 单独生产本批 exact Wall 技术前置。每个直接操作需按 V2 `grants` 与 D 的 `permitted_operations/allowed_writes` 子集机械核验，**不授权修改 Wall、F3/F4、其他上游 Feature、公共处理器或其业务规则／参数／输出合同**，也不授权覆盖其它 Run、改无关代码、force push、删除生产数据或扩大业务对象／时间范围。

为 V2 `authority_quote`，以下是**本次初始 GO 中 Owner 实际授权原文**，主控按每条原文提取 `operation / execution_context / allowed_writes / authority_quote`；其中 CSV 项按独立 `allowed_writes` 元素登记。不要用自己编造的权限描述代替：

```text
operation=eaw-build-run-profile execution_context=/dwdhome/fy/EAW_P1_PARALLEL/build allowed_writes=/dwdhome/fy/EAW_P1_PARALLEL/build
operation=eaw-build-repair-and-publish execution_context=/dwdhome/fy/EAW_P1_PARALLEL/build allowed_writes=/dwdhome/fy/EAW_P1_PARALLEL/build,daowei2026/tis:codex/oi-eaw-p1-build-fix-20261124-01,daowei2026/observe-iterate:codex/oi-eaw-p1-build-stat-20261124-01
operation=eaw-attack-run-profile execution_context=/dwdhome/fy/EAW_P1_PARALLEL/attack allowed_writes=/dwdhome/fy/EAW_P1_PARALLEL/attack
operation=eaw-attack-repair-and-publish execution_context=/dwdhome/fy/EAW_P1_PARALLEL/attack allowed_writes=/dwdhome/fy/EAW_P1_PARALLEL/attack,daowei2026/tis:codex/oi-eaw-p1-attack-fix-20261124-01,daowei2026/observe-iterate:codex/oi-eaw-p1-attack-stat-20261124-01
operation=eaw-absorb-run-profile execution_context=/dwdhome/fy/EAW_P1_PARALLEL/absorb allowed_writes=/dwdhome/fy/EAW_P1_PARALLEL/absorb
operation=eaw-absorb-repair-and-publish execution_context=/dwdhome/fy/EAW_P1_PARALLEL/absorb allowed_writes=/dwdhome/fy/EAW_P1_PARALLEL/absorb,daowei2026/tis:codex/oi-eaw-p1-absorb-fix-20261124-01,daowei2026/observe-iterate:codex/oi-eaw-p1-absorb-stat-20261124-01
operation=eaw-p1-controller-chat-archive execution_context=github:daowei2026/observe-iterate:feat/statistics-driven-feature-closure-v0.3-20261122 allowed_writes=longrun/controller/chats/
```

三线独立管理成果、Finding 和 Release。重要回交时，manager 维护 `business_control/BUSINESS_PROGRESS.md`（业务进展）和 `TASK_PROGRESS.md`（运行状态），并向 GitHub 保存准确引用。主控仅负责 V2 物理调度、真实回执、版本／资源核验和跨 Run 路由；不得改写业务判断，也不自行创造 Owner 审批点。主控自身 Chat 的自动归档按本 GO `eaw-p1-controller-chat-archive` 授权及 cgpterm Skill 执行，仅在实际 Git 工作树、分支、真实线程和推送权限核验通过时，提交到现行控制分支 `longrun/controller/chats/`；它**不是**三个 executor 的直接操作 grant，不得混入它们的 `executor_direct_grants`。不导出 manager/executor Chat；归档失败仅形成欠账，不影响独立专业工作。

## 五、实际启动、继续及首轮回报

请先核三个工作区实际存在、realpath 不重叠、旧 Run 工作区占用、现行 TIS/FRP 模块、Wall artifact 的代码／参数／scope 身份、Codex 物理创建和审批政策、输出及共享缓存写面。不能把文档已提交或本 GO 已发送等同于已真实启动。满足条件的 Run 及时注册、分别新建 manager + executor，在同一批调度中允许合法并行；未满足的 Run 保留具名阻断，不因此阻断别的 Run。

三个 Run 的专业 Workflow 为首轮 U→X→G，按真实 finding 进入 D、必要修正和后续轮次；不要求逐问题先问 Owner，不要求每个 finding 单独全量重跑，不预设固定统计结论。每线达到本轮深度后自主形成 FeatureReleaseGate 和必要的 UpstreamReleasePackage，历史证据只作为对照。

**首次回报给我**只需一个简表：三个 Run 是否真实注册／派达、独立工作区和实际加载 commit、Wall 技术前置状态、各自当前业务节点、最新 BUSINESS_PROGRESS、具体阻断和下一合法动作。不要用模型调用成功或 GitHub 文件存在冒充 Feature 已运行／验收。
