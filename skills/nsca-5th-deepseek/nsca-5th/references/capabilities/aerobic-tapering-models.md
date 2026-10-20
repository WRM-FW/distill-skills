# 赛前减量（tapering）模型选择

## R — 原文 (Reading)

> "The most common tapering models are linear, step, and progressive tapers. The linear taper is characterized by a gradual decrease in the overall daily training volume" ... "a step taper is typified by an abrupt and considerable reduction (normally ≥50%) in training volume" ... "a progressive taper uses a combination of the linear and step tapering models" ... "a rapid 10% to 15% immediate reduction in training volume, with smaller, more gradual reductions in volume at each tier."

— Chapter 21 · "Tapering"（`ch21.txt` 第 1346–1355 行）

## I — 自述 (Interpretation)

赛前减量通过**系统性降低训练量 + 维持强度与频率 + 强化技术与营养**，让运动员在比赛日达到峰值；典型减量期 **7–28 天**。三种模型可选：

- **Linear（线性）**：在整个减量期内**每日训练量逐步下降**。
- **Step（阶梯）**：**骤然大幅降量（通常 ≥50%）**，并在整段减量期内保持该低量不变、不再波动。
- **Progressive（渐进）**：线性 + 阶梯的组合——**先即时降量 10%–15%**，随后每一档做更小幅的递减。

**共同原则**：降的是**训练量**，同时**维持强度与频率**。（误把强度一起降掉是常见错误。）模型选择依运动员与项目对减量的反应。减量还帮助恢复与再水合、促进肌/肝糖原储备回升。

底层依据（Ch22 fitness–fatigue）：疲劳消退约比体能快三分之二，故"保持体能、削减疲劳"即可抬升备战状态——这正是减量与赛前 peak 的理论基础。

## A1 — 案例 / 演练 (Application)

**原书未提供减量例题**（该节为规则文章节）。以下为**明确标记的合成演练**（`_verified/E-aerobic.md` V2 walkthrough）：

- **情境**：马拉松跑者、距主要比赛 14 天、拟用 progressive taper。
- **按规则可推出的方案**：定 14 天减量期；**即时降量 10%–15%**，随后每档更小幅递减；全程**维持强度与频率**；强化技术与营养。
- 原书未说明该方案的实际比赛结果。

## A2 — 未来触发 (Trigger)

**用户会在什么情境下遇到这类问题**
1. 距主要比赛还有 X 天，问"该怎么减量、减多少"。
2. 纠结用线性、阶梯还是渐进减量模型。
3. 不确定减量时"该降量还是也降强度"。
4. 想用减量让运动员在比赛日达峰，但怕减过头或减不够。

**语言信号（中英双写关键 trigger）**
- 中文：「赛前怎么减量」「tapering 怎么排」「线性/阶梯/渐进减量」「减量期多少天」「减量要不要降强度」「赛前两周怎么练」
- English: "tapering", "taper before competition", "linear vs step vs progressive taper", "how many days to taper", "reduce volume keep intensity", "peaking for race"

**与相邻能力的区分（初稿，阶段 3 回填）**
- 与 `aerobic-program-design-five-variables`：那张排常规计划；本卡只处理赛前减量窗口。
- 与 `aerobic-progression-10pct-single-variable`：一个是"加量"、一个是"减量"，方向相反，触发词不同。
- 与 `peaking-vs-maintenance`、`periodization-*`（周期化簇）：峰值/维持的赛季级决策归那组；本卡是赛前 7–28 天的减量模型。
- 与 `aerobic-recovery-session`：恢复课是日常低强度短课，不是减量。

## E — 执行 (Execution)

**输入契约**
- 必需：① 主要比赛日期；② 当前日期（算剩余减量天数）；③ 运动员/项目对减量的历史反应（可选但影响模型选择）；④ 当前训练量与强度基线。
- 缺失处理：比赛日期缺失 → 无法定减量窗口，先询问；无历史反应数据 → 选较保守的 progressive 并标为约定。

**执行步骤（四步，每步有完成标准）**
1. **定减量时长**：典型 7–28 天（依比赛重要性、项目、个体反应）。完成标准：给出起止日期与天数。
2. **选模型**（完成标准：写明所选模型及依据）：
   - 稳定、想平稳降量 → **linear**：每日量逐步递减；
   - 想快速卸掉疲劳、量低且不再波动 → **step**：突降 ≥50% 并保持；
   - 想兼顾两法、常见默认 → **progressive**：先即时降 10%–15%，再逐档小幅递减。
3. **降量、保强度与频率**：训练**量**系统性下调，**强度与频率维持**。完成标准：量有降幅数值、强度与频率取值与减量前一致。
4. **配套技术与营养**：强化技术工作与营养干预；促进恢复与再水合、提升糖原储备。完成标准：列出技术/营养安排。

**判停点/分支**
- 若出现"把强度也降了"→ 违规，回 Step 3 修正（减量只减量不减强度）。
- 若减量期内又想加练 → 检查是否偏离"维持强度、降低量"；超过 28 天窗口须另评估（峰值窗口不宜延长）。

**输出契约**
- `{减量天数（起止）, 模型, 逐档降量曲线（%）, 维持的强度与频率, 技术与营养配套}`。
- 数值口径：typical 7–28 天；step 降量 ≥50%；progressive 首档 10%–15%。逐日具体曲线原文未给（本卡以模型定义为准，具体落值标为约定）。

## B — 边界 (Boundary)

- **不要用**：当问题是赛季级"峰值 vs 维持"时（用 `peaking-vs-maintenance`）；当只是日常恢复课时（用 `aerobic-recovery-session`）；当问题是"如何加量进阶"时（用进阶卡）。
- **作者警告的失败模式**：把减量误解为"少练点"而同时降强度——会丧失峰值所需的强度刺激；峰值窗口拉长反而使表现下降（见 Ch22 fitness–fatigue）。
- **盲点（BOOK_OVERVIEW 步骤 3）**：减量研究**多数在游泳者**（原书明示），迁移到跑/骑有证据但需校验；7–28 天为"typical"区间而非精确处方；各模型逐日降量曲线原文未给；个体对减量反应差异大。
- **相邻易混**：`peaking-vs-maintenance`（赛季级峰值/维持）、`aerobic-recovery-session`（日常恢复课）。

## 相关能力

- 组合（常配合使用）：`aerobic-program-design-five-variables`
- 组合（常配合使用）：`peaking-vs-maintenance`
