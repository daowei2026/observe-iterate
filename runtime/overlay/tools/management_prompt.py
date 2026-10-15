"""Generic coordinator prompt assembler.

This module performs deterministic text assembly only. It has no scheduler,
phone integration, authority inference, or professional-judgment capability.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Iterable

ROLE_MARKERS: dict[str, str] = {
    "management": "MANAGEMENT_DUTY",
    "professional": "PROFESSIONAL_DUTY",
    "review": "REVIEW_DUTY",
    "receiver": "REVIEW_DUTY",
    "worker": "WORKER_DUTY",
}


def marked(body: str, name: str) -> str:
    """Return the one text block delimited by the named HTML markers."""
    begin = f"<!-- {name}_BEGIN -->"
    end = f"<!-- {name}_END -->"
    if body.count(begin) != 1 or body.count(end) != 1:
        raise ValueError(f"MARKER_MISSING_OR_DUPLICATE:{name}")
    start = body.index(begin) + len(begin)
    stop = body.index(end, start)
    text = body[start:stop].strip()
    if not text:
        raise ValueError(f"EMPTY_MARKER:{name}")
    return text


def prepare(
    policy_path: str | Path,
    config_path: str | Path,
    work_id: str,
    role: str,
    task_text: str,
    refs: Iterable[str],
) -> dict[str, str]:
    """Assemble an exact role prompt from a policy block and authorized task text."""
    if role not in ROLE_MARKERS:
        raise ValueError(f"UNSUPPORTED_ROLE:{role}")
    if not task_text.strip():
        raise ValueError("EMPTY_TASK_TEXT")

    policy = Path(policy_path).read_text(encoding="utf-8")
    config = json.loads(Path(config_path).read_text(encoding="utf-8"))
    try:
        work = config["works"][work_id]
    except (KeyError, TypeError) as exc:
        raise ValueError(f"UNKNOWN_WORK:{work_id}") from exc

    ref_lines = [f"- {ref}" for ref in refs if str(ref).strip()]
    source_block = "来源：\n" + ("\n".join(ref_lines) if ref_lines else "- 未提供；必须返回原责任者补齐")
    payload = "\n\n".join(
        [
            marked(policy, ROLE_MARKERS[role]),
            task_text.strip(),
            source_block,
        ]
    )
    return {
        "work_id": work_id,
        "role": role,
        "stage": str(work["stage"]),
        "payload": payload,
        "sha256": hashlib.sha256(payload.encode("utf-8")).hexdigest(),
    }
