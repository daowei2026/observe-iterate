"""Bounded R0011 reference checks, not a fresh Feature read or chart test.
Run: python verify_r0011.py
The field excerpts below were read from immutable GitHub exports. The 24 hc
close rows are the COMPLETE PREFIX only, not the full 454-row working path.
"""
from __future__ import annotations
import ast
import importlib.util
import json
import math
from pathlib import Path
from statistics import median
from uuid import UUID

ROOT = Path(__file__).resolve().parent
INVOCATION = 'BI01-FO-01-R0011-20261022T145041Z-c822c94f'
W03 = ('daowei2026/observe-iterate@d04f3b08892ccf334a06028f3caab994743566a0:'
       'runs/BI-01-FO-01/artifacts/worker-BI01-FO01-N-READABILITY-CROSSK-03/')
INPUTS = {
 'source_root': W03,
 'qualification': 'Actual connector-read field excerpts; not a replacement formal product.',
 'i': {
  'node_life': '9410abda-b111-442d-aa25-6b99da2afeb6',
  'cuts': [35360400,35361000,35361600],
  'working_life_words': [6280244740041886338,10111421440293504716],
  'same_words_read_from': ['data/crossk/i_before_missing_recovery/working_values.csv',
      'data/crossk/i_recovery/working_values.csv','data/crossk/i_after_recovery/working_values.csv'],
  'working_start':35319000, 'direction_code':1,
  'direct_recovery': {
   'working_progress': {'value':12.0,'present':1,'knownness':0,'blob':'c493d7dfb2358e9733be7587a1b8bf285e49e8cb'},
   'working_waiting': {'value':0.0,'present':1,'knownness':0,'blob':'d4a6acc70ff34b00884c0baa4cda9a6b81d94edf'},
   'working_efficiency': {'value':None,'present':0,'knownness':4,'blob':'349def5de5377e4d446951c748822b58a2f54793'},
   'working_waiting_ratio': {'value':None,'present':0,'knownness':3,'blob':'562c90c41ec49fa2347a06732859ed6064732fc6'},
   'rhythm': {'local_start':35361000,'local_count':0,'last_update':None,'last_update_present':0,
              'current_median':None,'current_median_present':0,'blob':'03326e0be1e73296ad2fe14cf7c1363ac5732620'},
   'overall_knownness':4,'completion_knownness':2,
  },
  'direct_after': {'progress':9.5,'waiting':600.0,'overall_knownness':4,'completion_knownness':2,
       'progress_blob':'a7b0f509c9db7f256014b2f48ec79d18c3176ee0',
       'waiting_blob':'90c46e7cbdcac38f6f0668f638a6b6a43fe9fa1e'},
  'duration_from_worker_summary':[41400.0,42000.0,42600.0],
  'duration_qualification':'Adopted W03 CROSSK_SUMMARY values; not independently fetched duration tables this round.',
  'price_reference': {'source':'W02@081e31241a0c88e47631f80a8b9b8dd43b2b569c:data/i_missing_context/i_5m_price_calendar.csv',
       'qualification':'Reuse of R0009 actual original-price reading, not a new price read.',
       'recovery_close':572.0,'next_close':574.5}
 },
 'hc': {
  'node_life':'6f92034c-bd94-4d3f-8b7c-6c69e24959ff',
  'exact_revision':'76d5cfc3-f505-4b62-89b8-b081aedb90f0',
  'K':103315800,'start':103044000,'direction_code':0,
  'formal_rhythm':{'last_update':103057800,'local_count':14,'full_count':14,'current_median':600.0,
                   'previous_median':600.0,'median_change':0.0,'blob':'3680fdfec9656492e17c615f591af39f26a8feac'},
  'formal_intervals':[600.0,1200.0,600.0,2400.0,600.0,600.0],
  'intervals_blob':'ed4a5c22073c63e0afd815d6370ead56d026f4e4',
  'formal_progress':45.0,'progress_blob':'832f8adfef1d2bf73926945fb1c0d6413208ae7a',
  'waiting_from_worker_summary':258000.0,'ratio_from_worker_summary':430.0,'duration_from_worker_summary':271800.0,
  'price_source':'data/crossk/hc_final/hc_5m_price_calendar.csv',
  'price_blob':'ddd03aea930d08a169e85846e581aa7294e1f7a2',
  'price_read_scope':'request 1..101 truncated after part of prefix; exact 24 rows below fully visible at CSV lines 2..25; tail lines 449..455 fully read',
  'prefix_uti_close':[
   [103044000,3859],[103044600,3861],[103045200,3862],[103045800,3866],
   [103046400,3870],[103047000,3867],[103047600,3868],[103048200,3875],
   [103048800,3875],[103049400,3869],[103050000,3882],[103050600,3880],
   [103051200,3895],[103051800,3902],[103052400,3907],[103053000,3898],
   [103053600,3910],[103054200,3921],[103054800,3919],[103055400,3921],
   [103056000,3921],[103056600,3929],[103057200,3939],[103057800,3952]],
  'tail_uti_close':[[103312200,3905],[103312800,3911],[103313400,3908],
                    [103314000,3901],[103314600,3908],[103315200,3908],[103315800,3904]],
  'qualification':'Strict-new-close-high reference reconstructed only over the complete 24-row prefix; no independent claim over all 454 rows.'
 }
}

