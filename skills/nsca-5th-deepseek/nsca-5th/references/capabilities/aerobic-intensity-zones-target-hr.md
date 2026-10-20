# 有氧强度分区与目标心率计算（两套公式 + 五区/三区标尺）

## R — 原文 (Reading)

> "Age-predicted maximum heart rate (APMHR) = 220 - age. Heart rate reserve (HRR) = APMHR - resting heart rate (RHR). Target heart rate (THR) = (HRR × exercise intensity) + RHR." ... "Lowest number of the athlete's THRR = (130 × 0.60) + 60 = 78 + 60 = 138 beats/min; Highest number of the athlete's THRR = (130 × 0.70) + 60 = 91 + 60 = 151 beats/min."

— Chapter 21 · "Step 3: Training Intensity" → "Target Heart Rate Calculations" sidebar（`ch21.txt` 第 523–537 行）

## I — 自述 (Interpretation)

有氧处方里"相对强度（%）"必须落成"绝对心率（次/分）"才能执行，本书用两套互不通用的公式，先选公式再算区间：

**公式一 · 心率储备法（Karvonen / %HRR）**：APMHR = 220 − age；HRR = APMHR − RHR；THR = (HRR × 强度) + RHR。它把运动员的静息心率 RHR 纳入基线，是"个人化程度更高"的一种。
**公式二 · 最大心率法（%MHR）**：APMHR = 220 − age；THR = APMHR × 强度。它不用 RHR，读同一条处方百分比时心率会与 %HRR 明显不同。

两套都要用"处方强度的最小值和最大值各算一次"，得到目标心率**区间**（THRR），不是单点。5 区标尺（Table 21.1，%VO2max / %HRmax / 乳酸 mmol/L / 典型累积时长四列）与 %VO2max–%HRR–%MHR 对照表（Table 21.2）是把"想练哪个区/哪个代谢强度"翻译成百分比的中间桥；三区模型则按血乳酸 <2 / 2–4 / >4 mmol/L 划低-阈-高。整条链是：定目标区 → 取该区的强度百分比 → 选公式算成心率区间（或反之）。

## A1 — 案例 / 演练 (Application)

**原书例题 1（`c21-1`，类型：worked-example，Ch21 Target Heart Rate Calculations sidebar）**：30 岁运动员、RHR 60 次/分，处方 60%–70% 功能容量。APMHR = 220 − 30 = 190；HRR = 190 − 60 = 130；下限 (130 × 0.60) + 60 = 138；上限 (130 × 0.70) + 60 = 151 → **目标心率区间 138–151 次/分**。方法列为 Karvonen/%HRR 法，出处 Ch21。

**原书例题 2（`c21-2`，类型：worked-example，同 sidebar）**：20 岁运动员、处方 70%–85% 最大心率。APMHR = 220 − 20 = 200；下限 200 × 0.70 = 140；上限 200 × 0.85 = 170 → **目标心率区间 140–170 次/分**。方法列为 %MHR 法，出处 Ch21。

> 交叉核对（`_verified/E-aerobic.md` V2 演练）：40 岁、RHR 55、70–80% 功能容量 → Karvonen 得 143–155 次/分；同样处方若换成 %MHR 口径则约 146–158 次/分。两法**不相同但相邻**（差异可达 10 次/分以上），故必须写明所用方法。

## A2 — 未来触发 (Trigger)

**用户会在什么情境下遇到这类问题**
1. 拿到一条"60%–70% 强度"的处方，要换成运动员能看着表执行的心率区间。
2. 纠结该用 Karvonen（%HRR）还是 %MHR，或发现两法算出的心率对不上。
3. 想知道某个心率/乳酸/%VO2max 落在五区或三区的哪一档、典型能持续多久。
4. 只有年龄（有时加静息心率），没有实验室实测值，需要估计并知道误差多大。

**语言信号（中英双写关键 trigger）**
- 中文：「目标心率怎么算」「Karvonen 公式」「心率储备 / HRR」「%MHR 和 %HRR 有什么区别」「60% 强度是多少心率」「五区/三区怎么划」「最大心率怎么估」
- English: "target heart rate", "Karvonen formula", "heart rate reserve / HRR", "percent of maximal heart rate", "220 minus age", "five-zone intensity scale", "which zone is this", "aerobic training zones"

**与相邻能力的区分（初稿，阶段 3 回填）**
- 与 `aerobic-program-design-five-variables`：本卡只解决"强度这一变量"的换算与分区；频率/时长/模式/进阶归那张卡。
- 与 `energy-system-to-interval-ratio`：本卡给"心率/百分比强度档"，后者给"由供能系统查工作-休息比"（T37），两者可接力但不重叠。
- 与 `nsca-speed-agility-design`、`nsca-resistance-program-design`：那两张的心率无关；本卡仅限有氧/代谢训练强度。
- 与"过度训练与恢复"：本卡不判定疲劳状态，只做强度换算。

## E — 执行 (Execution)

