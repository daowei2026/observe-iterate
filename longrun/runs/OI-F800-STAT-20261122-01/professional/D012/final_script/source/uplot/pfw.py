"""
Plotting Framework

"""

__all__ = [
    "ensure_list",
    "DynStd",
    "CurrWidgets",
    "PlotCtx",
    "BasePPChangeWidget",
    "BasePlotter",
]

from typing import *
import traceback

from collections import *

import time
import os.path
import itertools

import numpy as np
import pandas as pd
from numba import njit

from m3 import *
from m3v import *

from mquant.frame import *
from mquant.frame.lib3 import *

from .core import *
from .pdt import *

from mquant.quant.stra import TrialOptimizer


def ensure_list(vs):
    if isinstance(vs, (list, tuple)):
        return vs
    return [vs]


class DynStd:
    """
    动态标准化数据集合

    每个 fig 可能关联多个动态标准化数据集，因为一个 fig 的 x_range 变动事件需要延迟响应（不然会有过多不必要重复计算），需要收集所有关于一个 fig 的动态标准化数据集，注册到一个 JS Handler 合并处理。

    """

    def __init__(
        self,
        base_cds: bkh.ColumnDataSource,
        method: str = "diff",
        base_x: str = "x",
        base_y: str = "y",
        extra_ys: Sequence[str] = (),
    ):
        base_cds.data[f"__prestd_{base_y}"] = base_cds.data[base_y]

        self.base_cds = base_cds
        self.method = method
        self.base_x = base_x
        self.base_y = base_y
        self.extra_ys = extra_ys
        for y in extra_ys:
            base_cds.data[f"__prestd_{y}"] = base_cds.data[y]
        self.driven_list = []

    def drive(
        self, cds: bkh.ColumnDataSource, xy_pairs: list[tuple[str, str]] = [("x", "y")]
    ):
        for x, y in xy_pairs:
            cds.data[f"__prestd_{y}"] = cds.data[y]

        self.driven_list.append((cds, xy_pairs))


class CurrWidgets(AbsContextManager):
    """
    Manager for current widgets in context

    """

    __slots__ = "_all_figs", "_live_ctrls", "_live_updaters", "_upd_btn", "_plot_roots"

    def __init__(
        self,
        all_figs=None,
        live_ctrls=None,
        live_updaters=None,
        manual_upd=True,
        plot_roots: Optional[list[PlotDataFolder]] = None,
    ):
        self._all_figs = all_figs if all_figs is not None else []
        self._live_ctrls = live_ctrls if live_ctrls is not None else {}
        self._live_updaters = live_updaters if live_updaters is not None else {}
        assert isinstance(self._all_figs, list)
        assert isinstance(self._live_ctrls, dict)
        assert isinstance(self._live_updaters, dict)

        if isinstance(manual_upd, bkh.Button):
            self._upd_btn = manual_upd
        elif isinstance(manual_upd, str):
            self._upd_btn = bkh.Button(label=manual_upd)
        elif manual_upd:
            self._upd_btn = bkh.Button(label="更新")
        else:
            self._upd_btn = None
        assert self._upd_btn is None or isinstance(self._upd_btn, bkh.Button)

        self._plot_roots = plot_roots if plot_roots is not None else []
        assert isinstance(self._plot_roots, list)

    def __iter__(self):
        yield self._all_figs
        yield self._live_ctrls
        yield self._upd_btn

    def __repr__(self):
        return f"CurrWidgets#{len(self._all_figs)}#{len(self._live_ctrls)}#"

    @classmethod
    def all_figs(cls, required=True):
        curr = cls.get(required=required)
        if curr is None:
            return None
        return curr._all_figs

    @classmethod
    def live_ctrls(cls, required=True):
        curr = cls.get(required=required)
        if curr is None:
            return None
        return curr._live_ctrls

    @classmethod
    def live_updaters(cls, required=True):
        curr = cls.get(required=required)
        if curr is None:
            return None
        return curr._live_updaters

    @classmethod
    def upd_btn(cls, required=True):
        curr = cls.get(required=required)
        if curr is None:
            return None
        return curr._upd_btn

    @classmethod
    def plot_roots(cls, required=True):
        curr = cls.get(required=required)
        if curr is None:
            return None
        return curr._plot_roots

    @classmethod
    def reset_live_ctrls(cls):
        curr = cls.get(required=True)
        live_ctrls, upd_btn = curr._live_ctrls.copy(), curr._upd_btn
        curr._live_ctrls.clear()
        curr._live_updaters.clear()
        if upd_btn:
            curr._upd_btn = bkh.Button(label=upd_btn.label)
        return live_ctrls, upd_btn


