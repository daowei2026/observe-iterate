# Worker05 工作2 Notebook 技术交付

工单 BI01-FO01-N-UPLOT-NOTEBOOK-05，签发 BI01-FO-01-R0014-20261023T153303Z-57f340f3；结果返回原 BI01-FO01-执行 Pro。

主文件为 `N_observation_Worker05.ipynb` 与 `DISPLAY_PLAN.json`。从 P11 不可变候选真实修订，在现场 m3py310 新 kernel 使用正常 Uplot/CAEGraph 重新绘图；不是旧 HTML/PNG 的重存。正式原件只读复用 W02/W03 锁定 Git 文件，未重新生成 N。

aidata 源码在独立分支 `fy/bi01-fo01-n-work2-r0014`，最终提交 `e8aaa464e30259c84dac47260104c5acda1eac5b`（基础接入 `7d4c48a`，实际像素反馈后修标量标签）；已通过专用 ref 从 GitHub fresh 读回。主报告 `FULL_RESPONSE.md` 给源码修改、范围、真实操作、失败/修复与全部未完，发布信息见 `GITHUB_RECEIPT.json`。

## 在已验证的本机环境打开

1. 使用 `/m3c3/Linux/apps/anaconda3/bin/python` 所属现有 JupyterLab 4.4.6/m3py310 kernel。
2. 打开本目录 `N_observation_Worker05.ipynb`，保持本目录 DISPLAY_PLAN.json。
3. **Restart Kernel → Run All。** 不把重开时缓存的 widget 模型引用、GitHub 静态预览或文件上传当成实际运行。
4. 选择 rb 的知识 K 与完整/局部范围；i 的知识 K；使用图上的 hover、实际 Wheel Zoom、Pan、Reset 与图例。Bokeh3 的滚轮工具需按其实际激活状态选择；已激活的工具再点会关闭。

图使用常规1800px宽；窄窗口可用 Jupyter 的 Ctrl+B 收起文件侧栏，或使用水平滚动，不需要极度放大。背景K线按正常bar中心显示，原close/N的知识UTI不移动；末根蜡烛中心K+300并非新增K后bar，逐bar原价/标签与无未来记录检查已通过。

实际运行环境的启动形式：

```bash
PYTHONPATH=/tmp/bi01-fo01-w03-runtime-20261022:/dwdhome/fy/BASE_E6_2 \
M3ROOT=/m3c3 M3WORKS=/dwdhome/fy/BASE_E6_2 \
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 \
/m3c3/Linux/apps/anaconda3/bin/python -m jupyterlab --no-browser \
  --ServerApp.ip=127.0.0.1 \
  --ServerApp.root_dir=/dwdhome/fy/observe-iterate-bi01-fo-01
```

这是本次实际环境的路径，不承诺其他机器已安装相同环境。临时 overlay 若已清理，先恢复已核依赖；不换用 main 掩盖缺件。Notebook 可通过 OBSERVE_REPO、BI01_W05_ARTIFACT_DIR、BI01_W05_AIDATA 指定真实仓库/配置/本单 aidata 工作区。执行脚本所需的现场端口通过本机环境变量 BI01_W05_JUPYTER_PORT 传入，不硬编码/提交现场端口或凭据。

本单实际验证的本机入口和生命周期另存 cgpterm ignored `artifacts/bi01-worker05-runtime/LOCAL_NOTEBOOK_ACCESS.md`；认证材料未交 GitHub。前端只在 Worker 本机实际打开，没有向原 Pro 转发或授权远程入口，不声称 Pro 本人已看图。Notebook 是可在该环境重新执行和交互的主交付；截图只作 ignored 技术取证。没有工作3平台 URL、平台节点或 board 包。

## 查证入口

- 当前运行权限：`evidence/RUNTIME_PERMISSION_CHECK.json`。
- 实际 kernel、导入文件、配置路径和执行身份：`evidence/EXECUTION_RUNTIME.json`、`KERNEL_COMPLETION.json`。
- 现场版本/dirty 与有效 TIS 文件比对：`evidence/ENVIRONMENT.json`。
- 不可变正式源逐文件指纹：`evidence/SOURCE_READS.json`；显示投影另在 `plot_view_data/`，不作为正式 N。
- 实际前端动作与实际 CDS：`evidence/FRONTEND_EVENTS.json`、`FRONTEND_INTERACTION_EVENTS.json`、`BROWSER_*.json`。
- 原表→图用 CSV→实际浏览器 renderer 的技术核验：`evidence/TECHNICAL_VERIFICATION.json`。
- 失败和先前运行：`failures/`、`iterations/`；原 R11 失败版本仍在原提交。
- 完整文件字节/hash：`DELIVERY_MANIFEST.json`。

技术结果交原 Pro 消费、判断与必要返修，再由管理对具名工作2成果作认可/返修/待证决定。未自动进入工作3/4，未创建 Goal/轮询/自动恢复来源。
