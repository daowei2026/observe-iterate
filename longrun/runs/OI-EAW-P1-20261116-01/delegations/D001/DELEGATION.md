# D001｜EAW P1 整体材料核定与最小业务预期形成

## 0. 正式身份

- `run_id`：`OI-EAW-P1-20261116-01`
- `delegation_id`：`D001`
- `issuer_call_id`：`C0001`
- `issuer`：`chatgpt:OI-EAW-P1-20261116-01:manager`
- `recipient`：`chatgpt:OI-EAW-P1-20261116-01:executor:E1`
- `return_to`：`chatgpt:OI-EAW-P1-20261116-01:manager`
- `work_item_id`：`WI-D001-P1-INTEGRATED-INTAKE`
- M 阶段实例：`M-P1-INTEGRATED-001`
- R 阶段实例：`R-P1-EXPECTATION-001`
- R 轮次：`AR-P1-001`

本 D 只有在主控真实派发并核实独立 executor 物理接收后才算开始。文件存在本身不等于已送达或已执行。

## 1. 当前业务问题

### Q-EAW-P1-COVERAGE-001

Owner 提供的 CAEGraph 脚本和 `caegraph-data-30tick.zip`，实际覆盖哪些 EAW P1 产品、实质处理阶段、对象、尺度、字段与场景？哪些材料可直接进入后续合理性分析，哪些只能作为局部图证据，哪些仍缺最小补证？

### Q-EAW-P1-EXPECTATION-001

针对本轮实际能够纳入的 P1 产品，如何从 Owner 原始设计、业务推导和现有实现分别形成可检验预期与场景，并避免：

- 把 Wall 的设计预期外推成全部 P1；
- 把候选需求包当成已获 Owner 逐项接受；
- 把代码行为当成业务应然；
- 把看到图或字段当成产品语义已完整成立。

本 D 为后续 `Q-EAW-P1-REASONABLENESS-001` 准备合格输入，但**不执行正式 R2 支持/反证对照**。

## 2. 所属 Workflow、专业节点及已接受上游结果

本 D 合并两组已具备共同上游输入、但必须分别交付和验收的工作：

### M｜观察材料准备

按固定版 `control/02_L1_观察材料准备流程.md` 的原专业步骤 1～7执行：

- 步骤 0 的完整重复资产盘点按 Owner 本轮特例跳过，记录为“Owner 指定跳过”，**不是完成**；
- 步骤 1：处理骨架与预期/实际输出核对；
- 步骤 2：材料取舍；
- 步骤 3：数据处理与观察方法；
- 步骤 4：现成脚本/图/数据复用和必要最小增量；
- 步骤 5：真实取得材料；
- 步骤 6：质量检查；
- 步骤 7：材料交接。

### R｜合理性分析

只执行 R0/R1 的事实准备和预期形成：

- `ExpectationRegister`
- `InputSuitabilityAssessment`
- `ScenarioExpectationSet`
- `OpenQuestions`
- 可供 manager 作 G-EXPECTATION-FREEZE 判断的候选冻结包/建议

允许将真实小样本用于字段、时间、场景理解，但必须标作探索；不得给出正式 `SUPPORTS/COUNTERS`。

### 已接受的上游结果

- H0 已由 manager 限域接受；详见：
  `daowei2026/observe-iterate@e5bbea4c62c9b2a3eba84989fb776cf9b77a3788:longrun/runs/OI-EAW-P1-20261116-01/business_control/decisions/MD-0001.md`
- 本次接管事实和边界：
  `daowei2026/observe-iterate@1b86e13374f3d6c520f4c29dfebd795d315ca9c2:longrun/runs/OI-EAW-P1-20261116-01/calls/C0001/MANAGER_REPORT.md`

尚未接受：H1 MATERIAL-HANDOFF、G-EXPECTATION-FREEZE、G-COMPARISON、任何合理性结论。

## 3. 必须亲自采用的固定来源

### 3.1 Owner GO、运行与方法

1. `daowei2026/observe-iterate@6a2d0abd34d44fd20fe7119035a8227e6b019625:longrun/runs/OI-EAW-P1-20261116-01/OWNER_START.md`
2. `daowei2026/observe-iterate@1a04ea440f395026491036d405d82e653a5fecbd:longrun/runs/OI-EAW-P1-20261116-01/RUN_BINDING.json`
3. `daowei2026/observe-iterate@1a04ea440f395026491036d405d82e653a5fecbd:longrun/runs/OI-EAW-P1-20261116-01/RUN_RESOURCE_BINDING.json`
4. 固定方法版本 `daowei2026/observe-iterate@7e240b650b6ba6274b0263e34f5b0616a9a8ff1c`：
   - `longrun/professional/PRO_EXECUTOR_GUIDE.md`
   - `control/02_L1_观察材料准备流程.md`
   - `skills/reasonableness-analysis/README.md`
   - `skills/reasonableness-analysis/business-expectation-derivation/SKILL.md`
   - 如需理解证据资格边界，再读 `business-evidence-comparison/SKILL.md`

