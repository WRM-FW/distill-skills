# 无氧能力测试协议族（Wingate / 300-yd / 90-s 箱跳 / Margaria 冲刺）

## R — 原文 (Reading)

> "It is typically quantified as the maximal power output during muscular activity between 30 and 90 seconds using a variety of tests for the upper and lower body, as opposed to maximal anaerobic power tests, which last no longer than a few seconds. ... Six such round trips are made as fast as possible without stopping (6 × 50 yd = 300 yd [274 m])"

— Chapter 14 · Anaerobic Capacity / 300-yard Shuttle（`ch14.txt:147-150, 878-879`）

## I — 自述 (Interpretation)

无氧能力 = 磷酸原 + 无氧糖酵解系统联合的最大产能速率，通常以 **30–90 秒**肌肉活动中的最大功率输出量化，区别于只持续数秒的最大无氧功率测试（爆发动作约 1 s、低速最大力量 2–5 s，均以磷酸原 + ATP 为主）。

| 测试 | 关键参数 | 计分 |
|---|---|---|
| **Wingate** | 30 s 全力；达近最大踏频（通常 90–110 rpm）后快速加载；阻力按体重比例（如 7.5%，训练有素者更高）；功 = 阻力 × 转数 | 每 5 s 区间功率 = 功 ÷ 时间；峰值功率、平均功率、疲劳指数（最大/最小区间功率之比） |
| **300-yd 折返** | 25 yd 两平行线，6 个往返（6×50 yd = 274 m），不停歇；两人配对同时测；两次之间休息 5 min | 两次平均，精确到 0.1 s |
| **90-s 箱跳** | 18 in 高 × 30 in 宽箱；90 s 内左右横向跳越；双脚离地、双脚触箱顶后跳向另一侧；**禁踩箱** | 90 s 内合规触顶次数 |
| **Margaria-Kalamen** | ≥9 级台阶（级高约 18 cm）、助跑 ≥6 m、三级一跨；记录第 3→第 9 级触级时间（0.01 s） | 功率（见 `margaria-kalamen-power-calc`）；两次间隔 2–3 min |

## A1 — 案例 / 演练 (Application)

**原书未提供完整数值案例**（`f14-10`、`f14-25`、`p14-07`、`p14-08`、`p14-19`、`p14-20`）。

**合成演练（明确标记）**：运动员 300-yd 两轮成绩 55.0 s 与 56.4 s；90 s 箱跳触顶 78 次但踩箱 2 次。
- 300-yd = (55.0 + 56.4)/2 = **55.7 s**（0.1 s）。
- 箱跳合规 = 78 − 2 = **76 次**（踩箱不计）。
- 结论：平均值与合规计数口径明确。

## A2 — 未来触发 (Trigger)

**用户情境**：
1. 要测无氧能力，问选哪个测试、怎么计时/计数。
2. Wingate 的阻力设置、功率与疲劳指数怎么算。
3. 300-yd 两次成绩怎么汇总；箱跳哪些次数不算。
4. 想区分"无氧功率"（数秒）与"无氧能力"（30–90 s）。

**语言信号（中英双写）**：无氧能力 / 无氧功率 / Wingate / 300 码 / 折返跑 / 箱跳 / 疲劳指数 / anaerobic capacity / anaerobic power / Wingate test / 300-yard shuttle / box jump / 90 秒 / fatigue index / 重复次数计分。

**与相邻能力的区分**：本卡管 30–90 s 无氧能力族；Margaria 功率**换算**归 `margaria-kalamen-power-calc`；冲刺/变向（数秒）归 `speed-agility-test-protocols`；有氧能力族归 `aerobic-capacity-test-protocols`。

## E — 执行 (Execution)

**输入契约**：测试名 + 原始数据（两轮时间 / 触顶次数与违规次数 / 转数与阻力）。缺测试名无法选口径。

**步骤与完成标准**：
1. **选测试并确认时长口径**：确认属 30–90 s 无氧能力类（非数秒无氧功率）。完成标准：写明时长。
2. **300-yd**：配对、6×50 yd 不停歇、两次间隔 5 min → 取平均（0.1 s）。完成标准：给出平均时间。
3. **90 s 箱跳**：计合规触顶次数，**踩箱/单脚/未触顶不计**。完成标准：给出合规次数。
4. **Wingate**：功 = 阻力 × 转数；功率 = 功 ÷ 时间（每 5 s 区间）；报峰值/平均功率与疲劳指数。完成标准：给出三项参数。
5. **Margaria**（若用）：记录 0.01 s 精度时间，两次间隔 2–3 min；功率换算见 `margaria-kalamen-power-calc`。完成标准：给出时间（或移交换算）。
6. **输出**。

**输出契约**：`{测试名, 原始数据, 计分口径, 结果(平均时间/合规次数/功率参数), 无效或不计项说明}`。

**判停点/分支**：
- 计数类出现违规动作 → 该次不计（不是整测无效）。
- Wingate 未达近最大踏频即加载 → 标"加载条件不满足"。

**约定**：原文**未细化 Wingate"功 = 阻力 × 转数"的单位换算（如 kp·m）**，也未给疲劳指数的具体计算式（仅描述为最大/最小之比）；300-yd 与 90 s 箱跳"何时选用"未给判据（`p14-07`、`f14-10` gap）。本卡不虚构换算。

## B — 边界 (Boundary)

- **不要**把 Margaria 台阶冲刺当"无氧能力"测试——它是数秒的无氧**功率**测试。
- **不要**用计数值替代时间口径混淆（箱跳计次数、折返计时间、Wingate 计功率）。
- **作者盲点（3.3-5）**：7.5% 阻力等参数的"训练有素者更高"仅定性，共识 ≠ 实证。
- **常模时效（3.1）**：箱跳/折返常模来自特定组合项目，非普遍常模。
- **专业边界（2.2-14）**：无氧测试强度大，健康风险须先过 `test-health-safety-referral` 的红旗筛查。
- **相邻易混**：与 `speed-agility-test-protocols`（数秒速度）和 `aerobic-capacity-test-protocols`（长时间有氧）不同。

## 相关能力

- 组合（常配合使用）：`energy-system-interval-ratio`
- 组合（常配合使用）：`local-muscular-endurance-protocols`
