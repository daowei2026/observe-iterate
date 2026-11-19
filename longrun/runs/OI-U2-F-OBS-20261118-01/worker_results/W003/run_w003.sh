#!/usr/bin/env bash
set -e
BASE=/dwdhome/fy/BASE_E6_2_copy
RUN_ROOT="$BASE/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W003"
SOURCE_ROOT="$RUN_ROOT/source/observe-iterate"
OUTPUT_ROOT="$RUN_ROOT/output/u2_f_caegraph"
LOG_ROOT="$RUN_ROOT/logs"
if [[ -e "$LOG_ROOT/w003_run.started_at" ]]; then
  printf '%s\n' 'EFFECT_UNKNOWN: W003 already has a D invocation receipt; refusing repeat'
  exit 91
fi
export PYTHONDONTWRITEBYTECODE=1
source "$BASE/m3rc"
if [[ -z "${M3HOST:-}" ]]; then
  M3HOST="$(python - <<'PYHOST'
import socket
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
    sock.connect(("gogs.dw",443))
    print(sock.getsockname()[0])
PYHOST
)"
  export M3HOST
fi
export NO_PROXY="${NO_PROXY:+${NO_PROXY},}${M3HOST},localhost,127.0.0.1,gogs.dw"
export no_proxy="$NO_PROXY"
if [[ -d "$BASE/.runtime/python-deps" ]]; then
  export PYTHONPATH="$BASE/.runtime/python-deps${PYTHONPATH:+:$PYTHONPATH}"
fi
export LD_PRELOAD="/lib/x86_64-linux-gnu/libssl.so.3:/lib/x86_64-linux-gnu/libcrypto.so.3${LD_PRELOAD:+:$LD_PRELOAD}"
export TMPDIR="$RUN_ROOT/cache/tmp"
export XDG_CACHE_HOME="$RUN_ROOT/cache/xdg"
export NUMBA_CACHE_DIR="$RUN_ROOT/cache/numba"
export MPLCONFIGDIR="$RUN_ROOT/cache/matplotlib"
ulimit -c 0
cd "$SOURCE_ROOT"
command -v python > "$LOG_ROOT/python_entry.txt"
python --version > "$LOG_ROOT/python_version.txt" 2>&1
printf '%s\n' python longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/D/u2_f_caegraph_definition.py --output-dir "$OUTPUT_ROOT" > "$LOG_ROOT/w003_run.argv.txt"
pwd > "$LOG_ROOT/w003_run.cwd.txt"
set +e
set -o pipefail
find /dev/shm -maxdepth 1 -name 'sem.*' -printf '%f\t%u\t%g\t%m\t%s\t%T@\t%i\n' 2> "$LOG_ROOT/dev_shm_sem.before.stderr" | LC_ALL=C sort > "$LOG_ROOT/dev_shm_sem.before.tsv"
printf '%s\n' "$?" > "$LOG_ROOT/dev_shm_sem.before.exit_code"
date -u +%Y-%m-%dT%H:%M:%S.%NZ > "$LOG_ROOT/w003_run.started_at"
printf '1\n' > "$LOG_ROOT/w003_run.attempt_count"
python \
  longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/D/u2_f_caegraph_definition.py \
  --output-dir "$OUTPUT_ROOT" \
  > "$LOG_ROOT/w003_run.log" \
  2>&1
RUN_EXIT=$?
printf '%s\n' "$RUN_EXIT" > "$LOG_ROOT/w003_run.exit_code"
date -u +%Y-%m-%dT%H:%M:%S.%NZ > "$LOG_ROOT/w003_run.finished_at"
find /dev/shm -maxdepth 1 -name 'sem.*' -printf '%f\t%u\t%g\t%m\t%s\t%T@\t%i\n' 2> "$LOG_ROOT/dev_shm_sem.after.stderr" | LC_ALL=C sort > "$LOG_ROOT/dev_shm_sem.after.tsv"
printf '%s\n' "$?" > "$LOG_ROOT/dev_shm_sem.after.exit_code"
exit "$RUN_EXIT"
