## 更新日志
## [e6.2.0.12] - 2025-09-23 - cyf
### Updated
- 图集基类 `BaseFigSet` 增加参数 `log_y`, 用来设置y轴是否使用对数坐标。具体说明见 `mquant/docs/cae/核心类详解/基础类.md`。并且对应调整 `fit_y_range.js` 脚本。

## [e6.2.0.11] - 2025-08-05 - cyf
### Updated
- 特征雷达 `ExtractEntityTimespans` `ExtractTimespans` 
  - 当 `startDay` `endDay` 时间范围内，一个所指定的特征的occurrence都不存在时，其 `timespans` 方法不再报错而是返回空列表，并提示用户在 `startDay` `endDay` 范围内没有occurrence.

## [e6.2.0.10] - 2025-08-04 - cyf
### Fixed
- 修复 `MultiScaleLayout` 中的中尺度图特征雷达的开始结束时间没有按照大尺度图的画图开始结束时间设置的问题。

## [e6.2.0.9] - 2025-07-24 - cyf
### Added
- 增加 `MultiScaleLayout` 多个尺度图表的布局配置类
  - 与岳总确认, 因为这个比较新, 所以新建了一个文件 `multiscale.py`(名字比较贴合业务) 来放

## [e6.2.0.8] - 2025-07-10
### Updated
- 图例中,增加如果板块名是"blk@"前缀,则去掉该前缀的逻辑,为了让图例尽可能短

## [e6.2.0.7] - 2025-05-27
### Added
- 增加`CAEGraph使用手册.md`，帮助更快的使用CAEGraph

## [e6.2.0.6] - 2025-05-21
### Added
- 取消`ExtractTimespans`中,n_inter参数需要大于n_margin参数的限制
  
## [e6.2.0.5] - 2025-05-21
### Added
- `TextPlot` 支持画文本信息
  
## [e6.2.0.4] - 2025-05-12
### Updated
- 将uplot/core/theme.py中`DefaultFigTheme`和`TBFigTheme` 背景网格线的透明度设置不起作用

## [e6.2.0.3] - 2025-05-07
### Updated
- 重构 `e6.2.0.2` 版 `MulFieldsGlyphs` 增加的功能
  - 去掉 `LiveUpdater` 中固定按扭的实现，而交给用户自行实现
  - 示例参考 `TestMidZigGraph`

## [e6.2.0.2] - 2025-05-06
### Updated
- `MulFieldsGlyphs` 增加参数 `live_event`
  - `BasePPChangeEvent` 子类,用于实现如中尺度参数切换触发改变小尺度图
  - 示例参考 `TestMidZigGraph`

## [e6.2.0.1] - 2025-04-30
### Updated
- `MulSegPlot` 支持在多品种情况下显示品种参数
  
## [e6.2.0.0] - 2025-04-30
### Updated
- `VBarPlot` 增加参数 `hover_tslabel`
- `MulSegPlot` 支持界面拖动修改参数

## [6.1.0.6] - 2025-03-17
### Updated
- `UTKLine` 增加参数 `NextProcess`
    - 对 `figure` 进一步加工，如绑定各种事件等
    - 基于用例 `大中小尺寸高频事件图`，点击中尺度图打开小尺寸图
    - 示例: `BigMidDenseUTGraphV2`, 更新 `mquant.worker`

## [6.1.0.5] - 2024-11-28
### Updated
- `MulFieldsPerSymPlot`  增加参数 `timefieldtype`,支持idx、ts、uti类型

## [6.1.0.4] - 2024-11-15
### Updated
- `KLinePlot` 增加参数 `NextProcess`
    - 对 `figure` 进一步加工，如绑定各种事件等
    - 基于用例 `大中小尺寸高频事件图`，点击中尺度图打开小尺寸图

## [6.1.0.3] - 2024-10-11
### Added
- "OneFieldPlot"增加size参数
  
## [6.1.0.2] - 2024-09-27
### Added
- 完善"CAEGraph"注释中,指定在多个图所画内容的功能的说明
  
## [6.1.0.1] - 2024-09-26
### Added
- 完善定义CAE图相关功能的注释

## [6.1.0.0] - 2024-08-15
### Fixed
- `KLinePlot` 的title名中加上sym属性

## [6.0.2.4] - 2024-04-26
### Updated
- `BasePlotter` 继承 `PlotterMixIn`,以便可以创建 `Plot` 节点

## [6.0.2.3] - 2024-03-29
### Updated
- 修改 `BasePlotter` `_finish_fig` 函数, 消除没有 `legend` 时的警告

## [6.0.2.2] - 2024-03-18
### Updated
- 支持在 `Notebook` 中拖动带拖动控件的 `CAEGraph`，而无需手动启动 `Bokeh server`
    - 见函数 `CAEGraph.bkapp` 说明

## [6.0.2.1] - 2024-02-25
### Fixed
- `StrasTradePlot`
  - traders参数类型从[]修改为符合fao框架的GMap()
  - legend_labels参数如果为None,则使用traders的key
  - 添加说明
  
## [6.0.2.0] - 2023-12-05
### Updated
- `OneFieldPlot` 增加调整函数`adjustfield`,可通过lambda函数调整原始值
### Added
- `MulPointPlot` 多个历史点的图
- `OneToGroupPointPlot` 多个历史点防重叠的分组分色图

## [6.0.1] - 2023-12-4
- `OneFeatMulFieldsPlot`指定要画的单个特征的多个字段及相关画图属性

## [6.0.0] - 2023-11-17
- `SeqPlotter`类改为使用白圣fao框架的写法

## [5.0.0.0] - 2023-10-31
### Updated
- `MainFig + OneFieldMulSymPlot` 支持联合动态标准化,其他形式不变
    - 注意: MainFig(dynstd_method只支持 ratio 和 ratio-back) + OneFieldMulSymPlot(这里不要设置 dynstd_method 参数，而是自动使用MainFig的 dynstd_method)
- 不再依赖 `cae.mfig` 库    
    - 将 `cae.mfig.utils` 迁移到 `mquant.uplot.core.utils` 中

## [0.0.1] - 2023-10-30
### Updated
- `CAEGraph`特征增加Context参数, 不需要在"with CurrTradeSet(sof):"下面运行特征
