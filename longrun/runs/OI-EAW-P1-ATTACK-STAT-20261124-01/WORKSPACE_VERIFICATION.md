# Attack copy 工作区释放对账与基线核验

Owner 本次 GO 明确“之前使用的 copy 工作区已经释放”，并指定 /dwdhome/fy/BASE_E6_2_copy；此为本次资源采用的最新依据。已与现场核对：旧 F800 manager/executor 最近真实 turn 已 completed、当前 notLoaded、队列为空；定向检查未见旧 F/Q/V 或该 copy 工作区任务进程。原共享主控仍 Owner paused、原计划 cancelled/timer inactive，未恢复或强停旧线程。旧 F800 的业务暂停和历史成果保留；仅其旧工作区预约按本次 Owner 释放信息解除，不将其专业工作写作完成，也不改旧 Run 的既有记录。

本机 realpath 分别为 /dwdhome/fy/BASE_E6_2_copy 与 Build 的 /dwdhome/fy/BASE_E6_2，互不重叠。两个 TIS git common directory 独立。共享重型生产锁在本次非阻塞探测未持有；Build 当前执行 U、未运行正式生产。两 Run 后续若触及相同数据库/缓存写面，仅该具体写入按既有共享互斥串行；独立读取与 U/统计/诊断不由另一 Run 阻断。

copy 原先为干净的 codex/save-copy-workspace-20261124，HEAD 2b4af7d32f0b353f30e575266ce9a028b101cd5f；不是本次指定源码。确认无未提交/未跟踪文件、无同名现役修复分支/写者后，已保留原保存分支并以普通 git switch -c 从179016111ed0394f92025313e46bd13534932a74创建本次专用 codex/oi-eaw-p1-attack-fix-20261124-01。原保存分支和 Build checkout 均保留，未清理或强推。

切换后的 HEAD 正确、工作树干净；Attack/Wall assembler 及 core 文件与锁定 commit 逐字一致。通过本工作区已有 run-python.sh 做只读模块导入，命令真实 exit 0；Attack 与 Wall 的 __file__ 都落在 copy/mquant/tis/hf/prel0/。没有执行 Feature，未以模块导入冒充正式 X。

正式GitHub权限沿用同一已核Personal连接；新目标分支经精确查找无现役同名者。copy原origin仍保留，目标GitHub修复分支独立。现役App Server与真实peer已核；model/list包含gpt-6.1-sol和max。copy config/read为danger-full-access、approvals_reviewer=auto_review、approval_policy=null；新角色还需真实创建与回合读回，不假定Owner GO已批准所有外部动作。

same code/ppdict/data scope下的exact Wall及F4 tactical/structural receipts、完整参数和公开结果读回尚未验实；若缺少可按初始授权由executor合法物化。旧WALL未完成合理性Release；本记录不改变此事实。

原始Owner附件8515 bytes，sha256=02d6c8c9674a2a63329b36ad9846b2af84288b04ffa3a79881685937c5a3320c；完整原件、真实角色/进程/锁/配置/模块路径证据只存gitignored controller artifacts。此核验支持控制层注册和新角色创建，仍不代表Attack正式参数、技术上游或业务结果已验收。
