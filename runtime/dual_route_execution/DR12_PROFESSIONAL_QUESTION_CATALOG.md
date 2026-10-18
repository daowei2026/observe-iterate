# BI-01 V2 专业问题与来源索引

## 1. 本轮业务主轴

当前专业工作只用 **S1 确定观察对象 → S2 使用 aidata 形成图及同源数据 → S3 给观察想法**，S3 需要继续观察时可回到 S2。题号只用于有权任务和接续，不代表新增角色、写权、手机派发授权或新 Gate。

**完整目标：**从 U2/U3 的 Owner Decision、Narrative 和 Use Case 理解 `DirectionalReleaseIntent` 下多个品种共同单边方向机会以及成员运动质量为什么需要被识别，再从固定 rb/i/hc K线、Zig、贴近转折基础行情自行确定真实值得观察的位置；检查 U2 实际识别的共同机会/成员边界，在这些位置以 U3 的 Progress、Friction、Retention、ObservabilityAndConstraint **当时已知**的字段判断能否区分成员强弱、后续市场运动支持还是反证，是否比 C0/N 和简单共同事件关联更有价值。场景类别、阈值、选样数量由实际观察决定，**不在合同里预分类**；固定两份预计算输入不补算正式 U3。

## 2. 专业来源与具体题

| 题号 | 主要问题 | 方法与交付 |
|---|---|---|
| S1 | 从原 U2/U3 叙事理解场景，通过基础 K线/贴近转折观察自主选真实位置 | [00 业务总目标](../../professional/v2/00_PURPOSE_AND_THREE_STEP_FLOW.md) + [07 场景观察方法](../../professional/v2/07_BUSINESS_SCENE_OBSERVATION_METHOD.md) + [06 原设计入口](../../professional/v2/06_U2_U3_DESIGN_SOURCE_MAP.md)：先行情后设计验证，非固定类别、配额或赢家 |
| S2 | 用现有 aidata 先画基础行情与对应数据，再在具名位置显示 U2/U3/N 层 | [01 aidata](../../professional/v2/01_AIDATA_CHART_AND_DATA.md) + [05 固定 ZIP](../../professional/v2/05_BI01_FIXED_INPUT_DATA.md) + [07 方法](../../professional/v2/07_BUSINESS_SCENE_OBSERVATION_METHOD.md)：真实浏览器可见、时间与图数同源 |
| S3 | U2 找位和成员是否合理，U3 四方面能否在当时辨别后续强弱、正反事实、既有基线增量及不足 | [02 业务分析](../../professional/v2/02_OBSERVATION_IDEAS_AND_VALIDATION.md) + [07 方法](../../professional/v2/07_BUSINESS_SCENE_OBSERVATION_METHOD.md)：明确哪些只是描述、哪些已有可信的 Current→Outcome 对照、哪些因缺项不可判 |
| 全部 | 管理、Worker 委派与结果交接 | [V2 交接](../../professional/v2/03_EXECUTION_HANDOFF.md)及真实角色协议 |

## 3. 管理、审查和局部问题

- M-START：从实际 Owner GO 形成真实管理地图、任务和签发；没有现行地图可合法先 BOOTSTRAP。
- M-REASSESS：重要图与数据结果、设计反证、Owner 反馈或到期投入复看时，对完整目标作新安排。
- M-CLOSE：检查完整目标与所有未完成处，决定真实接收、继续或有据等待。
- AUDIT / INDEPENDENT_REVIEW：仅凭明确审查权限和真正覆盖的专业方法评价，不以管理认可冒充独立检查。
- CASE-...：有真实业务必要时的具名局部研究问题。必须保留 S1–S3 总目标和任务的全部剩余，不能因为局部 Case 完成而主动收工。

## 4. 源读取和真实交付

管理/专业任务必须准确定位并真正读取 [00 当前业务目的](../../professional/v2/00_PURPOSE_AND_THREE_STEP_FLOW.md)、[07 叙事驱动的业务场景方法](../../professional/v2/07_BUSINESS_SCENE_OBSERVATION_METHOD.md)、[06 U2/U3 设计导航](../../professional/v2/06_U2_U3_DESIGN_SOURCE_MAP.md)及本次承重的 Owner Decision/Narrative/Use Case **完整原文**、[04 原 I1–I3](../../professional/v2/04_BI01_BUSINESS_BASELINE.md)、[05 固定两份 ZIP](../../professional/v2/05_BI01_FIXED_INPUT_DATA.md)，再按阶段读 01/02/03。真正的 source_reads 要带 Git exact commit/path/selector，不能以导航标题当已阅读。新的 `BI-01-V2-02` 自主选择市场场景，旧 `BI-01-V2-01` 的选样、任务、Gate/回交及在途不继承；旧图数只能核实来源后有限复用。分析重点是 U3 对后续强弱的辨别，不是细字段问题的数量。

**本轮不重算或替换既定数据**。若发现数据具体疑问，具名报告成员、时间/字段、方法与受影响判断，允许有限核查并反馈；不借机重新生产 U2/U3。Worker 优先原样使用 aidata；实际必须扩展时只在 **aidata 新建独立分支**施工，不改其现有分支、不在 observe-iterate 另造图系统。**AI 本轮不视觉看图**：Owner 看图，AI 看同图对应的 CSV/图层数据；图成不等于业务分析完成。
