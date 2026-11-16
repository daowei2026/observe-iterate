"""读取独立数据包，通过 Bokeh server 查看 CAEGraph；不生成 HTML 文件。"""
from pathlib import Path
import argparse
import csv
import gc
import json
import os


def load_index(data_dir):
    data_dir = Path(data_dir).expanduser().resolve()
    if not (data_dir / 'manifest.json').is_file():
        raise ValueError(f'找不到 {data_dir / "manifest.json"}，请先解压数据包')
    manifest = json.loads((data_dir / 'manifest.json').read_text())
    with (data_dir / 'timespans.csv').open() as source:
        rows = list(csv.DictReader(source))
    lookup = {row['node_id']: row for row in rows}
    nodes = [('overview', 'run_overview')]
    nodes += [('multiscale', node) for node in manifest['included_big_node_ids']]
    nodes += [('tick', node) for node in manifest['included_tick_node_ids']]
    return manifest, lookup, nodes


def make_layout(kind, node_id, root):
    from caegraph_definitions import build_overview, build_multiscale, build_tick
    if kind == 'overview':
        return build_overview(root)
    if kind == 'multiscale':
        return build_multiscale(root, node_id=node_id)
    return build_tick(root, node_id=node_id)


def inspect_layout(layout, kind, node_id):
    from bokeh.models import Div, Plot, GlyphRenderer
    models = layout.references()
    errors = [m.text for m in models if isinstance(m, Div) and
              any(term in m.text for term in ('Traceback', '读取失败', '未读取'))]
    if errors:
        raise RuntimeError(f'{node_id}: {errors[0]}')
    counts = {'node_id': node_id, 'kind': kind,
              'figures': sum(isinstance(m, Plot) for m in models),
              'glyphs': sum(isinstance(m, GlyphRenderer) for m in models),
              'plot_roots': len(getattr(layout, 'plot_roots', []))}
    expected = {'overview': 1, 'multiscale': 16, 'tick': 4}[kind]
    if counts['figures'] != expected or not counts['plot_roots']:
        raise RuntimeError(f'图数量或 CAEGraph 数据树异常：{counts}')
    return counts


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--data-dir', type=Path, default=Path(__file__).resolve().parent / 'data',
                        help='解压后的 data 目录，默认与脚本相邻的 data/')
    parser.add_argument('--chart', choices=['all', 'overview', 'multiscale', 'tick'], default='all')
    parser.add_argument('--node-id', help='只查看指定节点，例如 big_000002 或 tick_000030')
    parser.add_argument('--list', action='store_true', help='列出可用图窗，不加载绘图库')
    parser.add_argument('--check', action='store_true', help='逐一构造所选图窗并检查，不启动网页或生成 HTML')
    parser.add_argument('--report', type=Path, help='可选：将检查报告保存为 JSON')
    parser.add_argument('--host', default='127.0.0.1')
    parser.add_argument('--port', type=int, default=5006)
    parser.add_argument('--no-browser', action='store_true')
    args = parser.parse_args(argv)
    try:
        manifest, lookup, nodes = load_index(args.data_dir)
    except (ValueError, OSError) as exc:
        parser.error(str(exc))
    nodes = [(kind, node) for kind, node in nodes
             if (args.chart == 'all' or kind == args.chart)
             and (args.node_id is None or node == args.node_id)]
    if not nodes:
        parser.error('所选节点不在数据包内；使用 --list 查看可用节点')
    if args.list:
        for kind, node in nodes:
            row = lookup.get(node, {})
            print(kind, node, row.get('parent_node_id', ''),
                  row.get('start_ts', ''), row.get('end_ts', ''))
        return
    root = args.data_dir.expanduser().resolve().parent
    os.environ['CAEGRAPH_DATA_ROOT'] = str(root)
    if args.check:
        reports = []
        for kind, node in nodes:
            print('正在检查', kind, node, flush=True)
            layout = make_layout(kind, node, root)
            reports.append(inspect_layout(layout, kind, node))
            del layout
            gc.collect()
        report = {'data_scope': manifest['data_scope'], 'checked': reports}
        if args.report:
            args.report.parent.mkdir(parents=True, exist_ok=True)
            args.report.write_text(json.dumps(report, ensure_ascii=False, indent=2))
        print('通过：', len(reports), '组图窗；未生成 HTML 文件。', flush=True)
        return report

    from bokeh.layouts import column
    from bokeh.models import Select, Div
    from bokeh.server.server import Server

    def application(doc):
        def label(kind, node):
            if kind == 'overview':
                return '长期概览（日线；6个大尺度定位框）'
            row = lookup[node]
            prefix = '30min / 1min / 5s 组合' if kind == 'multiscale' else 'Tick'
            return f"{prefix} | {node} | {row['parent_node_id']} | {row['start_ts']} ~ {row['end_ts']}"
        index = {label(kind, node): (kind, node) for kind, node in nodes}
        selector = Select(title='选择图窗', value=label(*nodes[0]),
                          options=list(index), width=1100)
        detail = Div(width=1100)
        content = column()

        def select_node(attr, old, new):
            content.children = []
            kind, node = index[new]
            detail.text = '<p>数据范围：1个概览、6个30min、18个1min、54个5s，Tick暂含前30个窗口。</p>'
            content.children = [make_layout(kind, node, root)]
            gc.collect()
        selector.on_change('value', select_node)
        select_node(None, None, selector.value)
        doc.add_root(column(selector, detail, content))
        doc.title = '钢铁板块 CAEGraph 多尺度观察'

    origins = [f'{host}:{args.port}' for host in {args.host, 'localhost', '127.0.0.1'}]
    server = Server({'/': application}, address=args.host, port=args.port,
                    allow_websocket_origin=origins)
    server.start()
    print(f'打开 http://{args.host}:{server.port}/ ，在页面下拉框选择图窗。', flush=True)
    if not args.no_browser:
        server.io_loop.add_callback(server.show, '/')
    server.io_loop.start()


if __name__ == '__main__':
    main()
