# D｜CommonPriceTurnGroupCandidatesFrp CAEGraph 定义集成

## 0. 产物身份与阶段结论

| 项目 | 值 |
|---|---|
| `run_id` | `OI-U2-F-OBS-20261118-01` |
| `work_item_id` | `OI-U2-F-OBS-20261118-01-WI-D` |
| `stage_instance_id` | `OI-U2-F-OBS-20261118-01-M-D` |
| `delegation_id` | `D004` |
| 执行调用 | `C0010` |
| 定义编号 | `OI-U2-F-OBS-20261118-01-D-CAEGRAPH-V1` |
| 特征 | `CommonPriceTurnGroupCandidatesFrp`，即正式 `make_features(...)` 返回的第一项 `f` |
| 锁定 FRP | `daowei2026/frp@67711c492da909ed0f044f357beb278abf7fc71c` |
| 锁定 TIS | `daowei2026/tis@2f460d663d821cf2ba25555eda13e78b697d0767` |
| 锁定 CAEGraph | `daowei2026/uplot@0a4fcd54059782572a3f7e82fad041121e8c65ad` |
| D 阶段状态 | **完整** |
| Worker | 零 W |

本 D 已将外层真实实例构造、A 的事件／字段、B-POS-001 的 SOF／日历／对象／时间，以及 C2-CURRENT-V2 与 C3 的注入合同，集成为一份可以直接交 E 在锁定工作区尝试执行的完整 Python CAEGraph 定义。

本阶段没有运行最终图、没有读取真实 F 结果、没有生成 E HTML，也没有重跑 F producer。真实环境导入、既存正式产品读取、Bokeh 布局、HTML、PlotDataTree 和图中数据检查仍由 E 完成。

---

## 1. 单一集成动作的结果

完整定义：

`daowei2026/observe-iterate@f4f0e4b276b1118b779473c1fbe462bc7a64b358:longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/D/u2_f_caegraph_definition.py`

定义级检查：

`daowei2026/observe-iterate@37f81088985ff3f1d8c2e7fa409db7529586073f:longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/D/DEFINITION_CHECKS.json`

定义的正式输入链为：

```text
make_features(**FEATURE_PARAMS)[0]
+ A 的 occurrences / members / previous / Required / overlap / covered-by
+ B-POS-001
+ C2-CURRENT-V2
+ C3 prepare_display_tables 与 DisplayBindings
+ uplot@0a4fcd... 的正式导出、PlotSet、布局、PlotCtx 和 PlotDataTree
→ OI-U2-F-OBS-20261118-01-D-CAEGRAPH-V1
```

---

# 2. 上游兼容性核对

## 2.1 同一任务与版本

| 输入 | 当前有效引用 | D 核对结果 |
|---|---|---|
| A occurrence 理解 | `823b56a...:artifacts/A/FEATURE_OCCURRENCE_UNDERSTANDING.md` | 与 F@67711c、TIS@2f460d 一致；候选 revision 为主 occurrence |
| B 观察位置 | `6f1ee9e...:artifacts/B/OBSERVATION_POSITION_PREPARATION.md` | 普通默认位置；`B-POS-001` 可唯一绑定 |
| C 展示方式 | `bcb94cc...:artifacts/C/CAEGRAPH_DISPLAY_PREPARATION.md` | `C2-CURRENT-V2` 与 C3 注入合同一致 |
| C 当前 HTML | `56eef30...:artifacts/C/caegraph_display_preview.html` | 仅作 E 核图基准；不是 D/E 真实图 |
| C3 代码 | `508d494...:artifacts/C/caegraph_display.py` | 表准备逻辑复用；绘图接线按锁定源码作确定性修正 |
| 外层实例 | `tis@2f460d...:frp/fqv_kline_example.py` | 正式进入 `CurrSof/CurrCalendar` 后调用；只消费返回的 `f` |
| CAEGraph | `uplot@0a4fcd...` | 精确提交已核；不沿用旧示例猜 API |

## 2.2 业务边界保持

- 只观察 `f`；`make_features` 按正式构造返回 `f/q/v`，脚本只把 `f` 绑定为 `candidate_feature`，不读取或运行 Q/V。
- 不进入合理性分析。
- 不预接受历史观察成果。
- 不调用 `f.rerun(...)`；精确实例缺少 `fields.json` 时显式失败，不暗中执行全历史 F producer。
- D 不重新选择 B 位置，也不改变 C2 页面和业务阅读语义。

