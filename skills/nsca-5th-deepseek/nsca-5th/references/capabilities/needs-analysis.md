# 需求分析（Step 1：运动特征评估 + 运动员评估）

## R — 原文 (Reading)

> "The strength and conditioning professional's initial task is to perform a needs analysis, a two-stage process that includes an evaluation of the requirements and characteristics of the sport and an assessment of the athlete."

— Chapter 18 · Step 1: Needs Analysis（`ch18.txt` 229–231）

## I — 自述 (Interpretation)

需求分析是抗阻训练计划设计七步的第 1 步，也是后面所有参数的查表键来源。它分两个阶段、必须先运动后运动员：

1. **评估运动（Evaluation of the Sport）**——搞清"这项运动到底要什么"。三条最小维度：动作分析（反复性动作模式与主要发力肌群）、生理分析（strength / power / hypertrophy / muscular endurance 四素质的优先级排序）、伤病分析（常见过用与非接触性损伤部位及机制）。可用等长力量测试、慢/快伸缩循环功能（CMJ、rebound jump）等刻画运动员的发力剖面。
2. **评估运动员（Assessment of the Athlete）**——搞清"这名运动员现在有什么"。评估训练与损伤状态、实施测试、把结果对照常模或队内描述性数据，找出强项与弱项，最后定主训练目标。

输出三件事：运动需求画像、训练状态类别、训练目标。评估越个体化，后续动作/负荷/量越有据可依。跳过这一步，Step 2–7 全是在猜。

## A1 — 案例 / 演练 (Application)

**原书案例（in-book-athlete-scenario，c18-17，Figure 18.3–18.5）**：一名足球运动员——等长中大腿拉（IMTP）峰值力与相对峰值力在联赛中仅平均；反向纵跳高度 45 cm 属很好，但因起跳时间偏长（1.0 s），修正反应力量指数（mRSI = 跳跃高度 / 起跳时间）0.46 仅平均，说明其用更长加速时间换取跳跃高度、力-时间剖面次优；反弹跳触地时间 163 ms 良好，但反弹跳高度仅 22 cm，RSI 1.40 平均。**结论（原文）**：该运动员需强化最大与快速发力，宜先安排一训练块强调最大力量，再安排一训练块强调 speed–strength。

**原书案例（tabular-example，c18-3）**：三情境需求分析应用表分别给出运动评估（动作/生理/损伤）+ 训练状态 + 主目标：A（女 20 岁大学篮球中锋，in-season）主目标 Strength/power；B（男 28 岁职业橄榄球锋线，off-season）主目标 Hypertrophy；C（男 17 岁高中越野跑者，preseason）主目标 Muscular endurance。

## A2 — 未来触发 (Trigger)

**用户会遇到这类问题的情境（3–5 条）**
- 用户要为某个专项/位置的运动员"从零开始"设计抗阻训练计划，但还没说这项运动需要什么、运动员现在处于什么水平。
- 用户问"这个运动员到底该先练力量还是练爆发/耐力"。
- 用户拿到一份测试结果，想知道这些数字对训练计划意味着什么。
- 用户在比较两名同队运动员为何该用不同方案。
- 用户想核对"我是不是漏了运动的某个需求或伤病风险"。

**语言信号（中英双写关键 trigger 词）**
- "帮这个运动员排计划前，先看这项运动需要什么" / "what does this sport require"、"needs analysis"、"sport evaluation"、"movement analysis"、"physiological analysis"、"injury analysis"、"athlete assessment"、"训练状态"、"主训练目标"、"primary training goal"、"他适合练什么"。
- 英文常见："design a program for a [sport] athlete"、"what are the demands of this sport"、"assess this athlete"。

**与相邻能力的区分（初稿）**
- 与 **training-status-classification**：本卡负责"要不要做/怎么组织需求分析"并调用该能力做状态判档；状态判档是其中一步，专属查 Table 18.1。
- 与 **primary-training-goal**：需求分析产出的目标需要目标决策框架去收敛到"每块单一主目标"，该决策另卡承载。
- 与 C-testing 簇（测试选择/实施/数据解释）：本卡只给流程骨架，具体测什么、常模怎么读交测试簇。

## E — 执行 (Execution)

**输入契约**
- 必需：运动项目与位置、赛季阶段（off/pre/in/post-season）、运动员训练背景（项目类型、近期规律参与时长、既往强度、技术经验程度）、损伤史。
- 可选：测试结果（力量/爆发/耐力/体成分等）、可用器械与时间。
- **先询问（缺失不得静默猜值）**：若无运动员训练背景四维信息 → 无法定训练状态，先询问；若无任何测试结果且无法测试 → 以"无数据"登记，不得臆造 1RM/素质水平；若无赛季阶段 → 先询问后再进 Step 2 之后。
- 适用条件：任何运动员；`reference` 级（无交付物、仅约束其他单元）的处方原则不在此。

**步骤（每步有完成标准）**
1. **做运动评估**——完成标准：产出 (a) 动作分析（列表：反复动作模式 + 主要发力肌群）；(b) 生理分析（四素质 priority 排序）；(c) 伤病分析（常见过用/非接触损伤部位与机制）。判停点：若无法区分 four quality 优先级，先补观察/录像再继续。
2. **做运动员评估**——完成标准：产出 (a) 训练状态类别（调用 training-status-classification 查 Table 18.1）；(b) 测试结果及其对照常模/队内数据的强项-弱项判断；(c) 损伤状态（需运动医学评估者先转诊）。
3. **定主训练目标**——完成标准：产出本训练块 dominant 目标（strength/power/hypertrophy/muscular endurance）。三路证据 = 测试结果 + 运动动作/生理分析 + 赛季优先级（调用 primary-training-goal 收敛）。
4. **交付**——完成标准：输出含上述三项的"需求分析结论"。

**输出契约**
- 结论结构：`{ 运动评估:{动作,生理,损伤}, 运动员评估:{训练状态,测试强项/弱项,损伤}, 主训练目标 }`。
- 训练状态只能取 `beginner | intermediate | advanced`，且注明"三档为连续谱"。
- 主训练目标只能四选一。
- 无规定处标注为约定：原文未给统一"需求分析报告"模板，本卡字段为约定；具体测试项目与常模表去 Ch13/Ch14。

## B — 边界 (Boundary)

- **不要**在信息不足以定运动需求或运动员状态时强行产出——需求分析是"先搞清再设计"，信息不足应先补测或询问。
- 作者警告的失败模式：**cookie-cutter（一刀切）**——对所有人套同一计划，忽视个体化；即使动作 80%–90% 相同，**负荷也必须按各自能力个体化**（ce18-01）。
- **常模时效性/人群依赖**（BOOK_OVERVIEW 3.1）：测试结果对照的常模/描述性数据来自特定年代、队伍、协议；跨年代/地区套用需核对该表样本人群与设备。
- **共识 ≠ 实证、迁移不保证**（3.3）：需求分析只给出方向，体能改善是否迁移到专项表现高度依赖专项与技术。
- **教练专业边界**：损伤须由 sports medicine 评估，教练不得自行诊断或处置。
- 易混淆：与 **C-testing 簇**（测什么/怎么测/怎么解释数据）不同——本卡不重建测试方法论；与 **primary-training-goal** 不同——本卡产出候选目标，收敛到单目标由后者负责。

## 相关能力

- 依赖（先理解）：`nsca-testing-and-evaluation`
- 依赖（先理解）：`training-status-classification`
- 组合（常配合使用）：`primary-training-goal`
- 组合（常配合使用）：`sport-specific-test-battery`
