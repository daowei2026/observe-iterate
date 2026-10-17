# 观察迭代 Agent — 专业 V2（未正式开跑）

**业务目标：**使用已提前验算的 rb/i/hc 真实数据，判断 U2 共同机会簇识别的位置与边界是否合理，以及在这些位置上 U3 四方面能否辨别品种好不好做；指出具体不合理处、原因、反证与有无业务增量，形成可供 Owner 看图核验的观察和后续修订方向。

工作步骤：**S1 确定观察对象与问题 → S2 用 aidata 为既定数据画图并提供同源数据 → S3 根据同源数据给出业务想法**，需要时 S3 再返回 S2。AI **本轮不视觉看图**：图给 Owner，AI 读图对应的结构化数据。

## 当前入口

- [专业 V2 总入口](professional/v2/README.md)和[业务总目标](professional/v2/00_PURPOSE_AND_THREE_STEP_FLOW.md)
- [已积累的原 I1/I2/I3 业务背景与有权 Source](professional/v2/04_BI01_BUSINESS_BASELINE.md)
- [固定两份 ZIP 的位置、清单、数据身份与差异](professional/v2/05_BI01_FIXED_INPUT_DATA.md)
- [aidata 只读优先/确需修改另建分支的规则](professional/v2/01_AIDATA_CHART_AND_DATA.md)
- [全新预备运行 BI-01-V2-01](runs/BI-01-V2-01/README.md)及[运行指南](runtime/operations/BI01_V2_RUN_GUIDE.md)

本轮原件为 `steel_U2_U3_执行结果_20261010.zip` 和 `rb_hc_i_mid贴近转折_zig_small_K线_20210101_20240229.zip`。不重新验算一版或替换源；对已验算数据发现具名疑问可以核查与反馈。上游 ZIP 的本次外层哈希与旧讨论记录存在差异，详情见固定数据文档，不能静默解释为同一字节，也不凭此断言业务数据必错。

长程管理/角色/回交机制仍在 `runtime/`；图和数据工具统一使用 [aidata](https://github.com/daowei2026/aidata)，尽量不修改。确需修改/新增时必须在 aidata **新分支**实施，不改现有分支。旧业务合同和旧 run 已从 V2 工作树删除，**原 I1–I3 的业务知识以来源和 V2 专题文档复用**，不继承旧运行聊天、Gate 或任务状态。

状态：`PREPARED_NOT_STARTED / NO_SEND`；本次只是修改运行材料，没有实际发起新 Pro、Worker 或手机任务。
