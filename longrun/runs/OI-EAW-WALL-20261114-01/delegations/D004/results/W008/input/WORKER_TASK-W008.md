[OI-EAW-WALL-20261114-01-W008-FIRST-DISPATCH-01]
你是原专用Worker W1，现在执行原E1 C0017已正式签发、主控已核验的全新W008/D004。本消息不是W007恢复、重发、steer或测试Run。旧D3/W7已由原manager C16及原E1 C17合法SUPERSEDED，旧W7物理STOP和85原件保留，不补造W7 Return。新Owner A001前瞻变更已生效，旧隔离工程绝不作为前置。

完整原工单必须阅读，不以本主控定位正文代替：
MD逐字镜像：/dwdhome/fy/cgpterm/artifacts/oi-eaw-wall/OI-EAW-WALL-20261114-01/C0017-pin-ORDER.md
JSON逐字镜像：/dwdhome/fy/cgpterm/artifacts/oi-eaw-wall/OI-EAW-WALL-20261114-01/C0017-pin-ORDER.json
MD ref：daowei2026/observe-iterate@dee27c90b8bd95c949387c1b6604eeda6d22b773:longrun/runs/OI-EAW-WALL-20261114-01/work_orders/W008/ORDER.md
JSON ref：daowei2026/observe-iterate@a61efeed234064599011ebc897e4da61928c2403:longrun/runs/OI-EAW-WALL-20261114-01/work_orders/W008/ORDER.json
签认原E1 Return原文：/dwdhome/fy/cgpterm/artifacts/oi-eaw-wall/OI-EAW-WALL-20261114-01/C0017-pin-PRO_RETURN.json
Return ref：daowei2026/observe-iterate@fad0e1fcdab93d9091f546fe153ba8300ef1f412:longrun/runs/OI-EAW-WALL-20261114-01/calls/C0017/PRO_RETURN.json

24份精确输入逐字远端回读、Gitblob/bytes/SHA核验后镜像在：/dwdhome/fy/cgpterm/artifacts/oi-eaw-wall/OI-EAW-WALL-20261114-01/W008-INPUT_INDEX.json。索引列每份exact ref/本地绝对路径/bytes/hash，不猜路径或改用旧版。包括D4、新Owner原文/授权、C16决定、C17closeout/材料计划/WORKING预期及D1/D2已接受资料、dc18a版control02/03/角色指南。按当前W所需完整消费对应原件；原Worker更早上下文中的旧W指令、隔离、closure、四PASS/八EP整包前置均不得带入新W。

实际执行context：原thread01a1da55-5881-7590-94a1-0661f0236977；actual gpt-6.1-sol/max；cwd /dwdhome/fy/BASE_E6_2。主控仅在同原owner加载idle原聊天准备NEW W8，旧W7turn始终completed，Goalnull/queueempty，未恢复旧Goal/turn。Owner A001及D4新增Linux grant逐字：
operation=wall-observation-work execution_context=linux:/dwdhome/fy/BASE_E6_2 allowed_writes=/dwdhome/fy/BASE_E6_2

直接使用BASE已有源码、数据、构建环境和工具。本W业务主要新根=/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008。根尚未被业务写者创建；由你本W按工单新建。已有业务源码本W只读，不复制到独立源码树，不建设Landlock/seccomp/全局零外写/独立clean closure。不重跑任何旧W7 command、不恢复旧W7，不重做W1–W6原件。现有BASE正常build/cache路径按ORDER事前列位置/预计影响、核实际竞争、事后记变化；此新D4锁不宣称锁住全部BASE。现有源码不编辑，唯一阻断确需小改则交BASE_CHANGE_CANDIDATE，不实施。真实HOME/CODEX_HOME保持，新增业务文件留BASE/W8，必要临时/导出优先本W根；不要写Root cgpterm或HOME临时业务文件。

