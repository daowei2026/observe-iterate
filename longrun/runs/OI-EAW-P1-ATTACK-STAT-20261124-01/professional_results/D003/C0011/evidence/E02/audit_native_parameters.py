"""E02：只构造默认实例并核加载文件/参数消费，不运行任何Feature。"""
import ast
import datetime
import hashlib
import inspect
import json
from pathlib import Path

BASE=Path(__file__).resolve().parent
from mquant.frame.lang.internal.base import AbsFao
def forbidden(*args,**kwargs):raise RuntimeError('E02_FORBIDS_ALL_FEATURE_RUNS')
AbsFao.run=forbidden
AbsFao.rerun=forbidden
from mquant.quant import OptContext
from m3tt import CurrTradeSet,CurrSymbol
from mquant.frame import CurrCalendar
import mquant.tis.t0.gen.cc as cc
import mquant.tis.hf.mc as mc
import mquant.tis.hf.prel0.tick_quote_context as tq
import mquant.tis.hf.prel0.pressure_big_deal as f4
import mquant.tis.hf.prel0.wall_assembler as wall
import mquant.tis.hf.prel0.attack_flow_assembler as attack_module
import mquant.tis.hf.prel0.p1_dba_export as export

def encode(v):
    if v is None or isinstance(v,(str,int,float,bool)):return v
    if hasattr(v,'items'):return {str(k):encode(x)for k,x in v.items()}
    if isinstance(v,(list,tuple)):return [encode(x)for x in v]
    if hasattr(v,'val'):return encode(v.val)
    return str(v)
e=json.loads((BASE/'diagnostic-E01/diagnostic_result.json').read_text())
b=json.loads((BASE/'sources/x_binding.json').read_text())
modules=[]
for mod in (cc,mc,tq,f4,wall,attack_module,export):
    path=Path(mod.__file__).resolve();row=next(x for x in e['implementation_sources']if x['path']==str(path));assert hashlib.sha256(path.read_bytes()).hexdigest()==row['sha256']
    modules.append({'module':mod.__name__,'actual_loaded_file':str(path),'sha256':row['sha256'],'same_copy_snapshot_as_E01':True})
context=OptContext({'sof_name':'TA_updto20240229_DBA','stk_tlist':'m','startDay':'2021-01-01','endDay':'2021-12-31'})
features=[]
with CurrTradeSet(context.sof),CurrSymbol('m'),CurrCalendar('night_end_at_2300'):
    a=attack_module.AttackFlowAssembler()
    for name,obj in {'wall':a.P.wall,'tactical':a.P.directed_large_deal_tactical,'structural':a.P.directed_large_deal_structural,'attack':a}.items():
        old=next(x for x in b['per_feature_results']if x['symbol']=='m'and x['feature']==name)
        assert str(obj.ppid)==old['ppid']
        row={'feature':name,'ppid':str(obj.ppid),'same_as_original_bound_default_instance':True}
        if name in ('tactical','structural'):
            row['actual_parameters']=encode(obj.P)
            assert row['actual_parameters']==old['constructor_parameters']
        features.append(row)
source=inspect.getsource(tq.TickQuoteContextWrapperSupport._trading_day_chunk_plan)
tree=ast.parse(source.lstrip()) if not source.startswith('    ') else ast.parse(__import__('textwrap').dedent(source))
assert not any(isinstance(x,ast.Attribute)and x.attr=='P'for x in ast.walk(tree))
load_source=inspect.getsource(tq.TickQuoteContextWrapperSupport._load_cc_df)
assert 'self.P'not in load_source
result={
 'experiment_id':'E02','call_id':'C0011','delegation_id':'D003','qualification':'DIAGNOSTIC_ONLY_CONSTRUCTION_AND_SOURCE_AUDIT','checked_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'status':'PASS','Feature_run_permitted':False,'actual_modules':modules,'default_instances':features,
 'native_planner_reads_exposed_Feature_parameters':False,'shared_loader_reads_exposed_Feature_parameters':False,
 'parameter_consumers':[
  {'parameters':['parameter_set_id'],'consumer':'实例寻址/元数据，不改变cc时间轴'},
  {'parameters':['qualification_family','lane_threshold_map'],'consumer':'pressure_big_deal.py:593-597资格族一致性；179-193 threshold材料及247-250分块后阈值对齐；不改变cc索引'},
  {'parameters':['amt_n'],'consumer':'pressure_big_deal.py:176-193 AmountThreshold材料；与cc索引单独加载'},
  {'parameters':['same_best_tol_ticks','big_deal_ratio_min'],'consumer':'pressure_big_deal.py:230先分块校验，261以后才进入compute_pressure_big_deal_chunk业务计算'},
  {'parameters':['Attack自身参数'],'consumer':'Attack在755以后先取得Wall/F4；未到Attack业务计算，不能修复上游planner输入合同'}
 ],
 'hardcoded_or_external_constraints':[
  {'constraint':'searchsorted(start,left)/searchsorted(stop,right)、expected_start=0、严格start==previous_stop和末尾coverage==len(cc)','consumer':'tick_quote_context.py:220-246','effect':'固定输入轴覆盖不变量；没有可调缺口容忍参数'},
  {'constraint':'trading_days读取原生main_contract/m.csv，cc索引来自指定半秒calendar','consumer':'hf/mc.py:22-35；t0/gen/cc.py:150-183','effect':'当前正式SOF/日历/范围为输入绑定，不是可任意调参换范围的业务参数'},
  {'constraint':'DEFAULT_EPS_VOL=1e-12及uti=linear_ts//500-1','consumer':'pressure_big_deal_core.py:24及tick_quote_context.py:96-108','effect':'数值/半秒映射，不参与此次先于core的timestamp区间覆盖检查'}
 ],
 'parameter_repairability':{'feasibility_status':'PROVEN_NOT_ADJUSTABLE','scope':'当前正式已暴露的Attack/F4业务参数及已核数值容差常量，针对本次区间覆盖失败','proof':'相同cc.index和trading_days决定planner结果，planner/loader不读上述P；所有阈值和数值计算位于已失败覆盖检查之后或与cc独立。','not_claimed':'未声称所有实现方式或上游合同都无解；上游输入适配/元数据/分块合同需要其责任面处理，当前D不修改。'},
 'source_or_product_changes':False,'formal_X_or_G_performed':False
}
(BASE/'evidence/native_parameter_audit.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'E02':'PASS','actual_module_files':len(modules),'bound_default_instances':len(features),'Feature_runs':0,'parameter_repairability':result['parameter_repairability']['feasibility_status']},ensure_ascii=False))
