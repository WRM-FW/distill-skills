# 变阻负荷计算（链 / 弹力带：顶底平均后从目标 RM 扣除）

## R — 原文 (Reading)

> "... the absolute chain resistance at the top and at the bottom portion of the movement are summed and then averaged. For example, if athletes wanted to train at a 5-repetition maximum (5RM) load in the bench press ... if their 5RM is 120 kilograms (265 lb), they would subtract the average chain resistance from this load. If at the bottom position the load is 0 kilograms and at the top the chain load is 11.1 kilograms (24.5 lb), the average is 5.55 kilograms (12.2 lb). Thus, the athlete would add 114 to 115 kilograms ..."

— Chapter 17 · Determining the Load to Use With Chains（`ch17.txt` 第 469–478 行；弹力带同法见 617–633 行）

## I — 自述 (Interpretation)

链与弹力带都是**变阻力**：阻力随动作幅度变化（链在底部触地→阻力最小、顶部离地→阻力最大；带在底部松弛→0、顶部拉伸最大）。因此**不能用"标称重量"直接当额外负荷**——必须知道"整段行程平均多给了多少阻力"，再把这个平均值从目标负重里扣掉。

两条统一算法（链、带**同一套路**）：

1. 先测**无链/无带**下的目标 RM 负荷（如 5RM = X kg）。
2. 分别取**底部阻力**与**顶部阻力**（绝对负荷，单位 kg 或 lb）。
3. **平均阻力 = (底部 + 顶部) / 2**。
4. **杠上加载量 = 目标 RM 负荷 − 平均阻力**。

直觉：链/带在**平均**层面只是"替你多举了 avg 这么多"，所以杠铃要**减去**这部分，才能在整段行程维持目标 RM 的刺激。

**弹力带的两个补充口径**：①张力遵循 **Hooke 定律 Tension = k（刚度）× d（形变）**，但实际带同时存在**曲线与线性形变区**；②**带材差异**——两条"看似等同"的带可有 **3.2%–5.2%** 的差异，导致**平均张力相差 8%–19%**，故不能假定同规格带拉力一致。

## A1 — 案例 / 演练 (Application)

**书中案例一（worked-example，`c17-1`；出处 `ch17.txt` 第 472–478 行）——链（5RM 120 kg）**：
- 无链卧推 5RM = **120 kg**；底部链阻 = 0 kg、顶部链阻 = 11.1 kg。
- 平均链阻 = (0 + 11.1)/2 = **5.55 kg**。
- 杠上加载量 = 120 − 5.55 = **114–115 kg**（原文 "add 114 to 115 kilograms"）。
- 独立核算：120 − 5.55 = 114.45 → 取 114–115 kg，与预期一致。

**书中案例二（worked-example，`ch17.txt` 第 624–633 行）——弹力带（5RM 150 kg）**：
- 无带卧推 5RM = **150 kg**；底部带阻 = 0 kg、顶部带阻 = 26.6 kg。
- 平均带阻 = (0 + 26.6)/2 = **13.3 kg**。
- 杠上加载量 = 150 − 13.3 = **136–137 kg**（原文 "136 to 137 kilograms (300-302 lb)"）。

**书中表格案例（tabular-example，`c17-4`；出处 `ch17.txt` Table 17.2，第 586–615 行）**：给出各带宽/颜色在 110–150 cm 的**长度—张力对照值**（如 67 mm 黑带：110 cm→15.4 kg、150 cm→57.2 kg）。**查表路径可直接用**；预测方程路径见下"缺口"。原文未说明训练成效。

**合成演练（标记：合成；非书中案例）**：
- 链：目标卧推 5RM=140 kg、底部 0 kg、顶部 15 kg → 平均 7.5 kg → 杠上 = 140 − 7.5 = **132.5 kg**。
- 带：目标卧推 5RM=160 kg、底部 0 kg、顶部 30 kg → 平均 15 kg → 杠上 = 160 − 15 = **145 kg**。
- **原书未说明**合成输入的实测结果。

## A2 — 未来触发 (Trigger)

**用户会在什么情境下遇到这类问题**：
1. 用户问"加了链条/弹力带，杠铃该挂多重"。
2. 用户直接把链重当"额外重量"加上去，问为什么实际太重/太轻。
3. 用户问链/带在顶部和底部的阻力不一样，该按哪个算。
4. 用户问弹力带的张力怎么查、能不能用预测方程算。
5. 用户问"5RM 120 kg 加链 11 kg 该怎么配"这类具体数值。

**情境的语言信号（中英双写关键 trigger 词）**：链条 / 链负重 / chains / 弹力带 / 阻力带 / resistance bands / 变阻 / variable resistance / 加链后杠铃配多重 / 顶底平均 / average chain resistance / 弹力带张力 / 长度—张力 / Hooke / 5RM 加链怎么算 / 顶部底部阻力。

**与相邻能力的区分（初稿）**：本卡只产出**杠上加载量的数值计算**（顶底平均后扣除）。**用链/带是否合适（训练状态门槛）**与**其他替代手段的采用决策**属 `alternative-modes-decision`；**AEL 离心过载**属 `accentuated-eccentric-loading`；**RM 负荷本身怎么定**属负荷处方能力；**链/带动作本体技术**属 reference/`power-exercise-phases`。

## E — 执行 (Execution)

