# C0015 实际执行记录

仅D008/R2。原S01～S06和R1研究材料复用；未重跑生产特征、未改参数/数据库/生产代码，零Worker。源目录与旧C冻结文件只读。

定向scan首次在读取已知展示索引时用了错误列名wall_local_id；该表实际为wall_local_no。异常发生于catalog首条构造、尚未成功形成选样/未来价格访问；更正本C独立研究脚本后实际扫描成功，选样只冻结一次。此前quote读取来源表保留的是同批数据，无生产或远端副作用。

S07保存四例、条件统计、quote/P1完整可得来源及逐行核验。图用既有C0007 plot-env生成，四张已逐幅视觉检查；未用新图像服务。未来价格仅在冻结选样后按固定10/30/60秒访问，后验交互检索则在选样前已发生并在selection中明记。

S08读取新增参考PreL0/FaoIngress/Publication原件及已存设计/TIS/FRP相关片段；全文件exact保存不等于逐行代码审计。43PG试查直接原始行核验，只追加两项字符串，未来Resolved仅后验审计。验证不冒充实际P2行为或正式版本验收。

发布使用获准Personal连接的Contents API，先核实际head与路径、串行写入，逐次保存intent/响应，按返回exact commit核内容、blob和父提交。具体事实由PUBLICATION_READBACK.json和publication/RETURN_HANDOFF.json给出；本文不提前声称发布完成。
