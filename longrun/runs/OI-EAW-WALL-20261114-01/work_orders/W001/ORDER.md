# W001｜EawP1WallLifecycleFrp 真实工作区、物化资产与读取入口只读核验

## 0. 运输身份

- `run_id`：`OI-EAW-WALL-20261114-01`
- `work_order_id`：`W001`
- `issuer_call_id`：`C0003`
- `issuer`：`chatgpt:OI-EAW-WALL-20261114-01:executor:E1`
- `worker`：`codex:OI-EAW-WALL-20261114-01:worker:W1`
- `return_to`：`chatgpt:OI-EAW-WALL-20261114-01:executor:E1`
- `delegation_ref`：`daowei2026/observe-iterate@944f2c57e44ee9d89b69b6b24a03a3a32fdff11e:longrun/runs/OI-EAW-WALL-20261114-01/delegations/D001/DELEGATION.json`
- 专业问题：为 D001 的 `Q-WALL-IDENTITY-LIFECYCLE`、`Q-WALL-PUBLICATION-STATE`、`Q-WALL-BUSINESS-SUITABILITY` 取得不可由旧 GitHub 源码替代的 Linux 现场事实。

本 W 只执行工具与现场核验，不决定业务预期、材料必要性、合理性结论、冻结资格或父任务完成。所有结果先原封回交 E1，由 E1 专业消费。

## 1. 派发前必须由主控核真的物理绑定

- 请求模型：`GPT-6.1 Sol Max`；主控须记录实际模型与 effort，不得用逻辑名替代真实配置。
- 请求工作目录：`/dwdhome/fy/BASE_E6_2`；主控须核实实际 cwd、物理 thread 和该目录真实存在。
- Worker 逻辑身份：`codex:OI-EAW-WALL-20261114-01:worker:W1`。
- 主控须核实共享工作区单写者；本 W 只允许写入下述 Run 目录。
- 若任一物理绑定、权限或单写者状态无法核真，返回 `STOP`，不得猜测执行。

## 2. Owner grant 与写面

逐字授权：

```text
operation=wall-observation-work execution_context=linux:/dwdhome/fy/BASE_E6_2 allowed_writes=/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01
```

本 W 进一步收窄写面为：

```text
/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D001/W001/
```

允许：只读源码/配置/元数据调查、低成本文件清单、已有物化数据的有界 schema/数量/时间范围核验、已有日志/receipt/manifest 对账、把报告与清单写入上述目录。

禁止：

- 修改任何现役仓库、配置、数据库、物化产品、缓存、Notebook、生产目录或正式分支；
- `git checkout/reset/clean/pull/fetch/rebase/merge`、安装依赖、清缓存、覆盖文件；
- 启动全年、全品种或其他大范围重算；
- 在没有成本预检时加载整份大型数据；
- 把下游 EawBattleP 旧图冒充 Wall Lifecycle 材料；
- 根据代码或空 diagnostics 自行作业务合理性判断；
- 在授权目录外写临时文件、`__pycache__`、日志或导出。

如确需 Python 只读探测，设置 `PYTHONDONTWRITEBYTECODE=1`，并把 `TMPDIR`、缓存与输出显式指向本 W 写面；无法保证时不执行导入，只做静态核验。

## 3. 精确输入与旧阅读基线

### 3.1 当前 D 与专业边界

- `daowei2026/observe-iterate@cdec293a4bfdac85ca4ab3171f9eeb083a338493:longrun/runs/OI-EAW-WALL-20261114-01/delegations/D001/DELEGATION.md`
- `daowei2026/observe-iterate@ca7fdae84f65265332e3a53865724a2615508766:task-inputs/eaw-p1-wall-lifecycle/FEATURE_CONTEXT.md`

### 3.2 旧源码/需求基线——仅用于对照，不得拼成现役 tuple

