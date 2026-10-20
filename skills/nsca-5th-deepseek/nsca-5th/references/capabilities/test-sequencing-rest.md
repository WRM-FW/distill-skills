# 测试顺序编排与休息安排

## R — 原文 (Reading)

> "a test that maximally taxes the phosphagen energy system requires 3 to 5 minutes of rest for complete recovery, whereas a maximal test of the anaerobic glycolytic energy system requires at least 1 hour for complete recovery. ... A logical sequence, although there are some variations, is to administer tests in this order: 1. Nonfatiguing tests ... 2. Agility tests ... 3. Maximum power and strength tests ... 4. Sprint tests ... 5. Local muscular endurance tests ... 6. Fatiguing anaerobic capacity tests ... 7. Aerobic capacity tests"

— Chapter 13 · Sequence of Tests（`ch13.txt:871-893`）

## I — 自述 (Interpretation)

测试排序只有一条根本原则：**任何一项测试的完成不得损害后续测试的表现**，这样每项都能发挥最佳、且与既往数据可比。

排序依据是疲劳的产生与清除时间：磷酸原系统最大动员后 3–5 分钟恢复，糖酵解系统最大测试需 ≥1 小时恢复。因此"高技能、易被疲劳污染的测试"（敏捷）要排在"制造疲劳的测试"之前。

固定七段顺序：**非疲劳 → 敏捷 → 最大功率/力量 → 冲刺 → 局部肌耐力 → 疲劳性无氧能力 → 有氧能力**。

配套休息口径：
- 试次之间：不接近极限 ≥2 分钟；接近极限 ≥3 分钟（由上一试次相对难度判定）。
- 测试电池内不同测试之间：≥5 分钟。
- 疲劳性无氧/有氧测试宜另择一日；同日则置最后并延长休息。
- 固定每日同一时段（规避昼夜节律），尽量室内。

## A1 — 案例 / 演练 (Application)

**原书未提供完整单日排序案例**，仅给七段模板与休息口径（`ch13.txt:864-904`）。

**合成演练（明确标记）**：一天内需测：身高体重、T-test、1RM 深蹲、40 yd 冲刺、俯卧撑、300-yd 折返、1.5-mile 跑。
- 排序：非疲劳(身高/体重) → 敏捷(T-test) → 最大力量(1RM 深蹲) → 冲刺(40 yd) → 局部肌耐力(俯卧撑) → 无氧耐力(300-yd) → 有氧(1.5-mile)。
- 300-yd 与 1.5-mile 建议另日；同日则置最后；测试间 ≥5 分钟。
- 结论：一条无先后冲突的单日串；跨日拆分规则明确。

## A2 — 未来触发 (Trigger)

**用户情境**：
1. 一天要测很多项，问"先测哪个、后测哪个"。
2. 发现后测成绩总比平时差，怀疑被前一项疲劳污染。
3. 需要决定哪些测试拆到另一天做。
4. 要排定试次间休息时长。

**语言信号（中英双写）**：测试顺序 / 先测什么 / 测试流程排序 / 试次休息 / 电池间隔 / test order / sequence of tests / what to test first / rest between trials / test battery rest / 疲劳污染 / fatigue confound。

**与相邻能力的区分**：本卡只管"顺序 + 休息时长"；测什么由 `sport-specific-test-battery` 决定；测试员的岗位分工由 `tester-selection-duties` 决定；测日环境标准化由 `test-prep-standardization`。

## E — 执行 (Execution)

**输入契约**：待测测试清单（含各测试主导供能系统/是否疲劳性）+ 单日/跨日约束。缺测试清单无法排序。

**步骤与完成标准**：
1. **归类**：把每项测试归入七段中一类（非疲劳/敏捷/最大功率力量/冲刺/局部肌耐力/疲劳性无氧/有氧）。完成标准：每项都有归类，无"其他"。
2. **按七段排序**。完成标准：输出有序列表；同类内顺序不影响后续（可自定）。
3. **拆日**：把第 6、7 类（疲劳性无氧、有氧）尽量移出主测日。完成标准：给出"同日/异日"决策；若同日必须置最后并延长休息。
4. **填休息档位**：标注试次间（非极限 ≥2 min、接近极限 ≥3 min）与测试间（≥5 min）。完成标准：每个相邻测试对之间都标出 ≥5 min。
5. **固定时段与场地**：指定每日同一时段、尽量室内。完成标准：写明时段与场地。
6. **输出**。

**输出契约**：`{有序测试串(按七段), 同日/异日拆分表, 相邻测试最小间隔(分钟), 试次间休息档位, 时段/场地约定}`。

**判停点/分支**：
- 若必须在同一天同时放疲劳性无氧与有氧为主测 → 输出顺序并把二者置最后，同时给出"延长休息/次日复测"的提示。
- 若某测试无法归类 → 依其"是否疲劳 + 是否高技能"就近归段，并标注约定。

**约定**：原文未给"非疲劳性测试"的完整界定（仅以纵跳/静态跳举例，`f13-06` gap）。本卡按"不引起明显全身疲劳、不抬高心率至影响后续"操作化，标为约定。

## B — 边界 (Boundary)

- **不要**只按"想先看哪项"排序；必须服从"后测不受前测影响"原则。
- **不要**把 ≥5 分钟当成所有情况的上限——糖酵解主导测试后需 ≥1 小时，必要时须拆日。
- **作者盲点（3.3-3 变量耦合）**：七段模板是简化，真实排布会因人数、站点、器材而变（原文也承认"存在一些变体"）。
- **共识 ≠ 实证**：3–5 min / ≥1 h / ≥5 min 为书中口径，非唯一权威。
- **相邻易混**：与 `tester-selection-duties`（人员分工）和 `test-prep-standardization`（测日准备/记录）不同。

## 相关能力

- 依赖（先理解）：`sport-specific-test-battery`
- 组合（常配合使用）：`speed-agility-test-protocols`
- 组合（常配合使用）：`test-prep-standardization`
