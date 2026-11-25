# BUSINESS_PROGRESS｜EAW P1 挂单—成交演化的业务迭代点发现

## 一、当前任务与整体情况

本次继续在Owner指定的同批真实Tick窗口内，寻找有真实数据依据、能指向具体业务设计的EAW P1迭代点。

S01业务理解、S02数据核查、S03候选检索和S04第一轮B1对照已经实际完成并消费。S04形成六组、十二个真实案例：五组标准可观测量匹配、一组放宽条件的Wall补救对照，质量单列。当前两项方向都保持“研究线索”，正式表达缺口待证，已确认必须修改的正式设计为0。下一项独立S05/B2已经签发，待controller派达同一E1；父任务未完成。

## 二、实际工作与结果

| 工作 | 已取得的真实成果 | 当前状态与入口 |
| --- | --- | --- |
| S01＋S02 | 特征职责/依赖/业务边界，148窗口与实际数据/版本/有效性/独立性记录 | 已完成并消费，原C0002材料继续有效 |
| S03 | 全部有效范围三入口检索，190,829完整同价观察段、261,497去重研究区间，分布/对照/来源/使用索引 | 已完成并消费，原C0005候选表继续有效 |
| S04第一轮B1 | 6组12例、真实原始数值、六组对齐图/PDF、全部取得联合展示属性、反例和初步业务/表达判断 | 已完成并消费；[原专业报告](https://github.com/daowei2026/observe-iterate/blob/3cc71052916ed182f19ba76464c9ad213cc85d0b/longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261125-01/calls/C0007/EXECUTOR_REPORT.md)、[案例册](https://github.com/daowei2026/observe-iterate/blob/3cc71052916ed182f19ba76464c9ad213cc85d0b/longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261125-01/calls/C0007/B1_CASEBOOK.md) |
| S05第一轮B2 | 将独立研究挂量变化近似而成交负荷不同的过程，不能用B1结果替代 | 已签发待派；[D005](../delegations/D005/DELEGATION.md) |
| S06第一轮B3及归并 | 等待S05实际成果，单独组织B3和线索归并 | 未委派 |
| 逐候选S07＋S08、最终S09 | 后续按实际候选逐条深化并独立归并交付 | 未委派，尚未达到父任务结束条件 |

五组“标准”只指已用可观测量匹配。原始总成交无方向真值，C_quote与可见减量同源，不能把六组称为真实攻击背景已相同；粗时段、跨日期/连续合约和其他背景仍有混杂。Wall补救组不与五组混称同质量。

## 三、重要认识与当前成熟度

| 方向 | 真实过程及业务含义 | 已有信息、限制与下一步 | 当前等级 |
| --- | --- | --- | --- |
| H1 接触时的当前可见量、恢复与同价复见关系 | B1-01 A段末量139，2秒后同价复见量2；B1-03 A最低4后回20。旧段末量或“始终维持”可能混淆再次接触时的实际可见流动性及期间薄弱 | 需要核相容正式联合信息和接触关系；如果现有信息可恢复，应定位上层组合，而非新增同义P1量；未证明普遍性或预测价值 | **研究线索，正式缺口待证** |
| H2 Wall/Build活动历史与当前存量的联合解释 | B1-05-B Wall60164延续、可见量94→98→5→12；Build baseline=5、cum=177、ratio=35.4。活动比值不能解释为原起量已恢复35倍 | 既有baseline/cum、较早Absorb/Attack历史已提供区别；优先核完整历史、当前存量和可知时间的联合阅读，不预设重启StrengthDown或改Build算法 | **研究线索，正式缺口待证** |

以上认识及等级直接来自[E1原报告](https://github.com/daowei2026/observe-iterate/blob/3cc71052916ed182f19ba76464c9ad213cc85d0b/longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261125-01/calls/C0007/EXECUTOR_REPORT.md)与[摘要](https://github.com/daowei2026/observe-iterate/blob/3cc71052916ed182f19ba76464c9ad213cc85d0b/longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261125-01/calls/C0007/report/S04_SUMMARY.json)。缺实际producer/FRP版本、exact身份/upstream、参数receipt及完整正式history/current/发布时间，目前尚不能确认正式表达第一处损失或“过迟”，也未证明研发优先级。

保留的反例和边界有实际意义：B1-06在30秒的攻击方向位移为A +4、B −5.5，不能沿用“末量保留更多就一定更能阻挡”的简单预测；B1-04两例均退离，不能把B减A为正直接讲成突破。位移单位是数据内观察格点，不是已核实合约ticksize。B1-03 A只有47.5秒后期可用，60秒保持不可用，没有补0或换例。

## 四、材料范围、复用和可查看入口

十二例来自发现部分，落在11个保守PG、10个日期关联块；PG021跨组复用和同日跨品种相关性保留，不冒充已证明独立攻防数。预留53窗口/50组未深入、未参与线索形成。累计使用记录保留22个选样数值已见唯一区间、12次深入提取；初版另10个区间不再称为全未见。

| 成果 | 用途 | 入口 |
| --- | --- | --- |
| S04原报告及案例册 | 真实对照、标准/放宽质量、业务认识、完整联合展示与反例 | [EXECUTOR_REPORT](https://github.com/daowei2026/observe-iterate/blob/3cc71052916ed182f19ba76464c9ad213cc85d0b/longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261125-01/calls/C0007/EXECUTOR_REPORT.md)、[B1_CASEBOOK](https://github.com/daowei2026/observe-iterate/blob/3cc71052916ed182f19ba76464c9ad213cc85d0b/longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261125-01/calls/C0007/B1_CASEBOOK.md) |
| 冻结产物索引 | 103项报告、cases/数值、图/PDF、选样/冻结、累计使用和研究代码的准确路径/大小/哈希 | [ARTIFACT_INDEX](https://github.com/daowei2026/observe-iterate/blob/3cc71052916ed182f19ba76464c9ad213cc85d0b/longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261125-01/calls/C0007/ARTIFACT_INDEX.json) |
| 来源、摘要及E1自检 | 采用版本、结果/等级、实际核查及其边界 | [SOURCE_INDEX](https://github.com/daowei2026/observe-iterate/blob/3cc71052916ed182f19ba76464c9ad213cc85d0b/longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261125-01/calls/C0007/SOURCE_INDEX.json)、[S04_SUMMARY](https://github.com/daowei2026/observe-iterate/blob/3cc71052916ed182f19ba76464c9ad213cc85d0b/longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261125-01/calls/C0007/report/S04_SUMMARY.json)、[VERIFICATION](https://github.com/daowei2026/observe-iterate/blob/3cc71052916ed182f19ba76464c9ad213cc85d0b/longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261125-01/calls/C0007/report/VERIFICATION.json) |
| 独立S05委派 | 承接S03候选表和S04可复用材料，形成独立B2结果 | [D005](../delegations/D005/DELEGATION.md) |

详细专业根为 `/dwdhome/fy/BASE_E6_2/artifacts/oi-eaw-p1-business-discovery-20261125-01/calls/C0007/`。累计使用记录和图/大表等按准确冻结索引在本地核查，不要求每项远端发布；没有为未发布附件编造远端入口。原C0005候选及C0002上游资料保持有效。

方向代理同源、正式VolQuant/完整正式历史不足、无展示为Wall未知、窗口截断和连续边界仍限制相关判断；不会由材料缺件推成产品缺信息。这些局部限制不阻断其他可执行研究。

## 五、下一步

controller将D005派达同一E1，独立完成任务书S05/B2，并按原要求记录可比性、原始事实、业务差别、表达核查、候选成熟度、不足及反例。H1/H2保留作实际上下文，不把它们预设为必须确认的缺陷。manager消费B2真实成果后另行组织独立S06，再按Owner粒度逐候选S07＋S08、独立S09，不新增专业复审、分析计划或Owner审批。

技术恢复见 [TASK_PROGRESS](TASK_PROGRESS.md)，本次消费及后继见 [C0008报告](../calls/C0008/MANAGER_REPORT.md)。旧委派、历史版本与样本暴露记录保留，不重启Run或重放旧C。

更新时间：2026-11-25T18:39:09.090Z
