"""读取现有正式DBA；不实例化producer、不调用run、每路最多三个完整批次。"""
import contextlib
import inspect
import io
import json
import pathlib
import signal
import sys
import time
import traceback
from support import BASE, OUT, lease, now, readonly_audit, write_json, sha

started=time.monotonic()
binding=json.loads((OUT/'BINDING.json').read_text())
assert binding['binding_succeeded']
full=pathlib.Path(binding['bindings']['feature']['full_dir'])
source=pathlib.Path(binding['bindings']['source']['full_dir'])
report=dict(started_at_utc=now(),lease=lease(),full_dir=str(full),source_dir=str(source),
    read_mode='direct existing DbaStore and DbaUtil ACCESS_READ; no run/F',
    feature_calculation_executed=False,streams={},schema_files={},source_matches=[],audit=[])
readonly_audit(report['audit'],allow_git=True,read_prefixes=(full,source))
def forbid(frame,event,arg):
    if event=='call' and frame.f_code.co_name in ('_impl','_execute','_run_up','_run_ups','rerun') and '/mquant/' in frame.f_code.co_filename:
        raise RuntimeError('W001 prohibits feature execution: '+frame.f_code.co_filename)
sys.setprofile(forbid)
signal.signal(signal.SIGALRM,lambda *_: (_ for _ in ()).throw(TimeoutError('readback 180s limit')))
signal.alarm(180)

def jvalue(v):
    if hasattr(v,'_asdict'):
        return dict(__type__=type(v).__name__,**{k:jvalue(x) for k,x in v._asdict().items()})
    if isinstance(v,(list,tuple)):return [jvalue(x) for x in v]
    if isinstance(v,dict):return {str(k):jvalue(x) for k,x in v.items()}
    if hasattr(v,'dtype') and getattr(v.dtype,'kind','') in ('M','m'):return str(v)
    if hasattr(v,'item'):return jvalue(v.item())
    if isinstance(v,float) and (v!=v or abs(v)==float('inf')):return dict(__float__=str(v))
    if v is None or isinstance(v,(str,int,float,bool)):return v
    return str(v)

def schema_info(cls):
    p=pathlib.Path(inspect.getfile(cls))
    r=dict(class_name=cls.__name__,module=cls.__module__,file=str(p),adt=str(getattr(cls,'__adt__',None)),
        adt_fields=list(getattr(getattr(cls,'__adt__',None),'_fields',[])))
    if str(p) not in report['schema_files']:
        s=p.stat();report['schema_files'][str(p)]=dict(sha256=sha(p),size=s.st_size,mtime_ns=s.st_mtime_ns)
    return r

