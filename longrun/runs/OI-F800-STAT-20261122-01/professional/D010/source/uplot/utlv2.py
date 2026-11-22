"""
Unified Time Plotting Library Version 2

"""

__all__ = [
    "SegsPlot",
    "VBarPlot",
    "TickPriceLine",
    "KPriceLine",
    "MulUtiPointPlot",
    "ExtractEntityTimespans",
    "ExtractTimespans",
    "PerDPTimespans",
    "BaseNextProcessPlot",
    "MulSegPlot",
    "StrasTradePlot",
    "MulFieldsGlyphs",
    "CAEGraph",
    "PlotSet",
    "MulPointPlot",
    "OneToGroupPointPlot",
    "SeqOfFieldsPlot",
    "TextPlot",
    "DynamicGlyphPlot",
    "ObjsClustersPlot",
    "DynamicColorPlot",
]

from typing import *
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


def currTarget():
    sym = CurrSymbol.sym(False)
    if sym is not None:
        return sym
    blk = CurrIndustry.blk_expr(False)
    if blk is not None:
        return blk[4:] if blk.startswith("blk@") else blk
    return None


class SegsPlot(BasePlotter):
    """ """

    params = lambda: dict(
        feat=Nothing,  # 特征
        df_key="dseg_buy",
        uti1_field="data_uti1",  # 时间字段名
        uti2_field="data_uti2",  # 时间字段名
        y1_field="data_price1",  # y 值字段名
        y2_field="data_price2",  # y 值字段名
        color="black",  # 颜色
        alpha=0.8,  # 透明度
        line_width=5,  # 线宽
        label=None,  # 图例  None为默认值:代表不需要图例
    )

    def _plot_fig(self, ctx: PlotCtx):
        gps = ctx.gps
        fig = ctx.figs[-1]

        label = self.P.label or "线段"

        cds = ctx.live_feat_data(
            f"segment({__class__.__name__})",
            lambda df: {
                "x0": df[self.P.uti1_field].values,
                "x1": df[self.P.uti2_field].values,
                "y0": df[self.P.y1_field].values,
                "y1": df[self.P.y2_field].values,
            },
            self.P.feat,
            self.P.df_key,
            self.P.uti1_field,
            self.P.uti2_field,
        )

        ctx.add_hover(
            fig.segment(
                source=cds,
                color=self.P.color,
                alpha=self.P.alpha,
                line_width=self.P.line_width,
                legend_label=label,
                name=label,
            ),
            (label, "@y0 ~ @y1"),
        )

        ctx.fit_ys(cds, "x0", "y0")
        ctx.fit_ys(cds, "x1", "y1")


class VBarPlot(BasePlotter):
    """ """

    params = lambda: dict(
        feat=Nothing,  # 特征
        df_key="hd_buy",
        uti_field="uti",  # 时间字段名
        top_field="grade",  # top 字段名
        top_coeff=1,  # top 数据系数
        symseq_yshift=None,  # 按 CurrSymbol.seq() 在纵轴偏移，指定大于 0 的数字作为每品种偏移量， bottom 参数将失效
        bottom=0,  # bottom 值
        color="black",  # 颜色
        alpha=0.8,  # 透明度
        width=0.5,  # Bar 宽
        label=None,  # 图例  None为默认值:代表不需要图例
        hover_tslabel=True,  # 是否在浮标中显示时间戳
    )

    def _plot_fig(self, ctx: PlotCtx):
        gps = ctx.gps
        fig = ctx.figs[-1]

        label = self.P.label or "柱图"
        hover_tslabel = self.P.hover_tslabel

        bottom = self.P.bottom
        if self.P.symseq_yshift:
            bottom = CurrSymbol.seq() * self.P.symseq_yshift

        def fd_trans(df):
            fd = {
                "x": df[self.P.uti_field].values,
                "top": df[self.P.top_field].values * self.P.top_coeff,
            }
            if self.P.symseq_yshift:
                fd["top"] += bottom
            if hover_tslabel:
                fd["ts"] = ctx.uti2tslabel(df[self.P.uti_field].values)
            return fd

        cds = ctx.live_feat_data(
            f"vbar({__class__.__name__})",
            fd_trans,
            self.P.feat,
            self.P.df_key,
            self.P.uti_field,
        )

        ctx.add_hover(
            fig.vbar(
                source=cds,
                bottom=bottom,
                color=self.P.color or ctx.sym_color,
                alpha=self.P.alpha,
                width=self.P.width,
                legend_label=self.P.label,
            ),
            (label, "@ts @top" if hover_tslabel else "@top"),
        )

        ctx.fit_ys(cds, "x", "top")


class MulUtiPointPlot(BasePlotter):
    """
    Author: cyue
    Since : 2024-11-27
    Desc  :
       - 指定要画的多个图,多个图的多个特征字段的来源为单个特征的不同品种
    Params:
        glyphs: 形状
        feats: 特征
        dfkeys: 特征数据中取 DataFrame 的键值
        legend_labels: 图例
            None为默认值,None代表使用品种名,也可以直接给列表
        colors: 颜色
            None 则使用品种颜色，也可以直接给列表
        xfields: 横轴时间字段名
            None 则使用 df 索引时间
        yfields: 纵轴数值字段名
        size_fields: 通过特征值指定图形大小
        size_scale 图形大小的放大倍率
        size_base: 基础大小（防止过小的数据画了却看不到）
        size: 大小
        alphas: 透明度
        hover: 浮标
            默认为True,代表使用品种名;False代表不加浮标
    """

    params = lambda: dict(
        glyphs="asterisk",
        feats=Nothing,
        dfkeys=None,
        legend_labels=None,
        colors=[None],
        xfields=[None],
        yfields=[],
        size_fields=None,
        size_scale=100,
        size_base=5,
        size=5,
        alphas=0.6,
        hover=True,
    )

    def _plot_fig(self, ctx: PlotCtx):
        gps = ctx.gps
        fig = ctx.figs[-1]

        sym = CurrSymbol.sym()
        tgt = currTarget()

        # from IPython import get_ipython

        # ipy_ns = get_ipython().user_ns
        # ipy_ns.update(locals())

        for (
            feat,
            dfk,
            xfield,
            yfield,
            size_field,
            glyph,
            label,
            color,
            alpha,
        ) in zip(
            (
                self.feats.make_arr()
                if isinstance(self.P.feats, GMap)
                else itertools.repeat(self.feats)
            ),
            itertools.cycle(ensure_list(self.P.dfkeys)),
            itertools.cycle(ensure_list(self.P.xfields)),
            ensure_list(self.P.yfields),
            itertools.cycle(ensure_list(self.P.size_fields)),
            itertools.cycle(ensure_list(self.P.glyphs)),
            itertools.cycle(ensure_list(self.P.legend_labels)),
            itertools.cycle(self.P.colors),
            itertools.cycle(ensure_list(self.P.alphas)),
        ):

            # 有些参数给了必须是有效值,通过这个字典实现默认情况下不给参数
            glyph_args = {}
            if label is not None:
                legend_label = f"{tgt} - {label}"
                glyph_args["legend_label"] = legend_label
                glyph_args["name"] = legend_label
            else:
                legend_label = f"{tgt} - 值"
            if glyph != "line":
                glyph_args["size"] = self.P.size

            def fd_trans(df):
                fd = {"x": df[xfield], "y": df[yfield]}
                if size_field:
                    sd = df[size_field]
                    fd["size"] = scale_size(sd, self.P.size_base, self.P.size_scale)
                    glyph_args["size"] = "size"
                return fd

            cds = ctx.feat_data(
                f"scatter/{glyph}({__class__.__name__})", fd_trans, feat, dfk, xfield
            )

            ctx.add_hover(
                fig.scatter(
                    marker=glyph,
                    source=cds,
                    color=color or ctx.sym_color,
                    alpha=alpha,
                    **glyph_args,
                ),
                (legend_label, "@y"),
            )

            ctx.drive_entity_dynstd(cds)

            ctx.fit_ys(cds)


class ExtractTimespans(DoFunctionFao):

    class Meta:
        on_pable = True

    params = lambda: dict(
        uti2ts=False,  # True 则将 uti 转换为自然时间戳再输出； False 不转换
        feats=GMap(),  # 特征列表
        dfkeys=None,  # 特征数据中 df 的名字
        dffilters=[lambda df: df],  # 特征数据 df 过滤函数
        utifields=[
            ["uti"]
        ],  # 特征 df 中统一时间轴下标的字段名，每个特征 df 可以取多个时间字段
        symbollist=[],  # 提取特征数据的品种代码列表
        startDay="2024-01-01",  # 特征数据截取时间段的开始时间
        endDay="2024-02-28",  # 特征数据截取时间段的结束时间
        n_inter=7200 * 10,  # 单段内最大间隔半秒数
        n_margin=7200,  # 结果时间段两端的额外半秒数
        n_max=7200 * 20,  # 单段最多半秒数
        max_spans=100,  # 最多返回的段数（超过的丢弃）
        time_format="%Y-%m-%d %H:%M:%S",  # 时间格式字符串
    )

    def timespans(self):
        clip_by_uti = False
        try:
            start_uti = int(self.P.startDay)
            end_uti = int(self.P.endDay)
            clip_by_uti = True
        except ValueError:
            pass

        utias = []
        if isinstance(self.P.symbollist, list):
            syms = self.P.symbollist
        else:
            syms = BlockTarType.from_expr(self.P.symbollist).symbols()
        for sym in syms:
            with CurrSymbol(sym), CurrSymbolPable(sym):
                for _, feat, dfkey, dffilter, utifn in zip(
                    range(
                        max(
                            len(self.feats) if isinstance(self.P.feats, GMap) else 1,
                            (
                                len(self.P.dfkeys)
                                if isinstance(self.P.dfkeys, list)
                                else 1
                            ),
                            (
                                len(self.P.utifields)
                                if isinstance(self.P.utifields, list)
                                else 1
                            ),
                        )
                    ),
                    (
                        self.feats.make_arr()
                        if isinstance(self.P.feats, GMap)
                        else itertools.repeat(self.feats)
                    ),
                    itertools.cycle(ensure_list(self.P.dfkeys)),
                    itertools.cycle(self.P.dffilters),
                    itertools.cycle(ensure_list(self.P.utifields)),
                ):
                    if dfkey:
                        df = feat.rerun().to_dfs()[dfkey]
                    else:
                        df = feat.rerun().to_df()
                    df = dffilter(df)
                    if clip_by_uti:
                        for fn in utifn:
                            utis = df[fn]
                            start_i, end_i = np.searchsorted(utis, [start_uti, end_uti])
                            utias.append(utis[start_i:end_i])
                    else:
                        df = df[self.P.startDay : self.P.endDay]
                        for fn in utifn:
                            utias.append(df[fn])
        if len(union_uti_series(*utias)) == 0:
            print(f"union of utias is empty, maybe feats have no occurrence during startDay: {self.P.startDay}, endDay: {self.P.endDay}")
            return []
        uti_segs = identify_uti_segments(
            *utias,
            n_inter=self.P.n_inter,
            n_margin=self.P.n_margin,
            n_max=self.P.n_max,
        )[: self.P.max_spans]
        sof = CurrTradeSet.sof()
        full_tsa = sof.tsa_of(CurrCalendar.name())["natural_tsa"]
        dt_segs = [pd.to_datetime(full_tsa[[ds, de]]) for (ds, de) in uti_segs]
        if self.P.uti2ts:
            return [
                (
                    dt_s,
                    dt_e,
                    f"{dt_s.strftime(self.P.time_format)} ~ {dt_e.strftime(self.P.time_format)}",
                )
                for (dt_s, dt_e) in dt_segs
            ]
        return [
            (
                ds,
                de,
                f"{dt_s.strftime(self.P.time_format)} ~ {dt_e.strftime(self.P.time_format)}",
            )
            for ((ds, de), (dt_s, dt_e)) in zip(uti_segs, dt_segs)
        ]


