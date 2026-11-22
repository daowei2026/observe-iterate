# D002｜WALL 正式结果绑定与全量行为统计回交

整体 `GlobalProfileGate=BLOCKED`，等待 M001 的 Owner 决策。已完成新生产、独立读回和全部可支持的 **rb 2021 全年分层剖面**；m 的锁定默认实例真实失败，缺失结果没有按零计数。正式请求仍是 rb/m、2021 全年，整项 D002 尚未完成。

## 当前执行事实

| Owner要求的进度项 | 本 C 真实状态 |
|---|---|
| D001 | manager已接收最小核对；未重做完整理解 |
| X | 已开始；整体绑定PARTIAL，rb独立验证通过，m失败 |
| 复用还是生产 | 原生旧缓存版本不匹配，未采用；本Run新生产 |
| 正式Feature进程 | 两品种均真实调用默认WallAssembler().run()；当前主生产进程已退出，锁已释放 |
| 结果目录 | 本Run `.runtime/OI-WALL-STAT-20261122-01/native-cache`；精确full_dir见绑定。m路径只是失败现场 |
| G | 已对已验证rb层完成可读剖面及等价诊断载体统计；m未统计 |
| 真实阻断 | m分块覆盖缺口；正式采用空占位处理需要Owner确认M001 |

## 版本、配置与结果身份

实际wrapper/core来自TIS `6618d4d147d6ebbe634e61facddf2c9a0b996982`隔离检出，44份已加载tracked TIS源码逐字匹配。28项默认ppdict及完整配置已保存回读，receipt的18项有效业务参数和10项private参数均匹配。源指纹为：

`git:6618d4d147d6ebbe634e61facddf2c9a0b996982+source-sha256:5349ca9d2a53cd9065e29c4a1cbd1a8461b07fd708ce46a0feca0add6684d643`

范围保持 `TA_updto20240229_DBA / rb,m / 2021-01-01..2021-12-31 / night_end_at_2300`。仅用框架原生TmpStoreEnv重定向本Feature的结果存储，没有backup写面。原工作树两项修改保持原样，未采用现有输入过滤。

rb为243个交易日、9,959,400个输入观测拍；独立进程只经原生Dao读取，6张表与完整Parquet导出逐表逐行精确相等，fields/receipt和各文件SHA已记录。UTI、timestamp与物理ordinal分别保留。

## 输入资格到Wall的真实计数

原生WALL表没有下列资格列。本C用**未修改的锁定组件**取得新增诊断运行载体；其9,959,400拍trace和335,081条sparse事件的全部字段与正式结果严格相等，随后才使用诊断载体统计。载体、代码/参数/范围及SHA见 [RB_AUXILIARY_DIAGNOSTIC_RESULT.json](RB_AUXILIARY_DIAGNOSTIC_RESULT.json)。

| 业务项与单位 | bid | ask | 分母／含义 |
|---|---:|---:|---|
| 一档观测拍 | 9,959,400 | 9,959,400 | 每侧每半秒输入拍一次；不是逐笔委托事件 |
| 报价字段有限的观测拍 | 9,959,400 | 9,959,400 | 同侧观测拍 |
| QT正值观测拍 | 8,690,400 | 8,690,400 | 同侧观测拍；预热可用性单列 |
| F1大挂单资格命中拍 | 178,751 | 168,994 | 比例使用同侧QT正值拍作分母 |
| F6墙砖资格命中拍 | 178,673 | 168,560 | 转化分母为F1资格命中拍 |
| 新Wall identity | 36,197 | 34,698 | 当前每个身份一个Start；转化分母为F6资格命中拍 |
| 候选同拍未新建Wall | 142,476 | 133,862 | 候选资格不等于新对象；保留原对象的更新/恢复边界 |

