"""运输本单四个正常 packet；原 run 不改，只移除运输副本的私网 URL 基址。"""
from pathlib import Path
import hashlib, json, os, re, zipfile
from urllib.parse import urlsplit

OUT=Path(__file__).resolve().parents[1]
RT=Path(os.environ['BI01_W07_PRIVATE_RUNTIME'])
api=json.loads((RT/'API_RESULTS.private.json').read_text())
transformations=[]

def public_bytes(raw):
    text=raw.decode('utf-8')
    def replace(m):
        url=m.group(0)
        split=urlsplit(url)
        if split.hostname in ['github.com','raw.githubusercontent.com']:
            return url
        return '[AUTHORIZED_PLATFORM]'+split.path
    return re.sub(r'https?://[^\s"\x27<>\\]+',replace,text).encode('utf-8')

for symbol,result in api.items():
    run=Path(result['board']['run_dir'])
    target=OUT/'board_delivery'/run.name
    normal_manifest=run/'delivery/DELIVERY_MANIFEST.json'
    if normal_manifest.exists():
        target.mkdir(parents=True,exist_ok=True)
        (target/'NORMAL_RUN_DELIVERY_MANIFEST.json').write_bytes(public_bytes(normal_manifest.read_bytes()))
    for name in ['timespan_index.csv','feature_slice_stats.csv','chart_manifest.csv']:
        source=run/'manifest'/name
        if not source.exists():continue
        dest=target/'manifest'/name;dest.parent.mkdir(parents=True,exist_ok=True)
        dest.write_bytes(public_bytes(source.read_bytes()))
    for source in sorted((run/'delivery/big_node_packets').glob('*_packet')):
        packet=target/source.name
        for p in sorted(source.rglob('*')):
            if not p.is_file():continue
            raw=p.read_bytes()
            payload=public_bytes(raw)
            dest=packet/p.relative_to(source);dest.parent.mkdir(parents=True,exist_ok=True)
            dest.write_bytes(payload)
            transformations.append({'run_id':run.name,'node_id':source.name.removesuffix('_packet'),
                'path':str(dest.relative_to(OUT)),
                'source_path':str(p),'original_sha256':hashlib.sha256(raw).hexdigest(),
                'transport_sha256':hashlib.sha256(payload).hexdigest(),
                'transformation':'private URL base removed from transport copy' if raw!=payload else 'byte-identical'})
        with zipfile.ZipFile(target/(source.name+'.zip'),'w',compression=zipfile.ZIP_DEFLATED) as z:
            for p in sorted(packet.rglob('*')):
                if p.is_file():z.write(p,p.relative_to(packet))
(OUT/'evidence/TRANSPORT_SOURCE_INDEX.json').write_text(json.dumps(transformations,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'normal_packets':4,'files':len(transformations),'redacted_transport_files':sum(x['transformation']!='byte-identical' for x in transformations),
    'qualification':'正常 run 原件未改；同node原表CSV按源hash字节交付，具体变换见索引'},ensure_ascii=False))
