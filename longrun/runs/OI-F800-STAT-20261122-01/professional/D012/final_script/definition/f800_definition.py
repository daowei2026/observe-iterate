"""F800-D-v1：真实实例、完整B位置与C3-v1的正式集成定义。

导入、construct_instance和resolve_position不运行Feature、不构图。
build_bound_display由后继E调用；价格/上游从D008已验收物化源只读，
F主输出从同一准确实例的OnlyRead/to_dfs取得，绝不缺失时重算。
"""
from contextlib import contextmanager
from hashlib import sha256
from pathlib import Path
import inspect
import json
import os

import numpy as np
import pandas as pd
from m3sof import settings
from mquant.frame import CurrCalendar, CurrSof, CalType, opt_date_range
from mquant.tis.frp.fqv_kline_example import make_features
from mquant.tis.frp.CommonPriceTurnGroupCandidates import CommonPriceTurnGroupCandidatesFrp
from mquant.uplot.utlv2 import OptContext
from caegraph_display import build_display, raw_records

ROOT = Path(__file__).resolve().parents[1]
BASE = Path('/dwdhome/fy/BASE_E6_2_copy')
RUN = BASE / 'artifacts/OI-F800-STAT-20261122-01'
XROOT = RUN / 'D008'
RUNTIME = BASE / '.runtime/f800-input-missing-20261123/runtime'
FRP = '39f02ec4548e68ba8dbd30061afc870546000994'
TIS = '2f460d663d821cf2ba25555eda13e78b697d0767'
UPLOT = '0a4fcd54059782572a3f7e82fad041121e8c65ad'
DEFINITION_ID = 'F800-D-v1'
CONFIG_HASH = 'b72095ff100da926474701b74bff7586a74b9770bc81cadc34c23cfe223e5cb3'
C3_HASH = 'e5d6a235cd23f7e90ebbd8f020768f7e91b81ffd1782fc824362543c0f696ec0'


def load(name):
    return json.loads((ROOT / name).read_text())


def digest(path):
    h = sha256()
    with Path(path).open('rb') as f:
        for part in iter(lambda: f.read(1024 * 1024), b''):
            h.update(part)
    return h.hexdigest()


def require(condition, message):
    if not condition:
        raise ValueError(message)


def ordinary_position():
    source = load('inputs/OrdinaryPositions.json')
    require(source['位置用法'] == '任务明确指定', 'B来源发生变化，返回B')
    require(len(source['位置定义']) == 1, 'B位置数发生变化，返回B')
    return source['位置定义'][0]


def sof_parameters():
    b = ordinary_position()
    return dict(sof_name='TA_updto20240229_DBA', stk_tlist='steel',
                startDay=b['开始时间'], endDay=b['结束时间'], full_period=None)


@contextmanager
def bound_environment():
    """沿D008既有存储路由读准确实例；只把本次日志放到D011。"""
    require(Path(os.environ.get('M3WORKS', '')).resolve() == RUNTIME.resolve(),
            '必须从本定义的锁定runtime启动')
    names = ('APP_DIR', 'DEFAULT_STORE_DIR', 'MQUANT_LOGGER_DIR')
    previous = {k: settings.ctx.get(k) for k in names}
    settings.ctx['APP_DIR'] = str(XROOT / 'platform-app')
    settings.ctx['DEFAULT_STORE_DIR'] = str(XROOT / 'store')
    settings.ctx['MQUANT_LOGGER_DIR'] = str(ROOT / 'runtime-logs')
    try:
        with CurrSof(**sof_parameters()), CurrCalendar('night_end_at_2300'):
            yield
    finally:
        for k, v in previous.items():
            if v is None:
                settings.ctx.pop(k, None)
            else:
                settings.ctx[k] = v


def construct_instance():
    """正常参数构造；唯一override=800；此处没有run/rerun。"""
    require(digest(ROOT / 'inputs/configuration.json') == CONFIG_HASH, '完整配置字节漂移')
    params = load('inputs/base_parameters.json')
    params['symbols'] = tuple(params['symbols'])
    base, _, _ = make_features(**params)
    profile = dict(base.P.profile)
    profile['observation_multiple'] = 800
    require(base.P.inputs is not None, '正式inputs入口变化，返回D')
    instance = CommonPriceTurnGroupCandidatesFrp(
        inputs=base.P.inputs, domain=base.P.domain, profile=profile,
        result_layout=base.P.result_layout)
    actual = json.loads(instance.doFrpTaskParam(run_ups=False).for_json()['params'])
    expected = load('inputs/configuration.json')
    require(actual == expected, '真实构造参数与准确外层实例不一致')
    require(actual['profile']['observation_multiple'] == 800 and
            actual['profile']['delta'] == 600 and
            actual['profile']['method']['revision'] == '1', 'profile锁不一致')
    binding = load('inputs/FeatureRunResultBinding.json')
    require(str(instance.full_dir) == binding['result_identity']['full_dir'], '结果目录身份不一致')
    for cls, relative in [(make_features, 'fqv_kline_example.py'),
                          (CommonPriceTurnGroupCandidatesFrp, 'CommonPriceTurnGroupCandidates.py')]:
        require(Path(inspect.getfile(cls)).resolve() ==
                (RUNTIME / 'mquant/tis/frp' / relative).resolve(), '实际加载入口漂移')
    return instance


