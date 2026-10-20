# 反应力量指数（RSI）与离心利用率（EUR）计算

## R — 原文 (Reading)

> "reactive strength index (calculated as jump height divided by ground contact time). ... The ratio of the vertical jump height with countermovement to squat jump height can be calculated as the eccentric utilization ratio. ... For the 10-5 repeated jump test, the best 5 repetitions in terms of reactive strength index are used and averaged for the test outcome."

— Chapter 14 · Drop Jump; Rebound Jump（`ch14.txt:772-808`）

## I — 自述 (Interpretation)

拉长—缩短循环（SSC）相关的两个指标，把"跳多高"再除以"触地多久"或"有无反向动作增益"，得到更能反映**快速伸缩能力**的数值：

- **RSI（反应力量指数）= 跳跃高度 ÷ 触地时间**。用于落地跳（drop jump）与反弹跳；被认为反映运动员调动 SSC"快成分"的能力。触地越短、跳得越高，RSI 越大。
- **10-5 反复跳**：取 RSI **最好的 5 次重复求平均**作为结果。
- **EUR（离心利用率）= 反向纵跳（CMJ）高度 ÷ 蹲跳（静力跳）高度**（无量纲比值）。反映反向动作对跳跃的增益。
- 两指标都建立在"跳跃高度取三次最佳"等基础计分精度之上（跳类测法见 `jump-power-test-protocols`）。

即：把跳跃结果归一化到"时间"与"有无反向动作"，用于监测爆发力与 SSC 能力。

## A1 — 案例 / 演练 (Application)

**类型：worked-example（原书公式算例 `c14-08`）。**

- 原文只给计算方法、**未给数值算例** → 补**合成演练（明确标记）**：
  - 落地跳跳高 0.35 m、触地时间 0.20 s → **RSI = 0.35 / 0.20 = 1.75 m/s**；
  - CMJ 40 cm、蹲跳 34 cm → **EUR = 40 / 34 = 1.18**。
- 10-5 反复跳：先算 10 次各自 RSI，取**最好的 5 次**求平均（原书规则）。
- 独立核算：1.75 m/s、1.176 → 1.18，与预期一致。

## A2 — 未来触发 (Trigger)

**用户情境**：
1. 做了落地跳/反弹跳，问"RSI 怎么算"。
2. 问"10-5 反复跳取哪几次 / 怎么汇总"。
3. 有 CMJ 与蹲跳两个跳高，问"离心利用率怎么算、代表什么"。
4. 想知道 RSI/EUR 的数值好坏（分类阈值）。

**语言信号（中英双写）**：RSI / reactive strength index / 反应力量指数 / 触地时间 / ground contact time / 落地跳 / drop jump / 反弹跳 / rebound jump / 10-5 / EUR / eccentric utilization ratio / 离心利用率 / CMJ / 蹲跳 / squat jump / SSC / 拉长缩短循环。

**与相邻能力的区分**：本卡管 **RSI/EUR 的公式、单位与汇总口径**（计算）；跳跃/深蹲跳的施测与计分精度归 `jump-power-test-protocols`；RSI 对照常模表（表 14.11）的口径归 `norms-lookup-interpretation`。

## E — 执行 (Execution)

**输入契约（必需字段）**：算 RSI 需 `jump_height`（数值 + 单位，m 或 cm）+ `ground_contact_time`（数值 + 单位，s）；算 EUR 需 `CMJ_height` + `squat_jump_height`（两者**必须同一测法与单位**）；算 10-5 需 10 次 RSI 序列。**缺单位须先问，不得静默假定**。

**步骤与完成标准**：
1. **统一量纲**（RSI 前）：把 jump_height 与 ground_contact_time 统一到 m 与 s。完成标准：输出以 m、s 为单位的两量（跳高若为 cm 先 ÷100）。
2. **算 RSI**：`RSI = jump_height(m) / ground_contact_time(s)`。单位 m/s。完成标准：输出 RSI，保留 2 位小数。
3. **10-5 汇总**：对 10 次 RSI **排序取最大的 5 次**，求平均。完成标准：输出"最佳 5 次 RSI 均值"。
4. **算 EUR**：`EUR = CMJ_height / squat_jump_height`（同测法、同单位，单位相消）。完成标准：输出 EUR（无量纲），保留 2 位小数。
5. **输出**：`{RSI(m/s), (可选)10-5 最佳 5 次均值, EUR, 测量方式说明}`。

**计算顺序**：先统一量纲 → 再算 RSI/EUR → （10-5）先算各次、再取最佳 5 次平均。

**容差与舍入**：RSI 保留 2 位小数（合成例 1.75）；EUR 保留 2 位小数（1.176→1.18）；判定容差 ±0.01。

**分支/判停**：
- 若 jump_height 与 contact_time 单位不明 → **先问**，标准口径为 m 与 s（原文未明确，本卡记为约定）。
- 若两次跳高用了不同测法/设备（如摸高 vs 力台）→ **不可比**，拒绝计算 EUR，须同法重测。
- 若问"RSI 多少算好" → 原文**未给分类阈值**（gap）；可查表 14.11 的群体描述数据，勿自造阈值。

## B — 边界 (Boundary)

- **原文未明确 RSI 高度/时间的单位与归一口径**（随设备而变），并**未给分类阈值**（gap）——本卡采用 m/s 与保留 2 位小数为**约定**，不改变原意；不要宣称有权威阈值。
- **可比性约束**：不同测法（摸高 / 力台 / 接触垫）的跳跃高度不可互换比较，EUR 的两跳必须同法同设备。
- **10-5 汇总易错**：取 RSI 最佳 5 次**平均**，不是平均 10 次、也不是取单次最大。
- **变量耦合**：RSI 同时受"跳高"与"触地时间"驱动，单看它会掩盖是哪一成分改变。
- **共识 ≠ 实证 / 单次数据意义有限**：RSI/EUR 是描述性指标，单次值不直接等于训练结论。
- **迁移不保证（3.3-1）**：SSC 指标改善不自动迁移到专项表现，须专项验证。
- **相邻易混**：本卡算数；施测步骤与取三次最佳归 `jump-power-test-protocols`。

## 相关能力

- 依赖（先理解）：`jump-power-test-protocols`
- 组合（常配合使用）：`plyometric-progression`
- 组合（常配合使用）：`ssc-speed-training-criteria`
