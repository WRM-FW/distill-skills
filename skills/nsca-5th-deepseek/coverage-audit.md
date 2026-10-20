# coverage-audit.md — 原书关键任务覆盖审计

> 基准：`BOOK_OVERVIEW.md` 的原书关键任务清单 T01–T40（**独立于已验证候选**，不从旧版通过项反推）。
> 每项记录：任务 → 原文位置 → 候选 → decision → 最终交付去向。


## 簇 A-plan-design — 抗阻训练计划设计（需求分析 / 训练状态 / 七步变量）

（T01–T11）

| task_id | 任务 | 原文位置 | 对应候选 | decision | 去向 |
|---|---|---|---|---|---|
| T01 | 评估运动需求 + 评估运动员（需求分析） | Ch18 Step1（ch18.txt 228–451）；Ch13 | f18-01, f18-02, c18-1, c18-3, c18-17；目标部分 f18-04, p18-08 | verified | cap.nsca.needs-analysis + cap.nsca.primary-training-goal |
| T02 | 判定训练状态 | Ch18 Table 18.1（317–336） | f18-03, p18-07, c18-2 | verified | cap.nsca.training-status |
| T03 | 选择抗阻训练动作 | Ch18 Step2（455–793） | f18-05, f18-06, f18-07, f18-08, p18-09, p18-36, p18-37, c18-4, ce18-04, ce18-05 | verified | cap.nsca.exercise-selection |
| T04 | 确定训练频率 | Ch18 Step3；Table 18.4/18.7（794–943） | f18-09, f18-10, f18-11, p18-10, p18-11, p18-12, p18-35, c18-5 | verified | cap.nsca.training-frequency |
| T05 | 排列动作顺序 | Ch18 Step4（984–1168） | f18-12, f18-13, p18-13, p18-14, c18-6 | verified | cap.nsca.exercise-order |
| T06 | 确定 1RM / 由 xRM 估算 1RM / 确定 RM 负荷 | Ch18 Step5；Table 18.8/18.9（+Figure 18.8）（1331–1561） | f18-15, f18-16, f18-17, p18-17, p18-18, p18-19, p18-20, c18-7, c18-8, c18-15, c18-16 | verified | cap.nsca.one-rm-xrm-determination |
| T07 | 按目标分配负荷与重复 | Ch18 Step5；Table 18.11；RM continuum（1735–1910） | f18-14, f18-18, f18-19, p18-16, p18-23, p18-24, c18-7；特例 f18-20, p18-25, p18-29；替代 f18-24, p18-21, p18-22 | verified | cap.nsca.load-reps-by-goal + cap.nsca.power-load-assignment + cap.nsca.rpe-rir-srb |
| T08 | 判断何时、增加多少负荷 | Ch18 Step5；Table 18.12（1912–2012） | f18-21, f18-22, f18-23, p18-04, p18-26, p18-27, p18-33, c18-9, c18-10 | verified | cap.nsca.load-progression |
| T09 | 分配训练量 | Ch18 Step6；Table 18.13（2177–2381） | f18-25, f18-26, p18-15, p18-28, p18-30, c18-11, c18-12, c18-18 | verified | cap.nsca.volume-assignment |
| T10 | 确定组间休息 | Ch18 Step7；Table 18.15（2430–2519） | f18-27, f18-28, p18-31, p18-32, c18-13 | verified | cap.nsca.rest-periods |
| T11 | 完成完整 7 步计划 | Ch18 Step1–7 + 综合应用（191–204, 2520–2530, 2597–2650） | f18-29, p18-06, c18-14 | verified | cap.nsca.seven-step-program |

**T01–T11 全部有对应候选并 verified，无遗漏、无 needs_review。**

### 非本簇任务（登记去向，避免静默消失）

| task_id | 任务 | 归属 | 说明 |
|---|---|---|---|
| T20 | 评估测试质量（效度/信度/客观性）并选测试 | C-testing | 由 f13-*/p13-* 承载 |
| T21 | 规范测试实施流程与顺序 | C-testing | 由 f13-*/p13-* 承载 |
| T22 | 计算/解释测试数据、构建运动员画像 | C-testing + Ch14 | 由 C-testing 承载 |
| T23 | 运用常模数据做百分位比较 | C-testing | 由 C-testing 承载 |

