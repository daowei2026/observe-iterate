__all__ = [
  "HPValue", 
  "SeqOf_HPValue", 
  "MapEntry_Text_Double", 
  "SeqOf_MapEntry_Text_Double", 
  "LastSwing", 
  "SeqOf_LastSwing", 
  "ConfirmPoint_ThickSegPoint_ThickSegPoint", 
  "SeqOf_ConfirmPoint_ThickSegPoint_ThickSegPoint", 
  "Envelope2D_Double", 
  "SeqOf_Envelope2D_Double", 
  "MACDOcc", 
  "SeqOf_MACDOcc", 
  "Point2D__Double_Double", 
  "SeqOf_Point2D__Double_Double", 
  "ConfirmPoint__CoreExtra_BscOcc__MapEntry_Text_Double___BscOcc", 
  "SeqOf_ConfirmPoint__CoreExtra_BscOcc__MapEntry_Text_Double___BscOcc", 
  "ThickSegPoint", 
  "SeqOf_ThickSegPoint", 
  "BarSwing", 
  "SeqOf_BarSwing", 
  "Line2D_Double", 
  "SeqOf_Line2D_Double", 
  "XBox_Double_Double", 
  "SeqOf_XBox_Double_Double", 
  "ZigZagOcc", 
  "SeqOf_ZigZagOcc", 
  "Point2D_Double", 
  "SeqOf_Point2D_Double", 
  "CompleteScaleTurn2D", 
  "SeqOf_CompleteScaleTurn2D", 
  "CoreExtra_BscOcc__MapEntry_Text_Double_", 
  "SeqOf_CoreExtra_BscOcc__MapEntry_Text_Double_", 
  "ThickEnd", 
  "SeqOf_ThickEnd", 
  "XBox2Eval_Double_Double_Double", 
  "SeqOf_XBox2Eval_Double_Double_Double", 
  "Point2Dif_Int_Double", 
  "SeqOf_Point2Dif_Int_Double", 
  "ConfirmPoint__BscOccWithStrength__BscOcc", 
  "SeqOf_ConfirmPoint__BscOccWithStrength__BscOcc", 
  "XBox2EvalWrap_Double_Double_Double", 
  "SeqOf_XBox2EvalWrap_Double_Double_Double", 
  "ZigWithStatusOcc", 
  "SeqOf_ZigWithStatusOcc", 
  "XSimpleSymmetry", 
  "SeqOf_XSimpleSymmetry", 
  "BscOccWithStrength", 
  "SeqOf_BscOccWithStrength", 
  "BscOcc", 
  "SeqOf_BscOcc", 
  "Vector2D_Double", 
  "SeqOf_Vector2D_Double", 
]

import os.path
from collections import *
from pydim.dim import *

class HPValue(DbaStruct):
  __adt__ = namedtuple("HPValue", [ "hpValue", "nthHigh", "nthLow", "atrValue", ])

  def __arm_store__(self, store: DbaStore, sp: str):
    self.hpValue = DbArray(store.root_dir, os.path.join(sp, "hpValue::Double"), f8)
    self.nthHigh = DbArray(store.root_dir, os.path.join(sp, "nthHigh::Double"), f8)
    self.nthLow = DbArray(store.root_dir, os.path.join(sp, "nthLow::Double"), f8)
    self.atrValue = DbArray(store.root_dir, os.path.join(sp, "atrValue::Double"), f8)

  def count(self) -> int:
    return self.hpValue.len1d

  def load(self, vin: int) -> __adt__:
    return self.__adt__(
      hpValue = self.hpValue.ndarray[vin],
      nthHigh = self.nthHigh.ndarray[vin],
      nthLow = self.nthLow.ndarray[vin],
      atrValue = self.atrValue.ndarray[vin],
    )

class SeqOf_HPValue(DbaStruct):
  __adt__ = list[HPValue.__adt__]

  def __arm_store__(self, store: DbaStore, sp: str):
    self.__anchor__ = DbArray(store.root_dir, f"{sp}/anchor", intp)
    self.hpValue = DbArray(store.root_dir, os.path.join(sp, "hpValue::Double"), f8)
    self.nthHigh = DbArray(store.root_dir, os.path.join(sp, "nthHigh::Double"), f8)
    self.nthLow = DbArray(store.root_dir, os.path.join(sp, "nthLow::Double"), f8)
    self.atrValue = DbArray(store.root_dir, os.path.join(sp, "atrValue::Double"), f8)

  def count(self) -> int:
    return self.__anchor__.len1d

  def load(self, vin: int) -> __adt__:
    aa = self.__anchor__.ndarray
    i_next = aa[vin]
    i_start = aa[vin - 1] if vin > 0 else 0
    if i_next <= i_start:
        return []
    return [
        HPValue.__adt__(
            hpValue = hpValue,
            nthHigh = nthHigh,
            nthLow = nthLow,
            atrValue = atrValue,
        ) for (
            hpValue,
            nthHigh,
            nthLow,
            atrValue,
        ) in zip(
            self.hpValue.ndarray[i_start:i_next],
            self.nthHigh.ndarray[i_start:i_next],
            self.nthLow.ndarray[i_start:i_next],
            self.atrValue.ndarray[i_start:i_next],
        )
    ]

class MapEntry_Text_Double(DbaStruct):
  __adt__ = namedtuple("MapEntry_Text_Double", [ "meValue", "meKey", ])

  def __arm_store__(self, store: DbaStore, sp: str):
    self.meValue = DbArray(store.root_dir, os.path.join(sp, "meValue::Double"), f8)
    self.meKey = DbArray(store.root_dir, os.path.join(sp, "meKey::Text$Data.Text"), intp)

  def count(self) -> int:
    return self.meValue.len1d

  def load(self, vin: int) -> __adt__:
    return self.__adt__(
      meValue = self.meValue.ndarray[vin],
      meKey = self.__store__.load_Text(self.meKey.ndarray[vin]),
    )

class SeqOf_MapEntry_Text_Double(DbaStruct):
  __adt__ = list[MapEntry_Text_Double.__adt__]

  def __arm_store__(self, store: DbaStore, sp: str):
    self.__anchor__ = DbArray(store.root_dir, f"{sp}/anchor", intp)
    self.meValue = DbArray(store.root_dir, os.path.join(sp, "meValue::Double"), f8)
    self.meKey = DbArray(store.root_dir, os.path.join(sp, "meKey::Text$Data.Text"), intp)

  def count(self) -> int:
    return self.__anchor__.len1d

  def load(self, vin: int) -> __adt__:
    aa = self.__anchor__.ndarray
    i_next = aa[vin]
    i_start = aa[vin - 1] if vin > 0 else 0
    if i_next <= i_start:
        return []
    return [
        MapEntry_Text_Double.__adt__(
            meValue = meValue,
            meKey = meKey,
        ) for (
            meValue,
            meKey,
        ) in zip(
            self.meValue.ndarray[i_start:i_next],
            (self.__store__.load_Text(tvin) for tvin in
             self.meKey.ndarray[i_start:i_next]),
        )
    ]

class LastSwing(DbaStruct):
  __adt__ = namedtuple("LastSwing", [ "lsPrice", "lsPosUTI", "lsDirection", ])

  def __arm_store__(self, store: DbaStore, sp: str):
    self.lsPrice = DbArray(store.root_dir, os.path.join(sp, "lsPrice::Double"), f8)
    self.lsPosUTI = DbArray(store.root_dir, os.path.join(sp, "lsPosUTI::Double"), f8)
    self.lsDirection = DbArray(store.root_dir, os.path.join(sp, "lsDirection::Double"), f8)

  def count(self) -> int:
    return self.lsPrice.len1d

  def load(self, vin: int) -> __adt__:
    return self.__adt__(
      lsPrice = self.lsPrice.ndarray[vin],
      lsPosUTI = self.lsPosUTI.ndarray[vin],
      lsDirection = self.lsDirection.ndarray[vin],
    )

