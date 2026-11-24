"""只读确认原正式 m 范围的原生交易集及原 Run fresh 写面。"""
import datetime
import hashlib
import json
from pathlib import Path

from mquant.frame.lang.internal.base import AbsFao
def forbidden(*args, **kwargs):
    raise RuntimeError('A05_PREFLIGHT_FORBIDS_FEATURE_RUN')
AbsFao.run=forbidden
AbsFao.rerun=forbidden
from mquant.quant import OptContext
from m3tt import CurrTradeSet,CurrSymbol
from mquant.frame import CurrCalendar,TmpStoreEnv,CurrCalType,CalType
from mquant.frame.core.app.env import StraEnv
from mquant.tis.hf.prel0.p1_dba_export import P1DbaExportMixin
from mquant.tis.hf.prel0.p1_product_receipt import load_p1_product_receipt
from mquant.tis.hf.prel0.attack_flow_assembler import AttackFlowAssembler

base=Path(__file__).resolve().parent
old=json.loads((base.parent/'formal-attempt-A03/execution_result.json').read_text())
store=Path(old['store_root'])
previous={row['feature']:row for row in old['feature_results'] if row['symbol']=='m'}
assert previous['wall']['status']=='EXECUTED_AND_FULL_READBACK_VERIFIED'
context=OptContext({'sof_name':'TA_updto20240229_DBA','stk_tlist':'m','startDay':'2021-01-01','endDay':'2021-12-31'})
result={'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'call_id':'C0009','attempt_id':'A05','feature_run':False,'store_root':str(store),'source_scope_requested_unchanged':True,'p1':{}}
with CurrTradeSet(context.sof),CurrSymbol('m'),CurrCalendar('night_end_at_2300'),TmpStoreEnv(rule=P1DbaExportMixin,store_dir=str(store)):
    result.update(stk_tlist=context.stk_tlist,actual_trading_symbols=list(CurrTradeSet.symbols()),symbol_index=CurrSymbol.ii(),trading_unit=CurrTradeSet.sof().symbols_unit[CurrSymbol.ii()],sof_ori_dir=str(context.sof.ori_dir),start=str(context.sof.startDay),end=str(context.sof.endDay))
    assert result['actual_trading_symbols']==['m']
    attack=AttackFlowAssembler()
    for name,feature in {'wall':attack.P.wall,'tactical':attack.P.directed_large_deal_tactical,'structural':attack.P.directed_large_deal_structural,'attack':attack}.items():
        path=Path(feature.full_dir)
        assert str(path)==previous[name]['full_dir'] and str(feature.ppid)==previous[name]['ppid']
        assert not feature.backup_full_dirs and path.is_relative_to(store)
        exists=path.exists()
        if name=='wall':
            assert exists and load_p1_product_receipt(feature,'wall_lifecycle')==previous['wall']['receipts'][0]
        else:
            assert not exists,'A05_REFUSES_EXISTING_TARGET:'+str(path)
        result['p1'][name]={'path':str(path),'exists_before_A05':exists,'ppid':str(feature.ppid),'operation':'READONLY_REUSE_CURRENT_RUN' if name=='wall' else 'FRESH_GENERATION_NO_OVERWRITE'}
(base/'evidence/x_preflight-A05.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(result,ensure_ascii=False))