---


### 簇 A-plan-design 缺口清单

1. **无 critical/high 任务缺口**：T01–T11 均有原文支撑并 verified。
2. **数据冲突登记（未静默消失）**：Ch18 Step 5 应用表（Scenario B，off-season/hypertrophy）文本写「Assign 70% of the tested 1RM」，但所列负荷（deadlift 650→490 lb、back squat 675→505 lb、bench press 425→320 lb、shoulder press 255→190 lb）实按 ~75% 计算（650×0.75=487.5、675×0.75=506.25、425×0.75=318.75、255×0.75=191.25）。此为**原书内部不一致**（可能为表格取整/笔误）。核心规则来自 Table 18.11（hypertrophy 67%–80%），不受影响；U8 仍判 verified，但 c18-7 该行数值不应作为"70% 负荷"范例使用。若阶段 2 需引用该 worked example，建议按 Table 18.11 的 67%–80% 区间自行核算，或注明原书例值系 ~75%。
3. **原文未给的规则**（如实保留，未用常识补齐）：① p18-20 未列具体 1RM 预测方程系数（仅指向文献）；② 肌肉平衡未给具体肌群对的比值阈值；③ 动作类型存在边界争议（如 lunge 是否 core）；④ 变量强耦合无回环量化规则（U14 已注明不含回环）。这些不阻塞对应单元的通用可执行性。

---


## 簇 B-periodization — 周期化与年度计划编排

| task_id | 任务 | 原文位置 | 对应候选 | decision | 去向 |
|---|---|---|---|---|---|
| T12 | 设计周期化计划（时期划分与变量应用） | Ch22 全文；Table 22.2（ch22.txt 360–394）、Table 22.3（502–539）、年度计划样例（792–921） | f22-01~19、p22-01~23、c22-1/2/3、ce22-01~05 | verified（U1–U6、U8、U9、U10）/ reference（U11、case/ce 支持材料） | cap.nsca.periodization-three-level-build / periodization-model-choice / periodization-cycle-durations / season-to-period-mapping / annual-plan-construction / mesocycle-variable-filling / peaking-vs-maintenance / in-season-load-management / undulating-vs-traditional-identification；U11→overview；c22-*、ce22-*→A1/B 素材 |
| T13 | 理解并应用 GAS/刺激—疲劳—恢复理论 | Ch22 "Central Concepts"（ch22.txt 83–222）；Ch24（现象展开，属 H） | f22-09/10/11、p22-05/06/07 | verified（U7） | cap.nsca.periodization-mechanistic-theories |

**交界核对**：
- **与簇 H**：簇清单中的 **f24-01~10、p24-01~21（共 31 条）** 及 counter-examples 中的 **ce24-01~10** 均属 Ch24 过度训练/恢复/监控，按约定 **属簇 H**，本簇不重复验证；本簇仅收其被周期化理论引用的机制部分（已并入 U7）。→ 见缺口清单。
- **与簇 A**：候选 **f22-17 / p22-23 / p22-22** 中的"**%RM↔重复数换算、由多次 RM 估 1RM（Table 18.8/18.9）**"确属 **簇 A 的负荷计算**；本簇只在 U6 保留"在年度计划的中周期上如何把这些变量落值"的编排流程。**若阶段 1.6 判定需独立，"负荷换算/落值"应归 A 簇 canonical。**

---


### 簇 B-periodization 缺口清单

1. **Ch24 内容整体移交簇 H（非本簇遗漏）**：候选清单中 f24-01~10、p24-01~21（31 条）与 ce24-01~10 覆盖过度训练/恢复/监控（T27/T28 相关），按簇交界属簇 H。本簇未验证、未淘汰，**保持活跃交 H 处理**，避免"重要内容静默消失"。
2. **跨章依赖（非缺口，但需标注）**：U6 与 U9 引用的 **Table 18.8 / 18.9 / 18.15** 数值在 Ch18（簇 A），本簇只能给出"如何调用"的流程；实际换算需 A 簇提供表值。
3. **原文内部不一致（次要）**：ch22.txt 第 798 行 preseason 记 "August 21-November 5"，第 852 行记 "11 weeks (August 21-October 5)"。以后者与 in-season 起始（11/6）冲突，判为原文/提取笔误。已在 U5 注明，采用 11/5；不影响可执行性，但**未回书核对纸质版权页/图 22.8 原图**，如需零误差应补读原图。
4. **模型择优无定论（重要，已写入单元局限）**：原文自认 "linear periodization" 为 misnomer，且 DUP 与传统模型**优秀性研究结论互相矛盾**。本簇已在 U10 明确保留该争议于 B 段，**禁止在阶段 2 宣称任一模型更优**。此为"来源即冲突"，故不转 needs_review（辨识口径可执行），但须在最终能力卡 B 段显式标注。
5. **ce22-04 无预防措施**：反例"每日波动模型过度负荷/损伤风险"原文**未给预防做法**（仅陈述对立观点）。作 B 段失败边界素材时，不得补造预防规则。

