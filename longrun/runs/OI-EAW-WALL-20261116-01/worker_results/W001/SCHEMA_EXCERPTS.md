# 实际schema的本对象相关定义

实际路径：`/dwdhome/fy/BASE_E6_2/mquant/worker/adt/dbaw.py`；此为选段，不是整个schema文件。

原文件行 1091–1104：

```python
class MulWrap_P1WallCurrentStorage(DbaStruct):
  __adt__ = namedtuple("MulWrap_P1WallCurrentStorage", [ "mul", ])

  def __arm_store__(self, store: DbaStore, sp: str):
    self.mul = DbArray(store.root_dir, os.path.join(sp, "mul::[P1WallCurrentStorage]"), intp)
    self.mul_seq = store.arm_seq("[P1WallCurrentStorage]", SeqOf_P1WallCurrentStorage)

  def count(self) -> int:
    return self.mul.len1d

  def load(self, vin: int) -> __adt__:
    return self.__adt__(
      mul = self.mul_seq.load(self.mul.ndarray[vin]),
    )

```

原文件行 1106–1128：

```python
class SeqOf_MulWrap_P1WallCurrentStorage(DbaStruct):
  __adt__ = list[MulWrap_P1WallCurrentStorage.__adt__]

  def __arm_store__(self, store: DbaStore, sp: str):
    self.__anchor__ = DbArray(store.root_dir, f"{sp}/anchor", intp)
    self.mul = DbArray(store.root_dir, os.path.join(sp, "mul::[P1WallCurrentStorage]"), intp)
    self.mul_seq = store.arm_seq("[P1WallCurrentStorage]", SeqOf_P1WallCurrentStorage)

  def count(self) -> int:
    return self.__anchor__.len1d

  def load(self, vin: int) -> __adt__:
    aa = self.__anchor__.ndarray
    i_next = aa[vin]
    i_start = aa[vin - 1] if vin > 0 else 0
    if i_next <= i_start:
        return []
    return [
        MulWrap_P1WallCurrentStorage.__adt__(
        ) for (
        ) in zip(
        )
    ]

```

原文件行 4932–4946：

```python
class P1WallCurrentStorage(DbaStruct):
  __adt__ = namedtuple("P1WallCurrentStorage", [ "p1WallCurrentLocalNo", "p1WallCurrentState", ])

  def __arm_store__(self, store: DbaStore, sp: str):
    self.p1WallCurrentLocalNo = DbArray(store.root_dir, os.path.join(sp, "p1WallCurrentLocalNo::Int64"), i8)
    self.p1WallCurrentState = DbArray(store.root_dir, os.path.join(sp, "p1WallCurrentState::Text$Data.Text"), intp)

  def count(self) -> int:
    return self.p1WallCurrentLocalNo.len1d

  def load(self, vin: int) -> __adt__:
    return self.__adt__(
      p1WallCurrentLocalNo = self.p1WallCurrentLocalNo.ndarray[vin],
      p1WallCurrentState = self.__store__.load_Text(self.p1WallCurrentState.ndarray[vin]),
    )

```

原文件行 4948–4977：

```python
class SeqOf_P1WallCurrentStorage(DbaStruct):
  __adt__ = list[P1WallCurrentStorage.__adt__]

  def __arm_store__(self, store: DbaStore, sp: str):
    self.__anchor__ = DbArray(store.root_dir, f"{sp}/anchor", intp)
    self.p1WallCurrentLocalNo = DbArray(store.root_dir, os.path.join(sp, "p1WallCurrentLocalNo::Int64"), i8)
    self.p1WallCurrentState = DbArray(store.root_dir, os.path.join(sp, "p1WallCurrentState::Text$Data.Text"), intp)

  def count(self) -> int:
    return self.__anchor__.len1d

  def load(self, vin: int) -> __adt__:
    aa = self.__anchor__.ndarray
    i_next = aa[vin]
    i_start = aa[vin - 1] if vin > 0 else 0
    if i_next <= i_start:
        return []
    return [
        P1WallCurrentStorage.__adt__(
            p1WallCurrentLocalNo = p1WallCurrentLocalNo,
            p1WallCurrentState = p1WallCurrentState,
        ) for (
            p1WallCurrentLocalNo,
            p1WallCurrentState,
        ) in zip(
            self.p1WallCurrentLocalNo.ndarray[i_start:i_next],
            (self.__store__.load_Text(tvin) for tvin in
             self.p1WallCurrentState.ndarray[i_start:i_next]),
        )
    ]

```

