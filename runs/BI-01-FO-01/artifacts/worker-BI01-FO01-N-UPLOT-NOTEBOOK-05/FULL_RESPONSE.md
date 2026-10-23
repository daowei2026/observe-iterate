# Worker05｜工作2真实 Uplot Notebook 执行与交互技术回交

order_id: BI01-FO01-N-UPLOT-NOTEBOOK-05

work_id: BI-01

run_id: BI-01-FO-01

issuer_invocation_id: BI01-FO-01-R0014-20261023T153303Z-57f340f3

return_to: chatgpt:细节叙事生成_金标:BI01-FO01-执行

## 1. 结果与资格

本单从 P11 的真实 Notebook 候选修订，已在现场 JupyterLab 的新 m3py310 kernel 实际 Restart → Run All，六个代码单元完成并生成本次 Uplot/CAEGraph 新图。没有加载旧 HTML/PNG。主交付是同目录 `N_observation_Worker05.ipynb` 与实际消费的 `DISPLAY_PLAN.json`；图用 CSV、kernel renderer 和实际浏览器 CDS 是对应技术证据。

最终同会话实际通过 rb 三K/同exact不同范围、i三拍、hover、滚轮缩放、平移、复位和图例隐藏/恢复。独立技术核验693项、0失败，详见 `evidence/FRONTEND_EVENTS.json`、其真实动作子集 `FRONTEND_INTERACTION_EVENTS.json` 及 `TECHNICAL_VERIFICATION.json`。所有最终浏览器快照均核到当前 execution，不混用旧运行。

这份回交是工作2的现场工程结果。原执行 Pro 的本人消费/专业判断、具名工作2管理接收尚未由 Worker 代签。没有用当前候选调用平台三个入口、注册 CAE 平台节点、生成 board 正式交付或开展正式工作4。旧 Worker04 混合单没有恢复。本单没有操作手机、Root Goal、计时器或自动恢复机制。

## 2. 权力、原件与本次输入

- 当前 Task/Binding：observe-iterate@`f6f07531184c97ccbd7a7df34275046407de2e16` 的 `runs/BI-01-FO-01/01_当前任务.md` 全文；管理 M13@`2549c3bc3838024f6dae5ab0c3a1ef0b9f2aff2e` 完整决定及其 worker-disposition/next-professional；地图@`bb8818fd750472dc57f1acdd7615988682cd9d31`。
- 方法：`b81cfa14299a415bd4b666f9f69cdc4f5871931f` 的 professional/feature_observation README 与 00—04；本单按 Worker 的技术边界使用。
- 唯一工单：`0396aff17efc3fd7d1f955f6b05a26a2d0416c43:runs/BI-01-FO-01/artifacts/professional-R0014/WORKER_ORDER.md`；实际 SHA256 `1730c156996980ca664a0705f8aad20a70e5bb9724afd637f601cdb8821a7d30` 与投递原文一致。R14 完整报告取 `76a912dada353fbb7b3cdbd6d2dd8dc2dcd1ec3f`。
- P11 原 Notebook/配置/报告固定 `a2c9f9333c6578b8bf1dd26fb589b1a6b2956ae9`；Notebook blob `cad0e3fb1cc9dbccd113410676bb2bddf55c33ce`。原失败文件未修改，新副本保留原单元 id 作为代码谱系，当前标题/metadata/执行身份另记 Worker05。原件哈希见 `evidence/CANDIDATE_PROVENANCE.json`。
- 正式数据核源复用：W02@`081e31241a0c88e47631f80a8b9b8dd43b2b569c` 的 rb 三个 selected cuts 与同绑定行情、i 缺价行情；W03@`d04f3b08892ccf334a06028f3caab994743566a0` 的 i 三拍、hc 末拍原表/intervals/行情。实际读取 130 个不可变 Git 文件，逐文件 SHA256 见 `evidence/SOURCE_READS.json`。未以旧 plot_view_data 作正式输入，未新调用生产 N、未整批重读或重生成历史。

生产实例仍是原 R30 的 rb/hc/i、5m、night_end_at_2300、TA_updto20240229_DBA、MedianTwoWindowV1、N6/LOO3、normalization=null、compact_history=true/core.v2。本单没有重新实例化它，不按摘要重造完整 sources，也不声称保存目录本次已 fresh 可读。原生成程序身份继续沿原正式记录，后继读者不倒记为生成程序。

## 3. 实际环境与最小源码修改

开工实际 turn_context 证实 danger-full-access、approval never、effort xhigh；并在 cgpterm ignored artifacts 实际创建、读回文件，`git check-ignore` 命中。线程仍为 `01a12557-eb30-74b3-b394-99c45b97c2b9`，Goal 为空。见 `evidence/RUNTIME_PERMISSION_CHECK.json`。

