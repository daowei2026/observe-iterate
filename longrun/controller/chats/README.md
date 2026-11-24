# 主控 Chat 归档索引

此目录专门保存由当前 cgpterm Controller Skill 自动生成的**主控 Codex Chat** 记录：

```text
<controller-thread-id>.md
```

每份记录对应一个经核实的主控物理线程，可跨多个 Run。正文只包括用户与主控 Assistant 的可见文本；不包括 manager、executor、Worker 的 Chat，也不包含工具调用和内部推理。主控之外各专业角色已通过正式 D/Return、报告和运行产物在各 Run 目录中留痕，不再重复转录聊天。

写入方式由 `daowei2026/cgpterm` 当前采用的 `observe-iterate-longrun-v2-controller` Skill 规定，具体 [归档规则](https://github.com/daowei2026/cgpterm/blob/feat/observe-iterate-codex-native-direct-20261122/.agents/skills/observe-iterate-longrun-v2-controller/references/controller-chat-archive.md)。

## 状态解释

此 README 只提供阅读入口，**不是聊天原文，也不表示已成功归档任何真实主控 Chat**。当前仓库中的 `<thread-id>.md` 只有在受授权的主控真实调用只读读取接口、完成文件更新并推送 GitHub 后才会出现。

如果自动归档失败，主控应记录待同步原因、准确线程和恢复条件，不能提交离线 fixture 或其他角色的对话冒充主控记录；仍可继续不依赖归档的业务工作。
