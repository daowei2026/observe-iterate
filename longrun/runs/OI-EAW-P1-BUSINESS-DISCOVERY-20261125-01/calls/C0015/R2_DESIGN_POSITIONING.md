# R2 的 S08：设计定位、两项标签及等级

C0015／D008，仅R2。S07_EVIDENCE.md和四例原始联合材料已保存。本节回答原生问题：共同对象/价位及明确参考量下，已有联合历史/时点能否区分活动、当前存量与后续接触，第一处不可用信息在哪里。

## 目前能恢复什么

本批可得展示属性与按UTI的L1联合，已经足以恢复四类具体区别：累计活动量与当前量不是同一量；Build基线有自己的起点与最佳价；当前最优价可离开所绑定Wall价带；较晚Absorb交互结果不能作为较早切点的已知事实。四例均独立于原R2形成Wall，普通例R2-04当前同价量894高于Wall展示起量866，不能只找变薄例。R2-02的4359量56也不能填成4360墙当前量。

这些是可见L1/展示的局部对象关系。它们没有证明同一订单存续、真实补撤数量或正式exact Wall身份。只要合法消费者已有同版本原始属性、价带和L1关系，应先正确组合/表达现有信息；无须再造同义P1事件。没有取得实际P2产物，本次不认定P2误读。

## 准确出处与参考链

以下均为已读固定原件；准确路径、bytes、SHA256、Git blob及阅读范围列在SOURCE_INDEX.json。设计包是任务指定的`feature-refinement-implementation-agent-evolution@8d58ddd3392a3e67ef5ba44adf2c4cd0c9077f9f`，TIS参考为`179016111ed0394f92025313e46bd13534932a74`，FRP参考为`cac6c912dd65a14acbd591ca57e0afd8ddb4ef13`。后两者未证为本批实际运行版本。

|材料/位置|实际语义|本次定位与边界|
|---|---|---|
|设计包`02_FINAL_P1_ARCHITECTURE.md`、`01_EFFECTIVE_SCOPE_AND_REQUIREMENT_CORRECTIONS.md`|独立Feature/exact upstream；TIS形成业务变化，FRP维护正式状态/输出；P2形成自己的判断切面|不能把研究展示缺项直接归为底层缺字段；也不靠FRP重跑识别补真值|
|`dsu/P1-DSU-02_Build_活动_DSU.md`、`P1-DSU-04_Absorb_交互_DSU.md`|Build活动与Absorb交互各有run-local typed身份、exact Wall、occurrence/current/history/publication；milestone不是Committed，Absorb Resolved不是Wall Fate|Alive/Build/Absorb不是同一业务主语；local编号相合不等于正式exact身份验证|
|TIS `hf/prel0/build_assembler_core.py:525–550,917–938`|活动开始的`baseline_vol=best_vol_t`；内部留last_best_price/volume，稀疏事件输出baseline/cum/level/ratio等；该事件不携带起点参考价|R2-04实测baseline48取自729而Wall在728.5。参考价可用起点UTI+L1恢复；只看plot_price会丢失这个区别。这里定位到参考稀疏表达，不是证明整条实际联合链首损|
|TIS `hf/prel0/build_assembler.py:249`起的numeric stream物化|保留raw baseline、观测ratio和level等独立字段|raw观测ratio可与cum反算baseline；1585条一致是字段恒等核对，不是预测收益|
|FRP `src/Frp/Instance/ISL/Eaw/P1/FaoIngress.hs:638–667`；`Interface/PreL0.hs:199–238`|`decodeBuildNumericRow`读cum与continuity；milestone构造参数读`level`。`BuildMeasurements`仅累计addition proxy和continuity；typed payload没有raw baseline或观测ratio|**`BuildMilestoneRatio`在此是门槛值，不是raw观测ratio。**1579/1585条两者不同；不能用cum/typed门槛反算真实基线。raw→该typed投影有明确压缩，但原artifact、L1或其他合法联合材料可能仍可恢复，不能自动称全链缺口|
|FRP `FaoIngress.hs:1031–1075`|Absorb读consumed/replenishment/progress，区分Started/Milestone/Resolved及resolved reason，验证依赖Wall|Resolved是这次交互结论；不能扩大为Wall终结。参考TIS `absorb_assembler_core.py:1293–1298`的公开replenishment为非负visible剩量+consumed−initial代理；非独立真补单计数|
|TIS `attack_flow_assembler_core.py:814–829`；FRP `FaoIngress.hs:774–783`|Attack的start、business_end、closed_at分开；参考入口接收三时点|本批368/653条display UTI与ts差+0.5秒只提示时间锚区别，不证明正式发布延迟或Bug。业务发生/闭段/正式发布必须分开|
|FRP `P1/Products.hs:275–297,493–499,583–590`；`P1/BuildActivity.hs`/`AbsorbInteraction.hs`|receipt要求code/schema/参数/source/upstream；current保留最近typed occurrence，另有历史/发布|current不等于L1实时库存；最近typed payload也不能凭空恢复未承接的raw基线。当前无本批相容完整历史，不能宣布组合不可能|

