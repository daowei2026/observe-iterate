#!/usr/bin/env bash
set -e
source /dwdhome/fy/BASE_E6_2_copy/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W004/w004_environment.sh
cd "$RUN_ROOT/source/mquant/tis"
command -v python > "$RUN_ROOT/logs/tis_seed_python_entry.txt"
python --version > "$RUN_ROOT/logs/tis_seed_python_version.txt" 2>&1
date -u +%Y-%m-%dT%H:%M:%S.%NZ > "$RUN_ROOT/logs/tis_seed_inits.started_at"
python seed_inits.py > "$RUN_ROOT/logs/tis_seed_inits.stdout.log" 2> "$RUN_ROOT/logs/tis_seed_inits.stderr.log"
