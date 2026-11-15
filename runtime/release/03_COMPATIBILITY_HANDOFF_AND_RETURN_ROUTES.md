# Compatibility、交接与返回路线

## 版本组合

```text
Overlay v0.3
＋ A runtime v0.2
＋ B runtime v0.2
＋ C runtime v0.2
```

不得将 Overlay v0.2 和 v0.3 同时作为热规则。当前运行只使用 Overlay v0.3 与 A／B／C v0.2 runtime projection。旧版仅在归档区保留构建追溯，禁止作为运行输入，也不得要求执行器读取旧版目录。

## A→B

只有真实 A artifact 达到：

```text
Feature／Action／method／bounded-state／product／consumer闭合，
```

B才开始。A runtime包本身不是A业务artifact。

## B→C

只有真实 B artifact包含：

```text
frozen S0、realization、state plan、method binding、
materialization qualification、production/readback和VCC，
```

C才开始。B runtime包本身不是工程handoff。

## Return

```text
C repo fact → B RepoFact；
C realization/VCC → B Compiler；
B/C业务语义 → A；
平台能力 → platform owner；
价值取舍 → Owner。
```

## Existing artifact

恢复任何旧 artifact 时先比较其生成版本和当前release set，明确：

```text
KEEP；
REAUDIT_EXISTING；
RETROFIT_EXISTING；
STALE_PENDING_REBASE。
```

不得无声沿用旧完成声明。
