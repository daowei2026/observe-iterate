# C0009 / D005 / S05 持续进度

当前状态：S05 实际研究与报告已完成；发布回交进行中。只执行独立 B2。S01～S04 成果复用，父 Run 尚未完成。

实际输入：本目录 sources/INVOCATION.json、DELEGATION.json、DELEGATION.md、MANAGER_C0008_PRO_RETURN.json；任务书锁定 b1bf8025dd49091e71c8814caf36c2e02aced198；C0005 scan/CANDIDATES.csv.gz；C0007 冻结证据、SAMPLE_USE_CUMULATIVE.json。原始行情仅 Owner 同批目录。

已完成：亲自读取正式委派、调用身份、Manager 回交和通用 executor 指南；核本 D 只为 S05。累计样本记录待核后继承。

已确认边界：方向代理 C_quote 与可见减量同源，实际成交方向/撤单不可据此独立分解；正式 producer/FRP receipt、版本、身份及完整历史缺失不等于产品缺口。保留预留窗口，不据后续价格选例。

产出：sources/ 已保存本次正式原件；其他研究产物随实际执行分批保存。

实际检索检查点：selection/SELECTION_FROZEN.json 与 POOL_SUMMARY.json 已保存。共读取 261497 个候选标识，95565 个 reserved 在指标前排除；165932 个 discovery 的量变恒等核查全部成立；57585 个符合本次基本条件，467 个匹配对（quiet 198、decline 269），22 对有 Wall 展示。选出六组十二例：两组 rb 维持、两组 hc 下降、一组 i 的 Wall 可见/未知对照、一组 1 秒短片段。选样尚未读后期。B2-02 两侧 PG 与 S04 已用 PG 重合，候选区间均不同，保留依赖关系。

首个发现：51373 个发现集下降区间中，C_quote 小于净下降的数量为0，负 n_quote 为0；这是 C_quote=可见减量、n_quote=正向可见变动/q0 的机械关系，不证明真实撤单缺席。需保留真实成交方向/单位/完整性不足，并试查同批原始总成交能提供何种有条件约束。

执行记录：首次读取 raw 空报价需按无效值处理；零 C 的最大更新占比本来无定义，脚本仅为元数据记0，未据此匹配。两次均在冻结前停止，无案例后期读取。修正后 select_b2.py 实际完成；不是生产重跑。

后续实际完成：六组于2026-11-25T19:05:05.393085+00:00冻结；后期提取始于19:05:44.896589+00:00，未据未来换例。已保存1937行原始报价、250行本窗口可用同侧P1属性、六组PNG/PDF；全部六类来源可用性78条、73展示文件含空快照。86个源文件哈希/原文核对，自检PASS；旧C0002/C0005/C0007共24/33/103项冻结材料未变。

不足补救实际结果：5423个发现集下降区间总成交小于净下降，但按本次下降组原背景条件未匹配出补充例。总成交单位/计量范围/时序/完整性仍须receipt，未据其证明真实净撤单。

产出：EXECUTOR_REPORT.md、B2_CASEBOOK.md、report/S05_SUMMARY.json、VERIFICATION.json、P1_ATTRIBUTE_AUDIT.json、PAIR_SUMMARY.json、P1_SOURCE_AVAILABILITY.csv、SAMPLE_USE_CUMULATIVE.json、S04_REUSE_LINKS.json、原始cases、figures及研究代码均已形成。累计34个数值回看区间、24次深入提取；53预留窗口/50保守组未深入。B2-02与旧PG018/PG039相关、无同价片段或时间重叠，非独立复现。

专业判断：两条研究线索（来源/可识别性；存量/活动/联合时点），正式缺口及研发优先级未证，确认必须修改为0。Wall组已有联合属性区别，保留四个C_quote大于总成交的具体反例、B2-06价格反例、B2-01期限反转及后期截断。

发布前已核：指定Personal连接实际head=a93724b327c3a9c0a06b343be3854d2c0d8c4c34；C0009目录仅有原INVOCATION（blob bd7a136363c310e95b1e41cf951dd341ed8e5f19）。报告/Return目标尚不存在。仅本Run获准路径写入，不覆盖INVOC或其他Run。

下一步：冻结本地产物索引，按当前head逐文件条件发布并exact回读；先报告、后C0009/D005零W Return（REPORTED_COMPLETE，remaining_scope_ref=null），之后交controller实际回收、原Manager消费并单独安排S06。S06～S09未执行。