---

# 3. CAEGraph 仓库理解记录

## 3.1 仓库与版本

```text
daowei2026/uplot@0a4fcd54059782572a3f7e82fad041121e8c65ad
```

D 实际读取并沿调用链核实：

```text
CAEGraph使用手册.md
__init__.py
utlv2.py
utkv2.py
pfw.py
pdt.py
multiscale.py
app/plot.py
core/utils.py
```

### 路径事实

D004 引用中把若干源码写成 `uplot/__init__.py`、`uplot/utlv2.py` 等逻辑包路径；锁定 Git 仓库的真实文件位于仓库根目录：`__init__.py / utlv2.py / ...`。安装后的正式 Python 包导入面仍是：

```python
from mquant.uplot import ...
```

完整定义采用正式安装导入，不把 Git 仓库物理路径写成 Python import。

## 3.2 正式导出与本次采用类

锁定 `__init__.py` 正式导出：

```text
CAEGraph
PlotSet
BaseFigSet
BasePlotter
AllSymsFig
PerSymFigs
KPriceLine
PlotCtx
PlotDataFolder
PlotDataNode
DefaultFigTheme
```

D 的完整定义只从 `mquant.uplot` 导入这些公开对象；自定义 `StaticGlyphs`、`StaticSegments` 和说明区只继承公开基类，没有修改 uplot 仓库。

## 3.3 `CAEGraph / PlotSet` 配置链

真实调用链为：

```text
CAEGraph(Context=OptContext(SOF), plotsets=...)
  → CAEGraph.layout(...)
  → CurrWidgets / produce_widgets
  → CurrTradeSet(SOF)
  → PlotSet.plot(...)
  → CurrIndustry(blk) + CurrCalendar(calendar_name)
  → PlotCtx(start_time, end_time, symbols, calendar, SOF)
  → 各 BaseFigSet.plot_figs
  → 各 BasePlotter._plot_fig
```

本次绑定：

```text
Context.sof      = TA_updto20240229_DBA
PlotSet.blk      = [rb, hc, i]
calendar_name    = night_end_at_2300
timespans        = [(2021-01-01, 2022-12-31, B-POS-001)]
```

`PlotCtx` 使用 SOF 的 `natural_tsa` 将日期解析到当前日历 UTI；结束位置按源码增加一个 UTI 后形成半开 slice。D 不另造秒级边界，也不以自然日猜交易时段。

## 3.4 布局类

- `PerSymFigs`：在 `CurrSymbol` 上下文中为 `rb/hc/i` 各建一张独立原价图，符合 C2 不跨品种混合绝对价格的决定。
- `AllSymsFig`：只建一次候选 revision 面板和 Required 审计面板。
- `BaseFigSet`：首张真实图建立共享 `x_range`，后续面板复用；legend 使用 click-to-hide，hover 与 Y 范围由 finish 链处理。
- 本次 B 为普通默认位置，不使用 `MultiScaleLayout`；这不是能力缺失，而是 B 已判定多尺度路径不适用。

## 3.5 绘图类与数据合同

### 价格

```text
KPriceLine(feat=KLine(freq='5m'))
```

在每品种上下文中读取 5m KLine，按真实 `openUti/closeUti` 和 OHLC 绘制；不对 rb/hc/i 做显示标准化。

### 候选成员

D 使用 C3 准备出的只读表，并显式绑定：

```text
actual point           x=memberActual,       y=memberPrice
confirmation point     x=memberConfirmation, y=memberPrice
member-known point     x=memberKnownFrom,    y=memberPrice
actual→confirmation    segment
confirmation→known     segment
```

hover 保留 Candidate Life/Revision、Turn/Source exact、round、direction、type、member status 和各位置时间。

### 候选 revision

```text
x = groupKnownFrom
y = groupObservation 的显示类别位置
color = groupLocalBasis 显示编码
marker = groupObservation 显示编码
```

previous→revision 只在同一 Life 的 exact lookup 能唯一解析时画线。anchor/deadline/revisionEnd 为 Calendar-clock 原值，只进入 hover，不冒充 UTI。

### Required

每一候选 revision、每一坐标显示 C3 已接受的派生摘要：

```text
worst verdict
supports / unresolved / veto counts
```

