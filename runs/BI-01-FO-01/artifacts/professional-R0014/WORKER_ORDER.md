# BI01-FO01-N-UPLOT-NOTEBOOK-05｜工作2真实重画、Notebook执行与交互

work_id: BI-01  
run_id: BI-01-FO-01  
order_id: BI01-FO01-N-UPLOT-NOTEBOOK-05  
issuer_role: professional  
issuer_ref: chatgpt:细节叙事生成_金标:BI01-FO01-执行  
issuer_invocation_id: BI01-FO-01-R0014-20261023T153303Z-57f340f3  
issuer_assignment_token: BI01-FO-01-N-M13-CONTINUE-430990e5b328469298a00bec0b412dff  
recipient: 本run既有机制实际委派、具有现场执行能力的Worker  
return_to: chatgpt:细节叙事生成_金标:BI01-FO01-执行

<a id="authority"></a>
## 1. 当前签发范围、替代关系与交回

本单由原执行Pro依据当前Task/Binding实际签发：`daowei2026/observe-iterate@f6f07531184c97ccbd7a7df34275046407de2e16:runs/BI-01-FO-01/01_当前任务.md#technical-work`；管理采用为`2549c3bc3838024f6dae5ab0c3a1ef0b9f2aff2e:runs/BI-01-FO-01/reviews/management-R0013/FULL_RESPONSE.md#worker-disposition`及#next-professional。方法为b81cfa14299a415bd4b666f9f69cdc4f5871931f的professional/feature_observation/README及00—04。完整专业责任不改变。

**本单只执行工作2真实新绘图、Notebook执行/所需交互及其相连准备、修订和排障。**不执行工作3的平台消费或正式工作4。原`BI01-FO01-N-UPLOT-NOTEBOOK-PLATFORM-04`的整单派发效力已由M13撤销，本单替代其当前技术后继，不是重派旧载荷、恢复旧Worker或为旧图补验。旧工单及原失败版本保留历史。

当前技术目标不是验证一份已经成功运行的Notebook，而是完成第一次合格的新Uplot图和交互运行。Worker回真实技术实物给原Pro；原Pro消费、作有边界专业判断，再向管理申请具名工作2接收。**技术PASS后仍回原Pro，不自动进入任何平台任务。**管理认可及后继签发不是本单预先授予的条件许可。

不创建/恢复/停止Root Goal、计时器或运行调度；本次Owner允许接续原Run的事实沿当前管理决定使用，具体控制操作仍归原主控。本单发布只表示已签发，不表示已经派达、接单、创建现场分支或运行进程。

<a id="inputs"></a>
## 2. 实际输入、已有成果及原件复用

### 2.1 精确业务和代码输入

P11为`daowei2026/observe-iterate@a2c9f9333c6578b8bf1dd26fb589b1a6b2956ae9:runs/BI-01-FO-01/artifacts/professional-R0011/`。

- `FULL_RESPONSE.md`：原Pro完整正确认识和限制；按M13只作历史认识、参数/展示准备，不作为新规范下正式工作4结果。
- `N_observation_R0011.ipynb`：实质代码候选，原Git blob为cad0e3fb1cc9dbccd113410676bb2bddf55c33ce。首单元曾因缺mquant/ipywidgets失败，其余绘图/交互单元未执行。
- `DISPLAY_PLAN.json`：实际场景配置候选，原Git blob5583e768b1a4b8965b2c9fb5b8374d25ae3a2e9f，version=0.3.0-r0011-candidate，status=NOT_RENDERED_NOT_ACCEPTED。
- 原`verify_r0011.py`及`CHECK_RESULTS.json`保留限定参考依据，不要求重跑27项来代替绘图，不把其passed升级成运行成功。

不从头空写一份无真实调用的Notebook。以这份代码候选为起点，在本单新输出位置形成实际运行版本，保留本次所改代码、参数和对应配置；不修改P11原历史失败文件。

### 2.2 当前工作副本必须清除的旧下游要求

原P11配置和Notebook是历史输入，不是本单的另一套派发规范。准备本次运行副本时，按以下已由Pro决定的定向修订落地，不由Worker另判业务范围：

