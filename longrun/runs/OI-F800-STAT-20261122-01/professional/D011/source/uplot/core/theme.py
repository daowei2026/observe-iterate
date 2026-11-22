# ====== add by king 2023-09-08 ======
# mquant.viewer.core.figure 已经过时，在未来的版本中将会删除，迁移了部分代码到此处

import abc
import pandas as pd
import numpy as np
from dataclasses import dataclass
from bokeh.models import CrosshairTool
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource

__all__ = ["DefaultFigTheme", "TBFigTheme"]


class FigTheme(abc.ABC):
    """
    King 2022-12-06 11:54

    绘图主题
    """

    @abc.abstractmethod
    def draw_kline(
        self,
        fig: figure,
        i: int,
        sym: str,
        sym_color: str,
        df: pd.DataFrame,
        source: ColumnDataSource,
    ):
        """
        King 2022-12-06 11:56

        绘制主图K线
        Params:
           fig: 主图Figure
           i: 品种序号
           sym: 品种名称
           sym_color: 品种颜色
           df: 品种数据
           source: 绘图需要的数据源ColumnDataSource
        """
        raise NotImplementedError

    @abc.abstractmethod
    def set_main_theme(self, fig: figure):
        """
        King 2022-12-06 11:58

        设置主图主题
        """
        pass

    @abc.abstractmethod    
    def set_sub_theme(self, fig: figure):
        """
        King 2022-12-06 11:58

        设置附图主题
        """
        pass


@dataclass
class DefaultFigTheme(FigTheme):
    """
    King 2022-12-06 11:58

    默认主题,蜡烛图颜色为每个品种的颜色，不能分别涨跌
    Params:
       background_fill_color: 背景颜色

    """

    background_fill_color: str = "white"

    def draw_kline(
        self,
        fig: figure,
        i: int,
        sym: str,
        sym_color: str,
        df: pd.DataFrame,
        source: ColumnDataSource,
    ):
        fig.segment(
            x0="x",
            y0="h",
            x1="x",
            y1="l",
            color=sym_color,
            source=source,
            legend_label=sym,
        )
        fig.rect(
            x="x",
            y="y",
            width=0.3,
            height="height",
            fill_color=sym_color,
            line_color=sym_color,
            line_width=0.01,
            name="bar",
            source=source,
            legend_label=sym,
        )

    def set_main_theme(self, fig: figure):
        fig.background_fill_color = self.background_fill_color
        #fig.legend.background_fill_alpha = 0.6
        fig.grid.grid_line_dash = [6, 4]
        fig.grid.grid_line_alpha = 0

    def set_sub_theme(self, fig: figure):
        fig.background_fill_color = self.background_fill_color
        #fig.legend.background_fill_alpha = 0.6
        fig.grid.grid_line_dash = [6, 4]
        fig.grid.grid_line_alpha = 0


    def create_cross_hair_tool(self):
        return CrosshairTool()


@dataclass
class TBFigTheme(FigTheme):
    """
    King 2022-12-06 11:59

    TB主题，黑色背景，虚线，蜡烛图颜色与TB类似
    """

    def draw_kline(
        self,
        fig: figure,
        i: int,
        sym: str,
        sym_color: str,
        df: pd.DataFrame,
        source: ColumnDataSource,
    ):
        # 第一个品种涨红跌绿
        # 其他品种统一的浅红浅绿
        is_first_sym = i == 0

        bcolor = np.full_like(df.open, "white", dtype="<U10")
        bcolor[df.close > df.open] = "red" if is_first_sym else "#806060"
        bcolor[df.close < df.open] = "lime" if is_first_sym else "#608060"

        source.add(data=bcolor, name="bcolor")

        fig.segment(
            x0="x",
            y0="h",
            x1="x",
            y1="l",
            color="white",
            source=source,
            legend_label=sym,
        )
        fig.rect(
            x="x",
            y="y",
            width=0.3,
            height="height",
            fill_color="bcolor",
            line_color="black",
            line_width=0.01,
            name="bar",
            source=source,
            legend_label=sym,
        )

    def set_main_theme(self, fig: figure):
        # 黑色背景 + 虚线
        fig.background_fill_color = "black"
        fig.grid.grid_line_dash = [6, 4]
        fig.grid.grid_line_alpha = 0.3
        fig.grid.band_fill_alpha = 0  # Disable band fill

    def set_sub_theme(self, fig: figure):
        fig.background_fill_color = "black"
        fig.grid.grid_line_dash = [6, 4]
        fig.grid.grid_line_alpha = 0.3
        fig.grid.band_fill_alpha = 0  # Disable band fill

    def create_cross_hair_tool(self):
        return CrosshairTool(line_color="white")
