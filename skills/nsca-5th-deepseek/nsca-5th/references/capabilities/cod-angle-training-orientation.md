# 变向训练取向决策（角度/入速 → 快慢 SSC + GCT 基准）

## R — 原文 (Reading)

> "COD and agility movements performed at shallow cutting angles (less than 75 degrees) and associated with shorter ground contact times (less than 250 ms) benefit from training similar to speed training with regard to the physical demands but still require additional perceptual-cognitive training." ... "when a COD involves a more aggressive cutting angle (equal to or greater than 75 degrees), the length of ground contact time can often exceed 250 milliseconds."

— Chapter 20 · "Factors Affecting Change of Direction and Perceptual-Cognitive Ability"（`ch20.txt` 第 1172–1180 行）

## I — 自述 (Interpretation)

变向的力学需求随**变向角度**与**入速**变化，训练重点应据此切换。浅切角（<75°）且触地时间短（<250 ms）的变向，物理需求接近速度训练（偏快 SSC），但仍须补知觉—认知训练。更激进的切角（≥75°）因 braking 需求更大，触地时间常超过 250 ms（偏慢 SSC），应加大**偏心力量**（制动）、**最大力量**，以及再加速所需的**向心爆发力**；又因 plant 期的离心—向心耦合，**reactive strength** 也是训练优先项。入速越高、角度越大，改变动量所需的冲量越大，动作越吃力。因此设计时谨慎操纵这两个变量来定向施加所需适应。触地时间（GCT）基准可用于归类：敏捷动作 0.23–0.25 s、COD 约 0.15–0.6 s（随角度）、冲刺加速相 0.17–0.2 s、最大速相 0.09–0.11 s。

## A1 — 案例 / 演练 (Application)

原书未提供单个运动员案例，但给出角度/触地阈值与 GCT 基准。以下为**合成演练**（明确标记，规则来自 p20-08/09/10）：

- 输入：运动员以高速入速做 90° 切角变向。
- 执行：按 75°/250 ms 判据——90° ≥75° → 判定 GCT 常 >250 ms → 偏慢 SSC。
- 预期输出：训练重点 = 增强偏心力量（制动）+ 最大力量 + 再加速所需向心爆发力/reactive strength；对照浅切 30° 且 GCT<250 ms 时 → 接近速度训练但仍需补知觉—认知。并提示入速越高所需 impulse 越大（呼应 `speed-force-metrics-calculation` 的 braking impulse）。

## A2 — 未来触发 (Trigger)

**用户会在什么情境下遇到这类问题**
1. 纠结变向训练"该练速度还是该练力量"。
2. 运动员变向角度大、入速高，想知道制动/再加速该补什么。
3. 需要按可测变量（角度、触地时间）给变向训练定方向。
4. 想判断某变向动作落在快 SSC 还是慢 SSC。

**语言信号（中英双写关键 trigger）**
- 中文：「90° 变向该练什么」「浅切角要不要练力量」「触地时间多长算慢 SSC」「变向要不要加知觉认知」「eccentric braking 训练取向」
- English: "cutting angle 75 degrees rule", "fast vs slow SSC COD", "ground contact time 250 ms", "eccentric strength for braking", "shallow vs aggressive cutting"

**与相邻能力的区分（初稿，阶段 3 回填）**
- 与 `agility-needs-analysis-to-program`：本卡定**训练取向**（练什么素质），后者排**计划块与时间**。
- 与 `cod-technique-diagnosis`：本卡判取向，后者看**技术动作**哪里错。
- 与 `ssc-speed-training-criteria`：本卡用角度归 SSC 快慢，后者判 SSC 类练习是否达标。

## E — 执行 (Execution)

**输入契约**
- 必需：① 变向角度（°）；② 入速（高/中/低或 m/s）；③ 若可得，plant 期触地时间（ms）。
- 缺失 ③ 时：可按角度先判，再用 GCT 基准做近似归类，并标注为估计。

**步骤与完成标准**
1. 测/读切角与入速。
2. 判快/慢 SSC 倾向（分支）：<75° 且 GCT<250 ms → 偏快 SSC；≥75° 或 GCT>250 ms → 偏慢 SSC。
3. 定训练权重（分支）：
   - 偏快 SSC → 训练接近速度训练（RFD/弹反），但仍须加知觉—认知。
   - 偏慢 SSC → 加大偏心力量（制动）+ 最大力量 + 向心爆发力/reactive strength。
4. 提示入速↑或角度↑ → 所需 impulse 更大，物理负荷更高。
5. 完成标准：输出明确的训练取向（速度取向 vs 力量取向）及对应素质权重。

**输出契约**
- `{角度, 入速, GCT, SSC 倾向, 训练取向, 素质权重}`；含需补的知觉—认知提示。

**原文口径与内部不一致说明**
- **约定**：原文对不同分界给出两套数——一类按 **<45° 快 SSC / >45° 慢 SSC** 分类（p20-08），另一套按 **<75° vs ≥75°（配 250 ms）** 定训练取向（p20-10/U8）。两者角度不同（45° vs 75°）、用途不同（SSC 分类 vs 训练取向）。**本卡以 U8 采用的 75°/250 ms 为准**（verified 记录指定），45° 仅作参考；作者亦注明阈值取决于入速与个体能力。
- GCT 基准（第 400–410 行附近，p20-09）：敏捷 0.23–0.25 s、COD ~0.15–0.6 s、冲刺加速 0.17–0.2 s、最大速 0.09–0.11 s。

## B — 边界 (Boundary)

- **不要用**：当问题只是"这是哪种能力"时（用 `speed-cod-agility-attribution`）；当需要算具体冲量数值时（用 `speed-force-metrics-calculation`）。
- **作者警告的失败模式**：把浅切角的变向当纯速度练、漏掉知觉—认知；把大角度变向当纯技术练、漏掉偏心/最大力量。
- **盲点（BOOK_OVERVIEW 步骤 3）**：75°/250 ms 为**近似阈值**，作者明确说取决于进入速度与个体能力，不能脱离情境硬套；GCT 基准的 COD 区间跨度大（0.15–0.6 s），须结合具体角度取值；reactive strength 此处仅定性提及，Ch20 未给 RSI 公式（属 Ch19）。
- **相邻易混**：`cod-technique-diagnosis`、`ssc-speed-training-criteria`。

## 相关能力

- 组合（常配合使用）：`cod-technique-diagnosis`
- 组合（常配合使用）：`ssc-speed-training-criteria`