原文件行 5317–5345：

```python
class P1DiagnosticStorage(DbaStruct):
  __adt__ = namedtuple("P1DiagnosticStorage", [ "p1DiagnosticDouble1", "p1DiagnosticInt1", "p1DiagnosticInt2", "p1DiagnosticInt3", "p1DiagnosticSource", "p1DiagnosticKind", "p1DiagnosticText1", "p1DiagnosticText2", "p1DiagnosticText3", ])

  def __arm_store__(self, store: DbaStore, sp: str):
    self.p1DiagnosticDouble1 = DbArray(store.root_dir, os.path.join(sp, "p1DiagnosticDouble1::Double"), f8)
    self.p1DiagnosticInt1 = DbArray(store.root_dir, os.path.join(sp, "p1DiagnosticInt1::Int64"), i8)
    self.p1DiagnosticInt2 = DbArray(store.root_dir, os.path.join(sp, "p1DiagnosticInt2::Int64"), i8)
    self.p1DiagnosticInt3 = DbArray(store.root_dir, os.path.join(sp, "p1DiagnosticInt3::Int64"), i8)
    self.p1DiagnosticSource = DbArray(store.root_dir, os.path.join(sp, "p1DiagnosticSource::Text$Data.Text"), intp)
    self.p1DiagnosticKind = DbArray(store.root_dir, os.path.join(sp, "p1DiagnosticKind::Text$Data.Text"), intp)
    self.p1DiagnosticText1 = DbArray(store.root_dir, os.path.join(sp, "p1DiagnosticText1::Text$Data.Text"), intp)
    self.p1DiagnosticText2 = DbArray(store.root_dir, os.path.join(sp, "p1DiagnosticText2::Text$Data.Text"), intp)
    self.p1DiagnosticText3 = DbArray(store.root_dir, os.path.join(sp, "p1DiagnosticText3::Text$Data.Text"), intp)

  def count(self) -> int:
    return self.p1DiagnosticDouble1.len1d

  def load(self, vin: int) -> __adt__:
    return self.__adt__(
      p1DiagnosticDouble1 = self.p1DiagnosticDouble1.ndarray[vin],
      p1DiagnosticInt1 = self.p1DiagnosticInt1.ndarray[vin],
      p1DiagnosticInt2 = self.p1DiagnosticInt2.ndarray[vin],
      p1DiagnosticInt3 = self.p1DiagnosticInt3.ndarray[vin],
      p1DiagnosticSource = self.__store__.load_Text(self.p1DiagnosticSource.ndarray[vin]),
      p1DiagnosticKind = self.__store__.load_Text(self.p1DiagnosticKind.ndarray[vin]),
      p1DiagnosticText1 = self.__store__.load_Text(self.p1DiagnosticText1.ndarray[vin]),
      p1DiagnosticText2 = self.__store__.load_Text(self.p1DiagnosticText2.ndarray[vin]),
      p1DiagnosticText3 = self.__store__.load_Text(self.p1DiagnosticText3.ndarray[vin]),
    )

```

原文件行 5347–5408：

