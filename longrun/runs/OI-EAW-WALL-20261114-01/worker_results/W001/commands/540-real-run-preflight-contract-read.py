import pathlib,ast
B=pathlib.Path('/dwdhome/fy/BASE_E6_2');p=B/'mquant/tis/test/integration/verify_eaw_p1_real_run.py';lines=p.read_text().splitlines();print('FILE',p,'LINES',len(lines))
# Read exact CLI and production-side-effect gates, without importing or invoking the runner.
spans=[(120,174),(299,329),(427,473),(max(1,len(lines)-170),len(lines))]
for lo,hi in spans:
 for n in range(lo,min(hi,len(lines))+1):print(f'{n}: {lines[n-1]}')
# Standalone function names relevant to the generation/read boundaries.
for node in ast.parse(p.read_text()).body:
 if isinstance(node,(ast.FunctionDef,ast.AsyncFunctionDef)) and any(k in node.name for k in ('phase','generate','source','run','load','prepare','main')):print('FUNCTION_SPAN',node.name,node.lineno,node.end_lineno)
