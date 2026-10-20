# 周期化模型的选择框架（parallel / sequential / emphasis）

## R — 原文 (Reading)

> "The parallel training models ... involve targeting all training factors simultaneously within one training session, training day, series of training days, or a microcycle ... Sequential training models ... were created to address the limitations associated with the parallel model of training ... Emphasis training models ... contain aspects of both parallel and sequential models of periodization."

— Chapter 22 · Models of Periodization（`ch22.txt` 第 264–323 行）

## I — 自述 (Interpretation)

文献里周期化模型名目繁多，但**都可归入三类**（Figure 22.5）；选哪一类，取决于**训练状态**与**赛程密度**，而不是偏好：

- **parallel（并行/并发/复合）**：在同一课、同日、同一串训练日或同一 microcycle 内**同时**针对所有训练因素。适青训与新手/发展中运动员（对应长期发展模型早期）。代价：随水平提高，总负荷必须持续增加，**可能超出耐受**，故**不宜用于中高级/精英**。
- **sequential（序列）**：把单一或少数训练因素按逻辑顺序排列，导向目标结果；为弥补 parallel 的局限（无法同时发展多项、准备期长、难容纳密集赛程）而生。适合**需要更大刺激**者；已用于举重、越野滑雪、自行车、田径等个人项目及多支球类队伍。
- **emphasis（侧重）**：兼具两者特征——多因素同时进行，但**侧重随时间轮换（一般每两周轮换一次）**；部分因素过载以刺激适应、部分维持现状、部分给最小剂量（会有一定 detraining）。适合**中高级 + 赛程密集**的个人/团队运动员。

输出是"选哪一类模型 + 依据 + 该模型的局限"。

## A1 — 案例 / 演练 (Application)

原书列出了各模型的适用人群与已用项目，但**未给"两名运动员二选一"的带输入演练**。以下为**明确标记的合成演练**：

- 输入：(A) 14 岁新手、多元素质发展期；(B) 中级短跑运动员、赛程密集。
- 执行：A 对应长期发展早期 → 判 **parallel**（并注明其总负荷须持续上升、可能超耐受，不宜用于中/精英）；B 为中高级且赛程密集 → 判 **emphasis**（并注明每两周轮换重点；部分因素过载、部分维持、部分最小剂量）。
- 输出："A→parallel、B→emphasis" + 各自依据与风险。（原书未说明该演练的实际结果。）

## A2 — 未来触发 (Trigger)

**用户会在什么情境下遇到这类问题**
1. 用户问"该用并行还是序列周期化？"
2. 用户手上是青训队/新手，却想照搬精英的 sequential 安排。
3. 用户是有密集赛程的中高级运动员，想不出怎么同时练多个素质。
4. 用户听到 emphasis / concurrent / complex / block 等名词，分不清指哪一类。

**语言信号（中英双写）**
- 中："并行还是序列""parallel/sequential/emphasis 选哪个""赛程密集还要练多项素质""侧重轮换多久"。
- 英："parallel vs sequential periodization", "emphasis model", "concurrent training model", "which periodization model to use".

**与相邻能力的区分（初稿）**
- 本卡只做"选模型"。搭三级骨架 → `cap.nsca.periodization-three-level-build`；把模型落成中周期变量 → `cap.nsca.mesocycle-variable-filling`；在赛内调度 → `cap.nsca.in-season-load-management`。

## E — 执行 (Execution)

**输入契约**
- 必需：训练状态（beginner / intermediate / advanced）；赛程密度（每周比赛场次或赛季长度）。
- 可选：项目类型（个人/团队）。缺失训练状态时**先询问**，不得默认。
- 适用条件：本决策针对"如何组织多训练因素"，需已有年度时期框架。

**步骤**
1. 判训练状态档位。完成标准：写入 begin/intermediate/advanced 并按原书定义核对（新手/发展中 vs 中高级）。
2. 分支判定：
   - 若新手/青训/发展中 → **parallel**；并明示"随水平提高总负荷须持续增加、可能超耐受，不宜长期用于中/精英"。
   - 若中高级且**赛程密集** → **emphasis**（注明一般每两周轮换重点；区分"刺激/维持/最小剂量"三类因素）。
   - 若中高级、需更大刺激且赛程不密 → **sequential**（按逻辑顺序排列少数因素）。
3. 写出局限与监测点。完成标准：输出含"模型名 + 依据 + 该模型的主要风险 + 何时应改判"。

**判停点**：若训练状态未知 → 停在步骤 1 询问，不猜。
**输出契约**：`所选模型 | 依据（训练状态/赛程）| 模型局限 | 轮换周期（仅 emphasis）`。原书未给"刺激/维持/最小剂量"的量化负荷分界，**不得编造**，只标注三档概念。

## B — 边界 (Boundary)

- **不要用**：单次课编排；把模型选择当成"改负荷"。
- **作者警告的失败模式**：parallel 用于中/精英会因总负荷不断攀升而**超出耐受**（ch22）；emphasis 会把部分因素压到"最小剂量"而出现**被动 detraining**。
- **作者盲点（BOOK_OVERVIEW 步骤 3）**：这是**机构共识**呈现的"最佳实践"（3.2），对替代范式着墨有限；"三项分类"是教科书收敛结果，非唯一解——不要当成排他的定律。
- **相邻易混**：`cap.nsca.undulating-vs-traditional-identification`（辨识波动/传统，不是选 parallel/sequential/emphasis）。

## 相关能力

- 依赖（先理解）：`periodization-three-level-build`
- 对比（看情境选一）：`undulating-vs-traditional-identification`
- 组合（常配合使用）：`in-season-load-management`
