# Absorb｜吸收交互｜统计驱动单 Feature Run 输入

> 此文件**只定义业务任务和实例来源**。共同版本、数据范围、exact Wall 和历史边界见 [COMMON_INPUT.md](COMMON_INPUT.md)；Workflow、Skill 和调用／授权协议依 Run 的统一采用来源，不在这里重复。

## 1. 目标与范围

```yaml
target_feature: AbsorbAssembler
business_name: Absorb｜吸收交互
tis_source: daowei2026/tis@179016111ed0394f92025313e46bd13534932a74:hf/prel0/absorb_assembler.py
parameter_instance: absorb-default（当前代码默认值，运行前核完整 ppdict）
formal_product: absorb_interaction
p1_frp_contract_reference: mquant.tis.frp.EawBattleP.EawP1AbsorbInteractionFrp
p1_dsu_contract: AbsorbInteractionDSU
business_task: 对当前正式实例做 U/X/G，发现高置信不合理 finding 后逐一 D、必要修正和后续轮次，直到当前范围下完成判断
```

## 2. 特别需要保留的 Feature 事实与边界

- 目标是一次绑定 exact Wall 的 Absorb interaction，区分 `InteractionStarted`、`ConsumptionMilestone`、`Resolved` 的对象身份、状态及时间语义。
- 本实例依当前默认 `VolQuant/QuoteTrack` 相关输入与参数；在实际代码和真实运行中核对，不预先替换参数或输出合同。
- 11/23 的旧 `OI-ABSORB-STAT-20261123-01` 只是历史参考，不接续其 manager/E1、D/C、未完成状态，也不把旧报告视为新 Run 的完成产物。

## 3. 正式输入和完成边界

与 [COMMON_INPUT.md](COMMON_INPUT.md) 同一 SOF、rb/m、2021 全年、Calendar；`WallAssembler` 必须是同 commit、同范围、当前默认参数及准确 receipt 的技术上游。该 Feature 自己的正式数据、对象键、输出字段、内部处理链、统计内容与发现判断由被调用 Skill 查代码、实例和真实产物得出。

本 Run **只以 AbsorbAssembler 为目标**，不把另外两个 Feature 当作本 Run 的专业交付，也不重新做 Wall 合理性 Run、CAEGraph、Exhaustion 或 P2/P3 的独立 Workflow。

当前版本无合格正式产物时应运行实际市场数据；已存在结果只有完成当前代码／参数／数据／receipt／读回同一性核验才可复用。发现的问题由 executor 在启动 GO 的授权范围内自主修正并重新验证，不增加运行中 Owner 审批。

业务来源采用共同输入中列出的 P1 正式架构、对应 DSU 和原始组装器规范；需记录现有代码与原设计的差异，不以实现事实直接替代业务预期。
