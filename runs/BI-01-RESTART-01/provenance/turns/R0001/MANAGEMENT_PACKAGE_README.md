# BI01 M-START R0001 可落地包

本包由管理 Pro 的 R0001 回交生成，包含：

- `runs/BI-01-RESTART-01/00_长程推进地图.md`
- `runs/BI-01-RESTART-01/01_当前任务.md`
- `runs/BI-01-RESTART-01/reviews/MANAGEMENT_START_R0001.md`
- `runs/BI-01-RESTART-01/bindings/QUESTION_WORK_BINDING_I4.json`
- `runtime/config/WORKMAP_BINDING_CANDIDATE.json`
- `provenance/turns/R0001/ROLE_RETURN.json`
- `provenance/turns/R0001/QUESTION_WORK_RETURN.json`

## 重要边界

本包不是远端提交证明。当前连接没有 GitHub 写入动作。操作端需要：

1. 将文件原样落入 `daowei2026/observe-iterate` 的当前 run 分支；
2. 普通快进提交；
3. remote readback；
4. 运行 workmap intake / gate；
5. 用真实 commit 更新 `WORKMAP_BINDING.json` 为 ADOPTED；
6. 然后才派发执行 Pro。

禁止在第 5 步之前声称专业任务已经发送或 Gate 已通过。
