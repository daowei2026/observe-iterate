# W001｜BASE 现役绑定、三路输出形态与既有真实记录定向核查

## 1. 正式身份和原消费者

- run_id：OI-EAW-WALL-20261116-01；work_order_id：W001；issuer_call_id：C0003。
- issuer：chatgpt:OI-EAW-WALL-20261116-01:executor:E1。
- worker：codex:OI-EAW-WALL-20261116-01:worker:W1。
- return_to：chatgpt:OI-EAW-WALL-20261116-01:executor:E1。**先回 E1 专业消费，不直接回 manager 代替 E1。**
- 签发调用 token：f30dbae896605726339bf8c9c393a6e6；后续 Worker 通道身份仍由主控真实绑定，本 token 不替代发送回执。
- 唯一业务对象：EawP1WallLifecycleFrp。
- 工作身份：D001 / WI-WALL-SKELETON-001 / M-step-1-WALL-B001 / Q-WALL-01。
- analysis_round 尚未建立；expectation_version=not_frozen。

正式 D：
`daowei2026/observe-iterate@40310127d8b700141f2ab1a17a1b114cbd1ff95b:longrun/runs/OI-EAW-WALL-20261116-01/delegations/D001/DELEGATION.json`

D 完整正文：
`daowei2026/observe-iterate@4b918010f9ec48c48482acca066cea8e97fb5183:longrun/runs/OI-EAW-WALL-20261116-01/delegations/D001/DELEGATION.md`

E1 已实际完成的专业分析是本 W 的依据，不要求 Worker 重做业务分析：
`daowei2026/observe-iterate@54754891345bcb4f66b298cfbe2145c317e80b94:longrun/runs/OI-EAW-WALL-20261116-01/calls/C0003/PRO_REPORT.md`

准确历史源码和阅读范围：
`daowei2026/observe-iterate@298b35a68b32db01c136820bee63d82d0e630d99:longrun/runs/OI-EAW-WALL-20261116-01/calls/C0003/SOURCE_REGISTER.md`

## 2. 为什么签本 W；只需回答哪些事实

E1 已核对指定历史 FRP/TIS 源码：上游认墙、packed ingress、批事务、active map、current 更新表、三路 writer 和脚本能力。但这些不能证明 BASE 当前加载组合及既有产物相同。

本 W 只关闭报告 G01–G03，并尽量取得 G04 的现成时基元数据：

1. 实际使用的相关源码、Python 加载位置、generated ADT schema 和 FRP binary 是什么？与 E1 已核历史事实是否有直接可见差异？
2. 默认实例和实际 Wall source 绑定哪个 ppid、参数、full_dir、receipt、fields 和已有数据范围？哪些生成版本信息确实存在，哪些没有？
3. 现有只读路径能否读取三路真实输出，其 schema、批次/记录形态和必要对应关系是什么？不能读取时，确切失败在哪一层？

不让 Worker 判定业务合理性、材料充分性或步骤通过；不让 Worker 把所有历史源码重新完整分析一轮。没有证据的项写 unknown/not_checked，而不是补猜。

## 3. 首次派发前置由主控负责

主控在首次派本 W 前，独立核实物理线程与上述 Worker 逻辑身份映射、目标 Linux `/dwdhome/fy/BASE_E6_2`、单写者/占用情况及目标配置 `GPT-6.1 Sol Max`。现有逻辑 Binding 不是这些事实的证明。本席未宣称已核实。

若实际设施或占用冲突阻止操作，主控记录准确事实并回 E1；不启动另一个未授权工作区、不清除别人的锁、不伪造启动记录。普通事实读取不逐项转 Owner 审批。

## 4. 授权、写面和硬停止边界

采用 Owner 原文及 Binding：

`daowei2026/observe-iterate@55303ab99aeb349ddf9ffde7a375ca241b29d0f6:longrun/runs/OI-EAW-WALL-20261116-01/OWNER_START.md`

`daowei2026/observe-iterate@675c66a14a123f60409403030ef1a19540813430:longrun/runs/OI-EAW-WALL-20261116-01/RUN_BINDING.json`

Linux grant 原文：
```text
operation=wall-observation-work execution_context=linux:/dwdhome/fy/BASE_E6_2 allowed_writes=/dwdhome/fy/BASE_E6_2
```

本 W 再收窄：只读相关源码/已存产物，调查脚本、日志及少量样例写在：
```text
/dwdhome/fy/BASE_E6_2/.runtime/observe-iterate/OI-EAW-WALL-20261116-01/D001/W001/
```

不得修改业务源码、需求、参数实例、生成 schema、运行环境配置、正式 fields/receipt/DBA、现役产物或无关文件；不得 git reset/clean/checkout 覆盖现场，不安装依赖、不重建二进制、不另外造隔离工程。使用已有环境与启动器；避免无必要的 bytecode/缓存写入，发现会改动正式或未授权共享路径时停止该动作。

