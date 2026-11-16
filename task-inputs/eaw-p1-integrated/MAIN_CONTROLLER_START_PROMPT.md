# 新 Run 主控启动提示词｜OI-EAW-P1-20261116-01

> 此文件是待 Owner 发送给 cgpterm 主控的**拟用启动原文**；文件存在本身**不构成已发送的 GO 或实际 Run**。发送前可直接复制下列正文。源码、数据 ZIP 及两端共享路径的可取得性，主控必须在真实现场查证。

---

请作为 `daowei2026/observe-iterate` V2 多 Run 主控，**正式启动一个全新的 EAW P1 观察准备与业务合理性分析 Run**。本次仅采用下列明确的 BusinessTaskInput、运行身份、Owner 指定资源和权限，不迁移、复用或覆盖任何旧 Run 的工作状态、C/D/W、业务 Gate、进度或分析结论。

## 1. 本 Run 身份及业务目标

- `business_case_id=EAW-P1`
- `work_id=OI-EAW-P1`
- `run_id=OI-EAW-P1-20261116-01`
- 业务目标：EAW P1 相互关联的特征**作为一个整体**开展真实观察材料准备及业务合理性分析；不是仅针对 `EawP1WallLifecycleFrp`。正式纳入的 Feature/实际场景和能回答的问题，由专业 Pro 根据本 Run 的原始需求/设计与脚本真实数据定向核定，不强行把没有证据的产品归入本轮。
- 设计预期：**直接阅读** [《01.04.01 EAW叙事一个小范围完整的部分-preL0细节》§1.1.2「墙的基本思想」](https://github.com/daowei2026/feature-refinement-implementation-agent-evolution/blob/8d58ddd3392a3e67ef5ba44adf2c4cd0c9077f9f/candidate_gold_cases/eaw/preL0_source_materials_20261102/%E5%8E%9F%E6%96%87%E5%BF%AB%E7%85%A7/mquant/ssot/eaw/01.04.01%20EAW%E5%8F%99%E4%BA%8B%E4%B8%80%E4%B8%AA%E5%B0%8F%E8%8C%83%E5%9B%B4%E5%AE%8C%E6%95%B4%E7%9A%84%E9%83%A8%E5%88%86-preL0%E7%BB%86%E8%8A%82.md#112-%E5%A2%99%E7%9A%84%E5%9F%BA%E6%9C%AC%E6%80%9D%E6%83%B3)，并按专业 Skill 查其适用与 P1 其它产品的原设计来源。**不要让 AI 重写一段并冒充 Owner 正式设计预期**。
- 需求/工程：`daowei2026/feature-refinement-implementation-agent-evolution@8d58ddd3392a3e67ef5ba44adf2c4cd0c9077f9f:candidate_gold_cases/eaw/taskpacks_and_checkpoints/`；原业务资料同仓 `candidate_gold_cases/eaw/preL0_source_materials_20261102/`。
- 本次业务输入：`daowei2026/observe-iterate@3e3b258c2aac6b4f949dffce69886ef23180ff3f:task-inputs/eaw-p1-integrated/README.md`；源码/数据文件及共享路径清单：`daowei2026/observe-iterate@3e3b258c2aac6b4f949dffce69886ef23180ff3f:task-inputs/eaw-p1-integrated/CAEGRAPH_INPUT_MANIFEST.md`。**CAEGraph 原始脚本已直接入库，禁止再用脚本 ZIP 作为交付入口**：`daowei2026/observe-iterate@0082ae1e79aaa7ca0a15cadf2a89d799aa6c7fa6:task-inputs/eaw-p1-integrated/caegraph-review/` 下的 `caegraph_definitions.py`、`snapshot_data.py`、`run.py`、`README.md` 四个普通文件；已按原上传文件逐一核对字节数及来源哈希。主控/Worker 应直接读取这些仓库源码文件，并在 Worker 实际运行环境检查依赖。
- Owner 的现成真实数据文件名：**`caegraph-data-30tick.zip`**（在 Owner 所说的 Sources 中）。本任务会话已经取得原始附件并核对 16,654,307 字节、SHA-256=`73e7c5f289d7b25f08f11cffda7315ad2dad3f8c323715425afdd485e15c4233`、ZIP CRC、`data/manifest.json`（12 条 evidence_features、442 项资产，涉及 Wall/Build/Attack/Absorb/方向大成交等图证据）。**这些不是 cgpterm 或 Linux Worker 已经收到该文件的证明**；主控仍须核真实 Project/Sources 文件访问、转存及 Worker 实际取得的哈希和业务用途。

## 2. 本 Run 的现成图和数据特例

- 本轮**不重新研究 CAEGraph 绘图设计、图层组织或开发另一套画图方法**。优先用 Owner 提供的现成脚本及已生成的真实数据，核验质量、身份、处理阶段后，**按已有 M/R 控制面尽快交给合理性分析**。
- **脚本在 GitHub 中直接是四个原始文件**：`task-inputs/eaw-p1-integrated/caegraph-review/`。另行从 Owner Sources 实际取得 **`caegraph-data-30tick.zip` 数据包**，将其中 `data/` 放在运行目录 `caegraph-review/data/`，或使用 `--data-dir` 指向正确数据目录。优先不重算上游；执行入口、运行环境及依赖按已入库原始 `README.md` 核实（其中提及的原始脚本 ZIP 只属于上传来源说明，本 Run 交付无需它）。
- 该脚本和实际数据包的元信息覆盖钢铁板块 `rb/hc/i` 的长期、30min/1min/5s 和 30 个 Tick 图，现有 `manifest.json` 具名 Wall/Build/Attack/Absorb/方向大成交的绘图证据；**仍不能仅凭图证据推出已覆盖 EAW P1 全部正式输出、完整处理链或业务预期适用性**。由专业 Pro 核数据字段/时间/输出阶段是否满足本轮设计预期；如有缺口，只具名登记并执行合法的最小补证。**不得未经 Owner 允许改变 EAW P1 业务目标**。
- 本轮可跳过完整入口/已有图资产重新盘点；对已提供脚本和数据形成的合格成果无需机械重做设计工作。仍须由有权专业 Pro 对影响后继的取舍、材料实际质量、预期冻结和正式证据对照按既有 Skill/Control 接受，不把略过记作专业步骤已完成，也不把人工构造输入当成正式真实市场证据。

## 3. 采用来源和角色

- 主控 Skill：`daowei2026/cgpterm@034da33b774d7e3db50fcdda219a64d4ed0281be:.agents/skills/observe-iterate-longrun-v2-controller/SKILL.md`。本 Run 按该提交的多 Run 主控接线使用。
- 业务 Control、长程 V2 协议、观察材料准备与合理性分析 Skills：`daowei2026/observe-iterate@3e3b258c2aac6b4f949dffce69886ef23180ff3f` 中 `control/01～06`、`longrun/contracts/LONGRUN_PROTOCOL_V2.md`、`longrun/contracts/MULTI_RUN_CONTROLLER.md`、`skills/` 及 `longrun/professional/`。所有 D/W 使用该 Run 正式 GO 采用的精确版本，不因其他 Run 后续更新自动变化。
- 管理 Pro 与执行 Pro：ChatGPT Project **`细节叙事生成_金标`**，相互独立的角色聊天，推理档位 **`Pro`**；不提前探测或擅改模型名称。
- Owner 授权主控为**本新 Run**在该 Project 中合法新建/绑定各角色的独立 manager/executor ChatGPT 聊天，并为本 Run 在指定 Linux 工作区新建/绑定专用 Worker 线程；须按现有物理聊天/线程 Skill 实际检查和回执，不复制旧 Run 的会话身份，也不以逻辑角色字符串代替实际绑定。
- Worker：本 Run 专用 Linux Worker，目标配置 **`GPT-6.1 Sol Max`**，实际物理 thread 与授权在首次使用时核实。
- 本 Run 的业务 Control 仍由 manager Pro 全面负责：实际节点输入输出、业务 Gate、后继、补证、合理性分析以及完成全景；主控只管理物理派发、回执、机械对账、跨 Run 资源、已决定动作和 GitHub 原件，不代替专业取舍。

## 4. 工作区、跨端共享和文件传递

- **Owner 指定 Linux 工作区：`/dwdhome/fy/BASE_E6_2`**，必须核真实存在、realpath、实际 Worker cwd 和权限。与仍在运行的其他 Run 发生相同路径、父子目录或共享写目标冲突时，先处理该冲突；主控不得替 Owner 换工作区。
- Owner 指明 Windows MCP Server 端共享根为 **`H:\fy`**，Linux 端为 **`/dwdhome/fy`**。这是 Owner 提供的候选映射，不是已验证事实。首次使用前，请在两端用同一相对路径的测试文件进行双向读取和 SHA-256 对照。若不通，具名阻断跨端传输，不把文件同步成功作为已知事实。
- 本 Run **建议的交换目录**：Linux `/dwdhome/fy/BASE_E6_2/.runtime/observe-iterate/OI-EAW-P1-20261116-01/handoff/`，Windows `H:\fy\BASE_E6_2\.runtime\observe-iterate\OI-EAW-P1-20261116-01\handoff\`。不得对该路径以外的位置假定写权限。
- 已有数据优先从 Owner 的 Sources 读取/按真实可用通道放入本 Run 环境；**不要求把完整 20～30 MB 数据再提交进 Git**。
- 将来由 Worker 新生成的数据：按需导出并打包 ZIP，通过已授权的 MCP/手机 ChatGPT 聊天附件传到**原执行 Pro 的已绑定聊天**；主控先确认该已存在聊天的附件接线与真正发送成功，不擅自新建替代聊天，不绕过执行 Pro 直接让 manager 专业消费。GitHub 只存 V2 正式 C/D/W/Return、管理判断、进度、必要文本报告、数据清单/哈希及可追溯位置。

## 5. 本 Run 一次性工具授权（Owner 本条启动原文）

授予该 Run 在指定现场为正常 EAW P1 观察取材、现成脚本安全运行/读取、必要局部处理、数据与专业报告交接开展普通非破坏性操作的权限；不授权修改无关业务源码、危险 Git 操作、覆盖其他 Run 成果或越过物理访问控制：

```text
operation=eaw-p1-observation-work execution_context=linux:/dwdhome/fy/BASE_E6_2 allowed_writes=/dwdhome/fy/BASE_E6_2
operation=run-record-publish execution_context=github:daowei2026/observe-iterate:runs/OI-EAW-P1-20261116-01 allowed_writes=longrun/runs/OI-EAW-P1-20261116-01
```

为本 Run 正常数据交接，另授权在**经真实验证的前述独立交换目录**内通过 Windows MCP Server 读写本 Run 文件，并利用现有受控 ChatGPT 附件传输方式，将本 Run 需要给执行 Pro 的 ZIP 发送到**该 Run 已绑定的原执行人聊天**。不得把此描述解释成对所有 `H:\fy` 文件的任意写入或覆盖许可。若当前 V2 schema/物理工具的授权类别还需具体字段，由主控按真实 Owner 原文核验并报告精确缺口，不能伪造 `authority_quote`。

## 6. 正式动作与回报

本次是**新的 Run GO**，不是恢复 `OI-EAW-WALL-20261116-01`。主控先核全局 Registry 和旧 Run 的 BASE 占用、真实身份未重复、上述采用来源与写权限、两端共享目录/数据通道实际能力；依采用 V2 协议创建该 Run 独立 `OWNER_START.md`、`RUN_BINDING.json`、`RUN_RESOURCE_BINDING.json` 和 Registry，然后派本 Run manager Pro，后续按原控制面专业推进，不要求另跑测试 Run。

如 GitHub 中某份原始脚本文件在当前实际通道不可读取，或 Sources 数据 ZIP 暂不能取得，不假报已取得；可继续合法的独立文档级工作，把具体缺项、受影响工作和最小恢复条件记录到本 Run，而不是伪造 `DATA_READY`。本 Run 普通专业步骤、Gate 和补证不逐项向 Owner 求批准。

首次回报只需说明：新 Run 是否已实际注册与派发、准确 commit/路径、Windows↔Linux 共享验证结果、**GitHub 四份原始 CAEGraph 脚本文件**和 **Sources 的数据 ZIP** 是否可在执行现场读取、当前受阻项及准确下一合法动作。不要把 GO 发布、手机消息送达、Worker 真运行和专业验收混成一项完成事实。
