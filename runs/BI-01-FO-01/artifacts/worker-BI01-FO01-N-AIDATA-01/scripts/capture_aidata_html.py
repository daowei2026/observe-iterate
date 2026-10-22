#!/usr/bin/env python3
"""Open generated aidata HTML through localhost and capture real browser pixels."""

from __future__ import annotations

import argparse
import contextlib
import hashlib
import http.server
import json
import threading
from functools import partial
from pathlib import Path

import pandas as pd
from playwright.sync_api import sync_playwright


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        return


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run-dir", type=Path, required=True)
    args = parser.parse_args()
    run_dir = args.run_dir.resolve()
    evidence = run_dir / "render_evidence"
    html_paths = sorted(evidence.glob("*.html"))
    if len(html_paths) != 3:
        raise RuntimeError(f"expected three local HTML files, got {len(html_paths)}")

    handler = partial(QuietHandler, directory=str(evidence))
    server = http.server.ThreadingHTTPServer(("127.0.0.1", 0), handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    results = []
    try:
        with sync_playwright() as playwright:
            chromium = next(Path("/home/dw/.cache/ms-playwright").glob("chromium-*/chrome-linux64/chrome"), Path("/snap/bin/chromium"))
            browser = playwright.chromium.launch(executable_path=str(chromium), headless=True, args=["--no-sandbox"])
            page = browser.new_page(viewport={"width": 1600, "height": 1000}, device_scale_factor=1)
            for html_path in html_paths:
                url = f"http://127.0.0.1:{server.server_port}/{html_path.name}"
                response = page.goto(url, wait_until="load")
                page.wait_for_timeout(2500)
                title = page.title()
                body = page.locator("body").inner_text()
                canvases = page.locator("canvas").count()
                screenshot = evidence / f"{html_path.stem}.png"
                page.screenshot(path=str(screenshot), full_page=True)
                local_pass = response is not None and response.ok and canvases > 0
                results.append({
                    "kind": "local_standalone_html", "node_id": html_path.stem,
                    "http_status": None if response is None else response.status,
                    "title": title, "body_has_asof": "As-Of" in body,
                    "body_has_rb": "rb" in body, "canvas_count": canvases,
                    "screenshot": {"path": str(screenshot.relative_to(run_dir)), "bytes": screenshot.stat().st_size, "sha256": sha256(screenshot)},
                    "result": "PASS" if local_pass else "FAIL",
                    "note": "Bokeh canvas text is not required to appear in ordinary DOM innerText; title/canvas/pixels are checked separately",
                })
                for table_id in ("working_values", "working_rhythm"):
                    selected = page.evaluate("""table_id => {
                        const doc = Bokeh.documents[0]
                        const selectors = [...doc._all_models.values()].filter(model =>
                            model.type === 'Select' && Array.isArray(model.tags) &&
                            model.tags.some(tag => tag === 'aidata_fixed_layer_selector') &&
                            model.tags.some(tag => typeof tag === 'object' && tag.scope === 'known'))
                        const selector = selectors[0]
                        if (selector == null || !selector.options.some(option => option[0] === table_id)) return false
                        selector.value = table_id
                        return true
                    }""", table_id)
                    if selected:
                        page.wait_for_timeout(500)
                        table_image = evidence / f"{html_path.stem}_{table_id}.png"
                        page.screenshot(path=str(table_image), full_page=True)
                        results.append({
                            "kind": "local_table_selection", "node_id": html_path.stem,
                            "table_id": table_id, "selection_mechanism": "Bokeh Select model tagged aidata_fixed_layer_selector / known",
                            "screenshot": {"path": str(table_image.relative_to(run_dir)), "bytes": table_image.stat().st_size, "sha256": sha256(table_image)},
                            "result": "PASS",
                        })
                    if not selected:
                        results.append({"kind": "local_table_selection", "node_id": html_path.stem, "table_id": table_id, "result": "FAIL", "error": "table selector option not found"})

            pages_path = run_dir / "review/fixed_chart_pages.csv"
            if pages_path.exists():
                for item in pd.read_csv(pages_path).to_dict("records"):
                    try:
                        response = page.goto(str(item["report_url"]), wait_until="domcontentloaded", timeout=30000)
                        page.wait_for_timeout(3000)
                        screenshot = evidence / f"platform_{item['node_id']}.png"
                        page.screenshot(path=str(screenshot), full_page=True)
                        results.append({
                            "kind": "platform_report_url", "node_id": item["node_id"],
                            "report_url": item["report_url"],
                            "http_status": None if response is None else response.status,
                            "title": page.title(), "canvas_count": page.locator("canvas").count(),
                            "screenshot": {"path": str(screenshot.relative_to(run_dir)), "bytes": screenshot.stat().st_size, "sha256": sha256(screenshot)},
                            "result": "PASS" if response is not None and response.ok else "FAIL",
                        })
                    except Exception as exc:
                        results.append({"kind": "platform_report_url", "node_id": item["node_id"], "report_url": item["report_url"], "result": "FAIL", "error_type": type(exc).__name__, "error": str(exc)})
            browser.close()
    finally:
        server.shutdown()
        server.server_close()
        thread.join(timeout=5)

    local_results = [item for item in results if item["kind"] == "local_standalone_html"]
    table_results = [item for item in results if item["kind"] == "local_table_selection"]
    summary = {
        "schema_version": 1,
        "result": "PASS" if all(item["result"] == "PASS" for item in local_results + table_results) else "FAIL",
        "local_server_scope": "ephemeral localhost only; stopped before report write",
        "results": results,
        "distinction": "local standalone HTML pixel capture and platform report URL opening are recorded separately",
    }
    output = evidence / "BROWSER_CAPTURE.json"
    output.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False), flush=True)
    return 0 if summary["result"] == "PASS" else 2


if __name__ == "__main__":
    raise SystemExit(main())
