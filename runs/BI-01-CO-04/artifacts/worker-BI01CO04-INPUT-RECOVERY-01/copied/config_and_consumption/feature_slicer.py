"""主证据切片与 source occurrence 回查。

本模块负责从真实 feature runtime 中读取 dataframe，并按 aidata timespan
切出 `feature_slices/` 主证据。它也负责回查每个 node 的定位来源
`source_occurrences/`。切片语义应尽量贴近 PlotCtx / uplot 的 UTI 语义，
不要从 Bokeh CDS 或图层数据反推主证据。
"""

from __future__ import annotations

from pathlib import Path
from typing import Any
from contextlib import contextmanager, ExitStack
import json

import pandas as pd

from .contracts import (
    HASH_METHOD,
    feature_identity_hash,
    feature_ppid,
    feature_repr,
    feature_target_id,
    feature_target_scope,
    normalize_df_key,
    safe_path_token,
    sha1_text,
    write_csv,
)


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


def infer_time_binding(df: pd.DataFrame, binding: dict[str, Any]) -> dict[str, Any]:
    """在未显式指定时，从 dataframe 字段推断基本 time binding。"""
    if binding.get("time_mode"):
        return binding
    if "x" in df.columns:
        return {"time_mode": "uti_point", "uti_fields": ["x"], "uti1_field": "x", "uti2_field": None, "interval_policy": "point_inside"}
    if "uti" in df.columns:
        return {"time_mode": "uti_point", "uti_fields": ["uti"], "uti1_field": "uti", "uti2_field": None, "interval_policy": "point_inside"}
    if {"uti1", "uti2"}.issubset(df.columns):
        return {"time_mode": "uti_interval", "uti1_field": "uti1", "uti2_field": "uti2", "interval_policy": "overlap"}
    return {"time_mode": "index_natural", "uti1_field": "", "uti2_field": "", "interval_policy": "index_slice"}


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


def slice_df(
    df: pd.DataFrame,
    time_binding: dict[str, Any],
    start: Any,
    end: Any,
    runtime: dict[str, Any] | None = None,
) -> pd.DataFrame:
    """按 time binding 从 dataframe 中切出 timespan 窗口。"""
    binding = infer_time_binding(df, time_binding)
    mode = binding.get("time_mode")
    uti_window = plotctx_uti_window(start, end, runtime)
    if mode == "uti_point":
        fields = binding.get("uti_fields") or [binding.get("uti1_field")]
        field = fields[0]
        if uti_window is None:
            return df[df[field].between(start, end, inclusive="both")].copy()
        start_uti, end_uti = uti_window
        if df[field].is_monotonic_increasing:
            try:
                from mquant.uplot.pfw import uti_slice

                start_i, end_i = uti_slice(df[field], df[field], start_uti, end_uti)
                return df.iloc[start_i:end_i, :].copy()
            except Exception:
                pass
        values = df[field].values
        return df.iloc[(values >= start_uti) & (values < end_uti), :].copy()
    if mode == "uti_interval":
        left = binding.get("uti1_field")
        right = binding.get("uti2_field")
        if uti_window is None:
            return df[(df[left] <= end) & (df[right] >= start)].copy()
        start_uti, end_uti = uti_window
        return df[(df[left] < end_uti) & (df[right] >= start_uti)].copy()
    if mode == "index_natural":
        if uti_window is not None:
            return slice_natural_df_like_plotctx(df, uti_window, runtime)
        return df.loc[start:end].copy()
    raise ValueError(f"不支持的 time_mode: {mode!r}")


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


