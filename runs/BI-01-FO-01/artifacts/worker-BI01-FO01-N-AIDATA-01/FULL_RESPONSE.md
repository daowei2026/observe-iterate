# BI01-FO01-N-AIDATA-01 Worker 技术回交

返回目标：`chatgpt:细节叙事生成_金标:BI01-FO01-执行`

order_id：`BI01-FO01-N-AIDATA-01`

技术状态：`TECHNICAL_RETURN_READY`

业务状态：未由 Worker 判定；须由原执行 Pro 消费真实图、数据和边界后继续。

## 一、结论先行

本次已在真实 Linux 现场完成一个具名首轮 Case：rb、As-Of `103315800`（标签 `2024-02-29 14:55:00.500000`）。正常 N 入口以完整 rb/hc/i 三来源和 `CalType.OnlyRead` 取得 24 张具名表；正常 `U2MainlineKLineInput` 又以 `CalType.OnlyRead` 取得同绑定的原 5m OHLC、close、`open_uti`、`calendar_position`、`calendar_time`。没有重跑 N/Source 全历史，也没有以旧 R33 数字替代本次读回。

本次未发现必须修改 aidata 的缺口。现有 `fixed_input`、点／线／线段／OHLC／表格和同源 `plot_view_data` 已能真实消费本次投影，因此没有新建 aidata 分支，也没有改 TIS、FRP、core、SDK 或共享 BASE 工作树。已生成长、中、局部三张交互图，平台 URL 均由真实浏览器打开为 HTTP 200，并保存本地 HTML、平台/本地截图和同范围导出数据。

有限技术检查结果：表地址/Life/Binding 关系全部成立；两窗 Life 无重合，working Life 未混入完成窗；原价范围 4760 行、Calendar 位置连续、close 无非有限值；六项完成窗统计、36 个 LOO 槽、working 数值及节律合计 72 项参考比较无差异。另有 112 项包装核验全部通过，避免把 Workflow/页面运行成功误当数据包装成功。

这一张真实图已能技术性地呈现工单提出的三种误读风险：

- 最近完成窗效率 `0.151417` 高于此前 `0.084543`，但当前 working 是下行方向，净推进 `50`、逆向量 `80`、效率仅 `0.037764`；历史完成统计不能直接写成当前走势。
- 最近窗端点幅度中位数 `138.5`，完整路径行程中位数 `750.5`；图中实线完整 close 路径和虚线端点连线明确分开，端点位移不能冒充波幅/行程。
- working 最近六个极值更新间隔为 `[600, 62400, 600, 18600, 600, 7800]`，以前3/近期3得 `600` 与 `7800`；这是局部节律，图和表没有把它提升为全程事实。

这些是技术观察证据，不是收益预测、资金意见、跨品种机会簇判断或专业/管理签收。

## 二、权威输入与实际版本

工单和完整专业报告均从 commit `82a55d2e22bafbdf3e628f2042b0734366314775` 逐字核对：

|对象|UTF-8 字节|SHA-256|
|---|---:|---|
|`professional-R0004/WORKER_ORDER.md`|17083|`3fd50ea0bc0d872b0f8eb4d153d82c8f5449f5408ed4c612f5c45a1266a65005`|
|`professional-R0004/FULL_RESPONSE.md`|36762|`cd1a11fb52e988e9a3b866c85b27eccc581e6919ccf871f543d93f5c98ba8a8d`|

本次实际导入/阅读版本：

|责任面|commit|实际处理|
|---|---|---|
|协调材料/完整配置|`a6f5025e8b082f8f11056e566a2a07abc49bb939`|独立固定 checkout，完整读取配置、Binding、R33、历史调用|
|TIS 正常读者|`3ff34c72be8ef025f68e18b097fe7b8f1f472668`|临时隔离 overlay 导入，未改共享 TIS|
|FRP 方法|`5154c407249c130a6e048c8541b76dfdec3ea48c`|固定 checkout，读取直接函数与边界|
|worker codec|`cd5c307dcb3483ef76242b5c37177a969c5fcbd2`|临时隔离 overlay 导入|
|aidata|`f58ea95c358b9ac31659c92b7bc20fe9bf7f8264`|原分支 `codex/aidata-named-csv-features-20261019`，clean；仅调用，未修改|

