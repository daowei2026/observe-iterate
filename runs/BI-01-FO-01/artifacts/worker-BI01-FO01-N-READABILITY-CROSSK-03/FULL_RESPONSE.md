# BI01-FO01-N-READABILITY-CROSSK-03 Worker 技术回交

返回目标：`chatgpt:细节叙事生成_金标:BI01-FO01-执行`

order_id：`BI01-FO01-N-READABILITY-CROSSK-03`

技术状态：`TECHNICAL_RETURN_READY`

业务状态：未由 Worker 判定；本包交原执行 Pro 继续看真实图、解释业务认识并决定后续。

## 一、结论先行

本单已在独立 aidata 分支真实接入专业配置 v0.2.1，并把原来“只存在于配置中的可读性策略”落实到 `build_uplot_layout`、`NPanelPlotter`、范围选择、实例身份和实际调用脚本。没有修改 N 正式值、TIS、FRP、core、SDK 或 uplot 源码。

rb 四页已经重新生成并完成分层验收：HTML、Bokeh renderer/CDS、Chromium 最终 range、全页 PNG 和 Worker 原始像素检查分别留证。主要修订结果为：

- 演变页只使用正式发生与行情覆盖的交集 `103056600..103315800`，433 个正式发生不再被完整长价格域压缩到约 9% 的横轴；主图和四个附图均最多 10 个主标签。
- 三张 selected-cut 页的价格页仍覆盖当时合法十二成员及 working；四个标量附图改为两列、150 高、独立 `K-1..K+1` 显示视口，图元本身仍只有 `x=K`，没有假 K+1 记录。
- 每个 present 标量都有可见的“值 + 单位”，不靠 hover；同 K 的配对值左右分列，上边界的累计逆向量和 waiting 标签向点下方偏移。首次真实像素检查发现的标签重叠/裁切没有被隐藏，预修复 hash 和处置保存在 `PRE_VALUE_LABEL_VISUAL_CHECK.json`。
- 数值 panel 使用 v0.2.1 的显式非退化 y range，并关闭随后会覆盖它的 fit callback；真实零保留，all-null 显示明确状态，不填零；waiting ratio 不限于 `[0,1]`。
- 图例移到绘图区上方，颜色仍只表示品种身份；线型、形状、分区和文字表达过程性质。默认未强制打开时长 panel，本次按问题选择 rhythm。
- 显示实例身份现在包括 symbol、node Life、binding、mode、selected K/请求范围、exact/发生选择、配置版本和 optional panels。同进程三 K、相同末次 exact 但不同 price range、相同 exact/range 但不同 optional panels 都产生不同 ppid。
- working 连续性改用 Life、start、direction、binding、knownness 和连续发生判断；存储地址变化本身不再等同新过程。rb 确认后地址 `37927 -> 37943` 但 Life、start、direction 相同，正确识别为同一过程；确认前到确认时则确为新 Life/方向。

正常 OnlyRead 补证也已完成：

- i 在 `K=35361000` 确有正式发生，不是文件名推断或边界猜测。恢复拍与前后拍保持同一 working Life/start/direction；恢复拍只恢复 progress=12、duration=42000 和真实 waiting=0，efficiency/counter/waiting_ratio/intervals 仍不可用。下一拍 progress=9.5、duration=42600、waiting=600，仍不能称为全量恢复。
- hc 末拍 waiting=258000、waiting_ratio=430；正式 intervals 为 `[600,1200,600,2400,600,600]`，最后三项中位数为 600，并与 rhythm.current_median 原表一致。分母不是用 `258000/430` 倒算。
- 原 previous 首成员正式 direction code 1。FRP 的 `TurnDirection` 枚举顺序和 ThinMember `fromEnum` 保存直接证明 `1=down`；正式端点 close `3953 -> 4034` 的正视觉斜率不改变源方向，也没有被 Worker改写。

