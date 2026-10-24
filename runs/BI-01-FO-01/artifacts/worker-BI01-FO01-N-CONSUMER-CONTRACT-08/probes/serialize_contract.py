"""真实 Fao 隔离构造/序列化/恢复探针；不调用layout、run或DAO写方法。"""
from pathlib import Path
import argparse,contextlib,hashlib,json,logging,os,re,sys

def safe_error(exc):
    match=re.search(r"(\w+) have no param key '([\w_]+)'",str(exc))
    return {'type':type(exc).__name__, 'unknown_parameter':match.group(2) if match else None,
            'class':match.group(1) if match else None,
            'qualification':'完整异常只在ignored，不展开参数/环境'}

def main():
    p=argparse.ArgumentParser()
    p.add_argument('--variant',choices=['old','cbd'],required=True)
    p.add_argument('--aidata-tree',required=True)
    p.add_argument('--runtime',required=True)
    p.add_argument('--restore-input')
    args=p.parse_args()
    rt=Path(args.runtime);rt.mkdir(parents=True,exist_ok=True)
    result={'variant':args.variant,'scope':'真实Fao纯构造与序列化；无layout/Feature计算/DAO写入',
            'python':sys.executable,'objects':{},'restorations':{}}
    logging.disable(logging.CRITICAL)
    with (rt/(args.variant+'-library.private.log')).open('a') as log,contextlib.redirect_stdout(log),contextlib.redirect_stderr(log):
        try:
            os.environ.setdefault('M3ROOT','/m3c3')
            os.environ.setdefault('M3WORKS','/dwdhome/fy/BASE_E6_2')
            sys.path[:0]=['/tmp/bi01-fo01-w03-runtime-20261022','/dwdhome/fy/BASE_E6_2']
            import mquant
            overlay=rt/('import-'+args.variant);overlay.mkdir(exist_ok=True)
            link=overlay/'aidata'
            if not link.exists():link.symlink_to(Path(args.aidata_tree),target_is_directory=True)
            mquant.__path__.insert(0,str(overlay))
            import mquant.aidata.big_world_chart as chart
            from mquant.aidata.contracts import build_run_handle
            from mquant.quant import OptContext
            from mquant.quant.models.graph import CaeNodeDao
            result['module_file']=str(Path(chart.__file__).resolve())
            result['module_sha256']=hashlib.sha256(Path(chart.__file__).read_bytes()).hexdigest()
            cls=chart.AidataBigWorldReviewCAE
            result['declared_keys']=sorted(dict(cls().P))
            context=OptContext(sof_name='TA_updto20240229_DBA')
            run=build_run_handle(rt/'NON_MARKET_SERIALIZATION_ONLY')
            rbi=dict(context=context,blk='rb',calendar_override='night_end_at_2300',evidence_features=[],chart_review={})
            params=chart._chart_params_from_run_brief(run,rbi)
            params=chart._params_for_fao(cls,{**params,'big_node_id':'NO_REGISTERED_NODE'})
            result['ordinary_chart_parameter_keys']=sorted(params)
            cases={'ordinary_chart_path':params}
            if args.variant=='cbd':
                cases['ordinary_key_omitted']={k:v for k,v in params.items() if k!='normal_node_behavior_manifest'}
                cases['ordinary_explicit_empty']={**params,'normal_node_behavior_manifest':''}
                # 从W07持久选择恢复同样的N实例参数形状；不调用会写manifest的构造帮助函数。
                nrun=Path('/dwdhome/fy/observe-iterate-bi01-fo-01/artifacts/bi01-worker07-runs/BI01-FO01-W07-20261024T0028-rb')
                cases['named_n']={**params,'run_dir':str(nrun),'run_id':nrun.name,'big_node_id':'big_000002',
                                  'normal_node_behavior_manifest':str(nrun/'manifest/normal_node_behavior.json')}
            for name,values in cases.items():
                try:
                    obj=cls(values)
                    memory=dict(obj.P)
                    serial=obj.fason
                    (rt/(args.variant+'-'+name+'.fason.private.txt')).write_text(serial)
                    contains='normal_node_behavior_manifest' in serial
                    safe=not re.search(r'\w+://|(?i:password|access_token|api_key)\s*[:=]',serial)
                    result['objects'][name]={'input_key_present':'normal_node_behavior_manifest' in values,
                        'memory_key_present':'normal_node_behavior_manifest' in memory,
                        'memory_n_value':memory.get('normal_node_behavior_manifest'),
                        'serialized_key_present':contains,'serialized_bytes':len(serial.encode()),
                        'serialized_sha256':hashlib.sha256(serial.encode()).hexdigest(),
                        'serialized_representation':serial if safe else '<kept ignored; safe fragment only>',
                        'serialization_safe_for_delivery':safe,'ppid':obj.ppid}
                    # 正对照同样经过真正node2fao，避免把解析/环境错误误认作跨版本失败。
                    try:
                        restored=CaeNodeDao.node2fao({'params':serial,'cls_name':'AidataBigWorldReviewCAE'})
                        restored_memory=dict(restored.P)
                        result['objects'][name]['same_version_restore']={
                            'status':'accepted','keys':sorted(restored_memory),'ppid':restored.ppid}
                    except Exception as e:
                        result['objects'][name]['same_version_restore']={'status':'rejected','error':safe_error(e)}
                        import traceback;traceback.print_exc()
                except Exception as e:
                    result['objects'][name]={'error':safe_error(e)}
                    import traceback;traceback.print_exc()
            if args.restore_input:
                inputs=json.loads(Path(args.restore_input).read_text())
                for name,item in inputs['objects'].items():
                    if 'serialized_representation' not in item:continue
                    text=item['serialized_representation']
                    if not item.get('serialization_safe_for_delivery'):continue
                    try:
                        # 与正常node2fao相同的真实恢复函数；本地dict替代Neo4j行，不访问/修改节点。
                        restored=CaeNodeDao.node2fao({'params':text,'cls_name':'AidataBigWorldReviewCAE'})
                        actual=dict(restored.P)  # 强制懒代理经过真实参数校验
                        result['restorations'][name]={'status':'accepted','keys':sorted(actual),
                            'n_key_present':'normal_node_behavior_manifest' in actual,
                            'n_value':actual.get('normal_node_behavior_manifest')}
                    except Exception as e:
                        result['restorations'][name]={'status':'rejected','error':safe_error(e)}
                        import traceback;traceback.print_exc()
        except Exception as e:
            result['fatal_error']=safe_error(e)
            import traceback;traceback.print_exc()
    target=rt/(args.variant+('-restore' if args.restore_input else '-serialize')+'.json')
    target.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'result':str(target),'variant':args.variant,
        'objects':{k:{s:v.get(s) for s in ['serialized_key_present','memory_key_present','error']} for k,v in result['objects'].items()},
        'restorations':result['restorations'],'fatal_error':result.get('fatal_error')},ensure_ascii=False))

if __name__=='__main__':main()
