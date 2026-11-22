# D012｜M-E CAEGraph真实执行、核图与正式取数

Run `OI-F800-STAT-20261122-01`，issuer_call=C0026；原manager `codex:OI-F800-STAT-20261122-01:manager` → 本Run原独立executor `codex:OI-F800-STAT-20261122-01:executor:E1` → 回原manager。CODEX_NATIVE_DIRECT，workers=[]；一份D只委派原E Skill，E1—E6是原E1同线程连续工作，零W/W1/W2。

唯一专业依据 `daowei2026/observe-iterate@87b951bbd15078a2d6353bdd24afe0d8f19c845c:skills/observation-material-preparation/caegraph-execution/SKILL.md`，同版 `daowei2026/observe-iterate@87b951bbd15078a2d6353bdd24afe0d8f19c845c:skills/observation-material-preparation/caegraph-execution/WORKFLOW.md` 与 `daowei2026/observe-iterate@87b951bbd15078a2d6353bdd24afe0d8f19c845c:skills/observation-material-preparation/caegraph-execution/IO_SPEC.md`、原M外层Workflow。方法、工程处理/专业回流边界、图接受、正式取数及完成条件直接按原文，不附manager自造实现步骤、业务预期或Gate。

## 当前有效输入

原D011/C0025 Return `daowei2026/observe-iterate@8c3d8bb319643692e98f7a0924719cb7314561a2:longrun/runs/OI-F800-STAT-20261122-01/calls/C0025/PRO_RETURN.json` 已由原manager消费；定义 `daowei2026/observe-iterate@c19db65f5b7e228d1db4be61d06e361c16bafa33:longrun/runs/OI-F800-STAT-20261122-01/professional/D011/CAEGraphDefinitionIntegrationResult.json` 为完整F800-D-v1，无核心缺项、阻塞或具名回流。完整包由 `daowei2026/observe-iterate@c19db65f5b7e228d1db4be61d06e361c16bafa33:longrun/runs/OI-F800-STAT-20261122-01/professional/D011/PROFESSIONAL_MANIFEST.json` 的同一准确commit逐文件绑定，63项原件字节/hash核同；包括launcher、完整definition、逐字C3 renderer、inputs及准确uplot快照，不能只拿launcher脱离包运行。D原生10项定义检查通过、首次BOM误报/修复档案保留；不等于真实构图、核图或取数已通过。

实例/U为D008当前39f有效完整X/G，B为D009 F800-MB-D009-P001完整rb/hc/i、5m、2021-01-01—2023-12-31、原SOF/steel/night_end_at_2300。D已将原日期端点确定性解析为含端点UTI72003600—101813399，完整请求未缩短；见原D集成/纠正记录，不由E重新选位置。

C2基准为唯一F800-C2-v4 `daowei2026/observe-iterate@ec747f4d460956bd1a91f59d0dcbaba6722ce750:longrun/runs/OI-F800-STAT-20261122-01/professional/D010/C2_CURRENT_EXPECTATION.json` 和 `daowei2026/observe-iterate@ec747f4d460956bd1a91f59d0dcbaba6722ce750:longrun/runs/OI-F800-STAT-20261122-01/professional/D010/html/current.html`，HTML SHA-256 `3a24ab08887ce5d948b229e7d37f63a4f9a669218b47110ad4385f737a7bdded`。C3-v1原字节SHA-256 `e5d6a235cd23f7e90ebbd8f020768f7e91b81ffd1782fc824362543c0f696ec0`。C2的SYN业务值/短窗为预期预览；本D依据是D已绑定的真实三年实例，C浏览器检查不替代E3。D三项有据补齐及真实待确认项沿 `daowei2026/observe-iterate@c19db65f5b7e228d1db4be61d06e361c16bafa33:longrun/runs/OI-F800-STAT-20261122-01/professional/D011/UPSTREAM_CORRECTIONS.json`、`daowei2026/observe-iterate@c19db65f5b7e228d1db4be61d06e361c16bafa33:longrun/runs/OI-F800-STAT-20261122-01/professional/D011/E_PENDING.json` 原件，不重做专业定义或添一套核对法。

当前FRP `39f02ec4548e68ba8dbd30061afc870546000994`、TIS `2f460d663d821cf2ba25555eda13e78b697d0767`；配置SHA-256 `b72095ff100da926474701b74bff7586a74b9770bc81cadc34c23cfe223e5cb3`；800/600/CalendarUTITick/2Delta1200/method.revision1、PNV/完整范围不变。uplot沿已锁0a4fcd54059782572a3f7e82fad041121e8c65ad快照及D依赖绑定；不重解析分支。原U PARTIAL、未暴露轨迹、原四问题/七candidate-only及Q边界继续传递。

## 工作区、入口与授权

执行上下文 `/dwdhome/fy/BASE_E6_2_copy`。D已给出的真实入口（本manager未执行）：

```bash
PYTHONDONTWRITEBYTECODE=1 bash /dwdhome/fy/BASE_E6_2_copy/run-python.sh /dwdhome/fy/BASE_E6_2_copy/artifacts/OI-F800-STAT-20261122-01/D011/run_definition.py --output-html /dwdhome/fy/BASE_E6_2_copy/artifacts/OI-F800-STAT-20261122-01/caegraph-E/f800.html
```

最终HTML预定位置 `/dwdhome/fy/BASE_E6_2_copy/artifacts/OI-F800-STAT-20261122-01/caegraph-E/f800.html`，沿原定义输出；本次运行/修复和图数据写本Run独立产物，正式数据输出及与被接受运行的绑定由E4按原Skill形成。专业记录提交限定 `longrun/runs/OI-F800-STAT-20261122-01/professional/D012/` 与本次C/Run既有授权根，真实运行事实及必要物理映射保留现场账本。

权限仅来自最新 `daowei2026/observe-iterate@3dc11a9dbf39e181b3c6a3051419a90e46b92aac:longrun/runs/OI-F800-STAT-20261122-01/RUN_BINDING.json` 中 `run_result_statistics_analysis_write`（执行上下文BASE，允许BASE）和 `run_record_write`（observe-iterate@codex/oi-f800-stat-20261122-01，允许本Run/**），原Owner GO及MP002批准见JSON准确输入。E可在此权限内按原Skill调查、作不改变业务含义的run-local工程修复并连续重试；原Skill对安装/重建/受保护平台和锁定版本变更的授权边界照旧，不因一次普通import/API/路径错误停止整个Skill。

F只沿D既定OnlyRead/to_dfs和已接受物化上游源；缺源不转生产。本D未授 `formal_feature_run`、新Feature行为修改/代码采用、uplot仓库修改、Q/V或WALL。有效U/X/G/B/C/D复用，不新生产或重做统计；现行Run资源单写者及重型正式生产/shared写面flock规则保持，本D不声称已取得物理权限或持锁。

controller按V2核原E1真实线程、sol/max、cwd、权限/单写者及真实状态后合法派达，签D/发布不是物理送达或开工回执。原E直接执行的日志、diff、图接受、正式取数与一致性证据承载完成事实；无独立Worker不构成缺项。专业回交按原Skill和V2 Return，不越级签场景预期或FeatureRelease。manager消费本D真实回交后，沿既有C0020审查及适用S1/S2/L1继续。
