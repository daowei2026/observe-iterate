# 具名来源／业务待决项

1. **B 外层 ZIP 身份差异（成员一致，未换源）**：实际读取 `/dwdhome/fy/资金管理/rb_hc_i_mid贴近转折_zig_small_K线_20210101_20240229.zip` 的 SHA-256 为 `ff3215126461a0cda564c82c4a6e42b99bf94cb7b6a8320df9c8ba93d269d70a`；工单／Pro 实际消费字节记为 `4fd1af4e7b34af6fc099e6289ffdd5d83125412fc16d2a9902af4fd9741b3987`。FIXED_INPUT_MEMBERS 所列全部 40 个成员（38 CSV+2元数据）SHA／行数一致。按工单保留来源资格差异未知，不开展外层差异重验算，不更换输入，其他技术施工继续。请主控原样交执行 Pro 判断影响。
2. **N/02 单位标签已知限制**：business_duration、normalized_amplitude 空值仍保留原 unit_semantics=per_symbol_raw_quote；显示端明确“未输出值；该单位元数据不授予时长价格单位”，不填值、不改源。
3. **运输能力**：本调用环境未暴露 send_message_to_thread；不绕过工具发送消息。本目录文件与当前聊天 commentary 为主控读取实际进展的入口。
