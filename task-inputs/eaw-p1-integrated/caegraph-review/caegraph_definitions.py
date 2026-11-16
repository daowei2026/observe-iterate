"""三类 CAEGraph 的实际定义及必需绘图辅助代码。

本文件包含长期概览、30m/1m/5s 组合、Tick 多品种主附图的定义。
不导入 mquant.aidata；数据由相邻 snapshot_data.py 从包内 data/ 读取。
"""
from __future__ import annotations
import hashlib
import json
import math
import time
from pathlib import Path
from typing import Any, Callable
from contextlib import contextmanager, ExitStack
from contextvars import ContextVar
from dataclasses import dataclass, field
from functools import wraps
from types import SimpleNamespace
import numpy as np
import pandas as pd
from bokeh.models import ColumnDataSource, GlyphRenderer
from m3tt import CurrSymbol
from mquant.frame import CalType, DataFrameMixIn, FAnyParam, GeneralSymbolFao, GMap, GMapX, Nothing
from mquant.uplot import AllSymsFig, AllSymsMainFig, BasePlotter, CAEGraph, MulFieldsGlyphs, PlotSet, VBarPlot
from snapshot_data import SnapshotFeature, SnapshotContext, bundle


DEFAULT_DF_KEY = "__default__"

_EVIDENCE_SURFACES = ("overview", "big", "mid", "small", "tick")

_PLOT_BINDING_KEYS = {
    "kind",
    "surfaces",
    "label",
    "group",
    "visible",
    "x_field",
    "y_field",
    "x0_field",
    "x1_field",
    "y0_field",
    "y1_field",
    "style",
    "hover_fields",
    "text_field",
    "text_format",
    "text_surfaces",
}

_PLOT_STYLE_KEYS = {
    "marker",
    "marker_field",
    "color",
    "color_field",
    "size",
    "size_field",
    "size_scale",
    "size_base",
    "alpha",
    "alpha_field",
    "line_width",
    "line_width_field",
    "line_dash",
    "line_dash_field",
}

def normalize_df_key(value: Any) -> str:
    """把空 df_key 统一成路径安全的默认 token。"""
    return DEFAULT_DF_KEY if value in (None, "") else str(value)

def sha1_text(value: str) -> str:
    """对文本计算 SHA1。"""
    return hashlib.sha1(value.encode("utf-8")).hexdigest()

def feature_repr(anchor_or_feature: Any) -> str:
    """抽取 feature 的可读表示，用于 hash 和 manifest。"""
    if isinstance(anchor_or_feature, dict):
        return str(anchor_or_feature.get("feature_repr") or repr(anchor_or_feature.get("feature")))
    return repr(anchor_or_feature)

def feature_ppid(anchor_or_feature: Any) -> str:
    """读取 Fao/Pable 自身身份；aidata 不重新定义 feature 身份。"""
    feature = anchor_or_feature.get("feature") if isinstance(anchor_or_feature, dict) else anchor_or_feature
    try:
        ppid = getattr(feature, "ppid", "")
    except Exception:
        ppid = ""
    return "" if ppid in (None, "") else str(ppid)

def feature_identity_hash(anchor_or_feature: Any) -> str:
    """基于 Fao ppid 优先、repr 兜底的身份 hash。"""
    ppid = feature_ppid(anchor_or_feature)
    return sha1_text(ppid or feature_repr(anchor_or_feature))

def feature_tar_type(anchor_or_feature: Any) -> Any:
    """读取 feature 自身 tar_type；读取失败时返回 None。

    aidata 不让用户重复填写 feature 的目标类型，而是尽量沿用 Fao
    已经表达的目标语义。
    """
    feature = anchor_or_feature.get("feature") if isinstance(anchor_or_feature, dict) else anchor_or_feature
    if feature is None:
        return None
    try:
        return getattr(feature, "tar_type", None)
    except Exception:
        return None

def feature_target_scope(anchor_or_feature: Any) -> str:
    """根据 Fao tar_type 推断 aidata rerun scope。

    返回值只用于 aidata 内部调度：
    - symbol: 按板块成员品种逐个进入 CurrSymbol rerun。
    - board: 在 CurrIndustry 下 rerun 一次。
    - feature: 不额外展开，使用当前 runtime 上下文 rerun 一次。
    """
    tar_type = feature_tar_type(anchor_or_feature)
    if tar_type is None:
        return "feature"
    try:
        if tar_type.isSymbol():
            return "symbol"
    except Exception:
        pass
    try:
        if tar_type.isAskBlockSymbol():
            return "symbol"
    except Exception:
        pass
    try:
        if tar_type.isBlock():
            return "board"
    except Exception:
        pass
    return "feature"

def normalize_plot_binding(binding: dict[str, Any] | None) -> dict[str, Any]:
    """规范化 feature 自己声明的通用证据画法。

    显式声明 point/line/segment 和字段；自然时间索引使用 x_field="__index__"。
    """
    if not binding:
        return {}
    if not isinstance(binding, dict):
        raise ValueError("plot_binding 必须是 dict")

    out = dict(binding)
    kind = out.get("kind")
    if kind not in {"point", "line", "segment"}:
        raise ValueError(f"plot_binding.kind 仅支持 'point'、'line' 或 'segment'，收到 {kind!r}")

    unknown = sorted(set(out) - _PLOT_BINDING_KEYS)
    if unknown:
        raise ValueError(f"plot_binding 含不支持字段: {unknown}")

    required = (
        ("x_field", "y_field")
        if kind in {"point", "line"}
        else ("x0_field", "x1_field", "y0_field", "y1_field")
    )
    missing = [field for field in required if not str(out.get(field) or "").strip()]
    if missing:
        raise ValueError(f"plot_binding.kind={kind!r} 缺少字段: {missing}")

    raw_surfaces = out.get("surfaces", list(_EVIDENCE_SURFACES))
    surfaces = [raw_surfaces] if isinstance(raw_surfaces, str) else list(raw_surfaces)
    normalized_surfaces: list[str] = []
    for raw in surfaces:
        surface = str(raw)
        if surface not in _EVIDENCE_SURFACES:
            raise ValueError(f"plot_binding.surfaces 含不支持尺度: {surface!r}")
        if surface not in normalized_surfaces:
            normalized_surfaces.append(surface)
    if not normalized_surfaces:
        raise ValueError("plot_binding.surfaces 不能为空")
    out["surfaces"] = normalized_surfaces

    visible = out.get("visible", True)
    if isinstance(visible, dict):
        unknown_surfaces = sorted(set(visible) - set(_EVIDENCE_SURFACES))
        if unknown_surfaces:
            raise ValueError(f"plot_binding.visible 含不支持尺度: {unknown_surfaces}")
        out["visible"] = {
            surface: bool(visible.get(surface, True))
            for surface in _EVIDENCE_SURFACES
        }
    else:
        out["visible"] = {surface: bool(visible) for surface in _EVIDENCE_SURFACES}

    style = out.get("style") or {}
    if not isinstance(style, dict):
        raise ValueError("plot_binding.style 必须是 dict")
    unknown_style = sorted(set(style) - _PLOT_STYLE_KEYS)
    if unknown_style:
        raise ValueError(f"plot_binding.style 含不支持字段: {unknown_style}")
    out["style"] = dict(style)
    if out.get("text_field"):
        if kind not in {"point", "line"} or out.get("text_format", "plain") not in {"plain", "uti"}:
            raise ValueError("文本标注只支持 point/line，text_format 只支持 plain/uti")
        if set(out.get("text_surfaces", surfaces)) - set(_EVIDENCE_SURFACES):
            raise ValueError("text_surfaces 含不支持尺度")

    hover_fields = out.get("hover_fields") or []
    if not isinstance(hover_fields, (list, tuple)):
        raise ValueError("plot_binding.hover_fields 必须是 list")
    normalized_hover: list[dict[str, str]] = []
    for index, item in enumerate(hover_fields):
        if isinstance(item, str):
            normalized_hover.append({"field": item, "label": item, "format": ""})
            continue
        if not isinstance(item, dict) or not str(item.get("field") or "").strip():
            raise ValueError(f"plot_binding.hover_fields[{index}] 必须提供 field")
        extra = sorted(set(item) - {"field", "label", "format"})
        if extra:
            raise ValueError(f"plot_binding.hover_fields[{index}] 含不支持字段: {extra}")
        field = str(item["field"])
        normalized_hover.append(
            {
                "field": field,
                "label": str(item.get("label") or field),
                "format": str(item.get("format") or ""),
            }
        )
    out["hover_fields"] = normalized_hover
    out["label"] = str(out.get("label") or "证据")
    out["group"] = str(out.get("group") or "evidence")
    return out

def feature_df(anchor: dict[str, Any], runtime: dict[str, Any] | None = None) -> pd.DataFrame:
    """按 anchor rerun feature，并取 `to_df()` 或 `to_dfs()[df_key]`。"""
    feature = anchor.get("feature")
    if feature is None:
        raise ValueError(f"anchor {anchor.get('feature_key')!r} 缺少 feature 对象")
    with feature_runtime(anchor, runtime):
        run = feature.rerun()
        df_key = normalize_df_key(anchor.get("df_key"))
        if df_key == "__default__":
            return run.to_df()
        return run.to_dfs()[df_key]

@contextmanager
def feature_runtime(anchor: dict[str, Any], runtime: dict[str, Any] | None = None):
    """为 feature rerun 临时设置 mquant runtime 上下文。"""
    if not runtime:
        yield
        return
    try:
        from mquant.frame.lib3 import CurrSymbol, CurrTradeSet
        from mquant.frame.lang import CurrCalendar, CurrIndustry, CurrSymbolPable
    except Exception:
        yield
        return
    context = runtime.get("context")
    blk = anchor.get("target_id") if feature_target_scope(anchor) == "board" and anchor.get("target_id") else runtime.get("blk")
    calendar_name = runtime.get("calendar_name")
    with ExitStack() as stack:
        if context is not None and hasattr(context, "sof"):
            stack.enter_context(CurrTradeSet(context.sof))
        if blk:
            stack.enter_context(CurrIndustry(blk))
        if calendar_name:
            stack.enter_context(CurrCalendar(calendar_name))
        if feature_target_scope(anchor) == "symbol" and anchor.get("target_id") not in (None, "", "unknown"):
            stack.enter_context(CurrSymbol(anchor["target_id"]))
            stack.enter_context(CurrSymbolPable(anchor["target_id"]))
        yield

def plotctx_uti_window(start: Any, end: Any, runtime: dict[str, Any] | None = None) -> tuple[int, int] | None:
    """把 PlotCtx 风格 timespan 解析成半开 UTI 窗口。"""
    try:
        return int(start), int(end) + 1
    except (TypeError, ValueError):
        pass

    context = (runtime or {}).get("context")
    calendar_name = (runtime or {}).get("calendar_name")
    if context is None or not hasattr(context, "sof") or not calendar_name:
        return None

    try:
        from mquant.uplot.core import timesearch
    except Exception:
        return None

    utsa = context.sof.tsa_of(calendar_name)["natural_tsa"]
    start_uti, end_uti = timesearch(utsa, pd.to_datetime([start, end]))
    return int(start_uti), int(end_uti) + 1

