#!/usr/bin/env bash
set -euo pipefail
RUN_ROOT="$1"
export RUN_ROOT
BASE=/dwdhome/fy/BASE_E6_2_copy
SOURCE_ROOT="$RUN_ROOT/source/observe-iterate"
RUNTIME_SHM="$RUN_ROOT/runtime/shm"
export PYTHONDONTWRITEBYTECODE=1
date -u +%FT%TZ > "$RUN_ROOT/logs/private_shm_mount.inner_entered"
mount --make-rprivate /
mount --bind "$RUNTIME_SHM" /dev/shm
test -d /dev/shm
test -w /dev/shm
findmnt -T /dev/shm --json > "$RUN_ROOT/logs/private_shm_mount.findmnt.json"
/usr/bin/python -B - <<'PYALIAS'
import hashlib, json, os
from pathlib import Path
run = Path(os.environ['RUN_ROOT'])
outer = json.loads((run/'execution_receipt.json').read_text())['outer_namespaces']
inner = {name:os.readlink('/proc/self/ns/'+name) for name in ('user','mnt','pid')}
assert inner['pid'] == outer['pid'], 'PID namespace must remain unchanged'
assert inner['mnt'] != outer['mnt'], 'A private mount namespace is required'
assert inner['user'] != outer['user'], 'A user namespace is required'
backing = run/'runtime/shm'
alias = Path('/dev/shm')
assert (alias.stat().st_dev,alias.stat().st_ino) == (backing.stat().st_dev,backing.stat().st_ino)
name = '.w002-alias-'+str(os.getpid())
content = b'OI-U2-F-OBS-20261118-01/W002/private-shm-alias-proof\n'
created = alias/name
with created.open('xb') as stream:
    stream.write(content)
observed = backing/name
assert observed.read_bytes() == content
assert (created.stat().st_dev,created.stat().st_ino) == (observed.stat().st_dev,observed.stat().st_ino)
created.unlink()
assert not observed.exists()
mountinfo = [line for line in Path('/proc/self/mountinfo').read_text().splitlines() if line.split()[4]=='/dev/shm']
assert mountinfo
(run/'logs/private_shm_mount.mountinfo').write_text('\n'.join(mountinfo)+'\n')
proof = {'run_id':'OI-U2-F-OBS-20261118-01','work_order_id':'W002','backing':str(backing),'alias':'/dev/shm','outer_namespaces':outer,'inner_namespaces':inner,'backing_and_alias_same_dev_inode':True,'alias_file_visible_at_backing':True,'alias_probe_file_deleted':True,'alias_probe_sha256':hashlib.sha256(content).hexdigest(),'mountinfo':mountinfo,'verified':True}
(run/'logs/private_shm_mount.alias_report.json').write_text(json.dumps(proof,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(proof,ensure_ascii=False))
PYALIAS

source "$BASE/m3rc"
if [[ -z "${M3HOST:-}" ]]; then
  M3HOST="$(python - <<'PYHOST'
import socket
with socket.socket(socket.AF_INET,socket.SOCK_DGRAM) as sock:
    sock.connect(('gogs.dw',443))
    print(sock.getsockname()[0])
PYHOST
)"
  export M3HOST
fi
export NO_PROXY="${NO_PROXY:+${NO_PROXY},}${M3HOST},localhost,127.0.0.1,gogs.dw"
export no_proxy="$NO_PROXY"
if [[ -d "$BASE/.runtime/python-deps" ]]; then
  export PYTHONPATH="$BASE/.runtime/python-deps:$PYTHONPATH"
fi
export LD_PRELOAD="/lib/x86_64-linux-gnu/libssl.so.3:/lib/x86_64-linux-gnu/libcrypto.so.3${LD_PRELOAD:+:$LD_PRELOAD}"
export TMPDIR="$RUN_ROOT/runtime/tmp"
export XDG_CACHE_HOME="$RUN_ROOT/runtime/xdg"
export NUMBA_CACHE_DIR="$RUN_ROOT/runtime/numba"
export MPLCONFIGDIR="$RUN_ROOT/runtime/matplotlib"
ulimit -c 0
cd "$SOURCE_ROOT"
exec python "$RUN_ROOT/runtime_worker.py"
