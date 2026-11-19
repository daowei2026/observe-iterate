# OR001 第一项的预先选择授权采用记录

Run：`OI-U2-F-OBS-20261118-01`；原工作 `D005 / WI-E / M-E`。

## 真实来源及选择

Owner 在本聊天预先给出的原文为：

> 碰到需要我处理的问题，先选第一项

E 原生正式请求为：

`daowei2026/observe-iterate@6f2fb38d8ff7e45c1ae6e234eaf2c95b215ee4a9:longrun/runs/OI-U2-F-OBS-20261118-01/owner_requests/OR001/REQUEST.md`

该请求第一项原文为：

> A. 确认首选 sem.* 机读补正；

本记录是主控按 Owner 既有选择指令采用 OR001 的 A 项；不是一次新收到的逐字 INI 确认。Owner 原话、专业请求原文与主控形成的授权映射分别保留。第一项可被当前采用的 V2 Schema 表达，无需采用更宽的目录前缀选项。

## 本次精确授权映射

以下整段作为新 Binding 对应 grant 的 `authority_quote`：

```text
Owner 预先选择指令原文：碰到需要我处理的问题，先选第一项
适用请求：OR001；被选择的第一项：A. 确认首选 sem.* 机读补正；
operation=caegraph_run_and_repair
execution_context=/dwdhome/fy/BASE_E6_2_copy
allowed_writes=/dwdhome/fy/BASE_E6_2_copy/**,/dev/shm/sem.*
`/dev/shm` 只允许本 Run 的 CAEGraph 运行进程及其子进程为 Python multiprocessing 临时创建和删除 POSIX semaphore 对象 `sem.*`；不得写任意共享内存 payload、不得使用 sudo、不得建立 mount 绕过、不得 patch 平台源码、不得调用 F producer、不得读取 Q/V、不得据此启动正式数据导出。
```

这是 `caegraph_run_and_repair` 的操作级补正；`caegraph_data_export` 仍仅沿用原工作区授权，本记录不授予正式取数准入。新 W 仍须由原 E1 按 E 原生 Workflow 签发，并由主控核真实权限、物理绑定及共享写面。

## 已有来源和历史

- 原 GO：`daowei2026/observe-iterate@74ed0b11552f73b03e55e3e324f8325889730b52:longrun/runs/OI-U2-F-OBS-20261118-01/OWNER_START.md`
- 已确认路径补正：`daowei2026/observe-iterate@c47a984fb060182d691cc71e983a7bc55e9ce5a2:longrun/runs/OI-U2-F-OBS-20261118-01/OWNER_AUTHORITY_AMENDMENT_20261119.md`
- 旧 Binding/Resource：`daowei2026/observe-iterate@4d2eb6058babf47db130a6b7f5ed6e7c9d48cbda:longrun/runs/OI-U2-F-OBS-20261118-01/RUN_BINDING.json` 及同目录 `RUN_RESOURCE_BINDING.json`。
- C0016 Return：`daowei2026/observe-iterate@616497e3b3eb6f231c6b04f3218ea7ceea0e32b9:longrun/runs/OI-U2-F-OBS-20261118-01/calls/C0016/PRO_RETURN.json`。

A～D、已签发 D/W、旧 C、W001/W002 结果及原授权快照全部保留。E 尚未完成。Q 继续 Owner hold，V 未启动。