class ExtractEntityTimespans(DoFunctionFao):

    class Meta:
        on_pable = True

    params = lambda: dict(
        uti2ts=False,  # True 则将 uti 转换为自然时间戳再输出； False 不转换
        entity_feats=GMap(),  # 特征列表
        dfkeys=None,  # 特征数据中 df 的名字
        dffilters=[lambda df: df],  # 特征数据 df 过滤函数
        utifields=[
            ["uti"]
        ],  # 特征 df 中统一时间轴下标的字段名，每个特征 df 可以取多个时间字段
        startDay="2024-01-01",  # 特征数据截取时间段的开始时间
        endDay="2024-02-28",  # 特征数据截取时间段的结束时间
        n_inter=7200 * 10,  # 单段内最大间隔半秒数
        n_margin=7200,  # 结果时间段两端的额外半秒数
        n_max=7200 * 20,  # 单段最多半秒数
        max_spans=100,  # 最多返回的段数（超过的丢弃）
        time_format="%Y-%m-%d %H:%M:%S",  # 时间格式字符串
    )

    def timespans(self):
        sof = CurrTradeSet.sof(True)

        clip_by_uti = False
        try:
            start_uti = int(self.P.startDay)
            end_uti = int(self.P.endDay)
            clip_by_uti = True
        except ValueError:
            pass

        utias = []
        dfkeys_iter, dffilters_iter, utifields_iter = (
            itertools.cycle(ensure_list(self.P.dfkeys)),
            itertools.cycle(self.P.dffilters),
            itertools.cycle(ensure_list(self.P.utifields)),
        )

        def extract_feat_data(feat):
            dfkey = next(dfkeys_iter)
            dffilter = next(dffilters_iter)
            utifn = next(utifields_iter)
            if dfkey:
                df = feat.rerun().to_dfs()[dfkey]
            else:
                df = feat.rerun().to_df()
            df = dffilter(df)
            if clip_by_uti:
                for fn in utifn:
                    utis = df[fn]
                    start_i, end_i = np.searchsorted(utis, [start_uti, end_uti])
                    utias.append(utis[start_i:end_i])
            else:
                df = df[self.P.startDay : self.P.endDay]
                for fn in utifn:
                    utias.append(df[fn])

        for tgtx, feats in self.P.entity_feats.items():
            if tgtx.startswith("syms!"):
                all_symbols = BlockTarType.from_expr(tgtx[5:]).symbols()
                for i, sym in enumerate(all_symbols):
                    with CurrSymbol(sym, seq=i), CurrScope(), CurrSymbolPable(sym):
                        for feat in feats.values():
                            extract_feat_data(feat)
            elif tgtx.startswith("blk!"):
                with CurrIndustry(tgtx[4:]):
                    for feat in feats.values():
                        extract_feat_data(feat)
            elif tgtx.startswith("blks!") or tgtx.startswith("blksyms!"):
                all_blks = sof.resolve_hierarchical_block(tgtx[5:])
                for blk in all_blks:
                    with CurrIndustry(blk):
                        for feat in feats.values():
                            extract_feat_data(feat)
            elif "@" in tgtx:
                blk = tgtx
                with CurrIndustry(blk):
                    for feat in feats.values():
                        extract_feat_data(feat)
            else:
                sym = tgtx
                with CurrSymbol(sym), CurrScope(), CurrSymbolPable(sym):
                    for feat in feats.values():
                        extract_feat_data(feat)

        if len(union_uti_series(*utias)) == 0:
            print(f"union of utias is empty, maybe feats have no occurrence during startDay: {self.P.startDay}, endDay: {self.P.endDay}")
            return []
        uti_segs = identify_uti_segments(
            *utias,
            n_inter=self.P.n_inter,
            n_margin=self.P.n_margin,
            n_max=self.P.n_max,
        )[: self.P.max_spans]
        sof = CurrTradeSet.sof()
        full_tsa = sof.tsa_of(CurrCalendar.name())["natural_tsa"]
        dt_segs = [pd.to_datetime(full_tsa[[ds, de]]) for (ds, de) in uti_segs]
        if self.P.uti2ts:
            return [
                (
                    dt_s,
                    dt_e,
                    f"{dt_s.strftime(self.P.time_format)} ~ {dt_e.strftime(self.P.time_format)}",
                )
                for (dt_s, dt_e) in dt_segs
            ]
        return [
            (
                ds,
                de,
                f"{dt_s.strftime(self.P.time_format)} ~ {dt_e.strftime(self.P.time_format)}",
            )
            for ((ds, de), (dt_s, dt_e)) in zip(uti_segs, dt_segs)
        ]


class PerDPTimespans(DoFunctionFao):

    class Meta:
        on_pable = True

    params = lambda: dict(
        uti2ts=False,  # True 则将 uti 转换为自然时间戳再输出； False 不转换
        feats=GMap(),  # 特征列表
        dfkeys=None,  # 特征数据中 df 的名字
        dffilters=[lambda df: df],  # 特征数据 df 过滤函数
        utifields=[
            ["uti"]
        ],  # 特征 df 中统一时间轴下标的字段名，每个特征 df 可以取多个时间字段
        symbollist=[],  # 提取特征数据的品种代码列表
        startDay="2024-01-01",  # 特征数据截取时间段的开始时间
        endDay="2024-02-28",  # 特征数据截取时间段的结束时间
        n_margin=7200,  # 结果时间段两端的额外半秒数
        max_spans=100,  # 最多返回的段数（超过的丢弃）
        time_format="%Y-%m-%d %H:%M:%S",  # 时间格式字符串
    )

    def timespans(self):
        clip_by_uti = False
        try:
            start_uti = int(self.P.startDay)
            end_uti = int(self.P.endDay)
            clip_by_uti = True
        except ValueError:
            pass

        utias = []
        if isinstance(self.P.symbollist, list):
            syms = self.P.symbollist
        else:
            syms = BlockTarType.from_expr(self.P.symbollist).symbols()
        for sym in syms:
            with CurrSymbol(sym), CurrSymbolPable(sym):
                for _, feat, dfkey, dffilter, utifn in zip(
                    range(
                        max(
                            len(self.feats) if isinstance(self.P.feats, GMap) else 1,
                            (
                                len(self.P.dfkeys)
                                if isinstance(self.P.dfkeys, list)
                                else 1
                            ),
                            (
                                len(self.P.utifields)
                                if isinstance(self.P.utifields, list)
                                else 1
                            ),
                        )
                    ),
                    (
                        self.feats.make_arr()
                        if isinstance(self.P.feats, GMap)
                        else itertools.repeat(self.feats)
                    ),
                    itertools.cycle(ensure_list(self.P.dfkeys)),
                    itertools.cycle(self.P.dffilters),
                    itertools.cycle(ensure_list(self.P.utifields)),
                ):
                    if dfkey:
                        df = feat.rerun().to_dfs()[dfkey]
                    else:
                        df = feat.rerun().to_df()
                    df = dffilter(df)
                    if clip_by_uti:
                        for fn in utifn:
                            utis = df[fn]
                            start_i, end_i = np.searchsorted(utis, [start_uti, end_uti])
                            utias.append(utis[start_i:end_i])
                    else:
                        df = df[self.P.startDay : self.P.endDay]
                        for fn in utifn:
                            utias.append(df[fn])
        sof = CurrTradeSet.sof()
        full_tsa = sof.tsa_of(CurrCalendar.name())["natural_tsa"]
        utis = union_uti_series(*utias)
        segs = [
            (
                uti - self.P.n_margin,
                uti + self.P.n_margin,
                pd.to_datetime(full_tsa[uti]).strftime(self.P.time_format),
            )
            for uti in utis
        ][: self.P.max_spans]
        if self.P.uti2ts:
            return [
                (*pd.to_datetime(full_tsa[[ds, de]]), tp_str)
                for (ds, de, tp_str) in segs
            ]
        return segs


