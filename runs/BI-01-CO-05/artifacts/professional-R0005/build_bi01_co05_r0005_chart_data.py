#!/usr/bin/env python3
"""Prepare the BI-01 CO-05 chart and matching formal aidata delivery.

Business choices are fixed by the issuing Professional:
- symbols: rb, hc, i (steel-chain comparison)
- market frequency: 30m
- visible window: [2021-08-15 00:00, 2021-09-30 00:00)
- evidence layers: 30m KLine, ScaleTurnCalendar("large"),
  ScaleTurnCalendar("mid")

The Worker may make only ordinary compatibility/path fixes needed by the
current authorized aidata checkout. It may not change these semantic choices.
"""

from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path
from typing import Any

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
WINDOW_START = "2021-08-15"
WINDOW_END_EXCLUSIVE = "2021-09-30"
WINDOW_ID = "BI01-CO05-C001"
BLOCK_EXPRESSION = "blk@steel"
# The context starts well before the visible window so the current authorized
# feature implementation has history available. The visible graph/data window
# remains the manual timespan above.
CONTEXT_START = "2021-01-04"
CONTEXT_END = "2021-10-31"

OUTPUT_ROOT = Path(
    "/dwdhome/fy/BASE_E6_2/mquant/aidata/test_runs/"
    "bi01_co05_r0005_chart_data"
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
    """Normalize the page result without imposing an undocumented schema."""
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
    return [_jsonable(record) for record in records]


def _kline_evidence() -> Any:
    return make_point_anchor(
        KLine(freq=BAR_FREQUENCY),
        uti_fields="closeUti",
        label="30m KLine 正式行情数据",
        feature_key="bi01_co05_kline_30m",
        slice_levels=["big"],
        evidence_role="market_context_sidecar",
        is_raw_market_data=True,
    )


def _turn_evidence(scale: str, marker: str, size: int, label: str) -> Any:
    return make_point_anchor(
        ScaleTurnCalendar(scale),
        uti_fields="x",
        label=label,
        feature_key=f"bi01_co05_scale_turn_{scale}",
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


def main() -> int:
    OUTPUT_ROOT.mkdir(parents=True, exist_ok=True)
    ensure_profile_runtime()

    run_id = f"BI01_CO05_R0005_LM_{datetime.now():%Y%m%d_%H%M%S}"
    context = OptContext(
        {
            "sof_name": SOF_NAME,
            "stk_tlist": STK_TLIST,
            "startDay": CONTEXT_START,
            "endDay": CONTEXT_END,
        }
    )

    brief = {
        "output_root": str(OUTPUT_ROOT),
        "run_id": run_id,
        "run_note": (
            "BI-01 CO-05: rb/hc/i 30m large+mid turn chart and matching "
            "formal data for Professional observation"
        ),
        "context": context,
        # The authorized historical interface uses blk@steel for this exact
        # rb/hc/i steel-chain comparison. The Worker must verify that the
        # actual rendered/delivered symbols are exactly EXPECTED_SYMBOLS; if
        # the current API requires another explicit-symbol syntax, changing
        # only this selector is an ordinary compatibility fix.
        "blk": BLOCK_EXPRESSION,
        "extract_time_syms": BLOCK_EXPRESSION,
        "generation_depth": "big",
        "big_source": {
            "mode": "manual",
            "timespans": [
                (WINDOW_START, WINDOW_END_EXCLUSIVE, WINDOW_ID),
            ],
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
    feature_slice_stats = Path(str(board.feature_slice_stats_path))
    delivery_manifest = Path(str(board.delivery_manifest_path))
    missing = [
        str(path)
        for path in (feature_slice_stats, delivery_manifest)
        if not path.exists()
    ]
    if missing:
        raise RuntimeError(
            "The formal board call returned paths that do not exist: "
            + ", ".join(missing)
        )

    receipt = {
        "schema": "bi01-co05-chart-data-run/v1",
        "run_id": str(run.run_id),
        "output_root": str(OUTPUT_ROOT),
        "professional_fixed_inputs": {
            "symbols": list(EXPECTED_SYMBOLS),
            "bar_frequency": BAR_FREQUENCY,
            "window_start": WINDOW_START,
            "window_end_exclusive": WINDOW_END_EXCLUSIVE,
            "features": [
                "KLine(30m)",
                'ScaleTurnCalendar("large")',
                'ScaleTurnCalendar("mid")',
            ],
            "small_scale_enabled": False,
        },
        "owner_fixed_context": {
            "sof_name": SOF_NAME,
            "stk_tlist": STK_TLIST,
        },
        "professional_runtime_context": {
            "context_start": CONTEXT_START,
            "context_end": CONTEXT_END,
            "calendar_policy": "source_symbol_own_calendar",
        },
        "page_records": page_records,
        "formal_delivery": {
            "feature_slice_stats_path": str(feature_slice_stats),
            "delivery_manifest_path": str(delivery_manifest),
        },
        "required_worker_verification": {
            "actual_symbols_exactly": list(EXPECTED_SYMBOLS),
            "actual_visible_window": [WINDOW_START, WINDOW_END_EXCLUSIVE],
            "actual_layers": ["30m KLine", "large turns", "mid turns"],
            "one_figure_multi_symbol": True,
            "relative_price_ratio_axis": True,
            "source_symbol_own_calendars": True,
            "rb_background_axis": True,
            "page_opened_and_visually_checked": True,
            "formal_delivery_opened_and_read": True,
            "same_run_core_correspondence_checked": True,
        },
    }

    receipt_path = OUTPUT_ROOT / str(run.run_id) / "PROFESSIONAL_REQUEST_RECEIPT.json"
    receipt_path.parent.mkdir(parents=True, exist_ok=True)
    receipt_path.write_text(
        json.dumps(receipt, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    print(json.dumps({**receipt, "receipt_path": str(receipt_path)}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
