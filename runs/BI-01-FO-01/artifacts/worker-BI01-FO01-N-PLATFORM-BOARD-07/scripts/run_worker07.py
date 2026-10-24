"""W07 有限正常入口调用。需按 README 设置已核环境；不启动平台服务。"""
from pathlib import Path
import argparse, datetime, hashlib, io, json, os, subprocess, sys, traceback

REPO = Path('/dwdhome/fy/observe-iterate-bi01-fo-01')
OUT = Path(__file__).resolve().parents[1]
W02 = 'runs/BI-01-FO-01/artifacts/worker-BI01-FO01-N-DISPLAY-INTEGRATION-02/'
W03 = 'runs/BI-01-FO-01/artifacts/worker-BI01-FO01-N-READABILITY-CROSSK-03/'
R02 = '081e31241a0c88e47631f80a8b9b8dd43b2b569c'
R03 = 'd04f3b08892ccf334a06028f3caab994743566a0'


def raw(ref, path):
    return subprocess.check_output(['git','-C',str(REPO),'show',f'{ref}:{path}'])


def put(payload, path, source):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(payload)
    return {'path':str(path), 'sha256':hashlib.sha256(payload).hexdigest(), 'source':source}


def prepare():
    import pandas as pd
    from mquant.aidata.u2_normal_node_behavior_display import FORMAL_PRODUCTS
    cases = {
        'rb':(R02,W02+'data/selected_cuts/final/',R02,W02+'data/same_bound_price/rb_5m_price_calendar.csv',103315800,'b340dc6c-c135-462b-b6e0-04d24622c180','cfd51328-e2cf-4360-8314-20c9238e93fb','#4C78A8'),
        'i':(R03,W03+'data/crossk/i_recovery/',R02,W02+'data/i_missing_context/i_5m_price_calendar.csv',35361000,'9410abda-b111-442d-aa25-6b99da2afeb6','1d82177d-6e82-44fd-b4b8-8cb899a94e28','#F58518'),
        'hc':(R03,W03+'data/crossk/hc_final/',R03,W03+'data/crossk/hc_final/hc_5m_price_calendar.csv',103315800,'6f92034c-bd94-4d3f-8b7c-6c69e24959ff','76d5cfc3-f505-4b62-89b8-b081aedb90f0','#54A24B'),
    }
    selections = {}
    for symbol,(ref,folder,pref,price_path,K,life,revision,color) in cases.items():
        tables = {}
        # 原 intervals 为节律依赖；所有原表按指定 Git blob 复制，不从图投影还原。
        for name in (*FORMAL_PRODUCTS, *(['intervals'] if symbol!='rb' else [])):
            path=folder+name+'.csv'
            tables[name]=put(raw(ref,path),OUT/'inputs'/symbol/(name+'.csv'),{'repository':'daowei2026/observe-iterate','commit':ref,'path':path})
        price_raw=raw(pref,price_path)
        price=pd.read_csv(io.BytesIO(price_raw),dtype=str,keep_default_na=False)
        uti=pd.to_numeric(price.open_uti)
        keep=uti.le(K)
        source={'repository':'daowei2026/observe-iterate','commit':pref,'path':price_path,
                'original_sha256':hashlib.sha256(price_raw).hexdigest(),'selection':'open_uti <= knowledge K'}
        payload=price_raw if keep.all() else price.loc[keep].to_csv(index=False).encode()
        selection={'symbol':symbol,'color':color,'node_life':life,'as_of':K,
            'expected_exact':f'NodeBehaviorBook/NodeScaleTurnBehaviorRevision/{life}/{revision}',
            'tables':tables,'price':put(payload,OUT/'inputs'/symbol/'supplied_price_calendar.csv',source),
            'optional_panels':['rhythm','waiting_time']+(['duration'] if symbol=='i' else []),
            'accepted_display':'aidata@8a08300cb70a610401424bedadb42e9dcde13e71; M21 accepted W06',
            'selection_qualification':'正常 OnlyRead 原表的固定知识切面；缓存适配器身份与原 N 产品身份分开'}
        if symbol=='hc':
            selection['price_references']=[{'uti':103057800,'field':'close','label':'last_update 原close3952'},
                {'uti':103058400,'field':'close','label':'下一根close3946'},
                {'uti':103058400,'field':'high','label':'下一根high3959（非close更新）'},
                {'uti':K,'field':'close','label':'末拍close3904'}]
        selections[symbol]=selection
    return selections


