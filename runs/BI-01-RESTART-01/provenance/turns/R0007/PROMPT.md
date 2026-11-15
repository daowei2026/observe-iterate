[BI01-RESTART-01-R0007-621369295e944443984a81cb6a878f32]
work_id: BI-01
invocation_id: BI01-RESTART-01-R0007-621369295e944443984a81cb6a878f32
assignment_token: 3d3b47145c254b4c8ca6d534cd86f338
role: professional
recipient: chatgpt-project:细节叙事生成_金标/chat:new:BI01-RESTART-01-I5-OWNER-PACK
当前阶段：专业任务 BI01
当前职责：I5 Owner Pack 实际证据与图解释

**每次实质业务推进，都以完整完成 Owner 确定的本用例当前阶段全部约定工作为目标。禁止自行将本轮目标缩成单个 Case、一组局部 Case、一个文件、一个接口或最近几项修复。当前重点只决定顺序，不能成为主动收工点。**

**本任务按实际有权的I1–I6专业阶段完成对应工作；进入I4时须围绕真实结果、观察差异、层间增量/无增量、支持/反证、替代解释和下一问形成完整可核实的业务判断。具体方法与Gate从[专业P00/P02](../../professional/source/00_AGENT_CHARTER_AND_STAGE_CONTRACT.md)及[当前I4合同](../../professional/source/02_I4_OBSERVATION_AND_CHALLENGE.md)读取；其他阶段按对应方法，不从本通用模板推算。**

业务事实、CaseFinding、待证假设、设计/方法问题、证据缺失与计算错误分别表达；不得把单 Case 发现提升为普遍规律。需要补算时必须使用有权采用的真实 Case、Source、Method、As-Of 和数据，核实结果的可消费范围，不把技术失败伪装为市场现象。

本轮确有获授权技术任务时，已有实现可用于核对方法、数据与实际调用，不能以列出读过的文件代替核验，也不照搬未完成的方法。代码示例只用于理解适用做法，不要求所有 BI-01 观察问题使用统一Header、生命周期或固定数量模块；没有该技术任务时不把这些工程事项列为专业观察前置。

发现实际结果、方法或已授权工程有可证实错误时，按当前有权处置处理直接受影响的位置；新任务不默认开展清理、全仓审计或恢复工程。当前重点只决定推进顺序，不成为完成局部即停止的理由。

从完整目标、当前 I1–I6 子意图的 Input/Output/Gate、真实成果及未决问题出发，连续完成已经明确的全部剩余。围绕本轮业务问题组织实际证据、Case/Source/Method/As-Of、必要挑战、所得认识和下游使用资格；确需技术补证时再连同输入、计算、输出及直接消费者一起处理。已授权的相关修改可以跨多个文件；不按文件数判断完成，也不为了显得完整修改无关文件。

**管理已经完成的材料采用、旧要求撤销、已知问题裁定和全局安排直接使用。推进者不再每轮重判全部历史、维护公共工作量、编写独立接收结论或设计主控派发。**但仍须理解实际业务、读取必要完整专业正文、查真实数据/结果/方法和直接依赖；涉及代码时核实实际实现，不能以管理未点名某个文件为由漏掉真正的使用位置。

BI-01 的专业观察问题、可信结果范围、阶段成果与必要工单来源仍是相应专业产物；减负不取消实质义务。Worker回交真实技术变化，执行Pro消费后向管理交业务结果，管理维护完整推进位置。地图不能代替正确专业方法和事实正文。

**本轮确有授权工程修改时，新增内部函数、Direct 入口、适配器或类型，不等于真实业务结果已经改变。实际使用的公共入口、生产者和消费者必须改接；旧错误路径仍在使用时，不得宣称相关职责已经退出。**

本轮确需 Worker 技术执行时，在真实输入、权限和工具具备后及时补算、制图或构建并核查；未执行须说明具体限制，不以技术准备冒充专业成果。技术执行顺序与真实结果使用资格分别处理。Owner 优先审阅局部观察成果只改变反馈先后，不改变完整阶段责任，不形成逐项批准。

