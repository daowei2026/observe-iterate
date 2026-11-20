"""Locked-table loading and parent-coordinate indexes for the Q display adapter."""
from dataclasses import dataclass
from q_caegraph_common import *


def _read_duty_ends(q_feature: Any) -> pd.DataFrame:
    """Read v2 duty ends from the locked physical layout.

    tis@2f460d... loads core.v2, but its current DIRECTIONAL_TABLES registry
    does not expose organizationDutyEnds. These fields are the unique direct
    projection of DirectionalDutyEndRecord in frp@67711c....
    """
    fields = {
        "lastReference_referenceLife_idForm":
            "mul.organizationDutyEnds.organizationEndLast.organizationReference.referenceLife.idForm",
        "lastReference_referenceLife_idHigh":
            "mul.organizationDutyEnds.organizationEndLast.organizationReference.referenceLife.idHigh",
        "lastReference_referenceLife_idLow":
            "mul.organizationDutyEnds.organizationEndLast.organizationReference.referenceLife.idLow",
        "lastReference_referenceLife_idText":
            "mul.organizationDutyEnds.organizationEndLast.organizationReference.referenceLife.idText",
        "lastReference_referenceRevision_idForm":
            "mul.organizationDutyEnds.organizationEndLast.organizationReference.referenceRevision.idForm",
        "lastReference_referenceRevision_idHigh":
            "mul.organizationDutyEnds.organizationEndLast.organizationReference.referenceRevision.idHigh",
        "lastReference_referenceRevision_idLow":
            "mul.organizationDutyEnds.organizationEndLast.organizationReference.referenceRevision.idLow",
        "lastReference_referenceRevision_idText":
            "mul.organizationDutyEnds.organizationEndLast.organizationReference.referenceRevision.idText",
        "lastCandidate_referenceLife_idForm":
            "mul.organizationDutyEnds.organizationEndLast.organizationCandidate.referenceLife.idForm",
        "lastCandidate_referenceLife_idHigh":
            "mul.organizationDutyEnds.organizationEndLast.organizationCandidate.referenceLife.idHigh",
        "lastCandidate_referenceLife_idLow":
            "mul.organizationDutyEnds.organizationEndLast.organizationCandidate.referenceLife.idLow",
        "lastCandidate_referenceLife_idText":
            "mul.organizationDutyEnds.organizationEndLast.organizationCandidate.referenceLife.idText",
        "lastCandidate_referenceRevision_idForm":
            "mul.organizationDutyEnds.organizationEndLast.organizationCandidate.referenceRevision.idForm",
        "lastCandidate_referenceRevision_idHigh":
            "mul.organizationDutyEnds.organizationEndLast.organizationCandidate.referenceRevision.idHigh",
        "lastCandidate_referenceRevision_idLow":
            "mul.organizationDutyEnds.organizationEndLast.organizationCandidate.referenceRevision.idLow",
        "lastCandidate_referenceRevision_idText":
            "mul.organizationDutyEnds.organizationEndLast.organizationCandidate.referenceRevision.idText",
        "lastKnownFrom":
            "mul.organizationDutyEnds.organizationEndLast.organizationKnownFrom",
        "organizationEndReason": "mul.organizationDutyEnds.organizationEndReason",
        "organizationEndKnown": "mul.organizationDutyEnds.organizationEndKnown",
        "organizationEndProgress": "mul.organizationDutyEnds.organizationEndProgress",
    }
    frame = q_feature._event_df(q_feature.P.result_layout, fields, 3)
    if len(frame):
        unknown = set(map(int, frame.organizationEndReason)) - set(Q_END_REASON)
        if unknown:
            raise ValueError(f"unknown duty-end reason codes: {sorted(unknown)}")
        frame = frame.copy()
        frame["organizationEndReason_name"] = (
            frame["organizationEndReason"].map(Q_END_REASON).astype("string")
        )
    return frame


