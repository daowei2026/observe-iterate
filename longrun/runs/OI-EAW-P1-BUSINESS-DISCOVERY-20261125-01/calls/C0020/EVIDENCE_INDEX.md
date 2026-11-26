# S09 证据与重放入口

本地根：`/dwdhome/fy/BASE_E6_2/artifacts/oi-eaw-p1-business-discovery-20261125-01/calls/C0020`。本C正式43项输入逐项原ref/Git blob/bytes/SHA见 `SOURCE_INDEX.json`；任务正文精确副本 `sources/inputs/I035.md`。所有详细表/图/代码留本地，不编造各附件远端ref。

## 原件与冻结包

|阶段|正式冻结索引|本地根|文件数|SHA-256（索引本身）|
|---|---|---|---:|---|
|C0002|[exact index](https://github.com/daowei2026/observe-iterate/blob/2919b043df8ac5f2aafeebf425b93a25d118ab53/longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261125-01/calls/C0002/ARTIFACT_INDEX.json)|`/dwdhome/fy/BASE_E6_2/artifacts/oi-eaw-p1-business-discovery-20261125-01/calls/C0002`|24|`5658bad6ee359b9bae9e77b4582b1a6b3fc413b1a95e2f1170c3f46a0a2e522d`|
|C0005|[exact index](https://github.com/daowei2026/observe-iterate/blob/b9f722c3802b3380081946eb957a2c856f6466f9/longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261125-01/calls/C0005/ARTIFACT_INDEX.json)|`/dwdhome/fy/BASE_E6_2/artifacts/oi-eaw-p1-business-discovery-20261125-01/calls/C0005`|33|`d6d21bb24a068161411c7400d97d2dff46db112527d33daae4b829e4430a662d`|
|C0007|[exact index](https://github.com/daowei2026/observe-iterate/blob/3cc71052916ed182f19ba76464c9ad213cc85d0b/longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261125-01/calls/C0007/ARTIFACT_INDEX.json)|`/dwdhome/fy/BASE_E6_2/artifacts/oi-eaw-p1-business-discovery-20261125-01/calls/C0007`|103|`393df84bac279983ffea4bfec4432013db2fa2b920cf67a56718f883a95aff59`|
|C0009|[exact index](https://github.com/daowei2026/observe-iterate/blob/bdee0fa41e0fc7b17e619e45ad2011c8805c8370/longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261125-01/calls/C0009/ARTIFACT_INDEX.json)|`/dwdhome/fy/BASE_E6_2/artifacts/oi-eaw-p1-business-discovery-20261125-01/calls/C0009`|112|`7e426d82c7bb3ed3f0c8f11b79f990b47569bbf3dbadc53f517493d60b794db4`|
|C0011|[exact index](https://github.com/daowei2026/observe-iterate/blob/0e52ad9a51f2bc3803b2343b4b06daed616e91fa/longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261125-01/calls/C0011/ARTIFACT_INDEX.json)|`/dwdhome/fy/BASE_E6_2/artifacts/oi-eaw-p1-business-discovery-20261125-01/calls/C0011`|125|`6d20c0742c945e79d86b02d08a0929fdda710a6b6eee4baf851906c486e9e810`|
|C0013|[exact index](https://github.com/daowei2026/observe-iterate/blob/314804355a0a1e4458492ee536e67a2553f04452/longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261125-01/calls/C0013/ARTIFACT_INDEX.json)|`/dwdhome/fy/BASE_E6_2/artifacts/oi-eaw-p1-business-discovery-20261125-01/calls/C0013`|222|`da5538dd7700b5b83328f0ca7b49a5dd7223396b9aff2bce34bb68b826b7dab3`|
|C0015|[exact index](https://github.com/daowei2026/observe-iterate/blob/8cf263c0b2c2ada6b6916f093d5431c3a966cb82/longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261125-01/calls/C0015/ARTIFACT_INDEX.json)|`/dwdhome/fy/BASE_E6_2/artifacts/oi-eaw-p1-business-discovery-20261125-01/calls/C0015`|75|`87cc7744a712c6d31f40e6f0cf03061ae2d5cdcf8c900e95005b3714a6e34e5f`|
|C0017|[exact index](https://github.com/daowei2026/observe-iterate/blob/6a0072296dbdaf48f3972db3b974e4c6d417389e/longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261125-01/calls/C0017/ARTIFACT_INDEX.json)|`/dwdhome/fy/BASE_E6_2/artifacts/oi-eaw-p1-business-discovery-20261125-01/calls/C0017`|24|`0cefe93f748f636ad70eaf4776ebce978d749203a16812f3f147eee49196cf0c`|

8包718项共98,252,363 bytes；`report/FROZEN_FILE_AUDIT.json`列每项本次实核结果，旧索引不改写。`report/RAW_FILE_AUDIT.json`逐项核已知2,924源文件。读取/计算不等于本批actual producer可重跑。

## 主要认识与准确证据表

|认识|正式说明|准确本地数值/图/代码入口（相对于该C根）|
|---|---|---|
|R2 数量角色/参考价/切点|[R2定位](https://github.com/daowei2026/observe-iterate/blob/8cf263c0b2c2ada6b6916f093d5431c3a966cb82/longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261125-01/calls/C0015/R2_DESIGN_POSITIONING.md)，[结果](https://github.com/daowei2026/observe-iterate/blob/8cf263c0b2c2ada6b6916f093d5431c3a966cb82/longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261125-01/calls/C0015/report/R2_RESULT.json)|`R2_CASEBOOK.md`；`cases/R2-01`～`R2-04`下`CASE_METRICS.json/QUOTE_TRACE.csv/P1_AVAILABLE_HISTORY.csv/P1_SAME_LOCAL_WALL.csv`（原始引用在anchor_event.source_refs及SOURCE_INDEX）；`figures/R2-01.png`～04；`report/R2_STATISTICS.json`、`probe/BASELINE_INPUT.csv`、`TWO_LABEL_INPUT.csv`、`PROBE_AUDIT.csv`；`research/scan_r2.py/statistics_r2.py/probe_r2.py/verify_r2.py`|
|R1 当前量/阶段/复见|[R1定位](https://github.com/daowei2026/observe-iterate/blob/314804355a0a1e4458492ee536e67a2553f04452/longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261125-01/calls/C0013/R1_DESIGN_POSITIONING.md)，[结果](https://github.com/daowei2026/observe-iterate/blob/314804355a0a1e4458492ee536e67a2553f04452/longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261125-01/calls/C0013/report/R1_RESULT.json)|`R1_CASEBOOK.md`；`cases/*/CASE_METRICS.json`；`contact/cases/*`；`figures/R1-01.png`～04、R1-P01/P05/P07/P08；`contact/figures/R1-C01.png`～03；`report/CONDITIONAL_DENOMINATORS.csv`、`MATCHED_FIXED_FUTURES.csv`、`MINIMAL_BASELINE.csv`、`MINIMAL_ENHANCED.csv`；`scan/RECONTACT_SUMMARY.json`；`research/README.md`及scan_r1/conditional_r1/recontact_r1/probe_minimum/verify_evidence|
|R3 源可识别性|[R3定位](https://github.com/daowei2026/observe-iterate/blob/6a0072296dbdaf48f3972db3b974e4c6d417389e/longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261125-01/calls/C0017/R3_DESIGN_POSITIONING.md)，[来源实查](https://github.com/daowei2026/observe-iterate/blob/6a0072296dbdaf48f3972db3b974e4c6d417389e/longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261125-01/calls/C0017/report/SOURCE_AUDIT.json)|`S07_EVIDENCE.md`；`report/REUSED_CASE_SOURCE_CHECKS.csv`、`RECEIPT_FIELD_CHECK.csv`、`SUPPLIED_FIELD_COVERAGE.csv`、`MINIMAL_INFORMATION_DECISION.json`；`research/audit_sources_r3.py`及SOURCE_INDEX引用的CC/Absorb/typed合同原文|
|第一轮全对照|C0007/B1、C0009/B2、C0011/B3原报告和CASEBOOK；C0011 FIRST_ROUND_SYNTHESIS|每包`cases/*/CASE_METRICS.json`及原始引用、`figures/B*-01.png`～06及PDF；`report/CASE_SUMMARY.csv`、各SUMMARY/VERIFICATION；`research/README.md`与冻结选样/匹配配置|
|S02/S03范围|C0002与C0005冻结原件|C0002 `audit/WINDOW_PROCESS_INDEX.csv/PROCESS_GROUPS.json/FEATURE_AVAILABILITY.csv/FILE_INVENTORY.csv`；C0005 `research/SCAN_CONFIG.json`、`scan/PIECES.csv.gz/CANDIDATES.csv.gz/DISPLAY_REFERENCE_INDEX.csv.gz/WINDOW_SCAN.csv/SENSITIVITY.csv`与验证记录|
|S09另查方向|本C先冻结问题后实际核11片段|`research/S09_LOOKBACK_BASIS.json`；`report/S09_THIRD_ONLY_LOOKBACK.json`；`S09_LOOKBACK_RAW_VERIFICATION.json`给200唯一行/258来源行/12文件/17区间；`research/lookback_s09.py/verify_lookback_s09.py`；初次失败ATTEMPT_01与EXECUTION_NOTES保留|

表中目录下实际文件名以原冻结索引为准；不把概括性字段名当不存在的远端附件。69次旧深入的准确指标路径、图（若原为表格试查则给表）、PG/日期块与SHA统一列于 `report/CASE_REGISTER.json`。

## 版本、参数与时间政策

- Task/longrun固定b1bf8025dd49091e71c8814caf36c2e02aced198，controller固定da8dabfdaf9a46d563aab261bef77cb5d72d7782。D010@825306a116a40496aa19bf2ca6da8114ef0d9f2f；C0020 INVOCATION@ab33f347cd7823d66e0c6425520fabd221df07d2。Owner GO/Binding/最新粒度的exact ref在43项源表。
- 参考设计FRIA@8d58ddd3392a3e67ef5ba44adf2c4cd0c9077f9f，TIS@179016111ed0394f92025313e46bd13534932a74，FRP@cac6c912dd65a14acbd591ca57e0afd8ddb4ef13。具体代码路径、行区间、blob和本地原文SHA沿C0013/C0015/C0017 SOURCE_INDEX进入；不称本批实际运行版本。
- S03原配置：2/10/30秒，前60秒背景最少40个此前观测；基准large2/q95、change.3、load.5、retention.7；松/严配置在SCAN_CONFIG。B1/B2/B3、R1/R2选样规则及冻结时刻沿各selection/和README；未以未来价格调参。
- 数量保持供应原始单位；合约、正式计量与ticksize未知。价格差用观测格点rb/hc=1、i=.5，不把它当已认证合约最小变动。CSV时间无时区标记，不另造交易所时区或跨日合约身份；日期关联块是依赖分组，不等同所有案例自然日期（例如R2-02属于DB20211101而原时间为11月2日）。
- q包含t0/t1；C/V只累计t0<UTI≤t1。bid侧报价下降对应sell_order代理，ask对应buy_order代理。报价离开最优档时该价库存未知，不补0；内部时间一致不能替代feed覆盖认证。空本地快照保持空，不能用全局表静默替代。
- 两轮共用Owner同批目录，source_key9be111…是展示索引，不是正式code/upstream identity；没有新增行情、生产重跑、参数、公共上游或数据库修改。

## 本次复核实际做到了哪一步

`report/REPLAY_AUDIT.json`：718旧冻结项与2,924原始文件大小/SHA一致，56脚本AST、33PNG解码、33PDF文件头，错误0。`VISUAL_SPOT_REVIEW.json`列6张实际复看图及局部观察；不是全部PDF逐页渲染，也不是新未来样本或预测验证。旧各案例原执行中的逐行数值/P1属性/图核查记录继续有效；本C不把原自检当controller回执。

`research/audit_s09.py`按已知清单核文件和案例；`lookback_s09.py`只从旧表投影冻结的非future列；`verify_lookback_s09.py`只选择11片段内原始行再独立计算17区间。上述输出均已实际保存，本C只有这一小范围量变再核，无全量市场扫描。复核者可用`python research/check_delivery.py`只读核本C冻结包与关键一致性。旧研究生成器重放参数/环境从各research/README或代码CLI进入，输出应放新独立研究目录，避免覆盖原冻结成果。

## 结束与机器回交

`report/COMPLETION_EVIDENCE.json`对应S01～S09原生工作；`report/FINAL_RESULT.json`给目标部分达成、结束依据、未决问题及父Run未完成；`report/CANDIDATE_REGISTER.json`逐项保留原等级/出处并给取证顺序。`report/SAMPLE_USE_CUMULATIVE.json`原261条不变、现278；139旧区间口径与事件/来源回查分开，深入仍69。

正式报告/索引先发布，C0020零W PRO_RETURN后引用实际exact报告。全部远端写只在本Run获准前缀、同Personal连接Contents API，按真实head/不存在路径或blob条件串行写并exact回读。具体提交/父commit/回读与Git交回见publication/、PUBLICATION_READBACK.json与publication/RETURN_HANDOFF.json。父Run等原Manager实际消费，不能由本C单次Return代判。
