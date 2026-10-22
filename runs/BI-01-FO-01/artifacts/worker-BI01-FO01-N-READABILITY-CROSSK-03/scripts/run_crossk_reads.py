#!/usr/bin/env python3
"""对 W03 具名 i/hc 切点执行正常 OnlyRead，并保存完整原表。"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import inspect
import json
import subprocess
import time
from pathlib import Path
from typing import Any
from uuid import UUID

import numpy as np
import pandas as pd
from m3sof.settings.json import eval2
from m3tt import CurrTradeSet
from mquant.frame import CalType, CurrCalendar, CurrIndustry
from mquant.quant import OptContext
from mquant.tis.calendar.base import blk_suitable_calendars
from mquant.tis.frp.U2Mainline import U2MainlineKLineInput
from mquant.tis.frp.U2NodeBehavior import U2NormalNodeBehaviorFrp
from mquant.tis.lib3 import CurrSymbol
import mquant.aidata.u2_normal_node_behavior_display as display_module
import mquant.tis.frp.U2NodeBehavior as node_module
import mquant.tis.frp.U2ThinNode as thin_module
import mquant.uplot as uplot_module
import mquant.worker.adt.u2_node as worker_schema


SOF = "TA_updto20240229_DBA"
CONTEXT = "blk@steel"
CALENDAR = "night_end_at_2300"
EXPECTED_PRODUCT_DIR = Path(
    "/m3varK/BaseData/futures/TA_updto20240229_DBA/fao/prod/"
    "U2NormalNodeBehaviorFrp/9/0/d/3/7/a/4/"
    "fb2007d71be1e620801457424d6dea8b4/func"
)
PRODUCTS = (*display_module.FORMAL_PRODUCTS, "intervals")
CASES = (
    ("i_before_missing_recovery", "i", "9410abda-b111-442d-aa25-6b99da2afeb6", 35360400),
    ("i_recovery", "i", "9410abda-b111-442d-aa25-6b99da2afeb6", 35361000),
    ("i_after_recovery", "i", "9410abda-b111-442d-aa25-6b99da2afeb6", 35361600),
    ("hc_final", "hc", "6f92034c-bd94-4d3f-8b7c-6c69e24959ff", 103315800),
)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def clean(value: Any) -> Any:
    if isinstance(value, dict):
        return {str(key): clean(item) for key, item in value.items()}
    if isinstance(value, (list, tuple, set)):
        return [clean(item) for item in value]
    if isinstance(value, np.generic):
        return clean(value.item())
    if value is pd.NA or value is pd.NaT or (isinstance(value, float) and not np.isfinite(value)):
        return None
    if isinstance(value, (pd.Timestamp, dt.datetime, Path)):
        return str(value)
    return value


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(clean(payload), ensure_ascii=False, indent=2, allow_nan=False) + "\n",
        encoding="utf-8",
    )


def export_frame(frame: pd.DataFrame, path: Path) -> dict[str, Any]:
    path.parent.mkdir(parents=True, exist_ok=True)
    public = frame.reset_index()
    public.to_csv(path, index=False)
    return {
        "path": str(path), "rows": int(len(public)),
        "columns": list(public.columns), "bytes": path.stat().st_size,
        "sha256": sha256(path),
    }


def git_value(repo: Path, *args: str) -> str:
    return subprocess.check_output(
        ["git", "-C", str(repo), *args], text=True, stderr=subprocess.STDOUT
    ).strip()


def calendar_name(value: Any) -> str:
    for field in ("name", "calendar", "life"):
        candidate = getattr(value, field, None)
        if candidate:
            return str(candidate)
    return str(value)


def resolve_calendar(context: OptContext) -> tuple[Any, list[str]]:
    candidates = tuple(blk_suitable_calendars(context.sof, CONTEXT))
    matches = [value for value in candidates if calendar_name(value) == CALENDAR]
    if len(matches) != 1:
        raise RuntimeError(f"expected one {CALENDAR}; got {[calendar_name(v) for v in candidates]}")
    return matches[0], [calendar_name(value) for value in candidates]


def identifier(row: pd.Series, prefix: str = "") -> str:
    form = int(row[prefix + "form"])
    high = int(row[prefix + "high"])
    low = int(row[prefix + "low"])
    text = str(row[prefix + "text"] or "")
    if form == 1 and not text:
        return str(UUID(int=(high << 64) | low))
    if form == 2 and high == low == 0 and text:
        return text
    raise ValueError("invalid identifier")


def one(frame: pd.DataFrame) -> pd.Series:
    public = frame.reset_index()
    if len(public) != 1:
        raise RuntimeError(f"expected one row, got {len(public)}")
    return public.iloc[0]


def scalar(frames: dict[str, pd.DataFrame], name: str) -> dict[str, Any]:
    row = one(frames[name])
    return {
        "value": clean(row["value"]), "present": int(row["present"]),
        "knownness": int(row["knownness"]), "applicability": int(row["applicability"]),
        "reason": int(row["reason"]),
    }


def case_summary(symbol: str, life: str, requested_k: int, frames: dict[str, pd.DataFrame]) -> dict[str, Any]:
    origin, revision = one(frames["origins"]), one(frames["revisions"])
    binding, window, base = one(frames["bindings"]), one(frames["windows"]), one(frames["working_bases"])
    working = one(frames["working_values"])
    rhythm = one(frames["rhythm"])
    intervals = frames["intervals"].reset_index().sort_values("child_id_3", kind="stable")
    exact = (
        f"NodeBehaviorBook/NodeScaleTurnBehaviorRevision/{life}/{identifier(revision)}"
    )
    return {
        "symbol": symbol, "requested_k": requested_k,
        "resolved_as_of": int(origin["as_of"]), "timestamp": str(origin["timestamp"]),
        "occurrence": int(origin["occurrence"]), "record_id": int(origin["record_id"]),
        "source_exact": exact, "binding": int(binding["address"]),
        "window": int(window["address"]), "working_address": int(base["address"]),
        "working_life": identifier(base, "life_"), "working_start": int(base["start_value"]),
        "working_direction": int(base["direction"]), "working_through": int(working["through_value"]),
        "working_completion_knownness": int(working["completion_knownness"]),
        "scalars": {
            name: scalar(frames, name) for name in (
                "working_progress", "working_efficiency", "working_counter",
                "working_duration", "working_waiting", "working_waiting_ratio",
            )
        },
        "rhythm": clean({key: rhythm[key] for key in (
            "local_count", "knownness", "full_count_value", "full_count_present",
            "local_start_value", "local_start_present", "last_update_value",
            "last_update_present", "current_median_value", "current_median_present",
        )}),
        "intervals": clean(intervals[["child_id_3", "duration", "present"]].to_dict("records")),
        "recent_member_count": int(len(frames["recent_members"])),
        "previous_member_count": int(len(frames["previous_members"])),
    }


def read_price(
    *, context: OptContext, calendar: Any, symbol: str, start_uti: int, end_uti: int
) -> tuple[pd.DataFrame, dict[str, Any]]:
    with CurrTradeSet(context.sof), CurrIndustry(CONTEXT), CurrCalendar(calendar), CurrSymbol(symbol):
        feature = U2MainlineKLineInput(
            source=eval2("MapKLineOpenData(freq='5m')"),
            calendar_grid=eval2("ResampleCalendarTsa(resample_len=600)"),
        )
        full = feature.rerun(CalType.OnlyRead).to_df()
        product_dir = str(feature.full_dir)
    selected = full.loc[
        full["open_uti"].astype(np.int64).between(start_uti, end_uti, inclusive="both"),
        ["open_uti", "open", "high", "low", "close", "volume", "openInt",
         "calendar_position", "calendar_time"],
    ].copy()
    return selected, {
        "entry": "U2MainlineKLineInput.rerun(CalType.OnlyRead).to_df",
        "product_dir": product_dir, "requested_range": [start_uti, end_uti],
        "actual_range": [int(selected["open_uti"].min()), int(selected["open_uti"].max())],
        "rows": int(len(selected)), "missing_close": int(selected["close"].isna().sum()),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--w02-root", type=Path, required=True)
    parser.add_argument("--output-root", type=Path, required=True)
    parser.add_argument("--aidata-repo", type=Path, required=True)
    parser.add_argument("--uplot-repo", type=Path, required=True)
    args = parser.parse_args()
    started = dt.datetime.now(dt.timezone.utc)
    root = args.output_root.resolve()
    configuration = args.w02_root.resolve() / "inputs" / "ACTUAL_RUN_CONFIGURATION.json"
    actual = json.loads(configuration.read_text(encoding="utf-8"))
    sources = actual["配置"]["source"]["sources"]
    objects = [source["source"]["source"]["scope"]["object"] for source in sources]
    if set(objects) != {"rb", "hc", "i"} or len(objects) != 3:
        raise RuntimeError(f"complete source identity changed: {objects}")

    context = OptContext(sof_name=SOF)
    calendar, calendar_candidates = resolve_calendar(context)
    case_results: dict[str, Any] = {}
    exports: dict[str, Any] = {}
    with CurrTradeSet(context.sof), CurrIndustry(CONTEXT), CurrCalendar(calendar):
        feature = U2NormalNodeBehaviorFrp.from_sources(sources, compact_history=True)
        if Path(str(feature.full_dir)) != EXPECTED_PRODUCT_DIR:
            raise RuntimeError(f"unexpected product dir: {feature.full_dir}")
        feature.rerun(CalType.OnlyRead)
        for case_id, symbol, life, knowledge_k in CASES:
            print(f"READ_START {case_id} K={knowledge_k}", flush=True)
            case_started = time.monotonic()
            frames = feature.read_at_knowledge(life, knowledge_k, products=list(PRODUCTS))
            case_dir = root / "data" / "crossk" / case_id
            exports[case_id] = {
                name: export_frame(frame, case_dir / f"{name}.csv")
                for name, frame in frames.items()
            }
            result = case_summary(symbol, life, knowledge_k, frames)
            result["elapsed_seconds"] = time.monotonic() - case_started
            case_results[case_id] = result
            print(
                f"READ_DONE {case_id} resolved={result['resolved_as_of']} "
                f"exact={result['source_exact']}", flush=True,
            )

    hc_price, hc_price_runtime = read_price(
        context=context, calendar=calendar, symbol="hc", start_uti=103044000, end_uti=103315800
    )
    hc_price_export = export_frame(
        hc_price, root / "data" / "crossk" / "hc_final" / "hc_5m_price_calendar.csv"
    )

    i_before = case_results["i_before_missing_recovery"]
    i_recovery = case_results["i_recovery"]
    i_after = case_results["i_after_recovery"]
    hc = case_results["hc_final"]
    durations = [
        float(item["duration"]) for item in hc["intervals"] if int(item["present"]) == 1
    ]
    recent_three = durations[-3:]
    summary = {
        "schema_version": 1, "order_id": "BI01-FO01-N-READABILITY-CROSSK-03",
        "formal_mode": "CalType.OnlyRead + read_at_knowledge(explicit Life, integer K)",
        "i": {
            "resolved_occurrences": [
                {key: case_results[name][key] for key in (
                    "requested_k", "resolved_as_of", "timestamp", "occurrence", "source_exact"
                )}
                for name in ("i_before_missing_recovery", "i_recovery", "i_after_recovery")
            ],
            "same_working_life": len({i_before["working_life"], i_recovery["working_life"], i_after["working_life"]}) == 1,
            "same_start_direction": len({
                (item["working_start"], item["working_direction"])
                for item in (i_before, i_recovery, i_after)
            }) == 1,
            "storage_addresses": [i_before["working_address"], i_recovery["working_address"], i_after["working_address"]],
            "before_scalars": i_before["scalars"], "recovery_scalars": i_recovery["scalars"],
            "after_scalars": i_after["scalars"], "recovery_rhythm": i_recovery["rhythm"],
            "conclusion_boundary": (
                "恢复拍是实际正式发生；端点progress、duration与waiting恢复，其中waiting为真实零；"
                "efficiency/counter/ratio及intervals仍不可用。后一拍保持同Life，不能称为全量恢复。"
            ),
            "price_context_reference": {
                "path": str(args.w02_root.resolve() / "data/i_missing_context/i_5m_price_calendar.csv"),
                "sha256": sha256(args.w02_root.resolve() / "data/i_missing_context/i_5m_price_calendar.csv"),
                "qualification": "W02 normal OnlyRead export reused without rereading",
            },
        },
        "hc": {
            "source_exact": hc["source_exact"], "window": hc["window"],
            "working_address": hc["working_address"], "working_life": hc["working_life"],
            "working_start": hc["working_start"], "working_through": hc["working_through"],
            "waiting": hc["scalars"]["working_waiting"],
            "waiting_ratio": hc["scalars"]["working_waiting_ratio"],
            "rhythm": hc["rhythm"], "intervals": hc["intervals"],
            "recent_three_intervals": recent_three,
            "recent_three_median": float(np.median(recent_three)),
            "denominator_matches_formal_current_median": (
                float(np.median(recent_three)) == float(hc["rhythm"]["current_median_value"])
            ),
            "qualification": "分母直接来自正式intervals最后三项及rhythm原表，不由258000/430反推。",
            "price_runtime": hc_price_runtime, "price_export": hc_price_export,
        },
    }
    write_json(root / "evidence" / "CROSSK_SUMMARY.json", summary)
    manifest = {
        "schema_version": 1, "result": "PASS", "started_at": started.isoformat(),
        "finished_at": dt.datetime.now(dt.timezone.utc).isoformat(),
        "configuration": {"path": str(configuration), "sha256": sha256(configuration), "objects": objects},
        "formal_product_dir": str(EXPECTED_PRODUCT_DIR), "calendar_candidates": calendar_candidates,
        "calendar_selected": CALENDAR, "products": list(PRODUCTS), "cases": case_results,
        "exports": exports, "summary": summary,
        "imports": {
            "aidata": str(Path(inspect.getfile(display_module)).resolve()),
            "TIS_U2NodeBehavior": str(Path(inspect.getfile(node_module)).resolve()),
            "TIS_U2ThinNode": str(Path(inspect.getfile(thin_module)).resolve()),
            "worker_schema": str(Path(inspect.getfile(worker_schema)).resolve()),
            "uplot": str(Path(inspect.getfile(uplot_module)).resolve()),
        },
        "versions": {
            "aidata_branch": git_value(args.aidata_repo, "branch", "--show-current"),
            "aidata_head": git_value(args.aidata_repo, "rev-parse", "HEAD"),
            "uplot_head": git_value(args.uplot_repo, "rev-parse", "HEAD"),
            "uplot_status": git_value(args.uplot_repo, "status", "--short"),
        },
        "safety": {
            "formal_recomputed": False, "complete_three_source_identity_preserved": True,
            "protected_source_modified": False, "business_interpretation": False,
        },
    }
    write_json(root / "evidence" / "CROSSK_READ_MANIFEST.json", manifest)
    print(json.dumps({"result": "PASS", "cases": list(case_results)}, ensure_ascii=False), flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