方法未实现不能改称待校准；输入与调用未实现不能改称等数据；工程缺件不能改称市场正常 Pending。真实零、合法空、未成熟、输入缺失、未调用和读取失败分别说明。

受到实际容量、工具、真实权限或未定业务问题限制时，交出真实实物、具体限制及完整未完，并明确已知后继；不能以自设小目标达成作为停止理由。完整目标不授予跨仓、抢写或更改受保护业务的权限。

正确专业正文和本轮确有授权的工程细节禁止压缩、概述替换或只留历史链接。已否机制按现行处置连同专属使用位置删除，不换名称、换容器或移入 helper 保留。

按本次有效Binding的professional_mode/专业阶段和`source_reads`完整读取专业原文，完成实际授权的I1–I6阶段工作，交具名结果/可读证据/自查/未完/合法continuation。当前I4主要按[真实观察与挑战合同](../../professional/source/02_I4_OBSERVATION_AND_CHALLENGE.md)识别事实、层间有无增量、反例与未决；如需技术补算或制图，由执行Pro按[Pro→Worker合同](../../professional/source/04_PRO_WORKER_CODEX_HANDOFF.md)签发工单并消费回交，不自签G4/G5。不得把CYF原Mission A/B/C特征施工、Host五段或默认两路工程作为本专业任务。

## Owner完整目的

# 观察迭代专业 Agent：总意图与阶段合同

source:
- path: `00_长程任务总意图与六个子意图.md`
- blob: `d77c14e1564c2c751699073853887cfab9ce3ae6`
- extraction: 总意图、I1— I6 Input/Output/Gate、角色分工

## 总意图

建立由 AI 持续开展、Owner 在必要环节进行业务判断的长程业务观察与设计迭代过程。

基于已形成的特征细节设计和真实数据，使 AI 能够自主选择具有业务价值的观察问题，获取和核查对应特征的具体结果，分析结果揭示的业务现象，主动寻找反例与其他解释，发现现有设计的价值、问题和不足，并将观察结果转化为下一轮研究、验证或设计修订行动。

任务不以完成既定数量的特征计算或修改设计为成功标准，而以能否持续获得可检验的业务认识，并据此推动有意义的迭代为核心衡量标准。

## 所有子意图共同使用的字段

| 字段 | 必须表达什么 | 约束 |
|---|---|---|
| `IntentId / Purpose` | 本子意图要赢什么、为什么服务于总意图 | 不能只写“完成下一阶段” |
| `Input` | 哪些既有成果、原始数据、合同、决定或实例条件是当前工作的依据 | 用实际引用；可声明缺失或仅有报告 |
| `Output` | 必须形成的业务成果/可检查实物，及必要来源 | 结果不是一篇空泛总结，也不一律要求新文件 |
| `Gate` | 依据什么判断本子意图可交给下游消费，哪些情况需补修/暂停 | 执行 Pro 提交自查与证据；管理 Pro 在授权范围内作阶段接收判断、限定适用范围和后继，不由执行者自称通过代替 |
| `OwnerAdditions` | Owner 对本子意图的新增重点、输入/输出/Gate、授权或纠正 | 可留空；仅来自可追溯的真实 Owner/用户要求，不由 AI 代填 |
| `Handoff` | 交给下一子意图的成果、版本、明确限制及接收者 | 正常续作基于 Gate 结果；权限另按实际任务采用 |

Gate 最终阶段接收的责任者是管理 Pro，不由执行 Pro、Codex 或机械主控代签；重要业务取舍继续归 Owner。Gate 的判断至少区分：初步认为具备结果（Preliminary）、有据可被下游消费（Pass，可能限定范围）、需针对性补修（NeedsRepair）、等待具名输入或 Owner 判断（WaitingInput / WaitingOwner）。这些是工作表达的参考状态，不另建新的平台机器状态。

