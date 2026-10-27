"""真实打开 W03 原生统一页并保存整页、各图及渲染数据核对证据。"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import json
from pathlib import Path
import time

from playwright.sync_api import sync_playwright


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--page-record", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()
    record = json.loads(args.page_record.read_text())
    assert not args.output_dir.exists(), "Preserve each actual browser attempt"
    args.output_dir.mkdir(parents=True)
    result = {"url": record["combined_url"], "node_id": record["node_id"],
              "operator": "Worker Codex / existing headless Chromium",
              "started_at": datetime.now(timezone.utc).isoformat(),
              "page_errors": [], "failed_requests": [], "screenshots": []}
    try:
        with sync_playwright() as engine:
            browser = engine.chromium.launch(headless=True, args=["--no-sandbox"])
            page = browser.new_page(viewport={"width": 2600, "height": 1100}, device_scale_factor=1)
            page.on("pageerror", lambda error: result["page_errors"].append(str(error)[:1500]))
            page.on("requestfailed", lambda request: result["failed_requests"].append(
                {"url": request.url.split("?")[0], "failure": request.failure}))
            response = page.goto(result["url"], wait_until="domcontentloaded", timeout=45000)
            result["http_status"] = response.status if response else None
            page.wait_for_function("""() => {
                const docs=window.Bokeh?.documents||[];
                return docs.some(d=>Array.from(d._all_models.values())
                    .filter(m=>m.type==='Figure'||m.type==='Plot').length===5);
            }""", timeout=60000)
            deadline = time.monotonic() + 30
            while page.locator("canvas").count() < 10 and time.monotonic() < deadline:
                page.wait_for_timeout(500)
            page.wait_for_timeout(1500)
            result["title"] = page.title()
            result["canvas_count"] = page.locator("canvas").count()
            result["documents"] = page.evaluate("""() => {
                function plain(v) {
                    if (v==null || typeof v!=='object') return v;
                    if (Array.isArray(v)||ArrayBuffer.isView(v)||typeof v.length==='number') return Array.from(v).map(plain);
                    if (v.id) return {model_id:v.id,type:v.type};
                    return Object.fromEntries(Object.entries(v).map(([k,x])=>[k,plain(x)]));
                }
                return (window.Bokeh?.documents||[]).map(doc=>{
                    const models=Array.from(doc._all_models.values());
                    const legendByRenderer={};
                    for (const item of models.filter(m=>m.type==='LegendItem'))
                        for (const renderer of item.renderers||[]) legendByRenderer[renderer.id]=plain(item.label);
                    const sources={};
                    const figures=models.filter(m=>m.type==='Figure'||m.type==='Plot').map(plot=>({
                        id:plot.id,title:plot.title?.text,width:plot.width,height:plot.height,
                        x_range:{start:plot.x_range?.start,end:plot.x_range?.end},
                        renderers:plot.renderers.filter(r=>r.type==='GlyphRenderer').map(r=>{
                            const source=r.data_source;
                            if (source&&!sources[source.id]) sources[source.id]={id:source.id,data:plain(source.data)};
                            const glyph=r.glyph, fields={};
                            for(const key of ['x','y','x0','x1','y0','y1','top','bottom','left','right','width','height','marker','size','line_color','fill_color'])
                                if(glyph[key]!==undefined) fields[key]=plain(glyph[key]);
                            return {id:r.id,name:r.name,visible:r.visible,glyph_type:glyph.type,glyph_fields:fields,
                                source_id:source?.id,legend:legendByRenderer[r.id]||null};
                        })
                    }));
                    return {title:doc.title,figures,sources};
                });
            }""")
            figures = [figure for doc in result["documents"] for figure in doc["figures"]]
            assert len(figures) == 5 and result["canvas_count"] >= 10
            titles = [figure["title"] for figure in figures]
            for case in record["case_mapping"]:
                assert sum(all(token in title for token in [case["case_id"], "30m", "mid"]) for title in titles) == 1
            page.screenshot(path=str(args.output_dir / "whole_page.png"), full_page=True)
            result["screenshots"].append(str(args.output_dir / "whole_page.png"))
            # 每图有主 canvas 和交互 overlay canvas；保留每个主画布的真实截图。
            for index in range(5):
                path = args.output_dir / f"figure_{index+1:02d}.png"
                page.locator("canvas").nth(index * 2).screenshot(path=str(path))
                result["screenshots"].append(str(path))
            browser.close()
    except Exception as error:
        result["failure"] = {"type": type(error).__name__, "message": str(error)[:3000]}
    result["ended_at"] = datetime.now(timezone.utc).isoformat()
    (args.output_dir / "BROWSER_CAPTURE.json").write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    summary = {key: result.get(key) for key in ["url", "http_status", "canvas_count", "page_errors", "failure"]}
    summary["figures"] = [{"title": f["title"], "renderers": len(f["renderers"])}
                          for d in result.get("documents", []) for f in d["figures"]]
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    if "failure" in result:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