1. `DISPLAY_PLAN.json`删除`platform_acceptance`，并从`pending_real_display_changes`删除“normal platform pages and same-node board delivery are a separate real execution obligation”这一项。其余真实来源、K、品种色、稀疏点和缺件表达要求保留；记录本次实际配置版本。
2. Notebook的`r0011-09`说明保留hc原表核对和参考计算边界，删除“当前尚需完成的真实验证”中三公开入口、平台页面、同run/node正式交付及后续分析作为该Notebook当前完成项的句子，改为本次新图执行、必要交互、原Pro判断和工作2接收材料。没有新增平台代码；不要加入平台调用。
3. 新运行副本的标题、metadata及实际运行记录标明本单和真实本次执行身份；不得把原R11预检错误输出标成新版本执行结果。原代码可以按真实接口/错误继续修通，不为换标签无意义改业务计算。
4. 原Worker04的§4平台调用正文、相应前置/验收/直接后继不进入当前单，也不以“技术联调”名称执行。不得仅给旧混合单顶部加声明后原样运行。

以上处理只撤当前未获授权的下游执行要求，完整任务中的工作3/4义务仍由管理后续真实签发承担。

### 2.3 已有正常数据，不重新整批取数

W02为`observe-iterate@081e31241a0c88e47631f80a8b9b8dd43b2b569c:runs/BI-01-FO-01/artifacts/worker-BI01-FO01-N-DISPLAY-INTEGRATION-02/`，提供rb正常selected cuts及同绑定行情；其旧图和图用投影不作正式输入替代。

W03为`observe-iterate@d04f3b08892ccf334a06028f3caab994743566a0:runs/BI-01-FO-01/artifacts/worker-BI01-FO01-N-READABILITY-CROSSK-03/`，已有i三个知识切点35360400/35361000/35361600及hc末拍原rhythm/intervals、相关行情和方向映射。i恢复N及hc分母已补齐并被P11消费，不再重新整批读取来证明取数完成。缺的是新画法实际执行及判断，不是这些原件尚未到达。

rb三个已取K为103150800/103151400/103315800；Node Life为b340dc6c-c135-462b-b6e0-04d24622c180。i Node Life为9410abda-b111-442d-aa25-6b99da2afeb6；hc为6f92034c-bd94-4d3f-8b7c-6c69e24959ff。按原地址/修订/Life/时间关联，不按列表位置猜成员。保持UInt64身份、present/knownness/applicability/reason、实际/确认/known_from/as_of。

所有旧图，包括W01、W02原/修后及W03技术重渲染，均不采用为合格工作2成果；可信数据可核源复用，正确读取/图元代码只作未验证参考，必须本次重新调用绘图。

### 2.4 方法、环境和版本

已知aidata参考基线b044ad9c92ffc98ee1ac7aec829e3673c126c846；历史现场目录`/dwdhome/fy/BASE_E6_2/mquant/aidata`。先核当前实际目录、HEAD、有效文件、导入路径及他人dirty，再读所用版本README和本次所需合同，不用main文档暗换代码。uplot手册参考0a4fcd54059782572a3f7e82fad041121e8c65ad；历史实际uplot为13badc6c且有既有dirty，不只记录HEAD就声称干净锁定，不覆盖或提交他人成果。

生产N保持原R30完整实例：协调仓`feature-refinement-implementation-agent-evolution@a6f5025e8b082f8f11056e566a2a07abc49bb939`的`agent_evolution/pilot_cases/network-dynamic-ceps-factory-u2-u3/runs/first-two-fao-20261017/ENGINEER_STORAGE_REDUCTION_R30/ACTUAL_RUN_CONFIGURATION.json`。rb/hc/i三sources、5m、night_end_at_2300、TA_updto20240229_DBA、MedianTwoWindowV1、N6/LOO3、normalization=null、compact_history=true、core.v2。此摘要不能替代真正需要实例化时的完整嵌套原件，不能删sources改变产品身份。

TIS修后3ff34c72be8ef025f68e18b097fe7b8f1f472668、FRP5154c407249c130a6e048c8541b76dfdec3ea48c、workerADT cd5c307dcb3483ef76242b5c37177a969c5fcbd2保持只读。原正常保存路径为：

```text
/m3varK/BaseData/futures/TA_updto20240229_DBA/fao/prod/U2NormalNodeBehaviorFrp/9/0/d/3/7/a/4/fb2007d71be1e620801457424d6dea8b4/func
```

