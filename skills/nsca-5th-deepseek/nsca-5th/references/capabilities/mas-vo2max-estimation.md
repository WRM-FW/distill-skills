# 最大有氧速度（MAS）与 VO2max 估算

## R — 原文 (Reading)

> "The last speed maintained for at least 2 minutes is considered the speed associated with V̇O2max or MAS. ... The V̇O2max of the athlete can be calculated by multiplying 3.5 × MAS (speed in km/h)."

— Chapter 14 · Maximal Aerobic Speed（`ch14.txt:1126-1131`）

## I — 自述 (Interpretation)

MAS（最大有氧速度）测试是一条**递增跑**：锥距 25 m，起始速度按体能取 8–12 km/h（一般建议 10），每 2 分钟提速 1 km/h，直到跑不动。

- **MAS 判定**：能**以至少 2 分钟维持**的最后一级速度，即与 VO2max 对应的速度。
- **终止**：连续两次未在要求时间内到达下一锥即停；若还能跑完半程，则在最后完成级速度上加 0.5 km/h。
- **换算**：VO2max(mL·kg⁻¹·min⁻¹) = 3.5 × MAS(km/h)。这与 1.5 英里跑的"只能查表"形成鲜明对比——**MAS 有公式，1.5 英里跑没有**。
- **无音频时**用哨声计时：到达下一锥的间隔 t = 锥距 ÷ 速度（如 25 m、10 km/h → 每 9 秒一哨）。

这是一个把"能维持的最后速度"直接翻译成有氧能力数值的轻量算法。

## A1 — 案例 / 演练 (Application)

**类型：worked-example（原书算例 `c14-06`）。**

- **哨声计时（原书例）**：锥距 25 m、设定速度 10 km/h → 10 km/h = 2.778 m/s → t = 25 / 2.778 ≈ **9.0 s**，即每 9 秒吹哨一次。
- **VO2max 换算**：原文只给公式、**未代入具体 MAS 值**。故补一条**合成演练（明确标记）**：设某运动员 MAS = 16 km/h → VO2max = 3.5 × 16 = **56 mL·kg⁻¹·min⁻¹**。

（说明：原书未给"某运动员 MAS 为某值→VO2max"的完整数值算例。）

## A2 — 未来触发 (Trigger)

**用户情境**：
1. 跑完 MAS（递增跑）测试，问"最后速度怎么转 VO2max"。
2. 想知道 MAS 测试的起速、增速、终止规则与哨声计时。
3. 对比"跑完 1.5 英里能不能用公式算 VO2max / 能不能用同样的 3.5× 换算"。
4. 用手上的锥距与设定速度算哨声间隔。

**语言信号（中英双写）**：MAS / maximal aerobic speed / 最大有氧速度 / VO2max / V̇O2max / 3.5 × MAS / 递增跑 / 哨声计时 / whistle timing / 25 m / 10 km/h / 起速 / km/h。

**与相邻能力的区分**：本卡只管 **MAS→VO2max 换算与哨声计时**（计算）；MAS 测试的完整施测/终止步骤与 1.5-mile/12-min/Yo-Yo/30-15 的族级口径归 `aerobic-capacity-test-protocols`；常模查表口径归 `norms-lookup-interpretation`。相邻易混：1.5 英里跑（无公式、只能查表）**不在本卡**。

## E — 执行 (Execution)

**输入契约（必需字段）**：`MAS`（数值 + 单位 km/h）；或用于哨声计时的 `cone_dist`（m）+ `set_speed`（km/h）。**缺单位须先问，不得静默假定**。若用户给的是"1.5-mile 跑时间"，**立即改走查表路径**（见 B 与分支）。

**步骤与完成标准**：
1. **确认 MAS**：取"保持 ≥2 分钟的最后一级速度"为 MAS（km/h）。完成标准：输出 MAS 数值与速度层级。
2. **算 VO2max**：`VO2max = 3.5 × MAS`。单位 mL·kg⁻¹·min⁻¹。完成标准：输出 VO2max，舍入到整数。
3. **（可选）哨声间隔**：`t = cone_dist ÷ (set_speed / 3.6)`（速度 km/h→m/s 再除）。完成标准：输出 t(s)，保留 1 位小数。
4. **输出**：`{MAS(km/h), VO2max(mL·kg⁻¹·min⁻¹), (可选) whistle_interval(s)}`。

**计算顺序**：先定 MAS（第 1 步是唯一的判定点）→ 再乘系数 → 再（可选）算哨声。

**容差与舍入**：VO2max 判定容差 **±1 mL·kg⁻¹·min⁻¹**（系数 3.5 为经验回归，量纲原文未解释，见 gap）；哨声间隔容差 **±0.5 s**；中间量保留 3 位有效数字。

**分支/判停**：
- 若输入是 **1.5-mile 跑时间** → **不得用本卡拟合**，改查表 14.22–14.25（按年龄/性别）得估计 VO2max（原文只给查表、无回归式）。
- 若速度为 mph → 先 ×1.60934 转 km/h 再代入。
- 若问"系数 3.5 从哪来" → 这是经验回归系数，原文未给量纲解释，标记为约定。

## B — 边界 (Boundary)

- **重要约束（已回原文确认）**：**1.5 英里跑推算 VO2max 原文只给查表（表 14.22–14.25/14.26），无回归公式，不得自行拟合**。本卡只管 MAS 的 3.5× 换算——不要把它套到 1.5-mile 或其他跑时数据上。
- **系数 3.5 是经验回归系数**，原文未解释其量纲（gap）；不要当作物理恒等式。
- **变量耦合**：MAS 受配速策略、锥距、起始速度与场地（坡度/地面）影响，跨测试条件不可直接比。
- **作者盲点（3.1）**：常模表（14.26）来自特定年代/样本人群，跨年代套用须核对。
- **单次数据意义有限**：VO2max 估计值是单点，不能替代训练判断，须结合趋势与专项需求（3.3-2）。
- **相邻易混**：与 `aerobic-capacity-test-protocols` 分工——本卡算数，族卡管施测与终止。

## 相关能力

- 依赖（先理解）：`aerobic-capacity-test-protocols`
- 组合（常配合使用）：`aerobic-intensity-zones-target-hr`
