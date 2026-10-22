#!/usr/bin/env python3
"""Read the named i missing-data neighborhood through normal mainline OnlyRead."""

from __future__ import annotations

import argparse
import hashlib
import inspect
import json
from pathlib import Path

import numpy as np
import pandas as pd

from m3sof.settings.json import eval2
from m3tt import CurrTradeSet
from mquant.frame import CalType, CurrCalendar, CurrIndustry
from mquant.quant import OptContext
from mquant.tis.calendar.base import blk_suitable_calendars
from mquant.tis.frp.U2Mainline import U2MainlineKLineInput
from mquant.tis.lib3 import CurrSymbol
import mquant.tis.frp.U2Mainline as mainline_module


SOF = "TA_updto20240229_DBA"
CONTEXT = "blk@steel"
CALENDAR = "night_end_at_2300"
START = pd.Timestamp("2017-03-30 14:00:00")
END = pd.Timestamp("2017-03-31 10:00:00")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def calendar_name(value) -> str:
    for field in ("name", "calendar", "life"):
        candidate = getattr(value, field, None)
        if candidate:
            return str(candidate)
    return str(value)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()
    context = OptContext(sof_name=SOF)
    candidates = tuple(blk_suitable_calendars(context.sof, CONTEXT))
    matches = [value for value in candidates if calendar_name(value) == CALENDAR]
    if len(matches) != 1:
        raise RuntimeError(f"calendar resolution is not unique: {[calendar_name(v) for v in candidates]}")
    with CurrTradeSet(context.sof), CurrIndustry(CONTEXT), CurrCalendar(matches[0]), CurrSymbol("i"):
        feature = U2MainlineKLineInput(
            source=eval2("MapKLineOpenData(freq='5m')"),
            calendar_grid=eval2("ResampleCalendarTsa(resample_len=600)"),
        )
        full = feature.rerun(CalType.OnlyRead).to_df()
        product_dir = str(feature.full_dir)
    required = [
        "open_uti", "open", "high", "low", "close", "volume", "openInt",
        "calendar_position", "calendar_time",
    ]
    frame = full.loc[(full.index >= START) & (full.index <= END), required].copy()
    if frame.empty:
        raise RuntimeError("named i neighborhood returned no price rows")
    position_delta = frame["calendar_position"].astype(np.int64).diff()
    uti_delta = frame["open_uti"].astype(np.int64).diff()
    wall_delta = frame.index.to_series().diff().dt.total_seconds()
    gaps = []
    for position in np.flatnonzero((position_delta > 1).to_numpy()):
        gaps.append({
            "left_time": str(frame.index[position - 1]),
            "right_time": str(frame.index[position]),
            "left_open_uti": int(frame["open_uti"].iloc[position - 1]),
            "right_open_uti": int(frame["open_uti"].iloc[position]),
            "calendar_position_delta": int(position_delta.iloc[position]),
            "missing_calendar_bars": int(position_delta.iloc[position] - 1),
            "natural_uti_delta": int(uti_delta.iloc[position]),
            "right_close": float(frame["close"].iloc[position]),
        })
    wall_clock_gaps = []
    for position in np.flatnonzero((wall_delta > 300).to_numpy()):
        wall_clock_gaps.append({
            "left_time": str(frame.index[position - 1]),
            "right_time": str(frame.index[position]),
            "wall_clock_seconds": int(wall_delta.iloc[position]),
            "calendar_position_delta": int(position_delta.iloc[position]),
            "missing_calendar_bars": max(0, int(position_delta.iloc[position] - 1)),
            "right_open_uti": int(frame["open_uti"].iloc[position]),
            "right_close": float(frame["close"].iloc[position]),
        })
    missing = frame["close"].isna().to_numpy()
    missing_runs = []
    start = None
    for position, absent in enumerate([*missing, False]):
        if absent and start is None:
            start = position
        if not absent and start is not None:
            end = position - 1
            missing_runs.append({
                "first_missing_time": str(frame.index[start]),
                "last_missing_time": str(frame.index[end]),
                "missing_rows": end - start + 1,
                "previous_present_time": None if start == 0 else str(frame.index[start - 1]),
                "previous_present_close": None if start == 0 else float(frame["close"].iloc[start - 1]),
                "recovery_time": None if position == len(frame) else str(frame.index[position]),
                "recovery_open_uti": None if position == len(frame) else int(frame["open_uti"].iloc[position]),
                "recovery_close": None if position == len(frame) else float(frame["close"].iloc[position]),
            })
            start = None
    args.output_dir.mkdir(parents=True, exist_ok=True)
    output = args.output_dir / "i_5m_price_calendar.csv"
    frame.reset_index(names="bar_time").to_csv(output, index=False)
    manifest = {
        "schema_version": 1,
        "result": "PASS",
        "entry": "U2MainlineKLineInput.rerun(CalType.OnlyRead).to_df",
        "import": inspect.getfile(mainline_module),
        "sof": SOF,
        "context": CONTEXT,
        "calendar": CALENDAR,
        "object": "i",
        "product_dir": product_dir,
        "source_life": "/m3varI/var/L1_data/tick/map_kline_data/5m/i_night_end_at_2300",
        "requested_time_range": [str(START), str(END)],
        "actual_time_range": [str(frame.index[0]), str(frame.index[-1])],
        "rows": len(frame),
        "calendar_gap_count": len(gaps),
        "calendar_gaps": gaps,
        "wall_clock_gap_count": len(wall_clock_gaps),
        "wall_clock_gaps": wall_clock_gaps,
        "missing_close_rows": int(missing.sum()),
        "missing_close_runs": missing_runs,
        "qualification": "Calendar positions remain contiguous while close is nullable across the night rows. The first restored close remains an ordinary observed input and is not relabelled as an extreme confirmation",
        "output": {"path": output.name, "bytes": output.stat().st_size, "sha256": sha256(output)},
    }
    manifest_path = args.output_dir / "I_MISSING_CONTEXT.json"
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"result": "PASS", "rows": len(frame), "calendar_gaps": gaps, "wall_clock_gaps": wall_clock_gaps, "missing_close_runs": missing_runs}, ensure_ascii=False), flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
