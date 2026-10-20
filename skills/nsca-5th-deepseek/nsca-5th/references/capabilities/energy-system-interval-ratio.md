# 由专项主导供能系统推导间歇训练比（T37）

## R — 原文 (Reading)

> "90-100 % of maximum power / Phosphagen / 5-10 s / 1:12 to 1:20; 75-90 / Fast glycolysis / 15-30 s / 1:3 to 1:5; 30-75 / Fast glycolysis and oxidative / 1-3 min / 1:3 to 1:4; 20-30 / Oxidative / >3 min / 1:1 to 1:3." ... "it should be noted that more research is necessary to provide evidence-based recommendations for optimal work-to-rest ratios."

— Chapter 3 · Table 3.6 "Using Interval Training to Train Specific Energy Systems"（`ch03.txt` 第 1184–1195 行）与紧随其后的告警（第 1180–1182 行）

## I — 自述 (Interpretation)

间歇训练的"工作-休息比（W:R）"不应凭经验偏好拍脑袋，而可由专项的**代谢画像**推出。两步链：

**第一步 · 定位主导供能系统（Table 3.2）**：由"事件时长 × 强度"查表——0–6 s 极高强度 → 磷酸原；6–30 s 很高 → 磷酸原 + 快速糖酵解；30 s–2 min 高 → 快速糖酵解；2–3 min 中 → 慢速糖酵解 + 氧化；>3 min 低 → 氧化。前提口径：假设运动员为该事件**尽全力**（best effort）。

**第二步 · 由供能系统查工作时长与 W:R（Table 3.6）**：见 R 段。方向规则：**强度越高、时长越短 → W:R 越大**（休息越长，利于磷酸原再合成）。机制上，CP 半时约 30 s，但完全再合成需 3–5 min（可达 8 min），故短时高强度需要更大的 W:R。

**关键边界**：原书自认 Table 3.6 只是"基于代谢时程的一般性指引（general guidelines）"，并明确"**more research is necessary to provide evidence-based recommendations for optimal work-to-rest ratios**"——即它是**方向性启发**，**不是循证最优值**，使用时须配个体监测。

## A1 — 案例 / 演练 (Application)

**原书未提供数值案例**（Table 3.2/3.6 为规则表，无配套例题）。以下为**明确标记的合成演练**，按原书规则可复算：

- **情境 A（篮球反复约 4 s 最大冲刺）**：事件时长 4 s → Table 3.2 属"0–6 s / 极高强度"→ 主导 = **磷酸原** → Table 3.6：强度段 90–100% 最大功率、典型工作时长 **5–10 s**、W:R = **1:12 至 1:20**。
- **情境 B（200 m 冲刺约 25 s）**：时长 25 s → Table 3.2 属"6–30 s / 很高强度"→ 主导 = **磷酸原 + 快速糖酵解** → Table 3.6：75–90% 最大功率、工作时长 **15–30 s**、W:R = **1:3 至 1:5**。

（`_verified/E-aerobic.md` V2 walkthrough 记录此二例纸面演练结果可核对。）

## A2 — 未来触发 (Trigger)

**用户会在什么情境下遇到这类问题**
1. 问"这个项目的间歇训练该怎么设工作-休息比"。
2. 已知专项事件时长/强度，想反推该练哪个供能系统、工作段多长、休息多长。
3. 要给一个高强/爆发型专项（如篮球、短跑、举重类反复冲）设计间歇结构。
4. 想把"代谢特异性"落到具体 W:R 数字，而非笼统说"多休息"。

**语言信号（中英双写关键 trigger）**
- 中文：「工作-休息比怎么定」「间歇训练比」「这个项目该练哪个供能系统」「磷酸原/糖酵解/氧化主导」「W:R 是多少」「代谢特异性间歇」
- English: "work-to-rest ratio", "interval training ratio", "which energy system is primary", "phosphagen vs glycolysis", "metabolic specificity of intervals", "rest between intervals for sprints"

