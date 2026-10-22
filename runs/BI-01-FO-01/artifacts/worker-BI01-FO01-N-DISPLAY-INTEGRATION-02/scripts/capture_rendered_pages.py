#!/usr/bin/env python3
"""Open the four generated N display pages and capture real browser pixels."""

from __future__ import annotations

import argparse
import hashlib
import http.server
import json
import threading
from functools import partial
from pathlib import Path

from playwright.sync_api import sync_playwright


EXPECTED = {
    "rb_evolution_actual_occurrences",
    "rb_selected_before_confirmation_K103150800",
    "rb_selected_at_or_after_confirmation_K103151400",
    "rb_selected_final_K103315800",
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        return


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-root", type=Path, required=True)
    args = parser.parse_args()
    root = args.output_root.resolve()
    evidence = root / "render_evidence"
    pages = {path.stem: path for path in evidence.glob("*.html")}
    if set(pages) != EXPECTED:
        raise RuntimeError(f"unexpected rendered pages: {sorted(pages)}")

    handler = partial(QuietHandler, directory=str(evidence))
    server = http.server.ThreadingHTTPServer(("127.0.0.1", 0), handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    results = []
    try:
        with sync_playwright() as playwright:
            chromium = next(
                Path("/home/dw/.cache/ms-playwright").glob("chromium-*/chrome-linux64/chrome"),
                Path("/snap/bin/chromium"),
            )
            browser = playwright.chromium.launch(
                executable_path=str(chromium), headless=True, args=["--no-sandbox"]
            )
            page = browser.new_page(viewport={"width": 1800, "height": 1200}, device_scale_factor=1)
            for page_id in sorted(pages):
                response = page.goto(
                    f"http://127.0.0.1:{server.server_port}/{pages[page_id].name}",
                    wait_until="load",
                    timeout=60_000,
                )
                page.wait_for_timeout(2500)
                body = page.locator("body").inner_text()
                browser_models = page.evaluate("""() => {
                    const docs = (window.Bokeh && Bokeh.documents) || []
                    if (!docs.length) return {documents: 0, evidence: 0, groups: [], plots: 0, badge_text: ''}
                    const models = [...docs[0]._all_models.values()]
                    const evidence = models.filter(m => Array.isArray(m.tags) && m.tags.includes('aidata_evidence'))
                    const groups = [...new Set(evidence.flatMap(m => m.tags.filter(t => typeof t === 'string' && t.startsWith('group:'))))].sort()
                    const plots = models.filter(m => Array.isArray(m.renderers) && m.x_range && m.y_range)
                    const badge_text = models.filter(m => m.type === 'Div').map(m => m.text || '').join(' ')
                    return {documents: docs.length, evidence: evidence.length, groups, plots: plots.length, badge_text}
                }""")
                screenshot = evidence / f"{page_id}.png"
                page.screenshot(path=str(screenshot), full_page=True)
                checks = {
                    "http_200": response is not None and response.ok,
                    "title": page.title() == f"BI01 FO01 {page_id}",
                    "badge_has_rb": "rb" in browser_models["badge_text"],
                    "badge_has_history_basis": "同bar close" in browser_models["badge_text"],
                    "badge_has_gap_notice": "缺件/错误提示" in browser_models["badge_text"],
                    "canvas_present": page.locator("canvas").count() > 0,
                    "six_plots": browser_models["plots"] == 6,
                    "evidence_models_present": browser_models["evidence"] > 0,
                    "all_panel_groups_present": set(browser_models["groups"]) == {
                        "group:price", "group:completed_efficiency", "group:working_motion",
                        "group:working_efficiency", "group:duration", "group:rhythm",
                    },
                    "screenshot_nonempty": screenshot.stat().st_size > 50_000,
                }
                results.append({
                    "page_id": page_id,
                    "url_scope": "ephemeral localhost",
                    "http_status": None if response is None else response.status,
                    "browser_models": browser_models,
                    "canvas_count": page.locator("canvas").count(),
                    "screenshot": {
                        "path": str(screenshot.relative_to(root)),
                        "bytes": screenshot.stat().st_size,
                        "sha256": sha256(screenshot),
                        "width": page.evaluate("document.documentElement.scrollWidth"),
                        "height": page.evaluate("document.documentElement.scrollHeight"),
                    },
                    "checks": checks,
                    "result": "PASS" if all(checks.values()) else "FAIL",
                })
            browser.close()
    finally:
        server.shutdown()
        server.server_close()
        thread.join(timeout=5)

    summary = {
        "schema_version": 1,
        "result": "PASS" if all(item["result"] == "PASS" for item in results) else "FAIL",
        "local_server_scope": "ephemeral localhost only; stopped before report write",
        "results": results,
        "distinction": "HTML generation, browser opening, Bokeh model presence, screenshot capture and Worker visual inspection are separate facts",
    }
    output = evidence / "BROWSER_CAPTURE.json"
    output.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"result": summary["result"], "pages": len(results), "output": str(output)}, ensure_ascii=False), flush=True)
    return 0 if summary["result"] == "PASS" else 2


if __name__ == "__main__":
    raise SystemExit(main())
