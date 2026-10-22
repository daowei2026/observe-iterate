#!/usr/bin/env python3
"""不重读正式大表，验证 W03 包装、渲染、跨K和版本对齐。"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

EXPECTED_PAGES = {
    "rb_evolution_actual_occurrences",
    "rb_selected_before_confirmation_K103150800",
    "rb_selected_at_or_after_confirmation_K103151400",
    "rb_selected_final_K103315800",
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


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

    json_errors = []
    for path in sorted(root.rglob("*.json")):
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except Exception as exc:
            json_errors.append({"path": str(path.relative_to(root)), "error": str(exc)})
    check("all JSON parses", not json_errors, {"count": len(list(root.rglob('*.json'))), "errors": json_errors})

    professional = root.parents[1] / "artifacts/professional-R0009/u2_normal_node_behavior.py"
    check(
        "professional v0.2.1 configuration exact bytes",
        sha256(args.aidata_config.resolve()) == sha256(professional)
        == "39275fa22a564649d9092a9a28f30a7e018c27d3673212f18a9bc05ebd964641",
    )

    alignment = json.loads((root / "evidence/RUNTIME_COMMIT_ALIGNMENT.json").read_text())
    check(
        "runtime bytes aligned to published aidata commit",
        alignment["result"] == "PASS"
        and alignment["aidata"]["result_commit"] == args.aidata_commit
        and alignment["aidata"]["github_fresh_sha"] == args.aidata_commit,
        alignment["aidata"],
    )
    check(
        "protected dependencies remained read-only",
        alignment["protected_dependencies"]["protected_source_modified"] is False,
        alignment["protected_dependencies"],
    )

    tests = json.loads((root / "evidence/TEST_RESULTS.json").read_text())
    check(
        "aidata targeted and full tests passed",
        tests["result"] == "PASS" and [item["passed"] for item in tests["runs"]] == [34, 61],
        tests["runs"],
    )

    render = json.loads((root / "evidence/RENDER_MANIFEST.json").read_text())
    identity = json.loads((root / "evidence/THREE_K_AND_IDENTITY_CHECK.json").read_text())
    browser = json.loads((root / "render_evidence/BROWSER_CAPTURE.json").read_text())
    visual = json.loads((root / "render_evidence/WORKER_VISUAL_INSPECTION.json").read_text())
    page_ids = {item["page_id"] for item in render["pages"]}
    check("four expected pages", render["result"] == "PASS" and page_ids == EXPECTED_PAGES, sorted(page_ids))
    check("three-K and display identity checks", identity["result"] == "PASS" and all(identity["checks"].values()), identity["checks"])
    check("real browser capture", browser["result"] == "PASS" and len(browser["results"]) == 4)
    check("Worker final pixel inspection", visual["result"] == "PASS" and len(visual["pages"]) == 4)

    for page_id in sorted(EXPECTED_PAGES):
        html = root / f"render_evidence/{page_id}.html"
        png = root / f"render_evidence/{page_id}.png"
        validation = json.loads((root / f"render_evidence/{page_id}.validation.json").read_text())
        browser_page = next(item for item in browser["results"] if item["page_id"] == page_id)
        visual_page = visual["pages"][page_id]
        check(
            f"{page_id} HTML/PNG/model/range/pixel",
            html.stat().st_size > 100_000 and png.stat().st_size > 50_000
            and validation["result"] == "PASS"
            and browser_page["result"] == "PASS"
            and browser_page["screenshot"]["sha256"] == sha256(png)
            and visual_page["sha256"] == sha256(png),
            {"html_sha256": sha256(html), "png_sha256": sha256(png), "checks": validation["checks"]},
        )
        view_manifest = json.loads(
            (root / f"plot_view_data/{page_id}/plot_view_data_manifest.json").read_text()
        )
        bad = []
        for item in view_manifest["files"].values():
            path = root / f"plot_view_data/{page_id}" / item["file"]
            if not path.is_file() or sha256(path) != item["sha256"]:
                bad.append(item["file"])
        check(f"{page_id} plot_view_data hashes", not bad, {"files": len(view_manifest["files"]), "bad": bad})

    synthetic = json.loads((root / "evidence/SYNTHETIC_DISPLAY_PROBES.json").read_text())
    check("zero/null/waiting>1 display probes", synthetic["result"] == "PASS" and all(synthetic["checks"].values()), synthetic["checks"])

    crossk = json.loads((root / "evidence/CROSSK_READ_MANIFEST.json").read_text())
    expected_cases = {"i_before_missing_recovery", "i_recovery", "i_after_recovery", "hc_final"}
    check(
        "four normal OnlyRead cross-K cases",
        crossk["result"] == "PASS" and set(crossk["cases"]) == expected_cases
        and len(crossk["products"]) == 19,
        {"cases": sorted(crossk["cases"]), "products": len(crossk["products"])},
    )
    bad_crossk = []
    for case, files in crossk["exports"].items():
        for product, item in files.items():
            path = Path(item["path"])
            if not path.is_file():
                path = root / "data/crossk" / case / Path(item["path"]).name
            if not path.is_file() or sha256(path) != item["sha256"]:
                bad_crossk.append(f"{case}/{product}")
    check("cross-K exported table hashes", not bad_crossk, bad_crossk)

    summary = json.loads((root / "evidence/CROSSK_SUMMARY.json").read_text())
    i = summary["i"]
    hc = summary["hc"]
    check(
        "i recovery is partial and preserves true zero",
        [item["resolved_as_of"] for item in i["resolved_occurrences"]] == [35360400, 35361000, 35361600]
        and i["same_working_life"] is True
        and i["recovery_scalars"]["working_waiting"]["value"] == 0.0
        and i["recovery_scalars"]["working_efficiency"]["present"] == 0
        and i["after_scalars"]["working_waiting"]["value"] == 600.0,
        i["conclusion_boundary"],
    )
    check(
        "hc denominator comes from formal intervals/rhythm",
        hc["recent_three_intervals"] == [2400.0, 600.0, 600.0]
        and hc["recent_three_median"] == 600.0
        and hc["denominator_matches_formal_current_median"] is True
        and hc["waiting_ratio"]["value"] == 430.0,
        hc["qualification"],
    )
    direction = json.loads((root / "evidence/DIRECTION_SOURCE_CHECK.json").read_text())
    check("formal down direction mapping retained", direction["result"] == "PASS" and all(direction["checks"].values()), direction["formal_member"])

    result = {
        "schema_version": 1,
        "result": "PASS" if all(item["result"] == "PASS" for item in checks) else "FAIL",
        "aidata_commit": args.aidata_commit,
        "checks": checks,
        "summary": {
            "check_count": len(checks),
            "pass_count": sum(item["result"] == "PASS" for item in checks),
            "fail_count": sum(item["result"] == "FAIL" for item in checks),
        },
        "boundary": "验证的是技术读回、显示、包装和版本事实，不是专业市场解释或管理接受。",
    }
    output = root / "evidence/FINAL_VERIFICATION.json"
    output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({**result["summary"], "result": result["result"], "output": str(output)}, ensure_ascii=False))
    return 0 if result["result"] == "PASS" else 2


if __name__ == "__main__":
    raise SystemExit(main())
