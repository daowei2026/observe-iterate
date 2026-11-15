[OI-EAW-WALL-20261114-01-W006-FIRST-DISPATCH-01]
你仍是本真实Run原物理Worker W1，仅执行原E1 C0014正式新签W006，不新建Worker、不另安排测试Run。Owner已授权本Run必要源码调查/数据读取/隔离工作与归档；主控独立validate-executor-return与validate-order已通过，真实fresh独占另有现场证明。Root不预定结果，你须按原工单真实执行。

## 完整原件、准确采用及输入
必须完整读取并交叉核对，不以此控制消息代替：
- /dwdhome/fy/cgpterm/artifacts/oi-eaw-wall/OI-EAW-WALL-20261114-01/C0014-remote-work_orders--W006--ORDER.md
- 同目录 C0014-remote-work_orders--W006--ORDER.json
- 同目录 C0014-remote-calls--C0014--PRO_RETURN.json
- 同目录 C0014-remote-delegations--D003--results--W006_SUCCESSOR_DECISION_C0014.md
- 同目录 C0014-remote-delegations--D003--results--D003_W005_PROFESSIONAL_REVIEW_C0014.md、EP_ACCEPTANCE_MATRIX_C0014.md、D003_EXECUTOR_PROGRESS_C0014.md（后三者都以前述C0014-remote-delegations--D003--results--为文件名前缀）。
ORDER JSON精确ref：daowei2026/observe-iterate@050e7050a615709eadd10e811a75ad5a128db533:longrun/runs/OI-EAW-WALL-20261114-01/work_orders/W006/ORDER.json
ORDER MD精确ref：daowei2026/observe-iterate@b2f1af95604f5f690d1021f75553323737ccc552:longrun/runs/OI-EAW-WALL-20261114-01/work_orders/W006/ORDER.md
签单Return精确ref：daowei2026/observe-iterate@a9ae3b8a94b1dbfdef69ab2c5d048ab36f353cb3:longrun/runs/OI-EAW-WALL-20261114-01/calls/C0014/PRO_RETURN.json
全部34输入的精确ref→只读本地镜像或exact Git对象/hash映射：/dwdhome/fy/cgpterm/artifacts/oi-eaw-wall/OI-EAW-WALL-20261114-01/W006-input-mirror-index.json 。26本地原件本次已bytes/hash复核，8exact源码Git对象映射沿用已核不可变commit/hash，非本W新读取事实；你按工单Gate在需要时读取核对，不能在未做时称已读。禁止shared git checkout/reset/clean/pull/fetch/merge或写index/worktree。
专业/控制协议采用daowei2026/observe-iterate@ca7fdae84f65265332e3a53865724a2615508766，主控采用daowei2026/cgpterm@06eda7c9bed88ab1c35de1ff7e9e470bef341bab。本地只读协议/schema/Gate位于同B/observe-iterate/longrun/，不能修改。

## 实际物理资格与写面
原物理thread01a1da55-5881-7590-94a1-0661f0236977，实际gpt-6.1-sol/max，cwd /dwdhome/fy/BASE_E6_2。原W5本地及正式turn均completed/Goalnull/queue空，旧holder PID246047 gone、旧锁已释放。新W6root派发前不存在，由你验证后在合法单写资格下建立：
/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D003/W006
所有本任务新增业务脚本/source/staging/fixture/tmp/cache/config/build/log/trace/artifact只可在此真实子根。Owner Run根token仅运输表示，不授予写任何兄弟目录。B/cgpterm、W1–W5、shared源码/配置/数据/正式产物均只读。真实HOME=/home/dw、CODEX_HOME=/home/dw/.codex不重设、不新增业务写；Python -B等防外部pycache，任务临时缓存必须支持显式新root，否则STOP。procfs没有外写例外。

