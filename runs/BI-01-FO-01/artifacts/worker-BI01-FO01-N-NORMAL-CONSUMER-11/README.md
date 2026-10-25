# Worker11实物入口

完整事实、失败和未完见[FULL_RESPONSE.md](./FULL_RESPONSE.md)。这是普通CAE/正常board的隔离候选，不是共享平台发布。先读[inputs/NORMAL_RUN_INDEX.json](./inputs/NORMAL_RUN_INDEX.json)定位run/node/模式/K，再读各case packet；不能用比较最后exact代表全部K。

## 可读资料

- [N_normal_consumer_Worker11.ipynb](./N_normal_consumer_Worker11.ipynb)：实际新执行W11-20261025T025132Z-36244ab7；普通Fao恢复→普通CAE，不是W10旧输出。
- [notebook_source/NOTEBOOK_SOURCE.md](./notebook_source/NOTEBOOK_SOURCE.md)和INDEX.json：完整有序cell source、id/类型/计数/必要metadata。source与主ipynb逐字相同；大型保存JS/widget输出仅MIME/位置/hash索引，不展开，不等于完整Notebook。
- `normal_runs/<case>/run_brief.json`和manifest：实际正常输入/冻结范围、逐K选择/源及slice stats。NORMAL_RUN_INDEX保存descriptor/ppid/fason SHA和本机准确run路径；含context的fason全文只在ignored，不提交认证资料。
- `normal_runs/<case>/delivery/big_000001_packet/`：02来源、03自然切片、06字段/slice_index、05同行情、10_NORMAL_N_FORMAL_DEPENDENCIES中的逐K正式原表/INDEX/合格价和node价。早期基础与本K主结果分角色，保存时间不改。
- `plot_view_data/<case>/`：仅核图，ACTUAL_NORMAL_SELECTION保留模式/逐K/policy；不能作正式多K N。
- [CHECK_RESULTS.json](./CHECK_RESULTS.json)及evidence的COLD_CONSUMERS、DIRECT_CHECKS、FORMAL_DELIVERY_CHECK、FRONTEND_EVENTS、BROWSER、WORKER_VISUAL_INSPECTION：冷恢复/回归、图数与Worker实际操作/像素资格。

## 实际打开与复现

本机解释器`/m3c3/Linux/apps/anaconda3/bin/python`（3.10.13），kernel `python3`；候选工作树`/dwdhome/fy/BASE_E6_2/mquant/aidata-bi01-fo01-n-normal-consumer-r0041`实际HEAD f4f47acf99a3efa664b031cdc1ce1fd484ce1dfc。readonly overlay `/tmp/bi01-fo01-w03-runtime-20261022`、BASE_E6_2现有依赖及uplot既有dirty见RUNTIME_BOUNDARIES/EXECUTION_RUNTIME。不能只换HEAD推定运行相同，不追保护依赖latest。

Notebook位于观察仓本目录；正常run/data在观察仓`artifacts/bi01-worker11-runs/`，本单运行信息在cgpterm的`artifacts/bi01-worker11-runtime/`。首cell显式路径，后续读取BUILT_RUNS及保存fason；不依赖W10内存或向DAO取旧节点。在具备这些资源的本机环境，新kernel按顺序Run All，再用rb/i控件选择具名query/事后comparison。没有持续在线服务或交付端口；不声称Pro沙箱能访问本机路径，也不把GitHub预览称JS交互。

`scripts/build_normal_runs.py`实际使用公开build_chart_run/build_board_run；`cold_restore.py`实际使用正常node2fao/普通CAE/render_review_nodes。原件由固定Git W02/W03和W10场景生成只读source-cache，不计算N。BI01_W11_RUNTIME应为本机ignored目录，首次需本候选独立工作树、原依赖及观察仓固定对象。生成器会写自己的ignored观察run，不是只读检查；已有CATALOG恢复同一冻结选择，更改选择须正常新观察身份，不能覆盖旧run。

`check_delivery_consistency.py`只读核固定Git原CSV/已保存浏览器CDS/交付；`check_formal_delivery.py`还读取本机正常run的slice/packet。`direct_checks.py`需W08安全普通fason样本及W07旧本机只读run；缺挂载就报告，不伪造通过。

frontend_run.py/frontend_checks.py是实际探针，run_frontend_episode.py只为有权本机临时取证，finally收束，动态读取本单ignored访问文件。凭据/实际端口不提交，不用于共享服务。prepare_notebook.py会清输出重建，只供保留旧版后的有据新执行；不能覆盖唯一交付。prepare_frontend生成器还引用本机W10 runtime模板，该真实依赖未重复运输；最终driver/checks/wrapper已交，不声称生成器在未挂载沙箱独立可用。

脚本从真实ignored执行字节运输，仅显式runtime定位转换，源/运输hash与说明在SCRIPT_TRANSPORT。实际合同见aidata候选docs/RUN_BRIEF_INPUT_CONTRACT.md、DEVELOPMENT_GUIDE；本目录不是平行API规范。

## 当前没有的结果

没有新注册CAE id/report_url、共享导航/加载证据。build_big_world_chart_pages(save=False)仍注册，本轮未调用。25a原路线、M40工作2接收、W07旧页/packet和工作4边界保留；冷恢复/临时服务/HTTP200不替正常平台。
