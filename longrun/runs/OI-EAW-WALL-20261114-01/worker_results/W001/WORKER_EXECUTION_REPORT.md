# W001 本地执行报告

本地 outcome：**PARTIAL**。已实际完成有界现场核验并交付原件；当前同版运行 tuple 与正式出版/Return 仍有缺口。没有启动计算或新测试 Run，没有 GitHub 写入，没有作业务接受/完成决定。本地 Goal 完成只表示本地交付，不表示 W001、D001 或父任务完成。

## 身份、授权与交付

- Run：OI-EAW-WALL-20261114-01；D001/W001；Worker：codex:OI-EAW-WALL-20261114-01:worker:W1。
- 原 ORDER：`daowei2026/observe-iterate@ad20770c69bc431d2e9188dcecd89883bce20cfa:longrun/runs/OI-EAW-WALL-20261114-01/work_orders/W001/ORDER.json`；签单 Return：`daowei2026/observe-iterate@b94b367692c252ed2ef41441ff6244d6d71e4b0c:longrun/runs/OI-EAW-WALL-20261114-01/calls/C0003/PRO_RETURN.json`。
- return_to 只能是 **chatgpt:OI-EAW-WALL-20261114-01:executor:E1**。
- 唯一业务写面：`/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D001/W001/`；实际 cwd：`/dwdhome/fy/BASE_E6_2`；实际 thread：01a1da55-5881-7590-94a1-0661f0236977；session metadata 核实 gpt-6.1-sol / max，非逻辑名替代。
- 首次绑定可用磁盘 442721370112 bytes；UTC/主机/非敏感用户标识在绑定 JSON。
- 主控持有锁：PID227535 / startticks44274656 / inode14781898。开原 inode 的竞争 `LOCK_EX|LOCK_NB` 返回 EAGAIN；没有创建、截断、写锁文件，没有替换/释放/重取主控锁。只读描述符最初返回 EBADF，改为无写入的 O_RDWR 描述符完成竞争核验。每次 runner 前再次核验 holder 与保护。
- 本地输入原件在 `inputs/`；命令、stdout/stderr、每次 source 和失败记录在 `commands/`、`evidence/`、`COMMAND_LOG.txt`。执行器预览没有代替原件。

## 最重要的现场事实

真实 TIS 是 `/dwdhome/fy/BASE_E6_2/mquant/tis`，HEAD `ef887396e0a06d6e75be47efee0f1985ad7988a3`；真实 FRP 是 `/dwdhome/fy/BASE_E6_2/edh-universe/frp/frp`，HEAD `cac6c912dd65a14acbd591ca57e0afd8ddb4ef13`。两者与 ORDER 的旧源码阅读 SHA 相同，但分别有 STCalendar.py、BussinessUtils.hs 的既有 dirty 修改；m3sof、worker 等也有既有修改，未处理它们。完整路径/branch/worktree/remote/status/相关文件 sha256 和 blob 在绑定 JSON。D001 与 FEATURE_CONTEXT 本地镜像均已与其准确 Git object 核字节一致，无 fetch。

已找到真实 WallAssembler receipt、fields、sparse、state trace 和两个三路产品 leaf。三个候选 prod 根只做一层低成本清单，再对588个明确类路径作存在性检查；只进入已存在的 Wall/Wall产品，155目录、796文件的 metadata 清点共 41550396966 bytes，未载入这些数据。没有把目录名、mtime 或 success receipt 当本次运行证明。

旧产品与当前代码的关键差异：物化 fields 用 P1Wall*Storage；当前 writer 用 WallOccurrenceBatch/WallCurrentBatch/WallDiagnostic。产品生成版本回执缺失。现存 generated wrapper 有118类但没有 Wall/P1 类。因此“源码可读”“包装存在”“物化存在”“有界可解码”“当前同版”“用途适合”分别报告，不能逐级自动推导。

| 物化范围 | occurrence firing / records | current firing / records | diagnostic firing / records | 本W读取范围 |
|---|---:|---:|---:|---|
| 目录2020-12-01–2021-02-22 | 14,858 / 15,809 | 14,858 / 15,208 | 328 / 328 | header、短窗部分完整数值/时间列、真实3条链 |
| 目录2021-01-01–2021-12-31 | 241,659 / 266,469 | 241,659 / 254,424 | 7,456 / 7,469 | header和首尾，不声称全局min/max |

短窗物理 firing 时间列的全列范围是2021-01-14T09:04:10至2021-02-22T14:44:30（epoch数值转换为ISO Z，未核交易所时区解释），与目录范围及上游 receipt range 分开。短窗两路 localNo 均 min1/max5013/distinct5009，数值列 null/NaN/zero 等原始统计见 PHYSICAL_DATA_STATS；未把零值当缺失。独立 actual/confirm/known 时间字段未取得。

