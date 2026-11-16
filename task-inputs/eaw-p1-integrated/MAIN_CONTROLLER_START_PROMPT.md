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
- 本次输入及上传脚本清单：`daowei2026/observe-iterate@468100bab5f446f224d8ae7f8e4d89fcff003ef6:task-inputs/eaw-p1-integrated/README.md` 和 `...:task-inputs/eaw-p1-integrated/CAEGRAPH_INPUT_MANIFEST.md`。其中脚本原件文件名 `caegraph-scripts.zip`，需要**实际取得原 ZIP 字节**，不能只读 manifest 就声称已拿到脚本。
- Owner 的现成真实数据文件名：**`caegraph-data-30tick.zip`**（在 Owner 所说的 Sources 中）；先核清准确 Project/来源和实际访问能力，并以包内 `data/manifest.json`、字段/时间/参数等核对用途，不从文件名推测 EAW 产品覆盖。

## 2. 本 Run 的现成图和数据特例

- 本轮**不重新研究 CAEGraph 绘图设计、图层组织或开发另一套画图方法**。优先用 Owner 提供的现成脚本及已生成的真实数据，核验质量、身份、处理阶段后，**按已有 M/R 控制面尽快交给合理性分析**。
- `caegraph-scripts.zip` 包内是 `caegraph-review/caegraph_definitions.py`、`snapshot_data.py`、`run.py`、`README.md`；数据 `caegraph-data-30tick.zip` 应解压出并列 `caegraph-review/data/`。优先不重算上游；运行入口及依赖按脚本 README。
- 该脚本静态文档描述钢铁板块 `rb/hc/i` 的长期、30min/1min/5s 和 Tick 图；**这些不能自动证明已覆盖 EAW P1 全体业务输出**。请把脚本与数据 `manifest.json` 的真实范围核对交给专业 Pro，若不匹配，只具名记录不适用及缺什么；**不要未经 Owner 允许改掉 EAW P1 业务目标，也不要用无关图声称完成 EAW P1 观察**。
- 本轮可跳过完整入口/已有图资产重新盘点；对已提供脚本和数据形成的合格成果无需机械重做设计工作。仍须由有权专业 Pro 对影响后继的取舍、材料实际质量、预期冻结和正式证据对照按既有 Skill/Control 接受，不把略过记作专业步骤已完成，也不把人工构造输入当成正式真实市场证据。

## 3. 采用来源和角色

- 主控 Skill：`daowei2026/cgpterm@034da33b774d7e3db50fcdda219a64d4ed0281be:.agents/skills/observe-iterate-longrun-v2-controller/SKILL.md`。本 Run 按该提交的多 Run 主控接线使用。
- 业务 Control、长程 V2 协议、观察材料准备与合理性分析 Skills：`daowei2026/observe-iterate@468100bab5f446f224d8ae7f8e4d89fcff003ef6` 中 `control/01～06`、`longrun/contracts/LONGRUN_PROTOCOL_V2.md`、`longrun/contracts/MULTI_RUN_CONTROLLER.md`、`skills/` 及 `longrun/professional/`。所有 D/W 使用该 Run 正式 GO 采用的精确版本，不因其他 Run 后续更新自动变化。
- 管理 Pro 与执行 Pro：ChatGPT Project **`细节叙事生成_金标`**，相互独立的角色聊天，推理档位 **`Pro`**；不提前探测或擅改模型名称。
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

如脚本原件或 Sources 数据包暂不能实际取得，不假报已取得；可继续合法的独立文档级工作，把具体缺项、受影响工作和最小恢复条件记录到本 Run，而不是伪造 `DATA_READY`。本 Run 普通专业步骤、Gate 和补证不逐项向 Owner 求批准。

首次回报只需说明：新 Run 是否已实际注册与派发、准确 commit/路径、Windows↔Linux 共享验证结果、CAEGraph 脚本和数据 ZIP 是否可实际读取、当前受阻项及准确下一合法动作。不要把 GO 发布、手机消息送达、Worker 真运行和专业验收混成一项完成事实。
