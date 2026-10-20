# 训练状态分类（beginner / intermediate / advanced）

## R — 原文 (Reading)

> "Table 18.1 provides an example of how such information might be used to classify athletes' training status as beginner, intermediate, or advanced. The strength and conditioning professional should realize that the three classifications exist on a continuum and cannot be definitively demarcated."

— Chapter 18 · Step 1: Training Status / Table 18.1（`ch18.txt` 306–309）

## I — 自述 (Interpretation)

训练状态是本书几乎所有处方表的**查表键**——同一张频率/量/1RM 资格表，在三档下读法不同。判定它要结合"训练经历 + 当前能力"，共六个观察维度：

- 当前是否在训练（current program）
- 训练年龄（training age，月/年）
- 每周频率（frequency per week）
- 训练应激（training stress，即该抗阻计划对身体的需求/刺激程度）
- 技术与经验熟练度（technique experience and skill）
- 既往训练背景四维（项目类型、近期规律参与时长、既往强度、技术经验）

把六维对照 Table 18.1 即得档位：Beginner（未训练）＝未训练/刚开始、<2 个月、≤1–2 次/周、无/低应激、无/极少技术；Intermediate＝正在训练、2–6 个月、≤2–3 次/周、中应激、基础技术；Advanced＝正在训练、≥1 年、≥3–4 次/周、高应激、高技术。**关键提醒**：三档是连续谱，无法硬性切分；同为某项目运动员也可能终生只是 intermediate（如因赛季低频低应激，许多欧洲足球运动员难达 advanced）。信号跨档时按连续谱取保守档。

## A1 — 案例 / 演练 (Application)

**原书案例（tabular-example，c18-2 / Table 18.1）**：原书用 Table 18.1 把三情境分类——Scenario A（女 20 岁大学篮球中锋，自高中起抗阻训练、习惯大负荷、动作熟练）与 B（男 28 岁职业橄榄球锋线，同样资深）判为 **Advanced**；Scenario C（男 17 岁高中越野跑者，赛季前 4 周才开始抗阻、训练有限、技术未成熟）判为 **Beginner**。原书强调三档在连续谱上、无法截然划分。

**合成演练（标记：合成；用于演示取保守档规则，非书中案例）**
- 输入：22 岁业余足球运动员，赛季中每周仅 2 次抗阻、负荷中低、动作技术一般，训练年龄 3 年。
- 执行：逐维对照 Table 18.1——频率 2（落在 intermediate 的 ≤2–3）；训练年龄 3 年（≥1 年 vs. 2–6 月的中间地带）；技术一般；应激中。信号跨 beginner/intermediate/advanced 边界。
- 预期输出：按连续谱取 **conservative 档 = Intermediate**（与原文"欧洲足球运动员因赛季低频低应激常难达 advanced"口径一致）。原书未说明该合成输入的"实际结果"，此处为按规则复算。

## A2 — 未来触发 (Trigger)

**用户会遇到这类问题的情境（3–5 条）**
- 用户给出一名运动员，问"他算新手还是有经验/高级"以便选频率、量或能否测 1RM。
- 用户要用一张频率表或量分配表，但不知道该按哪一档读。
- 用户描述训练史时信号矛盾（练了很久但频率低/应激低）。
- 用户想确认"资历很深的专项运动员是不是就是 advanced"。
- 用户在比较两名运动员该不该用同一张表的同一行。

**语言信号（中英双写关键 trigger 词）**
- "这算 beginner 还是 intermediate/advanced" / "training status"、"beginner"、"intermediate"、"advanced"、"training age"、"训练年龄"、"训练应激"、"技术经验"、"他练了多久"、"每周练几次"、"能测 1RM 吗"、"is this athlete trained enough"。
- 英文常见："classify this athlete's training status"、"is he advanced"。

**与相邻能力的区分（初稿）**
- 与 **needs-analysis**：本卡是需求分析第 2 阶段的一个子步骤（训练状态）；需求分析另卡承载整体两阶段流程与运动评估。
- 与 **training-frequency / training-volume**：本卡只给"档位"，频率/量是据此查表取值，另卡承载。
- 与 **one-rm-xrm-determination**：本卡决定 1RM 测试资格，测试本身另卡承载。

## E — 执行 (Execution)

**输入契约**
- 必需：当前是否在训练；训练年龄（月或年）；每周抗阻频率；训练应激（无/低·中·高）；技术经验熟练度（无/极少·基础·高）。
- 可选：既往项目类型/时长/强度。
- **先询问（缺失不得静默猜值）**：若训练年龄未知 → 问"规律抗阻训练多久了（月/年）"；若频率未知 → 问"每周几次"；若技术熟练度未知 → 问"动作是否熟练/有无教练纠正"；若应激未知 → 需结合负荷与量判断，不得默认。
- 适用条件：任何抗阻训练者；连续谱判定。

**步骤（每步有完成标准）**
1. **收集六维信号**——完成标准：五维输入（当前训练、训练年龄、频率、应激、技术）+ 既往背景均已标注，缺失项已询问。
2. **对照 Table 18.1 逐维判档**——完成标准：给出每维落在哪一档：
   - Beginner：未训练/刚开始｜<2 月｜≤1–2/周｜无/低｜无/极少
   - Intermediate：正在训练｜2–6 月｜≤2–3/周｜中｜基础
   - Advanced：正在训练｜≥1 年｜≥3–4/周｜高｜高
3. **跨档裁决**——判停点：若各维信号不齐（部分指示高、部分指示低）→ 按**连续谱取保守档**并注明需观察期；若一致则直接定档。
4. **交付**——完成标准：输出单一档位 `beginner | intermediate | advanced`，并附"三档为连续谱"的说明。

**输出契约**
- 字段：`{ training_status: beginner|intermediate|advanced, 依据维度, 是否跨档说明 }`。
- 容差/舍入：无计算；档位为定性类别。
- 约定：原文未给量化评分法，各维阈值依赖专家判断；本卡不得用"出现频次"代替重要性来定档。

## B — 边界 (Boundary)

- **不要**把三档当作可按数字硬切分的固定边界——原文明确"exist on a continuum and cannot be definitively demarcated"。
- 不要因"资历深"就直接判 advanced：赛季低频低应激可让资深运动员终生仅 intermediate。
- **常模/人群依赖**（BOOK_OVERVIEW 3.1）：档位是查表键，但其下游的频率/量表有年代与人群前提，跨语境需校验。
- **共识 ≠ 实证**（3.3）：档位由专家判断构成，非精确量表；应与个体实际响应结合。
- 易混淆：与 **needs-analysis**（整体流程）、**training-frequency**（按档查表定次数）、**exercise-selection**（按经验选进阶/回归）不同——本卡只产出"档位"这一个交付物。

## 相关能力

- 依赖（先理解）：`needs-analysis`
- 组合（常配合使用）：`maturity-assessment-phv`
- 组合（常配合使用）：`one-rm-xrm-determination`
- 组合（常配合使用）：`training-frequency`
- 组合（常配合使用）：`training-volume`
- 组合（常配合使用）：`youth-resistance-training`