`Publication.hs`已exact保存，仅核对发布/序列化相关片段；不据此宣称完整序列化或现行代码验收。原件均可按SOURCE_INDEX进入。

## 第一处不可用信息的结论

|层次|实际已定位|尚不能声称|
|---|---|---|
|本批raw展示+L1|4类数量/价位/发生先后区别可恢复；baseline与当前量、门槛与观测比值都可分开|不是本批一开始就无信息；不是正式发布时间可由展示倒推|
|参考TIS状态→稀疏事件|起点参考价未直接随该Build事件输出，但起点UTI+L1可补回|不等于必须新增生产字段，更不是实际链第一处信息丢失已证|
|参考numeric→typed Build入口|baseline/观测ratio未进入该typed payload，门槛level进入MilestoneRatio|不等于其他产品/原artifact/历史对合法消费者不可得；不证明本批实际FRP做了同样压缩|
|本批正式联合链|actual producer/FRP commit、参数receipt、exact upstream身份及完整occurrence/current/publication未取得；这是一处取证可用性边界|不能选一个参考commit冒充实际运行，不能宣布首次正式信息损失/实现Bug|
|上层组合/展示|已有信息可解释区别，语义标签可表达消费规则|没有实际P2实物，不能称已验证错误率、收益或必须修改|

因此保留为**研究线索；正式链待证**。本次确认的是已有信息的消费/表达要求及参考投影中需核对的语义位置。已确认必须修改、正式信息缺口、生产Bug、有充分依据改进点、初步改进依据点均为0。该等级不因D008交付完成而提高。

## 43PG、两项标签的实际试查

selection/SELECTION_FROZEN.json在未来价格访问前冻结。每个未形成R2、此前未深入PG按event-ID哈希取一个比值≥1且累计/当前或价带关系有区别的里程碑，排除四例PG，共43事件/43 local Wall/43PG/21日期块。全部继承R1全批程序访问，其中41PG还曾有特定指标访问；不能称未见、严格留出或总体样本。原始quote及P1逐行/哈希核对PASS。

基准输入保留已有身份/UTI、baseline/cum/观测ratio/level、起点最佳价量、当前最佳价量及Wall价带。增强输入只追加两个字符串：`quantity_role`解释各数量及参考价角色，`time_basis`区分展示锚/当时L1/未知正式发布及后续resolved。原数值改动0、新增数值0。试查不是给一个只剩事件名的虚弱基准补整包数据；所有原字段在两版一致。

实际43条中，29条当前最佳价在Wall价带外，22条基线起点最佳价在价带外，42条raw观测ratio不同于level；当前量等于累计量0条。43条基线均与起点原始报价一致。8条另有10秒内后续Resolved展示，仅放在审计表，未放进截至点输入。1条ratio恰等于level的普通反例仍保留。所有正式发布可用性均未知。

两标签使上述既有数据的解释规则明确，可阻止“把门槛当观测比值”“把别价最佳量当旧墙存量”“把后验交互倒灌”的错误表达；它们没有添加原先缺失的市场事实。未运行真实P2、未进行人类误读实验、未证明标签带来预测或生产收益。准确输出为probe/BASELINE_INPUT.csv、TWO_LABEL_INPUT.csv、PROBE_AUDIT.csv及report/MINIMAL_PROBE_SUMMARY.json、MINIMAL_PROBE_VERIFICATION.json。

## 迭代记录与后继问题

- 对象/影响：跨Wall、Build、Absorb的数量参考与时点消费；误讲时会把累计活动、异价最优量或后验结论说成切点库存/已知事实。本次证明存在具体语义差别，未证明某个实际消费者犯错。
- 建议层次：当前先作已有信息的组合/表达要求；如果实际合法接口只给typed门槛而没有可用的原基线、参考价或相容联合历史，再决定是字段投影/元数据/上层关联的哪一处需要改。无需预设StrengthDown、负Build或新对象事件。
- 应表达什么：每个量的业务主语、参考量/参考价与时段；门槛和观测值的区别；对象同价/近价关系；发生/闭段/发布可知边界。
- 依赖：已有R1的L1恢复/身份限制与R3共享代理来源约束复用；未把R3独立结案。
- 下一轮设计问题：**在实际相容的receipt和合法消费投影下，消费者能否于切点取得Build起点baseline及其参考价、区分观测ratio/门槛level，并取得不晚于切点发布的交互历史？若不能，哪个确切投影/权限/历史边界首先阻断了这项恢复？**先回答此问题再决定是否需要研发点。由原Manager安排后继；本D不执行R3独立闭环或S09，不无限等待缺件。

D008的授权研究已完成；相容正式链缺件是结论等级的限制，不是本D剩余执行范围。父Run仍未完成。
