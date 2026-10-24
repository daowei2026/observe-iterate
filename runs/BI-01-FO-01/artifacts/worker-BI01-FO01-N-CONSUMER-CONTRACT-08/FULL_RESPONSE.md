# Worker08｜真实消费合同、非N兼容性与最小宿主调查

```text
work_id: BI-01
run_id: BI-01-FO-01
order_id: BI01-FO01-N-CONSUMER-CONTRACT-08
issuer_invocation_id: BI01-FO-01-R0027-20261024T111104Z-872350d4
issuer_assignment_token: BI01-FO-01-N-REASSESS-9e700882a7504150b7cdae5c3f84b3ec
return_to: chatgpt:细节叙事生成_金标:BI01-FO01-执行
```

## 1. 本次结论及资格

本单 A/B/C 调查和隔离验证已完成。最重要的新结果是：**cbd 对普通非N页面也改变了真实持久参数合同；旧恢复者拒绝新增空N字段的风险已复现，不能再仅列为待证。** 即使调用端完全不传该键，框架仍把声明中的默认空值展开进 `fason`。把 `_chart_params_from_run_brief` 改为仅在N时返回该键，单独这样做不足以修复跨版本兼容。

活动 Trier 的一个既有共享类节点6126经正常只读接口返回应用成功，实际展开的是不含新N字段的旧16键合同。该实例属于历史fixed_input，只用于观察活动类的恢复/展开合同，不认证它的图形，也不把它当作普通Feature非N页面成功。再对已有N节点6129作一次同接口的纯参数恢复对照，当前活动Trier确实拒绝 `normal_node_behavior_manifest`。因此 cbd 写入合同与当前 Trier 恢复合同不匹配有当前直接证据，非仅由磁盘版本推断。不能由此宣称所有普通平台页面已失败，本单也没有创建携带cbd参数的新普通平台节点。

独立具名 `BaseCAEFao` 是真实受支持宿主，不需要另建绘图库。隔离构造/序列化/正常恢复已成功；但额外验证还查实，**进程类注册与eval命名空间是两件事**：先初始化原 `EvalCtx`，随后才声明新类时，虽然 `StraApp` 已认识它，正常恢复仍报 `NameError`。因此“换一个类名就能免部署/免加载接线”不成立。

这使原Pro能够比较两个有证据的有限候选，而不必从N算法或Uplot重新开始。本Worker没有替Pro作最终宿主采用决定；未将本单技术检查当工作3接收或工作4签发。

## 2. 本单权力、输入与现场边界

采用当前完整Task/Binding3f8bb3e42a4b4e46ac623adac37a5aadff51a45e、M26完整决定9862ca3f75151491831b343ba520acbe680f6e42及21dd5971f493a6d724948b84dacb7b200ff43b54的README/00—04。R27完整报告按本次派工所附逐字全文采用，并核准确Git原件：ff66f314619ddfcbba5791c129b73a07370a3267，36117 bytes，SHA256 `19db420da9a67d64c63a529f554dcc6e3adef0ed99d13f88f4e2d1124bdd219f`。原单f52与ff66均为同一Git blob2221f8c7e2df1853e91c175d0eca0df8abbfe189，12714 bytes，SHA256 `1c6a29330f12e28279b48bec85523ebca0194bfbf484e3473c1fe95ff73ea5b5`。

本turn 01a16dd0-0e24-7a62-b139-a67f2caedc27 的实际记录为 danger-full-access、approval never、xhigh，已实际ignored读写/读回/check-ignore，Goal为空。没有借旧W07权限自动部署。本轮只写本Worker08 artifact及ignored取证，正常快进保留并行成果；未操作主控detached checkout、Task/Binding/地图/Intake、共享配置或认证。

固定W07的FULL_RESPONSE、SOURCES、PLATFORM_BLOCKER、API_RESULTS、PERSISTED_CAE_READBACK及环境/必要脚本按9aa0fe91e4c37a4d983ebd62aea0b5c45755206a复用；W06/P20/M21所列画法与限制继续作为输入，不重画或重做其消费。未新实例化/计算N，未fresh整批OnlyRead，未重跑三API或重新定位。W07原三run、四个节点6128—6131及正式包不改。

## 3. A：真正消费端、磁盘和新进程分别查到了什么

### 活动进程与正常入口

