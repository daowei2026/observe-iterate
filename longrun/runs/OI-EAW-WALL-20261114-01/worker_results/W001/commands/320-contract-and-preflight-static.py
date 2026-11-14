import pathlib,json,re
B=pathlib.Path('/dwdhome/fy/BASE_E6_2');oi=pathlib.Path('/dwdhome/fy/cgpterm/artifacts/oi-eaw-wall/OI-EAW-WALL-20261114-01/observe-iterate');W=pathlib.Path(__file__).resolve().parents[1]
p=oi/'longrun/contracts/longrun_schema_v2.json';j=json.loads(p.read_text());print('SCHEMA_TOP',list(j.keys()))
# Select only worker-return relevant definitions and references.
for k,v in j.items():
 if k in ('$defs','definitions'):
  print('DEF_NAMES',list(v.keys()))
  for name,val in v.items():
   if 'worker' in name.lower() and ('return' in name.lower() or 'result' in name.lower()):print('WORKER_DEFINITION',name,json.dumps(val,ensure_ascii=False,indent=2));(W/'inputs/WORKER_RETURN_SCHEMA_FRAGMENT.json').write_text(json.dumps({name:val},ensure_ascii=False,indent=2)+'\n')
p=oi/'longrun/runs/OI-EAW-WALL-20261114-01/RUN_BINDING.json';print('RUN_BINDING',p.read_text())
for rel in ('mquant/tis/frpExample','mquant/frame/core/base','mquant/frame/lang/internal','mquant/fis'):
 p=B/rel;print('DIR',p,[x.name for x in sorted(p.iterdir())[:70]] if p.is_dir() else None)
