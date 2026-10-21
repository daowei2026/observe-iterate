# 具体特征观察：仓库修改后准备 3 审查记录

审查日期：2026-10-21；审查对象：`daowei2026/observe-iterate@fy/bi01-feature-observation-prep-20261021`，以旧 `fy/bi01-v2-02-business-scene-20261018@34f6df18ffe111daf83b638026f117e46d150828` 为改动基线。

**资格：本次为仓库文本、源引用和配置结构的准备性自查，不是独立专业审查，不是现场执行验收，也不构成新的 Owner GO。** 下述事实只表示所列检查真实做过；未做的部分不能被推定通过。

## 1. 对照已确定的专业目标

新主干为以下四项：初始合理参数、特征展示方式、aidata 实际制图、围绕特征正确性与普通投资者正常解读的观察分析。

- 四项是**可往返的专业工作内容**，不设四个串行阶段或四次 Pro/Gate。
- 具体已实现且可取得数据的特征是本轮观察主体，当前优先研究 CYF 提供的 `U2NormalNodeBehaviorFrp`；正式工作需锁实际特征版本和数据，不能凭讨论文字认定已经取得本次结果。
- 原 S1–S3 **工作划分退出**，保留其中仍有用的专业知识。U2/U3 整体业务任务不继承，仅在本特征需要时作为上下文。
- 基本输出格式允许格式以外的有效分析；工作细节不要求在运行前预制一切专业结论，但已知或有充分理由预见的重要夜间阻断必须提前处理。

以上已分别进入 `professional/feature_observation/00`～`04` 与当前专业入口，并同步到 DR12、DR13、DR14 和操作端现行专业载荷段。

## 2. 发现并修正的确定问题

| 改动前确定问题 | 实际处理 | 静态检查边界 |
| --- | --- | --- |
| 旧 V2-02 在本仓的 Workmap Binding 实为 `ADOPTED`，而早期说明文本称未配置；不能让新任务误继承旧管理授权 | 新候选分支设为结构完整的 `NOT_CONFIGURED`，路径明确为 `<NEW_RUN_ID>` 占位，旧 run 的真实结果和采用历史保留在原记录/提交中 | JSON 可解析，尚无新地图/Owner GO，绝不标为 ADOPTED |
| 原 active 专业及运行入口仍把 S1–S3、旧两包、完整 U2/U3 当作当前目标 | 调整 root/professional/runtime 入口、Overlay08 有效角色片段、DR06/08/12/13/14、Overlay09/10/12/13 等具名当前使用位置 | 已审的主入口不再以旧 V2 文档作为现行必读专业合同，历史 V2 文件保留并标明来源性质 |
| 原 `COORDINATOR_DISPATCH` 把 S1、S2、S3 作为三个专业 mode | 新配置只有一个 `FEATURE_OBSERVATION` 专业 mode，原 M-START/M-REASSESS/M-CLOSE 与 INDEPENDENT_REVIEW 保留 | JSON 解析正常；mode 名称与新任务模板一致；未实际运行派发器 |
| 原 V2-02 地图、当前任务和 Binding 模板写死旧 run ID、S1–S3、固定 ZIP | 在 `runtime/operations/feature_observation/templates/` 新增**非活动**地图、当前任务及 Binding 模板；保持原地图七个 anchors 和既有 Binding schema；实际 run ID 等待 Owner 授权 | 占位不可直接派发；旧模板留作历史，不改写旧运行原件 |

## 3. 已进行的静态核查

1. **Git 改动范围：** 相对旧基线，在记录此次审查之前已有 7 次准备提交，变更 34 个路径（24 修改、10 新增），没有删除、重命名历史业务资料或改动旧 `runs/BI-01-V2-02` 运行成果。该统计来自 GitHub compare。
2. **配置结构：** `runtime/config/COORDINATOR_DISPATCH.json` 的 goal_ref 指向 `professional/feature_observation/00_PURPOSE_AND_FOUR_WORKS.md`；合法 mode 包括 `FEATURE_OBSERVATION`；当前及非活动模板 Binding 均为 `NOT_CONFIGURED`，现用 Binding 未保留旧实际采用路径。
3. **长程模板：** 新地图模板确实包含 `goal/stage/evidence/progress/remaining/management/next` 七个 section anchors，与新 Binding 模板中的 map.anchors 顺序一致；新 task 模板使用 `FEATURE_OBSERVATION`，run ID 是待确定占位。
4. **操作提示词标记：** `runtime/overlay/08_自然语言运行提示_v0.3.md` 的 `MANAGEMENT_DUTY`、`MANAGEMENT_STAGE_BI01`、`TASK_DUTY`、`STAGE_BI01`、`READONLY_RECEPTION_BI01`、`RETURN_REPAIR`、`REFERENCE_USE` 每个 BEGIN/END 均各保留一次；该文件没有现行 `professional/v2/` 强制取源链接。
5. **文档链接：** 对 root/professional/runtime、操作及 DR 等 23 个主要修改文件核对了 123 个相对 Markdown 链接，均能在当前 Git tree 找到目标路径；新增专业目录入口的 5 个局部链接此前亦已核对。外部链接并非真实访问测试。
6. **新旧权限：** 当前只是专业方法准备，不存在对本新任务实际发出的 Owner GO、管理签发、run ID、有效 Workmap Intake 或手机消息；旧 V2-02 的真实已采用和执行记录不因文字替换而失去历史事实，也不向新任务转移权限。

## 4. 仍须真实执行环境核查的条件（不能假称已通过）

以下是**尚未验证的必要关系，不等于已经证明存在故障**；到具名特征的现场代码、数据与操作环境具备时，应优先核实会不会阻碍夜间无人值守推进：

- **确切特征身份与数据消费：** `U2NormalNodeBehaviorFrp` 对应的实际代码版本、输出和读取接口能否准确给本次 Agent 使用。CYF 已经跑出数据，不等于 aidata 已能按当前 `Feature.rerun().to_df()/to_dfs()` 合同直接读取保存结果；需依据真实读取路径验证，而不能凭口头“已跑通”闭合。
- **展示方案与 aidata：** 实际需画的内容，现有 `feature_configs` 和点/线/线段等显示合同是否覆盖；已设计的画法是否能转成实际页面，必要时检验浏览器图层可见和数据对应；缺工具能力时按 aidata 自身独立分支处理。
- **新 run 的运行链：** 只有收到新 Owner GO、确定真实 run 身份和有权管理任务后，才能填补 `<NEW_RUN_ID>`、确定 Binding、取得 Intake、运行现有 Gate、核 cgpterm/专业仓版本和实际 Worker 能力。现阶段不能用历史测试、配置结构或静态校验宣称这一新链已经跑通。
- **现场运行验收：** 尚未在本会话内运行真实 Pro/Worker、特征读回、Bokeh 浏览器、手机发送或无人值守持续轮次，也没有在执行工作区跑 runtime Python 测试；这些应由实际授权与可用运行环境完成相应检查。

有明确前置阻断时，应在允许夜间无人值守运行前修复或安排不依赖问题的合法路径；尚不确定的专业理解/画法/参数优化可以由四项工作实际执行迭代解决。

## 5. 当前审查结论

**准备 1、准备 2 的初版，以及准备 3 的仓库文本/配置一致性审查和相应修正已形成。** 目前未发现主入口继续强制执行旧 S1–S3 的未消除矛盾；没有依据宣布新的真实长程运行已经准备就绪。下一步是否进入现场条件核查、真实授权和启动，由 Owner 基于当前实际执行环境和专业实例决定。

此记录是审查输入和自查事实，**不是独立审查 PASS、业务分析完成或正式 Owner GO**。
