# 密集赛程 / 长赛季的赛内负荷编排与卸载周

## R — 原文 (Reading)

> "a long competitive season (12-16+ weeks) presents unique programming challenges—in these situations, three- or four-week mesocycle blocks that unload the athlete in the last microcycle ... Repetition maximum loads are not used, as training to failure has been shown to reduce power output and increase the risk of overtraining ... percentage ranges based off of RM loads are used to deal with the accumulated fatigue."

— Chapter 22 · In-Season（`ch22.txt` 第 712–728 行）；样例注记第 1720–1732 行；Tournament Options 第 1690–1718 行

## I — 自述 (Interpretation)

赛内（in-season）的核心矛盾：**比赛太多、没时间也没恢复余量**，但又要"不丢力量与爆发"。原书给的解法是一套**块结构 + 微周期调制 + 卸载**：

1. **长赛季**（12–16+ 周）用 **3 或 4 周的中周期块**，把块内**最后一个 microcycle 设为卸载周**，以便在关键比赛前降疲劳、实现表现超量补偿。
2. **microcycle 级调制**：策略性改变训练日位置，并在每个微周期内升降强度与量，以在拥挤赛程中调控备战状态。
3. **卸载周**：主要放在 off-season/preseason 的下一块之前；赛内则放在**关键 microcycle** 处。（减量=降强度、量或两者。）
4. **不用力竭 RM**：赛内以"基于 RM 的百分比区间"替代真实 RM 负荷，应对累积疲劳。
5. **周内口径**：非关键课相对主课 **-10% 负荷**；目标组外另做 **3–5 组热身**；比赛与抗阻/plyo 之间留 **2–3 天**恢复间隔。

## A1 — 案例 / 演练 (Application)

**原书案例（tabular-example，c22-2 · Tournament Options A/B/C）**：原书给出三套锦标赛周样例——

- Option A（两周内 2 场比赛）：Practice(or rest) / Practice / Practice / Practice（含抗阻）/ Game / Practice / Game。
- Option B（两周内 2 场）：在 Practice/Game 之间插入 Plyometric 与 Resistance training。
- Option C（连续 3 场背靠背）：给出两周的周内排布，抗阻与 plyo 穿插在 Practice 之间。
- 原书注：**每个 mesocycle 视为一个训练块，含 2 或 3 个 microcycle；卸载 mesocycle 被策略性放在 off-season/preseason 的下一块之前、以及 in-season 的关键 microcycle 处。**

在其上做一次**合成演练**（对应 Option C）：某球队一周连续 3 场背靠背比赛 → 以 3–4 周中周期块组织、末周微周期设为卸载；比赛间留 2–3 天恢复后插入 plyo/抗阻课；同一微周期内升降强度与量；非关键课相对主课 -10%；赛内以 %RM 区间（如 75%–79% 6RM）替代力竭 RM。**原书未说明这些样例的训练成效。**

## A2 — 未来触发 (Trigger)

**用户会在什么情境下遇到这类问题**
1. 用户球队一周多赛，问"赛内还怎么安排抗阻/plyo？"
2. 用户问"赛季里什么时候卸载？卸载周怎么放？"
3. 用户要排"锦标赛周/背靠背比赛周"的训练。
4. 用户问"赛内要不要测 RM、练到力竭？"

**语言信号（中英双写）**
- 中："一周三赛怎么练""赛季内怎么排抗阻""锦标赛周计划""卸载周放哪""赛内力竭吗"。
- 英："in-season load management", "congested schedule", "tournament week plan", "unloading microcycle", "avoid training to failure in-season".

**与相邻能力的区分（初稿）**
- 本卡做**赛内排布与卸载**。赛季内打法选择（峰值/维持）→ `cap.nsca.peaking-vs-maintenance`；块内重量换算 → `cap.nsca.mesocycle-variable-filling`；年度时间表 → `cap.nsca.annual-plan-construction`。

## E — 执行 (Execution)

**输入契约**
- 必需：比赛日程（每周场次、是否背靠背、锦标赛时点）；赛季长度（周）。
- 可选：监测数据（表现、疲劳/恢复）、当前力量/爆发维持目标。
- 缺失处理：无比赛日历 → 先问；不得默认"无密集赛程"。
- 适用条件：处于 in-season。

**步骤**
1. 定量赛程密度：标出每周场次与关键比赛。完成标准：得到"每周场次 + 关键赛清单"。
2. 划块：长赛季（≥12–16 周）用 **3 或 4 周中周期块**，每块含 2–3 个 microcycle。完成标准：块结构与微周期数明确。
3. 置卸载：把块内**末个 microcycle 设为卸载**；卸载点对齐关键 microcycle 与块间过渡。完成标准：每块末周标为卸载，且关键赛前有卸载。
4. 微周期调制：在每个 microcycle 内升降强度与量、策略性移动训练日位置。完成标准：每个 microcycle 有明确的强度/量升降与训练日安排。
5. 负荷口径：赛内**不测真实 RM、不力竭**，改用 %RM 区间（如 75%–79% 6RM）；非关键课相对主课 -10%；目标组外另加 3–5 组热身；比赛与抗阻/plyo 间留 2–3 天。完成标准：无 RM-力竭处方，且周内口径齐全。
6. 参照锦标赛周样例（Option A/B/C，按场次数选）落成周计划。完成标准：周计划与场次数匹配。

**判停点**：若赛程过密（如连续 3 场）至无法安排抗阻 → 优先保 power/core 动作、砍辅助动作（原书对锦标赛周的建议）。
**输出契约**：`周 | 比赛场次 | 抗阻/plyo 位置 | 强度/量取向（升降）| 是否卸载` 的赛内周计划 + 块结构表。数值口径取自原书样例注记（见 `resources/periodization-model-table.md`）。

## B — 边界 (Boundary)

- **不要用**：把 off-season 的负荷/结构直接搬进赛内；赛内仍练到力竭。
- **作者警告的失败模式**：跳过卸载周 → 累积疲劳在关键赛前爆发；用力竭 RM → 降功率、增过度训练风险（`ch22` 样例注记）。
- **作者盲点（BOOK_OVERVIEW 步骤 3）**：样例面向**竞技团队项目**（3.2 人群偏向）；"每个 mesocycle 含 2–3 个 microcycle"由样例注记给出、非普适定律；**变量耦合**（3.3-3），改比赛日位置会牵动恢复与负荷。
- **相邻易混**：`cap.nsca.peaking-vs-maintenance`（打法选择）、`cap.nsca.mesocycle-variable-filling`（具体重量）。
- **resources**：本卡的口径与档位见 `resources/periodization-model-table.md`。

## 相关能力

- 组合（常配合使用）：`agility-multifactorial-plan`
- 组合（常配合使用）：`athlete-monitoring-plan-design`
- 组合（常配合使用）：`overtraining-prevention-integration`
- 组合（常配合使用）：`peaking-vs-maintenance`
- 组合（常配合使用）：`periodization-model-choice`
- 组合（常配合使用）：`plyometric-frequency-recovery`
- 组合（常配合使用）：`season-to-period-mapping`
- 组合（常配合使用）：`training-frequency`

## 配套资源

路径相对于本文件；脚本需先检查运行条件，不因附带而自动执行。

- [resources/periodization-model-table.md](../../resources/periodization-model-table.md)
