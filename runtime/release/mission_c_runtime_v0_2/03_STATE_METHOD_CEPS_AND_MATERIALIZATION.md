<!--
virtual_source_id: MC-RUNTIME-STATE-METHOD
candidate: Mission C v0.2
canonical_sources:
  - canonical_methods/host/HOST_IMPLEMENTATION_METHOD_FULL_REFERENCE.md
  - dependencies/ceps/THIN_BRIDGE_CONTRACT.md
manual_edit: forbidden
-->

# State、Method、CEPS 与物化

## State

分开：

```text
active runtime state；
formal durable history；
rebuildable／diagnostic material。
```

按业务结束清退active state，保留正式history；性能优化不能改回看或scope。

## Method

证明：

```text
version／参数进入；
asset加载；
输入as-of正确；
knownness正确；
输出被Action消费；
deterministic envelope；
commit不由method私自取得。
```

## CEPS

只有多个独立Action、事件拓扑、state owner、sampling/feedback或transaction需要时使用。简单Action保持pure／simple Event／simple state。root只连接，不吸收业务判断。

## 物化

新增 Book／owner／public product 必须引用 Mission B qualification；实现层不因readback方便创造业务对象。

CEPS使用现成实施模式，Skill不授新代码修改权。Codex运行可调查状态/方法事实，源码修改按Pro指令。结果保存使用既有平台，不预设本任务新增存储转换或编码解码。