## I1— I6 最小 Input / Output / Gate

| 子意图 | Input | Output | Gate |
|---|---|---|---|
| **I1：识别值得观察的业务问题** | 总业务意图、适用业务职责、已有成果与反馈、候选研究问题 | 被选观察点/核心问题、选择理由、拟观察的领域对象或变化、需要的依赖、当前非目标 | **G1：问题具备实质业务意义且边界可辨。** 知道要弄清什么、为什么值得观察、需何类证据；纯计算节点不能冒充业务问题 |
| **I2：使设计和数据成为可执行依据** | G1 的问题和范围；业务/工程 Source、数据、配置、已接受或候选 Method | 必要计算依赖、准确 Source/Method/Case 版本、输入及时间/状态/缺失规则、参考与正式边界、真实未决项 | **G2：本轮所需参考结果有合法获得途径。** 能按照明确规则计算或按合法 Pending/Withheld/条件分支处理；不得为取得理想结果悄悄猜 Source、改参数 |
| **I3：取得可信且可检查的具体业务结果** | G2 可消费的依据、真实冻结输入和可执行程序/结果、Case/As-Of | 所需中间及最终领域结果、版本与来源、足够核查/复算、实际未决状态 | **G3：结果已达到相应观察使用资格。** 实际成果可读取、关键来源/时间/方法可追、必要计算核对通过；只批准可信的结果范围，未决部分如实保留 |
| **I4：AI 主动业务观察与挑战** | G3 通过范围内的结果与视图、G1 问题、业务比较基线、适用的证据限制 | 可追溯的事实观察、层间新增认识或无增量结论、支持/反证/缺失、替代解释、必要挑战、下一步候选问题 | **G4：取得有实质业务内容、经必要挑战的认识。** 不仅复述数值/设计；能说明什么认识成立或未成立、证据范围和下一步未决 |
| **I5：支持 Owner 进行业务判断** | G4 的业务发现、挑战和未决；实际图/证据；总业务目的及当前权限 | 可直接审阅的 Owner Pack：关键市场过程、增量/无增量、支持反证、争议、具体可选行动与需 Owner 回答的问题 | **G5：材料足以支持真实判断。** Owner 无须从全量 CSV 自行倒推事实；“Pack 可审阅”不等于“Owner 已批准” |
| **I6：将反馈转化为下一轮实际行动** | G5 材料、已有 AI/Owner 反馈、实际授权与未完成工作 | 具备依据的继续/修订/补 Case/停止/暂缓决定，具体可执行的下轮目标、输入输出 Gate、职责与来源；需要时有正式回修请求 | **G6：后继行动已被准确安排或合法结束/等待。** 只有“建议继续”不通过；涉及正式合同或授权变更须等待有权决定 |

同一阶段可以跨多轮聊天和多个 Case。G1—G6 是业务可消费资格，不是六个独立 Owner 审批会，也不是僵硬瀑布流程。遇到真实证据问题，可定位返回受影响的前序子意图及其 Gate，不必清零所有已成立结果。

## 角色分工

- 管理 Pro：完整目标、各子意图工作安排、阶段 Gate 的实质接收判断以及 I6 后继。
- 执行 Pro：当前子意图的专业工作、必要 Codex 工单和专业结果交付；自查并提出通过 Gate 的依据，但不自行签署最终接收。
- Worker Codex：依据执行 Pro 的具体工单进行技术补算、制图或数据处理。
- 操作端：按有权任务和回交机械发送、收取、去重与接续，不作业务判断。
- 独立审查：按需发生；管理 Gate 判断不冒充独立审查，执行者自检也不构成独立审查。
- Owner：保留超授权、正式业务方向和重要业务取舍的决定权。

来源：daowei2026/observe-iterate@75d42776a78cd4cbdf3b61bbf86ec93701d06b84:professional/source/00_AGENT_CHARTER_AND_STAGE_CONTRACT.md::full

## 本轮当前工作

# BI-01-RESTART-01 当前任务：I5 Owner Pack 与真实取舍材料

