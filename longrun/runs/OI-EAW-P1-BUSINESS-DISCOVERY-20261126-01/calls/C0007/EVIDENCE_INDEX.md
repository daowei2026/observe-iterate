# D004 / C0007 证据入口与重放

本次独立根：`/dwdhome/fy/BASE_E6_2/artifacts/oi-eaw-p1-business-discovery-20261126-01/calls/C0007/`。以下均为该根相对路径；正式报告及索引发布到获准分支本Run路径，大表/图/代码依 D004 保留共享本地目录。未发布原 Chat 全文。

## 正式原件

- Invocation：`daowei2026/observe-iterate@a38c5d34b5dbeb69044ec3398c83d354ab6bf113:longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261126-01/calls/C0007/INVOCATION.json`。
- D004 JSON：`daowei2026/observe-iterate@a12bc31c95b6da76a17a9700ed436d34ecede397:longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261126-01/delegations/D004/DELEGATION.json`。
- D004 正文：`daowei2026/observe-iterate@8b46e9d660ede6f8f2141adf527f3d75aa45d223:longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261126-01/delegations/D004/DELEGATION.md`。
- Owner 恢复：`daowei2026/observe-iterate@cd6b79d09796b515dc630e86a24130f7b67bec82:longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261126-01/owner/RESUME_20261126_VOLQUANT_TRADE_VOLUME.md`。准确本地原文已保存 `sources/OWNER_RESUME_20261126.original.md`。
- 原 Manager C0006 Return：`daowei2026/observe-iterate@81f108555e468d07569a8bbd070dd2d8d8a7e99a:longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261126-01/calls/C0006/PRO_RETURN.json`。本次亲读准确原件及 Manager 完整报告/委派，副本和原路径/hash在 `SOURCE_INDEX.json`。
- 原任务 V0.4、新版 Executor Guide、TASK_WORK_PRACTICE 沿固定 OI `ff45aab0c8e66e4feb552b2c8a632210d9b58b56` 继续采用；controller `0f029333a7fc4b568b5e49a77a5c8ab185baa336` 不因数据变化而升级。D003 未执行，唯一现行委派 D004。

## 实际材料与版本

新材料根：`/home/dw/.codex/visualizations/2026/11/16/01a1e335-cd15-7f72-a7d9-f53c52feb09e/gallery/steel-ticks-qt-20261126/`。仅使用 manifest 的原148窗 tick 和 QT 资产，不从其他尺度增加行情。六个源入口的原bytes/hash及本次一致核对在 `SOURCE_INDEX.json`，888个实际资产hash在 `sources/NEW_ASSET_INDEX.json`。

既有正式P1沿 `../C0002/sources/RECEIPT_INDEX.json`、`RESOLVED_SOURCE_PATHS.json`、`../C0002/report/EXACT_UPSTREAM_CHECK.json` 和 `RECEIPT_CODE_VERIFICATION.json`；匹配源码在 `../C0002/sources/producer-source-matched/`，正式流在 `../C0002/formal/`。完整版本必须保留 `git:c747d88a93528fa65cce8f2a6238e1c925bb3b9f+source-sha256:…`。五组摘要复用 C0002 证据索引 exact ref：
`daowei2026/observe-iterate@77f11f6e5ea4de5ad9e0be1caa3d1312bf4e84c3:longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261126-01/calls/C0002/EVIDENCE_INDEX.md`。

旧身份、每侧窗口前状态及 N2 复用 `../C0004/`。其正式证据索引为：
`daowei2026/observe-iterate@8daeaa2906a1a138ce204057747358a31ecf62c8:longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261126-01/calls/C0004/EVIDENCE_INDEX.md`。
旧 R3 正文/结果实际回查 `/dwdhome/fy/BASE_E6_2/artifacts/oi-eaw-p1-business-discovery-20261125-01/calls/C0017/R3_DESIGN_POSITIONING.md` 及 `report/R3_RESULT.json`；不改旧稿或将其参考版本替代实际源。

## 主张与证据

