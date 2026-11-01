"""封装逐文件运输回执；不访问行情源，不进行行情或特征计算。"""
import csv
import hashlib
import json
import platform
from datetime import datetime, timezone
from pathlib import Path

OUT = Path(__file__).resolve().parents[1]


def load(p):
    return json.loads((OUT / p).read_text())


def sha(b):
    return hashlib.sha256(b).hexdigest()


def main():
    manifest = load('TAIL_MANIFEST.json')
    identity = load('SOURCE_IDENTITY_CHECK.json')
    reads = {x['snapshot_path']: x for x in load('REQUIRED_READS.json')}
    prefix = load('inputs/replay_PNV_PREFIX_ROUTE_RECEIPT.json')['files']
    ranges = {x['range_path']: x for x in identity['files']}
    command = load('logs/extraction-02-same-script-repair.json')['command']
    captured_at = datetime.now(timezone.utc).isoformat()
    tool = {'extraction': manifest['tool'], 'seal_python': platform.python_version(),
            'seal_script_sha256': sha(Path(__file__).read_bytes()),
            'validator_script_sha256': sha((OUT / 'scripts/validate_tail.py').read_bytes())}
    entries = []
    for path in sorted(OUT.rglob('*')):
        rel = str(path.relative_to(OUT))
        if not path.is_file() or '.runtime' in path.relative_to(OUT).parts or rel in {'TAIL_PACKAGE_RECEIPT.json', 'SHA256SUMS'}:
            continue
        assert not path.is_symlink()
        data = path.read_bytes()
        rec = {'path': rel, 'sha256': sha(data), 'bytes': len(data),
               'rows': None, 'first_timestamp': None, 'last_timestamp': None,
               'anchor_close': None, 'tail_first_close': None, 'tail_last_close': None,
               'timezone': 'Asia/Shanghai',
               'trading_day_convention': 'No per-row trading_day field in this source; blank retained; no external assignment',
               'night_session_convention': 'same source configuration 21:00-20:00; no per-row night-session attribution exposed',
               'source_snapshot': manifest['source_snapshot'], 'source_version': 'same prior SHA256-bound staging and exact PNV logical payload',
               'extraction_command': command, 'tool_version': tool, 'recorded_at': captured_at,
               'source_path': ['WORKER_ORDER.md', 'EXTRACTION_CONTRACT.json'],
               'classification': 'authored_wrapper_or_document',
               'copied_or_deterministically_extracted': 'NOT_APPLICABLE_AUTHORED_ENGINEERING_EVIDENCE',
               'not_applicable_reason': 'Non-row document/source/log; CSV row metadata supplied when applicable',
               'verification_status': 'HASH_BYTES_VERIFIED'}
        if rel in reads:
            r = reads[rel]
            rec.update(source_path=f"daowei2026/observe-iterate@{r['commit']}:{r['source_path']}",
                       classification='deterministically_extracted' if 'selection' in r else 'copied',
                       copied_or_deterministically_extracted='deterministically_extracted' if 'selection' in r else 'copied',
                       source_sha256=r.get('source_sha256', r['sha256']),
                       selection=r.get('selection', 'whole file original bytes'))
        elif rel.startswith('inputs/frozen_prefix/'):
            sym, field = path.parent.name, path.stem
            r = next(x for x in prefix if x['source_path'] == str(Path('/m3varF/BaseData/futures/GTQH_L1_20210104_20240208/pnv/30m') / sym / (field + '.dba')))
            rec.update(source_path='daowei2026/observe-iterate@e25e585779152aa670d54c87efecba984af4b7e3:runs/BI-01-CO-04/artifacts/worker-BI01CO04-ASOF-VISIBILITY-REPLAY-01/' + r['path'],
                       classification='copied', copied_or_deterministically_extracted='copied',
                       source_sha256=r['sha256'], rows=2160,
                       first_timestamp='2021-01-04T09:30:00+08:00', last_timestamp=manifest['cutoff'],
                       not_applicable_reason=None)
        elif rel in ranges:
            r = ranges[rel]
            rec.update(source_path=r['source_path'], classification='deterministically_extracted',
                       copied_or_deterministically_extracted='deterministically_extracted',
                       rows=r['range_rows'], first_timestamp=manifest['cutoff'], last_timestamp=manifest['endpoint'],
                       source_byte_start=r['source_byte_start'], source_byte_end_exclusive=r['source_byte_end_exclusive'],
                       not_applicable_reason=None, verification_status='RAW_RANGE_CSV_AND_LIVE_SOURCE_VERIFIED')
        elif rel in [s + '_30m_tail.csv' for s in manifest['symbols']]:
            s = path.name.split('_', 1)[0]
            stats = manifest['outputs'][s]
            rec.update(source_path=[r['source_path'] for r in identity['files'] if r['symbol'] == s],
                       classification='deterministically_extracted', copied_or_deterministically_extracted='deterministically_extracted',
                       anchor_close=stats['anchor_close'], tail_first_close=stats['tail_first_close'],
                       tail_last_close=stats['tail_last_close'],
                       not_applicable_reason=None, verification_status='INDEPENDENT_RAW_RANGE_LIVE_SOURCE_ANCHOR_ENDPOINT_METRICS_VERIFIED')
        elif rel == 'WORKER_ORDER.md':
            rec.update(source_path='daowei2026/observe-iterate@e2ca9cf0e264855f4c10a4f081fed13db1603e53:runs/BI-01-CO-04/reviews/management-R0010/WORKER_ORDER.md',
                       classification='copied', copied_or_deterministically_extracted='copied')
        elif rel.startswith('logs/') or rel == 'EXTRACTION_FAILURE.json':
            rec.update(classification='captured_execution_evidence',
                       copied_or_deterministically_extracted='NOT_APPLICABLE_CAPTURED_EXECUTION_EVIDENCE',
                       source_path='scripts/record_command.py + scripts/extract_tail.py or scripts/validate_tail.py; actual process output')
        if path.suffix == '.csv':
            with path.open(newline='') as f:
                rows = list(csv.DictReader(f))
            rec['rows'] = len(rows)
            field = next((s for s in ['business_timestamp', 'closeTs', 'bar_cutoff_asia_shanghai'] if rows and s in rows[0]), None)
            if field:
                times = [r[field] for r in rows]
                rec['first_timestamp'], rec['last_timestamp'] = min(times), max(times)
                rec['not_applicable_reason'] = None
        entries.append(rec)
    receipt = {'schema': 'frozen-tail-package-receipt/v1',
               'order_id': 'BI01CO04-FROZEN-TAIL-TRANSPORT-01', 'exit': manifest['exit'],
               'file_count_excluding_envelope': len(entries),
               'bytes_excluding_envelope': sum(r['bytes'] for r in entries),
               'self_reference_exclusion': ['TAIL_PACKAGE_RECEIPT.json', 'SHA256SUMS'],
               'self_reference_rule': 'receipt excludes itself and SHA256SUMS; SHA256SUMS includes receipt and every other deliverable except itself; final Git commit fixes SHA256SUMS',
               'runtime_exclusion': '.runtime (execution ledger and independent consumer temp output)',
               'files': entries}
    (OUT / 'TAIL_PACKAGE_RECEIPT.json').write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + '\n')
    sealed = [(r['path'], r['sha256']) for r in entries]
    sealed.append(('TAIL_PACKAGE_RECEIPT.json', sha((OUT / 'TAIL_PACKAGE_RECEIPT.json').read_bytes())))
    (OUT / 'SHA256SUMS').write_text(''.join(f'{h}  {name}\n' for name, h in sorted(sealed)))
    print(json.dumps({'files_excluding_envelope': len(entries), 'outer_seal_entries': len(sealed),
                      'bytes_excluding_envelope': receipt['bytes_excluding_envelope'], 'exit': manifest['exit']}))


if __name__ == '__main__':
    main()
