#!/usr/bin/env python3
"""Read the original rb 5m price/Calendar rows through U2Mainline OnlyRead."""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import inspect
import json
import time
from pathlib import Path

import numpy as np

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


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def calendar_name(value) -> str:
    for field in ("name", "calendar", "life"):
        candidate = getattr(value, field, None)
        if candidate:
            return str(candidate)
    return str(value)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--start", required=True, type=int)
    parser.add_argument("--end", required=True, type=int)
    parser.add_argument("--output-dir", required=True, type=Path)
    args = parser.parse_args()
    if args.start > args.end:
        raise ValueError("start must not exceed end")

    started_at = dt.datetime.now(dt.timezone.utc)
    started = time.monotonic()
    context = OptContext(sof_name=SOF)
    candidates = tuple(blk_suitable_calendars(context.sof, CONTEXT))
    matches = [value for value in candidates if calendar_name(value) == CALENDAR]
    if len(matches) != 1:
        raise RuntimeError(f"calendar resolution is not unique: {[calendar_name(v) for v in candidates]!r}")

    with CurrTradeSet(context.sof), CurrIndustry(CONTEXT), CurrCalendar(matches[0]), CurrSymbol("rb"):
        feature = U2MainlineKLineInput(
            source=eval2("MapKLineOpenData(freq='5m')"),
            calendar_grid=eval2("ResampleCalendarTsa(resample_len=600)"),
        )
        frame = feature.rerun(CalType.OnlyRead).to_df()
        required = [
            "open_uti", "open", "high", "low", "close", "volume", "openInt",
            "calendar_position", "calendar_time",
        ]
        missing = sorted(set(required).difference(frame.columns))
        if missing:
            raise RuntimeError(f"normal U2Mainline result lacks required fields: {missing}")
        feature_full_dir = str(feature.full_dir)
        uti = frame["open_uti"].to_numpy(dtype=np.int64)
        lo = int(np.searchsorted(uti, args.start))
        hi = int(np.searchsorted(uti, args.end))
        if lo >= len(uti) or hi >= len(uti) or int(uti[lo]) != args.start or int(uti[hi]) != args.end:
            raise RuntimeError(
                f"requested exact endpoints absent: start={args.start} found={None if lo >= len(uti) else int(uti[lo])}, "
                f"end={args.end} found={None if hi >= len(uti) else int(uti[hi])}"
            )
        selected = frame.iloc[lo : hi + 1][required].copy()

    args.output_dir.mkdir(parents=True, exist_ok=True)
    output = args.output_dir / "rb_5m_price_calendar.csv"
    selected.reset_index(names="bar_time").to_csv(output, index=False)
    manifest = {
        "schema_version": 1,
        "mode": "U2MainlineKLineInput_CalType_OnlyRead",
        "result": "PASS",
        "started_at": started_at.isoformat(),
        "finished_at": dt.datetime.now(dt.timezone.utc).isoformat(),
        "elapsed_seconds": time.monotonic() - started,
        "python_import": inspect.getfile(mainline_module),
        "sof": SOF,
        "context": CONTEXT,
        "calendar_candidates": [calendar_name(value) for value in candidates],
        "calendar_selected": CALENDAR,
        "object": "rb",
        "feature_full_dir": feature_full_dir,
        "source_life": "/m3varI/var/L1_data/tick/map_kline_data/5m/rb_night_end_at_2300",
        "source_revision": SOF,
        "requested_range": [args.start, args.end],
        "physical_row_range": [lo, hi],
        "rows": len(selected),
        "first_bar_time": str(selected.index[0]),
        "last_bar_time": str(selected.index[-1]),
        "columns": required,
        "nonfinite": {
            name: int((~np.isfinite(selected[name].to_numpy(dtype=float))).sum())
            for name in ("open", "high", "low", "close", "calendar_time")
        },
        "calendar_position_contiguous": bool(
            np.all(np.diff(selected["calendar_position"].to_numpy(dtype=np.int64)) == 1)
        ),
        "output": {"path": output.name, "sha256": sha256(output)},
    }
    manifest_path = args.output_dir / "KLINE_READ_MANIFEST.json"
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(manifest, ensure_ascii=False), flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
