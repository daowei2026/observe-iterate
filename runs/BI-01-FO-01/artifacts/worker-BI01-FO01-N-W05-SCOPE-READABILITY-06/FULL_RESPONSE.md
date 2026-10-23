# Worker06｜W05范围语义、HC活视口与精确Notebook源码技术回交

order_id: BI01-FO01-N-W05-SCOPE-READABILITY-06

issuer_invocation_id: BI01-FO-01-R0017-20261023T192809Z-edd5489f

work_id: BI-01；run_id: BI-01-FO-01

return_to: chatgpt:细节叙事生成_金标:BI01-FO01-执行

## 1. 结果与接收边界

本单三项技术工作均已实际完成：局部显示与源覆盖/真缺件的分类修订已接入新Notebook并真实运行；HC指定文字在同一活会话正常视口已实际看清，无需修改其标签；原W05确切blob及本次已保存执行Notebook都有逐cell完整源码、metadata和输出索引，可小文件读取。源码与成果分别发布到各自授权仓库，准确提交和fresh回读见GITHUB_RECEIPT.json。

本次最终执行身份为 `W06-20261023T205802Z-e33312ba`。最终保存的六个代码单元执行序号1—6、无error。实际浏览器同会话完成rb final/full→local→full及额外local可见页核查，i真实缺价/缺字段反例、HC活root侧栏操作和Worker像素检查。定向技术核验55项通过，相关aidata测试6项通过；没有重跑W05的693项、64项或356文件验收来替代本问题。

这是Worker技术回交，不是原Pro本人看图、专业判断、独立审查或管理接收。未执行工作3三个入口、平台节点/board或正式工作4；未修改公共Task/地图/Intake/计数、手机、Root Goal或调度。完整BI-01任务的其他责任仍由原Pro/管理承担，本单不预签下游。

## 2. 实际权力、版本和输入

- 当前Task/Binding沿 `f6f07531184c97ccbd7a7df34275046407de2e16:runs/BI-01-FO-01/01_当前任务.md`；Owner完整目的和专业方法沿b81cfa14299a415bd4b666f9f69cdc4f5871931f的README及00—04，已读未变正文按原上下文复用。本次另完整取得M16@842454a7e049aff2efe16b6b19cb0386526007da、R17@e0ed960fcc4e472d1345a24feb733cdc12fc36a3，以及b81的DR11、DR10和overlay08适用全文，未作全仓审查。
- 工单取 `b406bd297950d65ae56fc48fe82988e3367b693f:runs/BI-01-FO-01/artifacts/professional-R0017/WORKER_ORDER.md`：11078 bytes，SHA256 `197626041d08117e1c0198d3d0eea39d27e45587d8e0783daad39e2525e625a3` 与原件匹配。
- W05原件固定observe-iterate@b055102ad1a70b3c2824c2c6f5e540886deeb5f7，Notebook blob `96c80e9e21205126f16ace68c9f9029d09206cdf`、8175507 bytes、SHA256 `50a8f9cfddd51ff00151e3c2f7490134591f01ce6fe4dde970d3321fe270ff8d`。本单直接从该已保存Notebook派生，保留cell id谱系；没有从R11候选重头生成，也未改旧Notebook/输出/报告。
- 正式数据仍只读复用W02@081e31241a0c88e47631f80a8b9b8dd43b2b569c、W03@d04f3b08892ccf334a06028f3caab994743566a0的锁定正常导出。没有调用生产N、重算/重生成历史或再取i/hc。本次正常调用需要的130个源Git文件在请求内复用；它们不是新增生产数据。本单没有从摘要重新实例化R30，也没有改三sources、N6/LOO3、5m、night_end_at_2300、normalization或core.v2。
- actual turn `01a16a75-4262-7ba1-9c10-80bdf23117db` 为danger-full-access、approval never、effort xhigh；ignored创建/读回和check-ignore均通过，Goal为空。见evidence/PERMISSIONS.json。
- observe工作树先clean快进至已发布7cc6738，发布前再快进保留09112307的管理并行成果；fetch均使用本单私有refs与 `--no-write-fetch-head`。已完整读取该提交的M18报告，确认维持同一Worker06三项范围，未新增平台放行；主控/管理面未写入。本单aidata新工作树 `/dwdhome/fy/BASE_E6_2/mquant/aidata-bi01-fo01-n-w05-scope-r0017`、分支 `fy/bi01-fo01-n-w05-scope-r0017`，base e8aaa464；使用前已读该版README，原共享工作树未改。源码由5048816修订至最终 `8a08300cb70a610401424bedadb42e9dcde13e71`。

