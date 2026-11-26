# D001 / C0002 证据、版本与重放入口

本地研究根：`/dwdhome/fy/BASE_E6_2/artifacts/oi-eaw-p1-business-discovery-20261126-01/calls/C0002/`。以下相对路径均从该根进入。原数据及旧 Run 保留；大表/图/代码和原始Chat仅本地保存，由本索引及冻结清单关联，不伪造附件远端引用。

## 正式输入与新增来源

|入口|准确材料|
|---|---|
|本次采用|`SOURCE_INDEX.json`及`sources/`内正式 D001、Owner、TASK_V0.4、C0002 INVOCATION、Manager Return、旧成果入口和新版指南的准确副本/SHA。task/protocol/guides采用 observe-iterate@ff45aab0c8e66e4feb552b2c8a632210d9b58b56；controller@0f029333a7fc4b568b5e49a77a5c8ab185baa336|
|原数据 Chat|`sources/original-data-thread-read.json`：threadId=01a1e335-cd15-7f72-a7d9-f53c52feb09e，只读thread/read，21轮，SHA-256 `99148f7a0182f04db767cc60a6477d2ffb8c9b626c8b4c8fe269471724cb9453`。第19/20轮定位补齐148窗口及trainA；沿脚本准确引用追查。原文不发布|
|生成链|`sources/export_alltick_data.py`、`capture_split30_inputs.py`、`capture_split30_wall_windows.py`、`market_microstructure_evidence.py`；原出处为原Chat的准确关联材料。原运行目录为`/dwdhome/cyf/trainA`，不是当前研究工作区|
|实例与物理路径|`sources/RESOLVED_SOURCE_PATHS.json`：三个品种×Wall、两F4、Build、Attack、Absorb共18实例；只构造实例解析已有目录，未调用Feature.run/df|
|实际 receipt|`sources/RECEIPT_INDEX.json`列24张原件的物理路径、本地副本、bytes/SHA；`report/EXACT_UPSTREAM_CHECK.json`列共同Wall及直接上游逐项精确关联|
|实际 producer 源码|`report/RECEIPT_CODE_VERIFICATION.json`；`sources/producer-source-matched/`。五类源文件组合摘要均匹配receipt，不能以c747d88干净Git内容代替。`sources/producer-c747d88/`保留此次比对基线，不作实际生成源码|
|原批范围|原Owner数据根不变；`sources/ORIGINAL_WINDOW_UNION.json`为148窗口的区间并集；旧Run `calls/C0002/audit/WINDOW_PROCESS_INDEX.csv`提供PG/日期关联块，旧使用账沿用|

实际产品 code_version 的 Git 部分为 `c747d88a93528fa65cce8f2a6238e1c925bb3b9f`，匹配源码组合 SHA-256：Wall=e5144afcf10de8bda39625157a01b09297410c83dca65321340ad2460497be0d；Build=bcc762ed31b3df22c436d3654a1dfbaeb5e96cdb60fcbdefadd6dbad79d73563；Absorb=a699d8c95adf6df7fd0dac0dde43ec0964ce4e6c682ec25b30cc2ae114460ded；Attack=0be69c60a802982b630ea94523d4ff27a1e0dd51b98c7b53eea4d11c802fd6f5；F4=7f718553bf3ab8c420feeb0e198e40c17b0759f50e6287ba79901306f4562444。receipt包含实际参数及source_scope；完整源路径、字段schema也已留存。receipt只认证产品来源切面，不认证feed方向真值或FRP发布。

## 数据与实际结果

