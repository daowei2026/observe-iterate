import pathlib,json,sys
w=pathlib.Path(__file__).resolve().parents[1];base=pathlib.Path('/dwdhome/fy/BASE_E6_2');c=pathlib.Path('/dwdhome/fy/cgpterm/artifacts/oi-eaw-wall/OI-EAW-WALL-20261114-01');oi=c/'observe-iterate'
paths=[c/'W001-dispatch-metadata.json',c/'W001-worker-preflight-live.json',oi/'longrun/runs/OI-EAW-WALL-20261114-01/delegations/D001/DELEGATION.md',oi/'task-inputs/eaw-p1-wall-lifecycle/FEATURE_CONTEXT.md']
for p in paths:
 print('INPUT_PATH',p,'EXISTS',p.exists())
 if p.exists() and p.stat().st_size<70000:
  data=p.read_bytes();dest=w/'inputs'/p.name
  if not dest.exists():dest.write_bytes(data)
  print(data.decode())
for rel in ('edh-universe/frp/frp','edh-universe/frp/frp-core','m3','pydim','edh-universe/e-wrks/hasdim/host.py/hasdim','edh-universe/frp/frp-poc','notebook'):
 p=base/rel;print('LAYOUT',p,[(x.name,x.is_dir(),x.is_symlink()) for x in sorted(p.iterdir())[:70]])
for p in (base/'edh-universe/frp/frp/AGENTS.md',base/'edh-universe/frp/AGENTS.md',base/'edh-universe/AGENTS.md',base/'m3/AGENTS.md',base/'pydim/AGENTS.md'):
 if p.exists():print('AGENTS',p,p.read_text())