### 3.2 业务输入、脚本与数据清单

1. `daowei2026/observe-iterate@f48beffe5057ac77154c636d04674a81cbd33aad:task-inputs/eaw-p1-integrated/README.md`
2. `daowei2026/observe-iterate@a360361011ece1bdfd253878a31e6a779cf98e8f:task-inputs/eaw-p1-integrated/CAEGRAPH_INPUT_MANIFEST.md`
3. 脚本原始 ZIP：
   `daowei2026/observe-iterate@e4909b2e57d6e6122979ae0c4e57fb946b18e2d3:task-inputs/eaw-p1-integrated/caegraph-scripts.zip`
4. 原文件展开副本：
   `daowei2026/observe-iterate@036f24f4a4b7ca898280d8ed58cbf9c0b3634744:task-inputs/eaw-p1-integrated/caegraph-review/`
5. 数据预期身份：`caegraph-data-30tick.zip`，16,654,307 字节，SHA-256 `73e7c5f289d7b25f08f11cffda7315ad2dad3f8c323715425afdd485e15c4233`。

你必须在自己的实际会话/操作现场独立确认是否能读取该数据原件，并复核字节数、SHA、ZIP CRC 与 manifest；不得把 manager 已读成功替代自己的读取事实。

### 3.3 Owner 原始业务设计

必须亲自阅读固定原文 §1.1.1、§1.1.2：

<https://github.com/daowei2026/feature-refinement-implementation-agent-evolution/blob/8d58ddd3392a3e67ef5ba44adf2c4cd0c9077f9f/candidate_gold_cases/eaw/preL0_source_materials_20261102/%E5%8E%9F%E6%96%87%E5%BF%AB%E7%85%A7/mquant/ssot/eaw/01.04.01%20EAW%E5%8F%99%E4%BA%8B%E4%B8%80%E4%B8%AA%E5%B0%8F%E8%8C%83%E5%9B%B4%E5%AE%8C%E6%95%B4%E7%9A%84%E9%83%A8%E5%88%86-preL0%E7%BB%86%E8%8A%82.md>

Wall 以外的 P1 产品如实际纳入，必须追到各自对应原设计/需求来源，不能由 Wall 的思想代写。

### 3.4 P1 候选产品合同

固定提交：`daowei2026/feature-refinement-implementation-agent-evolution@8d58ddd3392a3e67ef5ba44adf2c4cd0c9077f9f`

重点读取：

- `candidate_gold_cases/eaw/taskpacks_and_checkpoints/p1/EAW_P1_EXISTING_PREL0_BASE_PRODUCTS_AND_SPARSE_OCCURRENCE_V0_6_20260813/TASKPACK.md`
- 同包 `tables/P1_PRODUCT_AND_OCCURRENCE_MATRIX.csv`
- `AUTHORITY_BY_SUBTREE.yaml`、`SOURCE_BASIS_AND_LIMITS.md`
- 需要字段、时间、身份或实现边界时，定向读取同包 Wall/Build/Attack/Absorb/F3/F4/Formation/Barrier 文件和后续工程设计包，不做无目的全包复述。

必须显式记录候选包的 authority/status；`included_does_not_mean_owner_accepted`。

## 4. 需要完成的实质专业工作

## 4.1 P1 整体处理骨架

形成 `ProcessingSkeleton`，至少覆盖：

- 业务输入与受限数据前提；
- canonical Wall 与 Build / Attack / Absorb 的共用和解耦关系；
- Wall、Build、AttackSegment、Absorb、FormationEvidence、Barrier、F3、F4 的生产权和消费者；
- dense F3 与 sparse occurrence 的边界；
- actual/business time、closed/confirm time 及身份；
- 现成 CAEGraph 数据到底处于源业务输出、后处理、构图快照还是显示数据阶段；
- 哪些字段/状态是正式产品，哪些只是绘图或诊断字段；
- 当前脚本/数据与候选合同之间的一致、缺失、歧义和不可证明项。

不得只按 Python 函数数目或图层数目列“处理链”。

## 4.2 产品—证据—场景覆盖矩阵

对八类 P1 候选产品逐项记录：

```text
产品身份
权威来源/成熟度
业务主语
occurrence 形态
actual / confirm / end 时间
必需 payload
消费者
manifest / asset / 字段映射
可核验场景
当前证据状态
缺口对本轮判断的影响
```

