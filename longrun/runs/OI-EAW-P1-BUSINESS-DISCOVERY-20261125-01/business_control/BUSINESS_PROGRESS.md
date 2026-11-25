# BUSINESS_PROGRESS｜EAW P1 挂单—成交演化的业务迭代点发现

## 一、当前进展

S01～S06、R1与R2各条S07＋S08均已完成并消费。R2保持研究线索：已有展示/L1联合可恢复数量角色、基线参考价、同价/近价对象与时点区别；参考投影有明确语义位置，本批正式链第一损失仍待证。正式缺口、必须修改、生产Bug、有充分依据/初步改进依据点均未确认。

现已签发[D009](../delegations/D009/DELEGATION.md)，仅组织R3共同来源可识别性的S07＋S08，待controller派达同一E1。已核共同来源证据复用，不另开独立真实补撤分解研究。R3真实成果回manager消费后再安排后继，S09仍单独。父Run为IN_PROGRESS。

## 二、R2实际成果与新认识

定向扫描17,863条来源引用、16,710去重逻辑记录，9,526条可锚定联合事件。主同价条件为里程碑、累计/基线≥1、当时最优价等于Wall core且展示段起点量可核：483事件/289活动/209 local Wall/83PG/22日期块中，219事件当前量≤展示段起点量1/4；每PG一条敏感性38/83。这是所选窗口的条件范围，重复事件不是独立攻防或全市场频率。

| 新案例 | 已有信息能区分什么 |
| --- | --- |
| R2-01 活动与存量 | Wall展示起量1844、Build基线369、累计1499.8511，而切点同价量271；活动累计约4倍不等于当前墙厚4倍 |
| R2-02 对象价位 | 当前4359量56不是旧4360墙当前库存，后者在当时不可见 |
| R2-03 可知时间 | Absorb“阻挡”在切点后2秒才展示，不能倒用为切点已知事实 |
| R2-04 普通反例 | 当前728.5量894高于展示起量866，但Build基线取起点729量48；不能把每个活动都解释成库存下降 |

四例来自此前未深入的不同PG、不同local Wall和源日期块，均非R2原形成Wall，但已有R1程序暴露。659行quote、174条P1来源引用不是独立事件计数。固定10/30/60秒可用例数4/3/3，R2-03仅27.5秒，方向混合且非匹配预测对照，缺失保留。日期块为源标签，R2-02实际11月2日而DB标签11月1日，不冒充精确交易日核验。

关键参考定位：FRP Build milestone读取门槛level，而非raw观测ratio；typed payload未承接raw baseline/观测ratio，不能用累计量/typed门槛反算真实基线。原始1585条里程碑中1579条观测ratio与level不同、6条相同。这是语义区别，不是生产错误率；actual producer/FRP版本未证，不能由参考投影直接宣布实际完整联合链缺口。

## 三、两标签试查与证据边界

43事件/43PG/21日期块的试查只增加quantity_role和time_basis两个字符串，原数值不改、新数值为0。29个切点最佳价在Wall价带外、22个基线起点价在价带外、42个raw观测ratio不同于level；1个相等普通例保留。8个较晚Resolved仅入后验审计，不进入切点输入。

两标签明确已有量的业务主语、参考价/参考量及发生/切点/未知正式发布边界，没有增加原先缺失的市场事实。未运行真实P2、未测误读率或生产/预测收益，不能据此升级为初步改进依据。试查43PG均继承R1暴露，41PG还曾有特定指标访问，不称未开封或严格留出，也不计作43次深入提取。

