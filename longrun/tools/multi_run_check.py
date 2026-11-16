#!/usr/bin/env python3
"""Read-only checks for a multi-Run registry; no messaging, Git, locks or grants."""
import argparse
import json
import os
import re
import sys
from pathlib import Path

SCHEMA = "observe-iterate-multirun-registry/v1"
REF = re.compile(r"^([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)@([0-9a-fA-F]{40}):(.+)$")
ID = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]*$")
REQUIRED = {
    "run_id", "work_id", "business_case_id", "binding_ref",
    "resource_binding_ref", "owner_workspace_path", "adopted_protocol_ref",
}


class CheckError(ValueError):
    pass


def require(condition, why):
    if not condition:
        raise CheckError(why)


def exact_ref(value, suffix=None):
    require(isinstance(value, str), "exact reference must be a string")
    match = REF.fullmatch(value)
    require(match is not None, f"not an exact owner/repo@40-hex:path reference: {value!r}")
    path = match.group(3)
    require(path.startswith("longrun/") or suffix is None,
            f"unexpected repository path: {path}")
    if suffix is not None:
        require(path == suffix, f"reference must point to {suffix}, got {path}")


def workspace_path(value, run_id):
    require(isinstance(value, str) and value.startswith("/") and "\x00" not in value,
            f"{run_id}: workspace must be an absolute Linux path")
    require(value != "/", f"{run_id}: cannot use filesystem root as workspace")
    require(os.path.normpath(value) == value,
            f"{run_id}: workspace must be normalized; do not use /./, /../ or trailing slash")
    return value


def overlap(a, b):
    try:
        return os.path.commonpath([a, b]) in (a, b)
    except ValueError:
        return False


def validate_registry(registry, on_worker_host=False):
    require(isinstance(registry, dict), "registry must be an object")
    require(registry.get("schema") == SCHEMA, f"schema must be {SCHEMA}")
    require(set(registry) == {"schema", "runs"}, "unexpected registry root fields")
    runs = registry.get("runs")
    require(isinstance(runs, dict), "runs must be a map (empty bootstrap is valid)")
    paths = []
    for key, entry in runs.items():
        require(isinstance(key, str) and ID.fullmatch(key) is not None,
                f"invalid run key: {key!r}")
        require(isinstance(entry, dict), f"{key}: run entry must be an object")
        require(set(entry) == REQUIRED, f"{key}: missing/extra fields: {sorted(set(entry) ^ REQUIRED)}")
        require(entry["run_id"] == key, f"{key}: run_id mismatch")
        for field in ("work_id", "business_case_id"):
            require(isinstance(entry[field], str) and entry[field].strip(),
                    f"{key}: missing {field}")
        exact_ref(entry["binding_ref"], f"longrun/runs/{key}/RUN_BINDING.json")
        exact_ref(entry["resource_binding_ref"], f"longrun/runs/{key}/RUN_RESOURCE_BINDING.json")
        exact_ref(entry["adopted_protocol_ref"], "longrun/contracts/LONGRUN_PROTOCOL_V2.md")
        p = workspace_path(entry["owner_workspace_path"], key)
        if on_worker_host:
            require(os.path.isdir(p), f"{key}: directory does not exist on this host: {p}")
            require(os.access(p, os.R_OK | os.W_OK | os.X_OK),
                    f"{key}: this process cannot read/write/traverse workspace: {p}")
            p = os.path.realpath(p)
        for prior_run, prior_path in paths:
            require(not overlap(p, prior_path),
                    f"workspace overlap: {prior_run}={prior_path}, {key}={p}")
        paths.append((key, p))
    return {"result": "STRUCTURE_VALID_ONLY" if not on_worker_host else "LOCAL_HOST_PATHS_CHECKED_ONLY",
            "run_count": len(runs), "workspaces_checked": len(paths)}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=["validate-registry", "check-workspaces"])
    parser.add_argument("registry", type=Path)
    parser.add_argument("--on-worker-host", action="store_true",
                        help="Required for check-workspaces: inspect actual Linux directories and resolve symlinks")
    args = parser.parse_args(argv)
    try:
        require(args.command != "check-workspaces" or args.on_worker_host,
                "check-workspaces requires --on-worker-host; do not treat remote path strings as physical proof")
        with args.registry.open(encoding="utf-8") as f:
            registry = json.load(f)
        result = validate_registry(registry, on_worker_host=args.on_worker_host)
        print(json.dumps(result, ensure_ascii=False))
        return 0
    except (CheckError, OSError, json.JSONDecodeError) as exc:
        print(json.dumps({"result": "BLOCKED", "reason": str(exc)}, ensure_ascii=False))
        return 2


if __name__ == "__main__":
    sys.exit(main())