当前证据状态至少区分：

- 已实际读取并可解释；
- 仅有 manifest 声明；
- 有图证据但不足以证明完整产品；
- 有数据但用途/时间/身份待核；
- 实际缺失；
- 不适用于本轮；
- Pending / history insufficient / valid empty / unavailable。

## 4.3 MaterialRequirementSet 与取舍

针对后续 Q3 的合理性分析，逐项标记：

- 必需；
- 有条件需要；
- 可选建议；
- 暂不准备。

每项说明“为什么看、缺它阻碍哪条预期、现有数据是否已经满足、如不满足的最小补法”。

不得为了覆盖全部 P1 名称而强制准备无消费者的图；也不得因已有图好看就将关键原值/中间状态降为可选。

## 4.4 复用现成脚本与真实取得材料

优先读取/复用现成数据和脚本，不重新设计图。

若当前会话已能直接读取数据包：

- 核实际哈希、CRC、manifest、timespans、对象、日历、字段和数据阶段；
- 只对本轮必要部分作定向读取；
- 可以不运行 Bokeh Server，只要本轮所需材料可由真实源/构图数据可靠取得并说明阶段。

若需要 Linux 环境验证依赖、`run.py --list`、`run.py --check`、现役库读取或导出：

- 可在本 D 范围内签 W；
- 不重算上游，除非真实缺口和脚本合同证明必须；
- 不修改无关源码；
- 任何新产物写入 `/dwdhome/fy/BASE_E6_2` 内本 Run 独立目录；
- 先检查输入文件实际哈希；
- 失败、部分、依赖缺失或高成本时准确停在当前动作并保留可用成果。

## 4.5 MaterialReview 与交接状态

对声明用途检查：

- 文件/数据真实存在；
- 对象与 DataBinding；
- 交易日历、Session、粒度和范围；
- actual / observed / closed / confirm 等时间语义；
- 参数、代码、数据版本；
- 空、缺失、Pending、历史不足；
- 源值、后处理值、构图值、显示值的阶段；
- 同一事件多图元不重复计为多事件；
- 图例/标题不替代参数和产品身份。

最终只能择实给出：`PLAN_READY / DATA_READY / PARTIAL_WITH_LIMITS / BLOCKED`，并列明可回答和不能回答的问题。

## 4.6 最小业务预期与场景

按预期推导 Skill 形成：

- `BusinessIntentStatement`
- `ExpectationRegister`
- `InputSuitabilityAssessment`（有效性、业务含义、当前目的适用性三层分开）
- `ScenarioExpectationSet`
- `OpenQuestions`
- 本轮冻结建议

每条预期必须标：

- `OWNER_EXPLICIT`
- `BUSINESS_INFERRED`
- `IMPLEMENTATION_DERIVED`

并包含适用条件、反例/证伪条件、所需证据、已知未知和来源。

至少建立能区分以下问题的场景：

1. 一堵墙从开始、加固/变化、受打/吸收、休眠到结束的生命周期；
2. Build、Attack、Absorb 与同一 canonical Wall 的关联和解耦；
3. 同向/反向、wall switch、direction switch 和 formal Barrier；
4. 完整 AttackSegment 的 business end 与 closed_at；
5. F4 tactical/structural 同 UTI 合并与 F3 dense/F4 sparse 边界；
6. 有事件、无事件、有效空、数据缺失、历史不足和 Pending；
7. 图证据出现但产品合同关键字段/时间/身份缺失的反例；
8. `rb/hc/i`、多尺度和 30 Tick 证据对 P1 业务问题的适用/不适用范围。

本 D 允许形成 `WORKING` 版本和“建议冻结”的精确集合。若你认为已经足够冻结，也必须把依据和已看证据截止写清，由 manager 下一轮作 G-EXPECTATION-FREEZE 接受；不得自行把冻结建议当作 Gate 已通过。

## 5. 最低证据、验证和交接条件

专业回交必须能够让 manager 分别判断：

1. M 各步骤成果是否真实完成、部分、缺证或不可得；
2. 哪些实际材料可进入 H1，具体用途和限制是什么；
3. R0/R1 产物是否来源分离、可证伪并具有场景；
4. 哪些预期具备冻结资格；
5. 正式 R2 需要的最小证据是否已齐；
6. 哪些缺口只阻断某个产品/场景，而不阻断其他独立工作；
7. 是否需要具名 `AdditionalEvidenceRequest`。

至少提供：

- 实际读取/运行清单；
- 文件大小、SHA-256、成员/记录数量；
- 关键 manifest / 表字段证据；
- 数据/时间/参数/代码版本；
- 产品—资产映射；
- 限制、替代解释和不能声称的结论；
- 如使用 Worker，逐张 W 的真实 Return 及 executor 接受意见。

