# W001 前置操作日志

- ENVFIX1 前三次 exec_command 在 bwrap uid-map 阶段 exit=1，无本机命令运行或写入；工具块：最初失败、ba49fd、b92331。
- ENVFIX1 后工具块 28da72：pwd、全文读取本地 ORDER.md、sha256sum 均 exit=0；hash 匹配。
- 224d77：读 INPUT_MANIFEST、启动器和 long-task-status skill。
- bfb3cb：PID/start_ticks/inode 匹配；初次 shell 只读FD竞争探测被 flock 以 Bad file descriptor/65 拒绝，未形成锁竞争证明。
- 143e55：更正为现有锁的 O_RDWR 无截断打开，fcntl LOCK_EX|LOCK_NB 以 errno11 拒绝；/proc/locks 确认 holder296712/inode13765718。没有写锁文件、夺锁、清锁或操作 release.flag。
- e84076/6d1891：只读检查原实例脚本、m3rc命令形态、状态工具写路径及Linux注册分支。原 run-python.sh 会截断W目录外迁移日志，未直接执行；W内调查副本只适配工作区定位与日志路径，见 launcher.diff。
- 首次W目录写入前已取得上述租约证据；后续命令由 command.py 在每次执行前复核，COMMANDS.jsonl 记录实际命令和归属。
- 原输入脚本未执行、未复制其全窗口读取和计数逻辑；后续调查脚本独立编写，使用相同候选上下文和缺产物停止约束。
- 所有前置命令已结束，无在途命令；前置调用没有单独测量的子阶段时长不补造。