try:
    # 与现役入口保持相同的模块注册；仅创建DBA读取对象。
    import numpy as np
    from mquant.tis.frp.EawBattleP import EawP1WallLifecycleFrp
    from mquant.frame import NormalField,DbaUtil
    from pydim.dim import DbaStore
    fields=json.loads((full/'fields.json').read_text())
    occurrence_targets=[]
    for name in ('wall_occurrences','wall_current_view','wall_diagnostics'):
        fact=dict(field_key_present=name in fields,path=str(full/name),samples=[],read_attempted=False)
        report['streams'][name]=fact
        if name not in fields:continue
        try:
            fact['fdtype']=fields[name]
            cls=NormalField.from_str(fields[name]).adt_class
            fact['schema']=schema_info(cls)
            fact['read_attempted']=True
            messages=io.StringIO()
            with contextlib.redirect_stdout(messages):
                store=DbaStore(str(full/name),cls)
            root=store.root_seq
            fact['arm_messages']=messages.getvalue()
            fact['schema_arm_complete']='FileNotFoundError' not in messages.getvalue() and type(root).__name__!='EmptyDbaStruct'
            fact['runtime_root_class']=type(root).__name__
            ts=DbaUtil.read_field_ts(str(full),name,True)
            count=int(root.count())
            fact.update(outer_event_count=int(count),timestamp_count=len(ts),axis_matches_root=count==len(ts),
                timestamp_range=[str(ts[0]),str(ts[-1])] if len(ts) else None)
            # MulWrap 层本身是外层事件；其 mul 字段是一个变长业务/诊断列表。
            pointers=root.mul.ndarray
            anchors=root.mul_seq.__anchor__.ndarray
            assert len(pointers)==count
            ends=anchors[pointers]
            starts=np.where(pointers>0,anchors[np.maximum(pointers-1,0)],0)
            lengths=ends-starts
            nonempty=np.flatnonzero(lengths>0)
            fact.update(inner_item_count_from_anchors=int(lengths.sum()),nonempty_outer_events=int(len(nonempty)),
                count_basis='all root pointers and list anchors only; no full payload decode',
                inner_count_role='stored diagnostic rows, not count of P1ProductDiagnostics envelopes' if name=='wall_diagnostics' else 'stored business rows')
            fact['nested_schema']=schema_info(type(root.mul_seq))
            selected=sorted(set(int(nonempty[x]) for x in (0,len(nonempty)//2,len(nonempty)-1))) if len(nonempty) else []
            if len(nonempty):fact['nonempty_timestamp_range']=[str(ts[int(nonempty[0])]),str(ts[int(nonempty[-1])])]
            for index in selected:
                sample=dict(original_outer_index=index,outer_time=str(ts[index]),
                    inner_anchor_start=int(starts[index]),inner_anchor_end=int(ends[index]),
                    inner_item_count=int(lengths[index]),source_path=str(full/name),complete_decoded_batch=False)
                if lengths[index]>64:
                    sample['not_expanded_reason']='batch exceeds bounded 64-row sample budget'
                else:
                    sample['decoded']=jvalue(root.load(index))
                    sample['complete_decoded_batch']=fact['schema_arm_complete']
                    if name=='wall_occurrences':
                        for row in sample['decoded'].get('mul',[]):
                            occurrence_targets.append(dict(outer_index=index,outer_time=sample['outer_time'],
                                uti=row.get('p1WallLifecycleOccurredAt'),local_no=row.get('p1WallOccurrenceLocalNo'),
                                occurrence_ref=row.get('p1WallOccurrenceRef')))
                fact['samples'].append(sample)
            fact['payload_read_succeeded']=fact['schema_arm_complete'] and fact['axis_matches_root']
            if fact['samples']:write_json('samples/'+name+'.json',dict(stream=name,fdtype=fields[name],samples=fact['samples']))
        except Exception:
            fact.update(payload_read_succeeded=False,traceback=traceback.format_exc())
    report['occurrence_targets']=occurrence_targets
    source_fields=json.loads((source/'fields.json').read_text())
    report['source_stream_checks']={}
    for key,columns in source_fields.items():
        if not key.startswith('wall__'):continue
        check=dict(columns=columns,matched_rows=[])
        report['source_stream_checks'][key]=check
        try:
            arrays={col:DbaUtil.read_ndarray(str(source),key+'.'+col,dt) for col,dt in columns.items()}
            utis=arrays['uti'];check['row_count_from_header']=len(utis)
            check['uti_range']=[int(utis[0]),int(utis[-1])] if len(utis) else None
            for target in occurrence_targets:
                if target['uti'] is None or target['local_no'] is None:continue
                lo=int(np.searchsorted(utis,target['uti'],side='left'))
                hi=int(np.searchsorted(utis,target['uti'],side='right'))
                if hi-lo>32:continue
                for i in range(lo,hi):
                    if int(arrays['wall_id'][i])==target['local_no']:
                        row=dict(target=target,physical_key=key,physical_row_index=i,
                            raw_row={col:jvalue(a[i]) for col,a in arrays.items()})
                        check['matched_rows'].append(row);report['source_matches'].append(row)
            check['match_basis']='binary search on stored UTI column + exact local_no; no full join'
        except Exception:check['traceback']=traceback.format_exc()
    if report['source_matches']:write_json('samples/source_wall_matches.json',report['source_matches'])
except Exception:
    report['fatal_traceback']=traceback.format_exc()
finally:
    signal.alarm(0);sys.setprofile(None)
    report['elapsed_seconds']=round(time.monotonic()-started,6)
    for event in report['audit']:
        if event.get('decision')!='READ_ONLY' or 'mtime_ns_before' not in event:continue
        p=pathlib.Path(event['path'])
        s=p.stat()
        event['unchanged_after_read']=(s.st_size,s.st_mtime_ns,s.st_ino)==(event['size_before'],event['mtime_ns_before'],event['inode_before'])
    write_json('READBACK.json',report)
    print(json.dumps({k:v for k,v in report.items() if k not in ('audit','source_matches')},ensure_ascii=False,indent=2,default=str))
    print('REPORT:',OUT/'READBACK.json')
