# 组间休息时长（Step 7）

## R — 原文 (Reading)

> "not all exercises in a resistance training program should be assigned the same rest periods. It is important that the strength and conditioning professional allocate rest periods based on the relative load lifted and the amount of muscle mass involved in each exercise."

— Chapter 18 · Step 7: Rest Periods（`ch18.txt` 2443–2446）

## I — 自述 (Interpretation)

第 7 步定"组间/动作间休息多久"。三个决定因素：**训练目标、相对负荷、训练状态**（体能差者初期需更长休息）。规则：**休息与负荷正相关**——负荷越重休息越长。

按目标查 Table 18.15：
- Strength：2–5 min
- Power（单次/多次用力项）：2–5 min
- Hypertrophy：多关节 2–3 min；单关节 60–90 s
- Muscular endurance：≤30 s

**核心微调原则**：**不要给整堂课套一个休息值**。休息应逐动作看**该动作实际相对负荷**与**参与肌群量**。表 18.15 脚注明确：当辅助动作的 %1RM 落在目标区间之外时（如力量计划中辅助用 ≥8RM 负荷），应按**该动作实际负荷**分配休息，而不是笼统套用目标档。典型示例：力量计划中 4RM 卧推（核心、多关节）约需 **4 min**，而同计划的 12RM 侧平举（辅助、单关节）只需约 **1 min**。

## A1 — 案例 / 演练 (Application)

**原书案例（worked-example，"Rest Periods"段）**：力量计划中，bench press 用 4RM 负荷 → 约 4 min 休息；lateral shoulder raise 用 12RM 负荷 → 仅需约 1 min 休息（即便 1 min 通常属肥大档）。

**原书案例（tabular-example，c18-13）**：三情境休息应用表——A：power/core 3 min、assist 60–90 s；B：core 2–3 min、assist 60–90 s；C：core 30 s、assist ≤20 s。

**合成演练（标记：合成；非书中案例）**
- 输入：同一力量（strength）程序内含 4RM bench press（核心、多关节）与 12RM lateral shoulder raise（辅助、单关节）。
- 执行：先按目标查 18.15 → 力量档 2–5 min；再按该动作实际负荷与肌群量逐动作微调——bench press 取约 3–4 min（偏长）；lateral raise 按其 12RM 实际负荷落到 60–90 s。
- 预期输出：两个不同休息值。原书未说明该合成输入的"实际结果"。

## A2 — 未来触发 (Trigger)

**用户会遇到这类问题的情境（3–5 条）**
- 用户问"每组之间休息多久"。
- 用户按力量/肥大/耐力目标问休息该怎么取。
- 用户想把整堂课用同一个休息值，问是否可行。
- 用户问辅助动作该休多久（负荷与目标不一致时）。
- 用户问体能差的运动员初期要不要延长休息。

**语言信号（中英双写关键 trigger 词）**
- "组间休息多久" / "rest period"、"inter-set rest"、"休息时长"、"力量/肥大分别休多久"、"整堂课一个休息时间行吗"、"辅助动作休息"、"table 18.15"、"休息和负荷的关系"、"体能差要休长点吗"。
- 英文常见："how long to rest between sets"。

**与相邻能力的区分（初稿）**
- 与 **load-reps-assignment**：休息依赖相对负荷，但负荷由后者定。
- 与 **exercise-order**：排序法（如 circuit 用 20–30 s）与休息相关，顺序由前者承载。
- 与 **training-volume**：休息时长不直接计入 volume-load，量由后者承载。
- 与 **power-load-assignment**：power 的休息档（2–5 min）随其负荷特例，但负荷特例由前者承载。

## E — 执行 (Execution)

**输入契约**
- 必需：训练目标、每个动作的相对负荷（RM 档）、训练状态、所涉肌群量（多关节/单关节、大/小肌群）。
- **先询问（缺失不得静默猜值）**：若不知每个动作的相对负荷 → 先由 load-reps-assignment 确定（休息需按实际负荷而非目标名）；若不知训练状态 → 询问；若体能差者 → 初期可延长，需注明。
- 适用条件：任何抗阻计划。

**步骤（每步有完成标准）**
1. **按目标查 Table 18.15 得区间**——完成标准：strength 2–5 min；power 2–5 min；hypertrophy 多关节 2–3 min / 单关节 60–90 s；endurance ≤30 s。
2. **逐动作微调（相对负荷 + 肌群量）**——完成标准：看该动作实际 RM 档与肌群量，在区间内上下调整。判停点：**辅助动作越出目标档**（如力量计划中辅助用 ≥8RM）→ **按该动作实际负荷**分配，而非套用目标档。
3. **体能差者延长**——完成标准：训练状态差者初期休息适当延长，并注明。
4. **交付**——完成标准：输出逐动作 `{ exercise, 目标档, 实际负荷依据, 休息时长 }`。

**输出契约**
- 字段：`[{ exercise, rest_period, unit(min|s), 依据(负荷+肌群量) }]`。
- 数值：分钟或秒，照 Table 18.15 档位与微调区间。
- 约定：原文未给"从负荷到具体秒数"的换算公式，微调靠教练判断；同一程序内不同动作负荷可跨目标，须逐动作判定。

## B — 边界 (Boundary)

- **不要**给整堂课套用同一个休息值——这是作者点名要避免的做法；应逐动作按相对负荷与肌群量分配。
- **不要**对辅助动作笼统套用目标档——其 %1RM 常落在目标区间之外，须按实际负荷判休息。
- **变量耦合**（BOOK_OVERVIEW 3.3）：休息与负荷、量、排序互相牵动；改休息会影响可完成次数与 volume-load。
- **共识 ≠ 实证**（3.3）：休息档位多来自实践惯例与研究，个体与动作差异大。
- 易混淆：与 **exercise-order**（排序法里含 circuit 的 20–30 s）、**load-reps-assignment**（负荷）不同——本卡只产出"休息时长"。

## 相关能力

- 依赖（先理解）：`load-reps-assignment`
- 依赖（先理解）：`seven-step-program-design`
- 组合（常配合使用）：`training-volume`

## 配套资源

路径相对于本文件；脚本需先检查运行条件，不因附带而自动执行。

- [resources/load-volume-rest-assignment.md](../../resources/load-volume-rest-assignment.md)
