# W02 实际输入、调用与完整日线交付

work_order_id: BI01-CO-01-W02-FULL-HISTORY-1D
parent_task_id: BI01-CO-01-CASE-RESEARCH-01
work_id: BI-01
run_id: BI-01-CO-01
issuer_invocation_id: BI01-CO-01-R0006-f352c5b081
return_to: chatgpt:BI-01-CO-01:professional
worker_thread_id: 01a17dd7-5033-7e63-b7a2-edd90b691c33
worker_execution_id: BI01-CO-01-W02-dispatch-c4202eae70

## 结果与直接文件入口

本单已经实际调用现有 aidata，取得 rb/hc/i 三份完整正式 1d CSV。每品种 763 行，其中 762 行有效 OHLC、一行共同空行情；总行数 2,289，有效行情合计 2,286。共同有效时点 762 个，首末收盘时间为 **2021-01-04 15:00:00—2024-02-28 15:00:00**。这些是平台导出的无时区自然时间文本，没有擅自转换成 UTC。

| 品种 | Git 可直接读取的 CSV | 全部行 | 有效 OHLC | 空 OHLC | 原文件字节 |
| --- | --- | ---: | ---: | ---: | ---: |
| rb | [完整原文件](delivery/bi01_co01_w02_1d_20261028_c4202eae70/feature_slices/big_000001/symbol/rb/kline_1d/__default__.csv) | 763 | 762 | 1 | 114654 |
| hc | [完整原文件](delivery/bi01_co01_w02_1d_20261028_c4202eae70/feature_slices/big_000001/symbol/hc/kline_1d/__default__.csv) | 763 | 762 | 1 | 113702 |
| i | [完整原文件](delivery/bi01_co01_w02_1d_20261028_c4202eae70/feature_slices/big_000001/symbol/i/kline_1d/__default__.csv) | 763 | 762 | 1 | 111330 |

所有 CSV 是本次原文件的逐字节副本，保留全列、空值和原始时间字段；没有只取 head/tail，没有填零、插值、拼接异时点或按事后结果筛选。副本↔源绝对路径↔run/node/feature_key/df_key/字节/hash 的完整对应见 [FILE_INDEX.json](delivery/bi01_co01_w02_1d_20261028_c4202eae70/FILE_INDEX.json) 和 [COVERAGE.json](delivery/bi01_co01_w02_1d_20261028_c4202eae70/COVERAGE.json)。原文件仍保留在本次独立运行目录。