class KPriceLine(BasePlotter):
    """
    统一时间轴 K 线

    """

    params = lambda: dict(
        std_method=None,
        feat=KLine(),
        extra_bars=0,  # 额外多画这么多个 bar
        add_hover=True,
        color=None,
        alpha=0.8,  # 透明度
        label="K",
        NextProcess=UnFree(
            Nothing
        ),  # 对 figure 进一步加工，如绑定各种事件等, add by king 2015-03-17
    )

    def _plot_fig(self, ctx: PlotCtx):
        gps = ctx.gps
        fig = ctx.figs[-1]

        tgt = currTarget()
        if tgt is None:
            legend_label = self.P.label
        else:
            tgt = tgt[4:] if tgt.startswith("blk@") else tgt
            legend_label = f"{tgt} - {self.P.label}"

        t0 = time.perf_counter()

        full_k_df = self.feat.rerun().to_df()

        t1 = time.perf_counter()

        k_df = ctx.slice_natural_df(full_k_df)
        if k_df.shape[0] < 2:
            self.logger.warning(f"No K data: {self.feat}")
            return

        try:
            open_uti = k_df["openUti"].values
            close_uti = k_df["closeUti"].values
        except:
            open_uti = k_df.uti.values
            close_uti = np.roll(open_uti, -1)  # bar 结束 uti 位置
            # 修正最后一个结束 uti，让最后一个 bar 与它之前一个 bar 等宽
            close_uti[close_uti.size - 1] = (
                open_uti[open_uti.size - 1] * 2 - open_uti[open_uti.size - 2]
            )

        # 到中间位置的偏移量
        x_shift = (close_uti - open_uti) / 2
        # 横把儿的宽度
        h_width = x_shift * 0.8

        # from IPython import get_ipython

        # ipy_ns = get_ipython().user_ns
        # ipy_ns.update(locals())

        ohlc_glyphs = []

        x = open_uti + x_shift  # 假定K线数据以开盘时点标示
        ts_labels = k_df.index.strftime("%F %H:%M").tolist()

        cds = ColumnDataSource(
            {
                "x": x,
                "x_l": x - h_width,
                "x_r": x + h_width,
                "open": k_df["open"],
                "high": k_df["high"],
                "low": k_df["low"],
                "close": k_df["close"],
                "volume": k_df["volume"],
                "ts": ts_labels,
            }
        )

        t2 = time.perf_counter()

        ctx.add_cds(f"ohlc({__class__.__name__})", cds, t1 - t0, t2 - t1)

        if self.P.std_method:
            ctx.add_dynstd(
                DynStd(
                    cds,
                    self.P.std_method,
                    base_y="open",
                    extra_ys=["high", "low", "close"],
                )
            )

        k_color = self.P.color or ctx.sym_color or "gray"
        ohlc_glyphs.append(
            fig.segment(
                source=cds,
                level="underlay",
                x0="x",
                x1="x",
                y0="high",
                y1="low",
                color=k_color,
                alpha=self.P.alpha,
                line_width=2,
                legend_label=legend_label,
            )
        )
        ohlc_glyphs.append(
            fig.segment(
                source=cds,
                level="underlay",
                x0="x_l",
                x1="x",
                y0="open",
                y1="open",
                color=k_color,
                alpha=self.P.alpha,
                line_width=2,
                legend_label=legend_label,
            )
        )
        ohlc_glyphs.append(
            fig.segment(
                source=cds,
                level="underlay",
                x0="x",
                x1="x_r",
                y0="close",
                y1="close",
                color=k_color,
                alpha=self.P.alpha,
                line_width=2,
                legend_label=legend_label,
            )
        )

        if self.P.add_hover:
            ctx.add_hover(
                ohlc_glyphs,
                ("ohlc", "@ts 开=@open,高=@high,低=@low,收=@close,量=@volume"),
                mode="mouse",  # mouse'，'hline'，'vline
                line_policy="none",  # prev'，'next'，'nearest'，'interp'，'none'）
                point_policy="snap_to_data",
                name="bar",
            )

        ctx.fit_ys(cds, "x", "high", "low")

        nextProcess = self.P.read("NextProcess")

        if isinstance(nextProcess, BaseNextProcessPlot):
            nextProcess.processFigure(fig, ctx)


class BaseNextProcessPlot(DoFunctionFao):
    """
    Author: King
    Since : 2024-11-13 14:46
    Desc  : 对 figure 进一步加工，如绑定各种事件等
    """

    __abstract_fao__ = True

    def processFigure(self, fig: figure, ctx: PlotCtx):
        """进一步加工 figure"""
        pass


class TickPriceLine(BasePlotter):
    """
    统一时间轴 Tick 线

    """

    params = lambda: dict(
        std_method=None,
        feat=SubContinuousContract(),
        df_key="value",
        line_field="price",
        color=None,
        alpha=0.8,  # 透明度
        line_width=1,  # 线宽
        label="Tick价格线",
    )

    def _plot_fig(self, ctx: PlotCtx):
        gps = ctx.gps
        fig = ctx.figs[-1]

        sym = CurrSymbol.sym(False)
        tgt = currTarget()
        if tgt is None:
            legend_label = self.P.label
        else:
            legend_label = f"{tgt} - {self.P.label}"

        t0 = time.perf_counter()

        tick_df = self.P.feat.rerun().to_dfs()[self.P.df_key]
        assert (
            tick_df.shape[0] == ctx.utsa.size
        ), f"{self.P.feat!r} 并非完整补齐数据，或者日历不匹配！"

        t1 = time.perf_counter()

        tick_data = tick_df[self.P.line_field].values[ctx.uti_slice]

        # from IPython import get_ipython

        # ipy_ns = get_ipython().user_ns
        # ipy_ns.update(locals())

        cds = ColumnDataSource({"x": ctx.uti_range, "y": tick_data})

        t2 = time.perf_counter()

        ctx.add_cds(f"line({__class__.__name__})", cds, t1 - t0, t2 - t1)

        fig.line(
            source=cds,
            level="underlay",
            color=self.P.color or ctx.sym_color or "gray",
            alpha=self.P.alpha,
            line_width=self.P.line_width,
            legend_label=legend_label,
        )
        if self.P.std_method:
            ctx.add_dynstd(DynStd(cds, self.P.std_method))


class MulSegPlot(BasePlotter):
    """
    Available Predefined Dash Styles:
        "solid": A solid line with no dashes.
        "dashed": A line with a standard dash pattern.
        "dotted": A line composed of dots.
        "dotdash": Alternates between dots and dashes.
        "dashdot": Alternates between dashes and dots.
    """

    params = lambda: dict(
        feats=Nothing,
        k_freq=None,
        x0s=None,
        x1s=None,
        y0s=None,
        y1s=None,
        dfkeys=None,
        timefieldtype="idx",  # 支持idx、ts、uti类型
        colors=[None],
        legend_labels=None,
        alphas=0.6,
        line_widths=1,
        line_dashs="solid",
        # 动态标准化方法
        #   False: 不动态标准化
        #   True: 跟随品种价格动态标准化
        #   字符串:
        #     ratio 除法
        #     diff 减法
        #     ratio-back 反向除法
        #     diff-back 反向减法
        dynstd_method=True,
        hover=True,
        usesymid_adjustfeat=None,
    )

    def _plot_fig(self, ctx: PlotCtx):
        gps = ctx.gps
        fig = ctx.figs[-1]
        sym = CurrSymbol.sym()
        tgt = currTarget()

        for i, (
            feat,
            x0,
            x1,
            y0,
            y1,
            dfkey,
            alpha,
            line_width,
            line_dash,
            label,
            color,
        ) in enumerate(
            zip(
                self.feats.make_arr(),
                itertools.cycle(ensure_list(self.P.x0s)),
                itertools.cycle(ensure_list(self.P.x1s)),
                itertools.cycle(ensure_list(self.P.y0s)),
                itertools.cycle(ensure_list(self.P.y1s)),
                itertools.cycle(ensure_list(self.P.dfkeys)),
                itertools.cycle(ensure_list(self.P.alphas)),
                itertools.cycle(ensure_list(self.P.line_widths)),
                itertools.cycle(ensure_list(self.P.line_dashs)),
                itertools.cycle(ensure_list(self.P.legend_labels)),
                itertools.cycle(self.P.colors),
            )
        ):
            # 有些参数给了必须是有效值,通过这个字典实现默认情况下不给参数
            glyph_args = {}
            full_label = None
            if label is not None:
                # glyph_args["legend_label"] = label
                full_label = f"{tgt} - {label}" if tgt else label
                glyph_args["legend_label"] = full_label

            def fd_trans(df):
                df = df.dropna(subset=[x0, x1, y0, y1])
                fd = {
                    "y0": df[y0],
                    "y1": df[y1],
                }
                if self.P.timefieldtype == "idx":
                    fd["x0"] = ctx.idx2x(df[x0], freq=self.P.k_freq)
                    fd["x1"] = ctx.idx2x(df[x1], freq=self.P.k_freq)
                elif self.P.timefieldtype == "ts":
                    fd["x0"] = ctx.ts2x(pd.to_datetime(df[x0], errors="coerce"))
                    fd["x1"] = ctx.ts2x(pd.to_datetime(df[x1], errors="coerce"))
                elif self.P.timefieldtype == "uti":
                    fd["x0"] = ctx.uti2x(df[x0].values)
                    fd["x1"] = ctx.uti2x(df[x1].values)
                else:
                    raise RuntimeError("只支持idx、ts、uti这几种时间字段类型")
                return fd

            if self.P.timefieldtype == "uti":
                cds = ctx.live_feat_data(
                    f"segment({__class__.__name__})",
                    fd_trans,
                    feat,
                    dfkey,
                    uti1_field=x0,
                    uti2_field=x1,
                )
            else:
                cds = ctx.live_feat_data(
                    f"segment({__class__.__name__})", fd_trans, feat, dfkey
                )

            if len(cds.data["x0"]) > 0:  # 有数据的才去画

                if self.P.dynstd_method is True:
                    ctx.drive_entity_dynstd(cds, [("x0", "y0"), ("x1", "y1")])
                elif self.P.dynstd_method:
                    # 独自动态标准化
                    dynstd = DynStd(
                        cds, method=self.P.dynstd_method, base_x="x0", base_y="y0"
                    )
                    dynstd.drive(cds, [("x1", "y1")])
                    ctx.add_dynstd(dynstd)

                ctx.add_hover(
                    fig.segment(
                        source=cds,
                        color=color or next(ctx.sym_colors),
                        alpha=alpha,
                        line_width=line_width,
                        line_dash=line_dash,
                        name=label,
                        **glyph_args,
                    ),
                    (label, "@y0 ~ @y1"),
                )

                ctx.fit_ys(cds, "x0", "y0")
                ctx.fit_ys(cds, "x1", "y1")


