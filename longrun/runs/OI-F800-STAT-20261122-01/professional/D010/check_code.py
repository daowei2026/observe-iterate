"""必要注入/身份/空输出检查；只建内存模型，不另生成预期HTML。"""
from pathlib import Path
import ast
import copy
import csv
import hashlib
import inspect
import json
import sys
import uuid
import numpy as np
import pandas as pd

ROOT=Path(__file__).resolve().parent
sys.argv=[str(ROOT/'preview.py'),'v4']
import preview as sample
from display_code import caegraph_display as impl

passed=[]
def check(name,condition,detail):
    if not condition:raise AssertionError(name+': '+str(detail))
    passed.append(dict(check=name,pass_=True,evidence=detail))

src=(ROOT/'display_code/caegraph_display.py').read_bytes()
tree=ast.parse(src)
signature=inspect.signature(impl.build_display)
check('required_injection_signature',all(signature.parameters[k].default is inspect.Parameter.empty for k in ('instance','reader','context','position','fields')),str(signature))
forbidden=('TA_updto20240229_DBA','2021-01-01','2023-12-31','CommonPriceTurnGroupCandidatesFrp','result_dir','loadFeature')
strings=[x.value for x in ast.walk(tree) if isinstance(x,ast.Constant) and isinstance(x.value,str)]
check('no_final_instance_sof_result_path_or_B_literal',not any(any(word in s for word in forbidden) for s in strings),{'scanned_file':'display_code/caegraph_display.py','forbidden_literals':list(forbidden)})
f=pd.DataFrame({'form':['1'],'high':[str(2**64-1)],'low':[str(2**64-2)],'text':['']})
cols={k:k for k in ('form','high','low','text')}
decoded=impl.decode_exact(f,cols).iloc[0]
check('uuid_uint64_lossless',decoded==str(uuid.UUID(int=2**128-2)),{'decoded':decoded,'words_as_decimal_text':True})
try:impl.decode_exact(f.assign(high=float(2**64-1)),cols)
except ValueError:rejected=True
else:rejected=False
check('float_identity_rejected',rejected,'不从浮点数猜回64位身份')

actual=ROOT.parent/'D008/readback/tables/occurrences.csv'
with actual.open(encoding='utf-8-sig') as stream:one=next(csv.DictReader(stream))
template=json.loads((ROOT/'FIELD_MAP_TEMPLATE.json').read_text())['fields']
required={v for spec in template['groups'].values() for v in (spec.values() if isinstance(spec,dict) else [spec])}
check('actual_public_schema_shape',required.issubset(one),{'required_fields':len(required),'actual_header_fields':len(one),'source':'D008/readback/tables/occurrences.csv（仅首行/表头）'})
realcodec=impl.decode_exact(pd.DataFrame([one]),template['groups']['life']).iloc[0]
check('current_native_identity_codec',bool(uuid.UUID(realcodec)),{'first_native_life':realcodec,'read_only_shape_probe':True,'not_instance_binding':True})

data=copy.deepcopy(sample.DATA);fields=copy.deepcopy(sample.fields)
rename={k:'injected_'+k for k in fields['groups']}
data['groups']=data['groups'].rename(columns=rename)
fields['groups']={k:rename[v] for k,v in fields['groups'].items()}
position=copy.deepcopy(sample.position)
position.update(symbols=['hc'],start=int(sample.u0)+1200,end=int(sample.u1)-1200,width=900)
sentinel=object();calls=[]
def reader(instance,pos):
    calls.append((instance,pos.copy()));return data
layout,meta=impl.build_display(instance=sentinel,reader=reader,context=sample.context,position=position,fields=fields,caption='contract check only; no HTML')
check('instance_position_field_replacement_native_run',calls[0][0] is sentinel and meta['fig_count']==3 and len(meta['records'])==6 and meta['shared_x_range'],
      {'instance_is_injected_object':True,'single_symbol':'hc','positions_are_injected_integer_UTI':True,'all_group_role_columns_renamed':True,'native_figures':meta['fig_count'],'native_revision_points':len(meta['records'])})
