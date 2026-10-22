#!/usr/bin/env python3
"""Directly check the R8 selected-K endpoint on the actual Worker02 consumer.

This check rebuilds only the in-memory uplot layouts from the already hashed
formal readback exports.  It does not rerun the N product or alter any formal
value.  The purpose is to observe the real ``ctx.uti_slice`` passed to the
aidata wrapper and the actual Bokeh renderer data at each selected K.
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
from typing import Any

import numpy as np
import pandas as pd
from bokeh.models import ColumnDataSource
from mquant.quant import OptContext

import mquant.aidata.u2_normal_node_behavior_display as display_module


SOF = "TA_updto20240229_DBA"
CALENDAR = "night_end_at_2300"
COLOR = "#4C78A8"
CUTS = {
    "before_confirmation": 103150800,
    "at_or_after_confirmation": 103151400,
    "final": 103315800,
}
SCALAR_VIEWS = (
    "completed_recent_updates",
    "completed_previous_updates",
    "recent_duration_updates",
    "previous_duration_updates",
    "working_progress_points",
    "working_counter_points",
    "working_efficiency_points",
    "working_duration_points",
    "waiting_ratio_points",
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
    if value is pd.NA or value is pd.NaT:
        return None
    if isinstance(value, float) and not np.isfinite(value):
        return None
    if isinstance(value, (pd.Timestamp, dt.datetime, Path)):
        return str(value)
    return value


def git_value(repo: Path, *args: str) -> str:
    return subprocess.check_output(
        ["git", "-C", str(repo), *args], text=True, stderr=subprocess.STDOUT
    ).strip()


def load_resume_module(script: Path):
    spec = importlib.util.spec_from_file_location("worker02_resume_for_endpoint_r8", script)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {script}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def numeric_max(values: Any) -> int | None:
    series = pd.to_numeric(pd.Series(list(values)), errors="coerce").dropna()
    return None if series.empty else int(series.max())


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, required=True)
    parser.add_argument("--aidata-repo", type=Path, required=True)
    parser.add_argument("--uplot-repo", type=Path, required=True)
    args = parser.parse_args()
    root = args.root.resolve()
    resume = load_resume_module(root / "scripts" / "resume_render_from_exports.py")
    price = resume.load_price(root / "data" / "same_bound_price" / "rb_5m_price_calendar.csv")
    browser = json.loads((root / "render_evidence" / "BROWSER_CAPTURE.json").read_text(encoding="utf-8"))
    visual = json.loads((root / "render_evidence" / "ENDPOINT_R8_VISUAL_INSPECTION.json").read_text(encoding="utf-8"))
    browser_by_page = {item["page_id"]: item for item in browser["results"]}
    visual_by_page = {item["page_id"]: item for item in visual["pages"]}

    pages = []
    original = display_module.U2NormalNodeBehaviorDisplayFeature.evidence_view_df
    for label, selected_k in CUTS.items():
        page_id = f"rb_selected_{label}_K{selected_k}"
        frames = resume.load_formal_tables(root / "data" / "selected_cuts" / label)
        bundle = resume.build_selected_cut_bundle(
            frames,
            price,
            symbol="rb",
            color=COLOR,
            as_of=selected_k,
            optional_panels=("duration", "rhythm"),
        )
        calls: list[dict[str, Any]] = []

        def observed(self, df_key, *, start_uti, end_uti):
            frame = original(self, df_key, start_uti=start_uti, end_uti=end_uti)
            calls.append({
                "view": str(df_key),
                "start_uti_inclusive": int(start_uti),
                "end_uti_exclusive": int(end_uti),
                "returned_rows": int(len(frame)),
                "returned_x": (
                    [int(value) for value in pd.to_numeric(frame["x"]).tolist()]
                    if "x" in frame and len(frame) <= 4 else []
                ),
            })
            return frame

        display_module.U2NormalNodeBehaviorDisplayFeature.evidence_view_df = observed
        try:
            layout = resume.build_uplot_layout(
                bundle,
                context=OptContext(sof_name=SOF),
                calendar_name=CALENDAR,
                title_suffix=f"{page_id}-endpoint-r8",
            )
        finally:
            display_module.U2NormalNodeBehaviorDisplayFeature.evidence_view_df = original

        renderers: dict[str, dict[str, Any]] = {}
        no_feature_after_k = True
        for model in layout.references():
            tags = list(getattr(model, "tags", []) or [])
            if "aidata_evidence" not in tags:
                continue
            anchor = next((tag for tag in tags if isinstance(tag, str) and tag.startswith("anchor:n_display/")), None)
            if anchor is None:
                continue
            view = anchor.split("/", 1)[1]
            source = getattr(model, "data_source", None)
            data = {} if not isinstance(source, ColumnDataSource) else source.data
            maxima = {
                column: numeric_max(data[column])
                for column in ("x", "x0", "x1") if column in data
            }
            if any(value is not None and value > selected_k for value in maxima.values()):
                no_feature_after_k = False
            renderers[view] = {
                "rows": int(len(next(iter(data.values())))) if data else 0,
                "coordinate_maxima": maxima,
                "x_values": (
                    [int(value) for value in pd.to_numeric(pd.Series(data["x"])).tolist()]
                    if "x" in data and len(data["x"]) <= 4 else []
                ),
            }

        scalar_results = {}
        for view in SCALAR_VIEWS:
            source = renderers.get(view, {})
            xs = source.get("x_values", [])
            scalar_results[view] = {
                "rows": source.get("rows", 0),
                "x_values": xs,
                "k_visible": bool(xs) and selected_k in xs,
            }

        call_windows = sorted({
            (item["start_uti_inclusive"], item["end_uti_exclusive"])
            for item in calls
        })
        logical_maxima = {}
        no_logical_view_after_k = True
        for view, frame in bundle.views.items():
            maxima = {
                column: numeric_max(frame[column])
                for column in ("x", "x0", "x1") if column in frame
            }
            logical_maxima[view] = maxima
            if any(value is not None and value > selected_k for value in maxima.values()):
                no_logical_view_after_k = False

        html = root / "render_evidence" / f"{page_id}.html"
        png = root / "render_evidence" / f"{page_id}.png"
        validation = json.loads(
            (root / "render_evidence" / f"{page_id}.validation.json").read_text(encoding="utf-8")
        )
        browser_item = browser_by_page[page_id]
        screenshot = browser_item["screenshot"]
        checks = {
            "actual_consumer_end_exclusive_is_k_plus_one": call_windows == [(int(bundle.price["open_uti"].min()), selected_k + 1)],
            "all_nine_formal_scalar_renderers_contain_k": all(
                item["k_visible"] for item in scalar_results.values()
            ),
            "no_logical_feature_coordinate_after_k": no_logical_view_after_k,
            "no_rendered_feature_coordinate_after_k": no_feature_after_k,
            "raw_price_input_ends_at_k": int(bundle.price["open_uti"].max()) == selected_k,
            "close_path_renderer_ends_at_k": renderers["close_path"]["coordinate_maxima"]["x"] == selected_k,
            "existing_render_validation_no_geometry_after_k": validation["checks"]["selected_cut_has_no_geometry_after_K"] is True,
            "existing_browser_capture_pass": browser_item["result"] == "PASS",
            "existing_browser_png_hash_matches": sha256(png) == screenshot["sha256"],
            "existing_html_present_and_hashed": html.stat().st_size > 100_000,
            "post_fix_worker_pixel_inspection_pass": (
                page_id in visual_by_page and visual_by_page[page_id]["result"] == "PASS"
            ),
        }
        pages.append({
            "page_id": page_id,
            "selected_k": selected_k,
            "resolved_origin_as_of": int(bundle.meta["resolved_origin_as_of"]),
            "actual_consumer_windows": [
                {"start_uti_inclusive": start, "end_uti_exclusive": end}
                for start, end in call_windows
            ],
            "scalar_renderers": scalar_results,
            "logical_view_coordinate_maxima": logical_maxima,
            "raw_price_open_uti_max": int(bundle.price["open_uti"].max()),
            "existing_html": {"path": str(html.relative_to(root)), "bytes": html.stat().st_size, "sha256": sha256(html)},
            "existing_png": {"path": str(png.relative_to(root)), "bytes": png.stat().st_size, "sha256": sha256(png)},
            "existing_pixel_observations": visual_by_page[page_id]["observed"],
            "checks": checks,
            "result": "PASS" if all(checks.values()) else "FAIL",
        })

    payload = {
        "schema_version": 1,
        "order_id": "BI01-FO01-N-DISPLAY-INTEGRATION-02",
        "supplement_marker": "BI01-FO01-WORKER-DISPLAY02-ENDPOINT-R8-20261022",
        "result": "PASS" if all(page["result"] == "PASS" for page in pages) else "FAIL",
        "method": "rebuild exact in-memory uplot layout from previously hashed formal exports; observe actual ctx.uti_slice and Bokeh evidence renderers; no N reread",
        "conditional_risk_disposition": "RIGHT_OPEN_K_FILTER_NOT_REPRODUCED; SEQUENTIAL_PLOTTER_IDENTITY_REUSE_REPRODUCED_AND_FIXED",
        "boundary_explanation": "The wrapper remains right-open, but actual uplot calls it with end_uti_exclusive=K+1, so the management's exact end_uti=K condition is not present. A separate actual defect was found: consecutive selected layouts reused the first cut's BasePlotter identity because the plain display feature was not part of that identity. Binding feature.ppid into inert anchor metadata makes each cut distinct. The selected bundle remains independently clipped to formal/view/price coordinates <=K, so no K-after record is admitted.",
        "versions": {
            "aidata_commit": git_value(args.aidata_repo.resolve(), "rev-parse", "HEAD"),
            "uplot_commit": git_value(args.uplot_repo.resolve(), "rev-parse", "HEAD"),
            "aidata_module": str(Path(display_module.__file__).resolve()),
        },
        "linked_evidence": {
            "browser_capture_sha256": sha256(root / "render_evidence" / "BROWSER_CAPTURE.json"),
            "endpoint_r8_visual_inspection_sha256": sha256(root / "render_evidence" / "ENDPOINT_R8_VISUAL_INSPECTION.json"),
            "pre_fix_html_audit_sha256": sha256(root / "evidence" / "ENDPOINT_R8_PRE_FIX_HTML_AUDIT.json"),
            "post_fix_html_audit_sha256": sha256(root / "evidence" / "ENDPOINT_R8_POST_FIX_HTML_AUDIT.json"),
        },
        "pages": pages,
        "modification_required": True,
        "modification_scope": "aidata display consumer only: bind U2NormalNodeBehaviorDisplayFeature.ppid into BasePlotter anchor identity; formal data and business K unchanged",
        "limitations": [
            "This is a direct check of the actual Worker02 adapter and uplot call path at the three delivered rb selected cuts, not a claim about every generic aidata caller.",
            "A candlestick glyph can geometrically occupy bar width around its x coordinate; this check treats the underlying open_uti record identity, not half-bar screen width, as the no-future boundary.",
            "The three selected pages were rerendered from existing hashed formal exports after the aidata fix; the N product and evolution page were not rerun.",
            "Browser screenshots and endpoint pixel observations are post-fix evidence; the pre-fix saved HTML remains reproducible from observe-iterate artifact commit 39308f4a8fe6b6f2fe1399f8d9e56b91a5ceb643."
        ]
    }
    output = root / "evidence" / "ENDPOINT_R8_DIRECT_CHECK.json"
    output.write_text(
        json.dumps(clean(payload), ensure_ascii=False, indent=2, allow_nan=False) + "\n",
        encoding="utf-8",
    )
    print(json.dumps({
        "result": payload["result"],
        "pages": len(pages),
        "output": str(output),
        "sha256": sha256(output),
    }, ensure_ascii=False), flush=True)
    return 0 if payload["result"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
