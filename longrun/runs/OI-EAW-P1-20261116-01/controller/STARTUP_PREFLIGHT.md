# 启动预检｜OI-EAW-P1-20261116-01

本记录由主控保存运行事实，不替 manager 判断业务范围、证据资格或 Gate。

## 注册与派发

本 Run **已正式注册，原 C0001 已在实际 Pro 档位发送并确认 committed**。准确原件：

| 原件 | 已发布并远端回读的精确引用 |
|---|---|
| Owner GO | `daowei2026/observe-iterate@6a2d0abd34d44fd20fe7119035a8227e6b019625:longrun/runs/OI-EAW-P1-20261116-01/OWNER_START.md` |
| Run Binding | `daowei2026/observe-iterate@1a04ea440f395026491036d405d82e653a5fecbd:longrun/runs/OI-EAW-P1-20261116-01/RUN_BINDING.json` |
| 资源 Binding | `daowei2026/observe-iterate@1a04ea440f395026491036d405d82e653a5fecbd:longrun/runs/OI-EAW-P1-20261116-01/RUN_RESOURCE_BINDING.json` |
| 全局 Registry | `daowei2026/observe-iterate@f70a6f49de3398d17637f434446aeedfbc1b978c:longrun/controller/RUN_REGISTRY.json` |
| 首次完整任务 | `daowei2026/observe-iterate@985f3579d8c77ef9c2179ee4437345376c422e8b:longrun/runs/OI-EAW-P1-20261116-01/calls/C0001/FULL_ASSIGNMENT.md` |
| 候选 Invocation | `daowei2026/observe-iterate@d7a813b8bae5e016cefffeecef593c5d9848d71d:longrun/runs/OI-EAW-P1-20261116-01/calls/C0001/INVOCATION.json` |

Binding schema 核验通过，结果仅 `STRUCTURE_VALID_ONLY`；多 Run 核验另通过实际 Linux 路径检查，其结果不替代锁、Send 或专业验收。可信全局索引已加入本 Run，旧条目保持。原 C0001 已完成一次真实发送，实际专业调用 **1**、Worker 派单 **0**。实际 Pro、全文 hash、提交时间和回复等待事实见同目录 `C0001_DELIVERY_STATUS.md`。

## 固定采用来源

- 主控：`daowei2026/cgpterm@034da33b774d7e3db50fcdda219a64d4ed0281be:.agents/skills/observe-iterate-longrun-v2-controller/SKILL.md`。
- 业务 Control、协议和专业方法：`daowei2026/observe-iterate@7e240b650b6ba6274b0263e34f5b0616a9a8ff1c`，采用 V2 C/D/W 和 professional-return/v2，不继承旧 Run 的 Gate、判断、会话或工单。
- 完整输入和权力范围以 Owner GO 原件为准，本预检不另设 TaskBoundary。

## 工作区及旧 Run

Linux `/dwdhome/fy/BASE_E6_2` 真实存在，realpath 一致，当前账户具基础读写和穿越权限。本 Run 的实际 Worker 线程尚未创建/绑定，留到首次真实 W 前核验。

Owner 已原文确认：“允许新 Run 接管 BASE_E6_2，旧 Run 保持暂停”；后续选择按首项处理的指示也已保存。准确接管原件：`daowei2026/observe-iterate@930af5649eee428a2d9630de6d420c216055780d:longrun/runs/OI-EAW-P1-20261116-01/controller/OWNER_WORKSPACE_TAKEOVER.md`。

两个旧 Run `OI-EAW-WALL-20261114-01` 和 `OI-EAW-WALL-20261116-01` 均维持 Owner 暂停，未获恢复、未被消息唤起，旧业务状态未移入本 Run。新 Run 只在自己的独立 handoff 目录使用数据交换通道。

## Windows↔Linux 共享

**双向实际文件与 SHA-256 核验 PASS**。在本 Run 独立 handoff 中生成唯一 75 字节原件，由正式 MCP 从 Windows 对应路径实际读取并暂存手机，再从手机拉回另一 Windows 唯一路径；Linux 实际读到返回文件，字节完全相同，SHA-256 `45ed4d7ffa09e09d2c290d2e4c7fb9dc6e59a40534f544e6214db53672412fae`。未覆盖既有业务文件。

精确证据：`daowei2026/observe-iterate@1a04ea440f395026491036d405d82e653a5fecbd:longrun/runs/OI-EAW-P1-20261116-01/controller/SHARED_PATH_VERIFICATION.md`。此结果验证授权交换目录的实际映射，不扩大其它 Windows 写面。

## CAEGraph 脚本与数据

| 输入 | 当前真实可用性 |
|---|---|
| 原始脚本 ZIP | 主控已实际读取 31,319 字节，SHA-256 `5eaf500616316ef7764cd30eb7467f2db3a6c85e45aa3b4f958becbc7818e8eb`，ZIP CRC 和四成员指纹均通过；已暂存本 Run Linux handoff/inputs/caegraph-scripts.zip 并复核同 hash。无实际 Worker 读取或运行证据。 |
| 四个展开原件 | `daowei2026/observe-iterate@036f24f4a4b7ca898280d8ed58cbf9c0b3634744:task-inputs/eaw-p1-integrated/caegraph-review/` 已补齐，四文件与原 ZIP 逐字相同；本次不重发 ZIP，不静默更新锁定方法版本。 |
| 数据 ZIP | 准确 Project Sources 列表中存在 1 个 `caegraph-data-30tick.zip` 压缩文件条目；点选与延时复核无预览，菜单只有“删除文件”，未点击删除。手机 Download 顶层无同名文件；主控、手机下载目录及 Linux Worker 均未取得可验文件。实际字节/hash未知，不记 DATA_READY。 |

数据预期身份仍为 16,654,307 字节、SHA-256 `73e7c5f289d7b25f08f11cffda7315ad2dad3f8c323715425afdd485e15c4233`，只作将来接收校验基准，不能代替本 Run 的实际接收或业务可用性。脚本未在本 Run 执行，证据资格与正式预期由有权专业 Pro 决定。

## 当前收束与后继

原 C0001 已于 **2026-11-17 11:17:15.728 +08:00** 取得明确提交证据，当前实际 **Pro推理强度** 已在输入前核实。正文 full hash 和长度完全匹配，输入和 Send 各一次；当前模型正在思考，尚未消费首答/专业 Return，没有 UNKNOWN Send。

Owner 的运行期补充明确：数据 ZIP 在指定 Project Sources，由管理/执行 Pro 按专业需要读取和使用；首次派发无需主控先下载，不能把主控尚未下载记作派发阻断，也不把 Sources 条目等同专业端已验证可读。最新 Owner 又要求按当前实际可选 Pro 档位，本次已满足。准确运行期原件与真实派发证据见 `C0001_DELIVERY_STATUS.md`。

下次本轮观察时点 **2026-11-17 11:27:15.728 +08:00**，同时依原标记及真实远端完成关联处理交付。首答完成后按既有规则核名，再消费 V2 Return，后继由 manager 的实际业务判断决定。当前仅注册、首次消息送达及回复等待成立，**业务尚未完成**。

记录更新时间：2026-11-17T03:21:34.604412+00:00。
