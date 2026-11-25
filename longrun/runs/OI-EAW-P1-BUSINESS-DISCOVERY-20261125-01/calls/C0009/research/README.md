# S05/B2 本地研究入口

本目录为D005的实际研究代码与证据，不是新的专业Workflow/Skill。原任务书版本b1bf8025、controller版本da8dabfd、当前C0009与原E1保持；只执行S05，workers=[]。

先读 `../EXECUTOR_REPORT.md` 和 `../B2_CASEBOOK.md`。完整本地产物见 `../ARTIFACT_INDEX.json` 的绝对路径、bytes、SHA-256；不要在已冻结目录重跑生成器覆盖文件。

实际执行顺序：

1. `select_b2.py`：沿用S03候选表；先排除reserved，再按白名单访问当期/前期字段，未使用后期字段选样。按同品种、侧别、时长、日夜和前期背景，实际检索维持/下降两类。六组保留467个配对的分母与条件；初次读取空报价和零C更新占比的问题均在冻结前修正，没有读取案例未来后改选。
2. `freeze_b2.py`：低C相对于净下降的分支机械不可识别，冻结前用同批原始总成交作条件上界尝试；5423个区间满足V低于净下降，严格背景匹配已选组得0例。没有新增或替换案例。所有计量假设与限制保存在 `RAW_VOLUME_BOUND_REMEDY.json`。
3. `extract_b2.py`：在最终组别冻结后，从原始报价重新取量，实际校核S03值；记录原文件/CSV行。只在有效同侧连续段内取前30秒、后60秒的可用上下文，不补断点。读取六类同侧P1可得窗口历史的全部原文，同时输出局部时间上下文；它不重建完整正式history/current。
4. `plot_b2.py`：实际报价图，分开量变与t1后固定观察。复用C0007的隔离环境 `/dwdhome/fy/BASE_E6_2/artifacts/oi-eaw-p1-business-discovery-20261125-01/calls/C0007/research/plot-env/bin/python`，依赖版本在C0007/research/PLOT_REQUIREMENTS.txt；无需生产环境或新增安装。六组PNG/PDF均已实际查看。
5. `summarize_b2.py`：同价最优复见量、Wall展示起点量、全部可用联合属性与原文引用、六类来源可用性及累计样本使用。S04旧记录原样继承，34个选样数值区间/24次深入提取；预留53窗口/50保守组未深入。
6. `verify_b2.py`：独立由原始CSV核量变/源文/匹配、价格方向及截断；86个源文件验证，旧C0002/C0005/C0007冻结文件未变。`VERIFICATION.json`是执行者自检，不是controller物理回执。
7. `write_reports.py`：从已核数值和逐组专业判断形成报告/案例册/S05_SUMMARY；不重新选样。源码中的解释、反例及不足是E1本次专业判断。

可安全只读复核入口：`../report/VERIFICATION.json`、`../report/PAIR_SUMMARY.json`、`../report/P1_ATTRIBUTE_AUDIT.json`、`../report/P1_SOURCE_AVAILABILITY.csv`、`../report/REVISIT_AND_WALL_START.json`、每例的QUOTE_TRACE/P1_CONTEXT/P1_AVAILABLE_HISTORY/CASE_METRICS。所有引用的Owner原始文件仅只读。

同价量变C/V均不含首行。C_quote是盘口减少代理；n_quote在本批等于正向可见变动/q0。真实净新增/撤单、真实方向成交、冰山或订单身份没有被识别。后期位移ask向上、bid向下，中间价观察格点rb/hc=1、i=.5；极值含起点0，缺失不填0。

如需重现生成，应另建本Run内独立scratch副本，保留原路径/相对输入关系及冻结文件；不要在本冻结根运行写输出的脚本。未要求或执行新的行情、生产特征重跑、数据库或生产代码写入。参考TIS/FRP代码只用于语义追查，不导入运行、不视为本批生产版本。

正式发布使用同Personal连接Contents API，串行核当前head、目标路径/已有blob、写入结果及exact commit内容/parent。详细表、图和代码按D留本地；正式报告与零W Return先后发布。实际运输事实见 `../PUBLICATION_READBACK.json` 与 `../publication/RETURN_HANDOFF.json`，不伪造Manager消费或Run完成。
