# Worker10：打开、复现与证据资格

主实物为 `N_time_expression_Worker10.ipynb`，不是PNG或独立HTML。准确有序源码另在 `notebook_source/NOTEBOOK_SOURCE.md`；该文本不展开Notebook保存的JS/widget输出。

## 已用现场

- observe工作树：`/dwdhome/fy/observe-iterate-bi01-fo-01`，FY正式分支；`OBSERVE_REPO`须含W02/W03/W09固定Git对象。
- aidata独立工作树：`/dwdhome/fy/BASE_E6_2/mquant/aidata-bi01-fo01-n-time-expression-r0038`；分支 `fy/bi01-fo01-n-time-expression-r0038`，准确运行提交见 `evidence/EXECUTION_RUNTIME.json`。
- 解释器 `/m3c3/Linux/apps/anaconda3/bin/python`，Python3.10.13；实际前端kernel为 `python3 / Python 3 (ipykernel)`。沿W09已验证环境，非Pro沙箱环境。
- 启动依赖路径为只读overlay `/tmp/bi01-fo01-w03-runtime-20261022` 与 `/dwdhome/fy/BASE_E6_2`；`M3ROOT=/m3c3`、`M3WORKS=/dwdhome/fy/BASE_E6_2`。overlay不存在时此现场打开条件尚不满足，不能用moving main替代。

本单自有Jupyter及kernel已关闭；没有遗留可打开的在线服务，亦不发布私网端口/token。Pro连接器未取得此机器可达能力，不能说Pro本人已经打开或看图。后续在这台有权机器的新Jupyter中，选择上述kernel，打开目标目录的主Notebook，**Restart Kernel → Run All Cells**。只重开缓存widget不等于新执行。

可由有权使用者自行在该环境启动正常JupyterLab；无需新建Host、公开服务或平台节点。令 `BI01_W10_AIDATA` 指向上述候选、`BI01_W10_ARTIFACT_DIR` 指向本目录，`OBSERVE_REPO` 指向实际observe仓；Notebook首单元检查候选路径并采用只属于本单的import别名。它不改共享mquant默认导入。

本机JupyterLab默认 `full` 虚拟挂载曾产生实际空白canvas。最终仅在本单自有用户设置目录把Notebook的 `windowingMode` 设为 `none`；真实前端DOM核到11个cell。复现时在自有JupyterLab设置中使用同样的Notebook非虚拟挂载，并在2300×1400、DPR1检查。不是要求任意窄屏适配，亦未改共享Jupyter配置。

## 阅读与操作

- rb查询仅有确认前、确认拍、末拍三个固定K。主价图103043400起，止于各自K；通过阅读模式切换进入相邻确认两拍的明确事后对照。末拍单独查询，不压入相邻两拍横轴。
- i查询仅有缺价末拍、恢复、后一拍三个固定K。事后三拍图用真实K坐标，原自然时间并列；CalendarUTITick不是自然秒/bar。
- 事后图只有真实不相连点、共同数值轴及原缺项说明；没有hold/step/插值。返回查询恢复本K轴/成员/说明，不借后拍数据解释较早K。
- 完整Life/exact、当前K、原基础保存坐标和状态可hover；短Life只为图上识别。原价缺口不补线；整个过程起点价未提供时只说明，不合成价格点。

## 三种数据不要混同

正式源是 `SOURCES.md` 指定的W02/W03正常OnlyRead导出，本单没有新生产读取或重算。`evidence/SOURCE_READS.json` 给逐原件hash。

`plot_view_data/` 仅为新图投影，不是正式N或board交付。每目录 `ACTUAL_DISPLAY_BINDINGS.json` 是本次真实spec、anchors、身份与全部time_contexts；原 `plot_view_data_manifest.json.configuration` 保留W09基础配置0.3.0和 `selected_cut` 网格语法，**不能拿其中单K默认文案描述本次多K事后对照**。比较的真实作用域在实际bindings及 `meta.time_expression`，完整列出各K/exact/Life；其价格上下文取最后列示K，不代表一个新正式多K产品。

场景 `TIME_EXPRESSION_PLAN.json` 0.5.1-worker10 由精确R38原JSON派生（原件在inputs）；`time_expression` 由本单Notebook/N准备器显式消费，不是新增通用aidata API。status保留执行前候选身份，实际执行结果以运行证据为准；没有管理接收含义。

先读 `FULL_RESPONSE.md`、`CHECK_RESULTS.json`、`evidence/FRONTEND_EVENTS.json`、`evidence/WORKER_VISUAL_INSPECTION.json`，再按原表/投影/当前root追查。截图/原日志只保留本机ignored技术取证，不作主交付或Pro本人视觉证据。

## 限定命令

`scripts/prepare_notebook.py` 会从准确W09 blob重新派生并清输出，**不要对唯一已执行实物盲目再跑**；需要改版时保留当前版本再运行。`scripts/check_delivery_consistency.py` 只读固定Git对象和本次实物，可复查原CSV→图用CSV→实际浏览器CDS。`scripts/run_unit_tests.py` 只跑本单有限合成反例。前端驱动须由有权的自有Jupyter启动上下文运行，未向任何共享服务注入检查。

M37已认可四视域仍是原25a/W09对象；本单不替换其采用请求。新时间用途回原签单Pro判断并交管理；没有平台注册/DAO/共享启停/正式工作4。
