# 测试员选拔、培训与施测分工

## R — 原文 (Reading)

> "It is preferable to have the same person administer a given test if time and schedules permit, because this eliminates the issue of interrater reliability. If this is not feasible, the test supervisor can allow simple, well-defined tests (e.g., counting correct push-ups) to be administered by different testers and tests requiring schooled judgment (as of proper form in the squat) to be scored by the most skilled and experienced personnel. As a rule, each tester should administer only one test at a time"

— Chapter 13 · Selection and Training of Testers / Test Format（`ch13.txt:826-834`）

## I — 自述 (Interpretation)

测试的可信度首先由"谁来测"决定，因此需要一套**选拔—培训—校验—分工**流程：

- **新手须被校验**：监督者要确认所有新手能正确地*执行*与*评分*（如掐表记冲刺、判定 1RM 深蹲），并要求其成绩与资深可靠测试员**高度相关**。
- **讲解一致**：测试员须被训练成以尽可能一致的方式讲解与施测；一组给言语鼓励、另一组不给，本身就破坏可比性。
- **备料**：测试员须持材料清单与书面协议，遇疑可查。
- **分工原则**（核心变量是被测人数）：
  - 首选**同一人施测同一项测试**（消除 interrater 信度问题）；
  - 不可行时：简单可计数的测试（数正确俯卧撑）可分包给不同人；需专业判断的测试（深蹲姿势）交最熟练者；
  - 通则：**每名测试员同一时间只测一项**；可在两站间轮转以省等待时间，但一次只聚焦一项。

## A1 — 案例 / 演练 (Application)

**原书未提供完整人员分工案例**，仅给规则与示例（`ch13.txt:792-839`；`p13-18`、`p13-20`）。

**合成演练（明确标记）**：30 人测试日，4 名测试员，5 项测试（身高体重计数类 / 深蹲动作判定 / 冲刺计时 / 俯卧撑 / 纵跳）。
- 深蹲判定与冲刺计时 → 指派**最熟练者**（需 schooled judgment）。
- 身高体重与俯卧撑计数 → 可分派新手（简单客观计数）。
- 每人同一时段只负责一站；配材料清单 + 书面协议；新手先做**一致性校验**（与资深者成绩比对）。
- 输出：可执行分工表（谁测哪项、谁需先校验）。

## A2 — 未来触发 (Trigger)

**用户情境**：
1. 多人测试日，问"谁测哪项、怎么分工"。
2. 队里带了新手助手，要判断他们能不能上手施测。
3. 担心评分者间不一致（宽严不同）污染结果。
4. 要给测试团队做上岗前的准备与校验。

**语言信号（中英双写）**：测试员 / 谁测哪项 / 分工 / 评分者 / 培训测试员 / tester / who administers / interrater reliability / scorer / 新手测试员 / novice tester / 讲解一致 / standardize instructions。

**与相邻能力的区分**：本卡管"人"（选拔/培训/分工）；"顺序与休息"归 `test-sequencing-rest`；"测日准备与记录表"归 `test-prep-standardization`；"评分者不一致导致前后测不可比的归因"归 `reliability-variability-troubleshoot`。

## E — 执行 (Execution)

**输入契约**：被试人数 + 可用测试员（数量与技能）+ 测试清单（含哪些需专业判断/哪些可客观计数）+ 时间约束。缺人数或测试清单无法分工。

**步骤与完成标准**：
1. **分类测试**：把每项测试标为"简单客观计数类"或"需专业判断类"。完成标准：每项都有标签。
2. **定上岗要求**：对新手，确认能正确执行 + 评分；要求其成绩与资深者**高度相关**后再独立施测。完成标准：给出"需校验 / 可直接上岗"结论。
3. **培训一致性**：统一讲解脚本与激励方式（勿只鼓励少数人）。完成标准：书面协议 + 讲解要点齐备。
4. **排班**：优先"同一人测同一项"；不可行时按复杂度分派；每站同一时段一人。完成标准：产出分工表，每名测试员同时只负责一项。
5. **备料**：材料清单 + 评分标准 + 记录表。完成标准：清单可交给测试员直接执行。
6. **输出**。

**输出契约**：`{测试→复杂度标签, 测试员→站点/测试映射, 上岗状态(需校验/已放行), 一致性校验记录, 材料与协议清单}`。

**判停点/分支**：
- 新手成绩与资深者不一致 → 不得独立施测，先补练。
- 某项需专业判断却只有新手可派 → 降级为"资深者抽检 + 新手仅记录原始数据"，或改日施测。

**约定**：原文未给"高度相关"的量化阈值（`f13-07` gap）。本卡要求以"与资深者成绩高度一致（无系统偏差）"作定性校验，标为约定，不虚构相关系数下限。

## B — 边界 (Boundary)

- **不要**为了省人力而让未校验新手独立负责需判断的测试。
- **不要**忽视"言语鼓励不一致"这类隐性污染源。
- **作者盲点（3.3-4）**：自评/量表类输入的信度依赖受试者经验与诚实度，本卡只覆盖施测者侧。
- **资源匮乏场景（3.2）**：原文默认有可轮换的测试团队；人少时需显式降级方案（本卡已给）。
- **共识 ≠ 实证**："高度相关"无阈值，勿当硬标准。
- **相邻易混**：与 `reliability-variability-troubleshoot`（测得飘了怎么归因）不同——本卡是"事前防"。

## 相关能力

- 组合（常配合使用）：`monitoring-protocol-design`
- 组合（常配合使用）：`reliability-variability-troubleshoot`
- 组合（常配合使用）：`test-prep-standardization`
