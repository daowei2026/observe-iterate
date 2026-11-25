# S01｜业务及特征理解（D002 / C0002）

状态：已完成。仅完成任务书 S01，不含候选检索、案例对照或设计缺陷判断。执行者：本 Run E1；零 Worker。

任务依据：[V0.4 全文及 §8.0](https://github.com/daowei2026/observe-iterate/blob/b1bf8025dd49091e71c8814caf36c2e02aced198/ai_chat/业务有效性/EAW_P1_挂单成交演化_迭代点发现任务_V0.4_长程执行版_20261125.md)，本轮范围为 [D002](https://github.com/daowei2026/observe-iterate/blob/9d4c87f77736e5a92eda33b7655065b698b6b4e9/longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261125-01/delegations/D002/DELEGATION.md)。

## 要保留的业务信息

EAW 最初讨论的是数分钟内，方向运动遇到流动性区域后，主动攻击、可见挂量消耗与补充、推进或退离、攻击活性改变之间的关系。三轮攻击、冰山及反转是原始故事假设，不能当作市场真值、固定顺序或本轮必须发现的模式。原始叙事 Chat 7/8 提出实证迭代；Chat 9/10/14 讨论既有特征、L1 与实现成本；Chat 28/29 明确业务 micro 与实际特征表达可替换。原文中的频率、胜率或典型性数字属于历史 AI 建议，本次不采用为验收阈值。

本轮需要分开看：对象是否延续、此刻可见量多大、期间承受多少可归属成交、补充是否跟得上、内部何时消退或恢复，以及后续价格/交互如何变化。Wall 活着不表示此刻仍异常厚；挂量下降不直接证明撤单或墙应终结；累积成交多也不直接证明真实冰山或反转。

## 现行正式职责与依赖

正式设计起点：[六 Feature 架构](https://github.com/daowei2026/feature-refinement-implementation-agent-evolution/blob/8d58ddd3392a3e67ef5ba44adf2c4cd0c9077f9f/candidate_gold_cases/eaw/taskpacks_and_checkpoints/p1/EAW_P1_PREL0_BASE_PRODUCTS_ENGINEERING_DESIGN_AND_VCC_V1_6_1_20260818/02_FINAL_P1_ARCHITECTURE.md)及同包 `01_EFFECTIVE_SCOPE_AND_REQUIREMENT_CORRECTIONS.md`、四个 `dsu/P1-DSU-0*.md`、`07_F4_MULTI_STREAM_AND_ATTACK_LOCAL_UNION.md`；已逐份读取并保存于本目录 `sources/`。

| 产品 | 业务职责与正式输出 | 依赖及解释边界 |
| --- | --- | --- |
| Wall | 流动性对象的 producer-local 身份、价带、Present/Dormant/Ended；Recognized、BandChanged、PresenceChanged、Ended 及 history/current view | 三个下游共用 exact Wall artifact。正式身份还需要 Wall FeatureRunIdentity，裸 wall_id 不可跨运行当相同对象。起墙与存续阈值不同，不能把 Alive 当作实时厚度。 |
| Build | 围绕 exact Wall 的一轮加固活动：Started、Milestone、Stopped | 使用 Wall 和方法所需方向压力材料；不消费 Attack/Absorb。只在其度量、时间窗口及触发允许时表达加固，不默认包含全部补充或负向挂量信息。 |
| AttackSegment | Numba 已完整形成的贴墙攻势段、FormationEvidence、WallRelationBarrier 三条材料；FRP 维护段簿 | 使用 Wall 和明确选择的 F4 实例；不消费 Build/Absorb。完整段在 closed_at 发生/发布，business_end 可早于该时点。在建段仅在 producer carry；普通 gap 不自动是 formal barrier。 |
| Absorb | 围绕 exact Wall 的局部挂单交互：Started、ConsumptionMilestone、Resolved | 有独立大挂量候选/跟踪及成交代理；不消费 Build/Attack。Resolved 不等于 Wall.End、Fate 或反转。 |
| F3/F4 与背景量 | 方向压力与方向大额成交；VolQuant/厚薄背景帮助解释入口与相对规模 | F4 资格族/参数实例分别对外，允许同 symbol/direction/UTI 多条；Attack 对同一底层半秒材料局部去重，保留资格标签。不得把 F4 当全部成交。 |

Numba 形成业务变化；FRP DSU 接纳 typed occurrence、核 exact upstream、维护 append-only history/current/publication，不重识别 Numba 对象。本批是否包含上述 FRP 正式产品须在 S02 核查，不能由合同或显示表推定。

## 已核到的设计取舍及计算入口

历史墙定义讨论已读大挂单入口风险（L4409–4669）、StrengthUp/Down 收缩与 Build/Absorb 分工（L5529–5819、L6050–6381）、L1 净新增修正（L7226–7305、L7445–7499）。历史 Burst/Grind 讨论已读相关小成交、跨墙及放弃 Dense 的段落（主要位于 L1052–1275、L1680–1775、L1990–2222）。均来自任务书指定原件；其中“罕见”“能兜底”等意见未经本次数据检验，不能沿用为结论。

1. 以异常大挂单起墙，之后以价带、存在感、存续/休眠恢复保持对象。无单档异常但持续补充、相邻档合力可能被入口遗漏，是研究线索；L1 不能直接验证完整深度合力。
2. 因稀疏化与重叠考虑，历史设计取消独立 StrengthUp/Down，寄望 Wall 生命周期、Build 和 Absorb 的属性/里程碑保留所需信息。是否足够必须查联合字段及完整历史，不能只数事件名。
3. 从全局 Dense 预筛选改向贴墙方向大成交组织 Attack，避免跨墙、聚合丢局部材料。持续小成交是否有重要业务信息需真实数据判断，不能事先认定被其他产品完全覆盖。
4. 历史 signed net_add 在同侧同价连续可见段定义为 Δq + C；只估计新增减撤减。参考 TIS 的 Build 已采用不同量：`max(visible_delta, 0) + attack_pressure_proxy`，并受 Alive、same-best、窗口和阈值约束。两者不能互称或用旧讨论直接解释本批 Build。
5. 参考 Absorb 保存 consumed proxy、visible remaining 与 replenish gap；其 `consumed - max(initial-visible_remaining,0)` 也不是总补单真值。Attack 则区分最后业务材料时点与闭段/正式可知时点。

参考代码固定为 [TIS@179016111ed0394f92025313e46bd13534932a74/hf/prel0](https://github.com/daowei2026/tis/tree/179016111ed0394f92025313e46bd13534932a74/hf/prel0)，已从本地 Git 对象只读导出 17 个指定入口至 `sources/tis-reference-179016/`：

- `wall_assembler.py`：双侧 exact state trace、稀疏生命周期及 wrapper 参数；`wall_assembler_core.py` 为状态识别入口。
- `build_assembler.py:207`、`build_assembler_core.py:128`：exact Wall receipt/axis、方向压力及上述 reload 公式。
- `attack_flow_assembler.py:740`、`attack_flow_assembler_core.py:813`：F4 多实例、内部合流、business_end/closed_at、FormationEvidence 与 Barrier。
- `absorb_assembler.py:272`、`absorb_assembler_core.py:328`：独立跟踪参数、consumed/visible/replenish。
- `tick_quote_context.py:154`：SubContinuousContract 输入、VolQuant 向后对齐；`pressure_big_deal_core.py:51`：方向列取绝对量、F3 比例分配及 same-best 命中。
- `p1_product_receipt.py:59`：产品实例、参数、source scope、code version、exact upstream 与 artifact location 是版本证明入口；`p1_dba_export.py`/`eaw_interface_contract.py` 为物化及字段入口。

仅进行了任务需要的语义与入口阅读，没有执行生产特征或全面正确性验收。

## 对三组对照的理解

| 对照 | 必须共同保留的信息 | 不能作出的跳跃 |
| --- | --- | --- |
| B1 成交背景近似、挂量演化不同 | 起始量/背景、方向成交与节奏、r/c/n、期间消退与恢复、前期运动、Wall 有/无/未知、全部可用联合输出 | 同价量变段内价格不变不能证明吸收；Alive 不等于实时厚；无新事件不等于无墙。 |
| B2 挂量变化近似、成交负荷不同 | 同侧同价的 Δq 与 C 分开记录、可见性、成交归属及来源依赖；比较静态维持、成交后维持、低成交消退 | n 不是真实总补单或真实撤单；若方向量由同一盘口变化估计，不能用它独立证明补充机制。 |
| B3 起止和累计量近似、中间形状不同 | 最低点、消退速度、恢复、分阶段量变/成交、实际发生与可知时间、片段及后续观察截断 | 最终同值不说明内部过程相同；显示缺字段不证明正式产物缺字段。 |

## 版本待核及可观测边界（交 S02）

本批实际行情、特征的生成 commit、参数实例、exact upstream、FRP 是否执行、窗口起点状态和历史完整性均待实查。TIS 参考 commit、FRP@cac6c912dd65a14acbd591ca57e0afd8ddb4ef13 仅为任务提供的参考，不能写成本批已确认版本。方向成交列是候选代理，须查是否来自盘口估计；无独立撤单 feed、无完整深度，不能恢复订单/参与者身份或意图。

原件追溯：三份历史讨论的任务书 main 链接在读取时已固定到 FRIA@77d75079b64ff6f1d22bf8b6e18ae9aba45c17a8；这是证据快照，不改变专业任务采用版本。完整原文、正式合同及代码快照保留 `sources/`，具体来源和哈希另见 `SOURCE_INDEX.json`。

任务书副本核对：exact 原件与 C0001 副本均为 52,362 bytes、SHA-256 `fa80b5eaf52a03edde167b5e13dc463c5b92c6dbea11a03f420e1c3e11a80089`。controller 提示路径副本仅多一个末尾换行；已改用 exact 副本，不存在业务条款差异。
