# 宏量营养素与能量需求估算

## R — 原文 (Reading)

> "The Cunningham equation takes fat-free mass (FFM) into account to estimate RMR, making it more applicable to athletes. RMR = 500 + 22 (FFM in kg)" / "strength or speed athletes should consume 5 to 6 grams of carbohydrate per kilogram body weight per day during peak training periods ... 1.4 to 2.0 grams of protein per kilogram body weight per day."

— Chapter 10（`ch10.txt:489`）+ Chapter 11（`ch11.txt:991, 1001, 1237-1239`）

## I — 自述 (Interpretation)

把「每公斤该吃多少」变成可核算的 g/kg 与 kcal 处方。骨架分三层：

- **能量需求估算**：三成分构成——BMR 约 65%–70%、体力活动约 20%–30%、食物热效应约 10%–15%。RMR 常用以替代 BMR（比 BMR 高 10%–20%）。运动员首选 **Cunningham**：`RMR = 500 + 22 × FFM(kg)`；再乘活动系数（PAL，见 Table 11.4，约 1.00–1.48；另一种口径 RMR×1.2–1.9）得 TDEE。
- **宏量换算底层常量**：碳水 4 kcal/g、蛋白 4 kcal/g、脂肪 9 kcal/g。
- **蛋白质档位（g/kg/天）**：成人 RDA 0.8；有氧耐力 1.2–2.0；增肌/正肌蛋白平衡 1.4–2.0；减热量期上调。蛋白 AMDR：成人 10%–35% 总热量（1–3 岁 5%–20%、4–18 岁 10%–30%）。**力量/速度运动员峰值训练期碳水 5–6 g/kg、蛋白 1.4–2.0 g/kg**（即使含耐力成分）。
- **单次剂量与分布**：运动后高质量蛋白约 0.4–0.5 g/kg 去脂体重；全天每 3–4 h 摄 20–40 g。
- **上限与辅助口径**：高蛋白安全上限约 **2.8 g/kg**（未损肾功能），但不应长期超过增肌/修复所需；纤维女 21–25、男 30–38 g/天；饱和脂肪 <10%、添加糖 ≤10% 总热量。
- **目标体重式**：`目标体重 = FFM ÷ (1 − 期望体脂%)`。

## A1 — 案例 / 演练 (Application)

**原书案例（worked-example，`c11-03`）**：Cunningham 方程为真题，但**原书未给 FFM 数值算例**；`c14-14` 给出 PAL 表（Table 11.4）。以下用真题**合成演练**（明确标记，可复算）。

**合成演练（标记：合成；可复算）**
- 输入：80 kg 力量运动员，FFM = 68 kg，峰值训练期；按蛋白 1.6–2.2 g/kg、碳水 5–6 g/kg 估算；用 Cunningham 估 RMR。
- 执行：
  1. 日蛋白 = 1.6×80 = **128 g** 至 2.2×80 = **176 g**；
  2. 日碳水 = 5×80 = **400 g** 至 6×80 = **480 g**；
  3. RMR = 500 + 22×68 = 500 + 1496 = **1996 kcal/天**；
  4. 乘活动系数（如 Active 1.25）→ TDEE ≈ **2495 kcal/天**。
- 容差：RMR 精确值 1996（±1）。
- 目标体重式核对：FFM 68、目标体脂 10% → 68/(1−0.10) = **75.6 kg**。
- 原书未说明该合成输入的「实际结果」，此处为按公式复算。

## A2 — 未来触发 (Trigger)

**用户情境（3–5 条）**
1. 运动员问「每天该吃多少蛋白质/碳水/热量」。
2. 需要按体重把宏量目标折算成克数与 kcal。
3. 要估算静息代谢率或每日总能耗。
4. 要按训练目标（增肌/减脂/耐力/力量）选蛋白档位。
5. 要算目标体重或核对宏量占比是否越界。

**语言信号（中英双写）**：每公斤蛋白 / 碳水摄入 / 热量需求 / 静息代谢率 / 每日总能耗 / 宏量营养素 / 能量需求 / macronutrient / energy needs / grams per kilogram / g/kg / protein RDA / Cunningham / RMR / TDEE / PAL / AMDR / target body weight。

**与相邻能力的区分（初稿）**
- 与 **body-composition-intervention**：本卡给「需求估算与 g/kg 档位」，增重/减脂的 ±500 kcal 干预归那张卡。
- 与 **competition-nutrition-timeline**：赛前/中/后的时机剂量归那张卡。
- 与 **nutrition-assessment-referral**：膳食换算查表（Table 10.8/10.11）与转诊边界归那张卡。
- 与 **glycemic-index-load**：GI/GL 计算另卡承载。