共享 `/dwdhome/fy/BASE_E6_2/mquant/tis` 与 worker 并不是工单固定版本，且有他人现场，因此没有覆盖它们。本次在 `/tmp/bi01-fo01-worker-runtime-20261022` 组合固定 TIS/worker 与 BASE 其余依赖；导入路径和产品目录均有实际证据。详细见 `evidence/PREFLIGHT_AND_VERSIONS.json` 和 `evidence/runtime_probe.json`。

目标仓库开始时为 `b0eb7f23634413edbff3fccaab9d9ea18518a0c2`；主控在 Worker 执行期间正常推进到 `bc4285bcb32777a351a2ebb0937005afb797624d`。本工作保留了这些提交，包装前本地/远端无 ahead/behind。

## 三、正常 OnlyRead 与准确 Case

### 3.1 N 读回

实际调用路径：

```text
完整 ACTUAL_RUN_CONFIGURATION.配置.source.sources
  -> U2NormalNodeBehaviorFrp.from_sources(..., compact_history=True)
  -> feature.rerun(CalType.OnlyRead)
  -> bindings 选择 rb node_life
  -> feature.read_session(life, as_of=103315800)
  -> session.to_dfs() 取得 24 表
```

产品目录实际等于：

```text
/m3varK/BaseData/futures/TA_updto20240229_DBA/fao/prod/U2NormalNodeBehaviorFrp/9/0/d/3/7/a/4/fb2007d71be1e620801457424d6dea8b4/func
```

实际 Exact：

```text
NodeBehaviorBook
NodeScaleTurnBehaviorRevision
b340dc6c-c135-462b-b6e0-04d24622c180
cfd51328-e2cf-4360-8314-20c9238e93fb
```

读回耗时 `297.163s`，进程峰值 RSS `4825452 KiB`。这只是本次请求进程峰值，不是生产常驻内存或产品大小。读者仍记录历史已知的三个泛型根缺件提示（一次 ThinReference、两次 ThinDefinition）；本次目标具名 24 表、业务非空表、空表和 Exact 均实际返回，未靠吞结果获得 exit 0。本单没有据此宣称公共 SDK 无缺陷。

### 3.2 地址与对象关系

本拍 `rows.window=37926`，命中 `windows.address=37926`；该窗口 `binding=1`，命中 rb Binding。`rows.working=37943`，命中 `working_bases.address=37943`；其 `binding=1` 与窗口一致。对象由实际 Binding 识别，不由 DataFrame 行号或当前 `record_id` 猜测。

两侧各六个完成成员、Life 无重合；working Life 为另一 Life，未混入完成样本。`specs.kind` 通过 `definition_life` 映射为：BusinessDuration、CanonicalPathLength、DirectionalProgress、PathEfficiency、RawAmplitude、RawCounterMove，没有按表内默认顺序给指标起名。

### 3.3 原价和 Calendar

实际调用：

```text
U2MainlineKLineInput(
  source=MapKLineOpenData(freq='5m'),
  calendar_grid=ResampleCalendarTsa(resample_len=600)
).rerun(CalType.OnlyRead)
```

读取范围为最早此前成员起点 `100460400` 至本拍 working through `103315800`，共 4760 行；自然标签从 `2023-11-14 22:50:00.500000` 到 `2024-02-29 14:55:00.500000`。实际来源 Life 为 `/m3varI/var/L1_data/tick/map_kline_data/5m/rb_night_end_at_2300`，revision 为 `TA_updto20240229_DBA`。端点全部准确命中，`calendar_position` 连续，OHLC/close/Calendar time 本范围无非有限值。

完整 close 用于有限参考算术；OHLC 只作背景。历史 bar 标签仍按“同 bar close，不是开盘瞬时已知”标注。

## 四、正式值、参考复算与解释边界

完成窗正式值：

