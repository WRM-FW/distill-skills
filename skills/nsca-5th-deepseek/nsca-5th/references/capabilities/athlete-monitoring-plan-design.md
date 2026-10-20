# 运动员监控计划设计（测试质量 + 敏感度排序 + 问卷选择）

## R — 原文 (Reading)

> "Qualities of the tests included in this program must be specific to the training being performed or the physiological system involved (i.e., valid), reliable (i.e., capable of providing consistent results), sensitive to the training and competition stimulus, and easy to incorporate into the regular athlete monitoring program. Furthermore, those administering the tests must precisely follow correct protocols and must ensure that each person performing the tests provides a maximal effort. If the tests are not administered correctly, the data acquired will be meaningless."

— Chapter 24 · Assessment of Overreaching and Overtraining（`ch24.txt` 第 594–606 行）

## I — 自述 (Interpretation)

设计一套**早期识别过度训练**的监控方案，核心不是"多测"，而是"测得对、测得准、读得快"：

1. **四项测试质量**：① **specific/valid**（对训练或生理系统特异/有效）② **reliable**（一致可重复）③ **sensitive**（对训练/竞赛刺激敏感）④ **easy to incorporate**（易纳入常规监控）。
2. **施测纪律**：施测者必须精确遵循协议；须确保受试者**尽最大努力**——否则数据无意义。
3. **数据回路**：需高效数据管理系统，**快速回传**结果，才能及时调整训练。
4. **指标优先级看敏感度**：不是所有指标同时下降。原文给出敏感度与出现顺序的排序表（Table 24.1）——**速度（冲刺）最敏感、最先下降**，其次功率，**最大力量最后下降**；恢复感知（perceptions of recovery）敏感度极高、数天内即可反映。
5. **主观问卷**：原文认为主观测量可能**比定量指标更有用于监控**（`ch24.txt` 第 819–827 行），选问卷有 6 条考量（长度/是否验证过/措辞易懂/能否快速处理/可否无胁迫作答/是否对过度训练刺激敏感）。
6. **监控面要全**：Figure 24.15 汇总量/生理/表现/心理/睡眠/教练主观评估等多维指标。

一句话：**速度功率优先、主观项不可省、施测纪律决定数据是否可用。**

## A1 — 案例 / 演练 (Application)

**原书素材（tabular-example · c24-4 / Figure 24.15，`ch24.txt` 第 776–817 行）与 Table 24.3 问卷清单（第 856–921 行）**：原文给出可执行的监控指标清单与问卷清单，**但明确原书不提供阈值**（监控项为罗列，非"低于 X 即报警"）。

**合成演练（明确标记）**：为某大学女子足球队设计"早期发现过度训练"的监控方案。
- 依四项质量 + Table 24.1 敏感度排序：优先纳入**冲刺速度（High，1+ 周）与纵跳动力学（High，1 周内）**，加**恢复感知（Very high，数天内）**与**训练意愿/自我效能（High，1 周内）**。
- **不**把 1RM 作为首发预警（Table 24.1 中敏感度 Low、最后发生）。
- 问卷据 6 条考量选取经效度验证、能快速回传者（如 RPE/CR10、恢复-压力类短量表）。
- 建立快速数据反馈通道后再定报警规则（原文未给阈值）。

## A2 — 未来触发 (Trigger)

**用户情境**：
1. 要"建一套监控体系，早点发现谁快练崩了"。
2. 问"我该测哪些指标来盯过度训练？"
3. 纠结用客观指标还是主观问卷。
4. 现有监控测了很多项但发现不了问题，想知道怎么选/怎么排优先级。
5. 想知道监控测试怎么做才算合格（施测规范）。

**语言信号（中英双写）**：运动员监控 / 监控指标 / 选什么指标 / 早期发现过度训练 / 监控问卷 / 主观 vs 客观 / 施测规范 / athlete monitoring / monitoring battery / which markers / RPE questionnaire / early detection of overtraining / internal and external load。

**与相邻能力的区分（初稿）**：本卡管"**监控方案设计**"。具体某类体能测试的协议在测试评估簇（`cap.nsca.max-strength-test-protocols`、`jump-power-test-protocols` 等）；测试质量（效度/信度）的通用判定在 `cap.nsca.test-selection-validity`；测后数据解释在 `cap.nsca.sport-specific-test-battery` 等。**与"测试与评估"簇不同**：那一簇是"如何把任何能力测准"，本卡是"为**早期发现过度训练**这一目的如何选指标、选问卷、定施测纪律"。若已选定指标、只差"升级检测" → `cap.nsca.overtraining-test-escalation`。

