#!/usr/bin/env python3
"""Prepare the BI-01 CO-05 full-range chart and matching formal aidata delivery.

Business choices are fixed by the issuing Professional:
- symbols: rb, hc, i (steel-chain comparison)
- market frequency: 30m
- main visible/data window: [2021-01-04 00:00:00, 2024-03-01 00:00:00)
- evidence layers: 30m KLine, ScaleTurnCalendar("large"),
  ScaleTurnCalendar("mid")
- no default small-scale layer
- one full-range main page plus deterministic half-year auxiliary pages
- chart and formal data must come from the same run/core

The Worker may make only ordinary compatibility/path/serialization fixes needed
by the current authorized aidata checkout. It may not change these semantic
choices. Any compatibility copy and diff must be returned to the issuing
Professional; this file itself and shared aidata/mquant/tis/FRP source must not
be overwritten.
"""

from __future__ import annotations

import hashlib
import json
from datetime import datetime
from pathlib import Path
from typing import Any, Iterable

from mquant.aidata.api import (
    build_big_world_chart_pages,
    build_board_run,
    build_chart_run,
    make_point_anchor,
)
from mquant.aidata.profiles import ensure_profile_runtime
from mquant.frame import KLine
from mquant.quant import OptContext
from mquant.tis import ScaleTurnCalendar


# Owner-fixed CO-05 environment inputs.
SOF_NAME = "GTQH_L1_20210104_20240229"
STK_TLIST = "gtqh_four"

# Professional-fixed business inputs.
EXPECTED_SYMBOLS = ("rb", "hc", "i")
BAR_FREQUENCY = "30m"
REQUEST_START = "2021-01-04"
REQUEST_END_EXCLUSIVE = "2024-03-01"
REQUEST_START_TS = "2021-01-04 00:00:00"
REQUEST_END_EXCLUSIVE_TS = "2024-03-01 00:00:00"
MAIN_WINDOW_ID = "BI01-CO05-FULL-20210104-20240301"
BLOCK_EXPRESSION = "blk@steel"

# The source itself starts on 2021-01-04. No earlier warm-up history is
# invented. Feature-effective coverage may therefore start later and must be
# reported from the formal delivery.
CONTEXT_START = "2021-01-04"
CONTEXT_END = "2024-02-29"

# The main full-range page is mandatory and comes first. Deterministic
# half-year pages are auxiliary readability views only; they neither replace
# the main page nor narrow the formal full-range request.
MAIN_TIMESPAN = (REQUEST_START, REQUEST_END_EXCLUSIVE, MAIN_WINDOW_ID)
AUXILIARY_TIMESPANS = (
    ("2021-01-04", "2021-07-01", "BI01-CO05-AUX-2021H1"),
    ("2021-07-01", "2022-01-01", "BI01-CO05-AUX-2021H2"),
    ("2022-01-01", "2022-07-01", "BI01-CO05-AUX-2022H1"),
    ("2022-07-01", "2023-01-01", "BI01-CO05-AUX-2022H2"),
    ("2023-01-01", "2023-07-01", "BI01-CO05-AUX-2023H1"),
    ("2023-07-01", "2024-01-01", "BI01-CO05-AUX-2023H2"),
    ("2024-01-01", "2024-03-01", "BI01-CO05-AUX-2024P"),
)
PAGE_TIMESPANS = (MAIN_TIMESPAN, *AUXILIARY_TIMESPANS)

OUTPUT_ROOT = Path(
    "/dwdhome/fy/BASE_E6_2/mquant/aidata/test_runs/"
    "bi01_co05_r0008_fullrange_chart_data"
)


def _jsonable(value: Any) -> Any:
    """Convert common aidata/pandas return values into JSON-safe objects."""
    if value is None or isinstance(value, (str, int, float, bool)):
        return value
    if isinstance(value, Path):
        return str(value)
    if isinstance(value, dict):
        return {str(k): _jsonable(v) for k, v in value.items()}
    if isinstance(value, (list, tuple, set)):
        return [_jsonable(v) for v in value]
    if hasattr(value, "isoformat"):
        try:
            return value.isoformat()
        except (TypeError, ValueError):
            pass
    if hasattr(value, "item"):
        try:
            return value.item()
        except (TypeError, ValueError):
            pass
    return str(value)