task_id: BI01-RESTART-01-I5-OWNER-PACK-01

## 0. 角色与任务性质

recipient：BI-01 执行 Pro，新专业会话 `BI01-RESTART-01-I5-OWNER-PACK`。  
professional_mode：`OBSERVATION_I5`。  
当前阶段：I5；I4/G4 已由管理在当前 Reference/Shadow 范围内通过。  
你不是管理 Pro、Owner、Worker Codex 或操作端。你负责把已接收的业务认识组织成 Owner 可直接判断的材料，并提交 G5 自查；不自行签 G5，不替 Owner 作方向决定。

<a id="full-scope"></a>
## 1. 完整范围

持续完成当前 I5 阶段全部约定工作：

- 只采用管理已经接收的 G3/G4 结果和明确限制；
- 把真实市场过程、设计价值、无增量、争议、替代解释和证据依赖组织成直接可审阅的 Owner Pack；
- 给出具体行动选项、前置、投入、风险和停止条件；
- 明确管理建议和真正需要 Owner 回答的问题；
- 形成足以让管理判断 G5 的完整交付。

当前任务不是新的市场观察、正式方法设计或工程实现。不得为“让 Pack 更完整”自动重开 I4、增加第三 Case、补造 formal 结果或扩大到全市场。

<a id="accepted-input"></a>
## 2. 管理已接收的输入，直接采用

管理决定：

```text
runs/BI-01-RESTART-01/reviews/MANAGEMENT_GATE_DECISION_R0006.md::full
```

I5 直接采用，不再重判：

1. Case-01、Case-02 的输入身份和当前 DataBinding；
2. G3 限定范围；
3. Case-01/02 的 accepted findings；
4. 当前 U2 组织价值与成员选择无增量边界；
5. 当前 U3 的适用边界；
6. MF-01 的 Withheld 处置；
7. formal Formation/Separation/C2/H1/U3 不具备当前资格；
8. I4/G4 已 Pass；
9. 不再追加第三 Case；
10. Owner 选项 A/B/C 与管理建议。

若 Pack 编制中发现 exact 引用与管理决定冲突，只返回受影响 claim、准确来源和 Pack 中需暂停的部分；不得笼统重开整套 I4。

<a id="current-purpose"></a>
## 3. 当前业务目的

Owner 需要判断的不是“两个报告写得是否完整”，而是：

> 当前 U2/U3 已经解决了哪个真实业务问题、没有解决什么；接下来应采用当前边界并结束本 reference 观察，还是值得投入一个具名 consumer 驱动的正式验证？

Pack 必须让 Owner 无需读取全量 CSV 或自行倒推专业分析，就能看懂：

- 市场实际发生了什么；
- 为什么原来容易读错；
- U2/U3 各增加了什么、没增加什么；
- 当前结论可靠到什么范围；
- 三个选项各自意味着什么。

<a id="owner-decision"></a>
## 4. Owner 决策框架

### 选项 A｜采用当前边界并结束本 reference 观察（管理建议）

保留：

```text
C0/N 真实结果
actual / knowledge / lifecycle
U2 的身份、同轮组织和可追溯性
```

暂不当成既成能力：

```text
exact 组 = 机会边界
当前 Reference assessment = 正式 Quality
当前 U3 = 独立投资增量
```

后继：进入 I6，把“保留组织层、暂停选择/Quality 投入”转成实际安排。

### 选项 B｜授权具名 consumer 驱动的正式验证

只有 Owner 确实需要“成员筛选、重复暴露或 Quality”改变下游判断时才选。Pack 必须列明最低前置：

- 下游 consumer 与要改变的判断；
- formal Source/Method/Scope/Δ/Epoch；
- 与单品种强基线的增量标准；
- 与 Case-01/02 不同源的 Case 集；
- 不通过时停止什么；
- 投入预算与责任者。

### 选项 C｜直接进入正式工程

