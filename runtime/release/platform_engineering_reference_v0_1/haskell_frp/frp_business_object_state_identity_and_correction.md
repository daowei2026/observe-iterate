# FRP 中 DSU / CEPS / CBPS 的状态、身份、版本与修正

## 0. 本文解决什么

本文说明怎样把 DSU 落到 Haskell / FRP 代码，并保持 DSU、CEPS、CBPS 三层关系清楚。Binder-facing 的物化对象是 DSU；CEPS 和 CBPS 不是另外两套平行对象系统，而是 DSU 的执行面和公共说话面。

本文沿用项目自己的正式语言：

| 项目术语 | 实现时回答的问题 |
|---|---|
| DSU | 谁在持续存在：它有什么 Payload、身份、状态生命、process、product、finality 和 revision。 |
| CEPS | DSU 怎样动：DSU 实例怎样响应 occurrence，怎样在 Global CEPS 中接线，DSU 内部是否使用 Local CEPS / processor / child DSU network。 |
| CBPS | DSU 什么时候向公共语义面说话：哪些 product 需要发布、订阅、历史回查、Context 汇编或以后动态解析。 |

一句话记：**DSU 是谁活着，CEPS 是它怎样动，CBPS 是它什么时候对外说话。**

实现时不需要先造一套脱离业务的“通用 DSU 框架”，但也不能把 DSU 弱化成普通 record 或含混的“业务对象”。应先按任务中的真实业务生命判断 DSU 边界，再决定它落成 materialized DSU、nested child DSU、父 DSU 拥有的 entity state、Local CEPS action、public product，还是 aggregate scope。

## 1. 先做 DSU materialization audit，不按图机械建模块

DSU-only 图表达业务 ownership / containment，但“图中一个节点”不自动等于“一个 Haskell 模块、一个顶层 catalog item 或一个 Global CEPS 节点”。每个候选先检查：

- 是否有自己的 Payload 或运行记忆；
- 是否响应输入 occurrence；
- 是否有独立 process；
- 是否产生可被下游稳定读取的 product；
- 是否有独立 instance life / finality；
- 是否有替换、重组、复用或审计价值；
- product 是否需要换 consumer、换解释器、换生成器或独立复用；
- 是否可能具有 CBPS eligibility。

检查后可落成：

| 落法 | 适用情况 |
|---|---|
| materialized DSU | 有独立 Payload、process、product、instance life，值得单独替换、复用或审计 |
| nested child DSU | 有自己的身份和状态生命，但由父 DSU containment 和调度 |
| owned entity state | 有业务身份和变化，但只需作为父 DSU Payload 中的有身份实体 |
| Local CEPS action / processor | 只是候选、过滤、分组、计算或提交动作，没有独立 DSU 生命 |
| public product / occurrence | 负责跨 DSU 交接，不因“被传递”就变成 DSU |
| aggregate scope | 只负责把一批 DSU / entity 纳入同一实例或观察范围 |

结论必须保留项目术语：它是哪个 DSU、归哪个 DSU owner、是否独立物化、process 在哪里、product 交给谁、是否有 CBPS role。不能只写成“一个普通对象”后丢掉 DSU ownership。

## 2. 每个 DSU 或 DSU-owned entity 至少写清什么

### 2.1 身份

- 哪些业务事实决定它是谁；
- 哪些技术编号只在一次 replay 或进程内有效；
- 同一对象更新时何时保留身份；
- split、merge、retract 或重新出现时何时产生新身份。

具体编码、数据库键和 hash 由实现者决定。不能只因时间接近就继承旧身份。

### 2.2 DSU Payload、当前正式状态和私有工作状态

明确区分：

- 下游可以读取的当前正式状态；
- 形成正式状态前的候选和累积状态；
- 只用于性能的缓存与索引；
- 只用于诊断和测试的轨迹。

下游只能按合同读取正式输出，不能穿透读取候选池、排序、缓存或上游内部 helper。

### 2.3 occurrence、DSU.process 和 CEPS 接线

每张 Per-DSU Process Card 和关键更新函数应能回答：

```text
收到什么 input occurrence；
通过哪条 Global CEPS edge 读取哪些上游 DSU product；
更新 DSU Payload 中的哪些状态；
是否产生新版本；
发出什么 output occurrence / product，交给哪些 consumer DSU；
哪些情况只保留为 pending 或 diagnostic。
```

