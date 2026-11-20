# C0003｜原 D001 的 V2 Return 同源格式补正

[OI-U2-Q-OBS-20261120-01-C0003]
invocation_token=1420381b6df34954aed0b736cd8b8ec5

你仍是本 Run 的原独立 Skill executor:E1；本次接续原 D001 / WI-A / M-A，仅补正机读回交格式。A 的专业报告和两份原生产物已经取得并逐字/hash核验，原生产物和历史原件保留，不重跑 A，不重签 D。

- run_id：OI-U2-Q-OBS-20261120-01
- sender：chatgpt:OI-U2-Q-OBS-20261120-01:executor:E1
- return_to：chatgpt:OI-U2-Q-OBS-20261120-01:manager
- 原 manager issuer_call_id：C0001
- delegation：daowei2026/observe-iterate@2944f650baf779308fcc7fa92d20c6b0b4ca0e71:longrun/runs/OI-U2-Q-OBS-20261120-01/delegations/D001/DELEGATION.json
- 原委派正文：daowei2026/observe-iterate@53efeadf4d38c335eae2bb2f874d2cce151ecac6:longrun/runs/OI-U2-Q-OBS-20261120-01/delegations/D001/DELEGATION.md
- 原实际 C0002 Return：daowei2026/observe-iterate@37548df36c05344854d2d6b2efe8ea94640323cf:longrun/runs/OI-U2-Q-OBS-20261120-01/calls/C0002/PRO_RETURN.json
- 原专业报告：daowei2026/observe-iterate@23aab75c3415fe247e91f78a4079dfc8a80bfa57:longrun/runs/OI-U2-Q-OBS-20261120-01/calls/C0002/PROFESSIONAL_REPORT.md

## 实际格式错误

当前已采用的 V2 Schema 为 `daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:longrun/contracts/longrun_schema_v2.json`。原 C2 Return 使用 status、artifacts、completion_evidence、delegation_id、errors、next_action、worker_orders、worker_results 等字段，且缺少 professional_return 必填字段；独立 validate-executor-return 因 additionalProperties=false 拒绝。主控没有替你改写 Return，也没有将它路由为已验收结果。

请由你同源发布原 C0002 的正确 V2 PRO_RETURN.json（保持原 C2 身份与原 D001；保留旧精确提交及原报告/产物），并为本次 C0003 发布你自己的合法 V2 PRO_RETURN.json 与必要的简短格式补正说明。原专业结论由你按已完成的 A 工作签认；本次不是新增专业工作或验收条件。必要原生产物仍通过原专业报告的精确引用完整交回原 manager。

请完整读取并采用原版本的 `longrun/professional/PRO_EXECUTOR_GUIDE.md`、`longrun/contracts/LONGRUN_PROTOCOL_V2.md` 及上述 Schema；不要沿用原错误 JSON 形状。下方是该 Schema 的 `$defs.professional_return` 原样对象提取，嵌套 $ref 的定义仍以完整原 Schema 为准：

```json
{
  "type": "object",
  "additionalProperties": false,
  "required": [
    "schema",
    "run_id",
    "call_id",
    "role",
    "sender",
    "delegation_ref",
    "return_to",
    "result_ref",
    "issued_delegation_refs",
    "issued_order_refs",
    "accepted_worker_refs",
    "professional_state",
    "remaining_scope_ref",
    "continuation_ref",
    "owner_request_ref"
  ],
  "properties": {
    "schema": {
      "const": "longrun-professional-return/v2"
    },
    "run_id": {
      "$ref": "#/$defs/id"
    },
    "call_id": {
      "type": "string",
      "pattern": "^C[0-9]{4,}$"
    },
    "role": {
      "enum": [
        "manager",
        "executor"
      ]
    },
    "sender": {
      "type": "string",
      "minLength": 1
    },
    "delegation_ref": {
      "$ref": "#/$defs/optionalRef"
    },
    "return_to": {
      "anyOf": [
        {
          "type": "string",
          "minLength": 1
        },
        {
          "type": "null"
        }
      ]
    },
    "result_ref": {
      "$ref": "#/$defs/ref"
    },
    "issued_delegation_refs": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/ref"
      },
      "uniqueItems": true
    },
    "issued_order_refs": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/ref"
      },
      "uniqueItems": true
    },
    "accepted_worker_refs": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/ref"
      },
      "uniqueItems": true
    },
    "professional_state": {
      "enum": [
        "IN_PROGRESS",
        "WAITING_OWNER",
        "REPORTED_COMPLETE"
      ]
    },
    "remaining_scope_ref": {
      "$ref": "#/$defs/optionalRef"
    },
    "continuation_ref": {
      "$ref": "#/$defs/optionalRef"
    },
    "owner_request_ref": {
      "$ref": "#/$defs/optionalRef"
    }
  }
}
```

三类 refs 数组以及专业状态/剩余范围/接续/Owner 请求字段均须按你当前真实工作填入。所有 ref 使用不可变40位Git提交；result_ref 指向真实先发布的专业报告/格式补正说明。Return 发布顺序及当前调用的准确身份按实际 INVOCATION.json 执行。不要把旧 C2 的正文改成 C3 身份，也不要把协议补正称为新的业务阶段完成。

回交时明确给出：原 C2 更正版 Return 的精确 ref、本 C3 Return 的精确 ref、原 A 专业报告与两产物的原精确 refs。当前原件的旧精确 ref 一律保留。当前 C3 的完整回交结束后，以实际 C3 marker 与 token 写 turn complete 并在答复结尾明确当前调用已完成。
