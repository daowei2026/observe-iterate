"""读取被接受HTML内同次构图的Bokeh模型；不调用Feature或重构业务图。"""
from pathlib import Path
import json,re,hashlib,math
import numpy as np
from bokeh.document import Document
from bokeh.models import ColumnDataSource,Plot

def load_document(path):
    text=Path(path).read_text()
    match=re.search(r'<script\b[^>]*type="application/json"[^>]*>(.*?)</script>',text,re.S)
    if match is None:raise ValueError('没有独立HTML内的Bokeh JSON文档')
    docs=json.loads(match.group(1));del text,match
    if len(docs)!=1:raise ValueError('期望唯一实际Bokeh文档')
    return Document.from_json(next(iter(docs.values())))

def plain(value):
    if isinstance(value,np.ndarray):return [plain(v) for v in value]
    if isinstance(value,np.generic):return plain(value.item())
    if isinstance(value,(list,tuple)):return [plain(v) for v in value]
    if isinstance(value,dict):return {str(k):plain(v) for k,v in value.items()}
    if isinstance(value,float) and not math.isfinite(value):return {'$float':'NaN' if math.isnan(value) else ('Infinity' if value>0 else '-Infinity')}
    if value is None or isinstance(value,(str,int,float,bool)):return value
    raise TypeError('未处理的实际CDS值：'+str(type(value)))

def encoded(data):return json.dumps(plain(data),ensure_ascii=False,sort_keys=True,separators=(',',':'),allow_nan=False).encode('utf-8')
def data_hash(data):return hashlib.sha256(encoded(data)).hexdigest()

def source_rows(doc):
    figures=sorted(doc.select(dict(type=Plot)),key=lambda f:f.id)
    rows=[]
    for source in sorted(doc.select(dict(type=ColumnDataSource)),key=lambda s:s.id):
        lengths={len(v) for v in source.data.values()}
        if len(lengths)!=1:raise ValueError('CDS各列长度不一致：'+source.id)
        renderers=[dict(figure_id=f.id,figure=f.title.text,renderer_id=r.id,renderer_name=r.name,glyph=type(r.glyph).__name__)
                   for f in figures for r in f.renderers if getattr(r,'data_source',None) is source]
        rows.append(dict(id=source.id,name=source.name,rows=next(iter(lengths)),columns=list(source.data),
                         sha256=data_hash(source.data),renderers=renderers,source=source))
    return rows
