# BI01-FO01-N-DISPLAY-INTEGRATION-02 Worker 技术回交

返回目标：`chatgpt:细节叙事生成_金标:BI01-FO01-执行`

order_id：`BI01-FO01-N-DISPLAY-INTEGRATION-02`

技术状态：`TECHNICAL_RETURN_READY`

业务状态：未由 Worker 判定；真实图、数据和时间差异须由原执行 Pro 继续解释。

## 一、结论先行

本单已完成 R0007 配置在真实 aidata/uplot 上的最小接入。实现没有修改 N 正式产品、TIS/FRP/core/SDK 或 uplot 源码，而是在 aidata 独立分支增加：R0007 `feature_configs/u2_normal_node_behavior.py`、正式多表到 `n_display/*` 的只读投影、显式 `OnlyRead/read_at_knowledge` 入口、`PerSymFigSet + MainFig/SubFig + KPriceLine` 消费者及定向测试。

实际运行保持完整 rb/hc/i 三来源、N=6、LOO minimum=3、5m、`night_end_at_2300`、`normalization=null`、`compact_history=true` 和原正式产品目录。一次正式演变读取取得 18 张本配置所需薄表；随后对 rb 实际发生自动选出三个知识切点，并逐个经过正常 `read_at_knowledge(node Life, K)`：

|切点|K|解析 exact|window / working|direction|
|---|---:|---|---|---|
|确认前真实发生|103150800|`6d4acb13-0d9b-48df-aced-4ec5e83f528a`|37912 / 37913|up|
|确认发生|103151400|`ef2f74f6-bdfe-4d89-bc78-4114de18e86c`|37926 / 37927|down|
|末拍|103315800|`cfd51328-e2cf-4360-8314-20c9238e93fb`|37926 / 37943|down|

成员实际结束 `103059000` 的前后正式发生为 `103058400 / 103059000`；确认 `103151400` 的前后为 `103150800 / 103151400`；末拍前一发生为 `103315200`。这些都来自本次 `origins.as_of`，没有以日期或固定步长猜前一拍。

已实际生成四页：一页 433 个真实发生的演变视图，以及确认前、确认时、末拍三个 selected-cut 视图。每页有价格、完成效率、working 推进/逆向量、working 前缀效率、时长、节律六个独立 y 面板。四页均由 Chromium 打开为 HTTP 200，每页实际有 6 个 Bokeh Plot、12 个 canvas 和六类 panel group；保存了 HTML、PNG、实际消费者 CSV 和 hash manifest。Worker 已逐张查看原始分辨率像素。

这次技术实证证明配置能表达而不倒填以下差异：确认前页面仍是 window 37912 / working 37913 / direction up；确认发生后才切到 window 37926 / working 37927 / direction down；末拍继续使用 window 37926，但 working 基础变为 37943。单切面只画当时合法标量点和成员几何，没有把末拍值补成连续历史。

补充技术线索也已保留：hc 最近 500 个实际发生中，正式可用 `waiting_ratio` 最大为 430（不截成概率，未作业务判断）；i 在具名缺价上下文内有 24 个连续 night 行的 nullable close，最后有效 close 是 2017-03-30 14:55 的 564.5，2017-03-31 09:00 恢复为 572.0，Calendar position 连续。恢复值保持普通观察输入，没有填零或标成新极值确认。

aidata 代码 commit 为 `db44a54fa30ff9b4b8dddbe37e020d087c914d62`，已推到 GitHub `daowei2026/aidata` 分支 `fy/bi01-fo01-n-display-r0007`。observe-iterate 技术包的最终 commit、远端 ref 和逐文件回读以 `GITHUB_RECEIPT.json` 为准。

## 二、权威原件与实际版本

本次先完整读取并核对正式原件：

|对象|UTF-8 字节|SHA-256|
|---|---:|---|
|`professional-R0007/WORKER_ORDER.md`|13135|`06c9ab52caf4d79111c3b7b8b52350cafd5ce98512ed62c5f3e8852650d562a3`|
|`professional-R0007/FULL_RESPONSE.md`|36758|`c0d4181ad2d34693d16b4592b92e4fea0d0117394cadb36c8ea13bc1cf715a29`|

