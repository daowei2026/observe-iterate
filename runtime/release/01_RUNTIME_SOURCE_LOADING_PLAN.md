# Runtime Source Loading Plan

## 固定 core

```text
R00 release front door；
O00 overlay entry；
O01 shared long-horizon contract；
O02 source/version/human participation；
O11 current-turn self-record and substantive material publication。
```

## Mission A selected core

```text
A00 front door；
A01 P0 feature narrative；
A02 Work Map 或 A03 Local Contract（二选一）。
```

## Mission B selected core

```text
B00 front door；
B01 RepoFact 或 B02 Compiler（二选一）；
Compiler额外B03 realization。
```

## Mission C selected core

```text
C00 front door；
C01 implementation judgment；
C02 host method。
```

## Triggered optional

```text
实现者finding → A06／B04；
handoff／stale → O06；
上下文续跑 → O07；
fuzzy/state/complexity → A04；
source/maintenance → A05／B05／C06；
production/checkpoint → C04；
defect/recovery → C05；
case/nonclaim → 各Mission末尾case文件。
```

规则：承重方法不靠摘要替代；减少上下文依赖“按对象选卷”，不是把方法正文缩成口号。

## 2026-09-07 持续工作面读取

新建／中途接续：读 `O09_GITHUB_WORKSPACE.md`、`O10_REVIEW_AND_ROUTE.md`，再选上述 Mission 主体卷。独立审查：读 O10、当前任务地图与被审完整正文，先判断实质，再选下一问题。普通执行：读地图、已签发任务、明确必读正文，按触发补相关深材料。

O09/O10 是对应 canonical Overlay 的完整生成副本；不要把所有 Mission 一次装入上下文，也不要把只读这两卷当成已读业务方法。实际文件对应关系见 `WORKSPACE_PROJECTION_MAP.yaml`。

## 2026-09-08 本轮交付与补齐

正常提交与 MATERIAL_CATCHUP 读取 O11；它规定 Pro 自存本轮、历史问答免补、必要正文去重入库和远端实读。对应 canonical 是 `11_本轮问答与实质材料入库.md`。补齐的分批启动语在 O_08，不另建第二套提示。保存完整不等于每轮全读历史；仍按当前问题加载业务正文。

## C的正常主线与实际当前工作

先从Mission C当前入口取得五段主线与相邻角色责任，再按实际问题读完整方法。每轮C消息从Overlay08取共同定位、角色定位及已采用任务／合法continuation原文；不用上轮读取布尔值替代新上下文取得。工程师另读DR11和current唯一工作单，材料更新不解除暂停。
