---
name: nsca-periodization
description: |
  当用户要"设计一套周期化/年度训练计划"或提到 periodization/annual plan/season planning 却不知从何入手时用：按九步整合流程产出「macrocycle→四赛季区间→mesocycle 列表→每周变量取值→测试节点→卸载周→竞赛期打法」。输入需竞赛日程、赛季数、关键比赛与已测 RM；任一关键输入缺失先问、不静默猜值。关键 trigger：design a periodized program、annual training plan、season planning、周期化总流程。红线：原文认定 linear periodization 是误称、且 DUP 与传统模型孰优无定论——不得宣称任一模型更优。仅限有赛季的竞技计划，不用于无赛季人群或单次课微调。
metadata:
  cangjie.generated-by: cangjie-tools v2.5.0
  cangjie.capability-id: cap.nsca.periodization
  cangjie.capability-revision: 1
  cangjie.bundle-id: bundle.nsca-5th
  cangjie.source-title: Essentials of Strength Training and Conditioning, 5th Edition
  cangjie.tags: procedure, periodization, program-design
---
# 周期化与年度计划编排（总纲）

## R — 原文 (Reading)

> "Periodization is the logical and systematic process of sequencing and integrating training interventions in order to manage the training process and to increase the potential of achieving peak performance at appropriate time points."

— Chapter 22 · Central Concepts Related to Periodization（`ch22.txt` 第 102–105 行）

## I — 自述 (Interpretation)

这是把簇 B 十个单元串成**一条可用流程**的伞形能力：从"分层"到"排年度"再到"填块、卸载、峰值"。八步骨架：

1. **分层**：periodization（宏观框架）≠ programming（微观内容）；用三级流程 periodization→planning→programming 建立，上层缺输入不往下推。
2. **选模型**：据训练状态与赛程选 **parallel / sequential / emphasis** 之一。
3. **定层级与时长**：multi → annual → macrocycle → mesocycle（2–6 周，默认 4）→ microcycle（默认 1 周）→ day → session。
4. **映射季节**：off→preparatory、preseason→first transition、in-season→competitive、postseason→second transition；焦点由"高量低强/一般"渐移向"低量高强/专项"，且 **preseason 不是建基础期**。
5. **排年度**：把 macrocycle 切成 2–4 周的 mesocycle，标相位、钉测试节点、放卸载周。
6. **填块**：用 Table 22.3 档位给每块定强度/量/组次，再用运动员 RM 落到具体重量（换算调用 `cap.nsca.load-and-repetition`）；周五 -10%、热身 3–5 组不计入。
7. **理论定调**：GAS 判是否滑向衰竭；SFR 解释负荷-恢复；体能—疲劳说明"减量可抬高备战状态"→ 据此安排卸载周。
8. **竞赛期分派**：短窗 peak（~1–2 周）、长赛季 maintain（microcycle 级调制）。

## A1 — 案例 / 演练 (Application)

**原书案例（sample-program，Figure 22.8 · c22-1，Ch22 "Example of an Annual Training Plan"）——全书唯一完整年度计划样例**：

- 输入：女性大学篮球中锋，单赛季；macrocycle = 5/1–次年 4/28。
- 结构：四赛季（off 5/1–8/20、preseason 8/21–11/5、in-season 11/6–4/14 含 4 周锦标赛、postseason 4/15 起）+ **14 个 mesocycle（每个 2–4 周）**；逐周期给出组×次与 %RM（如 Mesocycle 3 用 80%–84%/85%–89%/90%–94% 5RM 三周阶梯；Mesocycle 12 悬垂高翻 1×3、前蹲 1×5 @75%–89% 5RM）。
- 输出：跨度整年的逐中周期抗阻处方，含预测试周（5RM/3RM/2RM 核心、10RM/8RM 辅助）与卸载周；赛内以维持/峰值处理并附锦标赛周方案。
- **原书未说明该运动员的实际训练成效**（样例仅用于"说明如何细分年度计划并设计抗阻成分"）。

## A2 — 未来触发 (Trigger)

