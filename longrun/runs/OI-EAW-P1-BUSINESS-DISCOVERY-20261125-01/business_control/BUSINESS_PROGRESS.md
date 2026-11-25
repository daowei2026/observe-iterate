# BUSINESS_PROGRESS｜EAW P1 挂单—成交演化的业务迭代点发现

## 一、当前任务与整体情况

本轮仍以Owner给定的同批真实Tick窗口为范围，寻找有真实证据、可指向具体设计的EAW P1业务迭代点。

S01业务理解、S02数据接入及S03全范围候选检索已经实际完成并被manager消费。现已签发独立S04/B1对照，待controller派达同一E1。候选表中的研究位置尚不构成业务迭代点；第一轮B1/B2/B3深入对照尚未完成，父任务仍在进行。

## 二、已经开展的工作与结果

| 工作 | 实际成果 | 当前状态与入口 |
| --- | --- | --- |
| S01业务及特征理解 | 四特征职责、共同Wall依赖与互不消费关系、历史入口/稀疏化取舍、可观测性及版本边界 | 已完成并消费，原S01记录继续有效 |
| S02数据接入与版本核查 | 148窗口、rb/hc/i、444单元；文件/字段/时间/去重/有效性及发现/预留索引；正式历史与方向真值限制明确 | 本步已完成并消费，原C0002材料复用 |
| S03全范围候选检索 | 888窗口×品种×侧中886有有效范围、2全侧排除、未处理0；190,829完整同价观察段、261,497去重研究区间；三入口、分布、对照位置及重放程序已形成 | 已完成并由本次manager消费；[E1原报告](https://github.com/daowei2026/observe-iterate/blob/b9f722c3802b3380081946eb957a2c856f6466f9/longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261125-01/calls/C0005/EXECUTOR_REPORT.md) |
| S04第一轮B1 | 待比较成交背景近似而可见流动性演化不同的真实过程，初筛业务价值与当前表达 | 已独立签发，待实际执行；[D004](../delegations/D004/DELEGATION.md) |
| S05/S06第一轮B2/B3 | 依真实业务节点分别组织，不因B1有线索而跳过 | 待输入，未委派 |
| 逐候选S07＋S08、最终S09 | 后续按候选逐条深化并单独归并交付 | 尚无相应成果，未委派 |

## 三、当前研究材料说明与限制

三入口已实际尝试。以190,829完整同价片段为人口、片段或其尾窗任一命中计：局部相对大挂单17,089、显著量变74,779、累计报价代理负荷20,712；并集85,036，未命中105,793仍全部保留。各入口可重合，这些不是独立案例数或全市场频率，也不是三组深入对照已经完成。

| 已核材料事实 | 后继解释边界 |
| --- | --- |
| C_quote与可见减少量同源，n_quote与正向可见变化累计/q0恒等 | 不能独立证明真实成交消耗、补单或净新增；B1成交可比性只能按实际证据表述，局部受限部分保持待证 |
| 大挂量采用仅此前的局部窗口背景；大量同价段很短或单点，尾窗会截短 | 不等同正式历史VolQuant或完整名义时长；保留真实边界和后续可用性 |
| Wall匹配是展示对象上下文，未匹配为unknown；正式版本、参数、exact upstream及完整历史/发布仍未证实 | 不把无展示当无墙、把展示缺失当正式表达缺口；P1引用关系和可知时点仍需相容证据 |
| 发现95/预留53窗口；S03仅全范围通用程序量，未深读预留形成假设 | 保留同批复现机会及实际使用追溯；重复、多宽度复用与保守分组不冒充独立复现 |

目前没有已确认的市场差异、候选迭代点或正式设计缺陷。本次取得的是可追溯的研究位置集合和实际可用边界，将由S04及后续真实对照建立业务认识。

## 四、可以直接查看的成果

| 成果 | 用途 | 原件入口 |
| --- | --- | --- |
| S03原报告 | 覆盖、三入口、去重、分布、对照材料和局部限制 | [EXECUTOR_REPORT](https://github.com/daowei2026/observe-iterate/blob/b9f722c3802b3380081946eb957a2c856f6466f9/longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261125-01/calls/C0005/EXECUTOR_REPORT.md) |
| S03冻结索引 | 33项报告、候选表、分布、显示引用、使用索引、代码及真实核查历史的路径/大小/哈希 | [ARTIFACT_INDEX](https://github.com/daowei2026/observe-iterate/blob/b9f722c3802b3380081946eb957a2c856f6466f9/longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261125-01/calls/C0005/ARTIFACT_INDEX.json) |
| S03来源/摘要/自检 | 实际输入及版本、口径/人口和E1核查结果 | [SOURCE_INDEX](https://github.com/daowei2026/observe-iterate/blob/b9f722c3802b3380081946eb957a2c856f6466f9/longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261125-01/calls/C0005/SOURCE_INDEX.json)、[SUMMARY](https://github.com/daowei2026/observe-iterate/blob/b9f722c3802b3380081946eb957a2c856f6466f9/longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261125-01/calls/C0005/report/S03_SUMMARY.json)、[VERIFICATION](https://github.com/daowei2026/observe-iterate/blob/b9f722c3802b3380081946eb957a2c856f6466f9/longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261125-01/calls/C0005/report/VERIFICATION.json) |
| 独立S04委派 | 承接S03候选表及原证据限制，开展第一轮B1 | [D004](../delegations/D004/DELEGATION.md) |

详细专业材料位于 `/dwdhome/fy/BASE_E6_2/artifacts/oi-eaw-p1-business-discovery-20261125-01/calls/C0005/`，由原冻结索引核查，不重复远端发布大表。S01/S02的原报告与冻结索引仍有效。

## 五、下一步

controller派达D004/S04至既有E1，按任务书默认约4～6个高质量B1真实对照组开展初步深入，不凑数、不把孤例直接当充分迭代依据；实际可比性、业务影响、表达初筛和限制由E1依原任务研究。manager在本业务节点消费真实成果后，另行组织独立S05；其余步骤沿Owner最新粒度接续，不新增专业复审或Owner审批。

技术恢复见 [TASK_PROGRESS](TASK_PROGRESS.md)，本次真实消费及后继见 [C0006报告](../calls/C0006/MANAGER_REPORT.md)。旧D001被替代历史及已完成工作保持，不重启Run或重放旧C。

更新时间：2026-11-25T17:31:31.212Z
