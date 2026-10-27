"""核本次四窗正式切片，保留原文件副本与 Case/图/时间/确认字段对应。"""
from __future__ import annotations

import argparse
from collections import Counter
import csv
from datetime import datetime
from decimal import Decimal
import hashlib
import json
import math
from pathlib import Path
import shutil

FOLLOW_UP = {
    "CO01-C01": ("2021-04-06", "2021-04-06"),
    "CO01-C02": ("2021-10-08", "2021-10-14"),
    "CO01-C03": ("2022-06-13", "2022-06-23"),
    "CO01-C04": ("2023-10-10", "2023-10-11"),
}


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as stream:
        return list(csv.DictReader(stream))


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def finite(value: str) -> bool:
    try:
        return math.isfinite(float(value))
    except (TypeError, ValueError):
        return False


def valid_ohlc(row: dict) -> bool:
    return all(finite(row[key]) for key in ("open", "high", "low", "close")) and (
        float(row["low"]) <= min(float(row["open"]), float(row["close"]))
        <= max(float(row["open"]), float(row["close"])) <= float(row["high"]))


def equal_value(left: str, right: str) -> bool:
    if left == right:
        return True
    try:
        return Decimal(left) == Decimal(right)
    except Exception:
        return False


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("request", "run-dir", "daily-root", "page-record", "output-dir"):
        parser.add_argument("--" + name, type=Path, required=True)
    args = parser.parse_args()
    request = json.loads(args.request.read_text())
    run = args.run_dir.resolve()
    brief = json.loads((run / "run_brief.json").read_text())
    pages = json.loads(args.page_record.read_text())
    stats = read_csv(run / "manifest/feature_slice_stats.csv")
    spans = read_csv(run / "manifest/timespan_index.csv")
    by_label = {row["label"]: row for row in spans}
    assert brief["member_symbols"] == request["symbols"] == ["rb", "hc", "i"]
    assert len(spans) == 4 and all(row["level"] == "big" for row in spans)
    expected = {(by_label[case["case_id"]]["node_id"], symbol, feature)
                for case in request["cases"] for symbol in request["symbols"]
                for feature in ("kline_1d", "kline_30m", "scale_turn_mid")}
    assert Counter((row["node_id"], row["target_id"], row["feature_key"]) for row in stats) == Counter(expected)
    index = {(row["node_id"], row["target_id"], row["feature_key"]): row for row in stats}
    output = args.output_dir.resolve()
    output.mkdir(parents=True, exist_ok=True)
    copies = []

    def copy(source: Path) -> str:
        source = source.resolve()
        assert source.is_relative_to(run)
        relative = source.relative_to(run)
        destination = output / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        if destination.exists():
            assert destination.read_bytes() == source.read_bytes(), "Do not overwrite a differing original copy"
        else:
            shutil.copyfile(source, destination)
        assert source.read_bytes() == destination.read_bytes()
        copies.append({"source_absolute": str(source), "copy_relative": str(relative),
                       "bytes": source.stat().st_size, "sha256": digest(source)})
        return str(relative)

    daily_stats = read_csv(args.daily_root / "manifest/feature_slice_stats.csv")
    daily = {}
    for row in daily_stats:
        # FILE_INDEX defines the original server path to the actual Git copy.
        paths = json.loads((args.daily_root / "FILE_INDEX.json").read_text())["copied_files"]
        match = [item for item in paths if item["source_absolute"] == row["exported_file_path"]]
        assert len(match) == 1
        path = args.daily_root / match[0]["copy_relative"]
        assert digest(path) == match[0]["sha256"]
        daily[row["target_id"]] = {int(item["closeUti"]): item for item in read_csv(path)}

    report = {"run_id": brief["run_id"], "combined_node_id": pages["node_id"],
              "combined_url": pages["combined_url"], "cases": [], "critical_issues": [],
              "mid_field_source": "mquant/tis/frpExample/STCalendar.py: actual2D.x/y -> x/y; confirm2D.x/y -> xConfirm/yConfirm; value1/value2 concatenated without deleting rows",
              "limits": "确认坐标来自后端字段映射，不据字段名推断投资者当时可知；图数核对不证明研究解释。"}
    table = []
    for case in request["cases"]:
        case_id = case["case_id"]
        node = by_label[case_id]
        mapping = next(item for item in pages["case_mapping"] if item["case_id"] == case_id)
        entry = {"case_id": case_id, "node_id": node["node_id"], "manual_request": case["manual_request"],
                 "core_close_dates": case["core_close_dates"], "plotset_id": mapping["plotset_id"],
                 "plot_title": mapping["title"], "symbols": {}}
        raw_time_by_symbol = {}
        for symbol in request["symbols"]:
            symbol_report = {}
            data = {}
            for feature in ("kline_1d", "kline_30m", "scale_turn_mid"):
                stat = index[(node["node_id"], symbol, feature)]
                assert stat["slice_success"] == "True" and not stat["error_message"]
                source = Path(stat["exported_file_path"])
                assert source.stat().st_size == int(stat["exported_file_bytes"])
                values = read_csv(source)
                assert len(values) == int(stat["row_count"])
                data[feature] = values
                location = copy(source)
                item = {"feature_key": feature, "df_key_normalized": stat["df_key_normalized"],
                        "source": str(source), "copy_relative": location,
                        "sha256": digest(source), "bytes": source.stat().st_size,
                        "rows": len(values), "columns": list(values[0]) if values else [],
                        "time_field_used": stat["time_field_used"]}
                if feature.startswith("kline"):
                    valid = [row for row in values if valid_ohlc(row)]
                    times = [int(row["closeUti"]) for row in values]
                    assert times == sorted(set(times)), "Duplicate or unordered KLine closeUti"
                    item.update(valid_ohlc_rows=len(valid), invalid_ohlc_rows=len(values)-len(valid),
                                invalid_ohlc_close_times=[row["closeTs"] for row in values if not valid_ohlc(row)],
                                first_raw_times={key: values[0][key] for key in ("openUti", "closeUti", "openTs", "closeTs", "closeUti_ts")},
                                last_raw_times={key: values[-1][key] for key in ("openUti", "closeUti", "openTs", "closeTs", "closeUti_ts")},
                                closeTs_matches_exported_ts=all(row["closeTs"] == row["closeUti_ts"] for row in values))
                symbol_report[feature] = item
                table.append({"case_id": case_id, "node_id": node["node_id"], "symbol": symbol,
                              "feature_key": feature, "rows": len(values), "copy_relative": location,
                              "sha256": item["sha256"], "plotset_id": mapping["plotset_id"], "plot_title": mapping["title"]})
            kline = {int(row["closeUti"]): row for row in data["kline_30m"]}
            raw_time_by_symbol[symbol] = [(row["closeUti"], row["closeTs"]) for row in data["kline_30m"]]
            day_mismatches = []
            for row in data["kline_1d"]:
                old = daily[symbol].get(int(row["closeUti"]))
                if old is None:
                    day_mismatches.append({"time": row["closeTs"], "field": "source_row", "reason": "Not in W02"})
                else:
                    for field, value in row.items():
                        if field not in old or not equal_value(value, old[field]):
                            day_mismatches.append({"time": row["closeTs"], "field": field, "w02": old.get(field), "case_slice": value})
            symbol_report["kline_1d"]["w02_subset_mismatches"] = day_mismatches
            if day_mismatches:
                report["critical_issues"].append({"case_id": case_id, "symbol": symbol, "daily_subset_mismatches": day_mismatches})
            first_core = next(uti for uti, row in daily[symbol].items() if row["closeTs"][:10] == case["core_close_dates"][0])
            last_core = next(uti for uti, row in daily[symbol].items() if row["closeTs"][:10] == case["core_close_dates"][1])
            turn_rows = data["scale_turn_mid"]
            required_fields = {"x", "y", "xConfirm", "yConfirm", "x_ts", "xConfirm_ts"}
            assert not turn_rows or required_fields <= set(turn_rows[0])
            actual_points = [(int(row["x"]), row["y"]) for row in turn_rows if finite(row["x"]) and finite(row["y"])]
            start, end = map(datetime.fromisoformat, case["manual_request"])
            mid = symbol_report["scale_turn_mid"]
            mid.update(
                first_actual_time=min((row["x_ts"] for row in turn_rows), default=None),
                last_actual_time=max((row["x_ts"] for row in turn_rows), default=None),
                first_confirmation_time=min((row["xConfirm_ts"] for row in turn_rows), default=None),
                last_confirmation_time=max((row["xConfirm_ts"] for row in turn_rows), default=None),
                actual_points_outside_requested_window=[row for row in turn_rows if not start <= datetime.fromisoformat(row["x_ts"]) <= end],
                confirmations_outside_requested_window=sum(not start <= datetime.fromisoformat(row["xConfirm_ts"]) <= end for row in turn_rows),
                confirmation_before_actual=sum(int(row["xConfirm"]) < int(row["x"]) for row in turn_rows),
                duplicate_actual_point_rows=len(actual_points)-len(set(actual_points)),
                actual_points_before_core=sum(uti < first_core for uti, _ in actual_points),
                actual_points_between_daily_core_closes=sum(first_core <= uti <= last_core for uti, _ in actual_points),
                actual_points_after_core=sum(uti > last_core for uti, _ in actual_points),
                actual_points_with_formal_30m_close=sum(uti in kline and equal_value(value, kline[uti]["close"]) for uti, value in actual_points),
                actual_points_without_formal_30m_bar=[uti for uti, _ in actual_points if uti not in kline],
            )
            follow_start, follow_end = FOLLOW_UP[case_id]
            required_dates = sorted({row["closeTs"][:10] for row in daily[symbol].values()
                                     if follow_start <= row["closeTs"][:10] <= follow_end and valid_ohlc(row)})
            available_day = {row["closeTs"][:10] for row in data["kline_1d"] if valid_ohlc(row)}
            available_30m = {row["closeTs"][:10] for row in data["kline_30m"] if valid_ohlc(row)}
            follow = {"requested_follow_up_dates": list(FOLLOW_UP[case_id]),
                      "required_dates_from_original_W02_valid_calendar": required_dates,
                      "missing_from_1d": sorted(set(required_dates)-available_day),
                      "missing_from_30m": sorted(set(required_dates)-available_30m)}
            symbol_report["required_follow_up"] = follow
            if follow["missing_from_1d"] or follow["missing_from_30m"] or mid["actual_points_outside_requested_window"]:
                report["critical_issues"].append({"case_id": case_id, "symbol": symbol, "follow_up": follow, "mid_window_issue": bool(mid["actual_points_outside_requested_window"])})
            entry["symbols"][symbol] = symbol_report
        entry["three_symbol_30m_time_keys_equal"] = all(value == raw_time_by_symbol["rb"] for value in raw_time_by_symbol.values())
        if not entry["three_symbol_30m_time_keys_equal"]:
            report["critical_issues"].append({"case_id": case_id, "reason": "30m timestamp mismatch across symbols"})
        report["cases"].append(entry)
    for relative in ["run_brief.json", "manifest/run_summary.json", "manifest/timespan_index.csv",
                     "manifest/feature_slice_stats.csv", "manifest/chart_manifest.csv",
                     "delivery/DELIVERY_MANIFEST.json", "delivery/PACKAGE_INDEX.csv",
                     "review/big_world_chart_pages.csv"]:
        copy(run / relative)
    (output / "COVERAGE_AND_MID.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
    (output / "FILE_INDEX.json").write_text(json.dumps({"run_id": brief["run_id"], "copied_files": copies}, ensure_ascii=False, indent=2) + "\n")
    with (output / "CASE_FILE_PLOT_INDEX.csv").open("w", newline="", encoding="utf-8") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(table[0]), lineterminator="\n")
        writer.writeheader()
        writer.writerows(table)
    print(json.dumps({"run_id": brief["run_id"], "formal_slice_files": len(stats),
                      "copied_files": len(copies), "critical_issue_count": len(report["critical_issues"]),
                      "feature_rows": {key: sum(item["symbols"][symbol][key]["rows"] for item in report["cases"] for symbol in request["symbols"])
                                       for key in ["kline_1d", "kline_30m", "scale_turn_mid"]}}, ensure_ascii=False))


if __name__ == "__main__":
    main()
