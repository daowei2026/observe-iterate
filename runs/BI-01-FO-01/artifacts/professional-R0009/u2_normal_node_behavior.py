"""U2NormalNodeBehaviorFrp display configuration, professional R0009 v0.2.1.

Destination: aidata/feature_configs/u2_normal_node_behavior.py, on an authorized
independent branch. This file defines display choices, not N calculations,
formal-result loading, a renderer, or a new Feature identity.

configs(feature) uses the inspected aidata configs/plot_binding vocabulary.
Its df_keys below are explicitly DISPLAY VIEW names, NOT existing N table keys.
Work 3 must compare the actual local entry, supply read-only linked views, bind
ONE color per symbol and route each group to its declared MainFig/SubFig.
The stock registry/group tag alone does not implement those steps. Never pass
all returned anchors unmodified to a price-normalizing main-chart renderer.

Reference: uplot 0a4fcd54059782572a3f7e82fad041121e8c65ad;
aidata interface reference 9ff7ce4929b36945f63b1c9875e59f68141f997a.
Worker02 integrated v0.2.0 on aidata f58ea95c -> db44a54f -> 28260d3e,
with actual uplot 13badc6c (the manual version remains a reference).
R0009 read the real consumer and two delivered PNGs. v0.2.1 adds bounded
readability decisions; its NEW policies are not yet wired in that consumer.
See READABILITY_POLICY and WORKER_ORDER.md; file existence is not integration.
"""
from __future__ import annotations

from copy import deepcopy
from typing import Any, Iterable
from math import isfinite

CONFIG_VERSION = "0.2.1"
FEATURE_NAME = "U2NormalNodeBehaviorFrp"
SURFACES = ["overview", "big", "mid", "small"]

# The caller chooses the observation range; these are panes, not workflow gates.
PANELS = {
    "price": {"class": "MainFig", "title": "行情与过程边界", "unit": "price",
              "height": 420, "default": True, "price_normalization": False},
    "completed_efficiency": {"class": "SubFig", "title": "已完成过程效率：最近六段／此前六段",
                             "unit": "ratio", "height": 210, "default": True,
                             "price_normalization": False},
    "working_motion": {"class": "SubFig", "title": "当前未完成过程：沿原方向净推进／累计最大逆向量",
                       "unit": "price", "height": 210, "default": True,
                       "price_normalization": False, "include_zero": True},
    "working_efficiency": {"class": "SubFig", "title": "当前过程前缀效率（非已完成样本）",
                           "unit": "ratio", "height": 180, "default": True,
                           "price_normalization": False},
    "duration": {"class": "SubFig", "title": "已完成过程时长／当前过程年龄",
                 "unit": "CalendarUTITick", "height": 200, "default": False,
                 "price_normalization": False},
    "rhythm": {"class": "SubFig", "title": "局部等待／近期三个极值间隔中位数",
               "unit": "ratio", "height": 180, "default": False,
               "price_normalization": False, "clip_to_probability": False},
}

TIME_POLICY = {
    "evolution": {
        "x": "formal evaluation/knowledge UTI mapped by the bound Calendar",
        "source": "ordered formal occurrences and their own origins/revisions/bases",
        "completed_hold": "horizontal intervals only across verified covered state; no linear interpolation",
        "same_value_new_members": "retain a point/identity change even when the numeric value is unchanged",
        "working": "observed prefixes only; new Life, missing input or failure breaks the trace",
        "late_revision": "show at its actual known time; never overwrite the prior as-known trace",
        "single_snapshot": "insufficient for a historical curve; draw only its observed point",
    },
    "selected_cut": {
        "read": "read_at_knowledge(explicit_node_life, K), or its exact normally resolved equivalent",
        "membership": "only members and revisions eligible at K; not terminal-window backfill",
        "geometry": "actual process endpoints on price; confirmation markers at confirmation-time price",
        "cut_limit": "no price or working prefix beyond K in the selected-cut page",
        "later_revision_comparison": "separate labelled view with its own K and exact, never merged silently",
    },
    "bar_time": "HistoricalInputUTI/open_uti with same-bar close; NOT live opening knowledge certification",
    "units": "CalendarUTITick retained; no automatic conversion to seconds or bar count",
    "missing": "break numeric geometry; preserve present/knownness/applicability/reason and show a gap notice",
    "zero": "a present, applicable zero stays numeric zero; missing values never become zero",
    "no_live_engine": True,
}

