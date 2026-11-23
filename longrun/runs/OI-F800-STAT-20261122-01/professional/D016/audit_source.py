from common import *
b=json.loads((D008/'FRP_SOURCE_BINDING.json').read_text());source=Path(b['source_root']);runtime=Path(b['runtime'])/'edh-universe/frp/frp'
assert subprocess.check_output(['git','rev-parse','HEAD'],cwd=source).decode().strip()==FRP
names=['CommonPriceTurnGroupCandidates.hs']+['U2/'+x+'.hs' for x in ['GroupCandidateTypes','GroupCandidateMaterial','GroupCandidatePairs','GroupCandidateEvolution','GroupCandidateDecisions','GroupCandidateKLineInput','GroupCandidateStorage','FormationParticipationFacts']]
out=[]
for name in names:
 path='src/Frp/Instance/ISL/Opportunity/'+name
 raw=subprocess.check_output(['git','show',FRP+':'+path],cwd=source)
 assert raw==(source/path).read_bytes()==(runtime/path).read_bytes()
 dest=ROOT/'source/frp'/path;dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(raw)
 out.append(dict(source_ref='daowei2026/frp@'+FRP+':'+path,sha256=sha(raw),bytes=len(raw),lines=len(raw.splitlines()),local_copy=str(dest),source_and_loaded_runtime_match=True))
save('CURRENT_SOURCE_AUDIT.json',dict(frp_commit=FRP,checked_at=now(),source_root=str(source),loaded_runtime_source_root=str(runtime),binding_ref=pro_ref('FRP_SOURCE_BINDING.json'),files=out))
print(json.dumps(dict(exact_current_source_files=len(out),runtime_matches=True)))
