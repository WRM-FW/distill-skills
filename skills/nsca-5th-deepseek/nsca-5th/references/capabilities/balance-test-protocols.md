# 平衡测试协议族（BESS / SEBT）

## R — 原文 (Reading)

> "The stances are held for 20 seconds with eyes closed and hands on hips for each condition. ... Errors include opening eyes; lifting the hands from the hips; touchdown of nonstance foot; step, hop, or other movement of the stance foot or feet; lifting the forefeet or heel; moving the hip into more than 30 degrees of hip flexion or abduction; or remaining out of position for more than 5 seconds. The error scores from the BESS test are summed into a single score."

— Chapter 14 · Balance Error Scoring System（`ch14.txt:1350-1357`）

## I — 自述 (Interpretation)

两个平衡测试，分别测**静态**与**动态**平衡：

**BESS（静态平衡错误评分）**：
- **六条件** = 3 种站姿（双脚并拢双支撑 / 非优势腿单支撑对侧屈膝约 90° / 优势脚在前 tandem）× 2 种表面（硬地 / 软地泡沫垫）；
- 每条件**闭眼、手放髋、保持 20 秒**；失衡尽快回原位；
- 错误项（7 类）：睁眼、手离髋、非支撑脚触地、支撑脚移动/跳/步、抬前脚掌或脚跟、髋屈/外展 >30°、离位 >5 秒；
- **六条件错误数相加为单一总分**（对照表 14.34）。

**SEBT（星形偏移平衡，动态）**：
- 八条线以 45° 间隔外延、长 **120 cm**；
- 单腿站中心，对侧腿向各方向最远伸并触碰后返回；测中心到触点距离；
- 起始方向与支撑腿随机；**每条件 3 次取平均**；前伸间**休息 15 秒**；
- 无效判定：未触线、抬支撑脚离中心、失衡、起止位置未保持满 1 秒；
- 赛前**至少 4 次练习**；可只测前内侧/内侧/后内侧三方向。

## A1 — 案例 / 演练 (Application)

**原书未提供完整数值案例**（`f14-17`、`f14-18`、`p14-27`、`p14-28`）。

**合成演练（明确标记）**：BESS 六条件分别记错 2/3/1/2/4/2；SEBT 某方向三次 60/62/58 cm。
- BESS 总分 = 2+3+1+2+4+2 = **14**。
- SEBT 该方向取平均 = (60+62+58)/3 = **60 cm**。
- 结论：总分 14、方向均值 60 cm，汇总口径明确。

## A2 — 未来触发 (Trigger)

**用户情境**：
1. 要测静态/动态平衡，问用 BESS 还是 SEBT、怎么计分。
2. BESS 六个条件怎么摆、哪些算错误。
3. SEBT 一方向测几次、怎么汇总、什么时候判无效。
4. 想知道平衡测试结果怎么对照常模。

**语言信号（中英双写）**：平衡 / BESS / SEBT / 星形偏移 / 静态平衡 / 动态平衡 / balance / balance error scoring system / star excursion / 单腿站 / 20 秒 / 错误计数 / 前伸。

**与相邻能力的区分**：本卡管 BESS/SEBT；动作筛查与柔韧归 `movement-screen-flexibility`；神经系统/骨科异常提示须经 `test-health-safety-referral` 转诊。

## E — 执行 (Execution)

**输入契约**：测试名（BESS / SEBT）+ 条件/方向 + 试次数据。缺测试名无法选口径。

**步骤与完成标准**：
1. **布置**：BESS 六条件（3 站姿 × 硬/软地，需泡沫垫）+ 秒表；SEBT 铺八方向 120 cm、45° 网格。完成标准：场地就位。
2. **BESS 执行**：每条件闭眼、手放髋、保持 20 s → 逐条记 7 类错误。完成标准：六条件的错误数齐全。
3. **BESS 汇总**：六条件错误数相加为单总分。完成标准：给出总分。
4. **SEBT 执行**：单腿站中心、对侧腿最远伸触后返回；每条件 3 次；前伸间 15 s；赛前 ≥4 次练习。完成标准：给出各方向成绩。
5. **SEBT 汇总**：每方向 3 次取平均。完成标准：给出各方向均值。
6. **无效判定**：SEBT 未触线/抬脚/失衡/未保持 1 s → 该次无效。完成标准：记录无效试次。
7. **输出**。

**输出契约**：`{测试名, 条件/方向, 原始错误数或距离, 汇总(总分/均值), 无效试次说明}`。

**判停点/分支**：
- BESS 某条件站姿无法维持 → 按错误计数照常记（不中断整测）。
- SEBT 某次无效 → 重做该次。

**约定**：原文**未给 BESS 各条件顺序与条件间休息**，**未给 SEBT 归一化的完整公式**（在表格中，`f14-17`/`f14-18` gap）。本卡不虚构归一化公式；若需归一化为肢体长百分比须回查表 14.20–14.21。

## B — 边界 (Boundary)

- **不要**跨条件/跨表面直接比较 BESS 错误数（硬地与软地不可比）。
- **不要**跳过赛前练习直接测 SEBT（≥4 次练习保证信度）。
- **作者盲点（3.3-5）**：SEBT"三方向足够"仅为"有人建议"，未被确立为标准。
- **常模时效（3.1）**：BESS 常模（表 14.34）有年龄/性别依赖。
- **专业边界（2.2-14）**：平衡异常可能提示神经/骨科问题，越界解读与处置需转诊。
- **相邻易混**：与 `movement-screen-flexibility`（动作筛查/柔韧）不同。

## 相关能力

- 组合（常配合使用）：`movement-screen-flexibility`
- 组合（常配合使用）：`plyometric-pretraining-screen`