def _validate_definition(
    definitions: pd.DataFrame, bindings: pd.DataFrame
) -> dict[str, Any]:
    if len(definitions) != 1:
        raise ValueError(f"expected exactly one Q definition, got {len(definitions)}")
    row = definitions.iloc[0]
    direction = _enum(row, "organizationDirection", Q_DIRECTION)
    delta = float(row["organizationDelta"])
    observation = int(row["organizationObservationMultiples"])
    revision = int(row["organizationRevisionMultiples"])
    minimum = int(row["organizationMinimumMultiples"])
    stored_objects = list(map(str, bindings["bindingObject"]))
    if direction != "DirectionUp":
        raise ValueError(f"stored Q direction is {direction}, expected DirectionUp")
    if not math.isfinite(delta) or delta != float(PARAMS["delta"]):
        raise ValueError(f"stored delta {delta} != {PARAMS['delta']}")
    if (observation, revision, minimum) != (12, 6, 2):
        raise ValueError(
            "stored Q method contract is not observation=12/revision=6/minimum=2"
        )
    if (
        len(stored_objects) != len(set(stored_objects))
        or set(stored_objects) != set(OBJECTS)
    ):
        raise ValueError(
            f"stored Q bindings {stored_objects!r} != object universe "
            f"{list(OBJECTS)!r}"
        )
    return {
        "direction": direction,
        "delta": delta,
        "observation_multiples": observation,
        "revision_multiples": revision,
        "minimum_members": minimum,
        "objects": list(OBJECTS),
        "stored_binding_order": stored_objects,
        "domain": _safe_text(row.get("organizationDomain")),
        "time_unit": _safe_text(row.get("organizationTimeUnit")),
    }


def _records_by_parent(
    frame: pd.DataFrame, parent_levels: int
) -> dict[tuple[Any, ...], list[tuple[tuple[Any, ...], pd.Series]]]:
    grouped: dict[
        tuple[Any, ...], list[tuple[tuple[Any, ...], pd.Series]]
    ] = {}
    for index, row in frame.iterrows():
        full = _as_tuple(index)
        grouped.setdefault(_parent(full, parent_levels), []).append((full, row))
    return grouped


def _single_record_by_parent(
    frame: pd.DataFrame, parent_levels: int, label: str
) -> dict[tuple[Any, ...], tuple[tuple[Any, ...], pd.Series]]:
    grouped = _records_by_parent(frame, parent_levels)
    bad = {key: len(rows) for key, rows in grouped.items() if len(rows) > 1}
    if bad:
        raise ValueError(f"{label} is not optional-single: {bad}")
    return {key: rows[0] for key, rows in grouped.items()}


@dataclass(frozen=True)
class QAdapterTables:
    definition: Mapping[str, Any]
    natural_tsa: np.ndarray
    duty_ends: pd.DataFrame
    q_occ: pd.DataFrame
    f_occ: pd.DataFrame
    q_parent_levels: int
    f_parent_levels: int
    member_levels: int
    previous_by_q: Mapping[tuple[Any, ...], tuple[tuple[Any, ...], pd.Series]]
    q_member_records_by_q: Mapping[
        tuple[Any, ...], list[tuple[tuple[Any, ...], pd.Series]]
    ]
    f_member_records_by_f: Mapping[
        tuple[Any, ...], list[tuple[tuple[Any, ...], pd.Series]]
    ]
    successors: Mapping[tuple[Any, ...], tuple[tuple[Any, ...], pd.Series]]
    endpoints: Mapping[tuple[Any, ...], tuple[tuple[Any, ...], pd.Series]]
    missing_ranges: Mapping[tuple[Any, ...], tuple[tuple[Any, ...], pd.Series]]
    asked_clocks: Mapping[tuple[Any, ...], tuple[tuple[Any, ...], pd.Series]]
    used_clocks: Mapping[tuple[Any, ...], tuple[tuple[Any, ...], pd.Series]]
    successor_clocks: Mapping[tuple[Any, ...], tuple[tuple[Any, ...], pd.Series]]
    endpoint_prices: Mapping[tuple[Any, ...], tuple[tuple[Any, ...], pd.Series]]
    endpoint_clocks: Mapping[tuple[Any, ...], tuple[tuple[Any, ...], pd.Series]]
    quantity_records_by_member: Mapping[
        tuple[Any, ...], list[tuple[tuple[Any, ...], pd.Series]]
    ]
    quantity_numbers: Mapping[
        tuple[Any, ...], tuple[tuple[Any, ...], pd.Series]
    ]