真实局部链为 localNo=1 的 Start→band_updated→End，writer trigger 相隔1.5秒和3秒；每条都对上 source artifact / UTI、sparse、packed row、current update 和上游 trace。短窗三路全部 root list pointers 与 firing 行顺序也已实读核对。End 行上游 band/core 均为4269，旧 occurrence 对应值均为0且 measurement=`not_present`；差异原样保留，交 E1 解释。未取得 FRP active map，不从 current 缺行补状态。短窗 diagnostics **非空**；前三条实读是 ingress InvalidNumericDomain / wall_band。样本同 firing 未见诊断仅限这个范围，不证明错误路径正确。

## 工单逐项状态与证据

| 项 | 状态 | 实际事实或限制 | 原件证据 |
|---|---|---|---|
| A1 | EXECUTED | 真实 cwd/thread/model/effort、UTC、主机/用户、可用磁盘已核 | `/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D001/W001/evidence/PHYSICAL_BINDING.json` |
| A2 | EXECUTED | PID227535/startticks44274656/inode14781898；竞争 EX flock EAGAIN；未替换/释放主控锁 | `/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D001/W001/evidence/PHYSICAL_BINDING.json` |
| A3 | EXECUTED | 真实 TIS/FRP/reader 依赖仓库 HEAD/branch/status/worktree/remote 与文件 hash 已记录 | `/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D001/W001/WORKSPACE_BINDING.json` |
| A4 | EXECUTED | TIS 与 FRP 旧 SHA 在本地可比较，HEAD 匹配，相关路径 diff stat 为空；其他 dirty 不修改 | `/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D001/W001/WORKSPACE_BINDING.json` |
| A5 | PARTIAL | BASE/tis 向上归到无关 uplot，发生一次意外父仓库 status 元数据枚举；已隔离记录且未扩搜 | `/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D001/W001/WORKSPACE_BINDING.json` |
| B1 | EXECUTED | 当前注册、FaoMeta、Cal/Cache/OnlyRead、源码参数和默认配置入口已定位 | `/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D001/W001/CODE_AND_READER_ENTRYPOINTS.md` |
| B2 | UNKNOWN | 当前真实执行的对象/日历/生效参数/范围/binary tuple 缺生成回执；不以静态默认补值 | `/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D001/W001/WORKSPACE_BINDING.json` |
| B3 | EXECUTED | generic generated wrapper 存在；静态 AST 明确缺三组 P1 Wall 所需类型 | `/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D001/W001/evidence/GENERATED_WRAPPER_BINDING.json` |
| B4 | PARTIAL | 原生 FrpDbaDao/read接口已定位，未进行可能有副作用的项目导入；物理只读探针另行已实测 | `/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D001/W001/CODE_AND_READER_ENTRYPOINTS.md` |
| B5 | EXECUTED | 三路 writer 当前名称/typed schema/路径规则和上游 receipt/sparse/trace 保存入口已列 | `/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D001/W001/CODE_AND_READER_ENTRYPOINTS.md` |
| C1 | EXECUTED | 三个代码/配置指向的 prod 根，588 精确类路径检查；155 目录796 文件 metadata，未全盘递归 | `/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D001/W001/ASSET_INVENTORY.json` |
| C2 | EXECUTED | 已有三路旧物化、上游 receipt/fields/sparse/state trace 的存在性分开登记 | `/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D001/W001/ASSET_INVENTORY.json` |
| C3 | NOT_FOUND | 已核产品 leaf 未见产品自身生成版本 receipt/manifest；当前 canonical schema 的物化未核得 | `/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D001/W001/ASSET_INVENTORY.json` |
| C4 | NOT_FOUND | 未取得 FRP DSU 完整 active-map 物化；上游 trace 不替代它 | `/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D001/W001/SAMPLE_CHAIN.jsonl` |
| C5 | PARTIAL | 下游 EawBattleP 和 Notebook 仅候选登记，未作当前同版或 Wall 适合性确认 | `/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D001/W001/ASSET_INVENTORY.json` |
| D1 | STOPPED_FOR_COST | 全796文件 header 探测35秒超时；无完成清单，不声称成功；随后仅95明确文件头完成 | `/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D001/W001/evidence/340-headers-only.command.json` |
| D2 | EXECUTED | 95 文件头全部有效；两份产品数量和短窗数值/时间列已核；全年只读首尾 | `/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D001/W001/evidence/PHYSICAL_DATA_STATS.json` |
| D3 | EXECUTED | 3条真实 Start→非平凡BandUpdate→End，同 Wall/UTI 对应 sparse/packed/current/上游trace | `/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D001/W001/SAMPLE_CHAIN.jsonl` |
| D4 | PARTIAL | 样本没有 Dormant/恢复；未覆盖全部生命周期/异常场景；不合成 | `/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D001/W001/SAMPLE_CHAIN_README.md` |
| D5 | EXECUTED | 短窗diagnostics非空328 firing；前三条 InvalidNumericDomain，样本同firing无诊断 | `/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D001/W001/evidence/SHORT_WINDOW_PHYSICAL_PROBE.json` |
| D6 | PARTIAL | 保留 epoch trigger 与 raw UTI；独立 actual/confirm/known 字段和生成 code binding 未取得 | `/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D001/W001/SAMPLE_CHAIN_README.md` |
| E1 | EXECUTED | 只静态列真实CLI、模板、窗口候选、重算/构建风险、成本未知、前置条件和停止点 | `/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D001/W001/ACTION_PREFLIGHT_FACTS.md` |
| E2 | NOT_APPLICABLE | 没有实际运行计算、测试Run、构建、安装、git变更或GitHub写入 | `/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D001/W001/COMMAND_LOG.txt` |
| F1 | PARTIAL | 本地原件交付；真实发布commit/ref缺失，正式 WORKER_RETURN.json 等主控回准确refs再同单生成 | `/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D001/W001/WORKER_RETURN_PREPARATION.json` |
| F2 | NOT_APPLICABLE | 业务预期、合理性、冻结、专业接受与父任务完成不属本Worker权限 | `/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D001/W001/WORKER_EXECUTION_REPORT.md` |

