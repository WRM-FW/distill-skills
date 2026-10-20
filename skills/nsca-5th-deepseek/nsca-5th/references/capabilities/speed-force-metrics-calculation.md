# 速度 / 变向 / 敏捷的力学指标口径与计算（RFD / impulse / momentum / power / COD deficit）

## R — 原文 (Reading)

> "Impulse—The product of the generated force and the time required for its production, which is measured as the area under the force–time curve. According to the impulse–momentum relationship, net impulse dictates the magnitude of change of momentum of an object." ... "the generation of maximal contraction force takes at least 300 milliseconds, while many sport activities consume 0 to 200 milliseconds" ... "to isolate COD ability, the COD deficit (5-0-5 test time—10 m linear sprint time) could be determined."

— Chapter 20 · "Impulse"（`ch20.txt` 第 183–196 行）；"Rate of Force Development"（第 156–162 行）；"Factors Affecting Change of Direction…"（第 1235–1243 行）

## I — 自述 (Interpretation)

这套口径把"提升爆发/速度"从抽象目标改写成可测的力学量。关键事实：产生最大收缩力至少要 300 ms，而多数运动动作只占 0–200 ms，所以在限时场景里限制因素是**单位时间发力速率 RFD**（= Δforce/Δtime），而非最大力量。**Impulse 冲量**（力 × 时间 = 力—时间曲线下面积）经冲量—动量关系决定动量变化，是加速/减速的直接抓手；**Momentum 动量** = 质量 × 速度，体重固定时只能靠增大净力来改变动量。**Power 功率**是力与速度的派生量（P = F·v），单独测它不如直接测力与速度。变向还要区分 braking impulse（负向、制动）与 propulsive impulse（正向、再加速）：角度越大、入速越高，所需冲量越大。为把直线速度从变向测试里剥离，用 **COD deficit = 5-0-5 时间 − 10 m 直线冲刺时间**；再用 **sprint momentum = 均速 × 体重**表征制动需求。训练与监测都落在力、RFD、impulse 三项直接底层特征上。

## A1 — 案例 / 演练 (Application)

**原书例题（c20-5，Ch20）**：同长度直线冲刺时间与 COD 测试时间（如 10 m 直线 vs 5-0-5 的 10 m 段）；方法：COD deficit = COD 测试时间 − 同长度直线冲刺时间；结果：得出额外变向耗时，用于评估变向能力（原书另注该指标可能偏向慢速者）。原书未给具体数值结果。

**合成演练（明确标记，可复算；数据来自阶段 1.5 构造）**：力—时间曲线某次触地在 0→0.05 s 内力由 0 升至 1,500 N，随后 0.20 s 内平均力 500 N；运动员 80 kg；5-0-5 用时 2.60 s，10 m 直线冲刺 1.85 s，直线段均速 5.0 m/s。
- RFD = 1500 ÷ 0.05 = **30,000 N/s**
- Impulse = 500 × 0.20 = **100 N·s** → Δmomentum = 100 kg·m/s → Δv = 100 ÷ 80 = **1.25 m/s**
- COD deficit = 2.60 − 1.85 = **0.75 s**
- sprint momentum = 5.0 × 80 = **400 kg·m/s**
- 判定：触地窗口 0–200 ms 落在"最大力需 ≥300 ms"之下 → 限制项是 RFD/impulse 而非最大力。

## A2 — 未来触发 (Trigger)

**用户会在什么情境下遇到这类问题**
1. 想知道运动员"爆发力不足"到底该测什么、怎么量化。
2. 拿到 5-0-5 成绩，却想剥离"直线速度"影响，单独看变向能力。
3. 教练问"是不是该测 power"，或拿功率数据来指导训练。
4. 需要解释为什么慢速动作的测量对短时动作无代表性。

**语言信号（中英双写关键 trigger）**
- 中文：「算一下 COD deficit」「5-0-5 和直线冲刺差多少」「RFD 怎么算」「impulse/momentum 单位」「要不要测功率 power」「加速保持的力学」
- English: "COD deficit calculation", "rate of force development formula", "impulse-momentum", "should we measure power", "sprint momentum"

**与相邻能力的区分（初稿，阶段 3 回填）**
- 与 `speed-cod-agility-attribution`：本卡**计算数值**，后者做定性归因。
- 与 `speed-agility-monitoring`：本卡给公式与算例，后者给监控变量表与变化方向解读。
- 与 `cod-angle-training-orientation`：本卡算量，后者把量转化成训练取向。

## E — 执行 (Execution)

**输入契约**
- RFD：Δforce (N) + Δtime (s)，或力—时间曲线。
- Impulse：力—时间曲线（或 F、t）。
- Momentum：m (kg) + v (m/s)。
- COD deficit：5-0-5 用时 (s) + 10 m 直线冲刺用时 (s)（须**等长度口径**）。
- sprint momentum：冲刺平均速度 (m/s) + 体重 (kg)。
- 缺失上述任一必需项时应先询问，不得静默猜值。

**公式与计算顺序**
1. RFD = Δforce ÷ Δtime（N/s）
2. Impulse = F × t = ∫F dt；net impulse = Δmomentum = m·Δv（N·s）
3. Momentum p = m × v（kg·m/s）
4. Power P = F × v（W）——**派生量**，仅作参考
5. COD deficit = 5-0-5 时间 − 10 m 直线冲刺时间（s）
6. sprint momentum = 平均速度 × 体重（kg·m/s）

**判定分支**
- 若目标动作时间窗 ≤200 ms 而最大力需 ≥300 ms → 限制项是 RFD/impulse，而非最大力。
- 角度越大或入速越高 → 所需（braking）impulse 越大，动作物理负荷越高。

**容差与约定（原文未规定，标为本卡约定）**
- 原文**未显式给** impulse / momentum 的 SI 单位；本卡按 SI 采用 N·s、kg·m/s（verified 记录已标为待补规范项）。
- COD deficit 仅在 COD 测试总长与直线冲刺**等长**时成立（常见 5-0-5 = 10 m）。
- 计算建议保留 2 位小数；RFD/impulse 容差 ±2%，COD deficit 容差 ±0.01 s。

**输出契约**
- `{RFD, impulse, momentum, power, COD deficit, sprint momentum}` 各带单位 + 限制项判定结论。

**缺口声明（勿补造）**
- Ch20 **未给 RSI（reactive strength index）计量公式**；本章 "reactive strength" 只是定性训练优先项，RSI 数值口径属 Ch19（plyometric），本卡不补造。

## B — 边界 (Boundary)

- **不要用**：当问题只是"这是哪种能力"时（用 `speed-cod-agility-attribution`）；当需要判断进步方向而非算数时（用 `speed-agility-monitoring`）。
- **作者警告的失败模式**：只测 power 不看力/速度 → 得不到可操作的洞察（原书明确："measurement of power alone does not give insight…"）。
- **盲点（BOOK_OVERVIEW 步骤 3）**：RFD 在毫秒级窗口取值高度依赖采样频率与触发阈值；COD deficit "可能偏向慢速运动员"、提供信息有限；单次数据不足以决策，需与常模/历史/专项需求三方对照。
- **相邻易混**：`speed-agility-monitoring`（变量解读）、`sprint-step-length-frequency`（速度两变量诊断）。

## 相关能力

- 组合（常配合使用）：`margaria-kalamen-power-calc`
- 组合（常配合使用）：`power-load-assignment`
- 组合（常配合使用）：`speed-agility-monitoring`
- 组合（常配合使用）：`sprint-step-length-frequency`
