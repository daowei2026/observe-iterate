请作为现有 `observe-iterate` V2 主控，**正式启动 EAW P1 Build 单 Feature 的统计驱动合理性闭环 Run**。

本次只启动 **Build**，不启动 AttackSegment、Absorb、WALL 合理性或其它 Feature Run。本消息是一个新 Run 的初始 Owner GO，后续不再设置 Owner 业务审批节点。

### 一、Run 身份及采用来源

- `run_id`: `OI-EAW-P1-BUILD-STAT-20261124-01`
- `work_id`: `OI-EAW-P1-BUILD-STAT`
- `business_case_id`: `EAW-P1-BUILD`
- `execution_profile`: `CODEX_NATIVE_DIRECT`
- `post_start_owner_policy`: `AUTONOMOUS`

本次所有角色统一采用以下专业控制版本：

`daowei2026/observe-iterate@391adcd18bd2da82c13c01710980f41e01c7de25`

唯一正式业务任务输入：

`daowei2026/observe-iterate@391adcd18bd2da82c13c01710980f41e01c7de25:task-inputs/eaw-p1-build-stat-20261124/BUILD_RUN_INPUT.md`

主控 Skill：

`daowei2026/cgpterm@815c505c1cc3d965aaafa831d23c4c88368cb70a:.agents/skills/observe-iterate-longrun-v2-codex-native-controller/SKILL.md`

按锁定版本读取 `control/01_L0_统计驱动的单特征闭环.md`、相关专业 Skills、适用补充和 `longrun` 协议。业务目标、具体 Feature 和上游来源均以本次正式输入为准，不重复定义专业方法。

### 二、Feature 和正式实例

目标 Feature：`BuildAssembler`，EAW P1 Build 活动。

TIS 源码基线：

`daowei2026/tis@179016111ed0394f92025313e46bd13534932a74`

原分支：`codex/wall-output-consistency-20261121`

该版本包含此前完成的 Wall Bug 修复，不能改用旧 Wall 实现。

正式实例：

- SOF：`TA_updto20240229_DBA`
- 品种：`rb`、`m`
- 时间：`2021-01-01` 至 `2021-12-31`
- Calendar：`night_end_at_2300`
- 参数：`BuildAssembler` 当前默认实例 `build-default`

必须实际核对代码加载、实例完整参数、运行数据和结果读回。只使用真实市场数据作为正式 X/G 证据。

### 三、工作区与运行角色

本 Run 指定工作区：

`/dwdhome/fy/BASE_E6_2`

启动前先核实工作区存在、realpath、真实代码版本、旧 Run 占用和共享结果写入状态。

此前 `OI-ABSORB-STAT-20261123-01` 也绑定过此工作区。如果已真实结束，可按事实核对并释放旧资源记录；如果仍有活跃操作或状态不明，不得覆盖旧成果或强制中断，只记录具体阻断。

本 Run 创建两个全新的 Codex 线程：

- manager：仅负责已采用 Workflow 的执行协调。
- executor:E1：直接完成专业 Skill 与必要工程操作。

两者必须是不同线程，均使用本 Run 工作区，不复用旧 Run thread。

`workers=[]`，不签发 Worker。

模型：`gpt-6.1-sol`，推理强度：`max`。通过实际 Codex App Server 核实。

本次使用的 Git 分支：

- TIS 修改分支：`codex/oi-eaw-p1-build-fix-20261124-01`
- observe-iterate 运行记录分支：`codex/oi-eaw-p1-build-stat-20261124-01`

只从指定 TIS commit 起步，不修改原 Wall 修复分支。

### 四、一次性工程授权

作为 Owner，我授权本 Run 在指定工作区完成 Build 的真实实例运行、全量统计、业务诊断、高置信 finding 闭环、必要回归和正式重跑。

**代码修改范围仅限 Build Feature 自身：**

- `hf/prel0/build_assembler.py`
- `hf/prel0/build_assembler_core.py`
- 直接相关测试
- 当前 Build 自身的参数与业务常量

