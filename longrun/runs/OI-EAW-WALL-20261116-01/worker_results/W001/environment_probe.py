import json
import pathlib
import sys
from support import BASE, OUT, lease, readonly_audit, write_json

events = []
proof = lease()
readonly_audit(events)
found = []
for item in sys.path:
    root = pathlib.Path(item or '.')
    package = root / 'mquant'
    if package.is_dir():
        found.append(dict(path=str(package), realpath=str(package.resolve()),
                          direct_children=sorted(p.name for p in package.iterdir())))
result = dict(workspace=str(pathlib.Path.cwd()), executable=sys.executable,
              sys_path=sys.path, mquant_candidates=found, lease=proof, audit=events)
write_json('environment.json', result)
print(json.dumps(result, ensure_ascii=False, indent=2))