class SeqOf_LastSwing(DbaStruct):
  __adt__ = list[LastSwing.__adt__]

  def __arm_store__(self, store: DbaStore, sp: str):
    self.__anchor__ = DbArray(store.root_dir, f"{sp}/anchor", intp)
    self.lsPrice = DbArray(store.root_dir, os.path.join(sp, "lsPrice::Double"), f8)
    self.lsPosUTI = DbArray(store.root_dir, os.path.join(sp, "lsPosUTI::Double"), f8)
    self.lsDirection = DbArray(store.root_dir, os.path.join(sp, "lsDirection::Double"), f8)

  def count(self) -> int:
    return self.__anchor__.len1d

  def load(self, vin: int) -> __adt__:
    aa = self.__anchor__.ndarray
    i_next = aa[vin]
    i_start = aa[vin - 1] if vin > 0 else 0
    if i_next <= i_start:
        return []
    return [
        LastSwing.__adt__(
            lsPrice = lsPrice,
            lsPosUTI = lsPosUTI,
            lsDirection = lsDirection,
        ) for (
            lsPrice,
            lsPosUTI,
            lsDirection,
        ) in zip(
            self.lsPrice.ndarray[i_start:i_next],
            self.lsPosUTI.ndarray[i_start:i_next],
            self.lsDirection.ndarray[i_start:i_next],
        )
    ]

class ConfirmPoint_ThickSegPoint_ThickSegPoint(DbaStruct):
  __adt__ = namedtuple("ConfirmPoint_ThickSegPoint_ThickSegPoint", [ "actual", "confirm", ])

  def __arm_store__(self, store: DbaStore, sp: str):
    self.actual = DbArray(store.root_dir, os.path.join(sp, "_actual::ThickSegPoint"), intp)
    self.actual_seq = store.arm_seq("ThickSegPoint", ThickSegPoint)
    self.confirm = DbArray(store.root_dir, os.path.join(sp, "_confirm::ThickSegPoint"), intp)
    self.confirm_seq = store.arm_seq("ThickSegPoint", ThickSegPoint)

  def count(self) -> int:
    return self.actual.len1d

  def load(self, vin: int) -> __adt__:
    return self.__adt__(
      actual = self.actual_seq.load(self.actual.ndarray[vin]),
      confirm = self.confirm_seq.load(self.confirm.ndarray[vin]),
    )

class SeqOf_ConfirmPoint_ThickSegPoint_ThickSegPoint(DbaStruct):
  __adt__ = list[ConfirmPoint_ThickSegPoint_ThickSegPoint.__adt__]

  def __arm_store__(self, store: DbaStore, sp: str):
    self.__anchor__ = DbArray(store.root_dir, f"{sp}/anchor", intp)
    self.actual = DbArray(store.root_dir, os.path.join(sp, "_actual::ThickSegPoint"), intp)
    self.actual_seq = store.arm_seq("ThickSegPoint", ThickSegPoint)
    self.confirm = DbArray(store.root_dir, os.path.join(sp, "_confirm::ThickSegPoint"), intp)
    self.confirm_seq = store.arm_seq("ThickSegPoint", ThickSegPoint)

  def count(self) -> int:
    return self.__anchor__.len1d

  def load(self, vin: int) -> __adt__:
    aa = self.__anchor__.ndarray
    i_next = aa[vin]
    i_start = aa[vin - 1] if vin > 0 else 0
    if i_next <= i_start:
        return []
    return [
        ConfirmPoint_ThickSegPoint_ThickSegPoint.__adt__(
        ) for (
        ) in zip(
        )
    ]

class Envelope2D_Double(DbaStruct):
  __adt__ = namedtuple("Envelope2D_Double", [ "nenveLine", "nenveOnPoints", "nenveOutPoints", ])

  def __arm_store__(self, store: DbaStore, sp: str):
    self.nenveLine = DbArray(store.root_dir, os.path.join(sp, "nenveLine::Line2D Double"), intp)
    self.nenveLine_seq = store.arm_seq("Line2D Double", Line2D_Double)
    self.nenveOnPoints = DbArray(store.root_dir, os.path.join(sp, "nenveOnPoints::[Point2D Double]"), intp)
    self.nenveOnPoints_seq = store.arm_seq("[Point2D Double]", SeqOf_Point2D_Double)
    self.nenveOutPoints = DbArray(store.root_dir, os.path.join(sp, "nenveOutPoints::[Point2D Double]"), intp)
    self.nenveOutPoints_seq = store.arm_seq("[Point2D Double]", SeqOf_Point2D_Double)

  def count(self) -> int:
    return self.nenveLine.len1d

  def load(self, vin: int) -> __adt__:
    return self.__adt__(
      nenveLine = self.nenveLine_seq.load(self.nenveLine.ndarray[vin]),
      nenveOnPoints = self.nenveOnPoints_seq.load(self.nenveOnPoints.ndarray[vin]),
      nenveOutPoints = self.nenveOutPoints_seq.load(self.nenveOutPoints.ndarray[vin]),
    )

class SeqOf_Envelope2D_Double(DbaStruct):
  __adt__ = list[Envelope2D_Double.__adt__]

  def __arm_store__(self, store: DbaStore, sp: str):
    self.__anchor__ = DbArray(store.root_dir, f"{sp}/anchor", intp)
    self.nenveLine = DbArray(store.root_dir, os.path.join(sp, "nenveLine::Line2D Double"), intp)
    self.nenveLine_seq = store.arm_seq("Line2D Double", Line2D_Double)
    self.nenveOnPoints = DbArray(store.root_dir, os.path.join(sp, "nenveOnPoints::[Point2D Double]"), intp)
    self.nenveOnPoints_seq = store.arm_seq("[Point2D Double]", SeqOf_Point2D_Double)
    self.nenveOutPoints = DbArray(store.root_dir, os.path.join(sp, "nenveOutPoints::[Point2D Double]"), intp)
    self.nenveOutPoints_seq = store.arm_seq("[Point2D Double]", SeqOf_Point2D_Double)

  def count(self) -> int:
    return self.__anchor__.len1d

  def load(self, vin: int) -> __adt__:
    aa = self.__anchor__.ndarray
    i_next = aa[vin]
    i_start = aa[vin - 1] if vin > 0 else 0
    if i_next <= i_start:
        return []
    return [
        Envelope2D_Double.__adt__(
        ) for (
        ) in zip(
        )
    ]

class MACDOcc(DbaStruct):
  __adt__ = namedtuple("MACDOcc", [ "macdLineValue", "macdSignalValue", "macdHistogram", "macdFastEMA", "macdSlowEMA", ])

  def __arm_store__(self, store: DbaStore, sp: str):
    self.macdLineValue = DbArray(store.root_dir, os.path.join(sp, "macdLineValue::Double"), f8)
    self.macdSignalValue = DbArray(store.root_dir, os.path.join(sp, "macdSignalValue::Double"), f8)
    self.macdHistogram = DbArray(store.root_dir, os.path.join(sp, "macdHistogram::Double"), f8)
    self.macdFastEMA = DbArray(store.root_dir, os.path.join(sp, "macdFastEMA::Double"), f8)
    self.macdSlowEMA = DbArray(store.root_dir, os.path.join(sp, "macdSlowEMA::Double"), f8)

  def count(self) -> int:
    return self.macdLineValue.len1d

  def load(self, vin: int) -> __adt__:
    return self.__adt__(
      macdLineValue = self.macdLineValue.ndarray[vin],
      macdSignalValue = self.macdSignalValue.ndarray[vin],
      macdHistogram = self.macdHistogram.ndarray[vin],
      macdFastEMA = self.macdFastEMA.ndarray[vin],
      macdSlowEMA = self.macdSlowEMA.ndarray[vin],
    )

class SeqOf_MACDOcc(DbaStruct):
  __adt__ = list[MACDOcc.__adt__]

  def __arm_store__(self, store: DbaStore, sp: str):
    self.__anchor__ = DbArray(store.root_dir, f"{sp}/anchor", intp)
    self.macdLineValue = DbArray(store.root_dir, os.path.join(sp, "macdLineValue::Double"), f8)
    self.macdSignalValue = DbArray(store.root_dir, os.path.join(sp, "macdSignalValue::Double"), f8)
    self.macdHistogram = DbArray(store.root_dir, os.path.join(sp, "macdHistogram::Double"), f8)
    self.macdFastEMA = DbArray(store.root_dir, os.path.join(sp, "macdFastEMA::Double"), f8)
    self.macdSlowEMA = DbArray(store.root_dir, os.path.join(sp, "macdSlowEMA::Double"), f8)

  def count(self) -> int:
    return self.__anchor__.len1d

  def load(self, vin: int) -> __adt__:
    aa = self.__anchor__.ndarray
    i_next = aa[vin]
    i_start = aa[vin - 1] if vin > 0 else 0
    if i_next <= i_start:
        return []
    return [
        MACDOcc.__adt__(
            macdLineValue = macdLineValue,
            macdSignalValue = macdSignalValue,
            macdHistogram = macdHistogram,
            macdFastEMA = macdFastEMA,
            macdSlowEMA = macdSlowEMA,
        ) for (
            macdLineValue,
            macdSignalValue,
            macdHistogram,
            macdFastEMA,
            macdSlowEMA,
        ) in zip(
            self.macdLineValue.ndarray[i_start:i_next],
            self.macdSignalValue.ndarray[i_start:i_next],
            self.macdHistogram.ndarray[i_start:i_next],
            self.macdFastEMA.ndarray[i_start:i_next],
            self.macdSlowEMA.ndarray[i_start:i_next],
        )
    ]

