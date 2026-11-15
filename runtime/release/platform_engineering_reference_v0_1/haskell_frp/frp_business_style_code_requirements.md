# FRP 部分（从 L0 / Segmentor 开始）的业务风格代码写法要求

> 适用范围：从 L0 / Segmentor 开始的 FRP / CEPS 节点实现。
>
> 目标：让实现出来的代码既能运行，也能让业务侧快速审阅“它是什么、它吃什么、它怎么定稿、哪里最容易写歪”。
>
> 使用方式：实现 AI 必须同时参考本文件与 `02.CEP_Example.md`。当两者在“函数参数应该站在哪一层”上存在张力时，以本文件 **3.1 / 3.2 / 5.2 / 5.3** 的分层规则与 `02.CEP_Example.md` 的呈现方式为准。

> 结构前提：本文沿用 DSU / CEPS / CBPS 与 Action Refinement 口径。DSU 是持续存在的业务单元；DSU instance 可以在 Global CEPS 中扮演 node；DSU.process 内部可以由 Local CEPS / Action Nodes 实现；需要公共语义发布时由具体 DSU 承担 CBPS role。本文所称“正式 CEPS 节点”，只指 materialized DSU 在 Global CEPS 中的正式节点，或任务明确要求独立导出的 Local CEPS node，不指每个普通 Action Node。

---

## 0. 本文件解决的核心问题

这里要求的不是一般性的“代码整洁”，而是 **业务可审阅性**。

对于 materialized DSU / 正式 CEPS node，业务侧最关心的通常不是：
- `Map` 怎么组织
- `Maybe` 怎么折叠
- helper 函数怎么抽
- 某个 `foldDyn` 写法是否最短

而是：
- 这个 DSU / node 在业务上到底是什么、归哪个 DSU owner
- 输入和输出在业务上分别代表什么
- 哪些逻辑是固定骨架，哪些是可变策略
- 当前值、候选值、最终提交值是否混在一起
- 用户可选的函数参数到底是什么，应该站在哪一层
- 数据世界给进来的运行时输入又是什么
- 参数到底控制什么，以及是在什么时候被采样/生效
- 这个节点最容易写歪的时间语义/边界语义是什么

因此，本文件要求代码刻意长成一种 **“先能审业务，再看实现细节”** 的形状。

---

## 1. 以 `02.CEP_Example.md` 为参考时，必须学到什么

`02.CEP_Example.md` 中最值得学习的，不是某个具体算法，而是它的呈现方式：

1. **业务词汇本体先站起来**  
   例如 `EnveEvaluator`、`OutSingleSideSurndEvaluator`、`EnveFilter` 等对象先被定义成有业务名字的对象，而不是先扔出一堆匿名逻辑。

2. **可变逻辑先站在具名构造子 / GADT 层**  
   例如 `OutSingleSideSurndByPDif1`、`OutSingleSideSurndByPVDif1`、`OutSingleSideByNATR` 这类写法，让人能直接看出“当前到底在用哪类业务策略”，并且构造子本身可继续携带该策略的静态旋钮。

3. **定义 / 输入 / 输出 / 详细解释 / 类型边界 / `processEvents` 放得比较近**  
   reviewer 不应为了拼出“它是什么”和“它怎么做”，在多个文件中往返跳转。

4. **运行时输入与静态策略分层清楚**  
   构造子字段表达“当前选的是哪类做法 + 该做法的静态旋钮”；`FrpEvent` / `FrpBehavior` / `FrpDynamic` 表达“输入世界当前给进来的值 / 信息”。两者不得混层。

5. **组合逻辑是可追踪的**  
   例如先做基础评估，再串联过滤器，逻辑顺序在代码里是可读的，而不是埋在多层 helper 中。

本文件接下来要求的“业务风格代码写法”，本质上就是把这些优点迁移到 L0 / Segmentor 及后续 FRP 节点中。

---

## 2. 关键术语定义（实现 AI 必须按这里理解）

### 2.1 业务词汇壳（business vocabulary shell）

指一个节点 / 对象在代码里先以 **业务词汇** 的形式被明确命名和解释，而不是先出现一个执行函数。

至少应包含：
- 词汇名（这个对象业务上是什么）
- 定义（它负责判断 / 生成什么）
- 输入
- 输出
- 详细解释（尤其是边界和时间语义）