**输入契约**
- 必需（每项**数值 + 单位 + 测量位置**）：
  - `target_RM_load`：无链/无带下的目标 RM 负荷（kg 或 lb，须注明该 RM）。
  - `resistance_bottom`：动作**底部**的链/带绝对阻力。
  - `resistance_top`：动作**顶部**的链/带绝对阻力。
- 可选：带材规格（宽 mm/颜色）与拉伸长度（用于查 Table 17.2）。
- **缺任一阻力值或单位时应先询问**，不得假定底部 = 0（链在底部常为 0，但**必须确认**）。

**算法（链与带同一套；计算顺序固定）**
1. **统一单位**：把 `target_RM_load`、`resistance_bottom`、`resistance_top` 统一为同一单位（kg 或 lb）。**不得混用**（原文示例中对 120 kg 同列 265 lb，换算即成对出现）。
2. **平均阻力**：`avg = (resistance_bottom + resistance_top) / 2`。
3. **杠上加载量**：`bar_load = target_RM_load − avg`。
4. **取整/给出范围**：按器械可加的最小片重取整，给出**区间**（原文用"114 to 115 kg"式区间）。
   - 完成标准：输出 `avg` 与 `bar_load`（区间），并复核 `bar_load + avg = target_RM_load`（±最小片重容差）。

**步骤（可判断完成标准）**
- 完成标准：每一步给出中间量；最终 `bar_load + avg` 应回到 `target_RM_load`。

**数值演练（按原书规则复算）**
- 链：120 − (0 + 11.1)/2 = 120 − 5.55 = **114.45 kg → 114–115 kg**。
- 带：150 − (0 + 26.6)/2 = 150 − 13.3 = **136.7 kg → 136–137 kg**。
- 复算一致（容差 = 最小片重，通常 ≤2.5 kg）。

**输出契约**
- 字段：`{ implement(chain|band), target_RM_load{value,unit,rm}, resistance_bottom, resistance_top, avg_resistance, bar_load{lo,hi,unit} }`。
- 完成标准：`avg_resistance = (bottom+top)/2`；`bar_load ≈ target − avg`。
- 单位/容差：kg 或 lb（成对）；舍入到最小可行片重区间。
- **约定（原文未规定，标为约定）**：原文未给"底部必为 0"的普适假设，也未给取整规则；本卡要求**实测底部阻力**（若确为链触地/带松弛才可记 0），取整规则按可用片重，属实现约定，不改变原意。

**原文单位/信息缺口（如实登记，不臆补）**
1. **弹力带长度—张力预测方程的自变量单位未定义（`N15` / `p17-16`，原文 `ch17.txt` 第 583–615 行）**：Table 17.2 的方程 `Y = a·x² + b·x + c`（如 67 mm 黑带 `Y = −0.010x² + 3.73x − 269.21`）**未说明自变量 x 的物理量与单位**（是长度 cm？拉伸量？），且代入 150 得 `−225 + 559.5 − 269.21 = 65.29 kg`，与表中 150 cm 的 **57.2 kg 不符**，口径不明。
   → **本卡只采用"查表"路径**（直接读 Table 17.2 的张力值）；**预测方程分支不使用**，并在需要外推时标注"原文自变量单位未定义，不可直接代入"。
2. **原木直径单位标注自相矛盾（`N14` / `p17-31`，原文 `ch17.txt` 第 1021–1024 行）**：原文写"a thinner log (250 mm [1.0 in.] diameter)"与"a thicker log (316 mm [1.2 in.] diameter)"——**250 mm ≈ 9.8 in.、316 mm ≈ 12.4 in.**，与标注的 1.0/1.2 in. **互斥**（疑排版错误）。此项**不属本卡的负荷计算**，仅作为原文内部矛盾登记；如引用原木直径须先裁定口径。
3. Table 17.2 的方程系数对应**特定厂商带**，跨品牌不可直接套用（`ce17-05` 的带间 3.2%–5.2% 差异）。

## B — 边界 (Boundary)

- **不要**把链/带重量当作**恒定额外负荷**直接加上去——必须先取顶底平均再**扣除**（`ce17-01`）；否则实际负荷偏离目标 RM。
- **不要**用本卡给**新手/技术不稳者**开变阻处方：原文（`ce17-02`）建议链仅用于**技术稳定的中高级/精英**运动员，变阻会改变负荷曲线、影响技术。
- **不要**假定同规格带拉力一致：带间差异 3.2%–5.2% → 平均张力差 8%–19%（`ce17-05`）；跨批次/品牌混用须实测核定。
- **不要**用预测方程外推：自变量单位未定义且与表中值不符（`N15`）——**只用查表**。
- **不要**引用原木直径数字不作裁定（`N14`：mm 与 in. 标注互斥）。
- **变量耦合 / 共识 ≠ 实证**（BOOK_OVERVIEW 3.3）：变阻的"更好"证据本身有限（带的研究"minimal ... longitudinal"、链亦是），本卡只保证**算得对**，不宣称效果优越。
- **相邻易混**：把"该不该用链/带"（`alternative-modes-decision`）或"AEL"（`accentuated-eccentric-loading`）混入本卡。

## 相关能力

- 组合（常配合使用）：`accentuated-eccentric-loading`
- 组合（常配合使用）：`alternative-modes-decision`
- 组合（常配合使用）：`load-reps-assignment`