# (view name, pane, geometry, fields, label, style, optional mode)
_LAYER_SPECS = [
    ("close_path", "price", "line", ("x", "y"), "原5m close路径", {"line_width": 1, "line_dash": "solid"}, "both"),
    ("completed_recent_hold", "completed_efficiency", "segment", ("x0", "x1", "y0", "y1"), "最近六段效率中位数（保持区间）", {"line_width": 2, "line_dash": "solid"}, "evolution"),
    ("completed_previous_hold", "completed_efficiency", "segment", ("x0", "x1", "y0", "y1"), "此前六段效率中位数（保持区间）", {"line_width": 1.5, "line_dash": "dashed"}, "evolution"),
    ("completed_recent_updates", "completed_efficiency", "point", ("x", "y"), "最近窗已知更新／选定值", {"marker": "circle", "size": 6}, "both"),
    ("completed_previous_updates", "completed_efficiency", "point", ("x", "y"), "此前窗已知更新／选定值", {"marker": "square", "size": 6}, "both"),
    ("working_progress_steps", "working_motion", "segment", ("x0", "x1", "y0", "y1"), "当前过程沿原方向净推进", {"line_width": 2, "line_dash": "solid"}, "evolution"),
    ("working_counter_steps", "working_motion", "segment", ("x0", "x1", "y0", "y1"), "当前过程累计最大逆向量", {"line_width": 1.5, "line_dash": "dashed"}, "evolution"),
    ("working_progress_points", "working_motion", "point", ("x", "y"), "净推进实际观测值", {"marker": "circle", "size": 5}, "both"),
    ("working_counter_points", "working_motion", "point", ("x", "y"), "逆向量实际观测值", {"marker": "square", "size": 5}, "both"),
    ("working_efficiency_steps", "working_efficiency", "segment", ("x0", "x1", "y0", "y1"), "当前前缀效率", {"line_width": 2, "line_dash": "solid"}, "evolution"),
    ("working_efficiency_points", "working_efficiency", "point", ("x", "y"), "当前前缀效率观测值", {"marker": "circle", "size": 5}, "both"),
    ("recent_duration_hold", "duration", "segment", ("x0", "x1", "y0", "y1"), "最近六段时长中位数", {"line_width": 2, "line_dash": "solid"}, "evolution"),
    ("previous_duration_hold", "duration", "segment", ("x0", "x1", "y0", "y1"), "此前六段时长中位数", {"line_width": 1.5, "line_dash": "dashed"}, "evolution"),
    ("recent_duration_updates", "duration", "point", ("x", "y"), "最近六段时长中位数观测值", {"marker": "circle", "size": 5}, "both"),
    ("previous_duration_updates", "duration", "point", ("x", "y"), "此前六段时长中位数观测值", {"marker": "square", "size": 5}, "both"),
    ("working_duration_points", "duration", "point", ("x", "y"), "当前未完成过程年龄", {"marker": "triangle", "size": 6}, "both"),
    ("waiting_ratio_steps", "rhythm", "segment", ("x0", "x1", "y0", "y1"), "当前局部等待倍数（非概率）", {"line_width": 2, "line_dash": "solid"}, "evolution"),
    ("waiting_ratio_points", "rhythm", "point", ("x", "y"), "局部等待倍数观测值", {"marker": "circle", "size": 5}, "both"),
    ("selected_previous_boundaries", "price", "segment", ("x0", "x1", "y0", "y1"), "选定时点：此前窗端点连线（非行程）", {"line_width": 1, "line_dash": "dotted"}, "selected_cut"),
    ("selected_recent_boundaries", "price", "segment", ("x0", "x1", "y0", "y1"), "选定时点：最近窗端点连线（非行程）", {"line_width": 2, "line_dash": "dashed"}, "selected_cut"),
    ("selected_working_boundary", "price", "segment", ("x0", "x1", "y0", "y1"), "选定时点：未完成过程端点连线", {"line_width": 2, "line_dash": "dotdash"}, "selected_cut"),
    ("selected_actual_endpoints", "price", "point", ("x", "y"), "当时已知成员的实际端点", {"marker": "circle", "size": 7}, "selected_cut"),
    ("selected_confirmations", "price", "point", ("x", "y"), "确认／可知时点（非实际端点）", {"marker": "diamond", "size": 9}, "selected_cut"),
]

HOVER = [
    {"field": "symbol", "label": "品种"},
    {"field": "source_exact", "label": "正式来源exact"},
    {"field": "as_of_uti", "label": "本视图知识截止UTI"},
    {"field": "origin_uti", "label": "该发生知识UTI"},
    {"field": "state_text", "label": "状态／原因"},
    {"field": "meaning", "label": "对象、范围和单位"},
]


