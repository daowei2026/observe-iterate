import pathlib,json
B=pathlib.Path('/dwdhome/fy/BASE_E6_2');W=pathlib.Path(__file__).resolve().parents[1]
for rel,lo,hi in [('mquant/frame/lang/frp/base.py',1,175),('mquant/tis/test/integration/fixtures/eaw_p1_real_run.example.json',1,200)]:
 p=B/rel;print('FILE',p,'BYTES',p.stat().st_size)
 for n,line in enumerate(p.read_text().splitlines(),1):
  if lo<=n<=hi:print(f'{n}: {line}')
for x in [json.loads(line) for line in (W/'SAMPLE_CHAIN.jsonl').open()]:
 print('SAMPLE_VERIFIED',x['physical_value_row'],x['occurrence_payload']['p1WallLifecycleChangeKind'],x['writer_trigger_epoch_iso_z'],'UPSTREAM',len(x['upstream_sparse_rows']),len(x['upstream_packed_rows']),'NONFINITE',x.get('nonfinite_stored_values'))
