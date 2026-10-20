# 成绩下降归因排查（并非所有成绩下降都是过度训练）

## R — 原文 (Reading)

> "In summary, not all cases of underperformance are due to overtraining or overreaching (figure 24.11). … One common training error that can be mistaken for overtraining is due to the timing of the training program with the competition schedule. … At first glance, overtraining may be blamed for the underperformance, but the reality is that inappropriate timing, not excessive training, was the cause."

— Chapter 24 · Underperformance and Its Relation to Overtraining and Overreaching（`ch24.txt` 第 517–539 行）

## I — 自述 (Interpretation)

这是本簇的"分诊台"：**先别急着说练过头**。原文把"成绩下降"当成一个**多因**问题，各因**单独或叠加**都可能致因：

1. **过度训练/过度疲劳本身**（真因之一，不是默认答案）。
2. **训练峰值与比赛日程错配**——计划设计得再好，若 peak 没落在"需要出成绩"的时点，成绩照样差；这是**时机**问题，不是过量问题。
3. **训练不足**——负荷不够 → 成绩次优。
4. **非训练压力（allostatic load）**——生活、工作、家庭、旅行、时区、月经周期、年龄、伤史等，全部汇入同一个"适应负荷池"。
5. **营养 / 睡眠 / 疾病**——补能、睡眠不足、疾病同样压低表现。

原文用 Figure 24.11/24.12 区分**直接原因（实线）**与**贡献因素（虚线）**，并**明确承认因果方向难辨**：某些"贡献因素"也可能是 OTS 造成的（互为因果）。所以排查目标是**列出并列候选、逐项找可核查证据**，而不是抢先锁定"过度训练"。

## A1 — 案例 / 演练 (Application)

**原书案例（in-book/反面教材 · ce24-01 与 Figure 24.13，`ch24.txt` 第 532–539 行）**：一个为提升成绩设计良好的计划，因**训练峰值未与运动员需要出成绩的时点重合**而失效。原文点破："At first glance, overtraining may be blamed … but the reality is that inappropriate timing, not excessive training, was the cause." **原书未给具体队伍成绩数据**。

**合成演练（明确标记）**：某接力队在目标赛前 3 周成绩下降 2%。回顾：训练峰值被排在赛前 7 周；静息心率与情绪问卷无异常；训练负荷未额外升高。
- 排查：OT/OR？无超量负荷、无客观异常 → 排除 → 命中**时机错配**（peak 与出成绩时点脱节，`ce24-01` 范例）。
- 处置方向：**重排周期化时点**（而非减量）；真正问题是"何时该高、何时该减"，属计划编排。

## A2 — 未来触发 (Trigger)

**用户情境**：
1. 运动员/队伍成绩低于预期，用户问"是不是练过头了？"
2. 成绩一降就想减量，需要先确认**到底是不是**过量训练。
3. 训练量明明不大，成绩却崩了，用户疑惑原因。
4. 临近比赛成绩不升反降，想知道是训练问题还是时机问题。

**语言信号（中英双写）**：成绩下降 / 状态下滑 / 表现低于预期 / 是不是练过头了 / 为什么成绩掉了 / 比赛没发挥 / 减量还是加量 / underperformance / performance decrement / "why is my performance down" / mistimed peak / not responding to training。

**与相邻能力的区分（初稿）**：本卡只管**归因/分诊**（是什么原因）。一旦确认是 OT/OR，交 `cap.nsca.overtraining-continuum-classification` 命名分档、`cap.nsca.overtraining-recovery-strategy` 恢复。若归因指向"时机错配/训练不足/计划结构"，交**周期化簇**（`cap.nsca.season-to-period-mapping`、`cap.nsca.peaking-vs-maintenance`、`cap.nsca.annual-plan-construction`）。若问"该测什么来查" → `cap.nsca.athlete-monitoring-plan-design`。**与"测试与评估"不同**：那是"怎么准确测量"，本卡是"测出来下降后往哪归因"；**与"周期化"不同**：那是"怎么排计划"，本卡是"计划结果异常时怎么找原因"。

## E — 执行 (Execution)