- `daowei2026/feature-refinement-implementation-agent-evolution@8d58ddd3392a3e67ef5ba44adf2c4cd0c9077f9f:candidate_gold_cases/eaw/taskpacks_and_checkpoints/p1/EAW_P1_PREL0_BASE_PRODUCTS_ENGINEERING_DESIGN_AND_VCC_V1_6_1_20260818/01_EFFECTIVE_SCOPE_AND_REQUIREMENT_CORRECTIONS.md`
- `daowei2026/feature-refinement-implementation-agent-evolution@8d58ddd3392a3e67ef5ba44adf2c4cd0c9077f9f:candidate_gold_cases/eaw/taskpacks_and_checkpoints/p1/EAW_P1_PREL0_BASE_PRODUCTS_ENGINEERING_DESIGN_AND_VCC_V1_6_1_20260818/02_FINAL_P1_ARCHITECTURE.md`
- `daowei2026/feature-refinement-implementation-agent-evolution@8d58ddd3392a3e67ef5ba44adf2c4cd0c9077f9f:candidate_gold_cases/eaw/taskpacks_and_checkpoints/p1/EAW_P1_PREL0_BASE_PRODUCTS_ENGINEERING_DESIGN_AND_VCC_V1_6_1_20260818/dsu/P1-DSU-01_Wall_生命周期_DSU.md`
- `daowei2026/tis@ef887396e0a06d6e75be47efee0f1985ad7988a3:frp/EawBattleP.py`
- `daowei2026/tis@ef887396e0a06d6e75be47efee0f1985ad7988a3:hf/prel0/wall_assembler.py`
- `daowei2026/frp@cac6c912dd65a14acbd591ca57e0afd8ddb4ef13:src/Frp/Instance/ISL/Eaw/P1.hs`
- `daowei2026/frp@cac6c912dd65a14acbd591ca57e0afd8ddb4ef13:src/Frp/Instance/ISL/Eaw/P1/WallLifecycle.hs`
- `daowei2026/frp@cac6c912dd65a14acbd591ca57e0afd8ddb4ef13:src/Frp/Instance/ISL/Eaw/P1/Products.hs`
- `daowei2026/frp@cac6c912dd65a14acbd591ca57e0afd8ddb4ef13:src/Frp/Instance/ISL/Eaw/P1/Publication.hs`
- `daowei2026/frp@cac6c912dd65a14acbd591ca57e0afd8ddb4ef13:src/Frp/Instance/ISL/Eaw/P1/FaoIngress.hs`

## 4. 必须执行的只读核验

### A. 真实工作区与仓库绑定

1. 记录实际 `pwd`、主机/用户的非敏感标识、UTC 时间、磁盘可用量；不得记录凭据。
2. 找出 BASE 下与本任务有关的真实 Git repo/worktree，而不是假设目录名。对每个相关 repo 记录：
   - 绝对路径与 `git rev-parse --show-toplevel`；
   - 当前 branch/detached 状态、HEAD 40 位 SHA、`git status --short --branch`、`git worktree list --porcelain`；
   - remote 名称和仓库标识；敏感 URL/token 必须脱敏；
   - 本任务相关文件是否存在、其 blob/hash；
   - 与旧阅读基线在本地可比较时给出限定到相关路径的差异摘要；旧 commit 不在本地时明确写 `UNAVAILABLE_LOCALLY`，不得联网 fetch。
3. 明确共享工作区是否已有未提交改动；只记录，不修改。

### B. 现役代码、配置、包装和读取入口

围绕 `EawP1WallLifecycleFrp`、`WallOccurrenceFao`、`WallAssembler`，用静态搜索和有界只读检查定位：

1. 实际类/注册/配置定义、FaoMeta、`Cal`/`Cache`、OnlyRead、目标对象、日历、参数、source scope、time range 的来源；
2. generated wrapper、FrpDbaDao/DBA、公开物化产品读取入口及 `to_df` 限制的真实组合；
3. `wall_occurrences`、`wall_current_view`、`wall_diagnostics` 三路 writer 的实际名称、schema/字段、输出路径构造规则；
4. WallAssembler 的 receipt、sparse event/state trace 生成与保存入口；
5. 每项均给精确路径、行号/符号、当前 repo HEAD；无法判定时列出竞争解释与最小查证，不做推断补齐。

### C. 已有资产与物化数据清点

1. 只在由代码/配置/receipt 指向的候选目录内有界查找，不对整个磁盘无界递归。
2. 分开登记：
   - 源码可读；
   - generated wrapper 存在；
   - receipt/fields/manifest 存在；
   - WallAssembler sparse events/state trace 存在；
   - 三路 writer 的数据物化存在；
   - 数据可解码；
   - 数据是否具备本问题所需身份、时间、版本与对账字段。
3. 对每个候选资产记录绝对路径、文件类型、文件/分区数量、总大小、mtime、可得 hash（小文件全量，大文件可记录 manifest/hash 现状，不为求 hash 强读大文件）、对象/日历/时间范围/代码参数版本、读取方式和敏感性。
4. 对历史报告、旧目录、CAEGraph/Notebook 只判“候选复用资格”；必须说明它是否真是 Wall Lifecycle 材料、是否与当前 tuple 同版、是否当前可读。