|对象|本次实际情况|
|---|---|
|Python/kernel|`/m3c3/Linux/apps/anaconda3/bin/python`，Python 3.10.13，现有 m3py310 kernelspec；未升级共享依赖|
|前端|现有 JupyterLab 4.4.6、ipywidgets 8.1.2、Bokeh 3.6.0；Playwright 驱动真实 Chromium 前端|
|aidata 原共享工作树|f58ea95c，codex/aidata-named-csv-features-20261019，开工 clean，未写入|
|本单 aidata 工作树|`/dwdhome/fy/BASE_E6_2/mquant/aidata-bi01-fo01-n-work2-r0014`；新独立 `fy/bi01-fo01-n-work2-r0014`，base b044ad9 → 7d4c48a → 最终 e8aaa464e30259c84dac47260104c5acda1eac5b；已 fresh 回读|
|Uplot|实际 13badc6c；pfw.py 修改及两个未跟踪项开工已见，未覆盖/提交；有效文件和 diff 哈希记录于 ENVIRONMENT。手册参考另为 0a4fcd54|
|TIS|实际 overlay 的 checkout HEAD 为 f26495c，不能称 clean 锁定在 3ff34c72。两份有效 N 读者经 GitHub 精确 3ff34c72 fresh 取回逐字比对，SHA256 均一致；本次数据入口仍是已交正式导出|
|worker ADT|只读 overlay 指向 cd5c307d；FRP 方法来源仍 5154c407，本单没有调用 Haskell 生产者|

实际导入文件/哈希、工作树状态见 `evidence/EXECUTION_RUNTIME.json` 与 `evidence/ENVIRONMENT.json`。Notebook 使用已存在的只读运行 overlay，并仅把 aidata 解析到本单独立工作树；没有修改 TIS/FRP/workerADT/core/SDK/uplot 源码。

aidata 仅修改三个文件：

1. `feature_configs/u2_normal_node_behavior.py`：保留 N 图层和品种色，增加可选的局部等待/正式间隔中位数 CalendarUTITick 附图及具名原 close/high 点；实际显示配置版本 0.2.2-worker05。单切点附图改为 220px，以容纳标题/图例/K 和真实数值区域。
2. `u2_normal_node_behavior_display.py`：按原保存坐标投影 waiting 和原 rhythm.current_median；显示缺件状态、局部重启与缺 last_update；具名价格标记逐点核原价；修 JSON 导出对 Timestamp/nullable/UInt64 的处理；用正常 `nb_fig_time_range=False` 关闭嵌入 Notebook 中不使用的 Python 视口记录回调；保持 JS 原生交互及分轴。没有复制 N 算法、创建生产 Feature 或公共发布设施。
3. `tests/test_u2_normal_node_behavior_display.py`：针对真零/缺分母、原 close/high、拒绝未来数据及 UInt64/null 导出增加必要检查，更新 N 配置版本断言。

本次场景配置版本是 `DISPLAY_PLAN.json` 的 0.3.1-worker05，与 aidata 图元配置版本不同。按 R14 删除了 platform_acceptance 和当前 pending 列表的平台/board 项，替换 Notebook r0011-09 的旧下游完成条款，保留真实数据/场景语义；实际 Notebook 读取本目录新配置。原配置中的保留要求用于核展示，实际完成/未完以本次证据和本回交为准。

## 4. 已形成的真实画法与范围

### rb：两个完成窗、当前 working、知识切点与范围

Node Life `b340dc6c-c135-462b-b6e0-04d24622c180`；K 为 103150800、103151400、103315800。稀疏比较页只画实际取得的点，清空保持/steps，不宣称连续433发生。选定 K 控件实际重建当时合法成员及 working，末拍可切换完整已供成员/行情与确认附近局部行情；显示范围不改生产参数。

原 OHLC 为淡背景，close 为计算路径；实际端点和确认点保持不同形状，端点连线不冒充路径；不按视觉斜率改源 direction。两窗效率与 working 推进/逆向量/前缀效率分图，原方向和 completion 尚未完成（原码2）同时保留。末拍正式标量包括近期效率约0.151417、此前约0.084543、推进50、逆向量80、前缀效率约0.037764；技术核验以原精确值和实际 renderer 为准。

完整/局部视图可能具有相同最终 exact，但必须取得不同显示范围和实际文档身份；本次实际进行前后切换。K 后无行情/特征记录，横轴显示留白不算未来数据。局部范围省去的远端成员原价不伪造，完整范围仍可回看已供十二成员；这不证明所有历史和修订均已覆盖。

正常 Uplot KPriceLine 将原 K 线画在 bar 中心：本实例末根背景蜡烛的 x=原open_uti+300。这个中心是显示几何，不是新增知识时间或K后行情；原close路径与N标量仍在原UTI。技术核验逐根比较原输入、标签/OHLC、原open_uti≤K及正常中点计算，没有通过移动业务K或放入未来bar来过图。这项显示约定保留供Pro理解，而不是实时开盘已知认证。

