# 波动的辨识：undulating vs 传统"伪线性"周期化

## R — 原文 (Reading)

> "the term linear periodization creates a false narrative because one of the major tenets of periodization is the removal of linearity from the training process" ; "the nonlinear periodization model ... is sometimes described as an undulating or daily undulating periodization model because it involves larger daily (i.e., within the microcycle) fluctuations in the load and volume"

— Chapter 22 · Undulating Versus Linear Periodization Models（`ch22.txt` 第 736–791 行）

## I — 自述 (Interpretation)

本卡只做**术语与模型辨识**，不裁决优劣。

- 原文立场：周期化的一大要义恰恰是"**去除训练中的线性**"，故把传统模型称为 **linear periodization 是一种误称（misnomer / false narrative）**。
- 被误称的**传统模型**：各训练日**组数、次数不变**，只变负荷（如 4 组 × 6，周一 85%、周二 75%、周三 65% 1RM，重→轻结构）。但因 volume-load 在 microcycle 层波动，它**实为非线性**，不应叫 linear。
- **daily undulating（DUP / nonlinear）模型**：在 microcycle 内**同时**大幅波动负荷、量（重复数、volume-load）与训练焦点。例：周二 4×6RM（力量）、周四 3×10RM（肥大）、周六 5×3RM（爆发）。

**关于"哪个更好"，原文给不出裁决**：部分研究支持 DUP、部分显示无差异、部分显示传统更优。双方各持风险论据——DUP 派称其避免传统模型"持续递增强度累积的神经疲劳"；传统派称 DUP 的高 volume-load 带来**更多外周疲劳与伤风险**。原文**未给出择优结论**，故本卡**禁止宣称任一模型更优**，只做辨识与风险并列呈现。

## A1 — 案例 / 演练 (Application)

**原书案例（worked descriptions，`ch22.txt` 第 757–768 行）**：原书直接给出两种周内安排的对照描述。

- 输入：两种周内安排——
  - (甲) 周二 4×6RM、周四 3×10RM、周六 5×3RM；
  - (乙) 三天均 4 组 × 6，负荷分别 85% / 75% / 65% 1RM。
- 方法：检查周内是否**同时波动负荷、量与焦点**。
- 输出：甲 = **daily undulating**（周内同时波动负荷、量与焦点）；乙 = **传统模型**（各日组次不变、仅变负荷；因 volume-load 在 microcycle 波动，实为**非线性**，不应称 linear）。**原书未给这两种安排的成效对比结论（且明确其研究结论互相矛盾）。**

## A2 — 未来触发 (Trigger)

**用户会在什么情境下遇到这类问题**
1. 用户问"线性周期化 vs 非线性/波动周期化，哪个好？"
2. 用户描述了一个周内安排，问"这算 DUP 吗？"
3. 用户听人说"传统周期化就是线性"，想确认。
4. 用户看到 DUP 与传统两派的争论，想理清各自风险。

**语言信号（中英双写）**
- 中："线性还是波动周期化""DUP 是什么""传统模型是不是线性的""每日波动周期化更优吗""undulating vs linear"。
- 英："linear vs undulating periodization", "daily undulating periodization (DUP)", "is traditional periodization linear?", "which model is better".

**与相邻能力的区分（初稿）**
- 本卡只做**辨识 + 争议呈现**。选 parallel/sequential/emphasis → `cap.nsca.periodization-model-choice`；把辨识结果落成块内变量 → `cap.nsca.mesocycle-variable-filling`。

## E — 执行 (Execution)

**输入契约**
- 必需：至少一个 microcycle 内的**逐日安排**（组数、次数、负荷；是否有焦点变化）。
- 可选：运动员水平。
- 缺失处理：只有"用了波动周期化"的笼统说法 → 索取逐日组×次×负荷，否则无法辨识。
- 适用条件：用于**辨识与风险说明**，不用于择优。

**步骤**
1. 检查周内波动维度：看组数、次数（量）与负荷是否**同时**变化。完成标准：列出"逐日 组×次×负荷"。
2. 分类：
   - 若组、次、负荷、焦点**都**在周内大幅波动 → **DUP（daily undulating / nonlinear）**。
   - 若组、次**不变**、仅负荷变（重→轻）→ **传统模型**；并指出其 volume-load 在 microcycle 波动，故**应称非线性**，不应叫 linear。完成标准：给出模型名 + 依据。
3. 纠偏术语：明确"linear periodization"是原文认定的**误称**。完成标准：输出含该纠偏说明。
4. 风险并列（**不做择优裁决**）：并列呈现 DUP 派（避免累积神经疲劳）与传统派（高 volume-load → 外周疲劳/伤风险）的论据，并注明**原文承认"哪种更优"无定论**。完成标准：输出含"双方论据 + 无定论"声明，且**不得**写"X 更优"。

**判停点**：若用户要求"选一个更好的模型" → 依原文如实回答"研究结论矛盾、无定论"，**不得裁决**；可改问其训练状态/赛程以转向 `cap.nsca.periodization-model-choice` 的选型逻辑（选型 ≠ 择优）。
**输出契约**：`模型辨识 | 依据 | 术语纠偏 | 双方风险（并列）| 无定论声明`。原文未给切换条件，**不得编造**。

## B — 边界 (Boundary)

- **不要用**：把它当"择优工具"——原文明确**无定论**，任何"某模型更优"的宣称都超出原文。
- **作者警告的失败模式**：DUP 的高 volume-load → 外周疲劳、伤风险增加（`ce22-04`）；传统模型持续递增强度 → 累积神经疲劳（原文并列）。
- **原文信息不足**：`ce22-04` 仅陈述双方对立观点，**未给 DUP 过度负荷的预防做法**——本卡不得补造预防规则。
- **作者盲点（BOOK_OVERVIEW 步骤 3）**：这是**机构共识**教材对争议着墨有限（3.2）；作者本人即认定 "linear" 为误称（属立场表述）；"无定论"本身即"来源冲突"，须原样保留。
- **相邻易混**：`cap.nsca.periodization-model-choice`（选 parallel/sequential/emphasis，非 DUP/传统）。

## 相关能力

- 对比（看情境选一）：`periodization-model-choice`
- 组合（常配合使用）：`annual-plan-construction`
