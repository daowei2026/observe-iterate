from common import *

packet_path = Path('/dwdhome/fy/cgpterm/artifacts/wall-f-closure-20261122') / RUN / 'C0031-dispatch-packet.json'
packet = json.loads(packet_path.read_bytes())
assert packet['invocation']['token'] == 'b6f19c6b9e1146b3b125a89798ef17ec'
assert packet['delegation']['delegation_id'] == 'D014'
assert packet['record_branch'] == 'codex/oi-f800-stat-20261122-01'
for kind in ('invocation', 'delegation'):
    exact = packet[kind + '_ref']
    commit, path = exact.split('@', 1)[1].split(':', 1)
    assert read_json(commit, path) == packet[kind]
branch = subprocess.check_output(['git', 'branch', '--show-current'], cwd=RECORD).decode().strip()
assert branch == packet['record_branch']
refs = list(dict.fromkeys([packet['invocation_ref'], packet['delegation_ref'],
                          packet['delegation']['task_ref'], packet['delegation']['business_context_ref'],
                          *packet['invocation']['source_refs']]))
rows = []
for i, exact in enumerate(refs):
    commit, path = exact.split('@', 1)[1].split(':', 1)
    raw = git_bytes(commit, path)
    blob = hashlib.sha1(b'blob ' + str(len(raw)).encode() + b'\0' + raw).hexdigest()
    assert blob == subprocess.check_output(['git', 'rev-parse', f'{commit}:{path}'], cwd=RECORD).decode().strip()
    row = dict(source_ref=exact, bytes=len(raw), sha256=sha(raw), git_blob=blob)
    if len(raw) < 250000 and not path.endswith('.gz'):
        target = ROOT / 'inputs' / f'{i:02d}-{Path(path).name}'
        target.parent.mkdir(exist_ok=True)
        target.write_bytes(raw)
        row['exact_local_copy'] = str(target.relative_to(ROOT))
    rows.append(row)
skill = git_bytes(LOCKED, 'skills/reasonableness-analysis/business-evidence-comparison/SKILL.md')
(ROOT / 'locked_skill').mkdir(exist_ok=True)
(ROOT / 'locked_skill/SKILL.md').write_bytes(skill)
html = BASE / 'artifacts' / RUN / 'caegraph-E/f800.html'
expected = 'df4076f642d4d2b2ac7a6f8cc02899d9cf70e20dd8beb313e347e7545279b450'
assert sha(html.read_bytes()) == expected
mapping, data = formal_all()
assert len(data) == 21
save('SOURCE_REF_AUDIT.json', dict(run_id=RUN,call_id='C0031',delegation_id='D014',
    audited_at=now(),exact_sources=rows,count=len(rows),all_git_objects_match=True,
    packet_binding_match=True,branch=branch,html=dict(path=str(html),sha256=expected),
    formal_files=21,formal_gzip_and_json_hashes_match=True,workers=[]))
print(json.dumps(dict(source_count=len(rows),html_sha256=expected,formal_files=len(data),
    source_shapes={k: list(v) if isinstance(v,dict) else type(v).__name__ for k,v in data.items()}),ensure_ascii=False))