**输入契约**
- 必需：① 年龄（岁）；② 所选公式；③ 处方相对强度区间（%）与它是"功能容量/%HRR"还是"%MHR"口径；④ 若用 Karvonen，需 RHR（次/分，静息、至少 5 min 安静后测）。
- 可选：实验室/场地实测 HRmax、LT、VO2max（有则优先，替代 APMHR）。
- 缺失处理：既无实测 HRmax 又无年龄 → 先询问，不得静默猜值。用 %HRR 却缺 RHR → 要么补测 RHR，要么改走 %MHR 法并注明误差更大。

**执行步骤（两套公式 + 分区）**
1. **选公式**（完成标准：明确写出方法名，非"二选一模糊"）。判据：
   - 缺 RHR / 只想快速估 → %MHR 法；
   - 有稳定 RHR、想更个体化 → Karvonen/%HRR 法；
   - 有条件实测 HRmax → 用实测值替换 APMHR 代入任一法。
2. **算最大心率**：APMHR = 220 − age（次/分）。
3. **算心率区间**（两法各有公式，**计算顺序：先算 APMHR，再算 HRR[仅 Karvonen]，最后对强度最小/最大值各算一次**）：
   - Karvonen：`HRR = APMHR − RHR`；`THR = (HRR × 强度) + RHR`；
   - %MHR：`THR = APMHR × 强度`。
4. **舍入与容差**（约定）：算术结果按四舍五入取整到 1 次/分（原例 138/151、140/170 均为整数）。因 APMHR 的个体标准差为 10–12 次/分，**区间仅作处方靶区，不当作硬边界**；建议以 ±5–10 次/分的带宽监控。
5. **落分区**（可选）：用 Table 21.1 把心率/%VO2max 对应到 Zone 1–5（含该区乳酸 mmol/L 与典型累积时长）；或用 Table 21.2 在 %VO2max ↔ %HRR ↔ %MHR 间换算；三区模型则用血乳酸 <2 / 2–4 / >4 mmol/L 判低-阈-高。
6. **写结论**（完成标准：给出"方法名 + 公式代入 + 目标心率区间 + 对应区/百分比"四件套）。

**判停点/分支**
- 处方百分比落在 50%–90% 功能容量之外 → 心率与摄氧量关系变弱，**标注"心率法在本区间可靠性下降"**，优先改用 %VO2max/乳酸直接监控（见 B 段）。
- 环境为热/湿/高原 → 心率会被抬高，本卡给出的数值需上调预留，且不得把"心率偏高"直接判为强度达标。
- 运动员体能已改善（VO2max/LT 上升）→ 同一绝对心率变成更低的相对强度，须按新测试结果上调强度以维持刺激（原书明示）。

**输出契约**
- `{方法（Karvonen/%MHR/实测 HRmax）, APMHR, RHR?, HRR?, 强度区间, 目标心率区间（整数，次/分）, 对应五区/三区, 适用区间告警}`。
- 资源 `resources/aerobic-intensity-zones.md` 内含 Table 21.1 五区标尺、Table 21.2 对照表与两套公式算例，可随包直接调用。

## B — 边界 (Boundary)

- **不要用**：当问题不是"把强度换成心率"，而是"心率法整体可靠性"之外的机制解释时（走 glossary）；当需要的是频率/时长/进阶时（见 `aerobic-program-design-five-variables`、`aerobic-progression-10pct-single-variable`）。
- **作者警告的失败模式**：①**APMHR 是个体误差带 ±10–12 次/分（SD）**，任何 220−age 估计都带此偏差，实验室实测 HRmax 更准；②估计式**不含 LT 信息**——"without some knowledge of an athlete's LT ... a highly effective aerobic endurance training program cannot be developed"（第 515–518 行）；③心率与摄氧量仅在 **50%–90% 功能容量（HRR）区间**关系良好，越界即失真；④%MHR 与 %HRR **不可混用**，同一处方百分比下可差 10 次/分以上（`_verified/E-aerobic.md` V2）。
- **盲点（BOOK_OVERVIEW 步骤 3）**：Table 21.1 是**挪威奥委会**基于越野滑雪/赛艇/冬季两项的**通用指南（Seiler 2010）**，非个体化，跨项目迁移需校验；共识 ≠ 实证，分区边界是惯例而非生理断点；环境（热/湿/海拔）使心率偏移且未给量化修正；变量耦合（改强度区间会牵动时长与恢复）。
- **相邻易混**：`energy-system-to-interval-ratio`（按供能系统定工作-休息比）、`aerobic-program-design-five-variables`（五变量总入口）。

## 相关能力

- 组合（常配合使用）：`aerobic-capacity-test-protocols`
- 组合（常配合使用）：`aerobic-program-design-five-variables`
- 组合（常配合使用）：`mas-vo2max-estimation`

## 配套资源

路径相对于本文件；脚本需先检查运行条件，不因附带而自动执行。

- [resources/aerobic-intensity-zones.md](../../resources/aerobic-intensity-zones.md)
