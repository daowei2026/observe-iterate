#!/usr/bin/env python3
"""Cross-check delivered scalar CDS rows against projections and formal exports.

The audit reads the saved Bokeh HTML documents themselves.  It compares the
old delivery commit and the current worktree with the delivered plot-view CSVs,
then independently derives the nine expected scalar values from the already
hashed selected-cut formal tables.  It never reads or reruns the N product.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
import re
import subprocess
from typing import Any

import numpy as np
import pandas as pd
from bokeh.document import Document


OLD_DELIVERY_REF = "39308f4a8fe6b6f2fe1399f8d9e56b91a5ceb643"
CURRENT_ARTIFACT_REF = "081e31241a0c88e47631f80a8b9b8dd43b2b569c"
PAGES = (
    ("before_confirmation", 103150800),
    ("at_or_after_confirmation", 103151400),
    ("final", 103315800),
)
FORMAL_SOURCES = {
    "completed_recent_updates": ("metrics.csv", "kind=8", "current"),
    "completed_previous_updates": ("metrics.csv", "kind=8", "previous"),
    "recent_duration_updates": ("metrics.csv", "kind=0", "current"),
    "previous_duration_updates": ("metrics.csv", "kind=0", "previous"),
    "working_progress_points": ("working_progress.csv", "row=0", "value"),
    "working_counter_points": ("working_counter.csv", "row=0", "value"),
    "working_efficiency_points": ("working_efficiency.csv", "row=0", "value"),
    "working_duration_points": ("working_duration.csv", "row=0", "value"),
    "waiting_ratio_points": ("working_waiting_ratio.csv", "row=0", "value"),
}
SCALAR_COLUMNS = (
    "x",
    "y",
    "symbol",
    "source_exact",
    "as_of_uti",
    "origin_uti",
    "state_text",
    "meaning",
)


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def clean(value: Any) -> Any:
    if isinstance(value, np.generic):
        return clean(value.item())
    if value is pd.NA or value is pd.NaT:
        return None
    if isinstance(value, float) and not math.isfinite(value):
        return None
    if isinstance(value, dict):
        return {str(key): clean(item) for key, item in value.items()}
    if isinstance(value, (list, tuple, np.ndarray)):
        return [clean(item) for item in value]
    return value


def same_value(left: Any, right: Any) -> bool:
    left = clean(left)
    right = clean(right)
    if left is None or right is None:
        return left is right
    if isinstance(left, (int, float)) and isinstance(right, (int, float)):
        return math.isclose(float(left), float(right), rel_tol=1e-12, abs_tol=1e-12)
    return left == right


def git_bytes(repo: Path, root: Path, source_ref: str, relative: Path) -> bytes:
    path = root.relative_to(repo) / relative
    if source_ref == "WORKTREE":
        return (repo / path).read_bytes()
    return subprocess.check_output(["git", "-C", str(repo), "show", f"{source_ref}:{path}"])


def document_from_html(data: bytes) -> Document:
    match = re.search(
        rb'<script type="application/json"[^>]*>\s*(\{.*?\})\s*</script>',
        data,
        re.DOTALL,
    )
    if match is None:
        raise RuntimeError("Bokeh document JSON not found")
    documents = json.loads(match.group(1).decode("utf-8"))
    if len(documents) != 1:
        raise RuntimeError(f"expected one Bokeh document, got {len(documents)}")
    return Document.from_json(next(iter(documents.values())))


def renderer_rows(
    document: Document, selected_k: int
) -> tuple[dict[str, list[dict[str, Any]]], bool]:
    result: dict[str, list[dict[str, Any]]] = {}
    no_coordinate_after_k = True
    for model in document.models:
        tags = list(getattr(model, "tags", []) or [])
        if "aidata_evidence" not in tags:
            continue
        anchor = next(
            (tag for tag in tags if isinstance(tag, str) and tag.startswith("anchor:n_display/")),
            None,
        )
        if anchor is None:
            continue
        view = anchor.split("/", 1)[1]
        source = getattr(model, "data_source", None)
        data = {} if source is None else source.data
        lengths = {len(values) for values in data.values()}
        if len(lengths) > 1:
            raise RuntimeError(f"unequal CDS column lengths for {view}: {lengths}")
        count = next(iter(lengths), 0)
        rows = [
            {str(column): clean(values[index]) for column, values in data.items()}
            for index in range(count)
        ]
        if view in result and result[view] != rows:
            raise RuntimeError(f"non-identical duplicate renderer data for {view}")
        result[view] = rows
    for rows in result.values():
        for row in rows:
            for column in ("x", "x0", "x1"):
                value = row.get(column)
                if value is not None and float(value) > selected_k:
                    no_coordinate_after_k = False
    return result, no_coordinate_after_k


def scalar_projection(path: Path) -> dict[str, Any]:
    frame = pd.read_csv(path)
    if len(frame) != 1:
        raise RuntimeError(f"expected one scalar row in {path}, got {len(frame)}")
    return {column: clean(frame.iloc[0][column]) for column in SCALAR_COLUMNS}


def formal_value(formal_dir: Path, view: str) -> tuple[float | None, dict[str, Any]]:
    filename, selector, column = FORMAL_SOURCES[view]
    frame = pd.read_csv(formal_dir / filename)
    if selector.startswith("kind="):
        kind = int(selector.split("=", 1)[1])
        frame = frame[pd.to_numeric(frame["kind"]) == kind]
    if len(frame) != 1:
        raise RuntimeError(f"expected one formal row for {view} in {filename}, got {len(frame)}")
    row = frame.iloc[0]
    value = clean(row[column])
    state_columns = [
        name for name in ("present", "loo_knownness", "knownness", "applicability", "reason")
        if name in row.index
    ]
    return value, {
        "file": f"data/selected_cuts/{formal_dir.name}/{filename}",
        "selector": selector,
        "column": column,
        "state": {name: clean(row[name]) for name in state_columns},
    }


def selected_exact(temporal: dict[str, Any], label: str) -> str:
    return str(temporal["rb"]["selected_meta"][label]["source_exact"])


def compare_scalar_rows(actual: dict[str, Any], expected: dict[str, Any]) -> dict[str, Any]:
    fields = {column: same_value(actual.get(column), expected.get(column)) for column in SCALAR_COLUMNS}
    return {"fields": fields, "all_fields_match": all(fields.values())}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, required=True)
    parser.add_argument("--root", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    repo = args.repo.resolve()
    root = args.root.resolve()
    temporal = json.loads((root / "evidence" / "TEMPORAL_CASES.json").read_text(encoding="utf-8"))
    browser = json.loads((root / "render_evidence" / "BROWSER_CAPTURE.json").read_text(encoding="utf-8"))
    browser_by_page = {item["page_id"]: item for item in browser["results"]}

    pages = []
    for label, selected_k in PAGES:
        page_id = f"rb_selected_{label}_K{selected_k}"
        html_relative = Path("render_evidence") / f"{page_id}.html"
        png_relative = Path("render_evidence") / f"{page_id}.png"
        old_html = git_bytes(repo, root, OLD_DELIVERY_REF, html_relative)
        current_html = git_bytes(repo, root, "WORKTREE", html_relative)
        old_png = git_bytes(repo, root, OLD_DELIVERY_REF, png_relative)
        current_png = git_bytes(repo, root, "WORKTREE", png_relative)
        old_renderers, old_no_future = renderer_rows(document_from_html(old_html), selected_k)
        current_renderers, current_no_future = renderer_rows(document_from_html(current_html), selected_k)
        formal_dir = root / "data" / "selected_cuts" / label
        plot_dir = root / "plot_view_data" / page_id
        exact = selected_exact(temporal, label)
        origin_as_of = int(pd.read_csv(formal_dir / "origins.csv").iloc[0]["as_of"])
        price = pd.read_csv(plot_dir / "same_bound_5m_ohlc.csv")
        scalar_views = {}
        for view in FORMAL_SOURCES:
            projection = scalar_projection(plot_dir / f"n_display__{view}.csv")
            expected_value, formal_source = formal_value(formal_dir, view)
            old_rows = old_renderers.get(view, [])
            current_rows = current_renderers.get(view, [])
            old_row = old_rows[0] if len(old_rows) == 1 else {}
            current_row = current_rows[0] if len(current_rows) == 1 else {}
            projection_identity = {
                "x_is_k": same_value(projection["x"], selected_k),
                "as_of_is_k": same_value(projection["as_of_uti"], selected_k),
                "origin_is_k": same_value(projection["origin_uti"], origin_as_of),
                "exact_matches_selected_cut": projection["source_exact"] == exact,
                "y_matches_formal_table": same_value(projection["y"], expected_value),
            }
            scalar_views[view] = {
                "formal": {**formal_source, "value": expected_value},
                "projection": projection,
                "projection_checks": projection_identity,
                "old_delivery_html": old_row,
                "old_html_vs_projection": compare_scalar_rows(old_row, projection),
                "current_delivery_html": current_row,
                "current_html_vs_projection": compare_scalar_rows(current_row, projection),
            }

        current_matches = sum(
            item["current_html_vs_projection"]["all_fields_match"] for item in scalar_views.values()
        )
        old_matches = sum(
            item["old_html_vs_projection"]["all_fields_match"] for item in scalar_views.values()
        )
        projections_match_formal = all(
            all(item["projection_checks"].values()) for item in scalar_views.values()
        )
        screenshot = browser_by_page[page_id]["screenshot"]
        checks = {
            "all_nine_projection_rows_match_formal_value_and_identity": projections_match_formal,
            "all_nine_current_html_cds_rows_match_projection": current_matches == len(FORMAL_SOURCES),
            "current_html_has_no_feature_coordinate_after_k": current_no_future,
            "plot_price_ends_at_k": int(pd.to_numeric(price["open_uti"]).max()) == selected_k,
            "current_png_matches_browser_capture": sha256_bytes(current_png) == screenshot["sha256"],
            "browser_capture_result_pass": browser_by_page[page_id]["result"] == "PASS",
        }
        pages.append({
            "label": label,
            "page_id": page_id,
            "selected_k": selected_k,
            "source_exact": exact,
            "formal_origin_as_of": origin_as_of,
            "old_delivery": {
                "source_ref": OLD_DELIVERY_REF,
                "html_sha256": sha256_bytes(old_html),
                "png_sha256": sha256_bytes(old_png),
                "scalar_views_matching_current_projection": old_matches,
                "no_feature_coordinate_after_k": old_no_future,
            },
            "current_delivery": {
                "artifact_ref": CURRENT_ARTIFACT_REF,
                "html_sha256": sha256_bytes(current_html),
                "png_sha256": sha256_bytes(current_png),
                "scalar_views_matching_projection": current_matches,
                "no_feature_coordinate_after_k": current_no_future,
            },
            "scalar_views": scalar_views,
            "checks": checks,
            "result": "PASS" if all(checks.values()) else "FAIL",
        })

    first_projection = {
        view: item["projection"] for view, item in pages[0]["scalar_views"].items()
    }
    old_later_reuses_first = {}
    for page in pages[1:]:
        old_later_reuses_first[page["label"]] = all(
            compare_scalar_rows(page["scalar_views"][view]["old_delivery_html"], first_projection[view])[
                "all_fields_match"
            ]
            for view in FORMAL_SOURCES
        )

    old_pattern_reproduced = (
        pages[0]["old_delivery"]["scalar_views_matching_current_projection"] == len(FORMAL_SOURCES)
        and all(page["old_delivery"]["scalar_views_matching_current_projection"] == 0 for page in pages[1:])
        and all(old_later_reuses_first.values())
    )
    all_current_pass = all(page["result"] == "PASS" for page in pages)
    payload = {
        "schema_version": 1,
        "order_id": "BI01-FO01-N-DISPLAY-INTEGRATION-02",
        "supplement_marker": "BI01-FO01-W02-SCALAR-CONSISTENCY-20261022",
        "result": "PASS" if old_pattern_reproduced and all_current_pass else "FAIL",
        "method": (
            "Read saved Bokeh HTML/CDS from old Git artifact and current delivery; compare all nine scalar "
            "rows with delivered plot-view CSVs and values independently selected from existing formal tables. "
            "No formal N read or isolated layout rebuild is used by this audit."
        ),
        "old_delivery_finding": (
            "The 39308f4 before-confirmation page matches its projection.  Both later saved HTML documents "
            "reuse all nine before-confirmation scalar CDS rows, including x, y, exact and state fields."
        ),
        "current_delivery_finding": (
            "The R8-rerendered three saved HTML documents each contain nine scalar CDS rows matching their "
            "own projection and formal selected-cut values, and contain no feature coordinate after K."
        ),
        "old_sequential_reuse_pattern_reproduced": old_pattern_reproduced,
        "old_later_pages_reuse_all_first_page_scalar_rows": old_later_reuses_first,
        "all_current_pages_pass": all_current_pass,
        "linked_fix": {
            "aidata_commit": "28260d3ec5d2ed254b2539cb9abc656e4737f80b",
            "observe_iterate_artifact_commit": CURRENT_ARTIFACT_REF,
            "endpoint_check_sha256": sha256_file(root / "evidence" / "ENDPOINT_R8_DIRECT_CHECK.json"),
            "post_fix_html_audit_sha256": sha256_file(root / "evidence" / "ENDPOINT_R8_POST_FIX_HTML_AUDIT.json"),
            "rerender_record_sha256": sha256_file(root / "evidence" / "ENDPOINT_R8_RERENDER.json"),
        },
        "pages": pages,
        "limitations": [
            "The audit covers the three delivered rb selected cuts and all nine configured scalar views; it is not a claim about every aidata feature.",
            "The current HTML/PNG files were already rerendered sequentially in the R8 endpoint supplement from the same hashed formal exports; this challenge did not rerender them again.",
            "The evolution page follows the three selected pages and cannot retroactively alter their serialized HTML; it was not rerendered in R8 or this challenge.",
            "Pixel placement alone is not used to decide numeric correctness; the saved renderer CDS is authoritative for this technical display check.",
        ],
    }
    output = args.output.resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(clean(payload), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "result": payload["result"],
        "old_reuse_reproduced": old_pattern_reproduced,
        "current_pages_pass": all_current_pass,
        "output": str(output),
        "sha256": sha256_file(output),
    }, ensure_ascii=False), flush=True)
    return 0 if payload["result"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