class Point2D__Double_Double(DbaStruct):
  __adt__ = namedtuple("Point2D__Double_Double", [ "x_", "y_", "p_", ])

  def __arm_store__(self, store: DbaStore, sp: str):
    self.x_ = DbArray(store.root_dir, os.path.join(sp, "x_::Double"), f8)
    self.y_ = DbArray(store.root_dir, os.path.join(sp, "y_::Double"), f8)
    self.p_ = DbArray(store.root_dir, os.path.join(sp, "p_::Double"), f8)

  def count(self) -> int:
    return self.x_.len1d

  def load(self, vin: int) -> __adt__:
    return self.__adt__(
      x_ = self.x_.ndarray[vin],
      y_ = self.y_.ndarray[vin],
      p_ = self.p_.ndarray[vin],
    )

class SeqOf_Point2D__Double_Double(DbaStruct):
  __adt__ = list[Point2D__Double_Double.__adt__]

  def __arm_store__(self, store: DbaStore, sp: str):
    self.__anchor__ = DbArray(store.root_dir, f"{sp}/anchor", intp)
    self.x_ = DbArray(store.root_dir, os.path.join(sp, "x_::Double"), f8)
    self.y_ = DbArray(store.root_dir, os.path.join(sp, "y_::Double"), f8)
    self.p_ = DbArray(store.root_dir, os.path.join(sp, "p_::Double"), f8)

  def count(self) -> int:
    return self.__anchor__.len1d

  def load(self, vin: int) -> __adt__:
    aa = self.__anchor__.ndarray
    i_next = aa[vin]
    i_start = aa[vin - 1] if vin > 0 else 0
    if i_next <= i_start:
        return []
    return [
        Point2D__Double_Double.__adt__(
            x_ = x_,
            y_ = y_,
            p_ = p_,
        ) for (
            x_,
            y_,
            p_,
        ) in zip(
            self.x_.ndarray[i_start:i_next],
            self.y_.ndarray[i_start:i_next],
            self.p_.ndarray[i_start:i_next],
        )
    ]

class ConfirmPoint__CoreExtra_BscOcc__MapEntry_Text_Double___BscOcc(DbaStruct):
  __adt__ = namedtuple("ConfirmPoint__CoreExtra_BscOcc__MapEntry_Text_Double___BscOcc", [ "confirm", "actual", ])

  def __arm_store__(self, store: DbaStore, sp: str):
    self.confirm = DbArray(store.root_dir, os.path.join(sp, "_confirm::BscOcc"), intp)
    self.confirm_seq = store.arm_seq("BscOcc", BscOcc)
    self.actual = DbArray(store.root_dir, os.path.join(sp, "_actual::[CoreExtra BscOcc [MapEntry Text Double]]"), intp)
    self.actual_seq = store.arm_seq("[CoreExtra BscOcc [MapEntry Text Double]]", SeqOf_CoreExtra_BscOcc__MapEntry_Text_Double_)

  def count(self) -> int:
    return self.confirm.len1d

  def load(self, vin: int) -> __adt__:
    return self.__adt__(
      confirm = self.confirm_seq.load(self.confirm.ndarray[vin]),
      actual = self.actual_seq.load(self.actual.ndarray[vin]),
    )

class SeqOf_ConfirmPoint__CoreExtra_BscOcc__MapEntry_Text_Double___BscOcc(DbaStruct):
  __adt__ = list[ConfirmPoint__CoreExtra_BscOcc__MapEntry_Text_Double___BscOcc.__adt__]

  def __arm_store__(self, store: DbaStore, sp: str):
    self.__anchor__ = DbArray(store.root_dir, f"{sp}/anchor", intp)
    self.confirm = DbArray(store.root_dir, os.path.join(sp, "_confirm::BscOcc"), intp)
    self.confirm_seq = store.arm_seq("BscOcc", BscOcc)
    self.actual = DbArray(store.root_dir, os.path.join(sp, "_actual::[CoreExtra BscOcc [MapEntry Text Double]]"), intp)
    self.actual_seq = store.arm_seq("[CoreExtra BscOcc [MapEntry Text Double]]", SeqOf_CoreExtra_BscOcc__MapEntry_Text_Double_)

  def count(self) -> int:
    return self.__anchor__.len1d

  def load(self, vin: int) -> __adt__:
    aa = self.__anchor__.ndarray
    i_next = aa[vin]
    i_start = aa[vin - 1] if vin > 0 else 0
    if i_next <= i_start:
        return []
    return [
        ConfirmPoint__CoreExtra_BscOcc__MapEntry_Text_Double___BscOcc.__adt__(
        ) for (
        ) in zip(
        )
    ]

class ThickSegPoint(DbaStruct):
  __adt__ = namedtuple("ThickSegPoint", [ "uti", "price", ])

  def __arm_store__(self, store: DbaStore, sp: str):
    self.uti = DbArray(store.root_dir, os.path.join(sp, "uti::Int"), i8)
    self.price = DbArray(store.root_dir, os.path.join(sp, "price::Double"), f8)

  def count(self) -> int:
    return self.uti.len1d

  def load(self, vin: int) -> __adt__:
    return self.__adt__(
      uti = self.uti.ndarray[vin],
      price = self.price.ndarray[vin],
    )

class SeqOf_ThickSegPoint(DbaStruct):
  __adt__ = list[ThickSegPoint.__adt__]

  def __arm_store__(self, store: DbaStore, sp: str):
    self.__anchor__ = DbArray(store.root_dir, f"{sp}/anchor", intp)
    self.uti = DbArray(store.root_dir, os.path.join(sp, "uti::Int"), i8)
    self.price = DbArray(store.root_dir, os.path.join(sp, "price::Double"), f8)

  def count(self) -> int:
    return self.__anchor__.len1d

  def load(self, vin: int) -> __adt__:
    aa = self.__anchor__.ndarray
    i_next = aa[vin]
    i_start = aa[vin - 1] if vin > 0 else 0
    if i_next <= i_start:
        return []
    return [
        ThickSegPoint.__adt__(
            uti = uti,
            price = price,
        ) for (
            uti,
            price,
        ) in zip(
            self.uti.ndarray[i_start:i_next],
            self.price.ndarray[i_start:i_next],
        )
    ]

class BarSwing(DbaStruct):
  __adt__ = namedtuple("BarSwing", [ "swingStatus", "swingPrice", "swingPoivt", "swingPosUTI", ])

  def __arm_store__(self, store: DbaStore, sp: str):
    self.swingStatus = DbArray(store.root_dir, os.path.join(sp, "swingStatus::Double"), f8)
    self.swingPrice = DbArray(store.root_dir, os.path.join(sp, "swingPrice::Double"), f8)
    self.swingPoivt = DbArray(store.root_dir, os.path.join(sp, "swingPoivt::Double"), f8)
    self.swingPosUTI = DbArray(store.root_dir, os.path.join(sp, "swingPosUTI::Double"), f8)

  def count(self) -> int:
    return self.swingStatus.len1d

  def load(self, vin: int) -> __adt__:
    return self.__adt__(
      swingStatus = self.swingStatus.ndarray[vin],
      swingPrice = self.swingPrice.ndarray[vin],
      swingPoivt = self.swingPoivt.ndarray[vin],
      swingPosUTI = self.swingPosUTI.ndarray[vin],
    )

