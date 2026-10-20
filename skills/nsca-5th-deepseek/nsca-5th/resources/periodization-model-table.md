# 周期性抗阻模型与周期层级时长（对照表）

- 来源：src-nsca-essentials-5e · Chapter 22 "Periodization"（`ch22.txt`）
- 用途：为 `cap.nsca.mesocycle-variable-filling`（块内变量落值）、`cap.nsca.periodization-cycle-durations`（层级时长）、`cap.nsca.peaking-vs-maintenance` / `cap.nsca.in-season-load-management`（竞赛期档位）与伞形 `cap.nsca.periodization` 提供可复算的档位对照。
- 说明：下列数值逐字取自原文 Table 22.2 与 Table 22.3 及其脚注，未作改写。

---

## Table 22.3 — A Periodized Model for Resistance Training

| Period | Preparatory | Preparatory | First transition | Competition | Second transition |
|---|---|---|---|---|---|
| Phase | General preparatory | Specific preparatory | Precompetitive | Main competitive | Postcompetitive |
| Season | Off-season | — | Preseason | In-season | Postseason |
| Emphasis | Hypertrophy / strength endurance | Basic strength | Strength/power | Peaking **or** Maintenance | Active rest |
| Intensity | Low to moderate | High | Low to very high | Very high to very low | Moderate to high | Recreational activities (may not involve resistance training) |
| %1RM | 50%-75% 1RM | 80%-95% 1RM | 87%-95% 1RMa / 30%-85% of 1RMb | Peaking: 50% to ≥93% 1RM / Maintenance: 85%-93% 1RM | — |
| Volume | High | Moderate to high | Low | Very low (peaking) / Low to moderate (maintenance) | Low to moderate |
| Sets | 3-6 setsc | 2-6 setsc | 2-5 setsc | 1-3 setsc (peaking) / ~2-5 setsc (maintenance) | ~2-5 setsc |
| Reps | 8-20 reps | 2-6 reps | 2-5 reps | 1-3 reps (peaking) / 3-6 reps (maintenance) | 3-6 reps |

脚注（逐字）：
- a These percentages of 1RM apply to nonpower core exercises.
- b These percentages of 1RM apply to power exercises. The actual percentage used to elicit power development depends on the exercise that is used.
- c These recommendations do not include warm-up sets and represent only target sets for core exercises; they also do not include lower-intensity recovery days that are often part of a periodized training plan.

各相正文框口径（逐字，与上表并用）：
- Hypertrophy / strength–endurance：low to moderate intensity (50%-75% of the 1RM), high volumes (3 to 6 sets of 8-20 repetitions)
- Basic strength：higher intensity (80%-95% of the 1RM), moderate to high volumes (2 to 6 sets of 2 to 6 repetitions)
- Strength/power：low to very high loads (30%-95% of the 1RM, depending on the exercise), low volumes (2 to 5 sets for 2 to 5 repetitions)
- Peaking：very high to low intensities (50% to ≥93% of the 1RM), very low volume (1 to 3 sets of 1 to 3 repetitions) for one to two weeks
- Maintenance：moderate to high intensities (85%-93% of the 1RM), moderate volumes (about 2 to 5 sets of 3 to 6 repetitions)

---

## Table 22.2 — Periodization Cycles

| Period | Duration | Description |
|---|---|---|
| Multiyear training plans | 2-4 years | This contains interlinked annual training plans; the most common multiyear plan is the quadrennial plan. |
| Annual training plan | 1 year | The overall annual training plan can contain a single or multiple macrocycles. It can be subdivided into preparatory, competitive, and transitional periods of training. |
| Macrocycle | Several months to a year | It contains preparatory, competitive, and transitional periods of training. If it encompasses one year, some authors refer to this as an annual plan. |
| Mesocycle | 2-6 weeks | This medium-sized training cycle is sometimes called a block of training. It consists of microcycles that are linked together. The most common duration is 4 weeks. |
| Microcycle | Several days to 2 weeks | This small-sized training cycle is comprised of multiple workouts. It can range from several days to 2 weeks in duration; the most common duration is 1 week (7 days). |
| Training day | 1 day | One training day can contain multiple sessions. It is designed in the context of the microcycle in which it is contained. |
| Training session | Several hours | It generally consists of several hours of training. If the session has >30 min of rest between bouts of training, it should be considered as having multiple workouts. |

---

## 样例口径与换算提示（逐字 / 注明）

- "Friday session should use a load 10% less than Monday's."（样例 Mesocycle 2/3/4 注记；preseason 一处另作 "a load 15% less than Monday's"）
- "3 to 5 warm-up sets should be performed to provide an appropriate specific warm-up for the targeted loadings."
- "Repetition maximum loads are not used, as training to failure has been shown to reduce power output and increase the risk of overtraining. Therefore, percentage ranges based off of RM loads are used to deal with the accumulated fatigue associated with in-season training and competitions."
- 巅峰窗口：peak performance can be optimized only for short periods of time (7-14 days)，且可维持时间与平均训练强度成反比。
- 第二过渡期：generally lasts for one to four weeks；should not last longer than four weeks（除非伤后需额外恢复）。

## 与簇 A 的交界（不复制其数值）

- Table 18.8（%RM ↔ 可完成重复数）、Table 18.9（由多次 RM 估 1RM）、Table 18.15（按重复目标定休息时长）位于 **Ch18，属簇 A**。本资源只提示"到这些表做换算"，具体数值请调用 `cap.nsca.load-and-repetition`，**不在本文件内复制**。

## 口径说明（原文歧义，如实标注）

- 样例计划把强度写作 "80%-84% 10RM / 85%-89% 10RM / 90%-94% 10RM" 一类三周阶梯。本资源按阶段 1.5 验证口径解释为"**目标 RM 负荷的百分比**"（如 5RM=120 kg → 周1 = 0.80×120 = 96 kg）；该记法亦可读作 %1RM，属原文表记的歧义点，落到具体重量时须声明所用解读。
- `ch22.txt` 第 798 行 preseason 记 "August 21-November 5"，第 852 行记 "11 weeks (August 21-October 5)"；与 in-season 起始（11/6）衔接，采用 **11/5**，判第 852 行为笔误。
