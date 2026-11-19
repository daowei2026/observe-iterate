#!/usr/bin/env bash
set -e
base=/dwdhome/fy/BASE_E6_2_copy
run_root="$base/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W001"
source_root="$run_root/source/observe-iterate"
export PYTHONDONTWRITEBYTECODE=1
source "$base/m3rc"
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
if [[ -d "$base/.runtime/python-deps" ]]; then
  export PYTHONPATH="$base/.runtime/python-deps:$PYTHONPATH"
fi
export LD_PRELOAD="/lib/x86_64-linux-gnu/libssl.so.3:/lib/x86_64-linux-gnu/libcrypto.so.3${LD_PRELOAD:+:$LD_PRELOAD}"
export TMPDIR="$run_root/cache/tmp"
export XDG_CACHE_HOME="$run_root/cache/xdg"
export NUMBA_CACHE_DIR="$run_root/cache/numba"
export MPLCONFIGDIR="$run_root/cache/matplotlib"
ulimit -c 0
cd "$source_root"
exec python "$run_root/boundary_runner.py"   "$source_root/longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/D/u2_f_caegraph_definition.py"   --output-dir "$run_root/output/u2_f_caegraph"