## E — 执行 (Execution)

**输入契约（必需）**：训练目标与专项（决定"特异"）；可用人力/时间/软件（决定"易纳入"）；队内现有测试项；数据回传时效要求。**可选**：已有客观指标清单、问卷库。
- **缺失处理**：缺"专项/训练负荷特征"→ 无法判断特异性与敏感度，先问；不得默认可照搬通用清单。

**步骤与完成标准**：
1. **过四项质量闸**：候选指标逐项判定 valid / reliable / sensitive / easy。完成标准：每项给"通过/不通过 + 理由"。
2. **按敏感度排序选首发预警**：优先速度/冲刺、功率（含纵跳动力学）、速度型抗阻动作、EMG-to-force 效率，以及**恢复感知**等主观项；把最大力量放为**后置**而非首发。完成标准：指标清单按敏感度/发生顺序排好（依据 Table 24.1，见 `resources/overtraining-monitoring-checklist.md`）。
3. **选问卷**：按 6 条考量（长度、是否验证、措辞、可否快速处理、可否无胁迫、对 OT 刺激是否敏感）筛，优先短期、经验证、可快速回传者。完成标准：选定 1–N 份问卷 + 逐条理由。
4. **定施测纪律**：写明协议、施测者训练、最大努力保障（参照 `ce24-04`）。完成标准：可被他人照做。
5. **建快速数据回路**：定义采集→处理→回传→调整的链路与时限。完成标准：写明时限与责任人角色。
6. **覆盖多面**：确认监控覆盖 内/外部负荷、生理、表现、心理、睡眠、教练主观 等维度（参照 Figure 24.15）。完成标准：各维至少一项。
7. **输出监控方案**。

**输出契约**：`{指标清单(按敏感度排序), 问卷清单+理由, 施测规范, 数据回路/时限, 维度覆盖检查, 已知缺口}`。**约定**：原文**未给阈值**（Table 24.1 中多项为 "Unknown onset"、无百分比切点）——本卡只产出"监控什么 + 怎么测 + 怎么回传"，**不虚报报警阈值**；阈值须由队内基线自行建立并标注为约定。

**判停点/分支**：
- 某候选指标无法满足 valid/reliable → 剔除，不因"流行"而纳入。
- 施测无法保证最大努力/协议一致 → 标"数据将无意义"（`ce24-04`），先修正流程。
- 只盯力量、忽略速度功率早期窗口 → 明确纠正（`ce24-10`）。
- 一旦监控发现可疑趋势 → 交 `cap.nsca.overtraining-test-escalation` 升级。

## B — 边界 (Boundary)

- **不要**只测最大力量来预警——原文明言速度/功率更早下降，力量最后下降（`ce24-10`）。
- **不要**忽略主观问卷——原文认为主观测量可能**比定量更有用**。
- **不要**在施测不规范、未确保最大努力时采信数据（`ce24-04`）。
- **原文自认的局限（B 段主依据）**：生理/医学测试的"meaningfulness has been equivocal, dependent on the subjects being studied, the training program being performed, and the sport being monitored"（`ch24.txt` 第 683–687 行）；监控指标只是**趋势信号**，不是诊断。
- **阈值为零**：原文不给阈值；本卡**禁止**编造"低于 X 即过度训练"。
- **作者盲点（BOOK_OVERVIEW 3.3-4）**：量表与自评的可靠性依赖受试者经验与诚实度，原文对其**失效条件讨论不足**。
- **抽血/医学检测越界**：原文声明体能教练"does not typically order medical or laboratory tests"（`ch24.txt` 第 679–681 行）；医学检测须由医疗人员负责。
- **专业边界**：疑似疾病/心理问题 → 转诊，不由监控数据自诊。
- **相邻易混**：测试评估簇（测准任何能力）、`cap.nsca.overtraining-test-escalation`（升级检测）。

## 相关能力

- 组合（常配合使用）：`aerobic-recovery-session`
- 组合（常配合使用）：`in-season-load-management`
- 组合（常配合使用）：`monitoring-protocol-design`
- 组合（常配合使用）：`overtraining-test-escalation`
- 组合（常配合使用）：`rpe-rir-srb-load`
- 组合（常配合使用）：`speed-agility-monitoring`
- 组合（常配合使用）：`swc-effect-size`
- 组合（常配合使用）：`training-volume`
- 组合（常配合使用）：`underperformance-attribution-triage`

## 配套资源

路径相对于本文件；脚本需先检查运行条件，不因附带而自动执行。

- [resources/overtraining-monitoring-checklist.md](../../resources/overtraining-monitoring-checklist.md)
