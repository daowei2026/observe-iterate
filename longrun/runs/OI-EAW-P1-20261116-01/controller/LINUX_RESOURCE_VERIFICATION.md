# Linux 现场资源核验

- 本 Run：OI-EAW-P1-20261116-01；目标为当前实际 Linux 主机的 /dwdhome/fy/BASE_E6_2。
- 目录真实存在；realpath 为 /dwdhome/fy/BASE_E6_2，未解析为其他目录；当前主控账户具有基础读取、写入、穿越权限。
- 已核 /、/dwdhome、/dwdhome/fy、BASE_E6_2 的适用 AGENTS.md 文件入口，本次未发现附加文件。
- 两个旧 Wall Run 的准确暂停指令、stopped scheduler 与已释放的 Worker/写锁记录已核。Owner 后续明确允许新 Run 接管、旧 Run 保持暂停，原文见同目录 OWNER_WORKSPACE_TAKEOVER.md。
- 在 Owner 确认之后才创建本 Run 独立 handoff 目录 /dwdhome/fy/BASE_E6_2/.runtime/observe-iterate/OI-EAW-P1-20261116-01/handoff/。目录解析仍位于指定 BASE 内；已实际写入唯一75字节共享测试原件。未创建/复制其他 BASE 工作区。
- 共享测试原件 SHA-256：45ed4d7ffa09e09d2c290d2e4c7fb9dc6e59a40534f544e6214db53672412fae。Windows 对应路径的真实读取和返回写入正在正式 MCP 的独立 episode 核验，未预先声称通过。
- 尚未创建本 Run Worker 物理线程；首次 W 前必须核其真实 cwd、模型、当前 turn 与单写者资格。逻辑角色不代替实际线程绑定。

这是路径、权限与接管依据的现场记录，不是 Worker 已运行、共享通道已通过或专业材料已接受的证明。