def _records(frame_or_records: Any) -> list[dict[str, Any]]:
    """Normalize page results without imposing an undocumented schema."""
    if hasattr(frame_or_records, "to_dict"):
        records = frame_or_records.to_dict("records")
    elif isinstance(frame_or_records, list):
        records = frame_or_records
    else:
        raise RuntimeError(
            "build_big_world_chart_pages returned an unsupported result type: "
            f"{type(frame_or_records)!r}"
        )
    if not records:
        raise RuntimeError("No chart page record was produced.")
    normalized = [_jsonable(record) for record in records]
    if not all(isinstance(record, dict) for record in normalized):
        raise RuntimeError("Chart page result did not normalize to dictionaries.")
    return normalized


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _required_path(value: Any, label: str) -> Path:
    if value is None:
        raise RuntimeError(f"{label} was not returned by build_board_run.")
    path = Path(str(value))
    if not path.exists():
        raise RuntimeError(f"{label} does not exist: {path}")
    return path


def _optional_existing_path(obj: Any, names: Iterable[str]) -> dict[str, str] | None:
    """Return the first exposed existing path without guessing a schema."""
    for name in names:
        value = getattr(obj, name, None)
        if value is None:
            continue
        path = Path(str(value))
        if path.exists():
            return {
                "attribute": name,
                "path": str(path),
                "sha256": _sha256(path) if path.is_file() else "",
            }
    return None


def _kline_evidence() -> Any:
    return make_point_anchor(
        KLine(freq=BAR_FREQUENCY),
        uti_fields="closeUti",
        label="30m KLine 正式行情数据",
        feature_key="bi01_co05_kline_30m_fullrange",
        slice_levels=["big"],
        evidence_role="market_context_sidecar",
        is_raw_market_data=True,
    )


def _turn_evidence(scale: str, marker: str, size: int, label: str) -> Any:
    return make_point_anchor(
        ScaleTurnCalendar(scale),
        uti_fields="x",
        label=label,
        feature_key=f"bi01_co05_scale_turn_{scale}_fullrange",
        slice_levels=["big"],
        plot_binding={
            "kind": "point",
            "x_field": "x",
            "y_field": "y",
            "label": label,
            "surfaces": ["big"],
            "style": {"marker": marker, "size": size},
        },
    )


def _request_contract(run_id: str) -> dict[str, Any]:
    return {
        "schema": "bi01-co05-fullrange-chart-data-request/v1",
        "run_id": run_id,
        "professional_fixed_inputs": {
            "symbols": list(EXPECTED_SYMBOLS),
            "bar_frequency": BAR_FREQUENCY,
            "main_window": {
                "start": REQUEST_START_TS,
                "end_exclusive": REQUEST_END_EXCLUSIVE_TS,
                "window_id": MAIN_WINDOW_ID,
            },
            "auxiliary_timespans": [
                {"start": start, "end_exclusive": end, "window_id": window_id}
                for start, end, window_id in AUXILIARY_TIMESPANS
            ],
            "features": [
                "KLine(30m)",
                'ScaleTurnCalendar("large")',
                'ScaleTurnCalendar("mid")',
            ],
            "small_scale_enabled": False,
            "main_page_required": True,
            "auxiliary_pages_replace_main": False,
            "one_figure_multi_symbol": True,
            "relative_price_ratio_axis": True,
            "rb_background_axis": True,
            "calendar_policy": "source_symbol_own_calendar",
        },
        "owner_fixed_context": {
            "sof_name": SOF_NAME,
            "stk_tlist": STK_TLIST,
            "context_start": CONTEXT_START,
            "context_end": CONTEXT_END,
        },
        "identity_requirement": "chart_and_formal_data_same_run_core",
        "coverage_policy": {
            "requested_range_is_not_claimed_actual_coverage": True,
            "do_not_fill_missing_source_times": True,
            "report_actual_first_last_rows_missing_duplicates_per_symbol_layer": True,
            "report_feature_warmup_or_effective_start_separately": True,
        },
    }


