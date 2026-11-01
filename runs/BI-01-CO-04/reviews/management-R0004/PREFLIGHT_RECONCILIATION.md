# R0004 派发前快照机械校正

本记录由操作主控按 Management R0004 `DECISION.md#priority-and-next` 中“机械失败只定向修”的已签授权记录。管理的 Reader 接收、RECORDED 状态、context、独立性、input commit、reader fingerprint、报告 blob 和当前专业任务保持原值。

原 Intake 来自 `aea913ed2802115664209e3d910f8a883d0a11c8`，顶部 snapshot 沿用了 Reader 冻结输入的 `5f24d63895be9d5f52182fd8e4fa94a901667e8bdfda0fc4529f9addcecf19b2`。当前 preflight 实际返回 `INTAKE_STALE`。

定向比较确认：

- 原冻结输入、Management 实际 observed_commit `56ad93f138b6f62fb8435a8c667018f2ce701805`、当前 `f7b1459d41b79217f1c6f8290808c852d7a6eb05` 的 Reader 文档指纹均为 `b5f0c9826e1b7f639e39f64276e31d26a834e8ffcbd855497c6be628a63fc06b`。
- 当前任务 payload hash、binding、overview/map/task/owner/rule正文全部相同。
- 唯一完整快照差异是被明确排除的 Reader 输出使 `reviews/independent` 从 Git 树不存在（null）变成空投影（SHA256({})=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a）。实际该根下只有管理已授权排除的 `workmap-01/` 文件，没有新增受监看的业务结果。
- Management 的真实 observed_commit 与当前 ref 重新计算的完整 snapshot 相同，均为 `8169c23ff60c21da382a32c8e104c99678a2a793a04f8185b1d85ddc18771fbd`。

因此只把 Intake 顶部 `snapshot` 改为这一实际计算值；保留 observed_commit 以及 Reader 原始 workmap_snapshot（它仍准确描述原冻结输入）。原 Pro 报告、Return、旧 Intake 和冻结记录均保留在原 Git commit，没有新增管理判断、Reader、业务范围或通过声明。校正后仍须实际运行原 check/dispatch；成功只证明机械前置。
