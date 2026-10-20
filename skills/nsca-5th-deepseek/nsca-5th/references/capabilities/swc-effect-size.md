# 幅度统计（SWC / 效应量 / 差异分解读）

## R — 原文 (Reading)

> "The smallest worthwhile change can be determined in a number of ways, but it is typically calculated as 0.2 of the between-subjects standard deviation. ... reference values for small (0.2), moderate (0.6), large (1.2), and very large (2.0) can be a useful starting point for practitioners. ... The calculated effect size would be equal to (111.7 − 104.5) / 5.7 = 1.26."

— Chapter 14 · Magnitude Statistics（`ch14.txt:1666-1679`）

## I — 自述 (Interpretation)

"幅度统计"回答的不是"有没有变化"（统计显著），而是"变化**有没有实践意义**"。

- **最小有意义变化 SWC**：测试能检出的"最小实践重要变化"，通常取**受试者间 SD 的 0.2 倍**。其可追踪能力本身取决于测试的效度与信度（与准入卡呼应）。
- **效应量 ES**：ES = (后测均值 − 前测均值) / **前测 SD**。用于评价一次训练课对群体的效果或组间比较。
- **量级锚点（起点，非硬标准）**：小 0.2 / 中 0.6 / 大 1.2 / 极大 2.0。
- **用"进步幅度"评价计划的两大陷阱**：① 收益递减——起点训练状态高者进步本就更小；② 运动员可能故意在赛前测试保留实力以放大前后差。

即：把"测出来变了"升级为"变得有意义"，并识别"只看进步幅度"的失败边界。

## A1 — 案例 / 演练 (Application)

**类型：worked-example（原书算例 `c14-02` 与 `c14-03`）。**

- **SWC（原书算例 `c14-02`）**：女子组纵跳 SD = 10 cm → SWC = 0.2 × 10 = **2 cm**。
- **效应量（原书算例 `c14-03`）**：卧推 1RM 前测均值 104.5 kg（SD 5.7 kg），12 周后 111.7 kg → ES = (111.7 − 104.5) / 5.7 = **1.26 → 大效应**。

（两例均为原文数值，可直接复算；独立核算 ES = 6.2 / 5.7 = 1.263 → 1.26。）

## A2 — 未来触发 (Trigger)

**用户情境**：
1. 有前后测数据，问"这次训练到底有没有效果 / 值不值得改计划"。
2. 想知道"多大的变化才算真的有意义"（而不是统计显著）。
3. 问"SWC / 效应量怎么算、多算大"。
4. 想用"进步幅度"评价训练计划成效、拿不准是否可信。

**语言信号（中英双写）**：SWC / smallest worthwhile change / 最小有意义变化 / 最小可察觉变化 / 效应量 / effect size / ES / magnitude / 幅度 / 实用意义 / practical significance / 0.2 / 0.6 / 1.2 / 2.0 / 收益递减 / diminishing returns / 前测 SD。

**与相邻能力的区分**：本卡管**幅度意义判断**（SWC/ES 公式与解读）；z 分数、组内分布与画像流程归 `descriptive-stats-athletic-profile`；把运动员放进常模分布照 `norms-lookup-interpretation`。

## E — 执行 (Execution)

**输入契约（必需字段）**：算 SWC 需 `between_subjects_SD`（受试者间 SD，与指标同单位）；算 ES 需 `x̄_pretest`、`x̄_posttest`、`SD_pretest`（三者同单位）。**缺"SD 是组间还是组内 / 是前测 SD 还是后测 SD"须先问，不得静默假定**。

**步骤与完成标准**：
1. **算 SWC**：`SWC = 0.2 × between-subjects_SD`。完成标准：输出 SWC，单位同指标。
2. **算 ES**：`ES = (x̄_posttest − x̄_pretest) / SD_pretest`（**分母固定用前测 SD**）。完成标准：输出 ES（无量纲），保留 2 位小数。
3. **判定量级**：对照锚点 0.2（小）/0.6（中）/1.2（大）/2.0（极大）。完成标准：给出量级标签 + 所用锚点来源。
4. **（可选）判"变化是否有意义"**：把实际变化量与 SWC 比较（变化 > SWC 视为超过最小实践意义）。完成标准：输出"yes/no + 比较数值"。
5. **输出**：`{SWC, ES, 量级标签, (可选)是否超 SWC}`。

**计算顺序**：先确认分母是"前测 SD"（易错点）→ 再算 ES → 再套锚点。

**容差与舍入**：ES 保留 2 位小数，判定容差 **±0.01**（原文 1.263→1.26）；SWC 按指标精度舍入（如纵跳 2 cm）。

**分支/判停**：
- 若只有"进步幅度"而不知起点训练状态 → **给出收益递减预警**，不得单凭幅度判计划好坏。
- 若怀疑运动员赛前未全力 → 标注"疑似故意低报"，说明会放大前后差（f14-24）。
- 若问"SWC 还有别的算法吗" → 原文称"可用多种方式确定"，但未给其他公式，标记为 gap，勿自造。

## B — 边界 (Boundary)

- **量级阈值只是"起点"**（原文措辞），非唯一权威分级；不同来源阈值可能不同（3.3-5 共识≠实证）。
- **分母易错**：ES 分母是**前测** SD，不是后测或合并 SD；用错会系统性改变量级。
- **不要**仅凭进步幅度评价计划成效——须校正收益递减并排除故意低报（原文两大局限）。
- **SWC 依赖测试质量**：效度/信度不足时，SWC 本身不可信（呼应准入卡）。
- **作者盲点（3.1）**：相关参照若来自旧年代样本，套用须谨慎。
- **单次数据意义有限**：单次 ES 不代表个体响应，须结合趋势与专项（3.3-2）。
- **相邻易混**：本卡判"幅度意义"；"个体在组内/常模中的位置"归 `descriptive-stats-athletic-profile` 与 `norms-lookup-interpretation`。

## 相关能力

- 依赖（先理解）：`reliability-variability-troubleshoot`
- 组合（常配合使用）：`athlete-monitoring-plan-design`
- 组合（常配合使用）：`descriptive-stats-athletic-profile`