同时完整读取当前任务/Binding `20426e5e…`、管理采用 `270b8eca…`、Owner 纠正 `ea0ace45…`、Owner GO `9508df…`、方法 `068fc87` 的 README/00/01/02/04 和未变的 `4d501afa` 03。本单没有恢复旧相反配置、旧静态三图或“每 Case 必看 PNG”的退出要求。

实际运行版本：

|责任面|版本/路径|处理|
|---|---|---|
|完整 R30 配置|`a6f5025e…`，SHA-256 `946d16ab1e6888de6f5da6f7197eac8a0633ef1bd9433ae0d37c620f075408ec`|完整三来源原件，未手抄 sources|
|TIS 修后读者|`3ff34c72be8ef025f68e18b097fe7b8f1f472668`|固定 overlay，只读|
|FRP 正常构造/方法|`5154c407249c130a6e048c8541b76dfdec3ea48c`|固定 checkout，只读|
|worker ADT|`cd5c307dcb3483ef76242b5c37177a969c5fcbd2`|固定 overlay，用于保存类型匹配|
|aidata 基线|`f58ea95c358b9ac31659c92b7bc20fe9bf7f8264`|独立工作树/分支改动；9ff 仅作参考|
|aidata 结果|`db44a54fa30ff9b4b8dddbe37e020d087c914d62`|GitHub 分支 `fy/bi01-fo01-n-display-r0007`|
|uplot 实际导入|`13badc6c079eebe7242abd65e56b328c45dcee2a`|共享 checkout 只读；Owner 0a4fcd 只作参考|

共享 uplot 在本单前已有 `pfw.py` 修改和两个未跟踪项；共享 TIS 也有既有 `STCalendar.py` 修改。本单原样保留，没有覆盖或提交它们。实际导入路径记录在 `evidence/RUNTIME_AND_RENDER_MANIFEST.json`。

正式 N 产品目录实际等于：

```text
/m3varK/BaseData/futures/TA_updto20240229_DBA/fao/prod/U2NormalNodeBehaviorFrp/9/0/d/3/7/a/4/fb2007d71be1e620801457424d6dea8b4/func
```

## 三、为什么需要这一个最小 aidata 接入

现场 f58 原生 N Feature 的实际结果是：`evidence_feature_configs(feature) == None`，也没有 `evidence_view_df`。generic fallback 会调用 `feature.rerun()` 的默认 Cache 语义；generic `EvidencePlotter` 总把图层画到 `ctx.figs[-1]`，并对图元调用价格动态标准化。这不能满足本单的显式 OnlyRead、N 多表地址关联、六个独立单位面板或 ratio/CalendarUTITick 禁止价格标准化。

因此最小改动不是再造绘图库或改 N 读者，而是：

1. 注册专业配置 v0.2.0，并保持其 PANELS/TIME_POLICY/VIEW_RULES 与原件语义相等；
2. 用正式 `rows.window -> windows -> binding`、`rows.working -> working_bases`、`binding + specs.kind` 做请求内只读投影；
3. 演变图只在相邻真实发生且同一基础、无缺件/失败时画保持；working 更新用水平保持加真实发生点的垂直变化，新 working/缺件/失败断线；
4. selected-cut 经正常 `read_at_knowledge` 取得当时合法正文，实际端点为圆点、确认点为菱形，K 后价格和几何不进入页面；
5. 使用真正的 uplot `PerSymFigSet`、一个 `MainFig` 和五个 `SubFig`；OHLC 经 `KPriceLine(std_method=None)`，各 N 面板不调用价格 DynStd；
6. 所有 rb 图元使用同一个稳定蓝色 `#4C78A8`，性质靠线型、形状和分图区分。

