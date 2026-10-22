# 四项专业工作的初步细节（运行中继续迭代）

本文件只补充初始执行所需的思路及适用边界；其中专业方案可以根据具体特征和真实观察持续修改。**不在准备阶段预先穷尽所有参数方案、画法、正反例和业务结论。**

## 0. 开始时对准具体实例

从本次可运行特征及其实际代码、已生成结果和必要设计来源中，了解：它是什么、希望表达什么、消费什么输入、输出什么结果、可配置哪些参数，哪些内容已经真实计算而不是仅有设计。必要时回看 U2/U3 对应源设计，但不是自动把原 U2/U3 全套职责搬进来。

目前优先实例为 **U2NormalNodeBehaviorFrp**。CYF 2026-10-21 10:24 的具体反馈已说明其当前涉及两个完成过程窗口（最近六段与此前六段）、当前未完成过程、推进/幅度/持续/行程/效率/逆向运动及当前节律等。该说明是研究入口，实际运行时仍应核定具体版本和数据读出结果，不凭本文代替源合同。

**已有实例与来源可先参考，不必从零猜：**[CYF 的 U2NormalNodeBehaviorFrp 单特征任务说明](https://github.com/daowei2026/feature-refinement-implementation-agent-evolution/blob/main/agent_evolution/pilot_cases/network-dynamic-ceps-factory-u2-u3/implementation-start-prompts/U2_NORMAL_NODE_BEHAVIOR_FEATURE_TASK_20261016.md)定位了 FRP 的 `U2NormalNodeBehaviorFrp / constructNormalNodeBehaviorFrp`，以及 TIS 的 `U2NormalNodeBehaviorFrp.from_sources(sources)`、`to_dfs(products=...)`。先用它寻找真实实例化、结果读回与方法合同，再核当时和本次实际源码/数据版本，不能把该历史任务说明当成当前已完成证明。

**同一 N 特征此前真实运行的实例（优先作为本轮初始参数参考）：** [R30 实际运行配置 `ACTUAL_RUN_CONFIGURATION.json`](https://github.com/daowei2026/feature-refinement-implementation-agent-evolution/blob/main/agent_evolution/pilot_cases/network-dynamic-ceps-factory-u2-u3/runs/first-two-fao-20261017/ENGINEER_STORAGE_REDUCTION_R30/ACTUAL_RUN_CONFIGURATION.json)。原件记录 `U2NormalNodeBehaviorFrp`、rb/hc/i、5m、`night_end_at_2300`、`MedianTwoWindowV1`、完成过程 6、LOO 最低 3、`core.v2` 等当次实际配置；同目录的 [R30 工程回交](https://github.com/daowei2026/feature-refinement-implementation-agent-evolution/blob/main/agent_evolution/pilot_cases/network-dynamic-ceps-factory-u2-u3/runs/first-two-fao-20261017/ENGINEER_STORAGE_REDUCTION_R30/FULL_RESPONSE.md)和 [OnlyRead 记录](https://github.com/daowei2026/feature-refinement-implementation-agent-evolution/blob/main/agent_evolution/pilot_cases/network-dynamic-ceps-factory-u2-u3/runs/first-two-fao-20261017/ENGINEER_STORAGE_REDUCTION_R30/READ_REAL_N_01_BINDING.json)支持其真实运行和结果读取；[R33 管理接收](https://github.com/daowei2026/feature-refinement-implementation-agent-evolution/blob/main/agent_evolution/pilot_cases/network-dynamic-ceps-factory-u2-u3/runs/first-two-fao-20261017/MANAGEMENT_N_REASONABLENESS_RECEPTION_R33/FULL_RESPONSE.md)明确首版 N 本项接收。**引用它是为了先有可追溯的真实实例，而不是规定本轮参数不能调整，更不是证明已经能够用 aidata 画出该特征。**

**另一个用于学习实例化和制图调用的已运行示例：**[aidata/examples/microstructure_review.py](https://github.com/daowei2026/aidata/blob/main/examples/microstructure_review.py)实例化 Zig/ScaleTurn/Thick，组织 `run_brief` 并生成图页；其运行和验收入口见[aidata/tests/README.md](https://github.com/daowei2026/aidata/blob/main/tests/README.md)。它是**技术调用形式参考**，不是本次 N 特征已接入 aidata，也不代表参数应照搬。


## 1. 初始合理参数

- 先识别当前特征实际使用的参数及来源，也包括通过上游输入、子处理器和配置层层传入的参数。
- 考虑第一轮观察采用既有实际配置还是在有依据时先提出调整；不要求在没有真实图与分析之前，就证明一套参数已达到最终最优。
- 要留意“参数改变了什么”，区别影响特征实际结果的配置，与仅影响窗口和图形展示的配置；实际比较时说明比较的是否仍是同一特征实例。
- 无法确定的参数依据如实留待查询或观察，不把推测填作真实实现。

初始结果可以是**实际配置及依据 + 候选调整点**，不必先生成一个覆盖各种市场情况的参数优化方案。

## 2. 特征展示方式

- **主要参照实际采用版本的 uplot，而非从 aidata 现有页面或大中小图式反推设计。**先读 `CAEGraph使用手册.md`，结合本特征业务语义及真实输出选择布局、主/附图、点/线/线段、文本和交互等适用表达，不照抄单一示例。Owner 提供的核对起点为 [uplot/e6.2 手册的准确版本](https://github.com/daowei2026/uplot/blob/0a4fcd54059782572a3f7e82fad041121e8c65ad/CAEGraph%E4%BD%BF%E7%94%A8%E6%89%8B%E5%86%8C.md)；实际使用仍记录锁定版本，不推定所有 N 画法均已支持。
- 先选择真正有助于理解业务含义、输出变化和重要正确性问题的信息；其他输出、中间值可只用于核查。分别判断哪些适合叠加 K 线，哪些应使用独立附图或其他图形，不为了全显示而挤进 K 线图。
- 工作 2 自己决定被选信息所需的横纵轴、时间位置、点/线/区间、线型、形状、状态及更新方式、图层关系和业务含义。图形承担主要展示责任；表格按需辅助准确值、身份和核查，文字辅助解释短标签/图例不能说明的含义，不以长文代替画法。
- **展示对象不固定为一个 As-Of 的 6+6+Working 截面。**依据真实输出设计沿市场时间查看演变、选择任意或若干特殊时点回看的表达，区分实际发生、确认/可知、当时 As-Of 与后来修订，说明输出怎样产生、保持和改变。连续图形与修订显示须核其可消费数据，不预设三条曲线、逐拍绘图/重算或实时直播。
- 不以“先单品种还是多品种”作为本项独立任务或验收点；兼顾最终多品种共同呈现，颜色优先留给品种身份，完成/未完成、指标性质等优先用线型、形状、位置或分图区分，避免图例冲突。实际观察范围按具体问题确定。
- 展示配置先形成可修订首版，再依据工作 3、4 的真实结果调整。现有能力不足时指出缺少的具体表达及影响，分别记录专业设计与实现验证，不能让工作 3 替代重要业务画法的选择。

本项成果包括**实际展示配置文件及必要说明**，作为专业成果保存并交工作 3 消费；说明文件身份/版本与尚未验证部分，不以纯文字方案或既有三张静态图冒充通用展示设计已经完成，也不要求观察前永久定稿。

## 3. 使用 aidata 实际制图

- 先读实际采用 aidata 版本的 README，再按需查开发参考、run_brief 合同和实际示例。消费工作 2 的展示配置，将文件放到 `aidata/feature_configs` 对应位置，按真实分支、写权与调用验证；格式/接口若有较大问题，带证据提出最小修改，不自行改变配置归属。
- aidata 主要帮助多层定位值得观察的时间位置、组织图和观察范围，并向 AI 提供对应数据。已有长期概览和大—中—小窗口可以按问题采用，不能反向限定工作 2 的设计；须实际核清 uplot/CAEGraph 画法与 aidata 入口如何衔接。
- 优先核实正常 Feature 实例/已有正式结果能否直接供绘图。N 的多表 `to_dfs`/`read_session` 和 `CalType.OnlyRead` 可作为既有结果读取入口，不等于要重算整段历史。按锁定 aidata、uplot、TIS 版本实际核多表关联、时间变化及画法；不足时指出缺哪一层及最小接法，不能凭“24 表”直接断言必须改公共接口。
- `BI-01-FO-01` 首个 rb 单 As-Of 的八份 CSV 与 `fixed_input` 绘图是可复用的真实技术成果，但尚未比较原生入口，不能固化为默认路径。CSV 若只是必要缓存/导出可保留并说明理由；不为避免 CSV 重算 N、复制计算逻辑或预建平台。明确“已有正式结果”“绘图已消费”“数据已导出”“已完成专业观察”各自的实际证据。
- 尽量复用 aidata 已有机制，按需要叠加、比较或提供相应数据；必要的技术工作应放在 aidata 的有权工程修改流程内，不能在专业仓库重建一套画图工具。
- 真实图、同一观察范围的数据和读图说明尽可能对应；如果只是有链接、缺页面或数据，须如实区分。

## 4. 正确性与普通投资者正常解读的检查分析

- **真实数据优先，确有必要才视觉看图。**先用正式 N 输出、对应输入行情、必要上游及 aidata 对应数据，分析计算、时间/状态意义和正常市场解读；`plot_view_data` 只用于核图实际显示内容，不升级为正式特征结果。
- 围绕此特征在实际市场过程中产生的内容，检查其正确性以及它表达的现象是否合理、是否可能造成普通投资者的误解。
- 检查可以使用该特征本身的输出、原输入/行情、必要已有特征和相关设计背景；遇到具体疑问再追查，不能仅凭字段名或某次图形观感判定算法正确或错误。
- 允许形成支持、疑问、反例、缺乏足够信息等认识，并说明怎样影响参数、展示方案或特征本身的设计。若进一步涉及业务信息价值及与简单既有认识的对照，可随真实问题展开，不把此前完整 U2/U3 的增量门槛改成这次所有对象的统一强制目标。
- 发现前面工作有问题，可回到相应工作继续，不要求一次观察就完成全部专业结论。
- 数据足够时可直接给有边界认识，不强制每个 Case 都打开 PNG；需要辨别几何关系、图像误导或验证工作 2 的实际画法时，再定向视觉看图并记录实际所见。正确性、业务表达合理性和展示易误读分别判断，不强求每轮发现计算缺陷或新增收益结论。

## 5. 工作关系和组织方式

四项工作是研究内容而非四个派发/验收阶段。可在一次实质专业推进中反复涉及几项，也可以一次重点处理其中一项、保留下一步；管理安排以**当前具体特征的完整实际目标与已知结果**为依据，避免一项局部工作被误当作全任务永久终点。

已形成的正确图、配置和专业认识应尽量复用；发现必须回退时，说明回退的对象与原因，按需调整，不因局部变动把此前所有结果全部抹去。
