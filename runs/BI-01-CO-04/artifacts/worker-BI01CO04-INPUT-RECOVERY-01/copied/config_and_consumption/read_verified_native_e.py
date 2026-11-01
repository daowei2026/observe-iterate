"""Read original authoritative E-native Int/Double ScaleTurnCalendar events.

The original E generated ADT reader is loaded without importing the entire E
feature runtime. Coordinates remain int64; prices remain float64. No feature
generation, coordinate conversion, fallback, or store creation is performed.
"""
import importlib.util
import inspect
import json
import mmap
import pathlib
import hashlib

DEFAULT_ROOT = '/m3varF/BaseData/futures/GTQH_L1_20210104_20240208/fao/prod/ScaleTurnCalendar/c/f/6/6/7/d/5/25b8f5f784d6fdb13ed3c8235e71cb069'
ORIGINAL_E_ADT = '/m3varK/workspace/mquant_e6.2_prod/mquant/worker/adt/dbaw.py'
ORIGINAL_E_ADT_SHA256 = 'f6406f2a3ecc74d948fad179c2b9e29550097c2b4f0f292665f4c5c3bf358286'


def load_verified_native_e(symbol, cache_root=DEFAULT_ROOT, adt_source=ORIGINAL_E_ADT):
    import numpy as np
    import pandas as pd
    from pydim.dim import DbArray, DbaStore

    if symbol not in ['m', 'rb', 'hc', 'i']:
        raise ValueError('This verified E cache contains m/rb/hc/i only')
    if inspect.signature(DbArray).parameters['access'].default != mmap.ACCESS_READ:
        raise RuntimeError('The original ADT reader requires read-only DbArray defaults')
    if np.dtype(np.intp).itemsize != 8:
        raise RuntimeError('This native cache requires 64-bit anchors')
    adt_path = pathlib.Path(adt_source)
    if hashlib.sha256(adt_path.read_bytes()).hexdigest() != ORIGINAL_E_ADT_SHA256:
        raise RuntimeError('Use the verified original E ADT definition')
    directory = pathlib.Path(cache_root) / symbol
    schema = json.loads((directory / 'fields.json').read_text())
    if schema != {'value1': 'adt@CompleteScaleTurn2D', 'value2': 'adt@CompleteScaleTurn2D'}:
        raise ValueError('Unexpected original E feature schema')
    spec = importlib.util.spec_from_file_location('verified_original_e_adt', str(adt_path))
    native = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(native)
    result = {}
    for field in ['value1', 'value2']:
        root = directory / field
        required = [root / 'type', root / 'confirm2D::Point2Dif Int Double.dba',
                    root / 'actual2D::Point2Dif Int Double.dba',
                    root / 'Point2Dif Int Double/x::Int.dba',
                    root / 'Point2Dif Int Double/y::Double.dba',
                    directory / (field + '.__ts__.dba')]
        for path in required:
            if not path.is_file():
                raise FileNotFoundError(str(path))
        if (root / 'type').read_text().strip() != 'CompleteScaleTurn2D':
            raise ValueError('Unexpected native root type')
        store = DbaStore(str(root), native.CompleteScaleTurn2D)
        seq = store.root_seq
        axis = DbArray(str(directory), field + '.__ts__', 'M8[ns]', access=mmap.ACCESS_READ)
        count = int(seq.count())
        if count <= 0 or count != int(axis.len1d):
            raise ValueError('Original E ADT/axis is empty or has different lengths')
        data = {'x': np.asarray(seq['actual2D']['x']).copy(),
                'y': np.asarray(seq['actual2D']['y']).copy(),
                'xConfirm': np.asarray(seq['confirm2D']['x']).copy(),
                'yConfirm': np.asarray(seq['confirm2D']['y']).copy()}
        expected_types = {'x': np.dtype('i8'), 'xConfirm': np.dtype('i8'),
                          'y': np.dtype('f8'), 'yConfirm': np.dtype('f8')}
        if any(v.dtype != expected_types[k] or len(v) != count for k, v in data.items()):
            raise ValueError('Unexpected original Int/Double payload type or length')
        frame = pd.DataFrame(data, index=axis.ndarray.copy())
        frame.index.name = 'event_ts'
        result[field] = frame
    return result
