# 特征平台工程参考读取路由

## 1. 固定权力边界

```text
最新 Owner 明确纠正
> 当前 accepted Taskpack／业务合同
> 当前 Goal 与 exact RepoFact／工程设计锁
> 本包的宿主平台工程约束
> 历史用例、旧代码和导入 provenance。
```

本包回答“现有特征平台怎样支持实现、有哪些稳定工程约束”，不回答当前任务“应该做什么业务”。正文中若出现旧流程、具体用例提示或可选 generic correction／replay，只在当前合同命中时采用；不能据此扩张 scope。

## 2. 按问题选择正文

|Reference ID|触发问题|Mission B 使用|Mission C／其他实现者使用|正文|
|---|---|---|---|---|
|`FP-PY-OUTPUT-ENCODING`|Numba／Python 正式 wrapper、dtype、枚举编码、缺失值、稀疏事件 index|冻结正式产品、物理字段、writer/readback 与 consumer 接缝|实现并验证真实 wrapper 和输出|[`P_01`](../project_upload_optional/P_01_PY_OUTPUT_ENCODING.md)|
|`FP-PY-ARTIFACT-BOUNDARY`|scope、wrapper decision、正式／私有／诊断／audit artifact|防止把验证优先级当 scope 缩减，明确物化边界|防止实现时静默减项或把诊断面冒充正式产品|[`P_02`](../project_upload_optional/P_02_PY_ARTIFACT_BOUNDARY.md)|
|`FP-RUNTIME-HOTPATH`|stateful assembler、dense/sparse 边界、对象分配、跨语言扫描、长历史性能|在工程设计期决定数据密度、状态形状和语言边界|沿真实热路径实现、测量和收敛缺陷|[`P_03`](../project_upload_optional/P_03_RUNTIME_HOTPATH.md)|
|`FP-CROSS-LANGUAGE-HANDOFF`|Python／Numba → DBA／Fao → Haskell，或 Haskell 回 Python|锁业务身份、时间、有效性、密度、编码、writer/readback 和责任边界|实现并验证同一产品在跨语言链中的恢复与消费|[`P_04`](../project_upload_optional/P_04_CROSS_LANGUAGE_HANDOFF.md)|
|`FP-FRP-BUSINESS-CODE`|FRP 业务类型、节点、策略槽、typed ingress、working/committed、模块与测试组织|设计类型、Action／DSU 节点、参数与正式输出的最低充分结构|写出 owner 可读且类型承载语义的真实 FRP 代码|[`P_05`](../project_upload_optional/P_05_FRP_BUSINESS_CODE.md)|
|`FP-FRP-STATE-IDENTITY`|DSU／CEPS／CBPS、identity、occurrence/current/history、修正或 replay|决定状态 owner、生命周期、正式产品和受影响范围|实现状态隔离、提交、修正及适用测试|[`P_06`](../project_upload_optional/P_06_FRP_STATE_IDENTITY.md)|
|`FP-FRP-ACTION-CONTEXT`|Action Node、capability、Dynamic/event state、参数与采样|把 Action、上下文、状态和可替换方法参数编译成明确工程设计|实现事件顺序、实例隔离、参数生效和 public lifecycle|[`P_07`](../project_upload_optional/P_07_FRP_ACTION_CONTEXT.md)|
|`FP-FRP-RULEPACK`|RulePack／FIS、方法资产、模糊多输出、版本切换|锁 method binding、输入准备、结果使用、版本与正式/诊断边界|复用现有方法平台并证明参数和结果真实生效|[`P_08`](../project_upload_optional/P_08_FRP_RULEPACK.md)|

## 3. 角色合同

### Mission B／Engineering Compiler

Mission B 必须在工程方案冻结前读取命中的正文，把平台约束落实到 actual module/symbol/caller、状态物理计划、方法绑定、正式产品、writer/readback、consumer 和验证设计。不得只把 reference ID 填进任务包，也不得把尚未设计的热路径、跨语言接缝或状态生命周期留给实现者首次决定。

### Mission C／其他正式特征实现者

实现者读取 B 锁定的同一包和 reference ID，并在目标 exact ref 上核实当前源码。普通类型、wrapper、adapter、hot-path 和最近邻测试问题在授权写面内解决；若真实平台事实使已冻结方案不能成立，形成 RepoFact delta／窄 backpressure，不静默另造平台或改业务合同。

### RepoFact

本包属于固定冷工程参考，不是 `D0` live evidence。当前 Feature、Fao、Frame、DBA、CEPS、CFIS、注册入口、Reflex API、writer、readback 和 consumer 必须从任务选定的 exact repo/ref 动态取得。快照与 live 事实冲突时，记录 drift 并只阻止依赖该冲突的结论。

## 4. 交接锁

工程设计或 B→实现者 handoff 至少保存：

```yaml
platform_reference_lock:
  package_id: feature-platform-engineering-reference-pack-candidate-v0.1.0
  package_manifest: P01_FEATURE_PLATFORM_REFERENCE_MANIFEST.yaml
  required_reference_ids: []
  selected_member_sha256: {}
  live_repo_refs_checked: []
  unresolved_drift: []
```

不得复制正文进 handoff 后独立维护。runtime 的 flat upload 文件只是由本包生成的同字节投影，同样不能成为第二真源。
