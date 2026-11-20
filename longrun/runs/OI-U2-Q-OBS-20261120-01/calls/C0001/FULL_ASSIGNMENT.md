# Owner GO｜正式启动 Q 单特征观察材料准备 Run

[OI-U2-Q-OBS-20261120-01-C0001]
invocation_token=5bbb52abe3414a5f9bc2bfd39c7a560a

你是本 Run 唯一的多层 Workflow 运行协调 Chat（V2 manager）。这是 Owner 正式 GO 后的首次实际调用。请按已采用 Workflow 开始工作，维护 TASK_PROGRESS，并首先签发一次 A Skill 工作 D001，返回给主控实际派发独立 executor。

## 任务身份和真实现状

- run_id：OI-U2-Q-OBS-20261120-01
- work_id：OI-U2-Q-OBS；business_case_id：U2-FQV-Q
- 本次调用：C0001；manager：chatgpt:OI-U2-Q-OBS-20261120-01:manager
- Skill executor：chatgpt:OI-U2-Q-OBS-20261120-01:executor:E1，独立 Chat，由主控按 D 实际创建/绑定。
- Worker：codex:OI-U2-Q-OBS-20261120-01:worker:W1，仅逻辑预留；尚无物理Worker/工单，首次合法 W 前由主控创建Q专用Codex Chat。
- Owner已确认本Run工作区 /dwdhome/fy/BASE_E6_2_copy 和本Run记录、注册索引、运行/机械修复及导出权限；准确Binding以下列原件为准。
- F Run 已由 Owner 在独立 Codex Chat 直接完成 E（DATA_READY），本Run不重开F，也不把F阶段产物当作Q阶段已完成。Q自己的A～E现在均未执行。
- 本Run仅观察 make_features(...) 返回的 q；f 只是构造q的必要上游。V不启动，不全历史producer，不合理性分析；以Q的E交付为终点。
- 所有新业务产物和运行记录仅写 longrun/runs/OI-U2-Q-OBS-20261120-01/ 下；不写F Run路径。

## 已采用来源（必须读取原件）

- daowei2026/observe-iterate@1fb666ce9851138edf757b18ecba63d025eed240:longrun/runs/OI-U2-Q-OBS-20261120-01/OWNER_START.md
- daowei2026/observe-iterate@e5a6902148afc5deb2c8268b96856892e3a976a4:longrun/runs/OI-U2-Q-OBS-20261120-01/RUN_BINDING.json
- daowei2026/observe-iterate@e5a6902148afc5deb2c8268b96856892e3a976a4:longrun/runs/OI-U2-Q-OBS-20261120-01/RUN_RESOURCE_BINDING.json
- daowei2026/observe-iterate@40630e6d97ec28d2b519edf3ddea268527c760ee:longrun/controller/RUN_REGISTRY.json
- daowei2026/observe-iterate@3efb2719a66a2fcc1bb86f33b7b0a2258f9bfbf7:task-inputs/u2-fqv-observation/Q_OBSERVATION_RUN_INPUT.md
- daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:longrun/professional/PRO_MANAGER_GUIDE.md
- daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:longrun/professional/PRO_EXECUTOR_GUIDE.md
- daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:longrun/contracts/LONGRUN_PROTOCOL_V2.md
- daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:longrun/contracts/longrun_schema_v2.json
- daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:control/02_L1_观察材料准备流程.md
- daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:control/06_业务完成全景与更新协议.md
- daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:skills/observation-material-preparation/feature-occurrence-understanding/SKILL.md
- daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:task-inputs/u2-fqv-observation/实例运行脚本.py
- daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:task-inputs/u2-fqv-observation/无二义性需求和实现文件.md

主控职责版本仍为 cgpterm@d4ba9f8711f5d20633f789cacfe41c1aa8ba686a；你无需采用主控的物理操作职责。A～E Workflow、Skill、角色指南和协议固定 f7e8ff43；唯一Q业务输入固定3efb2719。输入中的工作区由本次 Owner 明确采用 /dwdhome/fy/BASE_E6_2_copy；其余业务目标、实例、代码版本及边界原样采用。F直接E的现有uplot例外没有自动授予Q。

## 本次调用工作

完整读取 manager 指南、已采用Workflow和Q输入。建立并维护本Run business_control/TASK_PROGRESS.md，记录工作、Skill阶段、执行Chat、版本依赖、未开始/在途/已回交/已完成及合法后继。按既定A→B/C→D→E关系启动A。请发布 delegations/D001/DELEGATION.md 与 DELEGATION.json，并在本次 manager PRO_RETURN.json 的 issued_delegation_refs 中签认这份D。每份D默认一项Skill工作；内部步骤不拆成多D。

