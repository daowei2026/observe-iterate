# D007｜已批准MP002的FI实施回交

已按批准的F800-MP-002具体diff完成正常KLine缺价覆盖修复，并提交、推送和采用FRP `39f02ec4548e68ba8dbd30061afc870546000994`。真实正常适配回归13项、既有窗口/数值/生命周期回归64项、Material覆盖控制8项及四个隔离构建目标均通过；旧be57在同一真实适配测试上产生预期失败。ImplementationFixReturn.ready_for_feature_rerun=true。

本D仅FI完成，GF002为FIXED_PENDING_RERUN，尚未关闭。新代码完整三年X/31表独立读回/G和释放由原manager消费后按原Workflow接续；批准已覆盖该后继，无需再次确认。原D005及GF001闭环原件保留；不把旧X/G当新版本证据。

## 准确委派与批准

C0017/D007，原E1，workers=[]。已亲自读取准确packet、D007全文、同版control-v0.3 L2的FI工程行、L0 §7/9以及control/03 §8.1、control/04 XI、control/05返回合同。FI不是新增Skill。47项exact输入、最新Owner原文及当前Binding核同；远端D/I/批准三份blob核同。

Owner批准：`daowei2026/observe-iterate@2fa5c26a739d8d97a733f6a7581092a271724e6e:longrun/runs/OI-F800-STAT-20261122-01/owner-decisions/F800-MP-002/OWNER_APPROVAL.original.txt`，原文923字节、SHA-256 `a9c626ec667171e7f4605b853d360597a471d6bc82002574f938ab4d269058eb`。最新Binding@3dc11a9dbf39e181b3c6a3051419a90e46b92aac。原提案diff为1630字节，SHA-256 `95d05a657e16537da28aaeea89d5d00c1302fc6c6427e801388c4985ac314d9e`；实际生产文件的变更及上下文与批准diff一致，另增必要回归源码和cabal目标。

## 修复与真实回归

生产改动仅`GroupCandidateKLineInput.hs:advance`：保留同拍close；非有限close（NaN/±Infinity）发InputMissing、清previous；有效UTI/Clock继续推进。恢复有限价先发行当前点，随后真实相邻边累计。有限价零量/无Turn仍可完整观察。源UTI准确相邻、800/600/实际2Delta=1200及既有材料/确认/保存合同不变。

新增回归以合成原始KLine Bar及无ScaleTurn/Zig事件注入既有Fao缓存，实际调用Generic KLine、close/UTI同拍join、buildKLineGroupSource及其局部advance和previous状态，再交真实Material。没有手造失败覆盖来替代分类位置。2492个Calendar时刻/7475个对象帧；旧be57的207个NaN帧全部为错误Observed，测试到缺价断言后真实退出1。修后同轴同输入全部209个非有限价帧（207 NaN、正负Infinity各1）为InputMissing，13项真实适配检查通过，包括单对象失败、Clock推进、恢复首点、满800Delta前/等号、真实1200UTI缺口、有限零量/无Turn。旧窗口64项及同新库Material覆盖控制8项也通过，分别保护GF001/生命周期边界与失败、失知、明确不适用等既有覆盖语义。

这是实际生产适配图的回归，使用明确合成上游，不是正式市场F实例。测试配置将PNV指向不存在的隔离路径、store指向本D fixture目录；成功只依赖注入Bar/空上游事件，不采用或修改真实PNV。首次测试编译遇到同名price字段歧义，改回归函数名后执行了有效旧版反例；原失败日志保留，不把编译失败当反例。只读加载预检首次误用目录包含关系判断逐文件软链接；核实际软链接后改为准确目标文件身份比较，最终预检须通过才采用，原失败日志保留。

## 新版本与隔离运行时

FRP分支 `codex/f-observation-multiple-20261122` 的真实新提交为 `39f02ec4548e68ba8dbd30061afc870546000994`，已推送至daowei2026/frp并远端blob回读。三个改动文件是生产适配文件、`test/U2KLineCoverageAdapterSpecMain.hs`及`frp.cabal`；其余source/test及完整配置经827文件manifest核同构建输入。

当前运行时：`/dwdhome/fy/BASE_E6_2_copy/.runtime/f800-input-missing-20261123/runtime`；新ts/dbaw/窗口检查/适配检查的实际二进制指纹见CodeVersionAdoption/BUILD_STATUS。重型复制与构建均持真实flock并记录PID、子进程和开始/释放；本C未启动正式F。旧be57源码归档后让旧runtime指向该相同内容快照，旧三份二进制指纹不变；D005结果目录及原件未动。

TIS仍为2f460d663d821cf2ba25555eda13e78b697d0767，同冻结mquant/tis实路径；配置SHA-256仍`b72095ff100da926474701b74bff7586a74b9770bc81cadc34c23cfe223e5cb3`。PNV、SOF/Calendar、steel、rb/hc/i、5m、2021—2023和全部正式配置保持。只补CurrentFeatureUnderstandingDelta的代码绑定/J4语义；保存结构/对象/事件/字段合同未变，不重做完整U。

## 后继与未完成边界

原manager应沿原FI返回Gate核受影响绑定后直接签新X，再31表独立OnlyRead和原Skill完整G。必须新attempt/store，运行前重核实际加载/配置/完整范围/Calendar/resultidentity/单写者并持实际flock。新生产需实测GF002原8观点自然对象对应、GF001原22+8控制、全量缺价窗冲突及Life/Revision/发行/UUID/exact链变化。13+64+8局部通过不预设新产量或修后完整结果。

共享适配的Q影响与Q另一路数值边界限制继续传递；本Run不运行/释放Q/V或修改WALL。当前无新FeatureReleaseGate/ReleasePackage，四项场景问题保留。旧G及Gate原件作为历史保留，当前合法路由为RERUN_REQUIRED；本D不伪造新G或替manager完成释放。

专业原件：ImplementationFixReturn、CodeVersionAdoption、REGRESSION_COMPARISON、ContractAndDependencyImpact、CurrentFeatureUnderstandingDelta、FindingDisposition及RERUN_HANDOFF。先发布这些结果并远端核同，再单独发布引用已有exact专业提交的C0017原V2 Return；executor完成不代表manager已消费。
