"""读取随包的真实输入；不访问原 Aidata run 或原始行情/特征目录。"""
from pathlib import Path
from types import SimpleNamespace
import json
import csv
import os
import numpy as np
import pandas as pd
from m3tt import CurrSymbol
from mquant.frame import DataFrameMixIn, GeneralSymbolFao
from mquant.quant import OptContext


_BUNDLES = {}
DEFAULT_ROOT = Path(os.environ.get('CAEGRAPH_DATA_ROOT', str(Path(__file__).resolve().parent))).resolve()


class SnapshotBundle:
    def __init__(self, root):
        self.root = Path(root).resolve()
        self.manifest = json.loads((self.root / 'data/manifest.json').read_text())
        self.frames = {}
        self._calendar = None
        with (self.root / 'data/included_tick_nodes.csv').open() as source:
            self._tick_windows = {(int(r['start_uti']), int(r['end_uti'])): r['node_id']
                                  for r in csv.DictReader(source)}
        self.blkset = SimpleNamespace(symbols=lambda _name: self.manifest['symbols'])
        self.name = 'steel_frozen_sample'
        self.stk_tlist = 'rb|hc|i'

    def frame(self, key):
        if key not in self.frames:
            spec = self.manifest['assets'][key]
            dtypes = {column: dtype for column, dtype in spec['dtypes'].items()
                      if dtype != 'object' and not dtype.startswith('datetime64')}
            frame = pd.read_csv(self.root / 'data' / spec['file'], index_col=0,
                                dtype=dtypes, float_precision='round_trip')
            if spec['datetime_index']:
                frame.index = pd.to_datetime(frame.index)
                frame.index.name = None
            for column, dtype in spec['dtypes'].items():
                if dtype.startswith('datetime64'):
                    frame[column] = pd.to_datetime(frame[column])
                elif dtype == 'object':
                    # object 列也可能存 Python 数值；保持可比较的 UTI 数值。
                    frame[column] = frame[column].astype(object)
            self.frames[key] = frame
        return self.frames[key]

    def tsa_of(self, name):
        if name != self.manifest['calendar_name']:
            raise KeyError(name)
        if self._calendar is None:
            data = np.load(self.root / 'data/calendar.npz')
            starts, timestamps, size = data['starts'], data['timestamps'], int(data['size'])
            # 原生 uplot 使用连续 UTI 数组；文件仅保存连续半秒段，展开值与原数组一致。
            calendar = np.empty(size, dtype='int64')
            ends = np.r_[starts[1:], size]
            for start, end, timestamp in zip(starts, ends, timestamps):
                for left in range(int(start), int(end), 1_000_000):
                    right = min(int(end), left + 1_000_000)
                    calendar[left:right] = timestamp + np.arange(left-start, right-start, dtype='int64') * 500_000_000
            self._calendar = calendar.view('datetime64[ns]')
        return {'natural_tsa': self._calendar}

    def load_iset(self, name):
        return SimpleNamespace(symbols=self.manifest['symbols'])

    def read_symbol_window(self, symbol, start_uti, end_uti):
        node_id = self._tick_windows.get((int(start_uti), int(end_uti)))
        if node_id is None:
            raise ValueError('该 Tick 区间未包含在数据包中，请查看 included_tick_nodes.csv')
        frame = self.frame(f'tick/{node_id}/{symbol}').copy()
        frame = frame.loc[frame.uti.between(start_uti, end_uti)].copy()
        if frame.empty:
            raise ValueError(f'{node_id}/{symbol} 的 Tick 行情为空')
        frame.attrs['resolved_start_uti'] = int(frame.uti.iloc[0])
        return SimpleNamespace(df=frame, resolved_start_uti=int(frame.uti.iloc[0]), warnings=[])


def bundle(root=None):
    root = str(Path(root or DEFAULT_ROOT).resolve())
    if root not in _BUNDLES:
        _BUNDLES[root] = SnapshotBundle(root)
    return _BUNDLES[root]


class SnapshotContext(OptContext):
    params = lambda: {'bundle_dir': str(DEFAULT_ROOT)}

    @property
    def sof(self):
        return bundle(self.P.bundle_dir)


class SnapshotFeature(DataFrameMixIn, GeneralSymbolFao):
    """供原生 KPriceLine/VBarPlot/事件 Plotter 读取包内 DataFrame。"""
    params = lambda: dict(kind='kline', freq='1d', source_key='',
                         df_key='__default__', bundle_dir=str(DEFAULT_ROOT), window_scope='')

    def rerun(self, *args, **kwargs):
        return self

    def to_df(self):
        data = bundle(self.P.bundle_dir)
        if self.P.kind == 'open_segments':
            key = 'open_segments'
        elif self.P.kind == 'kline':
            key = f'kline/{CurrSymbol.sym()}/{self.P.freq}'
        else:
            key = f'evidence/{self.P.source_key}/{CurrSymbol.sym()}/{self.P.df_key}'
        return data.frame(key)

    def to_dfs(self):
        return {self.P.df_key: self.to_df()}

    def evidence_view_df(self, key=None, **kwargs):
        return self.to_df()

    def window_snapshot(self, start_uti, end_uti):
        data = bundle(self.P.bundle_dir)
        key = (f'window_evidence/{self.P.window_scope}/{self.P.source_key}/{CurrSymbol.sym()}/'
               f'{self.P.df_key}/{int(start_uti)}-{int(end_uti)}')
        return data.frame(key) if key in data.manifest['assets'] else None