DSU.process 可以使用普通纯函数、FRP 组合、状态转换函数、Local CEPS subgraph、child DSU network 或局部 Monad。具体实现可自由选择，但 DSU owner、状态变化、正式 product 和 forbidden reads 必须在代码中可见。

### 2.4 时间

至少按任务需要区分：

- 业务锚点时间；
- 事件到达时间；
- 系统确认或发出时间；
- 结束或定稿时间；
- 修正生效时间。

锚点发生在过去、后来才确认时，不能用确认时间覆盖锚点，也不能让下游在确认前看见未来信息。

### 2.5 DSU product、正式输出与 CBPS role

DSU product 至少包含任务要求的：

- 精确业务身份和版本；
- 当前业务状态；
- 知识成熟度或输入可用性；
- 来源和形成方法；
- 必要的版本替代关系；
- 下游真正需要的摘要。

业务状态、知识是否充分、输入是否可用、版本是否被修正是不同维度，不能压成一个枚举。

随后显式记录 publication role：

- 只给已知局部 consumer：优先使用 CEPS direct dataflow；
- 需要开放订阅、历史回查、Context 汇编或未来动态解析：声明 CBPS publish / subscribe role；
- 当前不发布：写明 none with reason，而不是含混省略。

CBPS 不是另一个平行系统，也不是只有最外层 DSU 才能使用；它是具体 DSU 的公共说话面。

## 3. 修正和重新计算

### 3.1 修正不是静默覆盖

旧输入被修改后，应能从新结果回到被替代的旧版本。常见结果：

```text
同一业务生命仍成立：
  保留业务身份，形成新版本。

旧业务生命不再成立：
  撤回旧对象，形成新身份或不再形成对象。

一拆多：
  旧对象停止作为当前对象，每个新连续生命使用新身份并指向旧父。

多并一：
  旧父对象停止作为当前对象，新对象使用新身份并指向全部父对象。
```

具体判据由当前任务包提供，工程文档不替业务材料决定。

### 3.2 只重算受影响范围

DSU 实现需要能找到：

```text
被修正的 source revision
→ 直接受影响的 DSU / DSU-owned entity
→ 通过 CEPS / CBPS 消费其 product 的下游 DSU
→ 需要形成的新版本或撤回。
```

可以用索引、依赖表、事件折叠或直接重放实现。第一版不要求通用增量计算平台。

### 3.3 完整 replay 的最低要求

在相同输入范围和相同方法版本下，完整 replay 应产生相同的：

- 业务身份；
- 状态变化顺序；
- split / merge / retract 关系；
- 正式输出；
- 版本替代关系。

中途宕机恢复、持久化格式和快照策略只有在任务要求时才成为验收内容。

## 4. CEPS direct dataflow 与 CBPS publication

已知的局部 producer DSU 与 consumer DSU 可以通过 Global CEPS direct dataflow 接线，不必都走 CBPS。关键不是是否直连，而是传递什么：

```text
正确：
  producer DSU product → CEPS edge → consumer DSU

错误：
  consumer DSU 拿到 producer DSU 内部对象 → 读私有缓存、候选或 helper
```

只有 product 需要开放订阅、历史查询、多个未知消费者、Context 汇编或动态解析时，才赋予该 DSU CBPS role。CBPS publication 不是所有 DSU 的默认工作。

## 5. 推荐的代码审阅面

reviewer 应能从 DSU 类型、Process Card、Global / Local CEPS 接线和 CBPS role table 看到：

- DSU 的业务名字和 owner；
- input occurrence；
- 当前正式状态；
- 私有工作状态；
- DSU.process / Local CEPS action；
- product 及 consumer；
- CBPS role 或 none with reason；
- 身份和版本关系；
- 业务锚点与确认时间；
- 修正和撤回。

不要让 `StateMap`、`RuntimeRef`、`payload` 等技术词遮住这些业务词。

## 6. 最小测试

每个有版本生命的 DSU 或 DSU-owned entity 至少覆盖：

1. 正常形成；
2. 重复输入不重复形成；
3. 相同输入 replay 结果一致；
4. pending 与明确为零不同；
5. 同一身份的新版本；
6. retract；
7. 当前任务涉及的 split 或 merge；
8. 不相关上游修正不会更新本对象；
9. 下游无法读取私有工作状态。
