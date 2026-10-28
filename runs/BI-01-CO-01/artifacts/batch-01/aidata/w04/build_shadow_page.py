"""W04：只复用冻结 W03 原生五图及范围，建立可正常恢复阴影的页面。"""
from __future__ import annotations

import argparse
import csv
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import subprocess
from urllib.parse import urlsplit


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, required=True)
    parser.add_argument("--run-dir", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--defer-layout", action="store_true", help="只保存持久参数；正常平台layout另行实际核验，不据此宣布显示通过")
    args = parser.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    result_file = args.output_dir / "SHADOW_PAGE.json"
    if result_file.exists():
        raise FileExistsError("W04 output already has a page receipt: inspect it; do not return the old W03 page as a new build")
    started = datetime.now(timezone.utc).isoformat()
    source_index = args.run_dir / "manifest/timespan_index.csv"
    repo_index = args.repo_root / "runs/BI-01-CO-01/artifacts/batch-01/aidata/delivery/bi01_co01_w03_cases_20261028_5e4fa62eaf/manifest/timespan_index.csv"
    assert source_index.read_bytes() == repo_index.read_bytes()
    assert subprocess.check_output(["git", "-C", str(args.repo_root), "hash-object", str(repo_index)], text=True).strip() == "809bd1aa9a07b12f57dea5f96f2689e0fcc83868"
    rows = list(csv.DictReader(source_index.open(newline="")))
    assert [row["label"] for row in rows] == [f"CO01-C{n:02d}" for n in range(1, 5)]
    assert all(row["level"] == "big" for row in rows)
    frozen = [{**row, "scope_label": row["label"] + " / " + row["node_id"]} for row in rows]

    from mquant.aidata.profiles import ensure_profile_runtime
    from mquant.aidata.big_world_chart import AidataRunOverviewCAE, _review_window_bounds, _main_review_figures
    from mquant.aidata.feature_slicer import plotctx_uti_window
    from mquant.frame import TestCAE1, eval2
    from mquant.quant.models.graph import CaeNodeDao
    from bokeh.models import BoxAnnotation, Label, Toggle
    import pandas as pd

    ensure_profile_runtime()
    if not CaeNodeDao.is_exits(cls_name="AidataRunOverviewCAE"):
        raise PermissionError("W04 requires the existing class registration; no new registration is authorized")
    old = CaeNodeDao.fqueryById(node_id="6148")
    original = CaeNodeDao.fqueryById(node_id="6142")
    assert isinstance(old, TestCAE1) and isinstance(original, AidataRunOverviewCAE)
    before_fason = old.fason
    config = old.P.name
    source_plotsets = old.doShowCAEGraph().P.plotsets
    assert list(source_plotsets.P) == ["overview", "case_CO01_C01", "case_CO01_C02", "case_CO01_C03", "case_CO01_C04"]
    context, calendar = original.P.context, original.P.calendar_name
    assert calendar == "night_end_at_2300" and original.P.blk == "blk@steel"
    assert config["Context"].fason == context.fason
    coordinates = []
    tsa = None if args.defer_layout else context.sof.tsa_of(calendar)["natural_tsa"]
    for row in ([] if args.defer_layout else frozen):
        series = pd.Series(row)
        left, right = _review_window_bounds(series, context=context, calendar_name=calendar)
        window = plotctx_uti_window(row["start_uti"], row["end_uti"], {"context": context, "calendar_name": calendar})
        assert left < right and (left, right) == (window[0], window[1] - 1)
        coordinates.append({"case_id": row["label"], "node_id": row["node_id"],
                            "original_start_uti_field": row["start_uti"], "original_end_uti_field": row["end_uti"],
                            "label": row["scope_label"], "slice_half_open_uti": list(window),
                            "box_left": left, "box_right": right,
                            "left_natural_tsa": str(pd.to_datetime(tsa[int(left)])),
                            "right_natural_tsa": str(pd.to_datetime(tsa[int(right)])),
                            "conversion": "aidata.feature_slicer.plotctx_uti_window; right=stop-1; underlying uplot.timesearch; no day added"})
    params = {"run_dir": str(args.run_dir), "run_id": "bi01_co01_w03_cases_20261028_5e4fa62eaf",
              "context": context, "calendar_name": calendar, "blk": original.P.blk,
              "overview_start": original.P.overview_start, "overview_end": original.P.overview_end,
              "combined_graph_config": config, "overview_scope_rows_json": json.dumps(frozen, ensure_ascii=False)}
    page = AidataRunOverviewCAE(params)
    restored = eval2(page.fason)
    assert restored.P.combined_graph_config["plotsets"].fason == source_plotsets.fason
    # 真正执行该持久对象的正常 layout；不在业务脚本中事后注入 annotation。
    figures, boxes, labels = [], [], []
    if not args.defer_layout:
        layout = restored.doShowCAEGraph().layout()
        figures = _main_review_figures(layout)
        assert len(figures) == 5
        overview = next(fig for fig in figures if fig.title.text.startswith("全局概览 "))
        boxes = [model for model in overview.center if isinstance(model, BoxAnnotation)]
        labels = [model for model in overview.center if isinstance(model, Label)]
        assert [(box.left, box.right) for box in boxes] == [(item["box_left"], item["box_right"]) for item in coordinates]
        assert {label.text for label in labels} == {item["label"] for item in coordinates}
        assert all(not any(isinstance(model, BoxAnnotation) for model in fig.center) for fig in figures if fig is not overview)
        assert len(list(layout.select(type=Toggle))) == 1
    assert old.fason == before_fason
    (args.output_dir / "native_page.fason.txt").write_text(page.fason)
    (args.output_dir / "RANGE_COORDINATES.json").write_text(json.dumps(coordinates, ensure_ascii=False, indent=2) + "\n")
    created = CaeNodeDao.createUniqueWithFao(tar=page)
    node_id = str(created["node"]["id"])
    host = urlsplit(created["report_url"]).hostname
    result = {"worker_execution_id": "BI01-CO-01-W04-worker-ac26d5b83e", "started_at": started,
              "ended_at": datetime.now(timezone.utc).isoformat(), "node_id": node_id,
              "url": f"http://{host}:5006/cae?node_id={node_id}", "report_url": created["report_url"],
              "old_node_id": "6148", "old_url": "http://192.168.11.40:5006/cae?node_id=6148",
              "page_class": "AidataRunOverviewCAE", "new_class_registration": False,
              "run_id_reused": params["run_id"], "run_dir_reused": str(args.run_dir),
              "source_index_sha256": sha(source_index), "source_index_git_blob": "809bd1aa9a07b12f57dea5f96f2689e0fcc83868",
              "source_node_fason_sha256": hashlib.sha256(before_fason.encode()).hexdigest(),
              "plotsets_fason_sha256": hashlib.sha256(source_plotsets.fason.encode()).hexdigest(),
              "native_page_fason_sha256": sha(args.output_dir / "native_page.fason.txt"),
              "normal_eval2_layout_figures": [fig.title.text for fig in figures],
              "normal_layout_scope_count": None if args.defer_layout else len(boxes),
              "local_layout_executed": not args.defer_layout, "expected_frozen_scopes": frozen,
              "scope_labels": [label.text for label in labels],
              "coordinates": coordinates, "limits": "建页及本地正常eval2/layout已核；实际服务重开/像素/缩放/显隐/故事另记，未重启服务或重取行情。"}
    result_file.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"node_id": node_id, "url": result["url"], "normal_layout_figures": len(figures), "scope_count": len(boxes)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
