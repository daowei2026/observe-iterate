#!/usr/bin/env python3
"""有限合成显示探针；与真实市场页严格分开。"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import pandas as pd
from bokeh.models import LabelSet, Range1d, Title
from mquant.quant import OptContext
from mquant.aidata.u2_normal_node_behavior_display import (
    build_selected_cut_bundle,
    build_uplot_layout,
)


def load_formal_tables(directory: Path):
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


def load_price(path: Path):
    frame = pd.read_csv(path)
    first = frame.columns[0]
    frame[first] = pd.to_datetime(frame[first])
    return frame.set_index(first)


def figure_map(layout):
    result = {}
    for model in layout.references():
        title = getattr(getattr(model, "title", None), "text", "")
        if hasattr(model, "renderers") and title:
            if "沿原方向净推进" in title:
                result["working_motion"] = model
            elif "前缀效率" in title:
                result["working_efficiency"] = model
            elif "局部等待" in title:
                result["rhythm"] = model
    return result


def label_texts(layout):
    result = []
    for label in layout.references():
        if not isinstance(label, LabelSet) or "n_display_value_label" not in list(label.tags or []):
            continue
        result.extend(str(value) for value in label.source.data["display_value"])
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--aidata-repo", type=Path, required=True)
    parser.add_argument("--w02-root", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    context = OptContext(sof_name="TA_updto20240229_DBA")
    source_frames = load_formal_tables(args.w02_root / "data/selected_cuts/final")
    price = load_price(args.w02_root / "data/same_bound_price/rb_5m_price_calendar.csv")
    selected_k = 103315800

    baseline = build_selected_cut_bundle(
        source_frames, price, symbol="rb", color="#4C78A8",
        as_of=selected_k, optional_panels=("rhythm",),
    )
    baseline_layout = build_uplot_layout(
        baseline, context=context, calendar_name="night_end_at_2300", title_suffix="synthetic-baseline"
    )

    zero_frames = {name: frame.copy() for name, frame in source_frames.items()}
    zero_frames["working_progress"].iloc[
        0, zero_frames["working_progress"].columns.get_loc("value")
    ] = 0.0
    # A different formal payload must also carry a different exact identity;
    # otherwise the real in-process plotter cache is correctly entitled to
    # reuse the already rendered baseline exact.
    zero_frames["revisions"].iloc[
        0, zero_frames["revisions"].columns.get_loc("low")
    ] += 1
    zero = build_selected_cut_bundle(
        zero_frames, price, symbol="rb", color="#4C78A8",
        as_of=selected_k, optional_panels=("rhythm",),
    )
    zero_layout = build_uplot_layout(
        zero, context=context, calendar_name="night_end_at_2300", title_suffix="synthetic-zero"
    )

    null_frames = {name: frame.copy() for name, frame in source_frames.items()}
    for name in (
        "working_progress", "working_efficiency", "working_counter",
        "working_waiting", "working_waiting_ratio",
    ):
        null_frames[name].iloc[0, null_frames[name].columns.get_loc("present")] = 0
    null_frames["revisions"].iloc[
        0, null_frames["revisions"].columns.get_loc("low")
    ] += 2
    null = build_selected_cut_bundle(
        null_frames, price, symbol="rb", color="#4C78A8",
        as_of=selected_k, optional_panels=("rhythm",),
    )
    null_layout = build_uplot_layout(
        null, context=context, calendar_name="night_end_at_2300", title_suffix="synthetic-null"
    )
    null_figures = figure_map(null_layout)
    null_titles = [
        title.text for title in null_layout.references()
        if isinstance(title, Title) and "无正式数值" in title.text
    ]
    baseline_text = label_texts(baseline_layout)
    zero_text = label_texts(zero_layout)
    checks = {
        "singleton_scalar_range_is_k_plus_minus_one": all(
            isinstance(fig.x_range, Range1d)
            and (fig.x_range.start, fig.x_range.end) == (selected_k - 1, selected_k + 1)
            for fig in figure_map(baseline_layout).values()
        ),
        "waiting_above_one_visible_without_hover": "15.8462 ratio" in baseline_text,
        "true_zero_visible_without_hover": "0 price" in zero_text,
        "all_null_working_panels_marked_not_blank_or_zero": (
            set(null_figures) == {"working_motion", "working_efficiency", "rhythm"}
            and all(not fig.yaxis[0].visible for fig in null_figures.values())
            and len(null_titles) >= 3
        ),
    }
    payload = {
        "schema_version": 1,
        "qualification": "synthetic display mechanics only; not market evidence",
        "result": "PASS" if all(checks.values()) else "FAIL",
        "checks": checks,
        "baseline_labels": baseline_text,
        "zero_labels": zero_text,
        "null_state_titles": null_titles,
    }
    if payload["result"] != "PASS":
        raise RuntimeError(payload)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"result": "PASS", "output": str(args.output)}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