当前证据不足，不建议。Pack 应说明这是显式超出当前证据的方向授权，不是 G4 推导。

### Owner 问题

Pack 最终只问：

1. 是否批准选项 A 作为当前正式方向？
2. 若不批准，是否选择选项 B，并给出具名 consumer 与投入边界？

不得增加泛化的“还有什么意见”或把普通专业判断交给 Owner。

<a id="inputs"></a>
## 5. 输入

### 5.1 管理与阶段合同

- `professional/source/00_AGENT_CHARTER_AND_STAGE_CONTRACT.md`
- `professional/source/03_STAGE_HANDOFF_AND_READINESS.md`
- `professional/source/04_PRO_WORKER_CODEX_HANDOFF.md`
- `professional/source/05_ROLE_GATE_AND_HANDOFF_CONTRACT.md`
- `reviews/MANAGEMENT_GATE_DECISION_R0004.md`
- `reviews/MANAGEMENT_GATE_DECISION_R0006.md`
- 当前推进地图和本任务。

### 5.2 已接收专业成果

- `artifacts/I4_R0003/REPORT.md`
- `artifacts/I4_R0003/evidence/CHECK_SUMMARY.json`
- `artifacts/I4_R0005/REPORT.md`
- `artifacts/I4_R0005/evidence/CHECK_SUMMARY.json`
- `artifacts/I4_R0005/evidence/KEY_EVIDENCE.json`

原始 ZIP 只作为这些已接收结果的 DataBinding 身份保留；当前 Pack 不要求重新读取或重算它们。

<a id="allowed-use"></a>
## 6. 可消费资格与非主张

### 可直接使用

- 管理已接收的 CaseFinding、NoIncrementFinding、Method/Design Finding；
- actual、knowledge、Working/Completed 和公平比较；
- U2 的身份/时间/可追溯性增量；
- exact 成员选择和当前 U3 的无增量边界；
- 反证、替代解释、证据依赖和消费者限制；
- Owner 选项与管理建议。

### 必须保留为限制

- 两个 Case 相邻、同源，不是独立统计重复；
- formal Formation/Separation/C2/H1/U3 未验证；
- Case-02 没有对应 U3 输出；
- MF-01 字段 Withheld；
- 没有资金、收益或因果结论；
- 没有独立专业审查；
- 没有生产资格。

### 禁止

- 用“两个 Case 都一样”冒充普遍规律；
- 把组织便利直接写成投资收益；
- 把 exact actual 写成经济过程真理；
- 把当前无增量写成完整 U2/U3 无用；
- 把管理建议写成 Owner 已批准。

<a id="work"></a>
## 7. 连续专业工作

### A. 一页 Executive Summary

用普通投资业务语言回答：

1. 观察了什么；
2. 两个 Case 真正揭示了什么；
3. U2/U3 的价值边界是什么；
4. 当前管理建议是什么；
5. Owner 需要回答什么。

禁止以字段名或 schema 开头。

### B. 市场过程证据面板

至少形成两块可直接读的面板，可使用 Markdown 表格，不强制新图：

1. **Case-01：**共同 Trough、knowledge、Working/Completed、HC/RB/I 分化和伪排序纠正；
2. **Case-02：**HC/RB exact actual、I 早五 bar、共同可知时点、T0/11:30 次序变化和 formal status。

每块面板必须清楚区分 actual、knowledge、Working、Completed 和后继观察，不把后来 end 回填到旧 As-Of。

### C. 增量/无增量价值矩阵

逐层回答：

| 层 | Owner 应知道什么 |
|---|---|
| 单品种 KLine/C0/N | 已经能知道哪些路径、时间和生命周期事实 |
| 静态 HC/RB/I | 只提供什么对象范围，缺什么 |
| U2 组织 | 新增身份、同轮、knowledge、资格、追溯中的哪一项 |
| exact 成员组织 | 为什么未形成稳定机会边界 |
| 当前 U3 | Case-01/02 分别具备什么、缺什么 |
| formal U2/U3 | 哪些尚未实际验证，不能从当前结果推出 |