## 6. Worker 下放边界

你可以零 W 完成本 D。只有确需真实工具操作时才签 W。

### 允许下放

- 在本 Run 工作区读取、复制、解压和哈希核验已授权输入；
- 读取 manifest、CSV/GZ/NPZ 元信息和必要样本；
- 运行现成脚本的 `--list` / `--check` 或不修改源码的最小只读检查；
- 导出本轮已由你确定的必要材料、日志和清单；
- 对脚本依赖、数据路径和输出数量作事实核验。

### 不允许下放

- 决定哪些业务材料“应该”纳入；
- 改写 Owner 设计或给预期定来源；
- 判断 P1 合理/不合理；
- 自行扩大到 P2/P3/P4；
- 调参、修改业务源码、重做画图方案；
- 绕过你直接向 manager 专业回交。

### W 的操作和写面

- `operation=eaw-p1-observation-work`
- `execution_context=linux:/dwdhome/fy/BASE_E6_2`
- `allowed_writes=/dwdhome/fy/BASE_E6_2`

首张 W 前由主控核本 Run 专用 Worker 物理 thread、实际 cwd、配置和文件可达性。Worker Return 永远先回本 executor。

## 7. 成功、部分、缺证、不可得和失败时的回交

### 成功

提交完整 M 材料成果、R0/R1 产物、证据引用和准确后继；可建议 H1 / freeze / R2 的具体范围，但不自行宣布 Gate。

### 部分

保留可用产品/场景，逐项说明缺口、受影响问题和最小补证；不得因一类产品缺失把全包写成无用，也不得把部分交付写成 P1 整体完成。

### 缺证

形成具体缺失字段/时间/对象/版本/中间状态和它区分的竞争解释；可在授权内做低成本局部查证，真正跨 Workflow 时再提出具名补证。

### PROVEN_UNAVAILABLE / NOT_APPLICABLE

给出调查范围和依据，明确关闭哪项请求、哪些结论只能限域；不能循环请求同一无变化事实。

### 失败或工具不可用

准确记录实际失败点、已保留成果、恢复条件和不受影响的文档级工作。不得把工具限制写成 P1 业务反证，也不得伪造运行成功。

## 8. 明确非目标与硬停止点

本 D 不做：

- 正式 R2 证据支持/反证结论；
- R3 根因诊断；
- R4 参数标定；
- P2/P3/P4 业务分析；
- 新 CAEGraph/新画图 Skill 设计；
- 业务源码修改；
- 完整上游重算；
- 通用 identity/revision 平台；
- 最终策略/资金动作。

出现以下情况必须停止对应动作并回报，而非绕过：

- 输入哈希与固定身份不一致；
- 数据路径不可读且无合法转存；
- 运行将触发未授权破坏性写入或高成本重算；
- 需要改变 Owner 已固定目标；
- 需要写到 `/dwdhome/fy/BASE_E6_2` 或本 Run GitHub 路径之外；
- 物理 Worker 身份或单写者无法核实。

其他独立的文档、预期与已取得材料工作继续，不因一个动作受阻全停。

## 9. 预期交付物

1. D001 专业执行报告，逐项对应 M 步骤 1～7、R0/R1 和本 D 合同；
2. `ProcessingSkeleton`；
3. P1 产品—证据—场景覆盖矩阵；
4. `MaterialRequirementSet`；
5. 实际材料清单与 `MaterialReview`；
6. `PLAN_READY / DATA_READY / PARTIAL_WITH_LIMITS / BLOCKED` 之一及限制；
7. `ExpectationRegister`、`InputSuitabilityAssessment`、`ScenarioExpectationSet`、`OpenQuestions`；
8. 冻结建议、正式 R2 最小输入和准确后继；
9. 必要时 `AdditionalEvidenceRequest`；
10. 如签 W，正式 W 原件、Worker Return、executor 专业接受意见；
11. 符合 V2 的 executor `PRO_RETURN.json`。

## 10. 正式回交要求

- 先发布专业报告及实际 W/结果原件，再发布引用真实提交的 executor Return；
- `delegation_ref` 必须引用本 D 的 `DELEGATION.json` 精确 commit/path；
- `return_to=chatgpt:OI-EAW-P1-20261116-01:manager`；
- `REPORTED_COMPLETE` 只表示 D001 范围的专业报告完整，不表示 H1、冻结、R2 或父任务完成；
- 回报准确 commit 和路径，不使用 moving branch 引用；
- 不新增旧 ROLE_RETURN/QUESTION_WORK_RETURN 或 FPA 字段。