"""冻结可交接文本包和SHA256；不包含活跃状态、缓存、inbox和未来Return。"""
import json
from support import OUT,lease,sha,write_json,now

proof=lease()
names=['FACT_REPORT.md','FACTS.json','BINDING.json','BINDING.attempt1.json','BINDING.attempt2.json','BINDING.attempt3.json','BINDING.attempt4.json',
    'environment.json','SOURCES_INITIAL.json','METADATA_ENRICHMENT.json','RECONCILIATION.json','DELIVERY_VALIDATION.json',
    'INPUT_VERIFICATION.json','LEASE_INITIAL.json','PREFLIGHT_LOG.md','READ_MODE.md','SCHEMA_EXCERPTS.md','launcher.diff',
    'support.py','command.py','environment_probe.py','bind_metadata.py','source_inventory.py','read_existing.py',
    'enrich_metadata.py','reconcile.py','build_report.py','validate_delivery.py','freeze_delivery.py','PLAN.json','COMMANDS.jsonl']
names += [str(p.relative_to(OUT)) for p in sorted((OUT/'samples').glob('*.json'))]
names += [str(p.relative_to(OUT)) for p in sorted((OUT/'diffs').glob('*.diff'))]
names += ['logs/'+x+'.log' for x in ('binding','binding-devnull-adapter','binding-w001-tempdir','binding-keyword-api','binding-direct-sof',
    'readonly-readback','readonly-proof-2','readonly-proof-4','readonly-proof-6','readonly-proof-5.text',
    'class-loader-proof','diagnostic-shape-proof','storage-shape-proof','schema-namespace-proof',
    'binary-runtime-resolve','build-and-namespace-metadata','reconciliation','delivery-validation')]
names=sorted(set(names))
for name in names:
    (OUT/name).read_text()  # 强制所有待发布材料可按UTF-8回读。
manifest={name:dict(sha256=sha(OUT/name),bytes=(OUT/name).stat().st_size) for name in names}
(OUT/'SHA256SUMS.txt').write_text(''.join(v['sha256']+'  '+name+'\n' for name,v in manifest.items()))
packet=dict(frozen_at_utc=now(),lease=proof,files=manifest,sha256sum_file=dict(sha256=sha(OUT/'SHA256SUMS.txt'),bytes=(OUT/'SHA256SUMS.txt').stat().st_size),
    excludes=['inbox','tmp','status','raw mixed ELF log','SHA256SUMS self','future WORKER_RETURN.json','publication/control receipts'])
write_json('FROZEN_DELIVERY.json',packet)
print(json.dumps(dict(files=len(names),bytes=sum(x['bytes'] for x in manifest.values()),manifest=str(OUT/'SHA256SUMS.txt')),ensure_ascii=False))
