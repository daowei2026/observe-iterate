"""
Unified Time Plotting Kit Version 2

"""

__all__ = [
    "BaseFigSet",
    "OneFig",
    "MainFig",
    "SubFig",
    "AllSymsFig",
    "AllSymsMainFig",
    "PerSymFigs",
    "PerSymFigSet",
    "SpecSymsFigs",
    "SpecSymsFigSet",
    "FigCtrls",
    "SpecEntitiesFig",
    "SpecEntitiesMainFig",
]

import itertools
import traceback
from typing import *

import numpy as np
import pandas as pd
from numba import njit

import os

from m3 import *
from m3v import *

from mquant.frame import *
from mquant.frame.lib3 import *

from mquant.tis.t0.gen.cc import *

from .core import *
from .pfw import *


class BaseFigSet(DoFunctionFao):
    """
    图集基类

    """

    params = lambda: dict(
        title=None,
        fig_width=None,  # 图宽
        fig_height=None,  # 图高
        show_legend=True,  # 显示图例
        legend_alpha=1,  # 图例（不）透明度
        legend_size=10,  # 图例（单项）尺寸
        legend_location="top_right",
        hover=True,
        static_dynstd=False,  # 动态标准化数据进行静态处理，节省浏览器端计算，更快看到图
        fit_y_range=True,  # 自适应 y 轴显示范围，但有动态标准化内容的话则失效
        colors2=None,  # 两级色板
        nb_fig_time_range=True,  # 将 fig 显示的 x 轴时间范围记录到 notebook 全局变量
        log_y=False
    )

    def plot_figs(self, ctx: PlotCtx):
        raise NotImplementedError()

    def _title(self, ctx: PlotCtx):
        title = self.P.title
        if isinstance(title, str) and title.startswith("!"):
            return title[1:].format(
                sym=CurrSymbol.sym(False) or "",
                n_syms=len(ctx.all_symbols),
                **{f"span_info{i}": s for i, s in enumerate(ctx.span_info)},
                # TODO: support more vars
            )
        return title or ctx.plot_folder.name

    def _fig_height(self, ctx: PlotCtx):
        return self.P.fig_height or ctx.gps.fig_height

    def _set_theme(self, ctx, fig):
        ctx.gps.theme.set_sub_theme(fig)

    def _create_fig(self, ctx: PlotCtx):
        gps = ctx.gps

        fig = figure(
            **(dict(x_range=ctx.x_range) if ctx.x_range else {}),
            title=self._title(ctx),
            tools=[
                "xwheel_zoom",
                "ywheel_zoom",
                "pan",
                # "crosshair",
                "box_zoom",
                "undo",
                "redo",
                "reset",
            ],
            width=self.P.fig_width or gps.fig_width,
            height=self._fig_height(ctx),
            y_axis_type="log" if self.P.log_y else "linear"
        )
        self._set_theme(ctx, fig)

        labels = ctx.x_labels
        fig.xaxis.ticker = bkh.FixedTicker(ticks=list(labels.keys()))
        fig.xaxis.major_label_overrides = labels
        fig.xaxis.major_label_policy = bkh.NoOverlap()
        fig.xaxis.major_label_orientation = 0

        # crossHairTool = gps.theme.create_cross_hair_tool()
        # fig.add_tools(crossHairTool)
        ctx.figs.append(fig)
        if not ctx.x_range:
            ctx.x_range = fig.x_range

    def _finish_fig(self, ctx: PlotCtx):
        from IPython import get_ipython

        fig = ctx.figs[-1]
        fxr = fig.x_range

        if self.P.nb_fig_time_range:
            ipy = get_ipython()
            if ipy:  # 不在 nb 环境时跳过
                ipy_ns = ipy.user_ns

                def upd_xr(attr, old, new):
                    trd = ipy_ns.get("fig_time_range")
                    if trd is None:
                        ipy_ns["fig_time_range"] = trd = {}
                    trd[fig.title.text] = ctx.x_range_ts(fxr)

                fxr.on_change("start", upd_xr)
                fxr.on_change("end", upd_xr)

        if self.P.show_legend and len(fig.legend):
            fig.legend.location = self.P.legend_location
            fig.legend.click_policy = "hide"
            fig.legend.background_fill_alpha = self.P.legend_alpha / 2
            fig.legend.label_text_alpha = self.P.legend_alpha

            fig.legend.glyph_height = fig.legend.glyph_width = self.P.legend_size
            fig.legend.label_height = fig.legend.label_width = self.P.legend_size
            fig.legend.label_text_font_size = f"{self.P.legend_size}px"
        else:
            fig.legend.visible = False

        if ctx.y_fits:
            y_fits = ctx.y_fits
            ctx.y_fits = []
            if self.P.fit_y_range and not ctx.dynstd_list:
                # 如果有动态标准化内容则不自适应 y 轴
                with open(f"{os.path.dirname(__file__)}/fit_y_range.js", "r") as jsf:
                    fit_y_range_js = jsf.read()
                jsh = bkh.CustomJS(
                    args=dict(
                        fig=fig,
                        y_fits=y_fits,
                    ),
                    code=fit_y_range_js,
                )
                fxr.js_on_change("start", jsh)
                fxr.js_on_change("end", jsh)

        if self.P.static_dynstd:
            ctx.realize_static_dynstd()
        else:
            ctx.realize_dynstd()

        if self.P.hover:
            ctx.realize_hovers(fig)


