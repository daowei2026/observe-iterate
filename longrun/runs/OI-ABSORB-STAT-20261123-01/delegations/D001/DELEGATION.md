# D001｜Absorb 最小当前理解 U

- Run：`OI-ABSORB-STAT-20261123-01`；work：`OI-ABSORB-STAT-20261123`；business case：`EAW-P1-ABSORB-STATISTICS-CLOSURE`。
- 工作项：`ABSORB-U-001`；Workflow 节点：`control-v0.3 U`；实际签发调用：`C0001`。
- 签发／接收／回交：`codex:OI-ABSORB-STAT-20261123-01:manager` → `codex:OI-ABSORB-STAT-20261123-01:executor:E1` → `codex:OI-ABSORB-STAT-20261123-01:manager`。
- 专业控制完整 commit：`b8c2b513f0b08be6a1fa6782b71bf74a07faff0d`。
- 物理 profile：`CODEX_NATIVE_DIRECT`；controller Skill commit：`fc966bcf5441701182339c992865504692f3a466`；`workers=[]`。

## 原 Skill 和适用输入

本次执行一项原 Skill 工作：

`daowei2026/observe-iterate@b8c2b513f0b08be6a1fa6782b71bf74a07faff0d:skills/feature-understanding/SKILL.md`

其 `WORKFLOW.md`、`IO_SPEC.md`、`BUSINESS_OBJECT_QUALIFICATION_GUIDE.md` 均取同一完整 commit。U 的采用方式为该 commit 的 `control-v0.3/01_L0_统计驱动的单特征闭环.md` 第 2.1 节。

准确业务输入为：

`daowei2026/observe-iterate@f166dc12a0b89d295510d7a1b31b439c1c52ae85:longrun/runs/OI-ABSORB-STAT-20261123-01/OWNER_START.md`

本项工作是 Owner 第八节的 Absorb 最小理解核对，形成足以支持本轮 X/G/D 的当前理解；正式业务来源、实例、exact Wall 合同及权限以该 Owner 原文和本 D JSON 的 `input_refs` 为准。

Owner 已提供的实例事实：目标 `AbsorbAssembler`；TIS `179016111ed0394f92025313e46bd13534932a74`；入口 `mquant.tis.hf.prel0.absorb_assembler.AbsorbAssembler`；当前默认正式参数；`TA_updto20240229_DBA`，`rb/m`，`2021-01-01` 至 `2021-12-31`，`night_end_at_2300`；workspace `/dwdhome/fy/BASE_E6_2`。具体默认值读取 Owner 第六节与指定实现。

已有上游：本 Run 的 Owner、Binding、资源绑定和专业控制采用记录已存在；尚无本 Run 已接受的 Absorb UnderstandingPackage、正式运行结果或 exact Wall receipt/artifact。Owner 允许 exact Wall 技术依赖，但 WALL 合理性 Run 已停止且没有全面合理性 Release，旧 `6618d4d...` 的 rb 部分结果不能充当本 Run exact upstream。

## 回交

专业输出与完成状态直接遵循原 Skill 及其采用的 U 规则，以 `FeatureUnderstandingPackage` 回交原 manager，保留 `ABSORB-U-001 / D001` 身份。专业方法和完成条件由原 Skill 定义。

V2 回交使用 `longrun-professional-return/v2`，引用本 D 的已发布 exact JSON；`issued_order_refs=[]`、`accepted_worker_refs=[]`。按 native profile 在结果报告中说明实际采用的专业控制完整 commit。

操作权限来自准确 Owner GO 和 RUN_BINDING，机读范围见配套 JSON；controller 在实际派发时独立核验。manager 未创建 E1 物理线程；该创建与派达由 controller 在收到正式 D/Return 后办理。
