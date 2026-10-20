# 过度训练/过度劳累的定义与过度训练连续谱判定（FOR → NFOR → OTS）

## R — 原文 (Reading)

> "An important aspect of this definition that was also clarified in these position stands is that overtraining is actually the process (e.g., excessively high volumes and intensities of training) that then can result in an overtraining syndrome (i.e., the collection of symptoms and performance impairments) (88, 89). To be overtrained, one actually has the OTS and the required long-term performance impairments (i.e., weeks to months or longer). Performance impairments are necessary for overtraining to have occurred."

— Chapter 24 · Overtraining Defined（`ch24.txt` 第 205–214 行）

## I — 自述 (Interpretation)

这一节把"练过头"从一个混沌的直觉，拆成**过程 vs 结果**两条轴，再拼成一条连续谱：

1. **过载是过程，综合征是结果**：`overtraining (OT)` 指训练/非训练应激累积的**过程**；`overtraining syndrome (OTS)` 指这个过程造成的结果（一组相互关联的生理/心理症状 + 成绩受损）。判定"过度训练"的**必要条件**是出现长期成绩下降。
2. **用恢复时长切档**（ECSS-ACSM 共识）：
   - `overreaching (OR)`：短期降成绩，**数天到数周**恢复。
   - `OT/OTS`：长期降成绩，**数周到数月或更久**恢复。
3. **OR 内部再分两支**：
   - `FOR`（功能性过度疲劳）：有计划的短期超负荷，恢复后出现**超量恢复**（表现超过基线）——这是**可用的训练工具**。
   - `NFOR`（非功能性过度疲劳）：累积疲劳更大、恢复更久，**无超量恢复**，只能回到基线——无益且白白让运动员受压。
4. **OTS 再按自主神经反应分型**：`SOTS`（交感型，抗阻/力量功率训练更常见，儿茶酚胺反应增强）与 `POTS`（副交感型，耐力/大训练量者更常见，静息心率下降、交感反应减弱）。
5. **最轻的一档是"成绩停滞"**：既有训练者本就会周期性平台，它**难以**与好训练区分，除非确认由不当负荷引起，才需调整。

判定的落点不是"他练得苦不苦"，而是：**成绩是否下降 + 恢复需要多久 + 恢复后是超量还是仅回基线**。

## A1 — 案例 / 演练 (Application)

**原书案例（in-book-athlete-scenario · c24-3，`ch24.txt` 第 341–356 行）**：许多项目的**赛前训练营**（一日 2–3 练）或一般准备训练块，就是有计划的短期超负荷。原文结论：短期表现下降，但"recovery can be attained within days or weeks and can result in a supercompensation effect"——属 **FOR**。**原书未说明具体某名运动员的实际结果**（仅作为 FOR 的范式情境）。

**合成演练（明确标记，按原书规则复算）**：某短跑运动员在赛前训练营（一日两练）后成绩下降 8%；撤量 1 个减量周后，第 10 天成绩**超过**营前基线并创个人最好成绩。
- 判定路径：成绩下降 ✓ → 恢复时长 = 数天~数周 → 命中 OR 档；恢复后**超量恢复** → 命中 **FOR**。
- 反例校验：若同一情境撤量后第 10 天仍只回到基线、无超量 → 应为 **NFOR**；若数周仍有持续成绩损害、且伴 SOTS/POTS 自主神经症状 → 升级为 **OTS**。

## A2 — 未来触发 (Trigger)

**用户情境**：
1. 问"这算练过头了吗 / 是过度训练还是正常的减量超量？"——要区分 FOR/NFOR/OTS。
2. 训练营或大负荷块之后成绩掉了，担心是不是"训练过度"。
3. 要把"过度疲劳、过度训练、过度训练综合征"这些词的分界讲清楚。
4. 需要据此估计"要多久才能恢复"（天数/周数/月数）。

**语言信号（中英双写）**：过度训练 / 过度疲劳 / 过度劳累 / 功能性过度疲劳 / 非功能性过度疲劳 / 过度训练综合征 / 练过头 / 超量恢复 / overtraining / overreaching / OTS / FOR / NFOR / SOTS / POTS / supercompensation / "how long to recover"。

**与相邻能力的区分（初稿）**：本卡只做**分档命名与连续谱定位**（这是哪种？多严重？）。若问题是"到底是过度训练还是训练不足/时机错配/生活压力"→ 路由 `cap.nsca.underperformance-attribution-triage`（归因）。若已确认 OT 要选恢复手段 → `cap.nsca.overtraining-recovery-strategy`。若问监控怎么建 → `cap.nsca.athlete-monitoring-plan-design`。**与"周期化"不同**：那是"怎么把过载编排成计划"（计划编排），本卡是"计划已出问题后怎么命名与分级"；**与"测试与评估"不同**：那是"怎么测、测得准不准"（测量），本卡是"测出来的下降属于哪一类"。