class OneFig(BaseFigSet):
    """
    单图集基类

    """

    params = lambda: dict(
        plots=GMap(),  # 每张图上都画的内容
    )

    # 默认画单图，不做品种循环，不设品种上下文
    def plot_figs(self, ctx: PlotCtx):
        gps = ctx.gps

        self._create_fig(ctx)
        for _plot_folder in ctx.push_folder(
            f"{__class__.__name__}: {ctx.figs[-1].title.text}"
        ):
            for fpk, fp in self.P.plots.P.items():
                if not gps.switches.get(fpk, True):
                    continue
                fp._plot_fig(ctx)
        self._finish_fig(ctx)


class MainFig(OneFig):
    """
    单主图

    """

    params = lambda: dict(title="!{sym} - 主图")

    def _fig_height(self, ctx: PlotCtx):
        return self.P.fig_height or ctx.gps.fig_height1

    def _set_theme(self, ctx, fig):
        ctx.gps.theme.set_main_theme(fig)


class SubFig(OneFig):
    """
    单附图

    """

    params = lambda: dict(title="!{sym} - 附图")


class AllSymsFig(OneFig):
    """
    多品种单图

    """

    params = lambda: dict(
        title="!{n_syms} 品种图",
        sym_plots=GMap(),  # 每张图上都画，map key 解释为品种 id
        persym_plots=GMap(),  # 每张图上都画，且对每个品种各画一次的内容
        blk_as_1st_sym=False,  # 是否将板块当做第一个品种
    )

    def plot_figs(self, ctx: PlotCtx):
        gps = ctx.gps

        all_symbols = ctx.all_symbols
        if self.P.blk_as_1st_sym:
            all_symbols = [CurrIndustry.blk_expr(True), *all_symbols]

        self._create_fig(ctx)
        for _plot_folder in ctx.push_folder(
            f"{__class__.__name__}: {ctx.figs[-1].title.text}"
        ):
            for i, ((sym, plots), colors) in enumerate(
                zip(
                    self.P.sym_plots.items(),
                    itertools.cycle(self.P.colors2 or gps.colors2),
                )
            ):
                with CurrSymbol(sym, seq=i), CurrScope(), CurrSymbolPable(sym):
                    ctx.sym_color = colors[0]
                    ctx.sym_colors = iter(itertools.cycle(colors[1:]))
                    for _plot_folder in ctx.push_folder(f"sym: {sym}"):
                        for fpk, fp in plots.items():
                            if not gps.switches.get(fpk, True):
                                continue
                            fp._plot_fig(ctx)
            for fpk, fp in self.P.persym_plots.P.items():
                if not gps.switches.get(fpk, True):
                    continue
                for i, (sym, colors) in enumerate(
                    zip(all_symbols, itertools.cycle(gps.colors2))
                ):
                    with CurrSymbol(sym, seq=i), CurrScope(), CurrSymbolPable(sym):
                        ctx.sym_color = colors[0]
                        ctx.sym_colors = iter(itertools.cycle(colors[1:]))
                        for _plot_folder in ctx.push_folder(f"sym: {sym}"):
                            fp._plot_fig(ctx)
            for fpk, fp in self.P.plots.P.items():
                if not gps.switches.get(fpk, True):
                    continue
                fp._plot_fig(ctx)
        self._finish_fig(ctx)


class AllSymsMainFig(AllSymsFig, MainFig):
    """
    多品种单主图

    """


