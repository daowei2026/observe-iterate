# Worker09：有限共用展示实施回交

order_id：BI01-FO01-N-BOUNDED-DISPLAY-09；原签单Pro：chatgpt:细节叙事生成_金标:BI01-FO01-执行。
先读[完整技术回交](FULL_RESPONSE.md)，源码合同见[IMPLEMENTATION_CONTRACT.md](IMPLEMENTATION_CONTRACT.md)。
这是本单工程/图层事实，不自签工作2/3接收，不启动工作4。

主实物为[N_observation_Worker09.ipynb](N_observation_Worker09.ipynb)，从准确W06主Notebook派生，清旧输出后本次新kernel实际执行；准确有序源码入口为[notebook_source/NOTEBOOK_SOURCE.md](notebook_source/NOTEBOOK_SOURCE.md)。
源码文本不展开内嵌JS/widget输出，完整输出仍在ipynb。GitHub预览不保证执行Bokeh JS，不是交互入口。

## 在本现场复现

需要实际存在并核实的依赖：

- observe仓 `/dwdhome/fy/observe-iterate-bi01-fo-01`，含W02/W03准确Git对象；Notebook只读这些正常导出，不重算N。
- aidata独立工作树 `/dwdhome/fy/BASE_E6_2/mquant/aidata-bi01-fo01-n-bounded-display-r0035`，最终HEAD `25a9fd8b1333aafd4c56fd1b288e7f8d3c8c3113`。
- Python `/m3c3/Linux/apps/anaconda3/bin/python`，3.10.13，kernel `python3 (Python 3 ipykernel)`；不是Pro沙箱的Python3.13。
- 已有只读overlay `/tmp/bi01-fo01-w03-runtime-20261022`；共享uplot为13badc6c并有preexisting dirty，实际有效pfw hash及限制见正文，不能声称干净checkout。

在获准的本机Jupyter启动会话中设置：

```bash
export PYTHONPATH=/tmp/bi01-fo01-w03-runtime-20261022:/dwdhome/fy/BASE_E6_2
export M3ROOT=/m3c3
export M3WORKS=/dwdhome/fy/BASE_E6_2
export OBSERVE_REPO=/dwdhome/fy/observe-iterate-bi01-fo-01
export BI01_W09_AIDATA=/dwdhome/fy/BASE_E6_2/mquant/aidata-bi01-fo01-n-bounded-display-r0035
export BI01_W09_ARTIFACT_DIR=/dwdhome/fy/observe-iterate-bi01-fo-01/runs/BI-01-FO-01/artifacts/worker-BI01-FO01-N-BOUNDED-DISPLAY-09
```

用该解释器的现存合法Jupyter入口打开上述Notebook，选择Python3 kernel，**Kernel菜单→Restart Kernel→Run菜单→Run All Cells**。
首次无kernel时先实际Select Kernel，不把弹出的选择框当Restart确认。
Notebook会在本目录更新当前执行记录、图用导出和真实保存输出；复现前请保留冻结交付版本或使用自己的工作副本，并把BI01_W09_ARTIFACT_DIR指向工作副本（同目录放本版DISPLAY_PLAN）。
rb默认末拍，范围选项支持完整/局部；其他已取K均明确仅工作2准备/回归，不扩大平台资格。
如出现本单Notebook的File Changed保存提示，应先确认没有别的写者；仅本次独占工作副本可保留当前真实执行，不能盲目覆盖他人的文件。

本次临时Jupyter仅为有限技术验证，结束时关闭；没有交付持续在线入口，不公开私网地址/端口/token。Pro当前是否可达仍取决于其实际挂载/入口，不能据本机运行成功代称Pro本人已经打开。

## 定向验证复跑

`scripts/bootstrap.py`和探针仅使用明确候选；生成内容写到gitignored的BI01_W09_RUNTIME（默认本机cgpterm artifacts），不写共享源码。

```bash
/m3c3/Linux/apps/anaconda3/bin/python scripts/run_tests.py
/m3c3/Linux/apps/anaconda3/bin/python scripts/probe_final_contract.py
/m3c3/Linux/apps/anaconda3/bin/python scripts/cold_restore.py
```

board探针 `verify_board_replica.py`、`verify_remaining_board_replicas.py`只在ignored隔离副本消费相同冻结core和已核原件，不注册页面、不修改原W07包。不要将副本当正式平台发布。
前端脚本记录真实Jupyter动作和当前Bokeh root/CDS；须由现场已有授权会话提供实际连接环境，访问凭据不随仓运输。
测试数仅指技术夹具，真实Notebook、前端像素、共享采用和专业接收分别记录。