class StrasTradePlot(BasePlotter):
    """
    Author: cyue
    Since : 2023-10-31
    Desc  :
       - 指定要画交易的多个策略trader
       - 多向:开仓交易使用triangle图形,平仓交易使用triangle_dot图形
       - 空向:开仓交易使用star图形,平仓交易使用star_dot图形
       - 盈利交易使用实线,亏损交易使用虚线
    Params:
        traders:要画交易的多个策略trader
        colors:颜色列表,如果为None,则使用ContrastColors
        legend_labels:标签列表,如果为None,则使用traders的key
        trade_volume:是否显示交易量信息
    ChangeLog:
        20240225:
        traders参数类型从[]修改为符合fao框架的GMap()
        legend_labels参数如果为None,则使用traders的key
    """

    params = lambda: dict(
        traders=GMap(),
        colors=[],
        legend_labels=[],
        trade_volume=True,
    )

    def _plot_fig(self, ctx: PlotCtx):
        fig = ctx.figs[-1]
        sof = ctx.sof

        sym = CurrSymbol.sym()
        tgt = currTarget()

        for trader, label, tx_color in zip(
            self.traders.make_arr(),
            self.P.legend_labels or list(self.traders.keys()),
            itertools.cycle(self.P.colors or [cs[1] for cs in ctx.gps.colors2]),
        ):
            if label is None:
                label = repr(trader)

            df_tx = (
                TrialOptimizer(
                    {
                        "Context(OptContext).sof_name": sof.sof_name,
                        "Context(OptContext).stk_tlist": sym,
                        "Context(OptContext).startDay": sof.startDay,
                        "Context(OptContext).endDay": sof.endDay,
                        "Context(OptContext).config.opt_settings.is_save_record": True,
                        "Trader": trader,
                    }
                )
                .run()
                .record
            )

            # from IPython import get_ipython

            # ipy_ns = get_ipython().user_ns
            # ipy_ns.update(locals())

            assert df_tx.shape[1] > 0, f"交易记录结果异常： df_tx.shape = {df_tx.shape}"

            for tsCol in ["建仓时间", "平仓时间"]:
                df_tx[tsCol] = np.array(df_tx[tsCol], "M8[ns]")
            df_tx = df_tx[
                (df_tx.建仓时间 >= ctx.time_range.start)
                & (df_tx.平仓时间 <= ctx.time_range.stop)
            ]

            if self.P.trade_volume:
                cds = bkh.ColumnDataSource(
                    {
                        "x": ctx.ts2x(df_tx.平仓时间),
                        "y": df_tx.平仓价,
                        "text": df_tx.平仓量.map("[{:.1f}]".format),
                    }
                )
                fig.text(
                    source=cds,
                    color=tx_color,
                    text_font_size="9pt",
                    text_align="center",
                    text_baseline="top",
                    y_offset=7,  # 此参数值为屏幕单位，正负与数据空间的偏移方向相反
                    legend_label=f"{tgt} 平仓量 - {label}",
                )
                ctx.drive_entity_dynstd(cds)

            # 多向开平仓事件
            long_trade = df_tx[(df_tx.平仓量 > 0)]
            x0 = ctx.ts2x(long_trade.建仓时间)
            x1 = ctx.ts2x(long_trade.平仓时间)

            cds = bkh.ColumnDataSource(
                {
                    "x": x0,
                    "y": long_trade.建仓价,
                }
            )
            fig.scatter(
                marker="triangle",
                source=cds,
                color=tx_color,
                size=14,
                legend_label=label,
            )
            ctx.drive_entity_dynstd(cds)

            cds = bkh.ColumnDataSource(
                {
                    "x": x1,
                    "y": long_trade.平仓价,
                }
            )
            fig.scatter(
                marker="triangle_dot",
                source=cds,
                color=tx_color,
                size=14,
                legend_label=label,
            )
            ctx.drive_entity_dynstd(cds)

            # 空向开平仓事件
            short_trade = df_tx[(df_tx.平仓量 < 0)]
            x0 = ctx.ts2x(short_trade.建仓时间)
            x1 = ctx.ts2x(short_trade.平仓时间)

            cds = bkh.ColumnDataSource(
                {
                    "x": x0,
                    "y": short_trade.建仓价,
                }
            )
            fig.scatter(
                marker="star",
                source=cds,
                color=tx_color,
                size=14,
                legend_label=label,
            )
            ctx.drive_entity_dynstd(cds)

            cds = bkh.ColumnDataSource(
                {
                    "x": x1,
                    "y": short_trade.平仓价,
                }
            )
            fig.scatter(
                marker="star_dot",
                source=cds,
                color=tx_color,
                size=14,
                legend_label=label,
            )
            ctx.drive_entity_dynstd(cds)

            # 多向盈利交易
            long_wintrade = long_trade[(long_trade.盈亏 > 0)]
            x0 = ctx.ts2x(long_wintrade.建仓时间)
            x1 = ctx.ts2x(long_wintrade.平仓时间)

            cds = bkh.ColumnDataSource(
                {
                    "x0": x0,
                    "x1": x1,
                    "y0": long_wintrade.建仓价,
                    "y1": long_wintrade.平仓价,
                }
            )
            fig.segment(
                source=cds,
                color=tx_color,
                line_width=2,
                legend_label=label,
            )
            ctx.drive_entity_dynstd(cds, [("x0", "y0"), ("x1", "y1")])

            # 多向亏损交易
            long_losstrade = long_trade[(long_trade.盈亏 < 0)]
            x0 = ctx.ts2x(long_losstrade.建仓时间)
            x1 = ctx.ts2x(long_losstrade.平仓时间)

            cds = bkh.ColumnDataSource(
                {
                    "x0": x0,
                    "x1": x1,
                    "y0": long_losstrade.建仓价,
                    "y1": long_losstrade.平仓价,
                }
            )
            fig.segment(
                source=cds,
                color=tx_color,
                line_width=2,
                line_dash="dashed",
                legend_label=label,
            )
            ctx.drive_entity_dynstd(cds, [("x0", "y0"), ("x1", "y1")])

            # 空向盈利交易
            short_wintrade = short_trade[(short_trade.盈亏 > 0)]
            x0 = ctx.ts2x(short_wintrade.建仓时间)
            x1 = ctx.ts2x(short_wintrade.平仓时间)

            cds = bkh.ColumnDataSource(
                {
                    "x0": x0,
                    "x1": x1,
                    "y0": short_wintrade.建仓价,
                    "y1": short_wintrade.平仓价,
                }
            )
            fig.segment(
                source=cds,
                color=tx_color,
                line_width=2,
                legend_label=label,
            )
            ctx.drive_entity_dynstd(cds, [("x0", "y0"), ("x1", "y1")])

            # 空向亏损交易
            short_losstrade = short_trade[(short_trade.盈亏 < 0)]
            x0 = ctx.ts2x(short_losstrade.建仓时间)
            x1 = ctx.ts2x(short_losstrade.平仓时间)

            cds = bkh.ColumnDataSource(
                {
                    "x0": x0,
                    "x1": x1,
                    "y0": short_losstrade.建仓价,
                    "y1": short_losstrade.平仓价,
                }
            )
            fig.segment(
                source=cds,
                color=tx_color,
                line_width=2,
                line_dash="dashed",
                legend_label=label,
            )
            ctx.drive_entity_dynstd(cds, [("x0", "y0"), ("x1", "y1")])


SIZE_SCALE_FACTORS = {}