def main() -> None:
 checks=[]
 def check(name, actual, expected=True):
  numeric=(isinstance(actual,(float,int)) and not isinstance(actual,bool)
           and isinstance(expected,(float,int)) and not isinstance(expected,bool))
  ok=math.isclose(actual,expected,rel_tol=1e-12,abs_tol=1e-12) if numeric else actual==expected
  checks.append({'name':name,'actual':actual,'expected':expected,'passed':bool(ok)})
 i,h=INPUTS['i'],INPUTS['hc']
 life=str(UUID(int=(i['working_life_words'][0]<<64)|i['working_life_words'][1]))
 check('i exact integer Life decode',life,'5727e951-20b6-4a82-8c52-fc3a32f686cc')
 check('i age arithmetic against adopted duration', [K-i['working_start'] for K in i['cuts']],i['duration_from_worker_summary'])
 check('i local restart is later than working start',i['direct_recovery']['rhythm']['local_start']>i['working_start'])
 check('i waiting zero is present',i['direct_recovery']['working_waiting']['present'],1)
 check('i waiting zero numeric',i['direct_recovery']['working_waiting']['value'],0.0)
 check('i zero does not establish an extremum update',i['direct_recovery']['rhythm']['last_update_present'],0)
 check('i zero is not zero ratio',i['direct_recovery']['working_waiting_ratio']['present'],0)
 check('i path efficiency remains absent',i['direct_recovery']['working_efficiency']['present'],0)
 check('i ratio and efficiency preserve distinct original knownness',
       i['direct_recovery']['working_waiting_ratio']['knownness']!=i['direct_recovery']['working_efficiency']['knownness'])
 check('i next local waiting uses local restart',i['cuts'][2]-i['direct_recovery']['rhythm']['local_start'],i['direct_after']['waiting'])
 price=i['price_reference']
 check('i next progress change agrees with down-signed endpoint change',
       i['direct_after']['progress']-i['direct_recovery']['working_progress']['value'],
       -(price['next_close']-price['recovery_close']))
 inferred=[price['recovery_close']+12,price['next_close']+9.5]
 check('i inferred starting price consistency ONLY, not an independent start-price check',inferred[0],inferred[1])
 updates=[]; peak=h['prefix_uti_close'][0][1]
 for t,p in h['prefix_uti_close'][1:]:
  if p>peak: updates.append(t);peak=p
 intervals=[b-a for a,b in zip(updates,updates[1:])]
 check('hc prefix source row count',len(h['prefix_uti_close']),24)
 check('hc prefix strict-high count agrees with formal full_count',len(updates),h['formal_rhythm']['full_count'])
 check('hc prefix final record-high UTI agrees with formal last_update',updates[-1],h['formal_rhythm']['last_update'])
 check('hc last six reference intervals agree individually',intervals[-6:],h['formal_intervals'])
 check('hc actual last-three median agrees with original rhythm',median(h['formal_intervals'][-3:]),h['formal_rhythm']['current_median'])
 check('hc equal close is not counted as new strict high',103048800 not in updates)
 waiting=h['K']-h['formal_rhythm']['last_update'];age=h['K']-h['start']
 check('hc waiting arithmetic against adopted scalar',waiting,h['waiting_from_worker_summary'])
 check('hc ratio arithmetic against adopted scalar',waiting/h['formal_rhythm']['current_median'],h['ratio_from_worker_summary'])
 check('hc age arithmetic against adopted scalar',age,h['duration_from_worker_summary'])
 check('hc final endpoint progress versus direct formal field',h['tail_uti_close'][-1][1]-h['prefix_uti_close'][0][1],h['formal_progress'])
 check('hc late prices not motionless',len(set(p for _,p in h['tail_uti_close']))>1)
 env={}
 for m in ('mquant','mquant.uplot','mquant.aidata','mquant.tis','ipywidgets','nbformat','nbclient'):
  try:
   s=importlib.util.find_spec(m);env[m]={'available':s is not None,'origin':s.origin if s else None}
  except ModuleNotFoundError as e:env[m]={'available':False,'error':str(e)}
 nb_file=ROOT/'N_observation_R0011.ipynb'
 if nb_file.exists():
  import nbformat
  nb=nbformat.read(nb_file,as_version=4);nbformat.validate(nb)
  for n,c in enumerate(nb.cells):
   if c.cell_type=='code':ast.parse(c.source,filename=f'notebook-cell-{n}')
  check('Notebook schema and code syntax valid (NOT execution)',True)
  code='\n'.join(c.source for c in nb.cells if c.cell_type=='code')
  check('Notebook does not load old HTML or PNG', all(x not in code for x in ('IFrame(','.png','write_html(', 'load_reused_evolution')))
  check('Notebook calls normal new Uplot layout', 'build_uplot_layout(' in code and 'show(' in code)
  check('sparse known cuts never fabricate holds','_hold' in code and '_steps' in code and '.iloc[0:0]' in code)
  errors=[{'cell':n,'ename':o.ename,'evalue':o.evalue} for n,c in enumerate(nb.cells) if c.cell_type=='code'
          for o in c.get('outputs',[]) if o.output_type=='error']
  nbstatus={'executed_cells':sum(c.get('execution_count') is not None for c in nb.cells if c.cell_type=='code'),
            'errors':errors,'qualification':'Only a local execution attempt; graph and widget cells not executed.'}
 else:nbstatus={'qualification':'Notebook file not created yet'}
 result={'invocation_id':INVOCATION,'scope':'Pro bounded reference arithmetic + syntax/structure checks; not platform/runtime verification',
   'inputs':INPUTS,'derived':{'hc_prefix_new_high_utis':updates,'hc_prefix_path_reference':sum(abs(b[1]-a[1]) for a,b in zip(h['prefix_uti_close'],h['prefix_uti_close'][1:])),
    'hc_since_last_high_share_of_current_age':waiting/age,'hc_current_distance_below_prefix_last_high':peak-h['tail_uti_close'][-1][1],
    'i_inferred_start_price_NOT_independently_read':inferred},'checks':checks,'passed':all(c['passed'] for c in checks),
   'environment':env,'notebook_attempt':nbstatus,
   'not_executed':['New Uplot graph rendering','Jupyter/Bokeh interaction','Pro new-graph visual judgement','Three aidata platform API calls',
     'Open report_url','Board same-node formal delivery','Independent full hc 454-row recomputation','Fresh formal N computation or OnlyRead','Independent review/management acceptance']}
 (ROOT/'CHECK_RESULTS.json').write_text(json.dumps(result,ensure_ascii=False,indent=2,allow_nan=False)+'\n',encoding='utf-8')
 print(json.dumps({'passed':result['passed'],'checks':len(checks),'derived':result['derived'],'notebook_attempt':nbstatus},ensure_ascii=False,indent=2))
 if not result['passed']:raise SystemExit(1)

if __name__=='__main__':main()
