#!/usr/bin/env python3
"""Audit selected-cut scalar endpoints in saved Bokeh HTML documents."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess
from typing import Any

import pandas as pd
from bokeh.document import Document


PAGES = (
    "rb_selected_before_confirmation_K103150800",
    "rb_selected_at_or_after_confirmation_K103151400",
    "rb_selected_final_K103315800",
)
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


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def html_bytes(repo: Path, root: Path, source_ref: str, page_id: str) -> bytes:
    relative = root.relative_to(repo) / "render_evidence" / f"{page_id}.html"
    if source_ref == "WORKTREE":
        return (repo / relative).read_bytes()
    return subprocess.check_output(["git", "-C", str(repo), "show", f"{source_ref}:{relative}"])


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


def numeric_max(values: Any) -> int | None:
    series = pd.to_numeric(pd.Series(list(values)), errors="coerce").dropna()
    return None if series.empty else int(series.max())


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, required=True)
    parser.add_argument("--root", type=Path, required=True)
    parser.add_argument("--source-ref", required=True, help="Git commit or WORKTREE")
    parser.add_argument("--expect", choices=("defect", "fixed"), required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    repo = args.repo.resolve()
    root = args.root.resolve()
    pages = []
    for page_id in PAGES:
        selected_k = int(page_id.rsplit("K", 1)[1])
        data = html_bytes(repo, root, args.source_ref, page_id)
        document = document_from_html(data)
        renderers = {}
        no_feature_after_k = True
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
            values = {} if source is None else source.data
            maxima = {
                column: numeric_max(values[column])
                for column in ("x", "x0", "x1") if column in values
            }
            if any(value is not None and value > selected_k for value in maxima.values()):
                no_feature_after_k = False
            renderers[view] = {
                "rows": int(len(next(iter(values.values())))) if values else 0,
                "x_values": (
                    [int(value) for value in pd.to_numeric(pd.Series(values["x"])).tolist()]
                    if "x" in values and len(values["x"]) <= 4 else []
                ),
                "source_exact": (
                    [str(value) for value in values.get("source_exact", [])]
                    if len(values.get("source_exact", [])) <= 4 else []
                ),
                "coordinate_maxima": maxima,
            }
        scalar = {
            view: {
                **renderers.get(view, {"rows": 0, "x_values": [], "source_exact": [], "coordinate_maxima": {}}),
                "k_visible": selected_k in renderers.get(view, {}).get("x_values", []),
            }
            for view in SCALAR_VIEWS
        }
        pages.append({
            "page_id": page_id,
            "selected_k": selected_k,
            "html_bytes": len(data),
            "html_sha256": sha256(data),
            "scalar_renderers": scalar,
            "all_nine_scalar_renderers_contain_k": all(item["k_visible"] for item in scalar.values()),
            "no_rendered_feature_coordinate_after_k": no_feature_after_k,
            "close_path_max_x": renderers["close_path"]["coordinate_maxima"]["x"],
        })

    all_visible = all(page["all_nine_scalar_renderers_contain_k"] for page in pages)
    no_future = all(page["no_rendered_feature_coordinate_after_k"] for page in pages)
    defect_pattern = (
        pages[0]["all_nine_scalar_renderers_contain_k"]
        and any(not page["all_nine_scalar_renderers_contain_k"] for page in pages[1:])
        and no_future
    )
    expectation_met = all_visible and no_future if args.expect == "fixed" else defect_pattern
    payload = {
        "schema_version": 1,
        "order_id": "BI01-FO01-N-DISPLAY-INTEGRATION-02",
        "supplement_marker": "BI01-FO01-WORKER-DISPLAY02-ENDPOINT-R8-20261022",
        "source_ref": args.source_ref,
        "expectation": args.expect,
        "result": "PASS" if expectation_met else "FAIL",
        "all_selected_pages_have_k_scalar": all_visible,
        "all_selected_pages_exclude_post_k_feature_coordinates": no_future,
        "sequential_first_cut_reuse_pattern_observed": defect_pattern,
        "pages": pages,
    }
    output = args.output.resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "result": payload["result"],
        "expectation": args.expect,
        "output": str(output),
        "sha256": sha256(output.read_bytes()),
    }, ensure_ascii=False), flush=True)
    return 0 if expectation_met else 1


if __name__ == "__main__":
    raise SystemExit(main())