最终实际前端/保存Notebook的kernelspec为Python 3 (ipykernel)/python3，实际解释器仍 `/m3c3/Linux/apps/anaconda3/bin/python`、Python3.10.13；它与现有m3py310的kernel.json指向同一解释器。EXECUTION_RUNTIME.kernel及driver早期事件里的m3py310是继承代码的常量提示，不用它代替实际kernel核验，详见ACTUAL_KERNEL_CHECK.json。JupyterLab4.4.6、Bokeh3.6.0、ipywidgets8.1.2及只读临时overlay仍为已验证环境，没有升级共享依赖。uplot实际13badc6c及preexisting dirty保持，有效pfw.py与W05字节相同。TIS/FRP/workerADT/core/SDK/uplot本单只读；历史checkout HEAD与有效N读者身份的区别沿W05记录保留，不据本次导出消费新增fresh生产读回资格。实际导入路径/hash及本次配置在EXECUTION_RUNTIME.json，环境差分在ENVIRONMENT_DELTA.json。

## 3. 局部范围的直接生产者与消费者修订

原错误是回调先裁rb_price，边界投影再把不在字典的点叫price absent，页首把所有notice合计为缺件。修订后，Notebook回调始终传完整已供rb源价，另传 `display_range=(103140000,K)`；aidata先按原保存关系投影，再按显示范围省略几何。跨视域的端点线不裁成伪造新端点，不补价，也不强制把局部价图拉回长历史。

三类信息已真实进入bundle/export/页首：

|分类|实际表达|
|---|---|
|已供资料有价，但位置在本次视域外|display_omission，保存被省略几何的原坐标/原价/身份；不计入缺件或错误|
|本次未提供该价点/更早行情|input_coverage，标“未覆盖/未提供，不能推断市场缺价”；不伪称已取得完整历史|
|原输入真实NaN、正式present=0或实际读取错误|原NaN保持断线，并另列price_missing；正式状态/原因沿原notice保留；读取异常继续失败，不改称市场Pending|

页面直接显示原Pro确定文案：“局部价图仅显示所选范围；两完成窗统计仍取该K原成员；视域外过程边界未显示，不表示正式源缺失。”同时给已供源价范围/行数、实际显示范围/行数、原输入close缺值数及三类提示数。提示条数不是成员数或市场Case数。

同K103315800、同exact `NodeBehaviorBook/NodeScaleTurnBehaviorRevision/b340dc6c-c135-462b-b6e0-04d24622c180/cfd51328-e2cf-4360-8314-20c9238e93fb`，本次实际结果：

|项目|完整页|局部页|
|---|---|---|
|已供源价|100443000..103315800，4789行|相同4789行|
|实际价图|100443000..103315800，4789行|103140000..103315800，294行|
|正式窗口/working/binding|37926 / 37943 / 1|相同|
|缺件/原输入缺值提示|0|0|
|输入未覆盖|0|0|
|视域省略提示|0|5组几何提示|

此前窗成员0的100460400/3953→100633800/4034保存在局部页的省略记录，未画成局部过程、未称缺价；该价点在完整页仍可取得。两窗效率、working推进/逆向量/前缀效率/等待/倍数七个视图的实际CDS在full→local→full逐项完全相同，包括原x/K、y、exact与状态。不同范围取得不同当前root，主价图范围随选择改变。证据为BROWSER_rb_*、对应plot_view_data与FRONTEND_EVENTS，非孤立新layout。

修改仅aidata三个文件：N配置最终0.2.4-worker06；N显示helper增加显示范围与上述分类/页首；相关测试补本问题。READABILITY_POLICY的“覆盖全部十二成员”旧断言已同步退出，改为完整/局部范围与原成员统计分开；其中布局高度说明同步为实际既有220px，没有新增HC布局变化。最终新kernel已实际消费该配置，55项核验包含此项。场景配置为0.3.2-worker06，旧i helper“may require extension”准备句退出当前pending，已有正确图元继续使用。没有新N产品、告警平台、注册或发布机制。

## 4. i真实缺件反例与HC实际文字

### i恢复拍

K35361000、Node Life9410abda-b111-442d-aa25-6b99da2afeb6，原输入显示37行，其中24条close缺值；实际浏览器close_path保留24个null与断线。推进12、年龄42000及waiting=0可见；counter/efficiency仍p=0 k=4，ratio仍p=0 k=3，无伪零点。local_start35361000、local_count0、last_update缺及“非极值信号”说明仍可读。

原输入较早价点未覆盖与24条实际缺值分别列出；没有为消除rb误报清空全部notice。Worker实际查看本次像素；该结论不是Pro本人已看，也不推成缺口路径已恢复或整个N正确。

### HC活视口

K103315800、Node Life6f92034c-bd94-4d3f-8b7c-6c69e24959ff、修订76d5cfc3-f505-4b62-89b8-b081aedb90f0，当前活root p3694。浏览器窗口2300×1400、devicePixelRatio1，主图真实宽1800px：

- 开始侧栏打开，left-stack宽251，figure x378、宽1800；末拍close3904完整可读，附图K103315800可辨认。
- 实际Ctrl+B关闭文件侧栏，同root的figure x126、宽1800；末拍文字仍完整，未水平滚动或极度放大。
- last_update处close3952、下一根close3946/high3959分别可见；45/97 price、等待258000与正式分母600 CalendarUTITick、独立ratio430均可辨认，没有混成概率/价格单位。

