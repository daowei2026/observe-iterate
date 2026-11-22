# C3→D 集成差异

原renderer `definition/caegraph_display.py` 与C3-v1逐字相同，SHA-256 `e5d6a235cd23f7e90ebbd8f020768f7e91b81ffd1782fc824362543c0f696ec0`；没有重做图，没有改C2-v4或生成另一预期HTML。

| 原C接口/样例 | D实际绑定 | 依据/留痕 |
|---|---|---|
| instance未绑定；预览为SYN | 正常make_features的基线F复制profile，仅override800；真实F实例序列化/目录逐项核同D008 | construct_instance / BOUND_INSTANCE_CHECK |
| reader占位 | 真实F OnlyRead/to_dfs全部31表；行情/Rct/selected从同实例已接受物化入口只读并校哈希 | read_bound_frames / SOURCE_DATA_BINDING |
| context/SOF由调用方提供 | TA_updto20240229_DBA/steel，2021-01-01—2023-12-31；D008平台存储路由，D011日志 | bound_environment / OptContext |
| 样例2022短窗 | 原B明确rb/hc/i、5m三年；原SOF日期规则及真实Calendar解析为含端点UTI72003600—101813399 | D-BIND-01；原请求不缩短 |
| native Float64窗口与C3整型接口 | 原值不改，严格核验后增加六个__uti_*别名 | D-BIND-02；拒绝非有限/分数/精度丢失 |
| round_display示例占位 | value1/2原值保留，显示0/1；选中known来自原事件轴，不用几何C替代 | D-BIND-03 |
| group/children/metadata占位 | occurrences及所有26子表完整父键/child层级；其余4张definitions族原值进入metadata | FIELD_BINDING / 原Schema |
| 原G公开规范源含参考筛查 | 仅取公开源13列；不把eligible/first_block/bend等分析派生作为原生轨迹 | adapt_selected及元数据来源声明 |
| 旧共享uplot版本/脏工作树 | 单进程加载20文件准确0a4快照；17实际依赖内容锁 | run_definition.bootstrap |
| 原C3页面标题 | renderer内标题逐字保留，真实绑定/历史位置投影由caption及HTML文档title明确 | 不无痕调整C2页面/图元/交互 |

新增完整实例集成定义和启动器见Python文件；C3文本diff为空。各派生表示、源字段、显示语义及上游确定性补齐详见DEFINITION_INTEGRATION_RECORD/UPSTREAM_CORRECTIONS；无回流。E未来若需改变位置/展示/理解，按原Skill具名回流。