pair 级 verdict、gap、veto 和 distance 保留在 hover；派生摘要不替代原 pair 事实。

## 3.6 Feature／实例进入路径

```text
CurrSof(TA_updto20240229_DBA, steel)
+ CurrCalendar(night_end_at_2300)
→ make_features(**锁定完整参数)
→ f = 返回第一项 CommonPriceTurnGroupCandidatesFrp
→ fields.json 既存性守卫
→ f.to_dfs([...])
→ C3.prepare_display_tables(f)
→ FrameFeature / PerSymbolFrameFeature
→ D 的 StaticGlyphs / StaticSegments
```

价格入口另为同一上下文中的 `KLine(freq='5m')`。Q/V 对象虽然由正式构造函数同时返回，但不进入任何读取、表准备或图元。

## 3.7 DataFrame 到 Bokeh CDS

- KLine 走锁定 `KPriceLine` 正式路径。
- 候选表先由 C3 将公开嵌套表整理为 revisions、members、links 和 Required summary。
- D 对每个当前 PlotCtx UTI 范围进行显式 mask，再构造 `ColumnDataSource`。
- 每个 CDS 都通过 `ctx.add_cds(...)` 进入 PlotDataTree。
- `ctx.uti2x` 与 `ctx.uti2tslabel` 负责 UTI 横坐标及时间 hover。

## 3.8 构图数据树与 E 取数

`CAEGraph.produce_widgets` 建立根 `PlotDataFolder`；每个 PlotCtx／FigSet 继续建立文件夹，每个 `ctx.add_cds` 形成 `PlotDataNode`。D 脚本在 E 运行时递归导出：

```text
PlotDataTree logical path
CDS columns
CDS rows
fetch / transform time
CSV path
```

因此 E 可以同时核对最终 HTML 和实际图中 CDS 数据，而不只看截图。

## 3.9 动态、控件、多尺度和输出路径

本定义：

- 不使用 `DynStd`；业务原价不做动态标准化；
- 不使用参数控件或 live server；
- 不使用 `MultiScaleLayout`；
- 使用 `CAEGraph.layout()` 形成静态 Bokeh layout；
- E 使用 `bokeh.embed.file_html(..., INLINE, ...)` 输出独立 HTML；
- 若后续另用 uplot app，锁定 `app/plot.py` 的 `components(plot.layout())` 是另一条 server 输出路径，但不是本次正式脚本路径。

---

# 4. 上游确定性纠正记录

## D-CORR-01｜C3 非单调 UTI 表的静态切片路径

| 字段 | 记录 |
|---|---|
| 来源阶段 | C3 |
| 原位置 | `508d494...:caegraph_display.py` 中自定义 Glyphs／Segments 调用 `ctx.feat_data(...)` |
| 问题 | `PlotCtx.feat_data` 对显式 UTI 字段走 `uti_slice`；成员 actual、confirmation、known 及 revision link 可能重复或非单调，不能假定满足该静态切片前提 |
| 能否由 D 确定性纠正 | 是 |
| 唯一依据 | A 的业务位置是多成员／多 revision 记录；锁定 `PlotCtx.live_feat_data` 对非单调字段也明确采用布尔范围筛选；C2 图元不要求排序改写 |
| 修正前 | 直接把完整 FrameFeature 交 `ctx.feat_data` |
| 修正后 | 在 D `StaticGlyphs/StaticSegments` 中按当前 `ctx.uti_slice` 显式筛选，再构造 CDS |
| 改变位置选择 | 否 |
| 改变 C2 预期／HTML | 否 |
| 新业务判断 | 否 |
| 处理结果 | D 直接纠正 |

## D-CORR-02｜成员 confirmation／member-known 端点图元漏接

| 字段 | 记录 |
|---|---|
| 来源阶段 | C3 |
| 原位置 | `508d494...:caegraph_display.py` 的 per-symbol price plots |
| 问题 | C2-CURRENT-V2 与当前 HTML 明确要求 actual、confirmation、member-known 三类位置分别可见；C3 已有两段位置线和 actual 点，但没有把 confirmation、member-known 端点各自作为点图元接入 |
| 能否由 D 确定性纠正 | 是 |
| 唯一依据 | C2 当前 HTML 和展示合同已经固定三位置形状；只存在把既定字段机械接到既定图元的修法 |
| 修正前 | actual 点 + 两段线 |
| 修正后 | 保留原内容，并增加 confirmation 三角点、member-known 菱形点 |
| 改变位置选择 | 否 |
| 改变 C2 预期／HTML | 否；使 C3 与已接受 HTML 对齐 |
| 新业务判断 | 否 |
| 处理结果 | D 直接纠正 |