class PerSymFigs(BaseFigSet):
    """
    每品种一个图的多图集

    """

    params = lambda: dict(
        title="!{sym} - 图",
        plots=GMap(),  # 每个品种逐个要画的内容
        live_ctrls_persym=False,  # 每个品种之后显示拖动控件
        blk_as_1st_sym=False,  # 是否将板块当做第一个品种
    )

    def plot_figs(self, ctx: PlotCtx):
        gps = ctx.gps
        plots = self.P.plots

        all_symbols = ctx.all_symbols
        if self.P.blk_as_1st_sym:
            all_symbols = [CurrIndustry.blk_expr(True), *all_symbols]

        for _plot_folder in ctx.push_folder(__class__.__name__):
            for i, (sym, colors) in enumerate(
                zip(
                    all_symbols,
                    itertools.cycle(self.P.colors2 or gps.colors2),
                )
            ):
                with CurrSymbol(sym, seq=i), CurrScope(), CurrSymbolPable(sym):
                    ctx.sym_color = colors[0]
                    ctx.sym_colors = iter(itertools.cycle(colors[1:]))
                    self._create_fig(ctx)
                    for _plot_folder in ctx.push_folder(
                        f"sym: {sym} - {ctx.figs[-1].title.text}"
                    ):
                        for fpk, fp in plots.P.items():
                            if not gps.switches.get(fpk, True):
                                continue
                            assert isinstance(fp, BasePlotter)
                            fp._plot_fig(ctx)
                    self._finish_fig(ctx)

                    if self.P.live_ctrls_persym:
                        ctx.show_live_ctrls()


class PerSymFigSet(BaseFigSet):
    """
    每品种一套图的多图集

    """

    params = lambda: dict(
        title="!{sym} - 图",
        figs=GMap(),  # 每个品种逐个要画的图集
        live_ctrls_persym=False,  # 每个品种之后显示拖动控件
    )

    def plot_figs(self, ctx: PlotCtx):
        gps = ctx.gps

        for _plot_folder in ctx.push_folder(__class__.__name__):
            for i, (sym, colors) in enumerate(
                zip(
                    ctx.all_symbols,
                    itertools.cycle(self.P.colors2 or gps.colors2),
                )
            ):
                with CurrSymbol(sym, seq=i), CurrScope(), CurrSymbolPable(sym):
                    ctx.sym_color = colors[0]
                    ctx.sym_colors = iter(itertools.cycle(colors[1:]))
                    for _plot_folder in ctx.push_folder(f"sym: {sym}"):
                        for fk, fs in self.P.figs.P.items():
                            if not gps.switches.get(fk, True):
                                continue
                            if isinstance(fs, OneFig):
                                fs.plot_figs(ctx)
                            else:
                                raise TypeError(f"Unsupported fig set type: {type(fs)}")

            if self.P.live_ctrls_persym:
                ctx.show_live_ctrls()


class SpecSymsFigs(BaseFigSet):
    """
    指定品种列表，每品种一个图的多图集

    """

    params = lambda: dict(
        syms=[],  # 指定品种列表
        title="!{sym} - 图",
        plots=GMap(),  # 每个品种逐个要画的内容
        live_ctrls_persym=False,  # 每个品种之后显示拖动控件
    )

    def plot_figs(self, ctx: PlotCtx):
        gps = ctx.gps
        plots = self.P.plots

        for _plot_folder in ctx.push_folder(__class__.__name__):
            for i, (sym, colors) in enumerate(
                zip(
                    self.P.syms,
                    itertools.cycle(self.P.colors2 or gps.colors2),
                )
            ):
                with CurrSymbol(sym, seq=i), CurrScope(), CurrSymbolPable(sym):
                    ctx.sym_color = colors[0]
                    ctx.sym_colors = iter(itertools.cycle(colors[1:]))
                    self._create_fig(ctx)
                    for _plot_folder in ctx.push_folder(
                        f"sym: {sym} - {ctx.figs[-1].title.text}"
                    ):
                        for fpk, fp in plots.P.items():
                            if not gps.switches.get(fpk, True):
                                continue
                            assert isinstance(fp, BasePlotter)
                            fp._plot_fig(ctx)
                    self._finish_fig(ctx)

                    if self.P.live_ctrls_persym:
                        ctx.show_live_ctrls()


