"""R0009 bounded reference checks. Run: python verify_r0009.py.

Inputs below are explicitly transcribed field excerpts from the cited immutable
GitHub files actually read in this round. They are NOT a fresh N read, a new
formal product, or the full 433/500-row datasets. No network or platform imports.
"""
from __future__ import annotations
import hashlib
import json
import math
from statistics import median
from pathlib import Path
from u2_normal_node_behavior import (CONFIG_VERSION, configs, display_config,
    numeric_display_range, evolution_display_range)

ROOT = Path(__file__).resolve().parent
INVOCATION = 'BI01-FO-01-R0009-20261022T104606Z-658cee31'
SOURCE = 'daowei2026/observe-iterate@081e31241a0c88e47631f80a8b9b8dd43b2b569c:runs/BI-01-FO-01/artifacts/worker-BI01-FO01-N-DISPLAY-INTEGRATION-02/'
RECENT_BEFORE = [
 [101470800,101860200,101962800,'2426337100139220247:11186919927598872187'],
 [101860200,102297600,102394800,'10223083031665264409:9881213635706894390'],
 [102297600,102540600,102674400,'13995098069674248561:9958011312367626262'],
 [102540600,102837600,102958800,'5856542428334278608:9904800854582503728'],
 [102837600,102958200,103014000,'4659927943037143813:10369991133646758404'],
 [102958200,103043400,103058400,'1401460604430732245:9492637781681917187'],
]
# Independently read after-confirmation rows, not a generated rolling-window result.
RECENT_AFTER = [
 [101860200,102297600,102394800,'10223083031665264409:9881213635706894390'],
 [102297600,102540600,102674400,'13995098069674248561:9958011312367626262'],
 [102540600,102837600,102958800,'5856542428334278608:9904800854582503728'],
 [102837600,102958200,103014000,'4659927943037143813:10369991133646758404'],
 [102958200,103043400,103058400,'1401460604430732245:9492637781681917187'],
 [103043400,103059000,103151400,'16988890582587490391:12311274632557530968'],
]
PREVIOUS_BEFORE = [
 [100443000,100460400,100545600,'16301823789254921884:12017754914389061991'],
 [100460400,100633800,100723800,'15379319021888293305:11629421669636382479'],
 [100633800,100723200,100811400,'6283473817144739959:9983331986008483729'],
 [100723200,101074800,101136000,'2805277380320709794:11303899842317003906'],
 [101074800,101174400,101283600,'3878258401401849301:9604581699274870834'],
 [101174400,101470800,101586600,'2796108674180270449:9743133159322378602'],
]
PREVIOUS_AFTER = [
 [100460400,100633800,100723800,'15379319021888293305:11629421669636382479'],
 [100633800,100723200,100811400,'6283473817144739959:9983331986008483729'],
 [100723200,101074800,101136000,'2805277380320709794:11303899842317003906'],
 [101074800,101174400,101283600,'3878258401401849301:9604581699274870834'],
 [101174400,101470800,101586600,'2796108674180270449:9743133159322378602'],
 [101470800,101860200,101962800,'2426337100139220247:11186919927598872187'],
]
# K, current/previous completed efficiency, working direction/progress/efficiency/
# counter/duration/waiting/ratio, window, working address, Node revision.
RB = [
 [103058400,.14346657709103125,.1335430475976482,'up',95,.7142857142857143,7,15000,600,1,37912,37913,'2607d3e9-d2b0-4d2d-a458-939c4a3e7255'],
 [103059000,.14346657709103125,.1335430475976482,'up',99,.7226277372262774,7,15600,1200,2,37912,37913,'80bbcb6d-78da-40c3-b443-aadb27c5dfe0'],
 [103150800,.14346657709103125,.1335430475976482,'up',43,.0685805422647528,66,107400,93000,155,37912,37913,'6d4acb13-0d9b-48df-aced-4ec5e83f528a'],
 [103151400,.1514170159139533,.08454319929996491,'down',53,.1075050709939148,40,92400,49200,82,37926,37927,'ef2f74f6-bdfe-4d89-bc78-4114de18e86c'],
 [103315800,.1514170159139533,.08454319929996491,'down',50,.0377643504531722,80,256800,123600,15.846153846153847,37926,37943,'cfd51328-e2cf-4360-8314-20c9238e93fb'],
]
WORKING_LIVES = {
 'before_confirmation':'16988890582587490391:12311274632557530968',
 'at_or_after_confirmation':'12114914724127065318:9836511254728646171',
 'final':'12114914724127065318:9836511254728646171',
}
# UTI, close, Calendar position: all 48 rows actually read; other OHLC columns
# intentionally not reproduced. None is an absent input price, not zero.
I_PRICE = [
 [35339400,571.,58899],[35340000,570.,58900],[35340600,568.5,58901],
 [35341200,570.,58902],[35341800,567.5,58903],[35342400,569.,58904],
 [35343000,571.5,58905],[35343600,570.5,58906],[35344200,572.,58907],
 [35344800,570.,58908],[35345400,570.5,58909],[35346000,564.5,58910],
 [35346600,None,58911],[35347200,None,58912],[35347800,None,58913],
 [35348400,None,58914],[35349000,None,58915],[35349600,None,58916],
 [35350200,None,58917],[35350800,None,58918],[35351400,None,58919],
 [35352000,None,58920],[35352600,None,58921],[35353200,None,58922],
 [35353800,None,58923],[35354400,None,58924],[35355000,None,58925],
 [35355600,None,58926],[35356200,None,58927],[35356800,None,58928],
 [35357400,None,58929],[35358000,None,58930],[35358600,None,58931],
 [35359200,None,58932],[35359800,None,58933],[35360400,None,58934],
 [35361000,572.,58935],[35361600,574.5,58936],[35362200,574.,58937],
 [35362800,575.5,58938],[35363400,575.,58939],[35364000,575.5,58940],
 [35364600,575.,58941],[35365200,574.,58942],[35365800,570.,58943],
 [35366400,571.5,58944],[35367000,567.,58945],[35367600,568.,58946],
]
INPUTS = {
 'qualification':'field excerpts, manually transcribed from actual connector reads; not full formal export',
 'source_root':SOURCE,
 'rb_index':{'path':'data/formal_occurrence_index/rb_temporal_slice.csv','blob':'035841c3ca5607ccb7743c911fdb1e426dec8920','read_lines':[[1,9],[157,163],[433,434]],'rows':RB},
 'recent_before':{'path':'data/selected_cuts/before_confirmation/recent_members.csv','blob':'49a356e2fd4d623b44afc814c99380cae1046a6e','rows':RECENT_BEFORE},
 'recent_after':{'path':'data/selected_cuts/at_or_after_confirmation/recent_members.csv','blob':'297e44797aeb5cb656e1e9bfe76e0aa82290857c','rows':RECENT_AFTER},
 'previous_before':{'path':'data/selected_cuts/before_confirmation/previous_members.csv','blob':'5556fa352a844511dfd4a3b1c187000f14f202c9','rows':PREVIOUS_BEFORE},
 'previous_after':{'path':'data/selected_cuts/at_or_after_confirmation/previous_members.csv','blob':'58425568168a883ad293ba02b665220244b38945','rows':PREVIOUS_AFTER},
 'working_lives':{'paths':['data/selected_cuts/'+cut+'/working_values.csv' for cut in WORKING_LIVES],'values':WORKING_LIVES},
 'metrics':{'before_blob':'2ac6ff4dded36adb2ce9b1d54f077bd2eb40d9c9','after_blob':'7510a4897f2ae640b324f50398e66b7721e8a58b','kind8_before':[.14346657709103125,.1335430475976482,.009923529493383043],'kind8_after':[.1514170159139533,.08454319929996491,.06687381661398838]},
 'rhythm':{'after_path':'data/selected_cuts/at_or_after_confirmation/rhythm.csv','final_path':'data/selected_cuts/final/rhythm.csv','after_current_median':600.,'final_current_median':7800.,'after_last_update':103102200,'final_last_update':103192200},
 'rb_price':{'path':'data/same_bound_price/rb_5m_price_calendar.csv','blob':'88059cf85cafb3d02bcd10eb6100c554cd9db8f6','read_lines':[4514,4517],'K103150800_close':3778.,'K103151400_close':3781.},
 'hc_tail':{'path':'data/formal_occurrence_index/hc_tail_500.csv','blob':'222b3f2e448861612ebe6955c98fe59e66df8568','read_lines':[500,501],'waiting':[257400.,258000.],'waiting_ratio':[429.,430.],'working_efficiency':[.034482758620689655,.031578947368421054],'progress':[49.,45.],'counter':[97.,97.]},
 'i_price':{'path':'data/i_missing_context/i_5m_price_calendar.csv','blob':'16cab994bb8119a94e8b9c27d362f2898c371d4c','rows':I_PRICE},
 'i_N_index':{'path':'data/formal_occurrence_index/i_20170330_1455_to_20170331_0900.csv','blob':'221f6784f9424021e7d81ba66f2096f3747c4957','read_lines':[[1,5],[24,28]],'last_exported_uti':35360400,'last_exported_line':26,'restoration_N_row_present_in_this_export':False,'sampled_gap_duration_present':1,'sampled_gap_progress_present':0,'sampled_gap_efficiency_present':0,'sampled_gap_working_knownness':4},
}