最强可支持是已有信息的消费/表达要求及需核对的参考投影。actual版本/参数receipt/exact身份、相容完整occurrence/current/publication与实际P2仍缺；展示UTI/闭段不等于正式发布时间。实际合法接口能否在切点取得基线/参考价、区分ratio/level并取得已发布历史，仍是后继设计问题，未被本次完成态解决。[R2定位原件](https://github.com/daowei2026/observe-iterate/blob/8cf263c0b2c2ada6b6916f093d5431c3a966cb82/longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261125-01/calls/C0015/R2_DESIGN_POSITIONING.md)、[机读结果](https://github.com/daowei2026/observe-iterate/blob/8cf263c0b2c2ada6b6916f093d5431c3a966cb82/longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261125-01/calls/C0015/report/R2_RESULT.json)给准确边界。

## 四、逐项后继与使用状态

| 工作 | 真实状态与去向 |
| --- | --- |
| S01～S06 | 三入口及三组对照实际完成，原18组36深入区间和归并继续有效 |
| R1 / D007 | 已完成并消费；独立可见量/阶段证据与试查，正式链待证，优先已有信息消费 |
| R2 / D008 | 已完成并由C0016消费；四类区别可恢复、参考投影定位及两标签试查，仍研究线索 |
| R3 / D009 | 原共同来源约束尚未独立结案；本次只处理可得来源/计量/时间归属/完整性及proxy可用性表达与准确去向，已签待派 |
| S09 | 待真实后继及原任务整体结束依据，单独委派 |

R3继续遵守“真实补撤单独证明暂不优先投入”。已经核过的C/n同源、R1/R2局部缺件和已有来源语义复用；没有独立真值/有条件计量证据时停止真实分解推断，保留可见活动结论。不能从当前不可识别推出真实撤单不存在、无业务价值或产品缺字段。可行且有价值时按原任务最小信息试查，已有信息充分则承认，不新增审批或专业复审。

累计使用保留原210条，现257条、69次深入提取；上游139个特定唯一区间ID保留，R2事件/PG记录单位不同，不加成186区间。R1全批形态/交互暴露和R2联合110PG/23日期块访问继续记录，未深入不等于未见。详细账按冻结本地索引可查，不编造附件远端ref。

## 五、成果入口与接续

| 入口 | 内容 |
| --- | --- |
| [R2报告](https://github.com/daowei2026/observe-iterate/blob/8cf263c0b2c2ada6b6916f093d5431c3a966cb82/longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261125-01/calls/C0015/EXECUTOR_REPORT.md)、[案例册](https://github.com/daowei2026/observe-iterate/blob/8cf263c0b2c2ada6b6916f093d5431c3a966cb82/longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261125-01/calls/C0015/R2_CASEBOOK.md) | 四例真实数值、已有信息、普通/时点/对象反例及限制 |
| [S07证据](https://github.com/daowei2026/observe-iterate/blob/8cf263c0b2c2ada6b6916f093d5431c3a966cb82/longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261125-01/calls/C0015/S07_EVIDENCE.md)、[S08定位](https://github.com/daowei2026/observe-iterate/blob/8cf263c0b2c2ada6b6916f093d5431c3a966cb82/longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261125-01/calls/C0015/R2_DESIGN_POSITIONING.md) | 条件分母、角色/对象/时点、准确参考出处与正式链待证 |
| [条件统计](https://github.com/daowei2026/observe-iterate/blob/8cf263c0b2c2ada6b6916f093d5431c3a966cb82/longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261125-01/calls/C0015/report/R2_STATISTICS.json)、[两标签试查](https://github.com/daowei2026/observe-iterate/blob/8cf263c0b2c2ada6b6916f093d5431c3a966cb82/longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261125-01/calls/C0015/report/MINIMAL_PROBE_SUMMARY.json) | 对象/PG敏感性、原值不改的语义试查及失败边界 |
| [75项冻结索引](https://github.com/daowei2026/observe-iterate/blob/8cf263c0b2c2ada6b6916f093d5431c3a966cb82/longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261125-01/calls/C0015/ARTIFACT_INDEX.json)、[来源索引](https://github.com/daowei2026/observe-iterate/blob/8cf263c0b2c2ada6b6916f093d5431c3a966cb82/longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261125-01/calls/C0015/SOURCE_INDEX.json) | files/local_path准确本地路径、大小/hash及版本界限 |

最新专业根：`/dwdhome/fy/BASE_E6_2/artifacts/oi-eaw-p1-business-discovery-20261125-01/calls/C0015/`。旧C0013/C0011/C0009/C0007/C0005/C0002成果复用，详细表/图/代码无需重发。技术恢复见[TASK_PROGRESS](TASK_PROGRESS.md)，本次消费见[C0016报告](../calls/C0016/MANAGER_REPORT.md)。

controller向同一E1派达D009，manager在R3真实业务节点消费后安排后继。局部正式材料不足不阻断其余可做工作，不预设必须形成研发点或整批已结束；S09单独，不新增分析计划或Owner审批。

更新时间：2026-11-25T23:19:56.703Z
