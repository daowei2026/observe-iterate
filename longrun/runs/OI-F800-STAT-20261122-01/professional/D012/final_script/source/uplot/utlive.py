"""
Unified Time Live Plotting

"""

__all__ = [
    "LiveTradePlot",
    "LiveTrader",
    "LiveKPriceLine",
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

from m3bdp.lib import MongoDataClient

from .core import *
from .pfw import *
from .pdt import *

from .utkv2 import *


class LiveKPriceLine(BasePlotter):
    """
    统一时间轴 K 线

    """

    params = lambda: dict(
        feat=KLine(),
        extra_bars=0,  # 额外多画这么多个 bar
        add_hover=True,
        color=None,
        alpha=0.8,  # 透明度
        label="K",
        mongo_param={
            "ip": "localhost",
            "port": 27017,
            "r_database": "TestTradeFrp",
            "r_collection": "record",
            "k_database": "basic_feat_ctp",
        },
    )

    def _plot_fig(self, ctx: PlotCtx):
        gps = ctx.gps
        fig = ctx.figs[-1]

        sym = CurrSymbol.sym()
        calendar_name = CurrCalendar.name()

        legend_label = f"{sym} - {self.P.label}"

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

        async def live_update_cds():
            try:
                mdc = MongoDataClient(
                    self.P.mongo_param.ip,
                    self.P.mongo_param.port,
                    self.P.mongo_param.k_database,
                    True,
                )
                mdc._conn()
                coll_name = (
                    f"kline_{sym}_{self.feat.P.freq}"
                    if calendar_name == "@"
                    else f"kline_{sym}_{calendar_name}_{self.feat.P.freq}"
                )
                coll = mdc.get_coll(coll_name)
                async with coll.watch([], full_document="updateLookup") as stream:
                    async for chevt in stream:
                        if "fullDocument" not in chevt:
                            continue
                        doc = chevt["fullDocument"]
                        kdata = {}
                        kdata["open"] = doc["open"]
                        if doc["fn"] == "open":
                            kdata["high"] = doc["open"]
                            kdata["low"] = doc["open"]
                            kdata["close"] = doc["open"]
                        else:
                            kdata["high"] = doc["high"]
                            kdata["low"] = doc["low"]
                            kdata["close"] = doc["close"]
                            kdata["closeTs"] = doc["closeTs"]
                            kdata["closeUti"] = doc["closeUti"]
                        kdata["volume"] = doc["volume"]
                        kdata["openInt"] = doc["openInt"]
                        kdata["openTs"] = doc["openTs"]
                        kdata["openUti"] = doc["openUti"]

                        # Convert timestamps to x coordinates using ctx.ts2x()
                        open_x = ctx.ts2x(pd.to_datetime([kdata["openTs"]]))[0]

                        # For open bars, closeTs might not be available
                        if "closeTs" in kdata:
                            close_x = ctx.ts2x(pd.to_datetime([kdata["closeTs"]]))[0]
                        else:
                            # Estimate close_x based on bar width from previous bar
                            prev_bar_width = (
                                close_uti[close_uti.size - 1]
                                - open_uti[open_uti.size - 1]
                            )
                            close_x = open_x + prev_bar_width

                        # Calculate x coordinates following the same pattern as the original code
                        x_shift = (close_x - open_x) / 2  # 到中间位置的偏移量
                        h_width = x_shift * 0.8  # 横把儿的宽度

                        new_x = open_x + x_shift  # 中心位置
                        new_x_l = new_x - h_width  # 左侧位置
                        new_x_r = new_x + h_width  # 右侧位置

                        # Format timestamp for the new data point
                        new_ts = pd.to_datetime(kdata["openTs"]).strftime("%F %H:%M")

                        # Create new data dictionary for streaming
                        new_data = {
                            "x": [new_x],
                            "x_l": [new_x_l],
                            "x_r": [new_x_r],
                            "open": [kdata["open"]],
                            "high": [kdata["high"]],
                            "low": [kdata["low"]],
                            "close": [kdata["close"]],
                            "volume": [kdata["volume"]],
                            "ts": [new_ts],
                        }

                        # Use stream() to efficiently add the new data point
                        # Use Bokeh's add_next_tick_callback for thread-safe updates
                        cds.document.add_next_tick_callback(
                            lambda: cds.stream(new_data)
                        )
            except:
                self.logger.error("Live KLine data update error!", exc_info=True)

        asyncio.create_task(live_update_cds())


class LiveTrader(BaseCAEFao):

    params = lambda: {
        "mongo_param": {
            "ip": "localhost",
            "port": 27017,
            "r_database": "TestTradeFrp",
            "r_collection": "record",
        },
    }

    def live_tx_cds(self, ctx: PlotCtx):
        sof = ctx.sof

        sym = CurrSymbol.sym()
        calendar_name = CurrCalendar.name()

        # 模拟交易记录数据 TODO: load reall current data
        records = {
            "openTs": [
                "2020-01-06 09:58:00.500000+00:00",
                "2020-04-13 14:06:00.500000+00:00",
                "2020-07-28 09:00:00.500000+00:00",
            ],
            "closeTs": [
                "2020-01-06 10:00:00.500000+00:00",
                "2020-04-13 14:08:00.500000+00:00",
                "2020-07-28 14:30:00.500000+00:00",
            ],
            "openPrice": [3533, 3412, 3675],
            "closePrice": [3534, 3408, 3680],
            "lots": [1, 3, -5],
        }

        # 获取当前交易数据
        df = pd.DataFrame(records)

        # 计算每笔交易的盈亏
        # 多头: 盈亏 = (平仓价 - 开仓价) * 手数
        # 空头: 盈亏 = (开仓价 - 平仓价) * 手数
        df["profit"] = np.where(
            df["lots"] > 0,  # 多头
            (df["closePrice"] - df["openPrice"]) * df["lots"],
            (df["openPrice"] - df["closePrice"]) * abs(df["lots"]),  # 空头
        )

        # 分类交易记录
        long_trades = df[df["lots"] > 0]
        short_trades = df[df["lots"] < 0]

        # 创建cds数据
        def create_tx_cds(trades_df: pd.DataFrame):
            if trades_df.shape[0] < 1:
                cds_data = cds_data = {
                    "x0": [],
                    "x1": [],
                    "openPrice": [],
                    "closePrice": [],
                    "lots": [],
                    "lotsText": [],
                    "profit": [],
                }
            else:
                # 使用ctx.ts2x()将自然时间转为ut x值
                x0 = ctx.ts2x(pd.to_datetime(trades_df["openTs"]))
                x1 = ctx.ts2x(pd.to_datetime(trades_df["closeTs"]))

                cds_data = {
                    "x0": x0,
                    "x1": x1,
                    "openPrice": trades_df["openPrice"].values,
                    "closePrice": trades_df["closePrice"].values,
                    "lots": trades_df["lots"].values,
                    "lotsText": trades_df["lots"].map("[{:.1f}]".format),
                    "profit": trades_df["profit"].values,
                }

            return bkh.ColumnDataSource(cds_data)

        # 创建四种交易类型的cds
        tx_long_win = create_tx_cds(long_trades[long_trades["profit"] > 0])
        tx_long_loss = create_tx_cds(long_trades[long_trades["profit"] <= 0])
        tx_short_win = create_tx_cds(short_trades[short_trades["profit"] > 0])
        tx_short_loss = create_tx_cds(short_trades[short_trades["profit"] <= 0])

        async def live_update_cds():
            try:
                mdc = MongoDataClient(
                    self.P.mongo_param.ip,
                    self.P.mongo_param.port,
                    self.P.mongo_param.r_database,
                    True,
                )
                mdc._conn()
                coll = mdc.get_coll(self.P.mongo_param.r_collection)
                async with coll.watch([], full_document="updateLookup") as stream:
                    async for chevt in stream:
                        if "fullDocument" not in chevt:
                            continue
                        doc = chevt["fullDocument"]
                        record = {}
                        record["symbol"] = doc["symbol"]
                        record["direction"] = doc["direction"]
                        record["lots"] = doc["lots"]
                        record["openTs"] = doc["openTs"]
                        record["openPrice"] = doc["openPrice"]
                        record["openLots"] = doc["openLots"]
                        record["closeTs"] = doc["closeTs"]
                        record["closePrice"] = doc["closePrice"]
                        record["closeLots"] = doc["closeLots"]
                        record["localTs"] = doc["localTs"]

                        # 计算盈亏
                        if record["lots"] > 0:  # 多头
                            profit = (
                                record["closePrice"] - record["openPrice"]
                            ) * record["lots"]
                        else:  # 空头
                            profit = (record["openPrice"] - record["closePrice"]) * abs(
                                record["lots"]
                            )
                        record["profit"] = profit

                        # 确定交易类型并选择对应的cds
                        if record["lots"] > 0:  # 多头
                            if profit > 0:
                                target_cds = tx_long_win
                            else:
                                target_cds = tx_long_loss
                        else:  # 空头
                            if profit > 0:
                                target_cds = tx_short_win
                            else:
                                target_cds = tx_short_loss

                        # 如果目标cds存在，则增量更新
                        if target_cds is not None:
                            # 转换时间戳为x坐标
                            x0 = ctx.ts2x(pd.to_datetime([record["openTs"]]))[0]
                            x1 = ctx.ts2x(pd.to_datetime([record["closeTs"]]))[0]

                            # 创建新数据点
                            new_data = {
                                "x0": [x0],
                                "x1": [x1],
                                "openPrice": [record["openPrice"]],
                                "closePrice": [record["closePrice"]],
                                "lots": [record["lots"]],
                                "lotsText": ["[{:.1f}]".format(record["lots"])],
                                "profit": [profit],
                            }

                            # 使用stream方法增量更新cds
                            # Use Bokeh's add_next_tick_callback for thread-safe updates
                            target_cds.document.add_next_tick_callback(
                                lambda: target_cds.stream(new_data)
                            )
            except:
                self.logger.error("Live TX data update error!", exc_info=True)

        asyncio.create_task(live_update_cds())

        return (tx_long_win, tx_long_loss, tx_short_win, tx_short_loss)


class LiveTradePlot(BasePlotter):

    params = lambda: dict(
        traders=GMapX(
            {
                "default": LiveTrader(),
            }
        ),
        colors=[],
        legend_labels=[],
        trade_volume=True,
    )

    def _plot_fig(self, ctx: PlotCtx):
        fig = ctx.figs[-1]
        sym = CurrSymbol.sym()

        for trader, label, tx_color in zip(
            self.traders.make_arr(),
            self.P.legend_labels or list(self.traders.keys()),
            itertools.cycle(self.P.colors or [cs[1] for cs in ctx.gps.colors2]),
        ):
            if label is None:
                label = repr(trader)

            # 通过 trader 加载各种交易的 cds，实时更新
            (
                tx_long_win_cds,
                tx_long_loss_cds,
                tx_short_win_cds,
                tx_short_loss_cds,
            ) = trader.live_tx_cds(ctx)

            # 多向盈利交易
            fig.scatter(
                marker="triangle",
                source=tx_long_win_cds,
                x="x0",
                y="openPrice",
                color=tx_color,
                size=14,
                legend_label=label,
            )
            fig.segment(
                source=tx_long_win_cds,
                y0="openPrice",
                y1="closePrice",
                color=tx_color,
                line_width=2,
                legend_label=label,
            )
            fig.scatter(
                marker="triangle_dot",
                source=tx_long_win_cds,
                x="x1",
                y="closePrice",
                color=tx_color,
                size=14,
                legend_label=label,
            )
            if self.P.trade_volume:
                fig.text(
                    source=tx_long_win_cds,
                    x="x1",
                    y="closePrice",
                    text="lotsText",
                    color=tx_color,
                    text_font_size="9pt",
                    text_align="center",
                    text_baseline="top",
                    y_offset=7,  # 此参数值为屏幕单位，正负与数据空间的偏移方向相反
                    legend_label=f"{sym} 平仓量 - {label}",
                )

            # 多向亏损交易
            fig.scatter(
                marker="triangle",
                source=tx_long_loss_cds,
                x="x0",
                y="openPrice",
                color=tx_color,
                size=14,
                legend_label=label,
            )
            fig.segment(
                source=tx_long_loss_cds,
                y0="openPrice",
                y1="closePrice",
                color=tx_color,
                line_width=2,
                line_dash="dashed",
                legend_label=label,
            )
            fig.scatter(
                marker="triangle_dot",
                source=tx_long_loss_cds,
                x="x1",
                y="closePrice",
                color=tx_color,
                size=14,
                legend_label=label,
            )
            if self.P.trade_volume:
                fig.text(
                    source=tx_long_loss_cds,
                    x="x1",
                    y="closePrice",
                    text="lotsText",
                    color=tx_color,
                    text_font_size="9pt",
                    text_align="center",
                    text_baseline="top",
                    y_offset=7,  # 此参数值为屏幕单位，正负与数据空间的偏移方向相反
                    legend_label=f"{sym} 平仓量 - {label}",
                )

            # 空向盈利交易
            fig.scatter(
                marker="star",
                source=tx_short_win_cds,
                x="x0",
                y="openPrice",
                color=tx_color,
                size=14,
                legend_label=label,
            )
            fig.segment(
                source=tx_short_win_cds,
                y0="openPrice",
                y1="closePrice",
                color=tx_color,
                line_width=2,
                legend_label=label,
            )
            fig.scatter(
                marker="star_dot",
                source=tx_short_win_cds,
                x="x1",
                y="closePrice",
                color=tx_color,
                size=14,
                legend_label=label,
            )
            if self.P.trade_volume:
                fig.text(
                    source=tx_short_win_cds,
                    x="x1",
                    y="closePrice",
                    text="lotsText",
                    color=tx_color,
                    text_font_size="9pt",
                    text_align="center",
                    text_baseline="top",
                    y_offset=7,  # 此参数值为屏幕单位，正负与数据空间的偏移方向相反
                    legend_label=f"{sym} 平仓量 - {label}",
                )

            # 空向亏损交易
            fig.scatter(
                marker="star",
                source=tx_short_loss_cds,
                x="x0",
                y="openPrice",
                color=tx_color,
                size=14,
                legend_label=label,
            )
            fig.segment(
                source=tx_short_loss_cds,
                y0="openPrice",
                y1="closePrice",
                color=tx_color,
                line_width=2,
                line_dash="dashed",
                legend_label=label,
            )
            fig.scatter(
                marker="star_dot",
                source=tx_short_loss_cds,
                x="x1",
                y="closePrice",
                color=tx_color,
                size=14,
                legend_label=label,
            )
            if self.P.trade_volume:
                fig.text(
                    source=tx_short_loss_cds,
                    x="x1",
                    y="closePrice",
                    text="lotsText",
                    color=tx_color,
                    text_font_size="9pt",
                    text_align="center",
                    text_baseline="top",
                    y_offset=7,  # 此参数值为屏幕单位，正负与数据空间的偏移方向相反
                    legend_label=f"{sym} 平仓量 - {label}",
                )
