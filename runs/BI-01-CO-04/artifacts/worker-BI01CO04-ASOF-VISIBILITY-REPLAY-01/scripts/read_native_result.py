"""使用已核的原Int/Double ADT reader读回本单原生结果，不计算特征。"""
from pathlib import Path
import sys,importlib.util,json,hashlib
OUT=Path(__file__).resolve().parents[1]
sym=sys.argv[1];role=sys.argv[2];label=sys.argv[3]
receipt=json.loads((OUT/f'copied/baseline/copied/config_and_consumption/jobs/{sym}__{role}.validated.json').read_text())
directory=OUT/'execution/cache'/receipt['native_parameter_path']/sym
reader=OUT/'copied/baseline/copied/config_and_consumption/read_verified_native_e.py'
spec=importlib.util.spec_from_file_location('frozen_native_reader',reader);mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
frames=mod.load_verified_native_e(sym,cache_root=str(directory.parent),adt_source=str(OUT/'copied/baseline/copied/config_and_consumption/original_E_dbaw.py'))
rows=[]
for rnd,df in frames.items():
 for event,row in df.iterrows():rows.append({'symbol':sym,'scale':role,'turn_round':rnd,'event_ts':str(event),'x':int(row.x),'y':float(row.y),'xConfirm':int(row.xConfirm),'yConfirm':float(row.yConfirm)})
data={'source':'actual native recomputation','reader_sha256':hashlib.sha256(reader.read_bytes()).hexdigest(),'rows':rows}
p=OUT/'recomputed'/label;p.mkdir(parents=True,exist_ok=True);(p/f'{sym}_{role}.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'symbol':sym,'scale':role,'rows':len(rows),'path':str(p/f'{sym}_{role}.json')},ensure_ascii=False))
