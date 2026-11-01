# Python / Numba 到 DBA / Haskell 的业务产品交接

## 0. 用途

本文适用于 Python 或 Numba 形成数值和稀疏事件，随后经 DBA/fields 交给 Haskell typed ingress，恢复成 DSU input occurrence、上游正式 product 或有明确身份的业务类型。

它不要求 Python 输出复杂的 Haskell 对象。Python 侧要做的是：把数值、时间、来源、有效性和版本信息表达清楚，使 Haskell 不需要猜。

## 1. 交接物至少包含什么

每次跨工作区交接至少固定：

```text
生产代码版本；
字段表版本；
小型 fixture；
fixture 生成方式；
字段类型、单位和缺失含义；
同一业务对象多行时的顺序；
Python 本地编号的有效范围；
预期 Haskell 解码结果；
尚未完成的部分。
```

聊天里的字段名或一张临时 DataFrame 不能替代这份交接物。

## 2. Python / Numba 侧需要保证什么

### 2.1 输出业务事实，不输出含混容器

每个字段都应能回答：

- 它表示哪个业务事实；
- 数值单位是什么；
- 何时形成；
- 当前是否可用；
- 缺失、尚未形成、确实为零是否不同；
- 来自哪段上游材料；
- 修正后怎样识别旧值和新值。

正式 wrapper 不使用 `object` dtype 承载混合业务语义。枚举和标签应使用完整编码表，不能一半字符串、一半整数。

### 2.2 本地编号不是长期业务身份

`wall_id`、`segment_id`、`track_id` 等编号若只在一次 replay、一个 chunk 或一个 producer 内有效，必须明确标为本地编号。

长期 DSU identity 可以在 Haskell 的 DSU owner 侧形成，但 Python 需要提供足够的来源事实，例如：

- 品种和方向；
- 业务时间范围；
- 所属 Wall 或活动生命；
- producer 给出的 replacement / split / merge 关系；
- 精确 revision 或来源版本；
- 能证明同一生命延续的 source lineage。

不能只因两个时间段接近，就让下游继承同一长期身份。

### 2.3 时间至少区分业务时间和工程形成时间

如果一个事实的业务锚点发生在过去、系统后来才确认，应分别保留：

- 业务锚点时间；
- 观察或确认时间；
- 必要时的结束、定稿或修正时间。

不能用确认时刻覆盖业务锚点，也不能把后来才知道的事实伪装成当时已经知道。

### 2.4 有效性不能塞进数值 0

至少区分：

```text
available；
missing；
not yet formed / pending；
not applicable；
calculation unavailable；
invalid / stale。
```

具体编码由当前任务决定，但所有消费者必须得到同一解释。

### 2.5 先判断数据密度，再决定是否跨语言

业务文档中的 `A → B` 表示形成和消费关系，不自动表示 A 的每一行内部材料都要经 DBA 送入 Haskell。

生产路径若仍需要：

- 完整逐 tick / 逐 half-second stream；
- 多成员同一时点的 dense matrix；
- `member × time` 或 `pair × time` 扫描；
- 高频 working state，但只产生少量正式变化；

应优先在 Numba 或同等高吞吐层完成必要计算和稀疏化，再传 lifecycle delta、milestone、bounded summary 或 proposal。具体切口由实现者根据真实数据量、调用频率、复用性和代码复杂度决定，不能仅按产品名或包名划 Python/Haskell。

dense DataFrame 可作为诊断、fixture、Aidata 或离线复核产物并落 DBA，但“可落库”不等于“应成为 live FRP 主输入”。正式交接说明必须分别列出：Numba 内部 dense 材料、可选诊断产物、生产跨语言输入。

计算位置不改变 canonical owner。Haskell/FRP 侧的 stable identity、revision、correction 和 public lifecycle 不能因为数值 kernel 下沉而丢失；Python/Numba 与 Haskell 也不能各自维护一套竞争的正式结果。

## 3. DBA 层需要保证什么

物理上可以一表或多表，但必须做到：

- 不同业务产品可无损区分；
- 精确整数、时间、枚举和浮点不会在存取中悄悄变形；
- 同一业务身份的多行记录有稳定排序；
- revision、来源和修正关系不会丢失；
- diagnostics 与正式产品分开；
- 字段表版本和 fixture 可以追溯到生产代码版本。

DBA 只负责承载，不替 producer 或 Haskell 补业务事实。

## 4. Haskell 侧的恢复要求

Haskell typed ingress 应把 DBA 字段尽早恢复成具名业务类型、DSU input occurrence 或正式上游 product，而不是让 DSU.process 和 Local CEPS 长期读取无类型字段表。

恢复时检查：

- 必填字段是否存在；
- 枚举编码是否完整；
- 单位和范围是否合法；
- 时间顺序是否满足任务合同；
- 本地编号的有效范围；
- revision 和来源关系是否闭合；
- 不可用状态是否被错误解释成 0；
- 同一业务对象多行是否保持正确顺序。

恢复失败应给出具体产品、字段和记录位置，不能静默填默认业务值。

## 5. Haskell 再交回 Python

为了实现和检查中间链路，可以在最终 P8 产品之前增加较薄的 Python 包装。它可以暴露：

- 当前 Haskell 业务对象；
- 关键 revision 和来源；
- 状态变化；
- 便于核对的小型 `DataFrame`；
- 诊断和测试信息。

这不是提前实现最终 Aidata 产品，也不需要 Haskell 输出复杂对象再由 Numba 承载。

## 6. 最小核对样例

小型 fixture 至少覆盖：

1. 正常单对象；
2. 同一业务对象多行；
3. 明确为零；
4. 缺失或尚未形成；
5. 精确整数和边界浮点；
6. 时间锚点与确认时间不同；
7. 同一身份的新 revision；
8. split、merge 或 retract 中当前任务涉及的最小例子。

核对内容：

```text
Python 产出
→ DBA 保存
→ Haskell 恢复
→ Haskell 形成最小结果
→ Python 读取
```

前后字段、精度、缺失状态、时间、身份和 revision 关系应一致。

## 7. Agent 可以决定和不能决定的内容

Agent 可以决定：

- 表拆分；
- 内部字段名；
- Haskell ADT 和 Python wrapper 组织；
- 编解码 helper；
- fixture 和测试框架；
- 性能与缓存方式。

Agent 不能决定：

- 缺失是否等于零；
- 哪个来源事实构成业务身份；
- split / merge 后谁继承旧身份；
- 哪个时间是业务锚点；
- producer 没提供的业务事实由 consumer 猜出来；
- 为了方便解码删掉冻结合同要求的字段。
