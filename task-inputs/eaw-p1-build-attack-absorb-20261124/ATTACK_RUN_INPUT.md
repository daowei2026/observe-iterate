# AttackSegment｜贴墙攻势段｜统计驱动单 Feature Run 输入

> 此文件**只定义业务任务和实例来源**。共同版本、数据范围、exact Wall 和历史边界见 [COMMON_INPUT.md](COMMON_INPUT.md)；Workflow、Skill 和调用／授权协议依 Run 的统一采用来源，不在这里重复。

## 1. 目标与范围

```yaml
target_feature: AttackFlowAssembler
business_name: AttackSegment｜贴墙攻势段
tis_source: daowei2026/tis@179016111ed0394f92025313e46bd13534932a74:hf/prel0/attack_flow_assembler.py
parameter_instance: attack-default（当前代码默认值，运行前核完整 ppdict）
formal_product: attack_segment / attack_formation_evidence / wall_relation_barrier
p1_frp_contract_reference: mquant.tis.frp.EawBattleP.EawP1AttackSegmentBookFrp
p1_dsu_contract: AttackSegmentBookDSU
business_task: 对当前正式实例做 U/X/G，发现高置信不合理 finding 后逐一 D、必要修正和后续轮次，直到当前范围下完成判断
```

## 2. 特别需要保留的 Feature 事实与边界

- 当前默认正式实例除 Wall 外，选择 tactical 与 structural 两套 `DirectedBigDealTick`／F4 资格族。两套资格流的参数、资格、范围及 product receipt 需要按实际实例核对，不由输入稿另造。
- 一个 `AttackFlowAssembler` 生成 `attack_segment`、`attack_formation_evidence`、`wall_relation_barrier` 三类相关产品；应区分完整段、形成材料与 formal barrier，不能混成同一种 occurrence。
- 本 Feature 不消费 Build 和 Absorb 的正式产物；墙结束等信息来自 exact Wall。

## 3. 正式输入和完成边界

与 [COMMON_INPUT.md](COMMON_INPUT.md) 同一 SOF、rb/m、2021 全年、Calendar；`WallAssembler` 必须是同 commit、同范围、当前默认参数及准确 receipt 的技术上游。该 Feature 自己的正式数据、对象键、输出字段、内部处理链、统计内容与发现判断由被调用 Skill 查代码、实例和真实产物得出。

本 Run **只以 AttackFlowAssembler 为目标**，不把另外两个 Feature 当作本 Run 的专业交付，也不重新做 Wall 合理性 Run、CAEGraph、Exhaustion 或 P2/P3 的独立 Workflow。

当前版本无合格正式产物时应运行实际市场数据；已存在结果只有完成当前代码／参数／数据／receipt／读回同一性核验才可复用。发现的问题由 executor 在启动 GO 的授权范围内**仅修改当前目标 Feature 自身**并重新验证；Wall、F3/F4、其他 Feature、公共处理器与上游数据一律不得修改。若责任逻辑位于上游，形成具名上游问题与本 Run 影响记录，不抢改上游，也不增加运行中 Owner 审批。

业务来源采用共同输入中列出的 P1 正式架构、对应 DSU 和原始组装器规范；需记录现有代码与原设计的差异，不以实现事实直接替代业务预期。