fresh `/proc` 元数据分别定位到正常 `insights.trier` 与 `insights.trier.server.bokeh` 两个活动进程，均使用 `/m3c3/Linux/apps/anaconda3/bin/python3.10`、工作目录 `/dwdhome/fy/BASE_E6_2`，启动分别为2026-10-19T14:17:56.310Z和14:18:31.010Z。准确PID及白名单启动环境只留本机ignored。历史PID与当前一致是本次核出的事实，不是开工前的假定。

源码实际链路为：Trier的 `/graph/cae/{id}/report` 在 `_do_cae` 先调用 `CaeNodeDao.node2fao`，再取得显示对象/决定Bokeh页面；Bokeh是另一个进程，在 `create_layout` 中再次由DAO恢复对象后运行layout。两者不能混作一个消费者。原四页错误位于前一恢复阶段，不能用那次失败证明Bokeh也已执行或使用何种类版本。

### 活动Trier的直接证据

先核现有 `/api/fao/{cls_name}/ppdoc` 是只读参数文档接口。实际调用该接口返回500；当前去敏日志把错误准确定位到 `insights/trier/web/api/fao.py:26/get_ppdoc`，缺少的是文档对象的 `render` 属性，不是新的N字段失败。因此没有用其空结果声称读到了活动参数表。

随后沿现成只读DAO限定选择一个不含新N字段的既有共享类实例，再调用正常 `/api/graph/fao/{node_id}/doc`。该实现只恢复Fao并展开 `fason/ppjson`，不执行run/layout或写节点。最终选择最新符合该条件的实例 **6126**，HTTP200且应用code2000；由活动Trier实际返回的展开fason包含：

`run_dir/run_id/big_node_id/fixed_input_manifest/context/calendar_name/blk/display_blks/evidence_features/k_alpha/fig_width_big/fig_width_mid/fig_width_small/fig_height_big/fig_height_mid/fig_height_small`。

这16键与隔离8a基线一致，**没有** `normal_node_behavior_manifest`。同一响应的ppjson也具有相同键集。它是活动服务产生的参数展开，不是新子进程导入磁盘文件的推断。进一步辨认发现该实例的fixed_input_manifest非空，属于旧演示；因此只作为共享类合同的观测载体，不恢复旧图资格，不据此说普通Feature非N页已验证。安全观察、这一限定和响应hash见 `ACTIVE_TRIER_FASON_OBSERVATION.json`；原响应/地址仅在ignored。

随后只对已有N节点 **6129** 调用一次同一纯参数恢复接口，HTTP200但应用code3000，准确拒绝类为 `AidataBigWorldReviewCAE`、未知参数为 `normal_node_behavior_manifest`；响应SHA256为 `dcb0d3a68290d386e15562cce0077551f0d9a85ad7d58512894a52e95ef0a40d`。见 `ACTIVE_TRIER_N_RECOVERY.json` 的实际时点、调用范围和结果。这是与6126展开正对照相配的**当前活动恢复合同**证据；没有打开report、执行layout或进入Bokeh，也没有修改任何节点。只取这一次元数据对照，不重放W07四页500或以失败数计验收。

初筛时旧实例889的正常接口返回应用code3000，未知字段是 `bigscale_freq`。这是另一份历史参数合同与当前消费者的不匹配，不能归因于cbd或当作N空字段复现。未修改或修复该历史节点。后续改为最新符合选择条件的共享类实例取得上述成功正对照，未把HTTP200误当应用成功。

### 磁盘和不可直接观察部分

当前共享aidata磁盘HEAD为f58ea95c358b9ac31659c92b7bc20fe9bf7f8264；其big_world_chart与8a基线同blob1984f17ff2158cd0ff0ca759920bb89228c60ceb，声明没有N字段。本单独立构图候选工作树仍cbd0a1f9bf92d9d65e0ad00bfd1a9e3afb7c2cf0，对应blob531ce6034a382374763866012c0556894f8646e7。两工作树均只读，未修改。

已有正常接口没有返回活动类的 `__file__`、内存字节码、完整sys.path或Bokeh进程的参数声明。ppdoc失败后已取得Trier当前展开/拒绝的直接合同证据，但仍**不能唯一判定**旧常驻代码、另一导入目录、声明/命名空间缓存或Trier/Bokeh采用分离各占多少原因。磁盘旧声明、活动Trier旧16键与当前对6129新增字段的拒绝、cbd写入17键共同闭合“有效消费合同不匹配”；不把一个磁盘HEAD充作两个进程的真实模块版本。