def slice_natural_df_like_plotctx(
    df: pd.DataFrame,
    uti_window: tuple[int, int],
    runtime: dict[str, Any] | None = None,
    *,
    extra_n: int = 0,
) -> pd.DataFrame:
    """按 uplot / PlotCtx 方式切 natural-index dataframe。"""
    if df.shape[0] < 1:
        return df.copy()
    context = (runtime or {}).get("context")
    calendar_name = (runtime or {}).get("calendar_name")
    if context is None or not hasattr(context, "sof") or not calendar_name:
        return df.copy()
    try:
        from mquant.uplot.core import df_idx0, timesearch
    except Exception:
        return df.copy()

    utsa = context.sof.tsa_of(calendar_name)["natural_tsa"]
    start_uti, end_uti = uti_window
    uti2 = min(utsa.size - 1, end_uti)
    tsa = df_idx0(df)
    start_i, end_i = timesearch(tsa, utsa[[start_uti, uti2]])
    start_i = max(0, int(start_i) - extra_n)
    end_i = min(tsa.size, int(end_i) + 1 + extra_n)
    sliced = df.iloc[start_i:end_i, :].copy()
    if "uti" not in sliced.columns:
        sliced = sliced.assign(uti=timesearch(utsa, df_idx0(sliced)))
    return sliced

def _base_plotter():
    from mquant.uplot import BasePlotter

    return BasePlotter

@dataclass
class _CachedFrame:
    start_uti: int
    end_uti: int
    frame: pd.DataFrame

@dataclass
class _PageEvidenceCache:
    frames: dict[tuple[str, str, str], _CachedFrame] = field(default_factory=dict)

_CURRENT_PAGE_CACHE: ContextVar[_PageEvidenceCache | None] = ContextVar(
    "aidata_evidence_page_cache",
    default=None,
)

@contextmanager
def evidence_page_session():
    """把十年稀疏源的派生结果限制在单个 Bokeh 页面生命周期内。"""
    token = _CURRENT_PAGE_CACHE.set(_PageEvidenceCache())
    try:
        yield
    finally:
        _CURRENT_PAGE_CACHE.reset(token)

def evidence_page_cached(func: Callable[..., Any]) -> Callable[..., Any]:
    """给 CAE ``layout`` 建立并在返回前释放页面级证据缓存。"""

    @wraps(func)
    def wrapped(*args: Any, **kwargs: Any):
        with evidence_page_session():
            return func(*args, **kwargs)

    return wrapped

class EvidencePlotter(_base_plotter()):
    """只解释 point/line/segment 通用合同，不包含任何业务特征名。"""

    params = lambda: {
        # uplot 参数树要求可被替换的 Fao 参数拥有 Fao 默认值；None 会被
        # 解释成不能继续下钻的普通值。Nothing 是现有通用 Plotter 的惯例。
        "feature": Nothing,
        "anchor": {},
        "surface": "small",
    }

    def _plot_fig(self, ctx: Any):
        anchor = dict(self.P.anchor)
        # GMapX 会复制 Plotter 参数；业务 Feature 作为顶层参数传递，与已有
        # KPriceLine 等 Plotter 的 feat 参数保持同一种运行时对象语义。通用
        # 配置仍放在 anchor 中，进入读取层前再把两者组合起来。
        anchor["feature"] = self.P.feature
        binding = normalize_plot_binding(anchor.get("plot_binding") or {})
        surface = str(self.P.surface)
        if not _binding_enabled(binding, surface):
            return

        start_uti = int(ctx.uti_slice.start)
        end_uti = int(ctx.uti_slice.stop)
        started = time.perf_counter()
        frame = read_evidence_frame(
            anchor,
            start_uti=start_uti,
            end_uti=end_uti,
        )
        fetched = time.perf_counter()
        if frame.empty:
            return
        if binding.get("x_field") == "__index__":
            frame = ctx.slice_natural_df(frame)
        size_field = (binding.get("style") or {}).get("size_field")
        if size_field:
            _require_columns(frame, [size_field], label="point size")
            frame = frame.dropna(subset=[size_field])
        if frame.empty:
            return
        source_data = _source_data(frame, binding, index_to_uti=ctx.ts2x)
        if surface == "overview" and binding["kind"] in {"point", "line"}:
            source_data = _clip_before_market_start(source_data, ctx)
            if not len(source_data["x"]):
                return
        if binding.get("text_field"):
            values = source_data[binding["text_field"]]
            source_data["text"] = ctx.uti2tslabel(values) if binding.get("text_format") == "uti" else values
        transformed = time.perf_counter()

        from bokeh.models import ColumnDataSource

        cds = ColumnDataSource(source_data)
        ctx.add_cds(
            f"evidence/{anchor.get('anchor_name', anchor.get('df_key', 'unknown'))}",
            cds,
            fetched - started,
            transformed - fetched,
        )
        label = _entity_label(str(binding.get("label") or anchor.get("label") or "证据"), anchor)
        renderer = _render_evidence(
            ctx.figs[-1],
            cds,
            anchor=anchor,
            binding=binding,
            surface=surface,
            label=label,
            default_color=next(ctx.sym_colors),
        )
        if renderer is None:
            return
        if binding["kind"] in {"point", "line"}:
            ctx.drive_entity_dynstd(cds, [("x", "y")])
            ctx.fit_ys(cds, "x", "y")
        else:
            ctx.drive_entity_dynstd(cds, [("x0", "y0"), ("x1", "y1")])
            ctx.fit_ys(cds, "x0", "y0", "y1")

def evidence_plotters(anchors: list[dict[str, Any]], surface: str) -> list[Any]:
    """为指定现有尺度返回可追加到 entity plot list 的通用 plotter。"""
    return [
        EvidencePlotter(
            feature=anchor.get("feature"),
            anchor={key: value for key, value in anchor.items() if key != "feature"},
            surface=surface,
        )
        for anchor in anchors or []
        if _binding_enabled(normalize_plot_binding(anchor.get("plot_binding") or {}), surface)
    ]

def add_tick_evidence(
    fig: Any,
    anchors: list[dict[str, Any]],
    *,
    symbol: str,
    start_uti: int,
    end_uti: int,
    dynstd: Any,
    runtime: dict[str, Any],
) -> list[Any]:
    """把同一通用合同叠加到现有 half-second tick 主图。"""
    from bokeh.models import ColumnDataSource

    renderers: list[Any] = []
    for anchor in anchors or []:
        if feature_target_scope(anchor) == "board":
            continue
        binding = normalize_plot_binding(anchor.get("plot_binding") or {})
        if not _binding_enabled(binding, "tick"):
            continue
        frame = read_evidence_frame(
            anchor,
            start_uti=start_uti,
            end_uti=end_uti,
            runtime=runtime,
            symbol=symbol,
        )
        if frame.empty:
            continue
        if binding.get("x_field") == "__index__":
            frame = slice_natural_df_like_plotctx(frame, (start_uti, end_uti), runtime)
        size_field = (binding.get("style") or {}).get("size_field")
        if size_field:
            _require_columns(frame, [size_field], label="point size")
            frame = frame.dropna(subset=[size_field])
        if frame.empty:
            continue
        def index_to_uti(index):
            from mquant.uplot.core import timesearch
            utsa = runtime["context"].sof.tsa_of(runtime["calendar_name"])["natural_tsa"]
            return timesearch(utsa, index)

        source = _source_data(frame, binding, index_to_uti=index_to_uti)
        if binding.get("text_field"):
            values = source[binding["text_field"]]
            if binding.get("text_format") == "uti":
                utsa = runtime["context"].sof.tsa_of(runtime["calendar_name"])["natural_tsa"]
                values = pd.to_datetime(utsa[np.asarray(values, dtype=np.intp)]).strftime("%F %H:%M")
            source["text"] = values
        cds = ColumnDataSource(source)
        renderer = _render_evidence(
            fig,
            cds,
            anchor=anchor,
            binding=binding,
            surface="tick",
            label=f"{symbol} - {binding.get('label') or anchor.get('label') or '证据'}",
        )
        if renderer is None:
            continue
        if binding["kind"] in {"point", "line"}:
            dynstd.drive(cds, [("x", "y")])
        else:
            dynstd.drive(cds, [("x0", "y0"), ("x1", "y1")])
        renderers.append(renderer)
    return renderers

def read_evidence_frame(
    anchor: dict[str, Any],
    *,
    start_uti: int,
    end_uti: int,
    runtime: dict[str, Any] | None = None,
    symbol: str | None = None,
) -> pd.DataFrame:
    """按页缓存 feature view，再切成当前图窗；不会调用 ``rerun(2)``。"""
    feature = anchor.get("feature")
    if feature is None:
        raise ValueError(f"evidence anchor {anchor.get('anchor_name')!r} 缺少 feature")
    if end_uti <= start_uti:
        return pd.DataFrame()

    # 生命周期区间可能在图窗边界结束；使用该窗口的原始快照，避免合并其他窗的延长版本。
    window_reader = getattr(feature, 'window_snapshot', None)
    if callable(window_reader):
        frame = window_reader(start_uti, end_uti)
        if frame is not None:
            return frame.copy()

    resolved_symbol = str(anchor.get("target_id") or (symbol if feature_target_scope(anchor) == "symbol" else "") or _current_target(anchor))
    df_key = normalize_df_key(anchor.get("df_key"))
    cache_key = (feature_identity_hash(feature), df_key, resolved_symbol)
    cache = _CURRENT_PAGE_CACHE.get()
    cached = cache.frames.get(cache_key) if cache is not None else None
    if cached is None or start_uti < cached.start_uti or end_uti > cached.end_uti:
        load_start = min(start_uti, cached.start_uti) if cached is not None else start_uti
        load_end = max(end_uti, cached.end_uti) if cached is not None else end_uti
        loaded = _load_feature_view(
            anchor,
            start_uti=load_start,
            end_uti=load_end,
            runtime=runtime,
            symbol=resolved_symbol,
        )
        cached = _CachedFrame(load_start, load_end, loaded)
        if cache is not None:
            cache.frames[cache_key] = cached

    return _slice_evidence_frame(
        cached.frame,
        anchor.get("time_binding") or {},
        start_uti=start_uti,
        end_uti=end_uti,
    )

def _load_feature_view(
    anchor: dict[str, Any],
    *,
    start_uti: int,
    end_uti: int,
    runtime: dict[str, Any] | None,
    symbol: str,
) -> pd.DataFrame:
    feature = anchor["feature"]
    df_key = normalize_df_key(anchor.get("df_key"))
    view_reader = getattr(feature, "evidence_view_df", None)
    scoped_anchor = dict(anchor)
    if symbol:
        scoped_anchor["target_id"] = symbol

    with feature_runtime(scoped_anchor, runtime):
        if callable(view_reader):
            frame = view_reader(
                None if df_key == "__default__" else df_key,
                start_uti=int(start_uti),
                end_uti=int(end_uti),
            )
        else:
            # 普通 Feature 使用标准 DataFrame 读取，不强制重算上游。
            frame = feature_df(scoped_anchor, runtime=None)
    if not isinstance(frame, pd.DataFrame):
        raise TypeError(
            f"evidence feature {feature!r} 的 {df_key!r} 视图必须返回 DataFrame"
        )
    return frame

