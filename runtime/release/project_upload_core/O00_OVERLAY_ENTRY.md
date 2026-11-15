# Mission A／B／C 长程运行覆层 v0.3

```yaml
candidate_id: agent_owned_long_horizon_overlay_v0_3
supersedes: agent_owned_long_horizon_overlay_v0_2
runtime_maturity: human_led_candidate
validated_runnable: false
owner_acceptance: pending
physical_agent: none
```

本覆层不是第四个 Agent，不复制 A／B／C 的主体方法。它只负责：

```text
一个复杂任务怎样多轮收敛；
任务级Source／版本／权限怎样锁；
何时出现第二视角；
何时让人校准或决定；
A→B→C怎样滚动交接；
发现问题怎样精确回开；
已有产物何时需要重审、回修或标stale；
新聊天怎样继续而不重新吞全部历史。
```

## 默认读取

每个新任务先读：

```text
本文件；
01_共享长程执行合同_v0.3.md；
02_Source版本任务授权与人类参与_v0.3.md；
11_本轮问答与实质材料入库.md；
本 Mission 对应 binding；
task-local packet。
```

除下方 GitHub 入口与本轮入库规则外，其他深材料按 handoff、probe、return 或 branch 触发读取。不得把覆层全部文件、三个 Mission 全部 runtime bundle、raw chat 和全部 Harness 同时塞进一个聊天。

## v0.3 相对 v0.2 的实质变化

```text
Mission A handoff加入Feature／method／bounded-state／realization；
Mission B编译加入最低充分表达、method有效绑定和工程实现者probe；
Mission C normal path加入Implementation Judgment四前沿和四类再判断；
A→B→C handoff增加existing-artifact effect和stale传播；
人类参与明确分成Delegation、Calibration、Owner Decision；
runtime source改为generated Project bundles优先，不靠多跳GitHub链接；
Continuation 支持 artifact version、开放义务和下一次必读卷；采用持续工作面后的交接以修订后的 07 为准。
```

旧 v0.2 的 SourceFirst、Branch、人类信号、实现者探针、A→B、B→C、C再判断和自然语言提示都已被本目录完整承接；具体映射见 `MIGRATION_FROM_V0_2.md`。

## GitHub 持续工作面入口（执行修订 2026-09-08）

长程新建、接续或采用本修订时，先读 [09：建图、原位维护和版本管理](O09_GITHUB_WORKSPACE.md)；独立审查及里程碑离站时读 [10：实质审查和下一问题选择](O10_REVIEW_AND_ROUTE.md)。[08](../project_upload_optional/O_08_自然语言运行提示_v0.3.md) 提供可实例化启动语，[07](../project_upload_optional/O_07_Continuation_Branch与上下文控制_v0.3.md) 已改为从持续工作面交接，不再手工维护第二份下一任务。

本目录名保留以兼容已有引用，不复制一个新版本目录；本次执行规则以 `execution_contract_revision: 2026-09-08` 和 exact Git commit 区分。旧运行固定旧提交时仍是旧规则，不会自动升级。候选总体成熟度不变。

同一独立审查回合先检查正文，再参考实际进展和全图选下一问题；不新增每轮必经的协调 Agent。Builder 仍有专业解题自由，但不能自行放行并签发下一业务里程碑。

## 本轮自存与小批补齐（2026-09-08）

[11](O11_TURN_AND_MATERIAL_PUBLICATION.md) 是日常交付必读：Pro 自己保存本轮提示和完整回答，不补历史问答；必要任务正文与有效修订完整入库；总包成员被分别讲解不重复上传；提交后实际核对远端。补齐既有材料使用 [08 的小长程提示](../project_upload_optional/O_08_自然语言运行提示_v0.3.md)，默认 2–3 轮、可提前结束。它不启动新管理 Agent、不改变业务或代码写权，也不宣称已经部署 routine。
