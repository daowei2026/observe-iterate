#!/usr/bin/env python3
"""Rerender only the three selected-cut pages after the R8 endpoint fix."""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess

from mquant.quant import OptContext


CUTS = {
    "before_confirmation": 103150800,
    "at_or_after_confirmation": 103151400,
    "final": 103315800,
}
SOF = "TA_updto20240229_DBA"
CALENDAR = "night_end_at_2300"
COLOR = "#4C78A8"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def load_resume_module(script: Path):
    spec = importlib.util.spec_from_file_location("worker02_resume_for_endpoint_r8_render", script)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {script}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def git_value(repo: Path, *args: str) -> str:
    return subprocess.check_output(
        ["git", "-C", str(repo), *args], text=True, stderr=subprocess.STDOUT
    ).strip()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, required=True)
    parser.add_argument("--aidata-repo", type=Path, required=True)
    args = parser.parse_args()
    root = args.root.resolve()
    resume = load_resume_module(root / "scripts" / "resume_render_from_exports.py")
    price = resume.load_price(root / "data" / "same_bound_price" / "rb_5m_price_calendar.csv")
    context = OptContext(sof_name=SOF)
    pages = []
    for label, selected_k in CUTS.items():
        frames = resume.load_formal_tables(root / "data" / "selected_cuts" / label)
        bundle = resume.build_selected_cut_bundle(
            frames,
            price,
            symbol="rb",
            color=COLOR,
            as_of=selected_k,
            optional_panels=("duration", "rhythm"),
        )
        page_id = f"rb_selected_{label}_K{selected_k}"
        pages.append(resume.render(bundle, context, root, page_id))

    aidata_commit = git_value(args.aidata_repo.resolve(), "rev-parse", "HEAD")
    payload = {
        "schema_version": 1,
        "order_id": "BI01-FO01-N-DISPLAY-INTEGRATION-02",
        "supplement_marker": "BI01-FO01-WORKER-DISPLAY02-ENDPOINT-R8-20261022",
        "result": "PASS" if all(page["validation"]["result"] == "PASS" for page in pages) else "FAIL",
        "scope": "render only three selected-cut pages from existing hashed formal exports; no normal N reread and no evolution rerender",
        "aidata_commit": aidata_commit,
        "pages": pages,
    }
    output = root / "evidence" / "ENDPOINT_R8_RERENDER.json"
    output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    runtime_path = root / "evidence" / "RUNTIME_AND_RENDER_MANIFEST.json"
    runtime = json.loads(runtime_path.read_text(encoding="utf-8"))
    replacements = {page["page_id"]: page for page in pages}
    runtime["pages"] = [replacements.get(page["page_id"], page) for page in runtime["pages"]]
    runtime["endpoint_r8_supplement"] = {
        "result": payload["result"],
        "marker": payload["supplement_marker"],
        "aidata_commit": aidata_commit,
        "formal_n_reread": False,
        "evolution_page_rerendered": False,
        "selected_pages_rerendered": list(replacements),
        "pre_fix_audit": "evidence/ENDPOINT_R8_PRE_FIX_HTML_AUDIT.json",
        "direct_check": "evidence/ENDPOINT_R8_DIRECT_CHECK.json",
        "rerender_evidence": str(output.relative_to(root)),
    }
    runtime_path.write_text(json.dumps(runtime, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "result": payload["result"],
        "pages": len(pages),
        "output": str(output),
        "sha256": sha256(output),
        "runtime_manifest_sha256": sha256(runtime_path),
    }, ensure_ascii=False), flush=True)
    return 0 if payload["result"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
