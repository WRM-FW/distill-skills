# 训练量分配（Step 6 + volume-load 计算）

## R — 原文 (Reading)

> "Repetition-volume is the total number of repetitions performed during a workout session, and volume–load is the total number of sets multiplied by the number of repetitions per set, then multiplied by the weight lifted per repetition."

— Chapter 18 · Step 6: Volume（`ch18.txt` 2180–2183）

## I — 自述 (Interpretation)

第 6 步定"做多少组、多少次"。先分清两个口径：

- **repetition-volume** ＝ 总次数。
- **volume-load** ＝ 组数 × 每组次数 × 负荷重量（原文示例：2×10×50 lb = 1,000 lb）。

计算要点：
- 当**运动员自身质量被移动**时（如 loaded jump squat）用 **system mass volume-load**（体重 + 外部负荷）；仅外部负重时（如 bench press）只算外部负荷。示例：80 kg 运动员 + 40 kg 跳蹲负荷、4×3 → 120 kg × 12 = **1,440 kg**。
- 不同负荷的组分别算再相加。
- 位移修正：高的运动员同负荷同深度做功更多 → **volume-load displacement** ＝ volume-load × 动作位移（需技术测量）。
- volume-load 是机械功/代谢需求的代理量，用于规划变异、避免过度训练。跨模态类比：跑步=距离、plyometric=触地次数、游泳/划船=划次。

量的分配：
- **训练状态**：入门者仅 1–2 组，随适应渐加。
- **目标（Table 18.13）**：Strength ≤6 次（组 1–3/≥3/≥3）；Power 1–3 次（单次用力项 3–6，组 1–3/3–6）；Hypertrophy 8–12 次（novice/intermediate 6–12、advanced 3–12；组 1–3/≥3/≥3）；Muscular endurance 12–15 次（advanced 12–25；组 1–3/≥3/≥3）。
- 辅助动作常 1–3 组；每肌群约 8 组 @85% 1RM 获最大力量增益（剂量-反应）；单组适合未训练者/最初数月，多组更适合中高级。

## A1 — 案例 / 演练 (Application)

**原书案例（worked-example，c18-11）**：2 组 × 10 次 × 50 lb = **1,000 lb（454 kg）**；80 kg 运动员 + 40 kg 跳蹲负荷、4×3 = 120 kg × 12 = **1,440 kg**。

**原书案例（tabular-example，c18-12）**：三情境量分配——A：power 3×3、other core 3×4、assist 2×8；B：core 3×10、assist 3×10；C：core 3×12、assist 2×15。

**原书案例（worked-example，c18-18）**：5'6" 与 6'0" 运动员同负荷同深蹲深度的做功不同——较高者移动距离更远、做功更多（volume-load displacement 的依据）。

**合成演练（标记：合成；非书中案例）**
- A：4 组 × 6 次 × 100 kg 深蹲 → **2,400 kg**（容差 0）。B：90 kg 运动员负重跳蹲、外部 30 kg、5×3 → 系统质量 120 kg → 120×15 = **1,800 kg**（容差 0）。

## A2 — 未来触发 (Trigger)

**用户会遇到这类问题的情境（3–5 条）**
- 用户问"每个动作做几组几次"。
- 用户问"训练量怎么算/总量多少"（volume-load、组×次×负荷）。
- 用户问负重跳蹲这类"移动体重"的动作怎么折算量。
- 用户问不同身高运动员同负荷的做功差异。
- 用户要比较大重量高量计划的风险或规划减量周。

**语言信号（中英双写关键 trigger 词）**
- "做几组几次" / "training volume"、"volume load"、"volume-load"、"组数×次数×负荷"、"训练量怎么算"、"system mass"、"体重算不算"、"1×10×50 等于多少"、"每肌群几组"、"单组还是多组"、"训练总量"。
- 英文常见："how many sets and reps"、"how to compute volume load"。

**与相邻能力的区分（初稿）**
- 与 **load-reps-assignment**：后者定负荷×目标次数，本卡定组数与 volume-load 口径。
- 与 **rest-periods**：休息时长不直接计入 volume-load 计算（原文指出），由后者承载。
- 与 B-periodization 簇：减量周的 volume-load 编排归周期化；本卡只给量的口径与目标档。
- 与 **exercise-selection**：动作类型（core/assistance/power）影响量与组数，选择由前者承载。

## E — 执行 (Execution)

**输入契约**
- 必需：训练状态、主要训练目标、动作类型（core/assistance/power）、每个动作的组数/次数/负荷、是否涉及运动员自身质量与体重。
- **先询问（缺失不得静默猜值）**：若不知道是否"移动自身体重"（如跳蹲）→ 询问动作性质，决定是否用 system mass；若缺训练状态或目标 → 先补齐（决定 Table 18.13 档位）；若缺体重而动作移动自重 → 询问体重。
- 适用条件：任何抗阻计划。

**步骤（每步有完成标准）**
1. **按状态定起始组数**——完成标准：入门 1–2 组，随适应渐加；注明辅助动作常 1–3 组。
2. **按目标查 Table 18.13 取次数×组数**——完成标准：strength ≤6（组 1–3/≥3/≥3）；power 1–3（单次用力项 3–6；组 1–3/3–6）；hypertrophy 8–12（组 1–3/≥3/≥3）；endurance 12–15（组 1–3/≥3/≥3）。
3. **算 volume-load**——完成标准：`sets × reps × load`；移动自重者 `load_eff = 体重 + 外部负荷`；不同负荷的组分别算再相加。判停点：若需比较不同身高者做功 → 引入 volume-load displacement。
4. **交付**——完成标准：输出每动作 `{ 组数, 次数, repetition-volume, volume-load }` 及总训练课量。

**输出契约**
- 字段：`{ exercise, sets, reps, load, repetition_volume, volume_load, unit }`。
- 数值：单位 lb 或 kg（位移版 lb·m/kg·m）；示例容差 0（确定性乘法）。
- 约定：传统 volume-load 未计入位移；位移版需 anthropometry/技术测量。原文未给"上限"量化（高量风险仅提示）。

## B — 边界 (Boundary)

- **不要**忘记区分 system mass 与仅外部负荷——移动自重的动作（跳蹲）须加体重，只负重的动作（卧推/肩推）只算外部负荷。
- **不要**把高量计划普遍套用——原文提示高量（尤其重负荷高量肥大）有较大 volume-load 与耗时风险，未给上限，应谨慎。
- **训练到力竭非必要**：靠近力竭会增大随后 24 h 疲劳；RIR 法远离力竭时又变不准（ce18-02）。
- **共识 ≠ 实证**（BOOK_OVERVIEW 3.3）：8 组/肌群、单/多组等来自研究与实践惯例，个体响应不同。
- **变量耦合**（3.3）：改量会牵动负荷、休息与恢复安排。
- 易混淆：与 **load-reps-assignment**（负荷×次数）、**rest-periods**（休息不计入 volume-load）不同——本卡只处理"组数与量的量化"。

## 相关能力

- 依赖（先理解）：`training-status-classification`
- 组合（常配合使用）：`athlete-monitoring-plan-design`
- 组合（常配合使用）：`load-reps-assignment`
- 组合（常配合使用）：`local-muscular-endurance-protocols`
- 组合（常配合使用）：`older-adult-resistance-training`
- 组合（常配合使用）：`plyometric-intensity-volume`
- 组合（常配合使用）：`rest-periods`
- 组合（常配合使用）：`training-frequency`

## 配套资源

路径相对于本文件；脚本需先检查运行条件，不因附带而自动执行。

- [resources/load-volume-rest-assignment.md](../../resources/load-volume-rest-assignment.md)