def add_natural_time_columns(
    df: pd.DataFrame,
    runtime: dict[str, Any] | None = None,
    *,
    preferred_columns: list[str] | None = None,
) -> pd.DataFrame:
    """给常见 UTI 字段补充自然时间列，方便 Pro 和人直接阅读。"""
    if df.empty:
        return df.copy()
    context = (runtime or {}).get("context")
    calendar_name = (runtime or {}).get("calendar_name")
    if context is None or not hasattr(context, "sof") or not calendar_name:
        return df.copy()

    try:
        utsa = context.sof.tsa_of(calendar_name)["natural_tsa"]
    except Exception:
        return df.copy()

    out = df.copy()
    candidates = list(preferred_columns or [])
    candidates.extend(
        [
            "x",
            "xConfirm",
            "uti",
            "uti1",
            "uti2",
            "data_uti1",
            "data_uti2",
            "deci_uti1",
            "deci_uti2",
            "openUti",
            "closeUti",
            "posUTI0",
            "posUTI1",
        ]
    )
    seen: set[str] = set()
    for column in candidates:
        if not column or column in seen or column not in out.columns:
            continue
        seen.add(column)
        ts_column = f"{column}_ts"
        if ts_column in out.columns:
            continue
        out[ts_column] = _uti_series_to_ts(out[column], utsa)
    return out


def _uti_series_to_ts(values: pd.Series, utsa: Any) -> list[str]:
    out: list[str] = []
    size = len(utsa)
    for value in values:
        try:
            if pd.isna(value):
                out.append("")
                continue
            index = int(value)
            if index < 0 or index >= size:
                out.append("")
                continue
            out.append(pd.to_datetime(utsa[index]).strftime("%Y-%m-%d %H:%M:%S"))
        except Exception:
            out.append("")
    return out


def materialize_source_occurrences(
    run_dir: Path,
    timespan_index: pd.DataFrame,
    anchor_by_level: dict[str, dict[str, Any]],
    runtime: dict[str, Any] | None = None,
    logger: Any | None = None,
) -> pd.DataFrame:
    """为每个 timespan node 回查定位 source occurrence 明细。"""
    out = timespan_index.copy()
    for idx, row in out.iterrows():
        anchor = anchor_by_level.get(row["level"])
        if anchor is None:
            continue
        source_rows = _source_occurrence_rows_for_timespan(anchor, row, runtime)
        source_rows = add_natural_time_columns(source_rows, runtime, preferred_columns=_time_columns_for_anchor(anchor))
        duplicate_info = mark_duplicate_occurrences(source_rows)
        source_rows = duplicate_info["df"]
        source_path = (
            run_dir
            / "source_occurrences"
            / row["node_id"]
            / _artifact_target_type(anchor)
            / safe_path_token(_artifact_target_id(anchor, runtime=runtime, row=row))
            / "source_scope"
            / safe_path_token(row.get("source_symbollist", row.get("extract_time_syms", _artifact_target_id(anchor, runtime=runtime, row=row))))
            / row["anchor_feature_key"]
            / f"{row['source_df_key_normalized']}.csv"
        )
        write_csv(source_rows, source_path)
        out.at[idx, "source_occurrence_count"] = len(source_rows)
        out.at[idx, "source_occurrence_unique_count"] = duplicate_info["unique_count"]
        out.at[idx, "source_occurrence_duplicate_count"] = duplicate_info["duplicate_count"]
        out.at[idx, "source_occurrence_rows_path"] = str(source_path)
        out.at[idx, "source_occurrence_scope"] = "source_feature_rows_inside_plotctx_uti_window"
        out.at[idx, "source_occurrence_selection_rule"] = "actual_position_field_inside_node_window_for_extract_time_syms"
        if logger:
            symbol_count = source_rows["source_symbol"].nunique() if "source_symbol" in source_rows.columns and not source_rows.empty else 0
            logger.log(
                "SourceOccurrence",
                "已写入 source occurrence 明细",
                node_id=row["node_id"],
                level=row["level"],
                feature_key=row["anchor_feature_key"],
                row_count=len(source_rows),
                unique_count=duplicate_info["unique_count"],
                duplicate_count=duplicate_info["duplicate_count"],
                source_symbol_count=int(symbol_count),
                path=str(source_path),
            )
    return out


