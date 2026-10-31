# 观察研究Agent：基于既有特征形成可迭代用例

本分支采用 [基于既有特征的两层观察方法](professional/case_observation/README.md)：从贴近转折点、线段及属性关系出发，发现现象和候选规律，利用它们提前判断后续品种走势、机会与反向风险，优先形成一个有业务价值的初始用例。

**当前仅完成新方法和运行接线准备，未启动任务，未宣称数据已到或图面已通过。** 正式运行仍须真实Owner GO、独立Run、实际输入和原机制下的管理采用。

## 当前入口

| 需要理解什么 | 文件 |
|---|---|
| 完整目的、产出与完成边界 | [00 目标与产出](professional/case_observation/00_PURPOSE_AND_OUTPUTS.md) |
| 当前先试的框架及尚未成立的前提 | [05 初版场景设想](professional/case_observation/05_INITIAL_SCENARIO.md) |
| 怎样按时间观察、何时进入具体研究 | [01 两层观察方法](professional/case_observation/01_RESEARCH_METHOD.md) |
| 实际特征、确认语义及图面使用 | [03 特征数据与视图](professional/case_observation/03_FEATURE_DATA_AND_VIEWS.md) |
| 用例、观察材料和Owner交流 | [02 业务交付](professional/case_observation/02_OWNER_DELIVERY.md) |
| 按问题取得原文与旧实物 | [04 来源复用](professional/case_observation/04_SOURCES_AND_REUSE.md) |

第一层只取得足以研究的背景和结构，不先做全历史分段；第二层实际形成、检验和修订后续品种判断。两层可往返，不是两个固定Gate。当前同向大尺度框架是优先尝试的选择，不是已证实规律或唯一研究路径。

方法与设想分开维护：00—04规定专业责任，05是启动设想；运行中采用的修订及其依据保存在本Run。首轮不再固定3—5例，不以完整历史中最终整齐、最终谁较好倒选候选；不以工具成功代替业务进展。

## 分支内容与历史

- 新分支：`fy/feature-based-case-observation`。
- 基线：旧分支 `fy/multisymbol-case-observation-20261027` 的 `674c1be1820dfd5c0bfcb590fe934bf2b0dc328c`。原分支保持不变。
- 新工作树替换专业正文；旧CO-01、旧案例/数据/日志、旧输入示例和讨论全集不复制为当前上下文，需要时从[历史入口](runs/README.md)定向读取。
- `discuss-materials/`保留[两层观察说明](discuss-materials/初始用例设想与两层观察迭代说明.md)原文作为来历，不是第二套专业规范。
- 通用runtime协议、工具、测试和必要兼容材料复用；本次只更新专业接线说明与配置，不改工具代码或消息协议。

## 从准备到启动

见 [运行指南](runtime/operations/CASE_OBSERVATION_RUN_GUIDE.md)、[采用状态](runtime/config/ADOPTION_STATUS.md)和[运行机制](runtime/README.md)。配置目前NOT_CONFIGURED，NEW_RUN_ID为占位符；尚未建立实际Run或有效派发。

实际数据交付到达后，补入品种/范围、尺度配置、方向与确认语义、对象状态、图数入口和必要缺口；已有适用正式交付直接消费，不重复取数或全套环境预检。主控不代写业务场景，Worker结果回原签发Pro。方法修改不绑定或启动其他业务、设计或实现任务。
