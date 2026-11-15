# 03C runtime shape and hotpath checks

## 0. 用途

这份文档收录 pre-L0 review checks 中，与 stateful / assembler 的运行形态、checkpoint 稀疏性、热路径对象分配最相关的规则。


## 1. 规则目录

### PCHK-007 stateful / assembler 的 checkpoint 默认应是稀疏的

- 风险：
  - `checkpoint_assert` 被误实现成“每 tick 默认输出一条 checkpoint”
- 程序性检查建议：
  - 若 `chunk_checkpoints` 行数和 `n_ticks` 同量级，默认报警
  - 默认检查点应优先只包含：
    - chunk start
    - chunk end
    - state change
    - event emission

### PCHK-008 热路径不得靠长度为 1 的 ndarray / dict 拆箱驱动

- 风险：
  - assembler streaming loop 内每 tick 做 `np.array([x])`、小 dict 返回、`[0]` 拆箱，容易退化成高对象分配实现
- 程序性检查建议：
  - 对 stateful 主循环做静态 grep：
    - `np.array([`
    - 每 tick 小 dict 返回
    - 对长度 1 数组的 `[0]` 拆箱
  - 若这些模式位于主循环内部，则报警

### PCHK-009 不得把完整 dense 流搬到 FRP 后再逐格扫描

- 风险：
  - 业务形成图被误当成物理传输图；
  - 为了在 Haskell 形成后续产品，把完整 multi-series half-second stream 或 member-pair dense matrix 经 DBA 搬入 FRP；
  - Numba 只负责物化大表，没有完成平台原本需要的高吞吐计算和稀疏化。
- 检查：
  - 列出 `rows per UTI / rows per replay / member count / pair count`；
  - 标出仍做 `member × time`、`pair × time` 扫描的步骤；
  - 标出正式跨语言输入的预期密度；
  - dense 输出若只服务 fixture、Aidata、诊断或离线复核，应与 live FRP ingress 分开；
  - 若正式输出很稀疏但跨界输入仍与 tick 数同量级，默认要求重新检查边界。

本规则不预先裁定某个业务对象必须在哪种语言实现；它只禁止把已知不适合 FRP 的完整密集扫描推到 FRP 主路径。

### PCHK-010 稀疏事件不得按 occurrence 构造 Pandas 小表

- 风险：
  - 输入行数小于 dense Tick 数，就被误判为天然低成本；
  - 对每个 `(uti, side)`、segment 或其他 occurrence 执行 `groupby` 子表迭代、布尔筛选和 Series 取值；
  - 短 tape 或低事件密度年份运行正常，但完整历史的高密度区间按事件组数 `E` 产生数百万个 Python/Pandas 小对象。
- 程序性检查建议：
  - 除 `n_ticks` 外，同时报告 sparse rows、唯一 group／occurrence 数和每段耗时；
  - 检查 production caller 中按 group 执行的 `DataFrame.groupby`、`DataFrame.__getitem__`、小 dict／小表构造；
  - 比较分段耗时分别与 Tick 数 `T`、事件组数 `E` 的相关关系；
  - 对真实高密度区间做微测，不能只用平均密度或单一年份通过 Gate；
  - 业务等价时优先一次性 `searchsorted`／整数位置映射，加固定 dtype 数组上的粗粒度 Numba 或向量化归并。

本规则不授权合并或删除公开业务流。跨 lane 的局部归并只能发生在已有 consumer 的私有输入边界，并且必须保持信息无损与原 fail-closed 语义。


## 2. 使用建议

这组规则主要服务于：

- implement 自查
- review 时的工程形态核对
- 后续轻量性能风险扫描
