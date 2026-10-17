# R0005 定位适配 Worker 技术回交

工单 `BI01V2-R0005-RETURN-LOCATOR-FIX-01`；执行者为原操作 Codex 线程 `01a14a59-7f26-7921-b549-3e7cd9be5119`，按管理5e05e1e签发的本单Worker容量执行。只处理现有回交消费者，未新增Pro R或手机发送。

R4原派发行号与原Return锚点实际指向同一原Binding，却被两处字典字面比较拒绝。代码 `73789662405ec2bfb5c516f849de3450d1160593` 已提交推送，六文件fresh远端原字节回读通过；方法policy仍锁11626f64bc64ae21e52108b2e47fafbbc1023615，操作cgpterm仍锁a65739e8adecfa1e6c09d97a11a1b020bf765126。

## 改动与严格边界

复用management_prompt现有source/read_git/selected/loads，取得selector内唯一完整Binding及原blob/JSON字符区间。question_work_check的association_errors可接实际binding_resolver；bi01_run_gate.after_return已接同一解析及比较。严格要求同repo/40位commit/path、原文件内同一JSON位置和全部对象内容相同；association同时与实际已解析Binding对象核对。不同来源、版本、路径、对象位置、内容、缺失、多义、多个JSON、重复键、截断和不可取得源均拒绝。身份/token/question_work_ref/continuation/remaining检查保留，不能用解析成功覆盖其他冲突。无resolver的既有已解析字面相同调用保留兼容，selector差异不会在无源证明时放行；实际R4回用明确提供resolver。

未改schema、Owner目标、Task/Binding、市场数据、aidata或手机协议；未创建别名登记或另一运行时。R4 FULL_RESPONSE、两Return、INVOCATION、DISPATCH及原错误记录均原样保留。

## 实际验证

- 直接BI01回归16项通过（含新增三个分组及其正负subtests），Workmap一致性2项通过。包括锚点/行范围同原对象正例、相同内容不同位置拒绝、错误source/version/path/selector、重复JSON/键/锚点、身份/token及原回答引用冲突。原BOOTSTRAP/reader/professional与发送安全检查继续覆盖。
- question-work 35项中34通过、1旧试跑文件不可取得；原d8430e6代码实际复跑仍同1错误。coordinator旧A/B/C套件41项为10失败31错误，原d8430e6源码实际复跑同结果。startup来源9项中8通过，唯一失败要求NOT_CONFIGURED，而本run已经真实ADOPTED；测试及config未改。不将这些已有不适用/缺件检查称绿色，也不撤销真实采用来满足启动断言。命令及事实见 LOCATOR_TESTS.json。初次新增测试曾因重复提交空改动失败，修正测试提交条件后完整16项重跑通过，初次日志保留在gitignored现场证据。
- 从fresh回读后的7378966实际代码对真实R4原件运行：原文37,049字节、SHA256 `0c95743ca09496d95790a8a826ef763159ff873868f7e2b4216b909df412d7ad`，三原件逐字节与378d476相等；准确同回答question-work锚点仍解析为原Return。旧字面比较仍复现BINDING_MISMATCH；提供实际resolver后association_errors为空，BI01 after-return实际exit0/ok=true/errors=[]。两locator对应同原blob/字符区间及全部Binding，详见 LOCATOR_R4_REPLAY.json。旧失败记录未倒改。

R5实际Send回执另补齐原消费者必需的state=COMMITTED字段，依据同一实际17-send-once证据，正文/时刻/hash/次数不变；尚无完整R5回交时不提前签R5 after-return。

## 未完与合法后继

本单代码及真实R4机械回用已成，原R4有效结果现累计4份；不是独立专业审查、S3或全run完成。原aidata Worker工单持续在途，不被此工程替代。管理R5完整原答/Return/turn complete仍待实际收取，按该调用自己的Invocation核验。

按管理实际DECISION#adoption办理上一采用基准81533...的两提交snapshot/Intake/check/dispatch，保留旧reader输入原件及本次routine理由；真正通过后立即把已到当前146CSV包和源引用交原BI01-V2-执行继续S2/S3，不重派只改selector的Pro，不等320视图全部结束。后续新到实物分别辨明版本及尚未消费范围。
