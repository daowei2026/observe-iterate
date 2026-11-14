import pathlib,os,itertools
p=pathlib.Path('/dwdhome/fy/cgpterm/artifacts/oi-eaw-wall/OI-EAW-WALL-20261114-01/observe-iterate')
for rel in ('longrun','longrun/contracts','longrun/templates','longrun/runs/OI-EAW-WALL-20261114-01','longrun/runs/OI-EAW-WALL-20261114-01/worker_results','schemas'):
 x=p/rel;print('DIR',x,'EXISTS',x.exists())
 if x.is_dir():print('CONTENTS',[a.name for a in sorted(x.iterdir())[:85]])
