"""独立进程通过原生Life/AsOf reader核原GF00122+8控制及GF0028观点，不运行生产。"""
from pathlib import Path
from datetime import datetime, timezone
import csv
import json
import os
import sys
import uuid
sys.path.insert(0,str(Path(__file__).resolve().parent))
from run_formal import ROOT, SOF, setup, construct, write

def main():
    from mquant.frame import CurrSof, CurrCalendar, CalType
    cases=[]
    for source in ['comparison_ac/coverage_retest.csv','comparison/gf002_retest.csv']:
        with (ROOT/source).open(encoding='utf-8-sig',newline='') as f: cases.extend(csv.DictReader(f))
    results=[]
    setup()
    with CurrSof(**SOF), CurrCalendar('night_end_at_2300'):
        feature,_,_,_=construct()
        feature.run(CalType.OnlyRead)
        reader=feature.read_session()
        for case in cases:
            reader.choose(life=case['new_life'],as_of=int(case['known']))
            frame=reader.to_dfs(['occurrences'])['occurrences']
            assert len(frame)==1
            row=frame.iloc[0]
            rev=str(uuid.UUID(int=(int(row['groupReference_referenceRevision_idHigh'])<<64)|int(row['groupReference_referenceRevision_idLow'])))
            flag=int(row['groupCoverageIncomplete'])
            passed=(flag==int(case['expected_flag']) and rev==case['new_native_revision'] and int(row['groupKnownFrom'])<=int(case['known']))
            results.append(dict(retest_kind=case['retest_kind'],as_of=int(case['known']),life=case['new_life'],
                native_revision=rev,native_known_from=int(row['groupKnownFrom']),native_flag=flag,expected_flag=int(case['expected_flag']),
                csv_comparison_revision=case['new_native_revision'],passed=passed))
            print('NATIVE_ASOF_RETEST '+json.dumps(results[-1],ensure_ascii=False),flush=True)
    audit=dict(completed=all(r['passed'] for r in results),pid=os.getpid(),producer_executed=False,
        only_read=True,finished_at=datetime.now(timezone.utc).isoformat(),binding='FeatureRunResultBinding.json',
        reader='TIS@2f460d663d821cf2ba25555eda13e78b697d0767 GroupCandidateReadSession.choose Life/AsOf + to_dfs',
        total=len(results),passed=sum(r['passed'] for r in results),results=results)
    write(ROOT/'NATIVE_RETEST_API.json',audit)
    assert audit['completed']
    print('NATIVE_RETEST_PASSED',len(results))

if __name__=='__main__': main()
