__all__ = [
    "DbaStore",
    "DbaStruct",
]

from collections import *

import numpy as np
from numba import njit

from .rt import *


def _load_Text(pa, aa, vin: int):
    i_next = aa[vin]
    i_start = aa[vin - 1] if vin > 0 else 0
    if i_next <= i_start:
        return ""
    bs = pa[i_start:i_next].tobytes()
    return bs.decode("utf-8")


class DbaStore:

    def __init__(self, root_dir: str, root_struct: type):
        self.root_dir = root_dir
        self.seq_reg = {}
        self.root_seq = self.arm_seq("", root_struct)

        try:
            self.Text_payload = DbArray(root_dir, "Text$Data.Text/payload", byte)
            self.Text_anchor = DbArray(root_dir, "Text$Data.Text/anchor", intp)
        except:
            pass

        try:
            self.TextList_payload = DbArray(root_dir, "[Text]$Data.Text/payload", byte)
            self.TextList_anchor = DbArray(root_dir, "[Text]$Data.Text/anchor", intp)
            self.TextList_anchor1 = DbArray(root_dir, "[Text]$Data.Text/anchor1", intp)
        except:
            pass

    def load_Text(self, vin: int):
        return _load_Text(self.Text_payload.ndarray, self.Text_anchor.ndarray, vin)

    def load_TextList(self, vin: int):
        a1a = self.TextList_anchor1.ndarray
        i_next = a1a[vin]
        i_start = a1a[vin - 1] if vin > 0 else 0
        if i_next <= i_start:
            return []
        pa = self.TextList_payload.ndarray
        aa = self.TextList_anchor.ndarray
        return [_load_Text(pa, aa, i) for i in range(i_start, i_next)]

    def __repr__(self) -> str:
        return f"DbaStore({self.root_dir!r}, {type(self.root_seq)!r})"

    def __len__(self):
        return self.root_seq.count()

    def __iter__(self):
        return iter(self.root_seq)

    def arm_seq(self, sp: str, struct: type):
        adt_seq = self.seq_reg.get(sp, None)
        if adt_seq:
            return adt_seq
        adt_seq = struct()
        try:
            adt_seq.__store__ = self
            adt_seq.__arm_store__(self, sp)
        except FileNotFoundError as e:
            print(f"FileNotFoundError: {e}")
            adt_seq = EmptyDbaStruct()
        self.seq_reg[sp] = adt_seq
        return adt_seq

    def __getitem__(self, k: str):
        return self.root_seq[k]

    def get(self, k: str, default):
        try:
            return self.__getitem__(k)
        except KeyError:
            return default


class DbaStruct:

    __slots__ = ("__store__",)

    __adt__ = namedtuple("Void", [])

    def __arm_store__(self, store: DbaStore, sp: str):
        pass

    def count(self) -> int:
        raise NotImplementedError

    def load(self, vin: int) -> __adt__:
        raise NotImplementedError

    def __len__(self):
        return self.count()

    def __iter__(self):
        for vin in range(self.count()):
            yield self.load(vin)

    def __repr__(self) -> str:
        adt = self.__adt__
        try:
            if adt.__origin__ is list:
                edt = adt.__args__[0]
                return "SeqOf[" + edt.__doc__ + "]"
        except AttributeError:
            pass
        return adt.__doc__

    def __getitem__(self, k: str):
        return _VecFieldGetter(self)[k]


@njit(nogil=True)
def _varlenseq_idxs(aa, in_idxs, in_ridxs):
    assert in_idxs.ndim == in_ridxs.ndim - 1 == 1
    assert in_idxs.shape == in_ridxs.shape[1:]

    cap = in_idxs.size * 5
    idxs = np.empty(cap, np.intp)
    ridxs = np.empty((in_ridxs.shape[0] + 1, cap), np.intp)
    cnt = 0
    for ii in range(in_idxs.size):
        ai = in_idxs[ii]
        i_end = aa[ai]
        i_start = 0 if ai < 1 else aa[ai - 1]

        if cnt + i_end - i_start > cap:
            cap = int(cap * 1.5)
            old_idxs, old_ridxs = idxs, ridxs
            idxs = np.empty(cap, np.intp)
            ridxs = np.empty((in_ridxs.shape[0] + 1, cap), np.intp)
            idxs[:cnt] = old_idxs[:cnt]
            ridxs[:, :cnt] = old_ridxs[:, :cnt]
            old_idxs, old_ridxs = None, None

        for i in range(i_start, i_end):
            idxs[cnt] = i
            ridxs[-1, cnt] = i - i_start
            ridxs[:-1, cnt] = in_ridxs[:, ii]
            cnt += 1

    return idxs[:cnt].copy(), ridxs[:, :cnt].copy()


class _VecFieldGetter:
    __slots__ = ("seq", "idxs", "ridxs")

    def __init__(self, seq, idxs=None, ridxs=None):
        self.seq = seq
        self.idxs = idxs
        if ridxs is not None:
            assert idxs is not None and ridxs.shape[1:] == idxs.shape
            self.ridxs = ridxs
        else:
            ridxs = np.arange(seq.count())
            if idxs is None:
                self.ridxs = ridxs[np.newaxis, :]
            else:
                assert idxs.ndim == 1
                self.ridxs = ridxs[np.newaxis, idxs]

    def __repr__(self) -> str:
        return repr(self.seq) + "[???]"

    def __getitem__(self, k: str):
        assert isinstance(k, str)

        seq = self.seq
        try:
            va = getattr(seq, k)
        except AttributeError:
            raise KeyError(k)
        iva = va.ndarray if self.idxs is None else va.ndarray[self.idxs]

        if va.dtype != intp:
            # got a bits / final field
            return iva

        # still got a struct / indirect field
        try:
            outer_seq = getattr(seq, k + "_seq")
        except AttributeError:
            raise KeyError(k)
        try:
            aa = outer_seq.__anchor__
            # `outer_seq` is a SeqOf (i.e. variable length list) sequence
            idxs, ridxs = _varlenseq_idxs(aa.ndarray, iva, self.ridxs)
            return _VecFieldGetter(outer_seq, idxs, ridxs)
        except AttributeError:
            pass

        # got a plain indirect field
        return _VecFieldGetter(outer_seq, iva, self.ridxs)

    def get(self, k: str, default):
        try:
            return self.__getitem__(k)
        except KeyError:
            return default


class EmptyDbaStruct(DbaStruct):

    def count(self) -> int:
        return 0

    def load(self, vin: int):
        raise IndexError(f"vin={vin!r} on empty seq")