class SpecSymsFigSet(BaseFigSet):
    """
    指定品种列表，每品种一套图的多图集

    """

    params = lambda: dict(
        syms=[],  # 指定品种列表
        title="!{sym} - 图",
        figs=GMap(),  # 每个品种逐个要画的图集
        live_ctrls_persym=False,  # 每个品种之后显示拖动控件
    )

    def plot_figs(self, ctx: PlotCtx):
        gps = ctx.gps

        for _plot_folder in ctx.push_folder(__class__.__name__):
            for i, (sym, colors) in enumerate(
                zip(
                    self.P.syms,
                    itertools.cycle(self.P.colors2 or gps.colors2),
                )
            ):
                with CurrSymbol(sym, seq=i), CurrScope(), CurrSymbolPable(sym):
                    ctx.sym_color = colors[0]
                    ctx.sym_colors = iter(itertools.cycle(colors[1:]))
                    for _plot_folder in ctx.push_folder(f"sym: {sym}"):
                        for fk, fs in self.P.figs.P.items():
                            if not gps.switches.get(fk, True):
                                continue
                            if isinstance(fs, OneFig):
                                fs.plot_figs(ctx)
                            else:
                                raise TypeError(f"Unsupported fig set type: {type(fs)}")

            if self.P.live_ctrls_persym:
                ctx.show_live_ctrls()


class FigCtrls(BaseFigSet):
    """
    动态参数控件

    """

    def plot_figs(self, ctx: PlotCtx):
        ctx.show_live_ctrls()


class SpecEntitiesFig(OneFig):
    """
    多标的单图

    """

    params = lambda: dict(
        title="多标的图",
        entity_plots=GMap(),  # 每张图上都画，map key 解释为标的 id
    )

    def plot_figs(self, ctx: PlotCtx):
        sof = ctx.sof
        gps = ctx.gps

        self._create_fig(ctx)
        for _plot_folder in ctx.push_folder(
            f"{__class__.__name__}: {ctx.figs[-1].title.text}"
        ):
            colors_iter = iter(itertools.cycle(self.P.colors2 or gps.colors2))
            for tgtx, plots in self.P.entity_plots.items():
                if tgtx.startswith("syms!"):
                    all_symbols = BlockTarType.from_expr(tgtx[5:]).symbols()
                    for i, sym in enumerate(all_symbols):
                        with CurrSymbol(sym, seq=i), CurrScope(), CurrSymbolPable(sym):
                            colors = next(colors_iter)
                            ctx.sym_color = colors[0]
                            ctx.sym_colors = iter(itertools.cycle(colors[1:]))
                            for _plot_folder in ctx.push_folder(f"sym: {sym}"):
                                for fpk, fp in plots.items():
                                    if not gps.switches.get(fpk, True):
                                        continue
                                    fp._plot_fig(ctx)
                elif tgtx.startswith("blk!"):
                    with CurrIndustry(tgtx[4:]):
                        colors = next(colors_iter)
                        ctx.sym_color = colors[0]
                        ctx.sym_colors = iter(itertools.cycle(colors[1:]))
                        for fpk, fp in plots.items():
                            if not gps.switches.get(fpk, True):
                                continue
                            fp._plot_fig(ctx)
                elif tgtx.startswith("blks!") or tgtx.startswith("blksyms!"):
                    all_blks = sof.resolve_hierarchical_block(tgtx[5:])
                    for blk in all_blks:
                        with CurrIndustry(blk):
                            colors = next(colors_iter)
                            ctx.sym_color = colors[0]
                            ctx.sym_colors = iter(itertools.cycle(colors[1:]))
                            for fpk, fp in plots.items():
                                if not gps.switches.get(fpk, True):
                                    continue
                                fp._plot_fig(ctx)
                elif "@" in tgtx:
                    blk = tgtx
                    with CurrIndustry(blk):
                        colors = next(colors_iter)
                        ctx.sym_color = colors[0]
                        ctx.sym_colors = iter(itertools.cycle(colors[1:]))
                        for fpk, fp in plots.items():
                            if not gps.switches.get(fpk, True):
                                continue
                            fp._plot_fig(ctx)
                else:
                    sym = tgtx
                    with CurrSymbol(sym), CurrScope(), CurrSymbolPable(sym):
                        colors = next(colors_iter)
                        ctx.sym_color = colors[0]
                        ctx.sym_colors = iter(itertools.cycle(colors[1:]))
                        for fpk, fp in plots.items():
                            if not gps.switches.get(fpk, True):
                                continue
                            fp._plot_fig(ctx)

        self._finish_fig(ctx)


class SpecEntitiesMainFig(SpecEntitiesFig, MainFig):
    """
    多标的单主图

    """
