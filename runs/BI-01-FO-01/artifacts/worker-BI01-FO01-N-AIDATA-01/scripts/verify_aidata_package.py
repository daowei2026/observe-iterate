#!/usr/bin/env python3
"""Verify that successful rendering did not hide a broken result package."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import pandas as pd


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def raw(path: Path) -> pd.DataFrame:
    return pd.read_csv(path, dtype=str, keep_default_na=False)


def compare_raw(source: pd.DataFrame, exported: pd.DataFrame, columns: list[str]) -> bool:
    return source[columns].reset_index(drop=True).equals(exported[columns].reset_index(drop=True))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--projection-dir", required=True, type=Path)
    parser.add_argument("--run-dir", required=True, type=Path)
    args = parser.parse_args()
    projection = args.projection_dir.resolve()
    run = args.run_dir.resolve()

    fixed = json.loads((run / "manifest/fixed_input.json").read_text(encoding="utf-8"))
    summary = json.loads((run / "manifest/run_summary.json").read_text(encoding="utf-8"))
    browser = json.loads((run / "render_evidence/BROWSER_CAPTURE.json").read_text(encoding="utf-8"))
    visual = json.loads((run / "render_evidence/VISUAL_INSPECTION.json").read_text(encoding="utf-8"))
    render = json.loads((run / "render_evidence/RENDER_VALIDATION.json").read_text(encoding="utf-8"))
    sources = {item["id"]: item for item in fixed["sources"]}
    checks = []

    def check(name: str, passed: bool, evidence) -> None:
        checks.append({"name": name, "pass": bool(passed), "evidence": evidence})

    source_hashes = {}
    for source_id, item in sources.items():
        path = Path(item["path"])
        actual = sha256(path)
        source_hashes[source_id] = actual
        check(f"source_identity.{source_id}", actual == item["sha256"], {"path": str(path), "declared": item["sha256"], "actual": actual})

    check("aidata_feature_executions_zero", summary["feature_executions"] == 0, summary)
    check("three_fixed_views", summary["view_count"] == 3 and len(fixed["views"]) == 3, {"summary": summary["view_count"], "spec": len(fixed["views"])})
    check("three_bokeh_documents", len(render["documents"]) == 3, len(render["documents"]))
    check("bokeh_wire_serialized", all(item["bokeh_document_json_parsed"] for item in render["documents"]), [item["bokeh_document_json_sha256"] for item in render["documents"]])
    check("browser_capture", browser["result"] == "PASS", browser["result"])
    check("visual_inspection", visual["result"] == "PASS_WITH_SCOPE", visual["result"])
    platform = [item for item in browser["results"] if item["kind"] == "platform_report_url"]
    check("platform_three_http_200_with_canvas", len(platform) == 3 and all(item["result"] == "PASS" and item["http_status"] == 200 and item["canvas_count"] > 0 for item in platform), platform)

    expected_export_counts = {
        "render_rb_long_12_plus_working": 26,
        "render_rb_recent6_plus_working": 20,
        "render_rb_working_local": 20,
    }
    export_hashes = {}
    for view_id, count in expected_export_counts.items():
        directory = run / "plot_view_data" / view_id
        manifest = json.loads((directory / "plot_view_data_manifest.json").read_text(encoding="utf-8"))
        check(f"plot_package.{view_id}.not_primary", manifest["not_primary_evidence"] is True, manifest["not_primary_evidence"])
        check(f"plot_package.{view_id}.export_count", len(manifest["exports"]) == count, {"expected": count, "actual": len(manifest["exports"])})
        for item in manifest["exports"]:
            path = directory / item["file"]
            actual_rows = len(raw(path))
            check(f"plot_package.{view_id}.{item['file']}.rows", actual_rows == item["rows"], {"expected": item["rows"], "actual": actual_rows})
            export_hashes[str(path.relative_to(run))] = sha256(path)

    long_dir = run / "plot_view_data/render_rb_long_12_plus_working"
    pairs = {
        "statistics": (
            projection / "rb_completed_window_statistics.csv",
            long_dir / "fixed__rb_long_12_plus_working__known__completed_statistics.csv",
            None,
        ),
        "working": (
            projection / "rb_working_values.csv",
            long_dir / "fixed__rb_long_12_plus_working__known__working_values.csv",
            None,
        ),
        "rhythm": (
            projection / "rb_working_rhythm.csv",
            long_dir / "fixed__rb_long_12_plus_working__known__working_rhythm.csv",
            None,
        ),
        "price": (
            projection / "rb_price_display.csv",
            long_dir / "fixed__rb_long_12_plus_working__known__rb_ohlc.csv",
            None,
        ),
    }
    for name, (source_path, export_path, _) in pairs.items():
        source_frame, export_frame = raw(source_path), raw(export_path)
        original_columns = list(source_frame.columns)
        check(f"raw_columns_preserved.{name}", all(column in export_frame.columns for column in original_columns), {"source_columns": original_columns, "export_columns": list(export_frame.columns)})
        check(f"raw_values_preserved.{name}", compare_raw(source_frame, export_frame, original_columns), {"source_rows": len(source_frame), "export_rows": len(export_frame)})
        check(f"source_hash_column.{name}", set(export_frame["_aidata_source_sha256"]) == {sources[name]["sha256"]}, sorted(set(export_frame["_aidata_source_sha256"])))

    paths_source = raw(projection / "rb_process_paths.csv")
    for group, rows in (("previous", 2339), ("recent", 2004), ("working", 429)):
        export_path = long_dir / f"fixed__rb_long_12_plus_working__known__{group}_actual_close_path.csv"
        exported = raw(export_path)
        expected = paths_source.loc[paths_source["group"] == group]
        original_columns = list(paths_source.columns)
        check(f"filtered_path.{group}.rows", len(exported) == rows == len(expected), {"expected": len(expected), "exported": len(exported)})
        check(f"filtered_path.{group}.raw_values", compare_raw(expected, exported, original_columns), {"columns": original_columns})
        check(f"filtered_path.{group}.plot_coordinates_present", (exported["_aidata_plot_x"] != "").all() and (exported["_aidata_plot_y"] != "").all(), "x/y nonempty")

    stats_export = raw(long_dir / "fixed__rb_long_12_plus_working__known__completed_statistics.csv")
    working_export = raw(long_dir / "fixed__rb_long_12_plus_working__known__working_values.csv")
    rhythm_export = raw(long_dir / "fixed__rb_long_12_plus_working__known__working_rhythm.csv")
    check("statistics_six_formal_rows", len(stats_export) == 6 and set(stats_export["finite_reference_checks_pass"]) == {"True"}, stats_export[["metric", "current", "previous", "change"]].to_dict("records"))
    check("working_pending_and_available", len(working_export) == 6 and set(working_export["completion_knownness_name"]) == {"Pending"} and set(working_export["knownness_name"]) == {"AvailableCommitted"}, working_export[["field", "value", "completion_knownness_name", "knownness_name"]].to_dict("records"))
    ratio = working_export.loc[working_export["field"] == "waiting_ratio", "value"]
    check("waiting_ratio_not_clipped", len(ratio) == 1 and float(ratio.iloc[0]) > 1, ratio.tolist())
    check("rhythm_reference_pass", len(rhythm_export) == 1 and rhythm_export.iloc[0]["reference_checks_pass"] == "True", rhythm_export.to_dict("records"))

    result = {
        "schema_version": 1,
        "result": "PASS" if all(item["pass"] for item in checks) else "FAIL",
        "purpose": "detect packaging/data-source failures independently from workflow/render success",
        "checks": checks,
        "failed_checks": [item for item in checks if not item["pass"]],
        "source_hashes": source_hashes,
        "plot_export_hashes": export_hashes,
        "boundaries": [
            "platform URL creation, HTTP opening, Bokeh serialization, browser pixels, visual inspection, and CSV equality are separate checks",
            "the package remains not_primary_evidence; professional interpretation returns to the issuing Pro",
        ],
    }
    output = run / "render_evidence/PACKAGE_VERIFICATION.json"
    output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"result": result["result"], "checks": len(checks), "failed": result["failed_checks"]}, ensure_ascii=False), flush=True)
    return 0 if result["result"] == "PASS" else 2


if __name__ == "__main__":
    raise SystemExit(main())
