# 恢复会话（recovery session）使用规范

## R — 原文 (Reading)

> "A recovery session should be just that: a session with the intentional purpose of aiding recovery beyond that achievable via passive rest" ... "It is not designed to provide an extra training stimulus and definitely should not contribute to any further muscle damage. Therefore, the recovery session should be short in duration and of a low intensity (i.e., zone 1)" ... "an extensive aerobic endurance session or long, slow distance session should not be used as a recovery run, just because it is of a low intensity."

— Chapter 21 · "Recovery From Training"（`ch21.txt` 第 365–373 行）

## I — 自述 (Interpretation)

"恢复课"是一种**以促进恢复为目的**（超过被动休息的效果）的会话，属于 active recovery。它的定义性判据有三：

1. **目的**：助恢复——**不是**提供额外训练刺激，**绝不**制造进一步肌损伤。
2. **形态**：**短时长 + 低强度**（Zone 1）。
3. **反例边界**：长距离 extensive endurance / LSD **不能**当恢复跑——哪怕它强度低。低强度 ≠ 恢复课。

**结算口径**：恢复课虽不算训练刺激，但**仍计入训练周期的总运动量**，必须纳入计划与监控。

常见误用就是把"低强度"错当成"恢复"，从而在恢复日安排过长时间，反而增加总负荷、妨碍真正恢复。

## A1 — 案例 / 演练 (Application)

**原书未提供恢复课例题**（该节为规则文章节）。以下为**明确标记的合成演练**（`_verified/E-aerobic.md` V2 walkthrough）：

- **情境**：运动员赛/高强度课后疲劳，教练计划"明天来一次 60 min 慢跑当恢复"。
- **按规则判定**：60 min 长时慢跑**不属于**恢复课（其性质量上近似 extensive endurance/LSD）→ **拒绝**该安排；恢复课应为**短时、Zone 1**（约 60–72% HRmax），且该次仍计入周总量。

## A2 — 未来触发 (Trigger)

**用户会在什么情境下遇到这类问题**
1. 高强度课/比赛后，问"明天该不该安排一次轻松跑当恢复"。
2. 把"低强度长跑"当成恢复手段，需要判断是否合规。
3. 想知道恢复课的强度/时长该定多少、算不算训练量。
4. 区分"恢复课"与"低强度有氧课"两种不同目的的课。

**语言信号（中英双写关键 trigger）**
- 中文：「恢复跑怎么安排」「恢复课是啥」「低强度跑算恢复吗」「明天慢跑 60 分钟算恢复吗」「恢复课计不计训练量」
- English: "recovery session", "recovery run", "active recovery", "should I do an easy run to recover", "zone 1 recovery", "is LSD a recovery run"

**与相邻能力的区分（初稿，阶段 3 回填）**
- 与 `aerobic-program-design-five-variables`：那张排常规训练类型；本卡专门界定恢复课这一**非训练刺激**的课。
- 与 `aerobic-progression-10pct-single-variable`：恢复课计入总运动量，会进"周总量"口径，但本卡不负责进阶规则。
- 与 `aerobic-tapering-models`：恢复课是日常处理，减量是赛前窗口。
- 与"过度训练与恢复"（Ch24）：本卡只界定恢复课，不负责疲劳状态诊断/恢复策略目录。

## E — 执行 (Execution)

**输入契约**
- 必需：① 当前疲劳水平（赛/高强度课后）；② 拟安排课的目的（助恢复 vs 训练刺激）；③ 课表位置（周内哪一天）；④ 预期总运动量。
- 缺失处理：目的不明 → 先确认是"助恢复"还是"练刺激"；若是后者则不属于本卡。

**执行步骤（四步，每步有完成标准）**
1. **确认目的**：该课须以"助恢复"为目的。完成标准：写明目的为 aiding recovery（非额外刺激）。
2. **定形态**：设**短时长 + 低强度（Zone 1，约 60–72% HRmax / 50–60% VO2max）**，确保不造成进一步肌损伤。完成标准：给出强度区与相对短时长（原文未给具体分钟数——见判停点）。
3. **排除反例**：确认该课不是 extensive endurance/LSD。完成标准：若时长/距离量级接近 LSD → **判定为不合规**并改短。
4. **计入总量并监控**：把恢复课纳入训练周期总运动量与监控。完成标准：恢复课已登记进周总量与监控表。

**判停点/分支**
- **原书未给"短"的具体分钟阈值** → 本卡只判"是否属于恢复课"（目的+Zone 1+非 LSD），**不虚构固定分钟数**；需要具体时长时按"显著短于当日训练课、且不产生疲劳"原则，标为约定。
- 若该课目的实为训练刺激 → 不按恢复课处理，转 `aerobic-program-design-five-variables`。

**输出契约**
- `{是否属于恢复课（是/否）, 目的, 强度区（Zone 1）, 时长（相对，标注约定）, 是否计入总运动量, 监控登记}`。

## B — 边界 (Boundary)

- **不要用**：当问题是要安排训练刺激的课时（用五变量卡）；当问题是赛前减量时（用减量卡）；当问题是疲劳状态判定时（属过度训练与恢复）。
- **作者警告的失败模式（核心反例）**：把长距离慢跑当恢复跑——"just because it is of a low intensity"（`ce21-03`）；在恢复日安排过长时间，造成额外肌损伤与总负荷上升。
- **盲点（BOOK_OVERVIEW 步骤 3）**：原文**未给恢复课的具体分钟数**（本卡如实标为缺口）；Zone 1 阈值来自通用五区表（跨项目迁移需校验）；共识 ≠ 实证；恢复课对总运动量的贡献易被忽略。
- **相邻易混**：`aerobic-program-design-five-variables`（低强度有氧课 ≠ 恢复课）、`aerobic-tapering-models`（赛前减量）。

## 相关能力

- 组合（常配合使用）：`athlete-monitoring-plan-design`
- 组合（常配合使用）：`overtraining-recovery-strategy`
