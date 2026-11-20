#!/usr/bin/env python3
"""D004 integrated CAEGraph definition for Q.

Run identity:
  OI-U2-Q-OBS-20261120-01 / D004 / WI-D / M-D

This file binds the exact Q instance, the accepted B position and the A field
semantics into the C3 CAEGraph design.  It does not silently rerun F/Q.  The
default mode reads existing formal products.  A full-period Q rerun is only
allowed with both --mode rerun and --allow-full-period-rerun.

Locked sources:
  frp@67711c492da909ed0f044f357beb278abf7fc71c
  tis@2f460d663d821cf2ba25555eda13e78b697d0767
  uplot@0a4fcd54059782572a3f7e82fad041121e8c65ad
"""
from __future__ import annotations

import argparse
import json
import math
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Mapping, Sequence

import numpy as np
import pandas as pd
from bokeh.io import output_file, save
from bokeh.models import ColumnDataSource, FixedTicker, HoverTool
from mquant.frame import CurrCalendar, CurrSof, CurrSymbol, GMap, KLine, OptContext
from mquant.tis.frp.U2ThinRelations import _uuid
from mquant.tis.frp.fqv_kline_example import make_features
from mquant.uplot import (
    AllSymsFig,
    AllSymsMainFig,
    BasePlotter,
    CAEGraph,
    DefaultFigTheme,
    KPriceLine,
    MainFig,
    PerSymFigSet,
    PlotDataFolder,
    PlotDataNode,
    PlotSet,
    SubFig,
)

RUN_ID = "OI-U2-Q-OBS-20261120-01"
SOF_NAME = "TA_updto20240229_DBA"
BLOCK = "steel"
CALENDAR = "night_end_at_2300"
FREQUENCY = "5m"
OBJECTS = ("rb", "hc", "i")
# B gives date boundaries.  PlotCtx treats the right endpoint as a timestamp;
# 23:59:59 implements an inclusive end-date without mutating SOF startDay/endDay.
B_START = "2021-01-01 00:00:00"
B_END = "2022-12-31 23:59:59"
TIMESPANS = ((B_START, B_END),)

PARAMS: dict[str, Any] = {
    "freq": FREQUENCY,
    "symbols": OBJECTS,
    "delta": 600,
    "direction": "DirectionUp",
    "retrace_pct": 0.5,
    "check_retrace_pct": 0.5,
    "membership_line": 0.5,
    "spec_term": "M",
    "distance_times": 100,
    "x_step_times": 0.1,
    "overlap": 0.2,
    "source_core_multiples": 30,
}

DEFAULT_HTML = Path(
    "longrun/runs/OI-U2-Q-OBS-20261120-01/artifacts/E/Q_CAEGRAPH.html"
)
DEFAULT_DATA_DIR = Path(
    "longrun/runs/OI-U2-Q-OBS-20261120-01/artifacts/E/Q_CAEGRAPH_DATA"
)

Q_BOOK = "PostTurnGroupDirectionalOrganization"
Q_KIND = "Organization"
F_BOOK = "CommonPriceTurnGroupCandidates"
F_KIND = "Candidate"

Q_PRODUCTS = (
    "definitions",
    "definitions_organizationBindings",
    "occurrences",
    "occurrences_organizationPrevious",
    "occurrences_organizationMembers",
    "occurrences_organizationMembers_organizationAskedTurn_motionClock",
    "occurrences_organizationMembers_organizationUsedTurn_motionClock",
    "occurrences_organizationMembers_organizationSuccessor",
    "occurrences_organizationMembers_organizationSuccessor_motionClock",
    "occurrences_organizationMembers_organizationEndpoint",
    "occurrences_organizationMembers_organizationEndpoint_endpointPrice",
    "occurrences_organizationMembers_organizationEndpoint_endpointClock",
    "occurrences_organizationMembers_organizationQuantities",
    "occurrences_organizationMembers_organizationQuantities_motionNumber",
    "occurrences_organizationMembers_organizationMissingRange",
)
F_PRODUCTS = ("occurrences", "occurrences_groupMembers")

Q_DIRECTION = {0: "DirectionUp", 1: "DirectionDown"}
Q_OBSERVATION = {
    0: "MotionObserving",
    1: "HorizonReached",
    2: "MotionScopeEnded",
}
Q_APPLICABILITY = {0: "SubjectApplicable", 1: "SubjectWithdrawn"}
Q_QUALIFICATION = {
    0: "QualificationRejected",
    1: "QualificationConflict",
    2: "QualificationPending",
    3: "QualifiedCompleted",
    4: "QualifiedWorking",
}
Q_COMPLETION = {0: "MotionWorking", 1: "MotionCompleted"}
Q_VERDICT = {
    0: "SupportsAskedDirection",
    1: "ContradictsAskedDirection",
    2: "RequiredMotionConflict",
    3: "UndeterminedZeroProgress",
    4: "UndeterminedEndpoint",
    5: "WorkingNotMature",
    6: "WorkingPathUnavailable",
    7: "MemberAnchorWithdrawn",
}
Q_BASIS = {0: "CandidateMemberBasis", 1: "MemberBasisRevised"}
Q_QUANTITY = {
    0: "ProgressP",
    1: "AmplitudeA",
    2: "DurationD",
    3: "PathLengthL",
    4: "EfficiencyE",
    5: "CounterC",
}
Q_AVAILABILITY = {
    0: "QuantityKnown",
    1: "EndpointUnavailable",
    2: "ClockUnavailable",
    3: "PathUnavailable",
    4: "ZeroPathNotApplicable",
}
Q_END_REASON = {
    0: "DirectionalRevisionDutyEnded",
    1: "DirectionalScopeEnded",
}


