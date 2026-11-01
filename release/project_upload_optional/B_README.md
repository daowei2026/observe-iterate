<!--
virtual_source_id: MB-RUNTIME-README
candidate: Mission B v0.2
canonical_sources:
  - README.md
  - 10_methods/11_FEATURE_STATE_METHOD_REALIZATION_COMPILATION_V0_2.md
manual_edit: forbidden
-->

# Mission B Project Runtime Bundle — candidate-v0.2.0

本运行包用于两个独立聊天：

```text
RepoFact Profile：
  只调查 current repo fact，冻结 S0。

Compiler Profile：
  只读 S0，把 Mission A 合同编译为宿主 realization 和 VCC。
```

默认不加载 171 个既有 Harness。正常主体先读正向方法，只有具体风险命中时才回完整候选包读取相应 Harness。

状态：

```yaml
runtime_maturity: human_led_candidate
validated_runnable: false
owner_acceptance: pending
existing_engineering_artifacts_retrofitted: false
```