```python
class SeqOf_P1DiagnosticStorage(DbaStruct):
  __adt__ = list[P1DiagnosticStorage.__adt__]

  def __arm_store__(self, store: DbaStore, sp: str):
    self.__anchor__ = DbArray(store.root_dir, f"{sp}/anchor", intp)
    self.p1DiagnosticDouble1 = DbArray(store.root_dir, os.path.join(sp, "p1DiagnosticDouble1::Double"), f8)
    self.p1DiagnosticInt1 = DbArray(store.root_dir, os.path.join(sp, "p1DiagnosticInt1::Int64"), i8)
    self.p1DiagnosticInt2 = DbArray(store.root_dir, os.path.join(sp, "p1DiagnosticInt2::Int64"), i8)
    self.p1DiagnosticInt3 = DbArray(store.root_dir, os.path.join(sp, "p1DiagnosticInt3::Int64"), i8)
    self.p1DiagnosticSource = DbArray(store.root_dir, os.path.join(sp, "p1DiagnosticSource::Text$Data.Text"), intp)
    self.p1DiagnosticKind = DbArray(store.root_dir, os.path.join(sp, "p1DiagnosticKind::Text$Data.Text"), intp)
    self.p1DiagnosticText1 = DbArray(store.root_dir, os.path.join(sp, "p1DiagnosticText1::Text$Data.Text"), intp)
    self.p1DiagnosticText2 = DbArray(store.root_dir, os.path.join(sp, "p1DiagnosticText2::Text$Data.Text"), intp)
    self.p1DiagnosticText3 = DbArray(store.root_dir, os.path.join(sp, "p1DiagnosticText3::Text$Data.Text"), intp)

  def count(self) -> int:
    return self.__anchor__.len1d

  def load(self, vin: int) -> __adt__:
    aa = self.__anchor__.ndarray
    i_next = aa[vin]
    i_start = aa[vin - 1] if vin > 0 else 0
    if i_next <= i_start:
        return []
    return [
        P1DiagnosticStorage.__adt__(
            p1DiagnosticDouble1 = p1DiagnosticDouble1,
            p1DiagnosticInt1 = p1DiagnosticInt1,
            p1DiagnosticInt2 = p1DiagnosticInt2,
            p1DiagnosticInt3 = p1DiagnosticInt3,
            p1DiagnosticSource = p1DiagnosticSource,
            p1DiagnosticKind = p1DiagnosticKind,
            p1DiagnosticText1 = p1DiagnosticText1,
            p1DiagnosticText2 = p1DiagnosticText2,
            p1DiagnosticText3 = p1DiagnosticText3,
        ) for (
            p1DiagnosticDouble1,
            p1DiagnosticInt1,
            p1DiagnosticInt2,
            p1DiagnosticInt3,
            p1DiagnosticSource,
            p1DiagnosticKind,
            p1DiagnosticText1,
            p1DiagnosticText2,
            p1DiagnosticText3,
        ) in zip(
            self.p1DiagnosticDouble1.ndarray[i_start:i_next],
            self.p1DiagnosticInt1.ndarray[i_start:i_next],
            self.p1DiagnosticInt2.ndarray[i_start:i_next],
            self.p1DiagnosticInt3.ndarray[i_start:i_next],
            (self.__store__.load_Text(tvin) for tvin in
             self.p1DiagnosticSource.ndarray[i_start:i_next]),
            (self.__store__.load_Text(tvin) for tvin in
             self.p1DiagnosticKind.ndarray[i_start:i_next]),
            (self.__store__.load_Text(tvin) for tvin in
             self.p1DiagnosticText1.ndarray[i_start:i_next]),
            (self.__store__.load_Text(tvin) for tvin in
             self.p1DiagnosticText2.ndarray[i_start:i_next]),
            (self.__store__.load_Text(tvin) for tvin in
             self.p1DiagnosticText3.ndarray[i_start:i_next]),
        )
    ]

```

原文件行 5611–5647：

