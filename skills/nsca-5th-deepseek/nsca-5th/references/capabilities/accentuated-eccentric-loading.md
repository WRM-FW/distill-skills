# 强化离心负荷（AEL）编程

## R — 原文 (Reading)

> "loads of 20% to 30% of body mass should be implemented during AEL when attempting to potentiate performance during the concentric phase of a plyometric jumping activity (91). ... significant improvements in concentric velocity with loads between 30% and 80% of the 1RM during the bench press when a maximal AEL (100% of the 1RM) is implemented. ... if a differential >40% between the AEL and the concentric load is programmed, significant acute increases in velocity and power occur during the concentric phase of the repetition (92)."

— Chapter 17 · Accentuated Eccentric Loading（`ch17.txt` 第 686–821 行）

## I — 自述 (Interpretation)

**AEL（accentuated / augmented eccentric loading）**：在**离心相施加额外负荷**，到**向心相前把它移除**——利用"肌肉离心比向心强（离心力量亏缺）"，故意让离心相超载，从而在向心相换取更好的速度/功率乃至长期最大力量增益。实现工具通常是**weight releaser**（离心末自动脱开的装置），弹震动作则用**手持哑铃/壶铃/带**在跳起前释放。

**AEL 是进阶手段，只给有扎实抗阻经验的运动员用**。

**离心负荷分级**（以向心 1RM 为基准）：
- **次最大（submaximal）**：< 100% 向心 1RM；
- **最大（maximal）**：= 100% 向心 1RM；
- **超最大（supramaximal）**：> 100% 向心 1RM。

**负荷处方（两条分支，量纲不同）**：
1. **弹震/跳跃类**（countermovement/box/drop/depth jump）：离心相加 **体重的 20%–30%**，离心末释放。
2. **多关节抗阻类**（bench press/back squat/front squat，用 weight releaser 或电脑驱动装置）：**向心相取 30%–80% 1RM**；
   - **最大 AEL（100% 1RM）** → 向心速度显著提升；
   - **超最大 AEL（105%–120% 1RM）** → 向心速度**变慢**（除非差值够大）。

**差值（differential）阈值**：AEL 负荷与向心负荷之差 **> 40%** → 向心速度与功率**急性显著提升**，长期应用**最大力量增长更大**。故即便用超最大 AEL，只要差值 > 40%，也可能受益。

**三种组结构**（原文）：①**每个重复都加 AEL**——须用 **cluster 组**（组内重复间休息 **15–40 s**）以便每重复重新装回 weight releaser；②**仅首重复加 AEL**——其余重复连续做，靠"增强的后段速度"受益；③**混合**——做若干"3 次一簇"的 cluster，**仅首重复加 AEL**、簇间 **25–35 s**，在提升 AEL 密度的同时保留第 3 次的急性增强。

## A1 — 案例 / 演练 (Application)

**书中案例一（worked-example，`c17-2`；出处 `ch17.txt` 第 753–763 行）——弹震类次最大 AEL**：反向纵跳离心相手持 **20 kg**（约体重 20%）哑铃、离心末释放，跳跃表现被**急性增强**；落跳（drop jump）用**体重 20%–30%** 的离心负荷，离心末释放后表现提升。结论：**AEL 跳跃类取体重的 20%–30%**。

**书中案例二（worked-example，`c17-3`；出处 `ch17.txt` 第 784–790 行）——差值 > 40%**：若 AEL 与向心负荷**差值 > 40%**，向心相的**速度与功率急性显著提升**；长期应用**最大力量增长更大**。

**合成演练（标记：合成；非书中案例）**：
- ①运动员体重 80 kg、做反向纵跳 AEL → 离心相加 **体重 20%–30% = 16–24 kg**，离心末释放。
- ②卧推做 AEL：离心取 **100% 1RM**、向心取 **50% 1RM** → 差值 = 100% − 50% = **50% > 40%** → 预期向心速度/功率急性提升；组结构可选"仅首重复加 AEL"或"3 次 cluster（首重复 AEL、簇间 25–35 s）"。
- 前置门槛：须为**经验丰富**的运动员。**原书未说明**合成输入的实测结果。

## A2 — 未来触发 (Trigger)

**用户会在什么情境下遇到这类问题**：
1. 用户问"离心加重（AEL / 强化离心）怎么安排负荷"。
2. 用户问弹震动作该在离心相加多少重量。
3. 用户问 weight releaser 怎么用、离心和向心负荷该怎么配。
4. 用户问 AEL 在组里放几次（每次 / 首次 / cluster）。
5. 用户问"离心向心差值多少才有效""新手能不能用 AEL"。

**情境的语言信号（中英双写关键 trigger 词）**：强化离心 / 离心超载 / AEL / accentuated eccentric loading / augmented eccentric loading / 离心加重 / eccentric overload / weight releaser / 离心释放 / 弹震离心负荷 / 10/5 训练 / 离心向心差值 / differential / 20%–30% 体重 / 首重复 AEL / cluster 离心。

