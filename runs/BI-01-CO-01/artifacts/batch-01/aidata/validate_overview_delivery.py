"""只核本次 aidata 正式交付并复制原文件；不取数、不选例、不改行情。"""
from __future__ import annotations

import argparse
import csv
from datetime import datetime
import hashlib
import json
import math
from pathlib import Path
import shutil


def rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as stream:
        return list(csv.DictReader(stream))


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def finite(value: str) -> bool:
    try:
        return math.isfinite(float(value))
    except (TypeError, ValueError):
        return False


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run-dir", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()
    run = args.run_dir.resolve()
    output = args.output_dir.resolve()
    brief = json.loads((run / "run_brief.json").read_text())
    run_id = brief["run_id"]
    stats = rows(run / "manifest/feature_slice_stats.csv")
    spans = rows(run / "manifest/timespan_index.csv")
    expected = {"rb", "hc", "i"}
    assert set(brief["member_symbols"]) == expected, "Unexpected actual members"
    assert len(stats) == 3 and {row["target_id"] for row in stats} == expected
    output.mkdir(parents=True, exist_ok=True)
    copied = []

    def copy(source: Path) -> Path:
        source = source.resolve()
        assert source.is_relative_to(run), "Source outside this formal run"
        relative = source.relative_to(run)
        target = output / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        if target.exists():
            assert target.read_bytes() == source.read_bytes(), "Existing copy differs"
        else:
            shutil.copyfile(source, target)
        assert sha(source) == sha(target)
        copied.append({"source_absolute": str(source), "copy_relative": str(relative),
                       "bytes": source.stat().st_size, "sha256": sha(source)})
        return target

    report = {"run_id": run_id, "run_dir": str(run), "members": brief["member_symbols"],
              "valid_ohlc_definition": "all OHLC finite and low <= open,close <= high",
              "timestamp_basis": "original closeUti and aidata-exported closeUti_ts; no timezone/epoch guessing",
              "symbols": {}, "calendar_gap_classification": "observed calendar intervals, not proof of missing trading sessions"}
    valid_times = {}
    raw_times = {}
    natural_times = {}
    long_gaps = []
    for stat in stats:
        symbol = stat["target_id"]
        assert stat["run_id"] == run_id and stat["feature_key"] == "kline_1d"
        assert stat["level"] == "big" and stat["time_field_used"] == "closeUti"
        assert stat["slice_success"] == "True" and not stat["error_message"]
        assert any(span["node_id"] == stat["node_id"] for span in spans)
        source = Path(stat["exported_file_path"])
        assert source.stat().st_size == int(stat["exported_file_bytes"])
        data = rows(source)
        assert len(data) == int(stat["row_count"]) and data
        fields = list(data[0])
        assert {"open", "high", "low", "close", "openUti", "closeUti", "openTs", "closeTs", "closeUti_ts"} <= set(fields)
        times = [int(row["closeUti"]) for row in data]
        assert times == sorted(times) and len(set(times)) == len(times), "Unsorted or duplicate closeUti"
        valid, missing, bad_bounds = [], [], []
        for row in data:
            if not all(finite(row[key]) for key in ("open", "high", "low", "close")):
                missing.append(row["closeUti"])
            elif not (float(row["low"]) <= min(float(row["open"]), float(row["close"]))
                      <= max(float(row["open"]), float(row["close"])) <= float(row["high"])):
                bad_bounds.append(row["closeUti"])
            else:
                valid.append(row)
        raw_times[symbol] = set(times)
        valid_times[symbol] = {int(row["closeUti"]) for row in valid}
        stamp_by_uti = {int(row["closeUti"]): row["closeUti_ts"] for row in data}
        natural_times[symbol] = stamp_by_uti
        for previous, following in zip(times, times[1:]):
            start = datetime.fromisoformat(stamp_by_uti[previous])
            end = datetime.fromisoformat(stamp_by_uti[following])
            days = (end - start).total_seconds() / 86400
            if days > 3:
                long_gaps.append({"symbol": symbol, "previous_close": start.isoformat(sep=" "),
                                  "next_close": end.isoformat(sep=" "), "calendar_days": days})
        timestamp_fields = [key for key in fields if key.endswith("Ts") or key.endswith("_ts")]
        report["symbols"][symbol] = {
            "node_id": stat["node_id"], "feature_key": stat["feature_key"],
            "df_key_normalized": stat["df_key_normalized"], "source": str(source),
            "copy_relative": str(copy(source).relative_to(output)), "sha256": sha(source),
            "bytes": source.stat().st_size, "total_rows": len(data), "valid_ohlc_rows": len(valid),
            "missing_ohlc_rows": len(missing), "invalid_ohlc_bounds_rows": len(bad_bounds),
            "missing_ohlc_close_utis": missing, "invalid_bounds_close_utis": bad_bounds,
            "missing_ohlc_time_rows": [{key: row[key] for key in ["openUti", "closeUti", "openTs", "closeTs", "closeUti_ts", "volume"]}
                                        for row in data if row["closeUti"] in missing],
            "columns": fields, "missing_by_column": {key: sum(not row[key].strip() or row[key].strip().lower() in {"nan", "null", "none"} for row in data) for key in fields},
            "first_raw_times": {key: data[0][key] for key in ["openUti", "closeUti", *timestamp_fields]},
            "last_raw_times": {key: data[-1][key] for key in ["openUti", "closeUti", *timestamp_fields]},
            "first_valid_close": valid[0]["closeUti_ts"] if valid else None,
            "last_valid_close": valid[-1]["closeUti_ts"] if valid else None,
            "closeTs_equals_closeUti_ts_rows": sum(row["closeTs"] == row["closeUti_ts"] for row in data),
            "timestamp_offsets_present": sorted({str(datetime.fromisoformat(row["closeUti_ts"]).tzinfo) for row in data}),
        }
    common = set.intersection(*valid_times.values())
    union = set.union(*raw_times.values())
    timestamp_lookup = {int(row["closeUti"]): row["closeUti_ts"] for row in rows(Path(stats[0]["exported_file_path"]))}
    mismatches = [uti for uti in set.intersection(*raw_times.values())
                  if len({natural_times[symbol][uti] for symbol in expected}) != 1]
    assert not mismatches, "Same closeUti maps to different natural times across symbols"
    segments = []
    current = []
    for uti in sorted(union):
        if uti in common:
            current.append(uti)
        elif current:
            segments.append(current)
            current = []
    if current:
        segments.append(current)
    report["common"] = {"valid_close_uti_count": len(common), "union_close_uti_count": len(union),
                        "first_valid_close_uti": min(common) if common else None,
                        "last_valid_close_uti": max(common) if common else None,
                        "first_valid_close": timestamp_lookup[min(common)] if common else None,
                        "last_valid_close": timestamp_lookup[max(common)] if common else None,
                        "cross_symbol_time_mapping_mismatches": mismatches,
                        "valid_segments_on_observed_index": [{"first_close": timestamp_lookup[part[0]],
                            "last_close": timestamp_lookup[part[-1]], "rows": len(part)} for part in segments],
                        "missing_from_union_by_symbol": {symbol: sorted(union - raw_times[symbol]) for symbol in expected},
                        "noncommon_valid_rows_by_symbol": {symbol: sorted(valid_times[symbol] - common) for symbol in expected}}
    for name in ["run_brief.json", "manifest/run_summary.json", "manifest/feature_slice_stats.csv",
                 "manifest/timespan_index.csv", "manifest/chart_manifest.csv",
                 "delivery/DELIVERY_MANIFEST.json", "delivery/PACKAGE_INDEX.csv",
                 "review/run_overview_chart_page.csv", "review/run_overview_chart_page.md"]:
        copy(run / name)
    (output / "COVERAGE.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
    (output / "FILE_INDEX.json").write_text(json.dumps({"run_id": run_id, "copied_files": copied}, ensure_ascii=False, indent=2) + "\n")
    with (output / "LONG_GAPS.csv").open("w", newline="", encoding="utf-8") as stream:
        writer = csv.DictWriter(stream, fieldnames=["symbol", "previous_close", "next_close", "calendar_days"], lineterminator="\n")
        writer.writeheader()
        writer.writerows(long_gaps)
    print(json.dumps({"run_id": run_id, "symbols": {key: {name: value[name] for name in ["total_rows", "valid_ohlc_rows", "missing_ohlc_rows", "invalid_ohlc_bounds_rows"]} for key, value in report["symbols"].items()},
                      "common": report["common"], "long_gap_rows": len(long_gaps), "copied_files": len(copied)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
