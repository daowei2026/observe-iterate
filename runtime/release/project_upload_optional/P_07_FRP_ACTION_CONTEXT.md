# FRP Action Refinement：Action Node、上下文、状态与参数组织

## 0. 本文解决什么

本文把项目中的 **Action Refinement Protocol** 落到 Haskell / FRP 工程写法。业务任务写清字段和规则后，实现仍会遇到：

- 一层层函数重复传很多参数；
- 只读环境、事件状态和正式对象状态混在一起；
- 锚点时间、确认时间和修正时间混在一起；
- 为了“可配置”把所有 helper 都暴露成参数；
- 想使用 Monad 等表达，但不知道哪些属于工程判断。

本文不把 Action Refinement 改写成普通“函数拆分”。它要求先识别业务 Action Node，再说明节点归哪个 DSU / Local CEPS、能读什么、维护什么、产生什么，以及哪些内容才属于可替换方法参数面。

本文给出工程组织方法，不替业务材料决定候选、优先级、缺失含义或提交规则。

## 1. 先区分四种运行语义

### 1.1 monad-like context / capability：动作获准读取的上下文与能力

某个动作被允许读取的范围，例如：

- 当前观察对象和窗口；
- 当前方法绑定；
- 上游正式输出；
- 只读规则和单位；
- 当前实例允许看的通道。

重点是“这个 Action Node 能看什么、不能看什么、能发出什么效果”。capability 是业务授权边界，不等于某个具体 Haskell typeclass 或 Monad stack。

### 1.2 Dynamic / event state：随 occurrence 变化的私有状态

例如当前候选链、尚未结束的窗口、累积统计和未提交判断。重点是：

- 新事件到来怎样更新；
- 什么时候清空；
- 什么时候产生一个输出。

### 1.3 public ledger lifecycle：下游可读的 DSU product 生命周期

例如 candidate、committed、final、corrected 等正式 DSU product 生命。它会影响下游何时可读、修正后怎样产生新 revision，不能当普通 Dynamic state 静默覆盖。

### 1.4 instance identity guard：DSU 实例隔离

业务上应先说“同一 Wall 业务生命、同一 Battle / DSU instance、同一观察实例”，并说明它们归哪个 DSU owner。`ctx_key`、内部编号或 map key 只是实现这些 guard 的办法，不是业务主语。

这四类不能全部塞进一个万能 context，也不能全部藏进一个 Monad stack：

- capability 说明允许读写什么；
- Dynamic / event state 说明事件到来时怎样变化；
- public ledger lifecycle 说明正式 product 怎样被下游观察和修正；
- instance identity guard 说明本次变化属于哪个 DSU instance。

## 2. 先识别 Action Node，再写 Per-DSU Process Card

Action Node 是有业务含义的动作节点，不是任意 helper。常见类型包括：Scope / Observation、Candidate Generation、Filter / Gate、Group / Segment / Cluster、Rank / Select / Resolve、Project / Derive、Aggregate / Reduce / Score、Commit / Publish / Lifecycle、Consume / Guard、Diagnostics / Evidence。

不用为每个小 helper 写卡。凡是影响 DSU product、DSU Payload、时间、修正或跨 DSU 交接的 Action Node，都应挂回某个 DSU 的 Local CEPS / process，并至少说明：

```text
Action Node 的中文业务动作；
所属 DSU / Local CEPS；
什么时候运行；
允许读取哪些 capability，禁止读取什么；
自己维护哪些 Dynamic / event state；
occurrence 到来时怎样更新；
输出什么 private result / DSU product / diagnostic；
涉及哪些业务时间；
是否推进 public ledger lifecycle；
通过哪条 Global CEPS edge 或 CBPS role 交给谁；
当前实现保留什么替换空间。
```

Action Node 可以在 setup-time、event-time、窗口结束时或 correction 时运行；这些标签可以同时出现，不需要强行互斥分类。

复杂纵切的检查顺序应是：DSU-only containment → Global CEPS dataflow → Local CEPS / Action Nodes → Per-DSU Process Card → CBPS role，而不是先画一棵脱离 DSU owner 的函数树。

## 3. Action Refinement 后再组织函数参数

### 3.1 按含义聚合，不按方便塞进万能上下文

优先分成：

```text
capability / 只读业务环境；
当前 input occurrence；
该 DSU 自己的 Dynamic / event state；
当前方法配置；
本次 public ledger transition、output occurrence 和 diagnostic。
```

