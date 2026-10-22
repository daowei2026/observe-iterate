# BI01-FO01-N-DISPLAY-INTEGRATION-02｜配置接入、正常结果入口与时间表达实证

work_id: BI-01  
run_id: BI-01-FO-01  
order_id: BI01-FO01-N-DISPLAY-INTEGRATION-02  
issuer_role: professional  
issuer_ref: chatgpt:细节叙事生成_金标:BI01-FO01-执行  
issuer_invocation_id: BI01-FO-01-R0007-20261022T081903Z-a9efdb6a  
issuer_assignment_token: BI01-FO-01-N-OWNER-CORRECTION-0b65aeb5a3834499a24640864d0f1d3f

<a id="authority"></a>
## 1. 本单解决什么、谁接收

本单由执行Pro实际签发，接收者为本run现有机制真实委派的现场Worker；技术回交返回上述执行Pro。**签发/发布不等于派达、接单或执行。**旧单BI01-FO01-N-AIDATA-01已经结束，不恢复旧单，不复用其静态三图/八CSV为默认要求。

直接权力为当前任务 `observe-iterate@20426e5e88a67d58eaaf168168c5e4f74d73a31b:runs/BI-01-FO-01/01_当前任务.md#technical-work`，管理采用为 `270b8eca008fb20030fc8880355bcb60bb55b958:runs/BI-01-FO-01/reviews/management-R0006/FULL_RESPONSE.md#plan`。专业方法为068fc87的README/00/01/02/04和4d501afa的03，Owner原反馈ea0ace45及原GO9508df不变。

业务目标：让普通投资者能分别看懂“当时最近完成过程怎样”“当前未完成过程怎样”“这个数什么时候已知、何时保持、何时改变”，并在选定知识切点回看真实成员与价格；不能把事后确认的端点或最后一拍窗口回填成当时已知。工作2的重要画法已在具名配置中决定，本单负责真实接入/调用和数据技术核查，不重新决定业务目标、不做完整U2/U3。

<a id="inputs"></a>
## 2. 已有真实输入与配置

专业配置原件：

`daowei2026/observe-iterate@831a5d4398e02ff02abb3892e25030d983f06768:runs/BI-01-FO-01/artifacts/professional-R0007/u2_normal_node_behavior.py`

版本0.2.0。相同提交同目录的verify_r0007.py、CHECK_RESULTS.json保存执行Pro实际完成的28项局部算术/纯配置自检，不是现场框架或图像验收。重要解释及全部未完见本轮FULL_RESPONSE正文，不用自检计数替代业务工作。

原正式实例继续取完整JSON：

`daowei2026/feature-refinement-implementation-agent-evolution@a6f5025e8b082f8f11056e566a2a07abc49bb939:agent_evolution/pilot_cases/network-dynamic-ceps-factory-u2-u3/runs/first-two-fao-20261017/ENGINEER_STORAGE_REDUCTION_R30/ACTUAL_RUN_CONFIGURATION.json`

完整rb/hc/i sources、5m、night_end_at_2300、TA_updto20240229_DBA、N6/LOO3、normalization=null、compact_history=true、core.v2保持；按对象选显示，不删sources换产品身份。不扫描现行正常入口不支持的任意N，不重跑历史生成取代正常读回。

TIS修后读者3ff34c72be8ef025f68e18b097fe7b8f1f472668：frp/U2NodeBehavior.py、U2ThinNode.py；FRP正常构造5154c407249c130a6e048c8541b76dfdec3ea48c。历史生成程序身份继续按R30/R33原记录，不能把后继读者倒记为原生产者。正常结果目录为：

```text
/m3varK/BaseData/futures/TA_updto20240229_DBA/fao/prod/U2NormalNodeBehaviorFrp/9/0/d/3/7/a/4/fb2007d71be1e620801457424d6dea8b4/func
```

已可复用的首例是 `observe-iterate@d7410c70f7f43388946e3c9b7721202be53a24f9:runs/BI-01-FO-01/artifacts/worker-BI01-FO01-N-AIDATA-01/`：rb、As-Of103315800；正常24表、4760行情/Calendar行、旧图与技术记录。Exact为NodeBehaviorBook/NodeScaleTurnBehaviorRevision/b340dc6c-c135-462b-b6e0-04d24622c180/cfd51328-e2cf-4360-8314-20c9238e93fb。已有这份数据，不再报告“完全无数据”；数据身份与图用投影仍分开。

<a id="interface"></a>
## 3. 先在真实版本上核入口，不先判必须CSV