def mark_duplicate_occurrences(df: pd.DataFrame) -> dict[str, Any]:
    """标记原始 source occurrence 中重复出现的行。"""
    out = df.copy()
    duplicate_keys = [
        column
        for column in ["source_symbol", "x", "y", "xConfirm", "yConfirm", "uti", "uti1", "uti2", "deci_uti1", "deci_uti2"]
        if column in out.columns
    ]
    if out.empty or not duplicate_keys:
        if "is_duplicate_occurrence" not in out.columns:
            out["is_duplicate_occurrence"] = []
        return {"df": out, "unique_count": len(out), "duplicate_count": 0}
    duplicate_mask = out.duplicated(subset=duplicate_keys, keep="first")
    out["is_duplicate_occurrence"] = duplicate_mask
    duplicate_count = int(duplicate_mask.sum())
    return {"df": out, "unique_count": len(out) - duplicate_count, "duplicate_count": duplicate_count}


def _source_occurrence_rows_for_timespan(
    anchor: dict[str, Any],
    row: pd.Series,
    runtime: dict[str, Any] | None = None,
) -> pd.DataFrame:
    """按 node timespan 回查定位 anchor 的原始 occurrence 行。"""
    symbols = _source_symbols_for_row(row, runtime)
    if feature_target_scope(anchor) != "symbol" or not symbols:
        source_df = feature_df(anchor, runtime)
        binding = infer_time_binding(source_df, anchor.get("time_binding") or {})
        return slice_df(source_df, binding, row["start_uti"], row["end_uti"], runtime)

    frames: list[pd.DataFrame] = []
    for symbol in symbols:
        symbol_anchor = dict(anchor)
        symbol_anchor["target_type"] = "symbol"
        symbol_anchor["target_id"] = symbol
        source_df = feature_df(symbol_anchor, runtime)
        binding = infer_time_binding(source_df, symbol_anchor.get("time_binding") or {})
        sliced = slice_df(source_df, binding, row["start_uti"], row["end_uti"], runtime)
        if not sliced.empty:
            sliced = sliced.copy()
            if "source_symbol" not in sliced.columns:
                sliced.insert(0, "source_symbol", symbol)
        frames.append(sliced)
    if not frames:
        return pd.DataFrame()
    return pd.concat(frames, ignore_index=True)


def _source_symbols_for_row(row: pd.Series, runtime: dict[str, Any] | None = None) -> list[str]:
    raw = row.get("extract_time_syms", "")
    member_symbols = _json_list(row.get("member_symbols")) or []
    parsed = _json_value(raw)
    if isinstance(parsed, list):
        return [str(item) for item in parsed]
    if isinstance(parsed, str):
        if parsed == row.get("blk") and member_symbols:
            return [str(item) for item in member_symbols]
        try:
            from mquant.frame.lang import BlockTarType

            if parsed.startswith("blk@"):
                return [str(item) for item in BlockTarType.from_expr(parsed).symbols()]
        except Exception:
            pass
    target_id = row.get("target_id")
    return [] if target_id in (None, "", "unknown") else [str(target_id)]


def _json_value(value: Any) -> Any:
    if not isinstance(value, str):
        return value
    try:
        return json.loads(value)
    except Exception:
        return value


def _json_list(value: Any) -> list[Any]:
    parsed = _json_value(value)
    return parsed if isinstance(parsed, list) else []


