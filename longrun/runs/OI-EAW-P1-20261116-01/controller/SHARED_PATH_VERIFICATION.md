# Windows↔Linux 共享路径现场核验

本次在 Owner 明确允许新 Run 接管 BASE_E6_2 后，用本 Run 独立 handoff 内的同一相对文件完成正式 MCP 双向实际验证。

- Windows 根：H:\fy；Linux 根：/dwdhome/fy。
- 本 Run Windows handoff：H:\fy\BASE_E6_2\.runtime\observe-iterate\OI-EAW-P1-20261116-01\handoff\。
- 本 Run Linux handoff：/dwdhome/fy/BASE_E6_2/.runtime/observe-iterate/OI-EAW-P1-20261116-01/handoff/。
- Linux 写出唯一测试原件；正式 MCP stage 从准确 Windows 对应路径读取成功，写入本 Run 唯一手机目录。
- 正式 MCP pull 把同一手机原件写到唯一新的 Windows 返回文件；Linux 对应返回文件实际存在且可读。
- 原件/返回件均为75字节；逐字节相等；SHA-256均为45ed4d7ffa09e09d2c290d2e4c7fb9dc6e59a40534f544e6214db53672412fae。
- 两次 MCP 均终态；没有覆盖、聊天输入或发送，pending/unknown为0；控制已真实释放。精简实际收发与锁回执保存在gitignored主控运行目录。

结果：候选根映射在本次独立目录与测试文件上双向验证 PASS。此结果不是数据ZIP已转移、任意H:\fy路径可写、Pro已读取或专业DATA_READY的证明；后续每个ZIP仍须实核原件和SHA。