全部观测wide行数为9,959,400；两侧合计19,918,800个侧别观测。F1减F6的78/434拍是本配置下大挂单且偏薄的观测。上述资格是同一观测的不同资格，不增加新的持续Wall对象类型。转化率的逐项分母及月份/钟时分层均在原生剖面中。

## 事件、状态和生命周期

| 统计项 | bid | ask | 单位／口径 |
|---|---:|---:|---|
| 唯一Wall | 36,197 | 34,698 | source namespace + symbol + wall_id去重 |
| Start | 36,197 | 34,698 | occurrence；与唯一新身份数相符 |
| BandUpdate | 96,361 | 90,101 | occurrence；同拍多条按ordinal保留 |
| StateChange | 3,611 | 3,218 | occurrence；Alive/Dormant转换 |
| End | 36,197 | 34,698 | occurrence；Ended重复trace样本不重复计End |
| 完整寿命中位数 | 11 | 11 | UTI差，分母分别为36,197/34,698个完整life |
| 薄触End | 26,946 | 26,578 | occurrence；对应侧End为分母 |

共70,895个life，均有Start/End，右截尾为0。完整状态占用、连续状态段、寿命分位、结束原因、月度与钟时密度都已形成。钟时采用原生timestamp的[06:00,18:00)与其余时刻分箱，不声称官方SessionID。UTI差、状态样本拍和自然时间差保持不同单位；跨休市/周末的自然时间差不等同连续行情时长。

同对象同UTI的多事件组有800组，其中131组为`5→5`，全部保留；不能用`wall_id+uti+event_type`盲目去重。

## 已知问题复验及新疑点

- D1：331,061条适用的同拍同身份事件几何与trace无冲突；另4,020条旧身份事件均已逐项证明为同拍新Start可追溯的relocation旧End。对象拍时间与末状态检查也未检出冲突。
- D2：70,895个End对象拍中，进入Dormant与End同拍重叠为0；恢复Alive与End不误归为该冲突。
- D4：三组固定例回归通过。新增真实诊断载体对全部10,159个far End（bid5,408/ask4,751）检查，带有效support的far End为0、计数低于hold门的far End为0。完整逐拍far历史仍未暴露；这不是m或整个请求范围已完成复验。
- D3：在rb层，薄触End后同侧相邻新Start、且已发布band/core精确相同的子模式为6,847对；对应thin End共53,524次。它不是全部D3的穷尽计数，继续保持Owner暂缓，不以此阻断后继。
- 已验证rb层没有新的高置信结构finding，诊断适配包为空；寿命问题保留在场景问题队列及候选索引中，没有据数量直接宣布合理或不合理。

## 原生交付与下一步

[FeatureRunResultBinding](FeatureRunResultBinding.json)、[StatisticsInputReadiness](StatisticsInputReadiness.json)、[GlobalBehaviorProfile](GlobalBehaviorProfile.json)、[GlobalFindingCandidates](GlobalFindingCandidates.json)、[ScenarioQuestionQueue](ScenarioQuestionQueue.json)、[CandidateCaseIndex](CandidateCaseIndex.json)、[DiagnosisInputAdapters](DiagnosisInputAdapters.json)、[GlobalProfileGate](GlobalProfileGate.json)，以及组合原生 [FeatureGlobalBehaviorProfilingResult](FeatureGlobalBehaviorProfilingResult.json)。数据位置/SHA见[LOCAL_DATA_MANIFEST](LOCAL_DATA_MANIFEST.json)，统计自检见[STATISTICS_SELF_CHECK](STATISTICS_SELF_CHECK.json)。

m的真实失败及三天输入证据已经形成可审阅的[M001](MODIFICATION_PROPOSAL_M001.md)。原D明确未授权采用已有wrapper输入处理差异，因此本C不实施、提交或采用候选Feature改变。Owner确认后应更新正式锁并完成原范围X/G回环；当前rb结果和剖面完整保留。整体Gate为BLOCKED，专业回交为WAITING_OWNER，不是Feature释放。