---


## 簇 C-testing — 测试选择、实施与数据解释

| task_id | 任务 | 原文位置 | 对应候选 | decision | 去向 |
|---|---|---|---|---|---|
| T20 | 评估测试质量（效度/信度/客观性）并选测试 | Ch13（ch13.txt:166-357, 642-647） | f13-01/02/03/14, p13-01..12, ce13-01/04, c13-02 | verified | U1, U2,（+U6），另 U10–U19 各协议 |
| T21 | 规范测试实施流程与顺序 | Ch13（ch13.txt:723-904）/Ch14 管理 | f13-05..09, p13-18..26, f13-10..12, f14-01/02, p14-58 | verified | U3, U4, U5, U7, U8, U9 |
| T22 | 计算/解释测试数据并构建运动员画像 | Ch14（ch14.txt:63-835, 1589-1702） | p14-01/02/09/10/11/15/33..36, c14-01..08, f14-20..23, p14-39..46 | verified | U10, U14–U18, U20–U24, U26 |
| T23 | 运用常模数据做描述性与百分位比较 | Ch14 Table 14.1–14.37（ch14.txt:2537 及表区） | p14-47..52, c14-13, ce14-08 | verified | U25（+U23） |
| T40 | 判断年龄/性别/环境因素对测试的影响 | Ch13（ch13.txt:642-678） | p13-13, p13-14（年龄/性别）；f13-04, p13-15, f13-11, p13-16, ce13-05（环境） | verified | U2（年龄/性别）, U7（环境） |

> T40 说明：**本簇有对应候选**（p13-13 训练状态/经验、p13-14 年龄性别、f13-04/p13-15/f13-11/p13-16/ce13-05 环境），不构成缺口；年龄/性别的处方层差异（青少年/老年/女性）分别属 Ch7/Ch8，由其他簇负责。

---


### 簇 C-testing 缺口清单

1. **p14-14（1.5-mile 跑推算 VO2max）—— 原文无回归公式，只能查表**（已回原文 ch14.txt:1045-1048 确认：正文仅指向表 14.22–14.25/14.26）。已在 U16 写明"**只能查表、不可自行拟合**"。**重要缺口**：若阶段 2 需要公式，须回查 ACSM 原出处，不得由本簇补造。
2. **单位换算常数在原文自相矛盾**：ch14.txt:65-66（相对力量）用 `lb×4.44 / kg×9.81`；ch14.txt:833（Margaria 功率）用 `lb×4.45 / kg×9.807`。已裁断统一采用 kg×9.81、lb×4.448（见文首与 U10/U20）。**保留冲突定位备查**。
3. **p13-07 信度量化缺公式**：ICC 与典型误差（TE）原文仅定性（"ICC 用作重测信度、TE 合并设备误差+生物学变异"），未给解析式与可接受阈值。已并入 U6 并在此登记，未用常识补齐。
4. **p14-03 全尺度幂指数 b 未给数值**（原文明言"仍存争议"）；**f14-13 动作筛查"哪种最适用无共识、与损伤关联未确立"**；**p14-18 30-15 IFT"每变向 0.7 s"折算距离的完整式未给**；**p14-07 Wingate"功=阻力×转数"单位换算未细化**；**f13-01 Figure 13.1 中间步骤与 f13-02 四维权重未展开**。以上均为"部分条件缺失"，已在各单元标注，不补造。
5. **无障碍**：T20–T23、T40 均在本簇找到候选并验证；无"本簇确无候选"的任务。
6. **ce14-08 的预防措施原文未给**（作者仅标注数据"descriptive, not normative"）——已在 U25 以"强制核对样本/协议/年代"的 B 段约束承接，未虚构原文未给的判据。