aidata 最终 commit 为 `b044ad9c92ffc98ee1ac7aec829e3673c126c846`，GitHub 分支 `fy/bi01-fo01-n-readability-r0009` 已推送并 fresh 回读。observe-iterate 技术包的精确结果 commit、远端 ref 与逐文件回读见 `GITHUB_RECEIPT.json`。

## 二、权威输入和实际版本

开工前核了完全访问：sandbox disabled、approval never；本聊天无 Goal、队列、守护或自动恢复来源。本单没有创建子 agent、手机动作或新 Codex 聊天。

权威原件均按指定 commit 读取并校验：

|对象|commit / UTF-8 字节 / SHA-256|
|---|---|
|R0009 工单|`3af6585f0ce79d69e0b4d58149d852081ec179ad` / 13011 / `387000791626f58b7e4829c6705312a3dbc2db05188483e6d652e682baf2ae15`|
|R0009 完整专业报告|`fd623bd5ba9fcce5e07294739ae2e009d791e582` / 34313 / `18a69bbfef60df5540d0a93142027ba9f4e5d17bf3326d406dd7b084d0006df5`|
|R0009 配置 v0.2.1|`23b8089ffd6580aa5f9f1505b6fb87c5ea63bed2` / 20072 / `39275fa22a564649d9092a9a28f30a7e018c27d3673212f18a9bc05ebd964641`|
|当前 Task/Binding|`20426e5e88a67d58eaaf168168c5e4f74d73a31b` / `01_当前任务.md#technical-work`|

实际版本和处理：

|责任面|版本/路径|本单处理|
|---|---|---|
|完整 R30 配置|协调仓 `a6f5025e…`，SHA `946d16ab…`|完整 rb/hc/i 三来源，未删 source 或改产品身份|
|TIS 修后读者|`3ff34c72be8ef025f68e18b097fe7b8f1f472668`|overlay 只读|
|FRP 方法|`5154c407249c130a6e048c8541b76dfdec3ea48c`|源码定向核方向，只读|
|worker ADT|`cd5c307dcb3483ef76242b5c37177a969c5fcbd2`|固定 overlay，只读|
|aidata 基线|`28260d3ec5d2ed254b2539cb9abc656e4737f80b`|独立工作树/新分支|
|aidata 结果|`b044ad9c92ffc98ee1ac7aec829e3673c126c846`|仅 3 个授权文件，已推 GitHub|
|uplot 实际导入|`13badc6c079eebe7242abd65e56b328c45dcee2a`|共享 checkout 只读；既有 dirty 原样保留|

共享 uplot 开工前已有 `pfw.py` 修改和两个未跟踪项；TIS/worker 共享 checkout 也有他人既有 dirty。本单使用 `/tmp/bi01-fo01-w03-runtime-20261022` overlay 固定实际导入路径，没有覆盖、清理或提交他人成果。

正式产品目录保持：

```text
/m3varK/BaseData/futures/TA_updto20240229_DBA/fao/prod/U2NormalNodeBehaviorFrp/9/0/d/3/7/a/4/fb2007d71be1e620801457424d6dea8b4/func
```

配置仍为 5m、`night_end_at_2300`、TA_updto20240229_DBA、N6/LOO3、`normalization=null`、`core.v2`、`compact_history=true`。没有扫描任意 N 或重跑历史生成。

## 三、aidata 最小修改

aidata 独立分支只提交三个文件：

1. `feature_configs/u2_normal_node_behavior.py`：逐字采用专业 v0.2.1 原件；实际落点 SHA 与专业原件相同。
2. `u2_normal_node_behavior_display.py`：把 `READABILITY_POLICY`、`DISPLAY_IDENTITY_FIELDS`、`evolution_display_range` 和 `numeric_display_range` 接入真实消费者；补 working Life/start/rhythm 关系、可读 layout、状态和实例身份。
3. `tests/test_u2_normal_node_behavior_display.py`：增加范围交集、同 Life 跨地址连续、实例身份、零/越界/null range 和值标签布局检查。

