# 峰值 vs 维持的决策框架（peaking / maintenance）

## R — 原文 (Reading)

> "Peaking programs attempt to place the athlete in peak condition for about one or two weeks. Trying to extend this to longer durations ultimately results in reduced performance capacity ... For team sports, this period spans an entire season and may last for many months, requiring the use of a maintenance program."

— Chapter 22 · Competitive Period（`ch22.txt` 第 599–641 行；巅峰窗口另见第 94–96 行）

## I — 自述 (Interpretation)

竞赛期有两种打法，**按赛季长度分派**：

- **peaking（峰值）**：让运动员在约 **1–2 周**内达巅峰。强度区间很宽（**50%–≥93% 1RM**）、量极低（**1–3 组 × 1–3 次**）；随 taper **从高强度渐移向低强度**以削减疲劳。**延长峰值窗口会因体能下降或过度训练反而降低表现**。
- **maintenance（维持）**：团队项目赛季可跨数月，必须在 **microcycle 层**调制强度/量，在维持力量与爆发的同时管理密集赛程的疲劳——强度 **85%–93% 1RM**、中低量（**~2–5 组 × 3–6 次**），并依训练/旅行/赛程调制。

底层判据来自体能—疲劳与巅峰窗口规则：**巅峰表现只能在约 7–14 天内被优化，且可维持时间与平均训练强度成反比**（见 `cap.nsca.periodization-mechanistic-theories`）。故"短窗用峰值、长赛季用维持"。

## A1 — 案例 / 演练 (Application)

原书给出竞赛期的两条处方规则与锦标赛周样例（c22-2），但**未提供"两类运动员二选一"的带输入演练**。以下为**明确标记的合成演练**：

- 输入：(A) 举重运动员，关键赛在 5 周后（短窗）；(B) 足球队，赛季约 6 个月（长窗）。
- 执行：A → 采用 **peaking**：约 1–2 周、强度 50%–≥93% 1RM、1–3 组 × 1–3 次、随 taper 由高强度转低强度以降疲劳；B → 采用 **maintenance**：强度 85%–93% 1RM、约 2–5 组 × 3–6 次、在 microcycle 级依赛程调制并持续监测。
- 输出：两者均得确定的"峰值/维持"处方与调控要点。**原书未说明实际结果。**

## A2 — 未来触发 (Trigger)

**用户会在什么情境下遇到这类问题**
1. 用户问"赛前怎么 taper、峰值能保持多久？"
2. 用户是团队项目教练，赛季数月，想给队员一直"做峰值"。
3. 用户问"竞赛期还要不要大重量、练多少？"
4. 用户想知道"维持力量需要多少强度和量？"

**语言信号（中英双写）**
- 中："赛前减量多久""峰值能保持几周""团队项目赛季怎么练""竞赛期维持力量""taper 怎么排"。
- 英："peaking vs maintenance", "how long can you peak", "in-season maintenance program", "taper before competition", "competitive period training".

**与相邻能力的区分（初稿）**
- 本卡只做"峰值/维持的**打法选择与档位**"。赛季内具体排布与卸载周 → `cap.nsca.in-season-load-management`；块内重量换算 → `cap.nsca.mesocycle-variable-filling`；减量模型细节（linear/step/progressive，Ch21）属有氧耐力族，不在本卡。

## E — 执行 (Execution)

**输入契约**
- 必需：赛季长度（周/月）；关键比赛时点（相对当下的距离）。
- 可选：监测数据（表现、恢复）、训练状态。
- 缺失处理：无关键比赛日 → 先问；不得默认"没有峰值需求"。
- 适用条件：处于 competitive period。

**步骤**
1. 定关键比赛窗口：记录比赛日期与距今天数。完成标准：写出"窗口 ≤2 周 / >2 周（长赛季）"。
2. 分支：
   - 短窗（关键赛临近，峰值可行）→ **peaking**：1–2 周、50%–≥93% 1RM、1–3 组 × 1–3 次；随 taper 由高强度移向低强度。**不要把峰值期拉到 >1–2 周**。
   - 长赛季（团队项目数月）→ **maintenance**：85%–93% 1RM、~2–5 组 × 3–6 次；在 microcycle 级依训练/旅行/赛程调制。
3. 平衡核查：避免减量过度——若量/强度降太多，疲劳降但体能同降、备战度下降（`ce22-03`）。完成标准：写出"保持多少量/强度以维持竞技状态"。
4. 监测：依赖持续监测表现与恢复来微调。完成标准：列出监测指标与调整触发。

**判停点**：若用户既是长赛季又想"峰值全程" → 明确指出这与体能—疲劳范式冲突，改走 maintenance。
**输出契约**：`赛季长度 | 选定打法 | 强度区间 | 组×次 | taper/调制要点 | 监测点`。数值取自原书竞赛期处方（见 `resources/periodization-model-table.md`）。

## B — 边界 (Boundary)

- **不要用**：把 peaking 用于数月长赛季；把 maintenance 用到"个人短窗关键赛"（该 peak 却全程维持）。
- **作者警告的失败模式**：延长峰值期 → 表现下降（`ce22-01`）；减量过度 → 体能与备战度同降（`ce22-03`）。
- **作者盲点（BOOK_OVERVIEW 步骤 3）**：巅峰窗口 7–14 天为**经验值**（p22-08 明示无定量公式）；"维持时长与平均强度成反比"原文未给量化关系。**共识≠实证**（3.3-5）。
- **相邻易混**：`cap.nsca.in-season-load-management`（赛内每周怎么排）、Ch21 的减量模型（有氧耐力语境）。

## 相关能力

- 组合（常配合使用）：`aerobic-tapering-models`
- 组合（常配合使用）：`annual-plan-construction`
- 组合（常配合使用）：`competition-nutrition-timeline`
- 组合（常配合使用）：`in-season-load-management`

## 配套资源

路径相对于本文件；脚本需先检查运行条件，不因附带而自动执行。

- [resources/periodization-model-table.md](../../resources/periodization-model-table.md)
