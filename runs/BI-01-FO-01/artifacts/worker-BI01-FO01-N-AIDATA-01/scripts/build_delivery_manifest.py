#!/usr/bin/env python3
"""Hash the non-secret Worker return before Git publication."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


EXCLUDED = {"DELIVERY_MANIFEST.json", "GITHUB_RECEIPT.json"}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", required=True, type=Path)
    args = parser.parse_args()
    root = args.root.resolve()
    files = []
    for path in sorted(root.rglob("*")):
        if not path.is_file() or path.name in EXCLUDED or "__pycache__" in path.parts:
            continue
        files.append({"path": str(path.relative_to(root)), "bytes": path.stat().st_size, "sha256": sha256(path)})
    payload = {
        "schema_version": 1,
        "result": "PASS",
        "root": str(root),
        "excluded_self_referential_or_post_publish_files": sorted(EXCLUDED),
        "file_count": len(files),
        "total_bytes": sum(item["bytes"] for item in files),
        "files": files,
    }
    output = root / "DELIVERY_MANIFEST.json"
    output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"result": "PASS", "file_count": payload["file_count"], "total_bytes": payload["total_bytes"], "manifest_sha256": sha256(output)}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