```python
class P1WallOccurrenceStorage(DbaStruct):
  __adt__ = namedtuple("P1WallOccurrenceStorage", [ "p1WallOccurrenceLocalNo", "p1WallLifecycleOccurredAt", "p1WallBandLow", "p1WallBandHigh", "p1WallCore", "p1WallOccurrenceRef", "p1WallLifecycleSide", "p1WallLifecycleChangeKind", "p1WallBandMeasurementKind", "p1WallBandMeasurementReason", "p1WallPresence", "p1WallEndReason", "p1WallLifecycleAvailability", ])

  def __arm_store__(self, store: DbaStore, sp: str):
    self.p1WallOccurrenceLocalNo = DbArray(store.root_dir, os.path.join(sp, "p1WallOccurrenceLocalNo::Int64"), i8)
    self.p1WallLifecycleOccurredAt = DbArray(store.root_dir, os.path.join(sp, "p1WallLifecycleOccurredAt::Int"), i8)
    self.p1WallBandLow = DbArray(store.root_dir, os.path.join(sp, "p1WallBandLow::Double"), f8)
    self.p1WallBandHigh = DbArray(store.root_dir, os.path.join(sp, "p1WallBandHigh::Double"), f8)
    self.p1WallCore = DbArray(store.root_dir, os.path.join(sp, "p1WallCore::Double"), f8)
    self.p1WallOccurrenceRef = DbArray(store.root_dir, os.path.join(sp, "p1WallOccurrenceRef::Text$Data.Text"), intp)
    self.p1WallLifecycleSide = DbArray(store.root_dir, os.path.join(sp, "p1WallLifecycleSide::Text$Data.Text"), intp)
    self.p1WallLifecycleChangeKind = DbArray(store.root_dir, os.path.join(sp, "p1WallLifecycleChangeKind::Text$Data.Text"), intp)
    self.p1WallBandMeasurementKind = DbArray(store.root_dir, os.path.join(sp, "p1WallBandMeasurementKind::Text$Data.Text"), intp)
    self.p1WallBandMeasurementReason = DbArray(store.root_dir, os.path.join(sp, "p1WallBandMeasurementReason::Text$Data.Text"), intp)
    self.p1WallPresence = DbArray(store.root_dir, os.path.join(sp, "p1WallPresence::Text$Data.Text"), intp)
    self.p1WallEndReason = DbArray(store.root_dir, os.path.join(sp, "p1WallEndReason::Text$Data.Text"), intp)
    self.p1WallLifecycleAvailability = DbArray(store.root_dir, os.path.join(sp, "p1WallLifecycleAvailability::Text$Data.Text"), intp)

  def count(self) -> int:
    return self.p1WallOccurrenceLocalNo.len1d

  def load(self, vin: int) -> __adt__:
    return self.__adt__(
      p1WallOccurrenceLocalNo = self.p1WallOccurrenceLocalNo.ndarray[vin],
      p1WallLifecycleOccurredAt = self.p1WallLifecycleOccurredAt.ndarray[vin],
      p1WallBandLow = self.p1WallBandLow.ndarray[vin],
      p1WallBandHigh = self.p1WallBandHigh.ndarray[vin],
      p1WallCore = self.p1WallCore.ndarray[vin],
      p1WallOccurrenceRef = self.__store__.load_Text(self.p1WallOccurrenceRef.ndarray[vin]),
      p1WallLifecycleSide = self.__store__.load_Text(self.p1WallLifecycleSide.ndarray[vin]),
      p1WallLifecycleChangeKind = self.__store__.load_Text(self.p1WallLifecycleChangeKind.ndarray[vin]),
      p1WallBandMeasurementKind = self.__store__.load_Text(self.p1WallBandMeasurementKind.ndarray[vin]),
      p1WallBandMeasurementReason = self.__store__.load_Text(self.p1WallBandMeasurementReason.ndarray[vin]),
      p1WallPresence = self.__store__.load_Text(self.p1WallPresence.ndarray[vin]),
      p1WallEndReason = self.__store__.load_Text(self.p1WallEndReason.ndarray[vin]),
      p1WallLifecycleAvailability = self.__store__.load_Text(self.p1WallLifecycleAvailability.ndarray[vin]),
    )

```

原文件行 5649–5729：

