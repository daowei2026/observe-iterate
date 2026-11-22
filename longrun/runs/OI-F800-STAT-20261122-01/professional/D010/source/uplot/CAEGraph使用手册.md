# CAEGraph相关使用手册

----------------------------------------------------------------------
## 文档说明

**如何使用本文档 (快速实现绘图需求)**

本文档旨在帮助快速、高效地使用 `CAEGraph` 相关工具包（基于 `uplot`）来绘制符合需求的时间序列图表。

**当有一个具体的绘图想法时，可以尝试以下步骤来使用本文档：**

1.  **明确核心需求与图表类型：**
    *   **我想要画什么？** 是K线图、成交量柱状图、标记一些特殊事件点，还是组合多种图表？
    *   **可以先浏览"使用示例"章节**：这里提供了多种场景下的完整绘图代码。您或许能直接找到与您需求相似的例子，通过修改参数快速实现。
    *   **参考"名词定义"中的图表类别描述**：快速了解不同图表组件（如"绘图类"、"图表布局类"）能实现的效果。

2.  **如果想从头构建或深入定制图表：**
    *   **理解图表构建流程**：请先阅读"核心类详解"章节开头的**链路说明**。它将告诉图表是如何从顶层的"图表集成类"一步步到具体的"绘图类"和"基础组件"构建起来的。
    *   **选择合适的"图表布局类"**：查阅"核心类详解" -> "图表布局类"部分，特别是其中的"**图表布局类选择指南**"。根据想绘制"多品种同列"、"每品种独立出图"还是"单品种主副图"等需求选择合适的布局容器。
    *   **选择具体的"绘图类"**：接着，在"核心类详解" -> "绘图类"部分，参考开头的"**绘图类快速选择指南**"。根据要展示的数据类型（如K线、Tick线、事件点、自定义线段等）选择一个或多个绘图工具。
    *   **配置核心参数**：在确定了布局和绘图类后，仔细阅读对应类的"参数配置"和"使用示例"，了解如何传入数据、调整样式等。
    *   **数据准备与"特征雷达"**：如果图表需要展示特定条件下筛选出的时间段或数据点，可以了解"核心类详解" -> "特征雷达"部分，学习如何使用 `ExtractTimespans` 或 `PerDPTimespans` 来预处理数据。
    *   **添加交互与调整主题**：如果需要动态调整参数或更改图表风格，可以分别查阅"组件类"和"主题系统"部分。

3.  **快速查找与参考：**
    *   **利用文档顶部的"目录"**：直接跳转到感兴趣的类或章节。
    *   **理解整体结构**：当对多个类的协作方式有疑问时，可以查阅"类之间的关系"图。

**阅读建议：**
*   **动手实践**：最高效的学习方式是结合"使用示例"中的代码，动手修改参数并观察图表变化。
*   **理解术语**："名词定义"是理解本文档的基础，请确保对核心术语有清晰的认识。

----------------------------------------------------------------------
## 目录

