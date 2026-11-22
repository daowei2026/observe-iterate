"""D定义级检查；禁止真实Feature.run/构图/HTML/正式取图数据。"""
from pathlib import Path
from datetime import datetime, timezone
import ast
import csv
import json
import inspect
import sys
import traceback

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
from run_definition import bootstrap

checks = []
details = {}


def check(name, action, evidence):
    try:
        value = action()
        checks.append(dict(检查项=name, 结果='通过', 证据=evidence, 影响='不阻塞E', 修订目标='D'))
        return value
    except Exception as error:
        checks.append(dict(检查项=name, 结果='不通过', 证据=evidence,
                           影响=str(error), 修订目标='D', traceback=traceback.format_exc()))
        raise


def require(value, message):
    if not value:
        raise ValueError(message)


def syntax():
    for p in [ROOT / 'run_definition.py', ROOT / 'definition_checks.py',
              ROOT / 'definition/f800_definition.py', ROOT / 'definition/caegraph_display.py']:
        compile(p.read_text(), str(p), 'exec')


def main():
    result = dict(definition='F800-D-v1', run_id='OI-F800-STAT-20261122-01', call_id='C0025',
                  started_at=datetime.now(timezone.utc).isoformat(), scope='D定义级检查',
                  native_feature_run_calls=0, final_graph_built=False, html_generated=False,
                  formal_graph_data_extracted=False, checks=checks)
    try:
        check('完整脚本及C3语法', syntax, 'compile，不执行构图')
        check('锁定20个uplot源文件及17个依赖完整性/导入', bootstrap,
              'bootstrap逐文件SHA-256核对后导入，不构图；UPLOT_SOURCE_SNAPSHOT/DEPENDENCY_BINDING')
        import numpy as np
        import pandas as pd
        import f800_definition as d
        import caegraph_display as c3
        from mquant.frame import FaoType
        from mquant.uplot import CAEGraph, PlotSet, PerSymFigs, AllSymsFig, KPriceLine, MulFieldsGlyphs, MulSegPlot
        originals = (FaoType.run, c3.build_display, CAEGraph.layout)

        def forbidden(*args, **kwargs):
            raise AssertionError('D检查不得运行Feature或最终图')

        FaoType.run = forbidden
        c3.build_display = forbidden
        CAEGraph.layout = forbidden
        try:
            def exact_c3():
                require(d.digest(ROOT / 'definition/caegraph_display.py') == d.C3_HASH,
                        'C3字节改变')
                sig = inspect.signature(d.build_display)
                require(list(sig.parameters) == ['instance', 'reader', 'context', 'position', 'fields', 'caption'],
                        'C3接口变化')
            check('C3-v1准确字节/注入接口/C2-v4语义保留', exact_c3,
                  'SHA e5d6a235…；不运行C3，不复制或重生成预期HTML')

            def bound_instance():
                with d.bound_environment():
                    instance = d.construct_instance()
                    d.check_result_identity(instance)
                    context = d.OptContext(**d.sof_parameters())
                    position, boundary = d.resolve_position(context)
                    details['instance'] = dict(feature_class=type(instance).__name__, full_dir=str(instance.full_dir),
                                               configuration_sha256=d.CONFIG_HASH,
                                               constructor_file=inspect.getfile(d.make_features),
                                               native_run_called=False)
                    details['position'] = position
                    details['boundary'] = boundary
                    require(instance.sof.sof_name == context.sof.sof_name and
                            instance.sof.startDay == context.sof.startDay and
                            instance.sof.endDay == context.sof.endDay, '实例和绘图SOF不一致')
            check('真实正常构造/序列化配置/准确结果身份', bound_instance,
                  '真实CommonPriceTurnGroupCandidatesFrp构造及doFrpTaskParam(run_ups=False)；FaoType.run强制禁止')
            check('完整三年B位置及日历含端点进入真实配置',
                  lambda: require(details['position']['end'] + 1 == details['boundary']['plotctx_exclusive_stop'],
                                  '端点不一致'),
                  'BOUND_INSTANCE_CHECK.json：原请求日期→native opt_date_range→真实Calendar UTI；未采用数据首末缩短')

            schema = d.load('inputs/PUBLIC_TABLE_SCHEMA.json')
            fields = d.load('FIELD_BINDING.json')
            def mapped_fields():
                source = d.load('inputs/FIELD_MAP_TEMPLATE.json')['fields']
                declared = set(schema['tables']['occurrences']['fields'])
                declared.update(c + '_name' for c in schema['enums'] if c in declared)
                for role, spec in source['groups'].items():
                    for name in spec.values() if isinstance(spec, dict) else [spec]:
                        require(name in declared, '主输出字段未声明：' + name)
                require(fields['parents'] == ['timestamp', 'occurrence', 'record_id', 'child_id_2'],
                        '父坐标不完整')
                part = fields['participation']
                require(set(part[k] for k in ('duty', 'admission', 'handoff')).issubset(
                        schema['tables'][part['table']]['fields']), '参与字段未声明')
                require(set(source['groups']) == set(fields['groups']), 'C3语义字段丢失')
                require(fields['selected'] == source['selected'] and fields['raw'] == source['raw'] and
                        fields['kline'] == source['kline'], '字段语义改变')
                for role in d.WINDOW_ROLES:
                    require(fields['groups'][role] == '__uti_' + source['groups'][role], '坐标别名接线错误')
            check('共享Package/完整Schema/身份/状态/父键及字段绑定', mapped_fields,
                  'FIELD_BINDING.json对照准确D008 PUBLIC_TABLE_SCHEMA、原C3模板；仅增加无损窗口坐标别名')

            def axes():
                source = d.load('inputs/FIELD_MAP_TEMPLATE.json')['fields']['groups']
                names = [source[k] for k in d.WINDOW_ROLES]
                accepted = next(t for t in d.load('inputs/FeatureRunResultBinding.json')['run_result_tables']
                                if t['name'] == 'occurrences')
                p = Path(accepted['path'])
                require(d.digest(p) == accepted['sha256'], '已接受的兼容性样本源漂移')
                frame = pd.read_csv(p, usecols=names)
                adapted = d.adapt_window_axes(frame)
                require(adapted[names].equals(frame), '原生float字段被改写')
                require(all(pd.api.types.is_integer_dtype(adapted['__uti_' + n]) for n in names),
                        '显示别名不是整数')
                details['window_axis_compatibility'] = dict(checked_accepted_source_rows=len(frame),
                    source_sha256=accepted['sha256'], original_dtypes={n: str(frame[n].dtype) for n in names},
                    aliases_integer=True, original_columns_unchanged=True,
                    use='小范围源字段兼容性检查，不是E原生读回/构图/图数据')
                for value in [np.nan, np.inf, -np.inf, 0.5, float(2**53 + 2)]:
                    bad = pd.DataFrame({n: [value] for n in names})
                    try:
                        d.adapt_window_axes(bad)
                    except ValueError:
                        continue
                    raise ValueError('错误坐标被静默接受：' + str(value))
            check('原生Float64窗口→整型UTI无损别名及错误拒绝', axes,
                  '1538行×六坐标的已接受CSV字段兼容性检查；NaN/±Inf/小数/越界拒绝，原列保留')

            def selected():
                original = pd.DataFrame(dict(symbol=['rb', 'rb'], round=['value1', 'value2'],
                    source_row=[0, 1], turn_id=['fixture1', 'fixture2'], actual=[1, 2],
                    confirmation=[3, 4], known=[5, 6], actual_ts=['a', 'b'],
                    confirmation_ts=['c', 'd'], known_ts=['e', 'f'], price=[1., 2.],
                    confirmation_price=[3., 4.], raw_known=[2, 3], first_block_screen=['reference', 'reference']))
                out = d.adapt_selected(original)
                require(out.round_display.tolist() == [0, 1] and out['round'].tolist() == ['value1', 'value2'],
                        '轮次显示编码丢失原值')
                require(out.known.tolist() == [5, 6] and out.confirmation.tolist() == [3, 4], 'known被替换成几何C')
                require('first_block_screen' not in out, 'G参考筛查混入原生输入')
                source = next(x for x in d.load('SOURCE_DATA_BINDING.json')['source_files']
                              if x['kind'] == 'accepted_canonical_selected')
                with Path(source['path']).open(encoding='utf-8-sig') as f:
                    headers = next(csv.reader(f))
                require(set(d.SELECTED_COLUMNS).issubset(headers), '已接受上游规范形状缺列')
            check('selected轮次/已知轴/源定位键及G参考列隔离', selected,
                  '微型接线夹具+准确上游CSV表头；保留value1/value2，round_display仅0/1显示，未运行真实reader')

            def data_references():
                for item in d.load('SOURCE_DATA_BINDING.json')['source_files']:
                    require(d.digest(item['path']) == item['sha256'], '准确上游源字节变化：' + item['path'])
                binding = d.load('inputs/FeatureRunResultBinding.json')
                require(len(binding['run_result_tables']) == 31, '31表合同变化')
                children = [t for t in binding['run_result_tables'] if t['name'].startswith('occurrences_')]
                for t in children:
                    require(t['index_names'][:4] == fields['parents'], '子表完整父前缀错配')
                details['source_counts'] = dict(public_tables=31, group_children=len(children),
                    non_group_tables=31-len(children)-1, materialized_source_files=13,
                    policy='D核源引用/字节/声明；真实OnlyRead及图层内容待E')
            check('真实数据入口/全部子层级/非组根metadata引用', data_references,
                  'SOURCE_DATA_BINDING：13个已接受物化源哈希；31表合同，occurrences_*全部交children，其他公开表交metadata')

            def paths():
                code = ast.parse((ROOT / 'definition/f800_definition.py').read_text())
                calls = [n for n in ast.walk(code) if isinstance(n, ast.Call)]
                runs = [n for n in calls if isinstance(n.func, ast.Attribute) and n.func.attr in ('run', 'rerun')]
                require(len(runs) == 1 and ast.unparse(runs[0]) == 'instance.run(CalType.OnlyRead)',
                        '定义混入非OnlyRead的Feature执行路径')
                for token in ('SYN-Life', '2022-06-15', 'SYNTHETIC-ONLY'):
                    require(token not in (ROOT / 'definition/f800_definition.py').read_text(), '预览绑定泄漏')
                require(not (RUN_E := ROOT.parent / 'caegraph-E/f800.html').exists(), '本D不应生成最终HTML')
            check('无预览实例/日期泄漏、无生产路径、未运行最终图', paths,
                  'AST核只有OnlyRead调用；FaoType.run/CAEGraph.layout在本检查进程强制禁止')
            details['guards'] = dict(real_feature_run_forbidden=True, CAEGraph_layout_forbidden=True,
                                     reader_called=False, C3_called=False, html_generated=False)
        finally:
            FaoType.run, c3.build_display, CAEGraph.layout = originals
        result['all_passed'] = True
    except Exception:
        result['all_passed'] = False
        result['error'] = traceback.format_exc()
        print(result['error'], flush=True)
    result['finished_at'] = datetime.now(timezone.utc).isoformat()
    (ROOT / 'DEFINITION_CHECKS.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    (ROOT / 'BOUND_INSTANCE_CHECK.json').write_text(json.dumps(details, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps(dict(all_passed=result['all_passed'], checks=len(checks),
                         native_feature_run_calls=0, final_graph_built=False, html_generated=False), ensure_ascii=False))
    return 0 if result['all_passed'] else 1


if __name__ == '__main__':
    sys.exit(main())
