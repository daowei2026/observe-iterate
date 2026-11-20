# 观察—分析业务控制面三层 Workflow（候选 V0.2）

**本分支用途**：在现有多 Run 控制分支基础上，增加共享 Feature 理解、全量行为统计和严格串行的合理性分析闭环；观察材料准备改为 B～E，合理性 Skill 1／2 保留原目录名但调整职责，Skill 3／4 内部暂不修改。

控制程序和历史长程 Run 不因本分支文档变化自动改写；新工作需显式采用本分支版本。

## 目录与阅读顺序

| 目录 | 内容 | 性质 |
|---|---|---|
| [skills/feature-understanding](skills/feature-understanding/SKILL.md) | 共享 Feature 对象、状态、事件、中间判断、参数和结果字段理解 | 观察材料、全量统计、合理性分析共同前置 |
| [control/01 · L0 完整业务任务](control/01_L0_完整业务任务与双向衔接.md) | 材料准备 ↔ 合理性分析、总输入／输出、补证与任务收束 | 控制流程主体 |
| [control/02 · L1-M 材料准备](control/02_L1_观察材料准备流程.md) | **B 观察位置／C 展示方式 → D CAEGraph 定义集成 → E 执行、核图和取数** | 观察材料外层阶段与 I/O |
| [skills/reasonableness-analysis/README](skills/reasonableness-analysis/README.md) | 全量统计 → 问题闭环 → 图后选场景 → 场景过程对照 → 诊断／标定 | V0.2 合理性专业协作权威来源 |
| [control/03 · L1-R 合理性分析](control/03_L1_合理性分析流程.md) | 合理性控制面与 Gate；本分支同步 V0.2 串行闭环 | 控制流程主体 |
| [control/04 · L2 工作成果 I/O](control/04_L2_节点输入输出登记表.md) | 历史节点 I/O 登记；尚待后续按 V0.2 真实运行进一步校正 | 管理参考 |
| [control/05 · 三级 Gate](control/05_三级Gate及后继路由.md) | L0/L1/L2 Gate、阻断与定向返修 | 控制流程主体 |
| [control/06 · 业务完成全景](control/06_业务完成全景与更新协议.md) | 阶段、工作实例、业务问题和父任务的完成状态 | 跨层控制机制 |
| [longrun/](longrun/README.md) | C/D/W 协议、多 Run 主控、独立 Linux 工作区和跨 Run 校验 | 运行层 |

## 1. 共享 Feature 理解

原观察材料准备 A `feature-occurrence-understanding` 已移出观察材料大项，并扩展为：

```text
skills/feature-understanding/
├── SKILL.md
├── WORKFLOW.md
└── IO_SPEC.md
```

核心产物：

```text
FeatureUnderstandingPackage
```

包含：

- 当前实现来源；
- 业务对象与身份；
- 状态及合法转换；
- 输入／输出事件级 occurrence；
- 业务主输出与中间处理结果；
- 关键中间判断；
- 形成、更新、确认、结束和引用关系；
- 参数定义、派生与消费位置；
- 实际运行结果字段映射和未暴露项。

该 Package 同时供：

```text
全量行为统计
观察材料准备
合理性 Skill 1／2
偏差诊断
```

使用。它不运行 Feature、不做统计、不选场景、不画图、不判断合理性。

## 2. 观察材料准备：B～E

### 外层 Workflow

```text
外层输入：特征名称、代码版本、实例、FeatureUnderstandingPackage

B 观察位置准备 ─┐
                  ├→ D CAEGraph 定义集成 → E 执行／核图／正式取数
C 展示方式准备 ─┘

最终交付：ObservationMaterialPackage
```

共享 Package 是 B、C、D 的共同前置，但不是观察材料内部阶段。

### 阶段 Skill

| 类别 | 入口 | 作用 |
|---|---|---|
| **M 总入口** | [observation-material-preparation/SKILL.md](skills/observation-material-preparation/SKILL.md) | 索引 B～E、技术参考和模板 |
| **B 观察位置** | [observation-position-preparation](skills/observation-material-preparation/observation-position-preparation/SKILL.md) | 普通 Feature 经验默认位置；高频 Feature 复用 1d→30m→1m→5s→tick 位置层级 |
| **C 展示方式** | [caegraph-display-preparation](skills/observation-material-preparation/caegraph-display-preparation/SKILL.md) | 根据共享 Package 列待展示信息；形成并迭代展示预期与唯一预期 HTML；整理可注入代码 |
| **D 定义集成** | [caegraph-definition-integration](skills/observation-material-preparation/caegraph-definition-integration/SKILL.md) | 理解锁定 CAEGraph 仓库后，一次性集成实例、共享字段、B 位置和 C 展示 |
| **E 执行／运行** | [caegraph-execution](skills/observation-material-preparation/caegraph-execution/SKILL.md) | W1 运行／有限修复，E 专业核图，W2 正式取数，形成同版本图和数据 |

### 材料与合理性的边界

观察材料准备只交付：

```text
宽范围图
图数据
脚本
版本／参数／位置绑定
一致性核对
已知限制
```

它不：

- 从图中选择合理性正例或反例；
- 判断输出误报或漏报；
- 冻结场景预期；
- 宣布 Feature 合理或不合理。

这些工作由合理性 Skill 1／2 在 `ObservationMaterialPackage = DATA_READY` 后完成。