---


## 簇 D1-plyometric — 快速伸缩复合训练设计

| task_id | 任务 | 原文位置 | 对应候选 | decision | 去向 |
|---|---|---|---|---|---|
| T14 | 设计快速伸缩复合（plyometric）训练计划 | Ch19 Needs Analysis/Program Design（第 262–292、652–685 行）；Intensity/Volume（Table 19.5/19.6，第 460–619 行）；Frequency/Recovery（第 542–590 行）；Progression（第 621–666 行）；Pretraining Eval（第 900–1044 行）；Age（第 695–808 行）；Warm-Up（第 667–749 行）；Safety（第 888–1137 行）；Integration（第 817–887 行） | f19-01..f19-14；p19-01..p19-27；c19-1..c19-6；ce19-01..ce19-11 | verified×9 + reference×2 | cap.nsca.plyometric-program-design-sop / plyometric-intensity-volume / plyometric-frequency-recovery / plyometric-progression / plyometric-pretraining-screen / plyometric-age-adjustment / plyometric-warmup-ramp / plyometric-safety-troubleshooting / plyometric-integration-complex；reference→glossary/overview（plyometric-drill-catalog、ssc-mechanism） |

- 覆盖结论：T14 全流程（需求分析→强度/量→频率/恢复→进阶→评估→年龄裁剪→热身→安全→整合）在本簇均有两处以上原文支撑的候选，无遗漏。
- 交界说明：`f20-11`（SSC 训练设计两判据）属簇 D2（速度敏捷），本簇不重复收录；本簇仅收 `f19-08`（与抗阻整合 / complex training）与 `f19-14`（与有氧排序），均并入 U9。


### 簇 D1-plyometric 缺口清单

- **critical/high 任务缺口**：无"缺失候选"级缺口；但以下为原文固有信息不足，已如实保留、不在验证阶段用常识补齐：
  1. Table 19.5 各因素**无权重/无量化评分**（原文第 490–519 行）→ 强度档判定除查表分档外仍为定性（影响 U2）。
  2. p19-02 过渡相能量损失仅 4 个离散点、**无闭式公式**且仅卧推数据 → 降为 reference（REF-1）。
  3. **量–强度个体化换算曲线缺失**：原文未给把距离（bounds）换算成触地次数的公式，也未给各水平下强度×量的连续换算（Table 19.6 为区间档）。
  4. **无"可开始 plyo 的通用年龄"**；儿童起始量（50–60 跳/节）未按体重/强度分级（U6 已标注）。
  5. 同日"重抗阻+plyo"的**量化疲劳阈值**、complex training **最优组间休息**，原文均未给（U9 已标注）。
  6. 深跳箱高对 **<100 kg 者无精确上界**（仅给总区间 16–42 in 与常规 30–32 in，U8 已标注）。


## 簇 D2-speed-agility — 速度与敏捷训练设计

| task_id | 任务 | 原文位置 | 对应候选 | decision | 去向 |
|---|---|---|---|---|---|
| T15 | 设计速度与敏捷训练计划（Table 20.6/20.7/20.9/20.11） | Ch20: 1906–2520 | U3(f20-04,p20-25/26/27,p20-32,c20-2/3/4), U4(f20-08,p20-24,c20-1/6), U6(p20-17,f20-06,p20-15/16), U7(f20-07,p20-30,f20-13,p20-31), U8(f20-05,p20-08/09/10), U11(f20-15,p20-23), U12(f20-10,p20-28), U13(p20-14,f20-11,p20-07), U14(f20-03,p20-11/12), U15(f20-18) | verified（U15=reference） | cap.nsca.agility-needs-to-program / speed-short-to-long-periodization 等 |
| T16 | 区分变向能力与敏捷，并按需选择训练手段（"COD deficit"等指标口径） | Ch20: 1140–1283, 1235–1243, 2350–2384 | U1(f20-01,p20-01,f20-16,p20-21,ce20-04), U2(f20-09,p20-19,p20-20,c20-5), U3(f20-04,p20-32,c20-2), U7(f20-07,p20-30), U8(f20-05,p20-08/09/10) | verified | cap.nsca.speed-cod-agility-attribution（专责判定）+ cap.nsca.speed-force-metrics |

