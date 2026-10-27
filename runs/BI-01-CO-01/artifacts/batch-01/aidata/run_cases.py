"""Execute the existing aidata way-2 chain for this batch's actual selected windows.
Does not acquire data outside aidata, select cases, or compose the final native page.
Run only in the authorized business environment; see the signed W03 work order.
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


def read_request(path: Path) -> tuple[dict[str, Any], list[tuple[str, str, str]]]:
    request = json.loads(path.read_text(encoding="utf-8"))
    if request.get("schema") != "bi01-case-inputs/v1":
        raise ValueError("Unexpected request schema")
    if request.get("work_order_id") != "BI01-CO-01-W03-CASES-30M-MID":
        raise ValueError("Unexpected work order")
    if request.get("symbols") != ["rb", "hc", "i"]:
        raise ValueError("Do not change the authorized object universe")
    if request.get("end_day") != "2024-02-29":
        raise ValueError("Unexpected Context end boundary")
    cases = request.get("cases", [])
    if [c.get("case_id") for c in cases] != [
        "CO01-C01", "CO01-C02", "CO01-C03", "CO01-C04"
    ]:
        raise ValueError("W03 must contain the four actual selected cases")
    spans = []
    for case in cases:
        start, end = case["manual_request"]
        core_start, core_end = case["core_close_dates"]
        for value in (start, end, core_start, core_end):
            if datetime.strptime(value, "%Y-%m-%d").strftime("%Y-%m-%d") != value:
                raise ValueError("Expected YYYY-MM-DD date boundary")
        if not ("2021-01-01" <= start <= core_start <= core_end < end <= request["end_day"]):
            raise ValueError(f"Invalid requested range: {case['case_id']}")
        spans.append((start, end, case["case_id"]))
    return request, spans


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, required=True)
    parser.add_argument("--request", type=Path, required=True)
    parser.add_argument("--output-root", type=Path, required=True)
    parser.add_argument("--run-id", required=True)
    args = parser.parse_args()
    if not args.run_id.strip():
        parser.error("--run-id must identify this actual new run")
    request, spans = read_request(args.request)

    input_path = args.repo_root / "professional/case_observation/examples/aidata_inputs.py"
    spec = importlib.util.spec_from_file_location("co01_aidata_inputs", input_path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Cannot load input constructor: {input_path}")
    inputs = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(inputs)

    from mquant.aidata.api import build_chart_run, build_big_world_chart_pages, build_board_run
    from mquant.aidata.profiles import ensure_profile_runtime

    ensure_profile_runtime()
    brief = inputs.make_case_brief(
        args.output_root, args.run_id, end_day=request["end_day"], timespans=spans
    )
    emit("request", {"request_file": str(args.request), "request": request,
                     "input_constructor": str(input_path), "run_id": args.run_id,
                     "output_root": str(args.output_root),
                     "context_start": "2021-01-01",
                     "context_end": request["end_day"],
                     "blk": brief["blk"], "extract_time_syms": brief["extract_time_syms"],
                     "calendar_override": brief["calendar_override"],
                     "generation_depth": brief["generation_depth"],
                     "big_source": brief["big_source"],
                     "features": ["kline_1d", "kline_30m", "scale_turn_mid"]})
    emit("build_chart_run", "STARTED")
    run = build_chart_run(brief, dry_run=False)
    emit("build_chart_run", {"returned_run_id": run.run_id})

    page_failed = False
    emit("build_big_world_chart_pages", "STARTED")
    try:
        pages = build_big_world_chart_pages(run, run_brief_input=brief, save=True)
        emit("build_big_world_chart_pages", pages.to_dict("records"))
    except Exception as error:
        page_failed = True
        emit("case_page_error", {"type": type(error).__name__, "message": str(error)})
        traceback.print_exc(file=sys.stderr)

    # Formal data remain useful even if a page failed. Do not label that full PASS.
    emit("build_board_run", {"state": "STARTED", "reuse_core": True, "run_id": run.run_id})
    board = build_board_run({**brief, "run_id": run.run_id}, reuse_core=True, dry_run=False)
    emit("build_board_run", {
        "delivery_manifest_path": str(board.delivery_manifest_path),
        "feature_slice_stats_path": str(board.feature_slice_stats_path)})
    emit("remaining", "Native single-page composition, actual opening, coverage checks and Pro consumption")
    return 2 if page_failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