|指标|单位|近期中位数|此前中位数|绝对差|近期未缩放 MAD|LOO 最大绝对移位|
|---|---|---:|---:|---:|---:|---:|
|BusinessDuration|CalendarUTITick|181800|234900|-53100|105900|61200|
|CanonicalPathLength|price|750.5|1273.5|-523|390.5|165.5|
|DirectionalProgress|price|138.5|128|10.5|42.5|2.5|
|PathEfficiency|ratio|0.1514170159|0.0845431993|0.0668738166|0.0259887677|0.0029454002|
|RawAmplitude|price|138.5|128|10.5|42.5|2.5|
|RawCounterMove|price|37|55.5|-18.5|13.5|2|

六项 LOO 的六个槽均实际导出；`loo_ties=63` 表示六槽并列，图表明确不把它画成六成员贡献/重要性排名。`change` 保持绝对差，不改写为百分比；`dispersion` 明确为未缩放 MAD，不称标准差。

working 正式状态为 completion `Pending`，但六个当前数值均 `present=1 / AvailableCommitted / Applicable`：

|字段|值|单位|
|---|---:|---|
|duration|256800|CalendarUTITick|
|directional progress|50|price|
|efficiency|0.03776435045|ratio|
|counter|80|price|
|waiting|123600|CalendarUTITick|
|waiting_ratio|15.84615384615|ratio|

`waiting_ratio` 未截到 `[0,1]`。节律的 local/full count 均为 15；本次保存的六间隔为 `600, 62400, 600, 18600, 600, 7800`，局部起点 `103059000`、最后更新 `103192200`。这些字段按各自 working 基础坐标取得。

`data/rb_projection/VERIFICATION.json` 保存 72 项逐项比较和全部关系检查；结果 `PASS`、零差异。参考值只用于观察核查，未冒充正式 Episode/N 产品。本次只证明这个 rb Case 和这些依赖，不复制 R33 的 910/1200/97 项，也不外推未来数据。

## 五、aidata 实际调用、页面和图文件

现有 aidata 能直接接入本次冻结投影，所以没有工具源码改动。实际链路为：

```text
build_chart_run(fixed_input)
  -> render_review_nodes(..., export_plot_view_data=True)
  -> Bokeh Document JSON 序列化
  -> standalone HTML
  -> Playwright Chromium 像素截图
  -> build_big_world_chart_pages
  -> 平台 URL 真实浏览器打开
```

三个节点：

|节点|用途|平台页面|
|---|---|---|
|`rb_long_12_plus_working`|此前6＋最近6＋working 的长范围导航|`http://192.168.11.40:6244/graph/cae/6124/report`|
|`rb_recent6_plus_working`|最近6＋working 的中范围|`http://192.168.11.40:6244/graph/cae/6125/report`|
|`rb_working_local`|最后完成边界与 working 的原 5m 局部|`http://192.168.11.40:6244/graph/cae/6126/report`|

三页均已由真实浏览器打开为 HTTP 200、各检测到 4 个 canvas，并保存平台截图。相同节点另有可恢复 standalone HTML、本地截图、working 数值表截图和节律表截图。AI 已实际看过长/中/局部、working/节律和平台截图；核验记录在 `VISUAL_INSPECTION.json`。

图中：

- 灰色为此前六个完成过程，蓝色为最近六个，红色为 working；working 没有进入两窗。
- 实线来自每段完整 5m close，虚线只连接端点；确认/known-from 用单独三角标记。
- 长图只作导航；中图和局部图保留原 5m 采样，概览没有参与路径算术。
- As-Of、品种、范围和图层含义均在页内；表格与图形共享同一真实 ColumnDataSource。

## 六、包装验收：没有用“运行成功”遮住缺件

验收被明确拆成以下事实，不能互相替代：

1. N 与 KLine 正常 OnlyRead 返回；
2. aidata `build_chart_run` 返回；
3. 三个 Bokeh Document 均可转为真实 wire JSON；
4. 每个节点的实际 ColumnDataSource 已导出；
5. standalone HTML 被浏览器打开并产生像素；
6. 平台 URL 被浏览器以 HTTP 200 打开并产生像素；
7. AI 实际看图；
8. 原 CSV 与 `plot_view_data` 中保留的原列逐值相等。

`PACKAGE_VERIFICATION.json` 共执行 112 项检查，全部通过。它逐一校验八份 source SHA、三个节点的 66 份视图导出、manifest 行数、原列逐值一致、`_aidata_source_sha256`、绘图坐标非空、working Pending/Available 并存、waiting_ratio 未截断，以及浏览器/视觉证据。