### D. Claim 资格表

分成四栏：

```text
Accepted
Scoped / CaseFinding
Withheld / Not Established
Hypothesis
```

每条 claim 给 exact 来源和一句非主张。

### E. 反证、争议和证据依赖

至少说明：

- endpoint / maturity / knowledge 敏感；
- exact bound 敏感；
- C0/N/C1/U3 的同源事实；
- 两个 Case 的相邻与复用；
- Case-01 single-scale 和 Case-02 baseline 的 N consumer 差异；
- 组织价值与投资价值不是同一件事。

### F. 行动选项

为 A/B/C 分别写：

```text
要赢什么
当前证据支持度
前置输入
大致投入类别
失败/停止条件
主要风险
对既有成果的处置
```

不得伪造具体人天或预算数字；没有真实依据时用相对投入和需要 Owner 定界的项目。

### G. 管理建议与 Owner 问题

明确推荐 A，并说明为什么不是“因为做不出来所以停”，而是当前业务问题已经有据回答、继续工程需要新的 consumer 和证据合同。

最终只保留 §4 的两个 Owner 问题。

<a id="deliverables"></a>
## 8. 交付

1. `runs/BI-01-RESTART-01/artifacts/I5_OWNER_PACK/OWNER_PACK.md`；
2. 如确有必要，可附同目录不超过两份直接证据面板文件；不是数量要求；
3. Pack 内 exact source index；
4. G5 自查表；
5. 全部限制与未决；
6. ROLE_RETURN；
7. QUESTION_WORK_RETURN。

不得只交摘要而缺完整 Pack，也不得把 R0003/R0005 报告原样拼接当 Pack。

<a id="completion"></a>
## 9. G5 申请条件

只有同时满足以下条件才申请 G5：

- Owner 无需读取全量 CSV 即可理解关键市场过程；
- 增量/无增量、支持、反证、争议和未知分开；
- 每条承重 claim 都能追到管理已接收结果；
- 不把 CaseFinding 外推普遍规律；
- 不把 formal 缺件冒充当前失败，也不把当前诊断冒充 formal 结果；
- A/B/C 选项可真实执行，前置和停止条件清楚；
- 管理建议和两项 Owner 问题明确；
- 没有写成 Owner 已批准；
- 全部重要未决和 I6 候选清楚。

<a id="worker"></a>
## 10. Worker Codex

当前没有 Worker 工单。Pack 的核心是业务整理，不是绘图工程。Markdown 表格足以保真时禁止为了“更像报告”增加 Worker。

若确有一项不可访问的必要证据，先返回：

```text
exact Owner claim
缺少的证据
已有来源为何不足
受影响的 Pack 段落
最小技术输出
```

由管理决定；执行 Pro 不自行派发。

<a id="budget"></a>
## 11. 投入与复看

- 预计 1 次有效执行 Pro 调用；
- Pack 候选形成、出现具名证据冲突，或 1 次有效调用结束，均触发管理；
- 下一次管理只判断 G5、定向补 Pack 或 WaitingOwner；
- 不自动回 I4；
- 不自动进入 I6；
- Owner 未实际回答前不声称方向批准。

<a id="trigger-pack-result"></a>
## 12. RESULT 触发

当完整 Owner Pack 和 G5 自查形成时，触发管理接收。

<a id="trigger-evidence-conflict"></a>
## 13. 证据冲突触发

只有新发现与管理已接收 claim 的 exact 来源发生实质冲突时触发；明确受影响 claim。普通排版、引用修复或既知 formal 缺件不构成此触发。

<a id="trigger-change"></a>
## 14. CHANGE 触发

Owner、正式方法、业务方向或 DataBinding 发生实质变化时触发，只限制受影响部分。

<a id="route-same-work"></a>
## 15. 同工作续作正文

继续本任务。直接采用 R0006 的 G4 Pass、Owner 决策框架和全部限制；不要重做 I4。完成可直接审阅的 OWNER_PACK、行动选项和 G5 自查，形成结果后提交管理。