每组使用有业务名字的记录类型。不要把整个应用环境、所有上游 DSU、public lifecycle、技术 key 和调试开关放进一个万能记录或 Monad context。

### 3.2 Action Node 树和可替换方法参数面不是一回事

业务动作可以细化成很多 Action Node，但只有真正允许不同 use case / method binding 替换的部分，才进入公开的可替换方法参数面。

不应暴露：

- 固定业务不变量；
- 排序、遍历、缓存等工程 helper；
- 正式输出的机械拼装；
- 没有业务选择意义的内部函数。

可以暴露：

- 当前任务明确允许替换的方法；
- 不同用例会采用不同规则的方法；
- 当前只有临时方法、未来需要替换的方法；
- 会改变正式输出但已由任务包给出选项的方法。

### 3.3 每个可替换方法参数位至少保持稳定输入输出

方法合同卡应说明：

- 它回答哪个业务问题；
- 输入需要哪些业务信息；
- 输出的稳定形状；
- 当前默认方法；
- 不变量；
- 不适用和缺输入时怎么办；
- 方法版本怎样记录。

具体函数类型、typeclass 和模块组织由实现者决定。固定业务动作、v0 default、future placeholder 和真正的 replaceable method slot 必须区分，不能为了“可配置”全做成参数。

## 4. 什么时候值得把 capability 落成 Monad 或更高阶表达

Action Refinement 先确定 capability 和状态边界；Haskell 表达随后选择。不要因为 Haskell 支持 Monad 就先设计一套抽象。出现以下重复时，可以考虑局部使用 Reader、State、Writer、Except、能力 typeclass 或自定义业务组合：

- 多个相邻动作反复读取同一只读业务环境；
- 一组动作连续更新同一对象状态；
- 每一步都要积累相同格式的诊断和来源；
- 多个分支都需要一致处理 pending、unavailable 或 correction；
- 一段业务流程需要组合多种可替换方法，但对外仍保持同一合同。

采用前检查：

1. 抽象后业务动作名字是否更清楚；
2. 状态所有者是否仍然可见；
3. 正式输出和私有状态是否仍分开；
4. 锚点、确认、定稿和修正时间是否仍可追踪；
5. reviewer 是否能从局部代码看出输入、更新和输出；
6. 是否至少在一个完整业务流程中真实减少了重复。

不应为了统一形式把整个 Segmentor、长期 DSU ledger、instance identity 和所有 capability 放进一个巨大 Monad，也不应让 effect 名称替代 Action Node 的业务名字。

### 4.1 高阶表达不能反向扩大 FRP 输入

Haskell 中的 `FrozenCut → proposals → atomic commit`、局部 Monad 或其他组合表达，服务的是已经适合进入 FRP 的业务材料。它们不是把完整 multi-series half-second dense stream 或 `pair × UTI` 扫描搬进 FRP 的理由。

如果 Action Node 的输入仍是完整密集流，先判断其高吞吐计算和稀疏化是否应在 Numba 完成；FRP 再对稀疏 proposal/delta 做受限读取、身份管理、关系组合、correction 和公共提交。具体边界由实现者根据真实代码判断，但不得通过漂亮的 Haskell 抽象隐藏跨界数据量。

## 5. CEPS 事件顺序、因果时间与 public lifecycle

业务锚点在过去、后来确认时，应在类型或结果中同时保留锚点和确认时间。事件流实现不得：

- 使用未来窗口结果决定过去时刻当时可见的状态；
- 把 batch 后处理结果伪装成实时已知；
- 因 replay 重复发出同一业务事件；
- 让本次刚写入的历史状态立即成为本次判断自己的输入。

需要历史反馈时，Local CEPS / DSU.process 使用：

```text
读取旧状态
→ 运行本次判断
→ 形成输出
→ 写入新状态
```

## 6. 实现者自由和业务停止条件

实现者可以决定：

- 记录类型、和类型、Map、Set；
- fold、递归、图算法或状态组合；
- 私有 helper 和缓存；
- Monad/effect 的具体选型；
- 模块和测试组织。

以下内容若冻结材料未说明，不能由实现者猜：

- 候选资格和分组语义；
- 优先级和冲突处理；
- pending、missing、zero、unavailable 的区别；
- 哪个结果可以正式提交；
- identity、cardinality、split/merge；
- 下游可读范围；
- 修正后业务上应保留还是撤回什么。