def load_adapter_tables(q_feature: Any) -> QAdapterTables:
    formation = q_feature.P.formation
    q = q_feature.to_dfs(list(Q_PRODUCTS))
    f = formation.to_dfs(list(F_PRODUCTS))
    definition = _validate_definition(
        q["definitions"], q["definitions_organizationBindings"]
    )
    natural_tsa = CurrSof.sof().tsa_of(CALENDAR)["natural_tsa"]
    q_occ = q["occurrences"]
    f_occ = f["occurrences"]
    q_members = q["occurrences_organizationMembers"]
    q_parent_levels = q_occ.index.nlevels
    f_parent_levels = f_occ.index.nlevels
    member_levels = q_members.index.nlevels

    successors = _single_record_by_parent(
        q["occurrences_organizationMembers_organizationSuccessor"],
        member_levels, "member successor"
    )
    endpoints = _single_record_by_parent(
        q["occurrences_organizationMembers_organizationEndpoint"],
        member_levels, "member endpoint"
    )
    successor_depth = (
        q["occurrences_organizationMembers_organizationSuccessor"].index.nlevels
    )
    endpoint_depth = (
        q["occurrences_organizationMembers_organizationEndpoint"].index.nlevels
    )
    quantity_table = q[
        "occurrences_organizationMembers_organizationQuantities"
    ]
    quantity_depth = quantity_table.index.nlevels

    return QAdapterTables(
        definition=definition,
        natural_tsa=natural_tsa,
        duty_ends=_read_duty_ends(q_feature),
        q_occ=q_occ,
        f_occ=f_occ,
        q_parent_levels=q_parent_levels,
        f_parent_levels=f_parent_levels,
        member_levels=member_levels,
        previous_by_q=_single_record_by_parent(
            q["occurrences_organizationPrevious"], q_parent_levels, "Q Previous"
        ),
        q_member_records_by_q=_records_by_parent(q_members, q_parent_levels),
        f_member_records_by_f=_records_by_parent(
            f["occurrences_groupMembers"], f_parent_levels
        ),
        successors=successors,
        endpoints=endpoints,
        missing_ranges=_single_record_by_parent(
            q["occurrences_organizationMembers_organizationMissingRange"],
            member_levels, "member missing range"
        ),
        asked_clocks=_single_record_by_parent(
            q[
                "occurrences_organizationMembers_organizationAskedTurn_motionClock"
            ],
            member_levels, "asked clock"
        ),
        used_clocks=_single_record_by_parent(
            q[
                "occurrences_organizationMembers_organizationUsedTurn_motionClock"
            ],
            member_levels, "used clock"
        ),
        successor_clocks=_single_record_by_parent(
            q[
                "occurrences_organizationMembers_organizationSuccessor_motionClock"
            ],
            successor_depth, "successor clock"
        ),
        endpoint_prices=_single_record_by_parent(
            q[
                "occurrences_organizationMembers_organizationEndpoint_endpointPrice"
            ],
            endpoint_depth, "endpoint price"
        ),
        endpoint_clocks=_single_record_by_parent(
            q[
                "occurrences_organizationMembers_organizationEndpoint_endpointClock"
            ],
            endpoint_depth, "endpoint clock"
        ),
        quantity_records_by_member=_records_by_parent(
            quantity_table, member_levels
        ),
        quantity_numbers=_single_record_by_parent(
            q[
                "occurrences_organizationMembers_organizationQuantities_motionNumber"
            ],
            quantity_depth, "quantity number"
        ),
    )


__all__ = [name for name in globals() if not name.startswith("__")]