若要进一步取得活动模块来源与Bokeh声明，须原服务责任者使用现有获准诊断入口，白名单记录两进程各自的解释器/导入路径、`module.__file__`和代码标识、有效参数键、eval命名空间可见类。没有这种入口时，需要原有权决定安排有界观测或受控启动诊断。本单没有注入代码、远程eval、monkeypatch、reload或重启来取得这些值；也没有重复请求四次旧500。

## 4. B：真实序列化与跨版本恢复

使用实际本机Fao、OptContext、`_chart_params_from_run_brief`、`_params_for_fao`及正常 `CaeNodeDao.node2fao`，分别在独立Python进程加载已核8a与cbd工作树。普通输入是明示的 `NON_MARKET_SERIALIZATION_ONLY/NO_REGISTERED_NODE` 技术对象：合法OptContext和rb上下文、无任何观察Feature，未调用run/layout，未注册/写DAO。N对象只用W07已存在的rb局部run/node/manifest参数形状，不写manifest、不读N全表。

|真实序列化生产者|内存/序列化N键|旧8a恢复者|cbd恢复者|
|---|---|---|---|
|旧8a普通chart参数路径|均无|自身正对照接受|接受，并以自身新声明补入默认空值|
|cbd普通真实chart参数路径|均有，值为空|拒绝该N键|自身正对照接受|
|cbd普通构造时省略N键|内存补入、fason仍有|拒绝该N键|自身正对照接受|
|cbd普通显式传空|均有|拒绝该N键|自身正对照接受|
|cbd具名N对象|均有、非空manifest|拒绝该N键|自身正对照接受|

后两种普通构造与真实chart路径的序列化字节/hash完全相同。旧恢复的精确错误为 `MQuantException / AidataBigWorldReviewCAE / unknown_parameter=normal_node_behavior_manifest`，发生在实际参数校验；不是语法、模块或伪Fao失败。各自恢复及old→cbd正对照排除了这些替代解释。完整安全最小序列化输入、实际输出和模块文件hash见 `old-restore.json`、`cbd-restore.json`及原serialize记录。

代码依据也闭合：`FaoType.fason`使用`FasonP`，将forceAll=2传给`fasonMode`，而后展开完整P；`_full_params_stru`先从类默认声明补全。因而调用端不传空键也不会让声明中的默认字段消失。旧 `_update_params_stru`严格拒绝不认识的键。本单没有修改这个公共序列化器/校验器。

同一普通技术输入的ppid还从旧 `AidataBigWorldReviewCAE_21b232902032e41b1c4acd63dce64e0343cd6816` 变为cbd的 `AidataBigWorldReviewCAE_fc53e30e4807e4d0afac794672c12beea4ca09a2`；省略/显式空三种cbd构造一致。故公共影响不止分支是否执行，还包括实际持久形状和身份。没有据此宣称已发生全平台缓存故障。

**成立范围：**采用cbd共享类声明的新生产者输出的普通fason，送给旧16键恢复合同会失败；活动Trier现仍展示该16键合同。既有共享类实例6126的恢复/序列化成功，不等于其图形或普通Feature页面已通过；cbd接收旧参数的隔离正对照也成功。本单没有在正常平台创建此新普通节点，不能冒称现场普通页面故障已新增。

最小处理要求不是删N非空字段或放宽所有未知键：若保留共享可选分支，必须解决该类的持久合同/身份与版本混用，或明确且验证完整兼容发布边界；仅条件化返回空键不足。是否采用有界的该类序列化策略及身份迁移，或改用独立宿主，由Pro据本证据选择、管理裁公共采用；未把未验证的修补建议写成已修复。

## 5. C：真实宿主入口及加载条件

现有真实入口是 `BaseCAEFao/CAEFaoMixIn`：默认 `_impl`返回自身，`hold_on_bokeh_server`决定正常Bokeh承载，实例的layout可以直接返回完整Uplot布局。正常DAO `createUniqueWithFao(tar)`存tar.fason并可初始化类节点；`node2fao`从正常持久参数恢复。后两个写动作本单未调用。`TestCAE1`等既有类说明该能力早已存在，不需要虚构scene DSL、任意模块路径加载器或新Host。

本单只在隔离探针进程声明 `Worker08NamedNHostProbe`，参数为原 `run_dir/run_id/big_node_id/context/calendar_name` 五项，layout只委托现有 `normal_node_behavior.render_node`。委托函数实际只消费这五项，再从所属run固定manifest恢复N选择；因此N解释可以留在领域消费者，普通共享类不必为它新增N字段。使用实际rb局部run/node，构造/fason/正常恢复成功。没有执行该layout或新画图，已有W07新进程图元证据按原资格复用。