### 2.2 可变策略位（strategy / policy slot）

指节点内部业务上允许替换的做法 / 规则族 / 绑定方式 / 资格方式 / 时间语义方式。

**硬规则**：这类“可变策略位”必须优先站在 **GADT / ADT 具名构造子家族层**，而不是退化成：
- 裸函数槽
- `String` / `Text` / 文本标签
- 无名 record 再靠字段解释“当前是哪种做法”

即使当前只有一个已实现 variant，也应保持“家族 + 当前单构造子”的形状；不要误导 reviewer 以为这是语义上唯一且闭合的做法。

### 2.3 DSU / 正式 CEPS 节点级契约（node-level contract）

每个 materialized DSU 在 Global CEPS 中扮演的正式节点，以及任务明确要求独立导出的 Local CEPS node，都应有独立可审的：
- `type Input`
- `type Output`
- `processEvents`

如果因为工程结构原因暂时不直接写成独立 `instance CEPS`，也必须提供等价的“节点级契约壳”，让 reviewer 一眼能看见本节点的 I/O 与处理责任。

普通 Local CEPS Action Node 不因此被强制提升成独立 CEPS instance。它应按 Action Refinement 文档挂回所属 DSU.process，并写 Per-DSU Process Card / Action Node card。

### 2.4 合同对象 / 投影槽位（historical alias: 父 pack / 子 pack）

历史讨论中曾使用“父 pack / 子 pack”术语。今后它们仅作为兼容旧讨论的别名存在，**不再构成推荐命名后缀**。

真正的规则是：
- 对外正式输入合同对象，应使用能表达业务角色的类型名
- 内部子路径 / 投影槽位，也应使用业务语义名
- 不要求统一使用 `Pack` 后缀
- 如果某对象只是合同容器，也不必强制命名为 `*Pack`

### 2.5 参数合同（param contract）

参数不只是“这个字段是什么类型”，而是要回答：
- 参数 key 是什么
- 属于谁
- 在总合同中的路径是什么
- 被哪个节点消费
- 在什么触发点被读取 / 生效
- 它影响哪个决策面

本文件使用如下字段名：
- `param_key`
- `owner`
- `recipe_ref`
- `consumed_by`
- `bind_at`
- `decision_surface`

### 2.6 `bind_at`

`bind_at` 只回答一件事：

> **运行时输入世界中的当前值，在什么触发点被读取。**

它适用于：
- `FrpBehavior` 当前值
- `FrpDynamic` 当前态
- 外部事件到达时读取的当前上下文

它 **不** 用于解释：
- GADT / 构造子字段中的静态策略选择
- 构造子自带的静态参数旋钮

如果某个静态字段为了执行层复用，被 very local 地适配成 `const Behavior`，也不得因此把它重新定义成“运行时参数合同”。

### 2.7 `working-state`

节点内部或局部子树内部使用的 **当前候选 / 当前运行状态**，还不是可以给下游当正式结构事实使用的对象。

### 2.8 `committed output`

可以被下游当作 **正式结构事实 / 正式边界 / 正式段对象** 消费的输出。

### 2.9 触发点 / 采样点

对于 FRP 节点，必须明确：
- 谁触发了本次计算
- 本次计算时采样的是哪个当前值 / 哪个 `Behavior`

例如：
- `sample_when = eResolutionEvidence`
- `sample_target = current dLastInteraction`

不能只写类型，不写采样时机。

---

## 3. 顶层分层规则（硬规则）

### 3.1 三层必须分清：策略层 / 输入世界层 / 合同层

必须区分以下三层：

1. **策略层（GADT / ADT / 具名构造子家族）**  
   表达：
   - 当前是哪类业务对象
   - 当前选了哪类策略 / 做法
   - 该做法自带哪些静态旋钮

2. **输入世界层（`FrpEvent` / `FrpBehavior` / `FrpDynamic`）**  
   表达：
   - 本次触发时输入世界给到的当前值 / 当前信息
   - 上游数据态 / 上游事件流

3. **合同层（对外正式合同对象 / 投影槽位 / 参数 manifest）**  
   表达：
   - 对外正式输入口
   - 内部投影路径
   - `param_key / owner / recipe_ref / consumed_by / bind_at`