核实际工作树、HEAD、导入路径、dirty状态和运行上下文，先读**现场版本**aidata README。原Worker已实际使用 `/dwdhome/fy/BASE_E6_2/mquant/aidata` 的f58ea95c358b9ac31659c92b7bc20fe9bf7f8264、codex/aidata-named-csv-features-20261019；这不是此刻现场未变的证明。uplot实际导入版本另记。

配置的uplot参考是Owner锁定0a4fcd54059782572a3f7e82fad041121e8c65ad。执行Pro另读取了远端aidata **9ff7ce4929b36945f63b1c9875e59f68141f997a** 的README、feature_configs、feature_slicer.py及evidence_plot.py，以取得具体配置/读取合同；**9ff不是本单指定替换f58的运行基线**，不能用它暗换现场。该参考的已知实际代码关系为：

- feature_configs的注册函数调用configs(feature)，提供df_key、time_binding及plot_binding。
- 普通feature_df可调用to_dfs()[df_key]，不只支持单表；其rerun()默认语义应核实际CalType，不能仅凭函数名断言重算或安全OnlyRead。
- 图用读取优先识别evidence_view_df，否则退到普通Feature读取；它是可以比较的现有衔接点，不是已证N适配完成。
- generic EvidencePlotter把图形放到ctx.figs[-1]，随后调用drive_entity_dynstd；group标签本身不新建附图。不能仅把配置文件登记，就把ratio/CalendarUTITick送入价格标准化或都挤进主图。

因此本单先核现场有没有等价/更合适能力，并实际尝试正常Feature/已有结果入口。允许用有据的最小只读展示衔接处理多表关联、时间选择与几何，不要求先产八份CSV。若正常已有入口已满足，直接复用；若缺少层次，给出具体调用、返回结构、所缺关系和实际最小接法。不能从to_df拒绝、表数24或旧CSV成功推出原生入口必不支持。

明确OnlyRead；正常实例、上下文、product_definition/full_dir对应不符时先恢复原因，不改地址“对上数据”。合理复用正常session、分块及请求内缓存，避免每个图层读全历史。CSV可作真实缓存/运输/导出，保留来源和理由；不为了去CSV重算N、复制N算法或增加通用平台。

<a id="configuration"></a>
## 4. 配置原件的真实消费方式

目标落点确定为 **aidata/feature_configs/u2_normal_node_behavior.py**。configs(feature)返回已选图元的实际绑定；display_config(symbol=..., color=..., mode=...)选择实际模式、默认/可选附图并绑定品种颜色。PANELS/TIME_POLICY/VIEW_RULES是该N配置的业务选择，不是已实现的框架魔法字段。

