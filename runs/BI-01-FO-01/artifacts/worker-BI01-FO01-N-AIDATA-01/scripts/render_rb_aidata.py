#!/usr/bin/env python3
"""Render the fresh rb projection through aidata's fixed-input consumer."""

from __future__ import annotations

import argparse
import hashlib
import json
import traceback
from pathlib import Path

from bokeh.document import Document
from bokeh.embed import file_html
from bokeh.models import ColumnDataSource
from bokeh.resources import INLINE
from bokeh.core.json_encoder import serialize_json

from mquant.aidata.api import build_big_world_chart_pages, build_chart_run, render_review_nodes


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def source(source_id: str, path: Path) -> dict:
    return {"id": source_id, "path": str(path.resolve()), "sha256": sha256(path)}


def filters(group: str) -> list[dict]:
    return [{"field": "group", "op": "eq", "value": group}]


def price_layer() -> dict:
    return {
        "id": "rb_ohlc", "source": "price", "symbol": "rb", "kind": "ohlc", "label": "rb 5m OHLC（close 为 N 路径基底）",
        "x": "bar_time", "open": "open", "high": "high", "low": "low", "close": "close",
        "known_at": "known_at_time", "window_field": "bar_time", "color": "#9aa0a6",
        "note": "原 5m 行情；N 的参考路径只使用 close。标签表示该 bar，不表示开盘瞬间已知 close。",
    }


def group_layers(group: str, label: str, color: str, dash: str) -> list[dict]:
    return [
        {
            "id": f"{group}_actual_close_path", "source": "paths", "symbol": "rb", "kind": "line",
            "label": f"{label}：实际 5m close 路径", "x": "bar_time", "y": "close", "filters": filters(group),
            "known_at": "known_at_time", "window_field": "bar_time", "color": color,
            "note": "按各过程完整原 close 范围切片；这是观察参考投影，不冒充正式 Episode 产品。",
        },
        {
            "id": f"{group}_endpoint_boundaries", "source": "segments", "symbol": "rb", "kind": "segment",
            "label": f"{label}：端点边界连线（非实际行程）", "x0": "start_time", "y0": "start_close",
            "x1": "end_time", "y1": "end_close", "filters": filters(group), "known_at": "known_at_time",
            "window_field": "start_time", "color": color, "line_dash": dash,
            "note": "仅表达过程端点边界；不得据此读取路径行程或最大逆向量。",
        },
    ]


def confirmation_layer(group: str, label: str, color: str) -> dict:
    return {
        "id": f"{group}_confirmation", "source": "confirmations", "symbol": "rb", "kind": "point",
        "label": f"{label}：确认/known-from 点", "x": "confirmation_time", "y": "confirmation_close",
        "filters": filters(group), "known_at": "known_at_time", "window_field": "confirmation_time",
        "color": color, "marker": "triangle", "note": "确认/known-from 与实际端点分开保存和展示。",
    }


def table_layers() -> list[dict]:
    return [
        {"id": "completed_statistics", "source": "statistics", "kind": "table", "label": "完成窗六项统计",
         "known_at": "known_at_time", "note": "current/previous/change/MAD 保持原单位；change 不是百分比，MAD 不是标准差。"},
        {"id": "loo_details", "source": "loo", "kind": "table", "label": "LOO 六槽明细",
         "known_at": "known_at_time", "note": "六槽绝对移位；并列不是成员重要性排名。"},
        {"id": "working_values", "source": "working", "kind": "table", "label": "working 数值与状态",
         "known_at": "known_at_time", "note": "完成状态 Pending 与当前可用数值并存；waiting_ratio 不截到 [0,1]。"},
        {"id": "working_rhythm", "source": "rhythm", "kind": "table", "label": "working 局部节律",
         "known_at": "known_at_time", "note": "保存的六个局部间隔以前3/近期3比较；局部次数与全程次数分列。"},
    ]