> 说明：T15 的「设计完整速度/敏捷计划」由 U3（敏捷侧）+ U4（速度侧）两条可执行链共同覆盖，并以 U6/U7/U8/U11/U12/U13/U14 提供手段、进阶、取向、变量与常模支撑，故 task 层覆盖完整。


### 簇 D2-speed-agility 缺口清单

- **RSI（reactive strength index）计量口径缺失**（用户特别提示的力学指标之一）：Ch20 仅有 "reactive strength development is also a key training priority"（第 1183–1186 行）等定性表述，**未给 RSI 公式与单位**。RSI 数值口径应属 Ch19（plyometric，其他簇）；本簇 U2 不含 RSI，勿用常识补公式。
- **impulse / momentum / COD deficit / sprint momentum 的 SI 单位**：原文未显式给出（N·s、kg·m/s），U2 已如实标注为待补规范项，进入阶段 2 的 B/E 段。
- **Table 20.8/20.12 各监控变量的常模/目标值**：原文未给，只能做「变化方向」解读，不能做「达标判定」；已记入 U10。
- **速度/COD/敏捷的域专属周期化步骤**：Ch20 未展开（U15 仅桥接语句），须依赖 Ch22（其他簇）；本簇不重复制造该 SOP。


## 簇 E-aerobic — 有氧耐力训练与强度分区

| task_id | 任务 | 原文位置 | 对应候选 | decision | 去向 |
|---|---|---|---|---|---|
| T18 | 计算目标心率与强度分区（5 区/3 区） | Ch21 Step 3；Table 21.1/21.2/21.3；Target HR sidebar | p21-02..09, p21-24, p21-28, f21-02, c01-01, c01-02, c21-1..4 | verified | cap.nsca.aerobic-intensity-zones-target-hr（U1） |
| T17 | 设计有氧耐力训练计划（5 步变量） | Ch21 5 变量 + Table 21.4 | f21-01, p21-01, f21-04, p21-10, p21-14..18, f21-15, p21-27 | verified | cap.nsca.aerobic-program-design（U2） |
| T17 | 进阶规则（≤10%/周、单变量、按时间） | Ch21 Step 5；第 699–775 行 | f21-06, p21-12, p21-13, c21-10 | verified | cap.nsca.aerobic-progression-rule（U3） |
| T17 | 赛季化计划变量分配 | Ch21 Table 21.5；第 1012–1085 行 | f21-05, p21-11, c21-11 | needs_review | U10（Table 21.5 in-season 行源抽取错位，缺口待补） |
| T17 | 同期训练处理 | Ch21 第 1359–1511 行；Ch3 | f21-10, p21-20, p03-18 | verified | cap.nsca.concurrent-training-management（U5） |
| T17 | 赛前减量 | Ch21 第 1328–1357 行 | f21-09, p21-19 | verified | cap.nsca.tapering-model（U6） |
| T17 | 热适应 | Ch21 第 1546–1630 行 | f21-11, p21-21 | verified | cap.nsca.heat-acclimation（U7） |
| T17 | 高原/LHTL | Ch21 第 1512–1545 行 | f21-14, p21-22 | verified | cap.nsca.altitude-lhtl（U8） |
| T17 | 恢复会话使用 | Ch21 第 360–377 行 | f21-13, p21-26, ce21-03 | verified | cap.nsca.recovery-session（U9） |
| T17 | 交叉训练/停训 | Ch21 第 1292–1326 行 | f21-07, p21-25, f21-08 | reference | R2 → overview |
| T17 | 强度/剂量边界（MED/MTD 等） | Ch21 第 70–96、417–422 行 | f21-03, f21-12, f21-16, p21-23 | reference | R1 → overview |
| T37 | 判断主导供能系统并设间歇训练比 | Ch3 Table 3.2/3.6 | f03-01, p03-01, p03-06, p03-07 | verified | cap.nsca.energy-system-interval-ratio（U4） |
| T37 | 底物/限制因素口径（旁证） | Ch3 Table 3.4 等 | p03-04（及 p03-02..17） | reference | R3 → glossary/overview |

