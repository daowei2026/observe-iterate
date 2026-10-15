"""Minimal mechanical workmap check; no professional semantics."""
from pathlib import Path
import json
def check(root,binding_path):
    base=Path(root); b=json.loads((base/binding_path).read_text(encoding='utf-8')); e=[]
    for k in ('overview','streams','rule_paths'):
        if k not in b: e.append('MISSING_'+k.upper())
    return e