其中n_display/*是**本配置要求的图用视图名，不是TIS现有正式表名**。由实际入口可用能力从原正式表只读关联/投影；不声称直接N.to_dfs()已含这些key，不把投影发布为新的正式N产品。这些名字是逻辑视图，不要求23份CSV/物理表或重复全量读取；同一请求内共享正常结果。保持原table坐标、对象、binding/window/working地址、Life/revision、spec定义、origin/known/as-of和缺件状态。公共读者无需改写。

实际消费者必须做到：调用配置、绑定稳定品种色、按panel group进入声明的MainFig/SubFig、取得对应视图、渲染并导出实际显示数据。只创建registry条目/内部helper或文件，不算完成。具体绑定结果按本版配置记录；普通接口细节可必要适配并回交差异，不能默默删掉时间语义、附图或状态来取得exit0。

主图以原5m OHLC为淡背景、close为计算路径。只有selected_cut按当时成员叠加previous dotted/recent dashed/working dotdash端点连线，并分别用circle实际端点与diamond确认点；不是全程用末值成员反涂历史。当前默认附图分别为完成效率近期/此前、working净推进/累计逆向量、working前缀效率。时长与节律按问题开启。比率、时长与价格不共用价格y轴，也不对比率/时长做价格动态标准化。

每个品种的全部相关图元用该品种同一颜色；线型、形状及分图区分性质。布局为每品种一套相关图的PerSymFigSet，体现多品种扩展而不把选单/多作为验收任务；raw price不跨品种排强弱。颜色由现场稳定品种palette绑定，不使用旧灰/蓝/红分别表示previous/recent/working。

短标签/图例之外显示对象、当前K或as-known模式、历史close口径、真实覆盖范围、working方向/完成状态、缺件/错误提示。准确原值、六指标/MAD/LOO和身份按需详情，不把全部中间值默认作图或将LOO作重要性排名。没有值的状态要可见，不以空白、零值或未调用Pending混过去。

<a id="temporal"></a>
## 5. 时间及相连数据核查

当前rb末拍只有一个所选N发生，窗口基础保存于2024-02-23 21:05，working基础保存于2024-02-26 21:00。**这不证明此前整段状态从未变化，也不支持用末拍数值补造连续曲线。**

沿正常正式结果取得与当前业务问题有关的真实发生序列或明确知识切点。优先覆盖最后成员actual end103059000、confirmation103151400附近的真实前后发生，以及末拍103315800；具体前一拍用实际origins确定，不假造新的发生。根据实际情况加入相邻完成窗切换或普通稳定段，检查保持与改变，而非只换三个固定日期窗口截图。

正常关联以rows.window→windows.address→binding；rows.working→working_bases.address→同binding；成员及metrics使用所引用窗口自己的保存坐标，working基础/节律与本拍数值各用真实坐标。spec按binding+kind解释，不按数组下标猜名字。exact/read_at_knowledge必须带真实Node Life及原知识UTI，不将latest修订填入较早K。

演变视图中，完成统计以有证据的保持水平段表达，改变在真正可知时点出现；数值相同但成员不同的更新保留点和身份。working只表达已观察前缀的保持/变化，新Life、输入缺口或失败断开；变化段不画成未发生时已预知的斜线。将来修订在实际知道时出现，旧as-known不重写。缺乏时间覆盖时只显示实际点，不用单截面充历史。

selected_cut在K读取当时合法成员与状态，用actual坐标回看价格，并显式标注确认/可知；标量点在所选K表示“此刻状态”，hover另列基础保存时点，不混称首次可知。K之后行情不混进同页；要比较后来的修订另开清楚标明K的视图。现有选择窗口/参数调用或少数具名观察点足够，不必造实时播放器或每拍重算。

读到未成熟、缺价/Clock、合法空、真实零、未调用和失败时分别回交。working completion Pending不能遮掉合法数值；waiting_ratio不截[0,1]；缺价恢复waiting=0不是极值更新。已有rb可靠部分可先形成工具实证；在完整任务内继续按问题处理hc长窗/等待、i效率边界/缺价恢复等有价值线索及普通反例，不设必须几个Case或全部品种齐备的门槛，不重复原72/112全套作完成目标。

<a id="permissions"></a>
## 6. 写权和真实分支

如果实际接入需改aidata，在该仓核实际基线及工作树后**新建独立工作分支**。可用拟名fy/bi01-fo01-n-display-r0007；它当前不是已存在/已检出的事实。若同名存在或现场有他人未完，勿覆盖抢写，按现有机制取得不冲突工作区/分支并记实际base/head。

本单授权该N配置落地、既有读取/图用视图/布局消费者的最小相连接入、必要普通排障及验证；不逐文件请批。不改变其他特征默认业务行为、不迁移配置归属。若必须改变重大公共接口、生产方法、受保护源码或授权边界，给准确源、输入、影响和最小选择交执行Pro/管理，仅停受影响部分。

TIS、FRP、core、SDK只读；uplot参照/调用，不授源码修改权。不在observe-iterate另建绘图库、全历史Episode服务、私有发布/Host/恢复框架。没有必要通用扩展就不扩展。

<a id="return"></a>
## 7. 实际回交与未完

回交本run artifacts下的技术正文和可取得实物：现场aidata/uplot/TIS版本及真实导入路径；配置原版/实际落点/必要差异和提交；正常入口比较的真实调用与结果；所用source/对象/exact/K/完整成员和覆盖；已实际产生的图、对应正式数据及plot_view_data；状态/修订/附图单位与色彩的验证；具体失败和完整未完。

本次新画法的布局、图例、颜色、断线/状态及实际/确认标记需要真实渲染与定向像素检查；**不是每个市场Case必须看PNG**。Worker技术看图与Pro专业看图分开记录。链接存在、CDS含数据、图层可见、实际截图和AI看过像素分别如实说明。

实际数据给Pro继续业务分析；投影数据只用于核显示，不反推正式特征。核不一致时保留原件及准确行/字段/时间，给直接消费者影响；不得掩盖成正常市场Pending。处理完一个接口或一个rb窗口，不主动关闭整个单的已明确相关工作；真实工具/容量限制时交全部可用结果、具体限制和连续后继。

本单发布状态：**已签发；未由本Pro派达；未开始新的现场执行。**回交接收者为chatgpt:细节叙事生成_金标:BI01-FO01-执行。管理接受/独立审查/全局调度不是本单Worker自行签认的结果。