## 运行边界和失败原件

- 未执行任何 fetch/pull/checkout/reset/clean/rebase/merge、安装、构建、生产写入、数据库查询、全年/全品种重算或缓存清理。没有向其它聊天发消息或派生 Worker。
- 所有业务产物只在 W001；Python -B / PYTHONDONTWRITEBYTECODE=1，runner 的 TMPDIR、XDG_CACHE_HOME、PYTHONPYCACHEPREFIX、MPLCONFIGDIR 均指向 W001。没有 source m3rc，没有执行会在 W 外写 migration 日志的 run-python.sh，没有导入项目或触发 `.run/.F/to_df`。
- 796文件头尝试在35秒超时（exit124）；没有完整逐项回执，保留失败 stdout/stderr/命令，不补称已核。后续缩到95个明确文件头，结构全部有效，未重做大范围加载。
- 460样本JSON首次写出因真实NaN失败（exit1），空原件留存；470只修正JSON表示后重读。字段null均保留非有限值原因，无伪样本。
- 若干最初假设路径的 rg 返回exit2，真实错误全文保留；随后沿已定位路径查证。rg无匹配exit1按无匹配解释，不当运行成功证据。
- BASE/tis 的 Git 探测曾意外向上进入 `/dwdhome/fy` 的 uplot 父仓库并列未跟踪名称。没有读取那些文件内容、没有后续扩搜；此偏差明确登记。真实 TIS 另行准确核定。没有进行预计大搜索；进一步全盘、其它环境或更多数据库调查均未开展。

## 证据性质与专业未决

静态源码事实说明当前文本规定；现场绑定事实说明这台主机的 checkout、dirty、配置文本与文件存在；物化事实说明旧文件当前存在和具体 schema；可解码事实仅覆盖明确列和样本。没有当前同版生成回执/二进制绑定，不能将旧样本用作当前实现验收。当前 WallIdentity 结构本身仅含localNo，其与 run context 的业务含义交 E1，不用旧需求措辞替代源码事实。

E1 仍需判断旧材料可复用范围、当前身份/事务/End发布的业务适合性、完整 active map 或异常场景是否必要、是否签最小后继动作、是否具备冻结或专业接受资格。Worker 对这些项没有决定权。

## 主控逐字出版与原W1续签

请主控按 `PUBLICATION_MANIFEST.json` 的本地绝对路径与 sha256，逐字运输到 `daowei2026/observe-iterate` 获准分支 `runs/OI-EAW-WALL-20261114-01` 下 `longrun/runs/OI-EAW-WALL-20261114-01/worker_results/W001/`，保留相对目录。原始大数据仅引用不上传；本包没有复制原始大型市场文件。`HASHES.sha256` 覆盖自产原件，标准排除 hash索引自身；其自身摘要在本地封包命令及最终回报给出。

本地准备 `WORKER_RETURN_PREPARATION.json` 载明 outcome=PARTIAL、missing、准确 E1 及待填 result_ref，不是 V2 正式 Return。实际 commit 尚不存在，当前没有伪造精确ref。主控先出版证据，再回同W1：真实40位commit、各文件完整ref及sha256；W1核对后同单生成 `WORKER_RETURN.json`，按 V2 仅回原 E1，再由主控运输。不能改送manager，不能把本地Goal完成当作W或父任务完成。当前回合交件后自然结束，不轮询等ref。

采用的状态技能：[long-task-status](/home/dw/.agents/skills/long-task-status/SKILL.md)，只在W001内建 general/local ledger；没有对外发消息、通知或注册服务。本地阶段状态不代表专业接受。