```python
class SeqOf_P1WallOccurrenceStorage(DbaStruct):
  __adt__ = list[P1WallOccurrenceStorage.__adt__]

  def __arm_store__(self, store: DbaStore, sp: str):
    self.__anchor__ = DbArray(store.root_dir, f"{sp}/anchor", intp)
    self.p1WallOccurrenceLocalNo = DbArray(store.root_dir, os.path.join(sp, "p1WallOccurrenceLocalNo::Int64"), i8)
    self.p1WallLifecycleOccurredAt = DbArray(store.root_dir, os.path.join(sp, "p1WallLifecycleOccurredAt::Int"), i8)
    self.p1WallBandLow = DbArray(store.root_dir, os.path.join(sp, "p1WallBandLow::Double"), f8)
    self.p1WallBandHigh = DbArray(store.root_dir, os.path.join(sp, "p1WallBandHigh::Double"), f8)
    self.p1WallCore = DbArray(store.root_dir, os.path.join(sp, "p1WallCore::Double"), f8)
    self.p1WallOccurrenceRef = DbArray(store.root_dir, os.path.join(sp, "p1WallOccurrenceRef::Text$Data.Text"), intp)
    self.p1WallLifecycleSide = DbArray(store.root_dir, os.path.join(sp, "p1WallLifecycleSide::Text$Data.Text"), intp)
    self.p1WallLifecycleChangeKind = DbArray(store.root_dir, os.path.join(sp, "p1WallLifecycleChangeKind::Text$Data.Text"), intp)
    self.p1WallBandMeasurementKind = DbArray(store.root_dir, os.path.join(sp, "p1WallBandMeasurementKind::Text$Data.Text"), intp)
    self.p1WallBandMeasurementReason = DbArray(store.root_dir, os.path.join(sp, "p1WallBandMeasurementReason::Text$Data.Text"), intp)
    self.p1WallPresence = DbArray(store.root_dir, os.path.join(sp, "p1WallPresence::Text$Data.Text"), intp)
    self.p1WallEndReason = DbArray(store.root_dir, os.path.join(sp, "p1WallEndReason::Text$Data.Text"), intp)
    self.p1WallLifecycleAvailability = DbArray(store.root_dir, os.path.join(sp, "p1WallLifecycleAvailability::Text$Data.Text"), intp)

  def count(self) -> int:
    return self.__anchor__.len1d

  def load(self, vin: int) -> __adt__:
    aa = self.__anchor__.ndarray
    i_next = aa[vin]
    i_start = aa[vin - 1] if vin > 0 else 0
    if i_next <= i_start:
        return []
    return [
        P1WallOccurrenceStorage.__adt__(
            p1WallOccurrenceLocalNo = p1WallOccurrenceLocalNo,
            p1WallLifecycleOccurredAt = p1WallLifecycleOccurredAt,
            p1WallBandLow = p1WallBandLow,
            p1WallBandHigh = p1WallBandHigh,
            p1WallCore = p1WallCore,
            p1WallOccurrenceRef = p1WallOccurrenceRef,
            p1WallLifecycleSide = p1WallLifecycleSide,
            p1WallLifecycleChangeKind = p1WallLifecycleChangeKind,
            p1WallBandMeasurementKind = p1WallBandMeasurementKind,
            p1WallBandMeasurementReason = p1WallBandMeasurementReason,
            p1WallPresence = p1WallPresence,
            p1WallEndReason = p1WallEndReason,
            p1WallLifecycleAvailability = p1WallLifecycleAvailability,
        ) for (
            p1WallOccurrenceLocalNo,
            p1WallLifecycleOccurredAt,
            p1WallBandLow,
            p1WallBandHigh,
            p1WallCore,
            p1WallOccurrenceRef,
            p1WallLifecycleSide,
            p1WallLifecycleChangeKind,
            p1WallBandMeasurementKind,
            p1WallBandMeasurementReason,
            p1WallPresence,
            p1WallEndReason,
            p1WallLifecycleAvailability,
        ) in zip(
            self.p1WallOccurrenceLocalNo.ndarray[i_start:i_next],
            self.p1WallLifecycleOccurredAt.ndarray[i_start:i_next],
            self.p1WallBandLow.ndarray[i_start:i_next],
            self.p1WallBandHigh.ndarray[i_start:i_next],
            self.p1WallCore.ndarray[i_start:i_next],
            (self.__store__.load_Text(tvin) for tvin in
             self.p1WallOccurrenceRef.ndarray[i_start:i_next]),
            (self.__store__.load_Text(tvin) for tvin in
             self.p1WallLifecycleSide.ndarray[i_start:i_next]),
            (self.__store__.load_Text(tvin) for tvin in
             self.p1WallLifecycleChangeKind.ndarray[i_start:i_next]),
            (self.__store__.load_Text(tvin) for tvin in
             self.p1WallBandMeasurementKind.ndarray[i_start:i_next]),
            (self.__store__.load_Text(tvin) for tvin in
             self.p1WallBandMeasurementReason.ndarray[i_start:i_next]),
            (self.__store__.load_Text(tvin) for tvin in
             self.p1WallPresence.ndarray[i_start:i_next]),
            (self.__store__.load_Text(tvin) for tvin in
             self.p1WallEndReason.ndarray[i_start:i_next]),
            (self.__store__.load_Text(tvin) for tvin in
             self.p1WallLifecycleAvailability.ndarray[i_start:i_next]),
        )
    ]

```

