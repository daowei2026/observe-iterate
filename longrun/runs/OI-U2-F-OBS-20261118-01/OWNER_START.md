# Owner GO｜启动 F 单特征观察材料准备新 Run

请使用 `daowei2026/cgpterm@5461c6e51e73d011028afd8b41a0c5c340541df5` 中的 `.agents/skills/observe-iterate-longrun-v2-controller/SKILL.md`，正式启动本次新 Run。

**本消息是 Owner 正式 GO，不是要求重新制定方案。** 请在现有长程执行机制和真实授权范围内实际注册、派发并推进任务。

## 1. Run 身份与来源

- `work_id`：`OI-U2-F-OBS`
- `business_case_id`：`U2-FQV-F`
- `run_id`：`OI-U2-F-OBS-20261118-01`
- 运行记录分支：`runs/OI-U2-F-OBS-20261118-01`
- Linux 工作区：`/BASE_E6_2_copy`
- 业务仓正式采用版本：`daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288`

本次唯一业务输入原件：

`daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:task-inputs/u2-fqv-observation/F_OBSERVATION_RUN_INPUT.md`

请完整读取并原样采用这份输入的目标、特征实例、源码版本和范围边界。该文件此前标记为草案，本次 Owner GO 明确将上述精确版本作为正式运行输入。

不自行补充新的业务目标、观察位置、展示方案或其他专业判断。

## 2. 本次执行范围

本 Run 只做 `CommonPriceTurnGroupCandidatesFrp`（F）的观察材料准备。

完整执行当前采用版本中 `control/02_L1_观察材料准备流程.md` 规定的 A～E 五个 Skill。

构造特征实例时，按输入原件指定的 `make_features(...)` 入口，只以返回的 `f` 为本次观察对象。

Q、V 虽然共用构造入口，但不纳入本次任务。本 Run 不开展合理性分析，不把历史成果当成已完成的 A～E 产物，也不执行输入文件明确排除的全历史 producer 重跑。

本次以 E Skill 完成观察材料交付为任务终点，不自动进入合理性分析。

## 3. 两类 Chat 的运行方式

采用本次正式版本的：

- 多层 Workflow 运行协调 Chat（V2 `manager`）
- Skill 执行 Chat（V2 `executor`）

运行协调 Chat 按已经定义好的 Workflow 调用 Skill，并持续维护整个任务的 `TASK_PROGRESS`、当前工作、版本依赖、在途状态及合法后继。

**每次默认派发一个 Skill 工作。** 不允许运行协调 Chat 在 D 委派中另加专业执行约束、专业方法、业务预期、Worker 处理规则或额外验收条件。

Skill 执行 Chat 自己读取和执行指定 Skill 的完整原始文件及其内部 Workflow，专业完成判断和 Worker 返回处理完全依对应 Skill。

先执行 A；A 完成后，B/C 可以根据实际独立性和执行资源顺序或并行开展。允许按需增加第二个 Skill 执行 Chat，不要求为每个 Skill 单独创建 Chat。

D 消费当前有效的 A/B/C 产物后执行，随后进入 E。单个 Skill 一次调用做不完时，按 V2 接续原 D 和原工作项。

## 4. 项目与模型

两类 Chat 均使用 ChatGPT Project：

`细节叙事生成_金标`

正式发送前分别确认：

- 模型：`GPT-5.6 Sol`
- 推理强度：`Pro`

模型不匹配时，按照当前 cgpterm 模型设置 Skill 正式切换并回读，不把以前手动设置过视为本次已确认。

Worker 的目标配置按当前已采用主控来源中的 `GPT-6.1 Sol Max` 处理，实际派发前核对。

## 5. 本次运行授权与工作区

Owner 指定 `/BASE_E6_2_copy` 为本 Run 的 Linux 工作区。不得自行替换成旧的 `/dwdhome/fy/BASE_E6_2` 或其他 Run 工作区。

我授权本 Run 在既有 V2 机制内执行注册、创建或绑定本 Run 所需 Chat、正式 Skill 调用与合法接续，并在如下范围内写入运行记录和执行产物：

**运行记录写入：**
```ini
operation=run_record_write
execution_context=daowei2026/observe-iterate@runs/OI-U2-F-OBS-20261118-01
allowed_writes=longrun/runs/OI-U2-F-OBS-20261118-01/**
```

**Run 注册索引更新：**
```ini
operation=run_registry_update
execution_context=daowei2026/observe-iterate@feat/observe-iterate-multirun-controller-v1-20261116
allowed_writes=longrun/controller/RUN_REGISTRY.json
```

**CAEGraph 运行及 Skill 允许的机械修复：**
```ini
operation=caegraph_run_and_repair
execution_context=/BASE_E6_2_copy
allowed_writes=/BASE_E6_2_copy/**
```

**CAEGraph 正式图数据导出：**
```ini
operation=caegraph_data_export
execution_context=/BASE_E6_2_copy
allowed_writes=/BASE_E6_2_copy/**
```

以上为 Owner 对本 Run 的操作授权原文。主控应据实际工单按 V2 形成精确授权记录，不扩权；这些操作授权不替代专业 Skill 的方法和判断。

正式操作前，按 V2 核实工作区真实存在、权限、与其他 Run 的占用关系和实际物理绑定。不额外创建与本次专业目标无关的环境准备任务。

## 6. 实际启动与后续推进

请按已采用的 V2 协议完成本 Run 的正式注册、Binding、必要的物理 Chat 绑定和首次 C 调用。

注册及调用身份必须基于真实执行事实，不能把准备好的文件当成已经发送的调用。

**首先实际派发 A Skill，不要仅提交启动计划便停止。**

此后根据 Workflow、Skill 原生结果及已核实的运行状态继续推进 B/C、D、E；正常的 Skill 工作和接续不逐项向 Owner 申请批准。

确实遇到权限缺失、输入冲突、无法满足专业 Skill 条件或物理调用阻断时，记录实际原因、受影响范围及恢复入口。其他合法的独立工作继续。

首次回报请说明实际采用的版本、Run 注册结果、两类 Chat 的真实绑定、A 是否已实际派发，以及当前下一合法动作。所有状态必须区分“已准备”“已发送”“已回交”和“专业 Skill 已完成”。


---

# Owner 工作区更正

Owner 对当前 Run 的原文回复：

> 将本 Run 路径更正为 /dwdhome/fy/BASE_E6_2_copy

本更正应用于本 Run 的 Linux 工作区、现场 execution_context 和该目录下的 allowed_writes；原 GO 原样保留。


## 主控采用记录（事实，非 Owner 原文）

- 主控来源：daowei2026/cgpterm@5461c6e51e73d011028afd8b41a0c5c340541df5:.agents/skills/observe-iterate-longrun-v2-controller/SKILL.md
- 专业 Workflow/Skill/指南与唯一业务输入采用 daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288。
- Owner 原 GO 与路径更正分别保留；实际工作区为 /dwdhome/fy/BASE_E6_2_copy。
- 当前尚无真实 C/D/W；Chat 物理绑定与发送待登记，不将此文件视为已发送。