逻辑 `n_display/*` 只存在于显示投影，不被发布成 TIS 正式表或第二个 N 产品。CSV 是真实读回后的运输/核验实物，不是正常入口的替代。

## 四、真实发生、selected-cut 和数据关系

正式全量演变读取中主要表规模为：`rows=470887`、`windows=4154`、`metrics=24924`；bindings 为 rb/hc/i 三条。rb 本次导出的关键演变范围 `103056600..103315800` 有 433 个不同实际发生、3 个窗口基础、8 个 working 基础。

关键正式值显示变化发生在真实知识点：

|as_of|window|working|近期/此前效率|working 效率/推进/逆向量|exact|
|---:|---:|---:|---|---|---|
|103058400|37912|37913|0.143467 / 0.133543|0.714286 / 95 / 7|`2607d3e9…`|
|103059000|37912|37913|0.143467 / 0.133543|0.722628 / 99 / 7|`80bbcb6d…`|
|103150800|37912|37913|0.143467 / 0.133543|0.068581 / 43 / 66|`6d4acb13…`|
|103151400|37926|37927|0.151417 / 0.084543|0.107505 / 53 / 40|`ef2f74f6…`|
|103315800|37926|37943|0.151417 / 0.084543|0.037764 / 50 / 80|`cfd51328…`|

这些数值仅作为图层技术核对，不由 Worker升级为收益、机会或资金判断。`working_completion` 在三个 selected-cut 都保留正式 code 2；当前数值可用与 completion 状态并存，没有用 Pending 遮掉数值。

rb 同绑定价格经正常 `U2MainlineKLineInput.rerun(CalType.OnlyRead)` 取得，范围 `100443000..103315800`，共 4789 行。每个 selected-cut 的价格自动截到 K；三个页面所有 `x/x0/x1 <= K` 的包装检查通过。

i 缺价上下文另从同一正常主线入口读取 48 行。24 个 night bar 的 Calendar position 连续而 close 为合法空，恢复点为 UTI `35361000`；这区分了“缺值”“市场闭市造成的自然时间跳跃”和“读取失败”。详情见 `data/i_missing_context/I_MISSING_CONTEXT.json`。

## 五、页面、数据和实际像素

|页面|模式|用途|实际渲染|
|---|---|---|---|
|`rb_evolution_actual_occurrences`|evolution|真实发生的保持/改变/断线|6 plots / 12 canvas / 18 evidence renderers|
|`rb_selected_before_confirmation_K103150800`|selected_cut|确认前 as-known|6 plots / 12 canvas / 15 evidence renderers|
|`rb_selected_at_or_after_confirmation_K103151400`|selected_cut|确认发生 as-known|6 plots / 12 canvas / 15 evidence renderers|
|`rb_selected_final_K103315800`|selected_cut|末拍 as-known|6 plots / 12 canvas / 15 evidence renderers|

每页的 `plot_view_data/<page>/` 是渲染器实际消费的数据，包含 23 个逻辑视图文件、同绑定 OHLC 和逐文件 hash manifest。HTML 位于 `render_evidence/`，同名 PNG 是 Chromium 全页截图。

浏览器验收明确拆分为：HTTP 200、Bokeh Document、6 Plot、六类 group、canvas、截图文件。`BROWSER_CAPTURE.json` 四页全部 PASS。Worker 另用原始分辨率实际查看四张 PNG，确认页首 K/exact/口径、主图成员边界、实际/确认图例、六分图区分以及确认前后不同几何，记录在 `WORKER_VISUAL_INSPECTION.json`。这仍不等于执行 Pro 的专业看图或管理接受。

## 六、验证和失败恢复

最终检查：

- aidata 新测试与既有 evidence 合同测试共 `28 passed`；
- R0007 配置原件与实际落点的 CONFIG_VERSION、PANELS、TIME_POLICY、VIEW_RULES、23 个 configs 及两个 mode 的 `display_config` 全部语义相等；
- `FINAL_VERIFICATION.json` 共 19 项，19 PASS、0 FAIL；
- 四页 HTML/PNG/runtime validation、全部 plot_view_data hash 和三个 selected-cut 的 K 后几何检查均通过；
- i 缺价 24 行、恢复 UTI/close 得到固定核验。

