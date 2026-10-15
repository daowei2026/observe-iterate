"""Exact payload verification and action reconciliation; no scheduler or semantics."""
import hashlib
def verify_payload(prepared,payload):
    if hashlib.sha256(payload.encode()).hexdigest()!=prepared['sha256']: raise ValueError('PAYLOAD_MISMATCH')
def reconcile_actions(actions):
    seen=set(); out=[]
    for a in actions:
        k=(a.get('work_id'),a.get('obligation_id'),a.get('cycle_id'))
        if k not in seen: seen.add(k); out.append(a)
    return out