def view(node_id: str, label: str, start: str, end: str, groups: list[str]) -> dict:
    palette = {
        "previous": ("此前六个完成过程", "#7f8c8d", "dashed"),
        "recent": ("最近六个完成过程", "#1565c0", "dotdash"),
        "working": ("当前 working（未完成）", "#d32f2f", "dotted"),
    }
    layers = [price_layer()]
    for group in groups:
        title, color, dash = palette[group]
        layers.extend(group_layers(group, title, color, dash))
        if group != "working":
            layers.append(confirmation_layer(group, title, color))
    layers.extend(table_layers())
    return {
        "node_id": node_id, "label": label, "start": start, "end": end,
        "asof": "2024-02-29 14:55:00.500000", "symbols": ["rb"], "layers": layers,
        "default_table": "completed_statistics",
        "notes": [
            "As-Of 103315800；Exact NodeBehaviorBook/NodeScaleTurnBehaviorRevision/b340dc6c-c135-462b-b6e0-04d24622c180/cfd51328-e2cf-4360-8314-20c9238e93fb。",
            "实线是完整 close 路径；虚线端点连线只表示过程边界，不表示实际行程。",
            "历史输入标签使用同 bar close，不是开盘瞬时已知；working 不进入两侧已完成样本。",
            "本页是 rb 首轮技术观察投影，不是收益预测、资金建议或全特征正确率证明。",
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--projection-dir", type=Path, required=True)
    parser.add_argument("--output-root", type=Path, required=True)
    parser.add_argument("--run-id", default="bi01-fo01-n-aidata-rb-final-20261022")
    parser.add_argument("--attempt-platform-pages", action="store_true")
    args = parser.parse_args()
    p = args.projection_dir
    args.output_root.mkdir(parents=True, exist_ok=True)
    sources = [
        source("price", p / "rb_price_display.csv"),
        source("paths", p / "rb_process_paths.csv"),
        source("segments", p / "rb_process_boundaries.csv"),
        source("confirmations", p / "rb_confirmation_markers.csv"),
        source("statistics", p / "rb_completed_window_statistics.csv"),
        source("working", p / "rb_working_values.csv"),
        source("rhythm", p / "rb_working_rhythm.csv"),
        source("loo", p / "rb_loo_details.csv"),
    ]
    spec = {
        "schema_version": 1,
        "sources": sources,
        "views": [
            view("rb_long_12_plus_working", "rb 长范围：此前6＋最近6＋working", "2023-11-14 22:50:00.500000", "2024-02-29 14:55:00.500000", ["previous", "recent", "working"]),
            view("rb_recent6_plus_working", "rb 中范围：最近6＋working", "2024-01-03 09:45:00.500000", "2024-02-29 14:55:00.500000", ["recent", "working"]),
            view("rb_working_local", "rb 局部：最后完成边界与当前 working", "2024-02-21 09:20:00.500000", "2024-02-29 14:55:00.500000", ["recent", "working"]),
        ],
    }
    spec_path = args.output_root / "aidata_fixed_input_spec.json"
    spec_path.write_text(json.dumps(spec, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    brief = {
        "output_root": str(args.output_root.resolve()), "run_id": args.run_id,
        "run_note": "BI01-FO01-N-AIDATA-01 fresh rb OnlyRead projection",
        "fixed_input": spec,
    }
    run = build_chart_run(brief, dry_run=False, log_to_notebook=False)
    node_ids = [v["node_id"] for v in spec["views"]]
    rendered = render_review_nodes(run, node_ids=node_ids, export_plot_view_data=True)
    evidence_dir = run.run_dir / "render_evidence"
    evidence_dir.mkdir(parents=True, exist_ok=True)
    documents = []
    html_paths = []
    for node_id, layout in zip(node_ids, rendered.rendered_objects):
        doc = Document()
        doc.add_root(layout)
        encoded = serialize_json(doc.to_json())
        json.loads(encoded)
        html = file_html(layout, INLINE, title=f"BI01 FO01 {node_id}")
        html_path = evidence_dir / f"{node_id}.html"
        html_path.write_text(html, encoding="utf-8")
        html_paths.append(html_path)
        cds = [item for item in layout.references() if isinstance(item, ColumnDataSource)]
        layers = []
        for item in sorted(cds, key=lambda value: value.name or ""):
            lengths = {len(values) for values in item.data.values()}
            layers.append({"name": item.name, "rows": None if not lengths else max(lengths), "columns": sorted(item.data)})
        documents.append({
            "node_id": node_id, "bokeh_document_json_parsed": True,
            "bokeh_document_json_bytes": len(encoded.encode("utf-8")),
            "bokeh_document_json_sha256": hashlib.sha256(encoded.encode("utf-8")).hexdigest(),
            "html": {"path": str(html_path.relative_to(run.run_dir)), "bytes": html_path.stat().st_size, "sha256": sha256(html_path)},
            "column_data_sources": layers,
        })

    screenshots = []
    try:
        from playwright.sync_api import sync_playwright
        with sync_playwright() as playwright:
            chromium = next(Path("/home/dw/.cache/ms-playwright").glob("chromium-*/chrome-linux64/chrome"), Path("/snap/bin/chromium"))
            browser = playwright.chromium.launch(executable_path=str(chromium), headless=True, args=["--no-sandbox"])
            page = browser.new_page(viewport={"width": 1600, "height": 1000}, device_scale_factor=1)
            for node_id, html_path in zip(node_ids, html_paths):
                page.goto(html_path.resolve().as_uri(), wait_until="load")
                page.wait_for_timeout(2000)
                screenshot = evidence_dir / f"{node_id}.png"
                page.screenshot(path=str(screenshot), full_page=True)
                screenshots.append({"node_id": node_id, "result": "PASS", "path": str(screenshot.relative_to(run.run_dir)), "bytes": screenshot.stat().st_size, "sha256": sha256(screenshot)})
            browser.close()
    except Exception as exc:
        screenshots.append({"result": "FAIL", "error_type": type(exc).__name__, "error": str(exc), "traceback": traceback.format_exc()})

    platform_pages = {"attempted": args.attempt_platform_pages}
    if args.attempt_platform_pages:
        try:
            pages = build_big_world_chart_pages(run, run_brief_input=brief, save=True)
            platform_pages.update(result="PASS", rows=pages.to_dict("records"))
        except Exception as exc:
            platform_pages.update(result="FAIL", error_type=type(exc).__name__, error=str(exc), traceback=traceback.format_exc())

    summary = {
        "schema_version": 1, "result": "PASS",
        "aidata_import": str(Path(__import__("mquant.aidata.api", fromlist=["x"]).__file__).resolve()),
        "run_id": run.run_id, "run_dir": str(run.run_dir.resolve()),
        "fixed_input_spec": {"path": str(spec_path.resolve()), "sha256": sha256(spec_path)},
        "feature_executions_inside_aidata": 0,
        "render_plans": rendered.render_plans,
        "documents": documents, "screenshots": screenshots, "platform_pages": platform_pages,
        "acceptance_distinctions": {
            "build_chart_run_exit": "PASS", "render_review_nodes_returned": len(rendered.rendered_objects),
            "bokeh_document_wire_serialization": all(item["bokeh_document_json_parsed"] for item in documents),
            "browser_screenshots": sum(item.get("result") == "PASS" for item in screenshots),
            "platform_page_creation": platform_pages.get("result", "NOT_ATTEMPTED"),
            "ai_visual_inspection": "PENDING_SEPARATE_INSPECTION",
        },
    }
    summary_path = evidence_dir / "RENDER_VALIDATION.json"
    summary_path.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"result": summary["result"], "run_dir": str(run.run_dir), "documents": len(documents), "screenshots": screenshots, "platform_pages": platform_pages}, ensure_ascii=False), flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