class SeqOf_BarSwing(DbaStruct):
  __adt__ = list[BarSwing.__adt__]

  def __arm_store__(self, store: DbaStore, sp: str):
    self.__anchor__ = DbArray(store.root_dir, f"{sp}/anchor", intp)
    self.swingStatus = DbArray(store.root_dir, os.path.join(sp, "swingStatus::Double"), f8)
    self.swingPrice = DbArray(store.root_dir, os.path.join(sp, "swingPrice::Double"), f8)
    self.swingPoivt = DbArray(store.root_dir, os.path.join(sp, "swingPoivt::Double"), f8)
    self.swingPosUTI = DbArray(store.root_dir, os.path.join(sp, "swingPosUTI::Double"), f8)

  def count(self) -> int:
    return self.__anchor__.len1d

  def load(self, vin: int) -> __adt__:
    aa = self.__anchor__.ndarray
    i_next = aa[vin]
    i_start = aa[vin - 1] if vin > 0 else 0
    if i_next <= i_start:
        return []
    return [
        BarSwing.__adt__(
            swingStatus = swingStatus,
            swingPrice = swingPrice,
            swingPoivt = swingPoivt,
            swingPosUTI = swingPosUTI,
        ) for (
            swingStatus,
            swingPrice,
            swingPoivt,
            swingPosUTI,
        ) in zip(
            self.swingStatus.ndarray[i_start:i_next],
            self.swingPrice.ndarray[i_start:i_next],
            self.swingPoivt.ndarray[i_start:i_next],
            self.swingPosUTI.ndarray[i_start:i_next],
        )
    ]

class Line2D_Double(DbaStruct):
  __adt__ = namedtuple("Line2D_Double", [ "nanchorPoint", "ndirection", ])

  def __arm_store__(self, store: DbaStore, sp: str):
    self.nanchorPoint = DbArray(store.root_dir, os.path.join(sp, "nanchorPoint::Point2D Double"), intp)
    self.nanchorPoint_seq = store.arm_seq("Point2D Double", Point2D_Double)
    self.ndirection = DbArray(store.root_dir, os.path.join(sp, "ndirection::Vector2D Double"), intp)
    self.ndirection_seq = store.arm_seq("Vector2D Double", Vector2D_Double)

  def count(self) -> int:
    return self.nanchorPoint.len1d

  def load(self, vin: int) -> __adt__:
    return self.__adt__(
      nanchorPoint = self.nanchorPoint_seq.load(self.nanchorPoint.ndarray[vin]),
      ndirection = self.ndirection_seq.load(self.ndirection.ndarray[vin]),
    )

class SeqOf_Line2D_Double(DbaStruct):
  __adt__ = list[Line2D_Double.__adt__]

  def __arm_store__(self, store: DbaStore, sp: str):
    self.__anchor__ = DbArray(store.root_dir, f"{sp}/anchor", intp)
    self.nanchorPoint = DbArray(store.root_dir, os.path.join(sp, "nanchorPoint::Point2D Double"), intp)
    self.nanchorPoint_seq = store.arm_seq("Point2D Double", Point2D_Double)
    self.ndirection = DbArray(store.root_dir, os.path.join(sp, "ndirection::Vector2D Double"), intp)
    self.ndirection_seq = store.arm_seq("Vector2D Double", Vector2D_Double)

  def count(self) -> int:
    return self.__anchor__.len1d

  def load(self, vin: int) -> __adt__:
    aa = self.__anchor__.ndarray
    i_next = aa[vin]
    i_start = aa[vin - 1] if vin > 0 else 0
    if i_next <= i_start:
        return []
    return [
        Line2D_Double.__adt__(
        ) for (
        ) in zip(
        )
    ]

class XBox_Double_Double(DbaStruct):
  __adt__ = namedtuple("XBox_Double_Double", [ "minP", "maxP", ])

  def __arm_store__(self, store: DbaStore, sp: str):
    self.minP = DbArray(store.root_dir, os.path.join(sp, "minP::Point2D' Double Double"), intp)
    self.minP_seq = store.arm_seq("Point2D' Double Double", Point2D__Double_Double)
    self.maxP = DbArray(store.root_dir, os.path.join(sp, "maxP::Point2D' Double Double"), intp)
    self.maxP_seq = store.arm_seq("Point2D' Double Double", Point2D__Double_Double)

  def count(self) -> int:
    return self.minP.len1d

  def load(self, vin: int) -> __adt__:
    return self.__adt__(
      minP = self.minP_seq.load(self.minP.ndarray[vin]),
      maxP = self.maxP_seq.load(self.maxP.ndarray[vin]),
    )

class SeqOf_XBox_Double_Double(DbaStruct):
  __adt__ = list[XBox_Double_Double.__adt__]

  def __arm_store__(self, store: DbaStore, sp: str):
    self.__anchor__ = DbArray(store.root_dir, f"{sp}/anchor", intp)
    self.minP = DbArray(store.root_dir, os.path.join(sp, "minP::Point2D' Double Double"), intp)
    self.minP_seq = store.arm_seq("Point2D' Double Double", Point2D__Double_Double)
    self.maxP = DbArray(store.root_dir, os.path.join(sp, "maxP::Point2D' Double Double"), intp)
    self.maxP_seq = store.arm_seq("Point2D' Double Double", Point2D__Double_Double)

  def count(self) -> int:
    return self.__anchor__.len1d

  def load(self, vin: int) -> __adt__:
    aa = self.__anchor__.ndarray
    i_next = aa[vin]
    i_start = aa[vin - 1] if vin > 0 else 0
    if i_next <= i_start:
        return []
    return [
        XBox_Double_Double.__adt__(
        ) for (
        ) in zip(
        )
    ]

class ZigZagOcc(DbaStruct):
  __adt__ = namedtuple("ZigZagOcc", [ "zigBarSwing", "lastSwing", ])

  def __arm_store__(self, store: DbaStore, sp: str):
    self.zigBarSwing = DbArray(store.root_dir, os.path.join(sp, "zigBarSwing::BarSwing"), intp)
    self.zigBarSwing_seq = store.arm_seq("BarSwing", BarSwing)
    self.lastSwing = DbArray(store.root_dir, os.path.join(sp, "lastSwing::LastSwing"), intp)
    self.lastSwing_seq = store.arm_seq("LastSwing", LastSwing)

  def count(self) -> int:
    return self.zigBarSwing.len1d

  def load(self, vin: int) -> __adt__:
    return self.__adt__(
      zigBarSwing = self.zigBarSwing_seq.load(self.zigBarSwing.ndarray[vin]),
      lastSwing = self.lastSwing_seq.load(self.lastSwing.ndarray[vin]),
    )

class SeqOf_ZigZagOcc(DbaStruct):
  __adt__ = list[ZigZagOcc.__adt__]

  def __arm_store__(self, store: DbaStore, sp: str):
    self.__anchor__ = DbArray(store.root_dir, f"{sp}/anchor", intp)
    self.zigBarSwing = DbArray(store.root_dir, os.path.join(sp, "zigBarSwing::BarSwing"), intp)
    self.zigBarSwing_seq = store.arm_seq("BarSwing", BarSwing)
    self.lastSwing = DbArray(store.root_dir, os.path.join(sp, "lastSwing::LastSwing"), intp)
    self.lastSwing_seq = store.arm_seq("LastSwing", LastSwing)

  def count(self) -> int:
    return self.__anchor__.len1d

  def load(self, vin: int) -> __adt__:
    aa = self.__anchor__.ndarray
    i_next = aa[vin]
    i_start = aa[vin - 1] if vin > 0 else 0
    if i_next <= i_start:
        return []
    return [
        ZigZagOcc.__adt__(
        ) for (
        ) in zip(
        )
    ]

class Point2D_Double(DbaStruct):
  __adt__ = namedtuple("Point2D_Double", [ "x", "y", ])

  def __arm_store__(self, store: DbaStore, sp: str):
    self.x = DbArray(store.root_dir, os.path.join(sp, "x::Double"), f8)
    self.y = DbArray(store.root_dir, os.path.join(sp, "y::Double"), f8)

  def count(self) -> int:
    return self.x.len1d

  def load(self, vin: int) -> __adt__:
    return self.__adt__(
      x = self.x.ndarray[vin],
      y = self.y.ndarray[vin],
    )

