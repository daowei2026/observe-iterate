"""把外部固定 CSV 暴露为只读 Feature；沿用 aidata 原生图、窗口与切片。

alias 是可读名称，真实 Fao 身份还包含来源 SHA、成员、过滤和字段配置。
本模块只读取原结果，不计算业务指标；绘图类型转换另列保存。
"""

from __future__ import annotations

import hashlib
import io
import zipfile
from decimal import Decimal
from pathlib import Path

import pandas as pd

from mquant.frame import BaseSymbolDFFao
from mquant.frame.lib3 import CurrSymbol

_PARAM_NAMES = ('alias', 'path', 'member', 'sha256', 'symbol_field', 'index_field',
                'equals', 'numeric_columns', 'integer_columns')


def read_csv_result(params, symbol: str) -> pd.DataFrame:
    """验证原件，保留字面值/物理行号，再按明确配置提供类型化视图。"""
    path = Path(params['path'])
    member = params.get('member') or ''
    if member:
        with zipfile.ZipFile(path) as archive:
            payload = archive.read(member)
    else:
        payload = path.read_bytes()
    digest = hashlib.sha256(payload).hexdigest()
    if not params.get('sha256') or digest != params['sha256']:
        raise ValueError('CSV 成员 SHA-256 与锁定来源不一致')
    frame = pd.read_csv(io.BytesIO(payload), dtype=str, keep_default_na=False,
                        encoding='utf-8-sig')
    if any(str(c).startswith('_csv_') for c in frame.columns):
        raise ValueError('原 CSV 使用了保留的 _csv_ 列名前缀')
    frame['_csv_source_row'] = range(2, len(frame) + 2)
    frame['_csv_source_sha256'] = digest
    frame['_csv_source_member'] = member or path.name
    frame['_csv_alias'] = params['alias']
    symbol_field = params.get('symbol_field') or ''
    if symbol_field:
        if not symbol:
            raise ValueError('单品种 CSV Feature 缺少当前品种')
        frame = frame.loc[frame[symbol_field] == symbol].copy()
    for field, value in (params.get('equals') or {}).items():
        frame = frame.loc[frame[field] == str(value)].copy()
    for target, source in (params.get('numeric_columns') or {}).items():
        if not target.startswith('_csv_'):
            raise ValueError('类型化视图列必须使用 _csv_ 前缀，不能覆盖原字段')
        frame[target] = pd.to_numeric(frame[source].replace('', float('nan')), errors='raise')
    for target, source in (params.get('integer_columns') or {}).items():
        if not target.startswith('_csv_'):
            raise ValueError('类型化视图列必须使用 _csv_ 前缀，不能覆盖原字段')
        def exact_integer(value):
            number = Decimal(value)
            if not number.is_finite() or number != number.to_integral_value():
                raise ValueError(f'UTI 必须是精确整数，不能截断: {value}')
            return int(number)
        frame[target] = frame[source].map(exact_integer).astype('int64')
    if params.get('index_field'):
        frame.index = pd.DatetimeIndex(pd.to_datetime(frame[params['index_field']], errors='raise'),
                                       name='_csv_time')
    return frame


class ReadOnlyCsvFeature(BaseSymbolDFFao):
    """单品种只读 CSV Feature；同一类由 alias/来源参数区分不同固定结果。"""

    params = lambda: {
        'alias': '',
        'path': '',
        'member': '',
        'sha256': '',
        'symbol_field': 'symbol',
        'index_field': '',
        'equals': {},
        'numeric_columns': {},
        'integer_columns': {},
        'display_config_json': '',
    }

    def run(self, cal_type=None, clear=False):
        """固定结果不走框架的计算/落盘缓存；每次 to_df 都验证当前原件。"""
        return self

    def rerun(self, cal_type=None):
        return self.run(cal_type, clear=True)

    def to_df(self):
        values = {key: getattr(self.P, key) for key in _PARAM_NAMES}
        if not values['alias']:
            raise ValueError('只读 CSV Feature 必须提供可读 alias')
        return read_csv_result(values, str(CurrSymbol.sym(False) or ''))

    def to_dfs(self):
        return {'value': self.to_df()}

    def _impl(self):
        return {'value': self.to_df()}


# 持久参数名称在每个新进程导入时加载；沿用 Fao 原生具名参数机制。
from .csv_feature_catalog import load_named_csv_features
load_named_csv_features()
