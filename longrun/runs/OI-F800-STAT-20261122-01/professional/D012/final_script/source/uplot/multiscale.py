"""
Multi-Scale Layout Components

多尺度布局组件，用于构建复杂的多尺度图表应用
"""

__all__ = [
    "MultiScaleLayout",
]

from typing import *
from bokeh.models import CustomAction,ScrollBox
import itertools

import time

import numpy as np
import pandas as pd

from m3 import *
from m3v import *

from mquant.frame import *
from mquant.frame.lib3 import *
from mquant.quant import *

from mquant.tis.t0.gen.cc import *
from mquant.tis.blk.gen import *

from .core import *
from .pfw import *
from .pdt import *

from .utkv2 import *
from .utlv2 import *

class MultiScaleLayout(DoFunctionFao):
    """
    Author: cyf
    Since : 2025-07-24
    Desc  : |
       多个尺度图表的布局配置类
       封装多尺度图表的复杂布局逻辑
       支持2-3个尺度的图表自动布局
       大尺度图在顶部，中小尺度图按列排列
       自动处理时间段关系和滚动容器
    Params:
       scale_graphs: |
            GMap对象，包含2-3个尺度的CAEGraph
            填两个：依次是大尺度图和中尺度图
            填三个：依次是大中小尺度图
            要求每个CAEGraph的plotsets参数有且只有一个PlotSet
            除了最大尺度的图，其余图的PlotSet均使用timespans_fao参数
    """

    params = lambda: {
        "scale_graphs": GMap(),  # 多尺度图表配置
    }
    
    class Meta:
        on_pable = True
        
    def layout(
        self,
        ncols=1,  # 保持与CAEGraph一致，虽然在多尺度布局中可能不直接使用
        all_figs=None,
        live_ctrls=None,
        live_updaters=None,
        plot_roots: Optional[list[PlotDataFolder]] = None,
    ):
        """
        创建多尺度图表布局
        
        Args:
            ncols: 列数（保持与CAEGraph接口一致）
            all_figs: 图表列表（由CurrWidgets管理）
            live_ctrls: 实时控件字典（由CurrWidgets管理）
            live_updaters: 实时更新器字典（由CurrWidgets管理）
            plot_roots: 绘图根节点列表，用于notebook环境
            
        Returns:
            bokeh布局对象
        """
        scale_graphs = self.P.scale_graphs
        scale_list = list(scale_graphs.P.values())
        
        if len(scale_list) < 2 or len(scale_list) > 3:
            raise ValueError("scale_graphs必须包含2-3个尺度的图表")
            
        # 根据数量确定大中小尺度图
        if len(scale_list) == 2:
            big_graph, mid_graph = scale_list
            small_graph = None
        else:  # len(scale_list) == 3
            big_graph, mid_graph, small_graph = scale_list
            
        # 验证每个CAEGraph只有一个PlotSet
        for i, graph in enumerate(scale_list):
            plotsets = graph.P.plotsets
            if len(plotsets.P) != 1:
                raise ValueError(f"第{i+1}个尺度图的plotsets必须有且只有一个PlotSet")
                
        # 使用传入的参数初始化，如果没有传入则创建新的
        if live_ctrls is None:
            live_ctrls = {}
        if live_updaters is None:
            live_updaters = {}
        if plot_roots is None:
            plot_roots = []
            
        upd_btn = bkh.Button(label='更新')
        
        # 分别收集每个图的布局
        big_figs, mid_figs, mul_small_figs = [], [], []
        
        # 1. 绘制大尺度图
        big_layout = big_graph.layout(
            ncols=ncols,
            plot_roots=plot_roots
        )
        
        # 2. 获取中尺度图的时间段（用于确定中小尺度图的数量）
        mid_plotset = list(mid_graph.P.plotsets.P.values())[0]
        
        # 确定上下文和相关参数
        context = mid_graph.P.Context
        calendar_name = getattr(mid_plotset.P, 'calendar_name', '@')
        blk = getattr(mid_plotset.P, 'blk', [])
        # 1. 先获取大尺度图的时间范围
        big_plotset = list(big_graph.P.plotsets.P.values())[0]
        if hasattr(big_plotset.P, 'timespans') and big_plotset.P.timespans:
            big_timespan = big_plotset.P.timespans[0]  # 取第一个timespan
            big_start, big_end = big_timespan
            
            # 2. 将大尺度图的时间范围应用到中尺度图的timespans_fao
            mid_plotset = list(mid_graph.P.plotsets.P.values())[0]
            if hasattr(mid_plotset.P, 'timespans_fao') and mid_plotset.P.timespans_fao:
                # 动态设置中尺度图的时间范围
                mid_plotset_copy = mid_plotset({"timespans_fao.startDay": big_start, "timespans_fao.endDay": big_end})

        # 获取时间段
        with CurrTradeSet(context.sof), CurrIndustry(blk), CurrCalendar(calendar_name):
            if hasattr(mid_plotset_copy.P, 'timespans_fao') and mid_plotset_copy.P.timespans_fao:
                timespans = mid_plotset_copy.P.timespans_fao.timespans()
            else:
                raise ValueError("中尺度图必须指定timespans_fao")
                
        # 3. 遍历每个时间段，收集中尺度图和对应的小尺度图
        for i, timespan in enumerate(timespans):
            # 收集中尺度图
            mid_figs.append([])
            with CurrWidgets(mid_figs[i], live_ctrls, live_updaters, upd_btn, plot_roots=plot_roots) as widgets:
                # 动态设置中尺度图的时间段
                mid_graph_copy = mid_graph({
                    f"plotsets.{list(mid_graph.P.plotsets.P.keys())[0]}.timespans": [timespan],
                })
                mid_graph_copy.produce_widgets()
                
            # 收集小尺度图（如果存在）
            mul_small_figs.append([])
            if small_graph is not None:
                try:
                    with CurrWidgets(mul_small_figs[i], live_ctrls, live_updaters, upd_btn, plot_roots=plot_roots) as widgets:
                        # 动态设置小尺度图的时间段
                        small_plotset_key = list(small_graph.P.plotsets.P.keys())[0]
                        small_graph_copy = small_graph({
                            f"plotsets.{small_plotset_key}.timespans_fao.startDay": timespan[0],
                            f"plotsets.{small_plotset_key}.timespans_fao.endDay": timespan[1],
                        })
                        small_graph_copy.produce_widgets()
                except Exception as e:
                    # 异常处理：如果没有小尺度图，则对应位置为空列表
                    mul_small_figs[i] = []
                    
        # 4. 构建布局
        # 获取中尺度图的尺寸信息用于布局计算
        midscale_height = mid_graph.P.fig_height1 if hasattr(mid_graph.P, 'fig_height1') else 400
        big_width = big_graph.P.fig_width if hasattr(big_graph.P, 'fig_width') else 2400
        
        # 5. 每一列 = 中尺度图 + 小尺度图
        cols = []
        for mid_fig, small_figs in zip(mid_figs, mul_small_figs):
            # 中尺度图列
            mid_col = bkh.Column(children=mid_fig[0] if mid_fig else [])
            
            # 如果有小尺度图，加上滚动容器
            if small_figs:
                small_col = bkh.Column(children=[sf[0] for sf in small_figs])
                scrollable_small = ScrollBox(
                    child=small_col,
                    height=2 * midscale_height,
                    horizontal_scrollbar="hidden", 
                    vertical_scrollbar="auto"
                )
                cols.append(bkh.Column(children=[mid_col, scrollable_small]))
            else:
                cols.append(mid_col)
                
        # 6. 把所有列放到一个Row，并对整个Row做宽度限制
        mid_small_row = bkh.Row(children=cols)
        scrollable_mid_small = ScrollBox(
            child=mid_small_row,
            width=big_width,
            horizontal_scrollbar="auto",
            vertical_scrollbar="hidden"
        )
        
        # 7. 最终布局（按照CAEGraph的布局方式组织）
        items = []
        
        # 添加图表布局
        items.extend([
            big_layout,              # 大尺度图
            scrollable_mid_small,    # 中小尺度图（可横向滚动）
        ])
        
        # 添加更新按钮和控件（如果有的话）
        if live_ctrls:
            if upd_btn:
                items.append(upd_btn)
            items.extend(widget for _ctrl, widget in live_ctrls.values())
        return bkh.Column(children=items)
        
    def bkapp(self):
        """
        创建Bokeh应用，参照CAEGraph类的实现
        在notebook上画图的脚本: show(fig.bkapp(), notebook_url="http://192.168.11.152:8888")
        """
        def bkapp(doc):
            doc.add_root(self.layout())
        return bkapp