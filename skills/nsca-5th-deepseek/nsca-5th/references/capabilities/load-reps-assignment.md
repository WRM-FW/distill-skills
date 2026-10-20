# 按训练目标分配负荷与重复（Step 5 核心）

## R — 原文 (Reading)

> "focusing on one training goal automatically implies the use of a certain load and repetition regimen (e.g., training for maximal muscular strength involves lifting very heavy loads [i.e., ≥80% 1RM] for few repetitions [i.e., ≤6 repetitions])."

— Chapter 18 · Step 5: Relationship Between Load and Repetitions（`ch18.txt` 1236–1239）

## I — 自述 (Interpretation)

第 5 步的核心是**负荷—次数反比律**：重负荷→少次。因此**锁定一个训练目标就自动隐含了负荷×次数组合**。用两条链把"目标"变成"具体重量"：

1. **目标 → %1RM × 目标次数**（Table 18.11）：Strength ≥85% · ≤6；Multiple-effort event 75–85% · 3–5；Hypertrophy 67–80% · 8–12；Muscular endurance ≤67% · ≥12。
2. **目标次数 → %1RM**（Table 18.8 %1RM↔次数）：如 4 次≈90%、6 次≈85%、8 次≈80%、10 次≈75%、12 次≈67%。

计算三步：**由目标定最小 %1RM 门 → 由分配的目标次数在 Table 18.8 取对应百分数 → 乘（实测或估算）1RM 得具体重量 → 观察实际难易微调，并避免常规练到力竭**。

警告：%1RM–次数关系非线性且个体/动作特异（已训练者常超表值、下肢核心尤甚；小肌群可能更少；多组时需下调负荷）。辅助动作不重于 8RM；power 动作的负荷与 %1RM–次数关系**不一致**（见 power-load-assignment）。用实测 1RM 反推负荷比用次最大负荷估 1RM 更准。

## A1 — 案例 / 演练 (Application)

**原书案例（worked-example，"How to Calculate a Training Load"）**：卧推实测 1RM＝220 lb（100 kg），目标肌肉力量（需 ≥85% 1RM），分配 **4 次** → 对应约 **90% 1RM**（Table 18.8）→ 约 **200 lb（91 kg）**。原文提示按实际用力的难易微调，避免常规力竭。

**原书案例（worked-example，c18-7 Scenario A/B/C）**：A 力量/爆发目标——power 动作取估测 1RM 的 75%、other core ≥85% tested 1RM、assistance ≤8RM；B 肥大目标——67%–80%、8–12 次。**注**：B 应用表文本写"Assign 70% of the tested 1RM"，但所列负荷（deadlift 650→490、back squat 675→505 等）实按 ~75% 计——原书内部不一致，引用时应按 Table 18.11 区间自行核算。

**合成演练（标记：合成；非书中案例）**
- X：卧推 1RM＝220 lb，目标 strength，分配 4 次 → 期望 %1RM ≈90% → 负荷 ≈198–200 lb（书取整 200，容差 ±5）。
- Y：深蹲 1RM＝300 lb，目标 hypertrophy，分配 10 次 → 期望 %1RM ≈75% → 负荷 = 225 lb（容差 ±5）。

## A2 — 未来触发 (Trigger)

**用户会遇到这类问题的情境（3–5 条）**
- 用户已知目标（力量/肥大/耐力），问"每个动作该用多重、做几次"。
- 用户有 1RM（或估算值），问该乘多少百分比。
- 用户问"练力量到底是 5×5 还是 3×8""多少 %1RM 对应几次"。
- 用户想核对所排负荷是否与目标一致。
- 用户问辅助动作的负荷上限。

**语言信号（中英双写关键 trigger 词）**
- "按目标分配负荷" / "load and reps"、"load assignment"、"百分之多少 1RM"、"该做几次"、"练力量用什么负荷"、" hypertrophy 练多少 %1RM"、"目标→%1RM→次数"、"辅助动作能多重"、"卧推 1RM 220 该用多少"。
- 英文常见："what load for strength training"、"how many reps at what %1RM"。