**与相邻能力的区分（初稿，阶段 3 回填）**
- 与 `aerobic-program-design-five-variables`：那张给有氧五类训练的 W:R **示例值**（Table 21.4）；本卡是**由专项代谢画像反推** W:R 的通用推导（T37），跨有氧/无氧都适用。
- 与 `aerobic-intensity-zones-target-hr`：那张管心率/百分比强度档，本卡管时长与间歇比。
- 与 `nsca-plyometric-design`、`nsca-speed-agility-design`：那两张管落地/力学/技术，本卡只管代谢时程与间歇结构。

## E — 执行 (Execution)

**输入契约**
- 必需：① 专项/目标事件；② 该事件的关键持续时长（秒/分钟）；③ 该时长对应的努力强度（极高/很高/高/中/低，或 % 最大功率）；④ 目标（练哪个供能系统）。
- 缺失处理：只给项目名不给时长/强度 → 先补测或询问典型单次连续全力时长；无强度信息时用"事件尽全力"作默认前提（原书 Table 3.2 note）。

**执行步骤（两步查表 + 校验）**
1. **定位主导供能系统（Table 3.2）**：

   | 事件时长 | 强度 | 主导供能系统 |
   |---|---|---|
   | 0–6 s | 极高 | 磷酸原 |
   | 6–30 s | 很高 | 磷酸原 + 快速糖酵解 |
   | 30 s–2 min | 高 | 快速糖酵解 |
   | 2–3 min | 中 | 慢速糖酵解 + 氧化 |
   | >3 min | 低 | 氧化 |

   完成标准：写出主导系统。
2. **查工作时长与 W:R（Table 3.6）**：

   | % 最大功率 | 主导系统 | 典型工作时长 | 工作-休息比 |
   |---|---|---|---|
   | 90–100 | 磷酸原 | 5–10 s | 1:12 至 1:20 |
   | 75–90 | 快速糖酵解 | 15–30 s | 1:3 至 1:5 |
   | 30–75 | 快速糖酵解 + 氧化 | 1–3 min | 1:3 至 1:4 |
   | 20–30 | 氧化 | >3 min | 1:1 至 1:3 |

   完成标准：给出典型工作时长 + W:R 区间。
3. **方向一致性校验**：强度越高→工作时长越短→W:R 越大。完成标准：结果与该方向规则一致；若目标供能系统与所选强度段矛盾，回到 Step 1 重定强度。
4. **落地与标注（约定）**：把 W:R 转成具体"工作秒数 : 休息秒数"（如情境 A 取 1:12 → 5 s 工作 / 60 s 休息）。**完成标准：每条处方标注所用档位 + 原文告警**。

**判停点/分支**
- 事件为混合/间歇性项目（如球类反复冲刺）→ 以"单次最长全力时长"而非整场时长定位主导系统，否则会误落到氧化系统。
- 目标涉及有氧区（>3 min）→ 转交 `aerobic-program-design-five-variables` 用 Table 21.4 口径。

**输出契约**
- `{专项, 关键时长, 强度, 主导供能系统, 典型工作时长, W:R 区间, 具体工作:休息秒数, 循证告警}`。

## B — 边界 (Boundary)

- **不要用**：当目标是有氧耐力的频率/时长/进阶时（用有氧簇对应卡）；当问题落在落地力学/技术（用 plyometric / speed 卡）。
- **作者警告的失败模式（须保留告警）**：原书明确 **Table 3.6 不是循证最优值**——"more research is necessary to provide evidence-based recommendations for optimal work-to-rest ratios"（`ch03.txt` 第 1180–1182 行）。故本卡只把 W:R 当"基于代谢时程的方向性指引"，**不得宣称某 W:R 为最优处方**，实际使用须配个体监测。
- **盲点（BOOK_OVERVIEW 步骤 3）**：Table 3.2 的强度分级为**定性描述**（极高/很高/…），原文未给对应 % 最大功率的定量阈值；机制章节（生物能学）更新快，"机制过期而处方仍被引用"有滞后风险；共识/惯例 ≠ 实证；竞技术语（best effort）迁移到普通健身人群需额外判断。
- **相邻易混**：`aerobic-program-design-five-variables`（Table 21.4 的 W:R 示例）、`nsca-plyometric-design`（落地与量进阶）。

## 相关能力

- 组合（常配合使用）：`aerobic-program-design-five-variables`
- 组合（常配合使用）：`anaerobic-capacity-test-protocols`
- 组合（常配合使用）：`primary-training-goal`
