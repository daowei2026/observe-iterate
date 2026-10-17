# A／B／C Agent Refinement Runtime Release Candidate v0.3 — 2026-09-04

```yaml
release_set_id: agent-refinement-runtime-release-candidate-v0.3-integrated-20260904
mission_a: candidate-v0.2.0 runtime bundle
mission_b: candidate-v0.2.0 runtime bundle
mission_c: candidate-v0.2.0 runtime bundle
overlay: agent_owned_long_horizon_overlay_v0_3
execution_contract_revision: 2026-09-08
runtime_maturity: human_led_candidate
validated_runnable: false
owner_acceptance: pending
existing_business_or_engineering_artifacts_retrofitted: false
```

# 1. 这套东西怎样使用

每个聊天只选择一个 Mission 和一个 mode，不同时把 A／B／C 全部作为主体。

## 长程新建／接续与审查（执行修订 2026-09-08）

先读 `overlay_v0_3/09_GitHub持续工作面与版本管理.md` 与 `overlay_v0_3/10_独立审查与下一轮问题选择.md`；上传视图中对应 `O09_GITHUB_WORKSPACE.md`、`O10_REVIEW_AND_ROUTE.md`。已有地图就地接续，没有才按实际材料建立。当前任务及正文放在获授权 GitHub 目录，日常版本由 Git 保存。

每次独立审查先判断正文是否业务合理，再结合完整地图与实际进展确定下一轮核心问题。Builder 的 NEXT_ACTION 不自动获得任务权；任务卡与来源、输入提交共同投递。不要为普通迭代再复制整套版本目录。

## 本轮自存与材料补齐

日常交付再读 `overlay_v0_3/11_本轮问答与实质材料入库.md`，上传名为 `O11_TURN_AND_MATERIAL_PUBLICATION.md`。Pro 自己保存本轮提示和完整回答，不补历史；必要实质文件与有效修订完整入库，同内容只保留一份。中途补齐按 08 的 MATERIAL_CATCHUP 分 2–3 轮直接落正文，实际核验远端后报告。不是新建管理 Agent、运行实例或自动部署 routine。

## Mission A

```text
总入口：
  overlay 00／01／02／03
  A 00／01
按mode：
  WORK_MAP → A 02
  LOCAL_CONTRACT → A 03＋04
  probe/audit → A 06
task-local：
  A 08 模板的实例。
```

## Mission B RepoFact

```text
overlay 00／01／02／04
B 00／01
真实A→B handoff
live exact repo。
```

## Mission B Compiler

```text
overlay 00／01／02／04／06
B 00／02／03／04
frozen S0
真实A→B handoff。
```

## Mission C

```text
overlay 00／01／02／05／06
C 00／01／02
按需C 03／04／05
真实B→C handoff、Goal、exact repo scene和代码授权。
```

# 2. `project_upload_core` 与 `project_upload_optional`

`project_upload_core/` 保存公共前门和每个 Mission 的最重要正向骨架，适合上传为固定 Project Sources。

`project_upload_optional/` 保存按 mode／触发读取的深方法、probe、case、模板和回压材料。它们仍是 release set 的正式组成，但不要求每个聊天全部热读。

完整内容同时保存在四个嵌套 runtime bundle 中。flat 视图只是 generated projection，不是第二套真源。

# 3. Task-local 材料仍需单独提供

本 release set 不包含：

```text
当前 accepted taskpack／parent；
最新 Owner delta；
具体 U2／U3 artifact；
当前 repo live head；
某次 production/data evidence；
具体 Delegation Envelope。
```

这些必须通过 `02_TASK_LOCAL_PACKET_TEMPLATE.yaml` 的实例直接提供。

# 4. 已静态证明

A／B／C v0.2 successor 已分别从精确父包完整物化，完整承接应沿用的父包成员并加入本轮增量；运行时不依赖旧版目录。

# 5. 仍未证明

```text
没有运行 fresh-agent pilot；
没有修改 U2／U3；
没有执行 RepoFact／Compiler／Host 真实任务；
没有编译、production、writer/readback或真实数据；
没有取得Owner接受；
A／B／C v0.2 successor 虽已通过静态物化与完整性校验，但尚未完成 fresh-agent 和真实任务运行验证。
```