**与相邻能力的区分（初稿）**
- 与 **one-rm-xrm-determination**：后者给基准 1RM，本卡把 %1RM×1RM 变成具体负荷。
- 与 **power-load-assignment**：power 动作的负荷**不用**本卡常规 %1RM–次数关系，另卡承载特例。
- 与 **training-volume**：本卡定"负荷×目标次数"，组数与量由后者承载。
- 与 **rpe-rir-srb-load**：无法/不愿常测 RM 时用替代法，另卡承载。

## E — 执行 (Execution)

**输入契约**
- 必需：训练目标（strength/power 多次用力项/hypertrophy/muscular endurance）、实测或估算的 1RM、分配的目标次数、动作是否 power。
- **先询问（缺失不得静默猜值）**：若**无 1RM**（实测或估算）→ 先走 one-rm-xrm-determination，不得凭感觉填重量；若无目标次数 → 由 Table 18.13 或用户指定；若动作是 power → 转 power-load-assignment；若目标缺失 → 先定目标。
- 适用条件：核心动作按 Table 18.11；辅助动作负荷不重于 8RM。

**步骤（每步有完成标准）**
1. **由目标定最小 %1RM 门**（Table 18.11）——完成标准：strength ≥85%；power(多次用力项) 75–85%；hypertrophy 67–80%；endurance ≤67%；辅助动作 ≤8RM 负荷。
2. **由目标次数在 Table 18.8 取百分数**——完成标准：目标次数与 %1RM 一一对应（4→90、6→85、8→80、10→75、12→67 等）。
3. **乘 1RM 得具体重量**——完成标准：`load = %1RM × 1RM`；舍入取整到最近 5 lb（与原文应用表一致），容差 ±5 lb（或 ±2.5%）。
4. **观察微调并留余力**——完成标准：按实际用力的难易微调；避免常规力竭。判停点：若目标次数在 Table 18.8 对应 %1RM 低于目标门（罕见），以目标门为准（取两者中不低于门者）。
5. **交付**——完成标准：输出每个动作的 `{目标, %1RM, 目标次数, 具体重量, 单位}`。

**输出契约**
- 结构：动作级 `{ goal, %1RM, goal_reps, load, unit }`。
- 数值口径：%1RM 取 Table 18.8 档位；重量取整到最近 5 lb；容差 ±5 lb。
- 已知原文不一致（不静默消失）：Scenario B 文本"70%"与所列负荷实为 ~75% 冲突，本卡以 Table 18.11 的 67%–80% 区间为准，并注明原书例值系 ~75%。

## B — 边界 (Boundary)

- **不要**用本卡的 %1RM–次数关系给 power 动作赋值——power 的负荷与其次数关系不一致，必须走特例。
- **不要**给辅助动作赋重于 8RM 的负荷——孤立应力过大。
- **不要**把 Table 18.8 当作精确定律——它是线性近似（真实为曲线），已训练者、下肢核心、单组前提都会使其失真；多组时需下调负荷。
- **不要**把练到力竭当作达成目标的手段——力竭非最大适应所必需，靠近力竭会增大 24 h 疲劳（ce18-02）。
- **变量耦合**（BOOK_OVERVIEW 3.3）：改目标或负荷会牵动量、休息与动作选择。
- 易混淆：与 **one-rm-xrm-determination**（基准）、**power-load-assignment**（特例）、**training-volume**（组数）不同——本卡只产出"负荷×目标次数"。

## 相关能力

- 依赖（先理解）：`one-rm-xrm-determination`
- 对比（看情境选一）：`power-load-assignment`
- 对比（看情境选一）：`rpe-rir-srb-load`
- 组合（常配合使用）：`chains-bands-load-calc`
- 组合（常配合使用）：`mesocycle-variable-filling`
- 组合（常配合使用）：`primary-training-goal`
- 组合（常配合使用）：`rest-periods`
- 组合（常配合使用）：`training-volume`

## 配套资源

路径相对于本文件；脚本需先检查运行条件，不因附带而自动执行。

- [resources/load-repetition-table.md](../../resources/load-repetition-table.md)
- [resources/load-volume-rest-assignment.md](../../resources/load-volume-rest-assignment.md)
