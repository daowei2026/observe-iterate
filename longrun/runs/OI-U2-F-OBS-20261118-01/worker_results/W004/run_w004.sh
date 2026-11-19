#!/usr/bin/env bash
set -e
RUN_ROOT=/dwdhome/fy/BASE_E6_2_copy/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W004
LOG_ROOT="$RUN_ROOT/logs"
if [[ -e "$LOG_ROOT/w004_run.started_at" || -e "$LOG_ROOT/D_dispatch.json" ]]; then
  printf '%s\n' 'EFFECT_UNKNOWN: W004 wrapper or D already has dispatch receipt; refusing repeat'
  exit 91
fi
source "$RUN_ROOT/w004_environment.sh"
cd "$RUN_ROOT/source/observe-iterate"
command -v python > "$LOG_ROOT/python_entry.txt"
python --version > "$LOG_ROOT/python_version.txt" 2>&1
printf '%s\n' python "$RUN_ROOT/run_d_with_locked_tis.py" > "$LOG_ROOT/w004_run.argv.txt"
pwd > "$LOG_ROOT/w004_run.cwd.txt"
set +e
set -o pipefail
find /dev/shm -maxdepth 1 -name 'sem.*' -printf '%f\t%u\t%g\t%m\t%s\t%T@\t%i\n' 2> "$LOG_ROOT/dev_shm_sem.before.stderr" | LC_ALL=C sort > "$LOG_ROOT/dev_shm_sem.before.tsv"
printf '%s\n' "$?" > "$LOG_ROOT/dev_shm_sem.before.exit_code"
date -u +%Y-%m-%dT%H:%M:%S.%NZ > "$LOG_ROOT/w004_run.started_at"
printf '1\n' > "$LOG_ROOT/w004_run.attempt_count"
python "$RUN_ROOT/run_d_with_locked_tis.py" > "$LOG_ROOT/w004_run.log" 2>&1
RUN_EXIT=$?
printf '%s\n' "$RUN_EXIT" > "$LOG_ROOT/w004_run.exit_code"
date -u +%Y-%m-%dT%H:%M:%S.%NZ > "$LOG_ROOT/w004_run.finished_at"
find /dev/shm -maxdepth 1 -name 'sem.*' -printf '%f\t%u\t%g\t%m\t%s\t%T@\t%i\n' 2> "$LOG_ROOT/dev_shm_sem.after.stderr" | LC_ALL=C sort > "$LOG_ROOT/dev_shm_sem.after.tsv"
printf '%s\n' "$?" > "$LOG_ROOT/dev_shm_sem.after.exit_code"
exit "$RUN_EXIT"