没有用最终成功遮住中间问题：

1. 初次正式读回发现运行 overlay 的 worker 错指共享 checkout，导致 `MulWrap_U2ThinNodeRecord` 未注册；只调整 `/tmp` overlay 到固定 `cd5c307d…` 后恢复，未改受保护源码。
2. 正常读者仍打印三个已知旧可选布局缺文件提示；当前 18 表实际返回，和历史成功探针一致，提示未被吞成“全局无缺陷”。
3. 首次多品种索引为每个对象重复构建大缓存，已改为三个对象共享一次正式缓存；业务值和表未变。
4. 首次 layout 把实体路由键 `syms!rb` 误用作 PlotSet 的 BlockTarType；改成框架支持的 `["rb"]`。
5. KPriceLine 需要 Fao 参数，不接受普通 Python frame wrapper；改为请求内 display-only `BaseSymbolDFFao`，layout 完成即释放 frame 注册。
6. 浏览器普通 DOM `innerText` 看不到 Bokeh Shadow DOM badge；改为读取 Bokeh Div model，并仍以真实 canvas/截图验证。

失败后的渲染从已完成正常读回并带 hash 的 CSV 恢复，没有重新跑 N，也没有把 CSV 冒充原生入口。恢复边界写在 `RUNTIME_AND_RENDER_MANIFEST.json`。

## 七、提交、边界与剩余未完

aidata 原 origin 指向内网 Gogs；第一次 push 因代理 502 失败。随后只读确认 `daowei2026/aidata` GitHub 仓存在，直接将独立分支推到 GitHub并回读 ref；没有改共享默认 remote。最终提交：

```text
db44a54fa30ff9b4b8dddbe37e020d087c914d62
refs/heads/fy/bi01-fo01-n-display-r0007
```

本单未完成且不伪装完成的事项：

- hc 只做正式发生尾部技术切片，未制作 hc 专业观察页；i 只核具名缺价恢复，未制作 i 多面板页面；本单没有强制 Case 配额。
- 没有执行收益预测、真实市场研究、资金目标、机会簇或完整 U2/U3。
- 没有由 Worker 判断图所代表的业务认识、反例或参数是否应改；这些返回原执行 Pro。
- 没有操作手机、主控调度、TIS/FRP/core/SDK/uplot 源码或建立常驻服务。
- 没有创建平台永久 Host；交付的是可在 GitHub 下载的 standalone HTML/PNG/CSV 和可复跑脚本。

## 八、恢复入口

主要实物：

|实物|路径|
|---|---|
|正式 selected-cut 18 表|`data/selected_cuts/{before_confirmation,at_or_after_confirmation,final}/`|
|rb/hc/i 正式发生切片|`data/formal_occurrence_index/`|
|rb 同绑定价格|`data/same_bound_price/`|
|i 缺价恢复|`data/i_missing_context/`|
|四页实际消费者数据|`plot_view_data/<page>/`|
|HTML/PNG/浏览器/视觉证据|`render_evidence/`|
|运行与安全边界|`evidence/RUNTIME_AND_RENDER_MANIFEST.json`|
|19 项最终核验|`evidence/FINAL_VERIFICATION.json`|
|可复跑及失败恢复脚本|`scripts/`|

完整正式运行需固定：

```text
PYTHONPATH=/tmp/bi01-fo01-display-runtime-20261022:/dwdhome/fy/BASE_E6_2
TIS=3ff34c72...
worker=cd5c307d...
aidata branch=fy/bi01-fo01-n-display-r0007
```

`scripts/run_display_integration.py` 是完整读回/投影/渲染入口；`resume_render_from_exports.py` 只用于正式读回已经完成后的可审计渲染恢复；`capture_rendered_pages.py` 和 `verify_delivery.py` 分别执行浏览器及最终包装验收。