def build_feature_slices(
    run_dir: Path,
    run_id: str,
    timespan_index: pd.DataFrame,
    evidence_features: list[dict[str, Any]],
    runtime: dict[str, Any] | None = None,
    logger: Any | None = None,
) -> pd.DataFrame:
    """为所有 node 和 evidence features 导出主证据切片。

    `slice_levels` 会在这里生效，用于控制某个 feature 只在 big / mid /
    small 的部分层级导出。
    """
    rows: list[dict[str, Any]] = []
    frames: dict[tuple[str, str, str], pd.DataFrame] = {}
    windows = [plotctx_uti_window(row.start_uti, row.end_uti, runtime) for row in timespan_index.itertuples()]
    windows = [window for window in windows if window is not None]
    bounds = (min(w[0] for w in windows), max(w[1] for w in windows)) if windows else None
    for _, timespan in timespan_index.iterrows():
        for base_anchor in evidence_features:
            if not _slice_level_enabled(base_anchor, str(timespan["level"])):
                if logger:
                    logger.log(
                        "FeatureSlice",
                        "按 slice_levels 跳过 feature slice",
                        node_id=timespan["node_id"],
                        level=timespan["level"],
                        feature_key=base_anchor.get("feature_key"),
                        slice_levels=base_anchor.get("slice_levels", ["big", "mid", "small"]),
                    )
                continue
            for anchor in _feature_slice_anchor_variants(base_anchor, timespan, runtime):
                rows.append(_build_one_feature_slice(run_dir, run_id, timespan, anchor, runtime, logger, frames=frames, bounds=bounds))
    return pd.DataFrame(rows)


def _slice_level_enabled(anchor: dict[str, Any], level: str) -> bool:
    levels = anchor.get("slice_levels")
    if levels in (None, "", "all"):
        return True
    return level in set(levels)


def _feature_slice_anchor_variants(
    anchor: dict[str, Any],
    timespan: pd.Series,
    runtime: dict[str, Any] | None = None,
) -> list[dict[str, Any]]:
    if feature_target_scope(anchor) != "symbol":
        return [anchor]

    explicit_symbols = anchor.get("export_symbols") or anchor.get("evidence_symbols")
    if explicit_symbols:
        symbols = [str(symbol) for symbol in explicit_symbols]
    else:
        symbols = _source_symbols_for_row(timespan, runtime)

    if not symbols and anchor.get("target_id") not in (None, "", "unknown"):
        symbols = [str(anchor.get("target_id"))]

    out: list[dict[str, Any]] = []
    seen: set[str] = set()
    for symbol in symbols:
        if symbol in seen:
            continue
        seen.add(symbol)
        symbol_anchor = dict(anchor)
        symbol_anchor["target_type"] = "symbol"
        symbol_anchor["target_id"] = symbol
        out.append(symbol_anchor)
    return out