class MulFieldsGlyphs(BasePlotter):
    """
    Author: cyue
    Since : 2024-11-15
    Desc  :
       - 指定要画的多个图,多个图的多个特征字段的来源为单个特征的不同品种
    Params:
        glyphs: 形状
        feats: 特征
        legend_labels: 图例
            None为默认值,None代表使用品种名,也可以直接给列表
        colors: 颜色
            None 则使用品种颜色，也可以直接给列表
        xfields: 横轴时间字段名
            None 则使用 df 索引时间
        yfields: 纵轴数值字段名
        timefieldtype: 支持idx、ts、uti类型
        size_fields: 通过特征值指定图形大小
        size_scale_factor:
            * True - 使用预设缩放比例，若无预设则独立计算
            * 'set' - 计算缩放比例，并设为预设
            * 其它 - 独立计算缩放比例
        size_scale 图形大小的放大倍率
        size_base: 基础大小（防止过小的数据画了却看不到）
        size: 大小
        alphas: 透明度
        widgeter: BasePPChangeWidget 子类,用于实现如中尺度参数切换触发改变小尺度图
    """

    params = lambda: dict(
        glyphs="asterisk",
        feats=GMap(),
        dfkeys=[None],
        legend_labels=None,
        colors=[None],
        xfields=[None],
        yfields=[],
        timefieldtype="uti",
        size_fields=None,
        size_scale_factor=True,
        size_scale=100,
        size_base=5,
        size=5,
        alphas=0.6,
        # 动态标准化方法
        #   False: 不动态标准化
        #   True: 跟随品种价格动态标准化
        #   字符串:
        #     ratio 除法
        #     diff 减法
        #     ratio-back 反向除法
        #     diff-back 反向减法
        dynstd_method=True,
        hover_tslabel=True,
        widgeter=UnFree(Nothing),
    )

    def _plot_fig(self, ctx: PlotCtx):
        hover_tslabel = self.P.hover_tslabel

        gps = ctx.gps
        fig = ctx.figs[-1]

        sym = CurrSymbol.sym()
        tgt = currTarget()

        for (
            feat,
            dfkey,
            xfield,
            yfield,
            size_field,
            glyph,
            label,
            color,
            alpha,
        ) in zip(
            self.feats.make_arr(),
            itertools.cycle(ensure_list(self.P.dfkeys)),
            itertools.cycle(ensure_list(self.P.xfields)),
            itertools.cycle(ensure_list(self.P.yfields)),
            itertools.cycle(ensure_list(self.P.size_fields)),
            itertools.cycle(ensure_list(self.P.glyphs)),
            itertools.cycle(ensure_list(self.P.legend_labels)),
            itertools.cycle(self.P.colors),
            itertools.cycle(ensure_list(self.P.alphas)),
        ):
            # 有些参数给了必须是有效值,通过这个字典实现默认情况下不给参数
            glyph_args = {}
            if label is not None:
                legend_label = f"{tgt} - {label}" if tgt else label
                glyph_args["legend_label"] = legend_label
                glyph_args["name"] = legend_label
            if glyph != "line":
                glyph_args["size"] = self.P.size

            def fd_trans(df):
                fd = {"y": df[yfield]}
                if xfield:
                    if self.P.timefieldtype == "idx":
                        fd["x"] = ctx.idx2x(df[xfield], freq=feat.P.freq)
                        if hover_tslabel:
                            fd["ts"] = ctx.idx2tslabel(df[xfield])
                    elif self.P.timefieldtype == "ts":
                        fd["x"] = ctx.ts2x(pd.to_datetime(df[xfield], errors="coerce"))
                        if hover_tslabel:
                            fd["ts"] = ctx.ts2tslabel(pd.to_datetime(df[xfield]))
                    elif self.P.timefieldtype == "uti":
                        fd["x"] = ctx.uti2x(df[xfield].values)
                        if hover_tslabel:
                            fd["ts"] = ctx.uti2tslabel(df[xfield].values)
                    else:
                        raise RuntimeError("只支持idx、ts、uti这几种时间字段类型")
                else:
                    fd["x"] = ctx.ts2x(df.index.values)
                    if hover_tslabel:
                        fd["ts"] = ctx.ts2tslabel(df.index)

                if size_field:
                    sd = df[size_field]
                    sz_scale_key = (sym, feat.ppid, size_field)
                    scale_factor = None
                    if self.P.size_scale_factor == "set":
                        scale_factor = size_scale_factor(
                            sd.min(), sd.max(), self.P.size_scale
                        )
                        SIZE_SCALE_FACTORS[sz_scale_key] = scale_factor
                    elif self.P.size_scale_factor is True:
                        scale_factor = SIZE_SCALE_FACTORS.get(sz_scale_key, None)
                    if scale_factor is None:
                        scale_factor = size_scale_factor(
                            sd.min(), sd.max(), self.P.size_scale
                        )
                    fd["size"] = scale_size_by_factor(
                        sd, self.P.size_base, scale_factor
                    )
                    glyph_args["size"] = "size"

                return fd

            if xfield and self.P.timefieldtype == "uti":
                cds = ctx.live_feat_data(
                    (
                        f"{label}: line({__class__.__name__})"
                        if glyph == "line"
                        else f"{label}: scatter/{glyph}({__class__.__name__})"
                    ),
                    fd_trans,
                    feat,
                    dfkey,
                    xfield,
                    x_range=fig.x_range,
                    dynstd_ys=["y"],
                    widgeter=self.P.get("widgeter"),
                )
            else:
                cds = ctx.live_feat_data(
                    (
                        f"{label}: line({__class__.__name__})"
                        if glyph == "line"
                        else f"{label}: scatter/{glyph}({__class__.__name__})"
                    ),
                    fd_trans,
                    feat,
                    dfkey,
                    None,
                    x_range=fig.x_range,
                    dynstd_ys=["y"],
                    widgeter=self.P.get("widgeter"),
                )

            if self.P.dynstd_method is True:
                ctx.drive_entity_dynstd(cds)
            elif self.P.dynstd_method:
                # 独自动态标准化
                ctx.add_dynstd(DynStd(cds, method=self.P.dynstd_method))

            ctx.add_hover(
                (
                    fig.line(
                        source=cds,
                        color=color or next(ctx.sym_colors),
                        alpha=alpha,
                        **glyph_args,
                    )
                    if glyph == "line"
                    else fig.scatter(
                        marker=glyph,
                        source=cds,
                        color=color or next(ctx.sym_colors),
                        alpha=alpha,
                        **glyph_args,
                    )
                ),
                (label, "@ts @y" if hover_tslabel else "@y"),
            )

            ctx.fit_ys(cds)


class PlotSet(DoFunctionFao):

    params = lambda: dict(
        calendar_name="@",  # 日历
        blk=None,
        timespans=[],
        timespans_fao=Nothing,
        figs=GMap(),
    )

    def plot(self, plot_root: PlotDataFolder, plotset_name: str, gps):
        all_figs = CurrWidgets.all_figs()

        sof = CurrTradeSet.sof()
        blk = self.P.blk

        all_symbols = BlockTarType.from_expr(blk).symbols()
        timespans = self.P.timespans

        with CurrIndustry(blk), CurrCalendar(self.P.calendar_name):
            if not timespans:
                timespans = self.timespans_fao.timespans()

            for start_time, end_time, *span_info in timespans:
                ctx = PlotCtx(
                    plot_root,
                    plotset_name,
                    self.P.calendar_name,
                    sof,
                    all_symbols,
                    blk,
                    gps,
                    start_time,
                    end_time,
                    span_info,
                )

                for fk, fs in self.P.figs.P.items():
                    if not gps.switches.get(fk, True):
                        continue
                    if isinstance(fs, BaseFigSet):
                        fs.plot_figs(ctx)
                    else:
                        raise TypeError(f"Unsupported fig set type: {type(fs)}")

                all_figs.append(ctx.figs)


class CAEGraph(DoFunctionFao):
    """ """

    class Meta:
        on_pable = True

    params = lambda: dict(
        Context=OptContext(),
        plotsets=GMap(),
        theme=DefaultFigTheme(),  # 主题
        x_label_freq="1m",  # 画图X轴标注时间频度
        extra_time=0,  # 额外多画这么长时间
        fig_width=1200,  # 图宽
        fig_height1=500,  # 主图高
        fig_height=350,  # 附图高
        manual_upd=True,  # 控件拖动后手动更新画图数据
        colors2=None,  # 两级色板
        plot_name="总图集",  # 根节点名称
        switches={},  # 可以灵活指定的自定义开关
    )

    def layout(
        self,
        ncols=1,
        all_figs=None,
        live_ctrls=None,
        live_updaters=None,
        plot_roots: Optional[list[PlotDataFolder]] = None,
    ):
        assert 1 <= ncols < 500, f"ncols = {ncols} ?!"

        with CurrWidgets(
            all_figs,
            live_ctrls,
            live_updaters,
            manual_upd=self.P.manual_upd,
            plot_roots=plot_roots,
        ) as widgets:
            self.produce_widgets()
        all_figs, live_ctrls, upd_btn = widgets

        n = len(all_figs)
        start_i, end_i, rows = 0, ncols, []
        while start_i < n:
            rows.append(
                bkh.Row(
                    children=[
                        bkh.Column(children=figs) for figs in all_figs[start_i:end_i]
                    ]
                )
            )
            start_i, end_i = end_i, end_i + ncols

        items = []
        if live_ctrls:
            if upd_btn:
                items.append(upd_btn)
            items.extend(widget for _ctrl, widget in live_ctrls.values())
        items.extend(rows)
        return bkh.Column(children=items)

    def produce_widgets(self):
        sof = self.Context.sof

        gps = self.P
        if gps.colors2 is None:
            gps["colors2"] = ContrastColors2

        # 累积图形数据
        with CurrTradeSet(sof):
            plot_root = PlotDataFolder(self.P.plot_name)
            CurrWidgets.plot_roots().append(plot_root)

            for psk, ps in self.P.plotsets.P.items():
                if not gps.switches.get(psk, True):
                    continue
                ps.plot(plot_root, psk, gps)

    def bkapp(self, ncols=1):
        """
        在 Notebook 中 直接 show(CAEGraph(...).layout(ncols=1)), 拖动控件不起作用
        需要以下方式嵌入 Bokeh server 到 Notebook 中

        show(CAEGraph(...).bkapp(ncols=1),notebook_url="http://192.168.11.92:8888")

        注意修改对应的 notebook_url 地址
        notebook_url:
            - If the current notebook is not displayed at the default URL,
            - you must update the notebook_url parameter in the comment below to match, and pass it to show
        """

        def bkapp(doc):
            doc.add_root(self.layout(ncols=ncols))

        return bkapp


def convert_columns_to_datetime(df, columns_to_convert):
    """
    Convert specified columns of a DataFrame to datetime64[ns] format.

    Parameters:
    df (pandas.DataFrame): The DataFrame containing the columns to convert.
    columns_to_convert (list of str): List of column names to convert to datetime.

    Returns:
    pandas.DataFrame: DataFrame with specified columns converted to datetime64[ns].
    """
    return df.assign(
        **{
            column: pd.to_datetime(df[column], errors="coerce")
            for column in columns_to_convert
        }
    )


# 每隔n个成为1组，用相同颜色。每n个用1套不同的颜色，并且在数值上调整以区分。
# df -> n个df,每个df是相同颜色，n个df之间按指定函数(序号相关的逻辑)调整数值
def assign_df_every_nline(
    df, n, adjKey=["value.cprice2_0", "value.cprice2_1"], adjFunc=lambda df, i: df
):
    # 创建一个字典来保存每个子DataFrame
    sub_dfs = {f"df{i}": df.iloc[i::n] for i in range(n)}
    # 每个dataframe的数值调整
    nsub_dfs = {}
    for i in range(n):
        df = sub_dfs[f"df{i}"]
        #         print((adjFunc(df[adjKey],i)).combine_first(df))
        nsub_dfs[f"df{i}"] = (adjFunc(df[adjKey], i)).combine_first(df)
    return nsub_dfs