## E — 执行 (Execution)

**输入契约（必需）**：
- 成绩变化：方向（升/降）与幅度（%，相对本人近期基线）；观测时间窗（天/周）。单位：`%`、`天/周`。
- 恢复结局：撤销或大幅降低训练应力后，成绩是**超量**还是**仅回基线**，以及恢复耗时。
- 自主神经线索（可选但用于分型）：静息心率、对训练的交感反应、情绪/恢复感变化。
- 训练与非训练背景：近期负荷是否显著升高、有无生活/工作/睡眠应激（allostatic load）。
- **缺失处理**：若"恢复结局"或"恢复耗时"未知 → 只能给出**暂定档位 + 待观察**，并注明"需撤量后复测才能定 FOR/NFOR"；**不得**在仅有"成绩下降"一点时就下 OT/OTS 结论。

**步骤与完成标准**：
1. **确认前提**：是否存在成绩下降、且是否有长期损害的必要条件。完成标准：写明观测窗口与基线口径（否则标"待补"）。
2. **按恢复时长切 OR vs OT/OTS**：数天~数周 = OR；数周~数月或更长 = OT/OTS。完成标准：给出一档 + 依据的恢复时长。
3. **OR 内判 FOR / NFOR**：撤量后出现超量恢复 = FOR（可用工具）；仅回基线、无超量 = NFOR。完成标准：写明"超量/仅回基线"证据。
4. **OTS 分型（仅在疑似 OT 时）**：交感型（儿茶酚胺反应增强，抗阻/功率常见）= SOTS；副交感型（静息 HR 下降、交感反应减弱，耐力/大训练量常见）= POTS。完成标准：给出 SOTS/POTS 判定或标"未分型"。
5. **排除"成绩停滞"误纳**：若仅平台期、无法归因于不当负荷 → 不判为 OT/OR，标"可能为正常平台"。完成标准：明确说明理由。
6. **输出分档结论**。

**输出契约**：`{前提成立与否, 档位(FOR|NFOR|OTS), 严重度, 恢复时长预期, 分型(SOTS|POTS|未分型), 证据与缺口}`。
**约定与容差**：原文**未给任何精确切点**（如"下降 X% 即 NFOR"），档位由**恢复时长 + 是否超量恢复 + 症状**三条定性判据共同决定。本卡不虚构数值阈值；`%` 变化仅作记录。恢复时长量级取自 `ch24.txt` 第 936–939 行（超量约 1 周；重度过训练抗阻可达约 4 周、大容量长跑数月至一年）。

**判停点/分支**：
- 步骤 1 输入不足 → 停，输出"暂定 + 待复测"。
- 步骤 3 无法区分超量/仅基线 → 标 NFOR 待定，不冒认 FOR。
- 步骤 4 出现自主神经异常或疑似 RED-S/抑郁等共病 → **不自行处置**，转 `cap.nsca.rehab-scope-and-referral` 的转诊路径（原文明确需专业人员介入）。

## B — 边界 (Boundary)

- **不要**把"练得苦""一次成绩下降""某次没练好"判为 OT/OTS——原文反复强调 OTS 需**长期**成绩损害。
- **不要**把 FOR 当坏事：FOR 是**可用训练工具**，误判为 OTS 会导致不必要的大幅减量。
- **原文自认的核心局限（B 段主依据）**：`ch24.txt` 第 39–46、398–410 行明言 this is a "complex and often confusing phenomenon"、"our understanding … is far from complete"、需要更多研究；共识定义本身是**专家共识**，不是从机制推出的定律（BOOK_OVERVIEW 3.3-5 共识≠实证）。
- **切点缺失**：OT/OR 之间、FOR/NFOR 之间**无精确数值切点**，且原文承认类别间 "some overlap may exist"。本卡**禁止**编造阈值。
- **因果方向难辨**：OTS 的次要因素（生活压力等）**既可能是因，也可能是 OTS 的果**（`ch24.txt` 第 481–486 行）——同一份证据可有两解。
- **专业边界**：本卡是命名/分级框架，**不**用于诊断疾病；疑似 RED-S、抑郁、PTSD 等与 OTS 共享症状的状态须转诊（`ch24.txt` 第 369–384 行）。
- **变量耦合**：恢复时长受训练类型（抗阻 vs 耐力）、量/强度口径影响，不可跨情境照搬一个时长。
- **相邻易混**：`cap.nsca.underperformance-attribution-triage`（先排查是否真是 OT）、`cap.nsca.overtraining-recovery-strategy`（命名后的处置）。

## 相关能力

- 组合（常配合使用）：`periodization-mechanistic-theories`
- 组合（常配合使用）：`underperformance-attribution-triage`
