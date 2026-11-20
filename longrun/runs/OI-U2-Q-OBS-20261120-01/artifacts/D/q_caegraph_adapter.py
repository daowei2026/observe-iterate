"""Exact F/Q occurrence adapter for the D004 integrated Q CAEGraph definition."""
from q_caegraph_common import *
from q_caegraph_adapter_support import load_adapter_tables
from q_caegraph_adapter_members import collect_member_rows


TIMELINE_COLUMNS = [
    "event_uti", "event_kind", "event_id", "q_life", "q_revision",
    "previous_ref", "candidate_ref", "members", "known_uti",
    "qualification", "observation", "applicability", "end_reason",
    "last_successful_ref", "detail",
]
MEMBER_COLUMNS = [
    "publication_uti", "q_life", "q_revision", "member",
    "asked_uti", "asked_price", "asked_confirmation", "asked_known",
    "asked_clock", "asked_clock_known",
    "used_uti", "used_price", "used_confirmation", "used_known",
    "used_clock", "used_clock_known",
    "successor_uti", "successor_price", "successor_confirmation",
    "successor_known", "successor_clock", "successor_clock_known",
    "endpoint_uti", "endpoint_price", "endpoint_known",
    "endpoint_clock", "endpoint_clock_known",
    "completion", "verdict", "basis", "path_complete", "through",
    "material_known", "missing_range", "candidate_ref",
]
QUANTITY_COLUMNS = [
    "publication_uti", "q_life", "q_revision", "member",
    "quantity_kind", "quantity_value", "availability",
]


def _f_exact_index(tables: Any) -> dict[tuple[str, ...], tuple[Any, pd.Series, list[str]]]:
    result: dict[tuple[str, ...], tuple[Any, pd.Series, list[str]]] = {}
    for index, row in tables.f_occ.iterrows():
        exact = _f_exact(row)
        if exact in result:
            raise ValueError(f"duplicate formal F exact: {_ref_text(exact)}")
        names = sorted(
            str(member["memberObject"])
            for _, member in tables.f_member_records_by_f.get(_as_tuple(index), [])
        )
        result[exact] = (index, row, names)
    return result


