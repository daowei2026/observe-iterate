"""BI-01-CO-01: invoke the existing aidata full-history 1d chain.

Run only inside the authorized /dwdhome/fy/BASE_E6_2 environment.
This file does not select cases, query market data directly, or compose the final page.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import importlib.util
import json
from pathlib import Path
import sys
import traceback
from typing import Any


def emit(name: str, value: Any) -> None:
    print(json.dumps({"utc": datetime.now(timezone.utc).isoformat(),
                      "name": name, "value": value},
                     ensure_ascii=False, default=str), flush=True)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, required=True)
    parser.add_argument("--output-root", type=Path, required=True)
    parser.add_argument("--run-id", required=True)
    args = parser.parse_args()
    if not args.run_id.strip():
        parser.error("--run-id must identify this actual new run")

    # Load the existing input constructor; never import the old probe.py,
    # whose top-level code runs the historical 2013/large test.
    input_path = args.repo_root / "professional/case_observation/examples/aidata_inputs.py"
    if not input_path.is_file():
        raise FileNotFoundError(input_path)
    spec = importlib.util.spec_from_file_location("co01_aidata_inputs", input_path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Cannot load input constructor: {input_path}")
    inputs = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(inputs)

    from mquant.aidata.api import (
        build_chart_run, build_run_overview_chart_page, build_board_run,
    )
    from mquant.aidata.profiles import ensure_profile_runtime

    # Existing process-local profile setup from the known working call chain.
    # This is not permission to register new global features or alter services.
    ensure_profile_runtime()
    brief = inputs.make_overview_brief(
        args.output_root, args.run_id, end_day="2024-02-29"
    )
    emit("request", {
        "input_constructor": str(input_path), "run_id": args.run_id,
        "output_root": str(args.output_root), "startDay": "2021-01-01",
        "endDay": "2024-02-29", "sof_name": "TA_updto20240229_DBA",
        "stk_tlist": "tick_test_all57_takeout_lcNsiNcy", "blk": brief["blk"],
        "extract_time_syms": brief["extract_time_syms"],
        "calendar_override": brief["calendar_override"],
        "generation_depth": brief["generation_depth"],
        "big_source": brief["big_source"], "evidence_feature_key": "kline_1d",
        "time_field": "closeUti", "frequency": "1d",
    })
    emit("build_chart_run", "STARTED")
    run = build_chart_run(brief, dry_run=False)
    emit("build_chart_run", {"returned_run_id": run.run_id})

    page_failed = False
    emit("build_run_overview_chart_page", "STARTED")
    try:
        page = build_run_overview_chart_page(run, run_brief_input=brief, save=True)
        emit("build_run_overview_chart_page", page.to_dict("records"))
    except Exception as error:
        page_failed = True
        emit("overview_error", {"type": type(error).__name__, "message": str(error)})
        traceback.print_exc(file=sys.stderr)
        # A page failure is not evidence that the formal data cannot be produced.

    emit("build_board_run", {"state": "STARTED", "reuse_core": True,
                             "run_id": run.run_id})
    board = build_board_run({**brief, "run_id": run.run_id},
                            reuse_core=True, dry_run=False)
    emit("build_board_run", {
        "delivery_manifest_path": str(board.delivery_manifest_path),
        "feature_slice_stats_path": str(board.feature_slice_stats_path),
    })
    emit("scope", "API return only; data coverage, page opening and research remain to be checked")
    return 2 if page_failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
