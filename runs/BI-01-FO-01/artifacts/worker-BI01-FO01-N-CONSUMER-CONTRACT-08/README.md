# Worker08 回交入口

本单 BI01-FO01-N-CONSUMER-CONTRACT-08 已完成 A/B/C 的现场调查及隔离验证，结果交原签单执行 Pro。未部署、重启、改认证、修改/注册原四节点，未执行正式工作4。

主要新结论：cbd 的普通非N对象真实 `fason` 也携带新增空N字段，旧恢复者会拒绝；省略调用端空键不能消除此问题。既有共享类节点6126经活动Trier只读文档接口成功展开为旧16键合同；该节点属于历史fixed_input，仅作合同观察，不当普通Feature页面或旧图通过。已有N节点6129的一次同接口对照当前确实拒绝新增N字段；未打开report或运行layout。独立具名BaseCAEFao宿主可隔离构造恢复，但类在进程注册不等于已在eval命名空间可见，预热命名空间后再声明类的探针准确复现NameError。

- [完整技术回交](FULL_RESPONSE.md)：已证事实、剩余假设、两个候选的最小变动/权限及后继。
- `evidence/`：活动Trier安全元数据、真实序列化/跨版本恢复、独立宿主及命名空间边界。
- `probes/`：实际探针；不调用layout或DAO写方法。运行方法见完整报告。A类现场脚本需本机ignored的既有URL回执，不含私网基址。
- `CHECK_RESULTS.json`：对上述真实记录的完整性/正反对照核验，不是平台或业务PASS。
- `DELIVERY_MANIFEST.json`、`GITHUB_RECEIPT.json`：本单必要实物及发布读回；不重传W06/W07整包。

Trier活动类的文件路径/字节码及Bokeh活动类未由现有接口直接暴露，报告保留该限制。没有将磁盘HEAD或新进程导入当作活动服务模块版本。aidata没有本单源码改动，也没有新aidata分支或候选已采用的事实。

## 本机复现入口

在本目录下，以 `/m3c3/Linux/apps/anaconda3/bin/python` 执行 `probes/serialize_contract.py`。
`--variant old --aidata-tree /dwdhome/fy/BASE_E6_2/mquant/aidata-bi01-fo01-n-w05-scope-r0017` 对应已核8a；
`--variant cbd --aidata-tree /dwdhome/fy/BASE_E6_2/mquant/aidata-bi01-fo01-n-platform-board-r0022` 对应cbd。
两者均传 `--runtime /dwdhome/fy/cgpterm/artifacts/bi01-worker08-runtime`，每次调用是新进程。
先取得各自serialize记录，再分别用 `--restore-input` 指向另一版本的记录。
脚本内部保存安全输出和隔离库日志，不调用layout/Feature计算或DAO写方法。

独立宿主探针为 `probes/named_host_contract.py`，环境变量 `BI01_W08_RUNTIME` 指向同一ignored运行目录；
另一个新进程加 `--prewarm-json` 取得已初始化eval命名空间对照。
它依赖既有W07的真实run manifest，不能在缺mquant/现场输入的Pro沙箱中用假对象替代。
A类脚本依赖本机ignored的既有正常URL回执，地址不在Git包中；不重复请求原四N页面。

检查现有交付记录可运行：`python probes/verify_evidence.py --evidence evidence --output CHECK_RESULTS.json`。
这些是有界复现说明，不是常驻服务、自动恢复或已经采用的部署指令。
