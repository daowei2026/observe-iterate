# W008材料需求与本地选择

采用dc18a版control/02步骤0～7与原E1 C0017计划；预期EV-WALL-CURRENT-WORKING-v0.1只为WORKING，未冻结。以下落实已签W，不作专业必要性最终接受。

| 父问题 | 必需 | 有条件需要 | 可选建议 | 暂不准备 |
|---|---|---|---|---|
| Q-WALL-IDENTITY-LIFECYCLE | fresh live source/工具/输入绑定；最小Start→合法更新→End真实值 | active map或等价state；跨firing duplicate与after-End | 自然current样本 | 旧九场景整包、Dormant/restore新增fixture |
| Q-WALL-PUBLICATION-STATE | 输入与O/C角色、End shape、reader路径 | 同次两更新last C、A删除；既有diagnostic精确constructor | 现成可读图 | 新dedicated target、完整production多产品重算 |
| Q-WALL-BUSINESS-SUITABILITY | code/data/params/calendar/object/time资格与转换损失 | 至多两个现成高区分表达式低成本执行 | 自然数据、现成Notebook/CAEGraph视图 | 全年扫描/重算、为作图强制构建图、未准源码改动 |

本地选择：现有P1模块applyWallOccurrenceBatch直接编译自live BASE，现成GHC9.4.8 tinfo6和既有installed package DB只读复用；仅新增本W观察脚本与本W build/temp/export。复用existing test wallStart和两个已存在表达式；未新增Cabal target或独立源码树。normal为3个受控调用/4条typed输入，同次2条非平凡合法BandUpdate。场景总计2：cross-firing exact duplicate Start，after-End update（setup缩为Start/BandUpdate/End，省去Dormant/restore）。

观察方法：完整typed输入/O、实际返回state的既有derived Show；精确抽取wallViews和wallCurrentUpdateBatch，不引入生产accessor；当前ToBSON/FromBSON独立读回尝试。纯数据足以本轮取材，不强制图像。每份标static/controlled/synthetic/natural，不把Show/debug state等同FRP committed event或nativeDBA物化。失败只限制对应项，其他独立取材继续。

未运行WallAssembler行情计算；rb/SHFE-night为现有test的符号/日历label，UTI10/11/12/14为人工轴，未加载真实日历或epoch，未取得当前production FeatureRunIdentity。自然数据不是本W本轮必需，故不扩大到行情目录搜索。原生DBA完整reader和D事件是否取得见最终review，不能以typed/BSON材料代替其运行证明。
