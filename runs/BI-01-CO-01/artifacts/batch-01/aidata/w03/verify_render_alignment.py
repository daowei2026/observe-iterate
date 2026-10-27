"""将真实浏览器 Bokeh 数据与正式 CSV 全量比较；不调用或重取行情。"""
from __future__ import annotations

import argparse
from collections import Counter
import csv
import hashlib
import json
import math
from pathlib import Path


def rows(path):
    with path.open(newline="", encoding="utf-8") as stream:
        return list(csv.DictReader(stream))


def number(value):
    if value in (None, ""):
        return None
    parsed = float(value)
    # CSV 空行情在 Bokeh 中保持 NaN；两种缺失编码相同，不填成价格。
    return None if math.isnan(parsed) else parsed


def same(actual, expected):
    left, right = number(actual), number(expected)
    if left is None or right is None:
        return left is None and right is None
    return math.isclose(left, right, rel_tol=1e-12, abs_tol=1e-12)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for arg in ["capture", "case-delivery", "daily-root", "output"]:
        parser.add_argument("--" + arg, type=Path, required=True)
    args = parser.parse_args()
    capture = json.loads(args.capture.read_text())
    assert capture["http_status"] == 200 and not capture.get("failure")
    assert not capture["page_errors"] and not capture["failed_requests"]
    documents = capture["documents"]
    figures = [(doc, fig) for doc in documents for fig in doc["figures"]]
    assert len(figures) == 5
    coverage = json.loads((args.case_delivery / "COVERAGE_AND_MID.json").read_text())
    cases = {case["case_id"]: case for case in coverage["cases"]}
    daily_index = json.loads((args.daily_root / "FILE_INDEX.json").read_text())["copied_files"]
    checked = []
    for doc, fig in figures:
        overview = fig["title"].startswith("全局概览")
        case_id = None if overview else fig["title"].split(" / ")[0]
        source_by_label = {}
        renderers = fig["renderers"]
        assert len(renderers) == (9 if overview else 12)
        assert all(renderer["visible"] for renderer in renderers)
        for renderer in renderers:
            label = renderer["legend"]["value"]
            source_by_label.setdefault(label, set()).add(renderer["source_id"])
        assert len(source_by_label) == (3 if overview else 6)
        figure_result = {"title": fig["title"], "browser_figure_id": fig["id"],
                         "x_range": fig["x_range"], "symbols": {}}
        for symbol in ["rb", "hc", "i"]:
            if overview:
                matches = [item for item in daily_index if f"/symbol/{symbol}/kline_1d/" in item["copy_relative"]]
                assert len(matches) == 1
                path = args.daily_root / matches[0]["copy_relative"]
                expected_hash = matches[0]["sha256"]
            else:
                item = cases[case_id]["symbols"][symbol]["kline_30m"]
                path = args.case_delivery / item["copy_relative"]
                expected_hash = item["sha256"]
            assert hashlib.sha256(path.read_bytes()).hexdigest() == expected_hash
            assert len(source_by_label[symbol + " - K"]) == 1
            source_id = next(iter(source_by_label[symbol + " - K"]))
            source = doc["sources"][source_id]["data"]
            formal = rows(path)
            assert len(source["x"]) == len(formal)
            base = next(float(value) for value in source["__prestd_open"] if value is not None)
            max_ratio_error = 0.0
            for index, row in enumerate(formal):
                assert source["x"][index] == (int(row["openUti"]) + int(row["closeUti"])) / 2
                assert source["ts"][index] == row["closeTs"][:16]
                assert same(source["volume"][index], row["volume"])
                for field in ["open", "high", "low", "close"]:
                    assert same(source["__prestd_" + field][index], row[field]), (case_id, symbol, index, field)
                    expected = number(row[field])
                    expected = None if expected is None else expected / base
                    assert same(source[field][index], expected), (case_id, symbol, index, field, "ratio")
                    if expected is not None:
                        max_ratio_error = max(max_ratio_error, abs(source[field][index] - expected))
            result = {"formal_csv": str(path), "formal_sha256": expected_hash,
                      "kline_rows_checked": len(formal), "kline_source_id": source_id,
                      "missing_ohlc_rows_preserved": sum(any(number(row[field]) is None for field in ["open", "high", "low", "close"]) for row in formal),
                      "raw_ohlc_and_volume_equal": True, "x_equals_open_close_uti_midpoint": True,
                      "label_ts_equals_formal_close_minute": True, "ratio_base_open": base,
                      "ratio_max_abs_error": max_ratio_error,
                      "ratio_rule_source": "uplot/utlv2.py KPriceLine base_y=open; uplot/dynstd.js ratio uses first finite open in current viewport, driven mid uses same base"}
            if not overview:
                item = cases[case_id]["symbols"][symbol]["scale_turn_mid"]
                mid_path = args.case_delivery / item["copy_relative"]
                assert hashlib.sha256(mid_path.read_bytes()).hexdigest() == item["sha256"]
                formal_mid = rows(mid_path)
                label = symbol + " - 贴近转折（M，mid参数）"
                assert len(source_by_label[label]) == 1
                mid_id = next(iter(source_by_label[label]))
                mid = doc["sources"][mid_id]["data"]
                assert len(mid["x"]) == len(formal_mid)
                original = Counter((float(row["x"]), float(row["y"])) for row in formal_mid)
                rendered = Counter(zip(mid["x"], mid["__prestd_y"]))
                assert original == rendered, (case_id, symbol, "mid original points")
                assert all(same(y, raw / base) for y, raw in zip(mid["y"], mid["__prestd_y"]))
                labels = Counter((float(row["x"]), row["x_ts"][:16]) for row in formal_mid)
                assert Counter(zip(mid["x"], mid["ts"])) == labels
                result.update(mid_rows_checked=len(formal_mid), mid_source_id=mid_id,
                              mid_actual_xy_multiset_equal=True, mid_ratio_matches_kline_base=True,
                              mid_confirmation_not_plotted=True, mid_formal_csv=str(mid_path))
            figure_result["symbols"][symbol] = result
        checked.append(figure_result)
    result = {"url": capture["url"], "node_id": capture["node_id"],
              "browser_started_at": capture["started_at"], "browser_ended_at": capture["ended_at"],
              "capture_sha256": hashlib.sha256(args.capture.read_bytes()).hexdigest(),
              "figure_count": len(checked), "figures": checked,
              "status": "PASS", "scope": "实际浏览器首开全范围的图内全量原值和坐标对应；不替代专业解释、Pro或Owner看图"}
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"status": result["status"], "figure_count": len(checked),
                      "kline_rows": sum(s["kline_rows_checked"] for f in checked for s in f["symbols"].values()),
                      "mid_rows": sum(s.get("mid_rows_checked", 0) for f in checked for s in f["symbols"].values())}, ensure_ascii=False))


if __name__ == "__main__":
    main()