def configs(feature: Any = None) -> list[dict[str, Any]]:
    """Return concrete aidata-style bindings; the feature is NOT calculated here.

    Use display_config() in the N consumer to bind symbol color and panel routing.
    df_key is a required display projection, never a claimed native formal table.
    """
    result = []
    for key, panel, kind, fields, label, style, _mode in _LAYER_SPECS:
        if kind == "segment":
            geometry = dict(zip(("x0_field", "x1_field", "y0_field", "y1_field"), fields))
            time_binding = {"time_mode": "uti_interval", "uti1_field": "x0", "uti2_field": "x1", "interval_policy": "overlap"}
        else:
            geometry = dict(zip(("x_field", "y_field"), fields))
            time_binding = {"time_mode": "uti_point", "uti_fields": ["x"]}
        result.append({
            "view_id": key, "df_key": "n_display/" + key,
            "time_binding": time_binding, "slice_levels": ["big", "mid", "small"],
            "plot_binding": {"kind": kind, **geometry, "group": panel,
                             "label": label, "surfaces": list(SURFACES),
                             "style": deepcopy(style), "hover_fields": deepcopy(HOVER)},
        })
    return result


def display_config(*, symbol: str, color: str, mode: str = "evolution",
                   optional_panels: tuple[str, ...] = ()) -> dict[str, Any]:
    """Bind one instrument's configuration for the authorized aidata consumer.

    Color comes from the caller's stable palette, not status/direction.
    Layout and policies below require actual consumer wiring in Work 3; they are
    not fields the current generic registry is assumed to interpret magically.
    """
    if not isinstance(symbol, str) or not symbol.strip():
        raise ValueError("symbol must identify one actual bound instrument")
    if not isinstance(color, str) or not color.strip():
        raise ValueError("supply the instrument's one stable display color")
    if mode not in ("evolution", "selected_cut"):
        raise ValueError("mode must be evolution or selected_cut")
    if set(optional_panels) - set(PANELS):
        raise ValueError("unknown optional panel")
    selected = {k for k, v in PANELS.items() if v["default"]} | set(optional_panels)
    modes = {row[0]: row[-1] for row in _LAYER_SPECS}
    layers = []
    for entry in configs():
        panel = entry["plot_binding"]["group"]
        if panel not in selected or modes[entry["view_id"]] not in ("both", mode):
            continue
        entry["plot_binding"]["style"]["color"] = color
        entry["plot_binding"]["label"] = symbol + "｜" + entry["plot_binding"]["label"]
        if entry["plot_binding"]["kind"] == "point":
            if mode == "selected_cut":
                entry["plot_binding"]["style"]["size"] = 9
            elif entry["view_id"].startswith("working_") or entry["view_id"] == "waiting_ratio_points":
                entry["plot_binding"]["style"]["size"] = 3
        layers.append(entry)
    panels = {k: deepcopy(v) for k, v in PANELS.items() if k in selected}
    if mode == "selected_cut":
        for key, spec in panels.items():
            if key != "price":
                spec["height"] = 150
    return {
        "feature": FEATURE_NAME, "version": CONFIG_VERSION, "symbol": symbol,
        "mode": mode, "layout_class": "PerSymFigSet", "theme_class": "DefaultFigTheme",
        "shared_x": ("bound Calendar UTI" if mode == "evolution" else
                     "price uses Calendar UTI; scalar viewports are independent single-K summaries"),
        "independent_y_by_panel": True,
        "panels": panels,
        "readability_policy": deepcopy(READABILITY_POLICY[mode]),
        "display_identity_fields": list(DISPLAY_IDENTITY_FIELDS),
        "layers": layers, "time_policy": deepcopy(TIME_POLICY),
        "price_background": {"class": "KPriceLine", "source": "same-bound original 5m OHLC",
                             "color": color, "alpha": 0.25, "std_method": None, "enabled": True},
        "required_badges": ["symbol", "selected K or as-known mode", "input history basis",
                            "formal coverage (separate from price context)",
                            "working direction/completion at selected K or LAST occurrence",
                            "gap/error notices", "configuration version"],
        "disclosure": "选择时点回看不等于当时已经知道后来确认的端点；效率不是收益或胜率。",
    }


# N-specific view requirements, not a new generic data platform/schema.
VIEW_RULES = {
    "provenance": "keep original table coordinates, binding/window/working addresses, Life/revision, metric definition, source_exact and original status columns",
    "metrics": "resolve specs by the selected binding and kind; no positional naming; use official values, not recomputed medians",
    "completed_intervals": "y0=y1=official selected metric; x0/x1 bound verified validity coverage, not actual member start/end",
    "working_steps": "horizontal hold plus vertical change at the next observed evaluation; never a sloping prediction/interpolation; new Life/gap/failure or changed start/direction breaks; a storage-address change alone is NOT a new Life",
    "selected_scalar_points": "x=K; a value at the selected evaluation, not its first-known time; show base storage time separately and do not infer a timeline",
    "points": "all actual observations retained; isolated snapshot is a point, not an invented interval",
    "close_path": "original close; insert missing separators at actual missing data, not at every normal exchange closure",
    "selected_boundaries": "x0/x1 actual start/end or through; y0/y1 exact endpoint close; source direction separate from segment slope",
    "confirmations": "x=member confirmation/known time, y=actual close there, hover includes actual endpoint and delay; omit rather than invent unavailable price",
    "not_drawn_by_default": ["all-six-metric tables", "MAD curves", "LOO ranking", "physical addresses", "all intermediate calculations"],
    "auxiliary_detail": "selected original six metrics/MAD/LOO/member identities/statuses on demand; LOO ties not importance ranks",
    "required_runtime_checks": ["native entry vs read-only view", "explicit OnlyRead", "panel routing", "no price normalization on ratios/durations", "stable symbol palette", "As-Of/revision eligibility", "null/gap rendering"],
}