资源收束真实证据（先核hash后只读消费，逐字保留本W原件；不得伪造为你自己释放）：
/dwdhome/fy/cgpterm/artifacts/oi-eaw-wall/OI-EAW-WALL-20261114-01/W007_LOCK_RELEASE_PRE.json
/dwdhome/fy/cgpterm/artifacts/oi-eaw-wall/OI-EAW-WALL-20261114-01/W007_LOCK_RELEASE_POST.json
/dwdhome/fy/cgpterm/artifacts/oi-eaw-wall/OI-EAW-WALL-20261114-01/W008-W007-frozen85-current-verification.json
/dwdhome/fy/cgpterm/artifacts/oi-eaw-wall/OI-EAW-WALL-20261114-01/W008-originalW1-readonly-pre-resource.json
/dwdhome/fy/cgpterm/artifacts/oi-eaw-wall/OI-EAW-WALL-20261114-01/D004_W008_LOCK_BINDING.json
旧W7锁原PID251010/startticks48763578/inode14806399已实际释放，Root PTY输入工具策略拒绝后，按ORDER1.3核准仅承担锁的keeper身份并用pidfd SIGTERM结束；04:55:51.015714Z原PIDgone、kernelFLOCKgone、独立同inode竞争成功，85原件未变，精确内核unlock时刻未知，不伪称keeper cleanexit0。详细原件Root已有，无须再次做旧工程测试。

本W新真实排他锁由Root持有，唯一你为业务获准写者：
lock=/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/.D004-writer.lock
holderPID=255320 startticks=49586940 inode=14866078 fd3 session17409
主控真实竞争失败/内核FLOCK/PIDticks证据见D004_W008_LOCK_BINDING.json。先只读核Root holder仍为同实例/同fd/inode且独立O_RDWR|O_NOFOLLOW同inode flock(EX|NB)竞争应EAGAIN（NFS不要用O_RDONLY导致EBADF），不要替换/释放主控锁。Root持有是本W的排他保障，不是另一个业务writer。缺资格则STOP受影响写操作并回报，不另建第二个writer。

请创建仅本W8本地执行的有限Goal，实际持续完成工单两lane：只读核旧W7证据和真实收束receipt；按新control02原Skill0～7事实操作，在liveBASE复用existing reader/test/trace/runner，实际尝试current binding、最小controlled normal chain、reader，existing低成本高区分入口存在时至多两scenario。完整exactcommand/cwd/输入输出/版本绑定/exit/耗时/bytes/可见副作用和命令日志均记录。每个子动作按ORDER有界（不沿用旧cap/四PASS）：运行前列输入范围、输出位置、停止法；不full-year/unbounded计算，不覆盖现役成果/他人未提交修改，不破坏性Git或正式源码push；某条失败继续其他合法独立项，不盲重试unknown动作。若预计需大范围高成本搜索按用户规则先报告边界，继续可做小范围，不自行全盘扫描。

Worker只交事实/实物及准确原始material标签，材料专业可用性/必要性最终资格、expectation freeze、正式comparison/SUPPORTS/COUNTERS、父Q、H3和最终D3专业关闭由原E1/manager决定。当前预期仅WORKING，不帮专业角色后见冻结。不得只交PLAN_READY或源码定义冒充取得数据。源/controlled/static/natural证据类别精确区分；未取得项和局部失败据实missing。

你无本W GitHub写授权，先冻结实际本地原件，交完整manifest、bytes/SHA、outcome/missing/ORDER deliverable→本地文件映射以及准确出版目标：longrun/runs/OI-EAW-WALL-20261114-01/delegations/D004/results/W008/。非UTF8材料如实标类型/bytes/hash，不改原件冒充UTF8。Root会逐字运输实际文件并核真实远端refs/hash，再回原W1同W8仅生成正式WORKER_RETURN.json；准确正式路径为worker_results/W008/WORKER_RETURN.json，return_to原E1，不直接manager。真实出版refs尚未有时不得造future/self refs或假Return。无材料不造空数据文件。原件freeze/HASHES/PUBLICATION_MANIFEST要求同工单，数据量不虚报为零。

主控锁会保留至所有本地及同单正式Return写者/命令终态，由Root真实释放。本地阶段Goal完成只表明本地文件就绪，不等于W/D/父任务完成。请本地有限工作结束后自然回交，不常驻轮询、不向任何其他聊天发消息。
