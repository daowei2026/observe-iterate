#!/usr/bin/env python3
"""Run the BI-01 normal-N display integration against saved formal results.

The script deliberately uses the complete R30 product identity and explicit
``CalType.OnlyRead``.  It consumes the aidata display adapter, resolves actual
occurrences around the requested rb boundaries, performs normal as-known reads,
renders real uplot/Bokeh pages, and exports the exact display projections.
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import inspect
import json
import resource
import shutil
import subprocess
import sys
import time
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd
from bokeh.models import ColumnDataSource

from m3sof.settings.json import eval2
from m3tt import CurrTradeSet
from mquant.frame import CalType, CurrCalendar, CurrIndustry
from mquant.quant import OptContext
from mquant.tis.calendar.base import blk_suitable_calendars
from mquant.tis.frp.U2Mainline import U2MainlineKLineInput
from mquant.tis.frp.U2NodeBehavior import U2NormalNodeBehaviorFrp
from mquant.tis.lib3 import CurrSymbol
import mquant.aidata.u2_normal_node_behavior_display as display_module
import mquant.worker.adt.u2_node as worker_u2_schema
import mquant.tis.frp.U2Mainline as mainline_module
import mquant.tis.frp.U2NodeBehavior as node_module
import mquant.tis.frp.U2ThinNode as thin_module
import mquant.uplot as uplot_module

from mquant.aidata.u2_normal_node_behavior_display import (
    build_evolution_bundle,
    build_selected_cut_bundle,
    build_uplot_layout,
    export_plot_view_data,
    formal_occurrence_indexes,
    read_formal_evolution_frames,
    read_formal_selected_cut,
    write_html,
)


SOF = "TA_updto20240229_DBA"
CONTEXT = "blk@steel"
CALENDAR = "night_end_at_2300"
EXPECTED_PRODUCT_DIR = Path(
    "/m3varK/BaseData/futures/TA_updto20240229_DBA/fao/prod/"
    "U2NormalNodeBehaviorFrp/9/0/d/3/7/a/4/"
    "fb2007d71be1e620801457424d6dea8b4/func"
)
RB_EXPECTED_FINAL = 103315800
RB_ACTUAL_END = 103059000
RB_CONFIRMATION = 103151400
SYMBOL_COLORS = {"rb": "#4C78A8", "hc": "#F58518", "i": "#54A24B"}


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
    if value is pd.NA or value is pd.NaT:
        return None
    if isinstance(value, float) and not np.isfinite(value):
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


def calendar_name(value: Any) -> str:
    for field in ("name", "calendar", "life"):
        candidate = getattr(value, field, None)
        if candidate:
            return str(candidate)
    return str(value)


def git_value(repo: Path, *args: str) -> str:
    return subprocess.check_output(
        ["git", "-C", str(repo), *args], text=True, stderr=subprocess.STDOUT
    ).strip()


def resolve_calendar(context: OptContext) -> tuple[Any, list[str]]:
    candidates = tuple(blk_suitable_calendars(context.sof, CONTEXT))
    matches = [value for value in candidates if calendar_name(value) == CALENDAR]
    if len(matches) != 1:
        raise RuntimeError(
            f"expected exactly one {CALENDAR!r}; got {[calendar_name(v) for v in candidates]!r}"
        )
    return matches[0], [calendar_name(value) for value in candidates]


def actual_neighbors(values: pd.Series, target: int) -> dict[str, int]:
    unique = np.unique(values.astype(np.int64).to_numpy())
    before = unique[unique < target]
    after = unique[unique >= target]
    if not len(before) or not len(after):
        raise RuntimeError(f"no actual occurrence neighbors around {target}")
    return {"target": int(target), "before": int(before[-1]), "at_or_after": int(after[0])}


def export_frame(frame: pd.DataFrame, path: Path) -> dict[str, Any]:
    path.parent.mkdir(parents=True, exist_ok=True)
    public = frame.reset_index()
    public.to_csv(path, index=False)
    return {
        "path": str(path),
        "rows": int(len(public)),
        "columns": list(public.columns),
        "sha256": sha256(path),
    }


def read_price(
    *, context: OptContext, calendar: Any, symbol: str, start_uti: int, end_uti: int
) -> tuple[pd.DataFrame, dict[str, Any]]:
    started = time.monotonic()
    with CurrTradeSet(context.sof), CurrIndustry(CONTEXT), CurrCalendar(calendar), CurrSymbol(symbol):
        feature = U2MainlineKLineInput(
            source=eval2("MapKLineOpenData(freq='5m')"),
            calendar_grid=eval2("ResampleCalendarTsa(resample_len=600)"),
        )
        full = feature.rerun(CalType.OnlyRead).to_df()
        product_dir = str(feature.full_dir)
    required = [
        "open_uti", "open", "high", "low", "close", "volume", "openInt",
        "calendar_position", "calendar_time",
    ]
    missing = sorted(set(required).difference(full.columns))
    if missing:
        raise RuntimeError(f"normal U2Mainline result lacks fields: {missing}")
    selected = full.loc[
        (full["open_uti"].astype(np.int64) >= start_uti)
        & (full["open_uti"].astype(np.int64) <= end_uti),
        required,
    ].copy()
    if len(selected) < 2:
        raise RuntimeError(f"insufficient same-bound {symbol} price rows")
    return selected, {
        "entry": "U2MainlineKLineInput.rerun(CalType.OnlyRead).to_df",
        "product_dir": product_dir,
        "source_life": f"/m3varI/var/L1_data/tick/map_kline_data/5m/{symbol}_{CALENDAR}",
        "source_revision": SOF,
        "requested_range": [start_uti, end_uti],
        "actual_range": [int(selected["open_uti"].iloc[0]), int(selected["open_uti"].iloc[-1])],
        "rows": int(len(selected)),
        "first_bar_time": str(selected.index[0]),
        "last_bar_time": str(selected.index[-1]),
        "close_missing": int(selected["close"].isna().sum()),
        "elapsed_seconds": time.monotonic() - started,
    }


def selected_price_bounds(frames_by_label: dict[str, dict[str, pd.DataFrame]], fallback: int) -> int:
    candidates = [fallback]
    for frames in frames_by_label.values():
        for table in ("previous_members", "recent_members"):
            if table not in frames:
                continue
            body = frames[table].reset_index()
            for column in ("start", "end", "confirmation"):
                candidates.extend(int(value) for value in body[column].dropna() if int(value) > 0)
        bases = frames.get("working_bases")
        if bases is not None and len(bases):
            candidates.extend(
                int(value) for value in bases["start_value"].dropna()
                if int(value) > 0
            )
    return min(candidates)


def render_validation(layout: Any, bundle: Any, html_path: Path) -> dict[str, Any]:
    references = list(layout.references())
    figures = [
        model for model in references
        if hasattr(model, "renderers") and hasattr(model, "x_range") and hasattr(model, "y_range")
    ]
    sources = [model for model in references if isinstance(model, ColumnDataSource)]
    evidence_renderers = [
        model for model in references
        if "aidata_evidence" in list(getattr(model, "tags", []) or [])
    ]
    group_tags = sorted({
        tag for renderer in evidence_renderers for tag in (renderer.tags or [])
        if isinstance(tag, str) and tag.startswith("group:")
    })
    configured_panels = list(bundle.configuration["panels"])
    color_values = []
    marker_values = []
    for renderer in evidence_renderers:
        glyph = getattr(renderer, "glyph", None)
        for field in ("line_color", "fill_color"):
            value = getattr(glyph, field, None)
            if isinstance(value, str):
                color_values.append(value)
        marker = getattr(glyph, "marker", None)
        if isinstance(marker, str):
            marker_values.append(marker)
    geometry_checks = {
        "selected_cut_has_no_view_x_after_k": True,
        "working_segments_axis_aligned": True,
    }
    if bundle.mode == "selected_cut":
        k = int(bundle.meta["selected_k"])
        for frame in bundle.views.values():
            for column in ("x", "x0", "x1"):
                if column in frame and len(frame) and pd.to_numeric(frame[column]).max() > k:
                    geometry_checks["selected_cut_has_no_view_x_after_k"] = False
    for name in ("working_progress_steps", "working_counter_steps", "working_efficiency_steps"):
        frame = bundle.views[name]
        if len(frame) and not ((frame["x0"] == frame["x1"]) | (frame["y0"] == frame["y1"])).all():
            geometry_checks["working_segments_axis_aligned"] = False
    checks = {
        "html_nonempty": html_path.stat().st_size > 100_000,
        "one_figure_per_configured_panel": len(figures) == len(configured_panels),
        "all_evidence_colors_equal_symbol_palette": bool(evidence_renderers) and set(color_values) == {bundle.color},
        "independent_figure_ids": len({figure.id for figure in figures}) == len(figures),
        **geometry_checks,
    }
    if bundle.mode == "selected_cut":
        checks["actual_circle_and_confirmation_diamond_configured"] = {"circle", "diamond"}.issubset(marker_values)
    return {
        "result": "PASS" if all(checks.values()) else "FAIL",
        "mode": bundle.mode,
        "configured_panels": configured_panels,
        "figure_count": len(figures),
        "column_data_source_count": len(sources),
        "evidence_renderer_count": len(evidence_renderers),
        "evidence_group_tags": group_tags,
        "evidence_colors": sorted(set(color_values)),
        "evidence_markers": sorted(set(marker_values)),
        "checks": checks,
    }


def render_bundle(
    *, bundle: Any, context: OptContext, output_root: Path, page_id: str, title: str
) -> dict[str, Any]:
    plot_dir = output_root / "plot_view_data" / page_id
    view_manifest = export_plot_view_data(bundle, plot_dir)
    layout = build_uplot_layout(
        bundle, context=context, calendar_name=CALENDAR, title_suffix=title
    )
    html_path = output_root / "render_evidence" / f"{page_id}.html"
    write_html(layout, html_path, title=f"BI01 FO01 {page_id}")
    validation = render_validation(layout, bundle, html_path)
    validation_path = output_root / "render_evidence" / f"{page_id}.validation.json"
    write_json(validation_path, validation)
    if validation["result"] != "PASS":
        raise RuntimeError(f"render validation failed for {page_id}: {validation['checks']}")
    return {
        "page_id": page_id,
        "mode": bundle.mode,
        "html": {
            "path": str(html_path.relative_to(output_root)),
            "bytes": html_path.stat().st_size,
            "sha256": sha256(html_path),
        },
        "plot_view_data_manifest": view_manifest,
        "validation": {
            "path": str(validation_path.relative_to(output_root)),
            "sha256": sha256(validation_path),
            **validation,
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--configuration", type=Path, required=True)
    parser.add_argument("--professional-config", type=Path, required=True)
    parser.add_argument("--output-root", type=Path, required=True)
    parser.add_argument("--aidata-repo", type=Path, required=True)
    parser.add_argument("--uplot-repo", type=Path, required=True)
    args = parser.parse_args()

    started_at = dt.datetime.now(dt.timezone.utc)
    started = time.monotonic()
    output_root = args.output_root.resolve()
    output_root.mkdir(parents=True, exist_ok=True)
    (output_root / "inputs").mkdir(exist_ok=True)
    shutil.copyfile(args.configuration, output_root / "inputs" / "ACTUAL_RUN_CONFIGURATION.json")
    shutil.copyfile(args.professional_config, output_root / "inputs" / "professional_u2_normal_node_behavior.py")
    actual = json.loads(args.configuration.read_text(encoding="utf-8"))
    sources = actual["配置"]["source"]["sources"]
    configured_objects = [source["source"]["source"]["scope"]["object"] for source in sources]
    if len(configured_objects) != 3 or set(configured_objects) != {"rb", "hc", "i"}:
        raise RuntimeError(f"complete configured objects changed: {configured_objects!r}")

    context = OptContext(sof_name=SOF)
    calendar, calendar_candidates = resolve_calendar(context)
    print("PHASE formal-only-read", flush=True)
    with CurrTradeSet(context.sof), CurrIndustry(CONTEXT), CurrCalendar(calendar):
        feature = U2NormalNodeBehaviorFrp.from_sources(sources, compact_history=True)
        product_dir = Path(str(feature.full_dir))
        if product_dir != EXPECTED_PRODUCT_DIR:
            raise RuntimeError(f"unexpected formal product directory: {product_dir}")
        formal_started = time.monotonic()
        frames = read_formal_evolution_frames(feature)
        formal_elapsed = time.monotonic() - formal_started
        frame_shapes = {name: list(frame.shape) for name, frame in frames.items()}

        print("PHASE formal-occurrence-indexes", flush=True)
        indexes = formal_occurrence_indexes(frames, symbols=configured_objects)
        rb = indexes["rb"].sort_values(["as_of", "occurrence", "record_id"], kind="stable")
        end_neighbors = actual_neighbors(rb["as_of"], RB_ACTUAL_END)
        confirmation_neighbors = actual_neighbors(rb["as_of"], RB_CONFIRMATION)
        if RB_EXPECTED_FINAL not in set(rb["as_of"].astype(int)):
            raise RuntimeError("expected final rb occurrence 103315800 is not in the fresh formal index")

        unique_as_of = np.unique(rb["as_of"].astype(np.int64).to_numpy())
        before_end_pos = int(np.searchsorted(unique_as_of, end_neighbors["before"]))
        evolution_start = int(unique_as_of[max(0, before_end_pos - 3)])
        selection_plan = {
            "before_confirmation": confirmation_neighbors["before"],
            "at_or_after_confirmation": confirmation_neighbors["at_or_after"],
            "final": RB_EXPECTED_FINAL,
        }
        if len(set(selection_plan.values())) != len(selection_plan):
            raise RuntimeError(f"selected normal reads unexpectedly collapse: {selection_plan}")
        node_lives = sorted(set(rb["node_life"].astype(str)))
        if len(node_lives) != 1:
            raise RuntimeError(f"rb did not resolve one node Life: {node_lives!r}")
        node_life = node_lives[0]

        print("PHASE selected-normal-reads", flush=True)
        selected_frames: dict[str, dict[str, pd.DataFrame]] = {}
        selected_read_elapsed: dict[str, float] = {}
        for label, cut in selection_plan.items():
            cut_started = time.monotonic()
            selected_frames[label] = read_formal_selected_cut(
                feature, node_life=node_life, as_of=int(cut)
            )
            selected_read_elapsed[label] = time.monotonic() - cut_started
            print(f"PHASE selected-normal-read-complete label={label} K={cut}", flush=True)

    print("PHASE export-formal-selection", flush=True)
    formal_index_dir = output_root / "data" / "formal_occurrence_index"
    temporal_slice = rb.loc[
        rb["as_of"].between(evolution_start, RB_EXPECTED_FINAL, inclusive="both")
    ].copy()
    rb_index_export = export_frame(temporal_slice, formal_index_dir / "rb_temporal_slice.csv")
    hc_tail = indexes["hc"].sort_values("as_of", kind="stable").tail(500).copy()
    hc_export = export_frame(hc_tail, formal_index_dir / "hc_tail_500.csv")
    i_index = indexes["i"].copy()
    i_ts = pd.to_datetime(i_index["timestamp"])
    i_recovery = i_index.loc[
        (i_ts >= pd.Timestamp("2017-03-30 14:55"))
        & (i_ts <= pd.Timestamp("2017-03-31 09:00"))
    ].copy()
    i_export = export_frame(i_recovery, formal_index_dir / "i_20170330_1455_to_20170331_0900.csv")

    selected_exports: dict[str, Any] = {}
    for label, tables in selected_frames.items():
        selected_exports[label] = {}
        table_dir = output_root / "data" / "selected_cuts" / label
        for name, frame in tables.items():
            selected_exports[label][name] = export_frame(frame, table_dir / f"{name}.csv")

    price_start = selected_price_bounds(selected_frames, evolution_start)
    print(f"PHASE price-only-read range={price_start}:{RB_EXPECTED_FINAL}", flush=True)
    price, price_runtime = read_price(
        context=context, calendar=calendar, symbol="rb",
        start_uti=price_start, end_uti=RB_EXPECTED_FINAL,
    )
    price_path = output_root / "data" / "same_bound_price" / "rb_5m_price_calendar.csv"
    price_export = export_frame(price, price_path)

    print("PHASE project-and-render", flush=True)
    pages = []
    evolution = build_evolution_bundle(
        frames, price, symbol="rb", color=SYMBOL_COLORS["rb"],
        start_uti=evolution_start, end_uti=RB_EXPECTED_FINAL,
        optional_panels=("duration", "rhythm"),
    )
    pages.append(render_bundle(
        bundle=evolution, context=context, output_root=output_root,
        page_id="rb_evolution_actual_occurrences",
        title=f"真实发生 {evolution_start}—{RB_EXPECTED_FINAL}",
    ))
    for label, cut in selection_plan.items():
        bundle = build_selected_cut_bundle(
            selected_frames[label], price, symbol="rb", color=SYMBOL_COLORS["rb"],
            as_of=int(cut), optional_panels=("duration", "rhythm"),
        )
        pages.append(render_bundle(
            bundle=bundle, context=context, output_root=output_root,
            page_id=f"rb_selected_{label}_K{cut}",
            title=f"知识切点K={cut}｜{label}",
        ))

    technical_cases = {
        "rb_boundaries": {
            "actual_end": end_neighbors,
            "confirmation": confirmation_neighbors,
            "final": RB_EXPECTED_FINAL,
            "evolution_start": evolution_start,
            "selected_normal_reads": selection_plan,
            "rows_in_exported_temporal_slice": len(temporal_slice),
        },
        "hc_tail": {
            "scope": "latest 500 actual formal occurrences; technical triage, no business conclusion",
            "rows": len(hc_tail),
            "as_of_range": [int(hc_tail["as_of"].min()), int(hc_tail["as_of"].max())],
            "max_present_waiting_ratio": clean(pd.to_numeric(
                hc_tail.loc[hc_tail["working_waiting_ratio_present"] == 1, "working_waiting_ratio_value"],
                errors="coerce",
            ).max()),
            "distinct_working_addresses": int(hc_tail["working"].nunique()),
        },
        "i_missing_data_neighborhood": {
            "scope": "actual formal occurrences whose saved timestamp falls in the named interval",
            "rows": len(i_recovery),
            "as_of_range": None if i_recovery.empty else [int(i_recovery["as_of"].min()), int(i_recovery["as_of"].max())],
            "formal_failures": int(i_recovery["formal_failure"].sum()) if len(i_recovery) else 0,
            "working_waiting_present_zero": int((
                (i_recovery["working_waiting_present"] == 1)
                & (pd.to_numeric(i_recovery["working_waiting_value"], errors="coerce") == 0)
            ).sum()) if len(i_recovery) else 0,
            "qualification": "exported for Pro interpretation; zero is not relabelled as an extreme confirmation",
        },
    }
    write_json(output_root / "evidence" / "TEMPORAL_CASES.json", technical_cases)

    imported_paths = {
        "aidata_display": str(Path(inspect.getfile(display_module)).resolve()),
        "worker_u2_schema": str(Path(inspect.getfile(worker_u2_schema)).resolve()),
        "TIS_U2NodeBehavior": str(Path(inspect.getfile(node_module)).resolve()),
        "TIS_U2ThinNode": str(Path(inspect.getfile(thin_module)).resolve()),
        "TIS_U2Mainline": str(Path(inspect.getfile(mainline_module)).resolve()),
        "uplot": str(Path(inspect.getfile(uplot_module)).resolve()),
    }
    manifest = {
        "schema_version": 1,
        "order_id": "BI01-FO01-N-DISPLAY-INTEGRATION-02",
        "result": "PASS",
        "started_at": started_at.isoformat(),
        "finished_at": dt.datetime.now(dt.timezone.utc).isoformat(),
        "elapsed_seconds": time.monotonic() - started,
        "max_rss_kib": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        "python": sys.executable,
        "input": {
            "configuration": {"path": str(args.configuration.resolve()), "sha256": sha256(args.configuration)},
            "professional_config": {"path": str(args.professional_config.resolve()), "sha256": sha256(args.professional_config)},
            "complete_source_objects": configured_objects,
            "compact_history": True,
            "sof": SOF,
            "context": CONTEXT,
            "calendar_candidates": calendar_candidates,
            "calendar_selected": CALENDAR,
            "formal_product_dir": str(product_dir),
        },
        "runtime": {
            "imports": imported_paths,
            "aidata": {
                "repo": str(args.aidata_repo.resolve()),
                "branch": git_value(args.aidata_repo, "branch", "--show-current"),
                "head_before_commit": git_value(args.aidata_repo, "rev-parse", "HEAD"),
                "status_before_commit": git_value(args.aidata_repo, "status", "--short"),
            },
            "uplot": {
                "repo": str(args.uplot_repo.resolve()),
                "branch": git_value(args.uplot_repo, "branch", "--show-current"),
                "head": git_value(args.uplot_repo, "rev-parse", "HEAD"),
                "status": git_value(args.uplot_repo, "status", "--short"),
                "qualification": "read-only actual import; Owner reference 0a4fcd is recorded separately, not substituted",
            },
        },
        "formal_read": {
            "entry": "U2NormalNodeBehaviorFrp.rerun(CalType.OnlyRead) + to_dfs(18 required named tables)",
            "elapsed_seconds": formal_elapsed,
            "table_shapes": frame_shapes,
            "occurrence_index_rows": {symbol: len(index) for symbol, index in indexes.items()},
        },
        "selected_reads": {
            "entry": "U2NormalNodeBehaviorFrp.read_at_knowledge(explicit node Life, integer K, products=18) after OnlyRead",
            "node_life": node_life,
            "plan": selection_plan,
            "elapsed_seconds": selected_read_elapsed,
            "exports": selected_exports,
        },
        "price_read": {**price_runtime, "export": price_export},
        "formal_index_exports": {
            "rb": rb_index_export, "hc": hc_export, "i": i_export,
        },
        "pages": pages,
        "temporal_cases": technical_cases,
        "safety": {
            "formal_mode": "OnlyRead",
            "normalization": None,
            "complete_three_source_identity_preserved": True,
            "formal_N_recomputed": False,
            "TIS_FRP_core_SDK_uplot_source_modified": False,
            "display_projection_is_formal_product": False,
            "price_after_selected_K_drawn": False,
        },
        "acceptance_distinctions": {
            "normal_reader": "PASS",
            "aidata_configuration_consumed": "PASS",
            "uplot_layout_and_html": "PASS",
            "browser_pixels": "PENDING_SEPARATE_CAPTURE",
            "worker_visual_inspection": "PENDING_SEPARATE_INSPECTION",
            "professional_interpretation": "NOT_WORKER_AUTHORITY",
        },
    }
    write_json(output_root / "evidence" / "RUNTIME_AND_RENDER_MANIFEST.json", manifest)
    print(json.dumps({
        "result": "PASS", "output_root": str(output_root),
        "pages": [page["page_id"] for page in pages],
        "elapsed_seconds": manifest["elapsed_seconds"],
        "max_rss_kib": manifest["max_rss_kib"],
    }, ensure_ascii=False), flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