不执行 producer 新计算、参数搜索、完整链新跑或长窗口补算。不使用人工构造输入，包括用合成 occurrence 调 applyWallOccurrenceBatch 代替现役材料。不运行旧 Run 的测试/脚本来继承其完成状态。步骤 0 仍是 Owner 跳过，不做全资产、全仓库或全磁盘清点。

如果源码/缓存规则无法证明某入口只会读取已有数据，不以“先试一次”探测是否补算；停止该读取，返回准确缺口。缺 schema 或环境错误不是自动修复授权。所需新动作、风险和必要性回 E1，后续由 manager 在原边界内决定。

## 5. 操作顺序与具体交付事实

### 5.1 相关运行链定位：只查本对象

在已有 BASE 环境中确认 cwd、实际启动器及相关模块路径。不要假定所有仓库都直接位于 BASE/frp 或 BASE/tis；沿现有 launcher、import 文件位置与实际 repository root 定向查明。

记录相关 FRP、TIS 及确实影响本次回读的框架仓 HEAD、相关文件是否 dirty、实际文件 SHA-256；只保存相关文件的必要 diff/片段。若模块来自共享目录，记录真实位置，不把发现路径当作新增写权限。不要公开完整环境变量、凭据或包含秘密的配置全文。

重点对应报告来源登记中的：
- TIS frp/EawBattleP.py；WallAssembler 及其 core、tick_quote_context、p1_dba_export 的本对象相关段。
- FRP P1.hs、FaoIngress.hs、WallLifecycle.hs、Products.hs、Publication.hs、OccurrenceLedger.hs 的 Wall 段。
- 实际三路 ADT schema 的定义/导出入口；当前调用会使用的 FRP 可执行文件路径、可得 hash/构建记录。

可以用已读历史 SHA/blob 与实际相关文件比较，或记录 actual file hash 和必要片段给 E1。不要为“查版本”拉全仓历史或构建。HEAD、mtime、binary hash 分开记录：没有构建 provenance 时，不能把当前 HEAD 当成 binary/旧产物生成提交。此类 unknown 本身是合法事实交付，不要求先把一切版本补齐才做其他低风险读取。

### 5.2 默认实例绑定：实例化不等于运行

调查上下文沿用已提供入口：
```text
sof_name = TA_updto20240229_DBA
startDay = 2020-12-01
endDay = 2021-02-22
symbol = rb
calendar = night_end_at_2300
expression = EawP1WallLifecycleFrp()，默认参数
```

该上下文只是已知候选，**不是本 W 授权整段重算，也不是正式观察范围已选定**。

优先复用 `/dwdhome/fy/BASE_E6_2/run-python.sh` 和现有环境。按实际 API 安全实例化并记录：顶层 class_file、ppdict、ppid、full_dir、gfull_dir、cal type；经 wallLifecycleInput 到 wallOccurrenceSource 的实际类/参数/ppid/full_dir；不要把手写默认参数表替代实际值。

不得调用上游 `.rerun()`。检查 constructor/属性读取存在副作用时先保留源码事实，不以执行强行补全。未成功实例化也应交付前一步已经取得的路径、代码和准确异常。

### 5.3 已存 artifact 与 schema：先查资格再读 payload

针对实际 full_dir，定向读取现有 fields.json、必要文件列表/尺寸及现成 provenance/receipt。source 的 `p1_receipts/wall_lifecycle.json` 是明确检查项；顶层有没有独立 receipt 据实际记录，不能因为源码中 source 需要 receipt 就发明顶层同名要求。

分开记录：
- 顶层三路 `wall_occurrences`、`wall_current_view`、`wall_diagnostics` 的 key/字段/schema 是否存在，存在但为空与缺 key 分开。
- source 的 `wall__...` 物理流、稀疏 events 和 state_trace 哪些实际存在，勿把 docstring/runner 临时字典当正式物化结果。
- receipt product kind、artifact_location、parameter/effective-parameter 信息、source input scope、可得 code fingerprint/生成记录；与当前实例是否一致的客观比较。
- 业务 source namespace/local no 所依附的真实 artifact；已知时间范围是配置范围、metadata 范围还是实际已读记录范围。
- schema 的实际 Python 类型及字段；外层时间轴、root_seq、批次容器和业务对象的层数。诊断 envelope 与内部 errors 分开。

只做必要文件元信息及小型 receipt/schema 内容的读取，不为求完整 hash 扫完全部长窗口 DBA，不遍历全部行情库。已有材料的生成时间或文件名不是来源正确性的证明。

### 5.4 有条件读取少量已有真实记录

首先通过现役框架源码/已有明确只读 DAO 核实读取路径：必须不调用 producer/FRP 新计算、不回写正式产物、不因缺文件触发回补。优先既有 FrpDbaDao/ADT 的只读入口；允许在已证只读缓存分支下复用 `.run()/.F` 的读取方式，但不能只凭 fields.json 存在就调用。事前记下选择的路径和判断依据。

可参考而非无条件执行的原脚本：
`daowei2026/observe-iterate@56008df45473231c25d4ccae7f0a8c7ec599a18c:task-inputs/eaw-p1-wall-lifecycle/实例运行脚本.py`