def read_q_display_frames(q_feature: Any) -> QDisplayFrames:
    """Read exact formal F/Q products and form the C3 canonical frames."""
    t = load_adapter_tables(q_feature)
    f_by_exact = _f_exact_index(t)
    timeline_rows: list[dict[str, Any]] = []
    state_rows: list[dict[str, Any]] = []
    member_rows: list[dict[str, Any]] = []
    quantity_rows: list[dict[str, Any]] = []
    audit_rows: list[dict[str, Any]] = []
    q_by_exact: dict[tuple[str, ...], dict[str, Any]] = {}
    previous_by_exact: dict[tuple[str, ...], tuple[str, ...] | None] = {}
    candidate_refs: set[tuple[str, ...]] = set()

    for q_index, q_row in t.q_occ.iterrows():
        q_key = _as_tuple(q_index)
        exact = _q_exact(q_row)
        if exact in q_by_exact:
            raise ValueError(f"duplicate formal Q exact: {_ref_text(exact)}")
        candidate = _candidate_exact(q_row)
        candidate_refs.add(candidate)
        previous_record = t.previous_by_q.get(q_key)
        previous = (
            _previous_exact(previous_record[1])
            if previous_record is not None else None
        )
        if previous is not None and previous[2] != exact[2]:
            raise ValueError("Q Previous crosses Q Life")

        publication_uti = _event_uti_from_index(q_index, t.natural_tsa)
        known = int(q_row["organizationKnownFrom"])
        qualification = _enum(
            q_row, "organizationQualification", Q_QUALIFICATION
        )
        observation = _enum(
            q_row, "organizationObservation", Q_OBSERVATION
        )
        applicability = _enum(
            q_row, "organizationApplicability", Q_APPLICABILITY
        )
        event_id = str(_ref_text(exact))
        members, quantities, names = collect_member_rows(
            t, q_key, exact, candidate, publication_uti, event_id
        )
        member_rows.extend(members)
        quantity_rows.extend(quantities)
        detail = (
            f"known={known}; original=[{q_row['organizationOriginalAnchor']},"
            f"{q_row['organizationOriginalDeadline']},"
            f"{q_row['organizationOriginalRevisionEnd']}]; current=["
            f"{q_row['organizationAnchor']},{q_row['organizationDeadline']},"
            f"{q_row['organizationRevisionEnd']}]"
        )
        record = {
            "event_uti": publication_uti,
            "event_kind": "Q revision",
            "event_id": event_id,
            "q_life": exact[2],
            "q_revision": exact[3],
            "previous_ref": _ref_text(previous),
            "candidate_ref": _ref_text(candidate),
            "members": ",".join(names),
            "known_uti": known,
            "qualification": qualification,
            "observation": observation,
            "applicability": applicability,
            "end_reason": None,
            "last_successful_ref": None,
            "detail": detail,
        }
        timeline_rows.append(record)
        q_by_exact[exact] = record
        previous_by_exact[exact] = previous
        for kind, value in (
            ("qualification", qualification),
            ("observation", observation),
            ("applicability", applicability),
        ):
            state_rows.append(
                {
                    "publication_uti": publication_uti,
                    "q_life": exact[2],
                    "q_revision": exact[3],
                    "state_kind": kind,
                    "state_value": value,
                    "detail": detail,
                }
            )
        audit_rows.append(
            {
                "event_uti": publication_uti,
                "event_id": event_id,
                "event_kind": "Q revision",
                "previous_ref": _ref_text(previous),
                "candidate_ref": _ref_text(candidate),
                "publication_or_end_known": known,
                "detail": (
                    f"{qualification}; {observation}; {applicability}; "
                    f"members={','.join(names)}"
                ),
            }
        )

    # Real F occurrences are the upstream input events, not Q-derived pseudo-events.
    for candidate in sorted(candidate_refs):
        if candidate not in f_by_exact:
            raise ValueError(
                f"Q references F exact absent from formal F output: "
                f"{_ref_text(candidate)}"
            )
        index, row, names = f_by_exact[candidate]
        event_uti = _event_uti_from_index(index, t.natural_tsa)
        known = int(row["groupKnownFrom"])
        timeline_rows.append(
            {
                "event_uti": event_uti,
                "event_kind": "F candidate",
                "event_id": _ref_text(candidate),
                "q_life": None,
                "q_revision": None,
                "previous_ref": None,
                "candidate_ref": _ref_text(candidate),
                "members": ",".join(names),
                "known_uti": known,
                "qualification": None,
                "observation": _safe_text(row.get("groupObservation_name")),
                "applicability": None,
                "end_reason": None,
                "last_successful_ref": None,
                "detail": f"F candidate known={known}; members={','.join(names)}",
            }
        )
        audit_rows.append(
            {
                "event_uti": event_uti,
                "event_id": _ref_text(candidate),
                "event_kind": "F candidate",
                "previous_ref": None,
                "candidate_ref": _ref_text(candidate),
                "publication_or_end_known": known,
                "detail": "formal F candidate occurrence",
            }
        )

    # A duty end is a separate lifecycle occurrence, never a Q revision.
    for index, row in t.duty_ends.iterrows():
        last = _exact(
            Q_BOOK, Q_KIND,
            _row_uuid(row, "lastReference_referenceLife"),
            _row_uuid(row, "lastReference_referenceRevision"),
        )
        candidate = _exact(
            F_BOOK, F_KIND,
            _row_uuid(row, "lastCandidate_referenceLife"),
            _row_uuid(row, "lastCandidate_referenceRevision"),
        )
        if last not in q_by_exact:
            raise ValueError(
                "duty end references absent last-successful Q: "
                + str(_ref_text(last))
            )
        event_uti = _event_uti_from_index(index, t.natural_tsa)
        end_known = int(row["organizationEndKnown"])
        end_progress = float(row["organizationEndProgress"])
        reason = _enum(row, "organizationEndReason", Q_END_REASON)
        event_id = f"DutyEnd/{last[2]}/{last[3]}/{event_uti}"
        timeline_rows.append(
            {
                "event_uti": event_uti,
                "event_kind": "Duty end",
                "event_id": event_id,
                "q_life": last[2],
                "q_revision": last[3],
                "previous_ref": None,
                "candidate_ref": _ref_text(candidate),
                "members": q_by_exact[last]["members"],
                "known_uti": end_known,
                "qualification": None,
                "observation": None,
                "applicability": None,
                "end_reason": reason,
                "last_successful_ref": _ref_text(last),
                "detail": (
                    f"{reason}; end_known={end_known}; "
                    f"end_progress={end_progress}; no new Q revision"
                ),
            }
        )
        audit_rows.append(
            {
                "event_uti": event_uti,
                "event_id": event_id,
                "event_kind": "Duty end",
                "previous_ref": None,
                "candidate_ref": _ref_text(candidate),
                "publication_or_end_known": end_known,
                "detail": (
                    f"{reason}; last_successful={_ref_text(last)}; "
                    f"end_progress={end_progress}; no new Q revision"
                ),
            }
        )

    revision_rows: list[dict[str, Any]] = []
    for exact, record in q_by_exact.items():
        previous = previous_by_exact[exact]
        if previous is None:
            continue
        if previous not in q_by_exact:
            raise ValueError(
                "Q Previous absent from formal Q output: "
                + str(_ref_text(previous))
            )
        revision_rows.append(
            {
                "from_uti": int(q_by_exact[previous]["event_uti"]),
                "to_uti": int(record["event_uti"]),
                "q_life": exact[2],
                "from_revision": previous[3],
                "to_revision": exact[3],
            }
        )

    timeline = pd.DataFrame(timeline_rows, columns=TIMELINE_COLUMNS)
    if len(timeline):
        order = {"F candidate": 0, "Q revision": 1, "Duty end": 2}
        timeline["_kind_order"] = timeline.event_kind.map(order)
        timeline = (
            timeline.sort_values(["event_uti", "_kind_order", "event_id"])
            .drop(columns="_kind_order")
            .reset_index(drop=True)
        )

    frames = QDisplayFrames(
        timeline=timeline,
        revision_links=pd.DataFrame(
            revision_rows,
            columns=[
                "from_uti", "to_uti", "q_life",
                "from_revision", "to_revision",
            ],
        ),
        states=pd.DataFrame(
            state_rows,
            columns=[
                "publication_uti", "q_life", "q_revision",
                "state_kind", "state_value", "detail",
            ],
        ),
        members=pd.DataFrame(member_rows, columns=MEMBER_COLUMNS),
        quantities=pd.DataFrame(quantity_rows, columns=QUANTITY_COLUMNS),
        audit=pd.DataFrame(
            audit_rows,
            columns=[
                "event_uti", "event_id", "event_kind", "previous_ref",
                "candidate_ref", "publication_or_end_known", "detail",
            ],
        ),
        definition=t.definition,
    )
    frames.validate()
    return frames


__all__ = [name for name in globals() if not name.startswith("__")]