|主张|准确入口|
|---|---|
|新旧原13列346764窗口行一致；原148窗不变|`report/SOURCE_CONCORDANCE.json`、`NEW_OLD_WINDOW_CHECK.csv`；新源输入/QT缓存 `report/{rb,hc,i}-INPUTS.csv`|
|QT参数、96日频值和交易日对齐|`report/QT_DAILY_SELECTED.csv`、`sources/QT_DBA_READ_AUDIT.json`；实际Wall receipt三品种私有参数；当前源 `QT_SOURCE.json`|
|旧28例所检原区间低于QT，唯一same_core例可区分|`report/OLD_R1_QT_VOLUME.csv`、`OLD_R1_QT_AT_CUTS.csv`；对回 C0004 旧29例身份原件|
|真实采用平台期间总量，且不是新的独立方向观测|`report/SOURCE_CONCORDANCE.json`、`NATIVE_CC_SOURCE_CHECK.json`、`sources/NATIVE_CC_READ_AUDIT.json`；162原生定点与包一致。`sources/cc.py`为当前提取环境读入说明，不冒充receipt覆盖的代码指纹|
|正式C实际来自含起点盘口代理|`report/ACTUAL_PROXY_CLOCK_CHECK.csv`：4502可核 occurrence 全部相符；`ABSORB_TRADE_VOLUME_CONSTRAINTS.csv` 保留全部4526行与不适格记录|
|条件分母、聚集和反例|`report/ABSORB_LATEST_PER_TRACK.csv`、`ABSORB_TRACK_CONTEXT.csv`、`RECORDED_VOLUME_PROFILE.csv`、`ONE_TRACK_PER_PG.csv`、`TRADE_CONSTRAINT_SUMMARY.json`；以轨迹/PG报告，不把里程碑或重复Wall当独立样本|
|六真实过程及完整相关联合材料|`report/TRADE_CASE_INDEX.json`、`JOINT_CASE_SUMMARY.csv`；`cases/T01`～`T06`各有原始TRACK_INPUTS_AND_CLOCKS、QUOTE_CONTEXT、六类同对象正式历史、两资格族×两方向F4原行与CASE_METRICS|
|F4真实源与多族去重关系|`sources/F4_SELECTED_READ_AUDIT.json`，每例F4_*_WINDOW.csv的原生source_row_index；T05的6资格行/3方向UTI不可当6笔成交|
|量义和现有F3条件|匹配 `absorb_assembler.py:132` 后取方向列绝对值；core约1116行丢弃trade_vol，264行起同价hit累计，1293行起公开补充代理。`pressure_big_deal.py:360` 后临时F3；core约61行pressure=T×share，Build wrapper约125行调用；研究F3列仅为源公式核算|
|一个业务量、两种期间的最小信息试查|`report/ONE_FIELD_RECORDED_VOLUME_PROBE.csv`、`ONE_FIELD_PROBE_SUMMARY.json`；18PG/13日期块，主比较含起点，另存不含起点控制；真成交归属和净撤减均为空|
|后续价格不被用作原因或预测证据|`report/CASE_FIXED_HORIZONS.csv`：统一cut后10/30秒，六例均在原owner窗口内；只作背景描述|
|取样与研究去向|`research/RESEARCH_DECISIONS.json`：明确记录在观察后保存，不假称预注册或严格留出；不新增充分依据独立点，保留N1/N2|
|图可对回原数|`figures/TRADE_CONTEXT_CASES.png/.pdf`、`QUOTE_QT_TRADE_CASES.png/.pdf`；三品种原量尺不跨品种合并，零值/期间边界清楚|

PG/日期关联块复用旧 Run `calls/C0002/audit/WINDOW_PROCESS_INDEX.csv`。32个实际交易日与23个日期关联块是不同口径，不能互换为独立样本数。本次既有样本广泛暴露，仅为同批探索性复用。

## 重放顺序和读取边界

在本根使用既有 `/m3c3/Linux/apps/anaconda3/bin/python`：

1. `research/ingest_qt_volume.py`：按manifest精确读取444原始/444QT表，新旧必要13列比较、日频阈值点核对和输入缓存。
2. `research/qt_trade_joint.py`：旧R1受QT影响的回查、正式Absorb与记录总量的两种期间关联、全部occurrence/每track末条表。
3. `research/build_track_context.py`：保留PG/日期关联、实际匹配候选及六例的选择入口；不读未来挑选。
4. `research/trade_cases.py`：六例同对象历史、F4稀疏定向读取、研究算式、两种期间图及固定后续切点。
5. `research/volume_profile.py`：轨迹/PG分母、代理时间核回和18PG已有总量试查。
6. `research/check_native_source.py`：只读原生CC六例与试查162定点；不全扫dense行情，也不认证feed完整性。
7. `research/finish_research_tables.py`：F4多族计数、联合摘要、QUOTE/QT/成交图与实际研究决定。
8. `research/verify_delivery.py`：冻结包、准确输入、计数/真值保留、图/案例及原数对应核验，输出 `report/LOCAL_VERIFICATION.json`。

所需对象均沿既有真实源，F4只对六例范围二分定位读值；没有运行生产或恢复源Chat。当前提取环境的 `cc.py`、`track_wall_candidates_core.py` 副本/hash见 `report/NATIVE_CC_SOURCE_CHECK.json`，只提供读入/候选语义，未扩大旧receipt fingerprint的覆盖声明。

研究快照大小与 SHA-256 在 `ARTIFACT_INDEX.json`；进度、Return和发布回读不作自引用快照，排除项明列。`publication/`保存真实exact refs、blob逐字节核验和写任务交回。专业研究核验不冒充controller物理回收或Manager已接受。
