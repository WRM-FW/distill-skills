# 护腰（weight belt）使用判据

## R — 原文 (Reading)

> "It is recommended that a weight belt be worn for exercises that place stress on the lower back and during sets that use near-maximal or maximal loads. Adopting this strategy may reduce the risk of lower back injury when combined with proper lifting and spotting techniques. A drawback to weight belt use is that wearing a belt too often reduces opportunities for the abdominal and lower back muscles to be trained. Furthermore, no weight belt is needed for exercises that do not stress the lower back ..."

— Chapter 16 · Weight Belts（`ch16.txt` 第 190–210 行）

## I — 自述 (Interpretation)

护腰的作用是**在负重时帮助维持腹内压**，但它**不是逢练必戴**。原文给的是**双条件判据**，两条**同时满足**才建议佩戴：

1. **该动作对下背施加应力**（如 back squat、deadlift）；且
2. **该组用接近最大 / 最大的负荷**。

只要有一条不成立就不戴：不压迫下背的动作（如 biceps curl、lat pulldown）**不需要**；即便压迫下背、但**轻负荷**也**不需要**。

作者点名一个**代价（drawback）**：**腰带戴得太频繁，会减少腹部与下背肌群的训练机会**——即护具在帮你分担负荷的同时，也剥夺了核心肌群自我支撑的刺激。因此判据的实质是"**只在真正需要外部支撑的高负荷时用它**"，把其余场合留给核心自己练。

## A1 — 案例 / 演练 (Application)

**合成演练（标记：合成；非书中案例）**：
- 情形 A：杠铃弯举 4×8RM。该动作**不给下背施压**（条件 1 不满足）→ **不戴腰带**。
- 情形 B：后蹲 3×3 @ 90% 1RM。该动作**压迫下背**（条件 1 满足）且**接近最大**（条件 2 满足）→ **戴腰带**。
- 情形 C：后蹲 3×10 @ 60% 1RM。压迫下背但属**轻负荷**（条件 2 不满足）→ **不戴腰带**。
- **原书未说明**这些合成输入的实测结果；原文只给判据与 drawback。

## A2 — 未来触发 (Trigger)

**用户会在什么情境下遇到这类问题**：
1. 用户问"这个动作要不要戴腰带/护腰"。
2. 用户问"是不是所有动作都该戴""戴腰带会不会伤身/依赖"。
3. 用户问轻重量深蹲、或者器械动作要不要戴腰带。
4. 用户想知道戴腰带会不会影响核心训练。
5. 用户描述自己"每次训练都戴腰带"，问是否合理。

**情境的语言信号（中英双写关键 trigger 词）**：护腰 / 腰带 / weight belt / lifting belt / 要不要戴腰带 / 深蹲戴不戴 / 腰带有依赖吗 / 戴腰带核心会不会变弱 / 大重量才戴吗 / 硬拉护腰 / 买不买腰带。

**与相邻能力的区分（初稿）**：本卡只产出**戴/不戴的判据**。**呼吸与 Valsalva**（与护腰配合的躯干支撑）属 `exercise-technique-basics`；**保护者与失杠**属 `spotting-rules`；**大重量动作的具体技术**属 `power-exercise-phases`/`technique-error-correction`。

## E — 执行 (Execution)

**输入契约**
- 必需：**动作名称**（用于判断是否对下背施压）、**该组相对负荷**（%1RM 或 RM 档）。
- 可选：训练目标（是否要发展核心）、运动员训练状态。
- **缺失"相对负荷"应先询问**；不得因动作看起来"大"就默认戴。

**步骤（每步可判断完成标准）**
1. **判条件 1——是否给下背施压**：结构性/髋铰链类（squat/deadlift 等）下背受累；弯举、下拉等**不压迫下背**。
   - 完成标准：给出"是/否"。
   - **判停点**：若"否" → **不戴**，结束。
2. **判条件 2——是否接近最大/最大负荷**：按负荷档判断。
   - 完成标准：给出"是/否"。
   - **判停点**：若"否"（轻负荷）→ **不戴**，结束。
3. **两条件均满足 → 建议戴**；并提示 drawback（别戴过头，留核心训练机会）。
   - 完成标准：输出"戴"+ 依据（两条件）+ drawback 提示。
4. **交付**：见输出契约。

**量化阈值（关键约定，原文缺）**
> **原文未给 "近最大/最大负荷" 的量化阈值**（`ch16.txt` 只写 "near-maximal or maximal loads"，未给 %1RM），也未量化"轻负荷"。判据对清晰情形可执行，但**模糊区**（如后蹲 70% 1RM）无法自动裁定。

- **本卡采用的口径（约定，非原文规定）**：以**"结构性/压迫下背动作 + ≥80% 1RM"** 作为可建议戴腰带的默认阈值；低于该阈值（或非下背动作）默认不戴。
  - 依据与旁证：`ch17.txt` 第 53–55、101–103 行对同类躯干支撑问题使用 **"loads greater than 80% of maximal voluntary contraction or lighter loads to failure"** 的 80% 口径；跨章取用**仅为约定**。
  - **此阈值是约定，不是原文规定**；模糊区应显式标注不确定性（如"70% 1RM 后蹲处于约定边界附近，本卡默认不戴并说明可个案判断"），不得冒充原文。
- 另一**已知边界**：原文未量化"如何算下背受应力"（除举例外），本卡以"是否加载脊柱/髋铰链"为操作性判断，属实现约定。

**输出契约**
- 字段：`{ exercise, stresses_lower_back(bool), load_band(%1RM|RM), near_maximal(bool), decision(戴|不戴), rationale, convention_note }`。
- 完成标准：decision 与两条件一致；凡涉及数值阈值，`convention_note` 必须标明"约定，非原文"。
- 单位：%1RM 或 RM 档。

## B — 边界 (Boundary)

- **不要**逢练必戴：作者明确 drawback——过度佩戴**减少腹部与下背肌群的训练机会**（`ce16-03`）；本卡判据即为此设。
- **不要**对不压迫下背的动作、或轻负荷动作建议佩戴（原文"no weight belt is needed..."）。
- **不要**把"80% 1RM"当原文规定引用——原文**未给量化阈值**；该数值是本卡约定（借自 ch17 的相近口径），模糊区须保留不确定性。
- **不要**用护腰替代技术/保护：原文强调它是"**combined with proper lifting and spotting techniques**"才可能降低下背伤风险，护具不是安全兜底。
- **共识 ≠ 实证**：阈值与"降低下背伤风险"的表述来自实践惯例与文献推断，非硬证据；个体（腰椎状况）差异大。
- **医学边界**：已有腰椎伤病者是否使用属医疗判断，本卡不越界，必要时转诊。
- **相邻易混**：把"呼吸/Valsalva"或"保护人数"混入本卡。

## 相关能力

- 组合（常配合使用）：`exercise-technique-basics`
- 组合（常配合使用）：`one-rm-xrm-determination`