---


### 簇 E-aerobic 缺口清单

1. **[T17 · 高] Table 21.5 in-season 行源抽取错位（U10 → needs_review）**：`ch21.txt` 第 1035–1053 行的 beginner/advanced in-season 行，其"时长"与"强度"列三档被拆到两个文本块，列对齐无法唯一确证。需高保真来源重读该表后才能恢复完整查表能力。off-season/preseason/postseason 行与"季节目标/变量方向"散文结论可读。
2. **[T17 · 中] 热适应被动暴露 30 min 值待回查 Ch6**：ch21.txt 热适应段未直接给出"被动热暴露 30 min"，该值来自候选 f21-11 的概括，阶段 2 应回查 Ch6《Heat Acclimatization》节确认（不影响 U7 主流程）。
3. **[T37 · 中] 间歇比的循证不足（已保留）**：ch03.txt 第 1181–1182 行原文自认"需更多研究给出最优工作-休息比的循证推荐"，Table 3.6 仅为一般性指引——已记入 U4 的 V1 与 B 段，不作为"最优处方"宣称。
4. **[本簇无可执行处方的边界项] R1/R2 已如实降级为 reference**（MED/MTD、交叉训练、停训），未用常识补造其量化阈值。

> T17/T18/T37 三个任务在本簇**均有对应候选**，无"其他簇负责"造成的空缺；唯一阻塞是 Table 21.5 的源保真问题（缺口 1）。

---


## 簇 F-preparation-technique — 准备活动 / 柔韧 / 技术 / 护腰 / 保护 / 替代器械

| task_id | 任务 | 原文位置 | 对应候选 | decision | 去向 |
|---|---|---|---|---|---|
| T19 | 设计准备活动（RAMP）与柔韧训练 | Ch15；Table 15.1/15.2/15.3 | U1：f15-01/02/03/04、p15-01..11、c15-1/2/4 | verified | cap.nsca.warmup-ramp |
| T19 | （柔韧训练编程部分） | Ch15 静态/动态/PNF | U2：f15-06..13、p15-05/12/14..24、c15-3、ce15-01..07 | needs_review | 参数口径冲突待裁定（静态 10–30 s vs 15–30 s；PNF 3–6 s/≤20%MVC vs 6–10 s） |
| T24 | 技术规范：呼吸、身体稳定、护腰使用 | Ch16 | U3：f16-01..05/13、p16-*；U4：f16-06/p16-09；U6：f16-14..16/p16-20/21 | verified | cap.nsca.exercise-technique-basics / weight-belt-decision / power-exercise-phases |
| T25 | 保护（spotting）规则与判断 | Ch16 | U5：f16-07..12/18、p16-10..17、c16-2、ce16-04..07/10 | verified | cap.nsca.spotting-rules |
| T26 | 替代模式与非传统器械的训练应用 | Ch17 | U7：f17-04..08、p17-10..18、c17-1/4；U8：f17-09/10、p17-19..22、c17-2/3；U9：f17-01..03/11/13..16/21/22、p17-*；U10：f17-12/p17-26 | verified（U7/U8/U9/U10）；N14/N15 needs_review | cap.nsca.variable-resistance-load / ael-programming / alternative-modes-decision / technique-error-correction |

- T19、T24、T25、T26 均在本簇有对应候选，覆盖完整（无"其他簇负责"项）。
- 本簇不负责的 Ch15–17 外移内容：Ch18 training status 分类（供 U9 引用）、Ch16 逐动作技术细节（作 R11 资源）、Ch17 逐动作技术细节（作 R11 资源）——按 BOOK_OVERVIEW 4.2 归入参考而非独立能力。


### 簇 F-preparation-technique 缺口清单

