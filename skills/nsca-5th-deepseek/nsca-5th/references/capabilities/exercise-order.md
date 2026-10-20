# 动作顺序（Step 4）

## R — 原文 (Reading)

> "If power exercises are not selected in step 2 (exercise selection), the recommended order of exercises is core exercises (ideally with the most demanding exercises first) and then assistance exercises."

— Chapter 18 · Step 4: Exercise Order（`ch18.txt` 1040–1043）

## I — 自述 (Interpretation)

第 4 步排"单次课内动作先后"。决策主轴：**前一个动作如何影响后一个动作的用力质量或技术**；目标是让运动员在某组具备最大发力能力（足够恢复）与正确技术。四种常用排序法：

1. **默认主法：power → 其他 core → assistance**。爆发动作（举重派生、弹道动作）最先——神经肌肉需求大、需技术、易疲劳、耗能高，须在代谢新鲜时做；若无 power 动作，则 core（理想上最难者优先）→ assistance。依据：靠前动作产生更大最大力量适应，靠后动作受累积疲劳影响。
2. **下肢与上肢交替**——适合未训练者（连续多组同肢太吃力）与时间受限；**下肢先**（肌肉量大、绝对负荷高）；若用最小休息 20–30 s 即 circuit training（非最大化力量的最佳方式）。
3. **push 与 pull 交替**——确保同一肌群不连续使用，降低疲劳；连续多个拉动作会因肱二头疲劳而掉次数。
4. **superset（拮抗肌对）与 compound set（同肌群两动作）**——省时但更苛刻，不适合未训练者。

## A1 — 案例 / 演练 (Application)

**原书案例（tabular-example，c18-6）**：三情境动作顺序应用表给出每周各日编排，如 Scenario A 周一＝Push jerk; Front squat; Incline bench press; Triceps pushdown，并交替 push/pull；原文含例外注释——浓缩训练下背的动作应安排在中立脊柱/直立躯干动作之后。

**合成演练（标记：合成；非书中案例）**
- 输入：单次课动作＝push jerk、front squat、incline bench press、triceps pushdown。
- 执行：按默认主法排序——push jerk(power) → front squat(core, 最难) → incline bench press(core) → triceps pushdown(assistance)；若时间紧可 push–pull 交替（如 front squat 与 seated row 交替）。
- 预期输出：上述序列；校验关键稳定肌（erector spinae）未被两个动作连续过度疲劳。原书未说明该合成输入的"实际结果"。

## A2 — 未来触发 (Trigger)

**用户会遇到这类问题的情境（3–5 条）**
- 用户给出一组动作，问"先做哪个、后做哪个"。
- 用户问爆发/核心/辅助动作该怎么排。
- 用户时间受限，问能否上下肢交替或 push–pull 交替以省时。
- 用户问 superset / compound set 怎么用、适不适合。
- 用户问"为什么深蹲要排在腿屈伸前面"。

**语言信号（中英双写关键 trigger 词）**
- "先练哪个" / "exercise order"、"动作顺序"、"怎么排动作"、"power 放哪"、"核心动作在前"、"上下肢交替"、"push pull 交替"、"超级组"、"superset"、"compound set"、"省时间怎么排"。
- 英文常见："in what order should I do these exercises"、"ordering exercises in a session"。

**与相邻能力的区分（初稿）**
- 与 **exercise-selection**：本卡消费动作清单（含 core/power/assistance 标签），选动作由前者承载。
- 与 **training-frequency**：频率定"哪几天"，本卡定"单次课内顺序"。
- 与 **training-volume / rest-periods**：排序法与休息时长相关（如 circuit 用 20–30 s），但休息时长由 rest-periods 承载。

## E — 执行 (Execution)

**输入契约**
- 必需：当次动作清单（含 core/assistance/power 分类）、运动员训练状态、可用时间。
- **先询问（缺失不得静默猜值）**：若动作清单缺类型标签 → 先按 exercise-selection 的规则归类；若可用时间未知 → 问"单次课多久"以决定是否用交替/组配法；若训练状态未知 → 询问或调用状态判定。
- 适用条件：任何单次课编排。

**步骤（每步有完成标准）**
1. **按分类先排默认主法**——完成标准：输出序列 power → 其他 core（最难者优先）→ assistance。
2. **按需叠加交替/组配法**——完成标准：时间紧或新手 → 加用上下肢交替（下肢先）或 push–pull 交替；追求省时且体能达标 → superset/compound set。
3. **疲劳校验**——判停点：若某关键稳定肌（如 erector spinae）会在两个动作中被连续过度疲劳 → 调整顺序（浓缩下背的动作置于中立脊柱动作之后）；任何导致关键动作技术因疲劳变形的排序都需修正。
4. **交付**——完成标准：输出单次课动作执行序列 + 所采用的排序法说明。

**输出契约**
- 字段：`[{ order, exercise, type, 排序法 }]`。
- 约定：四种排序法之间原文无统一优先级公式，冲突时依目标与时间裁剪；superset/compound 术语有时被混用；未给体能门槛的量化界定。

## B — 边界 (Boundary)

- **不要**让 power 动作排在疲劳之后——技术会先于肌肉疲劳下降，且需靠前安排以获得最大力量适应。
- **不要**连续使用同一肌群（如连续多个拉动作）而不检查疲劳污染。
- **变量耦合**（BOOK_OVERVIEW 3.3）：顺序与休息、量、动作选择互相牵动。
- **共识 ≠ 实证**（3.3）：交替/组配法的省时收益与实践惯例相关，未给量化疲劳影响。
- 易混淆：与 **exercise-selection**（选哪些）、**rest-periods**（组间休息多长）不同——本卡只产出"先后顺序"。

## 相关能力

- 依赖（先理解）：`exercise-selection`
- 依赖（先理解）：`seven-step-program-design`
- 组合（常配合使用）：`power-exercise-phases`
