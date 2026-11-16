# 启动预检｜OI-EAW-P1-20261116-01

本记录由主控保存运行事实，不替 manager 判断业务范围、证据资格或 Gate。

## 当前状态

- Owner 已明确 GO：`business_case_id=EAW-P1`、`work_id=OI-EAW-P1`、`run_id=OI-EAW-P1-20261116-01`。
- 拟用分支：`runs/OI-EAW-P1-20261116-01`。主控在可信索引和相关远端 Run 分支检查中未发现该身份已被登记。
- 正式注册尚未完成；`RUN_BINDING.json`、`RUN_RESOURCE_BINDING.json` 与 Registry 尚未发布。专业实际调用 0，Worker 派单 0；没有本 Run 未知或在途 Send。首次 manager 任务只有本地未编号草稿。

## 采用来源

- V2 主控：`daowei2026/cgpterm@034da33b774d7e3db50fcdda219a64d4ed0281be:.agents/skills/observe-iterate-longrun-v2-controller/SKILL.md`，已读取固定版本及其多 Run 操作卡。
- 业务 Control、长程协议及专业方法：`daowei2026/observe-iterate@7e240b650b6ba6274b0263e34f5b0616a9a8ff1c`，实际角色使用同版入口，不混用旧 ROLE_RETURN。
- 完整任务和原始输入 exact 引用保留在 `OWNER_START.md`，不以本预检摘要替代。

## Linux 工作区与旧 Run

Owner 指定 `/dwdhome/fy/BASE_E6_2`，实际目录存在，realpath 为该路径，主控当前账户具基础读取、写入和穿越权限。尚未创建或绑定本 Run 的实际 Worker。

可信索引、旧主控最近实际 Owner 指令和现场接续记录显示：

| 旧 Run | 已核状态 | 本次复用的未决事项 |
|---|---|---|
| OI-EAW-WALL-20261114-01 | Owner 手动暂停；scheduler stopped；业务未完成；Worker 与写锁有释放记录 | 原绑定仍指向 BASE_E6_2，未得到本次接管决定 |
| OI-EAW-WALL-20261116-01 | Owner 原文“上述长程任务先暂停”；scheduler stopped；业务未完成；Worker 与写锁有释放记录 | 原绑定仍指向 BASE_E6_2，未得到本次接管决定 |

采用的多 Run 操作卡要求与“当前未结束 Run”核工作区重叠。本主控已向 Owner 提出一个准确问题：允许新 Run 接管 BASE_E6_2、旧 Run 在解除占用冲突前保持暂停，或为新 Run 指定另一已准备的工作区。当前尚无答复。本次没有恢复、改写或派发旧 Run，也没有向 BASE 写入新文件。

## 脚本和数据实际取得

- 固定原始脚本 ZIP 已在主控本机读取：31,319 字节；SHA-256 `5eaf500616316ef7764cd30eb7467f2db3a6c85e45aa3b4f958becbc7818e8eb`；ZIP CRC 通过，四成员及各自 SHA 与输入清单一致。Worker 尚未取得，脚本未在本 Run 执行。
- 准备聊天后来补齐的原始文件目录 `daowei2026/observe-iterate@036f24f4a4b7ca898280d8ed58cbf9c0b3634744:task-inputs/eaw-p1-integrated/caegraph-review/` 中四文件均与原 ZIP 成员逐字一致。本次不重新提交脚本 ZIP，不以该补充核对静默升级锁定的 GO/专业方法。
- 数据 `caegraph-data-30tick.zip` 尚未在主控或 Worker 取得。输入给定身份为 16,654,307 字节、SHA-256 `73e7c5f289d7b25f08f11cffda7315ad2dad3f8c323715425afdd485e15c4233`；这些是待核预期，不是本 Run 已收到的证据。Sources 访问查证正在独立受控 episode 中进行，结果另记。
- Windows H:\fy ↔ Linux /dwdhome/fy 的候选映射尚未双向读取和核 SHA；因工作区接管未明，尚未向建议 handoff 目录写测试文件。
- 正式 MCP 的共享网络准入已完成，Recent 与准确 Project 的列表均实际可读；控制已释放，回执留在 gitignored 可信运行记录。未检查或改变模型名称与推理档位，未发送专业消息。

## 准确下一合法动作

继续完成独立的 Sources 查证及文档准备。工作区接管关系明确后，在授权独立 handoff 目录验证两端共享，按真实字节核输入；再发布 Binding/资源绑定、核候选 Registry 并条件更新，随后准备、核验和实际派发首次 manager 调用。数据暂不可得时只局部登记，manager 可在原权限内组织有条件的独立文档级专业工作。

普通步骤、专业取舍、Gate 和补证由本 Run manager 依原 Control 负责；本预检不预先记 DATA_READY、业务接受或任务完成。