**用户会在什么情境下遇到这类问题**
1. 用户要"设计一套周期化/年度训练计划"，从零到可执行。
2. 用户已有一堆碎片决策（选模型、定块长、排赛季、填重量），想要一条整合流程。
3. 用户问"整个训练年应该怎么组织、什么时候减、什么时候 peak？"
4. 用户提到 periodization / macrocycle / 年度计划 / 赛季编排等词，但不知从哪一步入手。

**语言信号（中英双写）**
- 中："设计周期化计划""年度训练计划怎么搭""赛季怎么编排""什么时候卸载/峰值""周期化总流程"。
- 英："design a periodized program", "periodization plan", "annual training plan", "season planning", "macrocycle/mesocycle layout".

**与相邻能力的区分（初稿）**
- 本卡是**整合入口**；若已明确只需某一步，路由到对应子卡：分层 → `cap.nsca.periodization-three-level-build`；选模型 → `cap.nsca.periodization-model-choice`；层级时长 → `cap.nsca.periodization-cycle-durations`；季节映射 → `cap.nsca.season-to-period-mapping`；年度排布 → `cap.nsca.annual-plan-construction`；块内变量 → `cap.nsca.mesocycle-variable-filling`；机制理论 → `cap.nsca.periodization-mechanistic-theories`；峰值/维持 → `cap.nsca.peaking-vs-maintenance`；赛内排布 → `cap.nsca.in-season-load-management`；波动辨识 → `cap.nsca.undulating-vs-traditional-identification`。

## E — 执行 (Execution)

**输入契约**
- 必需：竞赛日程（四赛季区间，YYYY-MM-DD）；赛季数（单/多赛季）；关键比赛/锦标赛时点；运动员**已测 RM 或 1RM**（用于落值）。
- 可选：训练状态（判定 parallel/sequential/emphasis 与档位）、可用训练日/周、监测数据、非训练压力信息。
- 缺失处理：无赛程 → 先问；无训练状态 → 可完成步骤 1–3、5，步骤 2 与 6 的档位标注"待补"；**无 RM → 不得猜重量**，先安排测试周。任何一步缺关键输入都**不得静默猜值**。

**步骤（每步含完成标准）**
1. **分层**：写清 periodization（框架）与 programming（内容）之别，按三级流程产出"框架 → 选模型 → 落地 modes"。完成标准：三层各有交付物。（见 `cap.nsca.periodization-three-level-build`）
2. **选模型**：据训练状态 + 赛程密度在 parallel/sequential/emphasis 中选一并写依据与风险。完成标准：模型名 + 依据 + 局限。（见 `cap.nsca.periodization-model-choice`）
3. **定层级与时长**：annual/macrocycle（单赛季=1）/mesocycle（**2–6 周，默认 4**）/microcycle（**默认 1 周**）。完成标准：各周期时长与块数，总和与年度周数吻合（容差 1 周）。（见 `cap.nsca.periodization-cycle-durations`）
4. **映射季节**：off→preparatory、preseason→first transition、in-season→competitive、postseason→second transition，并标各期焦点；确认 **preseason 不建基础**。完成标准：季节↔时期↔焦点表无遗漏。（见 `cap.nsca.season-to-period-mapping`）
5. **排年度**：把 macrocycle 切成 2–4 周 mesocycle，标相位，钉测试节点（off 起始 + 赛季后段），在块间/关键赛前置**卸载周**。完成标准：整年无未定义周；卸载周与测试节点均有日期。（见 `cap.nsca.annual-plan-construction`）
6. **填块**：查 **Table 22.3**（`resources/periodization-model-table.md`）取相位档位（强度/量/组×次），再用 RM 落到 kg；**周五课 = 周一 ×0.90**（preseason 可 ×0.85）、**热身 3–5 组不计入目标组**；赛内改用 %RM 区间、不力竭。完成标准：每块有相位 + 每周 kg + 组×次；重量换算调用 `cap.nsca.load-and-repetition`。（见 `cap.nsca.mesocycle-variable-filling`）
7. **理论定调与卸载**：用 GAS 判是否滑向衰竭、用体能—疲劳说明"减量抬高备战状态"，据此确认卸载周；核查非训练压力。完成标准：卸载周有理论依据；若提示衰竭风险 → 优先卸载/转诊。（见 `cap.nsca.periodization-mechanistic-theories`）
8. **竞赛期分派**：短窗 → peak（~1–2 周、50%–≥93% 1RM、1–3×1–3）；长赛季 → maintain（85%–93% 1RM、~2–5×3–6、microcycle 级调制）；长赛季用 3–4 周块、末周卸载。完成标准：竞赛期打法与赛季长度匹配。（见 `cap.nsca.peaking-vs-maintenance`、`cap.nsca.in-season-load-management`）
9. **自检**：术语纠偏——**不得把传统模型称为 linear periodization**（原文认定其为误称）；**不得宣称某种周期化模型更优**（见下 B 段）。