@dataclass(frozen=True)
class QDisplayFrames:
    """Canonical frames consumed by the C3 plotters."""

    timeline: pd.DataFrame
    revision_links: pd.DataFrame
    states: pd.DataFrame
    members: pd.DataFrame
    quantities: pd.DataFrame
    audit: pd.DataFrame
    definition: Mapping[str, Any]

    def validate(self) -> None:
        required = {
            "timeline": {
                "event_uti",
                "event_kind",
                "event_id",
                "q_life",
                "q_revision",
                "previous_ref",
                "candidate_ref",
                "members",
                "known_uti",
                "qualification",
                "observation",
                "applicability",
                "end_reason",
                "last_successful_ref",
                "detail",
            },
            "revision_links": {
                "from_uti",
                "to_uti",
                "q_life",
                "from_revision",
                "to_revision",
            },
            "states": {
                "publication_uti",
                "q_life",
                "q_revision",
                "state_kind",
                "state_value",
                "detail",
            },
            "members": {
                "publication_uti",
                "q_life",
                "q_revision",
                "member",
                "asked_uti",
                "asked_price",
                "used_uti",
                "used_price",
                "successor_uti",
                "successor_price",
                "endpoint_uti",
                "endpoint_price",
                "completion",
                "verdict",
                "basis",
                "path_complete",
                "through",
                "material_known",
                "missing_range",
                "candidate_ref",
            },
            "quantities": {
                "publication_uti",
                "q_life",
                "q_revision",
                "member",
                "quantity_kind",
                "quantity_value",
                "availability",
            },
            "audit": {
                "event_uti",
                "event_id",
                "event_kind",
                "previous_ref",
                "candidate_ref",
                "publication_or_end_known",
                "detail",
            },
        }
        for name, columns in required.items():
            frame = getattr(self, name)
            if not isinstance(frame, pd.DataFrame):
                raise TypeError(f"{name} must be a DataFrame")
            missing = columns - set(frame.columns)
            if missing:
                raise ValueError(f"{name} missing columns: {sorted(missing)}")

        if not set(self.timeline["event_kind"]).issubset(
            {"F candidate", "Q revision", "Duty end"}
        ):
            raise ValueError("timeline contains an unknown event kind")

        q_rows = self.timeline[self.timeline.event_kind.eq("Q revision")]
        if q_rows["event_id"].duplicated().any():
            raise ValueError("one Q exact appears on multiple publication rows")
        if self.members.groupby(["q_life", "q_revision"]).size().lt(2).any():
            raise ValueError("a Q occurrence has fewer than two members")

        expected_kinds = tuple(Q_QUANTITY.values())
        member_keys = {
            (str(row.q_life), str(row.q_revision), str(row.member))
            for row in self.members.itertuples(index=False)
        }
        quantity_keys = {
            tuple(map(str, key))
            for key, _frame in self.quantities.groupby(
                ["q_life", "q_revision", "member"], dropna=False
            )
        }
        if member_keys != quantity_keys:
            raise ValueError(
                "member/quantity identity mismatch: "
                f"members_only={sorted(member_keys-quantity_keys)!r}, "
                f"quantities_only={sorted(quantity_keys-member_keys)!r}"
            )

        for key, frame in self.quantities.groupby(
            ["q_life", "q_revision", "member"], dropna=False
        ):
            kinds = tuple(frame["quantity_kind"])
            if kinds != expected_kinds:
                raise ValueError(
                    f"{key}: quantity order/content {kinds!r}, expected {expected_kinds!r}"
                )
            known = frame.availability.eq("QuantityKnown")
            if frame.loc[known, "quantity_value"].isna().any():
                raise ValueError(f"{key}: QuantityKnown without a value")
            if frame.loc[~known, "quantity_value"].notna().any():
                raise ValueError(f"{key}: unavailable quantity has a numeric value")

        if self.definition.get("objects") != list(OBJECTS):
            raise ValueError(
                f"stored object binding {self.definition.get('objects')} != {OBJECTS}"
            )


@dataclass(frozen=True)
class QPositionBinding:
    sof_name: str
    block: str
    calendar_name: str
    objects: Sequence[str]
    timespans: Sequence[tuple[str, str]]

    def validate(self) -> None:
        if self.sof_name != SOF_NAME or self.block != BLOCK:
            raise ValueError("D binding must use the accepted B SOF/block")
        if self.calendar_name != CALENDAR:
            raise ValueError("D binding must use the accepted B calendar")
        if tuple(self.objects) != OBJECTS:
            raise ValueError("D binding must use the exact Q object universe")
        if tuple(self.timespans) != TIMESPANS:
            raise ValueError("D binding must use the accepted inclusive B date interval")


