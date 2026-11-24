# D003｜原D002 m X异常的DiagnosisReport

本项诊断已完成。当前直接因果定位为**上游输入轴与交易日分块合同不兼容**；形成具名[UpstreamFinding](UpstreamFinding.json)和[ScopedBlocker](ScopedBlocker.json)，没有修复上游或恢复完整X。D003的诊断范围无剩余动作；原D002仍未完成，eligible_for_G=false，原U保持PARTIAL。

## 冻结预期、实际偏差与影响

预期沿原GO和唯一正式输入：当前179016/default、rb/m真实市场2021全年、指定SOF/Calendar应有实际有效的exact Wall/F4和Attack三产品及严格读回；没有将文件存在、局部实验或构造证据当作成功。当前诊断对象是已记录的X异常，不是G finding，也不以其它Run结论预定责任。

A05的m交易集已正确采用、Wall5表有效，但两F4均在`2021-03-12`前`1792800 != 1792801`失败，m Attack未启动。完整m F4/Attack结果及rb/m X资格尚缺；rb既有三产品35表严格读回和m Wall资格保留。当前诊断不说明Attack业务对象合理或不合理。

## 真实输入和最小区分检查

E01只读加载同一原生m源：9,959,400个半秒calendar索引行，索引单调唯一，243个有交集的交易日区间。共有17行price/buy_price1/buy_vol1/sell_price1/sell_vol1同时空；其中以下4行未被任何交易日区间覆盖。它们的预测主买/主卖价量四字段为0，linear_ts存在，**不是所有字段空，也不能当作有效无活动成交**。

| 原始位置 | 原市场时间 | 实际内容 |
|---:|---|---|
| 1792800 | 2021-03-11 21:00:00.500000 | 五报价空、hit代理为0、linear_ts存在 |
| 3916800 | 2021-05-28 21:00:00.500000 | 五报价空、hit代理为0、linear_ts存在 |
| 7200000 | 2021-09-22 21:00:00.500000 | 五报价空、hit代理为0、linear_ts存在 |
| 8634600 | 2021-11-17 21:00:00.500000 | 五报价空、hit代理为0、linear_ts存在 |

首个冲突前一交易日结束于2021-03-11 15:00:00，stop位置1792800；下一交易日2021-03-12的区间从2021-03-11 21:00:01、位置1792801开始。calendar轴仍有21:00:00.500的空报价行，所以覆盖检查在任何逐chunk F4计算之前失败。

原始全年输入精确复现A05异常。取首个冲突及前后各3条真实行共7行：原生planner报`3 != 4`；仅在内存去掉未覆盖行后6行、2个交易日区间通过；删除普通有效行但保留未覆盖行仍报`2 != 3`。紧邻异常前的3个正常真实行单独通过。没有人工生成报价或修改市场DBA。

全年索引轻量复核中，仅内存去4条未覆盖行，native planner覆盖243日、9,959,396行通过；仍有13条处于交易日区间内的空报价行，因此**不是任意NaN都触发此覆盖异常**。原cc索引摘要未变。该检查只证明planner的直接因果，不是F4 core、receipt或完整读回成功。

只读调用当前Wall既有空报价处理逻辑，去17行后得到9,959,383行，其index摘要与本Run当前合格m Wall trace完全一致。9,959,400、9,959,396和9,959,383三个轴不能混用；没有把Wall专用处理复制成F4生产修法。[最小实验原件](MinimalDiscriminatingExperiment.json)包含每个正反对照、完整输入绑定、计数单位及证据边界。

## 最早责任逻辑与竞争解释

`SubContinuousContract`把存储报价与半秒calendar直接组合；共享`_load_cc_df`只按SOF日期切片，保留上述4行；F4随后把这个轴交给要求交易日区间无缝覆盖全部输入的`_trading_day_chunk_plan`。**最早不兼容的交接是这个输入适配/分块合同组合**。guard按当前代码工作，不能仅从栈末行认定比较式、F4 core或源数据写入者本身写错。

原生真实输入和局部正反对照支持该直接因果。已排除当前m仍沿black遗漏、当前源码/默认实例错配、索引乱序/重复、区间外有效报价、F4阈值/Attack算法及旧结果读回作为本次覆盖异常起点。源DBA里这些空报价由哪一步写入，以及main_contract与输入adapter应如何正式统一，不由本证据指认；这属于上游最终修复责任的边界。[LogicLocalization](LogicLocalization.json)逐项保存源码/数据依据；[机器版DiagnosisReport](DiagnosisReport.json)分别列出事实、解释、排除、未决、处理链和实际/确认时间口径。

实现符合性：loader和guard按当前规则执行。业务适用性：该上游合同组合无法在本Run实际正式输入上形成所需F4；没有据此宣称F4大额成交业务规则普遍错误或市场数据整体错误。

## 参数能力、权限和合法后继

E02在禁止所有Feature运行的guard下核实际copy模块、四个默认实例PPID及两F4完整P。loader与planner均不读取业务P；F4门槛、same_best容差、比例、eps和Attack参数不能改变固定cc.index与trading_days的覆盖关系。当前异常的可修复性为`PROVEN_NOT_ADJUSTABLE`，仅限当前已暴露业务参数及已审计数值常量；不等于所有实现方式无解，也未启动标定。

F4/Wall/公共适配器、源数据和元数据均不是本Run可修改面。已形成具名上游问题、影响与恢复条件；本D没有改产品、改市场数据、缩减正式范围、旁路校验、重跑Gen或覆盖半成品。没有新增Skill/Gate、Worker或Owner节点，也未向其它Chat发送消息。

恢复需由原manager协调具有合法责任面的上游统一输入表示/区间/适配合同，并取得准确新绑定的有效全年F4、receipts和完整读回；同时核Wall/F4 availability/Attack消费轴一致。当前Attack也依赖同一公共载入/分块并要求exact axis，m尚未启动，不能从planner反事实通过推断后续Attack成功。原D002续作必须先核effects，使用新真实C/attempt与fresh写面，任何共享生产重新取得同一原flock；12个失败DBA保持原样。完整X成立后再依原Workflow协调G。

## 原件保留和专业完成边界

E01仅允许SubContinuousContract Cal/write=False，P1 dump及writer被禁止；E02只构造/读源码、禁止所有Feature run/rerun。本D无共享生产写入，因此没有占生产锁；原锁device83/inode15061041/0字节只读核对未变，没有用探测冒称持锁生产。

652个原产物前后清单一致；12个失败DBA共677,239,968字节逐文件SHA256与C0009原件一致。A01/A02/A03/R01/A04历史21个记录文件、C0007的31项和C0009的18项已发布manifest原件未变；U包blob15817e6仍PARTIAL。当前TIS HEAD179016、tracked代码无改。未消费Build业务成果。

D003已完成原Skill所需的直接因果/最窄责任定位、参数能力与合法路由，具名边界保留；[原D002局部阻断](ScopedBlocker.json)及其修复/完整X/G仍未完成。D003 Return采用REPORTED_COMPLETE、D003 remaining/continuation=null，无issued D/W和Owner请求；这是本项诊断完成，不是父Run、X/G或Feature验收完成。controller负责独立物理回执、完整executor_return核验与跨Chat运输。
