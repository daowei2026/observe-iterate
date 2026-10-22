#!/usr/bin/env python3
"""核 rb previous 首成员方向编码、原价和 FRP 来源语义。"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import subprocess
from pathlib import Path
from uuid import UUID


FRP_COMMIT = "5154c407249c130a6e048c8541b76dfdec3ea48c"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def git_show(repo: Path, path: str) -> str:
    return subprocess.check_output(
        ["git", "-C", str(repo), "show", f"{FRP_COMMIT}:{path}"], text=True
    )


def find_lines(text: str, needles: tuple[str, ...]) -> dict[str, str]:
    lines = text.splitlines()
    result = {}
    for needle in needles:
        matches = [line.strip() for line in lines if needle in line]
        if not matches:
            raise RuntimeError(f"source statement absent: {needle}")
        result[needle] = matches[0]
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--w02-root", type=Path, required=True)
    parser.add_argument("--frp-repo", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    members_path = args.w02_root / "data/selected_cuts/final/previous_members.csv"
    price_path = args.w02_root / "data/same_bound_price/rb_5m_price_calendar.csv"
    member = next(csv.DictReader(members_path.open(encoding="utf-8")))
    prices = {int(row["open_uti"]): row for row in csv.DictReader(price_path.open(encoding="utf-8"))}
    start, end = int(member["start"]), int(member["end"])
    high, low = int(member["life_high"]), int(member["life_low"])
    life = str(UUID(int=(high << 64) | low))

    types = git_show(args.frp_repo, "src/Frp/Instance/ISL/Opportunity/U2/Types.hs")
    thin = git_show(args.frp_repo, "src/Frp/Instance/ISL/Opportunity/U2/ThinNodeResults.hs")
    episode = git_show(args.frp_repo, "src/Frp/Instance/ISL/Opportunity/U2/Episode.hs")
    source_statements = {}
    source_statements.update(find_lines(types, (
        "data TurnDirection = DirectionUp | DirectionDown",
        "deriving (Eq,Ord,Show,Read,Enum,Bounded,Generic)",
    )))
    source_statements.update(find_lines(thin, (
        "(maybe 255 (fromIntegral . fromEnum) (semanticValue direction))",
        '"memberDirection" BSON.:=',
    )))
    source_statements.update(find_lines(episode, (
        "directionSign DirectionUp = 1",
        "directionSign DirectionDown = -1",
        "directionSign d * (b-a)",
    )))
    checks = {
        "life_components_match_order": high == 15379319021888293305 and low == 11629421669636382479,
        "life_uuid": life == "d56e512a-d30f-49b9-a164-0164a9e81f0f",
        "start_end": (start, end) == (100460400, 100633800),
        "direction_code_is_second_enum_constructor_down": int(member["direction"]) == 1,
        "direction_known": int(member["direction_knownness"]) == 0,
        "start_close": float(prices[start]["close"]) == 3953.0,
        "end_close": float(prices[end]["close"]) == 4034.0,
        "visual_slope_positive": float(prices[end]["close"]) > float(prices[start]["close"]),
        "frp_source_commit": subprocess.check_output(
            ["git", "-C", str(args.frp_repo), "rev-parse", "HEAD"], text=True
        ).strip() == FRP_COMMIT,
    }
    if not all(checks.values()):
        raise RuntimeError(f"direction source check failed: {checks}")
    payload = {
        "schema_version": 1, "result": "PASS", "checks": checks,
        "formal_member": {
            "life_high": high, "life_low": low, "life": life,
            "start": start, "end": end, "confirmation": int(member["confirmation"]),
            "known_from": int(member["known_from"]), "direction": int(member["direction"]),
            "direction_label": "down", "direction_knownness": int(member["direction_knownness"]),
        },
        "price": {
            "start_close": float(prices[start]["close"]),
            "end_close": float(prices[end]["close"]),
            "endpoint_displacement": float(prices[end]["close"]) - float(prices[start]["close"]),
        },
        "source_mapping": {
            "frp_commit": FRP_COMMIT, "statements": source_statements,
            "meaning": (
                "TurnDirection 的 Enum 构造顺序使 0=DirectionUp、1=DirectionDown；"
                "ThinMember 直接保存 fromEnum，不按端点斜率重映射；"
                "DirectionalProgress 再用 directionSign 乘端点位移，因此 down 与正端点位移可以并存。"
            ),
        },
        "inputs": {
            "previous_members": {"path": str(members_path), "sha256": sha256(members_path)},
            "same_bound_price": {"path": str(price_path), "sha256": sha256(price_path)},
        },
        "qualification": "核的是正常上游保存方向及方法映射；没有因视觉斜率改写正式方向。",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"result": "PASS", "output": str(args.output)}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
