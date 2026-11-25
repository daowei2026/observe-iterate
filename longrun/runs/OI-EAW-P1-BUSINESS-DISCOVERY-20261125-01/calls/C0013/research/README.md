# D007／R1 研究入口

本次只执行R1的S07＋S08。默认Python标准库；作图复用C0007的plot-env（matplotlib3.11.2/numpy2.5.5与原Noto CJK字体），没有重装生产环境。没有import或run生产producer。原始数据和S01～S06成果只读。

实际口径/首次预留访问之前冻结的问题在 `../selection/R1_BASIS_FROZEN.json`；匹配沿用原B3标准/放宽，非新审批计划。`scan_r1.py`明确不访问future列；同批全范围形态/交互访问有真实记录，不能称严格样本外。最小试查的18PG/候选ID由哈希选择。

## 已执行的程序和产物

1. `freeze_basis.py`：继承R1原文、旧使用账本SHA256和执行口径；只读取旧记录/代码后固化，未访问预留形态。
2. `scan_r1.py`：全部444个quote资产哈希核对、261,497区间条件分母、原B3匹配、PG隔离和确定性试查。`scan/`保留适格区间、whole片段、全部标准/放宽备选、PG不复用匹配和分母；`selection/`保留冻结输入。
3. `extract_r1.py`：冻结的4组/8例和18试查的真实quote轨迹、全部可用同侧P1展示历史、原始属性与固定10/30/60秒。改自C0011真实程序，实际差异见EXTRACT_REUSE.json。
4. `recontact_r1.py`：同有效连续侧段内，片段结束的下一quote向攻击方向离开，固定窗口首个同价最优复见数量/时延；截断分开，片段/PG分母同时保存。
5. `conditional_r1.py`：片段、PG/日期块/起量/时长/阈值敏感性；PG不复用的冻结匹配固定后期分布。未来价格仅作选样后描述，不改组。
6. `prepare_contacts.py`、`extract_contacts.py`：冻结的3个复见/普通/截断例。准备逻辑首次以内联脚本执行后保存；不声称其文件字节在更早时间已冻结。真实选择时间由RECONTACT_EXAMPLES_FROZEN和contact提取日志给出。
7. `summarize_r1.py`：全部29例索引、联合属性/实际源可用性、独立性/使用记录；原82条使用记录原样保留，另记全范围形态/交互及70个具体后期度量区间的访问。
8. `verify_evidence.py`：原始行号/哈希、连续性、可见下降代理/正向变动、阶段分母、未来完整性、全部可用P1原始attrs、样本隔离及S01～S06冻结文件不变。结果VERIFICATION_EVIDENCE.json。
9. `probe_minimum.py`：18个非形状选样区间只补min/q0与首次min位置，输出基准/增强研究表、普通/隐藏薄弱及失效边界，不改变正式特征。
10. `plot_r1.py`、`plot_contacts.py`：11幅真实证据图，PNG/PDF，包含量变段放大、C/原始总成交/G、固定后期与同侧展示上下文。长标题在首次数据视觉核对后缩短，数据和选组未改。未处最优档的旧价量留空。
11. `write_delivery.py`：依据已保存数值整理casebook、R1结果和正式报告；人工设计定位在R1_DESIGN_POSITIONING.md，准确设计/代码来源在SOURCE_INDEX.json。

## 复放边界

冻结目录是交付证据，**不要在原目录重跑生成器覆盖原冻结文件**。只读核查可直接运行后续 `check_frozen.py`。若需重放，使用本workspace内单独scratch/calls/C0013，复制research和sources；将原C0002/C0005/C0007/C0011目录作为只读上游入口，放在同级（可用指向原成果的符号链接，生成程序只读这些路径）。数据常量仍指原Owner批次。

在空scratch输出目录，按上列1～9顺序执行；步骤4/5相互独立但都须在步骤2选样冻结后。prepare_contacts依赖步骤4，extract_contacts依赖prepare_contacts；summarize依赖所有提取及conditional；verify依赖summarize。绘图用已存在C0007/plot-env/bin/python运行10。生成器带不覆盖已有关键冻结/提取文件的检查。复制SOURCE_INDEX及手工设计记录作引用，不因重放改变本次实际访问/签认时间。时间戳、路径、文件哈希会因scratch不同而变；候选IDs、实数值、分母和业务结果应相同。

这只是本C已有研究脚本的执行说明，不是新的通用workflow或专业复审。任务书与longrun版本不变，workers=[]。