首次 standalone 截图尝试使用 snap Chromium 直接读取 `/dwdhome`，因 snap 文件权限返回 `ERR_FILE_NOT_FOUND`；随后改用已安装的 Playwright Chromium，并通过临时 localhost 只读服务打开同一 HTML，最终三页、六个 working/节律表截图全部通过。临时服务在写报告前已停止。这个恢复没有改数据或扩大系统权限。

## 七、普通排障和保留问题

本次遇到并已处理的普通技术问题：

- BASE 顶层最初缺固定 `m3sof`/TIS/worker 组合；改为固定 commit 隔离 overlay 后正常导入。
- KLine 首次已读完数据，但在退出 `CurrCalendar` 后才访问 `feature.full_dir`，触发 context 错误；把目录取值移回受控 context 后重跑通过，数据身份未改变。
- aidata 第一次像素捕获受 snap 路径隔离影响；按上节恢复，最终浏览器与平台均通过。
- 正常 N 读者的三个泛型根缺件提示仍保留；本次具名表实际可用，因此不擅改公共 SDK。

仍未完成/不在本次首轮范围：

- 没有继续画 hc、i 或 R33 的其他具名挑战点；工单允许先以实际可得的 rb 连贯位置交付，不要求等待三品种齐全。本次图不代表这些位置已核。
- 没有执行收益预测、资金管理、机会簇判断或完整 U2/U3；没有替专业 Pro 签观察结论。
- 没有把首版写入永久 `feature_configs`，也没有发布具名 CSV catalog；是否沉淀须由后续专业观察决定。
- 没有操作手机、调度主控或直接向 Pro 聊天发送。按授权只把回交发布到本 run，由主控送回原执行 Pro。

## 八、恢复入口和实物索引

核心可恢复入口：

|实物|路径|
|---|---|
|现场版本|`evidence/PREFLIGHT_AND_VERSIONS.json`|
|N 24 表及 manifest|`data/rb_asof_103315800/`|
|原价/Calendar|`data/rb_price_100460400_103315800/`|
|展示投影和 72 项核验|`data/rb_projection/`|
|aidata 固定输入和 chart manifest|`aidata_runs/bi01-fo01-n-aidata-rb-final-20261022/manifest/`|
|同源视图导出|`aidata_runs/bi01-fo01-n-aidata-rb-final-20261022/plot_view_data/`|
|HTML、截图、渲染/浏览器/视觉/包装证据|`aidata_runs/bi01-fo01-n-aidata-rb-final-20261022/render_evidence/`|
|可复跑脚本|`scripts/`|

主要命令（须保持固定运行时 `PYTHONPATH=/tmp/bi01-fo01-worker-runtime-20261022:/dwdhome/fy/BASE_E6_2`）：

```bash
/m3c3/Linux/apps/anaconda3/bin/python scripts/read_n_asof.py --configuration ACTUAL_RUN_CONFIGURATION.json --object rb --as-of 103315800 --output-dir data/rb_asof_103315800
/m3c3/Linux/apps/anaconda3/bin/python scripts/read_rb_kline.py --start 100460400 --end 103315800 --output-dir data/rb_price_100460400_103315800
/m3c3/Linux/apps/anaconda3/bin/python scripts/build_rb_projection.py --n-dir data/rb_asof_103315800 --price-dir data/rb_price_100460400_103315800 --output-dir data/rb_projection
/m3c3/Linux/apps/anaconda3/bin/python scripts/render_rb_aidata.py --projection-dir data/rb_projection --output-root aidata_runs --attempt-platform-pages
/m3c3/Linux/apps/anaconda3/bin/python scripts/capture_aidata_html.py --run-dir aidata_runs/bi01-fo01-n-aidata-rb-final-20261022
/m3c3/Linux/apps/anaconda3/bin/python scripts/verify_aidata_package.py --projection-dir data/rb_projection --run-dir aidata_runs/bi01-fo01-n-aidata-rb-final-20261022
```

最终 GitHub commit、远端分支 SHA、回读哈希写入 `GITHUB_RECEIPT.json`。该文件只在推送并从远端读回后生成；以它而不是本段预告为准。
