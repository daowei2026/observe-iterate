# S04 研究重放及文件解释

没有重跑 S01～S03 或任何生产特征。`select_b1.py` 只对白名单内的 S03 发现部分量/前序字段匹配，代码不读取 post 字段进行选样。四次真实口径记录保留在 selection/：v1、v2（同昼夜）、wall_diagnostic（放开依赖仍为0）、wall_relaxed（较宽条件的补救组）；后期观察前合并冻结 ANALYSIS_GROUPS_FROZEN.json。标准402配对、Wall补救147配对是特定区间及多次复用人口，不是独立过程数或市场频率。

实际执行顺序为 `select_b1.py`、其余三个 variant、合并冻结、`extract_b1.py`、`plot_b1.py`、`summarize_b1.py`、`verify_b1.py`、`write_casebook.py`。初次合并冻结命令已保存为 freeze_b1.py，当前冻结原件不覆盖；不得看后期后再改口径来提高结果。五组标准对照、一个放宽 Wall 组质量不同，不能称六组等质量攻击背景已匹配。

重放可把本目录的 .py 文件复制到 **同 calls 父目录下的独立本地研究输出目录**（例如 LOCAL_REPLAY_S04/research），并明确它只是研究重放目录，不是新 C/角色/Run。S02/S03 输入仍读同父目录的 C0002/C0005；不要在本 C 已完成输出上反复覆盖。进入重放目录依次执行：

```bash
python research/select_b1.py
python research/select_b1.py --variant v2
python research/select_b1.py --variant wall_diagnostic
python research/select_b1.py --variant wall_relaxed
python research/freeze_b1.py
python research/extract_b1.py
python research/summarize_b1.py
# plot_b1.py 使用本 C 独立 plot-env 中的 Matplotlib，确切依赖见 PLOT_REQUIREMENTS.txt
../C0007/research/plot-env/bin/python research/plot_b1.py
python research/verify_b1.py
python research/write_casebook.py
```

需要源数据、同批 S02/S03 冻结输入和 NotoSansCJK-Medium 字体；根位置由脚本自身位置确定。记录时间与 PDF 元数据随重放改变，候选ID、原始量、匹配口径和后期观察应一致。plot-env 是本 C 独立绘图运行依赖，不加入正式研究产物索引；无生产环境/参数/代码写入。

CASE_METRICS 是原始度量与来源状态；QUOTE_TRACE 每行带原资产/CSV行，量变区间外累计列留空；同价位不在最优档时 q_at_tracked_price 留空，不推断深档存量。P1_CONTEXT 保存实际原始属性，`measurement_time_overlap` 只判断时间，Wall 价带匹配另列；其他产品不可因同侧时间近就当 exact 对象关系。0行的 `no_rows` 只表示当前展示选取未见行。

后期从 t1 之后开始，ask向上、bid向下。中间价位移单位为观察格点，最大推进/退离含起点0；不足固定窗不填0。离档指最优价向攻击方向越过观测价，同价复见不证明相同订单/Wall；`last_trade_cross_with_positive_raw_volume_s` 只反映半秒汇总字段，不能恢复逐笔时序。原总成交的真实方向、合约单位、producer参数及完整正式历史未确认。

图中量变段放大并标注末点，避免 step 图的末端跳变落在坐标边界难见；主图保留前后背景及可见性断开。每组 PNG、PDF 均由真实 CSV 绘制。图表是本批回顾研究，展示段结束或 Attack business_end 不表示该时点正式已发布。图和数值在本 C 已逐组检查，S04 不代替 S05/B2、S06/B3 或第二轮验证。