def resolve_position(context):
    """B日期按SOF既有21:00/20:00规则解析，再传真实含端点的UTI。

    右端使用right-1避免无交易标签的周末日期被PlotCtx的left+1
    扩到下一个交易时点。没有采用数据首末点缩短B请求。
    """
    b = ordinary_position()
    require(b['品种集'] == ['rb', 'hc', 'i'] and b['采样'] == '5m', 'B品种/频度改变')
    require((b['开始时间'], b['结束时间']) == ('2021-01-01', '2023-12-31'), 'B三年范围改变')
    period = opt_date_range(b['开始时间'], b['结束时间'])
    require(period.start == '2021-01-01 21:00:00' and
            period.end == '2023-12-31 20:00:00', '本SOF日期规则漂移')
    utsa = context.sof.tsa_of('night_end_at_2300')['natural_tsa']
    lo = int(np.searchsorted(utsa, np.datetime64(period.start), side='left'))
    hi = int(np.searchsorted(utsa, np.datetime64(period.end), side='right')) - 1
    require(0 <= lo <= hi < len(utsa), 'B日历范围为空或越界')
    position = dict(position_id=b['position_id'], symbols=list(b['品种集']),
                    start=lo, end=hi, calendar='night_end_at_2300', scale='5m',
                    width=1180, label_freq='120m')
    explanation = dict(requested_start=b['开始时间'], requested_end=b['结束时间'],
                       native_sof_start=period.start, native_sof_end=period.end,
                       first_calendar_label=str(utsa[lo]), last_calendar_label=str(utsa[hi]),
                       inclusive_start_uti=lo, inclusive_end_uti=hi,
                       plotctx_exclusive_stop=hi + 1,
                       source='mquant.frame.core.app.utils.opt_date_range + pinned PlotCtx inclusive integer UTI',
                       shortened_to_available_data=False, multiscale=None)
    return position, explanation


WINDOW_ROLES = ('original_anchor', 'original_d', 'original_r', 'anchor', 'd', 'r')


def adapt_window_axes(frame):
    """native Float64原值保留，只增加经严格核验的整数UTI显示别名。"""
    source_map = load('inputs/FIELD_MAP_TEMPLATE.json')['fields']['groups']
    out = frame.copy()
    for role in WINDOW_ROLES:
        original = source_map[role]
        values = out[original]
        if pd.api.types.is_integer_dtype(values):
            require(not values.isna().any(), original + '有缺值')
            require(((values >= -(2**53)) & (values <= 2**53)).all(), original + '超出本转换精确范围')
            alias = values.astype('int64')
        else:
            require(pd.api.types.is_float_dtype(values), original + '不是原生数值坐标')
            a = values.to_numpy(dtype='float64')
            require((np.isfinite(a) & (np.abs(a) <= 2**53) & (a == np.trunc(a))).all(),
                    original + '不能无损转整型UTI；禁止取整/插值，返回D或共享理解')
            alias = pd.Series(a.astype('int64'), index=values.index)
            require(np.array_equal(alias.to_numpy(dtype='float64'), a), original + '未通过回转核验')
        out['__uti_' + original] = alias
    return out


SELECTED_COLUMNS = ('symbol', 'round', 'source_row', 'turn_id', 'actual', 'confirmation',
                    'known', 'actual_ts', 'confirmation_ts', 'known_ts', 'price',
                    'confirmation_price', 'raw_known')


def adapt_selected(frame):
    """只绑定已接受的公开源坐标；不把G参考筛查列传成F原生轨迹。"""
    out = frame.loc[:, list(SELECTED_COLUMNS)].copy()
    require(out['round'].isin(['value1', 'value2']).all(), '未知ScaleTurn轮次')
    for c in ('source_row', 'actual', 'confirmation', 'known', 'raw_known'):
        require(pd.api.types.is_integer_dtype(out[c]) and not out[c].isna().any(),
                '上游整数坐标类型改变：' + c)
    out['round_display'] = out['round'].map({'value1': 0, 'value2': 1}).astype('int64')
    out['turn_id_role'] = 'D008公开上游简化定位键；不是native exact UUID'
    out['source_role'] = '同实例已接受公开投影；几何C与原事件selected-known分离'
    return out


def check_result_identity(instance):
    binding = load('inputs/FeatureRunResultBinding.json')
    require(isinstance(instance, CommonPriceTurnGroupCandidatesFrp), '真实Feature类型不符')
    require(str(instance.full_dir) == binding['result_identity']['full_dir'], '准确结果身份改变')
    fields = Path(instance.full_dir) / 'fields.json'
    require(fields.is_file() and digest(fields) == binding['result_identity']['fields_sha256'],
            '准确实例fields缺失或漂移；不得重算')
    return binding


