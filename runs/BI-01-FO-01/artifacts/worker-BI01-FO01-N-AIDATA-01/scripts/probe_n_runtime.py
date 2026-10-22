#!/usr/bin/env python3
"""Fresh probe of the exact normal-N reader and its saved product identity.

This script is deliberately read-only with respect to FAO products.  It loads the
complete R30 sources, requires the named calendar, invokes ``CalType.OnlyRead``,
and reads only the low-frequency ``bindings`` table.
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import inspect
import json
import sys
import time
from pathlib import Path

import numpy as np
import pandas as pd

from m3tt import CurrTradeSet
from mquant.frame import CalType, CurrCalendar, CurrIndustry
from mquant.quant import OptContext
from mquant.tis.calendar.base import blk_suitable_calendars
from mquant.tis.frp.U2NodeBehavior import U2NormalNodeBehaviorFrp
import mquant.aidata.api as aidata_api
import mquant.tis.frp.U2NodeBehavior as node_module
import mquant.tis.frp.U2ThinNode as thin_module


EXPECTED_DIR = Path(
    "/m3varK/BaseData/futures/TA_updto20240229_DBA/fao/prod/"
    "U2NormalNodeBehaviorFrp/9/0/d/3/7/a/4/"
    "fb2007d71be1e620801457424d6dea8b4/func"
)
EXPECTED_CALENDAR = "night_end_at_2300"
EXPECTED_SOF = "TA_updto20240229_DBA"
EXPECTED_CONTEXT = "blk@steel"


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def _clean(value):
    if isinstance(value, dict):
        return {str(key): _clean(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [_clean(item) for item in value]
    if isinstance(value, np.generic):
        return _clean(value.item())
    if value is pd.NA:
        return None
    if isinstance(value, float) and not np.isfinite(value):
        return None
    if isinstance(value, (pd.Timestamp, dt.datetime, Path)):
        return str(value)
    return value


def _calendar_name(value) -> str:
    for field in ("name", "calendar", "life"):
        candidate = getattr(value, field, None)
        if candidate:
            return str(candidate)
    return str(value)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--configuration", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    started = time.monotonic()
    actual = json.loads(args.configuration.read_text(encoding="utf-8"))
    sources = actual["配置"]["source"]["sources"]
    context = OptContext(sof_name=EXPECTED_SOF)
    candidates = tuple(blk_suitable_calendars(context.sof, EXPECTED_CONTEXT))
    matches = [value for value in candidates if _calendar_name(value) == EXPECTED_CALENDAR]
    if len(matches) != 1:
        raise RuntimeError(
            f"expected exactly one {EXPECTED_CALENDAR!r} calendar, got "
            f"{[_calendar_name(value) for value in candidates]!r}"
        )

    with CurrTradeSet(context.sof), CurrIndustry(EXPECTED_CONTEXT):
        with CurrCalendar(matches[0]):
            feature = U2NormalNodeBehaviorFrp.from_sources(sources, compact_history=True)
            full_dir = Path(str(feature.full_dir))
            if full_dir != EXPECTED_DIR:
                raise RuntimeError(f"unexpected product directory: {full_dir}")
            feature.rerun(CalType.OnlyRead)
            frames = feature.to_dfs(products=["bindings"])

    bindings = frames["bindings"]
    payload = {
        "schema_version": 1,
        "mode": "normal_feature_only_read_bindings_probe",
        "started_at": dt.datetime.now(dt.timezone.utc).isoformat(),
        "elapsed_seconds": time.monotonic() - started,
        "python": sys.executable,
        "configuration": {
            "path": str(args.configuration.resolve()),
            "sha256": _sha256(args.configuration),
            "source_count": len(sources),
        },
        "imports": {
            "U2NodeBehavior": inspect.getfile(node_module),
            "U2ThinNode": inspect.getfile(thin_module),
            "aidata_api": inspect.getfile(aidata_api),
        },
        "runtime": {
            "sof": EXPECTED_SOF,
            "context": EXPECTED_CONTEXT,
            "calendar_candidates": [_calendar_name(value) for value in candidates],
            "calendar_selected": _calendar_name(matches[0]),
            "feature_full_dir": str(full_dir),
            "expected_full_dir": str(EXPECTED_DIR),
            "product_definition": _clean(feature.product_definition()),
        },
        "bindings": {
            "shape": list(bindings.shape),
            "index_names": list(bindings.index.names),
            "dtypes": {name: str(dtype) for name, dtype in bindings.dtypes.items()},
            "records": _clean(bindings.reset_index().to_dict("records")),
        },
        "result": "PASS",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2, allow_nan=False) + "\n",
        encoding="utf-8",
    )
    print(json.dumps({
        "result": payload["result"],
        "output": str(args.output),
        "elapsed_seconds": payload["elapsed_seconds"],
        "binding_rows": len(bindings),
    }, ensure_ascii=False), flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
