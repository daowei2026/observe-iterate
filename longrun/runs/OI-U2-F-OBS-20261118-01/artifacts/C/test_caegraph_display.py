from __future__ import annotations
import importlib.util
import sys
from pathlib import Path
import pandas as pd

MODULE = Path('/mnt/data/caegraph_display.py')
spec = importlib.util.spec_from_file_location('caegraph_display', MODULE)
mod = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = mod
spec.loader.exec_module(mod)


def idx3(rows):
    return pd.MultiIndex.from_tuples(rows, names=['ts','record_id','child2'])

def idx4(rows):
    return pd.MultiIndex.from_tuples(rows, names=['ts','record_id','child2','child3'])

def idx5(rows):
    return pd.MultiIndex.from_tuples(rows, names=['ts','record_id','child2','child3','child4'])

occ = pd.DataFrame({
    'groupReference_referenceLife_idText':['L-A','L-A'],
    'groupReference_referenceRevision_idText':['R-1','R-2'],
    'groupKnownFrom':[100,130],
    'groupLocalBasis_name':['Incomplete','Supported'],
    'groupAlternative_name':['Unambiguous','Unambiguous'],
    'groupObservation_name':['Open','ClosedSupported'],
    'groupCoverageIncomplete':[1,0],
    'groupClosed':[0,1],
    'groupOriginalAnchor':[10.,10.],
    'groupOriginalDeadline':[20.,20.],
    'groupOriginalRevisionEnd':[30.,30.],
    'groupAnchor':[11.,11.],
    'groupDeadline':[19.,19.],
    'groupRevisionEnd':[29.,29.],
}, index=idx3([(100,0,0),(130,0,0)]))

members = pd.DataFrame({
    'memberObject':['rb','hc','rb','hc','i'],
    'memberTurn_referenceLife_idText':['T-rb','T-hc','T-rb','T-hc','T-i'],
    'memberTurn_referenceRevision_idText':['1','1','1','1','1'],
    'memberSource_referenceLife_idText':['S-rb','S-hc','S-rb','S-hc','S-i'],
    'memberSource_referenceRevision_idText':['1','1','1','1','1'],
    'memberActual':[80,82,80,82,84],
    'memberPrice':[4500.,4800.,4500.,4800.,1000.],
    'memberConfirmation':[90,92,90,92,94],
    'memberKnownFrom':[100,100,130,130,130],
    'memberDirection_name':['DirectionUp']*5,
    'memberType_name':['SourceTroughTurn']*5,
    'memberRound_name':['FirstRound','FirstRound','FirstRound','FirstRound','SecondRound'],
    'memberStatus_name':['CandidateMember','CandidateMember','ConfirmedMember','ConfirmedMember','ConfirmedMember'],
    'memberRetracted':[0]*5,
}, index=idx4([(100,0,0,0),(100,0,0,1),(130,0,0,0),(130,0,0,1),(130,0,0,2)]))

previous = pd.DataFrame({
    'referenceLife_idText':['L-A'],
    'referenceRevision_idText':['R-1'],
}, index=idx4([(130,0,0,0)]))

overlaps = pd.DataFrame({'idText':['L-X']}, index=idx4([(130,0,0,0)]))
covered = pd.DataFrame({'idText':['L-Y']}, index=idx4([(130,0,0,0)]))

req_rows=[]
req_index=[]
for ts, rev_i, pairs in [(100,0,[('T-rb','T-hc')]), (130,0,[('T-rb','T-hc'),('T-rb','T-i'),('T-hc','T-i')])]:
    for child,(left,right) in enumerate(pairs):
        req_index.append((ts,0,0,child))
        veto = 'CoordinateVeto' if ts==100 else 'CoordinateSupports'
        req_rows.append({
            'pairLeft_referenceLife_idText':left,
            'pairLeft_referenceRevision_idText':'1',
            'pairRight_referenceLife_idText':right,
            'pairRight_referenceRevision_idText':'1',
            'pairTime_requiredVerdict_name':veto,
            'pairTime_requiredGap_name':'NoGap',
            'pairTime_requiredVeto_name':'ActualDistanceExceeded' if ts==100 else 'NoVeto',
            'pairDirection_requiredVerdict_name':'CoordinateSupports',
            'pairDirection_requiredGap_name':'NoGap',
            'pairDirection_requiredVeto_name':'NoVeto',
            'pairType_requiredVerdict_name':'CoordinateSupports',
            'pairType_requiredGap_name':'NoGap',
            'pairType_requiredVeto_name':'NoVeto',
            'pairBend_requiredVerdict_name':'CoordinateUnresolved' if ts==100 else 'CoordinateSupports',
            'pairBend_requiredGap_name':'SelectedAnchorUnavailable' if ts==100 else 'NoGap',
            'pairBend_requiredVeto_name':'NoVeto',
        })
required = pd.DataFrame(req_rows, index=idx4(req_index))
distance = pd.DataFrame({'distanceValue':[5.,4.,6.,3.]}, index=idx5([(*i,0) for i in req_index]))

class FakeFeature:
    def __init__(self):
        self.tables = {
            'occurrences':occ,
            'occurrences_groupMembers':members,
            'occurrences_groupPrevious':previous,
            'occurrences_groupRequired':required,
            'occurrences_groupRequired_pairDistance':distance,
            'occurrences_groupOverlaps':overlaps,
            'occurrences_groupCoveredBy':covered,
        }
    def to_dfs(self, names):
        return {name:self.tables[name] for name in names}

out = mod.prepare_display_tables(FakeFeature())
assert list(out.revisions['candidate_revision']) == ['R-1','R-2']
assert out.revision_links.shape[0] == 1
assert out.revisions.loc[out.revisions.candidate_revision=='R-2','overlaps'].iloc[0] == 'L-X'
assert out.revisions.loc[out.revisions.candidate_revision=='R-2','covered_by'].iloc[0] == 'L-Y'
assert out.members.shape[0] == 5
assert set(out.members.symbol) == {'rb','hc','i'}
assert out.required_summary.shape[0] == 8
first_time = out.required_summary[(out.required_summary.candidate_revision=='R-1') & (out.required_summary.coordinate=='Time')].iloc[0]
assert first_time.verdict == 'CoordinateVeto'
assert 'distance=5' in first_time.details
assert any('groupFormationParticipation' in w for w in out.data_warnings)
print('prepare_display_tables fixture: OK')
print('revisions', out.revisions.shape, 'members', out.members.shape, 'required', out.required_summary.shape)
