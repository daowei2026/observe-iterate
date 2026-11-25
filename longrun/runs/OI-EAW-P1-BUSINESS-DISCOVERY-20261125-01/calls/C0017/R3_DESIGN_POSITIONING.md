# R3 的 S08：来源约束、设计定位与本条去向

C0017／D009，仅R3「真实消耗/净撤减的来源可识别性」。S07_EVIDENCE.md保存本批可得证据、复用分母和原始行核查。本条已完成授权工作；维持**研究线索（共同观测约束）**，停止本批真实补撤分解推断，保留可见活动结论。它不是已确认P1缺口、必须修改或实际P2错误。

## 来源与设计的逐层核对

准确版本/路径/字节哈希和阅读范围在SOURCE_INDEX.json。设计包锁定`feature-refinement-implementation-agent-evolution@8d58ddd3392a3e67ef5ba44adf2c4cd0c9077f9f`；TIS参考`179016111ed0394f92025313e46bd13534932a74`、FRP参考`cac6c912dd65a14acbd591ca57e0afd8ddb4ef13`。未将参考版本替代本批actual producer/FRP。

|层次与准确出处|已核语义|可支持的判断|
|---|---|---|
|原批manifest、S02 FILE_INVENTORY/SCHEMA_CATALOG及SOURCE_AUDIT|2,924文件清单不变；2,920资产没有实际producer/单位/计量覆盖receipt；有raw trade_volume及方向预测列|快照、时间轴和字段可核，但独立真实成交方向/订单事件不可得；不能认证真实消耗/撤减|
|TIS `t0/gen/cc.py:119–182`|trade_volume称Tick间成交量，方向列明确为盘口减少/消失等预测；代码从DbArray读入|已有代理说明，不应把名称或符号当独立成交归属。此处未交代本批feed单位/完整覆盖；没有定位实际生成源码或原物化receipt|
|TIS `hf/prel0/absorb_assembler.py:132–155`；`absorb_assembler_core.py:267–287,330–353,1090–1116,1293–1310`|方向列绝对量进入hit代理；消费累计逐步加hit_vol_proxy。虽然接口接收trade_vol，该参考函数随后`del trade_vol`；公开replenishment是非负visible_remaining+consumed_proxy−initial|多项事件沿同一估计形成不增加独立真值。这里的输入/输出忠于代理语义，不能要求它凭空变出真实补撤；不认定实现Bug。内部replenish_gap与公开replenishment不要混读|
|TIS `pressure_big_deal.py:105–115,450–486`及`eaw_interface_contract.py:343–393,404–445`|CC方向列作为命中代理；Attack load/volume_semantics、Absorb consumed/replenishment均具proxy语义与availability|已有语义，不能为本D重复凑同义字段；同源事件不是独立成交的交叉验证|
|FRP `Interface/PreL0.hs:199–238,334–398`；`P1/FaoIngress.hs:627–667,817–865,1022–1074`|Build累计addition proxy，Absorb consumed/replenishment proxy；入口保留availability枚举；Attack payload明确构造`PredictedDirectionalHitVolumePerHalfSecondV0`|参考typed出口已携带代理及计算可得性。`Available`/`Measured`表明该产品值可计算/有值，不能升级为真实方向已观测或总成交单位已认证|
|设计包`02_FINAL_P1_ARCHITECTURE.md`、`01_EFFECTIVE_SCOPE_AND_REQUIREMENT_CORRECTIONS.md`及Build/Absorb/Attack DSU|独立Feature、exact upstream、typed身份、产品特定current/history/publication；FRP不重跑微观识别|不由展示缺字段反推正式产品无信息，也不靠重复生产或FRP重判补真值。实际合法联合投影仍需相容版本/receipt才能确认|
|TIS `p1_product_receipt.py:1–88`；FRP `P1/Products.hs:275–297`|参考薄receipt有10项必需字段及source scope/upstream要求，含code/schema/参数/位置|本包没有这些认证材料；即使以后有Feature receipt，也须另核市场feed量尺/区间/完整性，receipt本身不产生独立方向真值|

所有参考代码只读，未导入运行producer。没有修改正式特征/参数/数据库。

## 第一处不可用信息