## E — 执行 (Execution)

**输入契约（必需字段）**
- 体重（kg）；去脂体重 FFM（kg，用于 Cunningham）；性别/身高/年龄（若用其他方程）；训练目标（增肌/减脂/力量/耐力）；训练量/活动水平；体脂率（若算目标体重）。
- **缺失须先询问，不得静默猜值**：若 FFM 未知 → 问体脂率或提示需体成分测量；若活动水平未知 → 问日常活动与训练时长以选 PAL；若目标未知 → 问增肌/减脂/维持。
- 适用条件：健康运动员与一般人群；临床营养问题须转诊。

**步骤（每步有完成标准）**
1. **算 RMR**——公式 `RMR = 500 + 22 × FFM(kg)`；单位 kcal/天。完成标准：输出 RMR 数值。
2. **算 TDEE**——查 Table 11.4 或取活动系数 1.00–1.48（另一口径 1.2–1.9）：`TDEE = RMR × 活动系数`。完成标准：输出 TDEE（kcal/天）。
3. **定蛋白档**——按目标查档（RDA 0.8 / 耐力 1.2–2.0 / 增肌 1.4–2.0 / 减脂上调）：`日蛋白(g) = 档位(g/kg) × 体重`。完成标准：输出蛋白克数区间。
4. **定碳水档（力量/速度峰值）**——5–6 g/kg：`日碳水(g) = 5~6 × 体重`。完成标准：输出碳水克数区间。
5. **换算与核对**——用 4/4/9 kcal/g 把克数折算热量，核对蛋白 AMDR（成人 10%–35%）与上限（≤2.8 g/kg）。完成标准：输出占比与是否越界。
6. **可选：目标体重**——`目标体重 = FFM ÷ (1 − 期望体脂%)`。

**输出契约**
- 字段：`{RMR(kcal/天), TDEE(kcal/天), 蛋白(g/天, g/kg), 碳水(g/天, g/kg), 占比(%), 是否越界, 目标体重(可选)}`。
- 单位：kcal/天；g/天；g/kg/天；%。
- 舍入/容差：RMR 取整（±1）；TDEE 取整；g/kg 区间照原文。
- **约定**：`目标体重式`原文写作 FFM/[100−期望体脂%]，百分号口径有歧义——本卡按 **FFM ÷ 期望去脂体重占比**处理并标注。
- **约束（原文只给方向未给数值，不得静默补值）**：
  - `p10-06` 低热量期蛋白「每降 100 kcal ≈ +1%」：原文**无精确公式与上下限**，本卡仅作经验换算，不外推。
  - `p11-04`「正常糖原基线」未定义；`p11-20` 目标体重式百分号歧义（已按上述处理）。
  - 原文未给 Cunningham 的适用人群边界，也未给 PAL 两套口径（PAL 值 vs 1.2–1.9）的换算关系。

## B — 边界 (Boundary)

- **不要**把预测方程当作精确值——RMR 预测不完美，FFM 可解释个体差异的 70%–80%，仍有个体残差（BOOK_OVERVIEW 3.3）。
- **不要**让高蛋白长期超过增肌/修复所需——可能挤占碳水与脂肪（及其附带营养素）。
- **不要**用 BMI 评估运动员——BMI 测「多余体重」非「多余体脂」，对肌肉发达者会高估、对老年人会低估；运动员应改体成分法。
- **作者盲点（3.1/3.3）**：方程系数与 PAL 表来自特定人群/年代；「共识 ≠ 实证」，g/kg 档位应结合个体响应与依从性。
- **专业边界（2.2-14）**：临床营养问题、以食物治疗疾病归运动营养师/医生（见 nutrition-assessment-referral）。
- **相邻易混**：与 **body-composition-intervention** 分工——本卡只算需求与档位，不裁 ±500 kcal 干预。

## 相关能力

- 组合（常配合使用）：`body-composition-intervention`
- 组合（常配合使用）：`competition-nutrition-timeline`
- 组合（常配合使用）：`energy-availability-red-s`
- 组合（常配合使用）：`ergogenic-dosing-evidence`
- 组合（常配合使用）：`glycemic-index-load`
- 组合（常配合使用）：`nutrition-assessment-referral`
- 组合（常配合使用）：`underperformance-attribution-triage`