### i：可用端点量、真零与缺路径量

Node Life `9410abda-b111-442d-aa25-6b99da2afeb6`；K 为35360400、35361000、35361600，同一 working Life `5727e951-20b6-4a82-8c52-fc3a32f686cc`。图上分别显示可用推进/年龄，效率/逆向量缺件与等待倍数缺分母；不填零。

恢复拍推进12、年龄42000、waiting=0；local_start35361000、local_count0、last_update缺，明确为局部重启，非新极值信号。下一拍推进9.5、年龄42600、waiting600，路径效率、逆向量及 ratio 仍按原状态缺失。稀疏比较不补造期间保持；原价 NaN 缺口保留断线。已有行情上下文不等于整个 working 完整路径或原起点价已取得。

### hc：close 极值、影线与正式等待基准

Node Life `6f92034c-bd94-4d3f-8b7c-6c69e24959ff`，K103315800，exact 修订 `76d5cfc3-f505-4b62-89b8-b081aedb90f0`。新图明确标原 last_update103057800 对应 close3952、下一根 close3946/high3959，以及末拍 close3904。三角形 high 标记不解释成 close 极值更新。

waiting258000 与原近期三间隔中位数600分别显示于 CalendarUTITick 附图；ratio430 用独立 ratio 轴，不截[0,1]。分母直接取正式 rhythm/intervals，原三间隔2400/600/600；原 Notebook 参考算术仍单独标识，不当成新生产结果。已供454行覆盖当前 working 相关行情，不冒称所有完成成员的更早原价均在此范围。

## 5. 执行、交互和定向技术核验

主操作是 JupyterLab 前端真实菜单 Restart Kernel and Run All Cells；六个代码单元均实际执行。当前执行 id 和完成标记见 `evidence/EXECUTION_RUNTIME.json`、`evidence/KERNEL_COMPLETION.json`；正常 show 接收的是本次新 CAEGraph.layout()，没有 iframe/旧 HTML/PNG 载入。

rb 的 before → confirmation → final，以及 final 的完整/局部/完整范围，通过真实 HTML select/ipywidgets 通信生成新前端 root 并分别保存实际 Bokeh CDS。为了避免核验器误取尚未替换的旧 root，切换核验明确等待本次新 root，且要求相应视图仍连接在当前 DOM。hover 用实际鼠标命中图元，核末拍 exact/K/状态和图上数值。原生工具实际激活状态、滚轮缩放、拖动、复位及图例操作按最终事件记录，不把设置模型属性当成用户操作。

独立核验脚本按 `origins K → rows → window.address → binding → specs.kind/definition → 对应保存坐标 metrics`，working 标量按本拍 root 取原表；比较原正式字段、实际图用 CSV、Notebook 浏览器 renderer/CDS 的 x/y/exact/K/状态，核缺件无伪零、范围非退化、K 后无记录、hc close/high 原值及稀疏点无插值。没有从新进程孤立重建一个正确 final 来替代已交前端页面。

最终 aidata 测试：64 passed、2 项已有 deprecation warnings，见 `evidence/AIDATA_TESTS.log`。测试数仅表明相应技术覆盖，不能代替画法专业判断、管理接受或全特征正确性证明。

## 6. 实际失败、修通与证据保全

- 首轮停在新增 kernel renderer 审计 JSON 导出：ndarray，随后 Series 不能直接序列化。修审计转换，原失败 Notebook 在 failures/ 保留。
- 图用 manifest 原 helper 遇 Timestamp 序列化失败：在 aidata 定向支持 Timestamp/nullable/NumPy 标量，UInt64 保持整数；保留该失败 Notebook。
- 前端保存 Notebook 时曾读到 Jupyter 尚未写完的 JSON。核验脚本改为等待稳定可解析文件，并要求新的 kernel completion execution_id 与当前 runtime 一致。原日志保留。
- 前端标题存在隐藏 ToC 同名节点；tooltip 内容在 Shadow DOM；重建异步过程曾让核验器匹配旧 root。均修核验定位/新 root 条件，不把这些测试脚本问题归因于生产 N。
- 嵌入输出的 Python 回调警告来自 Uplot 可选 nb_fig_time_range。通过其正常参数关闭不用的视口-to-user_ns 记录，未改受保护源码。JS 图形交互和 ipywidgets 重建另有实际验证。
- 实际像素发现150px附图的数据区域过窄、上沿等待值标签易出框，调整为220px与内侧标签并重新新kernel执行。旧输出在 iterations/ 保留，不用新数据遮盖旧表现。
- i 实际像素又显示推进12和年龄42000的数值标签仍触上沿，因此按实际 panel range 将上沿标签向内放；近期/此前时长分别在点的左右，hc 末拍价格说明向内对齐。修后按最终源码重新新kernel/前端验证，不改变正式数值或知识时间。
- Wheel/Pan 的实际工具状态需要正确使用：缩放需选实际 x 工具，已激活 Pan 再点会关闭。核验脚本按真实状态操作，原失败探针日志保留，未为通过断言更改正式值或业务 K。
- 无未来检查最初把KPriceLine的显示中点当发生时间，出现24项失败；随后依据实际Uplot代码逐bar核源，保留原失败结果。另一次比较将浏览器Float NaN与JSON null当成不相等；最终明确核三拍各24条真实缺价，并将公开JSON的非有限数表示规范为null，原浏览器字节/hash保留在ignored材料。没有改运行CDS、补价或填零，详见 `BROWSER_JSON_NORMALIZATION.json`。