class SeqOf_Point2D_Double(DbaStruct):
  __adt__ = list[Point2D_Double.__adt__]

  def __arm_store__(self, store: DbaStore, sp: str):
    self.__anchor__ = DbArray(store.root_dir, f"{sp}/anchor", intp)
    self.x = DbArray(store.root_dir, os.path.join(sp, "x::Double"), f8)
    self.y = DbArray(store.root_dir, os.path.join(sp, "y::Double"), f8)

  def count(self) -> int:
    return self.__anchor__.len1d

  def load(self, vin: int) -> __adt__:
    aa = self.__anchor__.ndarray
    i_next = aa[vin]
    i_start = aa[vin - 1] if vin > 0 else 0
    if i_next <= i_start:
        return []
    return [
        Point2D_Double.__adt__(
            x = x,
            y = y,
        ) for (
            x,
            y,
        ) in zip(
            self.x.ndarray[i_start:i_next],
            self.y.ndarray[i_start:i_next],
        )
    ]

class CompleteScaleTurn2D(DbaStruct):
  __adt__ = namedtuple("CompleteScaleTurn2D", [ "confirm2D", "actual2D", ])

  def __arm_store__(self, store: DbaStore, sp: str):
    self.confirm2D = DbArray(store.root_dir, os.path.join(sp, "confirm2D::Point2Dif Int Double"), intp)
    self.confirm2D_seq = store.arm_seq("Point2Dif Int Double", Point2Dif_Int_Double)
    self.actual2D = DbArray(store.root_dir, os.path.join(sp, "actual2D::Point2Dif Int Double"), intp)
    self.actual2D_seq = store.arm_seq("Point2Dif Int Double", Point2Dif_Int_Double)

  def count(self) -> int:
    return self.confirm2D.len1d

  def load(self, vin: int) -> __adt__:
    return self.__adt__(
      confirm2D = self.confirm2D_seq.load(self.confirm2D.ndarray[vin]),
      actual2D = self.actual2D_seq.load(self.actual2D.ndarray[vin]),
    )

class SeqOf_CompleteScaleTurn2D(DbaStruct):
  __adt__ = list[CompleteScaleTurn2D.__adt__]

  def __arm_store__(self, store: DbaStore, sp: str):
    self.__anchor__ = DbArray(store.root_dir, f"{sp}/anchor", intp)
    self.confirm2D = DbArray(store.root_dir, os.path.join(sp, "confirm2D::Point2Dif Int Double"), intp)
    self.confirm2D_seq = store.arm_seq("Point2Dif Int Double", Point2Dif_Int_Double)
    self.actual2D = DbArray(store.root_dir, os.path.join(sp, "actual2D::Point2Dif Int Double"), intp)
    self.actual2D_seq = store.arm_seq("Point2Dif Int Double", Point2Dif_Int_Double)

  def count(self) -> int:
    return self.__anchor__.len1d

  def load(self, vin: int) -> __adt__:
    aa = self.__anchor__.ndarray
    i_next = aa[vin]
    i_start = aa[vin - 1] if vin > 0 else 0
    if i_next <= i_start:
        return []
    return [
        CompleteScaleTurn2D.__adt__(
        ) for (
        ) in zip(
        )
    ]

class CoreExtra_BscOcc__MapEntry_Text_Double_(DbaStruct):
  __adt__ = namedtuple("CoreExtra_BscOcc__MapEntry_Text_Double_", [ "ceCore", "ceExtra", ])

  def __arm_store__(self, store: DbaStore, sp: str):
    self.ceCore = DbArray(store.root_dir, os.path.join(sp, "ceCore::BscOcc"), intp)
    self.ceCore_seq = store.arm_seq("BscOcc", BscOcc)
    self.ceExtra = DbArray(store.root_dir, os.path.join(sp, "ceExtra::[MapEntry Text Double]"), intp)
    self.ceExtra_seq = store.arm_seq("[MapEntry Text Double]", SeqOf_MapEntry_Text_Double)

  def count(self) -> int:
    return self.ceCore.len1d

  def load(self, vin: int) -> __adt__:
    return self.__adt__(
      ceCore = self.ceCore_seq.load(self.ceCore.ndarray[vin]),
      ceExtra = self.ceExtra_seq.load(self.ceExtra.ndarray[vin]),
    )

class SeqOf_CoreExtra_BscOcc__MapEntry_Text_Double_(DbaStruct):
  __adt__ = list[CoreExtra_BscOcc__MapEntry_Text_Double_.__adt__]

  def __arm_store__(self, store: DbaStore, sp: str):
    self.__anchor__ = DbArray(store.root_dir, f"{sp}/anchor", intp)
    self.ceCore = DbArray(store.root_dir, os.path.join(sp, "ceCore::BscOcc"), intp)
    self.ceCore_seq = store.arm_seq("BscOcc", BscOcc)
    self.ceExtra = DbArray(store.root_dir, os.path.join(sp, "ceExtra::[MapEntry Text Double]"), intp)
    self.ceExtra_seq = store.arm_seq("[MapEntry Text Double]", SeqOf_MapEntry_Text_Double)

  def count(self) -> int:
    return self.__anchor__.len1d

  def load(self, vin: int) -> __adt__:
    aa = self.__anchor__.ndarray
    i_next = aa[vin]
    i_start = aa[vin - 1] if vin > 0 else 0
    if i_next <= i_start:
        return []
    return [
        CoreExtra_BscOcc__MapEntry_Text_Double_.__adt__(
        ) for (
        ) in zip(
        )
    ]

class ThickEnd(DbaStruct):
  __adt__ = namedtuple("ThickEnd", [ "teBuyGradeSum", "teSellGradeSum", "teDenseStrength", "teDenseBuyStrength", "teDenseSellStrength", "teFightStrength", "teSymCnt", "teSConfirmActual", "teConfirmActual", ])

  def __arm_store__(self, store: DbaStore, sp: str):
    self.teBuyGradeSum = DbArray(store.root_dir, os.path.join(sp, "teBuyGradeSum::Double"), f8)
    self.teSellGradeSum = DbArray(store.root_dir, os.path.join(sp, "teSellGradeSum::Double"), f8)
    self.teDenseStrength = DbArray(store.root_dir, os.path.join(sp, "teDenseStrength::Double"), f8)
    self.teDenseBuyStrength = DbArray(store.root_dir, os.path.join(sp, "teDenseBuyStrength::Double"), f8)
    self.teDenseSellStrength = DbArray(store.root_dir, os.path.join(sp, "teDenseSellStrength::Double"), f8)
    self.teFightStrength = DbArray(store.root_dir, os.path.join(sp, "teFightStrength::Double"), f8)
    self.teSymCnt = DbArray(store.root_dir, os.path.join(sp, "teSymCnt::Int"), i8)
    self.teSConfirmActual = DbArray(store.root_dir, os.path.join(sp, "teSConfirmActual::ConfirmPoint ThickSegPoint ThickSegPoint"), intp)
    self.teSConfirmActual_seq = store.arm_seq("ConfirmPoint ThickSegPoint ThickSegPoint", ConfirmPoint_ThickSegPoint_ThickSegPoint)
    self.teConfirmActual = DbArray(store.root_dir, os.path.join(sp, "teConfirmActual::ConfirmPoint ThickSegPoint ThickSegPoint"), intp)
    self.teConfirmActual_seq = store.arm_seq("ConfirmPoint ThickSegPoint ThickSegPoint", ConfirmPoint_ThickSegPoint_ThickSegPoint)

  def count(self) -> int:
    return self.teBuyGradeSum.len1d

  def load(self, vin: int) -> __adt__:
    return self.__adt__(
      teBuyGradeSum = self.teBuyGradeSum.ndarray[vin],
      teSellGradeSum = self.teSellGradeSum.ndarray[vin],
      teDenseStrength = self.teDenseStrength.ndarray[vin],
      teDenseBuyStrength = self.teDenseBuyStrength.ndarray[vin],
      teDenseSellStrength = self.teDenseSellStrength.ndarray[vin],
      teFightStrength = self.teFightStrength.ndarray[vin],
      teSymCnt = self.teSymCnt.ndarray[vin],
      teSConfirmActual = self.teSConfirmActual_seq.load(self.teSConfirmActual.ndarray[vin]),
      teConfirmActual = self.teConfirmActual_seq.load(self.teConfirmActual.ndarray[vin]),
    )