def selected_fields(tar, fields):
    """从特征获取字段名"""
    f1v = tar.F
    f1dict = Ndict().fold(f1v)  # 打平字典，防止有多层而取不到字段
    allfields = [k for (k, v) in f1dict.items()]  # 全部字段
    if fields is None:  # 不给fields，取出全部tensor
        sfields = allfields
    elif isinstance(fields, str):
        sfields = []
        for j in allfields:
            if j.startswith(fields):
                sfields.append(j)
    else:  # 否则，只取出fields开头的tensor
        sfields = []
        for i in fields:
            for j in allfields:
                if j.startswith(i):
                    sfields.append(j)
    return sfields


class MulPointPlot(BasePlotter):
    """
    Author: zy
    Since : 2023-12-05 22:30
    Desc  : 多个历史点的图
    Params:
        feats: 提供点的特征,可以是单个特征的多个点，可以是多个特征的单个点
        xfield: 多个x字段，如果只有1个，表示多个特征用相同字段，或是单个特征的所有以它开头的字段。
        yfield: 多个y字段
        timefieldtype: 支持idx或者ts类型
        colors: 颜色
        legend_labels: label
        size_base: 基础大小（防止过小的数据画了却看不到）
        size: 大小
        size_field 通过特征值指定图形大小
        size_scale 图形大小的放大倍率
        alphas: 透明度
        line_widths: 粗细
        hover: 浮标
    """

    params = lambda: {
        "feats": Nothing,  # 可以是单个特征的多个点，可以是多个特征的单个点
        "xfield": [],  # 多个x字段，如果只有1个，表示多个特征用相同字段，或是单个特征的所有以它开头的字段。
        "yfield": [],
        "timefieldtype": "idx",  # 支持idx或者ts类型
        "colors": [None],
        "legend_labels": None,
        "size_base": 20,
        "size": 5,
        "size_field": None,  # 通过特征值指定图形大小
        "size_scale": 100,  # 图形大小的放大倍率
        "alphas": 0.6,
        "line_widths": 1,
        "hover": True,
    }

    def _prep_fields(self):
        # 准备fields
        xfield = self.P.xfield
        yfield = self.P.yfield
        if not isinstance(self.feats, GMap):
            # 找出以它开头的所有字段
            if len(self.P.xfield) == 1:
                xfield = selected_fields(self.feats, self.P.xfield)
            if len(self.P.yfield) == 1:
                yfield = selected_fields(self.feats, self.P.yfield)
        return xfield, yfield

    def _single_plot_fig(self, ctx, datasource, x, y, alpha, line_width, label, color):
        fig = ctx.figs[-1]

        glyph_args = {}  # 有些参数给了必须是有效值,通过这个字典实现默认情况下不给参数
        if label is not None:
            glyph_args["legend_label"] = label
        glyph_args["size"] = self.P.size

        def fd_trans(df):
            fd = {"y": df[y]}
            if self.P.timefieldtype == "idx":
                fd["x"] = ctx.idx2x(df[x], freq=datasource.P.freq)
            elif self.P.timefieldtype == "ts":
                df = convert_columns_to_datetime(df, [x])
                fd["x"] = ctx.ts2x(df[x])
            else:
                raise RuntimeError("只支持idx和ts这两种时间字段类型")
            if self.P.size_field:
                sd = df[self.P.size_field]
                fd["size"] = scale_size(sd, self.P.size_base, self.P.size_scale)
                glyph_args["size"] = "size"
            return fd

        cds = ctx.feat_data(f"circle({__class__.__name__})", fd_trans, datasource)

        # 有数据才画
        if len(cds.data["x"]) > 0:
            ctx.add_hover(
                fig.circle(
                    source=cds,
                    color=color,
                    alpha=alpha,
                    line_width=line_width,
                    name=label,
                    **glyph_args,
                ),
                (label, "@y"),
            )

            ctx.fit_ys(cds)

    def _plot_fig(self, ctx: PlotCtx):
        gps = ctx.gps
        fig = ctx.figs[-1]

        xfield, yfield = self._prep_fields()

        # 找出多个点的信息
        for i, (feat, x, y, alpha, line_width, label, color) in enumerate(
            zip(
                (
                    self.feats.make_arr()
                    if isinstance(self.feats, GMap)
                    else [self.feats] * len(xfield)
                ),
                itertools.cycle(ensure_list(xfield)),
                itertools.cycle(ensure_list(yfield)),
                itertools.cycle(ensure_list(self.P.alphas)),
                itertools.cycle(ensure_list(self.P.line_widths)),
                itertools.cycle(ensure_list(self.P.legend_labels)),
                itertools.cycle(self.P.colors or [cs[1] for cs in gps.colors2]),
            )
        ):
            self._single_plot_fig(ctx, feat, x, y, alpha, line_width, label, color)


class OneToGroupPointPlot(MulPointPlot):
    """
    Author: zy
    Since : 2023-12-05 22:33
    Desc  : 多个历史点防重叠的分组分色图
    Params:
        groupN: 分成n组
        adjField: 多个需要调整值的字段
        adjFunc: 每组数据，对需要调整的字段应用什么函数，输入要求是df和i
    """

    params = lambda: {
        "groupN": 1,  # 分成n组
        "adjField": [],  # 多个需要调整值的字段
        "adjFunc": None,  # 每组数据，对需要调整的字段应用什么函数，输入要求是df和i
    }

    def _one_to_grp_ds(self):
        df = self.feats.run().to_df()
        adjFunc = self.P.adjFunc or (lambda df, i: df)
        return assign_df_every_nline(df, self.P.groupN, self.P.adjField, adjFunc)

    def _plot_fig(self, ctx: PlotCtx):
        # 多组数据
        dfs = self._one_to_grp_ds()

        gps = ctx.gps
        fig = ctx.figs[-1]

        xfield, yfield = self._prep_fields()

        # 找出多个点的信息
        for k in range(self.P.groupN):
            if isinstance(self.P.legend_labels, list):
                groupLabel = [f"group{k}_" + lbl for lbl in self.P.legend_labels]
            else:
                groupLabel = f"group{k}_" + self.P.legend_labels
            for i, (df, x, y, alpha, line_width, label, color) in enumerate(
                zip(
                    [list(dfs.values())[k]] * len(xfield),
                    itertools.cycle(ensure_list(xfield)),
                    itertools.cycle(ensure_list(yfield)),
                    itertools.cycle(ensure_list(self.P.alphas)),
                    itertools.cycle(ensure_list(self.P.line_widths)),
                    itertools.cycle(ensure_list(groupLabel)),
                    itertools.cycle(self.P.colors),
                )
            ):
                self._single_plot_fig(
                    ctx,
                    df,
                    x,
                    y,
                    alpha,
                    line_width,
                    label,
                    color or next(ctx.sym_colors),
                )


def split_dataframe(df):
    """拆分 DataFrame, 把同一时间的多条数据分开成多个df"""
    # 创建一个空的列表来保存分割后的 DataFrame
    split_dfs = []

    # 获取所有唯一的 (timestamp, record_id) 组合
    unique_indices = df.index.unique()

    # 创建一个临时字典用于存储每个 record_id 的 DataFrame
    temp_dict = {}

    # 遍历所有唯一的 (timestamp, record_id) 组合
    for idx in unique_indices:
        timestamp, record_id = idx
        if record_id not in temp_dict:
            temp_dict[record_id] = []
        record_dict = df.loc[idx].to_dict()
        record_dict["timestamp"] = timestamp
        temp_dict[record_id].append(record_dict)

    # 将临时字典中的数据转换为 DataFrame
    for record_id, records in temp_dict.items():
        temp_df = pd.DataFrame(records)
        temp_df.set_index("timestamp", inplace=True)
        split_dfs.append(temp_df)

    return split_dfs


class SeqOfFieldsPlot(BasePlotter):
    """
    Author: zy
    Since : 2024-06-11 20:27
    Desc  : 不定长度的occur拆成多个df,分别画图
    Params:
        feat: 特征
        field: 拥有不定长度数据的字段名
        glyphs: 形状
        colors: 颜色
        labels: 图例
    """

    params = lambda: dict(
        feat=Nothing,  # 特征
        field="value",  # 不定长度的字段名
        glyphs="cross",  # 形状
        colors=[None],  # 颜色  None为默认值:代表使用默认颜色列表中的第一个
        labels=None,  # 图例  None为默认值:代表不需要图例
    )

    def _plot_fig(self, ctx: PlotCtx):
        gps = ctx.gps
        fig = ctx.figs[-1]

        if not hasattr(ctx, "_hover_glyphs"):
            ctx._hover_glyphs = []

        # 变长df取出来，然后拆成多个df
        df = self.feat.run().to_df()
        dfs = split_dataframe(df)

        for i, (df, glyph, label, color) in enumerate(
            zip(
                dfs,
                itertools.cycle(ensure_list(self.P.glyphs)),
                itertools.cycle(ensure_list(self.P.labels)),
                itertools.cycle(self.P.colors),
            )
        ):
            # 有些参数给了必须是有效值,通过这个字典实现默认情况下不给参数
            glyph_args = {}
            if label is not None:
                glyph_args["legend_label"] = label
            cds = ctx.feat_data(
                f"scatter/{glyph}({__class__.__name__})",
                lambda df: {
                    "y": df[self.P.field],
                },
                df,
            )

            ctx.add_hover(
                fig.scatter(
                    marker=glyph,
                    source=cds,
                    color=color or next(ctx.sym_colors),
                    name=label,
                    **glyph_args,
                ),
                (label, "@y"),
            )

            ctx.fit_ys(cds)


