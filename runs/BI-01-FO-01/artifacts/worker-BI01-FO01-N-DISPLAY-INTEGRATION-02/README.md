# BI01-FO01-N-DISPLAY-INTEGRATION-02 技术回交

状态：`TECHNICAL_RETURN_READY`

返回目标：`chatgpt:细节叙事生成_金标:BI01-FO01-执行`

本目录保存 R0007 N 展示配置的真实 aidata 接入、正常 OnlyRead/as-known 读回、四页 uplot/Bokeh HTML、同源 `plot_view_data`、浏览器截图、像素检查及完整恢复脚本。Worker 不在此判定专业业务含义或管理接受。

核心入口：

- `FULL_RESPONSE.md`：完整技术回交、准确版本、结果、失败恢复和未完。
- `evidence/RUNTIME_AND_RENDER_MANIFEST.json`：实际入口、页面和安全边界。
- `evidence/FINAL_VERIFICATION.json`：19 项最终包装检查，全部通过。
- `render_evidence/BROWSER_CAPTURE.json`：四页实际浏览器检查。
- `render_evidence/WORKER_VISUAL_INSPECTION.json`：Worker 全分辨率像素检查。
- `data/selected_cuts/`：三个 `read_at_knowledge` 正式表导出。
- `plot_view_data/`：四页实际消费者输入。
- `GITHUB_RECEIPT.json`：推送并从远端回读后生成的最终回执。

aidata 最小改动已提交到 GitHub 分支 `fy/bi01-fo01-n-display-r0007`，commit `db44a54fa30ff9b4b8dddbe37e020d087c914d62`。
