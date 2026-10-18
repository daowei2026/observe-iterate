# 主Case五个知识截面的连续解释与F05反证

work_id: BI-01
run_id: BI-01-V2-01
invocation_id: BI01-V2-01-R0010-9c54d7a73e2bd619ee5d9f47
assignment_token: 99ff37c6ea307fb90ba24f046e
role: professional
professional_mode: OBSERVATION_SCOPE

本文件是本轮按业务问题保存的实证正文，不是新的控制表、工单、管理接收或全目标完成。原完整S1—S3及广域/未覆盖责任不变。当前图数读取根固定为`observe-iterate@b9ecbfa4b27f40365ed72f35448116420fb085a6:runs/BI-01-V2-01/artifacts/worker-R0004/readable_views/REQUESTED_51_CURRENT/`。本文件路径中的node、known/retrospective和原行都是实际对应关系；保留R7逐字段可知限制，不把known整行的未来完成辅助字段用于当时判断。

## P10-03：同一参考组织能够持续存档，不代表三个成员当下仍是同一运动

### 真实对象、截面与原资格

主参考对象`refonly-ad8824a52552d7bffa91`共同actual为2021-04-30 15:00，五个As-Of是5月6/7/11/14/18日10:00。Owner入口分别为`http://192.168.11.40:6244/graph/cae/5781/report`至5785，使用既有内网/服务；本专业者读取结构化数据，不声称亲自打开像素。

R6已经实际读取并由R7接收的同图R02 15行、N1 15行、N2 120行和R03 15行，按原版本和资格复用。本轮补读MAIN_ASOF_2—5的known CASE_C1全文，MAIN_ASOF_2的CASE_S/CASE_C2全文，以及下面实际known价格/端点层。来源绑定MAIN_ASOF_2/SOURCE_BINDING.json与UNCOVERED_01为同一个Git blob `7a8cc3fd8fd0864153c5608f970851881ec37886`；实际取得相关原source-member及SHA正文，不由名字猜测输出。

| As-Of | 原C1状态及epoch_processed_bars | 原R02的测量对象 | 能回答的问题及限制 |
|---|---|---|---|
| 5月6日10:00 | FormationWorking/QualificationPending/ValidityPending，2 | 三品种Up Working2 | 已知共同锚点之后的很短前缀；跨日期跃升不等于很多根连续推进 |
| 5月7日10:00 | FormationAccepted/QualifiedWorking/ValidityAcceptedWorking，14 | hc/rb Working14，i Completed1 | hc/rb可在同原区间描述峰值保持差异；不能把组名QualifiedWorking解释成三个成员都在同长Working段 |
| 5月11日10:00 | 同上，38 | hc Working38，rb Completed33，i Completed1 | 混合端点与生命周期；不按效率或保持率跨对象排名 |
| 5月14日10:00 | FormationAccepted/QualifiedCompleted/ValidityAcceptedCompleted，74 | 三者旧锚定段均Completed | 正在存档的原历史段，不是截至当时的连续质量序列 |
| 5月18日10:00 | 同上，98 | 旧R02不变，N的当前段与recent/prior历史仍滚动 | 原对象可追溯有用，不自动证明当前方向或资金资格保持 |

新读的CASE_C1各表物理2行分别对应固定A的`single_scale_U2_C1_S_C2_U3/C1/03_case_formation_and_three_assessments.csv`物理3—6行。共同理由原文是`all_members_positive_mature_reference`；formal_assessments_committed仍NO。其epoch条数描述组参考时钟，不可暗换为每个成员都观察了14/38/74/98个间隔。原参考方法允许组织历史段事实；本轮不据上述混合状态断言计算错误，指出的是实际消费问题和需要保留的解释边界。

MAIN_ASOF_2/known CASE_S物理2行（原S物理3）outside_count=0，evidence_count_reference=13，elapsed_reference_bar_positions=12，required_k=3，required_elapsed_bars=8，ValidEmptyPersistent，observation_proof为`30M_CANONICAL_BAR_FRONTIER_ASSUMED_ELIGIBLE_PER_BAR_REFERENCE`。13不是13次独立组外比较，更不是13个差品种。该样本没有非空组外，不能证明外部分离优势。

同节点CASE_C2原物理3行：four_gate_reference_pass=True，但prior_cluster_domain=`NOT_EVALUATED_ALL_HISTORICAL_EPOCHS`，verdict=`SHADOW_ELIGIBLE_NEEDS_PRIOR_CATALOG_AND_PUBLICATION`，official_cluster_committed/official_h1_emitted均NO。由此保留参考链组织意义，不升级为正式机会簇或已通过完整Network增量Gate。

### 新读价格使历史端点与当前保持的区别落到真实过程