def main():
    checks=[]
    def check(name,actual,expected=True):
        ok = (math.isclose(actual,expected,rel_tol=1e-12,abs_tol=1e-12)
              if isinstance(actual,(int,float)) and isinstance(expected,(int,float))
              and not isinstance(actual,bool) and not isinstance(expected,bool) else actual==expected)
        checks.append({'name':name,'actual':actual,'expected':expected,'passed':bool(ok)})
    before,after,final=RB[2:]
    check('five retained recent members, ordered and same Life',RECENT_BEFORE[1:],RECENT_AFTER[:-1])
    check('previous window also rolls five members',PREVIOUS_BEFORE[1:],PREVIOUS_AFTER[:-1])
    check('outgoing recent member enters previous window',RECENT_BEFORE[0],PREVIOUS_AFTER[-1])
    for name, members, expected in [('recent-before',RECENT_BEFORE,270000.),('previous-before',PREVIOUS_BEFORE,136500.),('recent-after',RECENT_AFTER,181800.),('previous-after',PREVIOUS_AFTER,234900.)]:
        check('duration median '+name,median([r[1]-r[0] for r in members]),expected)
    check('new completed Life is prior working Life',RECENT_AFTER[-1][3],WORKING_LIVES['before_confirmation'])
    check('new member not knowable at preceding K',RECENT_AFTER[-1][2]>before[0])
    check('new member knowable at confirmation K',RECENT_AFTER[-1][2],after[0])
    check('actual end did not itself change completed window',RB[0][10],RB[1][10])
    check('actual-end prefix agrees with prior 27-close reference',RB[1][5],99/137)
    check('same working Life after confirmation and at final',WORKING_LIVES['at_or_after_confirmation'],WORKING_LIVES['final'])
    check('same Life need not have same storage base',after[11]!=final[11])
    delta_current=after[1]-before[1]
    delta_previous=after[2]-before[2]
    delta_contrast=(after[1]-after[2])-(before[1]-before[2])
    check('change in contrast decomposes into current minus previous changes',delta_contrast,delta_current-delta_previous)
    check('newly known down working already has past duration',after[7],after[0]-103059000)
    check('price rose at the interpretation switch',INPUTS['rb_price']['K103151400_close']-INPUTS['rb_price']['K103150800_close'],3.)
    check('after waiting uses actual rhythm denominator',after[8]/600.,after[9])
    check('final waiting uses actual rhythm denominator',final[8]/7800.,final[9])
    check('absolute waiting increases while its ratio falls',final[8]>after[8] and final[9]<after[9])
    check('after waiting starts at formal last update',after[0]-103102200,after[8])
    check('final waiting starts at formal last update',final[0]-103192200,final[8])
    hc=INPUTS['hc_tail']
    check('hc reported waiting and ratio are arithmetically compatible with 600', [w/r for w,r in zip(hc['waiting'],hc['waiting_ratio'])],[600.,600.])
    check('i price excerpt contains 48 actual rows',len(I_PRICE),48)
    missing=[i for i,(_,c,_) in enumerate(I_PRICE) if c is None]
    check('i missing close count',len(missing),24)
    check('i missing prices contiguous in supplied excerpt',missing,list(range(12,36)))
    check('Calendar positions are contiguous despite missing price',all(b[2]-a[2]==1 for a,b in zip(I_PRICE,I_PRICE[1:])))
    check('Clock progresses across all excerpt records',all(b[0]-a[0]==600 for a,b in zip(I_PRICE,I_PRICE[1:])))
    check('i recovery price is an actual record',I_PRICE[36],[35361000,572.,58935])
    check('N export ends before recovery, not evidence of no recovery in product',INPUTS['i_N_index']['last_exported_uti']<I_PRICE[36][0])
    check('display bindings retained',len(configs()),23)
    cfg=display_config(symbol='rb',color='#4C78A8',mode='selected_cut',optional_panels=('duration','rhythm'))
    check('all selected scalar panels compact',all(v['height']==150 for k,v in cfg['panels'].items() if k!='price'))
    check('single-K summary, not fake historical curve',cfg['readability_policy']['scalar_layout']['arrangement'],'compact_grid')
    check('one identity color retained',all(x['plot_binding']['style']['color']=='#4C78A8' for x in cfg['layers']))
    for panel,value in [('working_efficiency',final[5]),('rhythm',final[9]),('working_motion',0.)]:
        low,high=numeric_display_range(panel,[value])
        check('single-value nondegenerate bounds '+panel,low<value<high)
    check('all-null is still absent',numeric_display_range('working_efficiency',[None,float('nan')]),None)
    check('efficiency outlier not clipped',numeric_display_range('working_efficiency',[1.2])[1]>1.2)
    check('waiting 430 is not clipped to probability',numeric_display_range('rhythm',[430.])[1]>430.)
    check('evolution viewport follows formal, not long price context',evolution_display_range([103056600,103315800],[100443000,103315800]),(103056600,103315800))
    ranges={p:numeric_display_range(p,[v]) for p,v in [('working_efficiency',final[5]),('rhythm',final[9]),('working_motion',0.)]}
    images=[]
    for basename in ['BI01FO01_W02_081e312_rb_selected_final.png','BI01FO01_W02_39308f4_rb_evolution.png']:
        p=Path('/mnt/data')/basename
        if p.exists():
            images.append({'attachment':basename,'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'qualification':'actual attachment bytes; not assumed byte-identical to repository original PNG'})
    output={'invocation_id':INVOCATION,'config_version':CONFIG_VERSION,'scope':'Pro local bounded arithmetic, membership/time comparison and pure display-config checks; not fresh OnlyRead, rendering or independent review','inputs':INPUTS,'derived':{'completed_current_change':delta_current,'completed_previous_change':delta_previous,'contrast_change':delta_contrast,'reference_drop_share_of_contrast_change':-delta_previous/delta_contrast,'working_absolute_waiting_growth':final[8]/after[8],'rhythm_denominator_growth':7800/600,'formal_evolution_share_of_old_price_UTI_domain':(103315800-103056600)/(103315800-100443000),'single_value_display_ranges':ranges},'checks':checks,'passed':all(x['passed'] for x in checks),'image_attachments':images,'not_executed':['new normal Feature reads','independent full 433/500-row recalculation','rerun of persisted HTML/CDS audit','v0.2.1 aidata integration','new rendering or rerendering','i recovery-K formal N read','hc rhythm/member original-table read','independent professional review','management acceptance']}
    (ROOT/'CHECK_RESULTS.json').write_text(json.dumps(output,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'passed':output['passed'],'checks':len(checks),'derived':output['derived'],'failures':[x['name'] for x in checks if not x['passed']]},ensure_ascii=False,indent=2))
    if not output['passed']:
        raise SystemExit(1)

if __name__=='__main__':
    main()
