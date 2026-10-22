#!/usr/bin/env python3
"""Verify the BI01 N display delivery without rerunning the formal product."""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path

import pandas as pd


EXPECTED_PAGES = {
    "rb_evolution_actual_occurrences",
    "rb_selected_before_confirmation_K103150800",
    "rb_selected_at_or_after_confirmation_K103151400",
    "rb_selected_final_K103315800",
}
CUTS = {
    "rb_selected_before_confirmation_K103150800": 103150800,
    "rb_selected_at_or_after_confirmation_K103151400": 103151400,
    "rb_selected_final_K103315800": 103315800,
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def module_from(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, required=True)
    parser.add_argument("--aidata-config", type=Path, required=True)
    parser.add_argument("--aidata-commit", required=True)
    args = parser.parse_args()
    root = args.root.resolve()
    checks = []

    def check(name: str, passed: bool, evidence=None):
        checks.append({"name": name, "result": "PASS" if passed else "FAIL", "evidence": evidence})

    json_files = sorted(root.rglob("*.json"))
    json_errors = []
    for path in json_files:
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except Exception as exc:
            json_errors.append({"path": str(path.relative_to(root)), "error": str(exc)})
    check("all JSON parses", not json_errors, {"count": len(json_files), "errors": json_errors})

    professional = module_from(root / "inputs" / "professional_u2_normal_node_behavior.py", "professional_r0007_config")
    adopted = module_from(args.aidata_config.resolve(), "adopted_aidata_config")
    comparisons = {
        "CONFIG_VERSION": adopted.CONFIG_VERSION == professional.CONFIG_VERSION,
        "PANELS": adopted.PANELS == professional.PANELS,
        "TIME_POLICY": adopted.TIME_POLICY == professional.TIME_POLICY,
        "VIEW_RULES": adopted.VIEW_RULES == professional.VIEW_RULES,
        "configs": adopted.configs() == professional.configs(),
        "evolution": adopted.display_config(symbol="rb", color="#4C78A8", mode="evolution", optional_panels=("duration", "rhythm")) == professional.display_config(symbol="rb", color="#4C78A8", mode="evolution", optional_panels=("duration", "rhythm")),
        "selected_cut": adopted.display_config(symbol="rb", color="#4C78A8", mode="selected_cut", optional_panels=("duration", "rhythm")) == professional.display_config(symbol="rb", color="#4C78A8", mode="selected_cut", optional_panels=("duration", "rhythm")),
    }
    check("R0007 configuration semantic equality", all(comparisons.values()), comparisons)

    runtime = json.loads((root / "evidence" / "RUNTIME_AND_RENDER_MANIFEST.json").read_text(encoding="utf-8"))
    browser = json.loads((root / "render_evidence" / "BROWSER_CAPTURE.json").read_text(encoding="utf-8"))
    visual = json.loads((root / "render_evidence" / "WORKER_VISUAL_INSPECTION.json").read_text(encoding="utf-8"))
    check("runtime/render manifest PASS", runtime["result"] == "PASS")
    check("browser capture PASS", browser["result"] == "PASS" and len(browser["results"]) == 4)
    check("Worker visual inspection PASS", visual["result"] == "PASS" and len(visual["pages"]) == 4)
    scalar_consistency = json.loads(
        (root / "evidence" / "SCALAR_DISPLAY_CONSISTENCY_CHECK.json").read_text(encoding="utf-8")
    )
    check(
        "saved scalar HTML/CDS matches projections and formal tables",
        scalar_consistency["result"] == "PASS"
        and scalar_consistency["old_sequential_reuse_pattern_reproduced"] is True
        and scalar_consistency["all_current_pages_pass"] is True,
        {
            "old_reuse_reproduced": scalar_consistency["old_sequential_reuse_pattern_reproduced"],
            "current_page_results": {
                page["label"]: page["result"] for page in scalar_consistency["pages"]
            },
        },
    )
    page_ids = {page["page_id"] for page in runtime["pages"]}
    check("four expected pages", page_ids == EXPECTED_PAGES, sorted(page_ids))

    for page_id in sorted(EXPECTED_PAGES):
        html = root / "render_evidence" / f"{page_id}.html"
        png = root / "render_evidence" / f"{page_id}.png"
        validation = json.loads((root / "render_evidence" / f"{page_id}.validation.json").read_text(encoding="utf-8"))
        check(f"{page_id} HTML/PNG/runtime validation", html.stat().st_size > 100_000 and png.stat().st_size > 50_000 and validation["result"] == "PASS", {
            "html_sha256": sha256(html), "png_sha256": sha256(png), "validation": validation["checks"],
        })
        manifest = json.loads((root / "plot_view_data" / page_id / "plot_view_data_manifest.json").read_text(encoding="utf-8"))
        bad_hashes = []
        for item in manifest["files"].values():
            path = root / "plot_view_data" / page_id / item["file"]
            if sha256(path) != item["sha256"]:
                bad_hashes.append(item["file"])
        check(f"{page_id} plot_view_data hashes", not bad_hashes, {"files": len(manifest["files"]), "bad": bad_hashes})
        if page_id in CUTS:
            k = CUTS[page_id]
            after = []
            for path in (root / "plot_view_data" / page_id).glob("n_display__*.csv"):
                frame = pd.read_csv(path)
                for column in ("x", "x0", "x1"):
                    if column in frame and len(frame) and pd.to_numeric(frame[column]).max() > k:
                        after.append({"file": path.name, "column": column})
            check(f"{page_id} contains no geometry after K", not after, after)

    i_context = json.loads((root / "data" / "i_missing_context" / "I_MISSING_CONTEXT.json").read_text(encoding="utf-8"))
    runs = i_context["missing_close_runs"]
    check("i nullable-close recovery preserved", i_context["missing_close_rows"] == 24 and len(runs) == 1 and runs[0]["recovery_open_uti"] == 35361000 and runs[0]["recovery_close"] == 572.0, runs)

    check("aidata commit recorded", len(args.aidata_commit) == 40, args.aidata_commit)
    summary = {
        "schema_version": 1,
        "result": "PASS" if all(item["result"] == "PASS" for item in checks) else "FAIL",
        "aidata_commit": args.aidata_commit,
        "checks": checks,
        "summary": {
            "check_count": len(checks),
            "pass_count": sum(item["result"] == "PASS" for item in checks),
            "fail_count": sum(item["result"] == "FAIL" for item in checks),
        },
        "boundary": "This verifies transport/render/package facts, not professional market interpretation or management acceptance",
    }
    output = root / "evidence" / "FINAL_VERIFICATION.json"
    output.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary["summary"] | {"result": summary["result"], "output": str(output)}, ensure_ascii=False), flush=True)
    return 0 if summary["result"] == "PASS" else 2


if __name__ == "__main__":
    raise SystemExit(main())
