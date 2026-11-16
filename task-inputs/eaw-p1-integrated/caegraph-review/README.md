# CAEGraph 完整脚本与独立数据包

将 `caegraph-scripts.zip` 和 `caegraph-data-30tick.zip` 解压到同一目录。
两个压缩包合并为以下结构；均不含 HTML 文件：

```text
caegraph-review/
  caegraph_definitions.py
  snapshot_data.py
  run.py
  README.md
  data/
    manifest.json
    timespans.csv
    included_tick_nodes.csv
    calendar.npz
    frame_*.csv.gz
    window_*.csv.gz
```

在已有 mquant 依赖的 Python 环境中运行：

```bash
cd caegraph-review
python run.py
```

脚本启动本地 Bokeh 页面，下拉框可选择长期概览、6个大中小尺度组合页和30个 Tick 窗口；
按需绘制当前选中的图，不生成 HTML 文件。用 Ctrl+C 停止。

```bash
python run.py --list
python run.py --chart tick --node-id tick_000030
python run.py --check
```

数据目录也可单独放置：`python run.py --data-dir /解压位置/data`。
运行库依赖为 mquant/uplot/frame/quant、m3tt、Bokeh、pandas、numpy；
这些库的源码没有携带。脚本不导入 Aidata，不读取原 run、原行情或原特征存储，
也不运行旧 example 或重算上游特征。沿用当前已安装的 mquant/Bokeh 兼容环境。

## 数据范围与图的数量

| 层级 | 数据中可绘制的窗口数 |
|---|---:|
| 长期概览（日线） | 1 |
| 大尺度（30min） | 6 |
| 中尺度（1min） | 18 |
| 小尺度（5s） | 54 |
| Tick | 30 |

每个组合页包含1个30min窗口、3个1min窗口及9个5s窗口。
中尺度是1min，当前没有5min定义。
每个 Tick 窗口包含 rb、hc、i 三个品种，以及1张主图和3张附图；
这里按一个窗口为一组图计数。

Tick 按节点编号选取 `tick_000001` 至 `tick_000030`：前24个属于 `big_000001`，
后6个属于 `big_000002`。精确父节点、时间和品种见 `data/included_tick_nodes.csv`。
`timespans.csv` 保留原始全部148个 Tick 节点，用于复现5s图上的定位框；
其余118个只有时间窗，没有随包行情，入口不会将它们列为可打开的 Tick 图。

数据按原始图窗从已落盘结果读取：K线保留归一化前价量，事件保留原始字段与绘图绑定，
Tick 保留买卖一价量、成交量、持仓和主买主卖等当前绘图字段。
日历以连续半秒段无损压缩，原生 uplot 运行时展开，不依赖原日历目录。
墙生命周期的区间按各图窗分别保存，保留该窗口原本可见的结束边界。

## 实际图定义的位置

全部图定义和必需辅助代码都在 `caegraph_definitions.py`，没有藏在 Aidata 模块里：

- 概览：`OverviewCAE`、`_register_run_overview_graph`。
- 大中小尺度：`MultiscaleCAE`、`_register_big_graph`、`_register_mid_graph`、`_register_small_graph`。
- Tick：`build_tick_caegraph`，使用原生 `AllSymsMainFig`、`AllSymsFig`、`VBarPlot`、`MulFieldsGlyphs`。
- `snapshot_data.py` 只负责把独立数据交给已有绘图库。

嵌入其他程序时：

```python
from caegraph_definitions import build_overview, build_multiscale, build_tick

overview = build_overview()
multiscale = build_multiscale(node_id='big_000002')
tick = build_tick(node_id='tick_000030')
# 以上对象均保留 layout.plot_roots，可交给既有 CAEGraph 数据导出工具。
```

如果数据不与脚本同目录，传入 `root='/包含data子目录的目录'`。
