# 有氧耐力训练设计（晋级伞形卡）

## R — 原文 (Reading)

> "Aerobic Training Program Design Variables. Step 1: Exercise mode. Step 2: Training frequency. Step 3: Training intensity. Step 4: Exercise duration. Step 5: Exercise progression." ... "The program design variables and the various types of aerobic endurance training are applied to athletes' sport seasons to create a yearly or season-long training program."

— Chapter 21 · "Aerobic Training Program Design Variables"（`ch21.txt` 第 236–241 行）；"Application of Program Design to Training Seasons"（第 1014–1016 行）

## I — 自述 (Interpretation)

这是一张把 Ch21 全部有氧设计环节串起来、自包含端到端回答"给一名运动员怎样设计有氧耐力训练"的主卡。骨架为八环：

**① 定目标与强弱项**——先评估 VO2max、乳酸阈（LT）、运动经济性等决定因素，把训练重点压在最弱者，而非照抄成功者方案（"train smarter"，MED/MTD 风险-收益观）。
**② 选模式 mode**——尽量匹配比赛的移动方式（跑/骑/游）；多项目者用交叉训练。
**③ 定频率 frequency**——由强度×时长、训练状态、赛季阶段三者交互决定；提升 VO2max 须 >2 次/周，维持可低至 2 次/周。
**④ 定强度 intensity（核心）**——用 **Karvonen/%HRR** 法 `THR=(HRR×强度)+RHR` 或 **%MHR** 法 `THR=APMHR×强度`（APMHR=220−age），把"处方百分比"落成心率区间；或用 Table 21.1 五区标尺（%VO2max/%HRmax/乳酸/时长）、Table 21.2（%VO2max↔%HRR↔%MHR）、三区乳酸口径（<2/2–4/>4 mmol/L）定位强度。**两法不可混用**。
**⑤ 定时长与进阶**——时长与强度反比（越强越短）；进阶遵守 ≤10%/周、一次只加一个变量、按预测时间而非距离。
**⑥ 选训练类型**——Table 21.4 五类：extensive endurance(≤65% VO2max, 30–120 min)、pace/tempo(~LT, 20–30 min)、interval(3–5 min, W:R=1:1 @近 VO2max)、HIIT(30–90 s, W:R=1:5, >VO2max)、fartlek(20–60 min 混合)；不能只堆 LSD。
**⑦ 按赛季调整**——off/preseason/in-season/postseason 重排频率-时长-强度（Table 21.5；其 in-season 行存在源抽取缺口，见 B）。
**⑧ 处理特殊情境**——同期训练（重负荷低周量、自由重量多关节、最重要目标先做）、赛前减量（linear/step/progressive，降量保强度）、热适应（WBGT>30 °C、60/90/120 min）、高原（LHTL，住 2,000–3,000 m、缺氧剂量 ≥12 h/天 ≥3 周）。

## A1 — 案例 / 演练 (Application)

原书各环案例（明确标注类型与出处）：
- **心率换算法（`c21-1`/`c21-2`，worked-example）**：30 岁 RHR 60、60–70% → 138–151 次/分（Karvonen）；20 岁 70–85% MHR → 140–170 次/分（%MHR）。
- **分区标尺（`c21-3`/`c21-4`，tabular-example）**：Table 21.1 五区、Table 21.2 三列换算。
- **样例周（`c21-5`–`c21-9`，sample-program）**：初级马拉松休赛期、中级铁三游泳、初级车手赛前、中级 10 km 赛前晚期、5 km 越野赛季。
- **进阶算例（`c21-10`，worked-example）**：新手跑者 +0.3 mi vs 实际可 +1 mi；山地 10→11 mi 时间 +65% 判不合规。
- **赛季对照（`c21-11`，tabular-example）**：Table 21.5 各档变量。

## A2 — 未来触发 (Trigger)

