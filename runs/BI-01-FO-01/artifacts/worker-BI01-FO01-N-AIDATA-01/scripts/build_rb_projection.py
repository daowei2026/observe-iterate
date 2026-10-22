#!/usr/bin/env python3
"""Build the rb display projection and finite reference verification.

The projection never changes the saved N product.  It joins the returned
addresses, slices the original close/Calendar rows at exact member coordinates,
and labels every recalculated value as a display/reference value.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path

import numpy as np
import pandas as pd


KNOWNNESS = {
    0: "AvailableCommitted", 1: "ValidEmpty", 2: "Pending",
    3: "InsufficientHistory", 4: "DataUnavailable",
    5: "MissingExpectedArtifact", 6: "UnobservableUnderCurrentBinding",
    7: "UnsupportedByCurrentBinding", 8: "Conflict",
    9: "RetractedOrInvalidated",
}
APPLICABILITY = {0: "Applicable", 1: "NotApplicableZeroPathLength", 2: "NotApplicable", 3: "ApplicabilityPending"}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def clean(value):
    if isinstance(value, dict):
        return {str(k): clean(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [clean(v) for v in value]
    if isinstance(value, np.generic):
        return clean(value.item())
    if value is pd.NA or (isinstance(value, float) and math.isnan(value)):
        return None
    if isinstance(value, (pd.Timestamp, Path)):
        return str(value)
    return value


def write_json(path: Path, value) -> None:
    path.write_text(json.dumps(clean(value), ensure_ascii=False, indent=2, allow_nan=False) + "\n", encoding="utf-8")


def frame(path: Path) -> pd.DataFrame:
    return pd.read_csv(path)


def one(table: pd.DataFrame, name: str) -> pd.Series:
    if len(table) != 1:
        raise RuntimeError(f"expected exactly one {name} row, got {len(table)}")
    return table.iloc[0]


def median(values):
    ordered = sorted(float(v) for v in values)
    n = len(ordered)
    return ordered[n // 2] if n % 2 else ordered[n // 2 - 1] / 2 + ordered[n // 2] / 2


def primitive(part: pd.DataFrame, direction: int) -> dict:
    prices = part["close"].to_numpy(dtype=float)
    clocks = part["calendar_time"].to_numpy(dtype=float)
    positions = part["calendar_position"].to_numpy(dtype=np.int64)
    finite = bool(np.isfinite(prices).all())
    contiguous = bool(np.all(np.diff(positions) == 1))
    endpoint = bool(np.isfinite(prices[[0, -1]]).all())
    sign = 1 if direction == 0 else -1
    progress = float(sign * (prices[-1] - prices[0])) if endpoint else None
    amplitude = abs(float(prices[-1] - prices[0])) if endpoint else None
    travel = float(np.abs(np.diff(prices)).sum()) if finite and contiguous else None
    efficiency = None if travel in (None, 0) or amplitude is None else amplitude / travel
    counter = None
    if finite and contiguous:
        best = 0.0
        burden = 0.0
        for price in prices:
            q = sign * (float(price) - float(prices[0]))
            best = max(best, q)
            burden = max(burden, best - q)
        counter = burden
    return {
        "BusinessDuration": float(clocks[-1] - clocks[0]),
        "CanonicalPathLength": travel,
        "DirectionalProgress": progress,
        "PathEfficiency": efficiency,
        "RawAmplitude": amplitude,
        "RawCounterMove": counter,
        "sample_count": len(part),
        "nonfinite_close_count": int((~np.isfinite(prices)).sum()),
        "calendar_contiguous": contiguous,
    }


def rhythm_reference(part: pd.DataFrame, direction: int) -> dict:
    prices = part["close"].to_numpy(dtype=float)
    clocks = part["calendar_time"].to_numpy(dtype=float)
    uti = part["open_uti"].to_numpy(dtype=np.int64)
    positions = part["calendar_position"].to_numpy(dtype=np.int64)
    extreme = last = local_start = None
    local_count = 0
    full_count = 0
    intervals = []
    previous_good = False
    for j, (price, clock, at, position) in enumerate(zip(prices, clocks, uti, positions)):
        good = bool(np.isfinite(price))
        linked = j > 0 and position == positions[j - 1] + 1 and previous_good and good
        if not good:
            extreme = last = local_start = None
            local_count = 0
            full_count = None
            intervals = []
        elif j == 0 or not linked or extreme is None:
            extreme = float(price)
            last = None
            local_start = (int(at), float(clock))
            local_count = 0
            intervals = []
            if j > 0:
                full_count = None
        elif price > extreme if direction == 0 else price < extreme:
            if last is not None:
                intervals = (intervals + [float(clock) - last[1]])[-6:]
            extreme = float(price)
            local_count += 1
            if full_count is not None:
                full_count += 1
            last = (int(at), float(clock))
        previous_good = good
    base = last if last is not None else local_start
    waiting = None if base is None else float(clocks[-1]) - base[1]
    previous = median(intervals[:3]) if len(intervals) == 6 else None
    current = median(intervals[3:]) if len(intervals) == 6 else None
    return {
        "local_count": local_count,
        "full_count": full_count,
        "local_start": None if local_start is None else local_start[0],
        "last_update": None if last is None else last[0],
        "intervals": intervals,
        "previous_median": previous,
        "current_median": current,
        "median_change": None if previous is None or current is None else current - previous,
        "waiting": waiting,
        "waiting_ratio": None if waiting is None or current in (None, 0) else waiting / current,
    }


def close(actual, expected, *, atol=1e-9) -> bool:
    if actual is None or expected is None or pd.isna(actual) or pd.isna(expected):
        return actual is None and expected is None
    return bool(np.isclose(float(actual), float(expected), rtol=1e-12, atol=atol))


def life_text(row: pd.Series) -> str:
    text = row.get("life_text", "")
    return f"{int(row['life_form'])}:{int(row['life_high'])}:{int(row['life_low'])}:{'' if pd.isna(text) else text}"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--n-dir", type=Path, required=True)
    parser.add_argument("--price-dir", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)

    read_manifest = json.loads((args.n_dir / "READ_MANIFEST.json").read_text(encoding="utf-8"))
    kline_manifest = json.loads((args.price_dir / "KLINE_READ_MANIFEST.json").read_text(encoding="utf-8"))
    if read_manifest["result"] != "PASS" or kline_manifest["result"] != "PASS":
        raise RuntimeError("input read manifest did not pass")

    names = [
        "rows", "origins", "bindings", "specs", "windows", "recent_members", "previous_members",
        "metrics", "loo_shifts", "metric_gaps", "working_bases", "rhythm", "intervals",
        "working_values", "working_duration", "working_progress", "working_efficiency",
        "working_counter", "working_waiting", "working_waiting_ratio",
    ]
    tables = {name: frame(args.n_dir / f"{name}.csv") for name in names}
    price = frame(args.price_dir / "rb_5m_price_calendar.csv")
    price["bar_time"] = pd.to_datetime(price["bar_time"])
    if price["open_uti"].duplicated().any():
        raise RuntimeError("price open_uti is not unique")
    price_by_uti = price.set_index("open_uti", drop=False)

    row = one(tables["rows"], "rows")
    origin = one(tables["origins"], "origins")
    window = one(tables["windows"].loc[tables["windows"]["address"] == int(row["window"])], "selected window")
    binding = one(tables["bindings"].loc[tables["bindings"]["address"] == int(window["binding"])], "window binding")
    working_base = one(tables["working_bases"].loc[tables["working_bases"]["address"] == int(row["working"])], "working base")
    if int(working_base["binding"]) != int(window["binding"]):
        raise RuntimeError("working/window bindings differ")
    if binding["object_name"] != "rb" or read_manifest["selection"]["object"] != "rb":
        raise RuntimeError("resolved object is not rb")
    if int(origin["as_of"]) != read_manifest["selection"]["as_of"]:
        raise RuntimeError("origin/read manifest As-Of mismatch")
    if len(tables["recent_members"]) != 6 or len(tables["previous_members"]) != 6:
        raise RuntimeError("selected window is not 6+6")
    if len(tables["metric_gaps"]) != 0:
        raise RuntimeError("selected complete window unexpectedly has metric gaps")

    spec_map = {int(row.kind): {"name": str(row.definition_life), "unit": str(row.unit)} for _, row in tables["specs"].iterrows()}
    if len(spec_map) != 6:
        raise RuntimeError("metric spec kinds are not unique")
    exact = read_manifest["selection"]["exact"]
    exact_text = ":".join(str(v) for v in exact)
    asof_time = str(pd.Timestamp(row["timestamp"]))

    paths = []
    segments = []
    confirmations = []
    member_values = {"recent": {}, "previous": {}}
    member_lives = {}

    for group, source in (("previous", tables["previous_members"]), ("recent", tables["recent_members"])):
        source = source.sort_values("child_id_3")
        for _, member in source.iterrows():
            slot = int(member["child_id_3"]) + 1
            start, end = int(member["start"]), int(member["end"])
            direction = int(member["direction"])
            if int(member["direction_knownness"]) != 0:
                raise RuntimeError(f"{group}[{slot}] direction is not AvailableCommitted")
            if start not in price_by_uti.index or end not in price_by_uti.index:
                raise RuntimeError(f"{group}[{slot}] exact price endpoints absent")
            lo = int(np.searchsorted(price["open_uti"].to_numpy(), start))
            hi = int(np.searchsorted(price["open_uti"].to_numpy(), end))
            part = price.iloc[lo : hi + 1].copy()
            values = primitive(part, direction)
            member_values[group][slot] = values
            life = life_text(member)
            member_lives[(group, slot)] = life
            known_uti = int(member["known_from"])
            confirmation_uti = int(member["confirmation"])
            known_time = str(price_by_uti.loc[known_uti, "bar_time"])
            confirmation_time = str(price_by_uti.loc[confirmation_uti, "bar_time"])
            direction_name = "up" if direction == 0 else "down"
            for _, quote in part.iterrows():
                paths.append({
                    "group": group, "slot": slot, "member": f"{group}-{slot}", "life": life,
                    "direction": direction, "direction_name": direction_name,
                    "open_uti": int(quote.open_uti), "bar_time": str(quote.bar_time), "close": quote.close,
                    "known_from_uti": known_uti, "known_at_time": known_time,
                    "confirmation_uti": confirmation_uti, "confirmation_time": confirmation_time,
                    "n_exact": exact_text, "as_of_uti": int(origin["as_of"]), "as_of_time": asof_time,
                    "projection_status": "reference close path; not a formal Episode product",
                })
            segments.append({
                "group": group, "slot": slot, "member": f"{group}-{slot}", "life": life,
                "direction": direction, "direction_name": direction_name,
                "start_uti": start, "start_time": str(price_by_uti.loc[start, "bar_time"]), "start_close": price_by_uti.loc[start, "close"],
                "end_uti": end, "end_time": str(price_by_uti.loc[end, "bar_time"]), "end_close": price_by_uti.loc[end, "close"],
                "confirmation_uti": confirmation_uti, "confirmation_time": confirmation_time,
                "known_from_uti": known_uti, "known_at_time": known_time,
                "sample_count": values["sample_count"], "calendar_contiguous": values["calendar_contiguous"],
                "n_exact": exact_text, "as_of_uti": int(origin["as_of"]), "as_of_time": asof_time,
                "projection_status": "endpoint boundary segment only; not actual path",
            })
            confirmations.append({
                "group": group, "slot": slot, "member": f"{group}-{slot}", "life": life,
                "confirmation_uti": confirmation_uti, "confirmation_time": confirmation_time,
                "confirmation_close": price_by_uti.loc[confirmation_uti, "close"],
                "known_from_uti": known_uti, "known_at_time": known_time,
                "actual_end_uti": end, "actual_end_time": str(price_by_uti.loc[end, "bar_time"]),
                "n_exact": exact_text, "as_of_time": asof_time,
                "projection_status": "confirmation/known-from marker, separate from actual endpoint",
            })

    recent_lives = {member_lives[("recent", slot)] for slot in range(1, 7)}
    previous_lives = {member_lives[("previous", slot)] for slot in range(1, 7)}
    if recent_lives.intersection(previous_lives):
        raise RuntimeError("recent/previous member lives overlap")

    working = one(tables["working_values"], "working values")
    working_start, working_end = int(working_base["start_value"]), int(working["through_value"])
    if not int(working_base["start_present"]) or not int(working["through_present"]):
        raise RuntimeError("working start/through is absent")
    working_direction = int(working_base["direction"])
    lo = int(np.searchsorted(price["open_uti"].to_numpy(), working_start))
    hi = int(np.searchsorted(price["open_uti"].to_numpy(), working_end))
    working_part = price.iloc[lo : hi + 1].copy()
    working_reference = primitive(working_part, working_direction)
    rhythm_reference_values = rhythm_reference(working_part, working_direction)
    working_life = life_text(working_base)
    if working_life in recent_lives or working_life in previous_lives:
        raise RuntimeError("working life was mixed into completed windows")
    for _, quote in working_part.iterrows():
        paths.append({
            "group": "working", "slot": 1, "member": "working", "life": working_life,
            "direction": working_direction, "direction_name": "up" if working_direction == 0 else "down",
            "open_uti": int(quote.open_uti), "bar_time": str(quote.bar_time), "close": quote.close,
            "known_from_uti": int(origin["known_from"]), "known_at_time": asof_time,
            "confirmation_uti": "", "confirmation_time": "",
            "n_exact": exact_text, "as_of_uti": int(origin["as_of"]), "as_of_time": asof_time,
            "projection_status": "working reference close path; completion remains Pending",
        })
    segments.append({
        "group": "working", "slot": 1, "member": "working", "life": working_life,
        "direction": working_direction, "direction_name": "up" if working_direction == 0 else "down",
        "start_uti": working_start, "start_time": str(price_by_uti.loc[working_start, "bar_time"]), "start_close": price_by_uti.loc[working_start, "close"],
        "end_uti": working_end, "end_time": str(price_by_uti.loc[working_end, "bar_time"]), "end_close": price_by_uti.loc[working_end, "close"],
        "confirmation_uti": "", "confirmation_time": "", "known_from_uti": int(origin["known_from"]), "known_at_time": asof_time,
        "sample_count": working_reference["sample_count"], "calendar_contiguous": working_reference["calendar_contiguous"],
        "n_exact": exact_text, "as_of_uti": int(origin["as_of"]), "as_of_time": asof_time,
        "projection_status": "working endpoint boundary segment; completion Pending",
    })

    comparisons = []
    stats = []
    metrics = tables["metrics"].sort_values("child_id_3")
    loo = tables["loo_shifts"]
    metric_name_by_slot = {
        int(metric["child_id_3"]): spec_map[int(metric["kind"])]["name"]
        for _, metric in metrics.iterrows()
    }
    for _, metric in metrics.iterrows():
        kind = int(metric["kind"])
        spec = spec_map[kind]
        recent = [member_values["recent"][slot][spec["name"]] for slot in range(1, 7)]
        previous = [member_values["previous"][slot][spec["name"]] for slot in range(1, 7)]
        expected = {
            "current": median(recent), "previous": median(previous),
        }
        expected["change"] = expected["current"] - expected["previous"]
        expected["dispersion"] = median([abs(value - expected["current"]) for value in recent])
        metric_checks = {}
        for field_name, expected_value in expected.items():
            actual_value = metric[field_name]
            passed = close(actual_value, expected_value)
            metric_checks[field_name] = passed
            comparisons.append({
                "target": f"metric.{spec['name']}.{field_name}", "formal": actual_value,
                "reference": expected_value, "pass": passed,
            })
        metric_loo = loo.loc[loo["child_id_3"] == int(metric["child_id_3"])].sort_values("child_id_4")
        if len(metric_loo) != 6:
            raise RuntimeError(f"{spec['name']} does not have six LOO slots")
        loo_checks = []
        for _, slot in metric_loo.iterrows():
            omitted = int(slot["child_id_4"])
            alternative = median([value for j, value in enumerate(recent) if j != omitted])
            shift = abs(alternative - expected["current"])
            passed = close(slot["median"], alternative) and close(slot["shift"], shift)
            loo_checks.append(passed)
            comparisons.append({
                "target": f"metric.{spec['name']}.loo[{omitted}]", "formal_median": slot["median"],
                "reference_median": alternative, "formal_shift": slot["shift"], "reference_shift": shift,
                "pass": passed,
            })
        stats.append({
            "kind": kind, "metric": spec["name"], "unit": spec["unit"],
            "present": int(metric["present"]), "current": metric["current"], "previous": metric["previous"],
            "change": metric["change"], "dispersion_unscaled_mad": metric["dispersion"],
            "loo_knownness": int(metric["loo_knownness"]), "loo_knownness_name": KNOWNNESS.get(int(metric["loo_knownness"]), "unknown"),
            "loo_base": metric["loo_base"], "loo_maximum_absolute_shift": metric["loo_maximum"],
            "loo_ties_bitmask": int(metric["loo_ties"]), "all_six_loo_slots_tied": int(metric["loo_ties"]) == 63,
            "finite_reference_checks_pass": all(metric_checks.values()) and all(loo_checks),
            "reference_recent_values": json.dumps(recent), "reference_previous_values": json.dumps(previous),
            "window_address": int(window["address"]), "binding_address": int(window["binding"]),
            "known_at_time": str(pd.Timestamp(window["timestamp"])), "as_of_time": asof_time, "n_exact": exact_text,
            "interpretation_boundary": "change is an absolute difference; dispersion is unscaled MAD; LOO is not member importance",
        })

    working_formal = {
        "BusinessDuration": one(tables["working_duration"], "working duration"),
        "DirectionalProgress": one(tables["working_progress"], "working progress"),
        "PathEfficiency": one(tables["working_efficiency"], "working efficiency"),
        "RawCounterMove": one(tables["working_counter"], "working counter"),
    }
    for metric_name, actual in working_formal.items():
        passed = close(actual["value"], working_reference[metric_name])
        comparisons.append({"target": f"working.{metric_name}", "formal": actual["value"], "reference": working_reference[metric_name], "pass": passed})
    formal_waiting = one(tables["working_waiting"], "working waiting")
    formal_ratio = one(tables["working_waiting_ratio"], "working waiting ratio")
    comparisons.extend([
        {"target": "working.waiting", "formal": formal_waiting["value"], "reference": rhythm_reference_values["waiting"], "pass": close(formal_waiting["value"], rhythm_reference_values["waiting"])},
        {"target": "working.waiting_ratio", "formal": formal_ratio["value"], "reference": rhythm_reference_values["waiting_ratio"], "pass": close(formal_ratio["value"], rhythm_reference_values["waiting_ratio"])},
    ])
    rhythm = one(tables["rhythm"], "rhythm")
    formal_intervals = tables["intervals"].sort_values("child_id_3")["duration"].tolist()
    rhythm_checks = {
        "local_count": close(rhythm["local_count"], rhythm_reference_values["local_count"]),
        "full_count": close(rhythm["full_count_value"], rhythm_reference_values["full_count"]),
        "previous_median": close(rhythm["previous_median_value"], rhythm_reference_values["previous_median"]),
        "current_median": close(rhythm["current_median_value"], rhythm_reference_values["current_median"]),
        "median_change": close(rhythm["median_change_value"], rhythm_reference_values["median_change"]),
        "intervals": len(formal_intervals) == len(rhythm_reference_values["intervals"]) and all(close(a, b) for a, b in zip(formal_intervals, rhythm_reference_values["intervals"])),
    }
    comparisons.extend({"target": f"rhythm.{name}", "pass": passed} for name, passed in rhythm_checks.items())

    working_rows = []
    for label, formal_name, unit in (
        ("duration", "BusinessDuration", "CalendarUTITick"),
        ("progress", "DirectionalProgress", "price"),
        ("efficiency", "PathEfficiency", "ratio"),
        ("counter", "RawCounterMove", "price"),
    ):
        item = working_formal[formal_name]
        working_rows.append({
            "field": label, "unit": unit, "value": item["value"], "present": int(item["present"]),
            "knownness": int(item["knownness"]), "knownness_name": KNOWNNESS.get(int(item["knownness"]), "unknown"),
            "applicability": int(item["applicability"]), "applicability_name": APPLICABILITY.get(int(item["applicability"]), "unknown"),
            "reason": int(item["reason"]), "reference_value": working_reference[formal_name],
        })
    for label, item, ref in (("waiting", formal_waiting, rhythm_reference_values["waiting"]), ("waiting_ratio", formal_ratio, rhythm_reference_values["waiting_ratio"])):
        working_rows.append({
            "field": label, "unit": "CalendarUTITick" if label == "waiting" else "ratio",
            "value": item["value"], "present": int(item["present"]),
            "knownness": int(item["knownness"]), "knownness_name": KNOWNNESS.get(int(item["knownness"]), "unknown"),
            "applicability": int(item["applicability"]), "applicability_name": APPLICABILITY.get(int(item["applicability"]), "unknown"),
            "reason": int(item["reason"]), "reference_value": ref,
        })
    for result in working_rows:
        result.update({
            "direction": working_direction, "direction_name": "up" if working_direction == 0 else "down",
            "start_uti": working_start, "through_uti": working_end,
            "completion_knownness": int(working["completion_knownness"]),
            "completion_knownness_name": KNOWNNESS.get(int(working["completion_knownness"]), "unknown"),
            "known_at_time": asof_time, "as_of_time": asof_time, "n_exact": exact_text,
        })

    rhythm_rows = [{
        "local_count": int(rhythm["local_count"]), "full_count": rhythm["full_count_value"],
        "local_start_uti": rhythm["local_start_value"], "last_update_uti": rhythm["last_update_value"],
        "previous_median": rhythm["previous_median_value"], "current_median": rhythm["current_median_value"],
        "median_change": rhythm["median_change_value"], "intervals": json.dumps(formal_intervals),
        "waiting": formal_waiting["value"], "waiting_ratio": formal_ratio["value"],
        "knownness": int(rhythm["knownness"]), "knownness_name": KNOWNNESS.get(int(rhythm["knownness"]), "unknown"),
        "known_at_time": asof_time, "as_of_time": asof_time, "n_exact": exact_text,
        "scope_note": "six saved local intervals compare previous 3 vs recent 3; local/full counts remain distinct",
        "reference_checks_pass": all(rhythm_checks.values()),
    }]

    price_export = price.copy()
    price_export["bar_time"] = price_export["bar_time"].astype(str)
    price_export["known_at_time"] = price_export["bar_time"]
    price_export["symbol"] = "rb"
    loo_export = tables["loo_shifts"].copy()
    loo_export["metric"] = loo_export["child_id_3"].map(metric_name_by_slot)
    loo_export["known_at_time"] = str(pd.Timestamp(window["timestamp"]))
    loo_export["as_of_time"] = asof_time
    loo_export["n_exact"] = exact_text
    loo_export["interpretation_boundary"] = "six leave-one-out absolute shifts; not a member importance ranking"
    outputs = {
        "price": ("rb_price_display.csv", price_export),
        "process_paths": ("rb_process_paths.csv", pd.DataFrame(paths)),
        "segments": ("rb_process_boundaries.csv", pd.DataFrame(segments)),
        "confirmations": ("rb_confirmation_markers.csv", pd.DataFrame(confirmations)),
        "statistics": ("rb_completed_window_statistics.csv", pd.DataFrame(stats)),
        "working": ("rb_working_values.csv", pd.DataFrame(working_rows)),
        "rhythm": ("rb_working_rhythm.csv", pd.DataFrame(rhythm_rows)),
        "loo": ("rb_loo_details.csv", loo_export),
    }
    output_manifest = {}
    for name, (filename, output_frame) in outputs.items():
        path = args.output_dir / filename
        output_frame.to_csv(path, index=False)
        output_manifest[name] = {"path": filename, "rows": len(output_frame), "sha256": sha256(path), "columns": list(output_frame.columns)}

    verification = {
        "schema_version": 1,
        "result": "PASS" if all(bool(item["pass"]) for item in comparisons) else "FAIL",
        "scope": "rb final As-Of finite reference arithmetic and table/address relationships only",
        "relation_checks": {
            "row_window_to_window_address": int(row["window"]) == int(window["address"]),
            "window_to_binding": int(window["binding"]) == int(binding["address"]),
            "row_working_to_working_address": int(row["working"]) == int(working_base["address"]),
            "working_binding_equals_window_binding": int(working_base["binding"]) == int(window["binding"]),
            "recent_previous_lives_disjoint": not bool(recent_lives.intersection(previous_lives)),
            "working_life_not_completed": working_life not in recent_lives | previous_lives,
            "price_calendar_position_contiguous": bool(kline_manifest["calendar_position_contiguous"]),
            "price_nonfinite_close": int(kline_manifest["nonfinite"]["close"]),
        },
        "selection": {
            "object": "rb", "exact": exact, "as_of_uti": int(origin["as_of"]), "as_of_time": asof_time,
            "window_address": int(window["address"]), "working_address": int(working_base["address"]),
            "binding_address": int(binding["address"]), "n": int(binding["n"]), "loo_minimum": int(binding["loo_minimum"]),
        },
        "comparisons": comparisons,
        "comparison_count": len(comparisons),
        "failed_comparisons": [item for item in comparisons if not bool(item["pass"])],
        "boundaries": [
            "reference arithmetic is observation-only and does not become a formal Episode/N product",
            "the check covers this selected rb As-Of, not the full feature or future data",
            "endpoint segments are explicitly separate from the actual close paths",
        ],
    }
    write_json(args.output_dir / "VERIFICATION.json", verification)
    manifest = {
        "schema_version": 1, "result": verification["result"],
        "inputs": {
            "n_manifest": {"path": str((args.n_dir / "READ_MANIFEST.json").resolve()), "sha256": sha256(args.n_dir / "READ_MANIFEST.json")},
            "kline_manifest": {"path": str((args.price_dir / "KLINE_READ_MANIFEST.json").resolve()), "sha256": sha256(args.price_dir / "KLINE_READ_MANIFEST.json")},
        },
        "selection": verification["selection"], "outputs": output_manifest,
        "verification": {"path": "VERIFICATION.json", "sha256": sha256(args.output_dir / "VERIFICATION.json")},
    }
    write_json(args.output_dir / "PROJECTION_MANIFEST.json", manifest)
    print(json.dumps({"result": manifest["result"], "outputs": output_manifest, "comparisons": len(comparisons)}, ensure_ascii=False), flush=True)
    return 0 if verification["result"] == "PASS" else 2


if __name__ == "__main__":
    raise SystemExit(main())