class TextPlot(BasePlotter):
    """ """

    params = lambda: dict(
        feat=Nothing,  # 特征
        df_key=None,
        x_field=None,  # x值字段名
        y_field=None,  # y值字段名
        text_field=None,  # 文本信息字段名
        field_uti2ts=True,  # 文本信息字段是否要进行从uti转为时间戳的处理
        color="black",  # 颜色
        alpha=0.8,  # 透明度
        #         line_width=5,  # 线宽
        label=None,  # 图例  None为默认值:代表不需要图例
        # 动态标准化方法
        #   False: 不动态标准化
        #   True: 跟随品种价格动态标准化
        #   字符串:
        #     ratio 除法
        #     diff 减法
        #     ratio-back 反向除法
        #     diff-back 反向减法
        dynstd_method=True,
    )

    def _plot_fig(self, ctx: PlotCtx):
        gps = ctx.gps
        fig = ctx.figs[-1]

        label = self.P.label

        sym = CurrSymbol.sym()
        if label is not None:
            label = f"{sym} - {label}" if sym else label

        cds = ctx.live_feat_data(
            f"text({__class__.__name__})",
            lambda df: {
                "x": df[self.P.x_field].values,
                "y": df[self.P.y_field].values,
                "text": (
                    ctx.uti2tslabel(df[self.P.text_field].values)
                    if self.P.field_uti2ts
                    else df[self.P.text_field].values
                ),
            },
            self.P.feat,
            self.P.df_key,
            self.P.x_field,
        )

        if self.P.dynstd_method is True:
            ctx.drive_entity_dynstd(cds)
        elif self.P.dynstd_method:
            # 独自动态标准化
            ctx.add_dynstd(DynStd(cds, method=self.P.dynstd_method))

        fig.text(
            source=cds,
            color=self.P.color,
            text_alpha=self.P.alpha,
            #                 line_width=self.P.line_width,
            legend_label=label,
            name=label,
        )

        ctx.fit_ys(cds)


class DynamicGlyphPlot(BasePlotter):
    """
    Params:
        glyphs: 形状列表
        glyph_fields: 形状下标字段
        feats: 特征
        dfkeys: 特征数据中取 DataFrame 的键值
        legend_labels: 图例
            None为默认值,None代表使用品种名,也可以直接给列表
        colors: 颜色
            None 则使用品种颜色，也可以直接给列表
        xfields: 横轴时间字段名
            None 则使用 df 索引时间
        yfields: 纵轴数值字段名
        timefieldtype: 支持idx、ts、uti类型
        size_fields: 通过特征值指定图形大小
        size_scale_factor:
            * True - 使用预设缩放比例，若无预设则独立计算
            * 'set' - 计算缩放比例，并设为预设
            * 其它 - 独立计算缩放比例
        size_scale 图形大小的放大倍率
        size_base: 基础大小（防止过小的数据画了却看不到）
        size: 大小
        alphas: 透明度
        widgeter: BasePPChangeWidget 子类,用于实现如中尺度参数切换触发改变小尺度图
    """

    params = lambda: dict(
        glyphs=[
            "circle",
            "square",
            "triangle",  # 正三角
            "diamond",
            "cross",  # 十字
            "star",  # 五角星
            "x",  # 叉形
            "asterisk",  # 星花
            "inverted_triangle",
            "hex",  # 六边形
            "plus",  # + 号，细线
            "square_cross",
            "diamond_cross",
            "circle_cross",
            "triangle_dot",
            "square_dot",
            "diamond_dot",
            "circle_dot",
            "hex_dot",
            "star_dot",
            "circle_x",
            "square_x",
            "triangle_pin",
            "square_pin",
            "dash",
            "dot",
            "y",  # “Y” 形
            "circle_y",
        ],
        glyph_fields=[],
        feats=GMap(),
        dfkeys=[None],
        legend_labels=None,
        colors=[None],
        xfields=[None],
        yfields=[],
        timefieldtype="uti",
        size_fields=None,
        size_scale_factor=True,
        size_scale=100,
        size_base=5,
        size=5,
        alphas=0.6,
        # 动态标准化方法
        #   False: 不动态标准化
        #   True: 跟随品种价格动态标准化
        #   字符串:
        #     ratio 除法
        #     diff 减法
        #     ratio-back 反向除法
        #     diff-back 反向减法
        dynstd_method=True,
        hover_tslabel=True,
        widgeter=UnFree(Nothing),
    )

    def _plot_fig(self, ctx: PlotCtx):
        hover_tslabel = self.P.hover_tslabel

        gps = ctx.gps
        fig = ctx.figs[-1]

        sym = CurrSymbol.sym()
        tgt = currTarget()

        glyphs = self.P.glyphs
        for (
            feat,
            dfkey,
            xfield,
            yfield,
            size_field,
            glyph_field,
            label,
            color,
            alpha,
        ) in zip(
            self.feats.make_arr(),
            itertools.cycle(ensure_list(self.P.dfkeys)),
            itertools.cycle(ensure_list(self.P.xfields)),
            itertools.cycle(ensure_list(self.P.yfields)),
            itertools.cycle(ensure_list(self.P.size_fields)),
            itertools.cycle(ensure_list(self.P.glyph_fields)),
            itertools.cycle(ensure_list(self.P.legend_labels)),
            itertools.cycle(self.P.colors),
            itertools.cycle(ensure_list(self.P.alphas)),
        ):
            # 有些参数给了必须是有效值,通过这个字典实现默认情况下不给参数
            glyph_args = {}
            if label is not None:
                legend_label = f"{tgt} - {label}" if tgt else label
                glyph_args["legend_label"] = legend_label
                glyph_args["name"] = legend_label
            glyph_args["size"] = "size" if size_field else self.P.size

            def fd_trans(df_all):
                all_fd = {}
                for iv, df in df_all.groupby(glyph_field):
                    if iv < 0:
                        continue
                    all_fd[glyphs[iv]] = fd = {"y": df[yfield]}
                    if xfield:
                        if self.P.timefieldtype == "idx":
                            fd["x"] = ctx.idx2x(df[xfield], freq=feat.P.freq)
                            if hover_tslabel:
                                fd["ts"] = ctx.idx2tslabel(df[xfield])
                        elif self.P.timefieldtype == "ts":
                            fd["x"] = ctx.ts2x(
                                pd.to_datetime(df[xfield], errors="coerce")
                            )
                            if hover_tslabel:
                                fd["ts"] = ctx.ts2tslabel(pd.to_datetime(df[xfield]))
                        elif self.P.timefieldtype == "uti":
                            fd["x"] = ctx.uti2x(df[xfield].values)
                            if hover_tslabel:
                                fd["ts"] = ctx.uti2tslabel(df[xfield].values)
                        else:
                            raise RuntimeError("只支持idx、ts、uti这几种时间字段类型")
                    else:
                        tsa = df_idx0(df)
                        fd["x"] = ctx.ts2x(tsa)
                        if hover_tslabel:
                            fd["ts"] = ctx.ts2tslabel(tsa)

                    if size_field:
                        sd = df[size_field]
                        sz_scale_key = (sym, feat.ppid, size_field)
                        scale_factor = None
                        if self.P.size_scale_factor == "set":
                            scale_factor = size_scale_factor(
                                sd.min(), sd.max(), self.P.size_scale
                            )
                            SIZE_SCALE_FACTORS[sz_scale_key] = scale_factor
                        elif self.P.size_scale_factor is True:
                            scale_factor = SIZE_SCALE_FACTORS.get(sz_scale_key, None)
                        if scale_factor is None:
                            scale_factor = size_scale_factor(
                                sd.min(), sd.max(), self.P.size_scale
                            )
                        fd["size"] = scale_size_by_factor(
                            sd, self.P.size_base, scale_factor
                        )

                return all_fd

            if xfield and self.P.timefieldtype == "uti":
                all_cds = ctx.live_split_feat_data(
                    f"{label}: scatter({__class__.__name__})",
                    fd_trans,
                    feat,
                    dfkey,
                    xfield,
                    x_range=fig.x_range,
                    dynstd_ys=["y"],
                    widgeter=self.P.get("widgeter"),
                )
            else:
                all_cds = ctx.live_split_feat_data(
                    f"{label}: scatter({__class__.__name__})",
                    fd_trans,
                    feat,
                    dfkey,
                    None,
                    x_range=fig.x_range,
                    dynstd_ys=["y"],
                    widgeter=self.P.get("widgeter"),
                )

            for glyph, cds in all_cds.items():
                if self.P.dynstd_method is True:
                    ctx.drive_entity_dynstd(cds)
                elif self.P.dynstd_method:
                    # 独自动态标准化
                    ctx.add_dynstd(DynStd(cds, method=self.P.dynstd_method))

                ctx.add_hover(
                    fig.scatter(
                        marker=glyph,
                        source=cds,
                        color=color or next(ctx.sym_colors),
                        alpha=alpha,
                        **glyph_args,
                    ),
                    (label, "@ts @y" if hover_tslabel else "@y"),
                )

                ctx.fit_ys(cds)


