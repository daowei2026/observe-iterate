"""DIAGNOSTIC_ONLY：只读已有输入/输出，重放覆盖方程，不运行正式Feature。"""
from pathlib import Path
from hashlib import sha256
from collections import Counter
from datetime import datetime,timezone
import ast,csv,json,math,subprocess,uuid

ROOT=Path(__file__).resolve().parent
PREV=ROOT.parent/'D002'
FRP=Path('/dwdhome/fy/BASE_E6_2_copy/.runtime/f-observation-multiple-github-20261122/frp')
RUNTIME=Path('/dwdhome/fy/BASE_E6_2_copy/.runtime/f-wide-observation-20261122/runtime/edh-universe/frp/frp')
PIN='ac1927518ad6105f15ffbe37fea45e4be91ba574'
def load(path):return json.loads(path.read_text())
def read(path):
    with path.open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))
def write(name,value):(ROOT/name).write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n')
def csvwrite(name,rows):
    with (ROOT/name).open('w',encoding='utf-8-sig',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(dict.fromkeys(k for r in rows for k in r)));w.writeheader();w.writerows(rows)
def n(x):return int(float(x))
def ident(r,p):
    return r[p+'_idText'] if n(r[p+'_idForm'])==2 else str(uuid.UUID(int=(int(r[p+'_idHigh'])<<64)|int(r[p+'_idLow'])))

cfg=load(PREV/'configuration.json');binding=load(PREV/'FeatureRunResultBinding.json')
assert sha256((PREV/'configuration.json').read_bytes()).hexdigest()==binding['parameter_version']
sources=[]
for suffix in ['CommonPriceTurnGroupCandidates.hs','U2/GroupCandidateKLineInput.hs','U2/GroupCandidateMaterial.hs','U2/GroupCandidateTypes.hs','U2/GroupCandidateEvolution.hs','U2/GroupCandidateStorage.hs']:
    path='src/Frp/Instance/ISL/Opportunity/'+suffix
    blob=subprocess.check_output(['git','show',PIN+':'+path],cwd=FRP)
    assert (FRP/path).read_bytes()==(RUNTIME/path).read_bytes()==blob
    sources.append(dict(ref='daowei2026/frp@'+PIN+':'+path,sha256=sha256(blob).hexdigest(),runtime_match=True))
adapter=(FRP/'src/Frp/Instance/ISL/Opportunity/U2/GroupCandidateKLineInput.hs').read_text()
assert 'round u,u/step,marketUnitsPerCalendarTick market*u' in adapter
assert 'position-p==1->old;_->u' in adapter
assert 'geometry (Just (clock turnKnown actual)) False Nothing' in adapter
assert 'FormationFrame u known (firstTurns++secondTurns) [] False coverage' in adapter
write('CODE_AUDIT.json',dict(sources=sources,condition='position-p==1',position='raw closeUti / frequency step',
    frame_patches_empty=True,selected_clock_always_just=True,formal_source_changed=False))
metadata=load(PREV/'UPSTREAM_EXTRACTION.json')
data={s:read(PREV/'upstream'/f'{s}_kline.csv') for s in ['rb','hc','i']}
for s,rs in data.items():
    meta=next(f for f in metadata['features'] if f['symbol']==s and f['kind']=='kline')['tables'][0]
    assert meta['sha256']==sha256((PREV/'upstream'/f'{s}_kline.csv').read_bytes()).hexdigest()
    assert len(rs)==49683
step=5*cfg['sources'][0]['market']['units_per_open_minute'];assert step==600
W=cfg['profile']['delta']*cfg['profile']['observation_multiple'];assert W==480000

traces={};breaks=[];restorations=[];controls=[]
for s,rs in data.items():
    previous=None;start=None;exact_start=None;old_incomplete=None;trace={}
    for row in rs:
        u=n(row['closeUti']);pos=u/float(step)
        contiguous=previous is not None and pos-previous['position']==1
        exact_contiguous=previous is not None and u-previous['u']==step
        segment_from=previous['u'] if contiguous else u
        start=min(start,segment_from) if start is not None and segment_from<=previous['u'] else segment_from
        exact_segment=previous['u'] if exact_contiguous else u
        exact_start=min(exact_start,exact_segment) if exact_start is not None and exact_segment<=previous['u'] else exact_segment
        incomplete=start>u-W
        if previous and exact_contiguous and not contiguous:
            breaks.append(dict(symbol=s,timestamp=row['timestamp'],previous_uti=previous['u'],uti=u,integer_delta=u-previous['u'],
                previous_position=previous['position'],position=pos,position_delta=pos-previous['position'],
                previous_position_hex=previous['position'].hex(),position_hex=pos.hex(),position_delta_hex=(pos-previous['position']).hex(),
                native_segment_from=segment_from,previous_accumulated_start=previous['start'],new_accumulated_start=start,
                needed_from=u-W,source_guard_pass=False,integer_diagnostic_guard_pass=True))
        if old_incomplete is True and incomplete is False:restorations.append(dict(symbol=s,timestamp=row['timestamp'],uti=u,start=start))
        trace[u]=dict(timestamp=row['timestamp'],u=u,native_derived_start=start,native_derived_flag=int(incomplete),
            integer_diagnostic_start=exact_start,integer_diagnostic_flag=int(exact_start>u-W),position=pos)
        previous=dict(u=u,position=pos,start=start);old_incomplete=incomplete
    traces[s]=trace
