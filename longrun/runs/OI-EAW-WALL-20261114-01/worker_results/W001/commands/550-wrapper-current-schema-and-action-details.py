import pathlib,json,ast,hashlib,re
B=pathlib.Path('/dwdhome/fy/BASE_E6_2');W=pathlib.Path(__file__).resolve().parents[1]
p=B/'mquant/worker/adt/dbaw.py';print('GENERATED_WRAPPER',p,'EXISTS',p.exists(),'BYTES',p.stat().st_size if p.exists() else None)
if p.exists():
 data=p.read_bytes();text=data.decode();tree=ast.parse(text);names=[n.name for n in tree.body if isinstance(n,ast.ClassDef)];print('SHA256',hashlib.sha256(data).hexdigest(),'CLASSES',len(names),'WALL_P1_CLASSES',[n for n in names if 'Wall' in n or 'P1' in n]);print('HAS_EXPECTED_LEGACY', 'MulWrap_P1WallOccurrenceStorage' in names);print('HAS_EXPECTED_CURRENT', [n for n in names if 'WallOccurrenceBatch' in n or 'WallCurrentBatch' in n or 'WallDiagnostic' in n])
 (W/'evidence/GENERATED_WRAPPER_BINDING.json').write_text(json.dumps({'path':str(p),'sha256':hashlib.sha256(data).hexdigest(),'bytes':len(data),'class_count':len(names),'p1_wall_class_names':[n for n in names if 'Wall' in n or 'P1' in n],'legacy_required':['MulWrap_P1WallOccurrenceStorage','MulWrap_P1WallCurrentStorage','MulWrap_P1DiagnosticStorage'],'legacy_required_present':{k:k in names for k in ['MulWrap_P1WallOccurrenceStorage','MulWrap_P1WallCurrentStorage','MulWrap_P1DiagnosticStorage']},'current_required_present':{k:k in names for k in ['WallOccurrenceBatch','WallCurrentBatch','WallDiagnostic']},'runtime_import_performed':False,'reason':'AST-only static check; no project import'},ensure_ascii=False,indent=2)+'\n')
for rel,spans in [('mquant/frame/lang/frp/base.py',[(169,222)]),('mquant/tis/test/integration/verify_eaw_p1_real_run.py',[(20,82),(507,575),(596,651),(800,822)]),('edh-universe/frp/frp/src/Frp/Instance/ISL/Eaw/P1/Products.hs',[(300,400)]),('edh-universe/frp/frp/src/Frp/Instance/ISL/Eaw/P1/WallLifecycle.hs',[(15,180)])]:
 p=B/rel;print('FILE',p);lines=p.read_text().splitlines()
 for lo,hi in spans:
  for n in range(lo,min(hi,len(lines))+1):print(f'{n}: {lines[n-1]}')