|问题/结果|数值与逐行来源|
|---|---|
|原窗口正式流|`formal/{rb,hc,i}-{wall,build,absorb,segment,formation,barrier}__stream.csv`，18表。每行保留source_stream、source_row_index、within_original_windows。`sources/DBA_READ_AUDIT.json`记录只读mmap源路径、header、数据长度和mtime；只读取原窗口业务值与Wall前驱状态。初始18表统计见`report/FORMAL_READ_SUMMARY.json`|
|两条跨界闭合|`sources/BOUNDARY_SAME_OBJECT_READ_AUDIT.json`、`boundary-completion.log`：hc Segment20199、i Segment225185；仅补原展示已经引用对象的闭合正式行，未读边界外新Tick。故最终659条中657条在原窗口发出，2条为同对象补件|
|9537条展示/正式源对照|`report/DISPLAY_SOURCE_MATCH.json`：逐品种、family、字段匹配数量；三份`report/*-ATTACK_DISPLAY_JOIN.csv`保留源行连接。Build/Absorb按ID+UTI+event_type+occurrence区分，Attack按品种+segment_id连接；数值比较rtol=1e-12/atol=1e-9、NaN相等。Attack几何端点重写单列，不把展示uti当发出uti|
|N1条件分母|`report/ATTACK_TIMING.csv`、`FORMAL_BUSINESS_SUMMARY.json`：659/653的范围区别，PG与日期块、延迟、闭合原因；`INTERVENING_SAME_WALL_EVENTS.csv`为业务末端与闭合之间同物理Wall/侧的原始事件|
|同价等待期业务差异|`report/INVENTORY_DURING_CLOSURE.csv`、`INVENTORY_TIMING_SUMMARY.json`：653条范围、649有效、278全程同价、连续retention/min_ratio和换价/无效边界。每行指向原窗口及同一原包资产|
|6个案例与反例|`report/N1_CASE_INDEX.json`；`cases/N1-01`～`N1-06`内`CASE_METRICS.json`、`QUOTE_TRACE.csv`、`SEGMENT_FORMAL_ROW.csv`、五类同墙历史。图为`figures/N1_PROCESS_COMPARISON.png/.pdf`。`report/CASE_CLOCK_CHECK.json`核六例业务端点/闭合ts与原L1对应UTI均一致|
|最小信息试查|`report/N1_TWO_FIELD_PROBE.csv`，六例42切点。研究baseline明确是“把展示端点读为闭合”，不是实际P2行为；34个过早闭合读法只用于说明已有字段恢复能力，无误读率/预测/生产收益主张|
|R2真实源恢复|`report/R2_FORMAL_RECOVERY.csv`：原四案例与实际Build occurrence逐项精确相等、Start均取得、same_band_continuity_code=1。四例完整原始过程/图仍从旧Run C0015进入，不重复新算或加独立样本|
|来源能力限制|正式Formation中availability=6/body=6的区间针对near-miss和band-shift未观测能力，不能扩成整个攻击不可观察。实际源`attack_flow_assembler.py:241–255`和`:325–405`给原子、区间、available_at与能力范围|

具体设计位置：实际展示`market_microstructure_evidence.py:616–640`选取Attack字段、`:822–854`将展示uti/ts改成business_end并扩单原子几何；`:318–369`的读口未提供Formation/Barrier。实际producer `producer-source-matched/attack_flow_assembler_core.py:1037–1064`区分业务末端与closed_at；wrapper`:325–405`保留accepted material及其可得时间。Build原实际基线逻辑见`build_assembler_core.py:525–550`及正式schema；不把这些位置当FRP实际发布链。

## 独立性、时间与数量政策

继承旧Run全部样本使用限制。本次新增六个深入提取、6PG、6日期关联块、5自然日期；与旧样本可有重用，不与旧69次工作量相加成独立攻击数。完整范围统计是选择性窗口、特定闭合条件的条件结果。无严格留出、市场发生率、因果或预测主张。

业务区间与producer发出/available_at分开；FRP publication仍未知。CSV时间字符串不另造时区认证。bid取buy_price1/buy_vol1，ask取sell_price1/sell_vol1；无效最优档留空，换价后的数量不视为同价库存。方向成交/consumption/reload仍为原代理语义。真实消耗和净撤减=null；receipt的多年source_scope不构成本次新增行情范围。

## 重放与检查

使用 `/m3c3/Linux/apps/anaconda3/bin/python`（pandas/numpy/matplotlib）。所有研究输出必须放获准新目录；不要覆盖旧Run冻结成果。脚本中的ROOT为本C目录，若要重新生成请先复制本C必要输入到新的独立目录并调整ROOT。通常直接核冻结表和源行即可，无需重新提取生产数据。

1. `research/resolve_sources.py`只解析实例路径；依原trainA上下文，不运行特征。初次因缺CurrSymbol失败日志保留，修正后取得18实例。
2. `research/read_formal_windows.py`按DBA V0 header、data_length、只读mmap提取限定稀疏流；`complete_boundary_segments.py`仅补两条原展示对象。不要重复调用边界补件脚本覆盖冻结表。
3. `research/analyze_formal.py`对照展示并生成时序/中途事件表；`inventory_during_closure.py`对齐原L1，`cases_and_probe.py`生成六例、probe与图。研究timestamp dtype首次比对错误及修正日志保留，最终数值对照零差异。
4. `research/verify_delivery.py`只读核冻结包、匹配摘要、原始/正式时钟、限定计数及关键相等关系，不调用生产程序。实际结果保存在`report/LOCAL_VERIFICATION.json`。

`ARTIFACT_INDEX.json`冻结本C研究原件的bytes/SHA；publication、PRO_RETURN及其回读记录是后续实际发布记录，另存不造成自引用。最终报告、证据索引、RESULT、双进度和V2 Return会串行发布在唯一获准分支的本Run前缀；详细表/图/源码保留本地。controller仍负责真实路由与Manager消费，本文不冒称已被接受。
