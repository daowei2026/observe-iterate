BASE=/dwdhome/fy/BASE_E6_2_copy
RUN_ROOT="$BASE/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W004"
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
export OI_W004_RUN_ROOT="$RUN_ROOT"
ulimit -c 0