def _slice_evidence_frame(
    frame: pd.DataFrame,
    time_binding: dict[str, Any],
    *,
    start_uti: int,
    end_uti: int,
) -> pd.DataFrame:
    if frame.empty:
        return frame.copy()
    mode = time_binding.get("time_mode")
    if mode == "index_natural":
        # 交给 PlotCtx 切片，保留其邻接行及窗口内强度缩放口径。
        return frame.copy()
    if mode == "uti_interval":
        left = str(time_binding.get("uti1_field") or "")
        right = str(time_binding.get("uti2_field") or "")
        _require_columns(frame, [left, right], label="interval time_binding")
        mask = (frame[left].to_numpy() < end_uti) & (frame[right].to_numpy() >= start_uti)
        return frame.iloc[mask].copy()
    if mode == "uti_point":
        fields = time_binding.get("uti_fields") or [time_binding.get("uti1_field")]
        field = str(fields[0] or "")
        _require_columns(frame, [field], label="point time_binding")
        values = frame[field].to_numpy()
        return frame.iloc[(values >= start_uti) & (values < end_uti)].copy()
    raise ValueError(
        f"通用 evidence renderer 只支持 uti_point/uti_interval，收到 {mode!r}"
    )

def _source_data(frame: pd.DataFrame, binding: dict[str, Any], *, index_to_uti=None) -> dict[str, Any]:
    kind = binding["kind"]
    if kind == "line":
        # 确认记录的索引顺序不一定等于实际转折顺序；仅整理绘图副本。
        frame = (frame.sort_index(kind="stable") if binding["x_field"] == "__index__"
                 else frame.sort_values(binding["x_field"], kind="stable"))
    geometry = (
        {
            "x": binding["x_field"],
            "y": binding["y_field"],
        }
        if kind in {"point", "line"}
        else {
            "x0": binding["x0_field"],
            "x1": binding["x1_field"],
            "y0": binding["y0_field"],
            "y1": binding["y1_field"],
        }
    )
    style = binding.get("style") or {}
    fields = [field for field in geometry.values() if field != "__index__"]
    if binding.get("text_field"):
        fields.append(binding["text_field"])
    fields.extend(
        str(value)
        for key, value in style.items()
        if key.endswith("_field") and value not in (None, "")
    )
    fields.extend(str(item["field"]) for item in binding.get("hover_fields") or [])
    _require_columns(frame, list(dict.fromkeys(fields)), label="plot_binding")

    data = {
        field: _column_values(frame[field])
        for field in dict.fromkeys(fields)
    }
    for alias, field in geometry.items():
        if field == "__index__":
            if index_to_uti is None:
                raise ValueError("自然时间索引绘图需要当前日历的 UTI 映射")
            values = np.asarray(index_to_uti(frame.index.values))
        else:
            values = _column_values(frame[field])
        # Static DynStd mutates display y columns in place.  Keep those aliases
        # independent from the raw hover field and from each other: an interval
        # such as a horizontal wall maps both y0 and y1 to plot_price, and a
        # shared ndarray would otherwise be standardized twice.
        data[alias] = values.copy() if alias in {"y", "y0", "y1"} else values
    if style.get("size_field") and "size_scale" in style:
        from mquant.uplot.core.utils import scale_size
        data["evidence_size"] = scale_size(data[style["size_field"]], style.get("size_base", 5), style["size_scale"])
    return data

def _column_values(series: pd.Series) -> Any:
    if pd.api.types.is_string_dtype(series.dtype) or series.dtype == object:
        return series.fillna("").astype(str).to_numpy()
    return series.to_numpy(copy=False)

def _clip_before_market_start(data: dict[str, Any], ctx: Any) -> dict[str, Any]:
    """只过滤概览坐标；起点取当前实体实际可渲染的日 K 线，不改特征记录。"""
    from mquant.frame.lib3 import CurrEntity

    lookup = getattr(ctx, "dynstd_by_entity", None)
    dynstd = lookup(CurrEntity.id) if callable(lookup) else None
    if dynstd is None:
        return data
    market = dynstd.base_cds.data
    if not {"ts", "open", "high", "low", "close"}.issubset(market):
        return data
    valid = (np.isfinite(market["open"]) | np.isfinite(market["close"])
             | (np.isfinite(market["high"]) & np.isfinite(market["low"])))
    indices = np.flatnonzero(valid)
    keep = np.zeros(len(data["x"]), dtype=bool)
    if len(indices):
        first = indices[0]
        # KLine 的自然时间索引是收盘时点，KPriceLine 的 x 是开收盘中点。
        # 从两者还原开盘位置，保留首根 K 线内部的真实转折。
        first_ts = pd.to_datetime([market["ts"][first]]).to_numpy()
        close = ctx.ts2x(first_ts)[0]
        start = 2 * market[dynstd.base_x][first] - close
        keep = np.asarray(data["x"]) >= start
    return {key: np.asarray(values)[keep] for key, values in data.items()}

def _render_evidence(
    fig: Any,
    cds: Any,
    *,
    anchor: dict[str, Any],
    binding: dict[str, Any],
    surface: str,
    label: str,
    default_color: str = "#9467BD",
) -> Any | None:
    style = binding.get("style") or {}
    visible = bool((binding.get("visible") or {}).get(surface, True))
    if binding["kind"] == "point":
        renderer = fig.scatter(
            source=cds,
            x="x",
            y="y",
            marker=_style_value(style, "marker", "circle"),
            color=_style_value(style, "color", default_color),
            size="evidence_size" if "size_scale" in style else _style_value(style, "size", 7),
            alpha=_style_value(style, "alpha", 0.75),
            legend_label=label,
            name=label,
        )
    elif binding["kind"] == "line":
        renderer = fig.line(
            source=cds,
            x="x",
            y="y",
            line_color=_style_value(style, "color", default_color),
            line_alpha=_style_value(style, "alpha", 0.75),
            line_width=_style_value(style, "line_width", 2),
            line_dash=_style_value(style, "line_dash", "solid"),
            legend_label=label,
            name=label,
        )
    else:
        renderer = fig.segment(
            source=cds,
            x0="x0",
            x1="x1",
            y0="y0",
            y1="y1",
            line_color=_style_value(style, "color", default_color),
            line_alpha=_style_value(style, "alpha", 0.75),
            line_width=_style_value(style, "line_width", 2),
            line_dash=_style_value(style, "line_dash", "solid"),
            legend_label=label,
            name=label,
        )
    renderer.visible = visible
    renderer.tags = [
        *list(renderer.tags or []),
        "aidata_evidence",
        f"group:{binding.get('group') or 'evidence'}",
        f"anchor:{anchor.get('anchor_name') or anchor.get('df_key') or 'unknown'}",
        f"default_visible:{1 if visible else 0}",
    ]
    _add_hover(fig, renderer, binding)
    if binding.get("text_field") and surface in binding.get("text_surfaces", binding["surfaces"]):
        text = fig.text(source=cds, x="x", y="y", text="text", text_color="black", text_alpha=0.8)
        text.visible = visible
        text.tags = list(renderer.tags)
    return renderer

def _add_hover(fig: Any, renderer: Any, binding: dict[str, Any]) -> None:
    hover_fields = binding.get("hover_fields") or []
    if not hover_fields:
        return
    from bokeh.models import HoverTool

    tooltips: list[tuple[str, str]] = []
    formatters: dict[str, str] = {}
    for item in hover_fields:
        field = str(item["field"])
        fmt = str(item.get("format") or "")
        value = f"@{field}"
        if fmt == "datetime":
            value += "{%F %T.%3N}"
            formatters[f"@{field}"] = "datetime"
        elif fmt:
            value += "{" + fmt + "}"
        tooltips.append((str(item.get("label") or field), value))
    fig.add_tools(
        HoverTool(
            renderers=[renderer],
            tooltips=tooltips,
            formatters=formatters,
            mode="mouse",
        )
    )

def _style_value(style: dict[str, Any], name: str, default: Any) -> Any:
    field_name = style.get(f"{name}_field")
    if field_name not in (None, ""):
        return str(field_name)
    return style.get(name, default)

def _binding_enabled(binding: dict[str, Any], surface: str) -> bool:
    return bool(binding.get("kind")) and surface in set(binding.get("surfaces") or [])

def _require_columns(frame: pd.DataFrame, fields: list[str], *, label: str) -> None:
    missing = [field for field in fields if not field or field not in frame.columns]
    if missing:
        raise KeyError(f"{label} 引用了不存在的 DataFrame 字段: {missing}")

def _current_symbol() -> str:
    try:
        from m3tt import CurrSymbol

        return str(CurrSymbol.sym(False) or "")
    except Exception:
        return ""

def _current_target(anchor: dict[str, Any]) -> str:
    if feature_target_scope(anchor) == "symbol":
        return _current_symbol()
    from mquant.frame.lang import CurrIndustry
    return str(CurrIndustry.blk_expr(False) or "")

def _entity_label(label: str, anchor: dict[str, Any]) -> str:
    target = _current_target(anchor)
    target = target[4:] if target.startswith("blk@") else target
    return f"{target} - {label}" if target else label

def _base_cae_fao():
    from mquant.frame import BaseCAEFao

    return BaseCAEFao

class OverviewCAE(_base_cae_fao()):
    """run 级别的 1d 全局概览图节点。

    页面展示板块有效行情范围的 1d K 线，并叠加 search_timespans、big anchor
    与已生成 big node 的时间框。每个 big 的 30m-1m-5s 页面使用独立链接打开，
    不在 overview 中重复生成。
    """

    params = lambda: {
        "run_dir": "",
        "run_id": "",
        "big_node_id": "RUN_OVERVIEW",
        "context": None,
        "calendar_name": "",
        "blk": "",
        "display_blks": [],
        "overview_start": "",
        "overview_end": "",
        "overview_search_spans_json": "[]",
        "evidence_features": [],
        "k_alpha": 0.5,
        "fig_width_big": 2400,
        "fig_width_mid": 500,
        "fig_height_big": 600,
        "fig_height_mid": 400,
    }

    def hold_on_bokeh_server(self):
        return True

    @evidence_page_cached
    def layout(self, *args: Any, **kwargs: Any):
        _ensure_plot_runtime()
        import bokeh.layouts as bkh
        from mquant.uplot import CAEGraph

        timespans = _read_timespans(Path(self.P.run_dir))
        plot_roots = []
        big_rows = timespans[timespans["level"] == "big"].sort_values(["start_uti", "node_id"])
        _register_plotters(self)

        overview_graph_key = _graph_key(self, "run_overview")
        overview_span = (self.P.overview_start, self.P.overview_end, "板块有效行情范围")
        _register_run_overview_graph(self, overview_graph_key, overview_span)

        review_scope_models: list[Any] = []
        overview_layout = CAEGraph(overview_graph_key).layout(plot_roots=plot_roots)
        overview_node_row = _overview_node_row(self)
        search_rows = _overview_search_rows(self)
        _mark_review_scope(
            overview_layout,
            node_row=overview_node_row,
            child_rows=search_rows,
            run_dir=Path(self.P.run_dir),
            child_color="#BDBDBD",
            anchor_color="#D62728",
            models=review_scope_models,
        )
        _mark_review_scope(
            overview_layout,
            node_row=overview_node_row,
            child_rows=big_rows,
            run_dir=Path(self.P.run_dir),
            child_color="#F28E2B",
            anchor_color="#D62728",
            models=review_scope_models,
        )

        page_children = [
            _review_scope_toggle(review_scope_models),
            overview_layout,
        ]
        layout = bkh.Column(children=[item for item in page_children if item is not None])
        object.__setattr__(layout, 'plot_roots', plot_roots)
        return layout