### 3.2 用户可选函数参数 vs 数据输入，必须硬分

实现 AI 必须显式区分：

- **用户可选的函数参数 / 策略旋钮**：必须放到具名构造子 / GADT 层。
- **来自数据世界的输入**：例如 `FrpEvent`、`FrpBehavior`、`FrpDynamic`、上游事件、上游当前态，不得塞进策略构造子层。

当 `02.CEP_Example.md` 与某个用例文档在这里产生张力时，以这条为优先级更高的硬规则。

### 3.3 不能确定抽象层级时，也不得退回文本

如果当前还不能完全确定抽象层级或枚举族：
- 可以使用 **占位 ADT / GADT**
- 可以使用 `OPEN[contract]` / `PLACEHOLDER[data]` / `FROZEN` 等具名构造子
- 可以在 Haddock 中显式标明“抽象层级暂未冻结”

但 **不得退回 `String` / `Text`（即使包一层 newtype）来承担业务语义**。

---

## 4. 注释与 Haddock 规则（硬规则）

### 4.1 保留注释必须使用 Haddock 兼容格式

在生产业务模块中，所有保留性注释都必须使用 Haddock 兼容格式，例如：
- `-- |`
- `-- ^`
- `{-| ... -}`
- `{-^ ... -}`

普通 `--` 注释只允许用于：
- 临时本地调试说明
- 明确标注 `TEMP` / `TODO` / `DEBUG` 的短期注释

正式业务说明、合同说明、字段说明、函数参数说明，不得使用普通 `--` 行注释。

### 4.2 顶层声明必须有 Haddock

以下对象必须使用 Haddock：
- module header
- `data` / `newtype` / `type` / `class`
- 业务相关 top-level function
- record fields
- 关键构造子家族及其构造子
- pattern / instance（只要其业务语义需要 reviewer 直接看到）

### 4.3 每个 `data` / `newtype` / `type` 的每个 field 都必须有 Haddock

不允许“只给类型本体写注释，field 裸奔”。

对于 record fields，**最低必须**逐字段说明：
- 它在业务上表示什么

以下说明是 **按需添加**，不是机械必填：
- 它不是哪种东西（仅当该字段存在真实混淆风险时）
- 它属于 working-state / committed output / runtime input / static strategy 的哪一层（仅当从邻近类型、头卡或上下文中不明显时）

禁止为了凑格式而给所有字段机械追加：
- “它是 X，不是 Y”
- “它属于某层”但并未帮助消除任何真实歧义

换句话说：**字段 Haddock 必须先提供正向业务语义；防混淆说明只在真的会混淆时写。**

### 4.4 每个函数的每个输入 / 输出都必须有 Haddock 语义说明

不允许只有一句“这个函数做什么”，而不说明输入输出含义。

对于函数的 **每个输入** 与 **输出**，最低必须让 reviewer 一眼看出：
- 它在业务上表示什么

以下说明为 **按需补充**：
- 哪些输入来自数据世界
- 哪些输入是策略对象 / 构造子字段
- 返回值是 working-state 相关结果、committed output，还是纯辅助判断
- 若存在采样语义，补 `sample_when` / `sample_target` / `why_safe`

如果适合，优先使用 Haddock 对函数参数与返回值逐箭头标注的写法；  
若逐箭头不方便，也可以在 Haddock 正文中用分点列出每个输入 / 输出的语义。

### 4.5 不得用“注释补洞”替代类型层表达

注释必须是类型 / 构造子 / 合同的补充，而不是替代。

不允许：
- 类型只写成 `String` / `Text` / 文本包装，再靠 Haddock 解释“这里其实代表某类策略位”
- `data Foo = Foo` 空杆，再靠大段注释解释“以后会有不同变体”
- 明明应该站到 ADT / GADT 层的业务语义，只靠注释说明

---

## 5. 策略、参数与文本表达规则（硬规则）

### 5.1 可变策略必须优先站在具名构造子 / GADT 层

凡是业务上可替换的：
- 策略位
- 规则位
- 绑定方式
- 资格方式
- 时间语义方式
- 去重 / 多开 / 触发优先级治理语义

必须优先暴露成：
- GADT / ADT 构造子家族
- 命名 strategy / policy 数据类型