class SeqOf_ThickEnd(DbaStruct):
  __adt__ = list[ThickEnd.__adt__]

  def __arm_store__(self, store: DbaStore, sp: str):
    self.__anchor__ = DbArray(store.root_dir, f"{sp}/anchor", intp)
    self.teBuyGradeSum = DbArray(store.root_dir, os.path.join(sp, "teBuyGradeSum::Double"), f8)
    self.teSellGradeSum = DbArray(store.root_dir, os.path.join(sp, "teSellGradeSum::Double"), f8)
    self.teDenseStrength = DbArray(store.root_dir, os.path.join(sp, "teDenseStrength::Double"), f8)
    self.teDenseBuyStrength = DbArray(store.root_dir, os.path.join(sp, "teDenseBuyStrength::Double"), f8)
    self.teDenseSellStrength = DbArray(store.root_dir, os.path.join(sp, "teDenseSellStrength::Double"), f8)
    self.teFightStrength = DbArray(store.root_dir, os.path.join(sp, "teFightStrength::Double"), f8)
    self.teSymCnt = DbArray(store.root_dir, os.path.join(sp, "teSymCnt::Int"), i8)
    self.teSConfirmActual = DbArray(store.root_dir, os.path.join(sp, "teSConfirmActual::ConfirmPoint ThickSegPoint ThickSegPoint"), intp)
    self.teSConfirmActual_seq = store.arm_seq("ConfirmPoint ThickSegPoint ThickSegPoint", ConfirmPoint_ThickSegPoint_ThickSegPoint)
    self.teConfirmActual = DbArray(store.root_dir, os.path.join(sp, "teConfirmActual::ConfirmPoint ThickSegPoint ThickSegPoint"), intp)
    self.teConfirmActual_seq = store.arm_seq("ConfirmPoint ThickSegPoint ThickSegPoint", ConfirmPoint_ThickSegPoint_ThickSegPoint)

  def count(self) -> int:
    return self.__anchor__.len1d

  def load(self, vin: int) -> __adt__:
    aa = self.__anchor__.ndarray
    i_next = aa[vin]
    i_start = aa[vin - 1] if vin > 0 else 0
    if i_next <= i_start:
        return []
    return [
        ThickEnd.__adt__(
            teBuyGradeSum = teBuyGradeSum,
            teSellGradeSum = teSellGradeSum,
            teDenseStrength = teDenseStrength,
            teDenseBuyStrength = teDenseBuyStrength,
            teDenseSellStrength = teDenseSellStrength,
            teFightStrength = teFightStrength,
            teSymCnt = teSymCnt,
        ) for (
            teBuyGradeSum,
            teSellGradeSum,
            teDenseStrength,
            teDenseBuyStrength,
            teDenseSellStrength,
            teFightStrength,
            teSymCnt,
        ) in zip(
            self.teBuyGradeSum.ndarray[i_start:i_next],
            self.teSellGradeSum.ndarray[i_start:i_next],
            self.teDenseStrength.ndarray[i_start:i_next],
            self.teDenseBuyStrength.ndarray[i_start:i_next],
            self.teDenseSellStrength.ndarray[i_start:i_next],
            self.teFightStrength.ndarray[i_start:i_next],
            self.teSymCnt.ndarray[i_start:i_next],
        )
    ]

class XBox2Eval_Double_Double_Double(DbaStruct):
  __adt__ = namedtuple("XBox2Eval_Double_Double_Double", [ "xbeEvaluation", "xbeShape", ])

  def __arm_store__(self, store: DbaStore, sp: str):
    self.xbeEvaluation = DbArray(store.root_dir, os.path.join(sp, "xbeEvaluation::Double"), f8)
    self.xbeShape = DbArray(store.root_dir, os.path.join(sp, "xbeShape::XBox Double Double"), intp)
    self.xbeShape_seq = store.arm_seq("XBox Double Double", XBox_Double_Double)

  def count(self) -> int:
    return self.xbeEvaluation.len1d

  def load(self, vin: int) -> __adt__:
    return self.__adt__(
      xbeEvaluation = self.xbeEvaluation.ndarray[vin],
      xbeShape = self.xbeShape_seq.load(self.xbeShape.ndarray[vin]),
    )

class SeqOf_XBox2Eval_Double_Double_Double(DbaStruct):
  __adt__ = list[XBox2Eval_Double_Double_Double.__adt__]

  def __arm_store__(self, store: DbaStore, sp: str):
    self.__anchor__ = DbArray(store.root_dir, f"{sp}/anchor", intp)
    self.xbeEvaluation = DbArray(store.root_dir, os.path.join(sp, "xbeEvaluation::Double"), f8)
    self.xbeShape = DbArray(store.root_dir, os.path.join(sp, "xbeShape::XBox Double Double"), intp)
    self.xbeShape_seq = store.arm_seq("XBox Double Double", XBox_Double_Double)

  def count(self) -> int:
    return self.__anchor__.len1d

  def load(self, vin: int) -> __adt__:
    aa = self.__anchor__.ndarray
    i_next = aa[vin]
    i_start = aa[vin - 1] if vin > 0 else 0
    if i_next <= i_start:
        return []
    return [
        XBox2Eval_Double_Double_Double.__adt__(
            xbeEvaluation = xbeEvaluation,
        ) for (
            xbeEvaluation,
        ) in zip(
            self.xbeEvaluation.ndarray[i_start:i_next],
        )
    ]

class Point2Dif_Int_Double(DbaStruct):
  __adt__ = namedtuple("Point2Dif_Int_Double", [ "x", "y", ])

  def __arm_store__(self, store: DbaStore, sp: str):
    self.x = DbArray(store.root_dir, os.path.join(sp, "x::Int"), i8)
    self.y = DbArray(store.root_dir, os.path.join(sp, "y::Double"), f8)

  def count(self) -> int:
    return self.x.len1d

  def load(self, vin: int) -> __adt__:
    return self.__adt__(
      x = self.x.ndarray[vin],
      y = self.y.ndarray[vin],
    )

class SeqOf_Point2Dif_Int_Double(DbaStruct):
  __adt__ = list[Point2Dif_Int_Double.__adt__]

  def __arm_store__(self, store: DbaStore, sp: str):
    self.__anchor__ = DbArray(store.root_dir, f"{sp}/anchor", intp)
    self.x = DbArray(store.root_dir, os.path.join(sp, "x::Int"), i8)
    self.y = DbArray(store.root_dir, os.path.join(sp, "y::Double"), f8)

  def count(self) -> int:
    return self.__anchor__.len1d

  def load(self, vin: int) -> __adt__:
    aa = self.__anchor__.ndarray
    i_next = aa[vin]
    i_start = aa[vin - 1] if vin > 0 else 0
    if i_next <= i_start:
        return []
    return [
        Point2Dif_Int_Double.__adt__(
            x = x,
            y = y,
        ) for (
            x,
            y,
        ) in zip(
            self.x.ndarray[i_start:i_next],
            self.y.ndarray[i_start:i_next],
        )
    ]

class ConfirmPoint__BscOccWithStrength__BscOcc(DbaStruct):
  __adt__ = namedtuple("ConfirmPoint__BscOccWithStrength__BscOcc", [ "confirm", "actual", ])

  def __arm_store__(self, store: DbaStore, sp: str):
    self.confirm = DbArray(store.root_dir, os.path.join(sp, "_confirm::BscOcc"), intp)
    self.confirm_seq = store.arm_seq("BscOcc", BscOcc)
    self.actual = DbArray(store.root_dir, os.path.join(sp, "_actual::[BscOccWithStrength]"), intp)
    self.actual_seq = store.arm_seq("[BscOccWithStrength]", SeqOf_BscOccWithStrength)

  def count(self) -> int:
    return self.confirm.len1d

  def load(self, vin: int) -> __adt__:
    return self.__adt__(
      confirm = self.confirm_seq.load(self.confirm.ndarray[vin]),
      actual = self.actual_seq.load(self.actual.ndarray[vin]),
    )

class SeqOf_ConfirmPoint__BscOccWithStrength__BscOcc(DbaStruct):
  __adt__ = list[ConfirmPoint__BscOccWithStrength__BscOcc.__adt__]

  def __arm_store__(self, store: DbaStore, sp: str):
    self.__anchor__ = DbArray(store.root_dir, f"{sp}/anchor", intp)
    self.confirm = DbArray(store.root_dir, os.path.join(sp, "_confirm::BscOcc"), intp)
    self.confirm_seq = store.arm_seq("BscOcc", BscOcc)
    self.actual = DbArray(store.root_dir, os.path.join(sp, "_actual::[BscOccWithStrength]"), intp)
    self.actual_seq = store.arm_seq("[BscOccWithStrength]", SeqOf_BscOccWithStrength)

  def count(self) -> int:
    return self.__anchor__.len1d

  def load(self, vin: int) -> __adt__:
    aa = self.__anchor__.ndarray
    i_next = aa[vin]
    i_start = aa[vin - 1] if vin > 0 else 0
    if i_next <= i_start:
        return []
    return [
        ConfirmPoint__BscOccWithStrength__BscOcc.__adt__(
        ) for (
        ) in zip(
        )
    ]