class MultiscaleCAE(_base_cae_fao()):
    """一个 big local world 对应的 CAE 平台图节点。

    按包内 data/timespans.csv 的父子关系组织大、中、小尺度窗口。
    参数 run_dir 在这里表示交付包根目录。
    """

    params = lambda: {
        "run_dir": "",
        "run_id": "",
        "big_node_id": "",
        "context": None,
        "calendar_name": "",
        "blk": "",
        "display_blks": [],
        "evidence_features": [],
        "k_alpha": 0.5,
        "fig_width_big": 2400,
        "fig_width_mid": 500,
        "fig_width_small": 480,
        "fig_height_big": 600,
        "fig_height_mid": 400,
        "fig_height_small": 400,
    }

    def hold_on_bokeh_server(self):
        """平台中用 Bokeh server 打开，和现有交互 CAE 页面保持一致。"""
        return True

    @evidence_page_cached
    def layout(self, *args: Any, **kwargs: Any):
        """构造一个 big local world 页面。"""
        _ensure_plot_runtime()
        from bokeh.models import Button
        import bokeh.layouts as bkh
        from mquant.uplot import CAEGraph, CurrWidgets

        timespans = _read_timespans(Path(self.P.run_dir))
        plot_roots = []
        big_row = _node_row(timespans, self.P.big_node_id)
        mid_rows = _children(timespans, self.P.big_node_id, "mid")
        _register_plotters(self)

        big_graph_key = _graph_key(self, "big")
        mid_graph_key = _graph_key(self, "mid")
        small_graph_key = _graph_key(self, "small")
        _register_big_graph(self, big_graph_key, _span_tuple(big_row))
        _register_mid_graph(self, mid_graph_key)
        _register_small_graph(self, small_graph_key)

        live_ctrls, live_updaters, upd_btn = {}, {}, Button(label="更新")
        review_scope_models: list[Any] = []
        big_layout = CAEGraph(big_graph_key).layout(plot_roots=plot_roots)
        _mark_review_scope(
            big_layout,
            node_row=big_row,
            child_rows=mid_rows,
            run_dir=Path(self.P.run_dir),
            child_color="#4C78A8",
            anchor_color="#D62728",
            models=review_scope_models,
        )

        mid_cols = []
        for _, mid_row in mid_rows.iterrows():
            mid_figs: list[Any] = []
            mid_span = _span_tuple(mid_row)
            with CurrWidgets(mid_figs, live_ctrls, live_updaters, upd_btn, plot_roots=plot_roots):
                CAEGraph(mid_graph_key)({"plotsets.main.timespans": [mid_span]}).produce_widgets()

            small_figs = []
            small_rows = _children(timespans, mid_row["node_id"], "small")
            for _, small_row in small_rows.iterrows():
                one_small: list[Any] = []
                small_span = _span_tuple(small_row)
                with CurrWidgets(one_small, live_ctrls, live_updaters, upd_btn, plot_roots=plot_roots):
                    CAEGraph(small_graph_key)({"plotsets.smallscale.timespans": [small_span]}).produce_widgets()
                if one_small:
                    tick_rows = _merge_tick_rows_for_display(_children(timespans, small_row["node_id"], "tick"))
                    _mark_review_scope(
                        one_small,
                        node_row=small_row,
                        child_rows=tick_rows,
                        run_dir=Path(self.P.run_dir),
                        child_color="#F28E2B",
                        anchor_color="#D62728",
                        models=review_scope_models,
                    )
                    small_figs.append(one_small)

            _mark_review_scope(
                mid_figs,
                node_row=mid_row,
                child_rows=small_rows,
                run_dir=Path(self.P.run_dir),
                child_color="#59A14F",
                anchor_color="#D62728",
                models=review_scope_models,
            )
            mid_cols.append(
                _local_world_column(
                    header_children=mid_figs,
                    scroll_children=small_figs,
                    scroll_height=2 * int(self.P.fig_height_mid),
                )
            )

        scrollable_mid_small = _horizontal_scroll_columns(
            mid_cols,
            width=int(self.P.fig_width_big),
        )
        evidence_toggle = _evidence_toggle([big_layout, mid_cols])

        page_children = [
            _review_scope_toggle(review_scope_models),
            evidence_toggle,
            big_layout,
            scrollable_mid_small,
            upd_btn,
            bkh.Column(children=[widget for _ctrl, widget in live_ctrls.values()]),
        ]
        layout = bkh.Column(children=[item for item in page_children if item is not None])
        object.__setattr__(layout, 'plot_roots', plot_roots)
        return layout

def _params_for_fao(fao_cls: Any, params: dict[str, Any]) -> dict[str, Any]:
    """只把目标 FAO 声明过的参数传给它。

    mquant FAO 参数校验是严格的；big 页面和 mid-tick 页面共享 chart_params，
    但 tick 页面有自己的补充字段，不能透传给 big 页面。
    """
    allowed = set((fao_cls.params() or {}).keys())
    return {key: value for key, value in params.items() if key in allowed}

def _draw_tick_l1_main(
    cae: Any,
    tick_row: pd.Series,
    *,
    prepared_items: list[dict[str, Any]],
    warnings: list[str],
    fig: Any,
    plot_ctx: Any = None,
) -> Any:
    from bokeh.models import ColumnDataSource, HoverTool, Label
    from mquant.uplot import DynStd

    start = int(tick_row["start_uti"])
    end = int(tick_row["end_uti"])
    if end <= start:
        end = start + 1

    x_values = [
        value
        for item in prepared_items
        for value in item["line"].get("x", [])
        if _to_float(value) is not None
    ]
    if x_values:
        display_start = min(float(value) for value in x_values)
        step = _median_positive_step(x_values) or 1.0
        display_end = max(float(value) for value in x_values) + step
    else:
        display_start = float(start)
        display_end = float(end + 1)

    fig.x_range.start, fig.x_range.end = float(display_start), float(display_end)
    fig.xaxis.axis_label = "自然时间(交易时间轴，非交易时段压缩)"
    fig.yaxis.axis_label = "价格 ratio，基准=当前窗口首个有效最新价"
    _apply_tick_time_axis(fig, prepared_items, tick_row=tick_row, start_uti=start, end_uti=end)

    line_renderers = []
    depth_renderers = []
    dynstd_list = []
    evidence_renderers = []
    for prepared in prepared_items:
        symbol = prepared["symbol"]
        line_cds = ColumnDataSource(prepared["line"])
        depth_cds = ColumnDataSource(prepared["depth"])
        line_renderers.append(
            fig.step(
                source=line_cds,
                x="x",
                y="price",
                mode="after",
                line_color=prepared["color"],
                line_width=2.2,
                alpha=0.92,
                legend_label=symbol,
            )
        )

        if len(depth_cds.data.get("x0", [])):
            for side in ["bid", "ask"]:
                view = _side_source(depth_cds.data, side=side)
                if not view["x0"]:
                    continue
                view_cds = ColumnDataSource(view)
                renderer = fig.segment(
                    source=view_cds,
                    x0="x0",
                    x1="x1",
                    y0="y0",
                    y1="y1",
                    line_color=prepared["color"],
                    line_alpha=0.82,
                    line_width=1.35,
                    line_dash="solid",
                    legend_label=symbol,
                )
                depth_renderers.append(renderer)
                prepared["driven_sources"].append(view_cds)

        dynstd = DynStd(line_cds, "ratio", base_x="x", base_y="price")
        for cds in prepared["driven_sources"]:
            dynstd.drive(cds, [("x0", "y0"), ("x1", "y1")])

        evidence_renderers.extend(
            add_tick_evidence(
                fig,
                list(cae.P.evidence_features or []),
                symbol=symbol,
                start_uti=start,
                end_uti=end + 1,
                dynstd=dynstd,
                runtime={
                    "context": cae.P.context,
                    "blk": cae.P.blk,
                    "calendar_name": cae.P.calendar_name,
                },
            )
        )
        dynstd_list.append(dynstd)
    if dynstd_list:
        _apply_initial_ratio_dynstd(dynstd_list, x_start=float(display_start), x_end=float(display_end))
        for dynstd in dynstd_list:
            plot_ctx.add_dynstd(dynstd)
    else:
        fig.add_layout(
            Label(
                x=float(start),
                y=0,
                x_units="data",
                y_units="data",
                text="tick盘口图无有效数据",
                text_font_size="8pt",
                text_color="#555555",
            )
        )

    if line_renderers:
        fig.add_tools(
            HoverTool(
                renderers=line_renderers,
                tooltips=[
                    ("symbol", "@symbol"),
                    ("timestamp", "@timestamp{%F %T.%3N}"),
                    ("price(raw)", "@raw_price{0.####}"),
                    ("price(ratio)", "@price{0.######}"),
                ],
                formatters={"@timestamp": "datetime"},
                mode="mouse",
            )
        )
    if depth_renderers:
        fig.add_tools(
            HoverTool(
                renderers=depth_renderers,
                tooltips=[
                    ("symbol", "@symbol"),
                    ("side", "@side"),
                    ("timestamp", "@timestamp{%F %T.%3N}"),
                    ("price(raw)", "@raw_price{0.####}"),
                    ("price(ratio)", "@y0{0.######}"),
                    ("volume", "@volume{0}"),
                ],
                formatters={"@timestamp": "datetime"},
                mode="mouse",
            )
        )
    if warnings:
        fig.add_layout(
            Label(
                x=float(display_start),
                y=0,
                x_units="data",
                y_units="screen",
                text="; ".join(warnings[:3]),
                text_font_size="8pt",
                text_color="#666666",
            )
        )
    _style_tick_legend(fig)
    return fig

def _prepare_tick_l1_sources(df: pd.DataFrame, *, symbol: str, color: str) -> dict[str, Any] | None:
    if df.empty or "price" not in df:
        return None
    out = df.copy()
    out["x"] = range(len(out))
    start_uti = int(getattr(df, "attrs", {}).get("resolved_start_uti", 0) or 0)
    if "uti" not in out:
        out["uti"] = [start_uti + i for i in range(len(out))]
    out["timestamp"] = pd.to_datetime(out.get("timestamp"), errors="coerce")
    out["x"] = out["uti"].astype(float)
    out["price"] = pd.to_numeric(out["price"], errors="coerce")
    valid_price = out["price"].where(out["price"] > 0)
    if valid_price.dropna().empty:
        return None

    line = {
        "x": out["x"].tolist(),
        "price": valid_price.tolist(),
        "raw_price": valid_price.tolist(),
        "timestamp": out["timestamp"].tolist(),
        "symbol": [symbol] * len(out),
    }
    aux = _prepare_tick_aux_source(out, symbol=symbol)
    depth_rows = []
    median_step = _median_positive_step(out["x"].tolist()) or 1.0
    half_width = max(0.08, min(1.0, median_step * 0.34))
    for _, row in out.iterrows():
        x = float(row["x"])
        if not math.isfinite(x):
            continue
        ts = row["timestamp"]
        for side, price_col, vol_col in [
            ("bid", "buy_price1", "buy_vol1"),
            ("ask", "sell_price1", "sell_vol1"),
        ]:
            price = _to_float(row.get(price_col))
            volume = _to_float(row.get(vol_col))
            if price is None or price <= 0 or volume is None or volume <= 0:
                continue
            depth_rows.append(
                {
                    "x0": x - half_width,
                    "x1": x + half_width,
                    "y0": price,
                    "y1": price,
                    "raw_price": price,
                    "volume": volume,
                    "side": side,
                    "timestamp": ts,
                    "symbol": symbol,
                }
            )
    depth = pd.DataFrame(depth_rows)
    return {
        "symbol": symbol,
        "line": line,
        "depth": depth.to_dict("list") if not depth.empty else _empty_depth_source(),
        "aux": aux,
        "driven_sources": [],
        "color": color,
    }