1. **【高优先·阻断】柔韧参数口径冲突（T19/U2）**：原文对静态拉伸保持时长（10–30 s vs 15–30 s）与 PNF 收缩参数（3–6 s/≤20% MVC vs 6–10 s/中等强度）自相矛盾且未澄清适用边界 → 转 needs_review，需回读或专家裁定后方可进能力池。
2. **【中优先·边界】护腰"接近最大/最大"缺 %1RM 量化阈值（T24/U4）**：判据对清晰情形可执行，模糊区（如 70%1RM 后蹲）无法自动裁定；登记为 B 段边界，不以常识补阈值。
3. **【中优先·边界】爆发力动作无阶段时间/角度阈值（T24/U6）**：高翻/抓举/推举/中腿拉的阶段结构为定性描述；登记为 B 段边界。
4. **【中优先·缺口】Ch15 动态拉伸与 Ch16 各动作"常见错误"仅列症状、无纠错闭环（T24/R13）**：与 Ch17 轮胎翻转的 flaw→correction 形成对比；若需要纠错能力须补读或另据他源。
5. **【低优先·待核查】原木直径单位标注错误（T26/N14）**：250 mm=1.0 in.、316 mm=1.2 in. 明显矛盾，原文错误，口径未决 → needs_review。
6. **【低优先·待核查】弹力带预测方程自变量单位未定义（T26/N15）**：x 量纲不明且与表中值不符 → needs_review；查表分支不受影响。


## 簇 G-populations-nutrition-psych — 特殊人群 / 营养补水 / RED-S / 增补剂 / 心理

| task_id | 任务 | 原文位置 | 对应候选 | decision | 去向 |
|---|---|---|---|---|---|
| T30 | 青少年与老年人抗阻训练调整 | Ch7（ch07.txt 203–216, 484–497, 1442–1454）；Ch5/Ch7 | p07-01…p07-25, f07-01/02/03, c07-01, ce07-01…05 | verified / reference | U1 青少年处方、U2 成熟度评估、U3 老年人处方（+U6/U23 支持） |
| T31 | 女性运动员训练考量 | Ch8；Table 8.1/8.2 | p08-01…p08-21, f08-01/02, ce08-01 | verified / reference | U4 女性降伤与健康、U5 孕期/产后（+U6 性别差异 reference） |
| T32 | 制定补水与电解质方案 | Ch10；Table 10.15 | p10-16…p10-22, f10-02, c10-01, c11-02, ce10-01/02 | verified | U9 补水与电解质方案（含汗液率/分年龄处方） |
| T33 | 赛前/赛中/赛后营养策略 | Ch11；Table 11.1/11.2 | p11-01…p11-15, p11-28, f11-01/02, c11-01, ce11-02/03 | verified | U10 竞赛营养时间线、U11 体成分干预、U7 宏量与能量需求（+U8 GI/GL、U14 评估口径） |
| T34 | 识别 RED-S 与进食障碍并转诊 | Ch11 | p11-21…p11-26, f11-03, ce11-01/04 | verified | U12 EA/RED-S、U13 进食障碍/RWL 转诊 |
| T35 | 评估增补剂证据与风险 | Ch12；Table 12.1/12.2 | p12-01…p12-30, f12-01/02, ce12-01…05 | verified / reference | U15 证据评估、U16 滥用识别、U17 剂量处方（+U18 名称/剂量 reference） |
| T36 | 心理技能与唤醒调控 | Ch9 | p09-01…p09-32, f09-01…04, c09-01, ce09-01…03 | verified | U19 唤醒/心理技能、U20 动作技能教学、U21 心理健康转诊、U22 伤后心理支持 |

> 附：p05-*/p06-*/f05-01/f06-01/p07-14（基础适应，47 条）不映射 T30–T36，已纳入 U23（verified）与 U24（reference），未丢弃。


### 簇 G-populations-nutrition-psych 缺口清单

- **无 critical/high 任务缺候选**：T30–T36 均有对应候选且已归并为能力单元。
- **原文缺（非候选漏抄）——已限定范围，未补造**：
  - `p10-06` 低热量期蛋白上调「每降 100 kcal ≈ +1%」：原文无精确公式与上下限 → U7 仅作经验换算。
  - `p10-11` GL 缺高/中/低分档阈值与每日目标 → U8 只做 GI 分档。
  - `p11-04` 「正常糖原水平」基线未定义 → U10 以「较正常 +20%–40%」表述，不虚构基线。
  - `p11-20` 目标体重式百分号书写歧义 → U7 walkthrough 按 FFM ÷ 期望去脂体重占比处理并标注。
  - `p11-21` 缺运动能量消耗测算方法、30–45 过渡区命名 → U12 只做 45/<30 阈值判定 + 亚临床表述。
  - `p11-02` 赛前档仅耐力口径；`p11-09` 漱口缺浓度/频次 → U10 沿用原文区间、不扩项。