# New display-only decisions. Worker03 must connect these to the existing aidata
# consumer, not merely register another unused configuration or mutate uplot.
DISPLAY_IDENTITY_FIELDS = (
    "symbol", "node_life", "data_binding", "mode", "selected_k_or_requested_range",
    "resolved_exact_or_occurrence_selection", "configuration_version", "optional_panels",
)
READABILITY_POLICY = {
    "evolution": {
        "primary_range": "intersection of selected actual occurrence coverage and price coverage",
        "range_function": "evolution_display_range",
        "price_context": "separate price-only overview on demand; not the scalar-panel range",
        "tick_labels": {"mode": "adaptive", "maximum_visible": 10, "fixed_5m_labels": False},
        "legend": {"placement": "outside_above", "short_labels": True},
        "numeric_range_function": "numeric_display_range",
        "fit_y_range": "use explicit bounded range; do not allow a later callback to collapse it",
        "value_labels": "selected/last observed values in margins; no plot-wide labels per bar",
        "state_changes": "mark actual working-Life/start/direction changes at known K; not trading signals",
        "storage_changes": "retain in hover; never label every working address as a new market process",
        "rhythm_detail": "show actual waiting, current interval median, local-start and last-update when selected",
        "empty_region": "outside formal coverage is not zero, immature, or a market gap",
    },
    "selected_cut": {
        "price_range": "cover all twelve eligible members and working through K",
        "scalar_layout": {"arrangement": "compact_grid", "columns": 2, "height": 150},
        "scalar_x": "keep actual x=K; detach historical shared x range; show only K tick and a single-cut label",
        "scalar_x_padding": "equal display-only margins, at least 24 screen pixels; no synthetic or future records",
        "numeric_range_function": "numeric_display_range",
        "fit_y_range": "explicit nondegenerate y range; check final range after callbacks",
        "legend": {"placement": "outside_above", "short_labels": True},
        "value_labels": "each present scalar has a readable value+unit in the margin; no hover required",
        "absent_value": "explicit state/reason rather than an unexplained blank or zero",
        "price_tick_labels": {"mode": "adaptive", "maximum_visible": 10, "fixed_5m_labels": False},
        "temporal_note": "member actual endpoints and confirmation times differ; scalar has one observation only",
        "rhythm_detail": "waiting / actual recent interval median = waiting_ratio, never a probability cap",
    },
}


def numeric_display_range(panel: str, values: Iterable[float | None]) -> tuple[float, float] | None:
    """Display bounds only. No clipping, filling, normalization or feature math.

    Ratio efficiency usually lies in [0, 1], but observed outliers EXPAND the
    axis and require a source/status check. Empty/all-null input returns None,
    so the consumer must show the original absence state, not a numeric zero.
    """
    if panel not in PANELS:
        raise ValueError(f"unknown panel: {panel}")
    finite = []
    for value in values:
        if value is None:
            continue
        if isinstance(value, bool):
            raise TypeError("a Boolean is not a measured scalar")
        number = float(value)
        if isfinite(number):
            finite.append(number)
    if not finite:
        return None
    low, high = min(finite), max(finite)
    if panel in ("completed_efficiency", "working_efficiency"):
        low, high = min(0.0, low), max(1.0, high)
    elif panel != "price":
        low, high = min(0.0, low), max(0.0, high)
    span = high - low
    if span == 0:
        span = max(1.0, abs(high) * 0.1)
    padding = span * 0.05
    return low - padding, high + padding


def evolution_display_range(occurrence_utis: Iterable[int], price_utis: Iterable[int]) -> tuple[int, int]:
    """Inclusive focus range; the renderer separately keeps its right-open K+1.

    This chooses a viewport, not a new set of formal occurrences. The caller
    retains the original loaded data, provenance and any context overview.
    """
    def checked(values: Iterable[int]) -> list[int]:
        result = list(values)
        if not result or any(isinstance(v, bool) or not isinstance(v, int) for v in result):
            raise ValueError("need nonempty integer UTI sequences")
        return result
    occurrences, prices = checked(occurrence_utis), checked(price_utis)
    start = max(min(occurrences), min(prices))
    end = min(max(occurrences), max(prices))
    if start > end:
        raise ValueError("formal and price coverage do not overlap")
    return start, end
