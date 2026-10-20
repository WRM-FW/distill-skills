# 周期层级结构与时长口径（Table 22.2）

## R — 原文 (Reading)

> "Mesocycle 2-6 weeks ... This medium-sized training cycle is sometimes called a block of training ... The most common duration is 4 weeks. Microcycle ... can range from several days to 2 weeks in duration; the most common duration is 1 week (7 days)."

— Chapter 22 · Periodization Hierarchy（`ch22.txt` 第 324–394 行；Table 22.2）

## I — 自述 (Interpretation)

周期化本质是**把训练年按时间尺度分层**，由粗到细共七级（Table 22.2）。层越往上越概括、越往下越具体：

| 层级 | 时长 | 说明 |
|---|---|---|
| multiyear training plan | 2–4 年 | 互链的年度计划；最常见为 **quadrennial**（奥运周期） |
| annual training plan | 1 年 | 可含 1 个或多个 macrocycle；可再分预备/竞赛/过渡期 |
| macrocycle | 数月至 1 年 | 含预备/竞赛/过渡期；若跨满一年，有作者亦称其为 annual plan |
| **mesocycle** | **2–6 周** | 即"训练块"（block of training），由 microcycle 串联；**最常见 4 周** |
| **microcycle** | **数天至 2 周** | 由多次 workout 组成；**最常见 1 周（7 天）** |
| training day | 1 天 | 可含多次 session；在其 microcycle 语境中设计 |
| training session | 数小时 | 若课内两段之间休息 >30 min，应视为多次 workout |

关键口径：年度计划含几个 macrocycle 取决于项目——**单赛季项目（如美式橄榄球）年度 = 1 个 macrocycle**；**大学田径（室内+室外）= 2 个**；**高中三项目（橄榄球/篮球/田径）= 3 个**。本卡回答"各周期取多长"，是 U5 年度排布的前置。

## A1 — 案例 / 演练 (Application)

**原书案例（tabular-example，Table 22.2）**：原书直接给出七级层级与时长表，属可查表解读的原文例证，非虚构。要把它跑成一次排布：

- 输入：需为一名运动员的 1 年计划按标准层级拆块，已知"中周期与微周期各取多长"？
- 方法：查 Table 22.2——mesocycle 取 2–6 周（默认 4 周）、microcycle 取 1 周（默认 7 天）、年内默认单 macrocycle。
- 输出（预期）：meso = 4 周、micro = 1 周；52 周约合 13 个 4 周中周期（与样例年度计划的 14 个 2–4 周中周期同量级）。**原书未就该换算单独给数值，此处为按表复算。**

## A2 — 未来触发 (Trigger)

**用户会在什么情境下遇到这类问题**
1. 用户问"中周期一般多长？微周期几天？"
2. 用户把 mesocycle 与 microcycle 混用/口径不一。
3. 用户要"把一年切成训练块"，却不知每块多长。
4. 用户问"年度计划要放几个 macrocycle"。

**语言信号（中英双写）**
- 中："中周期几周""微周期几天""macrocycle/mesocycle/microcycle 区别""训练块多长""一年切几块"。
- 英："mesocycle length", "microcycle duration", "how many macrocycles per year", "training block duration", "periodization hierarchy".

**与相邻能力的区分（初稿）**
- 本卡只给**层级与时长的查表口径**。把年度实际排成日期表 → `cap.nsca.annual-plan-construction`；把块内变量落值 → `cap.nsca.mesocycle-variable-filling`。

## E — 执行 (Execution)

**输入契约**
- 必需：训练计划的时间跨度（年/多年，单位：年）；项目赛季数（单/多赛季）。
- 可选：是否有室内外双赛季、是否多项运动员。
- 缺失处理：连"计划跨度"都没有 → 先问；不得默认。

**步骤**
1. 选层级：先定 multiyear/annual，再定 macrocycle 数（单赛季=1，室内外=2，多项=3）。完成标准：写出该年度含几个 macrocycle 及理由。
2. 定 mesocycle：取 **2–6 周，默认 4 周**。完成标准：给出每个 mesocycle 的周数与目标名。
3. 定 microcycle：取 **数天至 2 周，默认 1 周（7 天）**；再落到 training day / session；课内两段休息 >30 min 记两次 workout。完成标准：给出 microcycle 的默认 7 天结构与日/课切分。
4. 自检一致性：块数 × 块长应与 macrocycle 总周数吻合（容差：可留 1 个过渡/卸载周）。完成标准：总周数对得上，否则回到步骤 2 调整块长。

**输出契约**：`层级 | 时长（默认值）| 目标名` 的层级表 + macrocycle 计数。时长数值取自 Table 22.2（见 `resources/periodization-model-table.md`）。原文未规定"必须 4 周"——4 周是**最常见值**而非强制值，本卡以约定形式默认取 4 周。

## B — 边界 (Boundary)

- **不要用**：把它当"固定套表"——2–6 周/1 周是**最常见值**，不是硬约束；特殊项目可偏离。
- **作者警告的失败模式**：层级口径混用（meso/micro 不分）会让后续负荷与恢复安排错位。
- **作者盲点（BOOK_OVERVIEW 步骤 3）**：表格易被当作"定律"，读者只读数值不读条件（3.4）；变量强耦合（3.3-3），改块长必须重估块内强度/量。
- **数值一致性**：原文 Table 22.2 中 microcycle 描述为"Several days to 2 weeks"，而正文一处作"several days to weeks"；本卡采用表值 **数天至 2 周**。
- **相邻易混**：`cap.nsca.annual-plan-construction`（实际排日期）。

## 相关能力

- 依赖（先理解）：`periodization-three-level-build`
- 组合（常配合使用）：`annual-plan-construction`

## 配套资源

路径相对于本文件；脚本需先检查运行条件，不因附带而自动执行。

- [resources/periodization-model-table.md](../../resources/periodization-model-table.md)