- [CAEGraph相关使用手册](#caegraph相关使用手册)
  - [文档说明](#文档说明)
  - [目录](#目录)
  - [名词定义](#名词定义)
  - [使用示例](#使用示例)
    - [观察多个品种的大单买卖和密集分析的用例](#观察多个品种的大单买卖和密集分析的用例)
    - [利用控件观察多参数的大单买卖和密集分析的用例](#利用控件观察多参数的大单买卖和密集分析的用例)
      - [交互控件使用提示](#交互控件使用提示)
    - [更多用例见：worker/example/cae](#更多用例见workerexamplecae)
  - [核心类详解](#核心类详解)
    - [图表集成类](#图表集成类)
      - [CAEGraph](#caegraph)
      - [PlotSet](#plotset)
    - [图表布局类](#图表布局类)
      - [**图表布局类快速选择指南**:](#图表布局类快速选择指南)
      - [AllSymsMainFig](#allsymsmainfig)
      - [AllSymsFig](#allsymsfig)
      - [PerSymFigs](#persymfigs)
      - [PerSymFigSet](#persymfigset)
      - [MainFig](#mainfig)
      - [SubFig](#subfig)
      - [OneFig](#onefig)
    - [绘图类](#绘图类)
      - [**绘图类快速选择指南**](#绘图类快速选择指南)
      - [KPriceLine](#kpriceline)
      - [TickPriceLine](#tickpriceline)
      - [VBarPlot](#vbarplot)
      - [MulFieldsGlyphs](#mulfieldsglyphs)
      - [MulSegPlot](#mulsegplot)
      - [StrasTradePlot](#strastradeplot)
      - [SegsPlot](#segsplot)
      - [TextPlot](#textplot)
      - [MulPointPlot](#mulpointplot)
      - [OneToGroupPointPlot](#onetogrouppointplot)
      - [SeqOfFieldsPlot](#seqoffieldsplot)
    - [特征雷达](#特征雷达)
      - [ExtractTimespans](#extracttimespans)
      - [PerDPTimespans](#perdptimespans)
    - [组件类](#组件类)
      - [FigCtrls](#figctrls)
      - [BasePPChangeWidget](#baseppchangewidget)
    - [主题系统](#主题系统)
    - [DefaultFigTheme](#defaultfigtheme)
    - [TBFigTheme](#tbfigtheme)
    - [基础组件](#基础组件)
      - [PlotCtx (用户通常不会直接使用)](#plotctx-用户通常不会直接使用)
      - [BaseFigSet(用户通常不会直接使用)](#basefigset用户通常不会直接使用)
      - [BasePlotter(用户通常不会直接使用)](#baseplotter用户通常不会直接使用)
  - [类之间的关系](#类之间的关系)

----------------------------------------------------------------------
## 名词定义

| 名词 | 解释 |
| :--- | :--- |
| **基础组件** | 提供图表绘制的核心功能和数据处理机制的基础类，包括PlotCtx(上下文数据转换器)、BaseFigSet(图集基类)和BasePlotter(绘图器基类)，它们构成了整个绘图系统的底层架构，用户不用重点了解。 |
| **绘图类** | 继承自BasePlotter的专用绘图工具集，每种类型专注于特定数据可视化需求，如K线图、线段图、柱状图、散点图等，使用户能直观展示不同类型的金融数据和指标。 |
| **图表布局类** | 继承自BaseFigSet的容器类集合，负责组织和排列各种图表，定义它们的位置关系和整体布局，包括单图、主副图、多品种图等不同展示方式。 |
| **特征雷达** | 用于提取数据中满足特定约束条件时间段的类似于"雷达"一样的高级工具，帮助用户高效的识别特征关系。目前有ExtractTimespans和PerDPTimespans两种。 |
| **组件类** | 为基础绘图系统提供扩展功能的辅助类组件，主要包括FigCtrls(提供动态参数调整的交互控件)和BasePPChangeWidget(用于创建参数范围改变的自定义组件)。这些类通过增强用户交互能力和动态参数调整功能，使绘图系统更具灵活性和响应性，支持用户在不重新生成图表的情况下实时调整数据视图。 |
| **图表集成类** | 负责整合所有图表组件的顶层类，是连接"绘图类"、"图表布局类"和"组件类"的最终环节。PlotSet负责将多个图表组织成有意义的集合，而CAEGraph则进一步将这些集合整合为完整的可视化应用。这些类充当系统的"总指挥"，协调不同级别的图表元素协同工作，为用户提供从单一图表到完整分析界面的无缝过渡。 |
| **主题系统** | 控制图表整体视觉风格的样式管理系统，包括DefaultFigTheme和TBFigTheme等主题，定义背景色、网格线、十字光标和K线样式等元素，使绘图风格统一且可定制。不用重点了解。 |

----------------------------------------------------------------------
## 使用示例

--------------------------------------------------
### 观察多个品种的大单买卖和密集分析的用例

```python
class MultiSymHFCAE(BaseCAEFao): # 定义一个多品种高频事件分析的CAE图表类
    """
    Author  : zx
    Since     : 2024-09-24 17:54
    Desc      : 观察多个品种的大单买卖和密集分析
    Params :
      blk: 品种列表
      priceline: 价格线  
                 tick线:TickPriceLine( feat=OriginalIndexData())
                 K线:KPriceLine(feat=KLine(freq="30m"), std_method = 'ratio',)
      calendar_name: 日历类型
      hd_feat: 大单特征
      thickfrp_dense: dense特征   
      thickfrp_fight: fight特征
      max_spans: 最多返回的段数（超过的丢弃）
    """
    params = lambda : { # 定义图表的可配置参数
        "blk": ["rb","j","i"], # 品种列表：螺纹钢、焦炭、铁矿石
        "priceline": TickPriceLine( feat=OriginalIndexData({'isOriginal': False}),std_method = 'ratio',), # 价格线类型：使用Tick线，基于原始指数数据，并进行比例标准化
        "calendar_name": "night_end_at_2300", # 交易日历：夜盘到23:00结束
        "hd_feat": HugeDealUTL("basic"), # 大单特征：使用基础版大单参数
        "thickfrp_dense": ThickFrp("basic_Dense"), # Dense特征：使用基础版高频Dense特征参数
        "thickfrp_fight": ThickFrp("basic_Fight"), # Fight特征：使用基础版高频Fight特征参数
        "max_spans": 1, # 特征雷达最大返回时间段数量
        "timespans": [("2023-02-19","2023-07-19")], # 默认分析的时间段
    }
   
    def _impl(self): # 图表实现的核心逻辑
        # 初始化配置
        # 创建特征实例，从参数中获取
        hd_feat = self.P.hd_feat # 大单特征实例
        thickfrp_dense = self.P.thickfrp_dense # Dense特征实例
        thickfrp_fight = self.P.thickfrp_fight # Fight特征实例
        timespans=self.P.timespans # 用户指定的时间段
        
        # 定义特征雷达，用于自动提取关注的时间段
        timespans_fao = ExtractTimespans("MidScale")({ # 中等尺度的时间段提取器
            'feats': GMapX.from_list([HugeDealUTL("basic"), HugeDealUTL("basic")]), # 基于大单买卖事件进行时间段提取
            'dffilters': [lambda df: df], # 不对大单数据进行额外过滤
            'dfkeys': ['hd_buy','hd_sell'], # 大单买入和卖出数据表名
            'utifields': [['uti'],['uti']], # 大单数据中的时间字段名
            'symbollist':  self.P.blk, # 要分析的品种列表
            'startDay': '2023-01-01', # 特征雷达扫描的开始日期
            'endDay': '2024-01-28', # 特征雷达扫描的结束日期
            'max_spans': self.P.max_spans, # 最多返回的时间段数量
        })
  
        # 配置绘图元素
        # 配置高频特征的绘图方式 (MulFieldsGlyphs)
        MulFieldsGlyphs["ThickFrp_basic"] = lambda: { # 定义一个名为 "ThickFrp_basic" 的多字段绘图配置
                "feats":GMapX({  # 特征映射，将不同特征映射到绘图元素
                    "dense_buy": thickfrp_dense, # dense买入信号
                    "dense_sell": thickfrp_dense, # dense卖出信号
                    "fight": thickfrp_fight # fight信号
                          }),
                'legend_labels': ['denseutl_buy', 'denseutl_sell','fightutl'],  # 图例标签
                "yfields": [ "deci_price2", "deci_price2","deci_price2", ], # Y轴数据字段（价格）
                'size_fields': [ 'dense_buy_strength', 'dense_sell_strength',"fight_strength"], # 点大小的数据字段（强度）
                'size_scale': 15, # 点大小的缩放系数
                'dynstd_method': 'ratio', # Y轴动态标准化方法：比例标准化
        }

        # 配置买盘大单的柱状图 (VBarPlot)
        VBarPlot["buy_alias"] = lambda: { # 定义一个名为 "buy_alias" 的柱状图配置
            "feat": hd_feat, # 使用的大单特征实例
            "df_key": "hd_buy", # 数据来源表名：大单买入
            "color": "green", # 柱子颜色：绿色
            "label": "买盘大单" # 图例标签
        }

        # 配置卖盘大单的柱状图 (VBarPlot)
        VBarPlot["sell_alias"] = lambda: { # 定义一个名为 "sell_alias" 的柱状图配置
            "feat": hd_feat, # 使用的大单特征实例
            "df_key": "hd_sell", # 数据来源表名：大单卖出
            "color": "red", # 柱子颜色：红色
            "top_coeff": -1, # 柱顶系数设为-1，使柱子向下绘制
            "label": "卖盘大单" # 图例标签
        }

        # 构建图形 (CAEGraph)
        graph = CAEGraph({ # 创建CAEGraph实例
            "Context": OptContext("TA_updto20240229_DBA"), # 数据上下文配置，指定数据源和时间范围
            "plotsets": GMap({ # 绘图集配置
                '高频事件和大单观察': PlotSet({ # 定义一个名为 "高频事件和大单观察" 的绘图集
                    "calendar_name": self.P.calendar_name, # 交易日历
                    "timespans": timespans, # 优先使用用户指定的时间段
                    "timespans_fao": timespans_fao, # 如果用户未指定，则使用特征雷达提取的时间段
                    "blk": self.P.blk, # 品种列表
                    "figs": GMapX.from_list([ # 图表布局配置
                        AllSymsMainFig( # 所有品种在同一个主图上显示
                            persym_plots=GMapX.from_list([ # 每个品种绘制的内容
                                self.P.priceline, # 价格线 (Tick线)
                                MulFieldsGlyphs("ThickFrp_basic") # 高频特征点图
                            ])
                        ),
                        PerSymFigs( # 每个品种单独一个附图
                            plots=GMapX.from_list([ # 每个品种的附图内容
                                VBarPlot("buy_alias"), # 买盘大单柱状图
                                VBarPlot("sell_alias"),  # 卖盘大单柱状图
                            ]),
                             fig_height=150, # 附图高度
                        )
                    ])
                })
            }),   
            "theme": DefaultFigTheme(), # 图表主题：使用默认主题
            "x_label_freq": "1m", # X轴时间标签频率：1分钟
            "extra_time": 0, # 图表两端额外显示的时间：0
            "fig_width": 1200, # 图表总宽度
            "fig_height1": 500, # 主图高度
            "fig_height": 200, # 附图高度 
            "colors2": None, # 备用颜色板
            "switches": {} # 自定义开关
        })
        return dict(value=graph) # 返回构建好的图表对象
# 显示图表
graph=MultiSymHFCAE().run().value # 实例化并运行图表类，获取图表对象
show(graph.layout()) # 在Jupyter Notebook中显示图表布局
```

--------------------------------------------------
### 利用控件观察多参数的大单买卖和密集分析的用例

```python
class MultiSymHFCAE_LIVE(BaseCAEFao): # 定义一个支持动态参数调整的多品种高频分析CAE图表类
    """
    Author  : zx
    Since     : 2024-09-24 17:54
    Desc      : 观察多个品种的大单买卖和密集分析 (支持动态参数调整)
    Params :
      blk: 品种列表
      priceline: 价格线  
                 tick线:TickPriceLine( feat=OriginalIndexData())
                 K线:KLine(feat=KLine(freq="30m"), std_method = 'ratio',)
      calendar_name: 日历类型
      hd_feat: 大单特征 (支持通过控件调整参数)
      thickfrp_dense: dense特征 (支持通过控件调整参数)
      thickfrp_fight: fight特征 (支持通过控件调整参数)
      max_spans: 最多返回的段数（超过的丢弃）
    """
    params = lambda : { # 定义图表的可配置参数
        "blk": ["rb","j","i"], # 品种列表：螺纹钢、焦炭、铁矿石
        "priceline": TickPriceLine( feat=OriginalIndexData({'isOriginal': False}),std_method = 'ratio',), # 价格线类型：使用Tick线，进行比例标准化
        "calendar_name": "night_end_at_2300", # 交易日历：夜盘到23:00结束
        "hd_feat": HugeDealUTL()@"basic", # 大单特征：使用基础版大单通用工具，并允许通过控件调整 "basic" 相关的参数
        "thickfrp_dense": ThickFrp()@"basic_Dense", # Dense特征：使用基础版高频Dense特征，并允许通过控件调整 "basic_Dense" 相关的参数
        "thickfrp_fight": ThickFrp()@"basic_Fight", # Fight特征：使用基础版高频Fight特征，并允许通过控件调整 "basic_Fight" 相关的参数
        "max_spans": 1, # 特征雷达最大返回时间段数量
        "timespans": [("2023-02-19","2023-07-19")], # 默认分析的时间段
    }
    def hold_on_bokeh_server(self): # 定义此方法以确保Bokeh服务器会话在交互时保持活跃
        """确保图表中的交互控件（如滑块、按钮）保持响应"""
        return True

    def _impl(self): # 图表实现的核心逻辑
        # 初始化配置
        # 创建特征实例，从参数中获取
        hd_feat = self.P.hd_feat # 大单特征实例 (范围参数)
        thickfrp_dense = self.P.thickfrp_dense # Dense特征实例 (范围参数)
        thickfrp_fight = self.P.thickfrp_fight # Fight特征实例 (范围参数)
        timespans=self.P.timespans # 用户指定的时间段
        
        # 定义特征雷达
        timespans_fao = ExtractTimespans("MidScale")({ # 中等尺度的时间段提取器
            'feats': GMap.from_list([HugeDealUTL("basic"), HugeDealUTL("basic")]), # 基于大单买卖事件
            'dffilters': [lambda df: df], # 无额外过滤
            'dfkeys': ['hd_buy','hd_sell'], # 数据表名
            'utifields': [['uti'],['uti']], # 时间字段
            'symbollist':  self.P.blk, # 品种列表
            'startDay': '2023-01-01', # 扫描开始日期
            'endDay': '2024-01-28', # 扫描结束日期
            'max_spans': self.P.max_spans, # 最大返回段数
        })
  
        # 配置绘图元素
        # 配置高频特征的绘图方式 (MulFieldsGlyphs)
        MulFieldsGlyphs["ThickFrp_basic"] = lambda: { # 定义名为 "ThickFrp_basic" 的多字段绘图配置，并设为默认
                "feats":GMapX({ 
                    "dense_buy": thickfrp_dense, # dense买入信号
                    "dense_sell": thickfrp_dense, # dense卖出信号
                    "fight": thickfrp_fight # fight信号
                          }),
                'legend_labels': ['denseutl_buy', 'denseutl_sell','fightutl'],  # 图例
                "yfields": [ "deci_price2", "deci_price2","deci_price2", ], # Y轴数据字段
                'size_fields': [ 'dense_buy_strength', 'dense_sell_strength',"fight_strength"], # 点大小字段
                'size_scale': 15, # 大小缩放
                'dynstd_method': 'ratio', # 动态标准化
        }

        # 配置买盘大单的柱状图
        VBarPlot["buy_alias"] = lambda: {
            "feat": hd_feat, 
            "df_key": "hd_buy", 
            "color": "green", 
            "label": "买盘大单"
        }

        # 配置卖盘大单的柱状图
        VBarPlot["sell_alias"] = lambda: {
            "feat": hd_feat, 
            "df_key": "hd_sell", 
            "color": "red", 
            "top_coeff": -1, 
            "label": "卖盘大单"
        }

        # 构建图形 (CAEGraph)
        CAEGraph["mul_hf"]  = lambda: { # 定义一个名为 "mul_hf" 的CAEGraph配置
            "Context":  OptContext("TA_updto20240229_DBA"), # 数据上下文
            "plotsets": GMapX({ # 绘图集
                '高频事件观察': PlotSet({ # 名为 "高频事件观察" 的绘图集
                    "calendar_name": self.P.calendar_name, # 日历
                    "timespans": timespans, # 时间段
                    "timespans_fao": timespans_fao, # 备选时间段 (特征雷达)
                    "blk": self.P.blk, # 品种
                    "figs": GMapX.from_list([ # 图表布局
                        AllSymsMainFig( # 所有品种在同一个主图
                            persym_plots=GMap.from_list([ # 每个品种绘制
                                self.P.priceline, # 价格线
                                MulFieldsGlyphs("ThickFrp_basic") # 高频特征
                            ])
                        ),
                        PerSymFigs( # 每个品种单独一个附图
                            plots=GMapX.from_list([ # 附图内容
                                VBarPlot("buy_alias"), # 买单
                                VBarPlot("sell_alias"),  # 卖单
                            ]),
                             fig_height=150, # 附图高度
                        ),
                        # FigCtrls()默认不填控件，会输出控件在图上方；如果需要控件在图下面，需要显式的将控件放在图表布局类后面。
                    ])
                })
            }),   
            "theme": DefaultFigTheme(), # 主题
            "x_label_freq": "1m", # X轴标签频率
            "extra_time": 0, # 额外时间
            "fig_width": 1200, # 总宽度
            "fig_height1": 500, # 主图高度
            "fig_height": 600, # 附图总高度
            "colors2": None, # 备用颜色板
            "switches": {} # 开关
        }

        return dict(value=CAEGraph("mul_hf")) # 返回CAEGraph的配置名，框架会自动实例化

# 显示图表
MultiSymHFCAE_LIVE().run(); # 实例化，并获取布局对象 (通常在Notebook中直接显示)
# 如果在Bokeh服务器环境中运行，使用 .bkapp()
show(CAEGraph("mul_hf").bkapp(),notebook_url="http://192.168.11.88:8888")# 需要将notebook_url替换为实际的Jupyter服务器地址
```

#### 交互控件使用提示
观察多参数带有控件的用例，界面上会出现更新按钮。
- **按钮状态**：按钮处于灰色时，表示不可点击或正在处理。
- **参数调整与更新**：拖动参数控件调整参数后，"更新"按钮会变为可点击状态（例如，白色）。
- **点击更新**：点击"更新"按钮后，系统会开始应用新参数并重新计算和加载数据。
    - **即时反馈**：此时，图表可能不会立即变化，"更新"按钮可能保持可点击状态。
    - **后台处理**：请留意终端（console/terminal）输出，通常会显示正在保存特征或加载数据的提示。
- **完成更新**：当"更新"按钮再次变灰，表示参数已成功应用，特征已保存，新的图表已加载完成并显示。

--------------------------------------------------
### 更多用例见：worker/example/cae
大中小尺度用例（小尺度会另开一个界面）见：worker/example/cae/dense_utv2
中小尺度在同一个界面上展示：worker/example/cae/zig.py

----------------------------------------------------------------------
## 核心类详解

本章节将详细介绍`uplot`库中的核心类。为了帮助用户更好地理解各个组件如何协同工作以构建出最终的图表应用，本章节的组织顺序参照了从顶层到底层、从整体到局部的图表构建链路：图表集成类 -> 图表布局类 -> 绘图类 -> 特征雷达 -> 组件类 -> 主题系统 -> 基础组件。
1.  **图表集成类 (`CAEGraph`, `PlotSet`)**: 最高层的封装，负责整合和管理整个图表应用或一组图表。
2.  **图表布局类 (`AllSymsMainFig`, `PerSymFigs`, etc.)**: 负责单个图表内或多个图表间的布局和组织。
3.  **绘图类 (`KPriceLine`, `VBarPlot`, etc.)**: 实际执行数据可视化，将数据点、线、柱等绘制到图表上。
4.  **特征雷达 (`ExtractTimespans`, `PerDPTimespans`)**: 根据特定规则从原始数据中提取和筛选时间段，为绘图类准备输入。
5.  **组件类 (`FigCtrls`, `BasePPChangeWidget`)**: 提供交互功能，如参数调整控件。
6.  **主题系统 (`DefaultFigTheme`, `TBFigTheme`)**: 控制图表的整体视觉风格。
7.  **基础组件 (`PlotCtx`, `BaseFigSet`, `BasePlotter`)**:构成绘图系统的底层抽象和共享功能，用户通常不直接操作。

在学习和使用这些类时，请注意它们之间的参数关联和数据流转关系。各类的"使用示例"部分会通过代码和注释具体展示这些依赖。对于一些通用的高级用法或跨多个类的配合技巧，建议详细阅读"使用示例"，并可参考"类之间的关系"图来理解整体架构。

--------------------------------------------------
### 图表集成类
------------------------------
#### CAEGraph

**功能**: 图表应用入口，组织和布局多个图表，并提供交互功能

**参数配置**:
- `Context`: 上下文对象，默认为OptContext()
- `plotsets`: GMap对象，包含要绘制的绘图集。参数为PlotSet。
- `theme`: 主题对象，默认为DefaultFigTheme()，可以选择TBFigTheme()
- `x_label_freq`: X轴标签频率，默认为"1m"
- `extra_time`: 额外绘制的时间，默认为0
- `fig_width`: 图宽，默认为1200
- `fig_height1`: 主图高，默认为500
- `fig_height`: 附图高，默认为350
- `colors2`: 两级颜色板
- `switches`: 自定义开关

**主要方法**:
- `layout`: 创建图表布局
- `bkapp`: 创建Bokeh应用

**使用示例**:
```python
CAEGraph["example"] = lambda: {
    "Context": OptContext(
        sof_name = "TA_updto20240229_DBA", 
        stk_tlist = "steel", 
        startDay = "2013-02-19", 
        endDay = "2024-02-29", 
    ),
    "plotsets": GMapX({
        'main': PlotSet("example"),
    }),
    "theme": DefaultFigTheme(),
    "x_label_freq": "1m",
    "extra_time": 0,
    "fig_width":1200,
    "fig_height1": 600,
    "fig_height": 300,
}
# 在Notebook中显示
from bokeh.plotting import show
show(CAEGraph("example").layout(ncols=2))
# 或作为Bokeh服务器应用
show(CAEGraph("example").bkapp(ncols=2), notebook_url="http://localhost:8888")#notebook_url需要替换成实际使用的地址
```
------------------------------
#### PlotSet

**功能**: 绘图集合，组织和管理一组图表

**参数配置**:
- `calendar_name`: 日历名称，默认为"@"，可以填的参数包括"@","no_night","night_end_at_2300","night_end_at_0100","night_end_at_0230"。
- `blk`: 板块表达式。支持三种形式：
    1、支持sof下面定义了csv配置文件的品种集，具体品种集路径查看m3sof/seetings/sof中具体sof设置的sof_tlist_dir(to_do:需要有个文件可以查询目前有哪些品种集配置了csv文件),例："black"
    2、支持m3sof下面的定义的板块。具体板块名见m3sof/seetings/sof/default.py的block_fixed。例："blk@black"。
    3、支持品种列表,例：["ag","au"]
- `timespans`: 时间段列表。参数格式：[("2023-02-20", "2023-04-29")]。
- `timespans_fao`: 通过特征雷达返回时间段。timespans参数的优先级高于timespans_fao,可以理解为 timespans_fao 是在 timespans 为空时的备选方案。
- `figs`: GMap对象,包含要绘制的图集。参数填写图表布局类，可以各种图表布局类进行组合。

**使用示例**:
```python
PlotSet["example"] = lambda: {
        "calendar_name": "no_night",
        "blk": "blk@steel",
        "timespans":  [("2023-02-20", "2023-04-29")],
        "figs": GMapX.from_list([ 
          AllSymsMainFig("blkfrp"),
          AllSymsFig("blkfrp"),
          PerSymFigs("Segs_Vbar"),
          PerSymFigSet("Segs_Vbar"),
        ]),
    }
```
--------------------------------------------------
### 图表布局类

------------------------------
#### **图表布局类快速选择指南**:
| 图表类型 | 主要特点 | 适用场景 | 典型应用 |
|:-------:|:------:|:-------:|:-------:|
| AllSymsMainFig |  • 所有品种在一张图 | • 多品种主图对比 | • 多品种k线上的高频事件 |
| AllSymsFig |  • 所有品种在一张图 | • 附图指标对比 | • RSI/MACD等指标 |
| PerSymFigs | • 每个品种单独一张图| • 单品种详细分析 | • 成交量指标 |
| PerSymFigSet | • 每个品种多张图• 定制每个品种图集 | • 多个品种一起既要观察主图又要观察附图进行多维分析| • 观察每个品种k线上的高频事件和成交量指标 |

------------------------------
#### AllSymsMainFig

**功能**: 多品种单主图，继承了AllSymsFig和MainFig的特性

**参数配置**:
- 继承AllSymsFig和MainFig的所有参数

**使用示例**:
```python
AllSymsMainFig["blkfrp"]= lambda: {
     'plots': GMapX.from_list([
        KPriceLine("blk_single"),
        MulFieldsGlyphs("BlkThickFrp"),
        ]),
     'persym_plots':GMapX.from_list([
        KPriceLine("sym_1m"),
        MulFieldsGlyphs("ThickFrp_dense"),
        ]),
     'blk_as_1st_sym': False}
```
------------------------------
#### AllSymsFig

**功能**: 多品种单图，同一图表上绘制多个品种的数据，更适用于主图下方的多品种附图

**参数配置**:
- 继承OneFig的所有参数
- `title`: 默认为"!{n_syms} 品种图"
- `persym_plots`: GMap对象，每个品种都会绘制一次的内容
- `plots`: GMap对象，只绘制一次的内容，通常用于画板块的内容
- `blk_as_1st_sym`: 是否将板块当做第一个品种（适用于画图的既需要画板块又需要画板块中各单品种的用例，需结合KPriceLine的参数合理使用）

**使用示例**:
```python
AllSymsFig["blkfrp"]= lambda: {
     'plots': GMapX.from_list([
        KPriceLine("blk_single"),
        ]),
     'persym_plots':GMapX.from_list([
        KPriceLine("sym_1m"),
        ]),
     'blk_as_1st_sym': False}
```

------------------------------
#### PerSymFigs

**功能**: 每品种一个图的多图集，为每个品种创建独立的图表

**参数配置**:
- 继承BaseFigSet的所有参数
- `title`: 默认为"!{sym} - 图"
- `plots`: GMap对象，每个品种要绘制的内容
- `live_ctrls_persym`: 是否为每个品种显示控件
- `blk_as_1st_sym`: 是否将板块当做第一个品种

**使用示例**:
```python
PerSymFigs["Segs_Vbar"]= lambda: {
      "plots":GMapX.from_list([
        VBarPlot("HugeDealUTL_basic_hd_buy"),
        ])
}
```

------------------------------
#### PerSymFigSet

**功能**: 每品种一套图的多图集，为每个品种创建一组相关的图表

**参数配置**:
- 继承BaseFigSet的所有参数
- `title`: 默认为"!{sym} - 图"
- `figs`: GMap对象，每个品种要绘制的图集，既有主图又有附图的情况需要用这个
- `live_ctrls_persym`: 是否为每个品种显示控件

**使用示例**:
```python
PerSymFigSet["Segs_Vbar"]= lambda: {
    "figs": GMapX.from_list([
        MainFig("ThickFrp_basic_Dense"),
        SubFig("HugeDealUTL_basic_hd_buy"),
      ])    
}
```

------------------------------
#### MainFig

**功能**: 单主图，用于绘制主图(通常是价格图)

**参数配置**:
- 继承OneFig的所有参数
- 默认`title="!{sym} - 主图"`

**使用示例**:
```python
MainFig["ThickFrp_basic_Dense"] = lambda: {
    "plots":GMapX.from_list([
        SegsPlot("ThickFrp_basic_Dense"),
        KPriceLine("sym_1m"),
        ])
}
```

------------------------------
#### SubFig

**功能**: 单附图，用于绘制附图(通常是指标图)

**参数配置**:
- 继承OneFig的所有参数
- 默认`title="!{sym} - 附图"`

**使用示例**:
```python
SubFig["HugeDealUTL_basic_hd_buy"]= lambda: {
     "plots":GMapX.from_list([
        VBarPlot("HugeDealUTL_basic_hd_buy"),
        ])
}

```
------------------------------
#### OneFig

**功能**: 单图集基类，绘制单个图表（通常用户不使用这个图）

**参数配置**:
- 继承BaseFigSet的所有参数
- `plots`: GMap对象，包含要绘制的所有图
--------------------------------------------------
### 绘图类

#### **绘图类快速选择指南**

下表旨在帮助您根据典型的可视化需求和数据特点，快速选择合适的绘图类。

| 绘图类             | 典型应用场景                     | 主要优势/特点                                                                            | 备注                                             |
| :----------------- | :------------------------------| :-------------------------------------------------------------------------- | :---------------------------------------------- |
| `KPriceLine`       | K线图（蜡烛图）                  | 清晰展示开盘价、收盘价、最高价、最低价；可配置标准化方法，便于不同量纲数据对比。  | 是价格分析的基础图表。                              |
| `TickPriceLine`    | Tick价格线                      | 能够细致、连续地反映价格的微小变动，适合观察短期价格行为。                      | 无                                                 |
| `VBarPlot`         | 柱状图                          | 直观表示某个时间点上数值的大小，常用于附图显示辅助分析信息。                    | Y轴通常从0开始（也可配置），高度代表数值。            |
| `MulFieldsGlyphs`  | 标记多种离散点/事件              | 高度灵活，支持多种图形标记，点的大小和颜色可由数据驱动，适合展示多维度信息。       | 是功能非常强大的通用点/标记绘图工具。    |
| `SegsPlot`         | 绘制单一直线段                  | 简单直接地连接两个数据点，用于表示一个具有起止点的事件或区间。                    | 若需绘制多种或多条线段，应考虑 `MulSegPlot`。        |
| `MulSegPlot`       | 绘制多种/多条连接线段            | 能够在一张图上清晰区分并展示多组线段数据，每种线段可有不同样式。                   | 比 `SegsPlot` 更通用，适合复杂线段组合。             |
| `StrasTradePlot`   | 策略交易记录图                  | 直观评估策略表现，快速识别交易信号的触发位置和结果。                             | 无                                                   |
| `TextPlot`         | 在图上特定位置显示文本           | 可以在关键位置提供额外的文字信息，增强图表的可读性和信息密度。                    | 无                                                    |
| `MulPointPlot`     | 绘制多个历史数据点              | 适用于数据点较少，或需要根据索引而非精确时间戳定位的旧版场景。                   | `MulFieldsGlyphs` 通常更为现代和灵活。                |
| `OneToGroupPointPlot` | 分组显示避免重叠的多个点      | 解决数据点在视觉上过度密集、难以分辨的问题。                                    | 是 `MulPointPlot` 的一种增强，改善拥挤区域的可视化效果。|
| `SeqOfFieldsPlot`  | 绘制不定长度字段序列             | 专门处理某些特征产生的数据结构，其中一个主记录可能包含一个变化长度的相关值列表。   | 使用场景相对特定。                                    |

------------------------------
#### KPriceLine

**功能**: K线图，绘制数据的OHLC烛台图

**参数配置**:
- `std_method`: 标准化方法
- `dynstd_sym`: 动态标准化品种。dynstd_sym 是手工给它分配一个品种 id，主要为了板块 K 线动态标准化时，基于它算的特征能够跟随它一起动态标准化，特征画图时 dynstd_sym 指定成一样的就达到效果。不要和现有品种 id 冲突。
- `force_sym`: 强制使用的品种,通常用来画板块k线
- `feat`: 特征对象，默认为KLine()
- `extra_bars`: 额外多画的K线数量，默认为0
- `add_hover`: 是否添加悬停提示，默认为True
- `color`: 颜色
- `alpha`: 透明度，默认为0.8
- `label`: 图例标签，默认为"K线"
- `NextProcess`: 进一步处理图表的函数(通常不用，只有特定用例用，详见大中小事件用例)

**使用示例**:
```python
#场景1：1m的k线，不进行标准化
KPriceLine["sym_1m"]= lambda: {
     'feat(KLine).freq': '1m',
}

#场景2：1m的k线，以"ratio"方式进行标准化
KPriceLine["sym_1m"]= lambda: {
     'std_method': "ratio",
     'feat(KLine).freq': '1m',
}

#场景3：用于画blk参数中是blk，既想画单品种k线，又想画板块k线，就需要组合下面这种只画板块的k线和场景2的k线在一张图中
KPriceLine["blk_single"]= lambda: {
     'std_method': "ratio",
     'force_sym': "blk@steel",#指定只画板块的k线
     'dynstd_sym': "blk001",#对应画板块特征图的这个参数也需要填同样的字符串
     'feat(KLine).freq': '1m',
     'extra_bars': 0,
     'add_hover': True,
     'color': None,
     'alpha': 0.8,
     'label': 'K线' 
}
#场景4：用于画多个品种和板块的k线，跟随指定品种进行标准化
KPriceLine["blk"]= lambda: {
     'std_method': "ratio",
     'dynstd_sym': "blk001",#对应画板块特征图的这个参数也需要填同样的字符串
     'feat(KLine).freq': '1m',
     'extra_bars': 0,
     'add_hover': True,
     'color': None,
     'alpha': 0.8,
     'label': 'K线' 
}

```

------------------------------
#### TickPriceLine

**功能**: Tick价格线，绘制连续的价格线

**参数配置**:
- `std_method`: 标准化方法
- `feat`: 特征对象，默认为SubContinuousContract()
- `df_key`:数据表名，默认为"value"
- `line_field`: 线值字段，默认为"price"
- `color`: 颜色
- `alpha`: 透明度，默认为0.8
- `line_width`: 线宽，默认为1
- `label`: 图例标签，默认为"Tick价格线"

**使用示例**:
```
# 指数tick线（默认是主力合约tick线），按照"ratio"进行标准化
TickPriceLine["index"]= lambda: {
    'feat': OriginalIndexData({'isOriginal': False})，
    'std_method': "ratio",
}
```

------------------------------
#### VBarPlot

**功能**: 柱状图，主要用于在时间序列图表中绘制垂直柱状条形图。通常用于绘制成交量等数据

**参数配置**:
- `feat`: 特征对象
- `df_key`:  数据表名，默认为"hd_buy"
- `uti_field`: 时间字段，用于X轴定位，默认为"uti"，
- `top_field`: 柱顶字段，指定哪个字段用于决定柱子的高度。默认为"grade"
- `top_coeff`: 柱顶系数，柱形高度的乘法系数，以整体放大或缩小所有柱子的高度，默认为1
- `top_up_offset`: top的向上偏移量，柱形高度的加法偏移量，可以整体上移或下移所有柱子默认为0
- `bottom`: 柱底值，默认为0。柱形实际高度值 = 原始数据[top_field] * top_coeff + top_up_offset
- `color`: 颜色，默认为"black"
- `alpha`: 透明度，默认为0.8
- `width`: 柱宽，默认为0.5
- `label`: 图例标签，必填，参数格式字符串
- `hover_tslabel`: 是否在浮标中显示时间戳，默认为True。需要注意如果数据太密会导致hover_tslabel显示不正常，太密的数据不建议显示。

**使用示例**:
```python
VBarPlot["HugeDealUTL_basic_hd_buy"]= lambda: {
     'feat':HugeDealUTL("basic"),
     'df_key': 'hd_buy',
     'uti_field': 'uti',
     'top_field': 'grade',
     'top_coeff': 1,
     'bottom': 0,
     'color': 'black',
     'alpha': 0.8,
     'width': 3,
     'label': "大买单",
     'hover_tslabel': False
}
```

------------------------------
#### MulFieldsGlyphs

**功能**: 多字段图形，绘制单个特征的多个字段

**参数配置**:
- `glyphs`: 图形形状，默认为"asterisk"
- `feats`: 特征对象
- `dfkeys`: 数据表名，默认为[None]
- `legend_labels`: 图例标签
- `colors`: 颜色列表
- `xfields`: 横轴时间字段名
- `yfields`: 纵轴数值字段名
- `timefieldtype`: 时间字段类型，支持"idx"、"ts"、"uti"，默认为"uti"
- `size_fields`: 指定图形大小的字段
- `size_scale`: 图形大小的放大倍率，默认为100
- `size_base`: 基础大小，默认为5
- `size`: 图形大小，默认为5
- `alphas`: 透明度，默认为0.6
- `dynstd_method`: 动态标准化方法
- `dynstd_sym`: 动态标准化品种
- `hover_tslabel`: 是否在浮标中显示时间标签，默认为True
- `widgeter`: 参数变更组件

**使用示例**:
```python
#画高频事件的点图
MulFieldsGlyphs["ThickFrp_dense"] = lambda: {
    "feats": GMapX({
        "f1": ThickFrp("basic_Dense"),  # 特征1: 高频dense特征
        "f2": ThickFrp("basic_Dense"),  # 特征2: 高频dense特征
    }),
    "legend_labels": ['denseutl_buy', 'denseutl_sell'],
    "yfields": [
        "deci_price2",                # 特征 f1 使用的 Y 轴字段，这里表示高频dense特征实际确认点
        "deci_price2"                 # 特征 f2 使用的 Y 轴字段
    ],
    "size_fields": [
        'dense_buy_strength',        # 特征 f1 使用的大小字段，这里表示高频dense特征买方向实际确认点强度
        'dense_sell_strength'        # 特征 f2 使用的大小字段，这里表示高频dense特征卖方向实际确认点强度
    ],
    "size_scale": 15,
}

#画贴近转折的线图
MulFieldsGlyphs["scaleturn"] = lambda: {
    "feats": GMap({
        "f1": ScaleTurnCalendar("mid") , # 特征: 提供不同线段类型数据的特征映射 (ScaleTurn, Zigzag)
    }),
    "glyphs": "line",  
    "xfields": ["x"],
    "yfields": ["y"],
    "legend_labels": ["scaleTurn"],
    "timefieldtype": 'uti',
    "alphas": 0.6,
}

#画板块高频事件的点图
MulFieldsGlyphs["BlkThickFrp"]=lambda :{
     'feats': GMapX.from_list([BlkThickFrp("basic_Dense")]), 
     'dfkeys': '',
     'xfields': ["deci_uti2"],
     'yfields': [ "deci_price2"],
     'legend_labels':["板块dense",],
     'alphas': 1,
     'size_fields': ["dense_strength",],
     'size_scale': 15,
     'dynstd_sym': "blk001",
    }

```

------------------------------
#### MulSegPlot

**功能**: 多段线绘图，绘制多段连接线

**参数配置**:
- `feats`: 特征对象
- `k_freq`: K线频率
- `x0s`, `x1s`, `y0s`, `y1s`: 线段起止点坐标字段
- `dfkeys`: 数据表名
- `timefieldtype`: 时间字段类型，支持"idx"、"ts"、"uti"
- `colors`: 颜色列表
- `legend_labels`: 图例标签
- `alphas`: 透明度，默认为0.6
- `line_widths`: 线宽，默认为1
- `line_dashs`: 线型，默认为"solid"
- `hover`: 是否启用悬停提示，默认为True

**使用示例**:
```python
MulSegPlot["ThickFrp_dense"] = lambda: {
    # 特征: 提供线段数据
    "feats": GMapX.from_list([ThickFrp("basic_Dense"), ThickFrp("basic_Dense")]),
    # x0s: 线段起点的时间字段 (UTI)
    "x0s": ["data_uti1", "deci_uti1"],
    # x1s: 线段终点的时间字段 (UTI)
    "x1s": ["data_uti2", "deci_uti2"],
    # y0s: 线段起点的数值字段 (价格)
    "y0s": ["data_price1", "deci_price1"],
    # y1s: 线段终点的数值字段 (价格)
    "y1s": ["data_price2", "deci_price2"],
    # timefieldtype: 使用的时间字段类型 ('uti' - 通用时间索引)
    "timefieldtype": 'uti',
    # colors: 每种线段类型的颜色
    "colors": ["blue", "red"],
    # legend_labels: 图例标签
    "legend_labels": ["dense实际点", "dense确认点"],
    # alphas: 线条的透明度
    "alphas": [0.6],
    # line_widths: 线条宽度
    "line_widths": [2],
    # line_dashs: 线条样式 ('solid', 'dashed', 'dotted'等)
    "line_dashs": ['solid', 'solid'],
}
```

------------------------------
#### StrasTradePlot

**功能**: 策略交易图，绘制交易记录，包括开仓点、平仓点、连接线以及盈亏情况。

**参数配置**:
- `traders`: GMap对象，包含要绘制交易的策略trader
- `colors`: 颜色列表
- `legend_labels`: 图例标签
- `trade_volume`: 是否显示交易量，默认为True

**使用示例**:
```python
StrasTradePlot["s1"] = lambda :{
        "traders":GMapX.from_list([
           SimSimpleTrader(Strategy=S1Brk_HP3_AMAAbsLt_KDJ()),
        ]),  
        "legend_labels":["kdj策略",],
        "trade_volume":False, # 是否显示交易手数
}  
```

------------------------------
#### SegsPlot

**功能**: 线段绘图，绘制两点之间的线段。单特征线段图，如果需要画多特征多线段用MulSegPlot。

**参数配置**:
- `feat`: 特征对象
- `df_key`: 数据表名，默认为"dseg_buy"
- `uti1_field`: 起始时间字段，默认为"data_uti1"
- `uti2_field`: 结束时间字段，默认为"data_uti2"
- `y1_field`: 起始Y值字段，默认为"data_price1"
- `y2_field`: 结束Y值字段，默认为"data_price2"
- `color`: 颜色，默认为"black"
- `alpha`: 透明度，默认为0.8
- `line_width`: 线宽，默认为5
- `label`: 图例标签，默认为None，会显示"线段"

**使用示例**:
```python
SegsPlot["ThickFrp_basic_Dense"] = lambda: dict(
    feat=ThickFrp("basic_Dense"),  # 特征
    df_key="",
    uti1_field="data_uti1",  # 时间字段名
    uti2_field="data_uti2",  # 时间字段名
    y1_field="data_price1",  # y 值字段名
    y2_field="data_price2",  # y 值字段名
    color="black",  # 颜色
    alpha=0.8,  # 透明度
    line_width=5,  # 线宽
    label=None,  # 图例  None为默认值:代表不需要图例
    )
```
------------------------------
#### TextPlot

**功能**: 文本绘图，在图表上显示文本标签

**参数配置**:
- `feat`: 特征对象
- `df_key`: 数据表名
- `x_field`: X坐标字段名
- `y_field`: Y坐标字段名
- `text_field`: 文本内容字段名
- `field_uti2ts`: 是否将UTI转为时间戳，默认为True
- `color`: 颜色，默认为"black"
- `alpha`: 透明度，默认为0.8
- `label`: 图例标签
- `dynstd_method`: 动态标准化方法
- `dynstd_sym`: 动态标准化品种

**使用示例**:
``` python
TextPlot["scaleturn_text"] = lambda : {
    "feat": ScaleTurnCalendar("large"),
    'label': "scale_text",
    'df_key': None,
    'x_field': "x", 
    'y_field': "y",
    'text_field': "x", 
}
```

------------------------------
#### MulPointPlot

**功能**: 多点绘图，绘制多个历史点

**参数配置**:
- `feats`: 特征对象，可以是单个特征(用于绘制多个点)，也可以是多个特征(每个特征绘制一个点)
- `xfield`: 横轴字段名，如果只有1个值，且feats是单个特征，将自动查找所有以该值开头的字段。如果有多个值，将与yfield一一对应绘制多个点
- `yfield`: 纵轴字段名，与xfield类似，如果只有1个值且feats是单个特征，会自动查找所有以该值开头的字段
- `timefieldtype`: 时间字段类型，默认为"idx"，"idx"（索引）或"ts"（时间戳）
- `colors`: 颜色列表
- `legend_labels`: 图例标签
- `size_base`: 基础大小，默认为20
- `size`: 图形大小，默认为5
- `size_field`: 指定图形大小的字段
- `size_scale`: 图形大小的放大倍率，默认为100
- `alphas`: 透明度，默认为0.6
- `line_widths`: 线宽，默认为1
- `hover`: 是否启用悬停提示，默认为True

**使用示例**:
```python
# 暂无实际可运行的用例
# 历史6.2版本可运行的用例：
MulPointPlot["simplesymmetry_test"] = lambda : {
    "feats": SimpleSymmetryFrp("test"),  # 可以是单个特征的多个点，可以是多个特征的单个点。
    "xfield": ["vertice2.x"],  # 多个x字段，如果只有1个，表示多个特征用相同字段，或是单个特征的所有以它开头的字段。
    "yfield": ["vertice2.y"],  # 与xfield类似，如果只有1个值且feats是单个特征，会自动查找所有以该值开头的字段
    "timefieldtype": "idx",  # 支持idx或者ts类型
    "colors": None,
    "legend_labels": "symmetry",
    "size_base": 20,
    "size": 5,
    "size_field": None,  # 通过特征值指定图形大小
    "size_scale": 100,  # 图形大小的放大倍率
    "alphas": 0.6,
    "line_widths": 1,
    "hover": True,
    "tarDf": None
}
```

------------------------------
#### OneToGroupPointPlot

**功能**: 一对多分组点图，将多个历史点分组并防止重叠

**参数配置**:
- 继承MulPointPlot的所有参数
- `groupN`: 分组数，默认为1。
- `adjField`: 需要调整值的字段，一般填价格字段
- `adjFunc`: 每组数据的调整函数。

**使用示例**:
```
暂无实际可用的用例
```

------------------------------
#### SeqOfFieldsPlot

**功能**: 不定长度字段序列绘图，将不定长度的数据拆分为多个df并绘制

**参数配置**:
- `feat`: 特征对象
- `field`: 不定长度的字段名，默认为"value"
- `glyphs`: 图形形状，默认为"cross"
- `colors`: 颜色列表
- `labels`: 图例标签

**使用示例**:
```
暂无实际可用的用例
```

--------------------------------------------------
### 特征雷达
特征雷达是基于岳总实现的python类，用于提取数据中满足特定约束条件时间段的类似于"雷达"一样的高级工具，帮助用户高效的识别特征关系。过去采用的方式需要一个个手动拖动，肉眼去找符合条件的时间段，依赖人工去定位。而这个工具是通过明确声明特征，自动根据这些特征快速定位所有符合条件的时间段。比如可以通过大拐头特征，定位出发生大拐头的时间段，观察大拐头附近发生了哪些高频事件、成交量和价格发生了什么变化。使用这种高级工具能够加快观察和分析的速度，让我们能够在短时间内找到符合条件的时间段，极大的提升工作效率。

"设计高级工具提升效率"这种思维方式是我们工具设计的核心原则，也是平台第一个版本的基础。未来我们将继续在这个原则上完善其他功能，尤其是针对一些难以用肉眼观察到的统计特征，继续提升工具的设计，优化其功能，让工作效率不断提高。

------------------------------
#### ExtractTimespans

**功能**: 提取时间段，从特征数据中提取连续的时间段

**处理逻辑**:
1、获取品种列表中多个特征事件发生的数据，通过dffilters对特征事件进行过滤，然后将所有品种所有特征发生事件的时间点被合并到同一个列表中（不区分时间点来自哪个品种哪种事件，所有的时间点被视为一个整体）。
2、将所有时间点数组连接成一个大数组，去除重复值并排序，返回一个有序无重复值的时间点数组。
3、n_inter是表示当前事件点与所处时间段的第一个事件点之间能够容忍的的最大间隔，如果超过这个间隔，当前事件点应划分到下一个时间段。如果是第一个事件点，就表示与startDay的最大间隔。
4、n_margin表示往时间段中的第一个事件点前扩n_margin，最后一个事件点往后扩n_margin。
5、n_max控制单个时间段的最大长度。即使事件连续发生，当时间段长度接近n_max时，也会开始一个新的时间段。n_max包含了n_margin。
6、max_spans表示最多需要返回多少个时间段。

**参数配置**:
- `uti2ts`: 是否将UTI转为时间戳，默认为False
- `feats`: GMap对象，包含特征列表
- `dfkeys`:特征数据中DataFrame的名称
- `dffilters`: 用于过滤特征数据的函数列表
- `utifields`: 时间字段名
- `symbollist`: 品种代码列表
- `startDay`, `endDay`: 时间范围
- `n_inter`: 单段内最大间隔半秒数，默认为72000（10小时）
- `n_margin`: 结果时间段两端的额外半秒数，默认为7200（1小时）
- `n_max`: 单段最多半秒数，默认为144000（20小时）
- `max_spans`: 最多返回的段数，默认为100
- `time_format`: 时间格式字符串，默认 '%Y-%m-%d %H:%M:%S'

**使用示例**:
```python
ExtractTimespans["BlkThickFrp"]=lambda :{
    'feats': GMapX.from_list([BlkThickFrp("basic_Dense")]),  # 分析特征
    'utifields': [['deci_uti2']],   # 时间字段
    'symbollist': ["y"],            # 品种列表
    'startDay': '2022-12-01',       # 开始日期
    'endDay': '2024-01-28',         # 结束日期
    'n_inter': 7200*5,  # 间隔时间5小时
    'n_margin': 720,    # 边界时间720秒
    'n_max': 7200*2,    # 最大持续时间2小时
    'max_spans': 6      # 最大时间片段数
}
timespans = ExtractTimespans("BlkThickFrp").timespans()
```

------------------------------
#### PerDPTimespans

**功能**: 每个数据点的时间段，为每个数据点创建一个时间窗口，窗口大小恒定

**处理逻辑**:数据处理步骤和ExtractTimespans类似，只是没有n_inter和n_max参数，是为每个事件点都创建一个时间窗口。更适用于分析比较离散的事件。
**参数配置**:
- `uti2ts`: 是否将UTI转为时间戳，默认为False
- `feats`: GMap对象，包含特征列表
- `dfkeys`:特征数据中DataFrame的名称
- `dffilters`: 用于过滤特征数据的函数列表
- `utifields`: 时间字段名
- `symbollist`: 品种代码列表
- `startDay`, `endDay`: 时间范围
- `n_margin`: 结果时间段两端的额外半秒数，默认为7200（1小时）
- `max_spans`: 最多返回的段数，默认为100
- `time_format`: 时间格式字符串，默认为"%Y-%m-%d %H:%M:%S"

**使用示例**:
```python
PerDPTimespans["ScaleTurnSeg_mid"]=lambda :{
    'feats': GMapX.from_list([ScaleTurnSeg("mid")]),  # 分析特征
    'utifields': [["x1"]],   # 时间字段
    'symbollist': ["ag"],            # 品种列表
    'startDay': '2022-12-01',       # 开始日期
    'endDay': '2024-01-28',         # 结束日期
    'n_inter': 7200*5,  # 间隔时间5小时
    'n_margin': 720,    # 边界时间1h
    'n_max': 7200*2,    # 最大持续时间2小时
    'max_spans': 6      # 最大时间片段数
}
timespans = PerDPTimespans("ScaleTurnSeg_mid").timespans()
```

--------------------------------------------------
### 组件类

------------------------------
#### FigCtrls

**功能**: 动态参数控件，显示交互控件。主要用于输入特征是范围参数，需要拖动看多组参数的情况。FigCtrls()放在图表布局类前，表示控件在页面顶部。放在图表布局类前，表示控件在页面底部。

**参数配置**:
- 继承BaseFigSet的所有参数

**使用示例**:
```python
ZigZag["small_turn"] = lambda: {
    "featIn": KLine(freq="30m") % ["close as value", "closeUti as uti"],
    "retracePct": plist([0.5, 0.8, 1.2, 1.8, 2.7]) # 转折点，被包络穿过0.5, 1, 1.5, 
}

RctZigWithStatus["small_turn"] = lambda: {
    "zig": ZigZag()@"small_turn"
}

MulFieldsGlyphs["zig"] = lambda: dict(
    glyphs= ["square"],
    feats=GMapX.from_list([RctZigWithStatus()@"small_turn"]),
        legend_labels=["turn"],
        colors=["grey"],
        xfields=["posUTI1"],
        yfields=["price1"],
        timefieldtype="uti",
        size=2.5,
        alphas = 0.5,
        size_fields=None,
        dynstd_method=True,
)
#多品种共用同一个控件，在同一张图上画，控件在图底部
PlotSet["zig_live"] = lambda: {
            "calendar_name": "no_night",
            "blk": ["ag","rb"],
            "timespans":[("2023-02-20", "2023-04-29")],
            "figs": GMapX.from_list([ 
                AllSymsMainFig(
                    persym_plots=GMapX.from_list([
                        KPriceLine(feat=KLine(freq=freq), alpha=1),
                        MulFieldsGlyphs("zig"),
                    ]),         
                ),
                FigCtrls()
            ]),
        }
#每个品种单独一张图一个控件，控件在图顶部。如果live_ctrls_persym=True会每个品种对应一张图，但多个品种共用一个控件。
PlotSet["zig_live_persym"] = lambda: {
            "calendar_name": "no_night",
            "blk":["ag","rb"],
            "timespans":[("2023-02-20", "2023-04-29")],
            "figs": GMapX.from_list([ 
                FigCtrls(),
                PerSymFigs(
                    plots=GMapX.from_list([
                        KPriceLine(feat=KLine(freq=freq), alpha=1),
                        MulFieldsGlyphs("zig"),
                    ]),   
                live_ctrls_persym=True      
                ),  
            ]),
        }
```

------------------------------
#### BasePPChangeWidget

**功能**: 参数范围改变自定义组件，用于动态调整参数。一般不单独使用，需要和其他图组合使用。

**参数配置**:
基类，具体参数由子类定义

**主要方法**:
- `create_widget`: 创建交互控件

**使用示例**:
```python
class TestMidZigChangeWidget(BasePPChangeWidget):#完整用例见worker/example/cae/zig.py
    """
    中尺度图切换参数后.点击确定切换小尺度图
    """

    params = lambda: {
        "Plot": TestSmallZigGraph(),
        "layout": None,  # bokeh layout
    }

    def create_widget(self, get_fao: callable):
        """ 
        Params:
            get_fao: 获取当前选择参数的特征对象, 这里即 ScaleTurnSeg
        """
        # 固定用例写法，可根据实际情况调整

        btn = bkh.Button(label="切换小尺度图", button_type="primary")

        def _click_btn():
            btn.label = "加载中..."
            btn.disabled = True

            f = get_fao()
            if not isinstance(f, ScaleTurnSeg):
                raise Exception(f"切换特征不是ScaleTurnSeg: {type(f)}")

            new = self.P.Plot(Tar=f)

            # 主要代码
            # 整个 bokeh 图删除最后一个后再添加新的(即删除旧的小尺度图后添加新的小尺度图)
            layout = self.P.layout
            layout.children.pop()
            layout.children.append(new.layout())

            btn.label = "切换小尺度图"
            btn.disabled = False

        btn.on_click(_click_btn)
        return btn
```

--------------------------------------------------
### 主题系统

--------------------------------------------------
### DefaultFigTheme

**功能**: 默认主题，提供基本的白色背景主题

**参数配置**:
- `background_fill_color`: 背景颜色，默认为"white"

**特点**:
- 白色背景
- 网格线默认隐藏（alpha=0）
- K线颜色跟随品种颜色（不区分涨跌）
- 简洁明亮的视觉风格

--------------------------------------------------
### TBFigTheme

**功能**: TB风格主题，黑色背景，类似交易软件的主题

**特点**:
- 黑色背景
- 显示虚线网格（alpha=0）
- K线根据涨跌显示不同颜色：第一个品种：涨-红色，跌-绿色；其他品种：涨-浅红色(#806060)，跌-浅绿色(#608060)
- TB交易软件风格

--------------------------------------------------
### 基础组件

------------------------------
#### PlotCtx (用户通常不会直接使用)

**功能**: 为指定时间段的图表，进行画图数据截取和转换。

------------------------------
#### BaseFigSet(用户通常不会直接使用)

**功能**: 图集基类，所有图集类的父类

**参数配置**:
- `title`: 图表标题，支持格式化(用`!`开头,可以填sym,n_sym,span_info)
- `fig_width`: 图宽
- `fig_height`: 图高
- `show_legend`: 是否显示图例
- `legend_alpha`: 图例透明度
- `legend_size`: 图例大小
- `legend_location`: 图例位置
- `hover`: 是否启用悬停提示
- `fit_y_range`:  是否自适应 y 轴显示范围。但有动态标准化内容的话则失效
- `colors2`: 两级颜色板

**主要方法**:
- `plot_figs`: 绘制图集(需要子类实现)
- `_create_fig`: 创建图表
- `_finish_fig`: 完成图表

------------------------------
#### BasePlotter(用户通常不会直接使用)

**功能**: 绘图器基类，所有绘图类的父类

**参数配置**:
根据子类不同而异

**主要方法**:
- `_plot_fig`: 绘制图表(需要子类实现)

----------------------------------------------------------------------
## 类之间的关系

```
BaseFigSet
  ├── OneFig
  │     ├── MainFig
  │     └── SubFig
  ├── AllSymsFig
  │     └── AllSymsMainFig
  ├── PerSymFigs
  └── PerSymFigSet

BasePlotter
  ├── SegsPlot
  ├── VBarPlot
  ├── KPriceLine
  ├── TickPriceLine
  ├── MulFieldsGlyphs
  ├── MulSegPlot
  ├── StrasTradePlot
  ├── MulPointPlot
  │     └── OneToGroupPointPlot
  ├── SeqOfFieldsPlot
  └── TextPlot

FigTheme
  ├── DefaultFigTheme
  └── TBFigTheme

DoFunctionFao
  ├── ExtractTimespans
  ├── PerDPTimespans
  ├── PlotSet
  └── CAEGraph
```
