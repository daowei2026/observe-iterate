U3：无 broad formal U3；i 不取得 member-quality 资格
Outcome：i 后续更强，只能挑战 formation boundary，不能倒签成员
增量：时间/身份问题被准确提出；最终成员答案尚未产生
行动：增加 ex-ante lead/lag Formation 评估，而不是简单放宽 fixed bar threshold
```

---

# 7. SCN-05：近邻同方向不等于同一机会

## 7.1 市场事实

三品种 Up turn 落在两个 bar 内：

```text
i  = 2021-10-27 22:00
rb = 2021-10-27 22:30
hc = 2021-10-27 23:00
```

共同可知到 `2021-10-28 15:00`。它不在 exact-UTI C1 raw 中，Worker 没有伪造 C1/U2 layer。

从最后一个 anchor 23:00 起的回顾性路径：

| horizon | rb | hc | i |
|---|---:|---:|---:|
| 4 bar | +0.60% | +1.14% | -3.25% |
| 12 bar | +2.67% | +2.96% | -2.59% |
| 24 bar | +1.63% | +2.30% | -7.91% |
| 48 bar | -6.73% | -4.93% | -14.34% |

i 很早就与 rb/hc 分化，后来整组都失败。

## 7.2 为什么 N 不能替代当前候选质量

在共同可知时，N 的三个 current working episodes 都从 `2021-10-28 11:30` 开始，不是 10 月 27 日晚的三个选中 turn：

- rb current progress 155、efficiency 0.928；
- hc 163、0.862；
- i 25、0.781。

这些值描述的是后续新/current episode，而不是“10 月 27 日晚的 near-time 三 turn 是否同一机会”。把 N 当前值当作候选成员质量，会发生身份替换。

## 7.3 U2 判断

该场景同时证明两件事：

1. exact-UTI baseline 会漏掉“可能有关”的错时启动；
2. 仅凭 2-bar 时间邻近又会把质量迅速分化的对象放在一起。

因此，不能把结论简化成：

```text
把 exact 条件放宽到 2 bar
```

合法设计应是：

```text
near-time Formation candidate
→ episode overlap / direction persistence / qualification
→ accept or reject
```

当前 fixed package没有 formal U2 输出，所以该场景的最终组身份是 Unknown。

## 7.4 U3 判断

没有合法 Cluster/member identity，也没有 formal broad U3，因此：

- 可以观察路径和反例；
- 不能宣布 U3 已经提前挑出 rb/hc；
- 不能把后验 i 失败回填成当时正式 Quality。

## 7.5 场景结论

```text
U2：near-time 只是 candidate，不足以成立同一机会
U3：未调用／未提供，不能由 N 冒充
Outcome：i 先分化；48 bar 三者全部失败
增量：当前只有 KLine 反例和身份问题，没有正式 U2/U3 新结论
行动：建立可拒绝的 near-time Formation；禁止用固定 2-bar 阈值直接成组
```

---

# 8. SCN-06：第三对象初始应排除，后来同向不应倒签

## 8.1 市场事实

hc/rb 在 `2021-07-30 15:00` 同时 peak、方向 Down；到 `2021-08-02 11:00` 共同可知：

| 成员 | 净推进/起点 | efficiency | counter/起点 |
|---|---:|---:|---:|
| hc | 6.34% | 0.878 | 0.44% |
| rb | 5.95% | 0.877 | 0.42% |

两成员非常接近，没有足够业务依据强行选 winner。

第三对象 i 的 current Down episode 从 `2021-07-30 21:30` 才开始；到 common cut：

```text
progress = -2
progress / start ≈ -0.21%
efficiency = 0.056
counter / start ≈ 1.98%
```

固定 12/24 bar 中 i 仍与 hc/rb 的方向性结果相反；到 48 bar 才出现约 +4.84% 的 Down 方向累计运动。

## 8.2 U2 判断

本场景对 U2 边界提供强支持：

- hc/rb 是同一轮初始 Down 机会；
- i 在初始窗口不是同一 episode；
- 后来 i 也下跌，不构成初始成员身份的反证。

因此，静态钢材三品种组会把后来的共同方向误当成同一轮机会；U2 的时间身份和第三对象边界有真实增量。

## 8.3 U3 判断

hc/rb 在 common cut 的 Progress、Friction 都接近。正确输出应是：

```text
当前无法形成有意义的成员优劣差异
```

而不是为了 U3 存在而强行排名。

广域正式 U3 仍缺失；上述结论来自 C1/C0 raw 和基础路径。

## 8.4 场景结论

```text
U2：支持排除 i 的初始成员身份
U3：hc/rb 没有清楚 winner；formal broad U3 缺失
Outcome：i 后来加入方向，不应倒签原组
增量：相对静态三品种组，机会身份与时间边界明确增加信息
行动：保留 third-object / later-join 语义；允许 no-winner
```

---

# 9. 跨场景业务认识

## 9.1 U2 到底增加了什么

### 已支持

1. **机会身份不是静态板块。** SCN-06 显示，静态三品种一起看会错误纳入 i。
2. **共同身份不等于质量。** SCN-03 的三成员真实共同启动，后来整组失败。
3. **成员身份与后续赢家分开。** SCN-04 的 i 后来更强，不能倒签。
4. **成员生命周期是机会身份的一部分。** SCN-01/02 中，相同 actual turn 后成员很快进入不同 Episode。
5. **第三对象和 later join 值得显式记录。**

### 尚未支持

1. exact-UTI 是否是最终 Formation 规则；
2. lead/lag outsider 应当何时纳入；
3. near-time neighborhood 的合法阈值与 Qualification；
4. closed Universe 的 External Separation；
5. broad official Cluster/H1。

因此，U2 当前最清楚的业务价值是：

> 将“同一轮机会是谁、何时开始、何时可知、成员属于哪一个 Episode”组织成稳定身份。

不是：

> 找到事后最强品种。

## 9.2 U3 到底增加了什么

### 已支持的设计价值

1. Progress 与 Friction/Retention 可能冲突，单字段排名不成立；
2. lifecycle 和 observed bars 必须先于数值比较；
3. member-episode lineage 能避免把后续新 Episode 混进原机会；
4. 应允许整组弱、无赢家和 Withheld；