本次概览：[实际平台页面](http://192.168.11.40:6244/graph/cae/6142/report)，CAE 节点 **6142**，图内标题“全局概览 1d 板块有效行情范围”，图例 `rb - K`、`hc - K`、`i - K`。已由本 Worker 用既有 Chromium 实际打开并检查渲染，HTTP 200、一个 Bokeh Figure、无捕获到的 page error；[浏览器记录](review/OVERVIEW_BROWSER.json) 与[实际截图](review/overview_full_width.png)可核。原专业者和 Owner 尚未据本记录被宣称看过图。本页只有本次全范围日线概览，不是父任务最终的全部 Case 统一页面。

## 有权来源、版本和环境

工单 exact 来源：`daowei2026/observe-iterate@c5955c2e562ca0f318cf08278b81ff56d6479d4e:runs/BI-01-CO-01/artifacts/batch-01/aidata/W02_WORK_ORDER.md::full`。原专业者签发回交为 `703f9fc1213002619aa651ee1fbbeed7f84f819d:runs/BI-01-CO-01/provenance/turns/R0006/ROLE_RETURN.json::full`；原调用的实际发送回执为 COMMITTED，未由 Worker 改写。

源码/成果 checkout：`/dwdhome/fy/observe-iterate-bi01-co-01`；分支 `fy/multisymbol-case-observation-20261027`；开工本地干净，fresh fetch 后 HEAD 仍为 `703f9fc1213002619aa651ee1fbbeed7f84f819d`。聊天工作区仍为 `/dwdhome/fy/cgpterm`，与实际业务 cwd `/dwdhome/fy/BASE_E6_2` 分开记录。未另建分支，也未切换业务工具到 latest。

专业/数据合同固定 `f7f2bffe9bcddd951d5bf218d56449e8f42999ae` 的 02/03 全文；输入构造器仍为 `professional/case_observation/examples/aidata_inputs.py`，blob `8f44359b17dde2d30e985f20f4866e23742a8f28`。实际运行的 [run_overview.py](run_overview.py) 与签发的 `eacadfa7d16493ad792de56123f69f1f1c19a864` 原件逐字相同，SHA256 `98b79ce2d0b9d0c0699edb4c4c7e0c5c7950d443e3d5699d289bdd49d370b3ab`。没有导入带顶层旧测试执行的 probe.py。通用操作规则采用 `/dwdhome/fy/cgpterm-bi01-co-01@86dec991abb27a927c1b5c22af1e51b3f39b918b`，未修改该仓。

业务解释器为 `/m3c3/Linux/apps/anaconda3/bin/python`，Python 3.10.13，pandas 2.3.2、numpy 1.26.4；入口为现有 `BASE_E6_2/run-python.sh`。该入口沿用既有 m3rc、进程 PYTHONPATH/系统 TLS 预加载设置；未安装或升级依赖，未输出环境凭据。详细版本见 [PYTHON_ENVIRONMENT.json](calls/PYTHON_ENVIRONMENT.json)。

| 实际依赖目录 | 完整 Git HEAD | 执行前已有的已跟踪差异 |
| --- | --- | --- |
| aidata | `f58ea95c358b9ac31659c92b7bc20fe9bf7f8264` | 无已跟踪文件差异 |
| uplot | `13badc6c079eebe7242abd65e56b328c45dcee2a` | pfw.py |
| frame | `4d0ff8f2640e07a8b9ff066c48114f451fca6cfe` | 无已跟踪文件差异 |
| quant | `c2dcad1b4a85f79d0d3d3f2986f00d803fa8f33a` | 无已跟踪文件差异 |
| tis | `f26495c23d4afd11dc8d03426eaf3ca5fd02f65b` | frpExample/STCalendar.py |
| m3sof | `f2d5b316b2d323c6344778f22561d56d258d252b` | __init__.py；core/__init__.py；settings/app.py；settings/env/default.py；settings/env/dev.py；settings/env/prod.py；settings/env/test.py；settings/sof/CTP.py |

[uplot/tis/m3sof 的完整状态与本地差异文件 SHA256](calls/DEPENDENCY_VERSIONS.json) 已保留；未覆盖这些真实差异。uplot 的已有 pfw.py 差异是 hover 空 tooltip 的兼容修正；TIS 的 STCalendar.py 差异是空转折结果转换处理，本单没有实例化 ScaleTurnCalendar。m3sof 环境/数据配置文件有既有本地差异，未把含敏感值的配置文件上传。aidata、Frame、Quant 均无已跟踪本地差异。

`ensure_profile_runtime()` 本次仍按原脚本调用，现有实现仅通过既有 `mquant.worker.beat` 导入完成运行配置准备。本单没有新增 Feature 定义、改注册配置、修改工具源码或共享服务。本 brief 的实际 `profile_id=""`、`profile_version=0`；不能称为标准 Profile v4。

## 实际请求和一次调用链

完整输入、构造器来源和 API 实参见 [INPUT.json](INPUT.json)。固定请求实际保持：

| 项 | 本次实际值 |
| --- | --- |
| Context | sof_name=`TA_updto20240229_DBA`，stk_tlist=`tick_test_all57_takeout_lcNsiNcy`，startDay=`2021-01-01`，endDay=`2024-02-29` |
| 对象 | blk=extract_time_syms=`blk@steel`；本次真实展开 `rb,hc,i` |
| 日历/节点 | calendar_override=`night_end_at_2300`；generation_depth=`big`；big_source.mode=`manual` |
| 窗口 | `("2021-01-01", "2024-02-29", "full_history")` |
| 正式证据 | `KLine(freq="1d")`；uti_fields=`closeUti`；feature_key=`kline_1d`；slice_levels=`["big"]`；market_context_sidecar |
| aidata run_id | `bi01_co01_w02_1d_20261028_c4202eae70` |
| output_root | `/dwdhome/fy/BASE_E6_2/mquant/aidata/test_runs/bi01_co_01_w02_full_history_1d_20261028_c4202eae70` |

实际执行命令（cwd=`/dwdhome/fy/BASE_E6_2`）：

```bash
/dwdhome/fy/BASE_E6_2/run-python.sh -u /dwdhome/fy/observe-iterate-bi01-co-01/runs/BI-01-CO-01/artifacts/batch-01/aidata/run_overview.py --repo-root /dwdhome/fy/observe-iterate-bi01-co-01 --output-root /dwdhome/fy/BASE_E6_2/mquant/aidata/test_runs/bi01_co_01_w02_full_history_1d_20261028_c4202eae70 --run-id bi01_co01_w02_1d_20261028_c4202eae70
```

| 顺序 | 实际 API 与实参 | 本次结果 |
| --- | --- | --- |
| 1 | `build_chart_run(brief, dry_run=False)` | 成功，返回上述同一 run_id；2026-10-28 05:02:03.028—05:02:03.522（Asia/Shanghai，来自 UTC 日志换算） |
| 2 | `build_run_overview_chart_page(run, run_brief_input=brief, save=True)` | 成功，返回节点 6142 的 URL；05:02:03.522—05:02:04.098 |
| 3 | `build_board_run({**brief, "run_id": run.run_id}, reuse_core=True, dry_run=False)` | 成功，同 core；05:02:04.098—05:02:12.733，3 份切片全部导出，0 失败、0 空切片 |

包装进程从本地 05:01:42.058 到 05:02:14.214，退出码 0，实测 32.127 秒，包含环境准备及导入。准备、恢复中断和后续验收不包含在这一个进程的计时中；本单总投入没有独立可靠边界，保持未知。没有第二次昂贵取数，没有 API 重试；服务重启恢复时先核已完成记录，再继续验收。

未调用 `build_big_world_chart_pages`，未生成 30m/mid，也未执行 Case 页面组合。两次浏览器读取的是同一个已创建的 6142 概览，用于打开及适配 2400 像素画布；不算重复生成 aidata run 或页面。

[实际执行身份/命令/起止/退出码](calls/W02_EXECUTION.json)、[stdout](calls/W02_STDOUT.log) 与[脱敏 stderr](calls/W02_STDERR_REDACTED.log)已提交。框架原 stderr 含连接认证串，原件仅留 gitignored 运行证据；提交版将连接 URI 脱敏为 `bolt://[REDACTED_CONNECTION_URI]`，保留原错误/成功事实。本次没有被隐藏的调用失败。

## 正式 manifest、DataBinding 与时间口径

正式来源为本 run 的 [DELIVERY_MANIFEST.json](delivery/bi01_co01_w02_1d_20261028_c4202eae70/delivery/DELIVERY_MANIFEST.json)、[feature_slice_stats.csv](delivery/bi01_co01_w02_1d_20261028_c4202eae70/manifest/feature_slice_stats.csv)、[timespan_index.csv](delivery/bi01_co01_w02_1d_20261028_c4202eae70/manifest/timespan_index.csv) 及其实际文件引用；没有套用旧测试节点或行数。本次 manifest 真实节点是 `big_000001 / full_history`，这是全范围输入节点，不是已经选出的业务 Case。formal CSV 的 df_key_normalized 实际为 `__default__`。

DataBinding：feature_ppid=`KLine_b1c78a836a84daaa3c8fe02057af79a05db9614c`，feature_identity_hash=`fc156d30e8cbdbd780acc6f8e5300ebbab0629aa`，feature_params_hash=`ae8e6b5a2a3114253fab77f45ada478c29f78f1a`；time_mode=`uti_point`，uti1_field=`closeUti`，interval_policy=`point_inside`。复制了原 [run_brief.json](delivery/bi01_co01_w02_1d_20261028_c4202eae70/run_brief.json)、[run_summary.json](delivery/bi01_co01_w02_1d_20261028_c4202eae70/manifest/run_summary.json) 与 chart/page 索引。context_ref 的 start_day/end_day 仍为原序列化的 null，未改原件；实际 camelCase 构造输入、完整窗口和真实数据覆盖分别由 INPUT.json、调用原件和本次 CSV 记录，不能由这两个 null 推断未设置日期。

UTI 是当前日历 `natural_tsa` 的索引。已定向核本次 aidata 实现 `feature_slicer.py` 的 plotctx_uti_window、add_natural_time_columns、_uti_series_to_ts：通过 `context.sof.tsa_of(calendar_name)["natural_tsa"]` 映射，并以 `%Y-%m-%d %H:%M:%S` 输出补充自然时间列。没有把 UTI 猜成 Unix 秒/毫秒。CSV 没有时区偏移，源数组的具体时区标签本次未独立核定；按平台导出文本使用。

每份 CSV 原始时间字段为 `openUti/closeUti/openTs/closeTs`，并保留 aidata 补充的 `openUti_ts/closeUti_ts`。第一行 openUti=`72003600`、closeUti=`72030599`，原生 openTs=`2021-01-04 09:00:00.500`、closeTs=`2021-01-04 15:00:00`；末行 openUti=`103233600`、closeUti=`103274999`，openTs=`2024-02-27 21:00:00.500`、closeTs=`2024-02-28 15:00:00`。补充 `_ts` 列格式精确到秒，不能用其舍去的小数精度覆盖原生 openTs。全部 763 行的 closeTs 与 closeUti_ts 相符；三个品种在共同 raw UTI 上的自然时间映射也全部一致。

请求结束 `2024-02-29` 是窗口边界，实际最后收盘为 2024-02-28；没有声称包括 29 日全天。请求起点 2021-01-01 与实际首条 1 月 4 日分开记录；本次没有调查或断言 2021 前是否存在历史。

## 有效性、共同范围和实际缺口

有效 OHLC 的核验定义为四价均为有限数值且 `low <= open,close <= high`。每品种 762 行符合，0 行价界矛盾，0 重复 closeUti，索引有序。三品种原始 763 个时点集合一致，没有某成员独有或相对共同 raw 索引缺行；有效交集 762，没有拼接不同自然时间。

**共同空行情：2023-03-13 15:00:00，closeUti=`93715199`**。三品种该行 OHLC/openInt 均为空、volume 原值为 0，原生窗口为 2023-03-10 21:00:00.500—2023-03-13 15:00:00；已原样交付。不能用 0 价格、前值或其他时点补成有效日线。其原因本次未由正式数据源另行说明，未自行认定为休市，也未反复重跑相同输入求消失。

按已观察共同索引分段，有效部分为 2021-01-04—2023-03-10 共 529 行，以及 2023-03-14—2024-02-28 共 233 行；这是对共同空行情的定位，不是新建研究阶段。跨这一日期的收益/路径解释需保留该缺口；其余已有可靠共同数据可由原专业者继续消费。

[LONG_GAPS.csv](delivery/bi01_co01_w02_1d_20261028_c4202eae70/LONG_GAPS.csv) 列出原始相邻收盘自然时间间隔大于 3 日的全部 60 条记录（三品种各 20 条）。最长为 2023-09-28→2023-10-09 和 2024-02-08→2024-02-19，均 11 个自然日；另有若干 10 日间隔。这只是自然日跨度，不把周末/长假或未核明原因的间隔自动算成漏交易日；未通过平行数据入口另造交易日历来填补。

## 价格、展示与已知限制

正式 CSV 来自上述 KLine sidecar 原文件，交付过程未作价格归一化。当前概览实现 `big_world_chart.py:_register_run_overview_graph` 使用 `KPriceLine(feat=KLine(freq="1d"), std_method="ratio")`、`extra_time=0`，所以图中的 ratio 坐标不等于 CSV 原始价格；图的轴刻度/留白也不代替正式范围。ratio 的具体基准算法本单未独立复验。

数据集与 KLine 身份已记录，但本批 CSV 不含底层合约代码、换月标记或调整算法字段；连续合约组成、换月日及前后调整的具体规则本次仍未知。原专业者若作依赖这些细节的解释，应定向取得所需依据；本 Worker 未修改口径、猜测复权规则或据图形推断它们。

原 DELIVERY_MANIFEST 及 PACKAGE_INDEX 中可选通用包仍指向业务环境原目录，本次 Git 交付复制了必须消费的三份完整原始 CSV、必需索引和可复现来源，未冒称复制全部通用模板包。工具自动生成包中的 LocalTurnNarrative/default_no_code 等模板文字不替代本任务已采用的 CASE_OBSERVATION/f7 合同；本单没有改写原模板。

## 后续复用位置与尚未执行

已方便定位原测试补充报告和真实引用的组合脚本，准确路径及脚本 SHA256 见 [OPTIONAL_COMBINATION_SOURCE.json](calls/OPTIONAL_COMBINATION_SOURCE.json)：`/dwdhome/fy/BASE_E6_2/mquant/aidata/test_runs/fy_owner_1d_30m_20261027/mid_combined_revision/build_native_combined.py`，SHA256 `14a1c846a602cbf8583696d694694de5700bf0f77eaab6fc82fc3c3f572b6008`。本单未运行该旧测试或该组合脚本，旧窗口/旧 URL 不作为本批结果。

本单把正式共同日线、真实调用和概览状态交回原签发专业者。尚未执行的是原专业者的全批候选比较、3–5 个不同用例与自主回看解释，以及其后依据真实窗口签发的 30m/mid 图数、最终全部 Case 统一页面、Owner 入口和管理接收。本次概览生成、数据核验和 Worker 返回不代表这些工作完成，也不新增管理 Gate。
