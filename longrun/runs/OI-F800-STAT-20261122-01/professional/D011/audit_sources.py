import hashlib
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PACKET = Path('/dwdhome/fy/cgpterm/artifacts/wall-f-closure-20261122/OI-F800-STAT-20261122-01/C0025-dispatch-packet.json')
p = json.loads(PACKET.read_text())
repo = Path(p['record_checkout'])
delegation = json.loads(Path(p['delegation_json_path']).read_text())
refs = list(dict.fromkeys(p['invocation']['source_refs'] + delegation['input_refs'] +
    [delegation['task_ref'], delegation['business_context_ref']] +
    [p['binding_adoption'][name] for name in ('binding_ref','approval_ref','decision_ref','authorization_ref')]))
rows = []
for ref in refs:
    identity, path = ref.split(':', 1)
    repository, commit = identity.rsplit('@', 1)
    assert repository in ('daowei2026/observe-iterate','daowei2026/uplot') and len(commit) == 40
    object_repo = repo if repository.endswith('/observe-iterate') else Path('/dwdhome/fy/BASE_E6_2_copy/mquant/uplot')
    data = subprocess.check_output(['git', 'show', f'{commit}:{path}'], cwd=object_repo)
    current = object_repo / path
    rows.append({'ref': ref, 'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest(),
        'pinned_git_blob': subprocess.check_output(['git', 'rev-parse', f'{commit}:{path}'], cwd=object_repo, text=True).strip(),
        'local_current_equal': current.exists() and current.read_bytes() == data})
approval = (repo / 'longrun/runs/OI-F800-STAT-20261122-01/owner-decisions/F800-MP-002/OWNER_APPROVAL.original.txt').read_bytes()
assert approval == Path(p['owner_latest_original_path']).read_bytes()
inv = json.loads((repo / 'longrun/runs/OI-F800-STAT-20261122-01/calls/C0025/INVOCATION.json').read_text())
assert inv == p['invocation']
out = {'run_id': p['run_id'], 'call_id': p['call_id'], 'count': len(rows),
       'exact_objects_available': True, 'owner_original_byte_equal': True,
       'packet_invocation_equal': True, 'rows': rows}
(ROOT / 'SOURCE_REF_AUDIT.json').write_text(json.dumps(out, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({k:v for k,v in out.items() if k != 'rows'}, ensure_ascii=False))
print('Current files differing from pinned inputs:', [r['ref'] for r in rows if not r['local_current_equal']])
