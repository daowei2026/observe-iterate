# C0015／D008：R2 的 S07＋S08 回交

E1已完成原D008中R2「活动基线、同价/近价对象及可知时间的联合解释」的授权研究。**R2保持研究线索，正式链待证**；已有展示属性与L1可恢复具体区别，未确认必须新增P1、生产Bug或实际P2误读。D008无剩余；父Run未完成，后继交原Manager安排。

实际定向扫描17,863条来源引用/16,710去重记录，9,526条可锚定联合事件。主同价条件为483里程碑/289活动/209 local Wall/83PG/22日期块，其中219事件当前量≤Wall展示段起量1/4；每PG取一条敏感性38/83。仅为所选窗口条件范围，不是独立攻防频率。价带外最优量不作为旧墙当前库存。

新增四个此前未深入PG的案例，659行quote和174条可得同侧P1来源引用，均非R2原形成Wall。活动累计与当前厚度、活动基线价与Wall价、较晚Absorb与切点可知信息均可由已有字段区分；普通例当前同价894高于Wall起量866，也保留。案例的未来方向混合且一例截断，不支持价格因果。四图已实际看过，原始行/哈希/连续性与旧冻结文件验证PASS。

S08核到具体参考链语义：FRP `FaoIngress.hs`的Build milestone读门槛`level`，不是raw观测`ratio`；该typed payload未承接raw baseline/观测ratio。1579/1585条raw观测ratio与level不同，不能拿门槛反算真实基线。TIS参考活动基线取起点最佳档量，价可异于绑定Wall；起点UTI+L1可恢复。上述仅定位参考投影，不证明本批实际正式联合链首损。

冻结的43事件/43PG/21日期块试查只追加`quantity_role`、`time_basis`两个语义标签，原值不改、新数值0；29个切点在Wall价带外，22个起点基线价在价带外，42个观测ratio不等于level。8个后续Resolved只入后验审计。标签表达既有信息，未测真实P2误读率或收益。全部继承R1全批暴露，41PG有此前特定指标访问，不称未开封或严格留出。

actual producer/FRP版本、参数receipt、exact身份及完整occurrence/current/publication未取得；展示发生/闭段不能冒充正式发布时间。该局部缺件限制正式成熟度，不妨碍上述已完成研究，也不转成D008剩余。最强支持是已有信息的消费/表达要求及需核对的参考投影。正式缺口、必须修改、生产Bug、有充分依据改进点、初步改进依据点均未确认。

正式成果入口：

- [S07证据与分母](S07_EVIDENCE.md)、[案例册](R2_CASEBOOK.md)。
- [S08定位、等级与原生后继问题](R2_DESIGN_POSITIONING.md)、[机读结果](report/R2_RESULT.json)。
- [条件统计](report/R2_STATISTICS.json)、[两标签试查](report/MINIMAL_PROBE_SUMMARY.json)、[试查原始核验](report/MINIMAL_PROBE_VERIFICATION.json)。
- [来源与版本索引](SOURCE_INDEX.json)、[全部本地材料冻结索引](ARTIFACT_INDEX.json)、[核查入口](LOCAL_ARTIFACTS.md)。

本地根：`/dwdhome/fy/BASE_E6_2/artifacts/oi-eaw-p1-business-discovery-20261125-01/calls/C0015/`。原S01～S06及R1复用，旧冻结文件未改；累计样本账在report/SAMPLE_USE_CUMULATIVE.json，保留此前210条原记录，新增4例深入提取与43条语义试查使用。详细表、图、代码留本地，按冻结索引可复核，不伪造单独远端入口。

调用身份：run `OI-EAW-P1-BUSINESS-DISCOVERY-20261125-01`，C0015，invocation token `eaw-discovery-c0015-d008-r2-s07-s08-20261126`，issuer C0014，delegation为`daowei2026/observe-iterate@33f1a0b155a7352b515b004c935c65050e337531:longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261125-01/delegations/D008/DELEGATION.json`。同E1 session，workers=[]，只读生产材料，仅写独立研究及本Run获准路径。

回原Manager：`codex:OI-EAW-P1-BUSINESS-DISCOVERY-20261125-01:manager`。按V2报告先发布，随后真实C0015零W PRO_RETURN引用exact报告；完成态REPORTED_COMPLETE，remaining_scope_ref/continuation_ref=null。原controller回收和Manager消费在交回时仍待实际执行，不代宣完成。