路径不是本次已可读证明。优先核源复用已交正常导出；确需更完整连续发生/上游时，再用正常具名read_session/read_at_knowledge等和显式OnlyRead限定补读，不强制重生成N，不把`to_df`拒绝单表解释为整个入口不可用。

<a id="drawing"></a>
## 3. 工作2实际画法及现场执行

### 3.1 正常入口与候选代码

Notebook原代码用本地Git读取不可变正常导出、恢复多表索引、保留64位Life，经正常bundle/layout重新绘图及show。b044参考的`build_uplot_layout`实际调用CAEGraph(...).layout()；可核源复用它的正确读取/图元能力，不得把旧HTML/PNG加载进Notebook，不能以重存旧页面恢复资格，也不在观察仓复制一套绘图库或N算法。

先使用已有合适Jupyter kernel，核实际mquant/Uplot和必要交互依赖。R11和R14的Pro沙箱缺依赖不证明Worker现场也缺，不因此先做全环境审计或无权升级共享依赖。选现成合法环境即可；确需独立环境按已有权力处理，需管理员/公共权限时具名报告，继续不依赖它的工作。

Notebook默认仓库路径`/dwdhome/fy/observe-iterate-bi01-fo-01`只是既有候选，须核实际存在。`OBSERVE_REPO`指含W02/W03锁定Git对象的实际仓库；原代码的`BI01_R11_ARTIFACT_DIR`可明确指向本次工作副本目录，以加载本次已修订的DISPLAY_PLAN，或同步修订环境变量名称及说明。不能让新Notebook悄悄读取旧混合配置。记录真正消费的配置路径和版本，不仅新建文件而旧路径照用。

### 3.2 rb：完成窗、working与知识时间

价格主图用原5m OHLC淡背景及close；已知成员的实际端点、确认点用不同形状/说明，不按可见线段斜率重写源方向。两完成窗的效率分别表达，保留成员更新和真实知识时间，不只显示change一个数。当前working净推进、累计最大逆向量、前缀效率与完成窗分开，单位明确，不能将两个中位数相除替代效率。

选定K只使用当时合法成员/修订和截至K的原行情；发生、确认/可知、As-Of和后来修订分开。新确认working已有过去年龄，不以确认拍年龄0或当根交易信号表示。页首注明所选K或末次状态，不能把最后down套在整个演变区间。相同Life的保存基础变更不直接叫新市场过程；不同Life/start/方向、缺价/失败或未知连续性不得跨越连接。

候选三切点只是已取数据的起点。稀疏K只画真实点，不造期间保持/斜线；确需连续演变时，使用合格正式发生与正常原表关联，保留覆盖和缺件，不以旧plot_view_data充正式历史。可先交真实已成的具名范围供Pro判断，但不能把三切点或一个图固定为全部目标。

### 3.3 i：真实零、部分恢复与缺路径量

沿同一working展示可用的推进/年龄；路径效率和逆向量缺件不能填0。恢复点局部waiting=0与local_start35361000、local_count0、last_update缺并列说明；ratio因分母缺仍不可用，不能标作“新极值信号”或零概率。下一拍9.5/600与恢复拍12/0的对照保持原字段资格。

图形需使等待零与缺ratio、可用端点量与缺路径量可辨认。原状态表仅辅助准确值和核查，不能只打印表就称图已表达这些含义。现有helper不足时，在有权aidata显示依赖内最小修订，并让实际Notebook消费；不改生产方法。原价缺口不能硬连，也不把正常休市与已记录缺价混同。

### 3.4 hc：close极值不是K线影线

当前已明确问题是用原close解释last_update及等待，而不是用high替代。需要图形说明时，把103057800的close3952与末拍3904、waiting258000及正式分母600/ratio430放在各自单位和时间位置。13:40影线high3959而close3946的反例要能避免“影线创新高就应更新close极值”的误读；不是要求每Case固定一张图。

W03/P11已有原分母和有限close前缀核对；不再用重复算术替代图形反馈。单品种原价量不跨品种直接排名，等待倍数不截[0,1]、不解释成概率或无行情活动。

### 3.5 共同的显示与交互要求