全新W6 rootkeeper独占仍HELD：root PTYsession91789 / PID248632 / startticks48206357 / inode14806399 / fd3，path /dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/.D003-writer.lock，cover整个D003及本W6。证据W006-lock-holder.json、W006-lock-competition-proof.json、W006-worker-loaded-context.json，均同B目录。先现场核新holder PID/startticks/inode/fdinfo FLOCK，并用existing-file O_RDWR|O_NOFOLLOW独立open-file-description作LOCK_EX|LOCK_NB竞争失败；不写内容，不重取/删/替换/释放主控锁。只关闭自身独立FD，不动holder。不得使用W4/W5旧PID/root值。

## 主控精确sentinel原件
主控已2026-11-15T01:07:47.641590Z对精确对象唯一一次有界只读lstat得ENOENT，create/write/delete0，cleanup notneeded：
/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D003/.W006-deny-outside-C0014-259834ad
原回执 /dwdhome/fy/cgpterm/artifacts/oi-eaw-wall/OI-EAW-WALL-20261114-01/CONTROLLER_SENTINEL_PRECONFIRMATION-W006.json
UTF8 bytes=609，SHA256=65b582f61d9a426f5dd860351ca81645a9bdbd54033fde9bb498c03de119aeac。完整读取并核bytes/hash，逐字存本W的CONTROLLER_SENTINEL_PRECONFIRMATION.json，引用于W006_BINDING；主控未创/写/删，也不让你预建或清理。该回执只是事前不存在，不是kernel拒绝或confinementPASS。其他精确SHARED/HOME/CODEX/symlink负目标由你按ORDER在policy前只读核不存在。

## 有限任务与失败边界
创建原生有限Goal，仅本W6本地执行与原件交付，不设token budget。持续实际执行到本地阶段终态，不逐项等Root许可或要求进度问询。
严格按ORDER P0历史两阶段分类→P1本机常量/layout→P2 fresh runtime/launcher/BPF→P3 pure evaluator/jump/路径终止/非ioctl等价。保留W5错误脚本冻结，不用所有历史FIOCLEX均EPERM断言。W4 trace exactSHA/line312前成功和line1509后EPERM分别保存，历史不替代当前static/kernel。
P0–P3全PASS才一次R0-A1；only verified FIOCLEX request且高32位0例外，其他ioctl/arch/x32/PR_SET_NAME/network/metadata/Landlock等安全规则保持。显式O_RDONLY stdin和继承FD规则不放宽。任一新static/kernel/bootstrap/probe/unknown/outsidewrite失败据实STOP，不自动修改/重试或扩大allowlist。A PASS才单一兼容offlineclosure，A/B PASS才四预算/continuousmonitor，四PASS才条件八EP。cap/全部禁令按完整原件不减。
禁止任何single/partial/full场景、normal、DBA、wrapper、native-reader、current/production材料、共享源码写/push、改production语义或旧assertion。没有四PASS，不建空条件成果；没有实测不冒称PASS/全局零外写。准确记录独立成功子事实与未执行缺口。

## 两阶段交付与运输
W6只下放Linux wall-observation-work，你不向GitHub写、不向其他聊天发消息。完整命令输入/退出/会话/trace/审计/原件/hash/逐字deliverable映射/manifest/缺项都在本W，禁止凭据、大型cache/binary或生产数据出档。
本地终态先冻结所有真实原件，给全文件绝对路径、bytes/hash/mtime/inode及明确出版目标：longrun/runs/OI-EAW-WALL-20261114-01/delegations/D003/results/W006/。真实GitHub commit未有时不造ref/future/self ref；本地result_ref可保持null并准确待出版。主控逐字出版全部真实文本原件并远端核后，把真实refs回同原W1同W6；你仅在W006/final-return新增正式longrun-worker-return/v2与validation，再由主控逐字运输到longrun/runs/OI-EAW-WALL-20261114-01/worker_results/W006/WORKER_RETURN.json及validation同目录。return_to只原E1，不直接manager。
主控新W6锁保护本地及后续同单正式Return，所有写者/命令终态前不释放。结束报告真实outcome/missing、全部原件/hash、阶段结果及出版/正式Return待办；有限Goal完成只表示本地交付，不等于W/D3/父任务完成或专业接受/G-RUN/H3。待真实出版refs时自然结束，不常驻轮询、不重跑旧调查。