不得退化成：
- 裸函数槽
- `String` / `Text` / 文本标签
- 泛化 record 再靠字段解释“当前是哪类做法”

### 5.2 当前只有一个 variant，也应保持“家族 + 当前构造子”

如果某个槽位在业务语义上是开放策略位，即使当前只有一个已实现 variant，也应保持：
- 策略家族类型
- 当前单构造子

避免误导 reviewer 以为该槽位语义上已经闭合。

但若只是某个已命名构造子内部的普通静态字段，则直接作为该构造子的字段即可，不必再人为额外包一层“只有一个构造子”的类型。

### 5.3 文本强门：禁止用文本载体承载业务语义

在生产业务模块中，**任何文本载体** 都不得直接承载业务语义。这里的文本载体包括：
- bare `String`
- bare `Text`
- 只包一层 `newtype` 但底层仍是 `String` / `Text` 的文本包装
- 本质上只是在文本外面再套一层名字、但仍允许任意文本流入业务判断面的对象

下列内容一律不得以文本载体表达：
- 有限业务语义集合
- 会影响业务判断的标签 / 名字 / kind / status / family / phase
- 通过 `if / case / == / /= / elem / notElem` 等参与分支的文本值
- 本质上应为策略位 / 规则位 / 角色位 / 资格位 / 时间语义位的内容

**默认裁决规则**：  
如果在“文本载体（哪怕包一层 newtype）”与“临时 ADT / 占位 ADT”之间犹豫，默认选择 **ADT**。

### 5.4 开放世界文本也不得直接暴露给业务层；优先用占位 ADT 消化

当外部世界确实给入开放世界文本（如外部系统原始 payload），允许其仅存在于：
- ingress adapter
- parser / decoder
- transport shell 的边界层

但必须满足：
- 对内暴露为 **抽象 ADT**；不要把文本直接带进业务层
- 若当前给不出稳定枚举或抽象层级，也应先用 **占位 ADT** 表达，而不是保留文本包装
- 业务层不得按原始文本做分支
- 文本只能停留在边界解码前后极短的局部范围，不得成为正式合同字段

也就是说：**不因为“现在还想不清名字/层级”就退回字符串；想不清时，先给临时 ADT。**

### 5.5 不得维护“已类型化语义”的并行文本镜像

如果某个业务语义已经由：
- 构造子
- 枚举
- ADT / GADT 字段
- 明确的 kind / family / status 类型

表达出来了，则不得再并行维护一个文本字段去“重复描述同一语义”。

处理规则：
- 若该文本字段不携带额外独立语义 → 删除
- 若只是为了显示 /打印 → 由已类型化语义派生，不单独存储
- 若它确实携带额外独立语义 → 把这份额外语义建模成新的类型化字段，而不是继续塞文本

### 5.6 参数状态必须显式标注为四类之一

每个关键参数必须归入且只归入以下四类之一：

1. `LOCAL_CONSUMED`  
   当前节点真实消费。

2. `DOWNSTREAM_CONSUMED`  
   当前节点只透传 / 投影，但预期由下游节点消费；必须写清 downstream consumer 与传递路径。

3. `OPEN_SLOT`  
   语义上预留、当前尚未冻结；必须写清未冻结原因，不得伪装成已接线。

4. `DEAD_FIELD`  
   当前没有消费者、没有明确下游路径，也不是保留位；这是应删除或重构的字段。

### 5.7 `bind_at` 只约束运行时输入值

`bind_at` 只用于说明：
- 哪个事件 / 触发点到来时读取当前 `Behavior` / `Dynamic` / 输入世界值

它不用于解释：
- 构造子字段中的静态策略选择
- 构造子静态旋钮
- “用户通过选构造子决定的函数参数”

### 5.8 参数变化默认只影响未来事件和未提交 working-state

除非明确另有合同，否则：
- 参数变化不应回写已提交的 `AnchorRef / SegmentRef`
- 已提交对象的合同不应因参数热切换而悄悄漂移

---

## 6. 每个 materialized DSU / 正式 CEPS 节点都必须长成什么样（硬规则）

### 6.1 每个正式导出节点都必须有局部业务头卡

不允许只给父节点写头卡，而子节点只剩 `data` + `instance` 空壳。