def _empty_depth_source() -> dict[str, list[Any]]:
    return {
        "x0": [],
        "x1": [],
        "y0": [],
        "y1": [],
        "raw_price": [],
        "volume": [],
        "side": [],
        "timestamp": [],
        "symbol": [],
    }

def _prepare_tick_aux_source(out: pd.DataFrame, *, symbol: str) -> dict[str, list[Any]]:
    buy_order = _numeric_nonnegative_series(out, "buy_order_vol")
    sell_order = _numeric_series(out, "sell_order_vol").abs()
    bid_vol = _numeric_nonnegative_series(out, "buy_vol1")
    ask_vol = _numeric_nonnegative_series(out, "sell_vol1")
    trade_volume = _numeric_nonnegative_series(out, "trade_volume")
    open_interest = _numeric_series(out, "open_interest")
    open_interest_delta = open_interest.diff().fillna(0)
    return {
        "x": out["x"].tolist(),
        "timestamp": out["timestamp"].tolist(),
        "symbol": [symbol] * len(out),
        "bid_vol": bid_vol.tolist(),
        "ask_vol": ask_vol.tolist(),
        "buy_order_vol": buy_order.tolist(),
        "sell_order_vol": sell_order.tolist(),
        "signed_buy": buy_order.tolist(),
        "signed_sell": sell_order.map(lambda value: -float(value)).tolist(),
        "trade_volume": trade_volume.tolist(),
        "open_interest": open_interest.tolist(),
        "open_interest_delta": open_interest_delta.tolist(),
    }

def _numeric_series(df: pd.DataFrame, field: str) -> pd.Series:
    if field in df:
        raw = df[field]
    else:
        raw = pd.Series(0, index=df.index)
    return pd.to_numeric(raw, errors="coerce").fillna(0)

def _numeric_nonnegative_series(df: pd.DataFrame, field: str) -> pd.Series:
    return _numeric_series(df, field).clip(lower=0)

def _scaled_nonnegative(values: Any, *, scale: float = 0.9) -> list[float]:
    series = pd.Series(values, dtype="float64").fillna(0).clip(lower=0)
    positive = series[series > 0]
    if positive.empty:
        return [0.0] * len(series)
    denom = float(positive.quantile(0.99)) or float(positive.max()) or 1.0
    if denom <= 0:
        return [0.0] * len(series)
    return (series.map(lambda value: min(scale, float(value) / denom * scale))).tolist()

def _scaled_signed(values: Any, *, scale: float = 0.85) -> list[float]:
    series = pd.Series(values, dtype="float64").fillna(0)
    abs_positive = series.abs()
    positive = abs_positive[abs_positive > 0]
    if positive.empty:
        return [0.0] * len(series)
    denom = float(positive.quantile(0.99)) or float(positive.max()) or 1.0
    if denom <= 0:
        return [0.0] * len(series)
    return [
        max(-scale, min(scale, float(value) / denom * scale))
        for value in series
    ]

def _apply_tick_time_axis(fig: Any, prepared_items: list[dict[str, Any]], *, tick_row: pd.Series, start_uti: int, end_uti: int) -> None:
    from bokeh.models import FixedTicker, NoOverlap

    labels = _tick_axis_labels(prepared_items, tick_row=tick_row, start_uti=start_uti, end_uti=end_uti)
    if not labels:
        return
    ticks = sorted(labels)
    fig.xaxis.ticker = FixedTicker(ticks=ticks)
    fig.xaxis.major_label_overrides = labels
    fig.xaxis.major_label_policy = NoOverlap()
    fig.xaxis.major_label_orientation = 0

def _tick_axis_labels(
    prepared_items: list[dict[str, Any]],
    *,
    tick_row: pd.Series,
    start_uti: int,
    end_uti: int,
    max_labels: int = 6,
) -> dict[float, str]:
    pairs: list[tuple[float, Any]] = []
    for item in prepared_items:
        line = item.get("line") or {}
        for x, ts in zip(line.get("x", []), line.get("timestamp", [])):
            x_val = _to_float(x)
            if x_val is not None and not pd.isna(ts):
                pairs.append((float(x_val), ts))
        if pairs:
            break
    if not pairs:
        start_ts = pd.to_datetime(tick_row.get("start_ts"), errors="coerce")
        end_ts = pd.to_datetime(tick_row.get("end_ts"), errors="coerce")
        if not pd.isna(start_ts):
            pairs.append((float(start_uti), start_ts))
        if not pd.isna(end_ts) and end_uti != start_uti:
            pairs.append((float(end_uti), end_ts))
    if not pairs:
        return {}
    pairs = sorted(pairs, key=lambda item: item[0])
    if len(pairs) > max_labels:
        idxs = sorted({round(i * (len(pairs) - 1) / (max_labels - 1)) for i in range(max_labels)})
        pairs = [pairs[idx] for idx in idxs]
    return {x: _format_tick_axis_time(ts) for x, ts in pairs}

def _format_tick_axis_time(value: Any) -> str:
    ts = pd.to_datetime(value, errors="coerce")
    if pd.isna(ts):
        return ""
    return pd.Timestamp(ts).strftime("%m-%d %H:%M")

def _style_tick_legend(fig: Any) -> None:
    if not len(fig.legend):
        return
    fig.legend.location = "top_right"
    fig.legend.click_policy = "hide"
    fig.legend.background_fill_alpha = 0.5
    fig.legend.label_text_alpha = 1
    fig.legend.glyph_height = 10
    fig.legend.glyph_width = 10
    fig.legend.label_height = 10
    fig.legend.label_width = 10
    fig.legend.label_text_font_size = "10px"

def _side_source(data: dict[str, Any], *, side: str) -> dict[str, list[Any]]:
    keep = [
        idx
        for idx, item_side in enumerate(data.get("side", []))
        if str(item_side) == side
    ]
    return {key: [values[idx] for idx in keep] for key, values in data.items()}

def _apply_initial_ratio_dynstd(dynstd_list: list[Any], *, x_start: float, x_end: float) -> None:
    for dynstd in dynstd_list:
        base_cds = dynstd.base_cds
        x_values = list(base_cds.data[dynstd.base_x])
        start_idx, end_idx = _visible_index_range(x_values, x_start=x_start, x_end=x_end)
        base_raw = base_cds.data.get(f"__prestd_{dynstd.base_y}", base_cds.data[dynstd.base_y])
        baseline = _first_finite(base_raw[start_idx:end_idx])
        if baseline is None or baseline == 0:
            continue
        _ratio_field(base_cds.data, dynstd.base_y, baseline, start_idx, end_idx)
        for y in dynstd.extra_ys:
            _ratio_field(base_cds.data, y, baseline, start_idx, end_idx)
        for cds, xy_pairs in dynstd.driven_list:
            for _x, y in xy_pairs:
                _ratio_field(cds.data, y, baseline, 0, len(cds.data.get(y, [])))

def _visible_index_range(x_values: list[Any], *, x_start: float, x_end: float) -> tuple[int, int]:
    if not x_values:
        return 0, 0
    start_idx = 0
    for idx, value in enumerate(x_values):
        if float(value) >= x_start:
            start_idx = max(0, idx - 1)
            break
    end_idx = len(x_values)
    for idx in range(len(x_values) - 1, -1, -1):
        if float(x_values[idx]) < x_end:
            end_idx = idx + 1
            break
    return start_idx, max(start_idx, end_idx)

def _ratio_field(data: dict[str, Any], field: str, baseline: float, start_idx: int, end_idx: int) -> None:
    raw = data.get(f"__prestd_{field}", data.get(field, []))
    values = list(data.get(field, []))
    for idx in range(start_idx, min(end_idx, len(values))):
        value = _to_float(raw[idx])
        values[idx] = value / baseline if value is not None else math.nan
    data[field] = values

def _first_finite(values: Any) -> float | None:
    for value in values:
        num = _to_float(value)
        if num is not None and math.isfinite(num):
            return num
    return None

def _to_float(value: Any) -> float | None:
    try:
        num = float(value)
    except Exception:
        return None
    return num if math.isfinite(num) else None

def _median_positive_step(values: list[Any]) -> float | None:
    nums = sorted(float(value) for value in values if _to_float(value) is not None)
    steps = [b - a for a, b in zip(nums, nums[1:]) if b > a]
    if not steps:
        return None
    return float(pd.Series(steps).median())

def _tick_symbol_color(idx: int) -> str:
    try:
        from mquant.uplot.utlv2 import ContrastColors2

        colors2 = ContrastColors2
        if colors2:
            return _foreground_color_from_group(colors2[idx % len(colors2)])
    except Exception:
        pass
    fallback = [
        ["#f8d7d4", "#f28c82", "#ef3b2c", "#cb181d"],
        ["#b3e6b0", "#74c476", "#41ab5d", "#238b45"],
        ["#d4b9da", "#bcbddc", "#9e9ac8", "#6a51a3"],
        ["#c6dbef", "#6baed6", "#4292c6", "#2171b5"],
        ["#a6cee3", "#1f78b4", "#b2df8a", "#33a02c"],
        ["#d2a679", "#a5723c", "#b98e57", "#8b5a2b"],
        ["#d0d1e6", "#a6bddb", "#67a9cf", "#3690c0"],
        ["#fdcc8a", "#fc8d59", "#ef6548", "#d7301f"],
    ]
    return _foreground_color_from_group(fallback[idx % len(fallback)])

def _foreground_color_from_group(colors: Any) -> str:
    valid = [str(color) for color in colors if _hex_rgb(str(color)) is not None]
    if not valid:
        return "#555555"
    same_hue = _same_hue_colors(valid, valid[0])
    usable = [color for color in same_hue if 0.12 <= _relative_luminance(color) <= 0.72]
    if not usable:
        usable = [color for color in valid if 0.12 <= _relative_luminance(color) <= 0.72]
    candidates = usable or valid
    return min(candidates, key=lambda color: abs(_relative_luminance(color) - 0.35))

def _same_hue_colors(colors: list[str], base_color: str) -> list[str]:
    base_hls = _hex_hls(base_color)
    if base_hls is None or base_hls[2] < 0.12:
        return colors
    base_hue = base_hls[0]
    same_hue = []
    for color in colors:
        hls = _hex_hls(color)
        if hls is None:
            continue
        hue, _lightness, saturation = hls
        if saturation < 0.08:
            continue
        if _hue_distance(hue, base_hue) <= 0.12:
            same_hue.append(color)
    return same_hue or colors

def _hex_hls(value: str) -> tuple[float, float, float] | None:
    import colorsys

    rgb = _hex_rgb(value)
    if rgb is None:
        return None
    red, green, blue = (channel / 255.0 for channel in rgb)
    return colorsys.rgb_to_hls(red, green, blue)

def _hue_distance(left: float, right: float) -> float:
    distance = abs(left - right)
    return min(distance, 1.0 - distance)

def _relative_luminance(hex_color: str) -> float:
    rgb = _hex_rgb(hex_color)
    if rgb is None:
        return 1.0

    def channel(value: int) -> float:
        normalized = value / 255.0
        if normalized <= 0.03928:
            return normalized / 12.92
        return ((normalized + 0.055) / 1.055) ** 2.4

    red, green, blue = (channel(value) for value in rgb)
    return 0.2126 * red + 0.7152 * green + 0.0722 * blue

