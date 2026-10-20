# 有氧强度分区标尺与目标心率公式（对照表）

- 来源：src-nsca-essentials-5e · Chapter 21 "Aerobic Endurance and Metabolic Training"（`ch21.txt`）
- 用途：为 `cap.nsca.aerobic-intensity-zones-target-hr`（心率/分区换算）、`cap.nsca.aerobic-program-design`（强度变量）、`cap.nsca.recovery-session`（Zone 1）与伞形 `cap.nsca.aerobic-endurance-design` 提供可复算的档位与公式。
- 说明：两类表格逐字取自原文 Table 21.1、Table 21.2；两套公式与算例逐字取自原书 "Target Heart Rate Calculations" sidebar。未作改写。

---

## Table 21.1 — Example of a Five-Zone Intensity Scale to Prescribe and Monitor Training of Aerobic Endurance Athletes

| Intensity zone | O2 (% max) [即 %VO2max] | Heart rate (% max) | Lactate (mmol/L) | Typical accumulated duration within zone |
|---|---|---|---|---|
| 1 | 50-60 | 60-72 | 0.8-1.5 | 1-6 h |
| 2 | 66-80 | 72-82 | 1.5-2.5 | 1-3 h |
| 3 | 81-87 | 82-87 | 2.5-4.0 | 50-90 min |
| 4 | 88-93 | 88-92 | 4.0-6.0 | 30-60 min |
| 5 | 94-100 | 93-100 | 6.0-10.0 | 15-30 min |

脚注（逐字）："This scale is typical of intensity zone scales used for aerobic endurance training prescription and monitoring. The scale was developed by the Norwegian Olympic Federation as a general guideline based on years of testing of cross-country skiers, rowers, and biathletes."（Reprinted by permission from S. Seiler, "What is Best Practice for Training Intensity and Duration Distribution in Endurance Athletes?" IJSPP 5 (2010): 277.）

> 使用告警：区间边界是**惯例而非生理断点**，属通用指南；跨项目迁移需校验。

---

## Table 21.2 — Relationship Between VO2max, Heart Rate Reserve (HRR), and Maximal Heart Rate (MHR)

| % VO2max | % HRR | % MHR |
|---|---|---|
| 50 | 50 | 66 |
| 55 | 55 | 70 |
| 60 | 60 | 74 |
| 65 | 65 | 77 |
| 70 | 70 | 81 |
| 75 | 75 | 85 |
| 80 | 80 | 88 |
| 85 | 85 | 92 |
| 90 | 90 | 96 |
| 95 | 95 | 98 |
| 100 | 100 | 100 |

> 要点（逐字）：%VO2max 与 %HRR 数值相等（近似线性），换算成 %MHR 时明显偏高。用途：心率为唯一监控手段时，把目标 %VO2max 换算为相应 %MHR。
> 使用告警：心率与摄氧量仅在 **50%–90% 功能容量（HRR）** 区间关系良好；越界（尤其高强度区）关系变弱。

---

## 两套目标心率公式与算例（逐字，Chapter 21 sidebar）

### 方法一 · Karvonen Method（%HRR）

Formula:
- Age-predicted maximum heart rate (APMHR) = 220 - age
- Heart rate reserve (HRR) = APMHR - resting heart rate (RHR)
- Target heart rate (THR) = (HRR × exercise intensity) + RHR

要得目标心率**区间（THRR）**，用处方强度的最小值和最大值各算一次。

Example（30 岁，RHR 60，强度 60%–70% 功能容量）：
- APMHR = 220 - 30 = 190 beats/min
- RHR = 60 beats/min
- HRR = 190 - 60 = 130 beats/min
- Lowest = (130 × 0.60) + 60 = 78 + 60 = **138 beats/min**
- Highest = (130 × 0.70) + 60 = 91 + 60 = **151 beats/min**
→ 目标心率区间 **138–151 次/分**

### 方法二 · Percentage of Maximal Heart Rate Method（%MHR）

Formula:
- Age-predicted maximum heart rate (APMHR) = 220 - age
- Target heart rate (THR) = (APMHR × exercise intensity)

Example（20 岁，强度 70%–85% 最大心率）：
- APMHR = 220 - 20 = 200 beats/min
- Lowest = 200 × 0.70 = **140 beats/min**
- Highest = 200 × 0.85 = **170 beats/min**
→ 目标心率区间 **140–170 次/分**

### 计算顺序与容差（约定）
1. 计算顺序：先算 APMHR →（Karvonen 再算 HRR）→ 对强度最小/最大各算一次 THR。
2. 舍入：四舍五入到 1 次/分（原例均为整数）。
3. 容差：APMHR 的个体标准差为 **10–12 次/分**（Fox 方程，原书明示），故心率区间为处方靶区，建议以 ±5–10 次/分带宽监控；**两法不可混用**。

---

## 附：三区口径（按乳酸/通气阈，`ch21.txt` p21-03 语境）
- 低强度/有氧区：血乳酸稳定 **<2 mmol/L**
- 乳酸阈区（LT 训练）：**2–4 mmol/L** 之间维持稳态
- 高强度/无氧区：**>4 mmol/L**
> 2/4 mmol/L 为常用口径，非绝对生理阈值；个体 LT 需实测。