**不能省略的加载条件：**正常框架 `FaoCacheMeta`会把类放入`StraApp`；但`EvalCtx.json_ctx`是懒加载的`m3sof.settings.json`，其中`mquant.frame.reload.cls`在导入时拷贝当时的类表。追加一项精确隔离对照：先初始化这个正常eval命名空间，再声明同样新类。结果类在StraApp中存在、eval命名空间却不含它，正常node2fao报NameError。见 `NAMED_HOST_PREWARMED.json`。这是真实框架的加载顺序边界，不是合成Python假Fao。

因此新类必须经真实受支持加载路径进入**两个服务各自的类注册和eval命名空间**。可由已验证的启动顺序在快照前加载，或沿现有json设置明确import等正常方式处理；哪一种最小，须看原部署者的真实启动链。不能保证仅在已导入模块增加新类、仅改名、或仅在新进程construct成功就让已有服务认识它；也不能预设必须改所有依赖latest。

本单没有修改aidata源码，故未建立新的aidata分支；两类探针只在本artifact及ignored运行目录，候选未采用。独立宿主不是已经完成的另一套平台实现，尚无公开入口工厂接线、共享服务加载或新节点发布事实。

## 6. 从真实共享基线到两候选的最小变动与权限

先固定已证的文件依赖，不机械cherry-pick一个提交。对本次承重生产文件作定向比较：f58→8a只有N显示helper、N图元配置及registry增加；EvidencePlotter、feature_slicer、contracts、ReadOnlyCsvFeature和原big_world_chart均未因W02—W06改变。8a→cbd才增加共享参数/页面分支、N选择/依赖模块、输入规格和board/delivery钩子等。本次不会把“cbd提交存在”当完整发布组合。

|文件/接口|已有作用与必须带到消费者的内容|两个候选的区别及权限|
|---|---|---|
|u2_normal_node_behavior_display.py、feature_configs/u2_normal_node_behavior.py、feature_configs/__init__.py|W06已认可领域读取/显示视图、布局/单位/状态与配置关联，来自8a|复用真实版本及有效依赖；aidata有权分支可准备，不改N方法或Uplot源码|
|normal_node_behavior.py|cbd的锁定选择恢复、既有布局委托、同node正式依赖补充|可以保留其有用部分，非永久唯一目录/通用解析框架；aidata候选验证可做，公共采用未批准|
|big_world_chart.py、声明及图页工厂|正常公开入口、冻结node、CAE选择、跳过不适用overview|共享方案需解决普通fason/身份影响；独立方案需新的具名类及N专用工厂选择，原普通类保持16键。均不能只写未消费字段|
|run_brief_spec.py、boardrun.py|声明N选择、保存参数和同core交付|两方案都需把真实K/Life/原件/范围送到所选消费者，不能依赖Notebook内存；按所选方案定向收敛|
|timespan_builder.py|原UTI和经绑定Calendar核得的自然时间可同时保留|不是业务重采样或N参数变化；如继续使用该既有能力，保留定向修复，不重定位原四node|
|delivery.py及原表补充钩子|node时间切片之外保留K所引用较早原表|两方案均保持正式源/图用视图分离、原坐标与空值；已有W07包可复用，不重导整包|
|正常类注册/eval命名空间、Trier/Bokeh版本采用|真正恢复/运行者需认识对应类、参数和依赖|原共享配置/部署/服务责任者的写面，本单不写、不reload/restart。独立类也不能绕过|
|原四CAE6128—6131|已存共享类名和非空N参数，原run/node身份保持|共享兼容消费者有条件可沿原id恢复，但未现场验证；独立宿主不能无痕把旧id换类，需管理决定保留旧记录后的正式视图映射/必要新节点或迁移权限。本单不更新、不重注册|

共享uplot HEAD13badc6c及既有dirty仍在；pfw.py实际SHA256为`d8d42b9a27078262d157ece595eb195c29fa6c764a797484520c3e333cb2a2f6`，没有清理/提交/覆盖。当前缓存消费不要求重算FRP或改TIS/workerADT/core/SDK；W07有效运行版本与原生产身份继续分开。本单不认证所有共享dirty行为或未来新版本，后续布局恢复仍需核正常服务自己的真实依赖和文件访问。