class ObjsClustersPlot(BasePlotter):
    """
    Params:
        glyphs: 形状列表
        obj_in_cluster: 形状下标字段
        feat: 特征
        dfkey: 特征数据中取 DataFrame 的键值
        legend_label: 图例
            None为默认值,None代表使用品种名,也可以直接给列表
        color: 颜色
            None 则使用品种颜色，也可以直接给列表

        cluster_time = None, # 填具体字段，代表用df里的该字段名对应的uti数据作为分簇时间，不填就代表用事件occ发生时的时间作为分簇时间。实现上，实际上是`DynamicGlyphColorPlot`的`xfields`参数
        obj_id = "objId", # 对象在对象集里的序号(第n个对象这个n)，用df里这个字段名的数据。实现上，实际上是`DynamicGlyphColorPlot`的`yfields`参数
        obj_in_cluster = "clusterId", # 作为对象所属簇的序号(第n个簇的n)，用df里这个字段名的数据，实际上是`DynamicGlyphColorPlot`的`glyph_fields`参数
        legend_label = "板块中对象的分簇"
        # 其余的color, tiemfieldtype, size_field, size_scale_factor, size_scale, size_base, size, alphas, widgeter参数保持原来的填法和含义(color, size_field这俩参数，MulFieldsGlyphs里支持填个列表，代表多个图(Glyph)各自用的参数，但是这里没必要，只需要指定单个就行，因为分簇的这种展示方式本来就不太能展示得了多个图)

        timefieldtype: 支持idx、ts、uti类型
        size_field: 通过特征值指定图形大小
        size_scale_factor:
            * True - 使用预设缩放比例，若无预设则独立计算
            * 'set' - 计算缩放比例，并设为预设
            * 其它 - 独立计算缩放比例
        size_scale 图形大小的放大倍率
        size_base: 基础大小（防止过小的数据画了却看不到）
        size: 大小
        alpha: 透明度
        widgeter: BasePPChangeWidget 子类,用于实现如中尺度参数切换触发改变小尺度图
    """

    params = lambda: dict(
        glyphs=[
            "circle",
            "square",
            "triangle",  # 正三角
            "diamond",
            "cross",  # 十字
            "star",  # 五角星
            "x",  # 叉形
            "asterisk",  # 星花
            "inverted_triangle",
            "hex",  # 六边形
            "plus",  # + 号，细线
            "square_cross",
            "diamond_cross",
            "circle_cross",
            "triangle_dot",
            "square_dot",
            "diamond_dot",
            "circle_dot",
            "hex_dot",
            "star_dot",
            "circle_x",
            "square_x",
            "triangle_pin",
            "square_pin",
            "dash",
            "dot",
            "y",  # “Y” 形
            "circle_y",
        ],
        obj_in_cluster=None,
        feat=Nothing,
        dfkey=None,
        legend_label=None,
        color=None,
        cluster_time=None,
        obj_id=None,
        timefieldtype="uti",
        size_field=None,
        size_scale_factor=True,
        size_scale=100,
        size_base=5,
        size=5,
        alpha=0.6,
        # 动态标准化方法
        #   False: 不动态标准化
        #   True: 跟随品种价格动态标准化
        #   字符串:
        #     ratio 除法
        #     diff 减法
        #     ratio-back 反向除法
        #     diff-back 反向减法
        dynstd_method=True,
        hover_tslabel=True,
        widgeter=UnFree(Nothing),
    )

    def _plot_fig(self, ctx: PlotCtx):
        P = self.P0
        p = DynamicGlyphPlot(
            {
                "glyphs": P.glyphs,
                "glyph_fields": [P.obj_in_cluster],
                "feats": GMap.from_list([P.feat]),
                "dfkeys": [P.dfkey],
                "legend_labels": [P.legend_label],
                "colors": [P.color],
                "xfields": [P.cluster_time],
                "yfields": [P.obj_id],
                "timefieldtype": P.timefieldtype,
                "size_fields": [P.size_field],
                "size_scale_factor": P.size_scale_factor,
                "size_scale": P.size_scale,
                "size_base": P.size_base,
                "size": P.size,
                "alphas": [P.alpha],
                "dynstd_method": P.dynstd_method,
                "hover_tslabel": P.hover_tslabel,
                "widgeter": P.widgeter,
            }
        )
        p._plot_fig(ctx)


class DynamicColorPlot(BasePlotter):
    """
    Params:
        colors: 颜色列表
        color_fields: 形状下标字段
        glyphs: 形状
        feats: 特征
        dfkeys: 特征数据中取 DataFrame 的键值
        legend_labels: 图例
            None为默认值,None代表使用品种名,也可以直接给列表
            None 则使用品种颜色，也可以直接给列表
        xfields: 横轴时间字段名
            None 则使用 df 索引时间
        yfields: 纵轴数值字段名
        timefieldtype: 支持idx、ts、uti类型
        size_fields: 通过特征值指定图形大小
        size_scale_factor:
            * True - 使用预设缩放比例，若无预设则独立计算
            * 'set' - 计算缩放比例，并设为预设
            * 其它 - 独立计算缩放比例
        size_scale 图形大小的放大倍率
        size_base: 基础大小（防止过小的数据画了却看不到）
        size: 大小
        alphas: 透明度
        widgeter: BasePPChangeWidget 子类,用于实现如中尺度参数切换触发改变小尺度图
    """

    params = lambda: dict(
        colors=[
            "#1f77b4",  # 蓝
            "#ff7f0e",  # 橙
            "#2ca02c",  # 绿
            "#d62728",  # 红
            "#9467bd",  # 紫
            "#8c564b",  # 棕
            "#e377c2",  # 粉
            "#7f7f7f",  # 灰
            "#bcbd22",  # 橄榄
            "#17becf",  # 青
            "#393b79",  # 深蓝
            "#637939",  # 深绿
            "#8c6d31",  # 土黄
            "#843c39",  # 深棕红
            "#7b4173",  # 暗紫
            "#3182bd",  # 钢蓝
            "#e6550d",  # 砖橙
            "#31a354",  # 翡翠
            "#756bb1",  # 淡紫
            "#636363",  # 深灰
        ],
        color_fields=[],
        glyphs=["asterisk"],
        feats=GMap(),
        dfkeys=[None],
        legend_labels=None,
        xfields=[None],
        yfields=[],
        timefieldtype="uti",
        size_fields=None,
        size_scale_factor=True,
        size_scale=100,
        size_base=5,
        size=5,
        alphas=0.6,
        # 动态标准化方法
        #   False: 不动态标准化
        #   True: 跟随品种价格动态标准化
        #   字符串:
        #     ratio 除法
        #     diff 减法
        #     ratio-back 反向除法
        #     diff-back 反向减法
        dynstd_method=True,
        hover_tslabel=True,
        widgeter=UnFree(Nothing),
    )

    def _plot_fig(self, ctx: PlotCtx):
        hover_tslabel = self.P.hover_tslabel

        gps = ctx.gps
        fig = ctx.figs[-1]

        sym = CurrSymbol.sym()
        tgt = currTarget()

        colors = self.P.colors
        for (
            feat,
            dfkey,
            xfield,
            yfield,
            size_field,
            color_field,
            label,
            glyph,
            alpha,
        ) in zip(
            self.feats.make_arr(),
            itertools.cycle(ensure_list(self.P.dfkeys)),
            itertools.cycle(ensure_list(self.P.xfields)),
            itertools.cycle(ensure_list(self.P.yfields)),
            itertools.cycle(ensure_list(self.P.size_fields)),
            itertools.cycle(ensure_list(self.P.color_fields)),
            itertools.cycle(ensure_list(self.P.legend_labels)),
            itertools.cycle(self.P.glyphs),
            itertools.cycle(ensure_list(self.P.alphas)),
        ):
            # 有些参数给了必须是有效值,通过这个字典实现默认情况下不给参数
            glyph_args = {}
            if label is not None:
                legend_label = f"{tgt} - {label}" if tgt else label
                glyph_args["legend_label"] = legend_label
                glyph_args["name"] = legend_label
            glyph_args["size"] = "size" if size_field else self.P.size

            def fd_trans(df_all):
                all_fd = {}
                for iv, df in df_all.groupby(color_field):
                    if iv < 0:
                        continue
                    all_fd[colors[iv]] = fd = {"y": df[yfield]}
                    if xfield:
                        if self.P.timefieldtype == "idx":
                            fd["x"] = ctx.idx2x(df[xfield], freq=feat.P.freq)
                            if hover_tslabel:
                                fd["ts"] = ctx.idx2tslabel(df[xfield])
                        elif self.P.timefieldtype == "ts":
                            fd["x"] = ctx.ts2x(
                                pd.to_datetime(df[xfield], errors="coerce")
                            )
                            if hover_tslabel:
                                fd["ts"] = ctx.ts2tslabel(pd.to_datetime(df[xfield]))
                        elif self.P.timefieldtype == "uti":
                            fd["x"] = ctx.uti2x(df[xfield].values)
                            if hover_tslabel:
                                fd["ts"] = ctx.uti2tslabel(df[xfield].values)
                        else:
                            raise RuntimeError("只支持idx、ts、uti这几种时间字段类型")
                    else:
                        tsa = df_idx0(df)
                        fd["x"] = ctx.ts2x(tsa)
                        if hover_tslabel:
                            fd["ts"] = ctx.ts2tslabel(tsa)

                    if size_field:
                        sd = df[size_field]
                        sz_scale_key = (sym, feat.ppid, size_field)
                        scale_factor = None
                        if self.P.size_scale_factor == "set":
                            scale_factor = size_scale_factor(
                                sd.min(), sd.max(), self.P.size_scale
                            )
                            SIZE_SCALE_FACTORS[sz_scale_key] = scale_factor
                        elif self.P.size_scale_factor is True:
                            scale_factor = SIZE_SCALE_FACTORS.get(sz_scale_key, None)
                        if scale_factor is None:
                            scale_factor = size_scale_factor(
                                sd.min(), sd.max(), self.P.size_scale
                            )
                        fd["size"] = scale_size_by_factor(
                            sd, self.P.size_base, scale_factor
                        )

                return all_fd

            if xfield and self.P.timefieldtype == "uti":
                all_cds = ctx.live_split_feat_data(
                    f"{label}: scatter({__class__.__name__})",
                    fd_trans,
                    feat,
                    dfkey,
                    xfield,
                    x_range=fig.x_range,
                    dynstd_ys=["y"],
                    widgeter=self.P.get("widgeter"),
                )
            else:
                all_cds = ctx.live_split_feat_data(
                    f"{label}: scatter({__class__.__name__})",
                    fd_trans,
                    feat,
                    dfkey,
                    None,
                    x_range=fig.x_range,
                    dynstd_ys=["y"],
                    widgeter=self.P.get("widgeter"),
                )

            for color, cds in all_cds.items():
                if self.P.dynstd_method is True:
                    ctx.drive_entity_dynstd(cds)
                elif self.P.dynstd_method:
                    # 独自动态标准化
                    ctx.add_dynstd(DynStd(cds, method=self.P.dynstd_method))

                ctx.add_hover(
                    fig.scatter(
                        marker=glyph,
                        source=cds,
                        color=color,
                        alpha=alpha,
                        **glyph_args,
                    ),
                    (label, "@ts @y" if hover_tslabel else "@y"),
                )

                ctx.fit_ys(cds)
