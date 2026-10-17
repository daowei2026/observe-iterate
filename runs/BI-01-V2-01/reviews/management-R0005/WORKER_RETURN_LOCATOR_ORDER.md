# R0005 回交定位适配：有界技术工作单

worker_order_id: BI01V2-R0005-RETURN-LOCATOR-FIX-01
work_id: BI-01
run_id: BI-01-V2-01
issued_by_role: management
issued_by_invocation: BI01-V2-01-R0005-e843decd6d255833e9d12e4a
issuer_assignment_token: abb213474937fe9b76dc388dd7f76a70
recipient: codex-thread:01a14a59-7f26-7921-b549-3e7cd9be5119
execution_capacity: 本单明确授权的Worker Codex技术容量；收取/投递时仍是原操作容量
status_at_issue: ISSUED_NOT_EXECUTED

<a id="authority"></a>
## 1. 直接目的和已定决定

按同目录`DECISION.md#locator`，把现有DR14“先解析成同一目标再比较”接到真实回交消费者，解决R4同一Binding的锚点/JSON行范围被字面比较误拒。不是删除身份/权限检查，不重写R4原文，不新造Binding，不让原专业者重做S1，也不创建另一套locator/gate/登记系统。

此线程已有本run运行材料和R2修补经验，现明确授权处理本单代码、必要依赖、测试、实际回用和技术回交。保持既有aidata Worker `BI01V2-R0004-AIDATA-FIXED-01`唯一在途并继续，不把此单交它排在制图之前，不为本地工程多开手机Pro轮次。

<a id="sources"></a>
## 2. 已核入口和实际原件

代码读取基线`daowei2026/observe-iterate@50fd379ea25600aa6bf1b530f9ca0d4109228b24`：
- `runtime/tools/bi01_run_gate.py`，blob `7476275ad38ad5652456e7e1dbba13d30ee5936b`，`after_return()`中`qret.get("binding_ref") != rec.get("binding_ref")`。
- `runtime/overlay/tools/question_work_check.py`，blob `649b484d15c1b64435e7ee3260668531aee0f2d8`，`association_errors()`中`returned["binding_ref"] != binding_ref`。
- 现有协调者source/selected/loads、local Git取源及现行association调用端。复用实际解析器，工程师沿真正依赖定位，不另做一套。
- `runtime/dual_route_execution/DR14_QUESTION_WORK_CONTRACT.md@11626f64bc64ae21e52108b2e47fafbbc1023615` §1.4与§2：正确引用可以是锚点/行范围，原回答载体不可偷换，真实冲突才走责任者补交。

实际原件：
R4 INVOCATION/PROMPT/两份Return与原答在本run `provenance/turns/R0004/`；原完整回答锁`378d476a2513c126bc7dc57a54c8e452fd170b11`，SHA256 `0c95743ca09496d95790a8a826ef763159ff873868f7e2b4216b909df412d7ad`。
原Binding是`81533abbced55b3af14a428dec9cbf8353fc8286:runs/BI-01-V2-01/01_当前任务.md`，实际派发selector `L124-L177`，Return使用`#question-work-binding`。旧故障全文锁`168994b58dac1155cc1a15c9e62437428d46a335:provenance/turns/R0004/RETURN_LOCATOR_ISSUE.md`。
所有省略本run前缀的路径均加`runs/BI-01-V2-01/`。读取精确旧派发，不用新HEAD替旧Binding。

<a id="contract"></a>
## 3. 行为合同与自由度

保留字面相同正常路径。selector字面不同，仅在同repo/40位commit/path且真实解析落在该原文件同一完整、唯一的Binding对象时允许等价；校验全部对象内容和原work/题组/权限/路由关联，不能只比一个hash/名称或接受任意位置的相似JSON。

不同repo/commit/path不得仅因JSON相等放行；selector不存在、多义、多个JSON块、截断或内容变化、原引用不可取得均维持拒绝/明确缺件。解析不能吞掉正文歧义，也不能从正文猜新业务权限。不引入跨版本“最近相同”策略，不把当前task与旧派发等同，不忽略token/Invocation/Return身份、question_work_ref及同一原回答锚点作用域。

R4 FULL_RESPONSE、ROLE_RETURN、QUESTION_WORK_RETURN、原INVOCATION/DISPATCH、COLLECTION/CONTROLLER错误原记录均原样保留；新验证记录附在本单技术回交或既有新的实际检查记录，不倒改旧错误为成功。可在机械验证内部使用经核实的同一目标表示，不把这种表示发布成作者修订过的原Return。

函数入参/可选resolver/公共helper/调用适配怎样安排由工程师依据现有代码决定。直接比较消费者、测试和实际调用闭环一并修通，不只改一个函数使另一条路继续卡住。正常依赖、表示/编码、工程选择、回归、调用与结果核验可连续处理，不逐错误回Pro。不要把纯解析器升级成业务裁定器或新公共运行时项目。

写面是observe-iterate既有V2工作分支上的相关runtime及必要测试/直接说明；这是起点而非封闭文件白名单。保留其他写者提交，只普通快进。不得改Owner/业务Task/Binding、原市场数据、aidata、cgpterm公共手机协议或正式业务资格。新实质语义/权限冲突才回管理。

<a id="checks"></a>
## 4. 必要验证与实际回用

使用已有tests/fixtures：正例为完全相同locator和本次同文件锚点/行范围同一Binding；负例覆盖错误文件/commit/内容/缺失或不完整selector、多JSON/歧义、错误Invocation/token、其他原关联冲突；原BOOTSTRAP、正常专业/独立读者、同回答continuation/remaining和after-return不回归。源不存在不能被当作相等，synthetic测试不伪造真实Owner/reader历史。

发布并fresh回读修补代码后，从真正执行的新代码版本对真实R4原件运行两条关联路径和BI01 after-return，记录原错误、实际新结果和所用源码commit。原题面policy_commit仍11626...，不因代码修补静默更新业务方法。R4不是重发，不能再IME/Send；R5的新Return也要按它自己的真实Invocation核验。

工程命令以已有测试入口为准；不为数量创建大测试框架，不跑无关特征编译或重算。修补完成后回到本次DECISION#adoption的two-commit snapshot/Intake/check和真实专业续作派发，不能以单测通过作为当前工作主动停点。

<a id="return"></a>
## 5. 回交与边界

技术回交写`runs/BI-01-V2-01/reviews/management-R0005/WORKER_RETURN_LOCATOR.md`：本工单/实际执行者、源码改动及commit、实际命令/测试结果、真实R4回用结果、未执行/限制和后继；原文保持证据。此为技术自检，不是独立业务审查或S3完成。

本地工程不计新R。该修补和Intake一旦实际通过，即把已经到达的146CSV当前图数据和其版本/来源交原BI01-V2-执行继续完整S2/S3；不再派只改selector的Pro。确有实际不能修通的错误时给已试动作、直接影响和必要决定回本管理；不无限重复同一机械错误。未受影响图数施工持续，首图专业消费后原完整工单仍继续。
