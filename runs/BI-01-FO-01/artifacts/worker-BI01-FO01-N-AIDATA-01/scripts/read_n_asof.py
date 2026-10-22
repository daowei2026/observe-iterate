#!/usr/bin/env python3
"""Read one real normal-N As-Of through the fixed thin-reader contract.

The script keeps the complete three-source product identity, selects the object
Life from the product's own bindings table, uses the original integer knowledge
time, and exports every returned named table without filling nullable values.
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import inspect
import json
import resource
import sys
import time
import traceback
from pathlib import Path

import numpy as np
import pandas as pd

from m3tt import CurrTradeSet
from mquant.frame import CalType, CurrCalendar, CurrIndustry
from mquant.quant import OptContext
from mquant.tis.calendar.base import blk_suitable_calendars
from mquant.tis.frp.U2NodeBehavior import U2NormalNodeBehaviorFrp
from mquant.tis.frp.U2ThinNode import identifier
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


def _write_json(path: Path, payload) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(_clean(payload), ensure_ascii=False, indent=2, allow_nan=False) + "\n",
        encoding="utf-8",
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--configuration", type=Path, required=True)
    parser.add_argument("--object", required=True)
    parser.add_argument("--as-of", type=int, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()

    started_at = dt.datetime.now(dt.timezone.utc)
    started = time.monotonic()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    actual = json.loads(args.configuration.read_text(encoding="utf-8"))
    sources = actual["配置"]["source"]["sources"]
    configured_objects = [source["source"]["source"]["scope"]["object"] for source in sources]
    if args.object not in configured_objects:
        raise ValueError(f"object {args.object!r} is not in complete sources {configured_objects!r}")

    context = OptContext(sof_name=EXPECTED_SOF)
    candidates = tuple(blk_suitable_calendars(context.sof, EXPECTED_CONTEXT))
    matches = [value for value in candidates if _calendar_name(value) == EXPECTED_CALENDAR]
    if len(matches) != 1:
        raise RuntimeError(f"calendar resolution is not unique: {[_calendar_name(v) for v in candidates]!r}")

    print("PHASE construct", flush=True)
    with CurrTradeSet(context.sof), CurrIndustry(EXPECTED_CONTEXT):
        with CurrCalendar(matches[0]):
            feature = U2NormalNodeBehaviorFrp.from_sources(sources, compact_history=True)
            full_dir = Path(str(feature.full_dir))
            if full_dir != EXPECTED_DIR:
                raise RuntimeError(f"unexpected product directory: {full_dir}")
            print("PHASE only_read", flush=True)
            feature.rerun(CalType.OnlyRead)
            print("PHASE bindings", flush=True)
            bindings = feature.to_dfs(products=["bindings"])["bindings"]
            object_bindings = bindings.loc[bindings["object_name"] == args.object]
            if len(object_bindings) != 1:
                raise RuntimeError(f"expected one binding for {args.object}, got {len(object_bindings)}")
            node_life = str(object_bindings.iloc[0]["node_life"])
            print(f"PHASE read_at_knowledge object={args.object} life={node_life} as_of={args.as_of}", flush=True)
            session = feature.read_session(life=node_life, as_of=args.as_of)
            frames = session.to_dfs()
            print("PHASE export", flush=True)

    table_manifest = {}
    for name, frame in frames.items():
        output = args.output_dir / f"{name}.csv"
        public = frame.reset_index()
        public.to_csv(output, index=False)
        table_manifest[name] = {
            "path": output.name,
            "rows": len(public),
            "columns": list(public.columns),
            "dtypes": {column: str(dtype) for column, dtype in public.dtypes.items()},
            "sha256": _sha256(output),
        }

    revision_ids = sorted({
        identifier(row)
        for _, row in frames["revisions"].iterrows()
    })
    if len(revision_ids) != 1 or revision_ids[0] is None:
        raise RuntimeError(f"As-Of result did not resolve one exact revision: {revision_ids!r}")
    exact = ["NodeBehaviorBook", "NodeScaleTurnBehaviorRevision", node_life, revision_ids[0]]

    finished_at = dt.datetime.now(dt.timezone.utc)
    report = {
        "schema_version": 1,
        "mode": "normal_feature_read_at_knowledge",
        "result": "PASS",
        "started_at": started_at.isoformat(),
        "finished_at": finished_at.isoformat(),
        "elapsed_seconds": time.monotonic() - started,
        "max_rss_kib": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        "python": sys.executable,
        "imports": {
            "U2NodeBehavior": inspect.getfile(node_module),
            "U2ThinNode": inspect.getfile(thin_module),
        },
        "input": {
            "configuration_path": str(args.configuration.resolve()),
            "configuration_sha256": _sha256(args.configuration),
            "complete_source_objects": configured_objects,
            "compact_history": True,
            "sof": EXPECTED_SOF,
            "context": EXPECTED_CONTEXT,
            "calendar_candidates": [_calendar_name(value) for value in candidates],
            "calendar_selected": _calendar_name(matches[0]),
            "product_dir": str(full_dir),
        },
        "selection": {
            "object": args.object,
            "node_life": node_life,
            "as_of": args.as_of,
            "exact": exact,
            "binding": _clean(object_bindings.reset_index().to_dict("records")),
        },
        "tables": table_manifest,
    }
    _write_json(args.output_dir / "READ_MANIFEST.json", report)
    print(json.dumps({
        "result": "PASS",
        "object": args.object,
        "as_of": args.as_of,
        "exact": exact,
        "tables": len(frames),
        "elapsed_seconds": report["elapsed_seconds"],
        "max_rss_kib": report["max_rss_kib"],
    }, ensure_ascii=False), flush=True)
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception:
        traceback.print_exc()
        raise
