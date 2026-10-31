# 来源与复用：本次特征输入优先，历史按问题读取

## 1. 当前依据与阅读顺序

本分支按Owner批准的新方法组织：基于既有贴近转折及衍生对象，先轻量核框架，再开展具体用例观察，优先取得一个有价值的初版。00—03为完整专业要求，05为启动时设想；运行后采用的当前修订、输入和授权以本Run准确来源为准。

优先读本次实际特征交付及其必要语义、当前任务/方法/设想。遇到具体关系词汇、时间或工具问题，再定向读下方原件。不是先通读U3和全部聊天，再从中挑一个故事套数据。

[两层观察的讨论说明](../../discuss-materials/初始用例设想与两层观察迭代说明.md)保留形成过程中的具体思考，不作为第二套执行规范；假想顺序不是固定状态机。文件中的范围选择仍须接受实际数据反馈。

## 2. 可选业务原文

以下固定版本供理解业务表达和关系语义，不是本轮已验证规律、市场答案或正式特征链前置：

- [U3人读叙事V0.3.0](https://github.com/daowei2026/complex-systems-vocabulary/blob/48f55f53e25d04e5b4b59fae1e652dd4b679c9d3/docs/network-dynamic-ceps-factory/U3_MOVEMENT_QUALITY_ACTIVITY_CONVERSION_ALLOCATION_NARRATIVE_SPEC_V0.3.0.md)：第4节及U3N05，理解推进/摩擦/保持、接近/分化、相对较好与绝对有利的区别。
- [U3用例卡V0.4.0](https://github.com/daowei2026/complex-systems-vocabulary/blob/48f55f53e25d04e5b4b59fae1e652dd4b679c9d3/docs/network-dynamic-ceps-factory/U3_MOVEMENT_QUALITY_ACTIVITY_CONVERSION_ALLOCATION_USE_CASE_CARD_V0.4.0.md)：按需参考细化情境与边界，不当作真实行情验证。
- [U2人读叙事V0.3.0](https://github.com/daowei2026/complex-systems-vocabulary/blob/48f55f53e25d04e5b4b59fae1e652dd4b679c9d3/docs/network-dynamic-ceps-factory/U2_OPPORTUNITY_CLUSTER_SCALE_TURN_NARRATIVE_SPEC_V0.3.0.md)与[U2用例卡V0.4.0](https://github.com/daowei2026/complex-systems-vocabulary/blob/48f55f53e25d04e5b4b59fae1e652dd4b679c9d3/docs/network-dynamic-ceps-factory/U2_OPPORTUNITY_CLUSTER_SCALE_TURN_USE_CASE_CARD_V0.4.0.md)：按需理解多品种转折、过程和关系，不导入全套工程职责。
- [历史U2/U3来源地图](https://github.com/daowei2026/observe-iterate/blob/9badfa6f30caebbe3156c5e4ee4deb43d22cacb5/professional/v2/06_U2_U3_DESIGN_SOURCE_MAP.md)：查具体设计或版本时使用，历史采用不是现场最新版证明。

项目原始附件按需使用，先确认接收角色能取得实际原文，不伪造Git路径：

| 原件 | 定向参考内容 |
|---|---|
| `00_MAIN_SOURCE.md` §6.3、§8—11 | 明确属性关系及其变化；组形成、组自身质量和组外差距不混成分数排名。 |
| `02_PRIMARY_NETWORK_DYNAMIC_USE_CASE_AND_VALIDATION_SOURCE.md` §3.2—3.3、§5、§7 | 不同性质关系和已有业务示例；示例性数据不当作本轮历史事实。 |
| `网络与非线性动力学裸词的业务表达词典（第一版）.md`、`基本的同步和网络词汇整理.md` | 按具体问题理解接近、分化、组及更新；旧机制标签或代码不成为本轮定论。 |
| `同步_策略特征需求规格说明书V0.1.0.0_结合业务分析实践提出特征需求文档模板雏形_创建日期：20240930.docx` | 原有口语化业务用例及细化思路，历史设想不自动成立。 |
| `从嵌合死亡的角度理解不利条件、锯子.docx`、`一个品种是否应当成为重点品种.md` | 业务问题与多角度叙事；不直接采用机制或构造数据结论。 |

参考用于理解，不新增AI重写的示范库，不要求每例包含全部网络词汇，也不强迫形成组或因果解释。

## 3. 旧分支的定向复用

本次基线为 `daowei2026/observe-iterate@674c1be1820dfd5c0bfcb590fe934bf2b0dc328c`，旧分支 `fy/multisymbol-case-observation-20261027` 保留全部历史。新分支不复制旧Run、讨论全集、测试脚本或旧规范。

| 确有问题时可查 | 准确入口与使用边界 |
|---|---|
| aidata接口关系、时间坐标及范围经验 | [旧03](https://github.com/daowei2026/observe-iterate/blob/674c1be1820dfd5c0bfcb590fe934bf2b0dc328c/professional/case_observation/03_AIDATA_USE.md)；只取适用知识，不继承旧品种、时间、mid参数或四例布局。 |
| 旧测试原件和输入示例 | [测试来源](https://github.com/daowei2026/observe-iterate/blob/674c1be1820dfd5c0bfcb590fe934bf2b0dc328c/professional/case_observation/references/aidata_20261027/README.md)、[输入示例](https://github.com/daowei2026/observe-iterate/blob/674c1be1820dfd5c0bfcb590fe934bf2b0dc328c/professional/case_observation/examples/aidata_inputs.py)；不是本次待执行脚本或现场成功证明。 |
| C01—C04、正式CSV及W04实物 | [旧Run](https://github.com/daowei2026/observe-iterate/tree/674c1be1820dfd5c0bfcb590fe934bf2b0dc328c/runs/BI-01-CO-01)；不默认选用旧区间，不继续原四篇修订。必要时只取实际承重片段并保留资格。 |
| 历史讨论来历 | [旧讨论目录](https://github.com/daowei2026/observe-iterate/tree/674c1be1820dfd5c0bfcb590fe934bf2b0dc328c/discuss-materials)；不是主控或专业每轮必读。 |

旧事实、失败和资格按原版本保留，引用不代表重做。旧GO、Binding、预算、在途、管理接收和环境待办不继承到新Run。当前任务不绑定或启动其他具名业务工作。
