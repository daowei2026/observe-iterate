# W04 实际输入、候选改动、运行与未通过项

order_id: BI01-CO-01-W04-OVERVIEW-SHADOWS-AND-STORY-VIEW

worker_execution_id: BI01-CO-01-W04-worker-ac26d5b83e

return_to: chatgpt:BI-01-CO-01:professional

## 当前结果

**本次未取得阴影及四例图面通过。** aidata候选源码及定向回归、持久参数保存/独立回读、冻结输入保护和定向字段核对已经完成。两项真实运行环境问题阻止继续实看：新页6149的共享运行进程仍使用旧参数定义；旧页6148和本地正常布局均遭遇同一自然日历文件的NFS I/O error。未刷新共享服务/注册、替换日历、修NFS或部署。

本次保存对象 **[6149](http://192.168.11.40:5006/cae?node_id=6149)** 是待运行时采用的候选，当前显示参数错误，不能作为已可用的新统一页。旧 **[6148](http://192.168.11.40:5006/cae?node_id=6148)** 原对象未变，但本次重新打开也因日历I/O失败而没有价格图。旧W03已完成事实保留，不能据此否认当时通过，也不能拿旧通过代替本次核验。

## 授权和真实身份

完整工单精确源 `ad7d3b94b04f93f2f188e99409b7ee39f10f4bbb:runs/BI-01-CO-01/artifacts/professional-R0013/WORKER_ORDER.md::full`，实际Git原件11530字节，SHA256 `3b5a1336be72b9601eba7357c84a2c25116ca13aa6b3b1e2b8c85e08f32c0316`，与派工原文相符。

Owner修正/专业方法采用dd89be6e93ad758385cf0e3a15bc9363cb87f2b0；管理采用34189351253d7355986b2516e555aaadfd540829；任务/Binding da7f038e97e5ba9639886ed0a6e146ad59912d15；地图dee3f2203d0fce3c03f99566fc4aa0914ec69ecc及ee836a23下真实恢复GO已按职责读取。操作入口仍86dec991abb27a927c1b5c22af1e51b3f39b918b；已采用工具实现235c0f29861340a56dbfd3bfd749532328583849不被本候选替换。没有新建Reader、Goal、聊天、分支或定时器。

当前聊天 cwd 实测 `/dwdhome/fy/cgpterm`，环境 `CODEX_THREAD_ID=01a17dd7-5033-7e63-b7a2-edd90b691c33`；实际写/读/删探针通过，sandbox disabled、approval never。开始UTC `2026-10-28T11:43:49.364154+00:00`。本地执行turn标识 `w04-b3576f243562448ba4659eb7dcfe9e71`，与派工/线程/开始时间关联。原生Codex turn ID未由环境暴露，只读应用查询未返回后已取消，不补造；详见 [WORKER_EXECUTION.json](WORKER_EXECUTION.json)。不使用原Pro invocation/token作为Worker身份。

观察checkout `/dwdhome/fy/observe-iterate-bi01-co-01` 起始clean、HEAD 1f7e4b441c2c0381790393fc46e61bc63c93171c，沿指定分支快进至b8ea40deb7d429dfe5c0af38197d3722560df529保留既有管理/专业成果；未重做W03。业务cwd `/dwdhome/fy/BASE_E6_2`，沿用 `run-python.sh` 和现有业务Python/配置、现有host Playwright/Chromium，无安装。

## 直接输入和保护

全文读取 `0b95b59237054eff3b001dd14b784052208a94e2` 下 `research/STORY_VISUAL_CHECKS.md`，定向完整消费四例R0013辨别故事；数值核对使用同快照 `R0013_JUDGMENT_CHECKS.json`。没有修改Case正文、判断、赢家、Owner入口、管理决定、任务、Binding或Intake。

W02/W03正式CSV、manifest及原运行文件复用；[FROZEN_INPUT_CHECK.json](FROZEN_INPUT_CHECK.json) 将两单FILE_INDEX内56份源文件与Git副本逐项核原SHA256，运行前后均相同。未执行 `build_chart_run`、`build_big_world_chart_pages`、独立overview、`build_board_run`，没有新core、新行情或mid计算交付。

W03冻结run=`bi01_co01_w03_cases_20261028_5e4fa62eaf`，现场run目录为 `/dwdhome/fy/BASE_E6_2/mquant/aidata/test_runs/bi01_co_01_w03_cases_30m_mid_20261028_5e4fa62eaf/bi01_co01_w03_cases_20261028_5e4fa62eaf`。原索引与Git副本字节相同，blob仍 `809bd1aa9a07b12f57dea5f96f2689e0fcc83868`。

| Case | 冻结node | 原start_uti/end_uti字符串 | PlotSet |
| --- | --- | --- | --- |
| CO01-C01 | big_000001 | 2021-02-01→2021-04-07 | case_CO01_C01 |
| CO01-C02 | big_000002 | 2021-07-01→2021-10-15 | case_CO01_C02 |
| CO01-C03 | big_000003 | 2022-04-01→2022-06-24 | case_CO01_C03 |
| CO01-C04 | big_000004 | 2023-06-01→2023-10-12 | case_CO01_C04 |

6148的真实fason与W03原件SHA256均为 `c120d15683e4f41fc7944f40fa89c3dc413ddfb0184efbed2c741e8266f0bdc0`。6149复用其五个PlotSet，完整概览仍对应W02的2021起1d，其余为四例30m/mid。独立进程回读确认五图参数相同、原6148未变、四个原始范围及Case/node标签保存完整，见 [PERSISTENCE_READBACK.json](PERSISTENCE_READBACK.json)。这只证明保存/恢复参数，不证明当前共享服务成功布局。

复用的Context/数据绑定仍为 `TA_updto20240229_DBA`、`tick_test_all57_takeout_lcNsiNcy`，`startDay=2021-01-01/endDay=2024-02-29`，`blk=extract_time_syms=blk@steel`，成员rb/hc/i，`night_end_at_2300`。big是节点、30m是频率、mid是ScaleTurnCalendar参数，均未改变。

## aidata候选改动和版本

实际工具checkout `/dwdhome/fy/BASE_E6_2/mquant/aidata`，开工为既有分支 `codex/aidata-named-csv-features-20261019`、HEAD f58ea95c358b9ac31659c92b7bc20fe9bf7f8264、clean。这是现场实值，不是切回历史版本。已在该同一分支普通提交：

`b5a752c2701dd8997b47583808f30bc5da5d9769`

只改 `big_world_chart.py` 和新增 `tests/test_overview_scope_restore.py`。完整可读取diff为 [AIDATA_SHADOW_REPAIR.patch](AIDATA_SHADOW_REPAIR.patch)，commit/父版本及patch hash在 [TOOL_COMMIT.json](TOOL_COMMIT.json)。工具仓按工单完成现场提交，未向现场工具远端推送；完整patch随观察仓GitHub回交，不只留本机源码路径。

功能提交为a014f639a11a5b7763fd573f2cd31ef145c7e12a，最终b5a752c仅准确化一条原生恢复路径注释，AST与已测功能提交完全相同；没有据此重跑无关测试或制造新的实跑结果。

具体修改：

- 既有AidataRunOverviewCAE增加可选持久五图配置及冻结范围JSON；正常布局只向唯一的完整概览附四个范围和标签，Case图保留原行情/转折。新分支路径明确回到本类layout，未修改共享原生入口。
- `_review_window_bounds` 保留既有数值/小数/单点窗口；日期复用正式切片的 `feature_slicer.plotctx_uti_window`，其半开窗口 `[start,stop)` 对Box使用 `stop-1` 的原end坐标。底层是同一Context/日历的 `uplot.timesearch`，结束点在非交易时间按既有搜索规则取前一索引，不追加自然日，不用Unix或首末有效行情替代。
- 解析失败显式报错；保留已有 `_add_window_box` 和 `_review_scope_toggle`。同文件其他直接调用者传入其既有Context/日历，避免日期处理新行为缺少上下文；未改uplot/frame/tis/frp。
- 默认非组合overview仍保留search与big标记；无新类、Feature或持久注册。34项定向回归检查这些路径，不能外推生产PASS。

[DEPENDENCY_VERSIONS.json](DEPENDENCY_VERSIONS.json) 保存六个相关checkout前后HEAD/status/既有差异hash。除aidata上述提交外一致；uplot的pfw.py既有修改、tis/STCalendar.py既有修改及m3sof既有配置差异保留，没有覆盖或提交到本单。无安装、部署、服务重启、NFS或全局注册动作。

## 实际调用与重试

本次新显示输出目录 `<out>`=`/dwdhome/fy/BASE_E6_2/mquant/aidata/test_runs/bi01_co_01_w04_shadows_20261028_ac26d5b83e`。下文 `<repo>` 为观察checkout，`<w04>` 为其本文件所在目录，`<run>`为上述冻结W03现场目录。完整记录/原件引用在 [logs](logs/) 和 [LOG_INDEX.json](LOG_INDEX.json)，原日志只留gitignored。

```bash
# cwd=/dwdhome/fy/BASE_E6_2；业务wrapper，实际两次建页入口
/dwdhome/fy/BASE_E6_2/run-python.sh -u <w04>/build_shadow_page.py \
  --repo-root <repo> --run-dir <run> --output-dir <out>
# 上次在读取natural_tsa时失败，尚未写出native配置或调用createUniqueWithFao。
# 实际第二次只保存已验证能序列化的参数，明确不把未执行layout记通过：
/dwdhome/fy/BASE_E6_2/run-python.sh -u <w04>/build_shadow_page.py \
  --repo-root <repo> --run-dir <run> --output-dir <out> --defer-layout

# cwd=<repo>，host Python；只读原CSV准备具体视口/字段定位
python <w04>/prepare_story_views.py --repo-root <repo> --page-dir <out>

# cwd=/dwdhome/fy/BASE_E6_2；独立进程正常DAO读取，不再创建节点或做行情计算
/dwdhome/fy/BASE_E6_2/run-python.sh -u <w04>/verify_saved_page.py --page-dir <out>

# cwd=<repo>；真实浏览器，分别执行browser_attempt01及02独立目录
python -u <w04>/check_native_views.py --page-record <out>/SHADOW_PAGE.json \
  --views <out>/STORY_VIEWPORTS.json --output-dir <out>/browser_attempt02 \
  --fallback-url 'http://192.168.11.40:5006/cae?node_id=6148'
```

| 实际动作 | 结果及时间 |
| --- | --- |
| 定向pytest attempt01 | 4 failed/30 passed，26.30s。测试最初误将非交易时间end期待为下一索引，另误把BoxZoom工具overlay计入scope；按真实timesearch及figure.center修正测试，未放松原输入hash |
| 定向pytest attempt02 | 34 passed，22.41s |
| 补齐原生恢复路径后attempt03 | 34 passed，20.57s，两条既有依赖警告；这是最终源码的相关验证 |
| build attempt01 | 本地同Context读取natural_tsa.dba返回Errno5；未到节点创建。起止未单独完整计时，不补造精确耗时 |
| build attempt02 | UTC 12:06:12.292→12:06:32.251，exit0，只保存参数，`local_layout_executed=false`；新节点6149，无新类注册，不是阴影PASS |
| 独立持久参数回读 | UTC 12:21:46.362，PERSISTED_PARAMETERS_PASS；四范围、五原PlotSet、旧6148未变 |
| browser attempt01 | 新6149及旧6148均未得到五张价格图，exit2；60s等待不足以取得旧页最终错误，不据此猜旧页根因 |
| browser attempt02 | UTC 12:15:31.754→12:21:40.921；6149明确旧参数定义拒绝，6148等待360s后同时取得同一自然日历I/O错误文本；两次HTTP200都不算布局成功，exit2 |

## 两项实际缺口及受影响范围

**共享运行进程的参数定义仍旧。** 新6149在 `insights/trier/server/bokeh.py:create_layout → cae.doShowCAEGraph → Fao参数实例化` 报错，服务端列出的允许字段没有 `combined_graph_config` 和 `overview_scope_rows_json`。当前工程进程用新源码可保存及独立恢复参数，现有共享进程未采用新增定义。错误全文见 [initial_error_sanitized.txt](browser/initial_error_sanitized.txt)。没有据文件已改/代码已提交声称运行端采用成功。

**既有自然日历当前不可读。** 本地首次正常布局及旧6148本次打开均报：

```text
OSError: [Errno 5] Input/output error:
/m3varI/BaseData/futures/TA_updto20240229_DBA/sof/../calendar/night_end_at_2300/natural_tsa.dba
```

旧页调用链为 `CAEGraph.layout → PlotSet.plot → PlotCtx.__init__ → sof.tsa_of(calendar)[natural_tsa] → DbArray`。错误全文见 [fallback_error_sanitized.txt](browser/fallback_error_sanitized.txt)。旧6148持久对象仍与原W03配置一致，错误不是本单倒写旧图证据。

更新共享运行时定义/注册或部署，以及恢复NFS/底层数据可读性均超出工单§1的“aidata页面组装及范围坐标局部修复”写面；该节明确禁止全局注册、安装部署或共享服务修改。未尝试越权修复、换数据绑定或用其他日历绕过。

因此四个**原始**范围和Case/node对应已核；四组**实际数值UTI**未成功计算，`RANGE_COORDINATES.json=[]`准确表示第二次只保存未布局，不是0窗口或转换通过。未用CSV第一/最后bar补造阴影坐标，未机械加一天。四个阴影像素、独立重开成功、缩放边界/宽度/遮挡、范围隐藏/恢复均未通过/未执行。

## 四例故事图面与定向字段核对

已按原Pro要求准备17个具体视口，见 [STORY_VIEWPORTS.json](STORY_VIEWPORTS.json)。其中x_start/x_end仅用于Bokeh视口，来自所选原30m bar的openUti与末closeUti+1，记录原openTs/closeTs及UTI_ts差异；**不是阴影边界转换结果**。没有用视口坐标替代四个冻结范围。

| Case | 已准备的必要视图 | 本次实际图面结果 |
| --- | --- | --- |
| C01 | 03-04—15依据；03-09—22首次失败；03-22—31 i反弹与后段推进 | 0张价格图/截图；三品种共同可读性及hc失效等关系未核 |
| C02 | 08-23—09-09两次恢复/回落；09-09—30回吐；09-22—24局部反例；10-08—14后续 | 同上，不能用9月底赢家或源数字代替实看 |
| C03 | 05-05—23依据；16—23共同反向/恢复；23—26再反向；05-30—06-08延伸；06-08—23失败 | 同上，未声称5月31日和6月1日图面已辨 |
| C04 | 07-10—28旧状态；08-10—21依据；21—29失败升级；09月重新恢复；10月失效 | 同上，未以0.09个百分点或0.5价位差制造“明显可见” |

[FIELD_LOCATIONS.json](FIELD_LOCATIONS.json) 只核R0013的19组时间对×三品种=57项原收盘/算式，均匹配。准确CSV路径/行号/hash和关键锚点保留，未重算全历史。它不证明故事合理或图面清楚。ratio基数变化、mid实际/确认、closeTs/closeUti_ts差异及历史可接收资格保留原限制；因未进入价格图，未制造“本次缩放基数”或hover成功记录。

[VISUAL_STATUS.json](VISUAL_STATUS.json) 逐视口明确NOT_VISUALLY_VERIFIED；[browser](browser/)保留真实两轮浏览器结果及错误页面截图。实际打开者是Worker Codex/现有Chromium，Worker实际查看的是错误页像素，未将其写成价格图、Pro或Owner看过。

## 可继续的位置

原Pro可以立即消费候选patch、34项定向回归、独立参数回读、57项字段定位及全部缺口，继续不依赖当前图面的研究。运行环境由有权责任者恢复日历读取并使共享运行端采用aidata候选定义后，先对已存在6149做正常重开及转换/阴影检查，不重复创建同一对象、core或行情。之后运行已交浏览器程序完成全范围/局部缩放/显隐和17视口，按实际像素回报清楚、部分或不支持项，再由原Pro修正解释和Owner入口、原管理接收。此处是剩余依赖与复用位置，不是Worker自行签发部署或新无限工单。