<a id="route-accept"></a>
## 16. 管理接收正文

向 `chatgpt-project:细节叙事生成_金标/chat:BI01-R01-管理` 提交完整 Pack、来源、限制、G5 自查、全部未决和双 Return。不得把执行自查当 G5 或 Owner 批准。

<a id="route-decide"></a>
## 17. 管理裁定正文

只在 Pack 形成、新证据冲突、Owner/正式方向变化或超授权投入时进入。写清受影响 claim、可继续部分和需要的具体决定。

<a id="route-return-repair"></a>
## 18. 回交修复正文

只修确切的 Return 字段、引用或 Pack 定位问题。缺专业内容则继续原 I5 工作，不为过结构检查制造 Owner 决定。

来源：daowei2026/observe-iterate@db61798c8d56a811a9db98d4b766ac584203f524:runs/BI-01-RESTART-01/01_当前任务.md::full

## 本轮原文与位置

本次原始要求：`daowei2026/observe-iterate@db61798c8d56a811a9db98d4b766ac584203f524:runs/BI-01-RESTART-01/01_当前任务.md::#route-same-work`
当前生效任务：`daowei2026/observe-iterate@db61798c8d56a811a9db98d4b766ac584203f524:runs/BI-01-RESTART-01/01_当前任务.md::full`
当前任务采用依据：`daowei2026/observe-iterate@db61798c8d56a811a9db98d4b766ac584203f524:runs/BI-01-RESTART-01/reviews/MANAGEMENT_GATE_DECISION_R0006.md::full`
上一轮实际采用的任务绑定：`daowei2026/observe-iterate@6fb03212ca3b0dcebe3dba0c0a1d0328e2f571d4:runs/BI-01-RESTART-01/bindings/QUESTION_WORK_BINDING_I5.json::full`
完整工作范围：`daowei2026/observe-iterate@db61798c8d56a811a9db98d4b766ac584203f524:runs/BI-01-RESTART-01/01_当前任务.md::#full-scope`
本次实际证据：`daowei2026/observe-iterate@b974d70aba6e0596a6251178caaf7f9f305def95:runs/BI-01-RESTART-01/provenance/turns/R0006/ROLE_RETURN.json::full`
本次实际证据：`daowei2026/observe-iterate@6b5d159b72484c16818ade45bb7b574516a31e0a:runs/BI-01-RESTART-01/provenance/turns/R0006/GATE_CHECK.json::full`
本次实际证据：`daowei2026/observe-iterate@b8f5d169251021fe3469f123d3a1a9c21785cb40:runs/BI-01-RESTART-01/reviews/WORKMAP_READER_R0006.md::full`
本次实际证据：`daowei2026/observe-iterate@1c7e04abfd44bbc3f2d96a17455a9f96fc0a3299:runs/BI-01-RESTART-01/reviews/WORKMAP_INTAKE_CURRENT.json::full`

## 本次直接读取的上下文

- MODE_FULL：`daowei2026/observe-iterate@75d42776a78cd4cbdf3b61bbf86ec93701d06b84:professional/source/00_AGENT_CHARTER_AND_STAGE_CONTRACT.md::full`
  用途与边界：完整总意图、I5 Input/Output/Gate、Owner与角色权限
  本checkout已核位置；正文仍须接收者实际读取。 本次不主张已读复用。

- BOUNDARY：`daowei2026/observe-iterate@75d42776a78cd4cbdf3b61bbf86ec93701d06b84:professional/source/03_STAGE_HANDOFF_AND_READINESS.md::full`
  用途与边界：G4到I5、限定接收、定向补修和阶段交接
  本checkout已核位置；正文仍须接收者实际读取。 本次不主张已读复用。

