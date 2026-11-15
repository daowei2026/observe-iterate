# FRP 中 RulePack 与模糊计算的接入

## 0. 本文解决什么

本文说明业务任务已经给出 RulePack、隶属函数、规则表和输出合同后，Haskell 怎样把 RulePack / FIS 作为所属 DSU.process 中的 Local CEPS Action Node，复用现有模糊计算能力，并把结果接回 DSU Payload、public ledger lifecycle 和正式 product。

默认不从头实现新的模糊引擎。任务代码需要的是一层接线：

```text
上游 DSU product / input occurrence
→ 测量和归一化
→ Local CEPS 中已冻结的 RulePack / FIS
→ 业务判断结果
→ DSU state transition
→ Global CEPS product / 必要的 CBPS publication
```

## 1. 三层内容不要混

### 1.1 方法合同

说明：

- 要回答哪个业务问题；
- 稳定输入和输出；
- 当前绑定哪个方法版本；
- 缺输入时怎样处理；
- 历史和版本兼容要求。

### 1.2 RulePack 资产

保存：

- 输入业务含义、测量和归一化；
- 隶属函数；
- 完整规则；
- 冲突、否决和保守选择；
- 历史条款；
- 数值版本、测试和来源。

### 1.3 Action Node 调用结果

交给所属 DSU.process：

- 业务现象判断；
- 当前知识是否充分；
- 当前结果是否允许提交；
- 必要的规则和校准版本；
- 正式来源摘要。

完整规则触发和数值轨迹留在 DSU private diagnostic 或测试中，不全部塞进正式 product。

## 2. 输入准备

Local CEPS 接线代码负责：

- 从正式上游产品取得任务要求的输入；
- 检查单位、范围和输入版本；
- 把缺失、尚未形成、不适用、计算失败与数值 0 分开；
- 按冻结任务执行 clamp、归一化和 fallback；
- 固定同一次判断使用的一致输入和方法版本。

实现者不能临时发明 rolling percentile、阈值、默认 0 或新的 fallback。

## 3. 多输出和多级判断

一个 RulePack Action Node 可以同时产生多个紧密相关的业务输出，只要它们：

- 回答同一个局部问题；
- 主要读取同一份输入快照；
- 同一次触发共同更新；
- 存在联合规则或一致性约束；
- 共同校准和版本化。

以下三种情况必须区分：

```text
一个 RulePack 的多个联合输出；
同一次判断中，前一个判断结果交给后一个判断；
跨事件读取以前已经形成的判断。
```

第二种有明确先后顺序；第三种需要 DSU owner 维护历史状态。不能把三者都写成一个无顺序的 RulePack 调用。

## 4. 现象、知识和提交权力分开

一次判断结果至少按任务需要区分：

- 现象表现多强、属于哪些相邻类别；
- 当前材料是否完整、是否存在竞争解释；
- 结果是 working、candidate、committed、final 还是 correction。

材料不完整不能自动把强现象压成弱现象。pending 不是 0，ambiguous 也不是中等强度。

RulePack / FIS 给出的支持度不自动创建 Anchor、Edge、Segment 对应的 DSU、DSU-owned entity 或正式 product。它们具体落在哪一层，先服从 DSU materialization audit；identity、revision 和 public lifecycle 仍由所属 DSU.process 决定。

## 5. 历史状态由 DSU owner 拥有

RulePack 可以规定“允许读取怎样的历史判断、历史如何影响当前规则”，但实际历史状态属于 DSU Payload / public ledger，由 DSU owner 维护。

推荐顺序：

```text
读取旧判断和旧对象版本
→ 运行当前输入的规则计算
→ 形成当前判断
→ 更新 DSU Payload、revision 和历史
```

若旧输入被修正，必须能沿 Global CEPS / CBPS 消费关系找到使用旧判断的 consumer DSU，并按任务要求形成新 revision、retract 或 replay。RulePack 资产本身不成为隐藏的 Dynamic state 容器。

## 6. 版本和切换

同一次判断固定：

- 输入业务对象的精确版本；
- 方法版本；
- RulePack 版本；
- 隶属函数和校准版本。

若多个 RulePack 或确定性步骤共同构成一个方法，它们可以作为一组兼容版本绑定，不必合成一个巨大 RulePack。

第一版不需要自动换挡系统，但不能在同一活动对象内悄悄混用不兼容版本。

## 7. 正式输出和诊断

正式 DSU product 通常保留：

- 稳定业务判断；
- 必要的多维支持度；
- 知识成熟度；
- 当前提交状态；
- 方法和 RulePack 版本；
- 决定性来源摘要。

诊断或测试保留：

- 原始测量；
- 归一化结果；
- membership；
- 触发规则；
- 冲突和否决；
- 完整数值轨迹；
- 校准版本。

私有实现可以保留索引和缓存，但下游 DSU 不能穿透读取。已知局部 consumer 走 Global CEPS direct dataflow；需要开放订阅、历史回查或 Context 汇编时，由所属 DSU 声明 CBPS role。

## 8. 接入检查

每个 RulePack 接入至少覆盖：

1. 正常数值；
2. 相邻集合同时激活；
3. top 两类接近时的保守选择；
4. required input 不可用；
5. optional input 的冻结 fallback；
6. pending 不被当成数值 0；
7. 相同输入和版本产生相同结果；
8. 多输出之间的一致性；
9. 旧输入修正后形成正确的新版本；
10. 正式输出不泄漏全部内部规则轨迹。

## 9. EAW P2 / P3 使用提示

- P2 已冻结 Materiality、Continuity、Opened 的集合、算子、灰区政策和提交边界；
- P3 已冻结 Phase、Pair 等 support 语言、reduced mode、规则表和状态时间线；
- 数值积分、采样密度、内部 FIS 类型、模块和缓存由实现者决定；
- 实现结果必须通过冻结 fixture 和 worked timeline；
- P2/P3 实现应把 RulePack / FIS Action Node 挂回明确的 DSU owner 和 Local CEPS，不建立脱离 DSU 的规则服务；
- 不因当前代码没有现成调用层，就把问题退回 Pro；
- 只有现有计算能力无法等价表达冻结规则、且任何替代都会改变业务结果时，才需要业务裁决。

### 9.1 RulePack 属于 P3，不等于逐半秒计算必须在 Haskell

业务方法 ownership、公共产品 ownership 与数值计算放置是三件事。若某个 RulePack 步骤仍要扫描完整 multi-series half-second stream 或 `pair × UTI` dense matrix，就不能为了复用 Haskell FIS 而把整条 dense 流搬进 FRP。

实现者应先选择合适的稀疏边界：

- 稀疏化后的 proposal/delta 进入 FRP，由所属 DSU 管 stable identity、revision、correction 和 public lifecycle；
- 若稀疏材料已足够，RulePack 可以继续由现有 Haskell FIS 执行；
- 若冻结方法必须在 Numba 热路径执行，首版使用专用、可 JIT 的等价数值函数，不建设第二套通用 fuzzy-controller runtime。

专用函数必须忠实实现当前 method/MF/RulePack binding，并通过冻结 fixture、灰区、membership 边界、状态阈值附近、missing/unavailable、tie 和最终状态变化的等价检查。参考结果可来自现有 Haskell FIS 或简单测试参考实现，数值容差必须明确。“典型样例看起来差不多”的硬阈值不是等价实现。

无论计算在哪边，只保留一份 canonical method semantics 和一份 canonical public result；不得让 Haskell 与 Numba 各自成为正式业务真相。
