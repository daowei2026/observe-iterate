from pathlib import Path
import json,sys,importlib.util,hashlib
import numpy as np
import pandas as pd
from pydim import DbArray
root=Path(__file__).resolve().parent;stage=root/"turn_staging"
sym=sys.argv[1];role=sys.argv[2]
state=json.loads((stage/(sym+"__"+role+".state.json")).read_text());assert state['state']=='generated_pending_readback'
catalog=json.loads((root/'turn_parameter_catalogue.json').read_text())
preset={'small':'small','mid':'mid','big':'large'}[role]
item=next(x for x in catalog['rows'] if x['preset']==preset)
formal=Path(next(x for x in item['symbols'] if x['symbol']==sym)['path'])
cache=(stage/'cache')/formal.relative_to('/m3varF');assert (cache/'fields.json').is_file(),str(cache)
reader=Path('/m3varF/BaseData/futures/GTQH_L1_20210104_20240208/feature-parameters/read_verified_native_e.py')
spec=importlib.util.spec_from_file_location('source_verified_E_reader',reader);module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
frames=module.load_verified_native_e(sym,cache_root=str(cache.parent))
base=Path('/m3varF/BaseData/futures/GTQH_L1_20210104_20240208/pnv/30m')/sym
close_uti=DbArray(str(base),'closeUti','i8').ndarray;close=DbArray(str(base),'close','f8').ndarray;prices=dict(zip(map(int,close_uti),map(float,close)))
checks={}
for name,df in frames.items():
 vals={}
 for x,y in [('x','y'),('xConfirm','yConfirm')]:
  vals[x]={'all_positions_on_gtqh_30m_close_axis':all(int(v) in prices for v in df[x]),'all_prices_match_gtqh_30m_close':all(int(v) in prices and abs(prices[int(v)]-float(p))<1e-8 for v,p in zip(df[x],df[y]))}
 assert all(v for row in vals.values() for v in row.values()),(sym,role,name,vals)
 checks[name]={'rows':len(df),'coordinate_checks':vals}
 frame=df.copy();frame['turn_round']=name
 frames[name]=frame
combined=pd.concat(list(frames.values())).sort_values('x',kind='stable');combined.index.name='event_ts'
csv_path=stage/'validated_csv'/(sym+'__'+role+'.csv');csv_path.parent.mkdir(exist_ok=True);combined.to_csv(csv_path)
report={'symbol':sym,'role':role,'preset':preset,'feature_ppid':item['feature_ppid'],'original_E_output':str(cache),'native_parameter_path':str(cache.parent.relative_to(stage/'cache')),'engine_binary_sha256':json.loads((root/'generation_engine_readiness.json').read_text())['current_sha256'],'rows':len(combined),'rounds':checks,'validated_csv':str(csv_path),'csv_sha256':hashlib.sha256(csv_path.read_bytes()).hexdigest(),'source_dataset':'GTQH_L1_20210104_20240208','readback':'原E ADT Int/Double读取器，保持实际x/y与确认位置语义','formal_F_source_modified':False}
(stage/(sym+'__'+role+'.validated.json')).write_text(json.dumps(report,ensure_ascii=False,indent=2));print(json.dumps(report,ensure_ascii=False,indent=2),flush=True)