- 核心新kernel同会话交互已通过后，额外尝试只重开缓存HC输出并收起侧栏，未取得live视图而超时；原日志在 `failures/attempt14_reopened_cached_hc_viewport.log`。未把该额外探针当成功，也未因此复跑昂贵正式数据。已验证的打开方式仍是新kernel Run All。
- 打包复核一度误用无pandas的系统默认Python，未进入核验；随后使用本次已验证的conda解释器运行。记录见 `failures/attempt15_packaging_default_python_missing_pandas.md`，未升级共享环境。

截图只在本机 ignored 运行材料中用于 Worker 技术核验；不是本次主看图交付。实际查看的像素、原始图像hash及边缘裁切限制见 `evidence/WORKER_VISUAL_INSPECTION.json`。原 Pro 本人尚未由这些操作被代称为已看新图。

## 7. Notebook 打开和实际访问边界

准确文件是本目录 `N_observation_Worker05.ipynb`，同目录必须有 DISPLAY_PLAN.json。已有 JupyterLab/m3py310 环境已实际打开并执行；实际本机入口、端口及认证材料仅存 cgpterm 的 ignored `artifacts/bi01-worker05-runtime/`，不提交到 GitHub。Notebook 上传不证明 GitHub 能运行 Bokeh JavaScript。

在本机用该环境的 Jupyter 打开文件，选择 m3py310，Restart Kernel → Run All。默认 OBSERVE_REPO 是本实际 observe 工作树；可显式设置 OBSERVE_REPO、BI01_W05_ARTIFACT_DIR 和 BI01_W05_AIDATA 为含锁定 Git 对象、当前配置及本单 aidata 版本的真实路径。运行时 PYTHONPATH/M3ROOT/M3WORKS 使用本次已验证环境，具体启动办法见 README。没有安装/升级共享环境。

当前复现依赖包含 `/tmp/bi01-fo01-w03-runtime-20261022` 的既有只读 overlay 及其 TIS/worker 指向；这些临时路径若在以后被清理，必须先恢复已核有效源码/环境，不可静默换 main。它是本次实际环境限制，不冒称跨机器即插即用。图使用常规1800px宽，窄窗口应收起Jupyter文件侧栏或水平滚动，并非依赖极度放大。重开缓存widget输出不保证连接当前视图，应按实际验证方式重新Run All。前端未向原 Pro 远程转发；本机实际可操作不等于 Pro 本人已打开，也不把临时本机地址当工作3平台链接。

本单的临时Jupyter服务及其kernel已正常关闭；重新操作需按README启动并Run All，没有留下等待后继的常驻服务。生命周期见 `evidence/FINITE_RUNTIME_LIFECYCLE.json`。本次实际总时长由ignored task-status账本记录；没有可靠的分阶段token/未来工时数据，不估造。

## 8. 完整未完和接收关系

本单具名技术范围已实际完成：R11合法副本修订、真实新图/Notebook执行、rb/i/hc已定问题表达、必要交互及当前execution的原表/投影/实际renderer一致性核验。完整专业任务仍有原 Pro 对本次图数和时间/状态表达的本人判断、必要返修；随后具名工作2管理认可及真实后继签发。对应工作3平台三入口、同节点正式数据与其管理接收、正式工作4及完整反例/参数探索/Owner成果不在本单执行，未被取消或提前放行。

当前图覆盖是已供 rb 三知识切点与范围回看、i 三拍部分恢复、hc close/影线/等待问题；未证明完整433发生连续演变、所有未来场景、任意参数或全部修订。没有无前视、收益、全算法正确性、独立审查 PASS 或管理认可主张。Worker 技术结果交原 Pro，由主控按原机制送回；Worker 未自行向手机/外部业务方发送。

## 9. 发布

源码与运行成果各归授权仓库/分支，跨仓不是原子发布。准确提交、清单及 fresh 精确回读见同目录 GITHUB_RECEIPT.json。只提交本单 artifact 路径及本单 aidata 三文件，保留并行成果、原失败与共享 dirty；不 force push。
