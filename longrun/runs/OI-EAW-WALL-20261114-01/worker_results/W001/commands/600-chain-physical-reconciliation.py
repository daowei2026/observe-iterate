import pathlib,sys,json,datetime,math
W=pathlib.Path(__file__).resolve().parents[1];sys.path.insert(0,str(W));from bounded_dba_reader import BudgetReader
records=[json.loads(x) for x in (W/'SAMPLE_CHAIN.jsonl').read_text().splitlines()];leaf=pathlib.Path(records[0]['source_partition']);r=BudgetReader(byte_limit=1024*1024,seconds=12,file_limit=20);checks=[]
for ev,record in [('wall_occurrences','P1WallOccurrenceStorage'),('wall_current_view','P1WallCurrentStorage'),('wall_diagnostics','P1DiagnosticStorage')]:
 refs=r.array(leaf/ev/('mul::['+record+'].dba'));ok=refs==list(range(len(refs)));assert ok;checks.append({'event':ev,'root_list_reference_rows':len(refs),'root_list_indices_are_exact_sequential':ok,'meaning':'verifies physical list anchor row and writer firing row alignment for this short-window leaf'})
for x in records:
 p=x['occurrence_payload'];uti=p['p1WallLifecycleOccurredAt'];local=p['p1WallOccurrenceLocalNo'];s=x['upstream_sparse_rows'];z=x['upstream_packed_rows'];assert len(s)==len(z)==1
 assert s[0]['payload']['uti']==z[0]['payload']['uti']==uti and s[0]['payload']['wall_id']==z[0]['payload']['wall_id']==local
 assert x['upstream_state_trace']['payload']['uti']==uti
 assert all(v['p1WallCurrentLocalNo']==local for v in x['current_updates_at_same_firing'])
 assert all(v['writer_trigger_epoch_ns']==x['writer_trigger_epoch_ns'] for v in x['current_updates_at_same_firing'])
 assert p['p1WallOccurrenceRef'].startswith(x['identity']['upstream_artifact_location']+':')
 assert s[0]['payload']['ts']==z[0]['payload']['ts']==x['writer_trigger_epoch_ns']
 band_eq={col:p[dst]==s[0]['payload'][col] for col,dst in [('band_lo','p1WallBandLow'),('band_hi','p1WallBandHigh'),('core_price','p1WallCore')]}
 checks.append({'sample_value_row':x['physical_value_row'],'uti':uti,'source_path_identity_uti_and_trigger_time_match':True,'source_and_product_numeric_values_equal':band_eq,'stored_change':p['p1WallLifecycleChangeKind'],'diagnostics_same_firing_count':x['diagnostics_at_same_firing']['count']})
summary=r.summary();r.close();assert all(v['unchanged_size_and_mtime'] for v in summary['files']);v={'checked_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'checks':checks,'read_budget':summary,'business_acceptance':None,'business_acceptance_reason':'physical reconciliation only; E1 decides professional use'}
(W/'evidence/CHAIN_RECONCILIATION_VALIDATION.json').write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n');print(json.dumps({'checks':checks,'bytes_read':summary['bytes_read']},ensure_ascii=False,indent=2))
