# 观察迭代 Agent — 专业 V2-02（准备，尚未正式启动）

**业务目标：**先阅读 U2/U3 叙事与设计，弄清共同方向机会中为何要分辨成员强弱；从已提前验算的 rb/i/hc 基础 K 线、Zig、贴近转折行情自主找到有研究意义的位置，再检查 U2 对机会/成员的识别、U3 四方面当时能否区分后续运动质量、与 C0/N 及简单关联相比有无增量，形成 Owner 可按图核验的判断及设计修订方向。具体场景分类、样本配额和赢家不预设。

工作步骤：**S1 理解叙事、先看基础行情并选择场景 → S2 用 aidata 出基础图、再定向叠加 U2/U3 并提供同源数据 → S3 以合法 As-Of 的 U3 四方面对照后续质量并给业务判断**，需要时 S3 再返回 S2。AI **本轮不视觉看图**：图给 Owner，AI 读图对应的结构化数据。

## 当前入口

- [专业 V2 总入口](professional/v2/README.md)和[业务总目标](professional/v2/00_PURPOSE_AND_THREE_STEP_FLOW.md)
- [07：叙事驱动、基础行情先行的场景观察方法](professional/v2/07_BUSINESS_SCENE_OBSERVATION_METHOD.md)
- [06：U2/U3 人读叙事及详细设计来源](professional/v2/06_U2_U3_DESIGN_SOURCE_MAP.md)
- [已积累的原 I1/I2/I3 业务背景与有权 Source](professional/v2/04_BI01_BUSINESS_BASELINE.md)
- [固定两份 ZIP 的位置、清单、数据身份与差异](professional/v2/05_BI01_FIXED_INPUT_DATA.md)
- [aidata 只读优先/确需修改另建分支的规则](professional/v2/01_AIDATA_CHART_AND_DATA.md)
- [全新预备运行 BI-01-V2-02](runs/BI-01-V2-02/README.md)及[运行指南](runtime/operations/BI01_V2_RUN_GUIDE.md)
- [旧 BI-01-V2-01 暂停运行史料](runs/BI-01-V2-01/README.md)，旧业务接收、授权和活动 Gate 均不继承

本轮原件为 `steel_U2_U3_执行结果_20261010.zip` 和 `rb_hc_i_mid贴近转折_zig_small_K线_20210101_20240229.zip`。不重新验算一版或替换源；对已验算数据发现具名疑问可以核查与反馈。上游 ZIP 的本次外层哈希与旧讨论记录存在差异，详情见固定数据文档，不能静默解释为同一字节，也不凭此断言业务数据必错。

长程管理/角色/回交机制仍在 `runtime/`；图和数据工具统一使用 [aidata](https://github.com/daowei2026/aidata)，尽量不修改。确需修改/新增时必须在 aidata **新分支**实施，不改现有分支。原 I1–I3 的业务知识以来源和 V2 专题文档复用；旧 V2-01 已被 Owner 暂停，其已有图/同源数据经版本和浏览器核验后可作历史技术输入，但不继承旧选样、聊天、Gate 或任务状态。

状态：`PREPARED_NOT_STARTED / NO_SEND`；本次只是修改运行材料，没有实际发起新 Pro、Worker 或手机任务。
