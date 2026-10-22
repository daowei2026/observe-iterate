#!/usr/bin/env python3
"""复用 W02 正式导出，按 aidata v0.2.1 真实重绘可读页面。"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import inspect
import json
import subprocess
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd
from bokeh.models import ColumnDataSource, FixedTicker, LabelSet, Legend, Range1d
from mquant.quant import OptContext
import mquant.aidata.u2_normal_node_behavior_display as display_module
from mquant.aidata.feature_configs.u2_normal_node_behavior import CONFIG_VERSION
from mquant.aidata.u2_normal_node_behavior_display import (
    NDisplayBundle,
    U2NormalNodeBehaviorDisplayFeature,
    build_selected_cut_bundle,
    build_uplot_layout,
    export_plot_view_data,
    write_html,
)
import mquant.tis.frp.U2NodeBehavior as node_module
import mquant.tis.frp.U2ThinNode as thin_module
import mquant.uplot as uplot_module
import mquant.worker.adt.u2_node as worker_schema


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
        frames[path.stem] = frame.set_index(["timestamp", "occurrence", "record_id", *child])
    return frames


def load_price(path: Path) -> pd.DataFrame:
    frame = pd.read_csv(path)
    first = frame.columns[0]
    frame[first] = pd.to_datetime(frame[first])
    return frame.set_index(first)


def load_reused_evolution(
    w02: Path,
    selected_final: NDisplayBundle,
) -> NDisplayBundle:
    directory = w02 / "plot_view_data/rb_evolution_actual_occurrences"
    manifest = json.loads((directory / "plot_view_data_manifest.json").read_text(encoding="utf-8"))
    views = {
        name: pd.read_csv(directory / item["file"])
        for name, item in manifest["files"].items()
        if name != "same_bound_5m_ohlc"
    }
    full_price = load_price(directory / manifest["files"]["same_bound_5m_ohlc"]["file"])
    occurrence_index = pd.read_csv(w02 / "data/formal_occurrence_index/rb_temporal_slice.csv")
    start = int(occurrence_index["as_of"].min())
    end = int(occurrence_index["as_of"].max())
    price = full_price[full_price["open_uti"].between(start, end, inclusive="both")].copy()
    for name, frame in list(views.items()):
        if {"x0", "x1"}.issubset(frame.columns):
            clipped = frame[(frame["x0"] <= end) & (frame["x1"] >= start)].copy()
            if len(clipped):
                clipped["x0"] = clipped["x0"].clip(lower=start)
                clipped["x1"] = clipped["x1"].clip(upper=end)
            views[name] = clipped
        elif "x" in frame:
            views[name] = frame[frame["x"].between(start, end, inclusive="both")].copy()

    ordered = occurrence_index.sort_values(["as_of", "occurrence", "record_id"], kind="stable")
    first = ordered.iloc[0]
    transitions = []
    for left, right in zip(ordered.to_dict("records"), ordered.iloc[1:].to_dict("records")):
        if int(left["working_direction"]) != int(right["working_direction"]):
            known_life = (
                selected_final.meta["working_life"]
                if int(right["as_of"]) == CUTS["at_or_after_confirmation"]
                else "not-read-at-this-boundary"
            )
            transitions.append({
                "as_of": int(right["as_of"]), "reason": "方向变化（连续性在此断开）",
                "working_life": known_life, "working_life_short": known_life[:8],
                "start": None, "direction": "up" if int(right["working_direction"]) == 0 else "down",
                "previous_address": int(left["working"]), "address": int(right["working"]),
                "source_exact": str(right["source_exact"]),
            })
    meta = dict(manifest["meta"])
    meta.update({
        "evolution_display_range": [start, end],
        "loaded_price_context_range": [
            int(full_price["open_uti"].min()), int(full_price["open_uti"].max())
        ],
        "working_storage_updates": int(ordered["working"].ne(ordered["working"].shift()).sum()),
        "working_process_transitions": transitions,
        "working_process_transition_count": len(transitions),
        "working_continuity_scope": (
            "reused W02 projection preserves gaps at unverified storage boundaries; the new consumer "
            "connects only when fresh bases prove same Life/start/direction"
        ),
        "source_exact_first": str(first["source_exact"]),
        "data_binding": int(first["binding_address"]),
        "working_life": selected_final.meta["working_life"],
        "working_start": selected_final.meta["working_start"],
        "rhythm_detail": selected_final.meta["rhythm_detail"],
        "price_rows": int(len(price)),
    })
    meta.pop("working_updates", None)
    optional_panels = ("rhythm",)
    meta["display_identity"] = {
        "symbol": "rb", "node_life": str(meta["node_life"]),
        "data_binding": int(meta["data_binding"]), "mode": "evolution",
        "selected_k_or_requested_range": {
            "requested_range": [int(value) for value in meta["requested_range"]],
            "display_range": [start, end],
        },
        "resolved_exact_or_occurrence_selection": {
            "first_exact": str(meta["source_exact_first"]),
            "last_exact": str(meta["source_exact_last"]),
            "formal_occurrences": int(meta["formal_occurrences"]),
        },
        "configuration_version": CONFIG_VERSION,
        "optional_panels": list(optional_panels),
    }
    return NDisplayBundle(
        symbol="rb", color=COLOR, mode="evolution", views=views, price=price,
        meta=meta, notices=manifest["notices"], optional_panels=optional_panels,
    )


def evidence_coordinate_max(layout: Any) -> float | None:
    values = []
    for renderer in layout.references():
        if "aidata_evidence" not in list(getattr(renderer, "tags", []) or []):
            continue
        source = getattr(renderer, "data_source", None)
        if source is None:
            continue
        for field in ("x", "x0", "x1"):
            if field in source.data and len(source.data[field]):
                values.extend(float(value) for value in source.data[field])
    return max(values) if values else None


def layout_models(root: Any):
    """Walk layout containers too; this Bokeh exposes grid rows as tuples."""
    yield root
    for child in getattr(root, "children", []) or []:
        model = child[0] if isinstance(child, tuple) else child
        yield from layout_models(model)


def validate_layout(layout: Any, bundle: NDisplayBundle, html_path: Path) -> dict[str, Any]:
    refs = list(layout.references())
    figures = [
        model for model in refs
        if hasattr(model, "renderers") and hasattr(model, "x_range")
        and getattr(getattr(model, "title", None), "text", None)
    ]
    labels = [model for model in refs if isinstance(model, LabelSet)
              and "n_display_value_label" in list(model.tags or [])]
    outside = [model for model in refs if isinstance(model, Legend)
               and "n_display_legend_outside_above" in list(model.tags or [])]
    grids = [model for model in layout_models(layout) if type(model).__name__ in {"GridBox", "GridPlot"}]
    panel_figs = {}
    for panel, spec in bundle.configuration["panels"].items():
        title = f"{bundle.symbol}｜{spec['title']}｜{spec['unit']}"
        found = [fig for fig in figures if fig.title.text == title]
        if len(found) != 1:
            raise RuntimeError(f"figure mapping failed for {panel}: {len(found)}")
        panel_figs[panel] = found[0]
    x_label_counts = {
        panel: max((len(dict(axis.major_label_overrides or {})) for axis in fig.xaxis), default=0)
        for panel, fig in panel_figs.items()
    }
    numeric_ranges = {
        panel: {
            "type": type(fig.y_range).__name__,
            "start": clean(getattr(fig.y_range, "start", None)),
            "end": clean(getattr(fig.y_range, "end", None)),
        }
        for panel, fig in panel_figs.items() if panel != "price"
    }
    checks = {
        "html_nonempty": html_path.stat().st_size > 100_000,
        "one_figure_per_panel": len(figures) == len(bundle.configuration["panels"]),
        "all_legends_outside_above": len(outside) == len(figures),
        "adaptive_labels_at_most_10": all(count <= 10 for count in x_label_counts.values()),
        "numeric_ranges_explicit_and_nondegenerate": all(
            item["type"] == "Range1d" and item["start"] < item["end"]
            for item in numeric_ranges.values()
        ),
        "config_v021_consumed": bundle.configuration["version"] == "0.2.1",
    }
    details: dict[str, Any] = {
        "figure_count": len(figures), "panels": list(panel_figs),
        "value_label_count": len(labels), "outside_legend_count": len(outside),
        "x_label_counts": x_label_counts, "numeric_ranges": numeric_ranges,
    }
    if bundle.mode == "selected_cut":
        k = int(bundle.meta["selected_k"])
        scalar = {panel: fig for panel, fig in panel_figs.items() if panel != "price"}
        grid_columns = sorted({int(item[2]) for grid in grids for item in grid.children})
        max_evidence = evidence_coordinate_max(layout)
        present_points = sum(
            len(bundle.views[layer["view_id"]])
            for layer in bundle.configuration["layers"]
            if layer["plot_binding"]["kind"] == "point"
            and layer["plot_binding"]["group"] != "price"
        )
        checks.update({
            "compact_two_column_grid": grid_columns == [0, 1],
            "scalar_height_150": all(fig.height == 150 for fig in scalar.values()),
            "scalar_width_880": all(fig.width == 880 for fig in scalar.values()),
            "scalar_independent_k_range": all(
                isinstance(fig.x_range, Range1d)
                and (fig.x_range.start, fig.x_range.end) == (k - 1, k + 1)
                for fig in scalar.values()
            ),
            "one_k_tick_per_scalar": all(
                all(isinstance(axis.ticker, FixedTicker) and list(axis.ticker.ticks) == [k]
                    for axis in fig.xaxis)
                for fig in scalar.values()
            ),
            "present_values_have_visible_labels": len(labels) == present_points,
            "evidence_geometry_not_after_k": max_evidence is None or max_evidence <= k,
            "price_input_not_after_k": int(bundle.price["open_uti"].max()) <= k,
        })
        details.update({
            "selected_k": k, "grid_columns": grid_columns,
            "present_scalar_points": present_points,
            "evidence_coordinate_max": max_evidence,
            "price_open_uti_max": int(bundle.price["open_uti"].max()),
            "kprice_coordinate_note": (
                "KPriceLine may store the center x of the K-opening bar at K+300; "
                "its source row open_uti remains K and no later market row is supplied."
            ),
        })
    else:
        checks.update({
            "primary_viewport_is_occurrence_price_intersection": (
                bundle.meta["evolution_display_range"] == [103056600, 103315800]
                and [int(bundle.price["open_uti"].min()), int(bundle.price["open_uti"].max())]
                == [103056600, 103315800]
            ),
            "price_rows_cropped_with_viewport": len(bundle.price) == 433,
        })
        details["evolution_display_range"] = bundle.meta["evolution_display_range"]
    result = "PASS" if all(checks.values()) else "FAIL"
    if result != "PASS":
        raise RuntimeError(f"layout validation failed: {checks}")
    return {"result": result, "checks": checks, **details}


def render(bundle: NDisplayBundle, context: OptContext, root: Path, page_id: str) -> dict[str, Any]:
    view_dir = root / "plot_view_data" / page_id
    view_manifest = export_plot_view_data(bundle, view_dir)
    layout = build_uplot_layout(
        bundle, context=context, calendar_name=CALENDAR, title_suffix=page_id
    )
    html_path = root / "render_evidence" / f"{page_id}.html"
    write_html(layout, html_path, title=f"BI01 FO01 W03 {page_id}")
    validation = validate_layout(layout, bundle, html_path)
    validation_path = root / "render_evidence" / f"{page_id}.validation.json"
    write_json(validation_path, validation)
    return {
        "page_id": page_id, "mode": bundle.mode,
        "display_identity": bundle.meta["display_identity"],
        "ppid": U2NormalNodeBehaviorDisplayFeature(bundle).ppid,
        "html": {"path": str(html_path.relative_to(root)), "bytes": html_path.stat().st_size,
                 "sha256": sha256(html_path)},
        "plot_view_data_manifest_sha256": view_manifest["manifest_sha256"],
        "validation": {"path": str(validation_path.relative_to(root)),
                       "sha256": sha256(validation_path), **validation},
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--w02-root", type=Path, required=True)
    parser.add_argument("--output-root", type=Path, required=True)
    parser.add_argument("--aidata-repo", type=Path, required=True)
    parser.add_argument("--uplot-repo", type=Path, required=True)
    args = parser.parse_args()
    root, w02 = args.output_root.resolve(), args.w02_root.resolve()
    context = OptContext(sof_name=SOF)
    price = load_price(w02 / "data/same_bound_price/rb_5m_price_calendar.csv")
    bundles: dict[str, NDisplayBundle] = {}
    for label, cut in CUTS.items():
        bundles[f"rb_selected_{label}_K{cut}"] = build_selected_cut_bundle(
            load_formal_tables(w02 / "data/selected_cuts" / label),
            price, symbol="rb", color=COLOR, as_of=cut, optional_panels=("rhythm",),
        )
    bundles = {
        "rb_evolution_actual_occurrences": load_reused_evolution(
            w02, bundles[f"rb_selected_final_K{CUTS['final']}"]
        ),
        **bundles,
    }

    pages = []
    for page_id, bundle in bundles.items():
        print(f"RENDER_START {page_id}", flush=True)
        pages.append(render(bundle, context, root, page_id))
        print(f"RENDER_DONE {page_id}", flush=True)

    selected = [bundle for bundle in bundles.values() if bundle.mode == "selected_cut"]
    ppids = [U2NormalNodeBehaviorDisplayFeature(bundle).ppid for bundle in selected]
    final = bundles[f"rb_selected_final_K{CUTS['final']}"]
    final_frames = load_formal_tables(w02 / "data/selected_cuts/final")
    shorter = build_selected_cut_bundle(
        final_frames, price.iloc[1:].copy(), symbol="rb", color=COLOR,
        as_of=CUTS["final"], optional_panels=("rhythm",),
    )
    no_optional = build_selected_cut_bundle(
        final_frames, price, symbol="rb", color=COLOR, as_of=CUTS["final"],
    )
    before = bundles[f"rb_selected_before_confirmation_K{CUTS['before_confirmation']}"]
    confirmed = bundles[f"rb_selected_at_or_after_confirmation_K{CUTS['at_or_after_confirmation']}"]
    checks = {
        "three_k_ppids_unique": len(set(ppids)) == 3,
        "same_exact_different_price_range_ppid_unique": (
            final.meta["source_exact"] == shorter.meta["source_exact"]
            and U2NormalNodeBehaviorDisplayFeature(final).ppid
            != U2NormalNodeBehaviorDisplayFeature(shorter).ppid
        ),
        "same_exact_different_optional_panels_ppid_unique": (
            final.meta["source_exact"] == no_optional.meta["source_exact"]
            and U2NormalNodeBehaviorDisplayFeature(final).ppid
            != U2NormalNodeBehaviorDisplayFeature(no_optional).ppid
        ),
        "confirmed_and_final_same_process": (
            confirmed.meta["working_life"] == final.meta["working_life"]
            and confirmed.meta["working_start"] == final.meta["working_start"]
            and confirmed.meta["working_direction"] == final.meta["working_direction"]
        ),
        "confirmed_and_final_storage_address_changed": (
            confirmed.meta["working_address"] != final.meta["working_address"]
        ),
        "before_and_confirmed_process_changed": (
            before.meta["working_life"] != confirmed.meta["working_life"]
        ),
    }
    if not all(checks.values()):
        raise RuntimeError(f"sequence/identity validation failed: {checks}")
    sequence = {
        "schema_version": 1, "result": "PASS", "checks": checks,
        "three_k": [
            {
                "selected_k": bundle.meta["selected_k"], "source_exact": bundle.meta["source_exact"],
                "working_address": bundle.meta["working_address"],
                "working_life": bundle.meta["working_life"],
                "working_start": bundle.meta["working_start"],
                "working_direction": bundle.meta["working_direction"],
                "ppid": U2NormalNodeBehaviorDisplayFeature(bundle).ppid,
            }
            for bundle in selected
        ],
        "same_exact_range_variant": {
            "base": final.meta["display_identity"], "variant": shorter.meta["display_identity"],
            "base_ppid": U2NormalNodeBehaviorDisplayFeature(final).ppid,
            "variant_ppid": U2NormalNodeBehaviorDisplayFeature(shorter).ppid,
        },
        "same_exact_optional_variant": {
            "base": final.meta["display_identity"], "variant": no_optional.meta["display_identity"],
            "base_ppid": U2NormalNodeBehaviorDisplayFeature(final).ppid,
            "variant_ppid": U2NormalNodeBehaviorDisplayFeature(no_optional).ppid,
        },
    }
    write_json(root / "evidence" / "THREE_K_AND_IDENTITY_CHECK.json", sequence)
    manifest = {
        "schema_version": 1, "result": "PASS", "order_id": "BI01-FO01-N-READABILITY-CROSSK-03",
        "render_recovery": (
            "Reused byte-hashed W02 formal selected-cut tables and display projections; "
            "did not reread the large rb normal-N tables."
        ),
        "pages": pages, "sequence_identity": sequence,
        "inputs": {
            "w02_root": str(w02),
            "rb_price_sha256": sha256(w02 / "data/same_bound_price/rb_5m_price_calendar.csv"),
            "evolution_manifest_sha256": sha256(
                w02 / "plot_view_data/rb_evolution_actual_occurrences/plot_view_data_manifest.json"
            ),
        },
        "imports": {
            "aidata": str(Path(inspect.getfile(display_module)).resolve()),
            "TIS_U2NodeBehavior": str(Path(inspect.getfile(node_module)).resolve()),
            "TIS_U2ThinNode": str(Path(inspect.getfile(thin_module)).resolve()),
            "worker_schema": str(Path(inspect.getfile(worker_schema)).resolve()),
            "uplot": str(Path(inspect.getfile(uplot_module)).resolve()),
        },
        "versions": {
            "configuration": CONFIG_VERSION,
            "aidata_branch": git_value(args.aidata_repo, "branch", "--show-current"),
            "aidata_head": git_value(args.aidata_repo, "rev-parse", "HEAD"),
            "uplot_head": git_value(args.uplot_repo, "rev-parse", "HEAD"),
            "uplot_status": git_value(args.uplot_repo, "status", "--short"),
        },
        "acceptance_distinctions": {
            "html_and_bokeh_models": "PASS", "browser_pixels": "PENDING_SEPARATE_CAPTURE",
            "worker_visual_inspection": "PENDING_SEPARATE_INSPECTION",
            "professional_interpretation": "NOT_WORKER_AUTHORITY",
        },
    }
    write_json(root / "evidence" / "RENDER_MANIFEST.json", manifest)
    print(json.dumps({"result": "PASS", "pages": list(bundles)}, ensure_ascii=False), flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