## D-CORR-03｜锁定 uplot 源码物理路径

| 字段 | 记录 |
|---|---|
| 来源阶段 | D004 引用／仓库参考 |
| 原位置 | 若干引用写作 `uplot/__init__.py`、`uplot/utlv2.py` 等 |
| 问题 | 锁定 Git 树中这些文件实际位于仓库根目录 |
| 能否由 D 确定性纠正 | 是 |
| 唯一依据 | `uplot@0a4fcd...` Git tree 与 blob 路径 |
| 修正前 | 以 `uplot/` 为物理仓库子目录理解 |
| 修正后 | 源码引用使用根目录真实路径；运行导入仍使用正式 `mquant.uplot` |
| 改变位置／展示 | 否 |
| 新业务判断 | 否 |
| 处理结果 | D 直接纠正引用理解 |

## 4.4 明确保留而未“修掉”的边界

1. `raw_turn_view=None`：C 已把 raw ScaleTurn 定义为可选叠加。D 不为补图而重跑或重建被排除的上游 producer；候选成员证据仍完整显示。
2. `groupFormationParticipation`：Haskell 已存，但锁定 TIS `GROUP_TABLES` 未公开。D 保留页首告警，不猜 admission／correction 细节。
3. overlap／covered-by：当前公开的是目标 Life，没有唯一目标 revision/time policy；只进入 hover，不伪造连线。
4. 外层 `Tick.ts`：没有替代 `groupKnownFrom`。

---

# 5. 完整定义集成记录

| 字段 | D 的绑定 |
|---|---|
| C3 版本 | `508d494c964d5dabeaa1e7ea17bef908f749e9c8:artifacts/C/caegraph_display.py` |
| C2 当前版本 | `C2-CURRENT-V2` |
| C2 HTML | `56eef30b28c928255329f77798fb46b9adbbc71a:artifacts/C/caegraph_display_preview.html` |
| 预览实例 | C2 是合成数据；D 未把它当真实结果 |
| 正式实例 | `make_features(**FEATURE_PARAMS)[0]` |
| F 正式数据入口 | `f.to_dfs(...)`，只读取既存正式输出 |
| 价格入口 | `KLine(freq='5m')`，在 `PerSymFigs` 的品种上下文中读取 |
| SOF | `TA_updto20240229_DBA` |
| 业务 block | `steel`；用于 `CurrSof` 外层构造 |
| 实际绘图对象 | `rb / hc / i`；写入 `PlotSet.blk` |
| 日历 | `night_end_at_2300` |
| 时间 | `2021-01-01` 至 `2022-12-31`；进入 `PlotSet.timespans` |
| 多尺度 | 不适用；没有伪造父子路径 |
| 候选 occurrence x | `groupKnownFrom` |
| 成员位置 | `memberActual / memberConfirmation / memberKnownFrom` |
| 主要身份 | Candidate Life/Revision/Previous、Turn exact、Source exact |
| Required | 四坐标 verdict/gap/veto/distance，图上摘要、hover 原明细 |
| 是否改变展示语义 | 否 |

## 5.1 C3→D 代码差异

- 注入了真实 SOF、symbols、calendar、timespan 和完整 `make_features` 参数；
- 注入了正式 `f` 与真实 5m `KLine`；
- 加入 `fields.json` 只读守卫；
- 将非单调位置表改为显式区间 mask；
- 补齐 C2 已要求的 confirmation／member-known 点；
- 加入独立 HTML、prepared tables、PlotDataTree CDS 与 run report 的 E 输出；
- 保留 C3 `prepare_display_tables`、显示编码、面板结构和业务阅读路径。

---

# 6. E 可直接执行的合同

在 `/dwdhome/fy/BASE_E6_2_copy` 中使用本 Run 分支工作树，从 `observe-iterate` 仓库根目录执行：

```bash
python longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/D/u2_f_caegraph_definition.py \
  --output-dir longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/E/runtime/u2_f_caegraph
```

可先作只读表准备检查：

