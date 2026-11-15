# W008真实材料核查

标签：**PARTIAL_WITH_LIMITS**；本地outcome **PARTIAL**。这是材料事实标签，不作业务合理性或专业接受决定。

normal实跑3个纯reducer调用：N1 Start UTI10，N2两条合法BandUpdate UTI11/12，N3 End UTI14。全部Right，O条数1/2/1；完整人工typed input、O和pre/post原始Show在CURRENT_NORMAL_CHAIN.jsonl。N2实际A与C仅ref wall-occurrence-2b（band[101,103]/core102）；N3 A为空，C仍含WallEndedState。A/C来自既有derived Show的精确字段抽取，CURRENT_NORMAL_RECONCILIATION保留原Show来源，不推断FRP提交。

当前Publication occurrence-level ToBSON/FromBSON实跑4条全部读回相等，compact-local-v2 schema及完整BSON文档Show保留。End只有reason，没有band/core字段，不按legacy zero表示重构当前数据。该读回是内存canonical occurrence adapter，未测试DBA物理批次/诊断schema或generated wrapper。

两个已存在场景表达式：cross-firing相同Start实际Left WallStartedTwice(local999)；已有test预期requireRight/空发布，二者的实现合同张力保留。after-End update实际Left WallUpdateBeforeStart(local999)，原test只要求任意Left；setup本W缩为Start/BandUpdate/End，省去Dormant/restore；update UTI11低于End14，不能另称已隔离late policy。harness exit0表示观察记录成功，不是整套smoke assertion通过；没有运行旧九场景整包或额外第三scenario。这里不作正式SUPPORTS/COUNTERS。

身份仅限本W人工数据scope/localNo999/ref；没加载生产FeatureRunIdentity或上游receipt。rb、BidWall和UTI值真实记录于typed input；SHFE-night只是现成testlabel，无实际日历/自然时间映射。command wallclock是执行时间，不是业务actual/confirm/known。现成依赖缓存只绑定packageDB metadata/ABI，不伪造全部生成来源。

缺失区分：N3 reducer A fromList []为实际有效空；normal中没有Left是本层成功，不等于D事件有效空；未物化current DBA、无真实生产参数tuple是DataUnavailable/NotObtained；自然无事件、InsufficientHistory、Pending runtime状态均未由该人工fixture验证，不能混成0。

可交原E1消费的事实：当前reducer正常身份/变化、同次两更新last C、reducer A删除、两个exact state error constructor、current End measurement shape、occurrence BSON adapter四条往返。不能回答：production engine/DBA writer/native reader完整链、实际诊断事件对账、自然频率、完整terminal/transaction/time policy或业务适用性最终判断。

首次PATH GHC缺libtinfo.so.5 exit127；现成tinfo6同9.4.8替代查询成功，无依赖安装。第一次脚本编译因Worker本W列表类型歧义exit1，5个production模块编译成功；仅新增脚本NoOverloadedLists后同范围编译成功，失败脚本及完整日志保留。现有snapshot361目录超过自定小搜索200边界，未逐项搜索，转用setup-config已给两个精确pkgdb。三项局部问题未冻结其他合法取材。

逐份bytes/SHA/真实missing见CURRENT_MATERIAL_MANIFEST；完整命令、exit、elapsed、输出和副作用见EXECUTION报告/COMMAND_LOG/receipts。旧W007的85原件只读保存，未作为本轮current material。