@dataclass(frozen=True)
class QDisplayBinding:
    q_feature: Any
    price_feature: Any
    frames: QDisplayFrames
    position: QPositionBinding
    graph_name: str
    plot_name: str

    def validate(self) -> None:
        self.position.validate()
        self.frames.validate()


def _as_tuple(index: Any) -> tuple[Any, ...]:
    return index if isinstance(index, tuple) else (index,)


def _parent(index: Any, nlevels: int) -> tuple[Any, ...]:
    value = _as_tuple(index)
    if len(value) < nlevels:
        raise ValueError(f"index {value!r} is shallower than parent depth {nlevels}")
    return value[:nlevels]


def _single_by_parent(
    frame: pd.DataFrame, parent_levels: int, label: str
) -> dict[tuple[Any, ...], pd.Series]:
    grouped: dict[tuple[Any, ...], list[pd.Series]] = {}
    for index, row in frame.iterrows():
        grouped.setdefault(_parent(index, parent_levels), []).append(row)
    bad = {key: len(rows) for key, rows in grouped.items() if len(rows) > 1}
    if bad:
        raise ValueError(f"{label} is not optional-single: {bad}")
    return {key: rows[0] for key, rows in grouped.items()}


def _many_by_parent(
    frame: pd.DataFrame, parent_levels: int
) -> dict[tuple[Any, ...], list[pd.Series]]:
    grouped: dict[tuple[Any, ...], list[pd.Series]] = {}
    for index, row in frame.iterrows():
        grouped.setdefault(_parent(index, parent_levels), []).append(row)
    return grouped


def _enum(row: pd.Series, field: str, mapping: Mapping[int, str]) -> str:
    named = field + "_name"
    if named in row and not pd.isna(row[named]):
        return str(row[named])
    raw = int(row[field])
    if raw not in mapping:
        raise ValueError(f"unknown {field} code: {raw}")
    return mapping[raw]


def _exact(book: str, kind: str, life: str, revision: str) -> tuple[str, ...]:
    return (book, kind, life, revision)


def _ref_text(reference: Sequence[Any] | None) -> str | None:
    if reference is None:
        return None
    return "/".join(map(str, reference))


def _row_uuid(row: pd.Series, field: str) -> str:
    return str(_uuid(row, field))


def _q_exact(row: pd.Series) -> tuple[str, ...]:
    return _exact(
        Q_BOOK,
        Q_KIND,
        _row_uuid(row, "organizationReference_referenceLife"),
        _row_uuid(row, "organizationReference_referenceRevision"),
    )


def _candidate_exact(row: pd.Series) -> tuple[str, ...]:
    return _exact(
        F_BOOK,
        F_KIND,
        _row_uuid(row, "organizationCandidate_referenceLife"),
        _row_uuid(row, "organizationCandidate_referenceRevision"),
    )


def _previous_exact(row: pd.Series) -> tuple[str, ...]:
    return _exact(
        Q_BOOK,
        Q_KIND,
        _row_uuid(row, "referenceLife"),
        _row_uuid(row, "referenceRevision"),
    )


def _f_exact(row: pd.Series) -> tuple[str, ...]:
    return _exact(
        F_BOOK,
        F_KIND,
        _row_uuid(row, "groupReference_referenceLife"),
        _row_uuid(row, "groupReference_referenceRevision"),
    )


def _event_uti_from_index(index: Any, natural_tsa: np.ndarray) -> int:
    raw = _as_tuple(index)[0]
    if isinstance(raw, (int, np.integer)) and not isinstance(raw, (bool, np.bool_)):
        position = int(raw)
        if not 0 <= position < len(natural_tsa):
            raise ValueError(f"event UTI {position} is outside {CALENDAR}")
        return position
    timestamp = pd.Timestamp(raw).to_datetime64()
    position = int(np.searchsorted(natural_tsa, timestamp))
    if position >= len(natural_tsa) or natural_tsa[position] != timestamp:
        raise ValueError(f"event timestamp {timestamp!s} is not on {CALENDAR}")
    return position


def _optional_number(row: pd.Series | None, field: str) -> float | None:
    if row is None or field not in row or pd.isna(row[field]):
        return None
    value = float(row[field])
    if not math.isfinite(value):
        raise ValueError(f"{field} is not finite")
    return value


def _optional_int(row: pd.Series | None, field: str) -> int | None:
    if row is None or field not in row or pd.isna(row[field]):
        return None
    return int(row[field])


def _safe_text(value: Any) -> str:
    if value is None or value is pd.NA:
        return ""
    try:
        if pd.isna(value):
            return ""
    except (TypeError, ValueError):
        pass
    return str(value)

# Export private integration helpers intentionally; these modules are one locked definition.
__all__ = [name for name in globals() if not name.startswith("__")]