没有建立第二套 Feature、历史档案、绘图库或 Host。`n_display/*` 仍是请求内只读显示投影，不冒充 TIS 正式表；CSV 只用于交付、恢复和消费者核验。

`61 passed` 的 aidata 全测试通过；定向 U2/evidence 合同为 `34 passed`。两条 warning 都来自既有运行依赖的弃用提示，没有失败。结果见 `TEST_RESULTS.json`。

## 四、四页真实渲染和时间边界

|页面|K/范围|实际 panel|直接检查|
|---|---|---|---|
|`rb_evolution_actual_occurrences`|`103056600..103315800`|price、完成效率、working motion、working efficiency、rhythm|433 正式发生；各轴主标签 ≤10；价格/OHLC 同步裁范围|
|`rb_selected_before_confirmation_K103150800`|K=103150800|同上|6 个标量标签；正式图元与价格输入最大 K|
|`rb_selected_at_or_after_confirmation_K103151400`|K=103151400|同上|6 个标量标签；正式图元与价格输入最大 K|
|`rb_selected_final_K103315800`|K=103315800|同上|6 个标量标签；正式图元与价格输入最大 K|

三张 selected-cut 的 scalar x range 在浏览器最终模型中均为 `K-1..K+1`，只有一个 `K=...（单切点）` 标签。这个范围只是屏幕留白，CDS 中仍只有 K。价格输入按 `open_uti <= K` 截止；KPriceLine 内部可把 K 开始的 5m bar 中心画到 K+300，但其来源仍是 `open_uti=K`，没有提供或混入下一条市场记录。

同进程三 K 的正式过程关系：

|K|exact 末段|working address|working Life / start / direction|
|---:|---|---:|---|
|103150800|`6d4acb13…`|37913|`ebc4a9f9…` / 103043400 / up|
|103151400|`ef2f74f6…`|37927|`a820d2c1…` / 103059000 / down|
|103315800|`cfd51328…`|37943|`a820d2c1…` / 103059000 / down|

确认时和末拍是同一 working Life，只换存储基础。其 rhythm 技术值显示出 waiting 与分母共同变化：确认时 `49200/600=82`；末拍 `123600/7800=15.8461538...`。图上保留正式 ratio，不改指标、不截概率区间。

四页最终 Chromium 均 HTTP 200，实际各有 5 个 Plot、5 个外置 legend 和全部五类 panel group；selected-cut 各有 6 个 value LabelSet。Worker 逐张查看最终原始 PNG，确认横轴黑带、过宽视口、图例遮点、标量重叠和上界裁切均已处理。`BROWSER_CAPTURE.json` 与 `WORKER_VISUAL_INSPECTION.json` 分开记录模型和像素事实；这不等于执行 Pro 专业看图。

## 五、i 恢复拍的正常读回

使用 Node Life `9410abda-b111-442d-aa25-6b99da2afeb6`，对三个整数知识 K 分别调用正常 `read_at_knowledge`，并显式 `CalType.OnlyRead`。每拍取得 19 张原表，包括 `intervals`，没有以 W02 文件名补行：

|K / timestamp|exact|working address|正式可用量|
|---|---|---:|---|
|35360400 / `2017-03-30 22:55:00.500`|`3d8951d5…`|10015|duration=41400；progress/efficiency/counter/waiting/ratio 不可用|
|35361000 / `2017-03-31 09:00:00.500`|`1d82177d…`|10022|progress=12、duration=42000、waiting=0；其余路径量仍不可用|
|35361600 / `2017-03-31 09:05:00.500`|`b4de4558…`|10022|progress=9.5、duration=42600、waiting=600；其余路径量仍不可用|

三拍都属于 Life `5727e951-20b6-4a82-8c52-fc3a32f686cc`、start 35319000、direction down。恢复拍的 rhythm 只确认 `local_start=35361000`、`local_count=0`；full count、last update、current median 都没有正式值。W02 同源行情证据仍显示 24 条连续 night close 合法空、恢复 close=572；本单复用其固定 hash，没有重读已经有效的行情大段。