重要信息优先，不默认全画六指标/MAD/LOO或中间地址；LOO并列不是成员重要性排名。颜色优先品种身份，完成/未完成、状态和指标性质用形状/线型/位置/分图，兼顾未来多品种但不设独立单/多品种验收任务。

price、ratio、CalendarUTITick不混轴或套价格DynStd；单值/零值有非退化显示范围，all-null保留缺件原因。图例不遮点、时间标签不成黑带，选定K单点不能因共享长横轴而不可辨认。修改视口/边距不能加入K后数据；原右开K+1未被证实有错，不反复修该已排除假设。显示范围不是生产N参数。

实际从新kernel执行适用单元，在Jupyter前端检查K选择、hover、缩放/平移/复位及本次需要的图例操作。分别核预期和实际值/身份/状态，连续切换不同K及不同range不得串用缓存；同末次exact不自动代表相同范围或配置。旧正确CSV不能掩盖新renderer显示错误。

交互需要真实发生。nbconvert退出0、Bokeh对象生成、HTML存在、HTTP200及GitHub上传都不能单独证明前端运行成功。记录操作者、动作、对象/版本、实际结果和限制；不以PNG作为看图交付。HTML只能辅助，主交付仍是实际执行成功、可复现且可交互的Notebook。

<a id="permissions"></a>
## 4. 写权、相连修通与禁止扩展

若工作2的实际显示helper/配置需要改aidata，先核其真实HEAD/工作树及他人修改，在该仓新建独立工作分支。可采用无冲突名称`fy/bi01-fo01-n-work2-r0014`，此处仅拟名，尚未创建。保留既有正确修复，不改共享原分支、不清理/覆盖他人dirty。

uplot/TIS/FRP/workerADT/core/SDK只读。授权覆盖Notebook当前调用、数据关联、展示配置、必要aidata显示helper和直接消费者、普通运行排障与验证，可跨必要文件连续修通，不逐报错请批。公共行为、受保护源码/注册或权限变化，给准确输入/调用/位置/受影响消费者，回原Pro/管理协调；局部失败只限制相关工作。

**不调用build_chart_run、build_big_world_chart_pages、build_board_run来消费当前候选；不注册平台CAE节点、不生成平台交付或board包、不开展正式工作4。**与画法无依赖的接口/环境阅读可作准备，但不产生下游完成资格。aidata显示helper用于Notebook的工作2依赖不等于取得平台权限。

不在观察仓建立第二绘图库、正式N算法、Host、通用身份/发布体系或全历史档案。缺方法、缺输入、未调用、环境未就绪、失败、未成熟、合法空和真实零分别报告，不能互相改名。

<a id="delivery"></a>
## 5. 实际交付和停止条件

回交原Pro，目标目录为`runs/BI-01-FO-01/artifacts/worker-BI01-FO01-N-UPLOT-NOTEBOOK-05/`，它是交付目标，不是当前已存在成果。交完整技术正文、实际新Notebook和配置、代码修改位置/提交、实际运行环境/kernel/导入及必要dirty差异、正式来源与图用投影对应、执行结果、所测交互、技术观察、失败/修复及全部未完。

给准确Notebook路径及实际打开办法；有现存Jupyter入口时报告确实可用的地址，不猜私网URL、访问令牌或现场权限。不要在GitHub提交凭据。GitHub不保证运行Bokeh JavaScript，不能把网页预览文件说成已交互打开。前端无法向Pro可达时，明确实际访问限制和已取得的证据，不代签Pro本人已看。

技术核验覆盖此次实际业务画法和直接调用，不以测试数、图数、文件数作为成功标准。可先回交可靠已成范围，但不以修一个依赖/轴/图为本单已明确相连工作的主动收工点。环境真正不可用或权限受限时交实际操作、错误、实物、影响范围和恢复条件，不能虚构成图。

**技术回交后的接收关系：Worker → 原执行Pro消费与专业判断 → 原管理对具名工作2成果申请作认可/返修/待证决定。**本单不替管理认可、不附技术通过后自动转平台的续行条款。其他合法工作1/2和无依赖准备不因申请接收而冻结；完整观察任务的其余责任保留在当前Task和原Pro续作正文。

当前签发状态：**已签发，未派达、未接单、未现场执行；没有新图、成功交互、拟分支或管理工作2认可的事实。**