每个正式导出节点至少要在本节点附近写清：
1. 节点中文名 / 英文名
2. 一句话定义
3. 输入（业务意义 + 类型边界）
4. 输出（业务意义 + 类型边界）
5. `working-state`
6. `committed output`
7. 最关键触发 / 采样点
8. 当前未冻结项

### 6.2 节点要有独立 CEPS 契约

materialized DSU 扮演的 Global CEPS node，或任务明确要求独立导出的 Local CEPS node，不要只写成普通函数。至少要能从源码中直接看到：
- `type Input`
- `type Output`
- `processEvents`

普通 Action Node 可以是具名纯函数、局部状态转换或 Local CEPS 组合；它不必伪装成独立 CEPS node，但必须保留所属 DSU、capability、Dynamic state、输入输出和 public lifecycle 影响。

### 6.3 输入 / 输出必须是“业务语义 + 类型边界”双写

不要只写：
- `FrpEvent StructEvidence`
- `Dynamic ContactContext`
- `Event AnchorRef`

还要写：
- 这类输入在业务上表示什么
- 它来自哪一层（策略 / 输入世界 / 合同 / working-state / committed output）
- 输出给下游后，下游把它当什么用

### 6.4 `processEvents` 必须贴着节点词汇出现

不要让 reviewer 必须跨很多文件，才能把：
- 节点定义
- 输入输出
- 参数
- 实现主线

拼回同一个对象。

### 6.5 节点名必须能被最小行为声明支撑

每个节点都必须在头卡中给出一句 **最小行为声明**：
- “它最少完成什么”
- “它不完成什么”

如果节点名暗示 stronger semantics（例如 `First` / `Commit` / `Qualification`），则实现中必须存在与该语义直接对应的选择 / 约束 / 定稿逻辑；否则要么改名，要么补语义。

---

## 7. 公开 ingress、`StructEvidence` 与运行时语义

### 7.1 公开合同层不得退回统一 `Event<StructEvidence>`

公开输入合同不得直接暴露为统一 `Event<StructEvidence>`。

`StructEvidence` 最多只能作为：
- 内部 transport shell
- 内部 envelope
- 从公开 ingress 进入局部子树之后的过渡表示

正式公开 ingress 必须体现业务语义对象类型划分。

### 7.2 `StructEvidence` 不是“无类型语义垃圾桶”

如果内部仍使用 `StructEvidence`：
- 它不得承载本应在 ADT / 构造子层表达的业务语义
- 不得用内部文本字段去重建策略位 / 规则位 / family / status
- 不得在业务层对文本 payload 做语义分支

### 7.3 所有关键 `Dynamic` / `Behavior` 读取都要写采样点说明

推荐固定注释格式：

```haskell
-- | sample_when: eResolutionEvidence
-- ^ sample_target: current dLastInteraction
-- ^ why_safe: 收官绑定只在确认事件到来时绑定当前候选
```

涉及以下语义时，必须在代码旁边可见：
- `ts_anchor` 与 `ts_confirm` 是否分离
- 段的 `t_start` / `t_end` 如何确定
- 同刻事件先后是否影响结果
- 过期 / 失效是事件驱动还是需要额外时间触发源
- final-only 还是允许 provisional / replace

---

## 8. working-state / Deferred / 反模式

### 8.1 `working-state` 与 `committed output` 不能混写

必须明确区分：
- 当前候选态 / 当前链 / 当前上下文（`Dynamic`）
- 最终锚 / 最终段（`Event`）

不要出现一种对象既被当当前候选、又被当最终结构提交的模糊写法。

### 8.2 `Deferred / OPEN / PLACEHOLDER` 不得静默写死

如果某条路径被标为：
- `Deferred`
- `OPEN[contract]`
- `PLACEHOLDER[data]`

就不得在真实效果上偷偷折叠成默认 allow / deny / drop 路径，而不显式 surfaced 给 reviewer。

### 8.3 反模式：表演式审阅面

以下都不算合格：
- 只在注释里写 `working-state`，代码里没有真实承载面
- 只定义 `Deferred / OPEN`，逻辑仍静默写死默认分支
- 只留参数字段名，但字段未进入任何消费路径
- 只给父节点写头卡，子节点仍不可审
- `data Foo = Foo` 空杆，而真正可换参数都躲在别处

---

## 9. 模块与测试组织要求

