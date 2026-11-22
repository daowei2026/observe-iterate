# D012 / C0027｜真实图、正式图数据与材料交付

原E1同线程按原caegraph-execution Skill连续完成E1—E6，材料状态 **DATA_READY**。实际执行了两次只读CAEGraph运行，最终图经D/C2-v4核对接受后才形成E4准入；21份正式CDS构图快照已取得，E5逐列/值与接受图一致。workers=[]。

最终可打开HTML：`/dwdhome/fy/BASE_E6_2_copy/artifacts/OI-F800-STAT-20261122-01/caegraph-E/f800.html`；SHA-256 `df4076f642d4d2b2ac7a6f8cc02899d9cf70e20dd8beb313e347e7545279b450`。记录分支无损封装为 `html/f800.html.gz`，解压字节和原HTML相同。完整最终脚本在 `final_script/`，入口 `run_definition.py`，包文件哈希见 `FINAL_SCRIPT_MANIFEST.json`；实际命令/PID/起止/退出码见 `RUN_ATTEMPT02.json`，实际日志保留。无需新生产或重跑G。

原D011入口首跑退出0，生成真实三年图；E3实际打开后发现全范围2072个时间刻度形成黑带。依C2已允许的标签频率变化和原E工程权限，在run-local副本只抽稀可见原时间刻度，随共享视窗更新；原120m标签值、实例/B位置/字段/源/CDS/业务图元均未改。第二次运行退出0，全范围每轴10个刻度，局部缩放仍沿原标签。21个CDS全量数据哈希与首跑完全相同。diff、首版原HTML压缩档和截图均保留；未改共享uplot、Feature或受保护平台。一次准备脚本的括号错误在执行任何修改前被解释器拒绝，修正记录保留，不伪称Feature失败。

亲自检查真实全图、局部、下拉/点选后的exact明细及实际hover；浏览器错误/警告和外部请求均为空。5图依次为三品种独立原价、上游selected-known、全局exact修订，阅读路径与唯一C2-v4保持。真实鼠标Tap与下拉/明细联动通过；hover启用后显示Life/Revision、完整父键、known及各独立状态/窗口。截图和模型证据见 `E3_ACCEPTANCE.json`，原C2只作预期，不冒充真实结果。

| 图层或数据 | 本次行数及计数单位 | 分母与解释 |
|---|---:|---|
| 原价K线 | rb/hc/i各49683行 | 各品种完整B位置5m K线行；各69个close NaN保留，不补零 |
| Rct实际投影 | rb7538 / hc7478 / i10738行 | 上游公开更新投影行，同一actual可多次出现；不是唯一原始转折分母 |
| 已选T、C、selected-known | 每层rb425 / hc430 / i1004行 | 同一公开选中记录分别在三个位置表达，不跨图层相加计对象 |
| exact修订发布点 | 1538行 | 完整父坐标对应的组观点发行视图；286个known位置含多个观点，均分行保留 |
| a→d携带窗口 | 1538条显示段 | 原观点携带界限按视区裁剪，不是持续状态/coverage |
| d→r携带窗口 | 1537条显示段 | 1条整个tail在视区外；原始端点仍在exact raw中，E5逐段核同 |

E3逐行核1538组UUID无损、父键唯一、known=点x；26种原生子表所有32553行及22646个“组×子表”空列表保留，4种definitions族原值进入元数据。空列表不等于0或失败。两次日志中两个空可选分支物理列的FileNotFoundError提示原样保留，公开31表检查通过，不补算缺源。

正式取数严格晚于E3接受。直接从被接受HTML内嵌的**同次Bokeh CDS**读取21个源，阶段明确为 `construction_snapshot`，没有重新构图、重跑Feature、从截图反推或把候选调试表升格。`FORMAL_GRAPH_DATA.json`给出图层/renderer→文件→阶段→列/行数/单位/哈希最小映射。正式JSON gzip以`$float`保留NaN/±Inf，原始身份JSON保持文字。E5对全部正式文件读回核列、行、值及浏览器模型身份，并核携带段裁剪；均一致。本图无动态标准化，fit_y/刻度只改轴，本轮不需另取viewport_final。

原U PARTIAL/未暴露内部轨迹、三年总览密度、Rct更新行口径、既有明细替代拓扑、Q边界以及四问题/七candidate-only均明确传递。原C3页内标题仍含“C2当前展示预期”，真实绑定在caption和文档title明确；未无痕改原C。`f800.runtime.json`是构图当时、E3/E5之前的原始记录，后续专业状态以E3/E5及材料包为准。

Owner连续状态：D001已接收；X/G沿D00839f有效新生产与完整统计成果复用，历史正式producer/native进程已结束；当前结果目录见原 `FeatureRunResultBinding.json`。本D实际运行的是只读F/CAEGraph Python进程，均已退出0，未启动新的正式生产进程。G的PASS_TO_SCENARIO_REVIEW和已关闭finding不改；本E无阻断。

专业结果先发布，再单独发布原V2 C0027 Return回原manager。仅本D/原E材料准备完成；未冻结场景预期、未签FeatureReleaseGate/ReleasePackage，不运行或释放Q/V、不改WALL，父Run仍待原manager继续。