禁止修改 Wall、F3/F4、Attack、Absorb、其他上游 Feature、公共处理模块、市场数据和无关 FRP 代码。

如果发现问题实际来自 Wall 或其他上游，只形成有据的 `UpstreamFinding`，说明原因、影响与恢复条件；不越权修复。

授权普通 Git commit/push 至上述指定分支，不授权 force push、破坏性清理、覆盖其他 Run 结果或扩大正式业务范围。

供 V2 从本次 Owner GO 原文提取的准确工程授权如下。`allowed_writes` 中逗号分隔的项目作为各自独立写面：
```bash
operation=eaw-build-execute-and-profile execution_context=/dwdhome/fy/BASE_E6_2 allowed_writes=/dwdhome/fy/BASE_E6_2
operation=eaw-build-repair-and-publish execution_context=/dwdhome/fy/BASE_E6_2 allowed_writes=/dwdhome/fy/BASE_E6_2,daowei2026/tis:codex/oi-eaw-p1-build-fix-20261124-01,daowei2026/observe-iterate:codex/oi-eaw-p1-build-stat-20261124-01
operation=eaw-build-controller-run-records execution_context=github:daowei2026/observe-iterate:codex/oi-eaw-p1-build-stat-20261124-01 allowed_writes=longrun/runs/OI-EAW-P1-BUILD-STAT-20261124-01/,longrun/controller/RUN_REGISTRY.json
operation=eaw-build-controller-chat-archive execution_context=github:daowei2026/observe-iterate:feat/statistics-driven-feature-closure-v0.3-20261122 allowed_writes=longrun/controller/chats/
```

主控按 V2 校验真实授权、D 委派范围、工作区及 Codex 物理审批设置。不要把 Owner 的任务授权误认为操作系统或 Codex 已经自动批准了所有命令。

### 五、业务执行和自主推进

本次按现行 L0 执行：

首轮 U 理解 Build → X 正式实例运行 → G 全量统计与高置信问题发现。

有待处理 finding 时执行 D，定位最早责任逻辑，必要时修改 Build，并进入后续轮次重新运行和统计。

不新增 Q 独立节点、实现修改 Skill 或额外专业 Gate；具体专业方法和完成条件遵循原 Skill。

Wall 使用当前修复后 TIS 版本的准确技术上游 artifact。若当前实例尚未物化，可以按既定实现和参数在本工作区物化并验证，但不得修改 Wall 的业务逻辑。旧 WALL 合理性 Run 没有全面通过，不能把技术上游可用解释为 Wall 已完成合理性验收。

启动后的正常诊断、授权范围内修改、测试、正式重跑和完成判断都由 AI 自主推进，不再请求 Owner 确认。超出初始范围或真实权限不足时，记录局部阻断与恢复条件，不伪造成功。

Manager 应维护两个文件：

- `BUSINESS_PROGRESS.md`：Build 的业务进展、发现与解决问题的过程、有效成果和下一业务动作。
- `TASK_PROGRESS.md`：Run 状态、版本、真实 C/D、产物引用与恢复条件。

达到本轮完成条件后形成 Build 的 `FeatureReleaseGate` 和必要的 `UpstreamReleasePackage`。主控 Chat 自身的归档按已采用 cgpterm Skill 执行，不归档 manager/executor Chat。

### 六、正式启动与第一次回报

现在开始执行合法启动：先核实工作区及旧 Run 状态、代码版本、Wall 技术前置、实际 Git 权限和 Codex 审批设置；条件满足则注册本 Run、创建新的 manager/executor 线程并正式派达工作。

首次向我回报：

1. Build Run 是否已经真实注册和派发；
2. 实际采用的 commit、工作区与运行记录链接；
3. 当前执行到 U、X、G、D 的哪一步；
4. exact Wall 技术前置是否具备；
5. 具体未完成事项、阻断原因及下一合法动作。

不要把 GO 文件发布、模型调用成功或 GitHub 上出现记录当作 Feature 已运行或业务验收通过。