若复用其代码，放在本 W 输出目录，保留原文引用和实际修改 diff；只允许路径/调查记录/读取层适配，不能修改业务算法、参数、fields-miss 停止条件。不要覆盖 `.runtime/parameter-inspection` 中旧报告。读取尝试可沿用 180 秒上限；超时或未知效果先记录，不原样反复重试。

读取内容仅用于验证实际接口与来源：
- 每路最多三处可直接定位的非空外层批次，并保存所选批次的原始 index、外层时间、完整 decoded 内容及来源；大批次不全展开时明确未展开，不能把截断内容标成完整批次。
- 如 cheaply available，可给外层 event 数与内部业务行数，但要标明计算依据和范围。不能为了几条样例把整段 payload 全部物化。
- diagnostics 按真实 schema 记录 envelope 数、ingress/state error 内容与相应范围；不能机械套用 occurrence 的 count 逻辑。
- 如容易通过已存 source 相同 UTI/local no 定位，附对应少量原始 wall 行与物理 key/ordinal；不得构造匹配行，不强行做整窗 join。
- 保留实际观察到的零/缺失/异常；没有检索到某种事件不等于整个窗口不存在该场景。

若三路中任一路不能读取，记录路径/API/异常及已查事实，保留其他合法读取结果；不自动改用 EawBattleP，也不把本 W 扩成全范围正式材料导出。没有现成安全路径时可以只交 metadata-only 结果和明确缺项。

### 5.5 完成前只做操作对账

记录本次实际执行的命令/脚本、运行成功与回读成功分别是什么、涉及哪些读取范围、创建哪些调查文件；核对相关源码和正式文件未被本动作修改。不得凭退出码或脚本自己的 success flag 宣称三路齐全。

本 W 不进行合理性判定、不画正式观察图、不形成市场结论、不把多批抽样称为完整生命周期覆盖。E1 将消费结果并决定是否需要进一步有界查证。

## 6. 最小交付与事实格式

在本 W 输出目录形成：

1. `FACT_REPORT.md`：按 G01/G02/G03/G04 分别列“实际操作、事实、证据位置、未核项、失败/限制”；区分历史基线与现役，列是否执行过特征计算（本 W 不授权）、读取模式及实际副作用检查。
2. `FACTS.json`：至少含 run_id、work_order_id、对象、真实 workspace、实际 context、related_sources、loaded_modules、binary/schema facts、feature/source binding、artifact_checks、read_mode、read_attempts、stream_checks、sample_locations、unknowns、created_files。缺失可用 null 加 reason，不伪造 hash/commit/行数。
3. 实际调查脚本及必要命令/异常日志；有样例才产生样例文件；有本地相关 dirty diff 才保存必要片段。无样例时不要制造空文件冒充读到空数据。
4. 交付文件 SHA-256 清单，排除清单自身和未来 Return，避免自哈希循环。

原始全量行情、凭据、环境秘密不上传。上述本 Run 允许公开/可交接的必要文本证据由具有真实 GitHub 发布权限的一方按原样发布到：
```text
longrun/runs/OI-EAW-WALL-20261116-01/worker_results/W001/
```

仓库和分支仍是 `daowei2026/observe-iterate` / `runs/OI-EAW-WALL-20261116-01`。Linux grant 不自动代表 Worker 具有 GitHub 工具；若没有，由主控依 Owner 的 run-record-publish grant 原样发布并回读。不得伪造远端 commit，不改业务管理文件，不复制旧 Run 结果顶替现场证据。

先发布报告/必要证据，再发布符合 `longrun-worker-return/v2` 的 `worker_results/W001/WORKER_RETURN.json`：order_ref 必须是已存在的本 W ORDER.json 精确引用，worker/return_to 如 §1，result_ref 指实际报告，missing 列未交付项，manifest 引用已发布文件和真实 SHA-256。不引用未来文件/自身 commit，不把 outcome=EXECUTED 解释为专业接受。

## 7. 停止、部分结果与后继

- 权限、物理映射或单写者未满足：停止对应现场动作，保留主控准确失败，不另开环境。
- 没有既有产物/receipt/schema/安全只读路径：保留已取得事实，列缺项，不计算补齐。
- 当前版本不同：给准确差异，继续不依赖该不确定性的低风险元信息读取，不强制切回历史 SHA。
- 需要源码、schema、binary、参数或正式产物改动：不执行，给具体必要性和影响范围。
- 未知效果：先查原运行/输出事实，不机械重复。

真实 Worker Return 触发 E1 新调用；E1 先将报告中的每项历史结论标为现役证实/现役不同/仍未核，核对三路实际形态及缺失，消费后再向 manager 回交 D001。W 完成不等于 D001 完成，更不等于步骤 1 被接受或父任务完成。本 W 不要求 Owner 另批普通节点。

本 ORDER.md 只记录 issuer_call_id，不反向引用尚未发布的 ORDER.json 或 C0003 PRO_RETURN。