**技术上可供Pro取舍的差异：**共享可选分支沿用四个既有持久类/id的代价较低，但当前普通持久合同和ppid变化已经有反证，不能说只影响N。独立具名宿主可将N参数/生命周期隔离于普通类，但需要正常工厂/加载接线，并面对既有四视图映射的真实迁移问题。两者都要原有权发布；本单不把其中之一指定为最终业务方案，不为抽象美观扩成通用多面板框架。

**未来时间视图的实际差异：**当前两个候选都委托同一个 `render_node→bundle_for_node→build_selected_cut_bundle`，仍是manual big、单K切面。独立类名并不自动获得演变能力，也没有本次新验证的连续发生/新K认可。后续时间视图应由领域消费者接入相应真实数据与已验证画法；共享路线继续增加公共参数会再次牵涉普通合同，若把领域选择留在原manifest则并非必然每次扩声明。独立宿主的已证优势是隔离普通类合同，不是已经画通未来功能。本单不实施这些后续扩展。

## 7. 验证、失败和未执行

实际探针/输入输出随包；`CHECK_RESULTS.json`只核这些观测的完整性和正反对照关系。B没有Feature计算、layout、DAO写入；C没有实际画图/新平台；A只用已有只读入口和活动/proc元数据，未读取进程内存或注入调试器。W07已有正式数据、模型、三API、同节点原表直接复用，没有重验370件或再画五图。

可恢复的承重源码位置如下；aidata定位采用cbd固定版本，框架/服务文件采用 `SOURCE_INVENTORY.json` 所列本次有效磁盘hash，不冒称活动模块来源：`big_world_chart.py:125/528/1578`（声明、过滤、真实chart参数路径）；`mquant/frame/lang/internal/base.py:367/902/1264/1388`（完整fason、补默认、拒绝未知键）；`mquant/quant/models/graph/dao/fao.py:184`（正常恢复）；`mquant/frame/lang/cae.py:45/67`（显示对象和BaseCAEFao）；`mquant/frame/core/app/env.py:131/171`、`mquant/frame/reload/cls.py:7`、`mquant/frame/core/base/json.py:79/147`（类表及eval快照）；`insights/trier/web/view/graph/view.py:15`、`insights/trier/server/bokeh.py:34`、`insights/trier/web/api/graph/fao.py:59`（前后两恢复者及只读文档入口）。探针保留了实际调用而非替代实现。

普通相连错误已修通：初次读取`cls.cls_params`时元类尚未初始化，返回None；改为正常默认实例.P取得完整声明。现有ppdoc接口因缺render返回500，转而使用既有共享类实例的只读doc取得实际fason。第一次旧实例889不兼容bigscale_freq，改限定选最新满足选择条件的实例6126；并明确它的历史fixed_input性质。所有这些错误各按实际来源留证，没有把它们当市场Pending或停在首错。

正常服务类文件/字节码与Bokeh声明仍有上述观测限制；原四个report页面在本单没有重开，只有6129的纯参数恢复得到当前字段拒绝。真实N前端/图层的最后记录仍为W07，不能把这次元数据错误说成当前浏览器500截图或已运行布局。当前调查不修公共服务/认证，不关闭原日志事件，也不复述敏感值。本单未输出或交付新的认证值；库日志抑制并隔离ignored，只运输安全字段及必要技术序列化，正常服务自身历史日志事件仍归原责任者处理。

## 8. 返回原Pro的后继与停止

原Pro现可据A/B/C作有边界宿主选择：保留领域读取/显示与正式数据，明确共享普通合同如何处理，或选独立正常宿主并交加载/视图映射差异。管理处理公共采用、原认可影响、共享配置/部署和原责任者；不让Owner在未经分析名词中再选一次。需要补活动来源时给本节已经具名的有界取证项，而不是再签一次“只有参数错误，请部署”的重复单。

采用方案并经有权方完成真实正常服务接线后，再对原认可范围核实际图层/单位/时间/状态及同node正式数据；具名可靠成果回Pro判断后申请管理接收。正式工作4仍未签发。本Worker不自签工作3接收、平台恢复或最终方案，不操作手机/主控Goal/调度，不常驻等待下一单。

本单GitHub交付和fresh回读后自然结束。A中不可得的活动__file__/Bokeh类信息明确列为限制而非编造；B风险已从待证收敛为条件性兼容失败；C提供真实入口、命名空间边界和最小修改/权限差异。完整观察任务继续由原Pro/管理承担，Worker08完成不等整体任务完成。
