# S06/B3及第一轮归并复核入口

本目录是D006任务书原生研究产物，不是新增Workflow/Skill或审批计划。继续原E1，workers=[]，仅S06；未执行S07/S08/S09。

先读 `../EXECUTOR_REPORT.md`、`../B3_CASEBOOK.md`、`../FIRST_ROUND_SYNTHESIS.md` 和 `../report/CANDIDATE_REGISTER.json`。ARTIFACT_INDEX.json给本C冻结文件的准确路径、bytes和SHA-256；详细图/表/代码留本地。

实际执行：

1. `select_b3.py`：复用C0005/scan/CANDIDATES.csv.gz，先排除reserved，只访问前期/当期白名单字段。匹配r/c/n/长度及可得背景，比较最低点、减量集中度、前后阶段/正向活动顺序。初版205个形状轴配对、四组；恢复和Wall不足时，读取后期前用 `--variant wall_recovery_relaxed` 扩到30秒并放宽匹配，2594配对，补两组。初版和补救均保留，旧四组未替换；四标准/两放宽质量分开。`MATCH_CONFIG`的初版calipers为基准，补救字段记录覆盖条件；最终 `ANALYSIS_GROUPS_FROZEN.json.effective_calipers` 给每组准确生效值。
2. `freeze_b3.py`：合并初版四组与补救两组，保留两个冻结源SHA；在后期提取前再次冻结分析组，检查12个不同片段/PG和先前暴露。没有用预留或后期修正口径。
3. `extract_b3.py`：复用既有真实取证机械过程，从原始报价独立重算量变及形状/阶段值并核S03；保存source_refs/CSV行。按连续有效侧段取前30秒/后60秒可得上下文，完整可得同侧P1窗口属性另存P1_AVAILABLE_HISTORY。它不是正式完整history/current重建。已有提取会拒绝覆盖。
4. `plot_b3.py`：实际挂量、同源C/原始V/正向可见活动、独立后期价格与联合展示对齐；量变末点和阶段中点另标。绘图复用C0007隔离环境 `/dwdhome/fy/BASE_E6_2/artifacts/oi-eaw-p1-business-discovery-20261125-01/calls/C0007/research/plot-env/bin/python`，依赖版本见该C的PLOT_REQUIREMENTS.txt，不安装或改生产环境。六组PNG/PDF均已实际查看。
5. `summarize_b3.py`：复见量、Wall展示起量、全部可得同侧属性与六类来源可用性；累计使用完整继承C0009记录。最初沿用B2低/高列名已在冻结报告前改为A/B，数据与选样未变；旧汇总日志保留。当前PAIR_SUMMARY按A/B解释，形状轴不同不混成统一高低效果。
6. `first_round_index.py`：对C0007/C0009/C0011实际36例建立精确索引、PG/日期块/时间/片段关系；三方向共有33保守PG/12日期块，非36个独立攻防。累计46数值回看区间含10个初版未最终选入区间；36次深入提取，53预留窗口/50组未深入。
7. `verify_b3.py`：独立原始源、量变/阶段分母、匹配、未来方向/截断、同价/近价关系、冻结顺序、旧索引与累计账核查。结果PASS，91源文件、2089报价行、425可得P1行；旧C0002/C0005/C0007/C0009冻结产物未变。自检不是controller物理回执或Manager消费。
8. `write_casebook.py`、`synthesize_first_round.py`、`write_report.py`：基于已核事实生成本D真实专业判断、三方向归并及后继顺序；不重选样本，不执行第二轮。R1/R2/R3等级都为研究线索；正式缺口/必须修改/生产Bug均未确认。

量尺约束：C/V不含首行；C_quote等于本批可见减量，n_quote等于正向可见变动/q0。阶段切分floor(更新数/2)，n_first分母q0、n_second分母q_mid，不能直接相加。B3-06-B的11是22/2，整体仍22/29。Wall band只对Wall作同价判断；B3-05-B有近价725.5对象而研究价725，不能改写无Wall。事件发生、Attack business_end/闭段、展示、实际发布时间分开。

安全只读复核：读取report/VERIFICATION、FIRST_ROUND_EVIDENCE_SUMMARY、PAIR_SUMMARY、P1_ATTRIBUTE_AUDIT、P1_SOURCE_AVAILABILITY、PRIOR_REUSE_LINKS、SAMPLE_USE_CUMULATIVE以及每例原始trace/history。`check_frozen.py`只读校验冻结索引，不改变产物。

所有会生成输出的脚本都应在独立scratch副本中重现，不在已冻结根重跑覆盖。仅Owner同批原件、授权工作区及本Run路径；未新增行情/生产重跑、未导入执行生产特征或修改数据库/参数/公共上游。参考TIS/FRP版本与本批实际版本不同，receipt/正式完整历史等缺件保持待证。

正式发布使用指定Personal连接Contents API，检查当前head、路径不存在或当前blob条件，写后exact回读内容和parent；报告先、零W Return后。本地PUBLICATION_READBACK.json及publication/RETURN_HANDOFF.json给实际运输事实，父Run未完成。
