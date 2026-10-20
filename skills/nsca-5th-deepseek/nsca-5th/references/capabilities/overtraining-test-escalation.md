# 分级检测升级协议（Category I → II → III）

## R — 原文 (Reading)

> "It is suggested that category I testing be performed first. If the results suggest possible overtraining concerns, testing for category II is warranted. Likewise, if the category II test suggests an overtraining problem, a category III test may be performed. In this manner, unnecessary testing can be avoided."

— Chapter 24 · Integrating Recovery Methods Into the Training Process（`ch24.txt` 第 1107–1111 行）

## I — 自述 (Interpretation)

把"要不要加检测"做成**成本/侵入性递增的三级阶梯**（引 Bernaciková 等），先用便宜快速的，异常才升级，从而**避免不必要的检测**：

- **Category I**：**每日**、易施测、便宜、结果**快速回传**、对教练和运动员方便。（如每日自评 RPE、睡眠、恢复感。）
- **Category II**：**每隔几天**、更复杂、更长的问卷、比 I 稍不便，但仍要求**快速回传**。
- **Category III**：**偶尔**（如每月一次）、更繁琐且更具侵入性、更贵、**回传时间更长**。（如抽血/实验室类。）

**升级规则**：先做 I → 若"提示可能有过训练顾虑" → 升级做 II → 若 II 提示过度训练问题 → 可做 III。
**关键点**：I 正常就**不必**上 II/III；把高成本高侵入的检测留给真正需要的人。

## A1 — 案例 / 演练 (Application)

**原书未提供完整案例**，只给三级分类定义与升级规则（`ch24.txt` 第 1044–1056、1107–1111 行）。

**合成演练（明确标记）**：某运动员 Category I 每日自评（RPE、睡眠、恢复感）连续 5 天呈现恶化趋势。
- 判定："possible overtraining concern" → **升级至 Category II**（每隔几天的更长问卷，仍要求快速回传）。
- **不**直接跳到 Category III（高侵入/高成本），因为 II 尚未提示"过度训练问题"。
- 待 II 若确认问题，再考虑 III。

## A2 — 未来触发 (Trigger)

**用户情境**：
1. 日常监控已发现异常，问"要不要进一步做更深入的检测？"
2. 纠结"该多久测一次、测多深"。
3. 想避免"动不动就抽血做一堆贵检测"。
4. 已有一套分级检测/问卷，问"什么条件下该升级"。

**语言信号（中英双写）**：分级检测 / 检测升级 / 要不要进一步检测 / 多久测一次 / 避免不必要检测 / category I II III / testing escalation / tiered testing / when to escalate monitoring / expensive lab tests。

**与相邻能力的区分（初稿）**：本卡管"**检测等级与升级决策**"。指标/问卷**怎么选、方案怎么建** → `cap.nsca.athlete-monitoring-plan-design`；监控发现趋势后的**分档命名** → `cap.nsca.overtraining-continuum-classification`。**与"测试与评估"簇不同**：那里是"测某个能力"，本卡是"为监控目的决定检测的深浅与升级时机"。

## E — 执行 (Execution)

**输入契约（必需）**：当前**检测级别**（I/II/III）；该级别的**结果**（是否提示顾虑/问题）；可用资源（成本、侵入性容忍度、回传时效）。**可选**：运动员症状与训练背景。

**步骤与完成标准**：
1. **先做 Category I**（每日、快、便宜）。完成标准：有 I 级数据与趋势判读。
2. **判是否"提示可能有过训练顾虑"**：I 级结果是否显示可疑趋势/异常。完成标准：给出"是/否 + 依据"。**否 → 维持 I，结束。**
3. **升级至 Category II**（每隔几天、更长问卷，仍要求快速回传）。完成标准：II 级数据 + 判读。
4. **判 II 是否提示"过度训练问题"**：完成标准：给出"是/否 + 依据"。**否 → 停在 II 或回落 I。**
5. **可做 Category III**（偶尔、更具侵入性、更贵、回传更慢）。完成标准：III 级检测记录与结论。
6. **输出级别轨迹**。

**输出契约**：`{当前级别, 判读结论(顾虑/问题 是·否), 升级建议(停留|升级一级|回落), 每级依据}`。

**判停点/分支**：
- I 正常 → 不升级（避免不必要检测）。
- II 未见问题 → 不升 III。
- **触发升级的"具体阈值"原文未给**：`ch24.txt` 仅用定性表述 "possible overtraining concerns" / "suggests an overtraining problem"。本卡**如实标注此缺口**，不虚构阈值；阈值须结合队内基线与监控方案（U3）自行约定。
- 出现疑似医疗/心理红旗 → 交 `cap.nsca.rehab-scope-and-referral`，由医疗人员决定医学检测，体能教练不自行下单。

**约定**：各级别的"频率/复杂度/侵入性/成本/回传速度"定义取自 `ch24.txt` 第 1048–1056 行，为**定性描述**；本卡不量化。

## B — 边界 (Boundary)

- **不要**跳过 I 直接做高侵入检测——本卡要旨即"避免不必要检测"。
- **不要**在 I 正常时仍升级，浪费资源并增加运动员负担。
- **原文自认的缺口（B 段主依据）**：升级的"具体阈值"原文**未给**，只有定性触发词；本卡**禁止**编造"达到 X 就升级"。
- **医学检测越界**：Category III 若涉及抽血/实验室检测，属医疗范畴，须由医疗人员执行与解读（原文：体能教练 "does not typically order medical or laboratory tests"）。
- **共识≠实证**：三级分类来自 Bernaciková 等的建议，是**实践框架**而非经证实的金标准。
- **变量耦合**：升级决策依赖 I 级趋势判读的质量；若 I 级数据本身不可靠（施测不规范），升级会放大误差。
- **相邻易混**：`cap.nsca.athlete-monitoring-plan-design`（建方案）、`cap.nsca.overtraining-continuum-classification`（命名分档）。

## 相关能力

- 依赖（先理解）：`overtraining-continuum-classification`
- 组合（常配合使用）：`athlete-monitoring-plan-design`

## 配套资源

路径相对于本文件；脚本需先检查运行条件，不因附带而自动执行。

- [resources/overtraining-monitoring-checklist.md](../../resources/overtraining-monitoring-checklist.md)
