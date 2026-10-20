# 运动季节 ↔ 周期化时期映射与传统四期演变

## R — 原文 (Reading)

> "The off-season should be considered the preparatory period ... The first transition period is often undertaken at this time with a focus on the strength/power phase ... The competitive, or in-season, period contains all the contests scheduled for the given year ... the postseason or second transition period provides the athlete with a relative or active rest."

— Chapter 22 · Periodization Periods / Applying Sport Seasons to the Periodization Periods（`ch22.txt` 第 395–476、671–735 行）

## I — 自述 (Interpretation)

把"抽象的四个时期"锚到运动员真实赛季日历上，是一张**双向映射表**（Figure 22.7）：

| 赛季 | 对应时期 | 焦点 |
|---|---|---|
| off-season | **preparatory**（预备期，含 general→specific 两相） | 建基础：高量低强、手段多样 |
| preseason | **first transition**（第一过渡期） | strength/power：把力量转向爆发 |
| in-season | **competitive**（竞赛期） | 全部比赛；维持/峰值 |
| postseason | **second transition**（第二过渡期/active rest） | 主动休息，恢复身心 |

两条关键律：
1. **演变律**（传统四期）：训练焦点在数周至数月内从"高量、低强、一般非专项"系统转向"低量、高强、专项"，以降低过度训练风险并优化表现。
2. **纠偏提醒**：**preseason 不是建基础的时候**——基础主要放在 off-season；preseason 是"收割" off-season 成果、把表现抬升到竞赛期水平。

另注：即使图上画成直线，volume/intensity 实为**非线性**（在 micro/meso 层有波动）。

## A1 — 案例 / 演练 (Application)

**原书案例（in-book scenario，Figure 22.7 + 正文）**：原书以"仅有一个赛季的项目（如美式橄榄球）"说明年度=1 macrocycle，并给出四赛季↔四时期的对应。

- 输入：美式橄榄球运动员，仅秋季一个赛季。
- 方法：按映射表——off-season→preparatory（含 general/specific 两相）；preseason→first transition（strength/power）；in-season→competitive（全部比赛）；postseason→second transition（active rest）。
- 输出：季节↔时期对应表 + 各期焦点，并标注"preseason 应收割 off-season 成果"。**原书未给该运动员的成效数据（原书未说明）。**

## A2 — 未来触发 (Trigger)

**用户会在什么情境下遇到这类问题**
1. 用户问"off-season / preseason 到底该练什么？"
2. 用户把"建基础"安排在 preseason（常见误用）。
3. 用户有多个赛季（室内+室外），不知如何映射时期。
4. 用户问"过渡期/主动休息对应哪个赛季？"

**语言信号（中英双写）**
- 中："季前赛练什么""off-season 和 preseason 怎么分""赛季对应哪个周期""过渡期是什么""基础期放哪"。
- 英："map sport seasons to periods", "off-season = preparatory?", "preseason focus", "first vs second transition", "competitive period".

**与相邻能力的区分（初稿）**
- 本卡做"季节↔时期映射与各期焦点"。把映射结果排成日期表 → `cap.nsca.annual-plan-construction`；量/强度如何随期演变落值 → `cap.nsca.mesocycle-variable-filling`。

## E — 执行 (Execution)

**输入契约**
- 必需：项目赛季结构（各赛季的起止日期或先后顺序）；是否有多个赛季。
- 可选：主项关键比赛时点。
- 缺失处理：无赛季日历 → 先问；不得凭常识编季节。

**步骤**
1. 列出该项目的四个赛季日历区间（off/preseason/in-season/postseason）。完成标准：每个赛季有区间。
2. 按映射表逐一双向绑定：off-season→preparatory、preseason→first transition、in-season→competitive、postseason→second transition。完成标准：得到对应表，无遗漏、无错配。
3. 标各期焦点：preparatory 内再分 general（高量低强、手段多样）与 specific（加大专项比重）；first transition 定 strength/power；competitive 定 peaking 或 maintenance；second transition 定 active rest。完成标准：每期有焦点词。
4. 复核"高量低强→低量高强"的时序方向，并检查是否误把基础放到 preseason。完成标准：方向正确 + 纠正 possible 误置。

**输出契约**：`赛季 | 时期 | 相位 | 焦点 | 量-强度取向` 表。原文未给统一表格格式，此处为**约定**。数值取向参见 `cap.nsca.mesocycle-variable-filling` 与资源 `resources/periodization-model-table.md`。

## B — 边界 (Boundary)

- **不要用**：把它当"日历必须四段均匀"——各季时长随项目差异极大（原书明示"varies greatly"）。
- **作者警告的失败模式**：把 preseason 当建基础期；把 postseason 拖过长（>4 周）会加速 detraining（见 `ce22-02`）。
- **作者盲点（BOOK_OVERVIEW 步骤 3）**：竞技人群偏向（3.2）——映射默认"有多个赛季/有 transition"的竞技语境，普通健身人群不适用。
- **相邻易混**：`cap.nsca.peaking-vs-maintenance`（竞赛期内怎么打）、`cap.nsca.in-season-load-management`（赛内排布）。

## 相关能力

- 组合（常配合使用）：`annual-plan-construction`
- 组合（常配合使用）：`in-season-load-management`