class XBox2EvalWrap_Double_Double_Double(DbaStruct):
  __adt__ = namedtuple("XBox2EvalWrap_Double_Double_Double", [ "xbes", ])

  def __arm_store__(self, store: DbaStore, sp: str):
    self.xbes = DbArray(store.root_dir, os.path.join(sp, "xbes::[XBox2Eval Double Double Double]"), intp)
    self.xbes_seq = store.arm_seq("[XBox2Eval Double Double Double]", SeqOf_XBox2Eval_Double_Double_Double)

  def count(self) -> int:
    return self.xbes.len1d

  def load(self, vin: int) -> __adt__:
    return self.__adt__(
      xbes = self.xbes_seq.load(self.xbes.ndarray[vin]),
    )

class SeqOf_XBox2EvalWrap_Double_Double_Double(DbaStruct):
  __adt__ = list[XBox2EvalWrap_Double_Double_Double.__adt__]

  def __arm_store__(self, store: DbaStore, sp: str):
    self.__anchor__ = DbArray(store.root_dir, f"{sp}/anchor", intp)
    self.xbes = DbArray(store.root_dir, os.path.join(sp, "xbes::[XBox2Eval Double Double Double]"), intp)
    self.xbes_seq = store.arm_seq("[XBox2Eval Double Double Double]", SeqOf_XBox2Eval_Double_Double_Double)

  def count(self) -> int:
    return self.__anchor__.len1d

  def load(self, vin: int) -> __adt__:
    aa = self.__anchor__.ndarray
    i_next = aa[vin]
    i_start = aa[vin - 1] if vin > 0 else 0
    if i_next <= i_start:
        return []
    return [
        XBox2EvalWrap_Double_Double_Double.__adt__(
        ) for (
        ) in zip(
        )
    ]

class ZigWithStatusOcc(DbaStruct):
  __adt__ = namedtuple("ZigWithStatusOcc", [ "price0", "pivot0", "posUTI0", "price1", "pivot1", "posUTI1", ])

  def __arm_store__(self, store: DbaStore, sp: str):
    self.price0 = DbArray(store.root_dir, os.path.join(sp, "price0::Double"), f8)
    self.pivot0 = DbArray(store.root_dir, os.path.join(sp, "pivot0::Double"), f8)
    self.posUTI0 = DbArray(store.root_dir, os.path.join(sp, "posUTI0::Double"), f8)
    self.price1 = DbArray(store.root_dir, os.path.join(sp, "price1::Double"), f8)
    self.pivot1 = DbArray(store.root_dir, os.path.join(sp, "pivot1::Double"), f8)
    self.posUTI1 = DbArray(store.root_dir, os.path.join(sp, "posUTI1::Double"), f8)

  def count(self) -> int:
    return self.price0.len1d

  def load(self, vin: int) -> __adt__:
    return self.__adt__(
      price0 = self.price0.ndarray[vin],
      pivot0 = self.pivot0.ndarray[vin],
      posUTI0 = self.posUTI0.ndarray[vin],
      price1 = self.price1.ndarray[vin],
      pivot1 = self.pivot1.ndarray[vin],
      posUTI1 = self.posUTI1.ndarray[vin],
    )

class SeqOf_ZigWithStatusOcc(DbaStruct):
  __adt__ = list[ZigWithStatusOcc.__adt__]

  def __arm_store__(self, store: DbaStore, sp: str):
    self.__anchor__ = DbArray(store.root_dir, f"{sp}/anchor", intp)
    self.price0 = DbArray(store.root_dir, os.path.join(sp, "price0::Double"), f8)
    self.pivot0 = DbArray(store.root_dir, os.path.join(sp, "pivot0::Double"), f8)
    self.posUTI0 = DbArray(store.root_dir, os.path.join(sp, "posUTI0::Double"), f8)
    self.price1 = DbArray(store.root_dir, os.path.join(sp, "price1::Double"), f8)
    self.pivot1 = DbArray(store.root_dir, os.path.join(sp, "pivot1::Double"), f8)
    self.posUTI1 = DbArray(store.root_dir, os.path.join(sp, "posUTI1::Double"), f8)

  def count(self) -> int:
    return self.__anchor__.len1d

  def load(self, vin: int) -> __adt__:
    aa = self.__anchor__.ndarray
    i_next = aa[vin]
    i_start = aa[vin - 1] if vin > 0 else 0
    if i_next <= i_start:
        return []
    return [
        ZigWithStatusOcc.__adt__(
            price0 = price0,
            pivot0 = pivot0,
            posUTI0 = posUTI0,
            price1 = price1,
            pivot1 = pivot1,
            posUTI1 = posUTI1,
        ) for (
            price0,
            pivot0,
            posUTI0,
            price1,
            pivot1,
            posUTI1,
        ) in zip(
            self.price0.ndarray[i_start:i_next],
            self.pivot0.ndarray[i_start:i_next],
            self.posUTI0.ndarray[i_start:i_next],
            self.price1.ndarray[i_start:i_next],
            self.pivot1.ndarray[i_start:i_next],
            self.posUTI1.ndarray[i_start:i_next],
        )
    ]

class XSimpleSymmetry(DbaStruct):
  __adt__ = namedtuple("XSimpleSymmetry", [ "slope1", "slope2", "height1", "height2", "heightR1", "heightR2", "width1", "width2", "prettiness", "vertice1", "vertice2", "vertice3", "symConfirm", ])

  def __arm_store__(self, store: DbaStore, sp: str):
    self.slope1 = DbArray(store.root_dir, os.path.join(sp, "slope1::Double"), f8)
    self.slope2 = DbArray(store.root_dir, os.path.join(sp, "slope2::Double"), f8)
    self.height1 = DbArray(store.root_dir, os.path.join(sp, "height1::Double"), f8)
    self.height2 = DbArray(store.root_dir, os.path.join(sp, "height2::Double"), f8)
    self.heightR1 = DbArray(store.root_dir, os.path.join(sp, "heightR1::Double"), f8)
    self.heightR2 = DbArray(store.root_dir, os.path.join(sp, "heightR2::Double"), f8)
    self.width1 = DbArray(store.root_dir, os.path.join(sp, "width1::Double"), f8)
    self.width2 = DbArray(store.root_dir, os.path.join(sp, "width2::Double"), f8)
    self.prettiness = DbArray(store.root_dir, os.path.join(sp, "prettiness::Double"), f8)
    self.vertice1 = DbArray(store.root_dir, os.path.join(sp, "vertice1::Point2D Double"), intp)
    self.vertice1_seq = store.arm_seq("Point2D Double", Point2D_Double)
    self.vertice2 = DbArray(store.root_dir, os.path.join(sp, "vertice2::Point2D Double"), intp)
    self.vertice2_seq = store.arm_seq("Point2D Double", Point2D_Double)
    self.vertice3 = DbArray(store.root_dir, os.path.join(sp, "vertice3::Point2D Double"), intp)
    self.vertice3_seq = store.arm_seq("Point2D Double", Point2D_Double)
    self.symConfirm = DbArray(store.root_dir, os.path.join(sp, "symConfirm::Point2D Double"), intp)
    self.symConfirm_seq = store.arm_seq("Point2D Double", Point2D_Double)

  def count(self) -> int:
    return self.slope1.len1d

  def load(self, vin: int) -> __adt__:
    return self.__adt__(
      slope1 = self.slope1.ndarray[vin],
      slope2 = self.slope2.ndarray[vin],
      height1 = self.height1.ndarray[vin],
      height2 = self.height2.ndarray[vin],
      heightR1 = self.heightR1.ndarray[vin],
      heightR2 = self.heightR2.ndarray[vin],
      width1 = self.width1.ndarray[vin],
      width2 = self.width2.ndarray[vin],
      prettiness = self.prettiness.ndarray[vin],
      vertice1 = self.vertice1_seq.load(self.vertice1.ndarray[vin]),
      vertice2 = self.vertice2_seq.load(self.vertice2.ndarray[vin]),
      vertice3 = self.vertice3_seq.load(self.vertice3.ndarray[vin]),
      symConfirm = self.symConfirm_seq.load(self.symConfirm.ndarray[vin]),
    )

