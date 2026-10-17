# BI-01 V2 专业问题与来源索引

## 1. 本轮业务主轴

当前专业工作只用 **S1 确定观察对象 → S2 使用 aidata 形成图及同源数据 → S3 给观察想法**，S3 需要继续观察时可回到 S2。题号只用于有权任务和接续，不代表新增角色、写权、手机派发授权或新 Gate。

**完整目标：**使用本轮 **rb/i/hc 已提前验算且固定的两份数据包**，检查 U2 共同机会簇识别的位置/边界是否合理、这些位置的 U3 四方面能否辨别品种好不好做，得到具体不合理处、原因、反证及有无新增业务认识。四方面的字段与状态须按有效业务 Source 和固定 CSV 核对，不能补算虚构。

## 2. 专业来源与具体题

| 题号 | 主要问题 | 方法与交付 |
|---|---|---|
| S1 | 固定范围内确定要检验的业务现象及合理性问题 | [V2 目标](../../professional/v2/00_PURPOSE_AND_THREE_STEP_FLOW.md) + [原 I1–I3 业务底稿](../../professional/v2/04_BI01_BUSINESS_BASELINE.md) + [U2/U3 叙事、详细设计与实际参考方法来源](../../professional/v2/06_U2_U3_DESIGN_SOURCE_MAP.md)：OP-01/Q-01、设计预期、四方面映射与合法对照 |
| S2 | 对现成已验算的参考结果画什么图、如何保持图数同源 | [固定 ZIP、CSV 和取用位置](../../professional/v2/05_BI01_FIXED_INPUT_DATA.md) + [aidata 制图合同](../../professional/v2/01_AIDATA_CHART_AND_DATA.md)：Owner 图、AI 同源数据和时间/来源资格 |
| S3 | 市场过程与特征判断是否合理、为何如此、是否有反证 | [观察想法与验证](../../professional/v2/02_OBSERVATION_IDEAS_AND_VALIDATION.md)：Owner 可按图审阅的发现、解释和未决 |
| 全部 | 管理、Worker 委派与结果交接 | [V2 交接](../../professional/v2/03_EXECUTION_HANDOFF.md)及真实角色协议 |

## 3. 管理、审查和局部问题

- M-START：从实际 Owner GO 形成真实管理地图、任务和签发；没有现行地图可合法先 BOOTSTRAP。
- M-REASSESS：重要图与数据结果、设计反证、Owner 反馈或到期投入复看时，对完整目标作新安排。
- M-CLOSE：检查完整目标与所有未完成处，决定真实接收、继续或有据等待。
- AUDIT / INDEPENDENT_REVIEW：仅凭明确审查权限和真正覆盖的专业方法评价，不以管理认可冒充独立检查。
- CASE-...：有真实业务必要时的具名局部研究问题。必须保留 S1–S3 总目标和任务的全部剩余，不能因为局部 Case 完成而主动收工。

## 4. 源读取和真实交付

管理/专业任务必须准确定位并真正读取 [00 V2 业务目标](../../professional/v2/00_PURPOSE_AND_THREE_STEP_FLOW.md)、[04 原 I1–I3 业务依据](../../professional/v2/04_BI01_BUSINESS_BASELINE.md)、[05 当前两份预计算 ZIP 与位置](../../professional/v2/05_BI01_FIXED_INPUT_DATA.md)、[06 U2/U3 人读叙事、详细设计与参考方法来源](../../professional/v2/06_U2_U3_DESIGN_SOURCE_MAP.md)，再按实际步骤读取 01/02/03 及 06 指向的承重原文。真实 source_reads 必须带准确 Git commit/path/selector；只有 ZIP 名称或导览不代表 Pro 已取得 CSV，也不代表用例候选合同已成为正式生效算法。旧 I1–I3 业务知识可以复用，旧 run 的 Gate/Pro 答复/在途不继承。

**本轮不重算或替换既定数据**。若发现数据具体疑问，具名报告成员、时间/字段、方法与受影响判断，允许有限核查并反馈；不借机重新生产 U2/U3。Worker 优先原样使用 aidata；实际必须扩展时只在 **aidata 新建独立分支**施工，不改其现有分支、不在 observe-iterate 另造图系统。**AI 本轮不视觉看图**：Owner 看图，AI 看同图对应的 CSV/图层数据；图成不等于业务分析完成。
