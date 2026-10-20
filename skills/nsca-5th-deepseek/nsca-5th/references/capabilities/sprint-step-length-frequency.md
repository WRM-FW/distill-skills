# 冲刺速度两变量与常模（步长 × 步频）

## R — 原文 (Reading)

> "sprint speed can be increased by an increase in step length or an increase in step frequency" ... "Elite male sprinters achieve a step length of 2.70 m (8.9 ft), whereas novice sprinters display a step length of 2.56 m (8.4 ft) at maximum velocity ... Elite male sprinters demonstrate step frequency near 4.63 steps per second compared to novice sprinters, who produce a lesser step frequency of 4.43 steps per second."

— Chapter 20 · "Physics of Sprinting, Change of Direction, and Agility"（`ch20.txt` 第 461–485 行）

## I — 自述 (Interpretation)

把"怎么跑更快"拆成两个可操作的表现变量：**步长**（连续两脚印 toe 到 heel 的距离）与**步频**（每秒步数；一个 stride/复步 = 两步）。冲刺速度可由增大步长或提高步频实现，且更高水平短跑者通常两者都更优。但底层机制不是"主动迈大步"或"刻意快倒腿"，而是**快速产生力**：更快、方向正确的垂直力缩短触地时间、增加腾空时间，让步长与步频自然提升（RFD 与正确生物力学是主要限制因素）。常模可用于水平定位：步长精英男 2.70 m vs 新手 2.56 m（最大速度）；步频精英男 4.63 步/s vs 新手 4.43 步/s；最大速度精英 11.0–12.5 m/s vs 团队运动约 8.0–9.5 m/s。诊断起点：先看是步长不足还是步频不足，再判断是力的量级还是生物力学问题。

## A1 — 案例 / 演练 (Application)

原书未提供单个运动员案例，但给出两变量框架与常模。以下为**合成演练**（明确标记，规则来自 p20-11/12）：

- 输入：团队运动运动员最大速约 9.0 m/s，步长偏短、步频尚可。
- 执行：用常模定位其处于团队运动档（8.0–9.5 m/s），据此判断主限制 = 步长不足。
- 预期输出：干预方向 = 改善发力方向与 RFD（而非直接"迈大步"），对应底层力产生/力学效率。
- 依据：原书"the underlying component to maximizing step length and step frequency is related to rapid force production"（第 464–465 行）。

## A2 — 未来触发 (Trigger)

**用户会在什么情境下遇到这类问题**
1. 想诊断冲刺速度限制因素，不确定该看步长还是步频。
2. 需要判断运动员处于哪个速度水平档。
3. 运动员想"迈大步"提速，需要纠正思路。
4. 要把最大速度/步长/步频与常模对照。

**语言信号（中英双写关键 trigger）**
- 中文：「他步频够快但跑不快」「该练步长还是步频」「迈大步能提速吗」「最大速度常模多少」「team sport 和 elite 差多少」
- English: "step length vs step frequency", "sprint speed limiting factor", "elite vs novice sprint norms", "should I increase stride length", "max velocity benchmarks"

**与相邻能力的区分（初稿，阶段 3 回填）**
- 与 `speed-force-metrics-calculation`：本卡先看步长/步频两变量诊断，后者算力学量。
- 与 `speed-agility-monitoring`：本卡专诊断两变量，后者是完整监控面板。
- 与 `sprint-technique-troubleshooting`：本卡归因到力/机制，后者按症状给技术纠正。

## E — 执行 (Execution)

**输入契约**
- 必需：① 最大速度下的步长与步频数据（或最大速度 + 技术视频）；② 项目类型（用于选常模档）。
- 缺失①时：无法判断限制因素，应先测量；不得凭主观"看着慢"下结论。

**步骤与完成标准**
1. 测步长与步频（或最大速度下的相关指标）。
2. 用常模定位水平（分支）：
   - 精英档：步长≈2.70 m、步频≈4.63 步/s、最大速 11.0–12.5 m/s。
   - 团队运动档：最大速≈8.0–9.5 m/s。
3. 判主限制（分支）：步长不足 vs 步频不足。
4. 归因到力产生能力或生物力学效率（步长/步频不足多源于力不足或力方向错，而非"没使劲迈"）。
5. 选择干预：改善发力方向/发力速率（RFD），而非直接迈大步或刻意快倒腿。
6. 完成标准：输出主限制因素 + 干预方向 + 水平定位。

**输出契约**
- `{步长, 步频, 水平档位, 主限制, 干预方向}`。

**原文口径与约定**
- 常模值（第 477–485、509–514 行）：步长 2.70/2.56 m；步频 4.63/4.43 步/s；最大速精英 11.0–12.5 m/s；团队运动 8.0–9.5 m/s。**常模来自 Mann (2011) 特定样本人群，缺女选手数值**，跨年代/性别/项目需重新校验。

## B — 边界 (Boundary)

- **不要用**：当需要算 RFD/impulse 等力学量时（用 `speed-force-metrics-calculation`）；当运动员冲刺有明显技术错误时（先用 `sprint-technique-troubleshooting`）。
- **作者警告的失败模式**：把"迈大步"当提速手段 → 触发 overstriding、抑制 SSC、降低步频（ce20-01）。
- **盲点（BOOK_OVERVIEW 步骤 3）**：常模有**人群/年代依赖**（Mann 2011、无女选手），套用需核对样本与测试协议；低于常模 ≠ 需要干预（常模非因果处方）；步长/步频是结果变量，直接操纵它们不改变底层力。
- **相邻易混**：`speed-agility-monitoring`、`speed-force-metrics-calculation`。

## 相关能力

- 组合（常配合使用）：`speed-force-metrics-calculation`
- 组合（常配合使用）：`sprint-technique-troubleshooting`