```bash
python longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/D/u2_f_caegraph_definition.py \
  --metadata-only \
  --output-dir longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/E/runtime/u2_f_caegraph
```

预期输出：

```text
artifacts/E/runtime/u2_f_caegraph/
├─ definition_run_report.json
├─ u2_f_caegraph.html                 # 非 metadata-only
├─ prepared_tables/
│  ├─ revisions.csv
│  ├─ revision_links.csv
│  ├─ members.csv
│  ├─ member_actual_confirmation.csv
│  ├─ member_confirmation_known.csv
│  ├─ required_summary.csv
│  └─ raw_turns.csv
└─ plot_data/                          # 非 metadata-only
   └─ *.csv                            # 各 PlotDataNode 的 CDS
```

失败策略：

- 精确 F 实例没有 `fields.json`：命名失败并停止；不调用 `f.rerun`。
- 公开表或字段不匹配：命名失败并记录 traceback；不猜字段。
- CAEGraph／Bokeh 运行失败：由 E 根据 run report 处理；D 定义不把失败包装成完成。

---

# 7. 定义级检查

完整机读结果见 `DEFINITION_CHECKS.json`。

| 检查 | 结果 | D 证据 | 是否需 E |
|---|---|---|---|
| Python 语法／编译 | 通过 | 完整脚本 definition-level parse/compile | 否 |
| 正式 uplot 导出 | 通过 | 与锁定 `__init__.py` 对齐 | 真实 import 仍需 E |
| 外层实例绑定 | 通过 | `CurrSof/CurrCalendar/make_features()[0]` | 数据存在性需 E |
| 禁止 F producer rerun | 通过 | 无直接 `f.rerun`；有 fields 守卫 | 守卫结果需 E |
| B 位置进入代码 | 通过 | constants + PlotSet | 日历解析需 E |
| A 字段进入图元 | 通过 | table preparation + glyph/hover binding | 实表列需 E |
| C2 页面／图元保持 | 通过 | 三类面板与三类成员位置 | 最终视觉核对需 E |
| 非单调位置处理 | 通过 | explicit range mask | 实数据需 E |
| PlotDataTree 取数 | 通过 | `plot_roots` + recursive export | 实 CDS 需 E |
| 真实平台运行 | D 未运行 | 阶段边界 | **E 必须完成** |

---

# 8. 只有 E 能确认的事项

1. `/dwdhome/fy/BASE_E6_2_copy` 中锁定的 `m3 / mquant / tis / uplot / bokeh` 是否能共同导入；
2. 精确 `f.full_dir/fields.json` 是否存在；
3. 2021～2022 范围内是否有候选 occurrence，以及空结果的真实含义；
4. TIS 当前实表索引层次、pair-distance join 和枚举名称是否与 C3 夹具一致；
5. `KLine(freq='5m')` 在每品种上下文中的实际读取与日历一致性；
6. Bokeh glyph、marker、hover、legend、共享 X 轴和静态 HTML 是否正常；
7. PlotDataTree 是否覆盖所有图元 CDS，导出数据与图是否一致；
8. 最终图与 C2-CURRENT-V2 HTML 的页面、信息和阅读路径是否一致；
9. `raw_turn_view=None` 对观察可读性的实际影响是否仍在 C 已接受边界内。

这些是 E 的运行验收，不是 D004 内未完成的定义工作。

---

# 9. 完成条件核对

| D Skill 完成条件 | 结果 |
|---|---|
| 按锁定仓库解释实际 CAEGraph 类、参数和数据链 | 已完成 |
| 正式绑定外层真实 `f`，未把 C 预览当真实实例 | 已完成 |
| B 位置与 A 字段进入可执行代码 | 已完成 |
| C2 展示预期未无痕改变 | 已完成 |
| 确定性纠正满足唯一、不改业务选择并留痕 | 已完成，共三条 |
| 拿不准的问题未在 D 猜测 | 已完成；真实接口缺口保留 |
| 形成可直接交 E 尝试运行的完整定义 | 已完成 |
| 定义级检查与 E 运行验证分开 | 已完成 |
| D 不派 Worker、不运行最终图 | 已遵守 |

**D 阶段最终状态：完整。**

D004 内不存在仍未满足的专业工作，不需要续接同一 D。父 Run 仍未完成；原 manager 应消费本 D 回交后，按既定 Workflow 推进 E 的真实运行、取图、取数和一致性核对。