MAIN_ASOF_3/known/hc-ohlc物理90—95（原KLine970—975）实际完整序列：5月10日21:30 close6482→22:00 6421→22:30 6443→23:00 6369→5月11日09:30 6364→10:00 6354。不是从两个端点猜出过程，六行已直接读取。5月11日10:00尚不能用该行保留的未来完成代理5月11日10:30，反过来在当时把hc标为Completed。

MAIN_ASOF_4/known/hc-completed-episodes全文物理2—8，原C0E403—409。主Episode原406：4月30日15:00 5684→5月10日21:30 6482，start_turn_known_from_proxy=5月6日10:00，completed_visible_from_proxy=5月11日10:30。到5月14日它确实是当时已经可知的历史完成段。

同cut known hc-ohlc物理125—131（原1005—1011）为：5月13日15:00 6429→21:30 6310→22:00 6348→22:30 6330→23:00 6288→5月14日09:30 6307→10:00 6288。因此Completed33的progress798、efficiency约0.882743、retained1，不能被解释为5月14日价格仍在6482或已经恢复。这是对原归档语义的合理使用，不是要求删掉历史Completed或重算统一窗口。

这里还应保留“declared close路径”和OHLC范围的区别：例如原5月10日21:30 high6560、low6415、close6482，R02/R06声明的路径摘要不自动涵盖全部盘中往返。没有逐tick资料或另一度量，不给实际交易回撤结论。

## P10-04：F05的解释要同时容纳较长已知后运动与短段迟知

### 支持例：高段内效率不保证跨段可持续

本轮已直接取得MAIN_ASOF_5/known/i-ohlc物理131—147全部17行（原KLine1011—1027），不再只依main1 retrospective或管理摘要。关键价点是：5月14日10:00 1167.5→14:00 1096.5→22:00 1139.5→23:00 1115→5月17日11:00 1152→14:00 1125.5。中间每根原OHLC及close也已读取。原N2 median efficiency=1/MAD=0/LOO最大移位=0仍按R6同图值保留，真实零不当缺失。

同cut known i-completed-episodes物理16—21，直接得到原C0E795—800，和R6 exact recent6对齐：

| 原C0E行 | actual起止 | 原预期方向 | 起点可知代理 | 完成可知代理 |
|---|---|---|---|---|
| 795 | 5月13日14:30—5月14日10:00 | Up | 5月13日22:30 | 5月14日14:30 |
| 796 | 5月14日10:00—14:00 | Down | 5月14日14:30 | 5月14日22:30 |
| 797 | 5月14日14:00—22:00 | Up | 5月14日22:30 | 5月17日09:30 |
| 798 | 5月14日22:00—23:00 | Down | 5月17日09:30 | 5月17日11:30 |
| 799 | 5月14日23:00—5月17日11:00 | Up | 5月17日11:30 | 5月17日14:30 |
| 800 | 5月17日11:00—14:00 | Down | 5月17日14:30 | 5月17日22:30 |

后五个效率1段，其起点可知都晚于actual end；它们不能被当作在actual起点已经收到信号的五次可捕获机会。F05反证的是“段内摘要本身充分证明持续好做”，不是中位数数值算错、i普遍难做、市场机制已经是锯子/死亡，或必须新增总摩擦指标。分段条件化、不同策略以及成本缺失都必须保留。

### 反向约束：也不能把所有确认之后都说成已经无运动

MAIN_ASOF_2/known/rb-ohlc物理59—71（原939—951）全文中，第一次knowledge时5月6日10:00 close5600，随后5598、5613、5616、5643、5649、5652、5660、5659、5662、5663，5月7日09:30 5644、10:00 5648。真实出现了已知后继续较高的价格，同时也有回落；不能把整个过程都说成起点之前/确认之前已经结束。

主hc原C0E406的start known在5月6日10:00、actual end在5月10日21:30；与上述i短段并不相同。即便hc后面的407/408两个短段起点可知晚于各自actual end，仍不能反过来否定此前长段中已经可知后留下的运动。

因此要检查的不是“效率1好/坏”或“确认一定晚”，而是业务正在比较哪一个对象、哪段已知路径、后续实际存在什么、使用什么策略及成本。已有原时间和身份字段已经能消除一大部分误读；本轮没有先增加评分器来替代这种解释。

### 当前结论与后继

保持F05为有证据的使用边界/待证设计问题：段内摩擦与跨段方向寿命/换向成本是不同问题，不能用相同名称暗接。但新指标/新网络是否必要尚未被本数据证明；先使用现有原Episode、N历史、已知时间和原价解释，其后才能判断到底缺什么。当前四束的价值是分开位移、路径、保持和可观察性；不把它们做成未经验证的总分。

原35个C1广域与组外正反例仍在继续，未以本主Case或已读几个图层代替完整阶段。原包未给LCC、Calendar原生时长、归一化Profile、dwell/recovery时间、多尺度、正式H1/Quality/Outcome等的具体限制继续保持；新读取的原行不补造这些输出。
