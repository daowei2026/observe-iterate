"""Recompute this batch's descriptive daily-close evidence from W02's formal CSVs.
No data acquisition, trading signal, feature implementation, or platform mutation.
"""
from __future__ import annotations
import argparse
import csv
import hashlib
import json
import math
from pathlib import Path

SYMBOLS = ("rb", "hc", "i")
HASHES = {
    "rb": "59aaf24c4594340c076f5f118e9deb8e8cf2c5998d660034cfcda47109976460",
    "hc": "e6f4f798e9e720b66942d1061b49fec373c74ba4d6fb4a55f0f8a468374f9947",
    "i": "dc152d88beb1dc844ba1bc2718997f9ccf59f03b6ead149dd07f2740670469ae",
}
CORES = {
    "CO01-C01": ("2021-03-09", "2021-03-31"),
    "CO01-C02": ("2021-08-23", "2021-09-30"),
    "CO01-C03": ("2022-05-10", "2022-06-08"),
    "CO01-C04": ("2023-08-10", "2023-09-28"),
}

def describe(values: list[float]) -> dict:
    if len(values) < 2 or any(not math.isfinite(v) or v <= 0 for v in values):
        raise ValueError("Need at least two positive, finite closes; never bridge missing rows")
    p0, pn = values[0], values[-1]
    distance = sum(abs(b-a) for a, b in zip(values, values[1:]))
    peak = p0
    retrace = 0.0
    for p in values:
        peak = max(peak, p)
        retrace = max(retrace, peak-p)
    return {
        "n": len(values), "start_close": p0, "end_close": pn,
        "net_pct": 100*(pn/p0-1),
        "signed_efficiency": (pn-p0)/distance if distance else None,
        "max_retrace_base_pct": 100*retrace/p0,
        "min_excursion_base_pct": 100*(min(values)/p0-1),
        "max_excursion_base_pct": 100*(max(values)/p0-1),
        "closes_below_base": sum(p < p0 for p in values),
    }

def load_formal(root: Path) -> tuple[dict, dict]:
    data, evidence = {}, {}
    for sym in SYMBOLS:
        path = root / "feature_slices/big_000001/symbol" / sym / "kline_1d/__default__.csv"
        raw = path.read_bytes()
        digest = hashlib.sha256(raw).hexdigest()
        if digest != HASHES[sym]:
            raise ValueError(f"{sym}: source SHA256 differs; do not silently mix versions")
        rows = list(csv.DictReader(raw.decode("utf-8").splitlines()))
        if len(rows) != 763:
            raise ValueError(f"{sym}: unexpected row count {len(rows)}")
        time_keys = [(r["closeUti"], r["closeTs"]) for r in rows]
        if len(set(time_keys)) != len(rows):
            raise ValueError(f"{sym}: duplicate time key")
        if time_keys != sorted(time_keys, key=lambda k: int(k[0])):
            raise ValueError(f"{sym}: unsorted closeUti")
        if data and time_keys != data[next(iter(data))]["time_keys"]:
            raise ValueError(f"{sym}: cross-symbol timestamp mismatch")
        closes = [float(r["close"]) if r["close"] else math.nan for r in rows]
        invalid = [r["closeTs"] for r in rows
                   if any(not r[k] or not math.isfinite(float(r[k])) for k in ("open","high","low","close"))]
        if invalid != ["2023-03-13 15:00:00"]:
            raise ValueError(f"{sym}: unexpected OHLC validity pattern: {invalid}")
        data[sym] = {"rows": rows, "closes": closes, "time_keys": time_keys}
        evidence[sym] = {"path": str(path), "sha256": digest, "rows": len(rows),
                         "invalid_closeTs": invalid}
    return data, evidence

def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--delivery-root", type=Path, required=True)
    parser.add_argument("--anchors", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    data, source = load_formal(args.delivery_root)
    # The R0008 projection is checked against actual source bytes, not a second projection.
    with args.anchors.open(encoding="utf-8", newline="") as f:
        anchors = list(csv.DictReader(f))
    for anchor in anchors:
        idx = int(anchor["source_csv_line"])-2
        for sym in SYMBOLS:
            row = data[sym]["rows"][idx]
            if row["closeTs"] != anchor["closeTs"] or float(row["close"]) != float(anchor[sym]):
                raise ValueError(f"Anchor mismatch: {anchor['closeTs']} {sym}; return actual source to issuer")
    results = []
    for case, (start, end) in CORES.items():
        for sym in SYMBOLS:
            rows = data[sym]["rows"]
            vals = [p for r,p in zip(rows,data[sym]["closes"])
                    if start <= r["closeTs"][:10] <= end]
            results.append({"case_id": case, "symbol": sym, "start": start, "end": end,
                            **describe(vals)})
    result = {"source_checks": source, "anchor_rows_checked": len(anchors),
              "metrics": results, "scope": "daily-close descriptive reconstruction only",
              "timezone_conversion": "NONE", "missing_fill": "NONE"}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2, allow_nan=False)+"\n",
                           encoding="utf-8")
    print(json.dumps({"output": str(args.output), "anchors": len(anchors),
                      "metrics_rows": len(results)}, ensure_ascii=False))

if __name__ == "__main__":
    main()
