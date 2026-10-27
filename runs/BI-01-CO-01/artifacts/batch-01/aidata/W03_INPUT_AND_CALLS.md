# W03 实际输入、调用和交付

work_order_id: BI01-CO-01-W03-CASES-30M-MID
worker_execution_id: BI01-CO-01-W03-dispatch-5e4fa62eaf
worker_thread_id: 01a17dd7-5033-7e63-b7a2-edd90b691c33
return_to: chatgpt:BI-01-CO-01:professional

## 交付入口与实际结果

本单实际执行了原日线重算、四窗方式二 core→页面→同 core board、既有原生组合、浏览器完整打开、五图目视及图内全量数据核对。新统一页是 **[原生平台节点 6148](http://192.168.11.40:5006/cae?node_id=6148)**，含 W02 完整概览及 C01—C04 的 30m/mid。辅助对象记录为 [6148 report](http://192.168.11.40:6244/graph/cae/6148/report)，实际五图打开使用前一原生入口。

正式文件全部在 [本次 delivery](delivery/bi01_co01_w03_cases_20261028_5e4fa62eaf/)：36 份完整原 CSV（12 份 1d、12 份 30m、12 份 mid）及 8 份原 manifest/索引/运行文件，逐字节核源与副本相同。[CASE_FILE_PLOT_INDEX.csv](delivery/bi01_co01_w03_cases_20261028_5e4fa62eaf/CASE_FILE_PLOT_INDEX.csv) 将每个 Case、品种、feature、节点、文件、SHA256、PlotSet 和图标题相连；[FILE_INDEX.json](delivery/bi01_co01_w03_cases_20261028_5e4fa62eaf/FILE_INDEX.json) 保留源绝对路径和副本位置。没有用抽样表或不可读取的本机路径代替数据。

本次共 753 行窗口 1d、8,928 行 30m、503 行 mid。四窗三个品种的 K 线 OHLC 均有效，窗口 1d 的全部字段与 W02 对应行相同，必要后续日期均存在。9 个 mid 点的确认坐标晚于请求终点，原字段完整保留；连续合约、换月/调整规则及源时区仍有未知，详见后文。技术核验不代替专业解释和整批接收。

## 授权、固定源与运行身份

- 完整工单：`f61e3c6d15c8150b2d183887a51341414e8d2a07:runs/BI-01-CO-01/artifacts/professional-R0008/WORKER_ORDER.md::full`，已全文读取；原 R8 最终回交 `398df1517218f47db2d9a01857b245d1368e329c` 的独立 Return 已核。
- 专业/数据 policy 固定 `f7f2bffe9bcddd951d5bf218d56449e8f42999ae`。操作入口固定 `/dwdhome/fy/cgpterm-bi01-co-01@86dec991abb27a927c1b5c22af1e51b3f39b918b`。既有实现候选 `235c0f29861340a56dbfd3bfd749532328583849` 不作为新 policy。
- 直接请求和执行程序来自 `84e4152b626502281fea64a66e72c50091566010`；现场使用的 `W03_CASE_INPUTS.json`、`run_cases.py`、原研究脚本/锚点/统计未改。请求 SHA256 `950466494465f0fc0c9b2cf4c8df4d1777bc7b728a496e83724c56cc1acaecbb`，调用脚本 SHA256 `c2685eceed4b863db4f8044775793dbe039427fbb6e0d11925237f9aa0227c60`。
- 输入构造器仍是固定 f7 的 `professional/case_observation/examples/aidata_inputs.py`，Git blob `8f44359b17dde2d30e985f20f4866e23742a8f28`。未导入旧 `probe.py`。
- 实际聊天 cwd `/dwdhome/fy/cgpterm`；技术 checkout `/dwdhome/fy/observe-iterate-bi01-co-01`，既有分支 `fy/multisymbol-case-observation-20261027`，开始时 clean，HEAD/首次 fresh 远端为 `16bc11681dd1e23857027269f9696dd4b8f2cdfa`。执行前实际写/读/删除临时探针通过，环境为 sandbox disabled / approval never。没有新建聊天或分支。
- 业务 cwd `/dwdhome/fy/BASE_E6_2`，调用入口 `/dwdhome/fy/BASE_E6_2/run-python.sh`，实际 Python `/m3c3/Linux/apps/anaconda3/bin/python` 3.10.13，pandas 2.3.2、numpy 1.26.4。浏览器核验使用已安装的 `/usr/bin/python` 3.12.3、Playwright/Chromium，没有安装或部署。
- Pro 的 invocation/token 只引用签发来源；本 Worker 执行身份是本文首列 dispatch ID，无独立被签发的 Worker token，不冒用 Pro 身份。

## 固定业务输入与现场版本

`OptContext` 通过原构造器传 `sof_name="TA_updto20240229_DBA"`、`stk_tlist="tick_test_all57_takeout_lcNsiNcy"`、`startDay="2021-01-01"`、`endDay="2024-02-29"`。`blk=extract_time_syms="blk@steel"`，实际展开且三个品种的时间键相同：`rb,hc,i`。日历 `night_end_at_2300`，generation `big`，`big_source.mode="manual"`，只建立四个 big 节点。实际 `run_brief` 的通用 `context_ref.start_day/end_day` 为 null，保留原件；这里的 Context 输入来自真实调用的 camelCase 字段及新旧 Context.fason 等值检查，不据 null 改写输入。运行的 search_start/end 是四窗联合边界 `2021-02-01→2023-10-12`，不是重新取得完整共同历史。

| Case | 核心收盘日期 | manual 请求边界 | 实际节点 | 原生 PlotSet |
| --- | --- | --- | --- | --- |
| CO01-C01 | 2021-03-09—03-31 | 2021-02-01→2021-04-07 | big_000001 | case_CO01_C01 |
| CO01-C02 | 2021-08-23—09-30 | 2021-07-01→2021-10-15 | big_000002 | case_CO01_C02 |
| CO01-C03 | 2022-05-10—06-08 | 2022-04-01→2022-06-24 | big_000003 | case_CO01_C03 |
| CO01-C04 | 2023-08-10—09-28 | 2023-06-01→2023-10-12 | big_000004 | case_CO01_C04 |

正式 feature 为 `KLine(freq="1d")`、`KLine(freq="30m")` 的 `closeUti` 行情 sidecar，以及 `ScaleTurnCalendar("mid")` 的实际点 `x/y`。实际参数 mid→`specTerm=M, stMembershipLine=0.3`，对应特征标识如下：

```text
kline_1d: KLine_b1c78a836a84daaa3c8fe02057af79a05db9614c
kline_30m: KLine_273ae3a17c71b574ce50c5106870d7348e2436da
scale_turn_mid: ScaleTurnCalendar_1108fcdf993ff41f1e26c18b3bf2097a3258a77f
```

实际参数组经 stats 定位为 `__default__`。没有生成 mid 子节点、改用 large 或手工增补节点。沿 W02 调用既有 `ensure_profile_runtime()`；本 brief 的 profile_id 空、version 0，不称为标准 Profile v4。

[DEPENDENCY_VERSIONS.json](w03/DEPENDENCY_VERSIONS.json) 保存相关仓库完整 HEAD、既有差异文件 SHA256 与运行前后状态，六个 checkout 的这些状态/字节一致：

| 组件 | 实际 HEAD | 既有差异 |
| --- | --- | --- |
| aidata | f58ea95c358b9ac31659c92b7bc20fe9bf7f8264 | clean |
| uplot | 13badc6c079eebe7242abd65e56b328c45dcee2a | pfw.py 已有 hover None 兼容改动，另有既存未跟踪副本/检查点 |
| frame | 4d0ff8f2640e07a8b9ff066c48114f451fca6cfe | clean |
| quant | c2dcad1b4a85f79d0d3d3f2986f00d803fa8f33a | clean |
| tis | f26495c23d4afd11dc8d03426eaf3ca5fd02f65b | STCalendar.py 已有空点转换兼容改动 |
| m3sof | f2d5b316b2d323c6344778f22561d56d258d252b | 既有环境配置差异，文件名/hash在版本记录，未提交配置正文 |

沿现有环境/数据绑定运行，不切换工具到 latest、不修改工具仓源码、全局配置、共享服务或注册。已有非空 mid 字段定义在实际 TIS 映射中定向核实，没有 Haskell 修改或无关编译。

## 实际命令和 API 顺序

以下路径中 `<repo>`=`/dwdhome/fy/observe-iterate-bi01-co-01`，`<aidata>`=`<repo>/runs/BI-01-CO-01/artifacts/batch-01/aidata`，`<new-output>`=`/dwdhome/fy/BASE_E6_2/mquant/aidata/test_runs/bi01_co_01_w03_cases_30m_mid_20261028_5e4fa62eaf`，`<run>`=`<new-output>/bi01_co01_w03_cases_20261028_5e4fa62eaf`。这些是路径缩写，完整 argv/cwd/时间在 [实际调用记录](w03/w03-attempt01.json) 和 [原生组合记录](w03/w03-native-attempt01.json)。时间记录均显式 UTC。

```bash
# cwd=/dwdhome/fy/BASE_E6_2；原W02 CSV，只读重算，没有API取数
/dwdhome/fy/BASE_E6_2/run-python.sh <repo>/runs/BI-01-CO-01/artifacts/batch-01/research/analyze_daily.py \
  --delivery-root <aidata>/delivery/bi01_co01_w02_1d_20261028_c4202eae70 \
  --anchors <repo>/runs/BI-01-CO-01/artifacts/batch-01/research/DAILY_ANCHORS.csv \
  --output <aidata>/w03/DAILY_RECOMPUTE.json

/dwdhome/fy/BASE_E6_2/run-python.sh -u <aidata>/run_cases.py \
  --repo-root <repo> --request <aidata>/W03_CASE_INPUTS.json \
  --output-root <new-output> --run-id bi01_co01_w03_cases_20261028_5e4fa62eaf

/dwdhome/fy/BASE_E6_2/run-python.sh -u <aidata>/w03/build_native_combined.py \
  --repo-root <repo> --request <aidata>/W03_CASE_INPUTS.json --run-dir <run> \
  --output-dir <new-output>/w03_validation --overview-node-id 6142

# 以下读取已有真实产物，不再建core或重取行情
python -u <aidata>/w03/inspect_native_page.py \
  --page-record <new-output>/w03_validation/COMBINED_PAGE.json \
  --output-dir <new-output>/w03_validation/browser_attempt01

/dwdhome/fy/BASE_E6_2/run-python.sh -u <aidata>/w03/validate_case_delivery.py \
  --request <aidata>/W03_CASE_INPUTS.json --run-dir <run> \
  --daily-root <aidata>/delivery/bi01_co01_w02_1d_20261028_c4202eae70 \
  --page-record <new-output>/w03_validation/COMBINED_PAGE.json \
  --output-dir <aidata>/delivery/bi01_co01_w03_cases_20261028_5e4fa62eaf

python <aidata>/w03/verify_render_alignment.py \
  --capture <new-output>/w03_validation/browser_attempt01/BROWSER_CAPTURE.json \
  --case-delivery <aidata>/delivery/bi01_co01_w03_cases_20261028_5e4fa62eaf \
  --daily-root <aidata>/delivery/bi01_co01_w02_1d_20261028_c4202eae70 \
  --output <aidata>/w03/RENDER_ALIGNMENT.json
```

| 实际事件 | UTC 时间 | 实参及结果 |
| --- | --- | --- |
| 新 run 进程开始 | 2026-10-27 23:12:42.732 | 独立目录此前不存在；最终 exit 0，总 62.251s（含环境入口） |
| build_chart_run 开始→返回 | 23:13:04.895→23:13:05.745 | `(brief,dry_run=False)`；返回本次新 run_id |
| build_big_world_chart_pages 开始→返回 | 23:13:05.746→23:13:07.140 | `(run,run_brief_input=brief,save=True)`；内部 overview 6143、四页 6144—6147，未截断；没有额外调用独立 overview |
| build_board_run 开始→返回 | 23:13:07.140→23:13:43.572 | `({**brief,run_id:run.run_id},reuse_core=True,dry_run=False)`；36 切片全成功，manifest/stats 返回真实绝对路径 |
| 原生组合进程 | 23:19:05.980→23:19:32.106 | 新 TestCAE1 节点 6148，exit 0，26.08s |
| Chromium 实际完整打开 | 23:22:07.026→23:22:21.863 | 原生 URL；5 Figures、10 canvases、无 pageerror/failed request，随后 Worker 查看整页及全部5图截图 |

原 manifest=`<run>/delivery/DELIVERY_MANIFEST.json`，stats=`<run>/manifest/feature_slice_stats.csv`，节点/窗口索引=`<run>/manifest/timespan_index.csv`。副本保留原绝对路径，并由新增 FILE_INDEX/Case 索引解析到 Git 可读位置，不改官方 manifest。页面返回 URL、实际打开、截图目视和图数核对是各自独立证据。

调用适配中，只读尝试旧 overview 的继承 `doShowCAEGraph()` 默认布局时得 IndexError；未因此创建节点或改冻结输出。实际生产布局来自已有 `_register_run_overview_graph`，改为只在本次调用脚本中恢复其进程内 PlotSet 后组合成功。`createUniqueWithFao` 前确认 TestCAE1 类已存在，未触发缺类注册。验证器最初将 CSV 空值与浏览器 NaN 直接比较报差，核实为 W02 已知 2023-03-13 空行情后显式比较缺失编码，原数据/哈希未改。显示范围转换首次遇到概览轴终点超出已有日历，改为明确保留该轴端点UTI和未知时间，未外推。没有 core 重跑、API 局部取数重试或额外窗口。

## 原 W02 日线重算

原输入固定 commit `3a761c4ebf4a203ec39cabbd1e9d25413b204f5a` 的完整 delivery。原 `analyze_daily.py` 实际核三份已知 SHA256、各763行、共同有序时间键、2023-03-13 15:00 唯一已知空行情，然后逐条核73个锚点（每锚点三品种）并重算12行核心统计，exit 0。[DAILY_RECOMPUTE.json](w03/DAILY_RECOMPUTE.json) 是实际结果。

按 case/symbol 与原 `DAILY_METRICS.csv` 的 n、核心起止及三个已发表数字字段逐项比较：12行日期/n准确相同，36个数字在文本末位半单位加4ULP浮点误差内，最大绝对差 `4.594596514980366919189691544E-10`。完整源文本值、重算浮点值、差和容差见 [DAILY_METRICS_COMPARISON.json](w03/DAILY_METRICS_COMPARISON.json)。没有通过修改原CSV、锚点或研究文句消除差异；此结果只证明原字节与计算对应。

[W02_FREEZE_CHECK.json](w03/W02_FREEZE_CHECK.json) 又将 W02 FILE_INDEX 中12份源文件及Git副本逐一核原SHA256，均未变。没有重取W02完整行情或把四窗1d当作新完整历史。

## 真实覆盖、缺项和时间口径

下表每个 Case 的行数对 rb/hc/i 均相同；三品种 30m 时间键逐项相同，OHLC有效行等于总行，空OHLC行0，未填零/前值/拼接异时点。全部原始 openUti/closeUti/openTs/closeTs/导出时间和每品种首末均在 [COVERAGE_AND_MID.json](delivery/bi01_co01_w03_cases_20261028_5e4fa62eaf/COVERAGE_AND_MID.json)。

| Case | 1d/每品种（行） | 1d 实际首→末收盘 | 30m/每品种（行） | 30m 实际首→末收盘 |
| --- | ---: | --- | ---: | --- |
| C01 | 41 | 2021-02-01 15:00→04-06 15:00 | 484 | 2021-02-01 09:30→04-06 23:00 |
| C02 | 69 | 2021-07-01 15:00→10-14 15:00 | 820 | 2021-07-01 09:30→10-14 23:00 |
| C03 | 54 | 2022-04-01 15:00→06-23 15:00 | 636 | 2022-04-01 09:30→06-23 23:00 |
| C04 | 87 | 2023-06-01 15:00→10-11 15:00 | 1036 | 2023-06-01 09:30→10-11 23:00 |

必要后续日期均在1d及30m有效数据中：C01 04-06；C02 10-08、11、12、13、14；C03 06-13、14、15、16、17、20、21、22、23；C04 10-10、11。日期列表来自 W02 实际有效日线而非猜交易所日历。所有本次1d日期也均有30m记录；逐日行数见 [INTRADAY_DATE_COVERAGE.json](w03/INTRADAY_DATE_COVERAGE.json)。没有另核完整交易所时段表，不能据此宣称每个理论30m时槽都存在；跨夜、周末与休市间隔保留原状。

边界是日期字符串的实际平台请求，本次末行如上，不承诺终点日全天覆盖。1d按 closeUti 切片，首行日线 openTs 可在请求开始前的夜盘（如C01为2021-01-29 21:00:00.500）；30m首行从请求首日日盘开始，所以不能机械把第一根1d解释为本窗30m的完整聚合。

UTI 的导出时间来自真实 `OptContext.sof.tsa_of("night_end_at_2300")["natural_tsa"]` 索引；`feature_slicer._uti_series_to_ts` 依该索引转换，未当作Unix时间或猜单位。K线 `closeTs` 与导出的 `closeUti_ts` 全量一致。原 `openTs` 的 `.500` 与按索引导出的秒级 `openUti_ts` 均保留，不擅自抹平。源时间输出无时区标识，没有给市场时间贴UTC/Asia-Shanghai；本文执行日志的UTC与行情时间分开。

未取得可核定的连续合约/主力切换、复权/调整算法或源时区规则，继续标未知。数据集、上下文和特征完全相同及逐行一致能支持本次同源比较，不能推出换月处的经济解释或不存在换月影响。

## mid 实际点与确认字段

实际正式CSV含 `x,y,xConfirm,yConfirm,x_ts,xConfirm_ts`。定向读取现场 `mquant/tis/frpExample/STCalendar.py`：`actual2D.x/y→x/y`、`confirm2D.x/y→xConfirm/yConfirm`，`to_df()` 合并 value1/value2并稳定排序。此为后端对象到字段的真实映射；本单未进一步证明投资者何时接收信息。不能把实际点x或图上的菱形当作确认时间。

| Case | mid行 rb/hc/i | 确认晚于manual终点的行 rb/hc/i |
| --- | --- | --- |
| C01 | 24 / 22 / 44 | 0 / 1 / 1 |
| C02 | 45 / 43 / 101 | 1 / 0 / 1 |
| C03 | 30 / 22 / 77 | 1 / 0 / 1 |
| C04 | 25 / 24 / 46 | 2 / 1 / 0 |

503行实际点全部在各自manual窗内，原x/y与同品种正式30m close逐点相同；无实际点缺对应30m bar、无重复实际点、无确认早于实际点。每品种在核心前/核心收盘区间内/核心后的点数及首末点/确认时间保留在 COVERAGE_AND_MID。9行未来确认完整源字段及准确CSV行号见 [MID_CONFIRMATIONS_OUTSIDE_REQUEST.json](w03/MID_CONFIRMATIONS_OUTSIDE_REQUEST.json)，最晚到2023-10-16 15:00。原切片按实际x取窗，确认坐标可在窗外，本次原生图只画实际x/y，不删这些行、不把未来确认改成窗内已知。

## 原生单页和实际查看

现场原组合脚本 `/dwdhome/fy/BASE_E6_2/mquant/aidata/test_runs/fy_owner_1d_30m_20261027/mid_combined_revision/build_native_combined.py` 已全文读取，其SHA256仍为 `14a1c846a602cbf8583696d694694de5700bf0f77eaab6fc82fc3c3f572b6008`。本次适配代码为 [w03/build_native_combined.py](w03/build_native_combined.py)，没有运行旧2013测试或旧run。新组合复用原W02节点6142的完整 overview PlotSet，旧PlotSet.fason SHA256 `65a1d559cef98ed8a29539f4396915c0d29d84d7c1f818dc44bcfda2247ed320`；与新正式run的Context.fason核为相同。新的 `TestCAE1→CAEGraph→GMap(5 PlotSets)` 原生对象编号6148，配置可 eval2 回读五个PlotSet，无临时名称注册依赖。[COMBINED_PAGE.json](w03/COMBINED_PAGE.json) 和 [原生配置](w03/combined_native_config.fason.txt) 保存准确对象及hash。

overview使用W02完整2021起1d：原行763/品种、有效OHLC762/品种、有效范围2021-01-04 15:00→2024-02-28 15:00，保留2023-03-13空行情。没有用本次四窗1d拼成全历史。其余四个标题分别为 `CO01-C01 / 30m / mid / 2021-02-01 → 2021-04-07` 等；完整标题来自实际 manifest，映射见Case索引。

颜色按品种，K线浅红rb/浅绿hc/浅紫i，mid用对应较深颜色菱形。`KPriceLine(std_method="ratio")` 与 mid `dynstd_method=True` 使用同一品种当前视口首个有效open作基数，纵轴是比值，不是价格。此规则经实际 `uplot/utlv2.py`、`uplot/dynstd.js` 与浏览器原值 `__prestd_*` 逐项核对；缩放改变基数是既有平台行为。K线横坐标是 `(openUti+closeUti)/2`，标签用收盘分钟；mid横坐标为真实x，不把两种横坐标含义混同。

`extra_time=0`，但Bokeh有自动轴边距，图轴可能早/晚于正式切片首末。实际浏览器 `x_range` 原值及通过同一natural_tsa对小数UTI作floor/ceil所得时间夹界见 [DISPLAY_RANGES.json](w03/DISPLAY_RANGES.json)，与正式CSV范围分别记录，不据轴边距声称多取得行情。概览右轴端点超出现有natural_tsa，保留原UTI并将其自然时间标未知；四例的两端均能在同一日历定位。该只读检查实际使用业务wrapper执行 `w03/map_display_ranges.py --repo-root <repo> --output-dir <aidata>/w03`，未调用Feature/core或取数。

[BROWSER_REVIEW.json](w03/BROWSER_REVIEW.json) 记录真实打开者Worker、UTC日期、五图标题、图例、渲染器、源ID、错误/请求状态和截图hash；[screenshots](w03/screenshots/)有整页及五张逐图截图，Worker已实际查看六张图。5图全部渲染，无空白/脚本错误/请求失败，overview每图例3个K线glyph、case每品种3个K线glyph加1个mid glyph。不是仅HTTP200或URL返回。

[RENDER_ALIGNMENT.json](w03/RENDER_ALIGNMENT.json) 从实际浏览器数据核全量11,217行K线（W02 2,289+本次30m 8,928）的原OHLC/volume、时间标签、中点横坐标和ratio数值，以及503个mid原x/y多重集及相同比值基数，全通过。W02三条空OHLC在Bokeh仍为NaN，无填补。浏览器原始数据位于 `<new-output>/w03_validation/browser_attempt01/BROWSER_CAPTURE.json` 并保留SHA256，正式可读原值全部由本次CSV及W02已有CSV交付，不依赖接收者访问此本机路径。

## 原件、日志和交回边界

[logs](w03/logs/) 为实际stdout/stderr的脱敏副本；[LOG_INDEX.json](w03/LOG_INDEX.json) 保留原日志gitignored位置/hash与副本hash、URI替换次数。14处非图页连接URI整串替换，提交副本去行尾空白；原始日志仅在 `artifacts/task-status/`，未提交认证串或配置正文。正式CSV/manifest/原生配置未为日志脱敏而改写。

本单不存在待修的core、board、四窗后续覆盖或统一页面依赖，没有未决发送或重复昂贵计算。全部Worker技术实物回原 `professional`，由其实际消费并处理四例支持/反证、当时可知边界、Owner入口和管理接收。Pro/Owner未由本Worker代登记看图；完整研究解释、管理接收和父任务关闭均未执行。未新建Goal、定时器、聊天或跨聊天发送；普通同分支GitHub回交及fresh回读后本单自然结束。
