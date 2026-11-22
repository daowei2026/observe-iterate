"""G1 只在新X独立验收后成立；复用结构合同并核当前最小版本适用绑定。"""
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
import json
ROOT=Path(__file__).resolve().parent
def load(n): return json.loads((ROOT/n).read_text())
def write(n,x): (ROOT/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
B=load('FeatureRunResultBinding.json'); U=load('CurrentFeatureUnderstandingPackage.json')
assert B['readback_validation']['all_31_tables_equal'] and B['readback_validation']['independent_process']
assert B['code_version']['frp'].split('@')[1]==U['feature_ref']['code_version']['frp']=='39f02ec4548e68ba8dbd30061afc870546000994'
assert B['code_version']['tis'].split('@')[1]==U['feature_ref']['code_version']['tis']=='2f460d663d821cf2ba25555eda13e78b697d0767'
assert B['parameter_version']==U['current_applicability']['parameter_version']==sha256((ROOT/'configuration.json').read_bytes()).hexdigest()
assert U['current_applicability']['structural_contract_changed'] is False
U['historical_gap_snapshot']=U['unconfirmed_items']
U['unconfirmed_items']=[dict(id='U3',gap='内部逐Tick材料/枚举/首次阻断轨迹未公开；独立上游分母与筛查可读取，但不能冒充native轨迹',impact='以公开结果与明确参考筛查限域统计，不阻断主要剖面'),
    dict(id='U5',gap='800的完整业务合理性与跨市场场景解释不由本G预先证明',impact='原生Gate按最新完整G与finding复验给出；场景问题保留')]
for obj in U['business_objects']:
    obj['historical_unconfirmed']=obj.get('unconfirmed')
    obj['current_evidence']='UPSTREAM_EXTRACTION.json' if obj['id'] in ('BO1','BO2') else 'FeatureRunResultBinding.json'
    obj['unconfirmed']='未暴露全部潜在原始市场转折，当前分母为准确上游Rct/ScaleTurn' if obj['id']=='BO1' else None
for occurrence in U['occurrences']:
    occurrence['historical_unconfirmed']=occurrence.get('unconfirmed')
    occurrence['unconfirmed']='没有独立selected_time列，已由上游原事件轴保留知识时间' if occurrence['id']=='O2' else None
    occurrence['current_evidence']='FeatureRunResultBinding.json; UPSTREAM_EXTRACTION.json'
for parameter in U['parameters']:
    parameter['historical_unconfirmed']=parameter.get('unconfirmed')
    if parameter['id']=='P1':parameter['unconfirmed']='已由实际引擎解码与480000UTI原生责任窗验实；800并非标定结论'
    if parameter['id']=='P6':parameter['unconfirmed']=None
for field in U['run_result_field_map']:
    if field.get('availability')=='UNCONFIRMED':
        field['availability']='AVAILABLE'
        field['scope']='D008准确实例31表独立读回已验收；空子表表示本输入未观察到该分支，不补造发生'
U['completion_statement']='复用D001结构合同，完成新39f最小适用绑定；X字段/加载/全范围及上游分母缺口已由本次真实读回解析，剩余内部未暴露轨迹及业务场景边界不强造。'
U['artifacts']['public_table_contract']='PUBLIC_TABLE_SCHEMA.json'
write('CurrentFeatureUnderstandingPackage.json',U)
old=ROOT.parent/'D002'
ready=json.loads((old/'StatisticsInputReadiness.json').read_text())
ready['prior_understanding_ref']=U['current_applicability']['original_package_ref']
ready['current_understanding_ref']='CurrentFeatureUnderstandingPackage.json'
ready['current_applicability_basis']=U['reuse_basis'][:4]
ready['binding_match']=dict(code_version='MATCH',parameter_version='MATCH',data_scope='CONFIRMED')
scope=load('INPUT_SCOPE_VALIDATION.json')
ready['data_quality_findings']=[dict(symbol=r['symbol'],rows=r['rows'],first=r['first'],last=r['last'],
    missing_close=r['close_nonfinite'],uti_step_distribution=r['uti_step_distribution'],
    duplicate_timestamps=r['duplicate_timestamps'],out_of_order=r['out_of_order']) for r in scope['symbols']]
ready['data_quality_findings'].append('31表独立OnlyRead完整且与生产后读取hash一致；未暴露内部逐Tick trace不冒充已统计结果。可选空分支按真实读表结果记录。')
ready['checked_at']=datetime.now(timezone.utc).isoformat()
ready['readiness_status']='PARTIAL'
ready['readiness_explanation']='核心代码/实例/Calendar/范围、对象/时间/父子键与完整公开表已可靠；D001结构理解按D007合同不变适用链与J4 delta绑定新39f，保留内部逐Tick/全部试探不暴露的界限。'
write('StatisticsInputReadiness.json',ready)
print('G1 binding MATCH / MATCH / CONFIRMED; current understanding applicable; core inputs qualified')