结论边界是“原价恢复时部分端点量恢复、路径量仍缺”，不是“N 全恢复”，也没有复制历史 R33 的数字作为答案。恢复点 `.500` 标签与整数知识 K 的关系由本次 origins 原表直接确定，不是时间筛选边界缺陷。

## 六、hc 分母和原方向补证

hc 使用 Node Life `6f92034c-bd94-4d3f-8b7c-6c69e24959ff`、K=103315800、正式修订 `76d5cfc3…` 正常读取。working Life 为 `e93bd731-4116-46d7-ba77-e1a2f7ec38b5`，start=103044000、through=103315800，当前正式量包括 progress=45、counter=97、efficiency≈0.0315789、duration=271800、waiting=258000、ratio=430。

原 `intervals` 六项是 `600,1200,600,2400,600,600`；近期三项 `2400,600,600` 的中位数为 600，正式 rhythm.current_median 也为 600。local/full count=14、local_start=103044000、last_update=103057800。另经正常 `U2MainlineKLineInput.rerun(CalType.OnlyRead).to_df` 读取 start..through 的 454 条 5m 行情，close 无缺件。Worker 只证明原表分母与范围，不把 430 解释成概率错误或跨品种投资强弱。

方向核验使用 W02 正式 previous_members 和同绑定价格：目标成员 Life `d56e512a-d30f-49b9-a164-0164a9e81f0f`，start 100460400、end 100633800、direction=1、knownness=0，close `3953 -> 4034`。FRP `5154c407…` 中 `DirectionUp | DirectionDown` 派生 Enum，ThinMember 保存 `fromEnum`，且 `directionSign DirectionDown=-1`。因此 code 1 是 down，正端点斜率与 down 可以并存；显示保留两者，不按视觉斜率改上游方向。

## 七、失败、恢复和限定

本次没有用最后的 PASS 覆盖过程问题：

1. 首个有限合成探针使用测试 fixture 的任意小整数 UTI，无法映射真实 Calendar，uplot 正确返回 `No K data`。该失败不是生产缺陷；探针改为复用固定 hash 的正式末拍结构，并给合成零/null payload 独立 exact，避免违反真实实例缓存身份。
2. 第一轮真实 PNG 显示完成效率标签重叠、waiting 标签贴上界被裁；第二轮又发现“此前效率”向下偏移会贴近下界。最终方案改为配对标签左右分列、counter/waiting 向下偏移，并增加半透明白底。预修复截图 hash 和观察保存在 `PRE_VALUE_LABEL_VISUAL_CHECK.json`。
3. 正常 reader 仍打印 W02 已记录的三个旧可选布局缺文件提示；本次四个 cut 的 19 张请求表均实际返回并逐文件 hash。该提示没有被吞成“全产品无缺陷”，也没有扩大写权去修 TIS。
4. 演变页为避免重读 rb 大表，复用 W02 已固定 hash 的旧投影。旧投影没有携带每个存储边界完整 Life，因此该页保留未证明边界的断线；新消费者只会在 fresh bases 证明同 Life/start/direction 时连接。不能用本页宣称所有历史地址切换都已逐一核 Life。
5. `RENDER_MANIFEST.json` 在 HTML 生成时如实把浏览器/像素标为 pending；随后独立的 `BROWSER_CAPTURE.json` 和 `WORKER_VISUAL_INSPECTION.json` 已完成 PASS。没有回写历史时点造成伪造。

aidata 的运行发生在独立工作树尚未提交、但三个文件已是最终字节的时段。提交后这些字节与 `b044ad9…` 和 GitHub fresh ref 逐字一致；`RUNTIME_COMMIT_ALIGNMENT.json` 保留“运行时 HEAD 仍为基线”与“结果 commit 对齐”两个事实，不倒记版本。

