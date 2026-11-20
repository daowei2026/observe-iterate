"""Member geometry and six-quantity extraction for the Q display adapter."""
from q_caegraph_common import *
from q_caegraph_adapter_support import QAdapterTables


def _record_row(
    value: tuple[tuple[Any, ...], pd.Series] | None
) -> pd.Series | None:
    return None if value is None else value[1]


def collect_member_rows(
    tables: QAdapterTables,
    q_key: tuple[Any, ...],
    exact: tuple[str, ...],
    candidate: tuple[str, ...],
    publication_uti: int,
    event_id: str,
) -> tuple[list[dict[str, Any]], list[dict[str, Any]], list[str]]:
    members: list[dict[str, Any]] = []
    quantities: list[dict[str, Any]] = []
    names: list[str] = []

    for member_key, member_row in tables.q_member_records_by_q.get(q_key, []):
        member_name = str(member_row["organizationObject"])
        names.append(member_name)
        successor_record = tables.successors.get(member_key)
        endpoint_record = tables.endpoints.get(member_key)
        successor_key = None if successor_record is None else successor_record[0]
        endpoint_key = None if endpoint_record is None else endpoint_record[0]
        successor = _record_row(successor_record)
        endpoint = _record_row(endpoint_record)
        missing = _record_row(tables.missing_ranges.get(member_key))
        asked_clock = _record_row(tables.asked_clocks.get(member_key))
        used_clock = _record_row(tables.used_clocks.get(member_key))
        successor_clock = _record_row(
            tables.successor_clocks.get(successor_key)
            if successor_key is not None else None
        )
        endpoint_price = _record_row(
            tables.endpoint_prices.get(endpoint_key)
            if endpoint_key is not None else None
        )
        endpoint_clock = _record_row(
            tables.endpoint_clocks.get(endpoint_key)
            if endpoint_key is not None else None
        )
        missing_text = None
        if missing is not None:
            missing_text = (
                f"{int(missing['missingActualFrom'])}:"
                f"{int(missing['missingActualThrough'])}"
            )

        members.append(
            {
                "publication_uti": publication_uti,
                "q_life": exact[2],
                "q_revision": exact[3],
                "member": member_name,
                "asked_uti": int(
                    member_row["organizationAskedTurn_motionActual"]
                ),
                "asked_price": float(
                    member_row["organizationAskedTurn_motionPrice"]
                ),
                "asked_confirmation": int(
                    member_row["organizationAskedTurn_motionConfirmation"]
                ),
                "asked_known": int(
                    member_row["organizationAskedTurn_motionKnownFrom"]
                ),
                "asked_clock": _optional_number(
                    asked_clock, "clockCoordinate"
                ),
                "asked_clock_known": _optional_int(
                    asked_clock, "clockKnownFrom"
                ),
                "used_uti": int(
                    member_row["organizationUsedTurn_motionActual"]
                ),
                "used_price": float(
                    member_row["organizationUsedTurn_motionPrice"]
                ),
                "used_confirmation": int(
                    member_row["organizationUsedTurn_motionConfirmation"]
                ),
                "used_known": int(
                    member_row["organizationUsedTurn_motionKnownFrom"]
                ),
                "used_clock": _optional_number(
                    used_clock, "clockCoordinate"
                ),
                "used_clock_known": _optional_int(
                    used_clock, "clockKnownFrom"
                ),
                "successor_uti": _optional_int(successor, "motionActual"),
                "successor_price": _optional_number(successor, "motionPrice"),
                "successor_confirmation": _optional_int(
                    successor, "motionConfirmation"
                ),
                "successor_known": _optional_int(
                    successor, "motionKnownFrom"
                ),
                "successor_clock": _optional_number(
                    successor_clock, "clockCoordinate"
                ),
                "successor_clock_known": _optional_int(
                    successor_clock, "clockKnownFrom"
                ),
                "endpoint_uti": _optional_int(endpoint, "endpointActual"),
                "endpoint_price": _optional_number(
                    endpoint_price, "motionValue"
                ),
                "endpoint_known": _optional_int(
                    endpoint, "endpointKnownFrom"
                ),
                "endpoint_clock": _optional_number(
                    endpoint_clock, "clockCoordinate"
                ),
                "endpoint_clock_known": _optional_int(
                    endpoint_clock, "clockKnownFrom"
                ),
                "completion": _enum(
                    member_row, "organizationCompletion", Q_COMPLETION
                ),
                "verdict": _enum(
                    member_row, "organizationVerdict", Q_VERDICT
                ),
                "basis": _enum(
                    member_row, "organizationBasis", Q_BASIS
                ),
                "path_complete": bool(
                    int(member_row["organizationPathComplete"])
                ),
                "through": float(member_row["organizationThrough"]),
                "material_known": int(
                    member_row["organizationMaterialKnownFrom"]
                ),
                "missing_range": missing_text,
                "candidate_ref": _ref_text(candidate),
            }
        )

        qrecords = tables.quantity_records_by_member.get(member_key, [])
        if len(qrecords) != 6:
            raise ValueError(
                f"{event_id}/{member_name}: expected six quantity records"
            )
        for quantity_key, quantity_row in qrecords:
            number = _record_row(tables.quantity_numbers.get(quantity_key))
            quantities.append(
                {
                    "publication_uti": publication_uti,
                    "q_life": exact[2],
                    "q_revision": exact[3],
                    "member": member_name,
                    "quantity_kind": _enum(
                        quantity_row, "motionQuantity", Q_QUANTITY
                    ),
                    "quantity_value": _optional_number(
                        number, "motionValue"
                    ),
                    "availability": _enum(
                        quantity_row,
                        "motionAvailability",
                        Q_AVAILABILITY,
                    ),
                }
            )

    if len(names) < 2 or len(names) != len(set(names)):
        raise ValueError(f"{event_id}: invalid member identity {names!r}")
    return members, quantities, names


__all__ = [name for name in globals() if not name.startswith("__")]
