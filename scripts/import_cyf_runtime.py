#!/usr/bin/env python3
"""Materialize an exact, source-preserving copy of the locked CYF long-run runtime.

This is migration stage 1 only. It deliberately performs no BI-01 semantic
adaptation and no long-run trial. Active runtime directories are replaced with
byte-identical copies from the locked upstream commit, and a manifest records
the source/target mapping and hashes.

Later migration stages must edit these complete copies section by section:
- preserve common runtime semantics;
- rename declaration-only Mission A/B/C role labels;
- replace substantive professional content with exact BI-01 references;
- mark missing professional references explicitly rather than summarizing away
  the upstream rule.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

LOCKED_UPSTREAM_COMMIT = "c6a930887c9148e76ba75f8a026549b9a46c9e35"
UPSTREAM_REPOSITORY = "daowei2026/feature-refinement-implementation-agent-evolution"

CANDIDATES = Path("agent_evolution/agent_candidates")
COPY_SPECS = (
    (
        CANDIDATES / "dual_route_execution",
        Path("runtime/dual_route_execution"),
    ),
    (
        CANDIDATES
        / "runtime_overlay_candidates"
        / "agent_owned_long_horizon_overlay_v0_3",
        Path("runtime/overlay"),
    ),
    (
        CANDIDATES
        / "runtime_release_candidates"
        / "agent_refinement_runtime_release_candidate_v0_3_20260904",
        Path("runtime/release"),
    ),
)
ROOT_FILE_SPECS = (
    (CANDIDATES / "AGENTS.md", Path("runtime/AGENTS.md")),
    (CANDIDATES / "README.md", Path("runtime/README.md")),
)

MANIFEST_PATH = Path("migration/EXACT_COPY_MANIFEST.json")
STATUS_PATH = Path("migration/RUNTIME_PORT_STATUS.md")


@dataclass(frozen=True)
class FileRecord:
    source: str
    target: str
    sha256: str
    size: int

    def as_dict(self) -> dict[str, object]:
        return {
            "source": self.source,
            "target": self.target,
            "sha256": self.sha256,
            "size": self.size,
            "copy_status": "EXACT_BYTE_COPY",
        }


def git_head(repo: Path) -> str:
    try:
        return subprocess.check_output(
            ["git", "-C", str(repo), "rev-parse", "HEAD"],
            text=True,
            stderr=subprocess.STDOUT,
        ).strip()
    except (OSError, subprocess.CalledProcessError) as exc:
        raise RuntimeError(f"cannot resolve source git HEAD: {exc}") from exc


def digest(path: Path) -> tuple[str, int]:
    h = hashlib.sha256()
    size = 0
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
            size += len(chunk)
    return h.hexdigest(), size


def iter_files(root: Path) -> Iterable[Path]:
    for path in sorted(root.rglob("*")):
        if path.is_file() and not path.is_symlink():
            yield path


def assert_source(source: Path) -> None:
    if not source.is_dir():
        raise RuntimeError(f"source checkout does not exist: {source}")
    actual = git_head(source)
    if actual != LOCKED_UPSTREAM_COMMIT:
        raise RuntimeError(
            "wrong upstream commit: "
            f"expected {LOCKED_UPSTREAM_COMMIT}, got {actual}"
        )
    missing = [
        str(path)
        for path, _ in (*COPY_SPECS, *ROOT_FILE_SPECS)
        if not (source / path).exists()
    ]
    if missing:
        raise RuntimeError("missing locked upstream paths: " + ", ".join(missing))


def copy_exact(source: Path, target: Path) -> list[FileRecord]:
    records: list[FileRecord] = []

    for src_rel, dst_rel in COPY_SPECS:
        src = source / src_rel
        dst = target / dst_rel
        if dst.exists():
            shutil.rmtree(dst)
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copytree(src, dst, copy_function=shutil.copy2)

        for src_file in iter_files(src):
            rel = src_file.relative_to(src)
            dst_file = dst / rel
            src_hash, src_size = digest(src_file)
            dst_hash, dst_size = digest(dst_file)
            if (src_hash, src_size) != (dst_hash, dst_size):
                raise RuntimeError(f"copy mismatch: {src_file} -> {dst_file}")
            records.append(
                FileRecord(
                    source=(src_rel / rel).as_posix(),
                    target=(dst_rel / rel).as_posix(),
                    sha256=src_hash,
                    size=src_size,
                )
            )

    for src_rel, dst_rel in ROOT_FILE_SPECS:
        src_file = source / src_rel
        dst_file = target / dst_rel
        dst_file.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src_file, dst_file)
        src_hash, src_size = digest(src_file)
        dst_hash, dst_size = digest(dst_file)
        if (src_hash, src_size) != (dst_hash, dst_size):
            raise RuntimeError(f"copy mismatch: {src_file} -> {dst_file}")
        records.append(
            FileRecord(
                source=src_rel.as_posix(),
                target=dst_rel.as_posix(),
                sha256=src_hash,
                size=src_size,
            )
        )

    return sorted(records, key=lambda record: record.target)


def write_manifest(target: Path, records: list[FileRecord]) -> None:
    payload = {
        "schema": "observe-iterate/exact-cyf-runtime-copy/v1",
        "upstream": {
            "repository": UPSTREAM_REPOSITORY,
            "commit": LOCKED_UPSTREAM_COMMIT,
        },
        "stage": "EXACT_SOURCE_COPY_COMPLETE",
        "semantic_adaptation": "NOT_STARTED",
        "trial_run": "NOT_REQUESTED",
        "file_count": len(records),
        "files": [record.as_dict() for record in records],
    }
    path = target / MANIFEST_PATH
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    status = f"""# CYF 长程运行迁移状态