**判停点/分支**
- 步骤 2 训练状态未知 → 停，交付"框架 + 待补"。
- 步骤 6 无 RM → 暂停落值，先测。
- 步骤 7 提示衰竭相 → 转"卸载 + 非训练压力核查"分支。
- 各步骤均可单独路由到对应子卡。

**输出契约**：整合交付 = `macrocycle → 四赛季区间 → mesocycle 列表（起止/周数/相位/microcycle 数）→ 每周变量取值（强度/量/组×次/kg）→ 测试节点 → 卸载周 → 竞赛期打法`。数值取自 Table 22.2/22.3（见 `resources/periodization-model-table.md`）；原书未给统一模板，本结构为**约定**。
**原文歧义（如实标注）**：`ch22.txt` 第 798 行 preseason 作 "August 21-November 5"，第 852 行作 "11 weeks (August 21-October 5)"；本卡采用与 in-season 起始衔接的 **11/5**。样例强度记法"80%-84% 5RM"存在"%RM 负荷 / %1RM"两种解读，本卡统一按"> 目标 RM 负荷的百分比"复算（5RM=120 kg → 0.80×120=96 kg）。

## B — 边界 (Boundary)

- **不要用**：无赛季的健康/康复人群；单次课或单周微调。本卡是**竞技计划层**工具。
- **必须写明且不得违反的原文立场**：
  - 原文自认 **"linear periodization" 是 misnomer / false narrative**（周期化的要义正是"去除线性"）；本卡**禁止**把传统模型称作 linear。
  - 关于 **DUP（波动）与传统模型"哪种更优"，原文明确无定论**（研究结论互相矛盾）。本卡**禁止宣称任一模型更优**，只做辨识与风险并列。
- **作者警告的失败模式**：峰值期 >1–2 周（`ce22-01`）；第二过渡期 >4 周（`ce22-02`）；减量过度致体能同降（`ce22-03`）；DUP 过度负荷（`ce22-04`，原文无预防做法，不得补造）；单调/过度变化 → 衰竭（`ce22-05`）。
- **作者盲点（BOOK_OVERVIEW 步骤 3）**：常模/处方的**时效与人群依赖**（3.1，竞技人群偏向）；**共识≠实证**（3.3-5）；**迁移不保证**（3.3-1，即体能改善未必等于专项表现）；**变量耦合**（3.3-3）；**教练专业边界**（2.2-14，医疗/心理越界应转诊）；**法域语境**（3.2，管理议题不跨法域照搬）。
- **组织前提**：本流程的成效依赖"运动教练与体能教练共同规划、共享目标"（`ch22.txt` 第 899–905 行）；该命题为规范主张、无可执行步骤，仅作**实施前提**提示，非独立能力。
- **相邻易混**：Ch18 的负荷/重复换算（`cap.nsca.load-and-repetition`，簇 A）、Ch24 的过度训练识别与恢复（簇 H）。

## 相关能力

- 组合（常配合使用）：`nsca-aerobic-endurance-design`
- 组合（常配合使用）：`nsca-overtraining-recovery`
- 组合（常配合使用）：`nsca-resistance-program-design`
- 组合（常配合使用）：`seven-step-program-design`

## 配套资源

路径相对于本文件；脚本需先检查运行条件，不因附带而自动执行。

- [resources/periodization-model-table.md](resources/periodization-model-table.md)
