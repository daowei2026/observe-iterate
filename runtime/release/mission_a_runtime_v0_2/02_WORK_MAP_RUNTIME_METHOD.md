<!--
virtual_source_id: MA-RUNTIME-WORK-MAP
runtime_bundle_id: mission-a-project-runtime-bundle-candidate-v0.2.0-integrated-20260904
canonical_successor_repo: daowei2026/feature-refinement-implementation-agent-evolution
canonical_successor_ref: SAME_GIT_TREE_AS_THIS_RUNTIME_RELEASE
canonical_paths:
  - references/work_map/WORK_MAP_CONSTRUCTION_METHOD_FULL_REFERENCE.md
  - references/work_map/WORK_MAP_GOLD_AND_ANTI_GOLD.md
  - references/work_map/CASE_SPECIFIC_VS_COMMON_CORE_DELTA.md
  - profiles/WORK_MAP_PROFILE.md
v0_2_integration_ids:
  - MA-V02-WM-P0-001
generated_release_candidate: true
manual_edit: forbidden
-->

# WORK_MAP Runtime Method

## 1. 合格输入

```text
一个待解释的完整市场过程或业务claim；
必要上下游；
current Owner／accepted authority；
预期consumer；
材料身份和证明边界。
```

不从 module、role、阶段名、已有 Book 或代码容器开始。

## 2. 主体推进

### A. Scope Lock

说清：

```text
当前完整问题；
内部过程；
外部但决定边界的合同；
本轮不处理的内容；
为什么仍是small-but-complete。
```

### B. 恢复市场过程

自然语言写：

```text
开始；
持续；
转折；
结束／未决；
可能的竞争解释。
```

### C. Source→Fact→Feature

逐项区分：

```text
Source／measurement；
客观业务事实；
Feature；
evidence；
knownness；
正式record。
```

### D. 提出少量真实候选

每个候选说明：

```text
得到什么；
牺牲什么；
怎样支持组合；
失败条件；
对state、method、product、consumer的影响。
```

不列无理由架构菜单。

### E. 多视图对账

```text
Feature叙事；
identity／state；
event／material／time；
process／method；
product／consumer；
communication/history（适用时）。
```

### F. 组合性挑战

```text
换搭档；
换解释器；
换消费者；
换生成器。
```

不是技术插件测试，而是检查对象和Feature是否是合理积木。

### G. P0 横切扫描

定位：

```text
需要局部合同的Feature；
需要current method的judgement；
可能fuzzy的位置；
需要lookback/state contract的位置；
需要pure／Reflex／CEPS处置的位置；
独立Book资格疑问；
需要市场Case的位置。
```

## 3. 输出

必须同时交付：

```text
scope lock；
market process story；
Feature Narrative Stack；
candidate comparison；
multi-view map；
Feature/infrastructure separation；
refinement coverage；
P0 Owner surface；
work-slice handoff；
MapRevision return path。
```

## 4. 完成判断

不能以：

```text
图画完；
对象都有名字；
所有格子非空；
gap都有ID；
```

判完成。

要看：

```text
Feature世界是否连贯；
Source到Feature是否可走；
正面含义和consumer是否明确；
Book／Life是否有资格；
Refiner不需要重新猜边界；
真正P0与局部provisional已分开。
```