class PlotCtx:
    """
    绘图上下文，各种 Plotter 有可能往这个类的对象增加属性

    并且为（指定时间段的）一个图，进行（源于特征的）画图数据截取和转换

    """

    x_range = None
    sym_color = "black"
    sym_colors = iter(itertools.repeat("blue"))

    def __init__(
        self,
        plot_root: PlotDataFolder,
        plotset_name: str,
        calendar_name,
        sof,
        all_symbols,
        blk,
        gps,
        start_time,
        end_time,
        span_info=[],
        data=None,
    ):
        # TODO validate all gps values
        assert (not gps.extra_time) or pd.to_timedelta("0h") <= pd.to_timedelta(
            gps.extra_time
        ) <= pd.to_timedelta("60d"), f"extra_time = {gps.extra_time} ?!"

        self.calendar_name = calendar_name
        self.sof = sof
        self.all_symbols = all_symbols
        self.blk = blk
        self.gps = gps

        self.start_time = start_time
        self.end_time = end_time
        self.span_info = span_info

        if calendar_name == "@":
            assert len(all_symbols) == 1, "calendar_name 只能在单品种时指定为 @"
            calendar_name = next(iter(all_symbols))
        utsa = sof.tsa_of(calendar_name)["natural_tsa"]

        try:
            start_uti, end_uti = int(start_time), int(end_time) + 1
        except (ValueError, TypeError):
            start_uti, end_uti = timesearch(
                utsa, pd.to_datetime([start_time, end_time])
            )
            end_uti += 1
        if gps.extra_time:
            extra_time_ut = int(pd.to_timedelta(gps.extra_time).value // 500e6)
            start_uti -= extra_time_ut
            end_uti += extra_time_ut
        start_uti = max(0, start_uti)
        end_uti = min(utsa.size, end_uti)
        label_uti_span = int(Freq(gps.x_label_freq).span // 500e6)
        label_utis = np.arange(
            start_uti // label_uti_span * label_uti_span,
            min(utsa.size, end_uti + label_uti_span),
            label_uti_span,
            dtype=np.intp,
        )
        label_strs = pd.to_datetime(utsa[label_utis]).strftime("%F %H:%M")

        self.utsa = utsa
        self.uti_slice = slice(start_uti, end_uti)
        self.time_range = slice(*utsa[[start_uti, min(utsa.size - 1, end_uti)]])
        self.x_labels = {uti: label for uti, label in zip(label_utis, label_strs)}

        self.data = data

        self.plot_folder = PlotDataFolder(
            f"{plotset_name} {self.time_range.start!s} ~ {self.time_range.stop!s}"
        )
        plot_root.children.append(self.plot_folder)

        self.figs = []
        self.dynstd_list = []
        self.entities_dynstd = {}

        self.hovers = defaultdict(list)

        self.y_fits = []

    def push_folder(self, name: str):
        curr_folder = PlotDataFolder(name)
        prev_folder = self.plot_folder
        prev_folder.children.append(curr_folder)
        try:
            self.plot_folder = curr_folder
            yield curr_folder
        finally:
            self.plot_folder = prev_folder

    def add_cds(
        self, name: str, cds: bkh.ColumnarDataSource, data_fetch_time, data_trans_time
    ):
        self.plot_folder.children.append(
            PlotDataNode(name, cds, data_fetch_time, data_trans_time)
        )

    def fit_ys(self, cds, x="x", y="y", *ys):
        self.y_fits.append((cds, x, [y, *ys]))

    def dynstd_by_entity(self, eid):
        if not eid:
            return None
        return self.entities_dynstd.get(eid)

    def drive_entity_dynstd(
        self, cds: bkh.ColumnDataSource, xy_pairs: list[tuple[str, str]] = [("x", "y")]
    ):
        dynstd = self.dynstd_by_entity(CurrEntity.id)
        if not dynstd:
            return
        dynstd.drive(cds, xy_pairs)

    def add_hover(self, glyph, tooltip=("Label:", "$name"), **hover_args):
        glyphs = self.hovers[(tooltip, tuple(hover_args.items()))]
        if isinstance(glyph, (list, tuple)):
            glyphs.extend(glyph)
        else:
            glyphs.append(glyph)

    def realize_hovers(self, fig):
        for (tooltip, hover_args), glyphs in self.hovers.items():
            hover = HoverTool(tooltips=[tooltip], **dict(hover_args))
            hover.renderers = glyphs
            fig.add_tools(hover)
        self.hovers.clear()

    def add_dynstd(self, dynstd):
        if dynstd is not None:
            self.dynstd_list.append(dynstd)
            eid = CurrEntity.id
            if eid is not None:
                self.entities_dynstd[eid] = dynstd

    def realize_dynstd(self):
        if not self.dynstd_list:
            return

        fig = self.figs[-1]
        with open(f"{os.path.dirname(__file__)}/dynstd.js", "r") as jsf:
            dynstd_js = jsf.read()
        fxr = fig.x_range
        jsh = bkh.CustomJS(
            args=dict(
                fig=fig,
                dynstd_list=[vars(ds) for ds in self.dynstd_list],
            ),
            code=dynstd_js,
        )
        fxr.js_on_change("start", jsh)
        fxr.js_on_change("end", jsh)

        self.dynstd_list = []

    def realize_static_dynstd(self):
        """Apply standardization to all dynstd_list entries once in Python"""
        if not self.dynstd_list:
            return

        for dynstd in self.dynstd_list:
            base_cds = dynstd.base_cds
            method = dynstd.method
            base_y = dynstd.base_y
            extra_ys = dynstd.extra_ys

            if f"__prestd_{base_y}" in base_cds.data:
                del base_cds.data[f"__prestd_{base_y}"]
            for y in extra_ys:
                if f"__prestd_{y}" in base_cds.data:
                    del base_cds.data[f"__prestd_{y}"]

            # Process base y data directly
            y_data = base_cds.data[base_y]
            bl = np.nan  # baseline value

            if method in ("diff", "diff-back"):
                # Find baseline value and apply standardization
                if method == "diff":
                    first_idx, bl = _find_first_valid(np_array(y_data))
                    if np.isfinite(bl):
                        y_data[first_idx:] -= bl
                        # Process extra ys
                        for y in extra_ys:
                            base_cds.data[y][first_idx:] -= bl
                else:  # diff-back
                    last_idx, bl = _find_last_valid(np_array(y_data))
                    if np.isfinite(bl):
                        y_data[: last_idx + 1] -= bl
                        # Process extra ys
                        for y in extra_ys:
                            base_cds.data[y][: last_idx + 1] -= bl

            elif method in ("ratio", "ratio-back"):
                # Find baseline value and apply standardization
                if method == "ratio":
                    first_idx, bl = _find_first_valid(np_array(y_data))
                    if np.isfinite(bl):
                        y_data[first_idx:] /= bl
                        # Process extra ys
                        for y in extra_ys:
                            base_cds.data[y][first_idx:] /= bl
                else:  # ratio-back
                    last_idx, bl = _find_last_valid(np_array(y_data))
                    if np.isfinite(bl):
                        y_data[: last_idx + 1] /= bl
                        # Process extra ys
                        for y in extra_ys:
                            base_cds.data[y][: last_idx + 1] /= bl

            # Process driven CDS entries
            for cds, xy_pairs in dynstd.driven_list:
                for x, y in xy_pairs:
                    if x not in cds.data or y not in cds.data:
                        continue

                    if f"__prestd_{y}" in cds.data:
                        del cds.data[f"__prestd_{y}"]
                    y_driven = cds.data[y]

                    # Find valid range and apply standardization
                    if method.endswith("-back"):
                        driven_idx, _ = _find_last_valid(np_array(y_driven))
                        if driven_idx >= 0 and np.isfinite(bl):
                            if method.startswith("diff"):
                                y_driven[: driven_idx + 1] -= bl
                            else:  # ratio
                                y_driven[: driven_idx + 1] /= bl
                    else:
                        driven_idx, _ = _find_first_valid(np_array(y_driven))
                        if driven_idx >= 0 and np.isfinite(bl):
                            if method.startswith("diff"):
                                y_driven[driven_idx:] -= bl
                            else:  # ratio
                                y_driven[driven_idx:] /= bl

        self.dynstd_list = []

    def show_live_ctrls(self):
        live_ctrls, upd_btn = CurrWidgets.reset_live_ctrls()
        if not live_ctrls:
            return
        items = []
        if upd_btn:
            items.append(upd_btn)
        for _ctrl, widget in live_ctrls.values():
            items.append(widget)
        self.figs.append(bkh.Column(children=items))

    def uti2x(self, uti):
        if uti.dtype.kind == "f":
            uti = np.where(np.isfinite(uti), uti.astype(np.intp), 0)
        return uti

    def ts2x(self, tsa):
        return timesearch(
            self.utsa,
            (
                tsa.values
                if isinstance(tsa, pd.Series)
                else np.array(tsa, self.utsa.dtype)
            ),
        )

    def idx2x(self, idxs, freq):
        kb = kline_msb(CurrSymbol.sym(True), freq, self.sof)
        return timesearch(
            self.utsa,
            kb.tsa[
                (idxs.values if isinstance(idxs, pd.Series) else idxs).astype(np.intp)
            ],
        )

    def x_range_ts(self, xr):
        utsa = self.utsa
        if np.isfinite(xr.start):
            ts_start = utsa[max(0, int(np.floor(xr.start)))]
        else:
            ts_start = None
        if np.isfinite(xr.end):
            ts_end = utsa[min(len(utsa) - 1, int(np.ceil(xr.end)))]
        else:
            ts_end = None
        return ts_start, ts_end

    def uti2tslabel(self, uti, fmt="%F %H:%M"):
        if uti.dtype.kind == "f":
            uti = np.where(np.isfinite(uti), uti.astype(np.intp), 0)
        return pd.to_datetime(self.utsa[uti]).strftime(fmt)

    def ts2tslabel(self, tsa, fmt="%F %H:%M"):
        return pd.to_datetime(tsa).strftime(fmt)

    def idx2tslabel(self, idxs, freq, fmt="%F %H:%M"):
        kb = kline_msb(CurrSymbol.sym(True), freq, self.sof)
        return pd.to_datetime(
            kb.tsa[
                (idxs.values if isinstance(idxs, pd.Series) else idxs).astype(np.intp)
            ]
        ).strftime(fmt)

    @property
    def uti_range(self):
        slc = self.uti_slice
        return np.arange(slc.start, slc.stop)

    def slice_natural_df(self, df, extra_n=0):
        if df.shape[0] < 1:
            return df

        utsa = self.utsa
        uti1 = self.uti_slice.start
        uti2 = min(utsa.size - 1, self.uti_slice.stop)

        tsa = df_idx0(df)
        start_i, end_i = timesearch(tsa, utsa[[uti1, uti2]])
        start_i = max(0, start_i - extra_n)
        end_i = min(tsa.size, end_i + 1 + extra_n)

        sdf = df.iloc[start_i:end_i, :]
        return sdf.assign(uti=timesearch(utsa, df_idx0(sdf)))

    def feat_data(
        self, plot_name, gen_cols, feat, df_key=None, uti1_field=None, uti2_field=None
    ):
        if "calendar_name" in feat.P:
            if feat.P.calendar_name != self.calendar_name:
                print(
                    f"！！特征的日历与画图日历 {self.calendar_name!s} 不匹配！！ {feat!r}"
                )

        t0 = time.perf_counter()
        if isinstance(feat, pd.DataFrame):
            full_df = feat
        elif isinstance(feat, TrialOptimizer):
            full_df = feat.rerun().equity
        elif not df_key:
            full_df = feat.rerun().to_df()
        else:
            full_df = feat.rerun().to_dfs()[df_key]

        t1 = time.perf_counter()

        if uti1_field is None:
            feat_df = self.slice_natural_df(full_df)
        else:
            start_i, end_i = uti_slice(
                full_df[uti1_field],
                full_df[uti2_field or uti1_field],
                self.uti_slice.start,
                self.uti_slice.stop,
            )
            feat_df = full_df.iloc[start_i:end_i, :]
        dd = gen_cols(feat_df)

        t2 = time.perf_counter()

        # from IPython import get_ipython

        # ipy_ns = get_ipython().user_ns
        # ipy_ns.update(locals())

        cds = bkh.ColumnDataSource(dd)
        self.add_cds(plot_name, cds, t1 - t0, t2 - t1)
        return cds

    def live_feat_data(
        self,
        plot_name,
        gen_cols,
        feat,
        df_key=None,
        uti1_field=None,
        uti2_field=None,
        x_range=None,
        dynstd_ys=[],
        widgeter=Nothing,
    ):
        cds = bkh.ColumnDataSource({})

        def update_cds_from(tt):
            if isinstance(tt, TrialOptimizer):
                full_df = tt.equity
            elif not df_key:
                full_df = tt.to_df()
            else:
                full_df = tt.to_dfs()[df_key]

            if uti1_field is None:
                feat_df = self.slice_natural_df(full_df)
            elif full_df[uti1_field].is_monotonic_increasing:
                start_i, end_i = uti_slice(
                    full_df[uti1_field],
                    full_df[uti2_field or uti1_field],
                    self.uti_slice.start,
                    self.uti_slice.stop,
                )
                feat_df = full_df.iloc[start_i:end_i, :]
            else:
                uti1_ds = full_df[uti1_field].values
                feat_df = full_df.iloc[
                    (uti1_ds >= self.uti_slice.start) & (uti1_ds < self.uti_slice.stop),
                    :,
                ]
                if uti2_field:
                    uti2_ds = feat_df[uti2_field]
                    feat_df = feat_df.iloc[
                        (uti2_ds >= self.uti_slice.start)
                        & (uti2_ds < self.uti_slice.stop),
                        :,
                    ]
            dd = gen_cols(feat_df)
            for y in dynstd_ys:
                if y in dd:
                    dd[f"__prestd_{y}"] = dd[y]
            cds.data = dd

            if x_range:
                x_range.start = x_range.start - 0.001  # to trigger dynstd

            # from IPython import get_ipython

            # ipy_ns = get_ipython().user_ns
            # ipy_ns.update(locals())

        live_updaters = CurrWidgets.live_updaters()
        live_updater = live_updaters.get(feat.that)
        if not live_updater:
            live_updaters[feat.that] = live_updater = LiveUpdater(
                feat, widgeter=widgeter
            )
        data_fetch_time, data_trans_time = live_updater.drive(update_cds_from)

        self.add_cds(plot_name, cds, data_fetch_time, data_trans_time)
        return cds

    def live_split_feat_data(
        self,
        plot_name,
        gen_cols,
        feat,
        df_key=None,
        uti1_field=None,
        uti2_field=None,
        x_range=None,
        dynstd_ys=[],
        widgeter=Nothing,
    ):
        all_cds = {}

        def update_cds_from(tt):
            if isinstance(tt, TrialOptimizer):
                full_df = tt.equity
            elif not df_key:
                full_df = tt.to_df()
            else:
                full_df = tt.to_dfs()[df_key]

            if uti1_field is None:
                feat_df = self.slice_natural_df(full_df)
            elif full_df[uti1_field].is_monotonic_increasing:
                start_i, end_i = uti_slice(
                    full_df[uti1_field],
                    full_df[uti2_field or uti1_field],
                    self.uti_slice.start,
                    self.uti_slice.stop,
                )
                feat_df = full_df.iloc[start_i:end_i, :]
            else:
                uti1_ds = full_df[uti1_field].values
                feat_df = full_df.iloc[
                    (uti1_ds >= self.uti_slice.start) & (uti1_ds < self.uti_slice.stop),
                    :,
                ]
                if uti2_field:
                    uti2_ds = feat_df[uti2_field]
                    feat_df = feat_df.iloc[
                        (uti2_ds >= self.uti_slice.start)
                        & (uti2_ds < self.uti_slice.stop),
                        :,
                    ]

            for dk, dd in gen_cols(feat_df).items():
                for y in dynstd_ys:
                    if y in dd:
                        dd[f"__prestd_{y}"] = dd[y]
                cds = all_cds.get(dk)
                if cds is None:
                    cds = bkh.ColumnDataSource(dd)
                    all_cds[dk] = cds
                else:
                    cds.data = dd

            if x_range:
                x_range.start = x_range.start - 0.001  # to trigger dynstd

            # from IPython import get_ipython

            # ipy_ns = get_ipython().user_ns
            # ipy_ns.update(locals())

        live_updaters = CurrWidgets.live_updaters()
        live_updater = live_updaters.get(feat.that)
        if not live_updater:
            live_updaters[feat.that] = live_updater = LiveUpdater(
                feat, widgeter=widgeter
            )
        data_fetch_time, data_trans_time = live_updater.drive(update_cds_from)

        for _dk, cds in all_cds.items():
            self.add_cds(plot_name, cds, data_fetch_time, data_trans_time)
        return all_cds


@njit(nogil=True)
def _uti_slice(uti1, uti2, start_uti, end_uti):
    assert uti1.ndim == uti2.ndim == 1
    assert uti1.shape == uti2.shape

    start_i = 0
    while start_i < uti1.size:
        if uti1[start_i] >= start_uti:
            break
        start_i += 1
    end_i = uti2.size
    while end_i - 1 >= 0:
        if uti2[end_i - 1] < end_uti:
            break
        end_i -= 1

    return start_i, end_i


@njit(nogil=True)
def _find_first_valid(arr):
    n = arr.size
    for i in range(n):
        if np.isfinite(arr[i]):
            return i, arr[i]
    return -1, np.nan


@njit(nogil=True)
def _find_last_valid(arr):
    n = arr.size
    for i in range(n - 1, -1, -1):
        if np.isfinite(arr[i]):
            return i, arr[i]
    return -1, np.nan


def _uti_array(a):
    if isinstance(a, (pd.Series, pd.Index)):
        if a.dtype.name.startswith("Int"):
            # possibly masked IntegerArray
            return a.to_numpy(dtype="f8")
        return a.values
    # todo other cases?
    return a


def uti_slice(uti1, uti2, start_uti, end_uti):
    return _uti_slice(_uti_array(uti1), _uti_array(uti2), int(start_uti), int(end_uti))


class BasePPChangeWidget(DoFunctionFao):
    """
    Author: King
    Since : 2025-05-06 14:46
    Desc  :
        - 参数范围改变,自定义组件
    """

    __abstract_fao__ = True

    def create_widget(self, get_fao: callable):
        """get_fao 获取当前选择参数的特征对象"""
        pass


class LiveUpdater:
    def __init__(self, feat, widgeter=Nothing):
        self.cbs = []

        live_ctrls = CurrWidgets.live_ctrls()
        upd_btn = CurrWidgets.upd_btn()
        feat_ctrls, single_vals = {}, {}

        def update_cds():
            dd = {**single_vals}
            for k, live_ctrl in feat_ctrls.items():
                v = live_ctrl[0].value
                dd[k] = eval(v) if isinstance(v, str) else v
            self.tt = eval_pprange(dd)
            for cb, sof, blk, cale, sym in self.cbs:
                with CurrTradeSet(sof), CurrIndustry(blk):
                    if cale is None:
                        if sym is None:
                            cb(self.tt.rerun())
                        else:
                            with CurrSymbol(sym), CurrSymbolPable(sym):
                                cb(self.tt.rerun())
                    else:
                        with CurrCalendar(cale):
                            if sym is None:
                                cb(self.tt.rerun())
                            else:
                                with CurrSymbol(sym), CurrSymbolPable(sym):
                                    cb(self.tt.rerun())
            if upd_btn:
                upd_btn.disabled = True

        for k, vs in OPIterator(Pable.doPaShareGroup(feat)[0]).params.items():
            live_ctrl = live_ctrls.get(k, None)
            if live_ctrl is not None:
                pass
            elif isinstance(vs, (prange, paxis, paxis4step, paxis4ratio)):
                slider = bkh.Slider(
                    title=str(k),
                    value=vs.start,
                    start=vs.start,
                    end=vs.stop - vs.step,
                    step=vs.step,
                )
                widget = slider
                doc = feat.getFieldDoc(k)
                if doc:
                    widget = bkh.row(
                        slider,
                        bkh.Div(
                            text=f"<b>{doc}</b>",
                            styles={"display": "flex", "align-items": "flex-end"},
                        ),
                    )
                live_ctrls[k] = live_ctrl = [slider, widget]
            elif isinstance(vs, (plist, pbox)):
                options = [repr(v) for v in vs]
                if len(options) == 1:
                    single_vals[k] = next(iter(vs))
                elif options:
                    slider = bkh.CategoricalSlider(
                        title=str(k), value=options[0], categories=options
                    )
                    widget = slider
                    doc = feat.getFieldDoc(k)
                    if doc:
                        widget = bkh.row(
                            slider,
                            bkh.Div(
                                text=f"<b>{doc}</b>",
                                styles={"display": "flex", "align-items": "flex-end"},
                            ),
                        )
                    live_ctrls[k] = live_ctrl = [slider, widget]
            else:
                raise ValueError(f"Unsupported param range: {type(vs)}")
            if not live_ctrl:
                continue  # single value

            feat_ctrls[k] = live_ctrl

            if upd_btn is None:

                def on_widget_change(attrname, old, new):
                    # print(f"Applying widget {attrname} change: {old} => {new}")
                    try:
                        update_cds()
                        # print(f"Widget {attrname} change applied: {old} => {new}")
                    except:
                        print(f"Widget {attrname} change failed: {old} => {new}")
                        traceback.print_exc()

                live_ctrl[0].on_change("value_throttled", on_widget_change)

            else:

                def on_widget_change(attrname, old, new):
                    upd_btn.disabled = False

                def on_upd_btn():
                    try:
                        update_cds()
                    except:
                        traceback.print_exc()

                live_ctrl[0].on_change("value", on_widget_change)
                upd_btn.on_click(on_upd_btn)

        # 存在范围参数时，添加自定义组件
        if isinstance(widgeter, BasePPChangeWidget) and live_ctrls:

            def _get_fao():
                return self.tt

            live_ctrls["__custom__"] = widgeter.create_widget(_get_fao)

        update_cds()

    def drive(self, cb):
        t0 = time.perf_counter()
        full_data = self.tt.rerun()
        t1 = time.perf_counter()
        cb(full_data)
        t2 = time.perf_counter()

        self.cbs.append(
            (
                cb,
                CurrTradeSet.sof(),
                CurrIndustry.blk_expr(),
                CurrCalendar.name(False),
                CurrSymbol.sym(),
            )
        )

        return t1 - t0, t2 - t1


class BasePlotter(PlotterMixIn, DoFunctionFao):

    def _plot_fig(self, ctx: PlotCtx):
        raise NotImplementedError()