- **口径冲突（`p10-16`）已解决**：Table 10.15 Body weight EUH `<1%` vs 正文脱水预警 `≥2%` 为不同目的阈值，可并存（详见文首）。相关单元 U9 判 verified，未登记 needs_review。
- **候选漏抄核查**：本簇营养候选报告中标注的 ~26 处 `missing_conditions`，回查原文后确认**均为「原文缺」**（公式/阈值/单位原文本身未给），未发现「原文有而候选漏抄」的数值。


## 簇 H-recovery-management — 过度训练与恢复 / 康复再训练 / 场地与管理

| task_id | 任务 | 原文位置 | 对应候选 | decision | 去向 |
|---|---|---|---|---|---|
| T27 | 识别与区分过度疲劳/过度训练 | Ch24（ch24.txt §174–539、590–1111） | f24-01/02/03/05/06/07/08/10, p24-01..10/12..16/19..21, ce24-01..05/07..10, c24-3, c24-4 | verified | U1–U4、U6 |
| T28 | 选择恢复策略 | Ch24 Table 24.4（§922–1022） | f24-09, p24-11/17, c24-1, c24-2；预防项 U6 | verified | U5（+U6 预防） |
| T29 | 康复与再训练阶段的负荷调整 | Ch23 Table 23.2/23.3（§802–1002） | f23-01..11, p23-01..21, ce23-01..05, c23-1..4 | verified | U7、U8、U9、U10、U11 |
| T38 | 场地空间估算与设备布置 | Ch25 Table 25.1/25.2（§798–1010） | f25-01..08, p25-01..18, ce25-01..05, c25-1, c25-2 | verified(U12)+reference(U13) | U12（可核算）；U13 并入 overview |
| T39 | 制定设施政策、应急预案与风险管理 | Ch26 Table 26.1（§158–196、1165–1286） | f26-01..11, p26-01..21, ce26-01..09, c26-1..3 | verified(U15,U16)+reference(U14) | U15、U16；U14 并入 overview，p26-05 入 glossary |

**簇表漏列说明**：`_clusters/H-recovery-management.md` 的候选表仅含 c23-1…4，**未列** c24-1…4 / c25-1…2 / c26-1…3；但任务书明确要求纳入 `cases-g2-ch15-26.md` 的 c23-*/c24-*/c25-*/c26-*。本验证已补齐并计入 163 条（154+9），未造成候选静默丢失。
**归属澄清**：`frameworks-g4-ch20-22.md` 的 f22-09/10/11（GAS、刺激—疲劳—恢复、体能—疲劳范式）**属 B 簇**，本簇未重复收录；簇表注记的“g4（Ch24 部分）”经回查为误标。

---


### 簇 H-recovery-management 缺口清单

- **p23-05（U7）**：成熟—重塑期"数月至数年"跨度过大且无个体推算方法；重返判据的具体数值原文未给（重返数值判据仅由 p23-17 的 <10% 对侧差异部分覆盖）。**不补造**。
- **p23-17（U11）**：<10% 对侧差异判据来自**单一引用（ch23 引 60）**，样本人群与测试协议未明，原文用 "may be considered" 属建议性。
- **p24-14（U6）**：>30% 训练量警戒线为原文**唯一数值**，但口径（单周？累计？按何标量）未明；其余规避条目为定性建议、无剂量。
- **p24-07（U3）**：Table 24.1 中离心力量、多/单关节 RFD 等敏感度为 Unknown/"Unknown onset"，无变化幅度阈值；"Within 1 week" 等也无百分比切点。
- **U10（热病/低温）**：补液量、降温目标温度、复温速率、发病环境温湿度阈值原文未给。
- **U13/U14（T38/T39）**：管理流程强依赖美国法规（ADA/OSHA/ANSI-ASHRAE/NCAA/HIPAA/911）与院校体制，**跨法域需重新校验**；已按 reference 出栈。
- **全局**：凡涉及法规/标准/单位者（U12、U13、U14、U15、U16），一律为美国语境 + 英制口径，跨法域须重新校验——这不是缺陷，但须在 B 段如实呈现。

---
