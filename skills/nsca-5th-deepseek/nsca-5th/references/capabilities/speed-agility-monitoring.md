# 速度/敏捷监控指标选择与解读

## R — 原文 (Reading)

> "decreased ground contact times coupled with improved sprint completion times may suggest that an athlete has improved the ability to generate high rates of force in a shorter amount of time. However, an athlete may demonstrate slightly longer ground contact times at the initial stages of the sprint due to acceleration mechanics." ... "Improved exit velocity with the same or faster ground contact times implies greater RFD relevant to improving COD ability."

— Chapter 20 · Table 20.8（`ch20.txt` 第 2262–2273 行）；Table 20.12（第 2581–2584 行）

## I — 自述 (Interpretation)

只看完成时间不足以反映进展——它会被直线速度"污染"，也不说明进步来自哪里。原书给出两组监控面板并要求交叉解读。**速度监控（Table 20.8）**：触地时间、步长/步幅长、腾空时间、步幅角、速度/瞬时速度、加速度、技术。解读规则：触地时间缩短且完赛时间改善 → 单位时间发力能力（RFD）增强；但加速初段触地时间略长属正常（加速机制所致）；腾空时间增加有二义——可能是"更短触地产生更高竖力"（优），也可能是"竖直振幅过大"（劣），须结合步幅角与速度判断所处阶段。**敏捷/COD 监控（Table 20.12）**：完成时间、COD deficit、GCT、exit velocity、entry velocity、决策时间、COD 分相信息。解读规则：exit velocity 在同或更短 GCT 下提升 → RFD 提升；entry velocity 是 COD 完成时间的强决定因素；决策时间可为负值（表示刺激定型前已预判，仅见于人际/视频刺激）。工具上，>100 fps 高速相机可替代昂贵的 3D 分析。

## A1 — 案例 / 演练 (Application)

原书未提供独立运动员案例，但给出两组监控变量与解读规则。以下为**合成演练**（明确标记，规则来自 Table 20.8/20.12）：

- 输入：运动员 A 5-0-5 完成时间变慢，但 COD deficit 不变；运动员 B 冲刺 GCT 缩短且完赛时间改善。
- 执行：按解读规则逐条归因。
- 预期输出：① A = 完成时间受直线速度影响，COD 能力未退化（COD deficit 不变）；② B = 单位时间发力能力（RFD）提升。若腾空时间增加，须结合步幅角与速度判断是"更短触地产生更高竖力"还是"竖直振幅过大"。

## A2 — 未来触发 (Trigger)

**用户会在什么情境下遇到这类问题**
1. 运动员 5-0-5/冲刺成绩变了，想知道是变向能力还是直线速度在变。
2. 拿到一批 GPS/高速相机指标，不知道各自含义与解读方向。
3. 需要判断"进步到底来自哪里"（发力速率 / 机制 / 策略）。
4. 想在 GPS/计时门之外补更细的技术监控。

**语言信号（中英双写关键 trigger）**
- 中文：「5-0-5 变慢是退步吗」「COD deficit 没变说明什么」「GCT 缩短代表什么」「腾空时间增加是好是坏」「监控该看哪些指标」
- English: "monitoring speed development variables", "interpret ground contact time", "COD deficit vs completion time", "exit velocity RFD", "flight time meaning"

**与相邻能力的区分（初稿，阶段 3 回填）**
- 与 `speed-force-metrics-calculation`：本卡给变量与**解读方向**，后者给公式与算例。
- 与 `speed-cod-agility-attribution`：本卡看**变化**，后者看**能力类别**。
- 与 `sprint-step-length-frequency`：本卡监控面板较全，后者专诊断步长/步频两变量。

## E — 执行 (Execution)

**输入契约**
- 必需：① 至少一个时间点的指标数据（完成时间/GCT/速度等）；② 最好有历史或常模做对照。
- 工具条件：>100 fps 高速相机 + 计时办法（手计或电子）即可做基本监控；3D 分析可选。
- 缺失对照数据时：只能做单次描述，不能做达标判定（原文未给常模）。

**步骤与完成标准**
1. 选指标：速度侧用 Table 20.8；敏捷/COD 侧用 Table 20.12。
2. 按规则解读（分支）：
   - GCT↓ + 完赛时间↓ → RFD 提升（但加速初段 GCT 略长属正常）。
   - 腾空时间↑ → 结合步幅角与速度判断：更短触地高竖力（优）or 竖直振幅过大（劣）。
   - 完成时间↓ 但 COD deficit 不变 → 变化来自直线速度，COD 能力未变。
   - exit velocity↑ 且 GCT 同或更短 → COD 相关 RFD 提升。
   - 决策时间为负 → 预判早于刺激定型（仅人际/视频刺激）。
3. 交叉验证：用至少两个指标互相印证，避免单指标误判。
4. **判停点**：若缺常模/目标值，只输出"变化方向"而非"达标/未达标"。
5. 完成标准：输出每条指标的归因（发力速率 / 机制 / 策略）与调整依据。

**输出契约**
- `{指标, 数值或变化方向, 归因, 调整建议}` 的监控面板；说明所依据的解读规则。

## B — 边界 (Boundary)

- **不要用**：当需要把指标换算成具体力学量时（用 `speed-force-metrics-calculation`）；当只做能力类别归因时（用 `speed-cod-agility-attribution`）。
- **作者警告的失败模式**：只看完成时间就下结论——它偏向直线速度优者、且不隔离要考察的素质（Table 20.12 明示）。
- **盲点（BOOK_OVERVIEW 步骤 3）**：**原文未给各变量的常模/目标值**，只能做"变化方向"解读，不能做"达标判定"；工具精度（采样率/触发阈值）会改变 GCT 等结果；监控指标是描述性的，非因果处方。
- **相邻易混**：`speed-force-metrics-calculation`、`sprint-step-length-frequency`。

## 相关能力

- 组合（常配合使用）：`athlete-monitoring-plan-design`
- 组合（常配合使用）：`speed-force-metrics-calculation`
