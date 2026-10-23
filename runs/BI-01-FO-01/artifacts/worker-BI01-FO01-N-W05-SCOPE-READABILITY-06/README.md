# Worker06 技术实物入口

工单BI01-FO01-N-W05-SCOPE-READABILITY-06，签发BI01-FO-01-R0017-20261023T192809Z-edd5489f。结果回原执行Pro，不代签专业判断/管理接收，不进入工作3/4。

主交付为 `N_observation_Worker06.ipynb` 和 `DISPLAY_PLAN.json`；完整技术结果、真实失败及限制见FULL_RESPONSE.md。aidata在新独立分支 `fy/bi01-fo01-n-w05-scope-r0017`，最终提交 `8a08300cb70a610401424bedadb42e9dcde13e71`，保留W05 e8aaa修复。最终两仓发布位置见GITHUB_RECEIPT.json。

## 小文件读源码

- [W05确切原blob的完整cell源码](notebook_source/W05_original/NOTEBOOK_SOURCE.md)
- [W06最终执行Notebook的完整cell源码](notebook_source/W06_executed/NOTEBOOK_SOURCE.md)

两侧INDEX.json/cells/*.json保留完整source、id、顺序、类型、执行序号和metadata；输出只列MIME/位置/错误等索引。未展开大段内嵌JS/保存图，不将文本等同完整Notebook。逐字对应见evidence/NOTEBOOK_SOURCE_VERIFICATION.json。

## 在本机已验证环境打开

解释器 `/m3c3/Linux/apps/anaconda3/bin/python`。最终实际kernelspec为Python 3 (ipykernel)/python3，与现有m3py310指向相同解释器；继承代码中m3py310常量提示不作为实际kernel名证明，见ACTUAL_KERNEL_CHECK.json。启动形式：

```bash
PYTHONPATH=/tmp/bi01-fo01-w03-runtime-20261022:/dwdhome/fy/BASE_E6_2 \
M3ROOT=/m3c3 M3WORKS=/dwdhome/fy/BASE_E6_2 \
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 \
/m3c3/Linux/apps/anaconda3/bin/python -m jupyterlab --no-browser \
  --ServerApp.ip=127.0.0.1 \
  --ServerApp.root_dir=/dwdhome/fy/observe-iterate-bi01-fo-01
```

打开本目录Notebook，**选择Worker06标签，Restart Kernel→Run All**。原先缓存widget输出不作为运行成功证据。Notebook默认使用本目录配置和实际observe仓库，aidata默认本单独立工作树；可用OBSERVE_REPO、BI01_W06_ARTIFACT_DIR、BI01_W06_AIDATA指定真实路径。若临时overlay已清理，先恢复W05/W06记录的有效依赖，不能换main掩盖缺件。

rb的“显示范围”切换完整/局部，页首区分源覆盖、价图范围、原输入缺值及视域省略，正式统计不随显示范围重算。i恢复拍保留24条原缺价及缺路径/缺ratio，waiting0另显。HC本次在2300×1400、1800px图宽下，侧栏关闭/打开均实际看清末拍close3904、K和其他具名标记；不承诺任意窄窗口适配。

本单临时Jupyter/kernel已关闭；需由获准操作者重新启动，不提供仍在线URL。端口/认证/截图只存cgpterm ignored artifacts/bi01-worker06-runtime，不在GitHub。Pro远程前端未接通；Notebook上传、源文本可读与Pro本人实际操作分别保持事实。

证据入口：evidence/FRONTEND_EVENTS.json、ACTUAL_EXECUTION_ALIGNMENT.json、WORKER_VISUAL_INSPECTION.json、SCOPE_VERIFICATION.json、TARGETED_TESTS.log；对应实际投影在plot_view_data。failures/保留本单真实问题。原W05整包沿b055102固定引用，未重传或倒改。
