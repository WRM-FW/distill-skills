# 用变量填充一个中周期（Table 22.3 档位落地）

## R — 原文 (Reading)

> "The hypertrophy or strength–endurance phase involves low to moderate intensity (50%-75% of the 1RM) and high volumes (3 to 6 sets of 8-20 repetitions). ... The basic strength phase involves higher intensity (80%-95% of the 1RM) and moderate to high volumes (2 to 6 sets of 2 to 6 repetitions). ... The strength/power phase involves low to very high loads (30%-95% of the 1RM, depending on the exercise) and low volumes (2 to 5 sets for 2 to 5 repetitions)."

— Chapter 22 · Preparatory/First Transition Period 各相正文框（`ch22.txt` 第 502–597 行；Table 22.3）

## I — 自述 (Interpretation)

"填充一个中周期"= 先看这块落在哪个 period，据此定**目标相位**，再用 **Table 22.3** 给该块设定强度、量、组数、次数，并选动作（表中按非爆发核心动作 / 爆发动作给出不同 %1RM）。五个相位的档位：

| 相位 | 强度 | 量 | 组×次 |
|---|---|---|---|
| hypertrophy / strength–endurance | 低–中 50%–75% 1RM | 高 | 3–6 组 × 8–20 次 |
| basic strength | 高 80%–95% 1RM | 中–高 | 2–6 组 × 2–6 次 |
| strength/power | 低–很高 30%–95% 1RM（依动作） | 低 | 2–5 组 × 2–5 次 |
| peaking | 50%–≥93% 1RM | 极低 | 1–3 组 × 1–3 次 |
| maintenance | 中–高 85%–93% 1RM | 低–中 | ~2–5 组 × 3–6 次 |

落到**具体重量**需三步：相位取档 → 用运动员已测 RM → 按样例的周内阶梯升负荷；并遵守两条样例口径：**周五课减 10%**（preseason 一处为 15%）；**3–5 组热身不计入目标组**。赛内则**不用真实 RM 负荷**（练到力竭会降功率、增过度训练风险），改用"基于 RM 的百分比区间"应对累积疲劳。**具体重量换算依赖 Ch18 的 RM 表**——见 `cap.nsca.load-and-repetition`（本节不复制其数值）。

## A1 — 案例 / 演练 (Application)

**原书案例（tabular-example，Table 22.3 / c22-3 + 样例 Mesocycle 3）**：原书 Table 22.3 给出五相档位；样例计划 Mesocycle 3（basic strength）以"**80%-84% 5RM / 85%-89% 5RM / 90%-94% 5RM**"的三周阶梯表示 3 组 × 5 次。

在其上做一次**可复算演练**（合成，步骤依原文规则）：
- 输入：中级运动员，处于 basic strength 相；已测 **back squat 5RM = 120 kg**；目标 3 组 × 5 次，排 3 周中周期。
- 计算：
  - 周1 = 80%–84% → 0.80×120 = **96 kg**，0.84×120 = 100.8 ≈ **101 kg**
  - 周2 = 85%–89% → 102 kg – 106.8 ≈ **107 kg**
  - 周3 = 90%–94% → 108 kg – 112.8 ≈ **113 kg**
  - 周五课 = 周一负荷 × 0.90（周一 100 kg → 周五 90 kg）
  - 热身另加 **3–5 组**，不计入 3 组目标组
  - 若该块落在竞赛期 → 改用 %RM 区间（如 75%–79% 6RM），**不练到力竭**
- 输出：一个"带目标相位与变量取值"的中周期，风格与样例 Mesocycle 3 一致。容差 ±1 kg。
- **口径说明**：样例把强度写作"80%-84% 5RM"，本卡按阶段 1.5 验证口径解释为**"目标 RM 负荷的百分比"**（故 0.80×120）。此为原文表记的歧义点（亦可读作 %1RM）；采用本口径以保证与样例金字塔自洽，按 %1RM 解释则须先由 RM 反推 1RM。

## A2 — 未来触发 (Trigger)