class SeqOf_XSimpleSymmetry(DbaStruct):
  __adt__ = list[XSimpleSymmetry.__adt__]

  def __arm_store__(self, store: DbaStore, sp: str):
    self.__anchor__ = DbArray(store.root_dir, f"{sp}/anchor", intp)
    self.slope1 = DbArray(store.root_dir, os.path.join(sp, "slope1::Double"), f8)
    self.slope2 = DbArray(store.root_dir, os.path.join(sp, "slope2::Double"), f8)
    self.height1 = DbArray(store.root_dir, os.path.join(sp, "height1::Double"), f8)
    self.height2 = DbArray(store.root_dir, os.path.join(sp, "height2::Double"), f8)
    self.heightR1 = DbArray(store.root_dir, os.path.join(sp, "heightR1::Double"), f8)
    self.heightR2 = DbArray(store.root_dir, os.path.join(sp, "heightR2::Double"), f8)
    self.width1 = DbArray(store.root_dir, os.path.join(sp, "width1::Double"), f8)
    self.width2 = DbArray(store.root_dir, os.path.join(sp, "width2::Double"), f8)
    self.prettiness = DbArray(store.root_dir, os.path.join(sp, "prettiness::Double"), f8)
    self.vertice1 = DbArray(store.root_dir, os.path.join(sp, "vertice1::Point2D Double"), intp)
    self.vertice1_seq = store.arm_seq("Point2D Double", Point2D_Double)
    self.vertice2 = DbArray(store.root_dir, os.path.join(sp, "vertice2::Point2D Double"), intp)
    self.vertice2_seq = store.arm_seq("Point2D Double", Point2D_Double)
    self.vertice3 = DbArray(store.root_dir, os.path.join(sp, "vertice3::Point2D Double"), intp)
    self.vertice3_seq = store.arm_seq("Point2D Double", Point2D_Double)
    self.symConfirm = DbArray(store.root_dir, os.path.join(sp, "symConfirm::Point2D Double"), intp)
    self.symConfirm_seq = store.arm_seq("Point2D Double", Point2D_Double)

  def count(self) -> int:
    return self.__anchor__.len1d

  def load(self, vin: int) -> __adt__:
    aa = self.__anchor__.ndarray
    i_next = aa[vin]
    i_start = aa[vin - 1] if vin > 0 else 0
    if i_next <= i_start:
        return []
    return [
        XSimpleSymmetry.__adt__(
            slope1 = slope1,
            slope2 = slope2,
            height1 = height1,
            height2 = height2,
            heightR1 = heightR1,
            heightR2 = heightR2,
            width1 = width1,
            width2 = width2,
            prettiness = prettiness,
        ) for (
            slope1,
            slope2,
            height1,
            height2,
            heightR1,
            heightR2,
            width1,
            width2,
            prettiness,
        ) in zip(
            self.slope1.ndarray[i_start:i_next],
            self.slope2.ndarray[i_start:i_next],
            self.height1.ndarray[i_start:i_next],
            self.height2.ndarray[i_start:i_next],
            self.heightR1.ndarray[i_start:i_next],
            self.heightR2.ndarray[i_start:i_next],
            self.width1.ndarray[i_start:i_next],
            self.width2.ndarray[i_start:i_next],
            self.prettiness.ndarray[i_start:i_next],
        )
    ]

class BscOccWithStrength(DbaStruct):
  __adt__ = namedtuple("BscOccWithStrength", [ "uti", "price", "strength", ])

  def __arm_store__(self, store: DbaStore, sp: str):
    self.uti = DbArray(store.root_dir, os.path.join(sp, "uti::Int"), i8)
    self.price = DbArray(store.root_dir, os.path.join(sp, "price::Double"), f8)
    self.strength = DbArray(store.root_dir, os.path.join(sp, "strength::Double"), f8)

  def count(self) -> int:
    return self.uti.len1d

  def load(self, vin: int) -> __adt__:
    return self.__adt__(
      uti = self.uti.ndarray[vin],
      price = self.price.ndarray[vin],
      strength = self.strength.ndarray[vin],
    )

class SeqOf_BscOccWithStrength(DbaStruct):
  __adt__ = list[BscOccWithStrength.__adt__]

  def __arm_store__(self, store: DbaStore, sp: str):
    self.__anchor__ = DbArray(store.root_dir, f"{sp}/anchor", intp)
    self.uti = DbArray(store.root_dir, os.path.join(sp, "uti::Int"), i8)
    self.price = DbArray(store.root_dir, os.path.join(sp, "price::Double"), f8)
    self.strength = DbArray(store.root_dir, os.path.join(sp, "strength::Double"), f8)

  def count(self) -> int:
    return self.__anchor__.len1d

  def load(self, vin: int) -> __adt__:
    aa = self.__anchor__.ndarray
    i_next = aa[vin]
    i_start = aa[vin - 1] if vin > 0 else 0
    if i_next <= i_start:
        return []
    return [
        BscOccWithStrength.__adt__(
            uti = uti,
            price = price,
            strength = strength,
        ) for (
            uti,
            price,
            strength,
        ) in zip(
            self.uti.ndarray[i_start:i_next],
            self.price.ndarray[i_start:i_next],
            self.strength.ndarray[i_start:i_next],
        )
    ]

class BscOcc(DbaStruct):
  __adt__ = namedtuple("BscOcc", [ "uti", "price", ])

  def __arm_store__(self, store: DbaStore, sp: str):
    self.uti = DbArray(store.root_dir, os.path.join(sp, "uti::Int"), i8)
    self.price = DbArray(store.root_dir, os.path.join(sp, "price::Double"), f8)

  def count(self) -> int:
    return self.uti.len1d

  def load(self, vin: int) -> __adt__:
    return self.__adt__(
      uti = self.uti.ndarray[vin],
      price = self.price.ndarray[vin],
    )

class SeqOf_BscOcc(DbaStruct):
  __adt__ = list[BscOcc.__adt__]

  def __arm_store__(self, store: DbaStore, sp: str):
    self.__anchor__ = DbArray(store.root_dir, f"{sp}/anchor", intp)
    self.uti = DbArray(store.root_dir, os.path.join(sp, "uti::Int"), i8)
    self.price = DbArray(store.root_dir, os.path.join(sp, "price::Double"), f8)

  def count(self) -> int:
    return self.__anchor__.len1d

  def load(self, vin: int) -> __adt__:
    aa = self.__anchor__.ndarray
    i_next = aa[vin]
    i_start = aa[vin - 1] if vin > 0 else 0
    if i_next <= i_start:
        return []
    return [
        BscOcc.__adt__(
            uti = uti,
            price = price,
        ) for (
            uti,
            price,
        ) in zip(
            self.uti.ndarray[i_start:i_next],
            self.price.ndarray[i_start:i_next],
        )
    ]

class Vector2D_Double(DbaStruct):
  __adt__ = namedtuple("Vector2D_Double", [ "x", "y", ])

  def __arm_store__(self, store: DbaStore, sp: str):
    self.x = DbArray(store.root_dir, os.path.join(sp, "x::Double"), f8)
    self.y = DbArray(store.root_dir, os.path.join(sp, "y::Double"), f8)

  def count(self) -> int:
    return self.x.len1d

  def load(self, vin: int) -> __adt__:
    return self.__adt__(
      x = self.x.ndarray[vin],
      y = self.y.ndarray[vin],
    )

class SeqOf_Vector2D_Double(DbaStruct):
  __adt__ = list[Vector2D_Double.__adt__]

  def __arm_store__(self, store: DbaStore, sp: str):
    self.__anchor__ = DbArray(store.root_dir, f"{sp}/anchor", intp)
    self.x = DbArray(store.root_dir, os.path.join(sp, "x::Double"), f8)
    self.y = DbArray(store.root_dir, os.path.join(sp, "y::Double"), f8)

  def count(self) -> int:
    return self.__anchor__.len1d

  def load(self, vin: int) -> __adt__:
    aa = self.__anchor__.ndarray
    i_next = aa[vin]
    i_start = aa[vin - 1] if vin > 0 else 0
    if i_next <= i_start:
        return []
    return [
        Vector2D_Double.__adt__(
            x = x,
            y = y,
        ) for (
            x,
            y,
        ) in zip(
            self.x.ndarray[i_start:i_next],
            self.y.ndarray[i_start:i_next],
        )
    ]

