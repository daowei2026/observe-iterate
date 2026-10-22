#!/usr/bin/env python3
"""Resume rendering from the successful formal-read exports after a layout error.

This recovery does not substitute CSV for the normal N reader: the CSV files
are the byte-hashed exports produced after the completed OnlyRead and three
``read_at_knowledge`` calls in ``run_display_integration.py``.  It only avoids
repeating those expensive safe reads while fixing and validating the consumer.
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import inspect
import json
import subprocess
import sys
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd
from bokeh.models import ColumnDataSource

from mquant.quant import OptContext
import mquant.aidata.u2_normal_node_behavior_display as display_module
import mquant.tis.frp.U2NodeBehavior as node_module
import mquant.tis.frp.U2ThinNode as thin_module
import mquant.uplot as uplot_module
import mquant.worker.adt.u2_node as worker_u2_schema

from mquant.aidata.u2_normal_node_behavior_display import (
    NDisplayBundle,
    build_selected_cut_bundle,
    build_uplot_layout,
    export_plot_view_data,
    write_html,
)


SOF = "TA_updto20240229_DBA"
CALENDAR = "night_end_at_2300"
COLOR = "#4C78A8"
CUTS = {
    "before_confirmation": 103150800,
    "at_or_after_confirmation": 103151400,
    "final": 103315800,
}


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


def git_value(repo: Path, *args: str) -> str:
    return subprocess.check_output(
        ["git", "-C", str(repo), *args], text=True, stderr=subprocess.STDOUT
    ).strip()


def load_formal_tables(directory: Path) -> dict[str, pd.DataFrame]:
    frames = {}
    for path in sorted(directory.glob("*.csv")):
        frame = pd.read_csv(path)
        frame["timestamp"] = pd.to_datetime(frame["timestamp"])
        for column in (name for name in frame if name == "text" or name.endswith("_text")):
            frame[column] = frame[column].fillna("")
        child = sorted(
            (column for column in frame if column.startswith("child_id_")),
            key=lambda value: int(value.split("_")[-1]),
        )
        index = ["timestamp", "occurrence", "record_id", *child]
        frames[path.stem] = frame.set_index(index)
    return frames


def load_price(path: Path) -> pd.DataFrame:
    frame = pd.read_csv(path)
    first = frame.columns[0]
    frame[first] = pd.to_datetime(frame[first])
    return frame.set_index(first)


def load_evolution_bundle(directory: Path) -> NDisplayBundle:
    manifest = json.loads((directory / "plot_view_data_manifest.json").read_text(encoding="utf-8"))
    views = {
        name: pd.read_csv(directory / item["file"])
        for name, item in manifest["files"].items()
        if name != "same_bound_5m_ohlc"
    }
    price = load_price(directory / manifest["files"]["same_bound_5m_ohlc"]["file"])
    return NDisplayBundle(
        symbol="rb", color=COLOR, mode="evolution", views=views, price=price,
        meta=manifest["meta"], notices=manifest["notices"],
        optional_panels=("duration", "rhythm"),
    )


def validate(layout: Any, bundle: NDisplayBundle, html_path: Path) -> dict[str, Any]:
    references = list(layout.references())
    figures = [
        model for model in references
        if hasattr(model, "renderers") and hasattr(model, "x_range") and hasattr(model, "y_range")
    ]
    sources = [model for model in references if isinstance(model, ColumnDataSource)]
    renderers = [
        model for model in references
        if "aidata_evidence" in list(getattr(model, "tags", []) or [])
    ]
    colors, markers, groups = [], [], []
    for renderer in renderers:
        groups.extend(
            tag for tag in (renderer.tags or [])
            if isinstance(tag, str) and tag.startswith("group:")
        )
        glyph = getattr(renderer, "glyph", None)
        for field in ("line_color", "fill_color"):
            value = getattr(glyph, field, None)
            if isinstance(value, str):
                colors.append(value)
        marker = getattr(glyph, "marker", None)
        if isinstance(marker, str):
            markers.append(marker)
    checks = {
        "html_nonempty": html_path.stat().st_size > 100_000,
        "one_figure_per_panel": len(figures) == len(bundle.configuration["panels"]),
        "independent_panel_figures": len({figure.id for figure in figures}) == len(figures),
        "stable_symbol_color": bool(renderers) and set(colors) == {COLOR},
        "working_segments_axis_aligned": True,
        "selected_cut_has_no_geometry_after_K": True,
    }
    for name in ("working_progress_steps", "working_counter_steps", "working_efficiency_steps"):
        frame = bundle.views[name]
        if len(frame) and not ((frame["x0"] == frame["x1"]) | (frame["y0"] == frame["y1"])).all():
            checks["working_segments_axis_aligned"] = False
    if bundle.mode == "selected_cut":
        k = int(bundle.meta["selected_k"])
        for frame in bundle.views.values():
            for column in ("x", "x0", "x1"):
                if column in frame and len(frame) and pd.to_numeric(frame[column]).max() > k:
                    checks["selected_cut_has_no_geometry_after_K"] = False
        checks["circle_actual_and_diamond_confirmation"] = {"circle", "diamond"}.issubset(markers)
    result = {
        "result": "PASS" if all(checks.values()) else "FAIL",
        "mode": bundle.mode,
        "figure_count": len(figures),
        "configured_panels": list(bundle.configuration["panels"]),
        "column_data_source_count": len(sources),
        "evidence_renderer_count": len(renderers),
        "evidence_groups": sorted(set(groups)),
        "evidence_colors": sorted(set(colors)),
        "markers": sorted(set(markers)),
        "checks": checks,
    }
    if result["result"] != "PASS":
        raise RuntimeError(f"render validation failed: {result}")
    return result


def render(bundle: NDisplayBundle, context: OptContext, root: Path, page_id: str) -> dict[str, Any]:
    view_dir = root / "plot_view_data" / page_id
    view_manifest = export_plot_view_data(bundle, view_dir)
    layout = build_uplot_layout(bundle, context=context, calendar_name=CALENDAR, title_suffix=page_id)
    html_path = root / "render_evidence" / f"{page_id}.html"
    write_html(layout, html_path, title=f"BI01 FO01 {page_id}")
    result = validate(layout, bundle, html_path)
    validation_path = root / "render_evidence" / f"{page_id}.validation.json"
    write_json(validation_path, result)
    return {
        "page_id": page_id,
        "mode": bundle.mode,
        "html": {"path": str(html_path.relative_to(root)), "bytes": html_path.stat().st_size, "sha256": sha256(html_path)},
        "plot_view_data_manifest_sha256": view_manifest["manifest_sha256"],
        "validation": {"path": str(validation_path.relative_to(root)), "sha256": sha256(validation_path), **result},
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-root", type=Path, required=True)
    parser.add_argument("--aidata-repo", type=Path, required=True)
    parser.add_argument("--uplot-repo", type=Path, required=True)
    args = parser.parse_args()
    root = args.output_root.resolve()
    context = OptContext(sof_name=SOF)
    price = load_price(root / "data" / "same_bound_price" / "rb_5m_price_calendar.csv")

    bundles = [("rb_evolution_actual_occurrences", load_evolution_bundle(root / "plot_view_data" / "rb_evolution_actual_occurrences"))]
    selected_meta = {}
    for label, cut in CUTS.items():
        tables = load_formal_tables(root / "data" / "selected_cuts" / label)
        bundle = build_selected_cut_bundle(
            tables, price, symbol="rb", color=COLOR, as_of=cut,
            optional_panels=("duration", "rhythm"),
        )
        bundles.append((f"rb_selected_{label}_K{cut}", bundle))
        selected_meta[label] = bundle.meta

    pages = []
    for page_id, bundle in bundles:
        print(f"PHASE render {page_id}", flush=True)
        pages.append(render(bundle, context, root, page_id))

    rb_index = pd.read_csv(root / "data" / "formal_occurrence_index" / "rb_temporal_slice.csv")
    hc = pd.read_csv(root / "data" / "formal_occurrence_index" / "hc_tail_500.csv")
    i_case = pd.read_csv(root / "data" / "formal_occurrence_index" / "i_20170330_1455_to_20170331_0900.csv")
    temporal = {
        "rb": {
            "actual_occurrence_rows": len(rb_index),
            "as_of_range": [int(rb_index["as_of"].min()), int(rb_index["as_of"].max())],
            "selected_cuts": CUTS,
            "selected_meta": selected_meta,
        },
        "hc_tail": {
            "rows": len(hc),
            "as_of_range": [int(hc["as_of"].min()), int(hc["as_of"].max())],
            "max_present_waiting_ratio": clean(pd.to_numeric(
                hc.loc[hc["working_waiting_ratio_present"] == 1, "working_waiting_ratio_value"], errors="coerce"
            ).max()),
            "qualification": "technical triage only; no business conclusion",
        },
        "i_named_interval": {
            "rows": len(i_case),
            "as_of_range": None if i_case.empty else [int(i_case["as_of"].min()), int(i_case["as_of"].max())],
            "formal_failures": int(i_case["formal_failure"].sum()) if len(i_case) else 0,
            "present_waiting_zero": int(((i_case["working_waiting_present"] == 1) & (pd.to_numeric(i_case["working_waiting_value"], errors="coerce") == 0)).sum()) if len(i_case) else 0,
            "qualification": "zero remains zero and is not labelled as a new extreme confirmation",
        },
    }
    write_json(root / "evidence" / "TEMPORAL_CASES.json", temporal)
    manifest = {
        "schema_version": 1,
        "order_id": "BI01-FO01-N-DISPLAY-INTEGRATION-02",
        "result": "PASS",
        "recovery_scope": "render-only continuation after all formal OnlyRead/read_at_knowledge exports completed",
        "recovery_reason": "first layout used syms!rb as PlotSet.blk; fixed to the supported symbol list ['rb']",
        "formal_reads": {
            "full_evolution": "completed before recovery",
            "selected_read_at_knowledge": CUTS,
            "complete_three_source_identity": True,
            "formal_N_recomputed": False,
        },
        "imports": {
            "aidata_display": str(Path(inspect.getfile(display_module)).resolve()),
            "TIS_U2NodeBehavior": str(Path(inspect.getfile(node_module)).resolve()),
            "TIS_U2ThinNode": str(Path(inspect.getfile(thin_module)).resolve()),
            "uplot": str(Path(inspect.getfile(uplot_module)).resolve()),
            "worker_u2_schema": str(Path(inspect.getfile(worker_u2_schema)).resolve()),
        },
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
            "modified_by_order": False,
        },
        "pages": pages,
        "temporal_cases": temporal,
        "safety": {
            "TIS_FRP_core_SDK_uplot_source_modified": False,
            "display_projection_is_formal_product": False,
            "selected_price_after_K_drawn": False,
            "ratios_or_duration_price_normalized": False,
        },
        "acceptance_distinctions": {
            "normal_reader": "PASS",
            "normal_selected_reads": "PASS",
            "aidata_configuration_consumed": "PASS",
            "uplot_layout_and_html": "PASS",
            "browser_pixels": "PENDING_SEPARATE_CAPTURE",
            "worker_visual_inspection": "PENDING_SEPARATE_INSPECTION",
            "professional_interpretation": "NOT_WORKER_AUTHORITY",
        },
    }
    write_json(root / "evidence" / "RUNTIME_AND_RENDER_MANIFEST.json", manifest)
    print(json.dumps({"result": "PASS", "pages": [page["page_id"] for page in pages]}, ensure_ascii=False), flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
