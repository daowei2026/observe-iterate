# BUSINESS_PROGRESS｜EAW P1 挂单—成交演化的业务迭代点发现

## 一、当前进展

S01～S06已实际完成并消费。三方向各六组、第一轮共18组36个深入区间已形成，归并为R1/R2/R3三条后继取证项，均保持研究线索。候选迭代点、有充分依据点、具有初步改进依据点均为0；正式设计缺口、确认必须修改及生产实现Bug未确认。

现已签发[D007](../delegations/D007/DELEGATION.md)，仅处理R1“当前接触与阶段性可见流动性”的S07＋S08，待controller派达同一E1。R1真实成果回交后消费，再安排后继；R2随后聚焦，R3随依赖核来源，S09单独。父任务仍未完成。

## 二、实际成果

| 工作 | 实际结果 | 状态 |
| --- | --- | --- |
| S01＋S02 | 业务/特征职责、同批真实材料及版本/独立性审计 | 已完成并消费，原C0002材料复用 |
| S03 | 全有效范围三个入口检索，261,497去重研究区间 | 已完成并消费，C0005候选表复用 |
| S04/B1 | 六组十二例，5标准/1放宽，H1/H2及反例/限制 | 已完成并消费，原C0007证据保留 |
| S05/B2 | 独立六组十二例，B2-L1/L2、同源代理限制与反例 | 已完成并消费，原C0009证据保留 |
| S06/B3及归并 | 六组十二例，4标准/2放宽补救；三方向归并、逐项等级与后继清单 | 已完成并消费；[原报告](https://github.com/daowei2026/observe-iterate/blob/0e52ad9a51f2bc3803b2343b4b06daed616e91fa/longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261125-01/calls/C0011/EXECUTOR_REPORT.md)、[归并原件](https://github.com/daowei2026/observe-iterate/blob/0e52ad9a51f2bc3803b2343b4b06daed616e91fa/longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261125-01/calls/C0011/FIRST_ROUND_SYNTHESIS.md) |
| R1第二轮S07＋S08 | 待补独立过程证据、影响范围/反例及相容正式表达定位，可行时最小信息试查 | D007已签待派，尚无实际结果 |
| R2/R3后继、S09 | 按真实业务节点接续，保留共同来源限制和未决去向 | 未完成，不提前合并整轮 |

## 三、已有认识与证据等级

| 取证项 | 已知业务差别、已有信息和局限 | 后继处理 |
| --- | --- | --- |
| R1 当前接触与阶段性可见流动性 | 近似端点/累计量仍可对应不同中途最低量、下降集中度或阶段位置；L1完整路径本来能恢复量，研究摘要不足不等于P1缺口 | 研究线索，顺序1；D007单条S07＋S08 |
| R2 活动基线、同价/近价对象与可知时间 | Wall/Build/Absorb已有联合属性能恢复部分差别；当前量、Wall展示起量、Build基线有不同参考时段，近价对象不能当同价对象 | 研究线索，顺序2；R1消费后聚焦另签，优先承认已有信息 |
| R3 真实消耗/净撤减来源 | C_quote/正向活动来自同源报价，不能独立分解真实成交和撤减，多事件不构成真值互证 | 研究线索/共同观测约束，随R1/R2核查；独立证明暂不优先，未记结案 |

等级与顺序直接来自[E1归并原件](https://github.com/daowei2026/observe-iterate/blob/0e52ad9a51f2bc3803b2343b4b06daed616e91fa/longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261125-01/calls/C0011/FIRST_ROUND_SYNTHESIS.md)和[逐项记录](https://github.com/daowei2026/observe-iterate/blob/0e52ad9a51f2bc3803b2343b4b06daed616e91fa/longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261125-01/calls/C0011/report/CANDIDATE_REGISTER.json)，属于后继研究顺序，不是研发优先级；未据此重启StrengthDown、负Build或新增事件。

B3提供的实际例子包括：B3-01末量和累计量近似，最低比例却为1/.278；B3-02总成交均83，最大单次减少占比.421/.954；B3-03前半减少63/2而累计65/67；B3-06累计代理C均27，中间量55/2。它们说明摘要不能唯一恢复路径，正式链第一处损失仍待定位。阶段n_second=22/2=11与整体n=22/29是研究分母不同，不是生产Bug。

两组放宽补救质量单列：B3-04不是真正最低量也相同的纯恢复时点实验；B3-05同价/近价Wall状态不一致。已有Wall/Build/Absorb对象、基线及阶段属性可区分处保留；Absorb replenishment325与本例正向可见变化325相等，不证明任意子段真实补单。

后期10/30/60秒完整配对为6/6/4。30秒B减A为−3、−2、+6、+1、0、−14观察格点，各组形状轴不同，不平均为统一效果。B3-03到60秒反转，B3-01/06短暂极薄后恢复侧反而推进更少，B3-05两例30秒均−2；截断保留NA、不换例不补0，不能推广预测或因果。

本批producer/FRP版本、相容receipt/参数、正式exact身份/upstream、完整history/current与发布时间仍缺；425行可得P1和含空表的展示记录不等于完整正式历史。参考代码不替换本批版本，空展示不证明正式无输出，没有P2实物不声称P2误读。缺件只局部限制依赖它的结论，其余可得业务证据继续。

## 四、样本依赖与成果入口

第一轮36个深入区间落33保守PG、12日期块，不是36个独立攻防。PG039/PG118跨方向相关、B1内部PG021复用及B2关联初版PG018保留；没有相同候选/同价片段跨方向重做，仍不能当独立复现。累计46个数值回看唯一区间含10个初版未最终选入区间、36次深入提取；旧58条使用记录保留，现82条。53预留窗口/50保守组尚未深入，是否足够可比须实际查，不预先承诺复现数或严格留出验证。

| 成果 | 内容 | 入口 |
| --- | --- | --- |
| S06报告/案例册 | B3真实轨迹、匹配/补救、联合表达、反例与限制 | [EXECUTOR_REPORT](https://github.com/daowei2026/observe-iterate/blob/0e52ad9a51f2bc3803b2343b4b06daed616e91fa/longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261125-01/calls/C0011/EXECUTOR_REPORT.md)、[B3_CASEBOOK](https://github.com/daowei2026/observe-iterate/blob/0e52ad9a51f2bc3803b2343b4b06daed616e91fa/longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261125-01/calls/C0011/B3_CASEBOOK.md) |
| 归并与逐项原件 | R1/R2/R3来源、原级认识、已有信息、后继问题和去向 | [FIRST_ROUND_SYNTHESIS](https://github.com/daowei2026/observe-iterate/blob/0e52ad9a51f2bc3803b2343b4b06daed616e91fa/longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261125-01/calls/C0011/FIRST_ROUND_SYNTHESIS.md)、[CANDIDATE_REGISTER](https://github.com/daowei2026/observe-iterate/blob/0e52ad9a51f2bc3803b2343b4b06daed616e91fa/longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261125-01/calls/C0011/report/CANDIDATE_REGISTER.json) |
| 125项冻结索引及来源 | 图/数值/代码/累计使用/首轮依赖的准确路径、大小、hash及版本来源 | [ARTIFACT_INDEX](https://github.com/daowei2026/observe-iterate/blob/0e52ad9a51f2bc3803b2343b4b06daed616e91fa/longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261125-01/calls/C0011/ARTIFACT_INDEX.json)、[SOURCE_INDEX](https://github.com/daowei2026/observe-iterate/blob/0e52ad9a51f2bc3803b2343b4b06daed616e91fa/longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261125-01/calls/C0011/SOURCE_INDEX.json) |
| 摘要与E1自检 | 真实工作量、等级计数、依赖和核查范围 | [S06_SUMMARY](https://github.com/daowei2026/observe-iterate/blob/0e52ad9a51f2bc3803b2343b4b06daed616e91fa/longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261125-01/calls/C0011/report/S06_SUMMARY.json)、[VERIFICATION](https://github.com/daowei2026/observe-iterate/blob/0e52ad9a51f2bc3803b2343b4b06daed616e91fa/longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261125-01/calls/C0011/report/VERIFICATION.json) |

详细专业根：`/dwdhome/fy/BASE_E6_2/artifacts/oi-eaw-p1-business-discovery-20261125-01/calls/C0011/`。本地累计使用/首轮关系表按冻结索引定位，不编造附件远端ref；已有大表、图及程序无需重发。C0009/C0007/C0005/C0002原成果继续有效。

## 五、当前后继

controller向现有E1派达D007。R1依原任务§6.3与§7补真实独立过程、条件分母/范围、业务影响、反例和正式联合表达证据，可行且有价值时试查最小信息；完成本条S07＋S08后回manager消费，再据真实认识安排R2等后继，S09单独。不新增专业复审、分析计划或Owner审批，也不预定本条必须形成修改。

技术恢复见[TASK_PROGRESS](TASK_PROGRESS.md)，本次消费及后继见[C0012报告](../calls/C0012/MANAGER_REPORT.md)。原历史、质量差异、暴露依赖和成熟度保留，父Run仍IN_PROGRESS。

更新时间：2026-11-25T20:56:06.957Z