本次最终真实操作是“已打开→关闭”，两种状态的截图均实际打开查看；预发布351e运行还记录了相反切换，未混用其像素。因此对所测正常窗口已有直接可读性证据，HC标签/容器代码无需额外修改。没有保证任意窗口尺寸适配，也未声称原Pro已直接访问。完整viewport、动作、对应root、图像hash与Worker观察在WORKER_VISUAL_INSPECTION.json；PNG只在本机ignored取证，不作为主交付或提交GitHub。

## 5. 精确可读源码运输与主Notebook

主运行实物为本目录 `N_observation_Worker06.ipynb` 与 `DISPLAY_PLAN.json`。原W05仍在原固定提交，不修改、不重新上传整包。

- `notebook_source/W05_original/NOTEBOOK_SOURCE.md`：从确切原blob96c80e9e取得，16074 bytes。
- `notebook_source/W06_executed/NOTEBOOK_SOURCE.md`：从本次最终实际保存Notebook取得，16576 bytes。
- 两侧各有INDEX.json及11个cells/*.json，保留原顺序、id、类型、完整source数组/全文、execution_count及完整cell metadata，顶层Notebook metadata也保留。22个cell逐字段读回与对应原JSON完全相同，见NOTEBOOK_SOURCE_VERIFICATION.json。
- 输出仅保留位置、MIME、JSON字节/hash、执行错误与有限实际stdout索引；大段内嵌Bokeh JS/HTML/保存图未全文展开。文本辅件不等于完整Notebook，也不以作者生成脚本替代最终实物。必要本次业务模型切片在实际BROWSER_*.json、kernel定向审计及plot_view_data，原完整输出仍在Notebook。

本次没有建立运输/哈希平台、H盘或远程Host。小文件已提供准确源对应；原Pro本人后续取得、消费与判断仍须真实发生，不因本次有文本就代签已读。

## 6. 实际运行、失败与核验限制

当前Notebook最终execution_count1—6、无error，KERNEL_COMPLETION实际完成时间20:58:52.403750Z。所有最终BROWSER快照均带当前execution；helper有效字节与实际导入记录一致。源表→投影→实际CDS的55项定向核验通过，6项相关aidata测试通过、10项未选，2项既有deprecation warnings；不把数量当专业/管理认可。

真实保留的工程问题：

1. 新增合成探针最初误以为fixture在K300已缺效率，实际fixture该拍有值。将合成输入明确设置present=0/knownness4，再检缺值不填零；真实市场表未改。首轮失败日志保留。
2. Jupyter恢复了隐藏旧Notebook标签，前端定位器先触发strict冲突，随后首个隐藏节点使wait超时。改为当前visible Notebook定位；旧W05 tracked实物未改变，未执行旧业务单。两个真实失败日志及首次W06 kernel记录保留。
3. 预发布351e复跑时旧完成文件使driver提早写出一条 `run_all_finished` 标签（20:44:23），早于当次kernel真正完成。原事件未改；随后driver加“当前execution不同于重启前”守卫。发布前又发现配置尾部仍有旧十二成员覆盖断言，已同步修正并以最终e333新kernel实际消费配置；当前完成标签晚于实际完成，保存六单元与所有当前root均独立核实。旧运行、早标签和旧配置样本保存在failures/pre_policy_alignment，未冒称旧配置已完整修通，也未重算生产N。
4. 同步配置时一条测试调用误用了artifact cwd，实际无tests路径、未运行测试；保留attempt04日志，随后在真实aidata工作树使用原解释器执行6项通过，不把该错误当环境缺依赖。

这些失败没有被改名市场Pending。原始失败/运行记录保留于failures/；源码运输不展开的保存JS亦未伪称亲读。没有新增保护面写权或全链无前视/收益/全算法正确性主张。

## 7. 打开、剩余与结束

准确打开办法见README：本机现有Jupyter/m3py310，打开本目录Notebook，使用当前配置与本单aidata分支，Restart Kernel→Run All，明确选中Worker06标签再操作。运行依赖既有 `/tmp/bi01-fo01-w03-runtime-20261022` 只读overlay；未来被清理时先恢复已核环境，不能悄换main。GitHub静态预览不保证执行Bokeh JS。没有向Pro提供远程可达前端，不猜私网URL或凭据。

本单临时Jupyter及自有kernel已正常关闭，没有留下等待后继的服务；Goal为空，未创建轮询、timer、daemon或自动恢复来源。现场入口/认证/截图仅ignored。准确生命周期与发布读回在本目录证据/回执。

本单已明确的三项技术交付到此完成。下一责任是原执行Pro消费修订Notebook/源码与HC限定视觉证据，形成专业判断和必要返修，再对适用具名范围申请管理工作2接收。管理须真实决定认可/返修/待证及后继签发；工作3、board、正式工作4和完整观察任务其余责任不由Worker代行。本回交不自领新单、不等待Pro而常驻。
