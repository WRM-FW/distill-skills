# 年度训练计划（macrocycle）的编排流程

## R — 原文 (Reading)

> "The annual plan example provided in this chapter defines a macrocycle that lasts from May 1 until April 28 ... subdivided into four seasons: off-season (May 1-August 20), preseason (August 21-November 5), in-season (November 6-April 14), and postseason (begins on April 15) ... subdivided into 14 mesocycles, which range in length between two and four weeks."

— Chapter 22 · Example of an Annual Training Plan（`ch22.txt` 第 792–921 行；Figure 22.8）

## I — 自述 (Interpretation)

年度计划（对单赛季项目即 1 个 macrocycle）的编排是一条"**先粗后细、把关键节点钉到时间轴**"的流程：先把年度切成四个赛季区间，再把 macrocycle 细分为若干 mesocycle（样例为 14 个、每个 2–4 周），每个 meso 标注**目标相位**与该块的 microcycle 数，然后在块间/过渡处安排**卸载周**，并在 off-season 与赛季后段安排**测试周**来设定/校准负荷。

原书样例（女性篮球运动员）的五要素：
- 1 个 annual plan = 1 个 macrocycle（5/1 – 次年 4/28）；
- 四赛季区间：off（5/1–8/20，约 16 周）、preseason（8/21–11/5）、in-season（11/6–4/14，约 22 周，含 4 周锦标赛期）、postseason（4/15–5/12，约 1 个月）；
- 14 个 mesocycle，每个 2–4 周；
- 测试节点：预测试周用 5RM/3RM/2RM（核心）、10RM/8RM（辅助）+ 专项测试，据此推算后续负荷；
- 抗阻优先级随期变化：off-season 最高 → preseason 3 天/周重力量与爆发 → in-season 压缩到约 30 min、1–3 次/周。

## A1 — 案例 / 演练 (Application)

**原书案例（sample-program，Figure 22.8 · c22-1）——全书唯一完整年度计划样例**：

- 输入：女性大学篮球运动员（中锋），单赛季；macrocycle = 5/1–次年 4/28。
- 方法：按 macrocycle→mesocycle→microcycle 分层，逐周期给出组×次与负荷（如 Mesocycle 12 悬垂高翻 1×3、前蹲 1×5 @75%–89% 5RM）；赛季以维持/峰值处理，并含锦标赛周方案。
- 输出：跨度整年的逐中周期抗阻处方（14 个 mesocycle、含测试周与卸载周）。
- **原书未说明该运动员的实际训练成效**（样例的用途是"说明如何细分年度计划并设计抗阻成分"）。

## A2 — 未来触发 (Trigger)

**用户会在什么情境下遇到这类问题**
1. 用户要"做一份完整的年度/赛季训练计划"。
2. 用户已有时期框架，要把它排成带日期的中周期时间表。
3. 用户问"什么时候测、什么时候卸载、什么时候加量"。
4. 用户要一份可复制的年度排布模板。

**语言信号（中英双写）**
- 中："排一份年度训练计划""赛季计划时间表""什么时候测试""卸载周放哪""中周期怎么排"。
- 英："build an annual training plan", "macrocycle layout", "season-long plan", "where to place testing/unloading weeks".

**与相邻能力的区分（初稿）**
- 本卡是**年度排布的整合主卡**。三级建立 → `cap.nsca.periodization-three-level-build`；层级时长 → `cap.nsca.periodization-cycle-durations`；季节映射 → `cap.nsca.season-to-period-mapping`；块内变量落值 → `cap.nsca.mesocycle-variable-filling`；赛内调度 → `cap.nsca.in-season-load-management`。

## E — 执行 (Execution)

**输入契约**
- 必需：赛季日历（四赛季区间，YYYY-MM-DD）；年度含几个 macrocycle（单赛季=1）；关键比赛/锦标赛时点。
- 可选：训练状态、可用训练日/周、测试项目清单。
- 缺失处理：无日历 → 先问；无关键比赛时点 → 至少问"哪几场最重要"，不得默认。
- 适用条件：单赛季或已明确赛季结构的竞技项目。

**步骤**
1. 定 macrocycle 边界与数量（单赛季=1）。完成标准：写出起止日期与 macrocycle 数。
2. 按四赛季切区间（引用 `cap.nsca.season-to-period-mapping`）。完成标准：四段区间首尾相接、无缝隙/重叠。
3. 细分 mesocycle：每块 **2–4 周**（样例 14 块），逐块标**目标相位**（hypertrophy/basic strength/strength-power/peaking/maintenance/active rest）与 microcycle 数。完成标准：块长之和 ≈ 年度总周数（保留 1 个过渡/卸载周的容差）。
4. 钉测试节点：在 off-season 起始（预测试）与赛季后段（再测）安排测试周，用 5RM/3RM/2RM（核心）、10RM/8RM（辅助）校准负荷。完成标准：至少 2 个测试节点，各自写明测什么 RM。
5. 排卸载周：策略性放在 off-season/preseason 的下一块之前、以及 in-season 的关键 microcycle 处（见 `cap.nsca.in-season-load-management`）。完成标准：卸载周有明确时点与形式（降量/降强度/两者）。
6. 自检：每块有相位、有 microcycle 数、有负荷来源（RPE/RIR 或 RM）；无空洞周。完成标准：整年无未定义周。

**输出契约**：年度时间表 = `macrocycle → 四赛季区间 → mesocycle 列表（起止/周数/相位/microcycle 数）→ 测试节点 → 卸载周`。原书未给统一输出模板，本表结构为**约定**。
**数值一致性（原文歧义）**：`ch22.txt` 第 798 行记 preseason 为 "August 21-November 5"，第 852 行正文却写 "11 weeks (August 21-October 5)"。二者与 in-season 起始日（11/6）对不上。本卡采用**与 in-season 衔接的 11/5**（采信样例总表口径），判第 852 行为笔误；如需零误差应回读纸质原图。

## B — 边界 (Boundary)

- **不要用**：无赛季或单次课/单周需求；把它当作"照抄样例日历"——原书明示该样例只是**一种**模型，"other athletes or sports may require subtle to radical variations"。
- **作者警告的失败模式**：把 preseason 当建基础期；漏排卸载周导致累积疲劳；把峰值期拉长 >1–2 周（`ce22-01`）。
- **作者盲点（BOOK_OVERVIEW 步骤 3）**：常模/处方表的**人群与时效依赖**（3.1）；表格易被当定律（3.4）；**迁移不保证**（3.3-1）——排进时间表不等于专项表现会提升。
- **相邻易混**：`cap.nsca.season-to-period-mapping`（只做映射）、`cap.nsca.mesocycle-variable-filling`（只填块内变量）。

## 相关能力

- 依赖（先理解）：`season-to-period-mapping`
- 组合（常配合使用）：`detraining-assessment`
- 组合（常配合使用）：`mesocycle-variable-filling`
- 组合（常配合使用）：`peaking-vs-maintenance`
- 组合（常配合使用）：`periodization-cycle-durations`
- 组合（常配合使用）：`periodization-mechanistic-theories`
- 组合（常配合使用）：`speed-short-to-long-periodization`
- 组合（常配合使用）：`undulating-vs-traditional-identification`

## 配套资源

路径相对于本文件；脚本需先检查运行条件，不因附带而自动执行。

- [resources/periodization-model-table.md](../../resources/periodization-model-table.md)