def read_bound_frames(instance, position):
    """E构图时调用。F走正式只读API，上游走已验收物化入口。"""
    binding = check_result_identity(instance)
    require(position['symbols'] == binding['data_scope']['symbols'] and
            position['calendar'] == binding['data_scope']['calendar'], 'reader位置绑定不符')
    instance.run(CalType.OnlyRead)
    frames = instance.to_dfs()
    expected = {x['name']: x for x in binding['run_result_tables']}
    require(set(frames) == set(expected), '原生公开表集合改变')
    for name, frame in frames.items():
        spec = expected[name]
        require(list(frame.columns) == spec['columns'] and
                list(frame.index.names) == spec['index_names'] and len(frame) == spec['rows'],
                '准确原生表结构/数量改变：' + name)
    groups = adapt_window_axes(frames['occurrences'])
    children = {k: v for k, v in frames.items() if k.startswith('occurrences_')}
    non_groups = {k: dict(index_names=list(v.index.names), columns=list(v.columns),
                         rows=raw_records(v.reset_index()))
                  for k, v in frames.items() if k != 'occurrences' and not k.startswith('occurrences_')}
    sources = load('SOURCE_DATA_BINDING.json')['source_files']
    for source in sources:
        require(digest(source['path']) == source['sha256'], '已接受上游物化源漂移：' + source['path'])
    klines, raw = {}, {}
    for symbol in position['symbols']:
        for kind, target in [('kline', klines), ('rct', raw)]:
            entry = next(s for s in sources if s.get('symbol') == symbol and s['kind'] == kind)
            frame = pd.read_csv(entry['path'], parse_dates=['timestamp'], encoding='utf-8-sig')
            require(list(frame.columns) == ['timestamp', *entry['columns']], '上游列改变')
            require(len(frame) == entry['rows'], '上游行数改变')
            target[symbol] = frame.set_index('timestamp') if kind == 'kline' else frame
    canonical = next(s for s in sources if s['kind'] == 'accepted_canonical_selected')
    selected_all = adapt_selected(pd.read_csv(canonical['path'], encoding='utf-8-sig'))
    selected = {}
    for symbol in position['symbols']:
        frame = selected_all.loc[selected_all.symbol == symbol].copy()
        # 用原事件timestamp在同一原KLine轴上的closeUti核对，不借几何C推断known。
        kt = klines[symbol]['closeUti']
        expected_known = kt.reindex(pd.DatetimeIndex(pd.to_datetime(frame.known_ts))).to_numpy()
        require(np.array_equal(expected_known, frame.known.to_numpy()), '上游selected-known与原事件轴不符')
        selected[symbol] = frame
    metadata = dict(definition=DEFINITION_ID, native_feature=binding['feature_name'],
                    feature_result_dir=binding['result_identity']['full_dir'],
                    fields_sha256=binding['result_identity']['fields_sha256'],
                    configuration_sha256=CONFIG_HASH, frp=FRP, tis=TIS, uplot=UPLOT,
                    feature_binding_ref=load('SOURCE_DATA_BINDING.json')['feature_binding_ref'],
                    understanding_ref=load('inputs/C2_CURRENT_EXPECTATION.json')['FeatureUnderstandingPackage引用'],
                    understanding_status='PARTIAL', non_group_tables=non_groups,
                    field_binding_ref='FIELD_BINDING.json', upstream_binding_ref='SOURCE_DATA_BINDING.json',
                    selected_identity_role='turn_id仅为公开源定位键；native member exact在各组原始children中',
                    selected_omitted_reference_columns='G的eligible_*_reference/first_block_screen及其他分析派生不冒充原生F轨迹',
                    native_window_columns='原float64不改；__uti_*只为经核实无损整数表示',
                    temporal_view='HISTORICAL_POSITION_PROJECTION_NOT_ASOF')
    return dict(klines=klines, selected=selected, raw=raw, groups=groups,
                children=children, metadata=metadata)


def build_bound_display():
    """E的直接入口；返回layout及含真实PlotData roots的meta，不宣告验收。"""
    require(digest(ROOT / 'definition/caegraph_display.py') == C3_HASH, 'C3源码漂移')
    with bound_environment():
        instance = construct_instance()
        context = OptContext(**sof_parameters())
        position, explanation = resolve_position(context)
        fields = load('FIELD_BINDING.json')
        caption = ('真实F800历史位置投影；rb/hc/i · 5m · 请求2021-01-01—2023-12-31；'
                   'SOF TA_updto20240229_DBA / steel / night_end_at_2300；'
                   'FRP39f / TIS2f；沿用C2-v4展示语义。'
                   '原生F与已接受公开上游均只读；U仍PARTIAL。')
        layout, meta = build_display(instance=instance, reader=read_bound_frames,
                                     context=context, position=position, fields=fields, caption=caption)
        meta.update(instance=instance, instance_full_dir=str(instance.full_dir),
                    position=position, boundary=explanation,
                    definition=DEFINITION_ID, source_binding=load('SOURCE_DATA_BINDING.json'))
        return layout, meta