### D. 有界解码与三路对账（仅资产存在且低成本时）

在不触发上游重算、不全量载入大型数据的前提下：

1. 核 schema、row/occurrence 数量、最早/最晚 actual/confirm/known 时间（字段存在时）、对象/`wall_local_no` 范围、分区范围和空值；优先 metadata/分区统计，必要时只读少量明确分区。
2. 找一条包含 Start 且尽可能包含非平凡 update、Dormant/Present 或 End 的真实 Wall 局部链；若自然样本没有这些状态，准确报告，不合成伪样本。
3. 保留同一身份的上游 sparse event/ref/payload、`wall_occurrences`、`wall_current_view` update、`wall_diagnostics` 和可得 active-map/state trace 的对应键与时间；不得把 current update 缺行解释为完整状态不变。
4. diagnostics 为空时只报告“在已核范围内未观察到诊断”；不得证明异常路径正确。
5. 若解码会触发大加载、隐式计算、未知写入或内存风险，立即停止在 metadata 层并记录原因。

### E. 无可用材料时的运行预检——禁止实际运行

若 C/D 不能取得可用材料，只调查并报告：

- 可执行入口和精确命令模板；
- 最小可区分窗口/对象的候选来源（历史 fixture、已知短窗或现有 receipt），以及是否必然重算 WallAssembler/上游；
- 预计文件/行数、内存/耗时的证据来源与不确定性；
- 需要的环境、日历、参数、数据权限；
- 安全停止点和可观察回执；
- 为什么该最小动作足以区分当前问题。

不得实际启动该运行。是否采用窗口及是否通过 G-RUN 由 E1/manager 后继决定。

## 5. 输出与文件合同

在唯一写面中生成：

```text
/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D001/W001/
├── WORKER_EXECUTION_REPORT.md
├── WORKSPACE_BINDING.json
├── CODE_AND_READER_ENTRYPOINTS.md
├── ASSET_INVENTORY.json
├── COMMAND_LOG.txt
├── HASHES.sha256
├── SAMPLE_CHAIN.jsonl                 # 仅真实低成本样本取得时
├── SAMPLE_CHAIN_README.md             # 同上
└── ACTION_PREFLIGHT_FACTS.md           # 无可用材料或需运行时
```

要求：

- `WORKER_EXECUTION_REPORT.md` 逐项列 `EXECUTED / PARTIAL / NOT_FOUND / NOT_APPLICABLE / STOPPED_FOR_COST / UNKNOWN`，并给证据；
- JSON 必须有效，未知项显式为 `null` 加 `reason`，不得猜值；
- `COMMAND_LOG.txt` 记录实际命令、exit code、开始/结束时间和输出摘要；敏感值脱敏；
- `HASHES.sha256` 覆盖本 W 自产文件；原始大数据只引用，不复制到 Run 目录；
- 样本只允许真实数据，包含 source path/partition、identity/time/version 和抽取方法；不得含凭据或不允许公开的原始敏感信息；
- 报告明确区分静态源码事实、现场绑定事实、物化数据事实、可解码事实和用途适合性所需但尚未由 Worker判断的专业问题。

Worker 正式回交还须按 V2 产生 `WORKER_RETURN.json`，`outcome` 如实为 `EXECUTED / PARTIAL / STOP / FAILED`，`return_to` 必须是 E1；`result_ref` 引用允许发布的 Worker 报告，manifest 引用真实产物及 sha256。若 Worker 无 GitHub 写工具，提供精确目标路径与完整正文给主控逐字发布，不捏造 commit。

## 6. 接收标准

E1 能据回交回答：

1. 当前真实 checkout/HEAD/dirty 状态是什么，旧 SHA 与现役 tuple 能否对应；
2. 真实配置、参数、对象、日历、范围和 source scope 在哪里、是否可核；
3. generated wrapper/DBA/读取入口与 `Cal`/`Cache` 的实际组合是什么；
4. receipt、sparse events/state trace、三路 writer 和必要 active-map 证据分别存在/缺失到什么程度；
5. 数据是否仅“存在”，还是已经“可解码且具备本问题所需身份/时间/版本”；
6. 若无材料，最小动作的入口、成本、停止点和前置条件是什么。

任一项失败不得抹掉其他已核事实；禁止只回“没找到”或五行预览。发现越权、共享写冲突、未知副作用或即将触发大计算时立即停止并回报。