def main() -> int:
    OUTPUT_ROOT.mkdir(parents=True, exist_ok=True)
    ensure_profile_runtime()

    run_id = f"BI01_CO05_R0008_FULL_LM_{datetime.now():%Y%m%d_%H%M%S}"
    context = OptContext(
        {
            "sof_name": SOF_NAME,
            "stk_tlist": STK_TLIST,
            "startDay": CONTEXT_START,
            "endDay": CONTEXT_END,
        }
    )

    request_contract = _request_contract(run_id)
    preflight_contract_path = OUTPUT_ROOT / f"{run_id}_REQUEST_CONTRACT.json"
    preflight_contract_path.write_text(
        json.dumps(request_contract, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    brief = {
        "output_root": str(OUTPUT_ROOT),
        "run_id": run_id,
        "run_note": (
            "BI-01 CO-05 R0008: rb/hc/i 30m full-range large+mid chart "
            "and matching formal data for Professional observation"
        ),
        "context": context,
        # The authorized historical interface used blk@steel for this exact
        # rb/hc/i comparison. Worker must verify actual rendered/delivered
        # symbols are exactly EXPECTED_SYMBOLS. If the current API requires
        # another explicit-symbol syntax, changing only this selector is an
        # ordinary compatibility fix and must be returned as a diff.
        "blk": BLOCK_EXPRESSION,
        "extract_time_syms": BLOCK_EXPRESSION,
        "generation_depth": "big",
        "big_source": {
            "mode": "manual",
            "timespans": list(PAGE_TIMESPANS),
        },
        "evidence_features": [
            _kline_evidence(),
            _turn_evidence(
                "large",
                marker="triangle",
                size=17,
                label="30m 大尺度贴近转折（L）",
            ),
            _turn_evidence(
                "mid",
                marker="diamond",
                size=12,
                label="30m 中尺度贴近转折（M）",
            ),
        ],
    }

    run = build_chart_run(brief, dry_run=False)
    pages = build_big_world_chart_pages(
        run,
        run_brief_input=brief,
        save=True,
    )
    board = build_board_run(
        {**brief, "run_id": run.run_id},
        reuse_core=True,
        dry_run=False,
    )

    page_records = _records(pages)
    feature_slice_stats = _required_path(
        getattr(board, "feature_slice_stats_path", None),
        "feature_slice_stats_path",
    )
    delivery_manifest = _required_path(
        getattr(board, "delivery_manifest_path", None),
        "delivery_manifest_path",
    )
    exposed_file_index = _optional_existing_path(
        board,
        (
            "file_index_path",
            "delivery_file_index_path",
            "formal_file_index_path",
            "delivery_index_path",
        ),
    )

    receipt = {
        **request_contract,
        "schema": "bi01-co05-fullrange-chart-data-run/v1",
        "run_id": str(run.run_id),
        "output_root": str(OUTPUT_ROOT),
        "page_records": page_records,
        "formal_delivery": {
            "feature_slice_stats_path": str(feature_slice_stats),
            "feature_slice_stats_sha256": _sha256(feature_slice_stats),
            "delivery_manifest_path": str(delivery_manifest),
            "delivery_manifest_sha256": _sha256(delivery_manifest),
            "file_index_if_exposed": exposed_file_index,
        },
        "required_worker_verification": {
            "actual_symbols_exactly": list(EXPECTED_SYMBOLS),
            "actual_main_window": [REQUEST_START_TS, REQUEST_END_EXCLUSIVE_TS],
            "main_window_id": MAIN_WINDOW_ID,
            "all_expected_window_ids": [
                window_id for _, _, window_id in PAGE_TIMESPANS
            ],
            "actual_layers": ["30m KLine", "large turns", "mid turns"],
            "small_absent_by_default": True,
            "full_range_main_page_present": True,
            "auxiliary_pages_are_additional_only": True,
            "one_figure_multi_symbol": True,
            "relative_price_ratio_axis": True,
            "source_symbol_own_calendars": True,
            "rb_background_axis": True,
            "page_opened_and_visually_checked": True,
            "formal_delivery_opened_and_read": True,
            "actual_coverage_and_missingness_reported": True,
            "manifest_and_file_index_read": True,
            "same_run_core_correspondence_checked": True,
        },
        "preflight_request_contract_path": str(preflight_contract_path),
        "preflight_request_contract_sha256": _sha256(preflight_contract_path),
    }

    receipt_path = (
        OUTPUT_ROOT
        / str(run.run_id)
        / "PROFESSIONAL_REQUEST_RECEIPT.json"
    )
    receipt_path.parent.mkdir(parents=True, exist_ok=True)
    receipt_path.write_text(
        json.dumps(receipt, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    print(
        json.dumps(
            {**receipt, "receipt_path": str(receipt_path)},
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