**用户会在什么情境下遇到这类问题**
1. 要"从头给一名运动员设计一套完整的有氧耐力训练计划"。
2. 手头有专项与训练状态，需走完"强弱项→模式→频率→强度→时长进阶→类型→赛季"全流程。
3. 既有常规设计，也需一并处理同期训练、减量、热适应或高原等情境。
4. 不确定该用哪张下钻卡、想让本卡做总入口统摄。

**语言信号（中英双写关键 trigger）**
- 中文：「设计有氧耐力训练计划」「有氧从零到一份方案」「有氧训练全流程」「跑步/骑行/游泳训练计划设计」「有氧强度怎么定、赛季怎么调」
- English: "design an aerobic endurance program", "full aerobic training design", "aerobic program from scratch", "endurance training plan design", "aerobic plan including taper and heat"

**与相邻能力的区分（初稿，阶段 3 回填）**
- 与 `nsca-speed-agility-design`（Ch20）：本卡专治**有氧耐力与代谢/强度分区**；速度-变向-敏捷归那张（判据是反应性刺激与变向角度）。
- 与 `nsca-resistance-program-design`（Ch18）：本卡仅限有氧；抗阻七步变量归那张。
- 与 `nsca-periodization`（Ch22）：本卡在赛季层面**桥接**到周期化，但年度/多年框架、模型选择、块结构归那张。
- 与"过度训练与恢复"（Ch24）：本卡给训练设计与减量，不负责诊断已成型的过度训练综合征。
- 与簇内下钻卡：细节下沉到 9 张卡（U1 心率分区 / U2 五变量 / U3 进阶 / U4 间歇比 / U5 同期 / U6 减量 / U7 热适应 / U8 高原 / U9 恢复课）。

## E — 执行 (Execution)

**输入契约**
- 必需：① 专项与比赛模式；② 训练状态（beginner/intermediate/advanced）；③ 赛季阶段；④ 每周可练天数与单课时长上限；⑤ 强度锚点（实测 LT/VO2max/配速，或年龄+[RHR] 用于心率法）；⑥ 目标与已知强弱项（若有测试数据）。
- 缺 ⑤ 时：退化用心率分区（须注明误差）；缺 ⑥ 时：先做需求/强弱项评估，否则后续聚焦无据。缺 ② 训练状态先问，不得静默猜档。

**完整设计流程（八步，每步有完成标准）**
1. **定目标与强弱项**：评估 VO2max / LT / 经济性，找出最弱项并聚焦；用 MED/MTD 做风险-收益定位。完成标准：给出主要需求 + 次要需求 + 弱点聚焦。
2. **选模式 mode**：匹配比赛移动模式。完成标准：写出主模式（多项目者列多模式）。
3. **定频率 frequency**：由强度×时长、训练状态、赛季阶段定；提升需 >2 次/周。完成标准：每周次数。
4. **定强度 intensity**：选法并算区间——Karvonen `HRR=APMHR−RHR; THR=(HRR×强度)+RHR` 或 `%MHR: THR=APMHR×强度`（APMHR=220−age）；用 Table 21.1 五区 / Table 21.2 换算 / 三区乳酸标定。**写明所用方法**。完成标准：每节课标注目标区 + 目标心率区间（整数次/分）。
5. **定时长与进阶**：时长按强度反比取；进阶 ≤10%/周、单变量、按时间。完成标准：每课时长 + 首周期进阶上限。
6. **选训练类型**：按 Table 21.4 组合 ≥2 类（LSD/pace-tempo/interval/HIIT/fartlek），其余日低强度/恢复。完成标准：周课表含多类型与各自组数×时长×W:R。
7. **按赛季调整**：定位 off/preseason/in-season/postseason，重排频率-时长-强度（Table 21.5：off-season 建基础长时低强；preseason 增强度、维持/减时长；in-season 维持专项、赛前低强度短时；postseason 低强低量）。完成标准：给出各季节变量分配。
8. **处理特殊情境**：按需调用——同期训练（≥90%1RM 或 ≤4RM、周量低、2–3 次/周、自由重量多关节、最重要目标先做）；减量（选 linear/step/progressive，降量保强度）；热适应（WBGT>30 °C、60/90/120 min、RPE 监控）；高原（LHTL，住 2,000–3,000 m、缺氧剂量 ≥12 h/天、≥3 周）。完成标准：每个适用情境给出参数。
- **失败处理/分支**：知识/设备不足（无 LT/VO2max、无测试成绩）→ 只完成可完成环并显式标注缺口，不虚构参数；未建有氧基础 → 不排 interval；高温/高原/减量并存时按优先级分步处理（安全 > 适应 > 峰值）。