def _hex_rgb(value: str) -> tuple[int, int, int] | None:
    raw = value.strip()
    if raw.startswith("#"):
        raw = raw[1:]
    if len(raw) == 3:
        raw = "".join(char * 2 for char in raw)
    if len(raw) != 6:
        return None
    try:
        return int(raw[0:2], 16), int(raw[2:4], 16), int(raw[4:6], 16)
    except ValueError:
        return None

def _json_list(value: Any) -> list[Any]:
    if isinstance(value, list):
        return value
    if value in (None, "") or (isinstance(value, float) and pd.isna(value)):
        return []
    try:
        parsed = json.loads(str(value))
    except Exception:
        return []
    return parsed if isinstance(parsed, list) else []

def _ensure_plot_runtime() -> None:
    try:
        from mquant.uplot import CAEGraph  # noqa: F401
    except Exception as exc:
        raise RuntimeError("当前环境无法使用 uplot/CAEGraph，不能生成 big world 图页面") from exc

def _node_row(timespans: pd.DataFrame, node_id: str) -> pd.Series:
    rows = timespans[timespans["node_id"] == node_id]
    if rows.empty:
        raise KeyError(node_id)
    return rows.iloc[0]

def _children(timespans: pd.DataFrame, parent_node_id: str, level: str) -> pd.DataFrame:
    rows = timespans[(timespans["parent_node_id"] == parent_node_id) & (timespans["level"] == level)]
    return rows.sort_values(["start_uti", "node_id"])

def _merge_tick_rows_for_display(tick_rows: pd.DataFrame) -> pd.DataFrame:
    """展示层合并同一 small 下重叠的 tick 窗口，避免旧 run 中橘色辅助框互相压住。"""
    if tick_rows.empty:
        return tick_rows
    rows = tick_rows.sort_values(["start_uti", "end_uti", "node_id"]).to_dict("records")
    merged: list[dict[str, Any]] = []
    for row in rows:
        start = int(row["start_uti"])
        end = int(row["end_uti"])
        if not merged or start > int(merged[-1]["end_uti"]):
            new_row = dict(row)
            new_row["_merged_node_ids"] = [str(row["node_id"])]
            merged.append(new_row)
            continue
        prev = merged[-1]
        if end > int(prev["end_uti"]):
            prev["end_uti"] = end
            prev["end_ts"] = row.get("end_ts", prev.get("end_ts", ""))
        prev["_merged_node_ids"].append(str(row["node_id"]))
        prev["node_id"] = "+".join(prev["_merged_node_ids"])
        prev["member_symbols"] = json.dumps(
            _merge_symbol_lists(prev.get("member_symbols", ""), row.get("member_symbols", "")),
            ensure_ascii=False,
        )
    for row in merged:
        row.pop("_merged_node_ids", None)
    return pd.DataFrame(merged, columns=tick_rows.columns)

def _merge_symbol_lists(left: Any, right: Any) -> list[Any]:
    out: list[Any] = []
    for value in [*_json_list(left), *_json_list(right)]:
        if value not in out:
            out.append(value)
    return out

def _span_tuple(row: pd.Series) -> tuple[Any, Any, str]:
    return (row["start_uti"], row["end_uti"], str(row["node_id"]))

def _overview_node_row(cae: OverviewCAE) -> pd.Series:
    window = _plotctx_window_for_cae(cae, cae.P.overview_start, cae.P.overview_end)
    start_uti = window[0] if window else 0
    end_uti = window[1] if window else 0
    return pd.Series(
        {
            "node_id": "run_overview",
            "level": "run",
            "start_uti": start_uti,
            "end_uti": end_uti,
            "start_ts": cae.P.overview_start,
            "end_ts": cae.P.overview_end,
            "source_occurrence_rows_path": "",
        }
    )

def _overview_search_rows(cae: OverviewCAE) -> pd.DataFrame:
    try:
        records = json.loads(str(cae.P.overview_search_spans_json or "[]"))
    except Exception:
        records = []
    rows: list[dict[str, Any]] = []
    for index, item in enumerate(records if isinstance(records, list) else [], start=1):
        if not isinstance(item, dict):
            continue
        start = item.get("start")
        end = item.get("end")
        window = _plotctx_window_for_cae(cae, start, end)
        if window is None:
            continue
        rows.append(
            {
                "node_id": str(item.get("label") or f"search_{index:03d}"),
                "level": "search",
                "start_uti": window[0],
                "end_uti": window[1],
                "start_ts": start,
                "end_ts": end,
            }
        )
    return pd.DataFrame(rows, columns=["node_id", "level", "start_uti", "end_uti", "start_ts", "end_ts"])

def _plotctx_window_for_cae(cae: Any, start: Any, end: Any) -> tuple[int, int] | None:

    return plotctx_uti_window(
        start,
        end,
        {
            "context": cae.P.context,
            "calendar_name": cae.P.calendar_name,
        },
    )

def _graph_key(cae: Any, suffix: str) -> str:
    mid_part = _param_value(cae.P, "mid_node_id", "")
    token = "".join(ch if ch.isalnum() else "_" for ch in f"{cae.P.run_id}_{cae.P.big_node_id}_{mid_part}_{suffix}")
    return f"aidata_{token}"

def _param_value(params: Any, key: str, default: Any = None) -> Any:
    try:
        return getattr(params, key)
    except (AttributeError, KeyError):
        return default

def _register_plotters(cae: MultiscaleCAE) -> None:
    from mquant.uplot import VBarPlot

    VBarPlot["aidata_open"] = lambda: {
        "feat": SnapshotFeature(bundle_dir=str(cae.P.run_dir), kind='open_segments', df_key='value'),
        "df_key": "value",
        "uti_field": "linear_ts_index",
        "top_field": "segment_flag",
        "top_coeff": 1,
        "bottom": 0,
        "color": "black",
        "alpha": 0.8,
        "width": 0.5,
        "label": "开盘时点",
        "hover_tslabel": True,
    }

def _register_run_overview_graph(cae: OverviewCAE, graph_key: str, overview_span: tuple[Any, Any, str]) -> None:
    from mquant.frame import GMap, GMapX
    from mquant.uplot import CAEGraph, DefaultFigTheme, KPriceLine, PlotSet, SpecEntitiesMainFig

    entity_plots = {
        f"syms!{cae.P.blk}": GMapX.from_list(
            _filter_none(
                [
                    KPriceLine(feat=SnapshotFeature(bundle_dir=str(cae.P.run_dir), kind='kline', freq='1d'), std_method="ratio"),
                    *_evidence_plotters(cae, "overview"),
                ]
            )
        )
    }
    for target in _as_list(cae.P.display_blks):
        entity_plots[target] = GMapX.from_list(
            [KPriceLine(feat=SnapshotFeature(bundle_dir=str(cae.P.run_dir), kind='kline', freq='1d'), std_method="ratio"), *_evidence_plotters(cae, "overview", scope="board", target=target)]
        )

    CAEGraph[graph_key] = lambda: {
        "Context": cae.P.context,
        "plotsets": GMap(
            {
                "main": PlotSet(
                    {
                        "calendar_name": cae.P.calendar_name,
                        "timespans": [overview_span],
                        "blk": cae.P.blk,
                        "figs": GMapX.from_list(
                            [
                                SpecEntitiesMainFig(
                                    entity_plots=GMap(entity_plots),
                                    title=f"!全局概览 {'1d'} {{span_info0}}",
                                )
                            ]
                        ),
                    }
                )
            }
        ),
        "theme": DefaultFigTheme(),
        "x_label_freq": '1d',
        "extra_time": 0,
        "fig_width": int(cae.P.fig_width_big),
        "fig_height1": int(cae.P.fig_height_big),
        "fig_height": 150,
    }

def _register_big_graph(cae: MultiscaleCAE, graph_key: str, big_span: tuple[Any, Any, str]) -> None:
    from mquant.frame import GMap, GMapX
    from mquant.uplot import CAEGraph, DefaultFigTheme, KPriceLine, PlotSet, SpecEntitiesMainFig

    cae_context = cae.P.context
    entity_plots = {
        f"syms!{cae.P.blk}": GMapX.from_list(
            _filter_none(
                [
                    KPriceLine(feat=SnapshotFeature(bundle_dir=str(cae.P.run_dir), kind='kline', freq='30m'), std_method="ratio"),
                    *_evidence_plotters(cae, "big"),
                ]
            )
        )
    }
    for target in _as_list(cae.P.display_blks):
        entity_plots[target] = GMapX.from_list(
            [KPriceLine(feat=SnapshotFeature(bundle_dir=str(cae.P.run_dir), kind='kline', freq='30m'), std_method="ratio"), *_evidence_plotters(cae, "big", scope="board", target=target)]
        )

    CAEGraph[graph_key] = lambda: {
        "Context": cae_context,
        "plotsets": GMap(
            {
                "main": PlotSet(
                    {
                        "calendar_name": cae.P.calendar_name,
                        "timespans": [big_span],
                        "blk": cae.P.blk,
                        "figs": GMap.from_list(
                            [
                                SpecEntitiesMainFig(
                                    entity_plots=GMap(entity_plots),
                                    title=f"!大尺度 {'30m'} {{span_info0}}",
                                )
                            ]
                        ),
                    }
                )
            }
        ),
        "theme": DefaultFigTheme(),
        "x_label_freq": '30m',
        "extra_time": "10h",
        "fig_width": int(cae.P.fig_width_big),
        "fig_height1": int(cae.P.fig_height_big),
        "fig_height": 150,
    }

def _register_mid_graph(
    cae: MultiscaleCAE,
    graph_key: str,
    *,
    fig_width: int | None = None,
    fig_height: int | None = None,
    title: str | None = None,
) -> None:
    from mquant.frame import GMapX
    from mquant.uplot import CAEGraph, KPriceLine

    entity_plots = {
        f"syms!{cae.P.blk}": GMapX.from_list(
            _filter_none(
                [
                    KPriceLine(feat=SnapshotFeature(bundle_dir=str(cae.P.run_dir), kind='kline', freq='1m'), std_method="ratio", alpha=cae.P.k_alpha),
                    *_evidence_plotters(cae, "mid"),
                ]
            )
        )
    }
    for target in _as_list(cae.P.display_blks):
        entity_plots[target] = GMapX.from_list(
            _filter_none(
                [
                    KPriceLine(feat=SnapshotFeature(bundle_dir=str(cae.P.run_dir), kind='kline', freq='1m'), std_method="ratio", alpha=cae.P.k_alpha),
                    *_evidence_plotters(cae, "mid", scope="board", target=target),
                ]
            )
        )

    CAEGraph[graph_key] = lambda: _mid_or_small_graph_config(
        cae,
        plotset_name="main",
        entity_plots=entity_plots,
        freq='1m',
        fig_width=int(fig_width if fig_width is not None else cae.P.fig_width_mid),
        fig_height=int(fig_height if fig_height is not None else cae.P.fig_height_mid),
        title=title or f"!中尺度 {'1m'} {{span_info0}}",
        include_open=True,
    )