**与相邻能力的区分（初稿）**：本卡只产出**AEL 的负荷分级、差值阈值、组结构与资格规则**。**链/带变阻负荷计算**属 `chains-bands-load-calc`；**替代手段是否采用**属 `alternative-modes-decision`；**plyometric 训练的整体编排**属 plyometric 能力；**RM 负荷本身**属负荷处方能力。

## E — 执行 (Execution)

**输入契约**
- 必需：**动作类型**（弹震/跳跃 vs 多关节抗阻）、**运动员抗阻训练经验**（是否达到 AEL 资格）、**向心 1RM**（抗阻分支需要）或**体重**（弹震分支需要）。
- 可选：目标（力量/功率/肥大）、可用装置（weight releaser / 电脑驱动 / 哑铃 / 带）。
- **缺失"经验"或"动作类型/基准负荷"应先询问**；新手不得默认给 AEL。

**步骤（每步可判断完成标准；含分支）**
1. **资格阀（前置门槛）**：确认运动员**有扎实抗阻经验**。
   - 完成标准：是 → 继续；否 → **不用 AEL**，改常规抗阻/弹震（原文：AEL 为 advanced tactic，仅限 extensive experience 者）。
2. **定分支与量纲**（分支）。
   - **弹震/跳跃类**：`离心负荷 = 体重的 20%–30%`（如 80 kg → **16–24 kg**），**离心末释放**。
   - **多关节抗阻类**：`向心负荷 = 30%–80% 1RM`；`离心负荷 ∈ {次最大 <100%, 最大 =100%, 超最大 105%–120%} × 向心 1RM`。
   - 完成标准：输出 `离心负荷` 与 `向心负荷`，并标明量纲（%体重 或 %1RM）。
3. **算差值并判增强**（判停点）。
   - `differential = 离心负荷% − 向心负荷%`。
   - **differential > 40%** → 预期向心速度/功率急性提升；**≤40%** → 不保证增强，需调整（提高离心% 或降低向心%）或改用其他方案。
   - **注意**：超最大 AEL（105%–120%）配 30%–80% 向心会使向心**变慢**，但差值 >40% 仍可能获益——须同时看差值。
   - 完成标准：输出差值数值与"是否 >40%"的结论。
4. **选组结构（三选一）**。
   - **①每重复 AEL**：用 **cluster 组，组内重复间 15–40 s**（给重新装回 releaser 的时间，含重新上/下架）。
   - **②仅首重复 AEL**：其余重复**连续**完成，靠后段速度增强受益。
   - **③混合**：**3 次一簇 cluster，仅首重复 AEL，簇间 25–35 s**。
   - （weight releaser 设置：使其在触胸前约 **2–4 in.（5–10 cm）** 处脱开。）
   - 完成标准：明确所选结构与对应间歇秒数。
5. **交付**：见输出契约。

**输出契约**
- 字段：`{ exercise_type(plyo|resistance), eligibility, eccentric_load{magnitude,unit(%BW|%1RM), level(submax|max|supramax)}, concentric_load(%1RM), differential(%), set_structure(every-rep|first-rep|hybrid), rest(15–40s | 25–35s | continuous), releaser_release(2–4in) }`。
- 完成标准：`differential` 与"是否 >40%"结论一致；组结构与间歇一致；资格未过则输出"不使用 AEL"。
- **已知边界（原文未定）**：原文明说"more research is needed to determine the most effective AEL programming strategies"；且**弹震分支（%体重）与抗阻分支（%1RM）量纲不同**，不可互相换算或混用。
- 单位：%体重 / %1RM；释放距离 in./cm（2–4 in. = 5–10 cm）。

## B — 边界 (Boundary)

- **不要**给新手/经验不足者用 AEL：原文明确"should be reserved for athletes with extensive resistance training experience"。
- **不要**混用量纲：弹震分支是 **%体重**、抗阻分支是 **%1RM**，二者不可互换。
- **不要**指望"超最大就更快"：105%–120% 超最大 AEL 配常规向心负荷会使向心**变慢**；增益取决于**差值 >40%**，须同时看差值。
- **不要**在"每重复 AEL"里省掉 cluster 间歇：否则来不及重装 weight releaser；三种结构各有其对应休息，不可随意删。
- **不要**把 AEL 当"确定的优越方案"：原文称"最优策略仍需更多研究"，肥大的增量与传统训练"comparable"，长期证据仍有限（共识 ≠ 实证）。
- **安全/医学边界**：离心超载对肌肉—肌腱应力大，损伤后或临床人群不适用；处置属医疗/康复范畴，教练不越界。
- **相邻易混**：把"链/带的负荷折算"（`chains-bands-load-calc`）或"该不该用某种替代手段"（`alternative-modes-decision`）混入本卡。

## 相关能力

- 组合（常配合使用）：`chains-bands-load-calc`
- 组合（常配合使用）：`plyometric-integration-complex`
