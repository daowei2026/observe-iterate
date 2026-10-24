# Worker07 技术回交入口

order_id：BI01-FO01-N-PLATFORM-BOARD-07。签发 invocation：BI01-FO-01-R0022-20261023T231811Z-3342cb6b。

**三 run、四个冻结节点的正常三 API、CAE 注册和 board 已完成；现有正常平台四页均 HTTP 500，工作3尚未技术验收通过。** 真实原因是服务仍加载旧版 `AidataBigWorldReviewCAE`，不认识本单声明参数。没有重启或替换共享服务。原 Pro / 管理需协调正常部署责任者采用已交代码，再复核同四节点页面。

- 完整事实、限制、恢复条件：[FULL_RESPONSE.md](FULL_RESPONSE.md)。
- 正常入口及选择：[scripts/run_worker07.py](scripts/run_worker07.py)、[run_briefs/](run_briefs/)。
- 同节点可读正式交付：[board_delivery/](board_delivery/)，包含四个 packet 目录和 ZIP；`10_NORMAL_N_FORMAL_DEPENDENCIES/INDEX.json` 是原表闭合入口。
- 平台真实打开：[evidence/ACTUAL_PLATFORM_OPEN.json](evidence/ACTUAL_PLATFORM_OPEN.json)。公开副本只给真实 report 路径与 URL 哈希；实际完整地址留在正常 run 的 `review/big_world_chart_pages.csv` 和本机 ignored 取证，不公开私网基址。
- 新进程真实消费者：[evidence/RECONSTRUCTED_CAE_RENDERERS.json](evidence/RECONSTRUCTED_CAE_RENDERERS.json)。这是已交代码的实际构图数据，不能当成当前平台前端成功。
- 正常读者比较：[evidence/FRESH_ONLYREAD_COMPARISON.json](evidence/FRESH_ONLYREAD_COMPARISON.json)。本次 rb 直接 OnlyRead 的18表与锁定 W02 正式导出逐原字段相符。
- 所有实物哈希见 `DELIVERY_MANIFEST.json`，运输变换见 `evidence/TRANSPORT_SOURCE_INDEX.json`。

复现环境沿已有 Python `/m3c3/Linux/apps/anaconda3/bin/python`、只读 overlay `/tmp/bi01-fo01-w03-runtime-20261022`，仅将 `mquant.aidata` 指向本单独立工作树。精确运行入口及版本见完整报告。脚本不会启动平台服务；正常服务需由有权部署者采用兼容代码。

本包是工作3技术交付，不替原 Pro 的消费/判断，不签管理接收，不启动正式工作4。泛型包内旧的通用合同字段不新增本任务权限或替代当前完整专业方法。