D仅传任务/工作身份、A完整原始Skill及适用文件的准确来源、当前有效上游输入、回交对象；专业执行和完成判断由executor依据原始Skill负责。manager不要另加专业方法、业务预期、Worker处理规则、执行约束或第二轮专业Gate，不设计Worker工单。真实操作权限按Binding中既有grants传递，不扩权。

Git引用顺序按V2：先发布D，再发布引用D的manager Return；D仅记录issuer_call_id=C0001，不倒引未来Return。所有正式ref使用40位commit。Return依longrun-professional-return/v2，role=manager，sender为本Run manager；尚未完成或缺失如实表达。不要把已准备的D称为executor已收到，也不要把本次manager工作称为A已完成。

本次正式回交：calls/C0001/MANAGER_REPORT.md、delegations/D001/DELEGATION.md/json、business_control/TASK_PROGRESS.md、calls/C0001/PRO_RETURN.json。若工具确实不能发布，保持原文完整交回并说明实际状态，不能虚构Git提交。

最后一条实际提交完成业务交付后，commit message 包含 turn complete [OI-U2-Q-OBS-20261120-01-C0001] invocation_token=5bbb52abe3414a5f9bc2bfd39c7a560a。最终回复给出原报告/Return/TaskProgress/D准确refs，真正结尾同样保留本轮marker与完整token。

## 唯一Q业务输入原文（除Owner工作区更正外不改写）

# Q｜观察材料准备 Run 输入

> **用途**：本文件只提供本次 Q 单特征观察材料准备任务的用例输入和范围边界。多层 Workflow 运行协调 Chat 的角色 Prompt、调度方法和 Skill Chat 调用协议由对应正式文件提供，不在这里重复定义。
>
> **状态**：输入草案。正式启动时，应由协调 Chat 将本次实际采用的 `observe-iterate` 精确 commit 写入运行记录；不得只引用分支浮动 HEAD。

## 1. 本次任务范围

本次只针对以下目标特征，完整执行现行观察材料准备外层 Workflow：

```text
A 特征事件级 occurrence 理解
→ B 观察位置准备 / C 展示方式准备
→ D CAEGraph 定义集成
→ E CAEGraph 执行／运行
```

目标特征：

```text
PostTurnGroupDirectionalOrganizationFrp
业务简称：Q｜转折后成员组的方向组织
```

本次明确不包括：

- `CommonPriceTurnGroupCandidatesFrp`（F）的独立观察材料准备 Workflow；
- `CommonTurnGroupValidityFrp`（V）；
- 合理性分析 Workflow；
- S、U2、U3 及其他后续特征；
- 参数标定、收益判断或资金配置；
- 未经另行明确授权的全历史 producer 重跑。

Q 的实例构造需要准确的 F 实例作为上游输入。F 可以按原始构造关系被创建、引用或读取，但只作为 Q 的必要上游依赖；不得因此把 F 当成本次目标特征，也不得把 F 的独立 A～E 产物计入本次完成范围。

虽然现有 Python 构造入口会返回 `f, q, v`，本次被观察实例只有其中的 `q`。V 不得因为共用构造入口而被扩入本次 A～E 的输入、产物或完成范围。

## 2. 外层输入

### 2.1 特征名称

```text
PostTurnGroupDirectionalOrganizationFrp
```

### 2.2 特征代码版本

| 层次 | 精确来源 | 本次用途 |
|---|---|---|
| FRP | `daowei2026/frp@67711c492da909ed0f044f357beb278abf7fc71c`，`src/Frp/Instance/ISL/Opportunity/` | Q 的业务实现 |
| TIS | `daowei2026/tis@2f460d663d821cf2ba25555eda13e78b697d0767:frp/fqv_kline_example.py` | 正常 Python 构造入口及 Q 对 F 的实例接线 |
| 完整配置 | `daowei2026/feature-refinement-implementation-agent-evolution@2d3f56a7944c44b2a1c441c15eebf9659835136b:agent_evolution/pilot_cases/network-dynamic-ceps-factory-u2-u3/configurations/fqv-kline-rb-hc-i.json` | 同批实例的完整参数和上下文；不得另造 JSON Runner |
| CAEGraph / uplot | `daowei2026/uplot@0a4fcd54059782572a3f7e82fad041121e8c65ad` | C、D、E 使用的锁定实现 |
| 观察材料 Workflow | `daowei2026/observe-iterate@<正式启动时锁定的精确 commit>` | 本次 A～E Control、Skills 和角色文件 |

### 2.3 特征实例

本次不在本文件中重新抄写 SOF、Calendar、品种和完整参数；直接读取以下原件：

1. **实例定义与现有用法参考**  
   `daowei2026/observe-iterate@<正式启动时锁定的精确 commit>:task-inputs/u2-fqv-observation/实例运行脚本.py`