source=meta['revision_source'].data
check('same_tick_exact_records_not_merged',source['x'][1]==source['x'][2] and source['y'][1]!=source['y'][2] and source['revision'][1]!=source['revision'][2],
      {'same_known':int(source['x'][1]),'distinct_rows':[float(source['y'][1]),float(source['y'][2])]})
detail=json.loads(meta['records'][2]['raw'])
check('full_parent_children_retained',detail['group']['child_id_2']==1 and len(detail['children']['members'])==3 and len({m['memberObject'] for m in detail['children']['members']})==3,
      {'parent_child_id_2':1,'member_count':3,'objects':sorted(m['memberObject'] for m in detail['children']['members'])})
ohlc=[n.cds for _,n in impl.walk(meta['roots']) if 'close' in n.cds.data]
check('native_price_nan_not_filled',len(ohlc)==1 and int(np.isnan(np.asarray(ohlc[0].data['close'])).sum())==1,
      {'native_ohlc_sources':len(ohlc),'close_nan_count':int(np.isnan(np.asarray(ohlc[0].data['close'])).sum())})
clipped=impl.clipped(pd.DataFrame(dict(a=[10],d=[30],y0=[0.],y1=[10.])),'a','d','y0','y1',15,25)
check('display_clipping_preserves_raw',clipped.iloc[0].a==10 and clipped.iloc[0].d==30 and clipped.iloc[0].draw_x0==15 and clipped.iloc[0].draw_x1==25,
      {'raw':[10,30],'display':[15,25],'no_business_value_mutation':True})
empty=copy.deepcopy(data);empty['groups']=empty['groups'].iloc[:0]
empty['children']={k:v.iloc[:0] for k,v in empty['children'].items()}
_,em=impl.build_display(instance=object(),reader=lambda i,p:empty,context=sample.context,position=position,fields=fields,caption='empty publication check; no HTML')
check('definitions_only_empty_output',len(em['records'])==0 and len(em['revision_source'].data['x'])==0,{'invented_group_points':0,'html_generated':False})
bad=copy.deepcopy(data);bad['groups']=pd.concat([bad['groups'],bad['groups'].iloc[[0]]],ignore_index=True)
try:impl.build_display(instance=object(),reader=lambda i,p:bad,context=sample.context,position=position,fields=fields,caption='reject duplicate')
except ValueError:rejected=True
else:rejected=False
check('duplicate_full_parent_rejected',rejected,'不以时间/known去重或合并父组')

browser=json.loads((ROOT/'BROWSER_v4.json').read_text())
check('current_html_real_browser',len(browser['plots'])==5 and len({p['x_range'] for p in browser['plots']})==1 and not browser['console'] and not browser['external_requests'],
      {'plots':5,'console':browser['console'],'external_requests':browser['external_requests'],'actual_UI_selection':browser['ui_select_probe'],'output_legend':browser['output_legend']})
check('current_prototype_C3_byte_equal',src==(ROOT/'archive/current_impl_v4.py').read_bytes(),{'sha256':hashlib.sha256(src).hexdigest(),'current_preview_renderer':'archive/current_impl_v4.py','second_expectation_html_generated':False})
out={'status':'PASS','checks':passed,'check_count':len(passed),'sample_models_only':True,'formal_feature_run':False,'final_B_binding':False,
     'C2_unique_html':'html/current.html','C3_source_sha256':hashlib.sha256(src).hexdigest(),'actual_uplot_path':str(Path(sys.modules['mquant.uplot'].__file__).resolve())}
(ROOT/'CODE_VALIDATION.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'status':'PASS','check_count':len(passed),'C3_source_sha256':out['C3_source_sha256']},ensure_ascii=False))