1. **源观测/研究材料层已证限制**：所给L1快照和从其变化形成的方向代理，不能唯一拆出真实成交、可见新增和撤减；缺相应独立逐笔/订单及可认证计量覆盖。即使把所有同源代理历史保留，独立信息也不会自动出现。
2. **实际正式链首损未证**：没有本批actual代码/参数receipt、exact upstream/Wall身份、相容完整occurrence/current/publication，不能判断这些语义在实际何处首次丢失或下游是否能正确恢复。展示缺项不是正式缺项证据。
3. **已有可恢复部分**：C_source、directional_truth_status、raw V、proxy名和availability足以在本研究材料中区分可见活动、未知方向及计算有值。R2已有quantity_role/time_basis可帮助避免跨数量/时点误讲；本D不重做其正式链后继问题。

因此没有把参考投影、研究缺件或源不可识别性包装为现行产品缺字段。未取得实际P2产物，不认定它已把Available或proxy误当真值。

## 计量、时间和上界的使用门槛

研究程序的区间口径为q(t0)、q(t1)与t0<UTI≤t1的增量求和，12行真实报价已按此核对。内部网格完整、重叠一致不证明交易feed完整；参考“Tick间成交量”描述也未认证实际归属。不能误加起点前的V或别价命中，更不能用display UTI、business_end或Resolved替代正式发布可知时点。

只有在同一计量单位、单/双边约定、区间归属及完整覆盖真实核定时，才可沿原条件使用0≤C_real≤V，并对N=q1−q0+C_real写N≤V−(q0−q1)。这仍是条件净量边界，不给订单身份、撤减总量或意图。本批这些前提未满足，四个回查过程应用真实上界0次，真实C/净撤减估计均null。5,423个旧条件区间没有被本C升级成已认证净撤单。

可见正变动是正变动，不等于净新增；C_quote等于可见减量的代数关系也不能识别撤减。零代理不认证该侧无真实成交，C≤V的普通例也不认证方向估计准确。这些约束同时适用于R1/R2。

## 最小信息试查的实际决定

本次没有新增数值、标签或“净撤单特征”，没有强制额外试查。理由是：已有C_source、不可独立方向状态、proxy/availability及R2角色/时点标签已能表达当前限制；再加同义标签不会提供缺少的计量receipt或独立真值。原始行回查本身是来源/时间核查，不冒充最小新特征收益验证。

已做的是检查现有语义的适用边界：在四个已暴露PG中，无论C>V或C≤V，都保留unknown的真实方向/覆盖状态，而不是把有值当真值。四例是复用来源核查，不新增4次深入提取或独立复现；未读取新后期价格，未运行P2/用户误读实验，新增字段收益及生产稀疏化成本均未评估。无需为了本D交付凑1～2字段。

## 迭代记录、等级与去向

|项|本次记录|
|---|---|
|业务问题/影响|把可见减量/累计命中代理说成真实成交负荷，或把正变动说成净新增，会改变对消耗、撤减和补充能力的叙事；本次明确可识别边界，未证明某个实际消费者犯错|
|支持等级|研究线索（共同观测约束）；不是候选研发点的自动升级。正式缺口/必须修改/生产Bug、有充分或初步改进依据点均0|
|当前设计去向|沿已有来源/量尺/可得性语义正确消费、保存未证状态；不提出同义P1字段或真正净撤单算法|
|已证与待证|材料层独立真值不可识别、参考链代理语义已核；实际合法出口是否正确承接仍待相容正式材料，不据缺件判它错误|
|依赖影响|R1/R2的可见过程/基线价量结论继续有效，真实消耗/补撤解释继续受共同约束；R1/R2正式链问题未被本D解决|
|本条停止依据|同批来源范围已核，缺独立真值及计量前提；重复恒等式/同源事件没有新增认识，授权不含新feed或生产重跑。按原D停止真实分解推断，不无限等待Owner|

原生后继问题保持具体：**若未来获得实际相容source/producer receipt、feed量尺与完整覆盖依据及独立成交方向/订单事件，哪些真实消耗/净量结论才可重新识别；现有合法消费者是否已正确保留proxy、availability与时点限定？**先核这些前提，再决定是否有产品改动；不预设新增特征。由原Manager消费D009后安排后继，S09单独。

D009的R3授权研究已完成，局部缺件记入结论边界而非本D剩余；父Run未完成。