2. **原始 Python 构造入口**  
   `daowei2026/tis@2f460d663d821cf2ba25555eda13e78b697d0767:frp/fqv_kline_example.py`

3. **完整展开配置**  
   `daowei2026/feature-refinement-implementation-agent-evolution@2d3f56a7944c44b2a1c441c15eebf9659835136b:agent_evolution/pilot_cases/network-dynamic-ceps-factory-u2-u3/configurations/fqv-kline-rb-hc-i.json`

本次实例选择规则：

```text
调用 make_features(...) 后，只选择返回值中的第二个对象 q；
q 的类型应为 PostTurnGroupDirectionalOrganizationFrp。
```

原始构造关系为：

```text
先构造准确的 f，
再由 PostTurnGroupDirectionalOrganizationFrp.from_formation(f, ...) 构造 q。
```

因此，本次允许构造或读取准确的 `f` 作为 Q 的上游依赖，但不能把 F 当作本次观察目标，也不能把 F 的输出冒充 Q 的主输出。

`实例运行脚本.py` 同时包含 F、Q、V 的检查和读取能力，只作为准确实例参数与既有用法的原件。本次若直接执行该脚本会连带处理 F、V，应改为沿原始构造入口选择 `q`，或使用不改变 Q 业务参数和 F→Q 接线的最小任务内调用；不得把 F、V 结果记为本次任务产物。

## 3. 运行工作区

```text
/BASE_E6_2_copy
```

本文件不新增环境预检、安装检查或数据挂载检查任务；这些运行条件由 Owner 已准备的现场和正式协调流程负责。

## 4. Workflow 执行边界

### 4.1 完整执行，不预先替代阶段工作

- A、B、C、D、E 均须按本次正式采用版本的 Control 和 Skill 自己形成产物；
- 不把历史报告、历史 CSV、既有结果包或过去聊天结论视为本 Run 已完成的 A～E 阶段产物；
- 现有资料可以在某一 Skill 实际需要时作为来源或代码／实例定位线索，但必须由该 Skill 自己判断、引用并形成当前阶段产物。

### 4.2 上游 F 的使用边界

- A 可以读取 Q 对 F 的真实输入合同、引用关系和必要 F 字段，以理解 Q 的输入 occurrence；
- D、E 可以按准确实例接线消费 F，以形成和运行 Q 的 CAEGraph；
- 不执行 F 的独立 A～E Workflow；
- 不要求形成 F 的独立观察材料交付；
- 不把 F 的历史结果当作 Q 当前阶段产物。

### 4.3 不预先指定 B 的产物

本任务不额外指定品种集、时间范围或样例位置。B 按当前 B Skill 和本次 Q 实例形成自己的观察位置产物。

### 4.4 不预先指定 C 的样例或展示方案

本任务不提供：

- 预选 occurrence；
- 预选展示日期；
- 预期主图／附图；
- 预期 HTML；
- 已接受的 CAEGraph 展示方案。

C 按 A 产物、锁定版本 CAEGraph 使用资料和 C Skill 自己完成 C1、C2、C3。

### 4.5 不进入合理性分析

E 交付观察材料后，本次任务结束。是否启动合理性分析由后续独立任务决定。

## 5. 可用索引资料及边界

### 5.1 需求与实现索引

```text
task-inputs/u2-fqv-observation/无二义性需求和实现文件.md
```

用途：定位 Q 的需求、源码、F→Q 实例关系、正式读取接口和现有资料。

边界：

- 不能替代 A 对 Q 当前代码和实例的 occurrence 分析；
- 不能替代 B 的观察位置产物；
- 不能替代 C 的展示设计；
- 不能替代 D 的完整定义；
- 不能替代 E 的真实运行、核图和取数结果。

### 5.2 实例运行脚本

```text
task-inputs/u2-fqv-observation/实例运行脚本.py
```

用途：提供本批准确实例上下文、参数、构造与既有公开读取方式。

边界：

- 其默认读取覆盖 F、Q、V，不等于本次任务范围覆盖三者；
- 本次只以 `q` 为观察目标，`f` 仅作为必要上游依赖；
- 脚本存在或历史读取成功，不等于本次 A～E 已完成；
- 本文件不授权 `--mode rerun --allow-full-period-rerun`。

## 6. 本次输入结论

```yaml
任务类型: 观察材料准备
目标特征: PostTurnGroupDirectionalOrganizationFrp
目标实例选择: make_features(...) 返回值中的 q
必要上游依赖: f，仅用于准确构造和运行 q
执行范围: A / B / C / D / E
合理性分析: 不执行
F: 非目标特征，仅作为 Q 的必要上游依赖
V: 不在范围
工作区: /BASE_E6_2_copy
B额外位置输入: 无
C额外样例或展示输入: 无
历史A-E产物预接受: 否
协调Chat Prompt: 使用其他正式文件，不在本输入中定义
```
