# OWNER GO｜OI-WALL-STAT-20261122-01

Run identity assigned by controller under Owner instruction. work_id=OI-WALL-STAT-20261122; business_case_id=WALL-STATISTICS-CLOSURE; execution_profile=CODEX_NATIVE_DIRECT; manager/executor target=gpt-6.1-sol/max from adopted V2 Codex target. workers=[].

BusinessTaskInput=daowei2026/observe-iterate@87b951bbd15078a2d6353bdd24afe0d8f19c845c:task-inputs/wall-f-parallel-closure-20261122/WALL_BASE_RUN_INPUT.md

This Run record branch: codex/oi-wall-stat-20261122-01. Linux workspace: /dwdhome/fy/BASE_E6_2. New manager and later E1 executor; no reused physical identities. Owner authorizes creating run-scoped record paths and branches; their concrete names are controller-assigned. Formal Feature changes require Owner approval.

以下为Owner原文（逐字保留）：

【Owner 指令｜结束旧 V Run，并启动 WALL / F 两条统计闭环 Run】

一、结束旧 V Run

现明确结束旧 V Run：

run_id = OI-U2-V-OBS-20261120-01
workspace = /dwdhome/fy/BASE_E6_2_copy

这是 Owner 主动终止，不代表该 V Run 的专业任务已完成，也不得标记为 REPORTED_COMPLETE 或业务验收通过。

请按原 V2 运行记录执行以下动作：

1. 停止为该 V Run 派发新的 C / D / W 或继续专业后继；
2. 对账该 Run 当前 manager、executor、Worker/Codex thread、在途 turn、Linux 进程及可能的写副作用；
3. 已经真实完成或产生的历史产物、调用记录、Git 记录和专业结果全部保留，不删除、不改写；
4. 对发送结果不明或可能仍在运行的动作先完成对账，不把 UNKNOWN 直接写成未发生；
5. 将该 Run 记为 OWNER_TERMINATED / CANCELLED_BY_OWNER，明确“未完成的业务范围不再继续”；
6. 在确认没有仍在写入的线程、进程、数据库、缓存和结果任务后，正式释放：
   /dwdhome/fy/BASE_E6_2_copy
7. 更新本 Run 的动作账本、资源状态和 RUN_REGISTRY；不得把旧 V Run 的物理线程或专业完成状态复用于新的 F Run。

释放完成后，不需要再向 Owner询问是否可以启动 F，直接按下面要求继续。

二、采用版本

本轮采用：

observe-iterate：
daowei2026/observe-iterate@87b951bbd15078a2d6353bdd24afe0d8f19c845c

cgpterm Codex-native controller：
daowei2026/cgpterm@fc966bcf5441701182339c992865504692f3a466:
.agents/skills/observe-iterate-longrun-v2-codex-native-controller/SKILL.md

执行 profile：
CODEX_NATIVE_DIRECT

每个新 Run：
- 新建一条 Codex manager thread；
- manager 签发首个正式 Skill D 后，新建一条独立 Codex executor:E1 thread；
- manager 与 executor 不得使用同一 thread；
- 不复用旧 V Run 或其他 Run 的 threadId；
- workers = []；
- executor 直接访问本 Run 的 Linux 工作区；
- 继续使用原 V2 的 C / D / PRO_RETURN 协议。

三、启动 WALL Run

请为 WALL 分配全新的唯一 run_id，并注册新 Run。

工作区：
/dwdhome/fy/BASE_E6_2

业务输入：
daowei2026/observe-iterate@87b951bbd15078a2d6353bdd24afe0d8f19c845c:
task-inputs/wall-f-parallel-closure-20261122/WALL_BASE_RUN_INPUT.md

代码：
daowei2026/tis@6618d4d147d6ebbe634e61facddf2c9a0b996982

Feature：
mquant.tis.hf.prel0.wall_assembler.WallAssembler

正式实例：
- 默认参数；
- sof_name = TA_updto20240229_DBA；
- symbols = [rb, m]；
- start_date = 2021-01-01；
- end_date = 2021-12-31；
- calendar = night_end_at_2300。

已确认采用 D1、D2、D4 修复链；D3 保持暂缓，本轮不因 D3 阻断下游。

启动前现场核实：
- 工作区存在和 realpath；
- 没有其他 Run 或旧进程继续写；
- Git HEAD 和 Python 实际加载文件对应 6618d4d...；
- 实际参数是锁定提交上的默认 WallAssembler 参数；
- 共享缓存、数据库和结果目录只有一个写者。

已有结果只在 commit、完整参数、范围、Calendar、输入处理、结果身份、哈希和独立读回全部一致时复用；否则运行正式实例。

WALL 满足自身预检后可以立即先启动，不需要等待 F。

四、启动 F Run

旧 V Run 完成收束并释放 /dwdhome/fy/BASE_E6_2_copy 后，为 F 分配全新的唯一 run_id，并注册新 Run。