**用户会在什么情境下遇到这类问题**
1. 用户要把某个中周期的"强度/量/组次/重量"具体排出来。
2. 用户问"basic strength 用多少 %1RM、几组几次？"
3. 用户想知道"赛内为什么不测 RM / 怎么定重量？"
4. 用户问"周五要不要减重 / 热身算不算组数？"

**语言信号（中英双写）**
- 中："这个中周期重量怎么定""基础力量相几组几次""赛内用多少 %RM""周五减多少""热身算几组"。
- 英："fill a mesocycle with variables", "intensity and volume for basic strength", "percentage based off RM in-season", "Friday 10% less".

**与相邻能力的区分（初稿）**
- 本卡只做"块内变量落值"。年度排布 → `cap.nsca.annual-plan-construction`；赛内调度 → `cap.nsca.in-season-load-management`；**纯 RM↔重复换算/由 RM 估 1RM（Table 18.8/18.9）** → `cap.nsca.load-and-repetition`（簇 A）。

## E — 执行 (Execution)

**输入契约**
- 必需：该 mesocycle 所属 period/相位；运动员**已测 RM**（如 5RM，单位 kg）或 1RM；目标组数×次数。
- 可选：是否落在竞赛期（决定用不用 RM 区间）、周内训练日安排。
- 缺失处理：**无 RM/1RM 不得猜重量**——先询问或安排测试周；无相位不得选档位。

**步骤**
1. 定相位：查该块所属 period，定 hypertrophy/basic strength/strength-power/peaking/maintenance。完成标准：写出相位名。
2. 取档位：查 Table 22.3（见 `resources/periodization-model-table.md`）取强度区间、量、组×次。完成标准：写出强度%与组×次。
3. 落值到重量：目标重量 = 强度下限/上限 × 参考 RM 负荷（或按 1RM 换算，换算见 `cap.nsca.load-and-repetition`）。**舍入到 1 kg（容差 ±1 kg）**。完成标准：得每周具体 kg。
4. 套样例口径：周五课 = 周一 ×0.90（preseason 可取 ×0.85）；另加 3–5 组热身、不计入目标组。完成标准：周内每日负荷列表完整。
5. 分支——赛内：若 block 在 in-season，**改用 %RM 区间、不练到力竭**，并保留 2–3 天恢复间隔。完成标准：无 RM-力竭处方。
6. 自检：组×次与强度区间是否落在同相位（如 5 次却在 peaking 档 → 冲突回步骤 1）。完成标准：无相位-档位错配。

**输出契约**：`mesocycle → 相位 → 每周 | 强度区间 | 目标重量(kg) | 组×次 | 热身组` 表。原书未给统一模板，此表结构为**约定**。
**原文并存表述（非冲突）**：Table 22.3 的 strength/power 记"87%–95% 1RMa / 30%–85% of 1RMb"（按非爆发/爆发动作分列），正文框记"30%–95% of the 1RM, depending on the exercise"（总括）。两处并存、均属原文。

## B — 边界 (Boundary)

- **不要用**：无 RM/1RM 数据时硬套百分比；把 Table 22.3 的组数当成"含热身组"（原书脚注 c 明示**不含热身、仅核心目标组**，且不含低强度恢复日）。
- **作者警告的失败模式**：赛内仍用 RM 力竭负荷 → 降功率、增过度训练风险；周五不减重导致周内恢复不足。
- **作者盲点（BOOK_OVERVIEW 步骤 3）**：**共识≠实证**（3.3-5）——许多进阶百分比是惯例；变量耦合（3.3-3），改次数须重估强度与休息；**迁移不保证**（3.3-1）。
- **相邻易混**：`cap.nsca.load-and-repetition`（Ch18 的换算表）、`cap.nsca.in-season-load-management`（赛内整体排布）。
- **resources**：本卡依赖 `resources/periodization-model-table.md`（Table 22.3 + 22.2 档位）。

## 相关能力

- 依赖（先理解）：`load-reps-assignment`
- 依赖（先理解）：`nsca-resistance-program-design`
- 依赖（先理解）：`training-volume`
- 组合（常配合使用）：`annual-plan-construction`

## 配套资源

路径相对于本文件；脚本需先检查运行条件，不因附带而自动执行。

- [resources/periodization-model-table.md](../../resources/periodization-model-table.md)
