<!--
virtual_source_id: MB-RUNTIME-FRONT
candidate: Mission B v0.2
canonical_sources:
  - 00_front_door/00_PACKAGE_FRONT_DOOR.md
  - 20_runtime_profiles/repofact/00_PROFILE_FRONT_DOOR.md
  - 20_runtime_profiles/compiler/00_PROFILE_FRONT_DOOR.md
manual_edit: forbidden
-->

# Mission B Runtime Front Door

## 选择 Profile

```text
用户要知道当前 repo 真有什么：
  REPOFACT。

用户已有 frozen S0，要形成工程设计／VCC：
  COMPILER。

用户要独立检查冻结工程包：
  COLD_AUDITOR。

只需机械摘取指定事实：
  EVIDENCE_WORKER。
```

RepoFact 与 Compiler 不在同一聊天混跑。Compiler 不得边设计边刷新 S0。

## 主体优先

```text
业务 Feature／Action
→ current repo facts
→ realization
→ state／method／product
→ VCC
→ implementer probe。
```

不得从文件 inventory、Harness 或 VCC 编号开始。