def _register_small_graph(
    cae: MultiscaleCAE,
    graph_key: str,
    *,
    fig_width: int | None = None,
    fig_height: int | None = None,
    title: str | None = None,
) -> None:
    from mquant.frame import GMapX
    from mquant.uplot import CAEGraph, KPriceLine

    entity_plots = {
        f"syms!{cae.P.blk}": GMapX.from_list(
            _filter_none(
                [
                    KPriceLine(feat=SnapshotFeature(bundle_dir=str(cae.P.run_dir), kind='kline', freq='5s'), std_method="ratio", alpha=cae.P.k_alpha),
                    *_evidence_plotters(cae, "small"),
                ]
            )
        )
    }
    for target in _as_list(cae.P.display_blks):
        entity_plots[target] = GMapX.from_list(
            _filter_none(
                [
                    KPriceLine(feat=SnapshotFeature(bundle_dir=str(cae.P.run_dir), kind='kline', freq='5s'), std_method="ratio", alpha=cae.P.k_alpha),
                    *_evidence_plotters(cae, "small", scope="board", target=target),
                ]
            )
        )

    CAEGraph[graph_key] = lambda: _mid_or_small_graph_config(
        cae,
        plotset_name="smallscale",
        entity_plots=entity_plots,
        freq='5s',
        fig_width=int(fig_width if fig_width is not None else cae.P.fig_width_small),
        fig_height=int(fig_height if fig_height is not None else cae.P.fig_height_small),
        title=title or f"!小尺度 {'5s'} {{span_info0}}",
        include_open=False,
    )

def _mid_or_small_graph_config(
    cae: MultiscaleCAE,
    *,
    plotset_name: str,
    entity_plots: dict[str, Any],
    freq: str,
    fig_width: int,
    fig_height: int,
    title: str,
    include_open: bool,
) -> dict[str, Any]:
    from mquant.frame import GMap, GMapX
    from mquant.uplot import DefaultFigTheme, PlotSet, SpecEntitiesMainFig, SubFig, VBarPlot

    figs = [
        SpecEntitiesMainFig(
            entity_plots=GMap(entity_plots),
            title=title,
            static_dynstd=(plotset_name == "smallscale"),
        )
    ]
    if include_open:
        figs.append(SubFig(plots=GMapX.from_list([VBarPlot("aidata_open")]), title="!中尺度 附图"))
    return {
        "Context": cae.P.context,
        "plotsets": GMap(
            {
                plotset_name: PlotSet(
                    {
                        "calendar_name": cae.P.calendar_name,
                        "timespans": [],
                        "blk": cae.P.blk,
                        "figs": GMapX.from_list(figs),
                    }
                )
            }
        ),
        "theme": DefaultFigTheme(),
        "x_label_freq": freq,
        "extra_time": "10m" if plotset_name == "smallscale" else 0,
        "fig_width": fig_width,
        "fig_height1": fig_height,
        "fig_height": 150 if plotset_name == "main" else 350,
        "colors2": None,
        "switches": {},
    }

def _filter_none(values: list[Any]) -> list[Any]:
    return [value for value in values if value is not None]

def _evidence_plotters(cae: Any, surface: str, *, scope: str = "symbol", target: str = "") -> list[Any]:

    anchors = [a for a in list(cae.P.evidence_features or [])
               if feature_target_scope(a) == scope
               and (not target or not a.get("target_id") or a["target_id"] == target)]
    return evidence_plotters(anchors, surface)

def _as_list(value: Any) -> list[Any]:
    if value in (None, ""):
        return []
    if isinstance(value, (list, tuple)):
        return list(value)
    return [value]

def _flatten_bokeh_children(values: Any) -> list[Any]:
    """把 uplot/CurrWidgets 收集到的嵌套图列表摊平成 Bokeh children。

    `CAEGraph.produce_widgets()` 往 `CurrWidgets.all_figs()` 里追加的是一个图组，
    常见形状类似 `[[figure]]` 或 `[[figure, widget]]`。Bokeh 的 `Column.children`
    只能接收 UIElement 列表，不能直接接收嵌套 list，所以这里仅做结构展开，不改变图对象。
    """
    children: list[Any] = []

    def visit(value: Any) -> None:
        if value in (None, ""):
            return
        if isinstance(value, (list, tuple)):
            for item in value:
                visit(item)
            return
        children.append(value)

    visit(values)
    return children

def _local_world_column(*, header_children: Any, scroll_children: Any, scroll_height: int) -> Any:
    """复用既有 local-world 列布局：列头固定，子图区在列内纵向滚动。"""
    from bokeh.models import ScrollBox
    import bokeh.layouts as bkh

    header_col = bkh.Column(children=_flatten_bokeh_children(header_children))
    body_children = _flatten_bokeh_children(scroll_children)
    if not body_children:
        return header_col
    body_col = bkh.Column(children=body_children)
    scrollable_body = ScrollBox(
        child=body_col,
        height=int(scroll_height),
        horizontal_scrollbar="hidden",
        vertical_scrollbar="auto",
    )
    return bkh.Column(children=[header_col, scrollable_body])

def _horizontal_scroll_columns(columns: list[Any], *, width: int) -> Any:
    """复用既有 local-world 多列布局：多列横向滚动，纵向交给列内 ScrollBox。"""
    from bokeh.models import ScrollBox
    import bokeh.layouts as bkh

    return ScrollBox(
        child=bkh.Row(children=columns),
        width=int(width),
        horizontal_scrollbar="auto",
        vertical_scrollbar="hidden",
    )

def _mark_review_scope(
    target: Any,
    *,
    node_row: pd.Series,
    child_rows: pd.DataFrame | None,
    run_dir: Path,
    child_color: str,
    anchor_color: str,
    models: list[Any] | None = None,
) -> None:
    """给图审页面叠加低意见的人审辅助标记。

    这里不参与 evidence，不改变 uplot 原始绘图，只在已生成的 Bokeh 主图上加两类标识：
    - 子节点时间窗：半透明 `BoxAnnotation`，帮助人看出下方 mid/small 图对应父图哪段时间。
    - 当前节点 anchor：仅当 `source_occurrences` 中存在明确实际位置字段时画竖线。
    """
    figures = _main_review_figures(target)
    if not figures:
        return

    if child_rows is not None and not child_rows.empty:
        for _, child in child_rows.iterrows():
            left = _number_or_none(child.get("start_uti"))
            right = _number_or_none(child.get("end_uti"))
            if left is None or right is None:
                continue
            for fig in figures:
                created = _add_window_box(fig, left, right, str(child.get("node_id", "")), child_color)
                if models is not None:
                    models.extend(created)

    for anchor_uti in _node_anchor_utis(node_row, run_dir):
        for fig in figures:
            created = _add_anchor_span(fig, anchor_uti, str(node_row.get("node_id", "")), anchor_color)
            if models is not None:
                models.extend(created)

def _main_review_figures(target: Any) -> list[Any]:
    """递归找出页面中的主图 figure，跳过中尺度附图。"""
    figures: list[Any] = []

    def visit(value: Any) -> None:
        if value in (None, ""):
            return
        if isinstance(value, (list, tuple)):
            for item in value:
                visit(item)
            return
        title = getattr(getattr(value, "title", None), "text", "")
        if hasattr(value, "add_layout") and hasattr(value, "x_range") and "附图" not in str(title):
            figures.append(value)
            return
        for attr in ("children",):
            children = getattr(value, attr, None)
            if children is not None:
                visit(children)
        child = getattr(value, "child", None)
        if child is not None:
            visit(child)

    visit(target)
    return figures

def _add_window_box(fig: Any, left: float, right: float, label: str, color: str) -> list[Any]:
    from bokeh.models import BoxAnnotation, Label

    models: list[Any] = []
    box = BoxAnnotation(
        left=left,
        right=right,
        level="underlay",
        fill_color=color,
        fill_alpha=0.08,
        line_color=color,
        line_alpha=0.35,
        line_dash="dashed",
        line_width=1,
    )
    fig.add_layout(box)
    models.append(box)
    if label:
        label_model = Label(
            x=left,
            y=10,
            x_units="data",
            y_units="screen",
            text=label,
            text_font_size="8pt",
            text_color=color,
            background_fill_color="white",
            background_fill_alpha=0.45,
        )
        fig.add_layout(label_model)
        models.append(label_model)
    return models

def _add_anchor_span(fig: Any, location: float, node_id: str, color: str) -> list[Any]:
    from bokeh.models import Label, Span

    models: list[Any] = []
    span = Span(
        location=location,
        dimension="height",
        level="underlay",
        line_color=color,
        line_alpha=0.75,
        line_dash="solid",
        line_width=2,
    )
    fig.add_layout(span)
    models.append(span)
    label_model = Label(
        x=location,
        y=26,
        x_units="data",
        y_units="screen",
        text=f"{node_id} anchor",
        text_font_size="8pt",
        text_color=color,
        background_fill_color="white",
        background_fill_alpha=0.55,
    )
    fig.add_layout(label_model)
    models.append(label_model)
    return models

def _review_scope_toggle(models: list[Any]) -> Any | None:
    """生成定位辅助显隐开关。

    这些辅助标记是 annotation，不适合接入 Bokeh legend；用 Toggle 控制
    `visible` 更直接，也避免查看 K 线 hover 时被半透明条带挡住。
    """
    if not models:
        return None
    from bokeh.models import CustomJS, Toggle

    toggle = Toggle(label="隐藏定位辅助", active=True, button_type="warning", width=120)
    toggle.js_on_change(
        "active",
        CustomJS(
            args={"models": models},
            code="""
                for (const model of models) {
                    model.visible = cb_obj.active
                }
                cb_obj.label = cb_obj.active ? "隐藏定位辅助" : "显示定位辅助"
            """,
        ),
    )
    return toggle

def _evidence_toggle(target: Any) -> Any | None:
    """整页隐藏/恢复证据图层，并保留每层自己的默认显隐。"""
    models: list[Any] = []
    figures = _main_review_figures(target)
    for fig in figures:
        for renderer in getattr(fig, "renderers", []):
            if "aidata_evidence" in set(getattr(renderer, "tags", []) or []):
                models.append(renderer)
    if not models:
        return None

    # 只有确实新增了 evidence renderer 的页面才改变 legend 的点击行为。
    for fig in figures:
        if len(getattr(fig, "legend", [])):
            fig.legend.click_policy = "hide"

    from bokeh.models import CustomJS, Toggle

    toggle = Toggle(label="隐藏特征证据", active=True, button_type="primary", width=150)
    toggle.js_on_change(
        "active",
        CustomJS(
            args={"models": models},
            code="""
                for (const model of models) {
                    if (!cb_obj.active) {
                        model.visible = false
                        continue
                    }
                    const tag = (model.tags || []).find((value) =>
                        typeof value === "string" && value.startsWith("default_visible:")
                    )
                    model.visible = tag ? tag.endsWith(":1") : true
                }
                cb_obj.label = cb_obj.active ? "隐藏特征证据" : "显示特征证据"
            """,
        ),
    )
    return toggle

def _number_or_none(value: Any) -> float | None:
    try:
        if pd.isna(value):
            return None
        return float(value)
    except Exception:
        return None

_CURRENT_TICK_WINDOW = ContextVar("aidata_tick_window", default=None)