**输入契约（必需）**：成绩下降的**事实与幅度**（%，相对何基线）；**时间窗**；**训练负荷轨迹**（量/强度近期是否显著变化，最好有 internal/external load）；**训练计划与比赛日程**（peak 落在何时、目标赛在何时）；**客观指标**（静息心率/HRV、体重、问卷、睡眠）；**非训练应激清单**（生活/工作/家庭/旅行/疾病/营养/月经周期）。
- **缺失处理**：缺"计划—赛程对齐关系"则无法排除时机因；缺客观指标则无法支持/排除 OT。**先问，不得静默猜值**；可在缺某维时给出"该维待补"的暂定分诊。

**步骤（含分支与完成标准）**：
1. **核实事实**：确认下降相对**本人基线**、有可比的测量口径、排除单次波动/测量误差。完成标准：写明基线与窗口；若为噪声 → 判"无实质下降"，结束。
2. **查训练—比赛时机**：peak 是否与"需要出成绩"的时点对齐？（Figure 24.13）→ 若错配 → **命中"时机性低谷"**（`ce24-01`），处置 = 重排 periodization 时点，**不加量也不减量盲调**。
3. **查训练量是否不足**：负荷是否长期低于适应所需 → **命中"训练不足"**，处置 = 恢复/提升负荷。
4. **查是否确为 OT/OR**：训练量/强度是否显著超载、恢复是否不足、是否有长期降成绩必要条件的迹象 → **命中 OT/OR** → 转 U1 分档 / U5 恢复。
5. **查 allostatic load（训练外压力）**：生活/工作/家庭/旅行/时区/月经/年龄/伤史是否叠加（`ce24-03`）→ **命中"非训练压力"**，处置 = 降总应激 + 外部压力管理。
6. **查营养/睡眠/疾病**：能量/蛋白/糖原不足、睡眠剥夺、疾病或感染 → 命中则先纠正该维。
7. **并列出结论**：允许**多因共存**；标注每因的**证据强度**与**因果方向不确定处**。完成标准：每个候选因有"是/否/待补 + 证据"三态。

**输出契约**：`{是否有实质下降, 候选因清单[时机错配|训练不足|OT/OR|非训练压力|营养睡眠疾病], 各因判定(是/否/待补)+证据, 因果方向存疑标注, 处置方向, 下一步能力}`。

**判停点/分支**：
- 步骤 1 判定为测量噪声 → 停。
- 多因共现 → **不得**只报一个；按证据强度排序并写清耦合。
- 出现疑似疾病/医疗红旗 → **转诊**（`cap.nsca.rehab-scope-and-referral`），不自行处置。
- 命中 OT/OR → 交 U1/U5，本卡结束。

**约定**：原文用 Figure 24.11/24.12 的实线（直接原因）/虚线（贡献因素）区分，但**未给各因的量化权重或判别阈值**。本卡以"逐项三态判定"落实，属**约定**，不虚构权重。

## B — 边界 (Boundary)

- **不要**把"成绩下降"等同于过度训练——原文标题句即为此而设（`ce24-02`）。
- **不要**只查训练量而忽略时机、非训练压力、营养睡眠（`ce24-01`/`ce24-03`）。
- **原文自认的因果困境（B 段主依据）**：`ch24.txt` 第 481–489 行指出 allostatic load 的次要因素**可能由 OTS 造成**而非引起它——因果方向**无法仅凭横断面证据确定**；本卡只能列候选并标注不确定性。
- **最轻一档难辨**：成绩停滞"difficult to differentiate from good training programs"（`ch24.txt` 第 329–334 行）——正常平台不应被当作病理。
- **共识≠实证**：Figure 24.12 的因素清单是**贡献因素罗列**，非经证实的最优排查顺序。
- **专业边界**：排查出的"疾病/营养/心理"维**不由体能教练处置**，应转诊；本卡不越界做医疗诊断。
- **变量耦合**：训练、生活、营养、睡眠共享同一适应负荷池，逐项"独立归因"可能误导（BOOK_OVERVIEW 3.3-3 变量耦合）。
- **相邻易混**：U1（命名分档）、周期化簇（时机/结构问题）、测试评估簇（测量问题）。

## 相关能力

- 依赖（先理解）：`overtraining-continuum-classification`
- 组合（常配合使用）：`athlete-monitoring-plan-design`
- 组合（常配合使用）：`macronutrient-energy-needs`
