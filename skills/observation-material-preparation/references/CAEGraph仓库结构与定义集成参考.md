# CAEGraph 仓库结构与定义集成参考

> **用途**：供 D｜CAEGraph 定义集成使用。D 不能只凭速查或旧示例猜 API；必须理解锁定版本 CAEGraph 仓库中，与本次完整定义实际相关的导出、配置、布局、绘图、数据、动态处理和运行链。
>
> **当前锁定来源**：`daowei2026/uplot@e6.2`。若任务锁定其他版本，必须重新核对相同调用链，不能直接沿用本参考中的实现事实。

## 1. “完全理解仓库”在 D 中的可执行含义

本要求不是把所有无关代码逐行抄进报告，而是要求 D 对本次定义涉及的真实调用链没有黑箱猜测：

```text
mquant.uplot 对外导出
→ CAEGraph / PlotSet 配置
→ 图表布局类
→ 绘图类及 feat 参数
→ PlotCtx 的时间、对象和数据截取
→ Feature / DataFrame 到 Bokeh CDS
→ PlotDataFolder / PlotDataNode 数据树
→ 动态标准化、控件及前端回调
→ layout / produce_widgets / server 或 HTML 输出
```

D 使用的每个类、参数、字段入口和运行假设，都应能回到对应源码或手册，而不是只因某个旧脚本曾经这样写。

## 2. 仓库文件地图

| 文件／目录 | 与 D 集成相关的职责 |
|---|---|
| `__init__.py` | `mquant.uplot` 的正式导出面；确认本次代码可以从哪里导入 `CAEGraph`、`PlotSet`、布局类、绘图类、`PlotCtx`、`PlotDataFolder` 等 |
| `CAEGraph使用手册.md` | 使用术语、构建链、布局类／绘图类选择和典型示例；用于理解公开用法，但不能替代源码核实 |
| `utlv2.py` | `CAEGraph`、`PlotSet`、主要绘图类和特征雷达；绘图类通过 `feat`、`df_key`、时间字段和数值字段进入 `PlotCtx` 数据读取／转换链 |
| `utkv2.py` | `BaseFigSet`、`MainFig`、`SubFig`、`AllSymsMainFig`、`PerSymFigs`、`PerSymFigSet` 等布局组织 |
| `pfw.py` | `PlotCtx`、`BasePlotter`、`CurrWidgets`、`DynStd`；处理对象／时间范围、Feature 数据截取、CDS、hover、动态标准化和控件上下文 |
| `pdt.py` | `PlotDataFolder`、`PlotDataNode`；记录构图阶段数据树和实际 `ColumnDataSource`，是 E 后续取图数据的重要入口 |
| `multiscale.py` | uplot 自带的多尺度布局能力；若本次定义使用，必须核实其真实接口，不能与具体用例脚本的 1d→30m→1m→5s→tick 位置树混为同一概念 |
| `core/` | 主题、事件和通用工具；本次使用到具体工具时再沿导出追入 |
| `dynstd.js` | 浏览器端动态标准化；构图时 CDS 与前端视窗最终值可能不同 |
| `fit_y_range.js` | 视窗变化后的纵轴适配；使用时需要区分 Python 构图结果和浏览器最终显示状态 |
| `app/` | Bokeh 应用／服务入口；本次若通过 server 运行或导出，需要核实对应入口 |
| `CHANGELOG.md` | 版本差异线索；不能用旧版示例替代锁定版本事实 |

## 3. 与特征实例绑定直接相关的事实

`uplot@e6.2` 中，绘图类普遍把业务 Feature 作为参数，例如：

```python
SegsPlot.params()['feat']
VBarPlot.params()['feat']
KPriceLine(feat=...)
MulFieldsGlyphs(...)
```

绘图器随后经 `PlotCtx.feat_data(...)`、`PlotCtx.live_feat_data(...)` 或相邻接口取得并转换 Feature 数据，再形成 Bokeh `ColumnDataSource`。

因此，实际特征实例是完整 CAEGraph 定义中的真实运行绑定，不只是展示样式的一部分。为保持 C／D 边界：

```text
C：定义 feat／数据入口的注入接口，可临时用实例做预览
D：把外层真实特征实例和正式数据入口注入该接口
```

若 C 的预期 HTML 临时使用了外层实例，D 仍须核对它只是可替换预览绑定，不能因为“已经跑过样例”而跳过正式实例绑定。

## 4. 与真实位置绑定直接相关的事实

`PlotCtx` 负责把 `start_time / end_time` 转换为当前日历的 UTI 范围，并在给定 SOF、calendar、symbols／blk 下组织绘图上下文。`PlotSet`／`CAEGraph` 又负责把：

```text
calendar_name
blk / symbols
timespans
figs
```

组合成页面。

所以 B 的品种、时间和高频多尺度位置，在 D 中应进入真实上下文、`PlotSet.timespans` 或相应多尺度配置；不能只写在注释或 HTML 标题中。

## 5. 与字段和图数据绑定直接相关的事实

`PlotCtx` 会把 Feature DataFrame 的字段转换为实际 CDS 列。`PlotDataFolder / PlotDataNode` 保存构图数据树，每个叶节点持有实际 `cds.data`。

D 因此必须核实：

- C 图元的横轴字段是否对应 A 的真实事件位置；
- 纵轴和 hover 字段是否真实存在；
- 同一 occurrence 的身份字段是否在多个图元间保留；
- 显示派生列是否与业务原值分开；
- 动态标准化前后列、构图 CDS 与浏览器最终显示值不能混同。

## 6. D 的阅读顺序

D 开始集成前，至少执行以下阅读顺序：

1. 读取锁定版本 `__init__.py`，确认正式导出；
2. 读取手册中本次涉及的构建链、布局类和绘图类；
3. 读取 C 代码中实际使用类的源码定义；
4. 沿这些类追到 `PlotCtx`、Feature 数据读取和 CDS 形成路径；
5. 若使用动态标准化、控件、多尺度或 server，继续读取对应 Python／JS／app 源码；
6. 核对 `pdt.py` 中构图数据树，以便完整定义能被 E 后续核图和取数；
7. 记录仍未核实的版本／运行假设，不能用“CAEGraph 应该支持”替代证据。

## 7. D 必须产出的仓库理解记录

每次 D 至少记录：

```text
锁定的 uplot 仓库和 commit／ref
实际读取的文件和类
C 代码使用的类从哪里导出
特征实例怎样进入绘图器
品种、时间和日历怎样进入 PlotCtx／PlotSet
真实字段怎样形成 CDS
是否使用动态标准化、控件、多尺度或 server
最终 HTML 与后续图数据可以从哪里取得
尚未确认、只能由 E 运行验证的事项
```

只有当这些内容能够解释当前完整定义时，才可称 D 已经理解了本次所需的 CAEGraph 仓库内容。
