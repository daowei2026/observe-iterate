# 首次地图 reader gate 的受派技术回交

- task_id：`BI01-V2-WORKMAP-FIRST-READER-FIX-01`。
- source_invocation：`BI01-V2-01-R0002-b2c88771267c2530631a43db`。
- 实际承办者：原 `codex-thread:01a14a59-7f26-7921-b549-3e7cd9be5119`，本单明确授权的 Worker Codex 容量；本报告后接回操作职责。
- 授权正本：`f87a9a64f4f0fa3ead13b9ee7c108f87847a581a` 的本目录 `WORKER_TASK.md` 和 `DECISION.md#reader-pre-adoption`；完整管理回交在 `df7bfd51a626be7a63ce97d58bdbc90e7a1583b8`，已实际核验。

## 已实际完成

已修通“采用证据的只读生产者先被要求消费 ADOPTED”的实际 BI01 gate 路径。源码已提交、推送、逐文件远端回读；54 项相关回归通过；从新代码对真正已准备的 R0003 完整派发实际回用通过。当前仍 NOT_CONFIGURED、无 Intake，R0003 仍 NOT_SENT；这不是独立读者已发生或业务采用通过。

源码提交：`2942ddd8f5210e68d394f6142f9087d4476101fc`。实际脚本 `runtime/tools/bi01_run_gate.py`，blob `7476275ad38ad5652456e7e1dbba13d30ee5936b`。测试在该提交对应的相同源码/测试工作树执行，提交后六个改动文件与远端逐字节一致。专业 policy 仍为 `11626f64bc64ae21e52108b2e47fafbbc1023615`，没有随运行修补升级业务方法。

## 最终改动与保护

受限入口只处理本 run 当前已签 `BI01-V2-WORKMAP-READER-01`。检查真实 current task/Binding 相同载体、实际 Binding JSON、管理 plan/adoption 来源与既有管理 Invocation/Return 关联；复用原 Overlay12 prepare/verify，核派发身份、review/INDEPENDENT_REVIEW、目标接收者和准确 payload。复用既有 Workmap snapshot 核冻结 reader-input 与当前受保护输入一致，不另写 resolver、签名、登记、reader 系统或全局 skip。

原 invocation、locator、完整 task、发送状态保护继续。其他角色、其他受托工作、错误来源/目标不能借道；管理 BOOTSTRAP 还须是实际 BOOTSTRAP 对象及其接收者，不能拿 reader Binding 冒充。普通专业仍须真实 ADOPTED/Intake。源码/测试和两份直接使用说明均在本次六文件提交，未改业务 map/task/专业 Binding、固定数据、市场方法、aidata 或 cgpterm 手机系统。

测试首次暴露原 `test_new_run_not_adopted_or_sent` 把活动现场永远断言为没有 Owner GO/BOOTSTRAP。真实 Owner 已启动后，该断言不适用；现定点核可复用未启动模板仍 NOT_CONFIGURED、没有伪造 Owner START/BOOTSTRAP，并保留本 run 目标路径/入口约束。不是删除失败业务断言或把真实运行记录清空。首建 base 的回归在现有 Workmap 临时 Git fixtures 中补入，没有旧 map/task/intake但已有模板 binding，后续合成阅读/采用/dispatch 可完成。合成材料没有进入真实 run。

## 实际验证

工作目录均为本实际 observe-iterate V2 checkout。

| 实际命令 | 结果 | 范围 |
|---|---|---|
| `python3 -m unittest discover -s runtime/tests -p 'test_bi01*.py'` | 24 项，exit 0 | 首次 reader 与普通角色/来源/目标/冻结输入/准确载荷/发送保护；既有 BOOTSTRAP、ADOPTED 专业、两份 Return |
| `python3 -m unittest discover -s runtime/overlay/tests -p 'test_workmap_gate*.py'` | 30 项，exit 0 | 既有 Workmap 和新增真实临时 Git 首建 base |
| `python3 -m unittest discover -s runtime/tests -p 'test_bi01_v2_source_boundary.py'` | 文档改动后9项，exit 0 | 模板、当前业务来源与直接说明边界 |
| `git diff --check` | exit 0 | 提交前差分 |

第一遍 BI01 全组因上述旧预启动断言有1项失败，其余通过；定点修正后重跑24项通过。完整命令输出及原始实际回用 JSON 保存在操作端 gitignored artifacts，不提交设备、控制权或大量现场原件。上述都是技术自检，没有独立专业审查资格。

## 真正 prepared R0003 的直接回用

R0003 发布与四文件远端逐字节读回：`93d5dd91fb845be3fa43f8665ca9d43f37fb4350`。Invocation `BI01-V2-01-R0003-104e88d2b67a7431818598f2`，真实目标 `chatgpt-project:细节叙事生成_金标/chat:new:BI01-V2-地图只读接收-01`。原样 PROMPT SHA-256 `af0904a4ebca61489b249c6a6b339f13085151e84b146a8aa6a6c4a2d7388c5a`，UTF-8 37,782字节、UTF-16 23,644 units。

Binding 按 `df7bfd51a626be7a63ce97d58bdbc90e7a1583b8` 的实际正文重新定位为 `READER_TASK.md::L98-L142`，不是沿用旧行号；完整 task 为同提交全文，采用依据为 R0002 `DECISION.md#adoption@f87a9a64…`。prepare/verify 实际通过。

实际命令：

```text
python3 runtime/tools/bi01_run_gate.py pre-dispatch --repo . --ref 93d5dd91fb845be3fa43f8665ca9d43f37fb4350 --round R0003
```

exit 0，`ok=true`、`errors=[]`、`recorded_send_state=NOT_SENT`、`sent=false`、`business_gate=false`；调用的新脚本源码版本见上。此时 `WORKMAP_BINDING.status=NOT_CONFIGURED`、Intake 文件不存在，未以改状态求通过。同一新代码对 R0002 `after-return` 实际通过。外部 Owner/角色授权、手机准确目标/控制权、scheduler 去重和原样 IME/Send 仍须实际执行。

真实 snapshot 输入为管理指定 `f87a9a64f4f0fa3ead13b9ee7c108f87847a581a`，reader_fingerprint `bc415dab26f34c1267141292218482e05d71dacec57553782aaa369569de5478`；snapshot fingerprint `bd1e2b1a5420eba80449577a1398b58e6ddfe0bed0ef5d0eb11443e6a2a413ab`；专业 task_payload SHA-256 `9c52e0f654db2cb9362cd6bc1a2000d94e56bfd37058e658f7b1469a0b4422dd`。与修补后真实 Git 的 reader-input 相同，未复制旧 ff84 指纹。

## 未执行与当前连续后继

R0003尚未创建新chat、输入或Send；真实 reader 报告、Intake/ADOPTED、专业首发、S1实际观察、S2真实图/同源数据、S3认识和管理阶段接收均未完成。没有再测试已确认 aidata 环境或共享ZIP，也没有重算固定结果。

本地技术单与Git提交不计新Pro R，已完整收到的有效Pro结果仍为R0001、R0002两次，4/8/12…复看起点保留。现在接回操作职责，按到期共享网络准入及准确新上下文实际发送R0003，取得独立报告后按R0002条件机械采用，继续首发原完整S1—S3。无新的Owner权限缺口，不以本技术报告作为整个运行停点。