## 3. 合理性分析 V0.2：严格串行

```text
FeatureUnderstandingPackage
→ 运行 Feature
→ Skill 0 全量行为统计
→ Skill 3 诊断全量结构疑点
    ├─ 参数问题 → Skill 4
    ├─ 实现问题 → 外部实现修正
    ├─ 设计问题 → 外部 Owner／设计接口
    └─ 仅需场景解释 → ScenarioQuestionQueue
→ 任何行为修改后重跑 Feature 和全量统计
→ GlobalProfileGate = PASS_TO_SCENARIO_REVIEW
→ 观察材料准备 B～E
→ Skill 1 从已画好的图和图数据中选真实场景、冻结场景预期
→ Skill 2 逐场景对照原始过程／预期过程／实际过程
→ 新疑点进入 Skill 3
→ 修改行为后重新回到 Feature 重跑和全量统计
```

线一与线二在 V0.2 中不是并行关系。

## 4. 合理性 Skill

| 顺序 | 目录 | 当前职责 |
|---|---|---|
| 0 | [feature-global-behavior-profiling](skills/reasonableness-analysis/feature-global-behavior-profiling/SKILL.md) | 新增：不依赖图，对最新运行结果做对象、事件、状态、生命周期和分层统计，形成结构疑点与全量 Gate |
| 1 | [business-expectation-derivation](skills/reasonableness-analysis/business-expectation-derivation/SKILL.md) | 名称暂不改：在图完成后选择真实正／负例、误报／漏报候选、参数边界和覆盖外场景，并冻结预期 |
| 2 | [business-evidence-comparison](skills/reasonableness-analysis/business-evidence-comparison/SKILL.md) | 名称暂不改：逐场景比较原始市场过程、预期 Feature 过程和实际 Feature 过程，定位第一次业务分歧 |
| 3 | [business-discrepancy-diagnosis](skills/reasonableness-analysis/business-discrepancy-diagnosis/SKILL.md) | 当前内部实现保持不变：查根因、做参数可修复性初筛和路由 |
| 4 | [feature-instance-calibration](skills/reasonableness-analysis/feature-instance-calibration/SKILL.md) | 当前内部实现保持不变：参数可行域、少量候选和完整实例验证 |

Skill 0 为兼容现有 Skill 3 输出 `DiagnosisInputAdapter`，本轮不改 Skill 3／4 内部文件。

## 5. 全量 Gate

| 状态 | 含义 |
|---|---|
| `BLOCKED` | 版本、参数实例、对象键、核心事件字段或运行范围不可靠 |
| `DIAGNOSIS_REQUIRED` | 存在尚未完成 Skill 3 的结构疑点 |
| `RERUN_REQUIRED` | 参数、实现、设计或数据修改改变了行为，旧统计失效 |
| `PASS_TO_SCENARIO_REVIEW` | 已确认缺陷已闭环；剩余问题需真实场景解释，允许进入图和场景分析 |

`PASS_TO_SCENARIO_REVIEW` 不是“Feature 已合理”的结论。

## 6. C 的三部分

```text
C1：根据 FeatureUnderstandingPackage 列出待展示信息
C2：形成并迭代展示预期
    C2A：阅读锁定 CAEGraph 使用手册
    C2B：形成第一版展示预期和 HTML
    C2C：从 HTML 识别复杂点
    C2D：核实现有能力并同步更新预期和 HTML
C3：整理可注入展示代码并核对 C2 语义
```

C2 结束时的当前 HTML 是唯一预期 HTML；C3 不另生成第二份。

## 7. 技术参考与模板

| 类别 | 入口 | 作用与边界 |
|---|---|---|
| D 仓库集成参考 | [CAEGraph 仓库结构与定义集成参考](skills/observation-material-preparation/references/CAEGraph仓库结构与定义集成参考.md) | uplot 调用链和真实集成边界 |
| B 高频位置参考 | [高频多尺度观察位置参考](skills/observation-material-preparation/observation-position-preparation/MULTISCALE_POSITION_REFERENCE.md) | 只复用位置层级与父子关系 |
| E 技术参考 | [CAEGraph 执行、核图与取数](skills/observation-material-preparation/references/CAEGraph执行取数与验证.md) | 最终图核对、核图后正式取数和一致性验证 |
| E Worker 派单 | [Worker 派单合同](skills/observation-material-preparation/caegraph-execution/WORKER_DELEGATION.md) | W1／W2 执行映射 |
| 任务记录模板 | [观察材料准备任务记录](skills/observation-material-preparation/templates/观察材料准备任务单.md) | 历史模板；后续可按真实运行再升级为共享前置+B～E 版本 |
| 候选方法索引 | [观察候选方法](skills/observation-method-candidates/README.md) | 候选方法，不是固定流程 |

## 8. 版本与历史

- `task-inputs/` 是具体用例输入，不替代通用 Skill；
- 历史 `longrun/runs/`、报告或聊天出现旧 A～E／四 Skill 结构，属于当时事实，不回写历史；
- 新工作以本分支当前 `FeatureUnderstandingPackage + 全量统计 + B～E + 场景分析` 规则为准；
- 后续应使用 EAW Wall 真跑一轮，再决定是否需要问题影响分级、局部重跑或场景反向驱动画图。
