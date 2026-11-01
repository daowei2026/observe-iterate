<!--
virtual_source_id: MA-RUNTIME-README
runtime_bundle_id: mission-a-project-runtime-bundle-candidate-v0.2.0-integrated-20260904
canonical_successor_repo: daowei2026/feature-refinement-implementation-agent-evolution
canonical_successor_ref: SAME_GIT_TREE_AS_THIS_RUNTIME_RELEASE
canonical_paths:
  - agent_evolution/agent_candidates/market_process_modeling_contract_pro_candidate_v0_2/README.md
v0_2_integration_ids:
  - MA-V02-MATERIAL-RUNTIME-001
generated_release_candidate: true
manual_edit: forbidden
-->

# Mission A Project Runtime Bundle — candidate-v0.2.0 Integrated Release Candidate

## 1. 身份

```yaml
package: Market Process Modeling & Contract Pro
candidate_version: v0.2.0
runtime_bundle_id: mission-a-project-runtime-bundle-candidate-v0.2.0-integrated-20260904
runtime_maturity: human_led_candidate
validated_runnable: false
owner_acceptance: pending
cross_use_case_validated: false
final_installable_release: false
```

这是从已物化且自包含的 Mission A v0.2 successor 生成的 Project Sources 运行投影候选。它的作用是让 GPT Pro 在正常 Mission A 工作中实际看见正向 P0 方法，而不是只拿到 GitHub 链接和短 Profile。

它不替代 canonical package，不单独拥有方法权力。任何修改必须回 canonical Mission A 包，再重建本 bundle。

## 2. 建议上传文件

本目录的 Markdown、YAML 和 `SHA256SUMS.txt` 可作为同一 Mission A Project 的稳定 Sources 候选。正常新聊天按以下顺序读：

```text
00_RUNTIME_FRONT_DOOR.md
01_P0_FEATURE_NARRATIVE_AND_OWNER_SPINE.md
然后根据mode：
  WORK_MAP → 02_WORK_MAP_RUNTIME_METHOD.md
  LOCAL_CONTRACT → 03_LOCAL_CONTRACT_RUNTIME_METHOD.md
  横切method/controller/state/complexity → 04_...
每个承重任务还读：
  05_SOURCE_ACTIVATION_USE_AND_MAINTENANCE.md
按触发读：
  06_IMPLEMENTER_PROBE_AND_AUDIT.md
  07_CASE_ROUTER_AND_NONCLAIMS.md
本轮task authority直接附：
  08_RUNTIME_TASK_PACKET_TEMPLATE.md的实例。
```

## 3. 热层与冷层

本 bundle 只承载正常运行所需的中等粒度语义卷。完整形成史、全部 anti-gold、原始聊天、accepted taskpack、live repo 和 generated validation 不进入常驻热层。

```text
Project runtime bundle：
  稳定方法和运行入口。

每任务 packet：
  current Owner delta、accepted parent、scope、consumer。

GitHub／外部Source：
  current repo fact和触发型深读。

完整canonical package：
  维护、争议、冷审、provenance。
```

## 4. 限制

本集成候选已经绑定 Mission B v0.2、Mission C v0.2 与 Overlay v0.3，但静态绑定不等于运行验证：

```text
跨包组合已声明，尚未完成 fresh-agent pilot；
Source Activation Gate 尚未在真实任务中验证；
没有实际用新 bundle 跑 Mission A；
没有对既有 U2／U3 产物执行 retrofit；
不得标为 final installable 或 Owner 已接受。
```