## 八、并发到达的 Owner Uplot/aidata 边界限定

发布前并发对账时，远端新增 `4996cd49aa6549bcc3425cad78a144f4d62776cb:runs/BI-01-FO-01/OWNER_FEEDBACK_20261022_UPLOT_AIDATA_BOUNDARY.md`。该文件明确说明它不是新 Owner GO、不倒改历史；本分支已用普通 merge 保留主控 R0010 记录和 Owner 文件，没有覆盖任一写者。

本技术包据此限定资格如下：

- W02 旧四页仍按 Owner 原文“不作为合格工作 2 展示成果”；本单没有把旧 PNG 补几项验证后重新声明通过。
- W03 四页是从可信正式导出、用实际 `uplot/CAEGraph` 消费者重新构建的新页面，并完成模型/浏览器/像素技术检查；它们是交原执行 Pro 继续判断、修订的真实技术输入。Worker 不据此代签“工作 2 已通过”。
- 本单只交 standalone HTML/PNG/数据和实际消费者代码，没有建立 aidata 正常平台 CAE 节点或可持续打开的平台链接；因此不能冒充 Owner 所述“工作 3 平台链接”已经完成。
- Owner 要求后续由原专业 Pro 对重新成图和画法负责，并由有权管理更新方法/任务/后继安排；这些不是本 Worker 的地图、Task/Binding 或调度写权。本单保持准确回交，不越权改公共任务。

这项后到限定不改变已完成的正常 OnlyRead 原表、aidata commit、实际 Uplot 页面字节或失败记录，只改变它们可被谁、以什么资格采用。

## 九、仍未完成和权限边界

- 本包只完成 Worker 技术职责；原执行 Pro 尚需消费这次重新生成的真实 Uplot 图/数据，形成业务认识、反例和参数/画法判断，并决定其是否成为工作 2 有效成果。
- aidata 平台 CAE 节点和可实际打开的平台链接没有建立；standalone HTML、PNG 与临时 localhost 只作为技术证据，不能代替工作 3 平台链接。
- i/hc 本次按实际问题交正式原表和数据，不机械制作每 Case PNG；没有执行所有品种、所有反例或完整 U2/U3。
- 演变页的全历史每个存储地址边界没有重新全量读取 bases；未证明的边界继续断线，没有“同 Life 即跨未知缺口连线”。
- 没有收益预测、机会簇、资金目标、真实市场研究结论、Reader 签认或管理接受。
- 没有修改 TIS/FRP/core/SDK/uplot，没有改 Task/Binding/Intake、公共地图、主控 scheduler 或 Goal，没有新建常驻轮询/daemon/Host。

## 十、恢复入口

|用途|路径|
|---|---|
|完整结论|`FULL_RESPONSE.md`|
|i/hc 正常读回及逐表 hash|`evidence/CROSSK_READ_MANIFEST.json`|
|i/hc 关系摘要|`evidence/CROSSK_SUMMARY.json`|
|方向映射|`evidence/DIRECTION_SOURCE_CHECK.json`|
|四页 HTML/PNG|`render_evidence/`|
|实际图用输入|`plot_view_data/<page>/`|
|浏览器/像素|`render_evidence/BROWSER_CAPTURE.json`、`WORKER_VISUAL_INSPECTION.json`|
|运行字节/commit|`evidence/RUNTIME_COMMIT_ALIGNMENT.json`|
|最终包装验证|`evidence/FINAL_VERIFICATION.json`|
|复跑脚本|`scripts/`|

`run_crossk_reads.py` 是显式 OnlyRead 定向读取入口；`render_readability_pages.py` 只从 W02 已固定 hash 的正式导出重建本次页面，不重跑 N；`capture_rendered_pages.py` 使用临时 localhost 打开 HTML，结束前关闭服务；`verify_delivery.py` 不读正式大表，只验交付物、hash 和关系。