## 当前阶段

- 上游仓库：`{UPSTREAM_REPOSITORY}`
- 锁定提交：`{LOCKED_UPSTREAM_COMMIT}`
- 原文复制：**已完成**
- 复制文件数：**{len(records)}**
- 语义适配：**尚未开始**
- 试跑：**未执行；本阶段不要求试跑**

`runtime/dual_route_execution/`、`runtime/overlay/`、`runtime/release/`
以及 `runtime/AGENTS.md`、`runtime/README.md` 均来自上述锁定提交，
并由 `EXACT_COPY_MANIFEST.json` 逐文件记录 SHA-256 和大小。

## 下一阶段边界

下一阶段必须以这些完整原文为基础逐段处理，不能再次将文件压缩为摘要壳：

1. 通用运行规则完整保留；
2. 仅声明性使用 Mission A/B/C 的表达改为通用角色；
3. 实质需要专业 Agent 内容的位置改为 exact BI-01 专业引用；
4. 暂无对应专业内容的位置显式标记缺口及受影响能力；
5. 修正相对引用、程序、Schema、测试与发布投影。

本状态文件不证明 BI-01 语义适配完成，也不证明系统可运行。
"""
    (target / STATUS_PATH).write_text(status, encoding="utf-8")


def load_manifest(target: Path) -> dict[str, object]:
    path = target / MANIFEST_PATH
    if not path.exists():
        raise RuntimeError(f"manifest missing: {path}")
    return json.loads(path.read_text(encoding="utf-8"))


def verify(source: Path, target: Path) -> None:
    assert_source(source)
    manifest = load_manifest(target)
    if manifest.get("stage") != "EXACT_SOURCE_COPY_COMPLETE":
        raise RuntimeError("manifest stage is not EXACT_SOURCE_COPY_COMPLETE")

    errors: list[str] = []
    files = manifest.get("files")
    if not isinstance(files, list):
        raise RuntimeError("manifest files must be a list")

    expected_targets: set[str] = set()
    for item in files:
        if not isinstance(item, dict):
            errors.append("manifest contains a non-object file record")
            continue
        source_rel = Path(str(item["source"]))
        target_rel = Path(str(item["target"]))
        expected_targets.add(target_rel.as_posix())
        source_file = source / source_rel
        target_file = target / target_rel
        if not source_file.is_file():
            errors.append(f"source missing: {source_rel}")
            continue
        if not target_file.is_file():
            errors.append(f"target missing: {target_rel}")
            continue
        src_hash, src_size = digest(source_file)
        dst_hash, dst_size = digest(target_file)
        if src_hash != dst_hash or src_size != dst_size:
            errors.append(f"content mismatch: {target_rel}")
        if src_hash != item.get("sha256") or src_size != item.get("size"):
            errors.append(f"manifest mismatch: {target_rel}")

    actual_targets: set[str] = set()
    for _, dst_rel in COPY_SPECS:
        dst = target / dst_rel
        if not dst.is_dir():
            errors.append(f"target directory missing: {dst_rel}")
            continue
        actual_targets.update(
            path.relative_to(target).as_posix() for path in iter_files(dst)
        )
    for _, dst_rel in ROOT_FILE_SPECS:
        if (target / dst_rel).is_file():
            actual_targets.add(dst_rel.as_posix())

    extra = sorted(actual_targets - expected_targets)
    missing = sorted(expected_targets - actual_targets)
    if extra:
        errors.append("unmanifested target files: " + ", ".join(extra))
    if missing:
        errors.append("manifested target files absent: " + ", ".join(missing))

    if errors:
        raise RuntimeError("\n".join(errors))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", required=True, type=Path)
    parser.add_argument("--target", required=True, type=Path)
    parser.add_argument("--verify-only", action="store_true")
    args = parser.parse_args()

    source = args.source.resolve()
    target = args.target.resolve()

    if args.verify_only:
        verify(source, target)
        print("exact-copy verification: PASS")
        return 0

    assert_source(source)
    records = copy_exact(source, target)
    write_manifest(target, records)
    verify(source, target)
    print(f"exact-copy materialization: PASS ({len(records)} files)")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:  # noqa: BLE001 - command-line boundary
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(1)
