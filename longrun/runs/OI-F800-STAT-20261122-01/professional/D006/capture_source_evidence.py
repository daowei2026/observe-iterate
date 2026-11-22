"""窄范围保存本finding相关源码/参数消费点及精确内容指纹。"""
from pathlib import Path
from hashlib import sha256
from datetime import datetime,timezone
import json,subprocess

ROOT=Path(__file__).resolve().parent
BASE=ROOT.parents[2]
RUNTIME=BASE/'.runtime/f800-exact-uti-20261122/runtime'
FRP=BASE/'.runtime/f-observation-multiple-github-20261122/frp'
CORE=RUNTIME/'edh-universe/frp/frp-core'
selections=[
 ('normal_kline_adapter',FRP,'src/Frp/Instance/ISL/Opportunity/U2/GroupCandidateKLineInput.hs',[(39,87),(127,153)]),
 ('material_coverage',FRP,'src/Frp/Instance/ISL/Opportunity/U2/GroupCandidateMaterial.hs',[(46,104),(126,141)]),
 ('coverage_types',FRP,'src/Frp/Instance/ISL/Opportunity/U2/GroupCandidateTypes.hs',[(18,26),(103,119)]),
 ('actual_entry',FRP,'src/Frp/Instance/ISL/Opportunity/CommonPriceTurnGroupCandidates.hs',[(175,201)]),
 ('candidate_propagation',FRP,'src/Frp/Instance/ISL/Opportunity/U2/GroupCandidateEvolution.hs',[(97,103),(127,143)]),
 ('output_encoding',FRP,'src/Frp/Instance/ISL/Opportunity/U2/GroupCandidateStorage.hs',[(48,86)]),
 ('downstream_reader',FRP,'src/Frp/Instance/ISL/Opportunity/U2/GroupValidityInputs.hs',[(20,35),(109,119)]),
 ('pair_consumer',FRP,'src/Frp/Instance/ISL/Opportunity/U2/GroupCandidatePairs.hs',[(26,49)]),
 ('revision_handoff',FRP,'src/Frp/Instance/ISL/Opportunity/U2/GroupCandidateDecisions.hs',[(35,56)]),
 ('native_pnv_loader',CORE,'src/Frp/Core/Fao/Tis.hs',[(27,68),(111,188)]),
 ('native_event_schedule',CORE,'src/Frp/Core/Engine/Class.hs',[(658,737),(865,881)]),
 ('native_event_push',CORE,'src/Frp/Core/Engine/Host.hs',[(304,347)]),
 ('native_mmap',CORE,'src/Frp/DbaStore/Class.hs',[(65,80)]),
 ('python_pnv_loader',RUNTIME,'mquant/frame/core/data.py',[(24,115)]),
 ('python_dba_read',RUNTIME,'mquant/frame/core/store.py',[(768,784)]),
 ('binary_layout',RUNTIME,'pydim/dim/rt.py',[(39,94),(107,127)]),
]
out=[]
for role,root,name,ranges in selections:
    p=root/name;b=p.read_bytes();lines=b.decode().splitlines()
    out.append(dict(role=role,path=str(p),sha256=sha256(b).hexdigest(),
        version=('daowei2026/frp@be57d6752c9d43d10f1d670e1d2993bb8153ea7c' if root==FRP else 'D005 actual frozen runtime; local file SHA-256'),
        excerpts=[dict(start=a,end=min(z,len(lines)),lines=[dict(line=j,text=lines[j-1]) for j in range(a,min(z,len(lines))+1)]) for a,z in ranges]))
config=json.loads((ROOT.parent/'D005/configuration.json').read_text())
package=(ROOT/'native-package-binding.txt').read_text()
pkgdir=Path(next(x.split(': ',1)[1] for x in package.splitlines() if x.startswith('import-dirs:')))
interfaces=[]
for stem in ['GroupCandidateKLineInput','GroupCandidateMaterial','GroupCandidateTypes']:
    p=pkgdir/'Frp/Instance/ISL/Opportunity/U2'/(stem+'.hi')
    interfaces.append(dict(path=str(p),bytes=p.stat().st_size,sha256=sha256(p.read_bytes()).hexdigest()))
status=subprocess.check_output(['git','status','--porcelain'],cwd=FRP,text=True)
head=subprocess.check_output(['git','rev-parse','HEAD'],cwd=FRP,text=True).strip()
assert status=='' and head=='be57d6752c9d43d10f1d670e1d2993bb8153ea7c'
evidence=dict(checked_at=datetime.now(timezone.utc).isoformat(),finding_id='F800-GF-002',source_files=out,
    frp_head=head,frp_clean=True,package=package,interfaces=interfaces,
    actual_configuration=dict(domain=config['domain'],profile=config['profile'],sources=[dict(input_symbol=s['input']['symbol'],calendar=s['input']['calendar'],frequency=s['input']['freq'],market=s['market']) for s in config['sources']]),
    native_library_binding='同D004构建并用于D005的当前runtime安装包；本C仅stack exec runghc调用上述暴露函数，不build、不启动Feature。',
    native_ts_sha256=sha256((RUNTIME/'edh-universe/bin/ts').read_bytes()).hexdigest(),
    calendar_exemption_check='当前固定域complete=true、coverage=[]；实际GroupKLineConfiguration分支无CoverageInapplicable输入或基于close缺失的豁免分支。Calendar UTI在69位置真实存在；不从零量推导不适用。')
(ROOT/'SOURCE_EVIDENCE.json').write_text(json.dumps(evidence,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(source_files=len(out),interface_files=len(interfaces),frp_head=head,frp_clean=True,native_ts_sha256=evidence['native_ts_sha256']),ensure_ascii=False))