assert len(breaks)==3 and len({r['uti'] for r in breaks})==1
csvwrite('SOURCE_FALSE_BREAKS.csv',breaks)
csvwrite('COVERAGE_RESTORATIONS.csv',restorations)

outputs=read(PREV/'readback/tables/occurrences.csv');comparisons=[];differences=[]
for r in outputs:
    u=n(r['groupKnownFrom']);replayed=max(traces[s][u]['native_derived_flag'] for s in data)
    diagnostic=max(traces[s][u]['integer_diagnostic_flag'] for s in data)
    item=dict(life=ident(r,'groupReference_referenceLife'),revision=ident(r,'groupReference_referenceRevision'),timestamp=r['timestamp'],
        known_uti=u,occurrence=r['occurrence'],record_id=r['record_id'],child_id_2=r['child_id_2'],
        published_flag=n(r['groupCoverageIncomplete']),native_derived_flag=replayed,integer_diagnostic_flag=diagnostic,
        native_derived_start=traces['rb'][u]['native_derived_start'],integer_diagnostic_start=traces['rb'][u]['integer_diagnostic_start'],
        required_from=u-W)
    comparisons.append(item)
    if item['published_flag']!=replayed:differences.append(item)
assert not differences, differences[:2]
changed=[r for r in comparisons if r['published_flag']!=r['integer_diagnostic_flag']]
old=read(PREV/'profile/violations_coverage_flag_vs_continuous_input.csv')
assert {(x['life'],x['revision']) for x in old}=={(x['life'],x['revision']) for x in changed}
assert len(changed)==22 and len({r['life'] for r in changed})==12
csvwrite('PUBLISHED_FLAG_RECONCILIATION.csv',comparisons)
csvwrite('DIAGNOSTIC_COUNTERFACTUAL_AT_PUBLISHED_LOCATIONS.csv',changed)

cut=breaks[0]['uti'];axis=traces['rb'];keys=sorted(axis)
for u in [keys[0],cut-step,cut,cut+step,cut+W-step,cut+W]:
    if u in axis:controls.append(dict(symbol='rb',**axis[u]))
csvwrite('BOUNDARY_CONTROLS.csv',controls)
summary=dict(diagnostic_only=True,formal_feature_run=False,source_behavior_changed=False,original_binding_unchanged=True,
    input_positions_per_symbol=49683,input_symbols=list(data),frequency_step=step,observation_W=W,
    false_breaks_per_symbol={s:sum(r['symbol']==s for r in breaks) for s in data},false_break_time=breaks[0]['timestamp'],
    false_break_uti=cut,integer_delta=600,position_delta=breaks[0]['position_delta'],
    coverage_restarts_at=cut,restorations=restorations,
    published_occurrences_checked=len(comparisons),published_flag_matches=len(comparisons)-len(differences),published_flag_mismatches=len(differences),
    diagnostic_changed_occurrences=len(changed),diagnostic_changed_lives=len({r['life'] for r in changed}),
    diagnostic_changed_ticks=len({r['timestamp'] for r in changed}),cold_start_flags_preserved=sum(r['integer_diagnostic_flag'] for r in comparisons),
    no_formal_new_result='反事实仅重放覆盖方程及对齐已有公开位置；未运行完整候选演化，不能作为新正式输出或断言未来总组数/观点数',
    native_trace_limit='native_derived为根据锁定源方程、同实例真实输入的隔离重放；不是未暴露的原生内部trace',
    completed_at=datetime.now(timezone.utc).isoformat())
write('EXPERIMENT_RESULTS.json',summary)
print(json.dumps(summary,ensure_ascii=False,indent=2))