**输出契约**
- 完整交付物：`{目标与主/次需求, 模式, 频率, 强度法+心率/分区区间, 各课时长与进阶上限, 训练类型周课表, 赛季变量分配, 特殊情境参数}`。
- 资源 `resources/aerobic-intensity-zones.md` 内含 Table 21.1 五区 + Table 21.2 换算 + 两套公式算例，随包可直接调用。

**原文口径与缺口（供复算）**
- 表值见各下钻卡与资源文件；关键阈值：APMHR=220−age；五区/三区边界见资源；≤10%/周；W:R 无氧 1:12–1:20 等见 Table 3.6。
- **缺口声明**：① Table 21.5 的 **in-season 行在 `ch21.txt` 源抽取错位**（第 1035–1053 行，beginner/advanced 的时长与强度三档被拆到两个文本块），本卡**不代为给出该行确切列对齐值**，需高保真来源重读；② Table 3.6 间歇比原文自认循证不足（`ch03.txt` 第 1180–1182 行）；③ 恢复课具体分钟数原文未给。

## B — 边界 (Boundary)

- **不要用**：当问题是速度/敏捷/快速伸缩复合时（用 `nsca-speed-agility-design`、`nsca-plyometric-design`）；当问题是纯抗阻计划时（用 `nsca-resistance-program-design`）；当问题是赛季/多年框架与周期模型时（用 `nsca-periodization`）；当只是单个心率换算或单条进阶判断时下钻到 U1/U3。
- **强度分区表的性质（必读）**：Table 21.1 的区间边界是**惯例（convention）而非生理断点**——它由挪威奥委会基于越野滑雪/赛艇/冬季两项的多年测试归纳为**通用指南（Seiler 2010）**，各区间是连续体上的人为切分，跨项目迁移需校验；三区的 2/4 mmol/L 亦为常用口径而非绝对阈值。**不要把区间边界当"生理开关"**（例如并非低于某心率就"不练到"，高于就"一定练到"）。
- **心率法在高强度区间的误差（必读）**：心率与摄氧量的良好关系仅在 **50%–90% 功能容量（HRR）**区间成立；**越过高强度区（Zone 4–5）误差显著变大**，此时心率不再是可靠的强度标尺——处方的相对强度与实际代谢应激偏离，应优先用 %VO2max、血乳酸或配速直接监控。此外 APMHR 本身有 **±10–12 次/分（SD）**的个体误差，且估计式**不含 LT 信息**；热/湿/海拔会抬高心率并使关系偏移。
- **其他盲点（BOOK_OVERVIEW 步骤 3）**：共识 ≠ 实证（Table 21.4/21.5、10% 规则、Table 3.6 多为经验/惯例值）；"体能改善 → 专项迁移"不保证；变量强耦合（改强度牵动时长与恢复）；教练专业边界（中暑/热病、损伤、RED-S 属转诊）。
- **相邻易混**：`nsca-speed-agility-design`、`nsca-resistance-program-design`、`nsca-periodization`。

## 相关能力

- 组合（常配合使用）：`concurrent-aerobic-resistance-training`
- 组合（常配合使用）：`nsca-overtraining-recovery`
- 组合（常配合使用）：`nsca-periodization`
- 组合（常配合使用）：`nsca-resistance-program-design`
- 组合（常配合使用）：`nsca-speed-agility-design`

## 配套资源

路径相对于本文件；脚本需先检查运行条件，不因附带而自动执行。

- [resources/aerobic-intensity-zones.md](../../resources/aerobic-intensity-zones.md)