def _build_one_feature_slice(
    run_dir: Path,
    run_id: str,
    timespan: pd.Series,
    anchor: dict[str, Any],
    runtime: dict[str, Any] | None = None,
    logger: Any | None = None,
    *,
    frames: dict | None = None,
    bounds: tuple[int, int] | None = None,
) -> dict[str, Any]:
    df_key = normalize_df_key(anchor.get("df_key"))
    target_type = _artifact_target_type(anchor)
    target_id = _artifact_target_id(anchor, runtime=runtime, symbol=anchor.get("target_id"))
    out_path = (
        run_dir
        / "feature_slices"
        / timespan["node_id"]
        / target_type
        / str(target_id)
        / anchor["feature_key"]
        / f"{df_key}.csv"
    )
    view_id = anchor.get("view_id", df_key)
    if view_id != df_key:
        out_path = out_path.with_name(f"{df_key}__{safe_path_token(view_id)}.csv")
    frepr = feature_repr(anchor)
    try:
        cache_key = (feature_identity_hash(anchor), df_key, str(target_id))
        full_df = frames.get(cache_key) if frames is not None else None
        if full_df is None:
            reader = getattr(anchor["feature"], "evidence_view_df", None)
            if callable(reader) and bounds is not None:
                with feature_runtime(anchor, runtime):
                    full_df = reader(None if df_key == "__default__" else df_key,
                                     start_uti=bounds[0], end_uti=bounds[1])
            else:
                full_df = feature_df(anchor, runtime)
            if frames is not None:
                frames[cache_key] = full_df
        binding = infer_time_binding(full_df, anchor.get("time_binding") or {})
        sliced = slice_df(full_df, binding, timespan["start_uti"], timespan["end_uti"], runtime)
        sliced = add_natural_time_columns(sliced, runtime, preferred_columns=_time_columns_for_anchor(anchor))
        write_csv(sliced, out_path)
        success = True
        error_message = ""
    except Exception as exc:
        binding = anchor.get("time_binding") or {}
        sliced = pd.DataFrame()
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text("", encoding="utf-8")
        success = False
        error_message = str(exc)

    fields = binding.get("uti_fields") or [binding.get("uti1_field") or ""]
    time_field_used = fields[0] if binding.get("time_mode") == "uti_point" else binding.get("uti1_field") or ""
    large_threshold = int((runtime or {}).get("large_slice_row_threshold", 10000))
    if logger:
        logger.log(
            "FeatureSlice",
            "已导出 feature slice",
            node_id=timespan["node_id"],
            level=timespan["level"],
            feature_key=anchor["feature_key"],
            target_id=target_id,
            row_count=len(sliced),
            column_count=len(sliced.columns),
            slice_success=success,
            error_message=error_message,
            path=str(out_path),
        )
    return {
        "run_id": run_id,
        "node_id": timespan["node_id"],
        "level": timespan["level"],
        "feature_key": anchor["feature_key"],
        "feature_name": anchor.get("feature_name") or anchor["feature_key"],
        "feature_ppid": feature_ppid(anchor),
        "feature_identity_hash": feature_identity_hash(anchor),
        "feature_repr": frepr,
        "feature_params_hash": sha1_text(frepr),
        "hash_method": HASH_METHOD,
        "slice_levels": json.dumps(anchor.get("slice_levels", ["big", "mid", "small"]), ensure_ascii=False),
        "target_type": target_type,
        "target_id": target_id,
        "df_key": anchor.get("df_key") or "",
        "df_key_normalized": df_key,
        "view_id": view_id,
        "time_mode": binding.get("time_mode"),
        "uti1_field": binding.get("uti1_field") or fields[0],
        "uti2_field": binding.get("uti2_field") or "",
        "time_field_used": time_field_used,
        "slice_window_start_uti": timespan["start_uti"],
        "slice_window_end_uti": timespan["end_uti"],
        "slice_window_start_ts": timespan.get("start_ts", timespan["start_uti"]),
        "slice_window_end_ts": timespan.get("end_ts", timespan["end_uti"]),
        "interval_policy": binding.get("interval_policy") or "point_inside",
        "slice_predicate": "plotctx_compatible_uti_window",
        "evidence_role": anchor.get("evidence_role", "internal_structure"),
        "selection_feature_id": anchor.get("selection_feature_id", ""),
        "selection_variant_id": anchor.get("selection_variant_id", ""),
        "is_raw_market_data": bool(anchor.get("is_raw_market_data", False)),
        "slice_success": success,
        "error_message": error_message,
        "row_count": len(sliced),
        "empty_slice_warning": success and len(sliced) == 0,
        "large_slice_warning": success and len(sliced) > large_threshold,
        "column_count": len(sliced.columns),
        "memory_bytes": int(sliced.memory_usage(deep=True).sum()),
        "export_format": "csv",
        "exported_file_path": str(out_path),
        "exported_file_bytes": out_path.stat().st_size,
    }


def _artifact_target_type(anchor: dict[str, Any]) -> str:
    return feature_target_scope(anchor)


def _artifact_target_id(
    anchor: dict[str, Any],
    *,
    runtime: dict[str, Any] | None = None,
    symbol: str | None = None,
    row: pd.Series | None = None,
) -> str:
    blk = (runtime or {}).get("blk")
    if not blk and row is not None:
        blk = row.get("blk")
    if feature_target_scope(anchor) == "symbol":
        value = symbol or anchor.get("target_id")
        if value not in (None, "", "unknown"):
            return str(value)
        return "extract_time_syms"
    return feature_target_id(anchor, blk=blk, symbol=symbol)


def _time_columns_for_anchor(anchor: dict[str, Any]) -> list[str]:
    binding = anchor.get("time_binding") or {}
    out = list(binding.get("uti_fields") or [])
    for key in ["uti1_field", "uti2_field"]:
        value = binding.get(key)
        if value:
            out.append(value)
    return out