class TickWindowFields(DataFrameMixIn, GeneralSymbolFao):
    """将已读的有界盘口交给原生 Plotter，不再读取或运行上游。"""

    params = lambda: {"window_id": ""}

    def hold_cal_type(self):
        return CalType.Cal

    def hold_on_run_ups(self):
        return False

    def _impl(self):

        runtime = _CURRENT_TICK_WINDOW.get()
        if runtime is None or runtime["window_id"] != self.P.window_id:
            raise RuntimeError("TickWindowFields 需要所属 CAEGraph 的有界图窗上下文")
        item = runtime["prepared"][CurrSymbol.sym()]
        frame = pd.DataFrame(item["aux"])
        frame["uti"] = frame["x"]
        frame["ask_height"] = _scaled_nonnegative(frame["ask_vol"])
        frame["bid_height"] = [-v for v in _scaled_nonnegative(frame["bid_vol"])]
        frame["trade_height"] = _scaled_nonnegative(frame["trade_volume"])
        frame["sell_height"] = _scaled_nonnegative(frame["sell_order_vol"])
        frame["buy_height"] = [-v for v in _scaled_nonnegative(frame["buy_order_vol"])]
        frame["oi_lane"] = [CurrSymbol.seq() * runtime["lane_gap"] + v
                            for v in _scaled_signed(frame["open_interest_delta"], scale=0.78)]
        return {"value": frame}

    def rerun(self, *args, **kwargs):
        return self

    def to_dfs(self):
        return self._impl()

def _retain_raw_values(ctx, cds, feature, field, lane_gap):
    frame = feature.rerun().to_dfs()["value"].set_index("uti")
    selected = frame.reindex(cds.data["x"])
    cds.data = {**cds.data, "raw_value": selected[field].tolist(),
                "timestamp": selected["timestamp"].tolist(),
                "symbol": [CurrSymbol.sym()] * len(selected),
                "lane_base": [CurrSymbol.seq() * lane_gap] * len(selected)}

class TickVolumePlot(VBarPlot):
    """使用 VBarPlot 的品种序号偏移，补存悬停与导出所需原始量。"""

    params = lambda: {"raw_field": "ask_vol"}

    def _plot_fig(self, ctx):
        before = len(ctx.figs[-1].renderers)
        super()._plot_fig(ctx)
        renderer = ctx.figs[-1].renderers[before]
        _retain_raw_values(ctx, renderer.data_source, self.P.feat, self.P.raw_field, self.P.symseq_yshift)
        ctx.add_hover(renderer, (f"{self.P.label} 原值", "@ts @raw_value"))

class TickOILinePlot(MulFieldsGlyphs):
    """原生多字段折线，保留持仓变化原值。"""

    def _plot_fig(self, ctx):
        before = len(ctx.figs[-1].renderers)
        super()._plot_fig(ctx)
        source = ctx.figs[-1].renderers[before].data_source
        feature = self.feats.make_arr()[0]
        _retain_raw_values(ctx, source, feature, "open_interest_delta", 3.0)

class TickPricePlot(BasePlotter):
    """由 AllSymsMainFig 提供品种上下文，盘口与事件跟随原生动态标准化。"""

    params = lambda: {"runtime": FAnyParam({})}

    def _plot_fig(self, ctx):

        runtime = self.P.runtime.get_val()
        symbol = CurrSymbol.sym()
        prepared = runtime["prepared"][symbol]
        prepared["color"] = ctx.sym_color
        frame, fetch_time = runtime["raw"][symbol]
        ctx.add_cds(f"raw_tick/{symbol}", ColumnDataSource(frame), fetch_time, 0)
        fig = ctx.figs[-1]
        before = len(fig.renderers)
        started = time.perf_counter()
        _draw_tick_l1_main(runtime["cae"], runtime["row"], prepared_items=[prepared],
                           warnings=runtime["warnings"], fig=fig, plot_ctx=ctx)
        register_tick_sources(ctx, fig, time.perf_counter() - started, renderers=fig.renderers[before:])

def register_tick_sources(ctx: Any, fig: Any, transform_time: float = 0, *, renderers=None) -> None:
    """每个图形数据源登记一次，包含盘口及事件证据。"""
    labels = {}
    for legend in fig.legend:
        for item in legend.items:
            label = getattr(item.label, "value", None) or "layer"
            for renderer in item.renderers:
                labels[renderer.id] = str(label)
    seen = set()
    for renderer in fig.renderers if renderers is None else renderers:
        if not isinstance(renderer, GlyphRenderer):
            continue
        cds = renderer.data_source
        if cds.id in seen:
            continue
        seen.add(cds.id)
        name = f"{len(seen):03d}_{labels.get(renderer.id, 'layer')}_{type(renderer.glyph).__name__}"
        ctx.add_cds(name, cds, 0, transform_time if len(seen) == 1 else 0)

def build_tick_caegraph(cae, tick_row, *, symbols, tick_provider):

    start, end = int(tick_row["start_uti"]), int(tick_row["end_uti"])
    end = max(start + 1, end)
    runtime = {"cae": cae, "row": tick_row, "prepared": {}, "warnings": [], "raw": {}, "lane_gap": 3.0}
    for index, symbol in enumerate(symbols):
        started = time.perf_counter()
        window = tick_provider.read_symbol_window(symbol, start, end)
        frame = window.df.copy()
        frame.attrs["resolved_start_uti"] = int(window.resolved_start_uti)
        raw = frame.copy()
        if "uti" not in raw:
            raw["uti"] = range(int(window.resolved_start_uti), int(window.resolved_start_uti) + len(raw))
        if "timestamp" not in raw:
            raw["timestamp"] = pd.to_datetime(raw.index)
        raw["symbol"] = symbol
        runtime["raw"][symbol] = (raw, time.perf_counter() - started)
        runtime["warnings"].extend(window.warnings)
        prepared = _prepare_tick_l1_sources(frame, symbol=symbol, color=_tick_symbol_color(index))
        if prepared is None:
            runtime["warnings"].append(f"{symbol}: no valid price/bid/ask data")
        else:
            runtime["prepared"][symbol] = prepared

    binding = FAnyParam(runtime)
    runtime["window_id"] = f"{cae.P.run_id}/{tick_row['node_id']}"
    feature = TickWindowFields(window_id=runtime["window_id"])
    members = list(runtime["prepared"])
    def bars(symbol, field, raw_field, label, alpha):
        return TickVolumePlot(feat=feature, df_key="value", uti_field="uti", top_field=field,
                              raw_field=raw_field, symseq_yshift=runtime["lane_gap"],
                              color=None, alpha=alpha, width=0.72, label=f"{symbol} - {label}")
    def sym_plots(panel):
        plots = {}
        for symbol in members:
            if panel == "price":
                items = [TickPricePlot(runtime=binding)]
            elif panel == "book":
                items = [bars(symbol, "ask_height", "ask_vol", "卖一挂量", 0.42),
                         bars(symbol, "bid_height", "bid_vol", "买一挂量", 0.26)]
            elif panel == "trade_oi":
                items = [bars(symbol, "trade_height", "trade_volume", "tick成交量", 0.34),
                         TickOILinePlot(glyphs="line", feats=GMapX.from_list([feature]),
                                        dfkeys=["value"], xfields=["uti"], yfields=["oi_lane"],
                                        dynstd_method=False, legend_labels=["持仓变化"], alphas=0.85)]
            else:
                items = [bars(symbol, "sell_height", "sell_order_vol", "主卖量", 0.38),
                         bars(symbol, "buy_height", "buy_order_vol", "主买量", 0.24)]
            plots[symbol] = GMapX.from_list(items)
        return GMap(plots)

    title = f"tick盘口 {tick_row['node_id']} | {tick_row.get('start_ts', start)} ~ {tick_row.get('end_ts', end)}"
    figs = [AllSymsMainFig(title=title, sym_plots=sym_plots("price"), fit_y_range=False, nb_fig_time_range=False)]
    for panel, label in [
        ("book", "附图：卖一/买一挂量（卖在上、买在下）"),
        ("trade_oi", "附图：tick成交量与持仓变化"),
        ("active", "附图：主卖/主买（卖在上、买在下）"),
    ]:
        figs.append(AllSymsFig(title=label, sym_plots=sym_plots(panel), nb_fig_time_range=False))
    graph = CAEGraph(
        Context=cae.P.context,
        plotsets=GMap({"tick": PlotSet(calendar_name=cae.P.calendar_name, blk=cae.P.blk,
            timespans=[(start, end, str(tick_row["node_id"]))], figs=GMapX.from_list(figs))}),
        x_label_freq="1m", extra_time=0,
        fig_width=int(cae.P.fig_width_small), fig_height1=int(cae.P.fig_height_small),
        fig_height=max(150, int(cae.P.fig_height_small * 0.42)), plot_name=f"tick/{tick_row['node_id']}",
    )
    roots = []
    all_figs = []
    token = _CURRENT_TICK_WINDOW.set(runtime)
    try:
        layout = graph.layout(plot_roots=roots, all_figs=all_figs)
    finally:
        _CURRENT_TICK_WINDOW.reset(token)
    for fig in all_figs[0]:
        _apply_tick_time_axis(fig, list(runtime["prepared"].values()), tick_row=tick_row, start_uti=start, end_uti=end)
    object.__setattr__(layout, "plot_roots", roots)
    return layout

def _read_timespans(root):
    return pd.read_csv(Path(root) / 'data' / 'timespans.csv')


def _node_anchor_utis(row, root, limit=12):
    return bundle(root).manifest['anchor_positions'].get(str(row['node_id']), [])[:limit]


def chart_params(root=None, window_scope=''):
    data = bundle(root)
    manifest = data.manifest
    features = []
    for item in manifest['evidence_features']:
        anchor = dict(item)
        anchor['feature'] = SnapshotFeature(kind='evidence', source_key=item['source_key'],
                                            df_key=normalize_df_key(item.get('df_key')),
                                            bundle_dir=str(data.root), window_scope=window_scope)
        features.append(anchor)
    return dict(run_dir=str(data.root), run_id='steel_frozen_sample',
                context=SnapshotContext(bundle_dir=str(data.root)),
                calendar_name=manifest['calendar_name'], blk=manifest['blk'], display_blks=[],
                evidence_features=features, k_alpha=0.5,
                fig_width_big=2400, fig_width_mid=500, fig_width_small=480,
                fig_height_big=600, fig_height_mid=400, fig_height_small=400)


def build_overview(root=None):
    """生成包内固定样本的长期概览图（含六个大尺度窗口）。"""
    params = chart_params(root)
    manifest = bundle(root).manifest
    params.update(overview_start=manifest['overview_start'], overview_end=manifest['overview_end'],
                  overview_search_spans_json=manifest['overview_search_spans_json'])
    return OverviewCAE(_params_for_fao(OverviewCAE, params)).layout()


def build_multiscale(root=None, node_id=None):
    """生成指定大尺度节点及其全部中、小尺度的组合图。"""
    node_id = node_id or bundle(root).manifest['big_node_id']
    params = chart_params(root, window_scope=node_id)
    params['big_node_id'] = node_id
    if params['big_node_id'] not in bundle(root).manifest['included_big_node_ids']:
        raise ValueError(f"数据包未包含大尺度节点 {params['big_node_id']}")
    return MultiscaleCAE(_params_for_fao(MultiscaleCAE, params)).layout()


def build_tick(root=None, node_id=None):
    """生成数据包内指定 Tick 节点的原生 CAEGraph 主附图。"""
    data = bundle(root)
    node_id = node_id or data.manifest['tick_node_id']
    params = chart_params(root, window_scope=node_id)
    params['fig_width_small'] = 1200
    cae = SimpleNamespace(P=SimpleNamespace(**params))
    if node_id not in data.manifest['included_tick_node_ids']:
        raise ValueError(f'数据包未包含 Tick 节点 {node_id}；请查看 included_tick_nodes.csv')
    row = _node_row(_read_timespans(data.root), node_id)
    return build_tick_caegraph(cae, row, symbols=data.manifest['symbols'], tick_provider=data)
