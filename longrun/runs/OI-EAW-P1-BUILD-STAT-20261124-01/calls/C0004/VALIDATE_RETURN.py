"""Validate authored V2 payload and source identities, without inventing controller receipts."""
import datetime as dt
import importlib.util
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parent
GATE=Path('/dwdhome/fy/cgpterm/artifacts/oi-eaw-p1-build-stat-20261124-01/adopted-observe-iterate/longrun/tools/longrun_gate.py')
spec=importlib.util.spec_from_file_location('adopted_longrun_gate',GATE)
gate=importlib.util.module_from_spec(spec)
spec.loader.exec_module(gate)
p=json.loads((ROOT/'PRO_RETURN.json').read_text())
i=json.loads((ROOT/'sources/c4_invocation.txt').read_text())
d=json.loads((ROOT/'sources/d2_json.txt').read_text())
b=json.loads((ROOT/'sources/RUN_BINDING.json').read_text())
gate.validated('professional_return',p)
gate.pro_state(p,b)
gate.object_ref_fields(p)
assert p['run_id']==i['run_id']==d['run_id']==b['run_id']
assert p['call_id']==i['call_id']=='C0004'
assert p['role']=='executor'
assert p['sender']==i['recipient']==d['recipient']==b['executors'][0]
assert p['delegation_ref']==i['assignment_ref']
assert p['return_to']==d['return_to']==b['manager']
assert i['token']=='build-c0004-56999f255cd6'
assert p['issued_delegation_refs']==p['issued_order_refs']==p['accepted_worker_refs']==b['workers']==[]
assert p['owner_request_ref'] is None
out={
 'checked_at':dt.datetime.now(dt.timezone.utc).isoformat(),
 'adopted_control_commit':'391adcd18bd2da82c13c01710980f41e01c7de25',
 'return_schema_valid':True,
 'professional_state_consistent':True,
 'source_identity_match':True,
 'workers':[],
 'controller_physical_receipt_verified_by_executor':False,
 'scope':'仅核本E实际拟交payload与已读原始C/D/Binding；controller独立核真实回交。'
}
(ROOT/'RETURN_CHECK.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(out,ensure_ascii=False))