- BOUNDARY：`daowei2026/observe-iterate@75d42776a78cd4cbdf3b61bbf86ec93701d06b84:professional/source/05_ROLE_GATE_AND_HANDOFF_CONTRACT.md::full`
  用途与边界：I5专业交付、G5管理接收和Owner权限
  本checkout已核位置；正文仍须接收者实际读取。 本次不主张已读复用。

- FOCUS_FULL：`daowei2026/observe-iterate@db61798c8d56a811a9db98d4b766ac584203f524:runs/BI-01-RESTART-01/reviews/MANAGEMENT_GATE_DECISION_R0006.md::full`
  用途与边界：当前G3/G4决定、I5目的、Owner选项、已知处置和禁止项
  本checkout已核位置；正文仍须接收者实际读取。 本次不主张已读复用。

- FOCUS_FULL：`daowei2026/observe-iterate@34d90874ddc9617a4dfecec1f39cbedf54c23845:runs/BI-01-RESTART-01/artifacts/I4_R0003/REPORT.md::full`
  用途与边界：Case-01市场过程、发现、无增量、反证和来源
  本checkout已核位置；正文仍须接收者实际读取。 本次不主张已读复用。

- FOCUS_FULL：`daowei2026/observe-iterate@ff0c157baf037f502f0158b35f92c26bec4218a4:runs/BI-01-RESTART-01/artifacts/I4_R0005/REPORT.md::full`
  用途与边界：Case-02市场过程、成员选择无增量、consumer边界和I5就绪
  本checkout已核位置；正文仍须接收者实际读取。 本次不主张已读复用。

- PROVENANCE_TRIGGER：`daowei2026/observe-iterate@ff0c157baf037f502f0158b35f92c26bec4218a4:runs/BI-01-RESTART-01/artifacts/I4_R0005/evidence/KEY_EVIDENCE.json::full`
  用途与边界：Owner Pack承重数字和Case-02直接证据，不用于新计算
  本checkout已核位置；正文仍须接收者实际读取。 本次不主张已读复用。

读取Owner完整要求、生效完整任务和输入输出地图，不能用最新remaining替全部责任。按source_reads取得准确正文用于判断，已读未变且可恢复者复用；不递归扫无关历史，不用索引/hash/旧回执代正文。

旧包中已被Owner否定的多余任务，必须由原有权责任者从当前正文、任务、前置、接收和后继删除；只为其存在的辅助代码与检查交原实现者删除。禁止继续完善、改名或列为暂缓/未来优化。不能只在顶部写新原则却继续采用相反正文。真实业务方法、时间、身份、状态、正式输出与消费者保留，技术机制替换回正常平台。正确正文禁止任何压缩或摘要替换。历史提交和实际记录不倒改；历史可追溯不授后续派发。通用材料维护不自动取得用例任务写权。

当前执行材料由管理和有权任务责任者明确采用。推进者取得实际需要的正确正文，不能用管理概述替代业务细节；也不要求每轮重读全部历史和已撤完整任务。

发现新的实质冲突时，给出准确位置与受影响结论，按原责任处理。来源不足只限制真正依赖的判断，不用旧快照补造事实，也不冻结无关工作。

方法版本、业务合同版本、源码版本和运行数据分别保持准确，不随一次方法更新全部追 latest。

运行事实（来自现有记录）：
观察时间：2026-10-16T14:32:17.000Z
有效回交数：0

按既有协议交完整实质回答及ROLE_RETURN/QUESTION_WORK_RETURN，来源、未执行和资格如实保留，不新增控制表，不重抄协调者已存提示。完整任务未完成就保留完整责任及连续后继，局部交付不自设停点。要求GitHub提交时普通快进并fresh回读，最后commit message带turn complete及本轮invocation_id，无invocation时简要标明执行身份；不造空提交。

专业者回交实际实物、必要自检／执行结果、具体限制及完整未完，不代写管理接收、全局预算或主控派发。管理回交已完成的判断、实际处置和可执行后继，不以问题目录代替决定。

没有完整完成时，说明真实停止原因及已经明确的下一步；不得以自设局部目标完成作为结束解释。