工作区：
/dwdhome/fy/BASE_E6_2_copy

业务输入：
daowei2026/observe-iterate@87b951bbd15078a2d6353bdd24afe0d8f19c845c:
task-inputs/wall-f-parallel-closure-20261122/F_BASE_RUN_INPUT.md

FRP：
repository = daowei2026/frp
branch = codex/f-observation-multiple-20261122
commit = ac1927518ad6105f15ffbe37fea45e4be91ba574

TIS：
daowei2026/tis@2f460d663d821cf2ba25555eda13e78b697d0767

构造入口：
frp/fqv_kline_example.py::make_features

Feature：
CommonPriceTurnGroupCandidatesFrp，即 make_features(...) 返回的 f。
本基础 Run 只运行和分析 F，不把 Q、V 作为本 Run 的专业产物。

正式实例必须满足：

profile.observation_multiple = 800
profile.delta = 600
profile.unit = CalendarUTITick
symbols = [rb, hc, i]
frequency = 5m
calendar = night_end_at_2300
sof_name = TA_updto20240229_DBA
industry = steel
start_date = 2021-01-01
end_date = 2023-12-31

旧实例脚本原样调用 make_features(**PARAMS) 会继续得到默认 observation_multiple=6，禁止把它直接作为 F800 正式入口。

正确做法是：
- 用原 U2/U3 参数构造基线 f；
- 复制基线 profile；
- 只加入 profile.observation_multiple = 800；
- 使用相同 inputs/sources、domain、result_layout 重建 F；
- 运行前保存并回读完整序列化配置；
- 证明除 observation_multiple 外，没有未声明的参数变化；
- 证明 2Δ 的实际转折贴近条件没有被放大；
- 证明 F800 full_dir 与默认 6 的结果目录不同。

若配置回读仍为 6，或实际加载的 FRP 不是 ac192751...，立即停止该次正式运行并报告，不得静默回退。

已有 F800 结果只有在以下全部一致时才可复用：
- FRP commit；
- TIS commit；
- 完整序列化配置；
- observation_multiple=800；
- 日期范围；
- symbols / 5m / Calendar；
- full_dir；
- fields/config hash；
- 独立公开表读回。

不满足时，只重跑正式 F800。

五、两条 Run 的专业范围

两条 Run 都按当前统计驱动的单 Feature 闭环推进：

最小必要理解核对
→ 正式实例运行或合格结果复用
→ 全量行为统计
→ 业务对象、Event、occurrence、字段和时序映射
→ 已知 finding 复核
→ 继续发现明显不合理问题
→ finding 诊断和证据闭环
→ 形成各自 ReleaseGate / ReleasePackage

Owner 当前重点是：
- 找问题；
- 分析问题；
- 处理改法明确的明显问题；
- 继续推进下游。

不要求本轮先研究复杂、低发生比例且改法不确定的规则。

若执行中建议改变正式 Feature 行为、参数、常量、期限关系、数据处理或输出合同：

ModificationProposal
→ 影响范围和验证方案
→ 回 Owner 确认
→ 确认后才实施、提交和采用

未经确认，不得修改、提交或推送新的 Feature 行为。

六、授权

本次授权两条新 Run 分别进行：

1. 读取锁定代码、业务输入、历史产物和已有缓存；
2. 核实工作区、代码加载、参数实例和结果身份；
3. 运行正式 Feature；
4. 写入本 Run 独立的运行结果、统计脚本、日志、图表和分析报告；
5. 写入并提交本 Run 的 OWNER GO、Binding、资源记录、调用记录、TASK_PROGRESS、专业报告和 ReleasePackage；
6. 在准确一致时读取和复用已有正式结果。

本次不授权：
- 未经 Owner 确认修改 Feature 正式行为；
- 将诊断候选参数直接变成正式参数；
- 复用其他 Run 的线程、身份、结果目录或完成状态；
- 擅自缩短正式品种、日期或尺度范围。

七、调度

WALL 和 F 是两个独立 Run，可以并行推进。

但“并行”不要求两个重型全量生产过程同一时刻争用共享存储、数据库或内存。若现场发现两个 X 阶段存在资源冲突，可以错峰运行重型生产；另一条 Run 的理解核对、已有结果读回、统计或诊断仍可继续。

请不要再次向 Owner询问以下已经明确的事项：
- WALL 的品种、年份、工作区、代码和默认参数；
- F 的品种、尺度、年份、工作区和 observation_multiple；
- 是否使用 Web manager；
- 是否使用 Worker；
- F 是否连 Q/V 一起跑；
- D1/D2/D4 是否采用；
- 新 finding 是否可以直接修改正式行为。

只在出现真实现场冲突时报告准确阻断，例如：
- 工作区未释放；
- 仍有旧进程或写副作用；
- 实际加载路径与锁定 commit 不一致；
- Codex model/effort 无法按目标值创建并回读；
- 结果身份无法核实；
- 共享写面不存在单写者。