def make_brief(selection, context, run_root, run_id):
    import pandas as pd
    from mquant.aidata.csv_feature import ReadOnlyCsvFeature
    symbol=selection['symbol']
    ranges={'rb':[(100443000,103315800,'rb_final_full'),(103140000,103315800,'rb_final_local')],
            'i':[(35339400,35361000,'i_recovery')], 'hc':[(103044000,103315800,'hc_close_waiting_final')]}[symbol]
    natural=context.sof.tsa_of('night_end_at_2300')['natural_tsa']
    price=pd.read_csv(selection['price']['path'])
    time_field=price.columns[0]
    spans=[]
    for start,end,label in ranges:
        stamps=[str(pd.Timestamp(natural[u])) for u in [start,end]]
        for u,stamp in zip([start,end],stamps):
            matches=price.loc[price.open_uti.eq(u),time_field]
            assert len(matches)==1 and pd.Timestamp(matches.iloc[0])==pd.Timestamp(stamp), (u,stamp,matches.tolist())
        spans.append(dict(start_uti=start,end_uti=end,start_ts=stamps[0],end_ts=stamps[1],label=label))
    anchors=[]
    for name,spec in selection['tables'].items():
        feature=ReadOnlyCsvFeature(dict(alias=f'W07_{symbol}_formal_{name}',path=spec['path'],sha256=spec['sha256'],symbol_field='',index_field='timestamp'))
        anchors.append(dict(feature=feature,anchor_name=f'{symbol}_formal_{name}',feature_key=f'{symbol}_formal_{name}',target_id=symbol,
            df_key=None,slice_levels=['big'],time_binding={'time_mode':'index_natural'}))
    ps=selection['price']
    pf=ReadOnlyCsvFeature(dict(alias=f'W07_{symbol}_original_price_calendar',path=ps['path'],sha256=ps['sha256'],symbol_field='',index_field=time_field))
    anchors.append(dict(feature=pf,anchor_name=f'{symbol}_price_calendar',feature_key=f'{symbol}_price_calendar',target_id=symbol,
        slice_levels=['big'],time_binding={'time_mode':'index_natural'},role='market_context_sidecar',evidence_role='market_context_sidecar',is_raw_market_data=True))
    return dict(output_root=str(run_root),run_id=run_id,context=context,blk=symbol,calendar_override='night_end_at_2300',
        generation_depth='big',big_source={'mode':'manual','timespans':spans},evidence_features=anchors,
        normal_node_behavior=selection,run_note='W07 M21已认可N画法的工作3技术接入；未签工作4',
        chart_review={'fig_width_big':1800})


def main():
    # 上游连接库的 INFO 日志含连接配置；不让它进入本单可读调用记录。
    import logging
    logging.disable(logging.INFO)
    parser=argparse.ArgumentParser()
    parser.add_argument('--run-root',required=True)
    parser.add_argument('--private-evidence',required=True)
    parser.add_argument('--symbols',nargs='+',default=['rb','i','hc'])
    parser.add_argument('--prefix',required=True)
    args=parser.parse_args()
    from mquant.quant import OptContext
    from mquant.aidata.api import build_chart_run,build_big_world_chart_pages,build_board_run
    selections=prepare()
    context=OptContext(sof_name='TA_updto20240229_DBA')
    private=Path(args.private_evidence);private.mkdir(parents=True,exist_ok=True)
    results={}
    for symbol in args.symbols:
        result={};results[symbol]=result
        rbi=make_brief(selections[symbol],context,Path(args.run_root),args.prefix+'-'+symbol)
        (OUT/'run_briefs').mkdir(exist_ok=True)
        plain={k:v for k,v in rbi.items() if k not in ['context','evidence_features']}
        plain['context']={'sof_name':'TA_updto20240229_DBA'}
        plain['evidence_features']=[{k:v for k,v in a.items() if k!='feature'}|{'feature_class':type(a['feature']).__name__,'ppid':a['feature'].ppid,'params':a['feature'].fason} for a in rbi['evidence_features']]
        (OUT/'run_briefs'/f'{symbol}.json').write_text(json.dumps(plain,ensure_ascii=False,default=str,indent=2)+'\n')
        try:
            run=build_chart_run(rbi)
            result['chart']={'run_id':run.run_id,'run_dir':str(run.run_dir),'timespan_sha256':hashlib.sha256(run.timespan_index_path.read_bytes()).hexdigest()}
            print(symbol,'chart complete',run.run_id,flush=True)
        except Exception:
            result['chart_error']=traceback.format_exc();continue
        try:
            pages=build_big_world_chart_pages(run,run_brief_input=rbi,save=True)
            pages.to_json(private/f'{symbol}-pages.private.json',orient='records',force_ascii=False,indent=2)
            result['pages']={'count':len(pages),'actual_urls_private':str(private/f'{symbol}-pages.private.json')}
            print(symbol,'normal CAE registration complete',len(pages),flush=True)
        except Exception:
            result['pages_error']=traceback.format_exc()
            print(symbol,'pages failed; board continues',flush=True)
        try:
            board=build_board_run({**rbi,'run_id':run.run_id},reuse_core=True)
            after=hashlib.sha256(board.timespan_index_path.read_bytes()).hexdigest()
            assert result['chart']['timespan_sha256']==after
            result['board']={'run_id':board.run_id,'same_frozen_core':True,'run_dir':str(board.run_dir)}
            print(symbol,'board complete same core',flush=True)
        except Exception:
            result['board_error']=traceback.format_exc()
        (private/'API_RESULTS.private.json').write_text(json.dumps(results,ensure_ascii=False,indent=2)+'\n')
    (private/'API_RESULTS.private.json').write_text(json.dumps(results,ensure_ascii=False,indent=2)+'\n')
    print('finite API sequence finished',flush=True)


if __name__=='__main__':
    main()
