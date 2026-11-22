"""
Plot Data Tree

"""

__all__ = [
    "PlotDataFolder",
    "PlotDataNode",
]

from typing import *
import traceback

from bokeh.models import ColumnDataSource


class PlotDataFolder:
    __slots__ = "name", "children"

    def __init__(self, name: str):
        self.name = name
        self.children = []

    def __len__(self):
        return len(self.children)

    def __repr__(self):
        return f"{self.name!s} /w {len(self.children)} children"

    def __getitem__(self, k):
        return self.children[k]

    def ndatapoints(self):
        return sum(c.ndatapoints() for c in self.children)

    def time_cost(self, full_dd=None, path=()):
        key = tuple((*path, self.name))
        data_fetch_time, data_trans_time = 0.0, 0.0
        for cnode in self.children:
            dd = cnode.time_cost(full_dd, key)
            data_fetch_time += dd["data_fetch_time"]
            data_trans_time += dd["data_trans_time"]
        sum_dd = {
            "data_fetch_time": data_fetch_time,
            "data_trans_time": data_trans_time,
        }
        if full_dd is not None:
            full_dd[key] = sum_dd
        return sum_dd

    def print(self, expr: str, indent: str = "", indent_step="  ", file=None):
        import sys

        real_file = file or sys.stdout

        print(f"{indent!s}{self.name}", file=real_file)

        cindent = indent + indent_step
        for i, child in enumerate(self.children):
            child.print(f"{expr}[{i}]", cindent, indent_step, file=file)


class PlotDataNode:
    __slots__ = "name", "cds", "data_fetch_time", "data_trans_time"

    def __init__(
        self, name: str, cds: ColumnDataSource, data_fetch_time, data_trans_time
    ):
        self.name = name
        self.cds = cds
        self.data_fetch_time = data_fetch_time
        self.data_trans_time = data_trans_time

    def data_shape(self):
        dlen = 0
        for d in self.cds.data.values():
            dlen = len(d)
            break
        cols = [str(n) for n in self.cds.data.keys()]
        return dlen, cols

    def ndatapoints(self):
        dlen = 0
        for d in self.cds.data.values():
            dlen = len(d)
            break
        return dlen * len(self.cds.data)

    def __repr__(self):
        dlen, cols = self.data_shape()
        return f"{self.name!s} /w {dlen} data points of columns: {','.join(cols)}"

    def __getitem__(self, k):
        return self.children[k]

    def time_cost(self, full_dd=None, path=()):
        dd = {
            "data_fetch_time": self.data_fetch_time,
            "data_trans_time": self.data_trans_time,
        }
        if full_dd is not None:
            key = tuple((*path, self.name))
            full_dd[key] = dd
        return dd

    def print(self, expr: str, indent: str = "", indent_step="  ", file=None):
        import sys

        real_file = file or sys.stdout

        dlen, cols = self.data_shape()

        print(f"{indent!s}{self.name} w/ {dlen} data points", file=real_file)
        if cols:
            print(f"{indent!s}-- data columns: {cols}", file=real_file)
        if dlen > 0:
            print(
                f"{indent!s}-- data frame: pd.DataFrame({expr}.cds.data)",
                file=real_file,
            )