原文件行 5731–5744：

```python
class MulWrap_P1WallOccurrenceStorage(DbaStruct):
  __adt__ = namedtuple("MulWrap_P1WallOccurrenceStorage", [ "mul", ])

  def __arm_store__(self, store: DbaStore, sp: str):
    self.mul = DbArray(store.root_dir, os.path.join(sp, "mul::[P1WallOccurrenceStorage]"), intp)
    self.mul_seq = store.arm_seq("[P1WallOccurrenceStorage]", SeqOf_P1WallOccurrenceStorage)

  def count(self) -> int:
    return self.mul.len1d

  def load(self, vin: int) -> __adt__:
    return self.__adt__(
      mul = self.mul_seq.load(self.mul.ndarray[vin]),
    )

```

原文件行 5746–5768：

```python
class SeqOf_MulWrap_P1WallOccurrenceStorage(DbaStruct):
  __adt__ = list[MulWrap_P1WallOccurrenceStorage.__adt__]

  def __arm_store__(self, store: DbaStore, sp: str):
    self.__anchor__ = DbArray(store.root_dir, f"{sp}/anchor", intp)
    self.mul = DbArray(store.root_dir, os.path.join(sp, "mul::[P1WallOccurrenceStorage]"), intp)
    self.mul_seq = store.arm_seq("[P1WallOccurrenceStorage]", SeqOf_P1WallOccurrenceStorage)

  def count(self) -> int:
    return self.__anchor__.len1d

  def load(self, vin: int) -> __adt__:
    aa = self.__anchor__.ndarray
    i_next = aa[vin]
    i_start = aa[vin - 1] if vin > 0 else 0
    if i_next <= i_start:
        return []
    return [
        MulWrap_P1WallOccurrenceStorage.__adt__(
        ) for (
        ) in zip(
        )
    ]

```

原文件行 6143–6156：

```python
class MulWrap_P1DiagnosticStorage(DbaStruct):
  __adt__ = namedtuple("MulWrap_P1DiagnosticStorage", [ "mul", ])

  def __arm_store__(self, store: DbaStore, sp: str):
    self.mul = DbArray(store.root_dir, os.path.join(sp, "mul::[P1DiagnosticStorage]"), intp)
    self.mul_seq = store.arm_seq("[P1DiagnosticStorage]", SeqOf_P1DiagnosticStorage)

  def count(self) -> int:
    return self.mul.len1d

  def load(self, vin: int) -> __adt__:
    return self.__adt__(
      mul = self.mul_seq.load(self.mul.ndarray[vin]),
    )

```

原文件行 6158–6180：

```python
class SeqOf_MulWrap_P1DiagnosticStorage(DbaStruct):
  __adt__ = list[MulWrap_P1DiagnosticStorage.__adt__]

  def __arm_store__(self, store: DbaStore, sp: str):
    self.__anchor__ = DbArray(store.root_dir, f"{sp}/anchor", intp)
    self.mul = DbArray(store.root_dir, os.path.join(sp, "mul::[P1DiagnosticStorage]"), intp)
    self.mul_seq = store.arm_seq("[P1DiagnosticStorage]", SeqOf_P1DiagnosticStorage)

  def count(self) -> int:
    return self.__anchor__.len1d

  def load(self, vin: int) -> __adt__:
    aa = self.__anchor__.ndarray
    i_next = aa[vin]
    i_start = aa[vin - 1] if vin > 0 else 0
    if i_next <= i_start:
        return []
    return [
        MulWrap_P1DiagnosticStorage.__adt__(
        ) for (
        ) in zip(
        )
    ]

```

