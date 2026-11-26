# D005 / C0009 证据与重放入口

本地根：`/dwdhome/fy/BASE_E6_2/artifacts/oi-eaw-p1-business-discovery-20261126-01/calls/C0009/`。以下均相对此根。主报告 EXECUTOR_REPORT.md；机器结果 report/RESULT.json；来源 SOURCE_INDEX.json；冻结清单 ARTIFACT_INDEX.json。大表、原始资产和图保留本地，不伪造远端附件。

|问题|实际证据及范围|
|---|---|
|本C正式指令/Owner原意|sources/INVOCATION.json、D005-DELEGATION.json/.md、C0008-PRO_RETURN.json、C0008-MANAGER_REPORT.md、OWNER_START.original.md、OWNER_RESUME.original.md、TASK_V0.4.md；新版指南两份；来源和准确refs见SOURCE_INDEX|
|具名读口版本和合同|sources/market_microstructure_evidence.py；report/READOUT_CONTRACT.json。读口sha256=93b55bf9c178c4834b486adb355ddbeb08c61e10c3918ff94a97c28cfbf4e3c5，与trainA该文件相同；不等于receipt版本。字段选择、hover、9个anchor/7个逻辑视图及时间绑定均从源码实际提取|
|实际导出而非假设消费者|sources/ACTUAL_READOUT_ASSETS.json：16窗口×6类资产共96引用，含共享与逐窗两种入口。复用C0002/sources/export_alltick_data.py与原manifest；不证明任何P2/FRP消费行为|
|展示重放核回|report/PROJECTION_EXACT_MATCH.csv：48组、1259行，全共同字段核回。仅AST抽取纯展示转换，不导入生产Feature；CSV时间先恢复原DBA的datetime dtype|
|本轮选例/相关性|report/CASE_SELECTION.json：J01–J12从既有条件表按品种×场景hash选择、排除列明既有深入/probe PG；J13–J16明确复用。16过程15PG12日期关联块，非严格留出；未声称旧Run所有暴露已排除|
|原输入与新QT定向独立核回|sources/RAW_QT_SELECTED_READ_AUDIT.json：只读16组原raw与新QT资产；465切点11数值列/时间、2QT列核回，不重复D004全包888资产扫描或原生存储核查|
|实际联合读表|report/JOINT_TRACE.csv 465行、JOINT_CUTS.csv 77行、FOCAL_READOUT.csv 16行；有exact Wall实例ppid、对象/侧/核心价/源cut、当前槽位、可见原因、活动起点/价位/年龄、两期间V及producer阶段。真实消耗/净撤始终空|
|每例可重放材料|cases/J01–J16：ORIGINAL_INPUTS、WALL_CONTEXT、5类正式HISTORY、6类ACTUAL_VIEW、JOINT_TRACE、JOINT_CUTS、CASE_METRICS。历史受原窗口/已有Wall前驱限制，不声称完整跨窗生命周期；CASE_READOUTS.md汇总实际读法|
|原/几何/闭合三时点|report/CLOCK_AUDIT.csv：7个Segment；最终原业务末端、几何末端和producer闭合分列，按available_at检验阶段。最终列仅事后核对，未注入JOINT_TRACE的当时已知端点。46个几何当闭合的假设过早点，不是实际消费者错读|
|期间端点影响|report/PERIOD_CLOCK_AUDIT.csv：77查询两种期间逐一直接核和；69处有起点量差。共同期间V不替代Absorb自己的track期间，也不解释为真实净撤|
|F4资格不是记录总量|report/F4_QUALIFICATION_CONTEXT.csv；FOCAL_READOUT内资格行及底层side/uti数。统计是共同期间两侧全部资格背景，不认证均归属目标Wall；J15六行/三底层瞬间、V0；J16零资格/V1306。已有D004反例明确复用|
|最小使用/删减试查|report/INFORMATION_ABLATION.csv、DESIGN_SUMMARY.json、ANSWERABILITY.csv。33个数量/基线可比查询有27数值不同、6相同；当前可见38/离开最佳价29/对象退出10；20查询为已接纳材料未闭合。人为删减研究，不是用户错误率|
|稀疏取舍实数|report/SPARSITY_BY_CASE.csv、SPARSITY_SUMMARY.csv；每例KEPT_*及STRATEGY_*保留保存点和逐切点对照。q/可见性变化219行但238个V差异；q或V变化450/465；按需仅答77。五列CSV成本不含身份/索引/传输/生产开销|
|设计位置与选择|report/DESIGN_DECISIONS.json：复盘侧按需联合；原时间字段不丢、几何另列；不为此次需求复制P1全局dense属性，不把缺hover全变新字段。N1/N2细化，新增独立迭代点0|
|图|figures/JOINT_READOUT_CASES.png/.pdf：6例当前量/活动参考/两期间V和阶段；SPARSITY_TRADEOFF.png/.pdf：行数与差异。PNG已实际查看，数量与量轴从0起；不画预测效果|
|独立核查与保留|report/LOCAL_VERIFICATION.json：24项通过，含原始源、独立asof当前对象和源行、期间、阶段、反例和策略。实际使用53输入和3个旧冻结入口hash稳定；不是再次全查644旧文件|

具名第一处限制：readout源码`_read_attack_segments`（616行起）未选closed_at，evidence_view_df（309行起）没有Formation分支；`_attack_segment_view`（822行起）将图的uti绑定业务端点，并扩单Tick几何。正式流仍保留原时钟。`_read_build_events`（593行起）已读baseline_vol/cum_reload_proxy；`_read_absorb_events`（643行起）未选累计C，不能把hit_vol_proxy当累计值。源缺项不自动成为业务缺陷；报告逐项给出用途与取舍。

P1真实来源复用C0002/sources/RECEIPT_INDEX.json、RESOLVED_SOURCE_PATHS.json、producer-source-matched与RECEIPT_CODE_VERIFICATION。Git部分c747d88…加逐源source-sha256；完整hash/参数见D001来源。QT/记录总量量义及源同一性复用D004已核事实；Owner“可能”语气保留。不把source_scope多年范围当本次新增行情。

重放入口（只写新的独立目录）：先复制本C必要输入与research目录到新目录，调整ROOT及相邻CALLS引用，不覆盖本冻结包。使用`/m3c3/Linux/apps/anaconda3/bin/python`。`prepare_readout.py`读取现有数据/源码，建立合同、样本、投影核回；`joint_readout.py`生成联合表和取值策略；`design_evidence.py`生成设计实表/案例读法/图；`source_index.py`索引准确输入；`verify_delivery.py`直接从原资产和正式表独立核查。原生产、参数、数据库及Chat均只读，不调用Feature.run/df，不扩行情。

此次已实际解决的接入问题：原30窗部分使用共享evidence表而非逐窗表，已定向回到manifest解决；冻结CSV整秒/毫秒混用，恢复原datetime dtype后纯投影核回；Wall结束后的同价L1量与当前对象分开。详见research/RESEARCH_DECISIONS.json。未将这些接入调整冒充新业务迭代点。

全部正式远端版本及精确读回由publication/PUBLICATION_READBACK.json记录。真实PRO_RETURN在所引用结果已发布后生成；RETURN_HANDOFF.md记录停止写和交回，controller再核物理结束及路由。Manager规范business_control双进度不由E1覆盖。