### 9.1 不要把“业务节点 + 参数 + 总装配 + helper + 测试辅助”揉成一个文件

推荐至少拆出：
- 节点定义 / 节点合同
- 策略对象 / 参数合同对象
- 总装配入口
- 纯 helper / reducer

### 9.2 主模块开头必须给导航

每个主模块建议至少给出：
- 本模块覆盖哪些节点
- 这些节点的顺序
- 哪些是输入节点
- 哪些是中间工作态节点
- 哪些是最终提交节点

### 9.3 测试面不能只有父节点总链

如果一个父节点下存在多个正式导出子节点，则测试面应同时覆盖：
- 父节点总链 / 组合链验证
- 关键子节点的节点级 spec 面

不允许只有父节点 spec，而子节点完全没有独立测试审阅面。

### 9.4 helper 不能吞掉业务词汇

允许有 helper，但不允许让 helper 名完全遮蔽业务对象。

---

## 10. 命名要求

### 10.1 节点名优先体现业务对象，不优先体现技术动作

优先：
- `BoundaryContactContextP`
- `ResolutionBindingP`
- `EscalationCoreSpanP`
- `ConflictContainerSpanP`

不推荐只写：
- `FoldContext`
- `LinkPair`
- `MakeSpan`
- `UpdateState`

### 10.2 类型名优先表达业务角色，不追求统一后缀

类型名应优先表达该对象在业务中的角色，例如：
- 合同对象
- 规则家族
- 资格方式
- 绑定方式
- 运行时输入对象
- 子路径投影槽位

不要求统一使用 `Pack`、`Config`、`Params` 等后缀。

### 10.3 策略名要能回答“当前到底选了哪种业务逻辑”

命名至少应体现：
- 依据什么量
- 依据什么关系
- 属于什么策略族

### 10.4 临时占位必须显式标出

如果某参数 / 字段 / 策略尚未冻结，不得伪装成最终业务语义。

推荐使用：
- `FROZEN`
- `PLACEHOLDER[data]`
- `OPEN[contract]`

三类标签之一。

---

## 11. Reviewer 快速检查清单

打开一个节点文件后，reviewer 应能在较短时间内回答以下问题；如果不能，说明代码形状不合格：

1. 这个节点在业务上到底是什么？
2. 输入是什么？输出是什么？
3. 哪些是当前候选态，哪些是最终提交态？
4. 当前到底用了哪类策略，而不是哪几个裸函数？
5. 用户可选函数参数是否站在构造子层？数据输入是否仍留在输入世界？
6. 参数是谁的、在什么时候被采样？
7. 最容易写歪的时间语义是什么？代码里有没有显式说明？
8. 哪些地方已经冻结，哪些只是占位？
9. 有没有任何 `String` / `Text` 在伪装业务语义？
10. 每个顶层声明、每个 field、每个函数输入输出是否都写了 Haddock？

---

## 12. 最后的执行要求（给实现 AI）

实现从 L0 / Segmentor 开始的 FRP 部分时，必须满足以下底线：

1. **每个正式节点都要先有业务词汇壳。**
2. **用户可选函数参数必须优先站在 GADT / 构造子层。**
3. **来自数据世界的输入不得塞进策略构造子层。**
4. **可变逻辑尽量命名成策略对象，不要只留裸函数槽。**
5. **每个节点都要有可读的 Input / Output 审阅面。**
6. **参数状态必须真实分类为四态之一。**
7. **`bind_at` 只约束运行时输入值。**
8. **公开 ingress 不得退回统一 `Event<StructEvidence>`。**
9. **生产业务模块中，不得使用 bare `String` / `Text` 承载业务语义。**
10. **所有保留注释都必须使用 Haddock 兼容格式。**
11. **每个 data 的每个 field、每个函数的每个输入输出都必须有 Haddock 语义说明。**
12. **working-state 与 committed output 必须显式分开。**
13. **Deferred / OPEN / PLACEHOLDER 不得静默写死。**
14. **模块必须可导航，不得一大坨。**
15. **任何会误导业务 reviewer 的实现压缩写法，都应让位于可审阅性。**

如果某个实现选择虽然技术上更短，但会明显损害“业务 reviewer 快速看懂节点合同与关键语义”的能力，则应优先选择更可审阅的写法。
