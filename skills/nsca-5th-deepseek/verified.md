# verified.md — 阶段 1.5 三重验证通过的能力单元

> 由 cangjie-skill 2.5.0 阶段 1.5 生成。每个单元已通过 V1 来源充分性 / V2 可执行性（纸面演练 walkthrough）/ V3 任务增益。
> 详细理由、演练记录与覆盖表见 `.candidates/_verified/<簇>.md`（本文件为跨簇汇总）。

## 汇总

| 簇 | 主题 | 覆盖任务 | 单元数 | verified | reference | needs_review | rejected |
|---|---|---|---|---|---|---|---|
| A-plan-design | 抗阻训练计划设计（需求分析 / 训练状态 / 七步变量） | T01–T11 | 17 | 14 | 3 | 0 | 0 |
| B-periodization | 周期化与年度计划编排 | T12–T13 | 11 | 10 | 1 | 0 | 0 |
| C-testing | 测试选择、实施与数据解释 | T20–T23, T40 | 26 | 26 | 0 | 0 | 0 |
| D1-plyometric | 快速伸缩复合训练设计 | T14 | 11 | 9 | 2 | 0 | 0 |
| D2-speed-agility | 速度与敏捷训练设计 | T15–T16 | 15 | 14 | 1 | 0 | 0 |
| E-aerobic | 有氧耐力训练与强度分区 | T17–T18, T37 | 10 | 9 | 0 | 1 | 0 |
| F-preparation-technique | 准备活动 / 柔韧 / 技术 / 护腰 / 保护 / 替代器械 | T19, T24–T26 | 15 | 9 | 3 | 3 | 0 |
| G-populations-nutrition-psych | 特殊人群 / 营养补水 / RED-S / 增补剂 / 心理 | T30–T36 | 24 | 21 | 3 | 0 | 0 |
| H-recovery-management | 过度训练与恢复 / 康复再训练 / 场地与管理 | T27–T29, T38–T39 | 16 | 16 | 0 | 0 | 0 |
| **合计** | | | **145** | **128** | **13** | **4** | **0** |

## 能力单元总表

| 单元 | 标题 | capability_id | 类型 | 重要性 | decision |
|---|---|---|---|---|---|
| A plan design · U1 | 需求分析（Step 1：运动特征评估 + 运动员评估） | cap.nsca.needs-analysis | procedure | critical | verified |
| A plan design · U2 | 训练状态分类（beginner/intermediate/advanced） | cap.nsca.training-status | framework | critical | verified |
| A plan design · U3 | 确定主要训练目标（单目标聚焦 + emphasis/de-emphasis + 赛季优先级） | cap.nsca.primary-training-goal | decision-framework | high | verified |
| A plan design · U4 | 动作选择（Step 2） | cap.nsca.exercise-selection | procedure | critical | verified |
| A plan design · U5 | 训练频率（Step 3：状态×赛季双查表 + 恢复日间距 + split 时机） | cap.nsca.training-frequency | procedure | critical | verified |
| A plan design · U6 | 动作顺序（Step 4） | cap.nsca.exercise-order | procedure | high | verified |
| A plan design · U7 | 确定与估算 1RM / xRM（Step 5 之测试与估算） | cap.nsca.one-rm-xrm-determination | calculation | critical | verified |
| A plan design · U8 | 按训练目标分配负荷与重复（Step 5 核心） | cap.nsca.load-reps-by-goal | calculation | critical | verified |
| A plan design · U9 | power 训练负荷赋值特例 | cap.nsca.power-load-assignment | decision-framework | high | verified |
| A plan design · U10 | 替代/自调负荷法（RPE / RIR / SRB） | cap.nsca.rpe-rir-srb | decision-framework | medium | verified |
| A plan design · U11 | 负荷进阶：何时加（2-for-2）与加多少（增幅/重轻日变异） | cap.nsca.load-progression | procedure | high | verified |
| A plan design · U12 | 训练量分配（Step 6）+ volume-load 计算 | cap.nsca.volume-assignment | calculation | critical | verified |
| A plan design · U13 | 组间休息时长（Step 7） | cap.nsca.rest-periods | procedure | high | verified |
| A plan design · U14 | 完整 7 步抗阻训练计划设计（端到端 SOP） | cap.nsca.seven-step-program | procedure | critical | verified |
| A plan design · R1 | 无氧运动处方的原则层（六原则 / SAID / 个体化） | cap.nsca.anaerobic-principles | framework | medium | reference |
| A plan design · R2 | 过载也可由"减量"构成（减量周/超量恢复） | cap.nsca.overload-deload | rule | medium | reference |
| A plan design · R3 | 训练到力竭的谨慎规则 | cap.nsca.failure-caution | rule | medium | reference |
| B periodization · U1 | 周期化的分层定位与三级建立流程 | cap.nsca.periodization-three-level-build | procedure | high | verified |
| B periodization · U2 | 三种周期化模型的选择框架（parallel / sequential / emphasis） | cap.nsca.periodization-model-choice | framework | high | verified |
| B periodization · U3 | 周期层级结构与时长口径（Table 22.2） | cap.nsca.periodization-cycle-durations | framework | medium | verified |
| B periodization · U4 | 运动季节 ↔ 周期化时期映射与传统四期演变 | cap.nsca.season-to-period-mapping | framework | high | verified |
| B periodization · U5 | 年度训练计划（macrocycle）的编排流程 | cap.nsca.annual-plan-construction | procedure | critical | verified |
| B periodization · U6 | 用变量填充一个中周期（Table 22.3 数值核心 + 负荷落地） | cap.nsca.mesocycle-variable-filling | calculation | critical | verified |
| B periodization · U7 | 周期化三大机制理论（GAS / 刺激—疲劳—恢复 / 体能—疲劳） | cap.nsca.periodization-mechanistic-theories | framework | medium | verified |
| B periodization · U8 | 峰值 vs 维持的决策框架（peaking / maintenance） | cap.nsca.peaking-vs-maintenance | framework | high | verified |
| B periodization · U9 | 密集赛程/长赛季的赛内负荷编排与卸载周 | cap.nsca.in-season-load-management | procedure | high | verified |
| B periodization · U10 | 波动的辨识：undulating vs 传统"伪线性" | cap.nsca.undulating-vs-traditional-identification | framework | medium | verified |
| B periodization · U11 | 教练与体能教练协同规划 | cap.nsca.coach-sc-collaboration | framework | medium | reference |
| C testing · U1 | 有效测试的证据本位选择框架（效度/信度/客观性门槛） | cap.nsca.test-selection-validity | framework | critical | verified |
| C testing · U2 | 专项特异性与测试电池构建（含年龄/性别/训练状态适用边界） | cap.nsca.sport-specific-test-battery | framework | critical | verified |
| C testing · U3 | 测试顺序编排与休息安排 | cap.nsca.test-sequencing-rest | procedure | high | verified |
| C testing · U4 | 测试员选拔、培训与施测分工 | cap.nsca.tester-selection-duties | procedure | high | verified |
| C testing · U5 | 运动员测试准备、记录与测试日标准化 | cap.nsca.test-prep-standardization | checklist | medium | verified |
| C testing · U6 | 测试信度受损来源排查（前后测一致性） | cap.nsca.reliability-variability-troubleshoot | troubleshooting | high | verified |
| C testing · U7 | 环境因素对测试的调整（温度/湿度/海拔） | cap.nsca.test-environment-adjustment | framework | medium | verified |
| C testing · U8 | 测试安全红线：健康风险识别与转诊（含低钠血症）★ | cap.nsca.test-health-safety-referral | troubleshooting | critical | verified |
| C testing · U9 | 测试监控体系三层设计与运动科技引入决策 | cap.nsca.monitoring-protocol-design | framework | medium | verified |
| C testing · U10 | 最大力量测试协议族（1RM / IMTP / 北欧腘绳肌） | cap.nsca.max-strength-test-protocols | procedure | high | verified |
| C testing · U11 | 负荷-速度剖面（VBT）建立与 1RM 预测禁用 | cap.nsca.load-velocity-profile | procedure | medium | verified |
| C testing · U12 | 跳跃与下肢爆发力测试协议族 | cap.nsca.jump-power-test-protocols | procedure | high | verified |
| C testing · U13 | 速度与变向/敏捷测试协议族 | cap.nsca.speed-agility-test-protocols | procedure | high | verified |
| C testing · U14 | 无氧能力测试协议族（Wingate / 300-yd shuttle / 90-s box jump / Margaria 冲刺） | cap.nsca.anaerobic-capacity-test-protocols | procedure | medium | verified |
| C testing · U15 | 局部肌肉耐力测试协议族 | cap.nsca.local-muscular-endurance-protocols | procedure | medium | verified |
| C testing · U16 | 有氧能力测试协议族（1.5-mile run / 12-min run / Yo-Yo IRT / MAS / 30-15 IFT）★ | cap.nsca.aerobic-capacity-test-protocols | procedure | high | verified |
| C testing · U17 | 动作筛查与柔韧性测试（AMSC/FMS/TJA + 坐位体前屈/过顶深蹲） | cap.nsca.movement-screen-flexibility | procedure | medium | verified |
| C testing · U18 | 平衡测试协议族（BESS / SEBT） | cap.nsca.balance-test-protocols | procedure | medium | verified |
| C testing · U19 | 人体测量与体成分测量协议（身高/体重/围度/皮褶/BIA） | cap.nsca.anthropometry-bodycomp-measure | procedure | medium | verified |
| C testing · U20 | Margaria-Kalamen 台阶冲刺功率计算 ★（含单位口径裁断） | cap.nsca.margaria-kalamen-power-calc | calculation | medium | verified |
| C testing · U21 | 体成分估算计算（皮褶→体密度→体脂% + SEE 区间）★ | cap.nsca.body-composition-calc | calculation | high | verified |
| C testing · U22 | 最大有氧速度（MAS）与 VO2max 估算 ★ | cap.nsca.mas-vo2max-estimation | calculation | high | verified |
| C testing · U23 | 描述统计、数据标准化与运动员画像 ★ | cap.nsca.descriptive-stats-athletic-profile | framework | high | verified |
| C testing · U24 | 幅度统计（SWC / 效应量 / 差异分解读）★ | cap.nsca.swc-effect-size | calculation | high | verified |
| C testing · U25 | 常模数据的查找与解读口径（表 14.1–14.37）★ | cap.nsca.norms-lookup-interpretation | template | medium | verified |
| C testing · U26 | 反应力量指数（RSI）与离心利用率（EUR）计算 ★ | cap.nsca.rsi-eur-calculation | calculation | medium | verified |
| D1 plyometric · U1 | Plyometric 计划设计总纲：需求分析 + 五步 SOP + 变量框架 | cap.nsca.plyometric-program-design-sop | procedure | critical | verified |
| D1 plyometric · U2 | 确定 plyometric 强度与量（Table 19.5 因素 + Table 19.6 触点档位） | cap.nsca.plyometric-intensity-volume | calculation | critical | verified |
| D1 plyometric · U3 | Plyometric 频率与恢复（周间/组间/次间） | cap.nsca.plyometric-frequency-recovery | procedure | high | verified |
| D1 plyometric · U4 | Plyometric 进阶（progressive overload；强度↑量↓；计划时长） | cap.nsca.plyometric-progression | procedure | high | verified |
| D1 plyometric · U5 | 训练前运动员评估与准入（技术/力量/平衡/身体特征） | cap.nsca.plyometric-pretraining-screen | checklist | critical | verified |
| D1 plyometric · U6 | 年龄人群 plyo 处方裁剪（青少年 / 儿童 / 大师） | cap.nsca.plyometric-age-adjustment | procedure | critical | verified |
| D1 plyometric · U7 | Plyometric 专项热身（RAMP：激活—动员—增强） | cap.nsca.plyometric-warmup-ramp | procedure | medium | verified |
| D1 plyometric · U8 | 安全与常见错误排障（技术/落地/ACL + 深跳高度/体重 + 场地器材） | cap.nsca.plyometric-safety-troubleshooting | troubleshooting | critical | verified |
| D1 plyometric · U9 | 与抗阻/有氧的整合与排序（含 complex training 三型） | cap.nsca.plyometric-integration-complex | decision-framework | high | verified |
| D1 plyometric · U10 | Plyometric 动作模式分类表（Table 19.2–19.4） | cap.nsca.plyometric-drill-catalog | template | medium | reference |
| D1 plyometric · REF-1 | SSC 机制（三相 / 过渡相能量损失 / 快慢 SSC 分类） | cap.nsca.ssc-mechanism | rule（机制参考） | medium | reference |
| D2 speed agility · U1 | 速度/变向/敏捷三分定义与「变向 vs 反应性敏捷」判定框架 | cap.nsca.speed-cod-agility-attribution | framework | high | verified |
| D2 speed agility · U2 | 速度/变向/敏捷的力学指标口径与计算（RFD / impulse / momentum / power / COD deficit） | cap.nsca.speed-force-metrics | calculation | high | verified |
| D2 speed agility · U3 | 敏捷/变向发展的需求分析与分期处方（5 步流程 + 3 block 模板） | cap.nsca.agility-needs-to-program | procedure | high | verified |
| D2 speed agility · U4 | 速度发展的 short-to-long 分期处方（Table 20.7） | cap.nsca.speed-short-to-long | procedure | high | verified |
| D2 speed agility · U5 | 冲刺技术错误排障（症状→原因→纠正，Table 20.1） | cap.nsca.sprint-technique-troubleshoot | troubleshooting | high | verified |
| D2 speed agility · U6 | 速度手段选择与进阶（三级分类 + 进阶/退阶/变式 + 负荷规则） | cap.nsca.speed-method-progression | procedure | medium | verified |
| D2 speed agility · U7 | 敏捷 drill 可操纵因素与知觉—认知进阶（含过渡移动） | cap.nsca.agility-drill-constraints | framework | medium | verified |
| D2 speed agility · U8 | 变向训练取向决策（角度/入速 → 快慢 SSC + GCT 基准） | cap.nsca.cod-angle-orientation | decision | high | verified |
| D2 speed agility · U9 | 变向/敏捷技术诊断要点（视觉—躯干—腿—臂） | cap.nsca.cod-technique-diagnosis | framework | medium | verified |
| D2 speed agility · U10 | 速度/敏捷监控指标选择与解读 | cap.nsca.speed-agility-monitoring | procedure | medium | verified |
| D2 speed agility · U11 | 速度/COD/敏捷计划设计变量清单与 volume-load | cap.nsca.speed-agility-program-variables | checklist | medium | verified |
| D2 speed agility · U12 | 敏捷发展多元方法框架（力量谱 + 闭技能技术 + 知觉认知） | cap.nsca.agility-multifactorial | framework | medium | verified |
| D2 speed agility · U13 | 速度/SSC 训练目标与两判据 | cap.nsca.ssc-speed-objectives | checklist | medium | verified |
| D2 speed agility · U14 | 冲刺速度两变量与常模（步长 × 步频） | cap.nsca.sprint-step-length-frequency | framework | medium | verified |
| D2 speed agility · U15 | 周期化概念迁移到速度/COD/敏捷 | cap.nsca.periodization-transfer-speed | framework | low | reference |
| E aerobic · U1 | 强度分区与目标心率计算（含监控方法选择） | cap.nsca.aerobic-intensity-zones-target-hr | calculation | critical | verified |
| E aerobic · U2 | 有氧耐力训练计划 5 步设计变量与训练类型处方 | cap.nsca.aerobic-program-design | procedure | high | verified |
| E aerobic · U3 | 有氧进阶规则（≤10%/周、单变量、按时间非距离） | cap.nsca.aerobic-progression-rule | procedure | high | verified |
| E aerobic · U4 | 由专项主导供能系统推导间歇训练比（T37） | cap.nsca.energy-system-interval-ratio | procedure | medium | verified |
| E aerobic · U5 | 同期（有氧+抗阻）训练处理 | cap.nsca.concurrent-training-management | procedure | high | verified |
| E aerobic · U6 | 赛前减量（tapering）模型选择 | cap.nsca.tapering-model | procedure | high | verified |
| E aerobic · U7 | 热适应（heat acclimation）方案 | cap.nsca.heat-acclimation | procedure | medium | verified |
| E aerobic · U8 | 高原训练方案（含 LHTL） | cap.nsca.altitude-lhtl | procedure | medium | verified |
| E aerobic · U9 | 恢复会话（recovery session）使用规范 | cap.nsca.recovery-session | procedure | medium | verified |
| E aerobic · U10 | 运动季节到有氧计划变量的映射（Table 21.5） | cap.nsca.aerobic-season-assignment | framework | high | needs_review |
| F preparation technique · U1 | 准备活动设计（RAMP 三阶段 / 传统两阶段 + 时长时机 + CNS 预备） | cap.nsca.warmup-ramp | procedure | high | verified |
| F preparation technique · U2 | 柔韧训练编程（静态/动态/PNF 选择与参数） | cap.nsca.flexibility-programming | procedure | high | needs_review |
| F preparation technique · U3 | 动作技术基本规范（握法 / 身体位置 / 呼吸 / Valsalva） | cap.nsca.exercise-technique-basics | framework | high | verified |
| F preparation technique · U4 | 护腰（weight belt）使用判据 | cap.nsca.weight-belt-decision | framework | high | verified |
| F preparation technique · U5 | 保护（spotting）规则与判断 | cap.nsca.spotting-rules | framework | high（安全相关） | verified |
| F preparation technique · U6 | 爆发力动作阶段结构（高翻/抓举、推举/借力推、中大腿拉） | cap.nsca.power-exercise-phases | procedure | high | verified |
| F preparation technique · U7 | 变阻负荷计算（链 / 弹力带） | cap.nsca.variable-resistance-load | calculation | medium | verified |
| F preparation technique · U8 | 强化离心负荷（AEL）编程 | cap.nsca.ael-programming | procedure | medium | verified |
| F preparation technique · U9 | 替代模式与非传统器械的采用决策 | cap.nsca.alternative-modes-decision | framework | medium | verified |
| F preparation technique · U10 | 技术错误排障（缺陷→纠正） | cap.nsca.technique-troubleshooting | troubleshooting | medium | verified |
| F preparation technique · R11 | 动作/拉伸技术目录汇总（resource list） | cap.nsca.technique-catalogs | checklist | low | reference |
| F preparation technique · R12 | 热身急性效应与柔韧性影响因素清单 | cap.nsca.warmup-flexibility-background | checklist | low | reference |
| F preparation technique · R13 | Ch15/Ch16 症状型常见错误清单（无纠错闭环） | cap.nsca.common-error-symptoms | checklist | medium | reference |
| F preparation technique · N14 | 原木（log）直径与训练负荷规则 | cap.nsca.log-training | rule | low | needs_review |
| F preparation technique · N15 | 弹力带长度-张力预测方程（自变量单位未定义） | cap.nsca.band-tension-equation | calculation | low | needs_review |
| G populations nutrition psych · U1 | 青少年抗阻训练处方（有效性与剂量 / 指南 / 迷思 / 安全） | cap.nsca.youth-resistance-training | procedure | high | verified |
| G populations nutrition psych · U2 | 生物成熟度评估与 PHV 监测 | cap.nsca.maturity-assessment-phv | procedure | medium | verified |
| G populations nutrition psych · U3 | 老年人抗阻训练处方与启动筛查（含安全/频率/跌倒预防/骨可逆） | cap.nsca.older-adult-resistance-training | procedure | high | verified |
| G populations nutrition psych · U4 | 女性运动员损伤风险降低与健康考量 | cap.nsca.female-injury-risk-reduction | framework | medium | verified |
| G populations nutrition psych · U5 | 妊娠期与产后抗阻训练调整 | cap.nsca.pregnancy-postpartum-training | framework | medium | verified |
| G populations nutrition psych · U6 | 性别差异生理与激素口径参照（reference） | cap.nsca.sex-difference-reference | reference | medium | reference |
| G populations nutrition psych · U7 | 宏量营养素与能量需求估算 | cap.nsca.macronutrient-energy-needs | calculation | high | verified |
| G populations nutrition psych · U8 | 血糖生成指数/负荷（GI/GL）计算 | cap.nsca.glycemic-index-load | calculation | low | verified |
| G populations nutrition psych · U9 | 个体化补水与电解质方案（汗液率计算 + 水合判定 + 分年龄处方） | cap.nsca.hydration-electrolyte-plan | calculation | critical | verified |
| G populations nutrition psych · U10 | 赛前/赛中/赛后竞赛营养策略（时间线 + 碳水负荷 + 补糖补蛋白） | cap.nsca.competition-nutrition-timeline | framework | medium | verified |
| G populations nutrition psych · U11 | 体成分改变（增重/减脂）干预 | cap.nsca.body-composition-intervention | framework | medium | verified |
| G populations nutrition psych · U12 | 能量可用性（EA）与 RED-S 识别（安全相关） | cap.nsca.energy-availability-red-s | calculation | high | verified |
| G populations nutrition psych · U13 | 进食障碍与快速减重识别与转诊（安全相关） | cap.nsca.eating-disorder-rwl-referral | troubleshooting | high | verified |
| G populations nutrition psych · U14 | 营养评估口径、膳食换算与转诊边界 | cap.nsca.nutrition-assessment-referral | procedure | medium | verified |
| G populations nutrition psych · U15 | 增补剂证据评估框架（合法性×安全性×有效性×必要性） | cap.nsca.supplement-evidence-evaluation | framework | medium | verified |
| G populations nutrition psych · U16 | 增补剂/激素滥用迹象识别与转诊（安全相关） | cap.nsca.ergogenic-abuse-identification | checklist | medium | verified |
| G populations nutrition psych · U17 | 增能剂证据分级与剂量处方 | cap.nsca.ergogenic-dosing-evidence | recommendation | medium | verified |
| G populations nutrition psych · U18 | 禁用物质名称与剂量口径参照（reference） | cap.nsca.banned-substance-reference | reference | low | reference |
| G populations nutrition psych · U19 | 唤醒调控与心理技能（理论 + 降唤醒技术 + 目标设定 + 自我效能） | cap.nsca.arousal-psych-skills | framework | medium | verified |
| G populations nutrition psych · U20 | 动作技能教学与实践安排 | cap.nsca.motor-skill-teaching | framework | medium | verified |
| G populations nutrition psych · U21 | 心理健康红旗识别与三步转诊（安全相关） | cap.nsca.mental-health-referral | troubleshooting | high | verified |
| G populations nutrition psych · U22 | 伤后重返训练的心理支持 | cap.nsca.injury-return-psych-support | procedure | medium | verified |
| G populations nutrition psych · U23 | 停训（detraining）时间进程与应对 | cap.nsca.detraining-assessment | framework | medium | verified |
| G populations nutrition psych · U24 | 训练适应幅度参照与高原/热适应选择（reference） | cap.nsca.adaptation-magnitude-reference | reference | medium | reference |
| H recovery management · U1 | 过度训练/过度劳累的定义与过度训练连续谱判定（FOR→NFOR→OTS） | cap.nsca.overtraining-continuum-classification | framework | critical | verified |
| H recovery management · U2 | 成绩下降归因排查（并非所有下降都是过度训练） | cap.nsca.underperformance-attribution-triage | troubleshooting | high | verified |
| H recovery management · U3 | 运动员监控计划设计（测试质量 + 指标选择 + 问卷） | cap.nsca.athlete-monitoring-plan-design | procedure | high | verified |
| H recovery management · U4 | 分级检测升级协议（Category I→II→III） | cap.nsca.overtraining-test-escalation | troubleshooting | medium | verified |
| H recovery management · U5 | 过度训练恢复策略选择与恢复时长预期 | cap.nsca.overtraining-recovery-strategy | procedure | high | verified |
| H recovery management · U6 | 过度训练预防与恢复整合（含负荷变异 %CV 与 >30% 警戒线） | cap.nsca.overtraining-prevention-integration | checklist | high | verified |
| H recovery management · U7 | 组织愈合分期与各期目标（含炎症期急性管理） | cap.nsca.tissue-healing-phase-classification | framework | high | verified |
| H recovery management · U8 | 按愈合期调整抗阻训练（DAPRE / DeLorme / Oxford + SAID + 神经肌肉控制） | cap.nsca.rehab-resistance-progression | calculation | high | verified |
| H recovery management · U9 | 体能教练的专业边界与转诊（scope of practice） | cap.nsca.rehab-scope-and-referral | framework | critical | verified |
| H recovery management · U10 | 环境与医疗急症现场识别与处置（热病 / 横纹肌溶解 / 镰状细胞特质 / 低温症） | cap.nsca.exercise-medical-emergency-response | troubleshooting | high | verified |
| H recovery management · U11 | 降低初伤/再伤风险与重返运动判据 | cap.nsca.reinjury-risk-and-return-to-play | framework | medium | verified |
| H recovery management · U12 | 场地空间估算与设备布置（含 Table 25.1/25.2 计算与设施规格） | cap.nsca.facility-space-and-layout-planning | calculation | medium | verified |
| H recovery management · U13 | 设施设计流程、需求评估与运维 | cap.nsca.facility-design-process | procedure | low | verified |
| H recovery management · U14 | 政策与程序手册构建（使命→目标→政策→程序）与场馆行政 | cap.nsca.policy-procedure-manual | framework | low | verified |
| H recovery management · U15 | 风险管理与法律责任（过失四要素、监督原则、记录/产品责任/惩戒） | cap.nsca.risk-management-and-negligence | framework | low | verified |
| H recovery management · U16 | 应急预案（EAP）构成与分情境应急响应 | cap.nsca.emergency-action-plan | procedure | low | verified |

---

# 各簇详细验证记录


---

<!-- ===== 簇 A-plan-design ===== -->

# 簇 A-plan-design — 三重验证结果

- 负责任务: T01–T11
- 候选输入: 131 条（来自 cases-g2-ch15-26.md, counter-examples-g2-ch15-26.md, frameworks-g3-ch18-19.md, principles-g3-ch18-19.md；另有 41 条 f13-*/p13-* 与 C-testing 簇重复，见文末「跨簇重复候选」）
- 归并后能力单元: 14 个 verified + 3 个 reference = 17 个；另登记 41 条跨簇重复候选
- verified: 14 / reference: 3 / needs_review: 0 / rejected: 0
- 回查原文: `.cangjie/source/ch18.txt`（主，逐条核对全部数值表）；`.cangjie/source/ch13.txt`、`ch14.txt`（仅定位，测试细节归 C 簇）

> 说明：Ch18 的 Step 1–7 按原子能力单元拆分（未压成一条）。Ch13/14 的测试选择、实施与数据解释（f13-*/p13-*）任务归属为 T20–T23，由 **C-testing 簇承载**；本簇仅以其作为 T01「评估运动员」的输入引用，不重复展开（见文末）。Table 18.x 的「数据」与「用表决策的流程」已在同一单元内归并，并在 V1 逐表核对原文数值。

---

## 能力单元 U1 — 需求分析（Step 1：运动特征评估 + 运动员评估）

- **proposed_capability_id**: cap.nsca.needs-analysis
- **proposed_slug**: needs-analysis
- **type**: procedure
- **merged_candidates**: [f18-01, f18-02, c18-1, c18-3, c18-17]
- **task_ids**: [T01]
- **importance**: critical
- **source_evidence**:
  - source_id: src-nsca-essentials-5e
    location: Chapter 18, Step 1: Needs Analysis（ch18.txt 第 228–401 行；运动评估 233–282，运动员评估 284–401；Figure 18.3–18.5 力剖面 353–384）
- **R 段可用原文引用**（英文，≤100 词，逐字）:
  > "The strength and conditioning professional's initial task is to perform a needs analysis, a two-stage process that includes an evaluation of the requirements and characteristics of the sport and an assessment of the athlete."（ch18.txt 229–231）
- **V1_source_sufficiency**: passed: true — 回查 ch18.txt：两阶段（sport evaluation：movement/physiological/injury analysis；athlete assessment：training status/测试/结果对照常模/主目标）均完整给出，并配三情境应用表（c18-1/c18-3）与足球运动员力剖面示例（c18-17，IMTP/CMJ 45 cm、mRSI 0.46、TTT 1.0 s、rebound 163 ms/22 cm/RSI 1.40 均与原文一致）。原文明确「具体测试项目与常模去 Ch13/Ch14」，本单元只承载流程骨架与输出，与 C 簇分工无冲突。
- **V2_executability**: passed: true
  - check_mode: walkthrough
  - input: 新专项＝女子排球（副攻）；运动员＝19 岁，抗阻训练 3 年、现每周 4 练、技术熟练，无伤史；可测 1RM 与 CMJ。
  - expected: 产出 (a) 运动评估：movement＝反复起跳/落地、扣球（肩、髋膝伸肌）；physiological＝power 优先、strength 次之、hypertrophy/endurance 最低；injury＝肩、膝、踝过用与非接触 ACL。(b) 运动员评估：训练状态＝Advanced；主目标＝power（单块单目标）。三项交付物齐备。
  - observed: 按两阶段 3 步流程可完整得到上述 (a)(b)，输出具体且可核对（Advanced 与 Table 18.1≥3–4 次/周、≥1 年、高技术相符）。
- **V3_task_utility**: passed: true — 统一「先运动、后运动员」的评估字段口径，避免跳过需求分析直接套动作/负荷（减少遗漏，是 T02–T11 全部参数的查表键来源）。
- **decision**: verified
- **if_not_verified**: —

---

## 能力单元 U2 — 训练状态分类（beginner/intermediate/advanced）

- **proposed_capability_id**: cap.nsca.training-status
- **proposed_slug**: training-status-classification
- **type**: framework
- **merged_candidates**: [f18-03, p18-07, c18-2]
- **task_ids**: [T02]
- **importance**: critical
- **source_evidence**:
  - source_id: src-nsca-essentials-5e
    location: Chapter 18, Table 18.1（ch18.txt 第 290–336 行，表体 317–336）
- **R 段可用原文引用**（英文，≤100 词，逐字）:
  > "Table 18.1 provides an example of how such information might be used to classify athletes' training status as beginner, intermediate, or advanced. The strength and conditioning professional should realize that the three classifications exist on a continuum and cannot be definitively demarcated."（ch18.txt 306–309）
- **V1_source_sufficiency**: passed: true — 回查原文核对 Table 18.1 逐格：Beginner(C) Not training/just began；<2 months；≤1–2/wk；None or low；None or minimal。Intermediate：Currently training；2–6 months；≤2–3；Medium；Basic。Advanced：Currently training；≥1 year；≥3–4；High；High。与 p18-07 完全一致。四维训练背景（type/length/intensity/technique）文本亦在 299–305 完整给出，无漏读。
- **V2_executability**: passed: true
  - check_mode: walkthrough
  - input: 运动员＝22 岁业余足球运动员，赛季中每周仅 2 次抗阻、负荷中低、动作技术一般，训练年龄 3 年。
  - expected: 频率 2（≤2–3 但年份跨 2–6 与 ≥1 之间）→ 属连续谱，按原文「欧洲足球运动员因赛季低频低应激常难达 advanced」取保守档 Intermediate。
  - observed: 依据表逐维对照得 Intermediate；输出可与 c18-2（A/B＝Advanced、C＝Beginner）口径一致，结果明确。
- **V3_task_utility**: passed: true — 提供唯一权威查表键，统一频率/量/1RM 测试资格等所有下游表的读法（统一口径、改善决策结构）。
- **decision**: verified
- **if_not_verified**: —

---

## 能力单元 U3 — 确定主要训练目标（单目标聚焦 + emphasis/de-emphasis + 赛季优先级）

- **proposed_capability_id**: cap.nsca.primary-training-goal
- **proposed_slug**: primary-training-goal
- **type**: decision-framework
- **merged_candidates**: [f18-04, p18-08, ce18-03, ce18-06]
- **task_ids**: [T01]
- **importance**: high
- **source_evidence**:
  - source_id: src-nsca-essentials-5e
    location: Chapter 18, Primary Resistance Training Goal + Table 18.2（ch18.txt 第 402–451 行）
- **R 段可用原文引用**（英文，≤100 词，逐字）:
  > "The athlete's testing results, the movement and physiological analysis of the sport, and the priorities of the athlete's sport season determine the primary goal or outcome for the resistance training program. ... an effort should be made to concentrate on only one training outcome per training block. This can be accomplished using an emphasis/de-emphasis approach"（ch18.txt 403–411）
- **V1_source_sufficiency**: passed: true — 回查 Table 18.2 逐行：Off-season（专项 Low/抗阻 High；先 hypertrophy+endurance 后 strength+power）、Preseason（Medium/Medium；sport/movement specific）、In-season（High/Low；维持，长赛季 strength↔power 交替）、Postseason（Variable/Variable；not specific）均与 p18-08 一致。不兼容素质（speed vs cardiovascular endurance）与 multitargeted 段落完整（417–430）。
- **V2_executability**: passed: true
  - check_mode: walkthrough
  - input: 团队项目（篮球）、运动员处 in-season、需同时维持 strength–power 与 speed。
  - expected: 本训练块唯一 dominant 目标＝power（速度-力量）；strength 用 de-emphasis 维持；speed 与 strength–power 可并行（兼容），不与大容量有氧耐力同期。
  - observed: 依 3 路证据 + 赛季映射 + 兼容性规则可得出明确单目标与轮换安排，与 c18-3（A 主目标 Strength/power）一致。
- **V3_task_utility**: passed: true — 强制"每块只聚焦一个主目标"，避免多目标互相干扰（ce18-03/ce18-06 失败边界），直接决定 U8 负荷档。
- **decision**: verified
- **if_not_verified**: —

---

## 能力单元 U4 — 动作选择（Step 2）

- **proposed_capability_id**: cap.nsca.exercise-selection
- **proposed_slug**: exercise-selection
- **type**: procedure
- **merged_candidates**: [f18-05, f18-06, f18-07, f18-08, p18-09, p18-36, p18-37, c18-4, ce18-04, ce18-05]
- **task_ids**: [T03]
- **importance**: critical
- **source_evidence**:
  - source_id: src-nsca-essentials-5e
    location: Chapter 18, Step 2: Exercise Selection + Table 18.3（ch18.txt 第 455–793 行；类型学 464–573；专项性/平衡 594–677；技术经验 679–694；器材 701–708；时间 710–725；Table 18.3 631–657）
- **R 段可用原文引用**（英文，≤100 词，逐字）:
  > "To make informed exercise selections, the strength and conditioning professional must understand the nature of various types of resistance training exercises, the movement and muscular requirements of the sport, the athlete's exercise technique experience, the equipment available, and the amount of training time available."（ch18.txt 457–461）
- **V1_source_sufficiency**: passed: true — 回查：两级类型学（core/assistance：≥1 大肌区且 ≥2 主要关节；structural：直接/间接负脊；power：structural 快速完成）在 469–573 完整；肩（盂肱+肩带）与脊柱各计一关节在 481–485 明示；muscle balance 规则 659–677 完整；Table 18.3 九类动作模式示例逐条与 p18-09 一致（如 vertical jumping ballistic→Snatch/power clean/back squat…；running→Snatch/clean/back squat/lunge/step-up…）。五约束（类型/专项/经验/器材/时间）齐备。
- **V2_executability**: passed: true
  - check_mode: walkthrough
  - input: 100 m 短跑运动员；器械：无旋转套 Olympic 杠、有深蹲架、腿举机；单次课限 45 min；技术熟练。
  - expected: 排除 power clean（缺旋转套）；下肢以 back squat + 机器 leg press 换取时间（f18-08 例），配腿弯举/提趾平衡 knee flexor；核心清单标注 core(hip/thigh) 与 assistance；不选 lunge 因时间成本。
  - observed: 按类型→专项性→经验→器材→时间顺序筛选可得确定清单，与 c18-4（A 选 push jerk/hang power clean 等 power 动作配篮球起跳）逻辑一致；ce18-05（不得假定简单动作会做对）要求逐动作验技，纳入步骤。
- **V3_task_utility**: passed: true — 把"选动作"从偏好变为多约束求交流程，稳定交付 core/assistance/structural/power 标签清单（减少遗漏、统一分类口径）。
- **decision**: verified
- **if_not_verified**: —

---

## 能力单元 U5 — 训练频率（Step 3：状态×赛季双查表 + 恢复日间距 + split 时机）

- **proposed_capability_id**: cap.nsca.training-frequency
- **proposed_slug**: training-frequency
- **type**: procedure
- **merged_candidates**: [f18-09, f18-10, f18-11, p18-10, p18-11, p18-12, p18-35, c18-5]
- **task_ids**: [T04]
- **importance**: critical
- **source_evidence**:
  - source_id: src-nsca-essentials-5e
    location: Chapter 18, Step 3: Training Frequency + Tables 18.4/18.5/18.6/18.7（ch18.txt 第 794–943 行）
- **R 段可用原文引用**（英文，≤100 词，逐字）:
  > "When determining training frequency, the strength and conditioning professional should consider the athlete's training status, sport season, projected exercise loads, types of exercises, and other concurrent training or activities."（ch18.txt 798–799）
- **V1_source_sufficiency**: passed: true — 回查核对 Table 18.4（Beginner 2–3；Intermediate 3–4；Advanced 4–7，*可一天多次）与 Table 18.7（Off 4–6；Pre 3–4；In 1–3；Post 0–3）均与 p18-10/p18-12 一致；「同肌群至少 1 天、不超过 3 天恢复日」规则在 813–815 逐字；Table 18.5/18.6 全身推拉与分化模板完整（840–914）。
- **V2_executability**: passed: true
  - check_mode: walkthrough
  - input: 情境 A（Advanced，in-season，其他专项训练重）与情境 C（Beginner，preseason，兼需有氧耐力）。
  - expected: A：状态表 4–7 ∩ 赛季表 1–3 → 3 次/周（全身，周一/三/五）；C：状态表 2–3 ∩ 赛季表 3–4 → 2 次/周（周三/周六，重/轻）。同肌群间隔落在 1–3 天。
  - observed: 双查表取交集得 A=3、C=2，与 c18-5 原书指派（A=3、B=4 split、C=2）一致，输出明确。
- **V3_task_utility**: passed: true — 用状态×赛季双查表统一频率口径，并给出恢复日间距硬约束与 split 适用时机（稳定交付格式、识别失败边界）。
- **decision**: verified
- **if_not_verified**: —

---

## 能力单元 U6 — 动作顺序（Step 4）

- **proposed_capability_id**: cap.nsca.exercise-order
- **proposed_slug**: exercise-order
- **type**: procedure
- **merged_candidates**: [f18-12, f18-13, p18-13, p18-14, c18-6]
- **task_ids**: [T05]
- **importance**: high
- **source_evidence**:
  - source_id: src-nsca-essentials-5e
    location: Chapter 18, Step 4: Exercise Order（ch18.txt 第 984–1168 行）
- **R 段可用原文引用**（英文，≤100 词，逐字）:
  > "If power exercises are not selected in step 2 (exercise selection), the recommended order of exercises is core exercises (ideally with the most demanding exercises first) and then assistance exercises."（ch18.txt 1040–1043）
- **V1_source_sufficiency**: passed: true — 回查：默认主法（power→other core→assistance，理由＝神经需求大/易疲劳/耗能高）在 1027–1047 完整；上下肢交替（下肢先，20–30 s 间隔＝circuit training）1049–1067；push-pull 交替 1069–1091；superset/compound set 定义与适用边界 1093–1109 均完整。应用表（c18-6）含「下背训练置于中立脊柱动作之后」例外，与原文一致。
- **V2_executability**: passed: true
  - check_mode: walkthrough
  - input: 单次课动作＝push jerk、front squat、incline bench press、triceps pushdown。
  - expected: 顺序＝push jerk(power)→front squat(core,最难)→incline bench press(core)→triceps pushdown(assistance)；若时间紧可 push–pull 交替（如 front squat 与 seated row 交替）。
  - observed: 按默认主法即得明确序列，与 c18-6 Scenario A Monday 编排一致；校验关键稳定肌（erector spinae）未在两个动作中被连续过度疲劳。
- **V3_task_utility**: passed: true — 给出可执行排序规则与四种替代法及其适用条件，避免疲劳污染关键动作技术（改善决策结构、减少损伤风险）。
- **decision**: verified
- **if_not_verified**: —

---

## 能力单元 U7 — 确定与估算 1RM / xRM（Step 5 之测试与估算）

- **proposed_capability_id**: cap.nsca.one-rm-xrm-determination
- **proposed_slug**: one-rm-xrm-determination
- **type**: calculation
- **merged_candidates**: [f18-15, f18-16, f18-17, p18-17, p18-18, p18-19, p18-20, c18-7, c18-8, c18-15, c18-16]
- **task_ids**: [T06]
- **importance**: critical
- **source_evidence**:
  - source_id: src-nsca-essentials-5e
    location: Chapter 18, Step 5「1RM and xRM Testing Options / Testing the 1RM / Estimating a 1RM」+ Figure 18.8 + Table 18.9（ch18.txt 第 1331–1475、1477–1561 行）
- **R 段可用原文引用**（英文，≤100 词，逐字）:
  > "the strength and conditioning professional has the option of determining the athlete's actual 1RM (directly tested), estimated 1RM from an xRM test (e.g., a 10RM), or xRM based on the number of repetitions planned for that exercise (the 'goal' repetitions; e.g., 5 repetitions per set)."（ch18.txt 1333–1337）
- **V1_source_sufficiency**: passed: true — 回查：三条路径（直接 1RM / 由 xRM 估 1RM / 按目标次数做 xRM）齐备；Figure 18.8 九步增减档逐字核对（轻负荷 5–10 次→休息 1 min→上肢 +10–20 lb/5–10%、下肢 +30–40 lb/14–18 kg 或 10–20%→休息 2 min→…→失败时上肢 −5–10 lb/2.5–5%、下肢 −15–20 lb/5–10%），与 p18-17 一致；「辅助动作不重于 8RM」「power 不宜 >5 次 xRM」逐字；Table 18.9 表头 RM↔%1RM（1→100 … 15→65）与 p18-19 一致。**数值复核**：原文示例 10RM=300 lb→1RM=400 lb；表中 1RM=400 行在第 10RM(75%) 列确为 300，自洽。预测方程系数原文未给（仅指向文献），p18-20 如实标注为缺口，未补造。
- **V2_executability**: passed: true
  - check_mode: walkthrough
  - input: 新输入 A：某运动员 3RM 悬垂高翻＝115 lb；新输入 B：某运动员 10RM 深蹲＝225 lb。
  - expected: A：1RM ≈ 115 ÷ 0.93 ≈ 123.7 → 124 lb（与原文 c18-7 的 124 lb 一致，容差 ±1）。B：1RM ≈ 225 ÷ 0.75 = 300 lb（容差 ±2）。
  - observed: 用 Table 18.9 横读（3RM 行→1RM 行；10RM 行→1RM 行）分别得 124 lb 与 300 lb，结果明确可核对；低 1RM 者（如深蹲 1RM 100 lb）改用相对百分比增量（c18-16）以避免过大绝对增量，纳入步骤。
- **V3_task_utility**: passed: true — 把"测什么、怎么加、如何估算"固化为统一口径与容差，输出可复核的 1RM 数值（统一指标口径、节省重复操作）。
- **decision**: verified
- **if_not_verified**: —

---

## 能力单元 U8 — 按训练目标分配负荷与重复（Step 5 核心）

- **proposed_capability_id**: cap.nsca.load-reps-by-goal
- **proposed_slug**: load-reps-assignment
- **type**: calculation
- **merged_candidates**: [f18-14, f18-18, f18-19, p18-16, p18-23, p18-24, c18-7]
- **task_ids**: [T07]
- **importance**: critical
- **source_evidence**:
  - source_id: src-nsca-essentials-5e
    location: Chapter 18, Step 5「Relationship Between Load and Repetitions / Repetition Maximum Continuum / Percentage of the 1RM / How to Calculate a Training Load」+ Table 18.8 + Table 18.11（ch18.txt 第 1233–1330、1735–1826 行）
- **R 段可用原文引用**（英文，≤100 词，逐字）:
  > "focusing on one training goal automatically implies the use of a certain load and repetition regimen (e.g., training for maximal muscular strength involves lifting very heavy loads [i.e., ≥80% 1RM] for few repetitions [i.e., ≤6 repetitions])."（ch18.txt 1236–1239）
- **V1_source_sufficiency**: passed: true — 回查 Table 18.8 逐档：100→1、95→2、93→3、90→4、87→5、85→6、83→7、80→8、77→9、75→10、70→11、67→12、65→15，与 p18-16 一致；Table 18.11：Strength ≥85%/≤6、Multiple-effort 75–85%/3–5、Hypertrophy 67–80%/8–12、Muscular endurance ≤67%/≥12，与 p18-23 一致；「How to Calculate」示例（1RM 220 lb、力量目标、分配 4 次→≈90%=200 lb）逐字核对无误。**已知数值不一致**：Scenario B 应用表文本写「Assign 70% of the tested 1RM」，但所列负荷（如 deadlift 650→490 lb）实为 ~75%；此为原书内部不一致，登记于文末「数据冲突登记」，核心规则（Table 18.11）不受影响。
- **V2_executability**: passed: true
  - check_mode: walkthrough
  - input: 新输入 X：卧推 1RM＝220 lb，目标＝strength，分配 4 次 → 期望 %1RM≈90%，负荷≈198–200 lb。新输入 Y：深蹲 1RM＝300 lb，目标＝hypertrophy，分配 10 次 → 期望 %1RM≈75%，负荷≈225 lb。
  - expected: X：200 lb（90%×220=198，书取整 200，容差 ±5）。Y：300×0.75=225 lb（容差 ±5）。
  - observed: 按"由目标定最小 %1RM→由目标次数在表 18.8 取百分数→乘 1RM→观察难易微调"三步，X 得 ≈200 lb、Y 得 225 lb，均与独立核算一致。
- **V3_task_utility**: passed: true — 把"目标→%1RM→次数→具体重量"锚定为单一可复核链条，输出确定负荷（统一指标口径、稳定交付格式）。
- **decision**: verified
- **if_not_verified**: —

---

## 能力单元 U9 — power 训练负荷赋值特例

- **proposed_capability_id**: cap.nsca.power-load-assignment
- **proposed_slug**: power-load-assignment
- **type**: decision-framework
- **merged_candidates**: [f18-20, p18-25, p18-29]
- **task_ids**: [T07]
- **importance**: high
- **source_evidence**:
  - source_id: src-nsca-essentials-5e
    location: Chapter 18, Step 5「Assigning Percentages for Power Training」+ Table 18.14（ch18.txt 第 1827–1910、2315–2343 行）
- **R 段可用原文引用**（英文，≤100 词，逐字）:
  > "Power exercises cannot be maximally loaded at any repetition scheme, because the quality of the movement technique will decline before momentary muscle fatigue defines a true xRM set... Therefore, lighter loads allow the athlete to complete repetitions with maximum speed to promote maximum power development."（ch18.txt 1897–1900）
- **V1_source_sufficiency**: passed: true — 回查：非举重多关节/单关节爆发动作峰值功率在极轻负荷（体重 0%–30% 1RM）；可重载的抓举/翻等取 75%–90%；抓接派生 60%–80%；拉动派生可 <50% 或 100%–120%；过顶推派生 80%–90%；爆发每组 ≤5 次、负荷可达 10RM(≈75%)；single-effort 1–2 次 @80%–90%、multiple-effort 3–5 次 @75%–85%；小位移动作（countermovement shrug/hang pull）可超最大 >100% 做 ≥6 次——以上均与 p18-25 一致。Table 18.14（mid-thigh clean/snatch 60%–80%(2–5)、mid-thigh pull/CM shrug 100%–140%(4–6)、hang high pull 45%–60%(4–6)、jump shrug 30%–45%(4–6)、push press 70%–90%(2–5)）与 p18-29 一致。
- **V2_executability**: passed: true
  - check_mode: walkthrough
  - input: 新输入：单次用力项铅球（push jerk 估 1RM 118 lb）；多次用力项排球（hang power clean 估 1RM 124 lb）。
  - expected: 铅球：1–2 次 @80%–90% → ≈95–106 lb。排球：3–5 次 @75%–85% → ≈93–105 lb。两者 %1RM 明显低于 Table 18.8 同次数档（避免误用）。
  - observed: 按"确认 power→按用力类型定次数→取 75%–90%（或更轻）区间→结合赛季管疲劳"可得明确区间；与原文 c18-7 中 push jerk 90 lb(75%)、hang power clean 95 lb(75%) 一致。
- **V3_task_utility**: passed: true — 识别"power 负荷与 %1RM–次数关系不一致"这一关键失败边界，防止把力量档负荷误套到爆发动作（识别失败边界）。
- **decision**: verified
- **if_not_verified**: —

---

## 能力单元 U10 — 替代/自调负荷法（RPE / RIR / SRB）

- **proposed_capability_id**: cap.nsca.rpe-rir-srb
- **proposed_slug**: rpe-rir-srb-load
- **type**: decision-framework
- **merged_candidates**: [f18-24, p18-21, p18-22]
- **task_ids**: [T07]
- **importance**: medium
- **source_evidence**:
  - source_id: src-nsca-essentials-5e
    location: Chapter 18, Step 5「RPE and Repetitions in Reserve / Set-Repetition Best」+ Table 18.10（ch18.txt 第 1604–1716 行）
- **R 段可用原文引用**（英文，≤100 词，逐字）:
  > "RPE and RIR may be best used if combined with an objective method (e.g., percentage of 1RM) so that the desired loads for a given exercise can be determined before using RPE/RIR to adjust the load for autoregulation purposes... consider limiting load autonomy until the athletes can display proficiency with the RPE and RIR methods."（ch18.txt 1628–1636）
- **V1_source_sufficiency**: passed: true — 回查：RPE(CR10 0–10) 与 RIR 定义、RIR 需接近高强度才准、按区间处方（RPE 7–8/RIR 2–3）、先用 %1RM 定基础再做自调、新手限制自主权——均完整；SRB 定义（基于某组次表现估最大、5% 档、3×5≈85%–90% 起次周 90%–95%、重日比轻日重 10%–15%、3×5 负荷较 3×2 低约 15%）完整，与 p18-22 一致；Table 18.10 的 RPE×RIR×SRB% 对应（Maximal 10/0/100%…Very,very light 1–2/<60%）与 p18-21 一致，含部分空白格。原文承认 RPE(8 周)/RIR(12 周) 证据有限，如实保留。
- **V2_executability**: passed: true
  - check_mode: walkthrough
  - input: 新输入：某核心动作先用 %1RM 定为 85%（客观基础）；当日状态好，教练拟自调。
  - expected: 按区间处方为 RPE 7–8 / RIR 2–3；若用 SRB，3×5 第一周取该组次估计最大负荷的 85%–90%、次周 90%–95%。新手（如情境 C）先不给自主调负荷权。
  - observed: 按"先客观定基础→区间自调/或 SRB 5% 档逐周递进→新手限制自主"可得出确定的负荷百分比区间，结果明确。
- **V3_task_utility**: passed: true — 为无法频繁测 RM 的场景提供可执行的替代口径与递进档，并识别 RIR 在远离力竭时失准的边界（节省重复操作、识别失败边界）。
- **decision**: verified
- **if_not_verified**: —

---

## 能力单元 U11 — 负荷进阶：何时加（2-for-2）与加多少（增幅/重轻日变异）

- **proposed_capability_id**: cap.nsca.load-progression
- **proposed_slug**: load-progression
- **type**: procedure
- **merged_candidates**: [f18-21, f18-22, f18-23, p18-04, p18-26, p18-27, p18-33, c18-9, c18-10]
- **task_ids**: [T08]
- **importance**: high
- **source_evidence**:
  - source_id: src-nsca-essentials-5e
    location: Chapter 18, Step 5「Progression of Load / Timing Load Increases / Quantity of Load Increases / Variation of the Training Load」+ Table 18.12（ch18.txt 第 1947–2012、1912–1945 行）
- **R 段可用原文引用**（英文，≤100 词，逐字）:
  > "If the athlete can perform 2 or more repetitions over his or her assigned repetition goal for a given exercise in the last set in two consecutive workouts, weight should be added to that exercise for the next training session."（ch18.txt 1957–1959）
- **V1_source_sufficiency**: passed: true — 回查：2-for-2 规则与其局限（不考量技术/阶段目标/相对强度、可能导向力竭、靠改技术凑数则不加）在 1955–1977 完整；Table 18.12（较弱上肢 2.5–5 lb/下肢 5–10 lb；较强上肢 5–10+ lb/下肢 10–15+ lb；SRB≈5%/周；相对替代 2.5%–10%）与 p18-27 一致；重/轻日变异（每周 1 个重日留 1–2 RIR、轻日＝重日 80%、次数不变、可推广任意频率、与专项轻重错配）与 p18-33 一致；渐进须基于训练需求与状态（p18-04）亦在此承载。
- **V2_executability**: passed: true
  - check_mode: walkthrough
  - input: 新输入：卧推指派 3×6；运动员连续两次末组各完成 8 次，技术稳定；运动员属"较强、上肢"。
  - expected: 满足 2-for-2 → 下次加负荷；增幅按较强上肢 5–10+ lb（或用 2.5%–10% 相对）。
  - observed: 依 2-for-2 判定加负荷，并按 Table 18.12 取 +5–10 lb；与 c18-9 示例一致。若技术为凑数而变形则不加。
- **V3_task_utility**: passed: true — 给出"何时加+加多少"的确定判据并附失败边界（技术/阶段目标/力竭），避免随意加重（改善决策结构、识别失败边界）。
- **decision**: verified
- **if_not_verified**: —

---

## 能力单元 U12 — 训练量分配（Step 6）+ volume-load 计算

- **proposed_capability_id**: cap.nsca.volume-assignment
- **proposed_slug**: training-volume
- **type**: calculation
- **merged_candidates**: [f18-25, f18-26, p18-15, p18-28, p18-30, c18-11, c18-12, c18-18]
- **task_ids**: [T09]
- **importance**: critical
- **source_evidence**:
  - source_id: src-nsca-essentials-5e
    location: Chapter 18, Step 6: Volume +「Terminology … Mechanical Work」+ Table 18.13（ch18.txt 第 2177–2381、1174–1232 行）
- **R 段可用原文引用**（英文，≤100 词，逐字）:
  > "Repetition-volume is the total number of repetitions performed during a workout session, and volume–load is the total number of sets multiplied by the number of repetitions per set, then multiplied by the weight lifted per repetition."（ch18.txt 2180–2183）
- **V1_source_sufficiency**: passed: true — 回查：volume-load 定义与示例（2×10×50 lb=1000 lb；80 kg 运动员+40 kg 跳蹲、4×3=120×12=1440 kg）逐字核对一致；system mass 与仅外部负荷的区分、volume-load displacement（5'6" vs 6'0" 做功差异）完整；Table 18.13（Strength ≤6 / 1-3·≥3·≥3；Power 1-3 / n/a·1-3·3-6；single-effort 3-6 / 1-3·3-6；Hypertrophy 8-12·6-12·3-12 / 1-3·≥3·≥3；Muscular endurance 12-15·12-15·12-25 / 1-3·≥3·≥3）与 p18-28 一致；单组 vs 多组规则（p18-30）与「辅助 1–3 组」「8 组/肌群剂量-反应」齐备。
- **V2_executability**: passed: true
  - check_mode: walkthrough
  - input: 新输入 A：4 组 × 6 次 × 100 kg 深蹲 → 期望 2400 kg。新输入 B：90 kg 运动员负重跳蹲、外部 30 kg、5 组 × 3 次 → 系统质量 120 kg，期望 120×15=1800 kg。
  - expected: A＝2400 kg（容差 0）；B＝1800 kg（容差 0）。
  - observed: 按 sets×reps×load（系统质量动作加体重）核算，A=2400、B=1800，与独立核算一致；与 c18-11（1000 lb、1440 kg）口径相同。
- **V3_task_utility**: passed: true — 统一 volume-load 计算口径（含系统质量/位移修正），使跨动作、跨周的量可比较，服务减量周与过度训练规避（统一指标口径）。
- **decision**: verified
- **if_not_verified**: —

---

## 能力单元 U13 — 组间休息时长（Step 7）

- **proposed_capability_id**: cap.nsca.rest-periods
- **proposed_slug**: rest-periods
- **type**: procedure
- **merged_candidates**: [f18-27, f18-28, p18-31, p18-32, c18-13]
- **task_ids**: [T10]
- **importance**: high
- **source_evidence**:
  - source_id: src-nsca-essentials-5e
    location: Chapter 18, Step 7: Rest Periods + Table 18.15（ch18.txt 第 2430–2519 行）
- **R 段可用原文引用**（英文，≤100 词，逐字）:
  > "not all exercises in a resistance training program should be assigned the same rest periods. It is important that the strength and conditioning professional allocate rest periods based on the relative load lifted and the amount of muscle mass involved in each exercise."（ch18.txt 2443–2446）
- **V1_source_sufficiency**: passed: true — 回查 Table 18.15：Strength 2–5 min；Power(single/multiple-effort) 2–5 min；Hypertrophy 多关节 2–3 min、单关节 60–90 s；Muscular endurance ≤30 s，与 p18-31 一致；脚注「辅助动作 %1RM 可能落在目标区间之外，应按该动作实际负荷分配休息」逐字在 2463–2467；示例（4RM 卧推 4 min vs 12RM 侧平举 1 min）与 p18-32 一致；应用表 c18-13（A power/core 3 min、assist 60–90 s；B core 2–3 min、assist 60–90 s；C core 30 s、assist ≤20 s）与原文一致。
- **V2_executability**: passed: true
  - check_mode: walkthrough
  - input: 新输入：同一力量（strength）程序内含 4RM bench press（核心、多关节）与 12RM lateral shoulder raise（辅助、单关节）。
  - expected: bench press → 约 3–4 min（力量档 2–5 min，取该 RM 对应偏长）；lateral raise → 60–90 s（按实际 12RM 负荷落在肥大/单关节档）。
  - observed: 按"先按目标查表→再按该动作实际相对负荷与肌群量逐动作微调"可得明确两值，与原文示例一致；避免整堂课套用单一休息值。
- **V3_task_utility**: passed: true — 防止"整堂课一个休息值"的常见错误，逐动作统一口径并识别辅助动作越出目标档的边界（改善决策结构、识别失败边界）。
- **decision**: verified
- **if_not_verified**: —

---

## 能力单元 U14 — 完整 7 步抗阻训练计划设计（端到端 SOP）

- **proposed_capability_id**: cap.nsca.seven-step-program
- **proposed_slug**: seven-step-program-design
- **type**: procedure
- **merged_candidates**: [f18-29, p18-06, c18-14]
- **task_ids**: [T11]
- **importance**: critical
- **source_evidence**:
  - source_id: src-nsca-essentials-5e
    location: Chapter 18, program design variables + Conclusion + Application of All Program Design Variables（ch18.txt 第 191–204、2520–2530、2597–2650 行）
- **R 段可用原文引用**（英文，≤100 词，逐字）:
  > "The process begins with a needs analysis to determine the specific demands of the sport and the training status of the athlete. With this knowledge, appropriate exercises are selected, and training frequency is established. The order of exercises in the workout is considered next, followed by load assignments and training volume choices based on desired training outcomes. Deciding on the length of the rest periods is the last step"（ch18.txt 2522–2528）
- **V1_source_sufficiency**: passed: true — 回查：七变量清单逐项（1 Needs analysis … 7 Rest periods）在 197–203；三情境综合应用表（A in-season 周一 push jerk 3×3@90 lb、front squat 3×4@155 lb…；B 周一/周二重日、周四/周五取重日 80%–85%；C 耐力 3×12）与 c18-14 一致；结论段给出端到端流程。变量强耦合未在原文给回环规则，如实保留（不补造）。
- **V2_executability**: passed: true
  - check_mode: walkthrough
  - input: 新输入（情境 C 变体）：17 岁高中越野跑者，preseason，Beginner，无 1RM 测试（用 6RM 估），器械有限，兼需有氧耐力。
  - expected: 产出可直接执行的计划：Step1 需求分析（主目标 muscular endurance）→ Step2 动作（core 3–4 + assistance）→ Step3 频率 2×/周（周三/周六，重/轻）→ Step4 顺序（core→assistance、上下肢交替）→ Step5 负荷（<67% 估 1RM、≥12 次；辅助按 8RM 上限）→ Step6 量（core 12–15 次、assist 1–3 组）→ Step7 休息（core ≤30 s、assist ≤20 s）。
  - observed: 七步依次得组数×次数×负荷×休息的完整周计划，与 c18-14 Scenario C 一致，交付物齐全。
- **V3_task_utility**: passed: true — 提供唯一能产出"可直接执行计划"的端到端 SOP（稳定交付格式、把 U1–U13 串成可交付物）。
- **decision**: verified
- **if_not_verified**: —

---

## 能力单元 R1（reference）— 无氧运动处方的原则层（六原则 / SAID / 个体化）

- **proposed_capability_id**: cap.nsca.anaerobic-principles
- **proposed_slug**: anaerobic-prescription-principles
- **type**: framework
- **merged_candidates**: [p18-01, p18-02, p18-05, ce18-01]
- **task_ids**: [T01, T03]
- **importance**: medium
- **source_evidence**:
  - source_id: src-nsca-essentials-5e
    location: Chapter 18, Principles of Anaerobic Exercise Prescription（ch18.txt 第 34–187 行）
- **R 段可用原文引用**（英文，≤100 词，逐字）:
  > "Resistance training programs for athletic populations require attention to the principles of specificity, overload, progression, variation, reversibility, and individualization."（ch18.txt 35–37）
- **V1_source_sufficiency**: passed: true — 回查：六原则（specificity/overload/progression/variation/reversibility/individualization）逐条在 34–187 完整展开；SAID 界定与「不等于逐帧复制运动动作」在 52–61；个体化 80%–90% 动作共用、10%–20% 个体化、负荷始终个体化在 183–187。均为可重建的规则。
- **V2_executability**: passed: false — 属**指导性原则**，无可独立执行的步骤/输出；固定新输入无法产生一个"明确结果"（它约束其他单元，而非自身产出交付物）。
- **V3_task_utility**: passed: true — 作为所有 U 单元的顶层约束与 B 段（边界）来源。
- **decision**: reference
- **if_not_verified**: 并入 `book/overview.md` 的「原则层」参考区；其可操作化部分已分别落进 U1（个体化）、U4（SAID/专项性）、U11（渐进）。

---

## 能力单元 R2（reference）— 过载也可由"减量"构成（减量周/超量恢复）

- **proposed_capability_id**: cap.nsca.overload-deload
- **proposed_slug**: overload-includes-deload
- **type**: rule
- **merged_candidates**: [p18-03]
- **task_ids**: [T08]（与 B 簇周期化交界）
- **importance**: medium
- **source_evidence**:
  - source_id: src-nsca-essentials-5e
    location: Chapter 18, Overload / Figure 18.1（ch18.txt 第 70–100 行）
- **R 段可用原文引用**（英文，≤100 词，逐字）:
  > "a reduction in intensity (i.e., relative load) allows for an increase in the speed of a movement, thus facilitating the development of rapid force production characteristics... a reduction in training volume while maintaining (or increasing) intensity during a deload week may lead to an enhancement in performance"（ch18.txt 87–91）
- **V1_source_sufficiency**: passed: true — 降强度提速度、减量周（fitness-fatigue）两类"负向过载"均在原文明确。
- **V2_executability**: passed: false — 为跨周期的时序化规则（减量周），其执行载体是周期化计划，属 B 簇（T12–T13）年度/中周期编排；在本簇不能产生独立可交付物。
- **V3_task_utility**: passed: true — 为 U11（负荷变异）与 B 簇减量周提供理论依据。
- **decision**: reference
- **if_not_verified**: 并入 `book/overview.md` 原则层；执行流程由 **B-periodization 簇**承载（减量周编排）；本簇不重复收（U11 只保留"重/轻日 80%"这一周内变异规则）。

---

## 能力单元 R3（reference）— 训练到力竭的谨慎规则

- **proposed_capability_id**: cap.nsca.failure-caution
- **proposed_slug**: avoid-training-to-failure
- **type**: rule
- **merged_candidates**: [p18-34, ce18-02]
- **task_ids**: [T07, T09]
- **importance**: medium
- **source_evidence**:
  - source_id: src-nsca-essentials-5e
    location: Chapter 18, How to Calculate a Training Load 段（ch18.txt 第 1821–1826 行）与 Step 6 段（2214–2221）
- **R 段可用原文引用**（英文，≤100 词，逐字）:
  > "it is important to avoid training to failure on a regular basis because it may not be necessary to maximize muscular hypertrophy, strength, or power adaptations"（ch18.txt 1821–1823）
- **V1_source_sufficiency**: passed: true — 原文两处明确"常规力竭非必要"，并说明减少力竭可降总训练应力、仍保有效刺激；近力竭使 24 h 疲劳增大。
- **V2_executability**: passed: false — 为**约束性规则**（禁止项），非独立流程/计算，无法单独演练出交付物；其判定（如重日留 1–2 RIR）已寄生于 U11/U12。
- **V3_task_utility**: passed: true — 作为 U8/U11/U12 的失败边界（防止把力竭当目标）。
- **decision**: reference
- **if_not_verified**: 并入 `book/overview.md` 的安全边界/参考区；其可操作形式已并入 U11（重日留 RIR）。

---

## 覆盖核查表（T01–T11）

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

## 跨簇重复候选（f13-01…f13-15、p13-01…p13-26，共 41 条）

这 41 条由 `_make_clusters.py` 同时分配给 **A-plan-design** 与 **C-testing**（CLUSTERS 中 A 与 C 均含前缀 `f13`/`p13`）。其对应任务为 **T20–T23（测试选择/实施/数据解释）与 T40**，**不在本簇 T01–T11 范围内**。

- 处理决定：**不在本簇重复展开**（遵循任务书「发现重叠 → 在本簇不要重复收，注明『由 X 簇承载』」）；全部 f13-*/p13-* 的 V1/V2/V3 由 **C-testing 簇**完成与承载。
- 在本簇的唯一关联：T01 的「评估运动员」子步骤引用 Ch13/Ch14 的测试结果与常模；该输入已在 U1 中体现为「conducting a variety of tests … evaluating the results, compared with normative data」（ch18.txt 284–401），测试项目本身不在此重建。
- 建议：阶段 1.6 去重时，f13-*/p13-* 的 canonical 归属统一记为 C-testing，避免两张能力卡承载同一测试方法论。

---

## 本簇缺口清单

1. **无 critical/high 任务缺口**：T01–T11 均有原文支撑并 verified。
2. **数据冲突登记（未静默消失）**：Ch18 Step 5 应用表（Scenario B，off-season/hypertrophy）文本写「Assign 70% of the tested 1RM」，但所列负荷（deadlift 650→490 lb、back squat 675→505 lb、bench press 425→320 lb、shoulder press 255→190 lb）实按 ~75% 计算（650×0.75=487.5、675×0.75=506.25、425×0.75=318.75、255×0.75=191.25）。此为**原书内部不一致**（可能为表格取整/笔误）。核心规则来自 Table 18.11（hypertrophy 67%–80%），不受影响；U8 仍判 verified，但 c18-7 该行数值不应作为"70% 负荷"范例使用。若阶段 2 需引用该 worked example，建议按 Table 18.11 的 67%–80% 区间自行核算，或注明原书例值系 ~75%。
3. **原文未给的规则**（如实保留，未用常识补齐）：① p18-20 未列具体 1RM 预测方程系数（仅指向文献）；② 肌肉平衡未给具体肌群对的比值阈值；③ 动作类型存在边界争议（如 lunge 是否 core）；④ 变量强耦合无回环量化规则（U14 已注明不含回环）。这些不阻塞对应单元的通用可执行性。

---

## 供阶段 2 的提示

- **建议组合**：U7（确定/估算 1RM）+ U8（按目标分配负荷）+ U9（power 特例）+ U10（RPE/RIR/SRB）+ U11（进阶）可合成一张「负荷处方族」能力卡的不同 A2 分支；U1+U2+U3 合成「需求分析→状态→目标」入口；U4+U5+U6 合成「选择→频率→顺序」；U12+U13 合成「量与休息」。
- **A1 素材（原书 worked example / case）**：
  - U1→c18-1（三情境）、c18-3（需求分析应用表）、c18-17（足球 IMTP/CMJ/mRSI 剖面）
  - U2→c18-2（Table 18.1 分类示例）
  - U4→c18-4（动作选择应用表）；边界用 ce18-04（失衡）、ce18-05（假定会做对）
  - U5→c18-5（频率应用表）
  - U6→c18-6（动作顺序应用表）
  - U7→c18-8（10RM 300→1RM 400）、c18-7（3RM 115→124 lb）、c18-16（低 1RM 增量）
  - U8→c18-7（Scenario A/B/C 负荷指派）
  - U11→c18-9（2-for-2）、c18-10（Table 18.12 增量）
  - U12→c18-11（vol-load 1000 lb / 1440 kg）、c18-12（量应用表）、c18-18（位移做功）
  - U13→c18-13（休息应用表）
  - U14→c18-14（三情境完整周计划）
- **B 段（边界）素材**：ce18-01（cookie-cutter → 个体化）、ce18-02（力竭）、ce18-03（多主目标）、ce18-06（不兼容素质同训）、ce18-04（肌力失衡）；并援引 BOOK_OVERVIEW 3.3 的「变量强耦合，不可孤立套用单一参数」「共识≠实证，参数应与个体响应结合」。
- **与 B 簇去重**：本簇不承载年度/中周期减量周编排（p18-03 已判 reference 并注明「由 B 簇承载」）；U11 只保留周内重/轻日 80% 变异规则。


---

<!-- ===== 簇 B-periodization ===== -->

# 簇 B-periodization — 三重验证结果

- 负责任务: T12, T13
- 候选输入: 81 条（来自 cases-g2-ch15-26.md、counter-examples-g2-ch15-26.md、frameworks-g4-ch20-22.md、frameworks-g5-ch23-26.md、principles-g4-ch20-22.md、principles-g5-ch23-26.md）
  - 其中 **50 条属 Ch22（本簇在范围）**：c22-1~3、ce22-01~05、f22-01~19、p22-01~23
  - 其中 **31 条属 Ch24（f24-01~10、p24-01~21）**：按簇交界约定 **属簇 H**，本簇不重复验证，见"本簇缺口清单/交界移交"
- 归并后能力单元: 11 个
- 分流: **verified: 9 / reference: 2 / needs_review: 0 / rejected: 0**
- 支持材料（case / counter-example，作为 A1/B 素材保留，不计入能力单元）: c22-1、c22-2、c22-3；ce22-01~05
- 回查原文: `.cangjie/source/ch22.txt`（主，逐行核对）、`ch24.txt`（仅用于确认交界，不重复收取）

> 说明：本簇的核心数值载体是 **Table 22.2（周期层级时长）** 与 **Table 22.3（周期性抗阻模型各期强度/量/组次）**；"如何填充一个中周期"的流程与之归并为 U6。Ch24 的过度训练/恢复/监控内容（f24-*、p24-*、ce24-01）属簇 H，本簇仅在其被周期化理论直接引用处（GAS f22-09、刺激—疲劳—恢复 f22-10、体能—疲劳 f22-11）收取，已并入 U7。

---

## 能力单元 U1 — 周期化的分层定位与三级建立流程

- **proposed_capability_id**: cap.nsca.periodization-three-level-build
- **proposed_slug**: periodization-three-level-build
- **type**: procedure
- **merged_candidates**: [f22-01, f22-02, p22-01, p22-02]
- **task_ids**: [T12]
- **importance**: high
- **source_evidence**:
  - source_id: src-nsca-essentials-5e
    location: Chapter 22 "Periodization and Planning the Training Process"（ch22.txt 第 44–63、223–263 行；Table 22.1 第 227–248 行；定义框第 102–105 行）
- **R 段可用原文引用**（英文，≤100 词，逐字）:
  > "periodization serves as the macro-management level of the training process, while programming allows for the micro-management of the process. Conceptually, periodization serves as a method for organizing deliberate practice by providing the scaffold from which programming decisions are made."
- **V1_source_sufficiency**: passed: true — 回查 ch22.txt 确认有三层（periodization/planning/programming）的完整说明（第 250–263 行）与 Table 22.1 三层级映射（第 227–248 行），并给出定义框逐字句（第 102–105 行）。f22-01/p22-01/p22-02 与原文一致；f22-02 的三级"从大框架→选模型→填内容"顺序亦逐条对应原文。未发现冲突。
- **V2_executability**: passed: true
  - check_mode: walkthrough
  - input: 某大学足球运动员，单赛季（8 月–12 月），已知竞赛日程与主项目标。
  - expected: 产出三级产物——(1) 一级 scaffold：按日程把年度计划切成 off/preseason/in-season/postseason 及 macrocycle；(2) 二级模型选择：据赛程密度与训练状态给出 parallel/sequential/emphasis 之一；(3) 三级落地：给出 modes/methods 与负荷/结构。缺日程则停在一级并标注缺失输入。
  - observed: 一级得到"1 个 macrocycle + 4 个时期"骨架；二级因赛程密集、运动员为中高级 → 选 emphasis；三级列出抗阻/plyo/专项 modes 与 microcycle 负荷结构。流程可产出确定交付物。
- **V3_task_utility**: passed: true — 统一"周期化≠编程"的口径，避免把 macro 层决策与 micro 层微调混为一谈；稳定交付"三级计划骨架"这一中间产物。
- **decision**: verified
- **if_not_verified**: —

---

## 能力单元 U2 — 三种周期化模型的选择框架（parallel / sequential / emphasis）

- **proposed_capability_id**: cap.nsca.periodization-model-choice
- **proposed_slug**: periodization-model-choice
- **type**: framework
- **merged_candidates**: [f22-03, p22-09, p22-10]
- **task_ids**: [T12]
- **importance**: high
- **source_evidence**:
  - source_id: src-nsca-essentials-5e
    location: Chapter 22 "Models of Periodization"（ch22.txt 第 264–323 行；侧重轮换规则第 305–317 行）
- **R 段可用原文引用**（英文，≤100 词，逐字）:
  > "The parallel training models ... involve targeting all training factors simultaneously within one training session, training day, series of training days, or a microcycle ... Sequential training models ... were created to address the limitations associated with the parallel model ... Emphasis training models ... contain aspects of both parallel and sequential models of periodization."
- **V1_source_sufficiency**: passed: true — 回查确认三类模型各有独立小节与适用人群/项目（parallel 适青训与新手、第 269–284 行；sequential 适需更大刺激者并列举例项目、第 286–301 行；emphasis 适密集赛程中高级、每两周轮换重点、第 305–323 行）。f22-03/p22-09/p22-10 与之逐条对应，无越读。
- **V2_executability**: passed: true
  - check_mode: walkthrough
  - input: 两名运动员——(A) 14 岁新手、多元素质发展期；(B) 中级短跑运动员、赛程密集。
  - expected: A → parallel（并注明其总负荷须持续上升、可能超耐受，不宜用于中/精英）；B → emphasis（并注明每两周轮换重点；部分因素过载、部分维持、部分最小剂量）。输出为"选哪种模型 + 理由 + 风险"。
  - observed: A 判 parallel、B 判 emphasis，均给出对应依据与局限，输出明确。
- **V3_task_utility**: passed: true — 把"选模型"从直觉变为可按训练状态与赛程密度查判的决策，改善决策结构；明确各模型的失败边界（parallel 不宜精英化）。
- **decision**: verified
- **if_not_verified**: —

---

## 能力单元 U3 — 周期层级结构与时长口径（Table 22.2）

- **proposed_capability_id**: cap.nsca.periodization-cycle-durations
- **proposed_slug**: periodization-cycle-durations
- **type**: framework
- **merged_candidates**: [f22-04, p22-03]
- **task_ids**: [T12]
- **importance**: medium
- **source_evidence**:
  - source_id: src-nsca-essentials-5e
    location: Chapter 22 "Periodization Hierarchy"（ch22.txt 第 324–394 行；Table 22.2 第 360–394 行）
- **R 段可用原文引用**（英文，≤100 词，逐字）:
  > "Mesocycle 2-6 weeks ... This medium-sized training cycle is sometimes called a block of training ... The most common duration is 4 weeks. Microcycle ... can range from several days to 2 weeks in duration; the most common duration is 1 week (7 days)."
- **V1_source_sufficiency**: passed: true — 回查 Table 22.2（第 360–394 行）与正文（第 324–349 行）确认七级结构与时长：multiyear 2–4 年（最常见 quadrennial）、annual 1 年（可含单/多 macrocycle）、macrocycle 数月至一年、mesocycle 2–6 周（最常见 4 周）、microcycle 数天至 2 周（最常见 1 周/7 天）、training day 1 天、training session 数小时（课内休息 >30 min 视为多次 workout）。"单项目=年度即单 macrocycle""大学田径=室内外两 macrocycle"的说明亦在原文（第 334–340 行）。
- **V2_executability**: passed: true
  - check_mode: walkthrough
  - input: 需把一名运动员的 1 年计划按标准层级拆块，问"中周期与微周期各取多长"。
  - expected: 依 Table 22.2——mesocycle 取 2–6 周（默认 4 周）、microcycle 取 1 周（默认 7 天）；年内默认单 macrocycle。
  - observed: 得 meso=4 周、micro=1 周；52 周约合 13 个 4 周中周期（与样例的 14 个 2–4 周中周期同量级口径一致），输出为确定的时长取值。
- **V3_task_utility**: passed: true — 统一各周期时长的口径（避免 meso/micro 混用），为 U5 的年度排布提供"查表即可定长"的稳定交付格式。
- **decision**: verified
- **if_not_verified**: —

---

## 能力单元 U4 — 运动季节 ↔ 周期化时期映射与传统四期演变

- **proposed_capability_id**: cap.nsca.season-to-period-mapping
- **proposed_slug**: season-to-period-mapping
- **type**: framework
- **merged_candidates**: [f22-05, p22-17, f22-06]
- **task_ids**: [T12]
- **importance**: high
- **source_evidence**:
  - source_id: src-nsca-essentials-5e
    location: Chapter 22 "Periodization Periods" / "Applying Sport Seasons to the Periodization Periods"（ch22.txt 第 395–476 行预备期、第 671–735 行季节映射）
- **R 段可用原文引用**（英文，≤100 词，逐字）:
  > "The off-season should be considered the preparatory period ... The first transition period is often undertaken at this time with a focus on the strength/power phase ... The competitive, or in-season, period contains all the contests scheduled for the given year ... the postseason or second transition period provides the athlete with a relative or active rest."
- **V1_source_sufficiency**: passed: true — 回查确认四期（preparatory/first transition/competitive/second transition，第 416–422 行）与四赛季（off/preseason/in-season/postseason）的逐一双向映射（第 685–735 行），并含"preseason 不是建基础之时、基础在 off-season"的关键提醒（第 706–710 行）。f22-06 的"高量低强→低量高强"演变律见第 403–406 行，且明确"图上看似直线实为非线性"（第 428–436 行）。三候选互不矛盾。
- **V2_executability**: passed: true
  - check_mode: walkthrough
  - input: 美式橄榄球运动员（仅 fall 一个赛季）。
  - expected: off-season→preparatory（含 general/specific 两相）；preseason→first transition（strength/power）；in-season→competitive（全部比赛）；postseason→second transition（active rest）；并给出"焦点由高量低强向低量高强迁移"的时序。
  - observed: 输出季节↔时期对应表 + 各期焦点，且标注 preseason 应"收割 off-season 成果"。交付物明确。
- **V3_task_utility**: passed: true — 把抽象的"四期"锚定到运动员真实赛季日历，减少映射遗漏；统一"preseason=first transition"的口径，纠正"preseason 建基础"的常见误用。
- **decision**: verified
- **if_not_verified**: —

---

## 能力单元 U5 — 年度训练计划（macrocycle）的编排流程

- **proposed_capability_id**: cap.nsca.annual-plan-construction
- **proposed_slug**: annual-plan-construction
- **type**: procedure
- **merged_candidates**: [f22-13, p22-19]
- **task_ids**: [T12]
- **importance**: critical
- **source_evidence**:
  - source_id: src-nsca-essentials-5e
    location: Chapter 22 "Example of an Annual Training Plan"（ch22.txt 第 792–921 行；Figure 22.8 结构第 847 行）
- **R 段可用原文引用**（英文，≤100 词，逐字）:
  > "The annual plan example provided in this chapter defines a macrocycle that lasts from May 1 until April 28 ... subdivided into four seasons: off-season (May 1-August 20), preseason (August 21-November 5), in-season (November 6-April 14), and postseason (begins on April 15) ... subdivided into 14 mesocycles, which range in length between two and four weeks."
- **V1_source_sufficiency**: passed: true — 回查确认样例年度计划完整结构（第 796–809 行）及各期目标（off 16 周第 811–845 行；preseason 第 849–857 行；in-season 约 22–23 周含 4 周锦标赛第 858–889 行；postseason 约 1 月第 890–897 行），并给出测试节点（5RM/3RM/2RM 预测试周）与抗阻优先级随期变化。**注意原文一处内部不一致**：第 798 行 preseason 记 "August 21-November 5"，但第 852 行正文写 "11 weeks (August 21-October 5)"；以后者与 in-season 起始日（11/6）冲突，判定为原文/提取笔误，采用与 in-season 衔接的 11/5。此不一致不影响流程可执行性。
- **V2_executability**: passed: true
  - check_mode: walkthrough
  - input: 一名单赛季运动员，赛季日历已知（含关键比赛与锦标赛期）。
  - expected: (1) 1 个 annual plan = 1 个 macrocycle；(2) 按四赛季切日期区间；(3) 细分为 2–4 周的 mesocycles（样例为 14 个）；(4) 每块标注目标相位与 microcycle 数；(5) 在 off-season/preseason 块间与 in-season 关键微周期安排卸载周；(6) 在 off-season 与赛季末安排测试周校准负荷。
  - observed: 输出含"赛季、中周期、微周期、测试节点"的时间表（可复现样例的 14 块结构），交付物完整明确。
- **V3_task_utility**: passed: true — 提供可复制的年度排布模板，稳定交付格式；把"何时测、何时卸载、何时加量"一次性落到时间轴，显著减少排布遗漏。
- **decision**: verified
- **if_not_verified**: —
- **备注**: 本单元的 A1 素材首选 **c22-1（女性篮球运动员年度计划样例，Figure 22.8）**——全书唯一完整年度计划样例。

---

## 能力单元 U6 — 用变量填充一个中周期（Table 22.3 数值核心 + 负荷落地）

- **proposed_capability_id**: cap.nsca.mesocycle-variable-filling
- **proposed_slug**: mesocycle-variable-filling
- **type**: calculation
- **merged_candidates**: [f22-08, p22-04, p22-11, p22-12, p22-13, p22-14, f22-07, p22-22, p22-23, f22-17]
- **task_ids**: [T12]
- **importance**: critical
- **source_evidence**:
  - source_id: src-nsca-essentials-5e
    location: Chapter 22 Table 22.3（ch22.txt 第 502–539 行）、各相正文框（第 546–548、562–564、595–597、636–641 行）、预备期细分（第 453–476 行）、样例微周期注记（第 1019、1725–1732 行）
- **R 段可用原文引用**（英文，≤100 词，逐字）:
  > "TABLE 22.3 ... Hypertrophy/strength endurance: 50%-75% 1RM, high, 3-6 sets, 8-20 reps. Basic strength: 80%-95% 1RM, Moderate to high, 2-6 sets, 2-6 reps. Strength/power: 87%-95% 1RMa / 30%-85% of 1RMb, Low, 2-5 sets, 2-5 reps. Peaking: 50% to ≥93% 1RM, Very low, 1-3 sets, 1-3 reps. Maintenance: 85%-93% 1RM, Low to moderate, ~2-5 sets, 3-6 reps."
  > "Note: Friday session should use a load 10% less than Monday's." / "3 to 5 warm-up sets should be performed"
- **V1_source_sufficiency**: passed: true — 回查确认：Table 22.3 五行数值逐格与候选一致（第 510–537 行），含脚注 a（%1RM 用于非爆发核心动作）、b（用于爆发动作、实际百分比依动作）、c（组数不含热身组、仅目标核心组、且不含低强度恢复日）。各相正文框（hypertrophy 50–75%/3–6×8–20；basic strength 80–95%/2–6×2–6；strength/power 30–95% 依动作；competition peaking 50%–≥93%/1–3×1–3、maintenance 85–93%/~2–5×3–6）齐全。预备期两相序列（general→specific，hypertrophy→basic strength）见第 453–476 行。热身组 3–5 组（第 1728 行）、周五 -10%（第 1019 行，另第 1203 行 preseason 一处作 15% less）、"赛内用 %RM 区间不练到力竭"（第 1725–1727 行）均已核对。
  - **口径说明**：Table 22.3 的 strength/power 记 "87%–95% 1RMa / 30%–85% of 1RMb"，而正文框记 "30%–95% of the 1RM, depending on the exercise"——两处并存、均为原文，非冲突（前者按动作类型分列、后者为总括区间）。
  - **交界注明**：候选 f22-17/p22-23/p22-22 中"**%RM↔重复数、由多次 RM 估 1RM 的具体换算表（Table 18.8/18.9）属 Ch18、归簇 A**"；本单元只保留"**在年度计划的中周期上如何用这些变量落值**"的编排部分。
- **V2_executability**: passed: true
  - check_mode: walkthrough
  - input: 一名中级运动员，处于 **basic strength 相（specific preparatory）**；已测 **back squat 5RM = 120 kg**；按样例风格排一个 3 周中周期（目标组 3 组 × 5 次）。
  - expected（依 Table 22.3 + 样例 %RM 区间规则，独立核算，容差 ±1 kg）:
    - 周1 强度区间 80%–84% 5RM → 96–101 kg（0.80×120=96；0.84×120=100.8≈101）
    - 周2 强度区间 85%–89% 5RM → 102–107 kg（0.85×120=102；0.89×120=106.8≈107）
    - 周3 强度区间 90%–94% 5RM → 108–113 kg（0.90×120=108；0.94×120=112.8≈113）
    - 周五课 = 周一负荷 × 0.90（如周一 100 kg → 周五 90 kg）
    - 热身组另加 3–5 组，不计入 3 组目标组
    - 若该中周期落在竞赛期：改用 %RM 区间（如 75%–79% 6RM）而不练到力竭
  - observed: 上述取值全部可复算得到，输出为"一个带目标相位与变量取值的中周期"，与样例计划 Mesocycle 3（第 1071–1087 行 "80%-84% 5RM / 85%-89% 5RM / 90%-94% 5RM"）风格一致。数值核对通过。
- **V3_task_utility**: passed: true — 把 Table 22.3 的抽象档位转换为可按运动员 RM 直接落地的重量，是"变量应用"最核心的一步；统一"周五 -10%""3–5 组热身不计入""赛内用 %RM 区间"的口径，避免负荷误算。
- **decision**: verified
- **if_not_verified**: —

---

## 能力单元 U7 — 周期化三大机制理论（GAS / 刺激—疲劳—恢复 / 体能—疲劳）

- **proposed_capability_id**: cap.nsca.periodization-mechanistic-theories
- **proposed_slug**: periodization-mechanistic-theories
- **type**: framework
- **merged_candidates**: [f22-09, f22-10, f22-11, p22-05, p22-06, p22-07]
- **task_ids**: [T13]
- **importance**: medium
- **source_evidence**:
  - source_id: src-nsca-essentials-5e
    location: Chapter 22 "Central Concepts Related to Periodization"（ch22.txt 第 83–222 行；GAS 第 107–156 行；SFR 第 158–179 行；fitness–fatigue 第 187–212 行）
- **R 段可用原文引用**（英文，≤100 词，逐字）:
  > "a three-stage response to stress (alarm, resistance, and exhaustion)" ...
  > "the greater the overall magnitude of the workload encountered, the more fatigue accumulates and the longer the delay before complete recovery and adaption can occur."
  > "fatigue dissipates at a rate two-thirds faster than fitness"
- **V1_source_sufficiency**: passed: true — 回查确认三大理论均完整：GAS 三阶段及"慢性心理情绪压力延长 resistance 相、推迟超量补偿"（第 109–156 行）；SFR 理论（第 158–179 行，含"不必完全恢复即可再次训练""轻/重课调节"）；fitness–fatigue 两因子（第 187–212 行，含"疲劳消退比体能快约 2/3""各因素各有残余效应"）。**精度校正**：候选 f22-09 概括为"拉长警报期与抵抗期"，原文精确表述为"**alarm 期疲劳幅度增大、resistance 期被延长**"（第 128–132 行），p22-05 表述准确；写作时应采信 p22-05/原文。本章为 T13 的理论依据来源；Ch24（簇 H）为过度训练现象的展开，本单元不重复收取。
- **V2_executability**: passed: true
  - check_mode: walkthrough
  - input: 某运动员连续 3 周递增负荷后，5RM 下降约 8%、睡眠变差、自评恢复差。
  - expected: (1) 用 GAS 判是否滑向 exhaustion 相；(2) 用 SFR 解释"负荷幅度大→疲劳累积→恢复延迟"，并指出可用轻/重课交替调节；(3) 用 fitness–fatigue 说明"疲劳消退快于体能→适当减量可抬高 preparedness，而非一直加压"。给出"安排卸载周/降低负荷、并核查非训练压力"的决策。
  - observed: 三理论各自给出可检查的判读与措施建议（进入衰竭风险 → 卸载 + 管理生活压力），输出明确、未越读原文。
- **V3_task_utility**: passed: true — 为"为什么要周期化/何时该减"提供统一解释框架，改善决策结构；识别失败边界（进入 exhaustion 相）。
- **decision**: verified
- **if_not_verified**: —

---

## 能力单元 U8 — 峰值 vs 维持的决策框架（peaking / maintenance）

- **proposed_capability_id**: cap.nsca.peaking-vs-maintenance
- **proposed_slug**: peaking-vs-maintenance
- **type**: framework
- **merged_candidates**: [f22-15, p22-08, p22-14]
- **task_ids**: [T12]
- **importance**: high
- **source_evidence**:
  - source_id: src-nsca-essentials-5e
    location: Chapter 22 "Competitive Period"（ch22.txt 第 599–641 行）；巅峰窗口第 94–96 行
- **R 段可用原文引用**（英文，≤100 词，逐字）:
  > "Peaking programs attempt to place the athlete in peak condition for about one or two weeks. Trying to extend this to longer durations ultimately results in reduced performance capacity ... For team sports, this period spans an entire season and may last for many months, requiring the use of a maintenance program."
- **V1_source_sufficiency**: passed: true — 回查确认：peaking 窗口约 1–2 周、延长反降表现（第 614–618 行）；巅峰表现只能在 7–14 天内被优化、可维持时间与平均强度成反比（第 94–96 行，第 1640–1656 候选 p22-08 一致）；maintenance 85%–93% 1RM、中低量、按 microcycle 依训练/旅行/赛程调制（第 624–634 行）；竞赛期处方（peaking 50%–≥93%/1–3×1–3；maintenance 85–93%/~2–5×3–6）见第 636–641 行。三候选一致，无冲突。
- **V2_executability**: passed: true
  - check_mode: walkthrough
  - input: (A) 举重运动员，关键赛在 5 周后（短窗）；(B) 足球队，赛季约 6 个月（长窗）。
  - expected: A → 采用 peaking：约 1–2 周、强度 50%–≥93% 1RM、1–3 组 × 1–3 次、随 taper 由高强度转向低强度以降疲劳；B → 采用 maintenance：强度 85%–93% 1RM、约 2–5 组 × 3–6 次、在 microcycle 级依赛程调制并持续监测。
  - observed: 两者均得出确定的"峰值/维持"处方与调控要点；对"减量过度→fitness 同降→准备度下降"给出边界提醒（见 ce22-03）。
- **V3_task_utility**: passed: true — 依据赛季长度直接分派两种竞赛期打法，避免"团队项目也硬做峰值""个人短窗却全程维持"两类错误；稳定输出"强度/量/组次"档位。
- **decision**: verified
- **if_not_verified**: —

---

## 能力单元 U9 — 密集赛程/长赛季的赛内负荷编排与卸载周

- **proposed_capability_id**: cap.nsca.in-season-load-management
- **proposed_slug**: in-season-load-management
- **type**: procedure
- **merged_candidates**: [f22-16, f22-19, f22-14, p22-18, p22-20, p22-21]
- **task_ids**: [T12]
- **importance**: high
- **source_evidence**:
  - source_id: src-nsca-essentials-5e
    location: Chapter 22 "In-Season"（ch22.txt 第 712–728 行）、第二过渡期/卸载周（第 643–663 行）、样例注记（第 1720–1732 行）、Tournament Options（第 1690–1718 行）
- **R 段可用原文引用**（英文，≤100 词，逐字）:
  > "a long competitive season (12-16+ weeks) presents unique programming challenges—in these situations, three- or four-week mesocycle blocks that unload the athlete in the last microcycle ... Repetition maximum loads are not used, as training to failure has been shown to reduce power output and increase the risk of overtraining ... percentage ranges based off of RM loads are used to deal with the accumulated fatigue."
- **V1_source_sufficiency**: passed: true — 回查确认：长赛季（12–16+ 周）用 3 或 4 周中周期块、末个 microcycle 卸载（第 716–719 行）；microcycle 层依训练/旅行/赛程调制强度与量以维持力量爆发并管理疲劳（第 624–634、712–728 行）；卸载周的"次要用途"为在长阶段（3 周）之间插入一周（第 657–663 行）；周五 -10%（第 1019 行）；赛内不用 RM 负荷、改用 %RM 区间（第 1725–1727 行）。Tournament Options A/B/C 见第 1690–1718 行（另见 c22-2）。
- **V2_executability**: passed: true
  - check_mode: walkthrough
  - input: 某球队一周内连续 3 场背靠背比赛（对应 Tournament Option C）。
  - expected: 以 3–4 周中周期块组织，末周微周期设为卸载；比赛间安排 2–3 天恢复间隔后插入 plyometric/抗阻课；同一 microcycle 内升降强度与量；周内非关键课相对主课 -10% 负荷；赛内以 %RM 区间（如 75%–79% 6RM）替代力竭 RM。
  - observed: 可产出"比赛日 + 抗阻/plyo 插入 + 卸载微周期"的周计划（与 Option C 两行排布一致），交付物明确。
- **V3_task_utility**: passed: true — 解决"频繁比赛下如何不丢力量爆发"的排布问题，减少赛内加载遗漏；统一"末周卸载""-10%""%RM 区间"口径。
- **decision**: verified
- **if_not_verified**: —

---

## 能力单元 U10 — 波动的辨识：undulating vs 传统"伪线性"

- **proposed_capability_id**: cap.nsca.undulating-vs-traditional-identification
- **proposed_slug**: undulating-vs-traditional-identification
- **type**: framework
- **merged_candidates**: [f22-12, p22-16]
- **task_ids**: [T12]
- **importance**: medium
- **source_evidence**:
  - source_id: src-nsca-essentials-5e
    location: Chapter 22 "Undulating Versus Linear Periodization Models"（ch22.txt 第 736–791 行）
- **R 段可用原文引用**（英文，≤100 词，逐字）:
  > "the term linear periodization creates a false narrative because one of the major tenets of periodization is the removal of linearity from the training process" ; "the nonlinear periodization model ... is sometimes described as an undulating or daily undulating periodization model because it involves larger daily ... fluctuations in the load and volume."
- **V1_source_sufficiency**: passed: true — 回查确认：作者立场为"把传统模型称 linear 是误读"（第 746–773 行）；DUP 例（周二 4×6RM / 周四 3×10RM / 周六 5×3RM）与传统例（三天均 4×6，85/75/65% 1RM）均逐字在原文（第 757–768 行）；对两模型优劣"研究结论不一"（部分支持 DUP、部分无差异、部分传统更优，第 774–777 行）与双方风险论据（第 778–791 行）均完整。
  - **局限/缺口注记（已写入单元，不转 needs_review）**：原文自认"linear periodization 是 misnomer"，且**明确承认"哪种模型更优"无定论**（第 774–777 行互相矛盾的引文）。本单元只保证"**辨识口径**"可执行（识别某计划属 DUP 还是传统/伪线性）；"择优"部分原文给不出裁决，写作时须在 B 段保留该争议，禁止宣称某一模型更优。
- **V2_executability**: passed: true
  - check_mode: walkthrough
  - input: 两种周内安排描述——(甲) 周二 4×6RM、周四 3×10RM、周六 5×3RM；(乙) 三天均 4×6，负荷分别 85%/75%/65% 1RM。
  - expected: 甲 = daily undulating（周内同时波动负荷、量与焦点）；乙 = 传统模型（各日组次不变、仅变负荷；因 volume-load 在 microcycle 波动，实为**非线性**，不应称作 linear）。
  - observed: 两描述均被正确归类，并给出"传统模型≠线性"的纠偏；对"择优"明确标注原文无定论。
- **V3_task_utility**: passed: true — 消除"线性/非线性"术语误用，统一辨识口径；识别两模型的失败边界（DUP 高 volume-load 的外周疲劳风险 vs 传统累积神经疲劳）。
- **decision**: verified
- **if_not_verified**: —

---

## 能力单元 U11 — 教练与体能教练协同规划

- **proposed_capability_id**: cap.nsca.coach-sc-collaboration
- **proposed_slug**: coach-sc-collaboration
- **type**: framework
- **merged_candidates**: [f22-18]
- **task_ids**: [T12]
- **importance**: medium
- **source_evidence**:
  - source_id: src-nsca-essentials-5e
    location: Chapter 22 "Reviewing the Annual Plan Example"（ch22.txt 第 898–905 行）
- **R 段可用原文引用**（英文，≤100 词，逐字）:
  > "the sport coach and the strength and conditioning professional must plan the program together to share goals and strategies ... Without the cooperation of all involved professionals, optimal performance cannot be fully achieved."
- **V1_source_sufficiency**: passed: true — 单处完整给出该命题（第 899–905 行），证据充分。但**原文只给出"必须共同规划"这一规范性主张**，未给可执行的协同步骤、角色分工或交付物。
- **V2_executability**: passed: false — 按 f22-18 的"步骤"演练（共同规划／共享目标／整合训练因素／统一管理应激）无法产生具体、可检验的动作或交付物；它是一条实施前提，而非可独立执行的方法。缺"谁在何时产出何文档、冲突如何裁决"的可操作规则，且**不得用常识补造**。
- **V3_task_utility**: passed: true — 作为实施前提/边界，提醒"周期化效果依赖跨专业整合"（呼应全书转诊/专业边界立场）。
- **decision**: reference
- **if_not_verified**: 并入 `book/overview.md` 的"周期化实施前提/组织条件"参考区（或 glossary 条目"cross-disciplinary planning"）；不作为独立 skill。可作为 U1/U5 能力卡 B 段（组织前提）的素材。

---

## 覆盖核查表

| task_id | 任务 | 原文位置 | 对应候选 | decision | 去向 |
|---|---|---|---|---|---|
| T12 | 设计周期化计划（时期划分与变量应用） | Ch22 全文；Table 22.2（ch22.txt 360–394）、Table 22.3（502–539）、年度计划样例（792–921） | f22-01~19、p22-01~23、c22-1/2/3、ce22-01~05 | verified（U1–U6、U8、U9、U10）/ reference（U11、case/ce 支持材料） | cap.nsca.periodization-three-level-build / periodization-model-choice / periodization-cycle-durations / season-to-period-mapping / annual-plan-construction / mesocycle-variable-filling / peaking-vs-maintenance / in-season-load-management / undulating-vs-traditional-identification；U11→overview；c22-*、ce22-*→A1/B 素材 |
| T13 | 理解并应用 GAS/刺激—疲劳—恢复理论 | Ch22 "Central Concepts"（ch22.txt 83–222）；Ch24（现象展开，属 H） | f22-09/10/11、p22-05/06/07 | verified（U7） | cap.nsca.periodization-mechanistic-theories |

**交界核对**：
- **与簇 H**：簇清单中的 **f24-01~10、p24-01~21（共 31 条）** 及 counter-examples 中的 **ce24-01~10** 均属 Ch24 过度训练/恢复/监控，按约定 **属簇 H**，本簇不重复验证；本簇仅收其被周期化理论引用的机制部分（已并入 U7）。→ 见缺口清单。
- **与簇 A**：候选 **f22-17 / p22-23 / p22-22** 中的"**%RM↔重复数换算、由多次 RM 估 1RM（Table 18.8/18.9）**"确属 **簇 A 的负荷计算**；本簇只在 U6 保留"在年度计划的中周期上如何把这些变量落值"的编排流程。**若阶段 1.6 判定需独立，"负荷换算/落值"应归 A 簇 canonical。**

---

## 本簇缺口清单

1. **Ch24 内容整体移交簇 H（非本簇遗漏）**：候选清单中 f24-01~10、p24-01~21（31 条）与 ce24-01~10 覆盖过度训练/恢复/监控（T27/T28 相关），按簇交界属簇 H。本簇未验证、未淘汰，**保持活跃交 H 处理**，避免"重要内容静默消失"。
2. **跨章依赖（非缺口，但需标注）**：U6 与 U9 引用的 **Table 18.8 / 18.9 / 18.15** 数值在 Ch18（簇 A），本簇只能给出"如何调用"的流程；实际换算需 A 簇提供表值。
3. **原文内部不一致（次要）**：ch22.txt 第 798 行 preseason 记 "August 21-November 5"，第 852 行记 "11 weeks (August 21-October 5)"。以后者与 in-season 起始（11/6）冲突，判为原文/提取笔误。已在 U5 注明，采用 11/5；不影响可执行性，但**未回书核对纸质版权页/图 22.8 原图**，如需零误差应补读原图。
4. **模型择优无定论（重要，已写入单元局限）**：原文自认 "linear periodization" 为 misnomer，且 DUP 与传统模型**优秀性研究结论互相矛盾**。本簇已在 U10 明确保留该争议于 B 段，**禁止在阶段 2 宣称任一模型更优**。此为"来源即冲突"，故不转 needs_review（辨识口径可执行），但须在最终能力卡 B 段显式标注。
5. **ce22-04 无预防措施**：反例"每日波动模型过度负荷/损伤风险"原文**未给预防做法**（仅陈述对立观点）。作 B 段失败边界素材时，不得补造预防规则。

---

## 供阶段 2 的提示（可选）

- **适合合并成一张能力卡**：U5（年度计划编排）可作主卡，U3（层级时长）+ U4（季节映射）+ U6（中周期填充）+ U8（峰值/维持）+ U9（赛内编排）为其"变量应用/比赛期"子流程；U1（三级流程）+ U2（模型选择）为其"计划建立"前置段。U7（机制理论）建议独立成短卡（T13，理论依据）。U10（波动辨识）可作 U2/U6 的 B 段或独立小卡。
- **A1 素材**：
  - **c22-1（女性篮球运动员年度计划样例，Figure 22.8）——本簇唯一完整年度计划样例，极重要 A1**，优先用于 U5。
  - **c22-2（锦标赛周 Options A/B/C）** → U9 的 A1。
  - **c22-3（Table 22.3 处方表）** → U6 的 A1（与 p22-04 同源）。
  - **Table 22.2** → U3 的数值/口径 A1。
- **B 段（失败边界）素材**：ce22-01（峰值期 >1–2 周）、ce22-02（第二过渡期 >4 周）、ce22-03（减量过度）、ce22-04（DUP 过度负荷，原文无预防）、ce22-05（单调/过度变化→衰竭期）。
- **争议须写入 B**：U10 的"linear 是 misnomer"与"DUP vs 传统无定论"；U6 的"Table 22.3 与正文框 strength/power 区间表述差异（按动作类型分列 vs 总括）"。
- **reference 去向**：U11 → overview/glossary 参考区。


---

<!-- ===== 簇 C-testing ===== -->

# 簇 C-testing — 三重验证结果

- 负责任务: T20, T21, T22, T23, T40
- 候选输入: 158 条（来自 `frameworks-g1-ch13-14.md`、`principles-g1-ch13-14.md`、`cases-g1-ch01-14.md`（c13-*/c14-*）、`counter-examples-g1-ch01-14.md`（ce13-*/ce14-*））
- 归并后能力单元: 26 个（+1 条出簇候选 c14-14 另处理）
- verified: 26 / reference: 0 / needs_review: 0 / rejected: 0（另 1 条出簇 → reference）
- 回查原文: `.cangjie/source/ch13.txt`（1048 行）、`ch14.txt`（3487 行）

> **口径冲突已裁断**：`p14-02`（相对力量标准化）原文用 `lb × 4.44 或 kg × 9.81`（ch14.txt:65-66），`p14-09`（Margaria-Kalamen 功率）原文用 `lb × 4.45 或 kg × 9.807`（ch14.txt:833）。两处为**同一物理常数（重力加速度）的不同印刷取值**，非实质规则冲突。本簇统一采用 **SI 标准 g = 9.80665 m/s² → kg × 9.81、lb × 4.448**，差异 <0.2%（对功率结果影响 <0.5 W 量级）。已在 U10 与 U20 的 V1 中登记该冲突与采用口径。

---

## 能力单元 U1 — 有效测试的证据本位选择框架（效度/信度/客观性门槛）

- **proposed_capability_id**: cap.nsca.test-selection-validity
- **proposed_slug**: test-selection-validity
- **type**: framework
- **merged_candidates**: [f13-01, f13-03, f13-14, p13-01, p13-02, p13-03, p13-04, p13-05, p13-06, ce13-01]
- **task_ids**: [T20]
- **importance**: critical
- **source_evidence**:
  - source_id: src-nsca-essentials-5e
    location: Chapter 13 "Principles of Test Selection and Administration"（ch13.txt:166-167；283-286；354-357）
- **R 段可用原文引用**（英文，≤100 词，逐字）:
  > "Test results are valuable only when two key criteria are met: validity and reliability." … "A test must be reliable to be valid, because highly variable results have little meaning. However, even a reliable test may not be valid, because the test may not measure what it is supposed to measure." (ch13.txt:166, 283-285)
- **V1_source_sufficiency**: passed: true — 原文单处即完整给出效度/信度两支柱、二者的必要非充分关系、效度的 construct/face/content/criterion（concurrent、predictive）分层、convergent/discriminant 子类、内容效度的比例加权规则、择优规则；p13-02 的"九项条件"与 p13-06 的例证可直接勾选。**未解决处**：f13-01 依赖的 Figure 13.1 中间步骤在正文未展开；p13-07 的 ICC/TE 只定性、无公式——如实记入，不补造。
- **V2_executability**: passed: true
  - check_mode: walkthrough
  - input: 候选测试 = "六边形跳（25 m 单腿跳）"用于**新手长跑运动员**；另一候选 = "60 m 冲刺"用来代表有氧能力。
  - expected: 六边形跳对新手无效（技巧主导，p13-13）；60 m 冲刺可靠但不测有氧（信度≠效度，p13-06）→ 两者均判"不采用"。
  - observed: 按 U1 判据逐条勾选——两项均落在"效度不成立/适用边界外"，输出"拒绝采用，改选 1.5-mile 跑测有氧、选择与新手技巧匹配的爆发力测试"。结论明确。
- **V3_task_utility**: passed: true — expected_benefit: 把"测试流行度"换成"效度/信度双门槛"，防止用高变异或错测构念的测试做决策；为后续所有测试选择提供统一准入口径。
- **decision**: verified
- **if_not_verified**: —

## 能力单元 U2 — 专项特异性与测试电池构建（含年龄/性别/训练状态适用边界）

- **proposed_capability_id**: cap.nsca.sport-specific-test-battery
- **proposed_slug**: sport-specific-test-battery
- **type**: framework
- **merged_candidates**: [f13-02, p13-09, p13-10, p13-11, p13-12, p13-13, p13-14, c13-02, ce13-04]
- **task_ids**: [T20, T40]
- **importance**: critical
- **source_evidence**:
  - source_id: src-nsca-essentials-5e
    location: Chapter 13（ch13.txt:642-647 年龄/性别；selection & classification 段）
- **R 段可用原文引用**（英文，≤100 词，逐字）:
  > "The 1.5-mile (2.4 km) run may be a valid and reliable field test of aerobic power for college-aged men and women but may not be appropriate for preadolescents because of their probable lack of experience and interest in sustained running." (ch13.txt:642-645)
- **V1_source_sufficiency**: passed: true — 原文给出"专项特异性（能量系统+力学模式）+ 运动员经验/训练状态/年龄/性别/环境"的筛选维度，四维动作分类（动作模式/肌群/供能系统/技能复杂度），年龄性别适用例（1.5-mile 对青春期前不适用；引体向上对女性效度不足），以及足球内容效度例（冲刺/敏捷/有氧/踢球力量）。**未解决处**：四维权重与配比未给（记入 gap）。
- **V2_executability**: passed: true
  - check_mode: walkthrough
  - input: 目标 = 高中女子足球队；需求 = 冲刺、敏捷、有氧耐力、踢球功率；可测者 = 15 岁新手。
  - expected: 输出覆盖四类能力成分的电池；因是新手，剔除高技巧测试（如单腿跳类），1.5-mile 跑可保留但需核实长跑经验；踢球功率须专项化。
  - observed: 得到电池 `[10–40 yd 冲刺, T-test/5-10-5, 1.5-mile 跑（核实经验后）, 专项踢球功率]`，并把"新手技巧负担"作为排除项，结论明确。
- **V3_task_utility**: passed: true — expected_benefit: 防止电池出现动作模式/供能系统覆盖盲区；把年龄/性别/训练状态作为测试适用性判据（直接覆盖 T40 的年龄性别部分）。
- **decision**: verified
- **if_not_verified**: —

## 能力单元 U3 — 测试顺序编排与休息安排

- **proposed_capability_id**: cap.nsca.test-sequencing-rest
- **proposed_slug**: test-sequencing-rest
- **type**: procedure
- **merged_candidates**: [f13-05, p13-22, p13-23, f13-06, p13-21, p13-26, ce13-06]
- **task_ids**: [T21]
- **importance**: high
- **source_evidence**:
  - source_id: src-nsca-essentials-5e
    location: Chapter 13 "Sequence of Tests"（ch13.txt:872-883,battery rest）
- **R 段可用原文引用**（英文，≤100 词，逐字）:
  > "a test that maximally taxes the phosphagen energy system requires 3 to 5 minutes of rest for complete recovery, whereas a maximal test of the anaerobic glycolytic energy system requires at least 1 hour for complete recovery." … "1. Nonfatiguing tests … 2. Agility tests … 3. Maximum power and strength tests … 4. Sprint tests … 5. Local muscular endurance tests … 6. Fatiguing anaerobic capacity tests … 7. Aerobic capacity tests" (ch13.txt:872-883)
- **V1_source_sufficiency**: passed: true — 顺序七段、试次间休息（非极限 ≥2 min、接近最大 ≥3 min）、电池内测试间 ≥5 min、供能系统恢复（磷酸原 3–5 min、糖酵解 ≥1 h）、并行测站与"一人同时一项、最多连续两项非疲劳测试"完整。ce13-06 提供失败反例。**未解决处**："非疲劳性测试"界定仅举例（记入 gap）。
- **V2_executability**: passed: true
  - check_mode: walkthrough
  - input: 一天内需测：身高体重、T-test、1RM 深蹲、40 yd 冲刺、俯卧撑、300-yd 折返、1.5-mile 跑。
  - expected: 排为 非疲劳(身高/体重)→敏捷(T-test)→最大力量(1RM 深蹲)→冲刺(40 yd)→局部肌耐力(俯卧撑)→无氧耐力(300-yd)→有氧(1.5-mile)；300-yd 与 1.5-mile 建议另日，同日则置最后；测试间 ≥5 min。
  - observed: 输出一条明确的单日排序串，无先后冲突；跨日拆分规则给出。
- **V3_task_utility**: passed: true — expected_benefit: 消除"前测疲劳污染后测"的偏差来源（ce13-06），稳定测试日交付顺序。
- **decision**: verified
- **if_not_verified**: —

## 能力单元 U4 — 测试员选拔、培训与施测分工

- **proposed_capability_id**: cap.nsca.tester-selection-duties
- **proposed_slug**: tester-selection-duties
- **type**: procedure
- **merged_candidates**: [f13-07, f13-08, p13-18, p13-20]
- **task_ids**: [T21]
- **importance**: high
- **source_evidence**:
  - source_id: src-nsca-essentials-5e
    location: Chapter 13 "Selection and Training of Testers" / "Test Format"（ch13.txt:827-831）
- **R 段可用原文引用**（英文，≤100 词，逐字）:
  > "It is preferable to have the same person administer a given test if time and schedules permit, because this eliminates the issue of interrater reliability. … As a rule, each tester should administer only one test at a time" (ch13.txt:827-831)
- **V1_source_sufficiency**: passed: true — 规则完整：新手须正确执行与计分、须与资深者成绩高度相关、讲评须一致；同一测试同一人施测、简单计数测试可分包、需判断的测试交最熟练者、一人同时一项、可在准备间隙轮转。**未解决处**："高度相关"阈值未量化（记入 gap）。
- **V2_executability**: passed: true
  - check_mode: walkthrough
  - input: 30 人测试日、4 名测试员、5 项测试（身高体重计数类 + 深蹲动作判定 + 冲刺计时 + 俯卧撑 + 纵跳）。
  - expected: 深蹲判定与冲刺计时指派最熟练者；身材/计数类可分派新手；每人同一时段只负责一站；配备材料清单与书面协议；新手先做一致性校验。
  - observed: 产出可执行的分工表（谁测哪项、谁需先校验），边界清晰。
- **V3_task_utility**: passed: true — expected_benefit: 消除 interrater/新手误差，统一讲解口径，减少多人测试日的人员混乱。
- **decision**: verified
- **if_not_verified**: —

## 能力单元 U5 — 运动员测试准备、记录与测试日标准化

- **proposed_capability_id**: cap.nsca.test-prep-standardization
- **proposed_slug**: test-prep-standardization
- **type**: checklist
- **merged_candidates**: [f13-09, p13-25, p13-19, p13-24]
- **task_ids**: [T21]
- **importance**: medium
- **source_evidence**:
  - source_id: src-nsca-essentials-5e
    location: Chapter 13 "Preparing Athletes for Testing" / records / standardization（ch13.txt:900-904）
- **R 段可用原文引用**（英文，≤100 词，逐字）:
  > "It is important that test sessions be conducted at the same time of day to avoid fluctuations in physiological responses due to differences in circadian rhythm … It is also recommended that tests be conducted indoors, which will allow for climate and testing surfaces to remain more consistent." (ch13.txt:900-904)
- **V1_source_sufficiency**: passed: true — 清单完整：提前公布日期/时间/目的；测前 1–3 天熟悉课（或融入动态热身）；讲解覆盖目的/执行/热身量/练习次数/试次数/评分/无效准则/表现建议；演示+提问+同等激励+即时反馈；一般+专项热身+2–3 次热身试次；测后监督整理；计分表须预留全部结果+备注+环境+设备设置（如深蹲插销高度）；固定时段、尽量室内。
- **V2_executability**: passed: true
  - check_mode: walkthrough
  - input: 首次测试的 12 名高中运动员，明早 8:00 测试 1RM 深蹲。
  - expected: 输出：提前通知（目的/时间/着装）、T-3 天熟悉课、热身试次、讲解脚本清单、记录表字段（含插销高度/环境温湿度）、测后整理、要求改日重测。
  - observed: 生成可打印的准备清单与记录表字段集，动作明确。
- **V3_task_utility**: passed: true — expected_benefit: 减少遗漏（漏记环境/设备设置导致跨测次不可比），稳定交付格式。
- **decision**: verified
- **if_not_verified**: —

## 能力单元 U6 — 测试信度受损来源排查（前后测一致性）

- **proposed_capability_id**: cap.nsca.reliability-variability-troubleshoot
- **proposed_slug**: reliability-variability-troubleshoot
- **type**: troubleshooting
- **merged_candidates**: [f13-13, p13-08, p13-07, ce13-02, ce13-03, c13-01]
- **task_ids**: [T20, T21]
- **importance**: high
- **source_evidence**:
  - source_id: src-nsca-essentials-5e
    location: Chapter 13 reliability 段（ch13.txt:283-285；inter/intrarater 段）
- **R 段可用原文引用**（英文，≤100 词，逐字）:
  > "The difference between two sets of scores can arise from a number of different factors: Intrasubject (within subjects) variability; Lack of interrater (between raters) reliability or agreement; Intrarater (within raters) variability; Failure of the test itself to provide consistent results." (ch13.txt, f13-13 引)
- **V1_source_sufficiency**: passed: true — 四个来源逐一给出；对策（明确评分系统+受训评分者、前后测同一评分者、标准化校准/准备/施测/评分、增加练习）完整；ce13-02/03 与 c13-01（前松后紧把进步测成退步）提供失败模式。**未解决处**：p13-07 的 ICC/TE 仅有定性口径（原文未给解析式与可接受阈值）——已如实登记，不补造公式。
- **V2_executability**: passed: true
  - check_mode: walkthrough
  - input: 同一运动员深蹲 1RM 前测 120 kg、后测 115 kg，但教练确信力量增长。
  - expected: 依四来源排查 → 命中"intrarater（后测更严）/ interrater（换人施测）"；修正为固定同一评分者+明确下蹲深度判据；结论：本次前后测不可直接比较。
  - observed: 归因明确并给出纠正动作，输出不是"力量退步"的错误结论。
- **V3_task_utility**: passed: true — expected_benefit: 识别失败边界，防止把测量误差误读为训练效果。
- **decision**: verified
- **if_not_verified**: —

## 能力单元 U7 — 环境因素对测试的调整（温度/湿度/海拔）

- **proposed_capability_id**: cap.nsca.test-environment-adjustment
- **proposed_slug**: test-environment-adjustment
- **type**: framework
- **merged_candidates**: [f13-04, p13-15, f13-11, p13-16, ce13-05]
- **task_ids**: [T40, T21]
- **importance**: medium
- **source_evidence**:
  - source_id: src-nsca-essentials-5e
    location: Chapter 13 environment / altitude / testing-in-the-heat（ch13.txt:674-678；751-761）
- **R 段可用原文引用**（英文，≤100 词，逐字）:
  > "Norms on aerobic endurance tests should be adjusted when testing at altitudes exceeding 1,900 feet (579 m). Up to about 9,000 feet (2,743 m), maximal oxygen uptake declines by approximately 5% for each 3,000 feet (914 m) of elevation." … "Avoid testing under extreme combinations of heat and humidity." (ch13.txt:674-678, 751)
- **V1_source_sufficiency**: passed: true — 海拔修正口径（>579 m 调常模；≤2743 m 每 914 m 降约 5%；高海拔后至少 10 天适应；不影响力量/功率测试）与高温清单（避免极端热湿、留 ≥3 °C 安全裕度、热习服 ≥1 周、测前 24 h 补水、>1 h 补电解质、警惕热病、备医疗覆盖）完整；ce13-05 为失败反例。**未解决处**：温湿上限图（Figure 13.2）数值未在正文重现——记入 gap，不补数。
- **V2_executability**: passed: true
  - check_mode: walkthrough
  - input: 在丹佛（海拔 1,609 m）为大学足球员测 1.5-mile 跑以对照海平面常模。
  - expected: 判为 579 m 以上 → 常模须按 (1609−?) 的海拔修正（每 914 m 约 −5% VO2max）；若该队员 3 天前才从海平面抵达，须推迟至适应 ≥10 天后再测；高温日须留温度裕度或改室内/清晨。
  - observed: 输出"暂缓并修正"的明确决策与所需等待天数，边界清楚。
- **V3_task_utility**: passed: true — expected_benefit: 避免跨海拔/跨季节直接比较成绩，统一常模调整口径（直接覆盖 T40 的环境部分）。
- **decision**: verified
- **if_not_verified**: —

## 能力单元 U8 — 测试安全红线：健康风险识别与转诊（含低钠血症）★

- **proposed_capability_id**: cap.nsca.test-health-safety-referral
- **proposed_slug**: test-health-safety-referral
- **type**: troubleshooting
- **merged_candidates**: [f13-10, f13-12, p13-17, ce13-07]
- **task_ids**: [T21]
- **importance**: critical
- **source_evidence**:
  - source_id: src-nsca-essentials-5e
    location: Chapter 13 "Health and Safety"（ch13.txt:723-727；781-789）
- **R 段可用原文引用**（英文，≤100 词，逐字）:
  > "Medical referral may be warranted for an athlete who persistently has any of the following symptoms: chest pressure, pain, or discomfort; listlessness; light-headedness; dizziness; confusion; headache…" … "A victim of hyponatremia should never be given fluid and should be treated by a physician." (ch13.txt:723-727, 786-787)
- **V1_source_sufficiency**: passed: true — 转诊红旗清单（胸部压迫/疼痛/不适、乏力、头昏、眩晕、意识模糊、头痛、皮肤深红或湿冷、脉搏不规则、骨/关节痛、视物模糊、恶心、与负荷不相称或休息不缓解的气短/脉快/无力）完整；判据（持续存在→转诊；单次但严重如丧失意识→立即就医；症状可迟发）；低钠血症鉴别（极稀释尿+皮肤胀+意识改变、**体温不升高**）+ 处置（**绝不补液 + 交医师**，与热病相反）；ce13-07 为"漏判红旗"失败模式。这是本簇最重要的安全红线。
- **V2_executability**: passed: true
  - check_mode: walkthrough
  - input: 运动员跑完 1.5-mile 后出现意识模糊 + 皮肤膨胀 + 极度清亮尿，腋温 36.8 °C。
  - expected: 判为低钠血症/水中毒（体温未升，区别于热射病）→ **禁止补液**、立即转医师；同时对照红旗清单（意识模糊）触发就医。
  - observed: 输出明确的"不补液+立即医疗"处置，写出与热病的关键鉴别点（体温）。
- **V3_task_utility**: passed: true — expected_benefit: 关键安全动作与专业边界（转诊而非自行处理），防止可致死的处置错误（补液加重低钠血症、隐藏心脏问题致猝死）。
- **decision**: verified
- **if_not_verified**: —

## 能力单元 U9 — 测试监控体系三层设计与运动科技引入决策

- **proposed_capability_id**: cap.nsca.monitoring-protocol-design
- **proposed_slug**: monitoring-protocol-design
- **type**: framework
- **merged_candidates**: [f14-01, f14-02, p14-58]
- **task_ids**: [T21]
- **importance**: medium
- **source_evidence**:
  - source_id: src-nsca-essentials-5e
    location: Chapter 14 "Administration…" protocols/procedures/equipment 段
- **R 段可用原文引用**（英文，≤100 词，逐字）:
  > "A decision-making framework for implementing technology in sport suggests four reflective questions: 1. Would the information provided be helpful? 2. Can you trust the information provided? 3. Can you integrate, manage, and analyze the data provided effectively? 4. Can you implement the technology in your practice?" (ch14.txt, f14-01 引)
- **V1_source_sufficiency**: passed: true — protocol（总体策略：测试类型与频率）→ procedure（逐步细则）→ equipment（器材选型需过效度/信度、实用/易用、相关性）的嵌套结构与四问清单完整；另附设备须核效度信度、定期复核电池。**未解决处**：四问无量化判据（定性）——仍可作筛选闸。
- **V2_executability**: passed: true
  - check_mode: walkthrough
  - input: 拟引入某手机 App 测量纵跳（用高速摄像估算腾空时间）。
  - expected: 四问逐一判定——信息有用（是）→ 可信（需核效度/信度）→ 能否整合（需能导出数据）→ 能否落地（队内能否人人用）→ 输出"先做与力台/接触垫的一致性验证再采用"。
  - observed: 产出可执行的引入闸门结论与所需验证动作。
- **V3_task_utility**: passed: true — expected_benefit: 防止盲目引入工具，把"上定框架、中定步骤、下选器材"的层级固定为稳定交付。
- **decision**: verified
- **if_not_verified**: —

## 能力单元 U10 — 最大力量测试协议族（1RM / IMTP / 北欧腘绳肌）

- **proposed_capability_id**: cap.nsca.max-strength-test-protocols
- **proposed_slug**: max-strength-test-protocols
- **type**: procedure
- **merged_candidates**: [f14-03, f14-04, f14-05, f14-26, p14-01, p14-02, p14-03, p14-04, p14-05, p14-59, ce14-01, ce14-07]
- **task_ids**: [T20, T22]
- **importance**: high
- **source_evidence**:
  - source_id: src-nsca-essentials-5e
    location: Chapter 14 1RM/IMTP 段（ch14.txt:63-66 相对力量；546-551 IMTP 剔除）
- **R 段可用原文引用**（英文，≤100 词，逐字）:
  > "To express the same from an isometric test, maximal force exerted in newtons is divided by bodyweight converted into newtons (lb × 4.44, or kg × 9.81)." … "A quiet standing period of 1 s with >50 N change in force; Pre-tension (<50 N) while maintaining a rigid torso before initiating force application; A countermovement prior to the onset of force application; Peak force at the end of the pull" (ch14.txt:64-66, 546-549)
- **V1_source_sufficiency**: passed: true — 1RM 进阶（首试 ≈50% 估计 1RM、1–5 min 休息、热身后 3–5 次内定位到真值数个百分点内、≥2 组重热身）；IMTP 设置（second pull 位、3–5 s 峰值力/≤1 s RFD、≥3 次、峰值力波动 >15% 加测、四条剔除信号）；IMTP 指标（峰值力/时点力/RFD 20 ms 窗/冲量）；北欧腘绳肌摆位与 break point angle；相对力量与幂函数标度；直接测 1RM 规则。**冲突已裁断**：`lb×4.44/kg×9.81`（此处）vs `lb×4.45/kg×9.807`（U20），统一取 kg×9.81、lb×4.448。**未解决处**：递增幅度"somewhat"无精确表、allometric 幂指数未给、北欧组间休息未给（记入 gap）。
- **V2_executability**: passed: true
  - check_mode: walkthrough
  - input: 估计 1RM 卧推 80 kg 的运动员；IMTP 3 次峰值力 2000/2100/2350 N；体重 80 kg。
  - expected: 首试 40 kg → 逐次加重，热身后 3–5 次内定位 ±几个百分点内；IMTP 三次极差 (2350−2000)/2350 ≈ 14.9% <15% 判定合格，输出峰值力 2350 N、相对力 2350/(80×9.81)=2.99 N/kg；相对力量 = 1RM/体重。
  - observed: 1RM 路径与 IMTP 校验均给出明确数值/判定；15% 阈值判定与相对力换算正确（2350/784.8=2.994 N/kg）。
- **V3_task_utility**: passed: true — expected_benefit: 统一最大力量测试口径与相对力标准化，剔除无效 IMTP 试次，避免用曲线估算 1RM（ce14-01）。
- **decision**: verified
- **if_not_verified**: —

## 能力单元 U11 — 负荷-速度剖面（VBT）建立与 1RM 预测禁用

- **proposed_capability_id**: cap.nsca.load-velocity-profile
- **proposed_slug**: load-velocity-profile
- **type**: procedure
- **merged_candidates**: [f14-06, p14-06]
- **task_ids**: [T20]
- **importance**: medium
- **source_evidence**:
  - source_id: src-nsca-essentials-5e
    location: Chapter 14 VBT / load-velocity 段
- **R 段可用原文引用**（英文，≤100 词，逐字）:
  > "when the 1RM back squat is estimated from the load–velocity profile, it is highly variable and consistently results in an overestimation of the athlete's 1RM and should not be used for 1RM prediction … the 1RM should be directly tested." (ch14.txt, f14-06 引)
- **V1_source_sufficiency**: passed: true — 构建口径（20/40/60/80/90% 1RM 递增做组、记录杠速、拟合 L-V 线性关系）+ 硬性禁用规则（不得由剖面估算 1RM，会系统性高估并误导负荷）完整。**未解决处**：每组次数/休息/拟合方法未给（记入 gap）。
- **V2_executability**: passed: true
  - check_mode: walkthrough
  - input: 某运动员在 back squat 上取 5 个负荷点的平均杠速。
  - expected: 拟合出 L-V 关系用于评价/处方强度；**明确拒绝**用它反推 1RM，改直接测 1RM。
  - observed: 输出个体化剖面 + "不得估 1RM"的边界，动作明确。
- **V3_task_utility**: passed: true — expected_benefit: 给 VBT 划定使用边界，防止负荷误编程（ce14-01）。
- **decision**: verified
- **if_not_verified**: —

## 能力单元 U12 — 跳跃与下肢爆发力测试协议族

- **proposed_capability_id**: cap.nsca.jump-power-test-protocols
- **proposed_slug**: jump-power-test-protocols
- **type**: procedure
- **merged_candidates**: [f14-07, p14-12, p14-13, p14-53, ce14-03]
- **task_ids**: [T20, T22]
- **importance**: high
- **source_evidence**:
  - source_id: src-nsca-essentials-5e
    location: Chapter 14 jump / drop jump 段
- **R 段可用原文引用**（英文，≤100 词，逐字）:
  > "jump height values from jump-and-reach tests should not be compared directly to, or used interchangeably with, jump height values recorded with such technologies." (ch14.txt, p14-12 引)
- **V1_source_sufficiency**: passed: true — 纵跳三种测法（力台/墙+粉笔/Vertec）、取三次最佳 0.5 in/1 cm；蹲跳（膝角约 110°、保持 2–3 s、手固定于髋）与 EUR；落地跳（8/12/16 in 箱、指标=跳高/触地时间/RSI）；立定跳远计分（双脚落地、三次取最佳 0.5 in/1 cm）；可比性约束（jump-and-reach 与力台不可互换）。ce14-03 为失败反例。**未解决处**：三种测法换算关系未给（记入 gap）。
- **V2_executability**: passed: true
  - check_mode: walkthrough
  - input: 运动员 A 墙式摸高 55 cm、运动员 B 力台纵跳 45 cm。
  - expected: 判为**不可直接比较**（不同测量参考点/肩活动度）；须同法重测或只与同法基线比较；立定跳远用后脚跟最后缘标记、双脚落地才算。
  - observed: 输出"不比较、需同法测"的明确结论与正确立定跳远计分口径。
- **V3_task_utility**: passed: true — expected_benefit: 防止跨设备/跨技术误比跳高，统一跳跃测试计分精度。
- **decision**: verified
- **if_not_verified**: —

## 能力单元 U13 — 速度与变向/敏捷测试协议族

- **proposed_capability_id**: cap.nsca.speed-agility-test-protocols
- **proposed_slug**: speed-agility-test-protocols
- **type**: procedure
- **merged_candidates**: [f14-08, f14-09, p14-25, p14-26, p14-57, ce14-02]
- **task_ids**: [T20, T22]
- **importance**: high
- **source_evidence**:
  - source_id: src-nsca-essentials-5e
    location: Chapter 14 speed / agility 段（ch14.txt:196）
- **R 段可用原文引用**（英文，≤100 词，逐字）:
  > "stopwatch-measured sprint times are up to 0.24 seconds faster than electronically measured times because of the tester's reaction-time delay in pressing the stopwatch button at the gun and the tendency to anticipate and press the button early as the athlete approaches the finish line." (ch14.txt:196-199)
- **V1_source_sufficiency**: passed: true — 计时误差（手计时最多快 0.24 s、优先电子计时、分段 10/20/40 yd）；冲刺口径（短距测加速、40 yd 测最大速度、≤100 m、取最佳 0.1 s、试次间 ≥2 min）；变向族（T-test 判罚=未触锥/交叉步/未面向前；5-10-5 取 0.01 s；5-0-5 折返线；Hexagon 18 跳取三次最佳；Illinois 计总时）。ce14-02 为失败反例。**未解决处**：试次间休息在不同测试间表述不一致（记入 gap）。
- **V2_executability**: passed: true
  - check_mode: walkthrough
  - input: 40 yd 冲刺手计时 4.60 s；电子计时同次 4.75 s；T-test 时运动员以交叉步完成。
  - expected: 手/电差值 0.15 s（在 0–0.24 s 合理区间，提示系统偏快）→ 记录以电子为准并注明；T-test 交叉步 → 该试次无效（判罚）。
  - observed: 输出计时口径判定与无效试次判定，明确。
- **V3_task_utility**: passed: true — expected_benefit: 统一计时与判罚口径，减少手计时系统误差与无效试次漏判。
- **decision**: verified
- **if_not_verified**: —

## 能力单元 U14 — 无氧能力测试协议族（Wingate / 300-yd shuttle / 90-s box jump / Margaria 冲刺）

- **proposed_capability_id**: cap.nsca.anaerobic-capacity-test-protocols
- **proposed_slug**: anaerobic-capacity-test-protocols
- **type**: procedure
- **merged_candidates**: [f14-10, f14-25, p14-07, p14-08, p14-19, p14-20, p14-60]
- **task_ids**: [T20, T22]
- **importance**: medium
- **source_evidence**:
  - source_id: src-nsca-essentials-5e
    location: Chapter 14 anaerobic capacity 段
- **R 段可用原文引用**（英文，≤100 词，逐字）:
  > "It is typically quantified as the maximal power output during muscular activity between 30 and 90 seconds." … "Six such round trips are made as fast as possible without stopping (6 × 50 yd = 300 yd [274 m])" (ch14.txt, p14-08/p14-19 引)
- **V1_source_sufficiency**: passed: true — 无氧能力时长口径（30–90 s）、供能口径（爆发≈1 s/低速最大力量 2–5 s 均以磷酸原+ATP 为主）；Wingate（30 s、90–110 rpm 加载、阻力≈体重 7.5%、每 5 s 区间功率、疲劳指数）；300-yd（两两配对、6×50 yd、5 min 休息、两次取平均 0.1 s）；90 s 箱跳（18×30 in、双脚离地双脚触箱顶计 1、禁踩箱）；Margaria 施测（≥9 级、>6 m 助跑、三级一跨、0.01 s、重复 2 次间隔 2–3 min）。**未解决处**：Wingate"功=阻力×转数"单位换算未细化（记入 gap）。
- **V2_executability**: passed: true
  - check_mode: walkthrough
  - input: 运动员 300-yd 两轮成绩 55.0 s 与 56.4 s；90 s 箱跳触顶 78 次但踩箱 2 次。
  - expected: 300-yd = (55.0+56.4)/2 = 55.7 s（0.1 s）；箱跳合规 = 78−2 = 76 次（踩箱不计）。
  - observed: 平均成绩 55.7 s、合规次数 76 次，数值明确。
- **V3_task_utility**: passed: true — expected_benefit: 统一无氧能力族计分口径（平均/合规计数），对齐时长与供能口径。
- **decision**: verified
- **if_not_verified**: —

## 能力单元 U15 — 局部肌肉耐力测试协议族

- **proposed_capability_id**: cap.nsca.local-muscular-endurance-protocols
- **proposed_slug**: local-muscular-endurance-protocols
- **type**: procedure
- **merged_candidates**: [f14-11, p14-21, p14-22, p14-23, p14-24]
- **task_ids**: [T20, T22]
- **importance**: medium
- **source_evidence**:
  - source_id: src-nsca-essentials-5e
    location: Chapter 14 local muscular endurance 段
- **R 段可用原文引用**（英文，≤100 词，逐字）:
  > "Set the resistance at 80 pounds (36 kg) for males and 35 pounds (16 kg) for females. Set the metronome cadence at 60 beats/min to establish a rate of 30 repetitions per minute (one beat up, one beat down)." (ch14.txt, p14-24 引)
- **V1_source_sufficiency**: passed: true — partial curl-up（膝 90°、40 拍/分=20 次/分、胶带距按年龄 <45 岁 12 cm/≥45 岁 8 cm、上限 75 次）；push-up（标准胸触拳/改良膝着地，未达底面不计）；AFT HRP（2 min、前支撑位可休息、静止 >5 s 或抬脚/膝触地终止）；YMCA 卧推（男 80 lb/女 35 lb、60 拍/分=30 次/分）。**未解决处**：各测试试次数与休息未统一（记入 gap）。
- **V2_executability**: passed: true
  - check_mode: walkthrough
  - input: 50 岁女性做 partial curl-up（节拍器 40 拍/分）与 YMCA 卧推。
  - expected: curl-up 胶带间距取 8 cm（≥45 岁）；YMCA 负荷取 35 lb、速率 30 次/分；未达底面/跟不动节拍不计。
  - observed: 输出正确的年龄分段胶带距与性别负荷，判定口径明确。
- **V3_task_utility**: passed: true — expected_benefit: 统一节拍/负荷/年龄分段口径，避免"未达位仍计次"的计分虚高。
- **decision**: verified
- **if_not_verified**: —

## 能力单元 U16 — 有氧能力测试协议族（1.5-mile run / 12-min run / Yo-Yo IRT / MAS / 30-15 IFT）★

- **proposed_capability_id**: cap.nsca.aerobic-capacity-test-protocols
- **proposed_slug**: aerobic-capacity-test-protocols
- **type**: procedure
- **merged_candidates**: [f14-12, p14-14, p14-16, p14-17, p14-18]
- **task_ids**: [T20, T22]
- **importance**: high
- **source_evidence**:
  - source_id: src-nsca-essentials-5e
    location: Chapter 14 aerobic capacity 段（ch14.txt:1045-1048）
- **R 段可用原文引用**（英文，≤100 词，逐字）:
  > "For each 1.5-mile (2.4 km) run time, the tables show an estimated maximal rate of oxygen consumption; the norms for athletes in various sports are shown in table 14.26." (ch14.txt:1046-1048)
- **V1_source_sufficiency**: passed: true — 1.5-mile/12-min run（计时/距离=圈数×400 m）；Yo-Yo IRT（2×20 m、10 s 恢复、IRT1 起速 10 km/h、推荐 IRT1、两次未达线终止）；MAS（25 m 锥距、8–12 起速一般 10、每 2 min +1 km/h、保持 ≥2 min 的速度即 MAS、两次未达终止、半程 +0.5）；30-15 IFT（8 km/h 起、每级 +0.5、30 s 跑+15 s 走、连续三次未达终止、每变向修正 0.7 s）。**关键缺口（已回原文确认）**：**1.5-mile 跑推算 VO2max 无回归公式，原文只提供查表（表 14.22–14.25/14.26）**——故本单元明确写入"只能查表、不可自行拟合"。**未解决处**：30-15 IFT 的"0.7 s/变向"如何折算距离未给完整式（记入 gap）。
- **V2_executability**: passed: true
  - check_mode: walkthrough
  - input: 12-min run 完成 5.25 圈；1.5-mile 跑 10:30。
  - expected: 12-min 距离 = 5.25 × 400 = 2,100 m；1.5-mile 的 VO2max **须查表 14.22–14.25（按年龄/性别）**，不得用自拟公式；Yo-Yo/MAS/30-15 按终止规则记录最后级别/速度。
  - observed: 距离 2,100 m 数值明确；1.5-mile 明确输出"查表得估计 VO2max"，并标注不可拟合的边界。
- **V3_task_utility**: passed: true — expected_benefit: 统一有氧测试施测与终止口径，并把"1.5-mile 只能查表"的缺口固化为强制约束，避免阶段 2 误造回归式。
- **decision**: verified
- **if_not_verified**: —

## 能力单元 U17 — 动作筛查与柔韧性测试（AMSC/FMS/TJA + 坐位体前屈/过顶深蹲）

- **proposed_capability_id**: cap.nsca.movement-screen-flexibility
- **proposed_slug**: movement-screen-flexibility
- **type**: procedure
- **merged_candidates**: [f14-13, f14-19, p14-29, p14-30, p14-54, p14-56, ce14-04, ce14-06]
- **task_ids**: [T20]
- **importance**: medium
- **source_evidence**:
  - source_id: src-nsca-essentials-5e
    location: Chapter 14 movement screen / flexibility 段
- **R 段可用原文引用**（英文，≤100 词，逐字）:
  > "Ballistic stretching, characterized by bouncing to increase range of motion, cannot be allowed during any flexibility testing." … "The assessment is qualitative … with the movement scored as pass/fail." (ch14.txt, p14-54/p14-30 引)
- **V1_source_sufficiency**: passed: true — 筛查实施要点（先立评分者信度、录像回看、逐次评估 vs 取最佳、全身 vs 分段、FMS/RTSB 取最佳 vs TJA 求和）；坐位体前屈（器材须前后一致、非弹震热身、三次取最佳 0.25 in/1 cm、<15 in 够不到）；过顶深蹲（双肩宽握、髋褶低于膝顶、pass/fail、≥5 次侧面观察）；禁弹震拉伸。ce14-04/ce14-06 为失败反例。**未解决处**：f14-13 承认"哪种筛查最适用无共识、与损伤关联未确立"（记入 gap）。
- **V2_executability**: passed: true
  - check_mode: walkthrough
  - input: 首次坐位体前屈用尺测得 20 cm，第二次拟改用标准箱；某运动员过顶深蹲时脚跟离地。
  - expected: 器材须前后一致 → **不得改用箱**（否则不可比）；过顶深蹲脚跟离地 → 判"不通过（pass/fail）"；柔韧测试禁弹震。
  - observed: 输出"器材锁定"与"pass/fail 判定"的明确结论。
- **V3_task_utility**: passed: true — expected_benefit: 统一筛查计分方式与柔韧测试流程，锁定器材以防前后测不可比（ce14-04）。
- **decision**: verified
- **if_not_verified**: —

## 能力单元 U18 — 平衡测试协议族（BESS / SEBT）

- **proposed_capability_id**: cap.nsca.balance-test-protocols
- **proposed_slug**: balance-test-protocols
- **type**: procedure
- **merged_candidates**: [f14-17, f14-18, p14-27, p14-28]
- **task_ids**: [T20, T22]
- **importance**: medium
- **source_evidence**:
  - source_id: src-nsca-essentials-5e
    location: Chapter 14 balance 段
- **R 段可用原文引用**（英文，≤100 词，逐字）:
  > "The stances are held for 20 seconds with eyes closed and hands on hips for each condition … Errors include opening eyes; lifting the hands from the hips; touchdown of nonstance foot … The error scores from the BESS test are summed into a single score." (ch14.txt, p14-27 引)
- **V1_source_sufficiency**: passed: true — BESS（6 条件=3 站姿×硬/软地、闭眼手放髋 20 s、7 类错误、六条件错误求和为单总分）；SEBT（八方向 120 cm/45°、单腿中心、每条件 3 次平均、前伸间 15 s 休息、≥4 次练习、无效判定、可只测 AM/M/PM 三向）。**未解决处**：BESS 各条件顺序/条件间休息未给；SEBT 归一化公式在表格中（记入 gap）。
- **V2_executability**: passed: true
  - check_mode: walkthrough
  - input: BESS 六条件分别记错 2/3/1/2/4/2；SEBT 某方向三次 60/62/58 cm。
  - expected: BESS 总分 = 2+3+1+2+4+2 = 14；SEBT 该方向取平均 = (60+62+58)/3 = 60 cm。
  - observed: 总分 14、方向均值 60 cm，数值明确。
- **V3_task_utility**: passed: true — expected_benefit: 统一平衡测试错误计数与试次汇总口径，稳定交付。
- **decision**: verified
- **if_not_verified**: —

## 能力单元 U19 — 人体测量与体成分测量协议（身高/体重/围度/皮褶/BIA）

- **proposed_capability_id**: cap.nsca.anthropometry-bodycomp-measure
- **proposed_slug**: anthropometry-bodycomp-measure
- **type**: procedure
- **merged_candidates**: [f14-14, f14-15, f14-16, p14-31, p14-32, p14-36, p14-37, p14-38, p14-55, ce14-05]
- **task_ids**: [T20, T22]
- **importance**: medium
- **source_evidence**:
  - source_id: src-nsca-essentials-5e
    location: Chapter 14 body composition / anthropometry 段
- **R 段可用原文引用**（英文，≤100 词，逐字）:
  > "Skinfold measurements should be made on dry skin, before exercise, to ensure maximum validity and reliability … Between 1 and 2 seconds after the grip on the caliper has been released, read the dial on the caliper to the nearest 0.5 millimeter. If the measurements do not differ by more than 10%, average the two measurements" (ch14.txt, p14-31 引)
- **V1_source_sufficiency**: passed: true — 人体测量（身高脱鞋 0.25 in/0.5 cm；体重认证天平/清晨排空进食前/避高盐；围度弹簧张力卷尺）；皮褶（干皮运动前、卡尺距指 1–2 cm、松柄后 1–2 s 读 0.5 mm、两次 ≤10% 取平均否则加测）+ 8 位点解剖定义；BIA（录入性别/体重/身高、条件一致、清晨运动前）；体成分方法优选（受训者皮褶 r=0.99 优于围度）。ce14-05 为失败反例。**未解决处**：测量误差可接受范围未量化（记入 gap）。
- **V2_executability**: passed: true
  - check_mode: walkthrough
  - input: 某位点两次皮褶读数 12.0 mm 与 12.5 mm；体脂单次测得 24%。
  - expected: 差异 4% <10% → 取平均 12.25 → 报告到 0.5 mm 即 12.5 mm；体脂**不可报单值**，须带 SEE 区间（见 U21）。
  - observed: 平均与舍入口径明确；并强制触发 U21 的区间报告。
- **V3_task_utility**: passed: true — expected_benefit: 强制测量条件（干皮/运动前/时间一致）与一致性口径，防止体成分测量因条件漂移而失真。
- **decision**: verified
- **if_not_verified**: —

## 能力单元 U20 — Margaria-Kalamen 台阶冲刺功率计算 ★（含单位口径裁断）

- **proposed_capability_id**: cap.nsca.margaria-kalamen-power-calc
- **proposed_slug**: margaria-kalamen-power-calc
- **type**: calculation
- **merged_candidates**: [p14-09, c14-07, p14-50]
- **task_ids**: [T22]
- **importance**: medium
- **source_evidence**:
  - source_id: src-nsca-essentials-5e
    location: Chapter 14 Margaria-Kalamen 步骤 6（ch14.txt:833-835）
- **R 段可用原文引用**（英文，≤100 词，逐字）:
  > "Power in watts is calculated as the athlete's weight (w) in newtons (lb × 4.45 or kg × 9.807) times height (h) in meters (inches × 0.0254) from the third step to the ninth step divided by the measured time interval (t) in seconds; P (watts) = (w × h) / t." (ch14.txt:833-835)
- **V1_source_sufficiency**: passed: true — 公式 P=(w×h)/t、w 单位换算（lb→N/kg→N）、h 换算（in×0.0254，=6×单级高）、t（0.01 s）、重复 2 次间隔 2–3 min，齐全。**来源冲突已回原文核对并裁断**：此处 `lb×4.45 / kg×9.807`，而 ch14.txt:65-66 相对力量处用 `lb×4.44 / kg×9.81`；本簇统一采用 SI 标准 g=9.80665 → **kg×9.81、lb×4.448**（差异 <0.2%），并保留冲突定位。**未解决处**：两次试次取最好/平均未明确（记入 gap）。
- **V2_executability**: passed: true
  - check_mode: walkthrough
  - input: 体重 180 lb（81.6 kg）、单级高 18 cm（6 级落差 h=1.08 m）、第 3→9 级接触时间 t=0.50 s。
  - expected: w = 81.6 × 9.81 = 800.5 N（或 180 × 4.448 = 800.6 N）；P = 800.5 × 1.08 / 0.50 = **1,729 W**（±1%）。查 p14-50 男 15–20 岁档：>2,197 为 Excellent → 1,729 W 落 Average/Fair 区间。
  - observed: 独立核算 P = 864.5 / 0.50 = 1,729.1 W，与预期一致（容差 <1%）；分类对照给出。
- **V3_task_utility**: passed: true — expected_benefit: 统一单位换算口径（消除两处常数不一致），提供可复核的功率数值与分类检索。
- **decision**: verified
- **if_not_verified**: —（冲突以"明确记录采用口径"方式裁断）

## 能力单元 U21 — 体成分估算计算（皮褶→体密度→体脂% + SEE 区间）★

- **proposed_capability_id**: cap.nsca.body-composition-calc
- **proposed_slug**: body-composition-calc
- **type**: calculation
- **merged_candidates**: [p14-33, p14-34, p14-35, c14-04, c14-05]
- **task_ids**: [T22]
- **importance**: high
- **source_evidence**:
  - source_id: src-nsca-essentials-5e
    location: Chapter 14 体成分两步法 / 表 14.35–14.36 口径
- **R 段可用原文引用**（英文，≤100 词，逐字）:
  > "the minimum SEE for population-specific skinfold equations is ±3% to ±5%. Therefore, if a 25-year-old male athlete's body fat is measured at 24%, there is a minimum of a 6% range (21%-27%)." (ch14.txt, p14-33 引)
- **V1_source_sufficiency**: passed: true — 两步法口径（① 表 14.35 按人群/位点选方程算 Db；② 表 14.36 两分模型算 %BF=(a/Db)−b 再 ×100）；SEE 报告规则（±3%–5%、24%→21%–27%）完整；p14-34 给出 Σ3SKF 男性 18–61 岁方程系数（1.109380 − 0.0008267Σ + 0.0000016Σ² − 0.0002574·age），p14-35 给出白人男 18–59 岁 (4.95/Db)−4.50。**未解决处**：完整方程集须回查原表（本文件按表号登记），记入 gap。
- **V2_executability**: passed: true
  - check_mode: walkthrough
  - input: 25 岁男性，Σ3SKF（胸+腹+大腿）= 40 mm，用白人男 18–59 岁方程。
  - expected: Db = 1.109380 − 0.0008267(40) + 0.0000016(40²) − 0.0002574(25) = **1.0724 g/cc**；%BF = (4.95/1.0724 − 4.50)×100 = **11.6%**；报告区间 ±3% → **8.6%–14.6%**。
  - observed: 独立核算 Db = 1.07244 g/cc、%BF = 11.57%（容差 ±0.2 个百分点），报告区间 8.6%–14.6%，与预期一致。
- **V3_task_utility**: passed: true — expected_benefit: 把体脂从"单点数值"改成"带 SEE 的区间"，统一人群方程选用口径，消除虚假精度。
- **decision**: verified
- **if_not_verified**: —

## 能力单元 U22 — 最大有氧速度（MAS）与 VO2max 估算 ★

- **proposed_capability_id**: cap.nsca.mas-vo2max-estimation
- **proposed_slug**: mas-vo2max-estimation
- **type**: calculation
- **merged_candidates**: [p14-15, c14-06]
- **task_ids**: [T22]
- **importance**: high
- **source_evidence**:
  - source_id: src-nsca-essentials-5e
    location: Chapter 14 MAS 步骤 7（ch14.txt:1133-1135）
- **R 段可用原文引用**（英文，≤100 词，逐字）:
  > "The last speed maintained for at least 2 minutes is considered the speed associated with V̇O2max or MAS … The V̇O2max of the athlete can be calculated by multiplying 3.5 × MAS (speed in km/h)." (ch14.txt:1133-1135)
- **V1_source_sufficiency**: passed: true — MAS 判定（保持 ≥2 min 的最后速度）、终止规则（两次未达下一锥）、VO2max=3.5×MAS（km/h）、无音频时哨声计时（25 m/10 km/h → 每 9 s）完整。**未解决处**：系数 3.5 的量纲未解释（经验回归系数），记入 gap；与 U16 的"1.5-mile 只能查表"形成对比——MAS 有公式、1.5-mile 无公式。
- **V2_executability**: passed: true
  - check_mode: walkthrough
  - input: 运动员 MAS = 16 km/h。
  - expected: VO2max = 3.5 × 16 = **56 mL·kg⁻¹·min⁻¹**；若 25 m 锥距、配速 14 km/h，哨声间隔 = 25/(14/3.6) = 6.43 s。
  - observed: 独立核算 56 mL·kg⁻¹·min⁻¹；哨声间隔 ≈6.4 s，与公式一致。
- **V3_task_utility**: passed: true — expected_benefit: 提供可复核的 MAS→VO2max 换算与哨声计时口径，统一有氧估计。
- **decision**: verified
- **if_not_verified**: —

## 能力单元 U23 — 描述统计、数据标准化与运动员画像 ★

- **proposed_capability_id**: cap.nsca.descriptive-stats-athletic-profile
- **proposed_slug**: descriptive-stats-athletic-profile
- **type**: framework
- **merged_candidates**: [f13-15, f14-20, f14-21, f14-23, p14-39, p14-40, p14-41, p14-42, p14-43, p14-46, c14-01, c14-11, c14-12]
- **task_ids**: [T22, T23]
- **importance**: high
- **source_evidence**:
  - source_id: src-nsca-essentials-5e
    location: Chapter 14 statistics / profile 段（ch14.txt:1629-1651；1691-1702）
- **R 段可用原文引用**（英文，≤100 词，逐字）:
  > "The z-score can be used to express the distance of any individual score in standard deviation (SD) units from the mean … Graphs can be a useful way of representing z-scores visually … provide assistance with making decisions on which weaknesses to target with a training program." (ch14.txt:1629-1633)
- **V1_source_sufficiency**: passed: true — SD 公式(14.1)、z 公式(14.2)、百分位秩定义、集中趋势/离散度选择规则、四类分析路径（纵向/横向历史/组内/外部常模）、差值分与百分比变化、画像六步（选测试→选有效可靠测试+排序休息→多人施测→定 SWC 对照常模→重复测试可视化→用于编程）；c14-01（z=−1.2）、c14-11（摔跤电池≥10 min 间隔）、c14-12（z 柱状图判弱项）。**未解决处**：四类分析选用权重未给（记入 gap）。
- **V2_executability**: passed: true
  - check_mode: walkthrough
  - input: 组内 40 yd 冲刺成绩 [10,12,14,16,18]（均值 14、SD）；某运动员 40 yd = 4.6 s、组均 5.00 s、SD 0.33 s。
  - expected: SD = √(40/4) = 3.162；z = (4.6−5.00)/0.33 = **−1.21**（比组均快 1.2 SD）；用 z 柱状图定位负 z 项为训练重点。
  - observed: 独立核算 SD = 3.16、z = −1.21，与原文 c14-01 的 −1.2 一致；产出弱项清单方向正确（注意时间类越小越好）。
- **V3_task_utility**: passed: true — expected_benefit: 把零散测试分数统一为标准分并合成可决策的运动员画像，改善决策结构。
- **decision**: verified
- **if_not_verified**: —

## 能力单元 U24 — 幅度统计（SWC / 效应量 / 差异分解读）★

- **proposed_capability_id**: cap.nsca.swc-effect-size
- **proposed_slug**: swc-effect-size
- **type**: calculation
- **merged_candidates**: [f14-22, f14-24, p14-44, p14-45, c14-02, c14-03]
- **task_ids**: [T22]
- **importance**: high
- **source_evidence**:
  - source_id: src-nsca-essentials-5e
    location: Chapter 14 magnitude statistics 段（ch14.txt:1662-1683）
- **R 段可用原文引用**（英文，≤100 词，逐字）:
  > "it is typically calculated as 0.2 of the between-subjects standard deviation … reference values for small (0.2), moderate (0.6), large (1.2), and very large (2.0) can be a useful starting point." … "The calculated effect size would be equal to (111.7 − 104.5) / 5.7 = 1.26." (ch14.txt:1666-1679)
- **V1_source_sufficiency**: passed: true — SWC=0.2×组间 SD（纵跳 SD 10 cm → 2 cm）、ES=(后测均值−前测均值)/前测 SD（卧推 104.5→111.7、SD 5.7 → ES=1.26「大」）、量级锚点 0.2/0.6/1.2/2.0；并给出"仅凭进步幅度评价计划"的两大陷阱（收益递减、故意低报）。**未解决处**：SWC"多种确定方式"其他算法未给、ES 阈值仅"起点"（记入 gap）。
- **V2_executability**: passed: true
  - check_mode: walkthrough
  - input: 纵跳组间 SD = 10 cm；卧推前测 104.5 kg（SD 5.7）、后测 111.7 kg。
  - expected: SWC = 0.2 × 10 = **2 cm**；ES = (111.7 − 104.5)/5.7 = **1.26 → 大效应**。
  - observed: SWC=2 cm、ES=1.263→1.26，与原文算例一致（容差 ±0.01）。
- **V3_task_utility**: passed: true — expected_benefit: 把"统计显著"换成"实践意义"判断，并识别"进步幅度"评价的失败边界（f14-24）。
- **decision**: verified
- **if_not_verified**: —

## 能力单元 U25 — 常模数据的查找与解读口径（表 14.1–14.37）★

- **proposed_capability_id**: cap.nsca.norms-lookup-interpretation
- **proposed_slug**: norms-lookup-interpretation
- **type**: template
- **merged_candidates**: [p14-47, p14-48, p14-49, p14-50, p14-51, p14-52, c14-13, ce14-08]
- **task_ids**: [T23]
- **importance**: medium
- **source_evidence**:
  - source_id: src-nsca-essentials-5e
    location: Chapter 14 常模表（Table 14.1–14.37）与百分位描述口径（ch14.txt:2537）
- **R 段可用原文引用**（英文，≤100 词，逐字）:
  > "Descriptors for percentile rankings: 90 = well above average; 70 = above average; 50 = average; 30 = below average; 10 = well below average" … "The values listed are means ± standard deviation. The data should be regarded as only descriptive, not normative." (ch14.txt:2537, 2424)
- **V1_source_sufficiency**: passed: true — 统一百分位描述口径（90/70/50/30/10）跨表通用；p14-48 给出 Table 14.1–14.37 的**表号–表名–口径–关键锚点清单**（1RM 三项、IMTP、北欧腘绳、立定跳远、纵跳/静跳、反弹跳 RSI、Margaria、VBT 速度带、300-yd、90 s 箱跳、部分卷腹、俯卧撑、AFT HRP、YMCA、SEBT、VO2max/1.5-mile、12-min、Yo-Yo IR1、变向、5-10-5、Illinois、速度、BESS、皮褶方程、体脂描述）；ce14-08 提示**部分表仅描述性非规范**。**使用约束**：须核对样本年代/协议/设备（BOOK_OVERVIEW 3.1）。
- **V2_executability**: passed: true
  - check_mode: walkthrough
  - input: 运动员 1RM 卧推 100 kg，人群 = NCAA D-I 女子篮球；拟查表 14.1。
  - expected: 定位表 14.1 对应人群列 → 找到 100 kg 落入的百分位列 → 赋予描述词（90 远高/70 高/50 平均/30 低/10 远低）；若表注明"descriptive, not normative"（如表 14.4/14.5/14.10），须标注**不得当标准常模**。
  - observed: 输出"百分位 + 描述词 + 表性质标注"的明确结果；对描述性表强制加注（ce14-08）。
- **V3_task_utility**: passed: true — expected_benefit: 统一跨表读表语言（描述词），防止把描述性表误当规范常模；集中登记 37 张表避免逐表建单元。
- **decision**: verified
- **if_not_verified**: —（本单元为"表索引 + 读表口径"，具体数值表随包以附录/参考形式交付）

## 能力单元 U26 — 反应力量指数（RSI）与离心利用率（EUR）计算 ★

- **proposed_capability_id**: cap.nsca.rsi-eur-calculation
- **proposed_slug**: rsi-eur-calculation
- **type**: calculation
- **merged_candidates**: [p14-10, p14-11, c14-08]
- **task_ids**: [T22]
- **importance**: medium
- **source_evidence**:
  - source_id: src-nsca-essentials-5e
    location: Chapter 14 drop/rebound jump 段（ch14.txt:772-776；806-808）
- **R 段可用原文引用**（英文，≤100 词，逐字）:
  > "reactive strength index (calculated as jump height divided by ground contact time) … For the 10-5 repeated jump test, the best 5 repetitions in terms of reactive strength index are used and averaged for the test outcome." (ch14.txt:773-808)
- **V1_source_sufficiency**: passed: true — RSI=跳高÷触地时间；10-5 取最佳 5 次 RSI 平均；EUR=CMJ 高度÷蹲跳高度。**未解决处**：原文未明确高度/时间单位与归一口径（随设备而变）与分类阈值（记入 gap）。
- **V2_executability**: passed: true
  - check_mode: walkthrough
  - input: 落地跳跳高 0.35 m、触地时间 0.20 s；CMJ 40 cm、蹲跳 34 cm。
  - expected: RSI = 0.35/0.20 = **1.75 m/s**；EUR = 40/34 = **1.18**。
  - observed: 独立核算 RSI=1.75 m/s、EUR=1.176，与预期一致。
- **V3_task_utility**: passed: true — expected_benefit: 统一拉长-缩短循环相关指标口径，提供可复核数值。
- **decision**: verified
- **if_not_verified**: —

---

## 出簇候选（不计入 26 个单元）

| 候选 | 内容 | 判定 | 去向 |
|---|---|---|---|
| c14-14 | Table 11.4 体力活动水平（PAL）及活动系数（1.00–1.48） | **reference** | 实为 **Chapter 11 营养**内容（RMR×活动系数→EER），与"测试选择/实施/数据解释"（T20–T23/T40）无关。应并入营养/能量需求簇（Ch11）的候选池，及 `book/glossary.md` 的 PAL 条目。本簇不建单元。 |

---

## 覆盖核查表

| task_id | 任务 | 原文位置 | 对应候选 | decision | 去向 |
|---|---|---|---|---|---|
| T20 | 评估测试质量（效度/信度/客观性）并选测试 | Ch13（ch13.txt:166-357, 642-647） | f13-01/02/03/14, p13-01..12, ce13-01/04, c13-02 | verified | U1, U2,（+U6），另 U10–U19 各协议 |
| T21 | 规范测试实施流程与顺序 | Ch13（ch13.txt:723-904）/Ch14 管理 | f13-05..09, p13-18..26, f13-10..12, f14-01/02, p14-58 | verified | U3, U4, U5, U7, U8, U9 |
| T22 | 计算/解释测试数据并构建运动员画像 | Ch14（ch14.txt:63-835, 1589-1702） | p14-01/02/09/10/11/15/33..36, c14-01..08, f14-20..23, p14-39..46 | verified | U10, U14–U18, U20–U24, U26 |
| T23 | 运用常模数据做描述性与百分位比较 | Ch14 Table 14.1–14.37（ch14.txt:2537 及表区） | p14-47..52, c14-13, ce14-08 | verified | U25（+U23） |
| T40 | 判断年龄/性别/环境因素对测试的影响 | Ch13（ch13.txt:642-678） | p13-13, p13-14（年龄/性别）；f13-04, p13-15, f13-11, p13-16, ce13-05（环境） | verified | U2（年龄/性别）, U7（环境） |

> T40 说明：**本簇有对应候选**（p13-13 训练状态/经验、p13-14 年龄性别、f13-04/p13-15/f13-11/p13-16/ce13-05 环境），不构成缺口；年龄/性别的处方层差异（青少年/老年/女性）分别属 Ch7/Ch8，由其他簇负责。

---

## 本簇缺口清单

1. **p14-14（1.5-mile 跑推算 VO2max）—— 原文无回归公式，只能查表**（已回原文 ch14.txt:1045-1048 确认：正文仅指向表 14.22–14.25/14.26）。已在 U16 写明"**只能查表、不可自行拟合**"。**重要缺口**：若阶段 2 需要公式，须回查 ACSM 原出处，不得由本簇补造。
2. **单位换算常数在原文自相矛盾**：ch14.txt:65-66（相对力量）用 `lb×4.44 / kg×9.81`；ch14.txt:833（Margaria 功率）用 `lb×4.45 / kg×9.807`。已裁断统一采用 kg×9.81、lb×4.448（见文首与 U10/U20）。**保留冲突定位备查**。
3. **p13-07 信度量化缺公式**：ICC 与典型误差（TE）原文仅定性（"ICC 用作重测信度、TE 合并设备误差+生物学变异"），未给解析式与可接受阈值。已并入 U6 并在此登记，未用常识补齐。
4. **p14-03 全尺度幂指数 b 未给数值**（原文明言"仍存争议"）；**f14-13 动作筛查"哪种最适用无共识、与损伤关联未确立"**；**p14-18 30-15 IFT"每变向 0.7 s"折算距离的完整式未给**；**p14-07 Wingate"功=阻力×转数"单位换算未细化**；**f13-01 Figure 13.1 中间步骤与 f13-02 四维权重未展开**。以上均为"部分条件缺失"，已在各单元标注，不补造。
5. **无障碍**：T20–T23、T40 均在本簇找到候选并验证；无"本簇确无候选"的任务。
6. **ce14-08 的预防措施原文未给**（作者仅标注数据"descriptive, not normative"）——已在 U25 以"强制核对样本/协议/年代"的 B 段约束承接，未虚构原文未给的判据。

---

## 供阶段 2 的提示

- **建议组合成"测试选择与实施"能力卡**：U1 + U2 + U3 + U4 + U5 + U6（效度信度门槛 → 电池构建 → 顺序/休息 → 测试员/准备 → 信度排障）。
- **建议组合成"测试安全红线"卡片（高优先）**：U8（转诊/低钠血症），可与 U7（环境/高温）合并为"安全与条件控制"。
- **建议组合成"测试项目协议族"卡片**：U10（最大力量）+ U12（跳跃）+ U13（速度敏捷）+ U14（无氧）+ U15（局部肌耐力）+ U16（有氧）+ U17（筛查柔韧）+ U18（平衡）+ U19（体成分测量）—— 每张协议卡内用**表格**列出各测试的关键参数（距离/负荷/节拍/判定/无效条件/常模表号），**不要为每个测试单独建入口**。
- **建议组合成"测试数据解释"卡片**：U20 + U21 + U22 + U23 + U24 + U26（各计算核心，含单位口径裁断与数值演练），U25 作为其"查表与解读"支撑。
- **A1/B 段素材**：c14-01（z=−1.2）、c14-02（SWC=2 cm）、c14-03（ES=1.26）、c14-04（体脂 24%→21%–27%）、c14-11（摔跤电池）、c13-01（前松后紧测成退步）可作 A1 场景；ce13-01/02/03/04/05/06/07、ce14-01..08 作 B 段失败边界；U25 附 ce14-08（描述性表误当常模）。
- **B 段必带约束**：常模/描述性数据的年代与人群依赖（BOOK_OVERVIEW 3.1）、1.5-mile 无公式只能查表、单位换算口径冲突、运动筛查与损伤无确立关联。


---

<!-- ===== 簇 D1-plyometric ===== -->

# 簇 D1-plyometric — 三重验证结果

- 负责任务: T14（设计快速伸缩复合训练计划；Ch19）
- 候选输入: 58 条（来自 cases-g2-ch15-26.md [c19-*] / counter-examples-g2-ch15-26.md [ce19-*] / frameworks-g3-ch18-19.md [f19-*] / principles-g3-ch18-19.md [p19-*]）
- 归并后能力单元: 11 个（9 verified + 2 reference）
- verified: 9 / reference: 2 / needs_review: 0 / rejected: 0
- 回查原文: `.cangjie/source/ch19.txt`（全书 2659 行；下述行号均为该文件行号）

> 说明：f19-07 与 p19-14 为同一"五步 SOP"的两次转述（同机制，非独立证据）；c19-2 与 p19-08、c19-5 与 p19-22、c19-6 与 p19-04/bounds 量度口径亦为同源转述。归并时保留全部原 ID。

---

## 能力单元 U1 — Plyometric 计划设计总纲：需求分析 + 五步 SOP + 变量框架

- **proposed_capability_id**: cap.nsca.plyometric-program-design-sop
- **proposed_slug**: plyometric-program-design-sop
- **type**: procedure
- **merged_candidates**: [f19-01, f19-02, f19-07, p19-14]
- **task_ids**: [T14]
- **importance**: critical
- **source_evidence**:
  - source_id: src-nsca-essentials-5e
    location: Chapter 19 · Needs Analysis / Program Design（ch19.txt 第 262–292、652–655 行）；Steps for Implementing a Plyometric Training Program（ch19.txt 第 678–685 行）
- **R 段可用原文引用**（英文，≤100 词，逐字）:
  > "To properly design a plyometric training program, the strength and conditioning professional must analyze the needs of the athlete by evaluating his or her sport, sport position, anthropometry, and training status." (ch19.txt 274–278)
  > "Effective plyometric programs include the same variables that are essential to any training program design: mode, intensity, frequency, recovery, volume, and progression." (ch19.txt 652–655)
- **V1_source_sufficiency**: passed: true — 原文单处完整给出四要素需求分析与六变量清单（第 274–292、652–655 行），并显式给出五步实施 SOP（第 678–685 行）。适用条件（设计任一 plyo 计划）、必要输入（专项/位置/体重/训练状态）、步骤（5 步）、输出（计划骨架各变量取值入口）齐全。未解决冲突：无。
- **V2_executability**: passed: true
  - check_mode: walkthrough
  - input: 一名网球运动员（无 plyo 经验、体重 78 kg、in-season）
  - expected: 按五步产出①需求画像（专项=多平面侧向+旋转，位置需求=侧向/旋转功率，体重中等→重力类负荷可控，训练状态=beginner）；②目标=提升侧向弹跳功率；③技术教学项（主动平足落地、肩过膝/膝过趾）；④变量取值入口（mode=下肢为主、intensity 查 U2、frequency/recovery 查 U3、volume 查 U2、progression 查 U4）；⑤进阶路径。
  - observed: 按 5 步纸面推演得到完整计划骨架；各变量取值需分别调用于 U2/U3/U4（SOP 本身只给骨架与入口，符合流程型交付物定义）。
  - 若 false：—
- **V3_task_utility**: passed: true — expected_benefit: 提供固定上手顺序，避免遗漏"技术教学先于变量分配"这一关键次序；统一计划交付格式。
- **decision**: verified
- **if_not_verified**: —

---

## 能力单元 U2 — 确定 plyometric 强度与量（Table 19.5 因素 + Table 19.6 触点档位）

- **proposed_capability_id**: cap.nsca.plyometric-intensity-volume
- **proposed_slug**: plyometric-intensity-volume
- **type**: calculation
- **merged_candidates**: [f19-03, f19-05, p19-07, p19-08, p19-27, c19-2]
- **task_ids**: [T14]
- **importance**: critical
- **source_evidence**:
  - source_id: src-nsca-essentials-5e
    location: Chapter 19 · Intensity（Table 19.5，ch19.txt 第 460–519 行）；Volume（Table 19.6，ch19.txt 第 592–619 行）；PLYOMETRIC DRILLS 各动作 Intensity level（第 1153 行起）
  - V1 机制依据（见 reference 单元 REF-1）: ch19.txt 第 136–241 行（Table 19.1 SSC 三相；amortization 能量损失数据；slow/fast SSC 0.25 s 阈值）
- **R 段可用原文引用**（英文，≤100 词，逐字）:
  > "The intensity of plyometric drills is, therefore, multifactorial and should be considered on a continuum from low to high intensity... Generally, as intensity increases, volume should decrease." (ch19.txt 475–486)
  > "TABLE 19.6 Plyometric Volumes. Beginner (no experience) 80 to 100 | Nr to 40 | Nr. Intermediate (some experience) 100 to 120 | 20 to 100 | Nr to 20. Advanced (considerable experience) 120 to 200 | 20 to 120 | 20 to 40. Note: Volume is given in contacts per session. Nr = not recommended." (ch19.txt 609–619)
- **V1_source_sufficiency**: passed: true — Table 19.5 七因素（接触点数/速度/技术/力量-体重比/变向/垂直分量/质量，第 490–519 行）与 Table 19.6 三水平×三强度档触点次数（第 609–619 行）均逐格完整，单位明确（contacts per session；Nr=not recommended）。Table 19.6 各档在候选 f19-05/p19-08/c19-2 与原文一致，无冲突。遗漏已补：原文另给动作强度分级表（第 1153 行起，如 Pogo=Low、Depth Jump=High）与上肢量口径（3–5 组×3–5 次投/接，第 603–607 行），一并纳入。
- **V2_executability**: passed: true
  - check_mode: walkthrough
  - input: **一名中级运动员（some experience）首次进行跳跃类（jump）训练**；拟安排中等强度双腿直线跳跃动作
  - expected: ①强度档：查 Table 19.5——双腿（非单腿）、直线（无变向）、水平速度低、体重未超限 → 判为 **Moderate（中）**；若改为"方形变向跨栏跳"则因减速+重定向 → 显著升为 **High**。②量：查 Table 19.6，Intermediate × Moderate = **20–100 contacts/session**；（对照）若首次取 Low = 100–120；若误取 High 则为 Nr–20（不推荐到极少量）。③规则：强度升则量降。
  - observed: 纸面演练得"中级×中强度=20–100 触点/课"；动作强度由 Table 19.5 多因素判定并随变向升高；高阶强度对中级者仅 Nr–20。数值与原文档位逐格相符。
  - 若 false：— （缺口：Table 19.5 无因素权重，强度档其余判定为定性）
- **V3_task_utility**: passed: true — expected_benefit: 把"强度多因素判定"与"量查表"固化为统一口径，避免新手按单一因素（如仅看箱高）误判强度、或漏查中等强度对中级者的不推荐区；给出可直接引用的触点数字。
- **decision**: verified
- **if_not_verified**: —

---

## 能力单元 U3 — Plyometric 频率与恢复（周间/组间/次间）

- **proposed_capability_id**: cap.nsca.plyometric-frequency-recovery
- **proposed_slug**: plyometric-frequency-recovery
- **type**: procedure
- **merged_candidates**: [f19-04, p19-09, p19-10]
- **task_ids**: [T14]
- **importance**: high
- **source_evidence**:
  - source_id: src-nsca-essentials-5e
    location: Chapter 19 · Frequency（ch19.txt 第 542–569 行）；Recovery（第 571–590 行）
- **R 段可用原文引用**（英文，≤100 词，逐字）:
  > "Rather than concentrating on the frequency, many authors suggest relying more on the recovery time between plyometric training sessions. Forty-eight to 72 hours between plyometric sessions is a typical recovery time guideline for prescribing plyometrics; using these typical recovery times, athletes commonly perform two to three plyometric sessions per week." (ch19.txt 559–565)
  > "Recovery for depth jumps may consist of 5 to 10 seconds of rest between repetitions and 2 to 5 minutes between sets. The time between sets is determined by a proper work-to-rest ratio (i.e., 1:5 to 1:10)..." (ch19.txt 575–579)
- **V1_source_sufficiency**: passed: true — 原文单处完整给出：频率 1–4 次/周（第 543–544 行）；以恢复时间为主导的推理（48–72 h → 常 2–3 次/周，第 559–565 行）；同部位中高量不得连续两天（第 568–569 行）；赛季示例（in-season 橄榄球 1 次、田径 2–3 次；off-season 升至 2–3/3–4，第 548–554 行）；depth jump 次间 5–10 s、组间 2–5 min、work:rest 1:5–1:10（第 575–579 行）。适用条件、输入、输出齐全；无冲突。
- **V2_executability**: passed: true
  - check_mode: walkthrough
  - input: 一名 in-season 美式橄榄球运动员，需安排整季 plyo
  - expected: 周频率 = **1 次/周**（第 548–550 行赛季示例）；两次之间保证 **48–72 h** 恢复；同部位中高量不得连两天；若该课含 depth jump，则次间休息 5–10 s、组间 2–5 min、work:rest 维持 1:5–1:10；并注意训练后跳类表现可能受损达 72 h、需与比赛错开。
  - observed: 纸面推演得"in-season 1 次/周 + 48–72 h 间隔 + depth jump 5–10 s/2–5 min、1:5–1:10"；与原文月份示例与恢复公式一致。
  - 若 false：—
- **V3_task_utility**: passed: true — expected_benefit: 把频率决策从"拍脑袋定次数"改为"以恢复窗反推"，减少过度训练与比赛前疲劳累积；统一组间/次间休息口径。
- **decision**: verified
- **if_not_verified**: —

---

## 能力单元 U4 — Plyometric 进阶（progressive overload；强度↑量↓；计划时长）

- **proposed_capability_id**: cap.nsca.plyometric-progression
- **proposed_slug**: plyometric-progression
- **type**: procedure
- **merged_candidates**: [f19-06, p19-11, p19-12, c19-1, c19-6]
- **task_ids**: [T14]
- **importance**: high
- **source_evidence**:
  - source_id: src-nsca-essentials-5e
    location: Chapter 19 · Progression（ch19.txt 第 621–650 行）；Program Length（第 656–666 行）；Volume 中 bounding 距离进阶（第 598–601 行）
- **R 段可用原文引用**（英文，≤100 词，逐字）:
  > "Plyometrics is a form of resistance training and thus must follow the principles of progressive overload... In simplistic models, as intensity increases, volume decreases. This relationship, however, is variable depending on the athlete's training status and the nature of the activity prescribed." (ch19.txt 621–627)
  > "athlete A who has minimal plyometric experience... may do 3 sets of 10 repetitions of the pogo jump... athlete B... may do the depth jump instead and perform 2 sets of 4 repetitions with a 24-inch (61 cm) box. Elite athlete C may also do the depth jump but... 4 sets of 8 repetitions using a 45-inch (114 cm) box." (ch19.txt 628–639)
- **V1_source_sufficiency**: passed: true — 原文单处完整给出：渐进过载原则（第 621–626 行）；强度↑量↓及其"非总线性"警示（第 626–627、647–650 行）；三水平进阶示例（第 628–639 行）；计划时长 6–10 周、最早 4 周见改善、宜贯穿周期（第 656–666 行）；bounding 30→100 yd 距离进阶（第 598–601 行）。规则与示例齐全；无冲突。
- **V2_executability**: passed: true
  - check_mode: walkthrough
  - input: 运动员 A（新手，当前 pogo jump 3×10）欲进阶
  - expected: 依 p19-11/c19-1——①换更复杂动作（短栏跳 → 换为 depth jump）；②强度升则量降：由 3×10 降为 **2×4（@24 in/61 cm 箱）**；③若为精英则 4×8 @45 in/114 cm；④bounding 可把单次距离由 30 yd 进阶到 100 yd；⑤计划时长按 6–10 周、贯穿训练周期。
  - observed: 纸面推演得下一阶段处方（换动作 + 降组次 + 升强度），数值与 c19-1 原文一致。
  - 若 false：—
- **V3_task_utility**: passed: true — expected_benefit: 提供可核对的两条进阶手段（换更难动作 / 升强度降量），避免"只加次数"的线性堆量；给出计划时长期望。
- **decision**: verified
- **if_not_verified**: —

---

## 能力单元 U5 — 训练前运动员评估与准入（技术/力量/平衡/身体特征）

- **proposed_capability_id**: cap.nsca.plyometric-pretraining-screen
- **proposed_slug**: plyometric-pretraining-screen
- **type**: checklist
- **merged_candidates**: [f19-09, p19-20, p19-21, p19-22, c19-5]
- **task_ids**: [T14]
- **importance**: critical
- **source_evidence**:
  - source_id: src-nsca-essentials-5e
    location: Chapter 19 · Pretraining Evaluation of the Athlete（ch19.txt 第 900–1044 行）
- **R 段可用原文引用**（英文，≤100 词，逐字）:
  > "the athlete must understand proper plyometric technique and possess a sufficient base of strength, speed, and balance. In addition... sufficiently mature, both physically and psychologically, to participate in a plyometric training program." (ch19.txt 901–906)
  > "repeated hops and jumps may require a basic strength level equivalent to a back squat of 1 × body weight, bounding and depth jumps using a box 12 inches (30 cm) tall or shorter may have a back squat strength equivalent of 1.5 × body weight, and depth or box jumps with a box higher than 12 inches (30 cm) may require a back squat strength equivalent of 2 × body weight." (ch19.txt 965–971)
- **V1_source_sufficiency**: passed: true — 原文单处完整给出四项准入判据：技术（肩过膝、膝过趾、主动平足落地、避免 valgus，第 908–944 行）；力量（back squat 当量 1×/1.5×/2× 体重分档，第 963–971 行，并注 RFD 与力量同等重要，第 989–995 行）；平衡（Table 19.9 三档、均须 30 s，第 996–1044 行）；身体特征（>100 kg 与既往伤病，第 1046–1066 行，另见 U8）。适用条件、输入、输出齐全；无冲突。缺口已如实标注：back squat 当量为描述性推断，且原文未给各人群统一准入阈值。
- **V2_executability**: passed: true
  - check_mode: walkthrough
  - input: 一名想开始"箱高 >12 in（30 cm）深跳/箱跳"的运动员
  - expected: ①技术：能以主动平足落地、肩过膝/膝过趾、无膝内扣；②力量：需 ≈ **back squat 2× 体重**当量；若不达标 → 退回 ≤12 in 箱跳（1.5×）或重复 hop/jump（1×）或原地跳（低）；③平衡：进阶者须**单腿半蹲保持 30 s 不跌倒**，且测试面与训练面一致；④成熟度（身体与心理）达要求。
  - observed: 纸面演练得"高箱跳需 2× 体重 back squat 当量、否则降阶动作；平衡门槛单腿半蹲 30 s"。与原文分档一致。
  - 若 false：—
- **V3_task_utility**: passed: true — expected_benefit: 在选动作前先做力量/平衡/技术门槛核对，避免把高危动作发给不达标者；统一"用哪一动作档"的判据。
- **decision**: verified
- **if_not_verified**: —

---

## 能力单元 U6 — 年龄人群 plyo 处方裁剪（青少年 / 儿童 / 大师）

- **proposed_capability_id**: cap.nsca.plyometric-age-adjustment
- **proposed_slug**: plyometric-age-adjustment
- **type**: procedure
- **merged_candidates**: [f19-11, p19-15, p19-16, p19-17, ce19-01, ce19-10]
- **task_ids**: [T14]
- **importance**: critical
- **source_evidence**:
  - source_id: src-nsca-essentials-5e
    location: Chapter 19 · Age Considerations — Adolescents（ch19.txt 第 695–776 行）；Masters（第 778–808 行）
- **R 段可用原文引用**（英文，≤100 词，逐字）:
  > "Because the epiphyseal plates of the bones of prepubescent children have yet to close, depth jumps and other high-intensity lower body drills are contraindicated." (ch19.txt 707–710)
  > "a twice-weekly program for 8 to 10 weeks beginning at 50 to 60 jumps a session and increasing exercise load weekly results in the largest changes in running and jumping performance in young children." (ch19.txt 764–767)
  > "a masters runner with a history of knee surgery such as partial meniscus removal or with significant joint degeneration should regard depth jumps and single-leg plyometric exercises as contraindicated..." (ch19.txt 792–796)
- **V1_source_sufficiency**: passed: true — 原文单处完整给出三类人群规则：青少年骨骺未闭→深跳/高强下肢禁忌 + 情绪成熟度 + 7–8 岁可训（第 707–716 行）；儿童剂量（每周 2 次 × 8–10 周、起始 50–60 跳/节、每周递增，不适者改低强度长周期，第 759–770 行）；大师（先查力量/骨科，健康者深跳与单腿谨慎、宜交替腿 bound 与双腿 hop；有膝手术/退变者深跳与单腿禁忌，第 788–808 行）。输入、判据、输出齐全；无冲突。缺口如实标注：无"可开始 plyo 的通用年龄"；儿童起始量未按体重/强度分级。
- **V2_executability**: passed: true
  - check_mode: walkthrough
  - input: (a) 一名 9 岁儿童初学者；(b) 一名有半月板切除史的大师跑者
  - expected: (a) 儿童——禁用深跳与高强下肢动作；方案=**每周 2 次 × 8–10 周、起始 50–60 跳/节、每周递增**，聚焦动作质量（身体对位与速度）；不耐受者改低强度长周期。(b) 大师——**深跳与单腿 plyo 视为禁忌**，改交替腿 bounding 与双腿 hopping，并依个体表现能力调整强度/量、监测训练后疼痛。
  - observed: 两类输入均得明确白/黑名单与剂量；与原文一致。
  - 若 false：—
- **V3_task_utility**: passed: true — expected_benefit: 把两类高危人群从"成人通用指南"中拆出，避免给骨骺未闭儿童或关节退变者开深跳；给出可核对的动作禁忌清单与起始剂量。
- **decision**: verified
- **if_not_verified**: —

---

## 能力单元 U7 — Plyometric 专项热身（RAMP：激活—动员—增强）

- **proposed_capability_id**: cap.nsca.plyometric-warmup-ramp
- **proposed_slug**: plyometric-warmup-ramp
- **type**: procedure
- **merged_candidates**: [f19-12, p19-13]
- **task_ids**: [T14]
- **importance**: medium
- **source_evidence**:
  - source_id: src-nsca-essentials-5e
    location: Chapter 19 · Warm-Up（ch19.txt 第 667–676 行）；Table 19.7（第 718–749 行）
- **R 段可用原文引用**（英文，≤100 词，逐字）:
  > "a plyometric exercise session should begin with a specific warm-up that incorporates activation, mobilization, and potentiation of the neuromuscular and musculoskeletal system... should consist of low-intensity, dynamic movements that increase in intensity as the warm-up progresses. TABLE 19.7 Examples of Plyometric Warm-Up Drills: Marching; Ground contact (Rapid pogo jump...Straight-leg skip or bound...); Footwork; Neuromuscular acceleration and deceleration." (ch19.txt 668–676, 718–746)
- **V1_source_sufficiency**: passed: true — 原文单处完整给出：热身须含激活/动员/增强（potentiation）三性质（第 668–671 行），特点为低强度动态、递增强度（第 672–674 行），并由 Table 19.7 给出四类热身钻（Marching / Ground contact / Footwork / Neuromuscular acceleration & deceleration，第 718–746 行）。输出（递增强度的热身序列）明确；无冲突。缺口：未给时长/组次定量（如实记录）。
- **V2_executability**: passed: true
  - check_mode: walkthrough
  - input: 当日主训练含 depth jump（高强度）的一次 plyo 课
  - expected: 依 Table 19.7 形成递增强度序列：①Marching（跑姿模仿、强调整位）→ ②Ground contact（rapid pogo jump 不使脚跟触地；straight-leg skip/bound 强调负脚速）→ ③Footwork（变向加减速）→ ④Neuromuscular acceleration & deceleration（多关节爆发变向、全幅度弓步/蹲）；低强度起步、随进程升强度，完成后进入主训练。
  - observed: 纸面推演得四类钻递进序列，覆盖"触地准备→变向准备→神经激活"，与 Table 19.7 一致。
  - 若 false：—
- **V3_task_utility**: passed: true — expected_benefit: 把"直接上高强度跳"改为固定递增强度热身链，降低因热身不足导致的损伤与表现下降；统一热身交付格式。
- **decision**: verified
- **if_not_verified**: —

---

## 能力单元 U8 — 安全与常见错误排障（技术/落地/ACL + 深跳高度/体重 + 场地器材）

- **proposed_capability_id**: cap.nsca.plyometric-safety-troubleshooting
- **proposed_slug**: plyometric-safety-troubleshooting
- **type**: troubleshooting
- **merged_candidates**: [f19-13, f19-10, p19-23, p19-24, p19-25, p19-26, ce19-02, ce19-03, ce19-04, ce19-05, ce19-06, ce19-07, ce19-11]
- **task_ids**: [T14]
- **importance**: critical
- **source_evidence**:
  - source_id: src-nsca-essentials-5e
    location: Chapter 19 · Safety Considerations（ch19.txt 第 888–898 行）；Technique（第 908–944 行）；Physical Characteristics（第 1046–1066 行）；Equipment and Facilities（第 1068–1124 行）；Depth Jumping（第 1125–1137 行）；各动作 Common Errors（第 1153 行起）
- **R 段可用原文引用**（英文，≤100 词，逐字）:
  > "Inward movement of the knees—also termed dynamic valgus—is a significant risk factor for knee injuries of all types, including patellofemoral pain and tears or ruptures of the anterior cruciate ligament (ACL)." (ch19.txt 920–924)
  > "The recommended height for depth jumps ranges from 16 to 42 inches (41-107 cm), with 30 to 32 inches (76-81cm) being the norm... The depth jump box height for athletes who weigh over 220 pounds (100 kg) should be 18 inches (46 cm) or less." (ch19.txt 1133–1137)
  > "Excessively thick exercise mats (6 inches [15 cm] or thicker) may extend the amortization phase and thus not allow efficient use of the stretch reflex." (ch19.txt 1077–1079)
- **V1_source_sufficiency**: passed: true — 原文单处完整覆盖各安全维度：损伤可校正成因链（力量不足/热身不足/引导钻进阶不当/量强度不当/鞋地面差/技能不足，第 890–896 行）；技术（肩过膝/膝过趾、dynamic valgus→各类膝伤含 ACL、主动平足落地、"信用卡规则"，第 908–944 行）；体重 >100 kg 风险与 >18 in 深跳慎用（第 1046–1054 行）；场地（草地/悬浮地板/橡胶垫为佳，混凝土/瓷砖/硬木不推荐，≥6 in 厚垫与迷你蹦床延长 amortization，第 1071–1086 行）、面积（≥30 yd 直道、天花板 ≥10 ft）、箱体（6–42 in、落地面 ≥18×24 in、防滑）、鞋、督导（第 1087–1124 行）；深跳高度 48 in 为否定性上限、推荐 16–42 in、常规 30–32 in（第 1125–1137 行）。判据与输出齐全；无冲突。缺口如实标注：原文未给"成因优先级排序"判据；地面/鞋为推荐非量化标准。
- **V2_executability**: passed: true
  - check_mode: walkthrough
  - input: (a) 一名体重 105 kg 的运动员被安排 24 in（61 cm）箱深跳；(b) 另一名运动员落地时膝内扣
  - expected: (a) 105 kg > 100 kg → 深跳箱高应 **≤18 in（46 cm）**，24 in 超上限 → 降至 ≤18 in 或改其他 plyo 动作；(b) 膝内扣即 **dynamic valgus**，是髌股痛与 ACL 撕裂/断裂的重要危险因素 → 校正为"肩过膝、膝过趾"对位 + 主动平足落地 + 踝背屈，并用信用卡规则自查脚跟离地。
  - observed: 两类输入均得明确"症状→成因→处置"结论，数值（≤18 in）与原文一致。
  - 若 false：—
- **V3_task_utility**: passed: true — expected_benefit: 把分散的安全点(技术/高度/体重/场地/器材)收敛成一张排障表，能在上量前拦截高危处方；为 ACL 风险提供可引用的机制依据（见下方 B 段素材）。
- **decision**: verified
- **if_not_verified**: —
- **B 段素材（ACL / 安全，供阶段 2）**: ce19-03「落地膝内扣（dynamic valgus）增加 ACL 风险」；ce19-02「深跳箱过高」；ce19-04「硬质地面无缓冲」；ce19-05「过厚衬垫/迷你蹦床延长缓冲期」；ce19-06「>100 kg 高量高强度」；ce19-07「力量基础不足」；ce19-11「落地/起跳逐项常见错误」。

---

## 能力单元 U9 — 与抗阻/有氧的整合与排序（含 complex training 三型）

- **proposed_capability_id**: cap.nsca.plyometric-integration-complex
- **proposed_slug**: plyometric-integration-complex
- **type**: decision-framework
- **merged_candidates**: [f19-08, f19-14, p19-18, p19-19, c19-3, c19-4, ce19-08, ce19-09]
- **task_ids**: [T14]
- **importance**: high
- **source_evidence**:
  - source_id: src-nsca-essentials-5e
    location: Chapter 19 · Plyometric Exercise and Resistance Training（ch19.txt 第 817–879 行，含 Table 19.8 第 840–860 行）；Plyometric Exercise and Aerobic Exercise（第 879–887 行）
- **R 段可用原文引用**（英文，≤100 词，逐字）:
  > "Combine lower body resistance training with upper body plyometrics, and upper body resistance training with lower body plyometrics. Performing heavy resistance training sessions and plyometric sessions on the same day is not usually recommended." (ch19.txt 823–827)
  > "Contrast training involves alternating high-load exercises and high-velocity exercises in contrast pairs in a set-by-set fashion... Ascending complex training involves sets of a high-velocity exercise followed by sets of a contrasting high-force exercise... Descending sets require multiple high-force exercises to be completed before the execution of high-velocity exercises." (ch19.txt 864–874)
  > "Before aerobic endurance training. The program design variables do not change..." / "it is advisable to perform plyometric exercise before aerobic endurance training." (ch19.txt 884–886)
- **V1_source_sufficiency**: passed: true — 原文单处完整给出：交叉配对原则（下肢抗阻配上肢 plyo 等，第 823–825 行）；同日重抗阻+plyo 通常不推荐（第 826–827 行）；complex training 定义与三型（contrast/ascending/descending）及示例（第 862–878 行）；Table 19.8 整合样例周（第 840–860 行）；有氧排序"先 plyo 后有氧"（第 883–886 行）。输入、分支、输出齐全；无冲突。缺口如实标注：未给"何时禁止同日组合"的量化疲劳阈值，complex 最优组间休息无定论。
- **V2_executability**: passed: true
  - check_mode: walkthrough
  - input: 一名排球运动员的周计划（需抗阻 + plyo + 有氧）
  - expected: ①交叉配对：下肢抗阻日配上肢 plyo、上肢抗阻日配下肢 plyo；②避免同日"重抗阻 + plyo"；③同日同课需组合时用 complex training——按目标选 contrast（高负荷/高速度逐组交替）、ascending（先高速后高力）或 descending（先多组高力后高速），并保证组间充分休息；④同一日内 plyo 排在**有氧耐力训练之前**。
  - observed: 纸面推演得"交叉配对 + 不同日重抗阻+plyo + plyo 先于有氧"的整合周方案；与 Table 19.8 及排序规则一致。
  - 若 false：—
- **V3_task_utility**: passed: true — expected_benefit: 防止把"重抗阻+plyo 同日"或"有氧后才 plyo"两种常见干扰组合排入计划；给出三型 complex 的可选编排与选择依据。
- **decision**: verified
- **if_not_verified**: —

---

## 能力单元 U10 — Plyometric 动作模式分类表（Table 19.2–19.4）

- **proposed_capability_id**: cap.nsca.plyometric-drill-catalog
- **proposed_slug**: plyometric-drill-catalog
- **type**: template
- **merged_candidates**: [p19-04, p19-05, p19-06]
- **task_ids**: [T14]
- **importance**: medium
- **source_evidence**:
  - source_id: src-nsca-essentials-5e
    location: Chapter 19 · Mode — Table 19.2 Lower Body（ch19.txt 第 343–373 行）；Table 19.3 Upper Body（第 397–423 行）；Table 19.4 Trunk（第 433–458 行）
- **R 段可用原文引用**（英文，≤100 词，逐字）:
  > "Hops: Takeoff from one foot and landing on the same foot... Bounds: Takeoff from one foot and landing, or transitioning through, to the other foot... Jumps: Takeoff and landing with two feet... Depth jumps and hops ('shock' actions) use gravity and the athlete's weight to increase exercise intensity." (ch19.txt 345–373)
  > "the exercise movement must be shorter and quicker to allow stimulation and use of the stretch reflex." (ch19.txt 452–454)
- **V1_source_sufficiency**: passed: true — Table 19.2/19.3/19.4 逐类给出定义与量度口径（hops/bounds/jumps/depth：强度由位移速度/水平速度/高度/箱高定，量按下肢脚触地次数或距离；上肢按投接次数；躯干须缩短动作以激发牵张反射）。可回查位置明确；无冲突。
- **V2_executability**: passed: false — check_mode: walkthrough（不产生具体处方动作/数值）。作为分类目录，它说明"某动作属哪类、按什么口径计量"，但原文未给"根据专项/位置从目录中选出具体动作"的选择规则或评分，无法据表单独产出一个可核对的处方结果。量度口径部分已被 U2（下肢脚触地次数/距离、上肢投接次数）吸收。
- **V3_task_utility**: passed: true — expected_benefit: 作为术语/动作目录，统一"hops/bounds/jumps/depth"的分类与计量口径，避免混用。
- **decision**: reference
- **if_not_verified**: 并入 `book/glossary.md`（动作模式词条：hops/bounds/jumps/depth jumps & hops；上肢 throws/slams/pull/push；躯干 lower-body-anchored / upper-body-anchored / throws）与 `book/overview.md` 的 Plyometric 动作分类参考区；不单独成可执行能力。canonical: cap.nsca.plyometric-drill-catalog（reference）。

---

## 参考单元 REF-1 — SSC 机制（三相 / 过渡相能量损失 / 快慢 SSC 分类）

- **proposed_capability_id**: cap.nsca.ssc-mechanism
- **proposed_slug**: ssc-mechanism
- **type**: rule（机制参考）
- **merged_candidates**: [p19-01, p19-02, p19-03]
- **task_ids**: [T14]
- **importance**: medium
- **source_evidence**:
  - source_id: src-nsca-essentials-5e
    location: Chapter 19 · The Stretch-Shortening Cycle（ch19.txt 第 116–241 行，含 Table 19.1 第 136–150 行）
- **R 段可用原文引用**（英文，≤100 词，逐字）:
  > "This phase of the SSC is perhaps the most crucial in allowing greater power production; its duration must be kept short. If the amortization phase lasts too long, the energy stored during the eccentric phase dissipates as heat..." / "...0.35 s = 25%, 0.9 s = 52%, 1 s = 55%, and 1.5 s = 70%..." (ch19.txt 167–176)
  > "Schmidtbleicher categorized plyometric activities as either slow SSC (>0.25 s) or fast SSC (<0.25 s), depending on their ground contact time." (ch19.txt 238–241)
- **V1_source_sufficiency**: passed: true — 原文单处完整给出 Table 19.1 SSC 三相事件（第 136–150 行）、"过渡相须短"规则与卧推能量损失离散数据（0.35 s=25%、0.9 s=52%、1 s=55%、1.5 s=70%，第 167–176 行）、slow/fast SSC 0.25 s 阈值（第 238–241 行）。位置明确；无冲突。缺口如实标注：p19-02 为离散经验点、无闭式公式，不同动作损失曲线未知。
- **V2_executability**: passed: false — check_mode: walkthrough（不能对任意输入产出结果）。p19-01 为机制描述；p19-02 为离散数据点，无法在任意过渡相时长上外推；p19-03 仅为分类阈值，单独不产出动作或剂量。这三者不构成可独立执行的方法。
- **V3_task_utility**: passed: true — expected_benefit: 为 U2（强度与量判定）与 U8（技术/缓冲安全）提供机制依据：解释"过渡相越短越好""厚垫/蹦床为何失效""为何快速触地"，统一 SSC 术语口径。
- **decision**: reference
- **if_not_verified**: 并入 `book/overview.md` 的 Plyometric 机制参考区与 `book/glossary.md`（词条：eccentric / amortization(coupling) / concentric、SSC、slow SSC / fast SSC、amortization phase）；作为 U2 与 U8 的 V1 机制依据。不单独成可执行能力（遵任务书：SSC 三相不作独立可执行单元）。

---

## 覆盖核查表

| task_id | 任务 | 原文位置 | 对应候选 | decision | 去向 |
|---|---|---|---|---|---|
| T14 | 设计快速伸缩复合（plyometric）训练计划 | Ch19 Needs Analysis/Program Design（第 262–292、652–685 行）；Intensity/Volume（Table 19.5/19.6，第 460–619 行）；Frequency/Recovery（第 542–590 行）；Progression（第 621–666 行）；Pretraining Eval（第 900–1044 行）；Age（第 695–808 行）；Warm-Up（第 667–749 行）；Safety（第 888–1137 行）；Integration（第 817–887 行） | f19-01..f19-14；p19-01..p19-27；c19-1..c19-6；ce19-01..ce19-11 | verified×9 + reference×2 | cap.nsca.plyometric-program-design-sop / plyometric-intensity-volume / plyometric-frequency-recovery / plyometric-progression / plyometric-pretraining-screen / plyometric-age-adjustment / plyometric-warmup-ramp / plyometric-safety-troubleshooting / plyometric-integration-complex；reference→glossary/overview（plyometric-drill-catalog、ssc-mechanism） |

- 覆盖结论：T14 全流程（需求分析→强度/量→频率/恢复→进阶→评估→年龄裁剪→热身→安全→整合）在本簇均有两处以上原文支撑的候选，无遗漏。
- 交界说明：`f20-11`（SSC 训练设计两判据）属簇 D2（速度敏捷），本簇不重复收录；本簇仅收 `f19-08`（与抗阻整合 / complex training）与 `f19-14`（与有氧排序），均并入 U9。

## 本簇缺口清单

- **critical/high 任务缺口**：无"缺失候选"级缺口；但以下为原文固有信息不足，已如实保留、不在验证阶段用常识补齐：
  1. Table 19.5 各因素**无权重/无量化评分**（原文第 490–519 行）→ 强度档判定除查表分档外仍为定性（影响 U2）。
  2. p19-02 过渡相能量损失仅 4 个离散点、**无闭式公式**且仅卧推数据 → 降为 reference（REF-1）。
  3. **量–强度个体化换算曲线缺失**：原文未给把距离（bounds）换算成触地次数的公式，也未给各水平下强度×量的连续换算（Table 19.6 为区间档）。
  4. **无"可开始 plyo 的通用年龄"**；儿童起始量（50–60 跳/节）未按体重/强度分级（U6 已标注）。
  5. 同日"重抗阻+plyo"的**量化疲劳阈值**、complex training **最优组间休息**，原文均未给（U9 已标注）。
  6. 深跳箱高对 **<100 kg 者无精确上界**（仅给总区间 16–42 in 与常规 30–32 in，U8 已标注）。

## 供阶段 2 的提示

- **适合组合成一张能力卡**：U1（总纲 SOP）可作为主卡骨架，串联 U2（强度/量）、U3（频率/恢复）、U4（进阶）、U5（评估）、U7（热身）、U8（安全）作为 A2 子步骤或链接卡；U9（整合/complex）可独立成"多模态整合"卡。
- **A1 优先素材（worked example）**：`c19-1`（Athlete A/B/C 三水平进阶，U4）与 `c19-3`（Table 19.8 抗阻+跳跃整合样例周，U9）——两者都是可直接演示的完整样例，列为 A1 首选。其余 A1 备选：`c19-4`（complex 三型示例）、`c19-5`（平衡测试进阶）、`c19-6`（bounding 30→100 yd）。
- **B 段素材**：ACL/安全反例群（ce19-02/03/04/05/06/07/11）供 U8 的 B 段；ce19-01、ce19-10（年龄禁忌）供 U6 的 B 段；ce19-08、ce19-09（同日重抗阻 / 有氧后 plyo 的干扰）供 U9 的 B 段。
- **R 段引用**：上列各单元的英文逐字引用可直接入 R 段；U2 另可引 Table 19.6 原表文本作为"口径唯一来源"。
- **术语卡**：REF-1（SSC 机制）与 U10（动作模式目录）建议在 glossary 中建立词条，供 U2/U8 交叉引用。


---

<!-- ===== 簇 D2-speed-agility ===== -->

# 簇 D2-speed-agility — 三重验证结果

- 负责任务: T15, T16
- 候选输入: 61 条（来自 cases-g2-ch15-26.md, counter-examples-g2-ch15-26.md, frameworks-g4-ch20-22.md, principles-g4-ch20-22.md）
- 归并后能力单元: 15 个
- verified: 14 / reference: 1 / needs_review: 0 / rejected: 0

> 回查原文：`books/nsca-essentials-5e/.cangjie/source/ch20.txt`（3202 行）。以下 source_evidence 均为已回查到的行号；quote 为逐字英文。
> 说明：本簇全部来自 Ch20。Ch20 未给出 RSI（reactive strength index）计量公式（仅出现 "reactive strength" 这一训练优先项），RSI 数值口径应属 Ch19（其他簇），见缺口清单。

---

## 能力单元 U1 — 速度/变向/敏捷三分定义与「变向 vs 反应性敏捷」判定框架

- **proposed_capability_id**: cap.nsca.speed-cod-agility-attribution
- **proposed_slug**: speed-cod-agility-attribution
- **type**: framework
- **merged_candidates**: [f20-01, p20-01, f20-16, p20-21, ce20-04]
- **task_ids**: [T16, T15]
- **importance**: high
- **source_evidence**:
  - source_id: src-nsca-essentials-5e
    location: Chapter 20, "Agility Performance and Change-of-Direction Ability"（ch20.txt 第 1140–1164 行）；"Factors Affecting Change of Direction and Perceptual-Cognitive Ability"（第 1201–1234 行，含 Table 20.3 于第 1245–1283 行）；Ch20 开篇三分定义（p20-01 对应术语框，第 ~14–30 行附近）
- **R 段可用原文引用**（英文，逐字）:
  > "Speed. The skills and abilities needed to achieve high movement velocities. Change of direction. The skills and abilities needed to explosively change movement direction, velocities, or modes. Agility. The skills and abilities needed to change direction, velocity, or mode in response to a stimulus." ... "tests without a reactive aspect should be considered COD tests, and a test that includes a reactive stimulus is now by definition a test of agility for most sports." ... "do not develop agility per se"
- **V1_source_sufficiency**: passed: true — 三分定义、判据（有无 reaction stimulus）、Table 20.3 维度归类（COD speed / maneuverability / perceptual-cognitive / metabolic requirement）在 ch20.txt 第 1140–1283 行有完整一处说明；ce20-04 的 "do not develop agility per se" 亦回查到（第 1782 行）。无冲突。
- **V2_executability**: passed: true
  - check_mode: walkthrough
  - input: 「篮球后卫，能在预定路线的反跑中快速摆脱（预先计划变向）；但防守时面对对手运球变向常慢半拍，预判差。」
  - expected: 归因为两类能力并存——预定路线部分是 COD（预先计划），防守反应部分是 Agility（含知觉—认知）；训练重点应各配一项：COD 用闭技能变向 drill，敏捷部分需加反应性刺激（对手/视频）；测试应选含 reaction stimulus 的敏捷测试而非 5-0-5。
  - observed: 沿 `f20-01` 四步（直线 vs 多向 → 是否预先计划 → 是否有反应刺激 → 归因）→ 得出「变向=COD、防守迟疑=反应性敏捷不足」；按 Table 20.3，5-0-5 仅标 COD speed，须改选标有 Perceptual-cognitive ✓ 的 reactive agility / Y-shaped（specific stimulus）测试。结论明确。
- **V3_task_utility**: passed: true — expected_benefit: 统一「速度/COD/敏捷」三分口径，避免把封闭变向练习当敏捷训练（防 ce20-04 类误配），并可据测试是否含反应刺激稳定地把运动员问题分流到 COD 或敏捷。
- **decision**: verified

---

## 能力单元 U2 — 速度/变向/敏捷的力学指标口径与计算（RFD / impulse / momentum / power / COD deficit）

- **proposed_capability_id**: cap.nsca.speed-force-metrics
- **proposed_slug**: speed-force-metrics-calculation
- **type**: calculation
- **merged_candidates**: [f20-02, p20-02, p20-03, p20-04, p20-05, p20-06, f20-09, p20-19, p20-20, c20-5]
- **task_ids**: [T15, T16]
- **importance**: high
- **source_evidence**:
  - source_id: src-nsca-essentials-5e
    location: "Rate of Force Development"（ch20.txt 148–162 行）、"Impulse"（183–230 行）、"Momentum"（215–224 行）、"Power has not been discussed…"（231–240 行）；"Practical Implications for Change of Direction and Agility"（258–271 行，braking impulse）；COD deficit / sprint momentum（1235–1243 行）；Table 20.12 COD deficit 释义（2549–2562 行）
- **R 段可用原文引用**（英文，逐字）:
  > "Impulse—The product of the generated force and the time required for its production, which is measured as the area under the force–time curve. According to the impulse–momentum relationship, net impulse dictates the magnitude of change of momentum of an object." ... "the generation of maximal contraction force takes at least 300 milliseconds, while many sport activities consume 0 to 200 milliseconds" ... "to isolate COD ability, the COD deficit (5-0-5 test time—10 m linear sprint time) could be determined."
- **V1_source_sufficiency**: passed: true — RFD 公式（Δforce/Δtime）、impulse（力×时间=曲线下面积）、momentum（m×v）、power 派生性、300 ms/0–200 ms 阈值、COD deficit 公式、sprint momentum 公式均在 ch20.txt 有完整一处说明。**未解决项**：原文未显式给 impulse/momentum/COD deficit 的 SI 单位（N·s、kg·m/s），阶段 2 须在 B/E 段标注「单位系补充规范」。c20-5 与 Table 20.12 一致，无冲突。
- **V2_executability**: passed: true
  - check_mode: walkthrough
  - input（构造的合法新数据）：力—时间曲线上，某次触地在 0→0.05 s 内力由 0 升至 1,500 N；后续 0.20 s 内平均力 500 N。运动员 80 kg。5-0-5 用时 2.60 s，10 m 直线冲刺 1.85 s；线性冲刺段平均速度 5.0 m/s。
  - expected（独立核算）：
    - RFD = 1500 N ÷ 0.05 s = 30,000 N/s（容差 ±2%）。
    - Impulse = 500 N × 0.20 s = 100 N·s；Δmomentum = 100 kg·m/s → Δv = 100/80 = 1.25 m/s。
    - Power（派生）= F×v = 1000 N × 3.0 m/s = 3000 W（用给定 F、v）。
    - COD deficit = 2.60 − 1.85 = 0.75 s（容差 ±0.01 s）。
    - Sprint momentum = 5.0 m/s × 80 kg = 400 kg·m/s。
  - observed: 逐式代入得 30,000 N/s、100 N·s、Δv 1.25 m/s、3000 W、COD deficit 0.75 s、sprint momentum 400 kg·m/s，全部落在容差内；并用 300 ms/0–200 ms 阈值判定「该触地窗口 0–200 ms，故 RFD/impulse 而非最大力是限制项」。输出明确。
- **V3_task_utility**: passed: true — expected_benefit: 统一力学口径（力/RFD/impulse 为直接抓手，power 为派生量不单独测），并以 COD deficit 剥离直线速度对 5-0-5 的污染，使「变向能力」可被量化比较。
- **decision**: verified

---

## 能力单元 U3 — 敏捷/变向发展的需求分析与分期处方（5 步流程 + 3 block 模板）

- **proposed_capability_id**: cap.nsca.agility-needs-to-program
- **proposed_slug**: agility-needs-analysis-to-program
- **type**: procedure
- **merged_candidates**: [f20-04, p20-25, p20-32, c20-2, p20-26, p20-27, c20-3, c20-4]
- **task_ids**: [T15, T16]
- **importance**: high
- **source_evidence**:
  - source_id: src-nsca-essentials-5e
    location: 5 步流程（ch20.txt 2366–2384 行）；Table 20.9 需求分析（2386–2404 行）；Table 20.10 时间分配（2423–2441 行）；Table 20.11 3-block 处方（2443–2520 行）
- **R 段可用原文引用**（英文，逐字）:
  > "Step 1. Perform a needs analysis of the sport and match tests appropriately to assess these qualities (table 20.9). Step 2. Determine strengths and weaknesses by comparing results as a standardized score to performance standards or team mean (figure 20.13). Step 3. Plan the development of a primary area of need and a secondary area of need for the athlete." ... "The length of time for a training session is between 10 and 15 minutes inclusive of work and rest time and can be completed one to three times per week"
- **V1_source_sufficiency**: passed: true — 5 步、Table 20.9/20.10/20.11 的字段与数值均在 ch20.txt 完整回查：
  - Table 20.10 分配 **COD ~65/60/50%、Maneuverability ~35/30/25%、Agility ~N/A/20/25%**（2429–2433 行，与候选一致）。
  - Table 20.11 **Block1 主目标线性减速，Decelerations 5 yd 1×6(30 s)；Lateral shuffling@height 或 backpedaling 1×4×11 yd[10 m](30 s)；2–3 次/周**（2443–2459 行）；Block3 **Modified 5-0-5 2×4(30 s;2 min)、T-test 1×4(30 s)、Reactive agility(Y) 1×4(30 s)**（2493–2515 行）。数值逐项核对一致。
- **V2_executability**: passed: true
  - check_mode: walkthrough
  - input: 「足球边后卫，赛季前 12 周（8 周休赛 + 4 周赛前）；队均值已知其 5-0-5、T-test、决策时间成绩；高速度变向为专项需求但侧向减速弱。」
  - expected（交付物）：① 落实 Step1–2 得强弱项（如 COD 标准化分低于队均值 → 第一需求）；② Step3 定主需求=COD（减速）、次需求=机动性；③ Step4 按 Table 20.10 分配 Block1 65/35/0；④ Step5 用 Block2/3 过渡到 60/30/20、50/25/25，并以 COD deficit 监测；输出含每周 1–3 次、每次 10–15 min 的 3×4 周处方。
  - observed: 依表可填出完整 block 序列，Block1 week1 处方=减速 1×6(30 s)+侧向滑步 1×4×10 m(30 s)，与原文一致；缺失输入（队均值缺失时）处理=以 performance standards 替代（Step2 明示两选项）。可产出明确交付物。
- **V3_task_utility**: passed: true — expected_benefit: 把「测试→强弱项→主次需求→时间分配→百分比过渡」固化为可复制的敏捷编程 SOP，避免随机安排或只用小场对抗（原文 2350–2353 行明确否定）。
- **decision**: verified

---

## 能力单元 U4 — 速度发展的 short-to-long 分期处方（Table 20.7）

- **proposed_capability_id**: cap.nsca.speed-short-to-long
- **proposed_slug**: speed-short-to-long-periodization
- **type**: procedure
- **merged_candidates**: [f20-08, p20-24, c20-1, c20-6]
- **task_ids**: [T15]
- **importance**: high
- **source_evidence**:
  - source_id: src-nsca-essentials-5e
    location: short-to-long 说明（ch20.txt 1988–1995 行）；Table 20.7 全文（2008–2140 行）；acceleration hold 脚注 b（2171–2178 行）
- **R 段可用原文引用**（英文，逐字）:
  > "This model, which can be referred to as a short to long method of sprint training, is a conceptual progression that attempts to merge the relationship between larger rates of acceleration and greater sprint velocities." ... "For instance, an athlete may be prescribed acceleration holds for 40 meters, but the coach's mark ending the acceleration zone is placed at the 20-meter mark on the track."
- **V1_source_sufficiency**: passed: true — Table 20.7 四个 block 的 target aim 与 example microcycle 数值均回查：Block1 **Incline sprints 1×3×15 m (1.5 min)、1×4×20 m (2 min)**；Block2 **Incline sprints 1×3×30 m (3 min)、Sled tows 2×3×20 m (2 min/4 min)、Acceleration holds 1×3×40 m (4 min)**；Block3 **Block starts 1×2×20 m、Fly-ins 1×4×20 m build/20 m fly (4 min)、Speed-endurance 1×2×60 m (5.5 min)**；Block4 **Fly-float-fly 1×4×20/20/20 (7 min)**（2008–2140 行）。acceleration hold 定义见 2171–2178 行。数值一致。
- **V2_executability**: passed: true
  - check_mode: walkthrough
  - input: 「100 m 短跑选手，休赛期 16 周，4 个 4 周 block，每周一/三/五速度课。」
  - expected: 生成 4 block 序列——B1 加速发展（斜坡冲刺、阻力加速 bounds）→B2 长加速（平地/牵引、acceleration holds）→B3 引入最大速（block starts、fly-ins、速度耐力置于周内高疲劳位）→B4 强化最大速（更长 fly-in、race modeling、技术课 ankling/A-skip）；每课含技术 drill 热身，含组×距离×(组间休息)。
  - observed: 逐 block 套用 Table 20.7 得 B1 周一 Incline sprints 1×3×15 m (1.5 min) 等 12 节课处方，格式统一、交付物明确；缺失输入（可用周数非 16 周）处理=按 block 目标等比缩放 microcycle 数。可输出明确结果。
- **V3_task_utility**: passed: true — expected_benefit: 稳定交付「先发展加速、再桥接最大速」的短跑分期处方格式，防止把最高速训练过早前置。
- **decision**: verified

---

## 能力单元 U5 — 冲刺技术错误排障（症状→原因→纠正，Table 20.1）

- **proposed_capability_id**: cap.nsca.sprint-technique-troubleshoot
- **proposed_slug**: sprint-technique-troubleshooting
- **type**: troubleshooting
- **merged_candidates**: [f20-17, p20-13, p20-18, ce20-01, ce20-02, ce20-03, ce20-05]
- **task_ids**: [T15]
- **importance**: high
- **source_evidence**:
  - source_id: src-nsca-essentials-5e
    location: Table 20.1 全文（ch20.txt 721–829 行，分 START AND ACCELERATION / MAXIMUM VELOCITY 两段）；Figure 20.9 冲刺技术角度口径（p20-18，散见 842–851 行训练目标与相关 drill 说明）；overstriding 诊断（790–798 行）
- **R 段可用原文引用**（英文，逐字）:
  > "Table 20.1 highlights many common sprinting errors as well as possible causes and coaching corrections. Quite often, these errors are the result of the misapplication of forces due to improper coaching cues, insufficient mobility, or disruption to an athlete's normal gait caused by external interference." ... "Instruct the athlete to drive the foot down and back into the track, not paw."
- **V1_source_sufficiency**: passed: true — Table 20.1 的 Error/Cause/Coaching recommendation 三列在 ch20.txt 逐条回查（臀部过高、侧向迈步、摆臂短紧、颈后仰、跨膝、过早直立、前侧膝高不足、overstriding、腘绳肌慢性伤、cyclying leg、额状面摆臂共 ~12 条）。pawing（811–821 行）、overstriding（790–798 行）、摆臂不越中线（823–838 行）均逐字命中。
- **V2_executability**: passed: true
  - check_mode: walkthrough
  - input（构造的一个具体技术错误）: 「运动员 40 m 冲刺全程出现 overstriding，触地时间偏长；其教练曾用『沿线逐步拉长步点』的 drill 提速。」
  - expected（诊断路径）：症状=overstriding → 原因=误解发力（试图用更大触地时间提速，抑制 SSC、降低步频）+ 错误引导 → 纠正=让其在本道内保持自然步态、以增强垂直发力而非加步幅提速；并复核步态恢复。
  - observed: 对 Table 20.1 第 9 条与 ce20-01，命中「cause=Misunderstanding of force application」「correction=run in their lane and maintain their natural gait cycle」，与预期一致；并可交叉提示 hamstring 风险（ce20-05/Table 20.1）。输出明确诊断+纠正。
- **V3_task_utility**: passed: true — expected_benefit: 把「表象→成因→纠正」固化为排障清单，避免只改表象（如给「扒地」口令）而漏改发力机制，并显式关联腘绳肌损伤边界。
- **decision**: verified

---

## 能力单元 U6 — 速度手段选择与进阶（三级分类 + 进阶/退阶/变式 + 负荷规则）

- **proposed_capability_id**: cap.nsca.speed-method-progression
- **proposed_slug**: speed-method-selection-progression
- **type**: procedure
- **merged_candidates**: [p20-17, f20-06, p20-15, p20-16]
- **task_ids**: [T15, T16]
- **importance**: medium
- **source_evidence**:
  - source_id: src-nsca-essentials-5e
    location: 手段三级分类（ch20.txt 881–902 行）；variation/regression/progression（f20-06 对应段，A-skip/A-march 说明）；Table 20.2 助力与抗阻（950–1125 行）中超速 ≤10%（见 ~963/1041 行）与抗阻负荷 10%–12%/20%–30% BW（1086/1102 行）
- **R 段可用原文引用**（英文，逐字）:
  > "no exercise improves running velocity more than maximum-velocity sprinting (i.e., primary methods) ... resisted and assisted sprint training techniques are often employed (i.e., secondary methods) ... weightlifting movements and jump training are prescribed to develop RFD and impulse at varying loads ... (i.e., tertiary methods)." ... "track and field sprinters may use loads that do not decrease running velocity by more than 10% to 12% ... field sport athletes ... can use loads 20% to 30% of body weight to improve the initial 5-10 m of movement."
- **V1_source_sufficiency**: passed: true — 三级分类原文完整（881–902 行）；抗阻/助力负荷区间原文完整（p20-15 ≤10%、p20-16 10%–12% 与 20%–30% BW）；f20-06 的进阶/退阶/变式在原文 A-skip 段落有说明。**未解决项**：原文以区间给负荷，未给统一换算等式（p20-16 的 missing_condition 已如实记录）。
- **V2_executability**: passed: true
  - check_mode: walkthrough
  - input: 「场地项目运动员（橄榄球），需强化起步 5–10 m；教练拟用雪橇拖。某运动员 A-skip 时对侧摆臂失调。」
  - expected：① 手段定位=Secondary（抗阻冲刺），负荷取 20%–30% BW；② 若为田径短跑选手则改用「跑速下降 ≤10%–12%」定负荷；③ A-skip 问题→退阶用手放髋上先建立对侧摆臂，再进阶到 running form 强调抬腿。
  - observed: 按 p20-16/p20-15/p20-17 与 f20-06 给出明确负荷档位与退阶动作，输出为「手段分类 + 负荷取值 + 退阶动作」，可执行。
- **V3_task_utility**: passed: true — expected_benefit: 统一「主/次/三级手段」优先级与助力/抗阻负荷口径，防止把超速牵引或雪橇负荷用过头；并为任何速度敏捷练习提供统一的进阶/退阶旋钮。
- **decision**: verified

---

## 能力单元 U7 — 敏捷 drill 可操纵因素与知觉—认知进阶（含过渡移动）

- **proposed_capability_id**: cap.nsca.agility-drill-constraints
- **proposed_slug**: agility-drill-constraints
- **type**: framework
- **merged_candidates**: [f20-07, p20-30, f20-13, p20-31]
- **task_ids**: [T15, T16]
- **importance**: medium
- **source_evidence**:
  - source_id: src-nsca-essentials-5e
    location: Table 20.6 可操纵因素（ch20.txt 1813–1905 行）；Perceptual-Cognitive Ability 进阶段（1791–1811 行）；过渡移动技术清单 Figure 20.12（1422–1554 行）
- **R 段可用原文引用**（英文，逐字）:
  > "Temporal or time constraints can be administered (i.e., athlete has 5 s to achieve the objective) to maintain quality and intensity." ... "Backpedaling for 20 yards (18 m) along a marked line on the football field to establish correct technique ... Backpedaling while tracking an opponent who is initially running forward and then changing direction to sprint once the opponent initiates a COD or sprint."
- **V1_source_sufficiency**: passed: true — Table 20.6 机械四因素（间距/进出速度动量/动作与角度/起始姿势）+ 知觉认知六因素（攻防人数/时间约束/规则/环境地面/通用到专项刺激/任务复杂度）在 ch20.txt 完整；后撤跑四步进阶与侧滑步技术清单回查（1422–1554 行）与候选一致。
- **V2_executability**: passed: true
  - check_mode: walkthrough
  - input: 「一篮球运动员已熟练闭技能 Z-drill，拟提高其认知负荷并更贴近比赛。」
  - expected：按 Table 20.6 逐步加因素——先加通用刺激（口令/箭头）于 Z-drill；再加时间约束（如 5 s 内完成）；再加 defending/attacking 人数与专项刺激（真实对手/small-sided game）；同步可用 backpedal 四步进阶（静态技术→音频变速→口令变向→追踪对手启动变向）。
  - observed: 依两表可列出「机械旋钮 + 知觉认知旋钮」的组合序列，输出为 drill 设计参数与进阶路径，明确可执行。
- **V3_task_utility**: passed: true — expected_benefit: 把 drill 难度分解为可独立调节的旋钮，稳定地由闭技能 COD 过渡到反应性敏捷（呼应 ce20-04 的失败边界）。
- **decision**: verified

---

## 能力单元 U8 — 变向训练取向决策（角度/入速 → 快慢 SSC + GCT 基准）

- **proposed_capability_id**: cap.nsca.cod-angle-orientation
- **proposed_slug**: cod-angle-training-orientation
- **type**: decision
- **merged_candidates**: [f20-05, p20-08, p20-10, p20-09]
- **task_ids**: [T15, T16]
- **importance**: high
- **source_evidence**:
  - source_id: src-nsca-essentials-5e
    location: 75°/250 ms 规则（ch20.txt 1168–1197 行）；快/慢 SSC 分类（p20-08）；GCT 基准（p20-09，与 400–410 行敏捷/COD/冲刺触地时间对比一致）
- **R 段可用原文引用**（英文，逐字）:
  > "COD and agility movements performed at shallow cutting angles (less than 75 degrees) and associated with shorter ground contact times (less than 250 ms) benefit from training similar to speed training with regard to the physical demands but still require additional perceptual-cognitive training." ... "when a COD involves a more aggressive cutting angle (equal to or greater than 75 degrees), the length of ground contact time can often exceed 250 milliseconds."
- **V1_source_sufficiency**: passed: true — 75°/250 ms 与快慢 SSC 规则在 ch20.txt 1168–1197 行完整回查；GCT 基准值（敏捷 0.23–0.25 s、COD ~0.15–0.6 s、冲刺加速 0.17–0.2 s、最大速 0.09–0.11 s）与 p20-09 一致。作者已注明依赖入速与个体能力（边界清楚）。
- **V2_executability**: passed: true
  - check_mode: walkthrough
  - input: 「运动员以高速入速做 90° 切角变向。」
  - expected：判定 GCT 常 >250 ms → 偏慢 SSC → 训练重点=增强偏心力量（制动）+ 最大力量 + 再加速所需向心爆发力/reactive strength；对照浅切 30° 且 GCT<250 ms 时→接近速度训练但仍需补知觉—认知。
  - observed: 按 75°/250 ms 判据给出「偏心+最大力量+向心爆发」取向，并提示入速越高所需 impulse 越大（呼应 U2 的 braking impulse）。输出为明确训练取向。
- **V3_task_utility**: passed: true — expected_benefit: 用角度与触地时间两个可测变量统一「该练速度还是该练力量」的取向，改善决策结构。
- **decision**: verified

---

## 能力单元 U9 — 变向/敏捷技术诊断要点（视觉—躯干—腿—臂）

- **proposed_capability_id**: cap.nsca.cod-technique-diagnosis
- **proposed_slug**: cod-technique-diagnosis
- **type**: framework
- **merged_candidates**: [f20-14]
- **task_ids**: [T15]
- **importance**: medium
- **source_evidence**:
  - source_id: src-nsca-essentials-5e
    location: 变向技术要点（ch20.txt deceleration/躯干与腿部说明，对应 f20-14 引用段，约 1420–1560 行附近与 1159–1164 行 "Athletes improve COD ability through…" 框）
- **R 段可用原文引用**（英文，逐字）:
  > "Control the trunk leading into the deceleration (decrease large amounts of trunk motion). When decelerating, posterior trunk lean may assist in orienting the force vector posteriorly." ... "Ensure that the athlete can effectively dissipate or tolerate the eccentric braking loads through an effective range of motion at the hip, knee, and ankle (i.e., co-triple flexion) and avoid a stiff-legged braking style."
- **V1_source_sufficiency**: passed: true — 四观察维度（视觉聚焦/躯干姿态/腿部缓冲 co-triple flexion/摆臂）在原文有明确要点（co-triple flexion 与 stiff-legged 表述逐字命中）。注：f20-14 为唯一候选载体，但原文一处说明完整。
- **V2_executability**: passed: true
  - check_mode: walkthrough
  - input: 「运动员变向时直腿制动、躯干大幅转动，减速后无法快速再加速。」
  - expected：诊断=腿部未以髋膝踝共同屈曲缓冲（stiff-legged），躯干过度转动妨碍力向量后向定位 → 纠正=降低重心、减少躯干转动、后倾定向力向量、屈髋膝踝吸能。
  - observed: 四维度逐项对照得具体纠正要点，输出明确。
- **V3_task_utility**: passed: true — expected_benefit: 给出「看哪里、改什么」的技术检查表，避免只凭总体观感评价变向技术。
- **decision**: verified

---

## 能力单元 U10 — 速度/敏捷监控指标选择与解读

- **proposed_capability_id**: cap.nsca.speed-agility-monitoring
- **proposed_slug**: speed-agility-monitoring
- **type**: procedure
- **merged_candidates**: [f20-12, p20-22, p20-29]
- **task_ids**: [T15, T16]
- **importance**: medium
- **source_evidence**:
  - source_id: src-nsca-essentials-5e
    location: Table 20.8 速度监控（ch20.txt 2260–2330 行附近）；Table 20.12 敏捷/COD 监控（2539–2662 行）；触地时间解读（483–486 行、1168 行）
- **R 段可用原文引用**（英文，逐字）:
  > "decreased ground contact times coupled with improved sprint completion times may suggest that an athlete has improved the ability to generate high rates of force in a shorter amount of time. However, an athlete may demonstrate slightly longer ground contact times at the initial stages of the sprint due to acceleration mechanics." ... "Improved exit velocity with the same or faster ground contact times implies greater RFD relevant to improving COD ability."
- **V1_source_sufficiency**: passed: true — Table 20.8 变量（GCT、step/stride length、flight time、stride angle、speed、acceleration、technique）与 Table 20.12 变量（completion time、COD deficit、GCT、exit/entry velocity、decision-making time、phase-specific）及解读规则均回查原文（2260–2330、2539–2662 行）。工具要求（>100 fps 高速相机）原文明确。常模值未给（如实记录于表格 missing_condition）。
- **V2_executability**: passed: true
  - check_mode: walkthrough
  - input: 「某运动员 5-0-5 完成时间变慢，但 COD deficit 不变；另一运动员冲刺 GCT 缩短且完赛时间改善。」
  - expected：① 前者=完成时间受直线速度影响，COD 能力未退化（COD deficit 不变）；② 后者=单位时间发力能力（RFD）提升。若腾空时间增加，须结合步幅角与速度判断是「更短触地产生更高竖力」还是「竖直振幅过大」。
  - observed: 按 Table 20.8/20.12 解读规则得两条明确归因，输出为「进展归因+调整依据」。
- **V3_task_utility**: passed: true — expected_benefit: 统一监控指标口径与交叉验证解读规则，避免仅看完成时间误判进步来源。
- **decision**: verified

---

## 能力单元 U11 — 速度/COD/敏捷计划设计变量清单与 volume-load

- **proposed_capability_id**: cap.nsca.speed-agility-program-variables
- **proposed_slug**: speed-agility-program-variables
- **type**: checklist
- **merged_candidates**: [f20-15, p20-23]
- **task_ids**: [T15]
- **importance**: medium
- **source_evidence**:
  - source_id: src-nsca-essentials-5e
    location: "Program Design" 段与变量清单（ch20.txt 1906–1932 行起）；volume-load 例（p20-23 对应段）
- **R 段可用原文引用**（英文，逐字）:
  > "Angle—The intended angle for COM deflection ... Approach velocity—The horizontal entry velocity of the COM ... Work-to-rest ratio—The relative density of exercise and relief intervals in a set, expressed as a ratio." ... "Volume-load—the density of volume performed at prescribed intensities—for example, 3 sets of 5 repetitions at 100 kilograms results in a volume-load of 1,500 kilograms."
- **V1_source_sufficiency**: passed: true — 变量清单（angle、approach velocity、exercise/work interval、order、frequency、intensity、recovery、repetition、series、set、volume-load、volume、work-to-rest ratio）与 volume-load 算例均在原文完整（1906–1932 行及后随定义段）。作者强调变量耦合（原文 "each variable must be considered individually, and … how it affects the collective system"）。
- **V2_executability**: passed: true
  - check_mode: walkthrough
  - input: 「一次课 3 组 × 5 次 × 100 kg 的抗阻 + angle=90°、approach velocity=高的一组变向 drill。」
  - expected：volume-load = 3×5×100 = 1,500 kg；变向变量填入 angle 与 approach velocity 两项并说明其调节膝负荷；整体以 work-to-rest ratio 描述密度。
  - observed: volume-load 独立核算=1,500 kg（容差 0），变量清单可逐项填值，输出为「变量取值组合+负荷量化」。
- **V3_task_utility**: passed: true — expected_benefit: 为速度/COD/敏捷提供与抗阻训练同构的变量清单，统一负荷量化口径（volume-load）。
- **decision**: verified

---

## 能力单元 U12 — 敏捷发展多元方法框架（力量谱 + 闭技能技术 + 知觉认知）

- **proposed_capability_id**: cap.nsca.agility-multifactorial
- **proposed_slug**: agility-multifactorial-plan
- **type**: framework
- **merged_candidates**: [f20-10, p20-28]
- **task_ids**: [T15]
- **importance**: medium
- **source_evidence**:
  - source_id: src-nsca-essentials-5e
    location: "Methods of Developing Agility"（ch20.txt 1570–1602 行，含 Table 20.4）；"Training Goals"（1561–1569 行）
- **R 段可用原文引用**（英文，逐字）:
  > "The three goals to enhance agility performance through training are to develop the physical qualities to allow athletes to adopt the required postures and positions for a range of different agility movements performed in the sport as well as enhance braking and propulsion of such tasks (action capacity); to develop movement efficiency and competency of range of agility movements pertinent to the athlete's sport, and to enhance perceptual-cognitive ability in various situations and tactical scenarios."
- **V1_source_sufficiency**: passed: true — 三目标与「力量策略 + 闭技能 COD 技术 + 知觉认知」三线在原文完整；Table 20.4（新手/高级 × 力量室/场上）逐栏可回查（1603–1666 行）。原文并提示「体能先于技术、技术表现滞后」（1597–1601 行）。
- **V2_executability**: passed: true
  - check_mode: walkthrough
  - input: 「新手与高级运动员各一名，均需提高敏捷。」
  - expected：新手→力量室以体重动作/箱跳/次最大落地稳定为主，场上以身体意识与低强度减速；高级→力量室用深蹲/举重派生/强化离心，场上用多种角度 COD 与最大努力减速；两线之外都须补知觉—认知。
  - observed: 依 Table 20.4 与三线框架给出两份差异化方案，输出明确。
- **V3_task_utility**: passed: true — expected_benefit: 防止用单一手段（只做变向 drill）发展敏捷，明确「体能先于技术」的进阶次序。
- **decision**: verified

---

## 能力单元 U13 — 速度/SSC 训练目标与两判据

- **proposed_capability_id**: cap.nsca.ssc-speed-objectives
- **proposed_slug**: ssc-speed-training-criteria
- **type**: checklist
- **merged_candidates**: [p20-14, f20-11, p20-07]
- **task_ids**: [T15]
- **importance**: medium
- **source_evidence**:
  - source_id: src-nsca-essentials-5e
    location: 速度发展两大训练目标（ch20.txt 842–851 行）；SSC 两判据（p20-07/f20-11 对应 "Training activities aimed at improving SSC…" 段）
- **R 段可用原文引用**（英文，逐字）:
  > "Emphasize brief ground support times as a means of achieving rapid step rate ... Emphasize the further development of the SSC as a means to increase the amplitude of impulse for each step of the sprint." ... "Training activities aimed at improving SSC performance should fulfill two criteria: They should involve skillful, multijoint movements that transmit forces through the kinetic chain and exploit elastic–reflexive mechanisms." ... "they should be structured around brief work bouts or clusters separated by frequent rest pauses."
- **V1_source_sufficiency**: passed: true — 两大目标与两判据原文完整；手段提示（完整举重动作及派生 + plyometric、复合/对比训练）在原文有述。未给「短触地/高力」量化目标值（如实记录）。
- **V2_executability**: passed: true
  - check_mode: walkthrough
  - input: 「候选练习：① 单关节腿屈伸（慢速）；② 深蹲跳；③ 反向下蹲跳 + 短工作段多次组、频繁休息。」
  - expected：两判据筛选——②③ 通过（多关节、经动力链、弹反机制 + 短工作段/频繁休息），① 不通过（单关节、无 SSC）。
  - observed: 逐项对照两判据得明确通过/不通过，输出为符合条件的练习与组间安排。
- **V3_task_utility**: passed: true — expected_benefit: 把「SSC 该练什么、怎么排」变成可检验条件，识别不达标练习。
- **decision**: verified

---

## 能力单元 U14 — 冲刺速度两变量与常模（步长 × 步频）

- **proposed_capability_id**: cap.nsca.sprint-step-length-frequency
- **proposed_slug**: sprint-step-length-frequency
- **type**: framework
- **merged_candidates**: [f20-03, p20-11, p20-12]
- **task_ids**: [T15]
- **importance**: medium
- **source_evidence**:
  - source_id: src-nsca-essentials-5e
    location: 步长/步频与常模（ch20.txt 对应 p20-11/p20-12 段）；结论段（2674–2679 行 "Running speed is associated with the relationship between step length and rate."）
- **R 段可用原文引用**（英文，逐字）:
  > "sprint speed can be increased by an increase in step length or an increase in step frequency" ... "Elite male sprinters achieve a step length of 2.70 m (8.9 ft), whereas novice sprinters display a step length of 2.56 m (8.4 ft) at maximum velocity ... Elite male sprinters demonstrate step frequency near 4.63 steps per second compared to novice sprinters, who produce a lesser step frequency of 4.43 steps per second."
- **V1_source_sufficiency**: passed: true — 两变量框架与常模（步长 2.70/2.56 m；步频 4.63/4.43 步/s；最大速精英 11.0–12.5 m/s vs 团队运动 8.0–9.5 m/s）在原文回查。常模来自特定样本人群（Mann 2011），跨年代/性别/项目需重校验（如实记录于 missing_condition）。
- **V2_executability**: passed: true
  - check_mode: walkthrough
  - input: 「团队运动运动员最大速约 9.0 m/s，步长偏短、步频尚可。」
  - expected：定位其处于团队运动档（8.0–9.5 m/s），据此判断主限制=步长不足（对应底层力产生/力学效率）；干预方向=改善发力方向与 RFD，而非直接「迈大步」。
  - observed: 依常模定位水平并给出发力干预方向，输出明确（不要求跨领域）。
- **V3_task_utility**: passed: true — expected_benefit: 统一冲刺速度诊断口径（先看步长还是步频），并列常模用于水平定位。
- **decision**: verified

---

## 能力单元 U15 — 周期化概念迁移到速度/COD/敏捷

- **proposed_capability_id**: cap.nsca.periodization-transfer-speed
- **proposed_slug**: periodization-transfer-speed-agility
- **type**: framework
- **merged_candidates**: [f20-18]
- **task_ids**: [T15]
- **importance**: low
- **source_evidence**:
  - source_id: src-nsca-essentials-5e
    location: Ch20 "Program Design"（ch20.txt 1906–1923 行）
- **R 段可用原文引用**（英文，逐字）:
  > "Program design involves planning at several levels, each with its own set of considerations: microcycles (short term), mesocycles (medium term), and macrocycles (long term). The process is referred to as periodization." ... "Chapter 22 explains periodization of resistance training programs, and the same concepts can be applied to sprint, COD, and agility training."
- **V1_source_sufficiency**: passed: true — 原文确有该衔接声明（1906–1923 行）。但原文本身只给出「概念可迁移」的桥接陈述，未在 Ch20 内展开可独立执行的速度/COD/敏捷周期化步骤（实际 SOP 在 Ch22，属其他簇）。
- **V2_executability**: passed: false — 仅有一句「same concepts can be applied」，Ch20 未给速度/敏捷域专属的微/中/宏周期编排规则；按本单元自身无法生成具体动作/结果，需借 Ch22（其他簇）的流程。
- **V3_task_utility**: passed: true — expected_benefit: 作为跨章路由提示，告诉读者速度/敏捷的周期化应调用 Ch22 的 SOP，避免在 Ch20 内另起炉灶。
- **decision**: reference
- **if_not_verified**: 并入 `book/overview.md` 参考区（Ch20↔Ch22 桥梁句），并在 glossary 注明「速度/COD/敏捷的周期化编排以 Ch22 能力单元为准」。

---

## 覆盖核查表

| task_id | 任务 | 原文位置 | 对应候选 | decision | 去向 |
|---|---|---|---|---|---|
| T15 | 设计速度与敏捷训练计划（Table 20.6/20.7/20.9/20.11） | Ch20: 1906–2520 | U3(f20-04,p20-25/26/27,p20-32,c20-2/3/4), U4(f20-08,p20-24,c20-1/6), U6(p20-17,f20-06,p20-15/16), U7(f20-07,p20-30,f20-13,p20-31), U8(f20-05,p20-08/09/10), U11(f20-15,p20-23), U12(f20-10,p20-28), U13(p20-14,f20-11,p20-07), U14(f20-03,p20-11/12), U15(f20-18) | verified（U15=reference） | cap.nsca.agility-needs-to-program / speed-short-to-long-periodization 等 |
| T16 | 区分变向能力与敏捷，并按需选择训练手段（"COD deficit"等指标口径） | Ch20: 1140–1283, 1235–1243, 2350–2384 | U1(f20-01,p20-01,f20-16,p20-21,ce20-04), U2(f20-09,p20-19,p20-20,c20-5), U3(f20-04,p20-32,c20-2), U7(f20-07,p20-30), U8(f20-05,p20-08/09/10) | verified | cap.nsca.speed-cod-agility-attribution（专责判定）+ cap.nsca.speed-force-metrics |

> 说明：T15 的「设计完整速度/敏捷计划」由 U3（敏捷侧）+ U4（速度侧）两条可执行链共同覆盖，并以 U6/U7/U8/U11/U12/U13/U14 提供手段、进阶、取向、变量与常模支撑，故 task 层覆盖完整。

## 本簇缺口清单

- **RSI（reactive strength index）计量口径缺失**（用户特别提示的力学指标之一）：Ch20 仅有 "reactive strength development is also a key training priority"（第 1183–1186 行）等定性表述，**未给 RSI 公式与单位**。RSI 数值口径应属 Ch19（plyometric，其他簇）；本簇 U2 不含 RSI，勿用常识补公式。
- **impulse / momentum / COD deficit / sprint momentum 的 SI 单位**：原文未显式给出（N·s、kg·m/s），U2 已如实标注为待补规范项，进入阶段 2 的 B/E 段。
- **Table 20.8/20.12 各监控变量的常模/目标值**：原文未给，只能做「变化方向」解读，不能做「达标判定」；已记入 U10。
- **速度/COD/敏捷的域专属周期化步骤**：Ch20 未展开（U15 仅桥接语句），须依赖 Ch22（其他簇）；本簇不重复制造该 SOP。

## 供阶段 2 的提示

- **建议合并成卡片**：U3 + U4 + U11 可合成「速度与敏捷训练计划设计」主卡（同一 5-step→变量→分期结构，速度侧与敏捷侧各一套处方模板）；U1 + U2 建议合成「速度/变向/敏捷能力判定与力学口径」主卡（判定 + 指标计算互为依据，可独立回答「变向还是反应性敏捷」）。
- **A1 素材（重要 case，用户特别标注）**：
  - `c20-1`（Table 20.7 分块微周期样例）→ U4 的 A1。
  - `c20-2`（篮球需求分析 Table 20.9）→ U3 的 A1。
  - `c20-3`（Table 20.10 时间分配）与 `c20-4`（Table 20.11 三块处方）→ U3 的 A1/A2。
  - `c20-5`（COD deficit 算例）→ U2 的 A1（计算演练）。
  - `c20-6`（加速保持 40 m 例题）→ U4 的 A1。
- **B 段素材（反例）**：`ce20-01`（overstriding 源于错误引导）、`ce20-02`（摆臂越中线）、`ce20-03`（"扒地"错误口令）、`ce20-05`（骨盆前倾/overstriding → 腘绳肌损伤）→ U5 的 B 段；`ce20-04`（用 COD 冒充敏捷）→ U1 的 B 段。
- **E 段边界**：常模（步长/步频、最大速度）的人群/年代依赖（U14）；负荷区间（超速 ≤10%、抗阻 10%–12%/20%–30% BW）为经验值（U6）；75°/250 ms、45° 快慢 SSC 分界依赖入速与个体（U8）。
- **引用表**：U3 交付时须带 Table 20.9/20.10/20.11 原表数值；U4 须带 Table 20.7 四 block 原表数值；U8 须带 GCT 基准（敏捷 0.23–0.25 s / COD 0.15–0.6 s / 冲刺加速 0.17–0.2 s / 最大速 0.09–0.11 s）。


---

<!-- ===== 簇 E-aerobic ===== -->

# 簇 E-aerobic — 三重验证结果

- 负责任务: T17（有氧耐力计划设计 5 步变量）、T18（目标心率与强度分区计算）、T37（判断主导供能系统并设间歇比）
- 候选输入: 82 条（来自 `frameworks-g4-ch20-22.md`、`principles-g4-ch20-22.md`、`cases-g2-ch15-26.md`、`counter-examples-g2-ch15-26.md`、`frameworks-g6-ch01-12.md`、`principles-g6-ch01-04.md`、`cases-g1-ch01-14.md`）
- 归并后能力单元: 10 个（9 verified 单元 + 1 needs_review 单元）+ 5 组 reference 归并条目
- verified: 48 / reference: 31 / needs_review: 3 / rejected: 0

> 回查基准：`books/nsca-essentials-5e/.cangjie/source/ch21.txt`（主）、`ch03.txt`（T37）。

---

## 能力单元 U1 — 强度分区与目标心率计算（含监控方法选择）

- **proposed_capability_id**: cap.nsca.aerobic-intensity-zones-target-hr
- **proposed_slug**: aerobic-intensity-zones-target-hr
- **type**: calculation
- **merged_candidates**: [p21-02, p21-03, p21-04, p21-05, p21-06, p21-07, p21-08, p21-09, p21-24, p21-28, f21-02, c01-01, c01-02, c21-1, c21-2, c21-3, c21-4]
- **task_ids**: [T18]
- **importance**: critical
- **source_evidence**:
  - source_id: src-nsca-essentials-5e
    location: Chapter 21, "Step 3: Training Intensity" → "Target Heart Rate Calculations" sidebar（ch21.txt 第 402–557 行）；Table 21.1（第 378–400 行）；Table 21.2（第 464–490 行）；Table 21.3（第 576–597 行）；MET 段（第 599–611 行）；HR–VO2 有效区间（第 436–440 行）；三区/乳酸口径见 p21-03/p21-24（第 74–96、1990–2010 行语境）；c01-01/c01-02 来自 ch01.txt。
- **R 段可用原文引用**（英文，逐字）:
  > "Age-predicted maximum heart rate (APMHR) = 220 - age. Heart rate reserve (HRR) = APMHR - resting heart rate (RHR). Target heart rate (THR) = (HRR × exercise intensity) + RHR. ... Lowest number of the athlete's THRR = (130 × 0.60) + 60 = 78 + 60 = 138 beats/min; Highest number of the athlete's THRR = (130 × 0.70) + 60 = 91 + 60 = 151 beats/min."
- **V1_source_sufficiency**: passed: true — 两套目标心率公式（Karvonen/%HRR 与 %MHR）、两处完整算例、五区标尺（Table 21.1 逐格值）、VO2max–HRR–MHR 对照（Table 21.2 逐行值）、RPE 1–10 全表（Table 21.3）、MET 定义（1 MET = 3.5 ml·kg⁻¹·min⁻¹）均一次完整给出；APMHR 精度告警（SD 10–12 bpm；Fox 方程）与 HR–VO2 仅在 50–90% 功能容量区间有效的边界亦在原文。已回查 ch21.txt 第 523–550 行核对公式与两个算例，逐字一致。
- **V2_executability**: passed: true
  - check_mode: walkthrough
  - input: (A) Karvonen：40 岁、RHR 55、处方 70–80% 功能容量；(B) %MHR：25 岁、处方 70–85% 最大心率；(C) MET：某活动 MET = 8。
  - expected: (A) APMHR=180、HRR=125、下限 (125×0.70)+55=142.5→≈143、上限 (125×0.80)+55=155 → THRR ≈ 143–155 次/分；(B) APMHR=195、下限 195×0.70=136.5→≈137、上限 195×0.85=165.75→≈166 → THRR ≈ 137–166 次/分；(C) VO2 = 8×3.5 = 28 ml·kg⁻¹·min⁻¹。
  - observed: 纸面演练全部产生明确数值：(A) 143–155、(B) 137–166、(C) 28 ml·kg⁻¹·min⁻¹。交叉验算（用 Table 21.2 把 (A) 的 70–80% HRR 换算为 %MHR）：70–80% HRR ↔ 81–88% MHR → 180×0.81=145.8 至 180×0.88=158.4，即 %MHR 法口径约 146–158，与 Karvonen 的 143–155 **不相同但相邻**——正说明两法不可互换，须标明所用方法。
- **V3_task_utility**: passed: true — expected_benefit: 统一"相对强度→绝对心率"的换算口径，避免把 %MHR 与 %HRR 混用（两者在同一处方百分比下差异可达 10 次/分以上）；给出一张可直接照做的换算与查表链，并在无实验室数据时明确误差带与适用区间。
- **decision**: verified
- **if_not_verified**: —

---

## 能力单元 U2 — 有氧耐力训练计划 5 步设计变量与训练类型处方

- **proposed_capability_id**: cap.nsca.aerobic-program-design
- **proposed_slug**: aerobic-program-design-five-variables
- **type**: procedure
- **merged_candidates**: [f21-01, p21-01, f21-04, p21-10, p21-14, p21-15, p21-16, p21-17, p21-18, f21-15, p21-27]
- **task_ids**: [T17]
- **importance**: high
- **source_evidence**:
  - source_id: src-nsca-essentials-5e
    location: Chapter 21, "Aerobic Training Program Design Variables"（ch21.txt 第 236 行）5 个 Step；Table 21.4（第 788–817 行）；Extensive endurance（第 818–891 行）；Pace/Tempo（第 893–900 行）；Interval（第 926–935 行）；HIIT/Tabata（第 947–969 行）；Fartlek（第 997 行语境）；强度—时长反比（第 695–697 行）。
- **R 段可用原文引用**（英文，逐字）:
  > "Extensive endurance 1-2 Race distance or longer (~30-120 min) ≤65% of VO2max; Pace/tempo 1-2 ~20-30 min At the LT; at or slightly above race pace; Interval 1-2 3-5 min (with a work:rest ratio of 1:1) Close to VO2max; High-intensity interval training 1 30-90 s (with a work:rest ratio of 1:5) Greater than VO2max; Fartlek 1 ~20-60 min Varies between LSD and pace/tempo training intensities."
- **V1_source_sufficiency**: passed: true — 5 个设计变量（mode/frequency/intensity/duration/progression）在原文逐条列出；Table 21.4 五类训练各给"频率/工作段时长/强度"完整处方，正文另给每类的执行规则（interval 3–5 min 休息=工作段 W:R=1:1 且需先建基础；HIIT/Tabata 20 s/10 s×7–8、长间歇 ≥2–3 min@≥90% VO2max；pace/tempo 近似 MLSS、轻松则加距离不加强度；extensive endurance 距离>比赛距离或 ≥30 min–2 h、Zone 2、优先加时长）。已回查 Table 21.4 原表（第 791–812 行）逐格核对，与候选一致；强度—时长反比（第 695–697 行）核对一致。
- **V2_executability**: passed: true
  - check_mode: walkthrough
  - input: 中级 10 km 跑者、赛前晚期、每周可练 6 天。
  - expected: 给出五变量取值：mode=跑；frequency=由训练状态/赛季定；intensity=以 LT/VO2max 分区锚定；duration=按强度反比取；progression=≤10%/周；并按 Table 21.4 组合训练类型（extensive endurance 1–2 次 ≤65% 30–120 min；pace/tempo 1–2 次 20–30 min@LT；interval 1–2 次 3–5 min@接近 VO2max W:R=1:1；HIIT 1 次 30–90 s W:R=1:5），其余日为低强度/恢复。
  - observed: 纸面演练产出完整处方骨架。交叉核对 c21-8（同一情境的样例周：周一 10×0.5 km@比赛配速 1:1；周二 10 km easy；周四 HIIT 3 min@90% VO2max/2 min×6；周六 45 min Fartlek）与 U2 推导的类型/参数一致，说明流程可落地。
- **V3_task_utility**: passed: true — expected_benefit: 把"有氧怎么练"从'只堆 LSD'扩展为可复制的 5 变量 + 5 类型处方；统一每类的频率/时长/强度/间歇口径，减少遗漏训练类型与参数漂移。
- **decision**: verified
- **if_not_verified**: —

---

## 能力单元 U3 — 有氧进阶规则（≤10%/周、单变量、按时间非距离）

- **proposed_capability_id**: cap.nsca.aerobic-progression-rule
- **proposed_slug**: aerobic-progression-10pct-single-variable
- **type**: procedure
- **merged_candidates**: [f21-06, p21-12, p21-13, c21-10]
- **task_ids**: [T17]
- **importance**: high
- **source_evidence**:
  - source_id: src-nsca-essentials-5e
    location: Chapter 21, "Step 5: Exercise Progression"（ch21.txt 第 699–775 行）；维持/提升频率（第 297–298、703–705 行）。
- **R 段可用原文引用**（英文，逐字）:
  > "exercise frequency, intensity, or duration should not increase more than 10% each week to avoid overtraining or injury ... only one training variable should be increased at a time. ... it is often recommended to use predicted time to set the duration of a training session rather than distance. This is because training time factors in the effects of terrain and environmental conditions, whereas distance does not."
- **V1_source_sufficiency**: passed: true — 三条规则一次完整：≤10%/周（并给出新手/低冲击可例外的边界与"必须先建立生理+心理过度训练监控"的前置条件）、一次只加一个变量、按预测时间而非距离设时长；并含 3 个数值算例（新手跑者 +0.3 mi；骑行者 +1.25–2.5 mi；10 mi→11 mi 山地方案时间 +65%）；另有维持规则（强度维持时降至 2 次/周可维持 ≤5 周；>2 次/周方能提升 VO2max）。已回查第 709–757、1092–1118 行核对，逐字一致。
- **V2_executability**: passed: true
  - check_mode: walkthrough
  - input: 中级跑者本周总量 40 km（单一变量=时长）；另一情境：平路 10 mi 用时 70 min，次周拟改 11 mi 山地路线。
  - expected: 本周→次周增量 ≤ 40×1.10 = 44 km，且只调时长；山地情境判定为不合规（距离仅 +10%，但时间 118 min → +48 min = +65% > 10%）。
  - observed: 纸面演练得出 44 km 上限、并正确拒绝山地 11 mi 方案（应按时间递增至 ≤77 min）。
- **V3_task_utility**: passed: true — expected_benefit: 用一条可检查的增幅上限 + 单变量 + 时间基准，避免"距离+10% 而实际负荷+65%"这类隐蔽过载；给出超限的前置条件，识别失败边界。
- **decision**: verified
- **if_not_verified**: —

---

## 能力单元 U4 — 由专项主导供能系统推导间歇训练比（T37）

- **proposed_capability_id**: cap.nsca.energy-system-interval-ratio
- **proposed_slug**: energy-system-to-interval-ratio
- **type**: procedure
- **merged_candidates**: [f03-01, p03-01, p03-06, p03-07]
- **task_ids**: [T37]
- **importance**: medium
- **source_evidence**:
  - source_id: src-nsca-essentials-5e
    location: Chapter 3 · Bioenergetics, Table 3.2（ch03.txt 第 703–717 行）；Table 3.6（第 1184–1196 行）；强度为主/时长为次（第 926–934 行语境，见 ch03.txt）；间歇与 CP 再合成（第 1106–1196 行）。
- **R 段可用原文引用**（英文，逐字）:
  > "90-100 % of maximum power → Phosphagen → 5-10 s → 1:12 to 1:20; 75-90 → Fast glycolysis → 15-30 s → 1:3 to 1:5; 30-75 → Fast glycolysis and oxidative → 1-3 min → 1:3 to 1:4; 20-30 → Oxidative → >3 min → 1:1 to 1:3."（Table 3.6）"the relationships ... assume that the athlete strives to attain the best possible performance for a given event"（Table 3.2 note）
- **V1_source_sufficiency**: passed: true — 判定链完整：Table 3.2 由"事件时长×强度"给出主导供能系统；Table 3.6 由"%最大功率/主导系统"给出典型工作时长与工作-休息比档位；并有方向规则（强度越高、时长越短→工作-休息比越大）与机制说明（CP 半时约 30 s、完全再合成 3–5 min 可至 8 min）。已回查 ch03.txt 第 703–717、1184–1196 行逐字核对。**V1 冲突/边界（如实记录，不阻断）**：原文自认"more research is necessary to provide evidence-based recommendations for optimal work-to-rest ratios"（第 1181–1182 行），故 Table 3.6 仅为"基于代谢时程的一般性指引"，其数值不可当作循证最优值使用——此点应在能力卡的 B 段显式保留。
- **V2_executability**: passed: true
  - check_mode: walkthrough
  - input: (A) 篮球专项，需反复约 4 s 最大冲刺；(B) 200 m 冲刺约 25 s。
  - expected: (A) 4 s、极高强度→Table 3.2 主导=磷酸原→Table 3.6：90–100% 最大功率、工作时长 5–10 s、工作-休息比 1:12–1:20；(B) 25 s、高强度→主导=磷酸原+快速糖酵解→75–90% 最大功率、15–30 s、工作-休息比 1:3–1:5。
  - observed: 纸面演练给出 (A) 5–10 s 工作 + 1:12–1:20 休息、(B) 15–30 s 工作 + 1:3–1:5，均明确可核对。
- **V3_task_utility**: passed: true — expected_benefit: 把"间歇比怎么定"从经验偏好变成"项目代谢画像→查表"的可复制推导；统一时长/强度/间歇三口径；并在原文自认循证不足处显式标注失败边界，防止把一般指引当最优处方。
- **decision**: verified
- **if_not_verified**: —

---

## 能力单元 U5 — 同期（有氧+抗阻）训练处理

- **proposed_capability_id**: cap.nsca.concurrent-training-management
- **proposed_slug**: concurrent-aerobic-resistance-training
- **type**: procedure
- **merged_candidates**: [f21-10, p21-20, p03-18]
- **task_ids**: [T17]
- **importance**: high
- **source_evidence**:
  - source_id: src-nsca-essentials-5e
    location: Chapter 21, "Concurrent Aerobic Endurance Training and Resistance Training"（ch21.txt 第 1359–1511 行，含 Exercise Selection / Training Intensity and Frequency / Recovery Time / Training Sequence）；Ch3 干扰规则（p03-18，ch03.txt）。
- **R 段可用原文引用**（英文，逐字）:
  > "keep the loads high (e.g., ≥90% of 1RM or ≤4RM) but the weekly volume low ... athletes who have benefited from concurrent training used free weight, multijoint exercises ... The training sequence should be varied throughout the phases of the training year ... the most important training goal should be trained first within a given workout while the athlete is fresh."
- **V1_source_sufficiency**: passed: true — 处方要点完整（自由重量多关节动作 + 快速/快速伸缩复合；重负荷低周量；每周 2–3 次；顺序随阶段变化、当期最高优先在体力充沛时先做；模式影响恢复[跑步>骑行肌损伤]；低训练状态者需更长恢复/更慢进阶；准备期力量可以每周 1 次维持 ≤12 周）。抗阻干扰规则（Ch3：有氧可能削弱高力量/高功率增益）作为边界补充。已回查第 1412–1441、1463–1511 行核对。
- **V2_executability**: passed: true
  - check_mode: walkthrough
  - input: 大学 5 km 越野跑者、赛季期，需同时维持力量与耐力。
  - expected: 抗阻≥90% 1RM 或 ≤4RM、周量低、2–3 次/周；选自由重量多关节 + 跳类；课上先做当期最高优先项（如赛季初先抗阻）；跑步课与抗阻课分开或按模式留足恢复。
  - observed: 纸面演练产出可执行的周安排；与 c22-1（Ch22 样例跨季维持）逻辑一致。
- **V3_task_utility**: passed: true — expected_benefit: 提供可复制的"如何合并不打架"参数组合，减少有氧/抗阻互相干扰；统一顺序与量-强口径。
- **decision**: verified
- **if_not_verified**: —

---

## 能力单元 U6 — 赛前减量（tapering）模型选择

- **proposed_capability_id**: cap.nsca.tapering-model
- **proposed_slug**: aerobic-tapering-models
- **type**: procedure
- **merged_candidates**: [f21-09, p21-19]
- **task_ids**: [T17]
- **importance**: high
- **source_evidence**:
  - source_id: src-nsca-essentials-5e
    location: Chapter 21, "Tapering"（ch21.txt 第 1328–1357 行）。
- **R 段可用原文引用**（英文，逐字）:
  > "The most common tapering models are linear, step, and progressive tapers. The linear taper is characterized by a gradual decrease in the overall daily training volume ... a step taper is typified by an abrupt and considerable reduction (normally ≥50%) in training volume ... a progressive taper uses a combination of the linear and step tapering models ... a rapid 10% to 15% immediate reduction in training volume, with smaller, more gradual reductions in volume at each tier."
- **V1_source_sufficiency**: passed: true — 三种模型一次讲清，并给时长区间（典型 7–28 天）、共同原则（系统性降"训练量"，维持"强度与频率"）、目的（比赛时达峰）与配套（强化技术与营养）。已回查第 1345–1357 行逐字核对。
- **V2_executability**: passed: true
  - check_mode: walkthrough
  - input: 马拉松跑者、距主要比赛 14 天、拟用 progressive taper。
  - expected: 定 14 天减量期；即时降量 10%–15%，随后每档更小幅递减；全程维持强度与频率；强化技术与营养。
  - observed: 纸面演练给出"14 天、首档 -10~15%、逐档递减、强度频率不变"的明确方案。
- **V3_task_utility**: passed: true — expected_benefit: 把"减量"从模糊的'少练点'变成可选模型 + 明确降量口径；避免误把强度也降掉（减量只减量不减强度）。
- **decision**: verified
- **if_not_verified**: —

---

## 能力单元 U7 — 热适应（heat acclimation）方案

- **proposed_capability_id**: cap.nsca.heat-acclimation
- **proposed_slug**: heat-acclimation-protocol
- **type**: procedure
- **merged_candidates**: [f21-11, p21-21]
- **task_ids**: [T17]
- **importance**: medium
- **source_evidence**:
  - source_id: src-nsca-essentials-5e
    location: Chapter 21, "Heat Acclimation / Heat Acclimation Protocols"（ch21.txt 第 1546–1630 行）。
- **R 段可用原文引用**（英文，逐字）:
  > "Heat acclimation protocols are typically classified as short (<7 days), medium (8-14 days), or long term (>15 days) ... the majority (~75%) of heat adaptations occur within the first four to six days ... it is generally recommended that athletes aim for 60 minutes of heat exposure ... and a maximum of 90 minutes, although 120 minutes has been shown to be effective ... it is recommended that the environment have a wet-bulb globe temperature >30 °C."
- **V1_source_sufficiency**: passed: true — 时长分类、适应时程（~75% 在前 4–6 天）、单次暴露 60/90/120 min、WBGT>30 °C、被动热暴露 30 min、频率规则（连续日更快；10–14 天协议缺 1–3 天影响不大；每天两次不优于一次）、监控（短期用心率/成绩会误导，宜用 RPE）、正向适应标志（同负荷下心率与核心体温下降、出汗率上升、有氧能力提升）均完整给出。已回查第 1571–1626 行核对。**注意**：被动热暴露 30 min 见候选 f21-11 概括，原文 ch21.txt 段落对"30 min"未在该区间直接出现，需在阶段 2 回查 Ch6 热适应节确认（记为本单元一个待补读点，但不影响主流程）。
- **V2_executability**: passed: true
  - check_mode: walkthrough
  - input: 运动员 10 天后在约 36 °C 环境比赛、当前未适应。
  - expected: 选"中期 8–14 天"协议；单次目标 60 min（最多 90）；环境 WBGT>30 °C；必要时加被动热暴露；用 RPE 监控、以同负荷心率/核心体温下降与出汗率上升判定适应；起训时先降低时长/强度再渐进建立。
  - observed: 纸面演练给出"8–14 天、60 min/次、WBGT>30 °C、RPE 监控"的明确方案与判据。
- **V3_task_utility**: passed: true — expected_benefit: 把"去热适应"落成有时长/环境/监控标量的协议，并明确短期用心率/成绩会误导，识别失败边界。
- **decision**: verified
- **if_not_verified**: —（被动热暴露 30 min 值转阶段 2 回查 Ch6）

---

## 能力单元 U8 — 高原训练方案（含 LHTL）

- **proposed_capability_id**: cap.nsca.altitude-lhtl
- **proposed_slug**: altitude-training-lhtl
- **type**: procedure
- **merged_candidates**: [f21-14, p21-22]
- **task_ids**: [T17]
- **importance**: medium
- **source_evidence**:
  - source_id: src-nsca-essentials-5e
    location: Chapter 21, "Altitude"（ch21.txt 第 1512–1545 行）。
- **R 段可用原文引用**（英文，逐字）:
  > "Altitude is classified into several categories ... low (>500-2,000 m ...), moderate (>2,000-3,000 m ...), high (>3,000-5,500 m ...), and extreme (>5,500 m) ... an athlete must receive a hypoxic dose of training ≥12 hours per day for a minimum of three weeks at moderate altitude (approximately 2,100-2,500 m) ... Live high, train low (LHTL) ... requires individuals to live at moderate altitudes, between 2,000 meters and 3,000 meters, and train at or near sea level."
- **V1_source_sufficiency**: passed: true — 海拔分级、有氧表现下降起点（约 700 m）、适应时程（≤2,300 m 约 12–14 天，可至数月）、增益的缺氧剂量（≥12 h/天、≥3 周、约 2,100–2,500 m）、LHTL 参数（住 2,000–3,000 m、在/近海平面训练）均完整。已回查第 1513–1545 行逐字核对。
- **V2_executability**: passed: true
  - check_mode: walkthrough
  - input: 海平面训练的跑者、6 周后在约 2,200 m 比赛。
  - expected: 判定需否高原增益→选 LHTL：住在 2,000–3,000 m、在/近海平面训练；缺氧剂量 ≥12 h/天、≥3 周、中海拔约 2,100–2,500 m；兼顾低海拔训练质量。
  - observed: 纸面演练给出明确 LHTL 方案参数。
- **V3_task_utility**: passed: true — expected_benefit: 把"要不要上高原/怎么上"落成海拔-剂量-时长三参数；统一 LHTL 口径。
- **decision**: verified
- **if_not_verified**: —

---

## 能力单元 U9 — 恢复会话（recovery session）使用规范

- **proposed_capability_id**: cap.nsca.recovery-session
- **proposed_slug**: aerobic-recovery-session
- **type**: procedure
- **merged_candidates**: [f21-13, p21-26, ce21-03]
- **task_ids**: [T17]
- **importance**: medium
- **source_evidence**:
  - source_id: src-nsca-essentials-5e
    location: Chapter 21, "Recovery From Training"（ch21.txt 第 360–377 行，"A recovery session should be just that..."）。
- **R 段可用原文引用**（英文，逐字）:
  > "A recovery session should be just that: a session with the intentional purpose of aiding recovery beyond that achievable via passive rest ... It is not designed to provide an extra training stimulus and definitely should not contribute to any further muscle damage. Therefore, the recovery session should be short in duration and of a low intensity (i.e., zone 1) ... an extensive aerobic endurance session or long, slow distance session should not be used as a recovery run, just because it is of a low intensity."
- **V1_source_sufficiency**: passed: true — 目的、强度（zone 1）、时长（short）、失效判据（不得造成进一步肌损伤、不得当额外刺激）、常见误用（长距离 LSD 不得当恢复跑）、结算口径（恢复课仍计入训练周期总量并须纳入监控）均完整。已回查第 360–377 行逐字核对。**边界**：原文未给"短"的具体分钟数（缺失阈值），故本单元只判"是否属于恢复课"，不给固定时长。
- **V2_executability**: passed: true
  - check_mode: walkthrough
  - input: 运动员赛/高强度课后疲劳，教练计划"明天来一次 60 min 慢跑当恢复"。
  - expected: 判定 60 min 长时慢跑**不属于**恢复课（性质量上近似 extensive endurance/LSD）→恢复课应为短时、Zone 1（约 60–72% HRmax）；且该次仍计入周总量。
  - observed: 纸面演练正确拒绝"60 min 慢跑作恢复"，输出"短时 Zone 1 恢复课"。
- **V3_task_utility**: passed: true — expected_benefit: 纠正"低强度=恢复"的常见混淆，给出可检查的判据（短+Zone 1+非 LSD+计入总量），识别失败边界。
- **decision**: verified
- **if_not_verified**: —

---

## 能力单元 U10 — 运动季节到有氧计划变量的映射（Table 21.5）

- **proposed_capability_id**: cap.nsca.aerobic-season-assignment
- **proposed_slug**: aerobic-season-program-assignment
- **type**: framework
- **merged_candidates**: [f21-05, p21-11, c21-11]
- **task_ids**: [T17]
- **importance**: high
- **source_evidence**:
  - source_id: src-nsca-essentials-5e
    location: Chapter 21, "Application of Program Design to ... seasons" + Table 21.5（ch21.txt 第 1012–1085 行）；正文季节目标（第 1086–1290 行）。
- **R 段可用原文引用**（英文，逐字）:
  > "Typically, the training year is divided into phases that include the off-season (sometimes called base training), preseason, in-season (sport competition), and postseason (active rest). Table 21.5 summarizes the main objectives and the typical program design assignments for each training season."（第 1016–1021 行）
- **V1_source_sufficiency**: passed: false（部分）— 赛季目标与变量方向的散文叙述可读且完整（off-season 建基础、长时低强、渐进增强度；preseason 逐步增强度、维持或减少时长、纳入各类刺激；in-season 维持专项因素、比赛前安排低强度短时课；postseason 低强度低量主动休息）。**但 Table 21.5 的 in-season 行在 ch21.txt（第 1035–1053 行）排版错位**：beginner in-season 的 Duration 列（Short(training)/Moderate/Race distance）与 Intensity 列（High(training)/Low or high/Moderate to high(racing)）被拆散到两个文本块，列对齐无法从抽取文本唯一确证；advanced in-season 行同样错位。off-season/preseason/postseason 行可读。此为由源头抽取造成的**未解决冲突**，按方法论"冲突未解决前转 needs_review"。
- **V2_executability**: passed: false
  - check_mode: walkthrough
  - input: 高级 10 km 跑者、in-season（比赛期）。
  - expected: 按 Table 21.5 查 advanced in-season 的频率/时长/强度三档值（5–6 次/周；Short(training)/Moderate/Race distance；Low(training)/Low or high/High(racing) 的精确对齐）。
  - observed: 频率 5–6 可读出；时长与强度三档的**列对齐无法从 ch21.txt 唯一确证**（候选 p21-11/c21-11 亦报告同一截断）→不产生可信的完整查表结果。
- **V3_task_utility**: passed: true — expected_benefit: 若能补全，将提供"赛季×训练状态→五变量档位"的查表键，直接服务 T17 的赛季化处方。
- **decision**: needs_review
- **if_not_verified**: 去向 needs_review。**具体缺口**：(1) 需以更高保真来源（原书 PDF 表格页 / 校对版 txt）重读 Table 21.5 的 in-season 行，确认 beginner 与 advanced 两行的 Duration/Intensity 各三档与列对应关系；(2) 确认 footnote a/b 差异。在缺口补齐前，仅"季节目标与变量方向"的散文结论可作为 overview 参考，不进入 active 能力池。同时 `c21-5`–`c21-9` 的样例周可作为补充旁证（见 R4）。

---

## Reference 归并条目（有来源价值，但不是可独立执行的方法 → overview / glossary）

### R1 — 有氧负荷的强度/剂量边界心智模型
- **merged_candidates**: [f21-03, f21-12, f21-16, p21-23]
- **source_evidence**: Ch21 "Minimum Effective Dose / Maximum Tolerated Dose"（ch21.txt 第 70–96 行）；"intensity too low / too high"（第 417–422 行）；强弱项聚焦（第 72–77 行）。
- **V1**: passed: true（概念与边界有原文依据）；**V2**: 降级 — 输出为"剂量定位/失效方向"的判断，无固定数值与判据分支，无法产生可核对的具体结果。**V3**: 作为 overview 的决策心智模型有增益。
- **decision**: reference → 并入 `book/overview.md`（有氧处方的风险—收益与失败边界小节）。作为 B 段素材：ce21-01、ce21-02。

### R2 — 交叉训练与停训（reduced-training 模式）
- **merged_candidates**: [f21-07, p21-25, f21-08]
- **source_evidence**: Ch21 "Cross-Training"（ch21.txt 第 1292–1310 行）、"Detraining"（第 1312–1326 行）。
- **V1**: passed: true（"维持 VO2max 需强度与时长等于主项；交叉训练不改善单项表现至同等幅度；停训应尽量保留主项并降频降强度，交叉训练仅部分减缓"）；**V2**: 降级 — "equal in intensity and duration" 无量化容差，输出不唯一。**V3**: overview 参考价值明确。
- **decision**: reference → 并入 `book/overview.md`（交叉训练/停训小节）。

### R3 — Ch3 纯生物能学机制（已被候选阶段剔除，本簇仅登记）
- **merged_candidates**: [p03-02, p03-03, p03-04, p03-05, p03-08, p03-09, p03-10, p03-11, p03-12, p03-13, p03-14, p03-15, p03-16, p03-17]
- **source_evidence**: ch03.txt Table 3.1/3.3/3.4/3.5 及 ATP/CP/糖原/乳酸/EPOC/hiit变量 段落。
- **V1**: passed: true（均有原文表/段依据）；**V2**: 降级 — 属量化机制口径（速率/容量排名、ATP 产量、糖原分解速率、底物偏好、乳酸阈数值、EPOC 决定、HIIT 九变量），非可独立执行处方流程；**V3**: 作为参考与术语口径有增益。
- **decision**: reference → 并入 `book/glossary.md`（生物能学口径区）与 `book/overview.md`（代谢特异性机制小节）。其中 p03-02（速率/容量反比）与 p03-16（HIIT 九变量）与 U4 有相邻，可在能力卡 A1 中引用但不单独成能力。

### R4 — 有氧样例训练周（case 支持材料）
- **merged_candidates**: [c21-5, c21-6, c21-7, c21-8, c21-9]
- **source_evidence**: Ch21 各类型训练后的 sample programs（ch21.txt）。
- **V1**: passed: true（作为支持材料）；**V2**: n/a（case 非可执行规则）；**V3**: 强 A1 素材价值（对应 U2 各情境）。
- **decision**: reference → 保留为 U2 的 A1 段素材（阶段 2 使用），并在 `book/overview.md` 登记样例周来源。

### R5 — 有氧训练反例素材（B 段）
- **merged_candidates**: [ce21-01, ce21-02, ce21-04, ce21-05, ce21-06]（ce21-03 已并入 U9）
- **source_evidence**: counter-examples-g2-ch15-26.md（Ch21 各节）。
- **V1**: passed: true（反例均有原文对应句）；**V2**: n/a；**V3**: B 段失败边界素材。
- **decision**: reference → 作为 U1–U9 的 B 段素材（照搬精英方案 / 迷信更多过载[→R1] / 周增幅>10% 与多变量并发[→U3] / 以距离定时长[→U3]）。

---

## 覆盖核查表

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

## 本簇缺口清单

1. **[T17 · 高] Table 21.5 in-season 行源抽取错位（U10 → needs_review）**：`ch21.txt` 第 1035–1053 行的 beginner/advanced in-season 行，其"时长"与"强度"列三档被拆到两个文本块，列对齐无法唯一确证。需高保真来源重读该表后才能恢复完整查表能力。off-season/preseason/postseason 行与"季节目标/变量方向"散文结论可读。
2. **[T17 · 中] 热适应被动暴露 30 min 值待回查 Ch6**：ch21.txt 热适应段未直接给出"被动热暴露 30 min"，该值来自候选 f21-11 的概括，阶段 2 应回查 Ch6《Heat Acclimatization》节确认（不影响 U7 主流程）。
3. **[T37 · 中] 间歇比的循证不足（已保留）**：ch03.txt 第 1181–1182 行原文自认"需更多研究给出最优工作-休息比的循证推荐"，Table 3.6 仅为一般性指引——已记入 U4 的 V1 与 B 段，不作为"最优处方"宣称。
4. **[本簇无可执行处方的边界项] R1/R2 已如实降级为 reference**（MED/MTD、交叉训练、停训），未用常识补造其量化阈值。

> T17/T18/T37 三个任务在本簇**均有对应候选**，无"其他簇负责"造成的空缺；唯一阻塞是 Table 21.5 的源保真问题（缺口 1）。

---

## 供阶段 2 的提示

- **建议组合成一张能力卡**：U1（强度分区与目标心率计算）作为 T18 的核心可独立成卡（calculation）；U2 + U3 + U10（若能补全）可组合为"有氧耐力计划设计"（procedure）；U4 独立成卡（T37，与 Ch3 代谢特异性挂钩）。U5–U9 体量小，建议作为"有氧计划变量与特殊情境"里的次级能力卡或并入 U2 的子段。
- **A1 可用素材**：U2 ← c21-5（初级马拉松休赛期）、c21-6（中级铁三游泳）、c21-7（初级骑行赛前）、c21-8（中级 10 km 赛前晚期）、c21-9（5 km 越野赛季）；U1 ← c21-1/c21-2（两法算例）、c01-01（HRmax 误差带）、c01-02（Fick→MET）。R4 全部样例周为 U2 的首选 A1。
- **B 段（失败边界）素材**：U1 ← ce21-01、ce21-02；U3 ← ce21-04、ce21-05、ce21-06；U9 ← ce21-03；U4 ← 原书"循证不足"告警；U1/U4 ← 环境（热/湿/海拔）使心率与摄氧量关系偏移。
- **需在阶段 2 显式写入 B 段**：①APMHR 个体误差 SD 10–12 bpm 与"估计式不含 LT 信息"；②%MHR 与 %HRR 不可混用；③Table 21.1 为挪威奥委会通用指南（Seiler 2010），跨项目迁移需校验；④Table 3.6 非循证最优值。


---

<!-- ===== 簇 F-preparation-technique ===== -->

# 簇 F-preparation-technique — 三重验证结果

- 负责任务: T19, T24, T25, T26
- 候选输入: 166 条（来自 frameworks-g2-ch15-17.md、principles-g2-ch15-17.md、cases-g2-ch15-26.md[c15-*/c16-*/c17-*]、counter-examples-g2-ch15-26.md[ce15-*/ce16-*/ce17-*]）
- 归并后能力单元: 15 个（U1–U10 为可执行单元；R11–R13 为参考单元；N14–N15 为待核查单元）
- verified: 9 / reference: 3 / needs_review: 3 / rejected: 0（单元级）
- 去重覆盖（候选级 rejected）: 13 条，见文末「去重说明」

---

## 能力单元 U1 — 准备活动设计（RAMP 三阶段 / 传统两阶段 + 时长时机 + CNS 预备）

- **proposed_capability_id**: cap.nsca.warmup-ramp
- **proposed_slug**: warmup-ramp-design
- **type**: procedure
- **merged_candidates**: [f15-01, f15-02, f15-03, f15-04, p15-01, p15-02, p15-03(rej), p15-04, p15-06, p15-07(rej), p15-08, p15-09, p15-10, p15-11, c15-1, c15-2, c15-4]
- **task_ids**: [T19]
- **importance**: high
- **source_evidence**:
  - source_id: src-nsca-essentials-5e
    location: Chapter 15, "Warm-Up" / RAMP 段（原文 ch15.txt 第 152–160、198–199、225–231、385–397 行）；Table 15.1（ch15.txt 第 327–383 行）；Table 15.2（第 542 行起）、Table 15.3（第 575 行起）
- **R 段可用原文引用**（英文，逐字）:
  > "is the raise, activate and mobilize, and potentiate (RAMP) protocol (51). ... raise, activate and mobilize, and potentiate are its three key phases. ... Typically, it should last between 10 and 20 minutes ... The warm-up should ideally end no more than 15 minutes before the start of the subsequent activity"
- **V1_source_sufficiency**: passed: true — 回查 ch15.txt：RAMP 三段定义（225–231）、总时长 10–20 min 与结束 ≤15 min（152–160）、potentiation 递进机制（385–397）、Table 15.1 RAMP 动作与组次（327–383）、Table 15.2/15.3 CNS 预备组合（542、575）均在原文完整给出。适用条件（活动性质/运动员特征/后勤）、输入、步骤、输出齐全；三段时长配比原文确实未给（仅总时长），已登记为边界而非缺口。
- **V2_executability**: passed: true
  - check_mode: walkthrough
  - input: 一名大学篮球运动员赛前热身（目标：提升纵跳与变向）；场地有锥桶、弹力带、栏架、药球；距比赛 12 min。
  - expected: 产出覆盖三段的完整热身结构，总时长 ≤20 min，结束距比赛 ≤15 min；Raise 用模拟专项的低强度位移动作、Activate&Mobilize 用深蹲/弓步/髋动态模式、Potentiate 用跳跃/冲刺递进到接近比赛强度；若需 CNS 预备，可从 Table 15.2 取"后蹲 60%–90%1RM×1–3 组×1–3 次→CMJ（休息 3–12 min）"。
  - observed: 依 ch15 三段定义与 Table 15.1 可拼出完整三段序列（慢跑/ankling→弹力带 Y's&T's、弓步过顶侧伸、蜘蛛爬→箱式蹲跳 2×6、反向纵跳 2×6、高栏跳 2×3），并落定 10–20 min 与"结束距活动 ≤15 min"约束；Table 15.2 组合可直接套用。结果明确。
- **V3_task_utility**: passed: true — expected_benefit: 统一热身"该覆盖什么"的口径（四渐进过程 + RAMP 三段），避免遗漏 potentiation 阶段与结束时机；把 Table 15.1/15.2/15.3 作为可复制交付格式，减少重复编排。
- **decision**: verified
- **if_not_verified**: —

---

## 能力单元 U2 — 柔韧训练编程（静态/动态/PNF 选择与参数）

- **proposed_capability_id**: cap.nsca.flexibility-programming
- **proposed_slug**: flexibility-programming
- **type**: procedure
- **merged_candidates**: [f15-06, f15-07, f15-08, f15-09, f15-10, f15-11, f15-12, f15-13, f15-14, p15-05, p15-12, p15-14, p15-15, p15-16, p15-17, p15-18, p15-19, p15-20, p15-21, p15-22, p15-23, c15-3, ce15-01, ce15-02, ce15-03, ce15-04, ce15-05, ce15-06, ce15-07]
- **task_ids**: [T19]
- **importance**: high
- **source_evidence**:
  - source_id: src-nsca-essentials-5e
    location: Chapter 15, 静态拉伸（ch15.txt 第 815、1072–1074、1169 行）；PNF（第 952、1826–1831 行）；动态拉伸/弹震（相关段落）；技术清单（第 1126、1455、1812 行）
- **R 段可用原文引用**（英文，逐字）:
  > "A static stretch involves a slow and constant movement toward the end position, which is then held for 10 to 30 seconds (66). ... 15 to 30 seconds is generally recommended (81) ... When using static contractions, these should be held for approximately 3 to 6 seconds at no more than 20% of maximum voluntary contraction ... Contractions are typically sustained for 6 to 10 seconds."
- **V1_source_sufficiency**: passed: false — 回查确认原文**自相矛盾**（非候选误引）：
  - 静态拉伸保持时长：ch15.txt 第 815 行"held for 10 to 30 seconds"；第 1072–1073 行"15 to 30 seconds is generally recommended"；第 1169 行（静态拉伸指南框）"Hold stretches for 15 to 30 seconds"。同一书内 10–30 s 与 15–30 s 并存。
  - PNF 收缩参数：ch15.txt 第 952–953 行（正文）"3 to 6 seconds at no more than 20% of maximum voluntary contraction"；第 1827 行（PNF 指南框）"Contractions are typically sustained for 6 to 10 seconds"（且指南框只说"moderate intensity"，未给 %MVC）。
  - 结局：核心处方参数存在两处口径冲突且原文未澄清适用边界 → 依方法论"存在冲突时保留冲突及定位，未解决之前转 needs_review"。
- **V2_executability**: passed: false
  - check_mode: walkthrough
  - input: 为一名需要提升静态 ROM 的体操运动员设计一次 PNF hold-relax 拉伸（腘绳肌）。
  - expected: 应能给出确定的收缩时长、强度、被动拉伸时长、组次与频率。
  - observed: 可确定的部分——被动预拉伸 10 s、被动拉伸 30 s、组间休息 30 s、每拉伸 2–4 次、每周 1–2 次（第 952、1828–1830 行一致）。**无法确定**的部分——等长收缩时长到底取"3–6 s"还是"6–10 s"；强度到底取"≤20% MVC"还是"中等强度（无数值）"。因原书自身冲突，无法在**不补造**的前提下给出唯一参数 → 不通过。
  - 若 false：缺"以正文口径还是指南框口径为准"的裁定规则；需阶段 2 前回读该书对应位置或由领域专家裁定。
- **V3_task_utility**: passed: true — expected_benefit: 统一"按目标选拉伸方法（动态热身 / 静态或 PNF 提 ROM）"的决策，并把频率优先于时长、避免触发牵张反射等规则固化，减少误用。任务增益成立，但受 V1/V2 阻断。
- **decision**: needs_review
- **if_not_verified**: needs_review → 需回读/裁定静态拉伸保持时长（10–30 s vs 15–30 s）与 PNF 收缩参数（3–6 s/≤20% MVC vs 6–10 s/中等强度）的适用边界；未裁定前不进入 active 能力池。可确定的部分（方法选择、时机、频率优先级、PNF 三技术三相框架）可作参考附于能力卡 B 段。

---

## 能力单元 U3 — 动作技术基本规范（握法 / 身体位置 / 呼吸 / Valsalva）

- **proposed_capability_id**: cap.nsca.exercise-technique-basics
- **proposed_slug**: exercise-technique-basics
- **type**: framework
- **merged_candidates**: [f16-01, f16-02, f16-03, f16-04, f16-05, f16-13, p16-01(rej), p16-02, p16-03(rej), p16-04(rej), p16-05, p16-06, p16-07(rej), p16-08(rej), p16-18, c16-1, ce16-01, ce16-02, ce16-08, ce16-09]
- **task_ids**: [T24]
- **importance**: high
- **source_evidence**:
  - source_id: src-nsca-essentials-5e
    location: Chapter 16, "Stable Body and Limb Positioning"（ch16.txt 第 97–106 行五点接触位）、握法/握距段、呼吸段（第 167–173 行 Valsalva）
- **R 段可用原文引用**（英文，逐字）:
  > "achieve a five-point body contact position: 1. Head is placed firmly on the bench or back pad. ... 5. Left foot is flat on the floor. ... This is why the breath-holding phase is—and should—be quite transient, only about 1 to 2 seconds (at most). Even a very well-trained individual should not extend the length of the breath-holding phase, because blood pressure can quickly rise to triple resting levels."
- **V1_source_sufficiency**: passed: true — 回查 ch16.txt：五点接触位（97–106 行，逐条列出并说明"建立并全程维持"）、站姿脚位与器械轴对齐（109–115 行）、Valsalva 适用条件与 1–2 s 上限（167–173 行）。握法（pronated/supinated/neutral/alternated/hook + closed/false）、握距（common/wide/narrow；clean/snatch grip）与呼吸（粘滞点呼气、离心吸气）在原文完整给出。适用条件、步骤、输出齐全；"慢而受控的具体秒数"与"爆发动作目标速度值"原文未给（已登记边界）。Valsalva 缺"大负荷"量化阈值（另见 U4 同类缺口）。
- **V2_executability**: passed: true
  - check_mode: walkthrough
  - input: 一名有经验运动员做杠铃平板卧推 3×5 @ 85% 1RM。
  - expected: 起始位建立并全程维持五点接触（头/肩与上背/臀/左右脚）；呼吸在粘滞点（向心初段）呼气、离心吸气；因属结构类大负荷且运动员有经验，可短暂使用 Valsalva 且闭气 ≤1–2 s。
  - observed: 依 ch16 可逐条落定 setup、呼吸时相与 Valsalva 判断，产出明确执行规范。结果确定。
- **V3_task_utility**: passed: true — expected_benefit: 把"握法选择—稳定体位—呼吸时相—Valsalva 判据"固化为可检查清单，统一教学口径并识别失败边界（如非结构类/新手不应延长闭气）。
- **decision**: verified
- **if_not_verified**: —

---

## 能力单元 U4 — 护腰（weight belt）使用判据

- **proposed_capability_id**: cap.nsca.weight-belt-decision
- **proposed_slug**: weight-belt-decision
- **type**: framework
- **merged_candidates**: [f16-06, p16-09(rej), ce16-03]
- **task_ids**: [T24]
- **importance**: high
- **source_evidence**:
  - source_id: src-nsca-essentials-5e
    location: Chapter 16, "Weight Belts"（ch16.txt 第 192–199 行）
- **R 段可用原文引用**（英文，逐字）:
  > "It is recommended that a weight belt be worn for exercises that place stress on the lower back and during sets that use near-maximal or maximal loads. ... A drawback to weight belt use is that wearing a belt too often reduces opportunities for the abdominal and lower back muscles to be trained. ... no weight belt is needed for exercises that do not stress the lower back."
- **V1_source_sufficiency**: passed: true — 回查 ch16.txt 第 194–198 行，双条件判据（下背受应力 + 接近最大/最大负荷）与 drawback 均在原文完整给出。**缺口**：原文未给"接近最大/最大"的 %1RM 量化阈值，也未量化"轻负荷"（f16-06/p16-09 已登记）。但判据对清晰情形可产生明确决策，规则本身完整。
- **V2_executability**: passed: true
  - check_mode: walkthrough
  - input: 情形A——杠铃弯举 4×8RM（不给下背施压）；情形B——后蹲 3×3 @ 90%1RM（给下背施压且接近最大）。
  - expected: A 不戴护腰；B 戴护腰。
  - observed: 依双条件判据，A 不满足"下背受应力"→不戴；B 两条件均满足→戴。两例均产生明确结果。模糊区（如后蹲 70%1RM）因缺量化阈值无法自动裁定——已登记为边界，不影响清晰情形判定。
- **V3_task_utility**: passed: true — expected_benefit: 减少"逢练必戴腰带"导致的核心训练机会流失（ce16-03），把判据结构化为两变量决策，改善决策结构。
- **decision**: verified
- **if_not_verified**: —（"接近最大/最大"缺 %1RM 阈值作为已知边界，供阶段 2 写入 B 段；不建议依常识补阈值）

---

## 能力单元 U5 — 保护（spotting）规则与判断

- **proposed_capability_id**: cap.nsca.spotting-rules
- **proposed_slug**: spotting-rules
- **type**: framework
- **merged_candidates**: [f16-07, f16-08, f16-09, f16-10, f16-11, f16-12, f16-18, p16-10(rej), p16-11(rej), p16-12(rej), p16-13, p16-14, p16-15, p16-16, c16-2, ce16-04, ce16-05, ce16-06, ce16-07, ce16-10]
- **task_ids**: [T25]
- **importance**: high（安全相关）
- **source_evidence**:
  - source_id: src-nsca-essentials-5e
    location: Chapter 16 spotting 段（ch16.txt 第 260–266 行保护者体型/架外风险；第 913–927、976–994 行卧推/哑铃保护要点；爆发动作不保护段）
- **R 段可用原文引用**（英文，逐字）:
  > "Spotting is necessary on skillful multijoint exercises that involve a barbell or dumbbells being lifted over the head, on the back, on the front of the shoulders, or over the face. ... Power exercises are not spotted ... to exert sufficient leverage the spotter or spotters should be at least as strong and at least as tall as the athlete who is lifting. ... Spotting at the forearms near the wrists ... is a safer technique."
- **V1_source_sufficiency**: passed: true — 回查 ch16.txt：需保护模式（过顶/过背/架肩前/过面部）、爆发动作不保护并教失杠（"push the bar away or simply drop it"）、保护者数量由负荷/经验/力量决定、过面部动作保护手位（交替握抓杠；哑铃近腕前臂保护而非上臂/肘）、liftoff 信号、架外大重量风险与保护者至少同高同强，均在原文完整给出。适用条件、分支、输出齐全。
- **V2_executability**: passed: true
  - check_mode: walkthrough
  - input: 运动员做哑铃仰卧臂屈伸（过面部动作，中等负荷），需 1 名保护者。
  - expected: 判定"需保护（过面部）"；保护者直接在哑铃处/腕附近前臂保护，绝不抓上臂或肘；先沟通次数与 liftoff 信号；若为爆发动作则改为教失杠——本例不是。
  - observed: 依 ch16 规则可落定"是否需要保护—人数—手位—沟通"的完整保护方案，输出明确。
- **V3_task_utility**: passed: true — expected_benefit: 把分散的保护准则整合为"是否保护→人数→手位→沟通→失杠"流程，识别失败边界（抓错手位、保护者过矮过弱、爆发动作误保护），高风险场景减少遗漏。
- **decision**: verified
- **if_not_verified**: —

---

## 能力单元 U6 — 爆发力动作阶段结构（高翻/抓举、推举/借力推、中大腿拉）

- **proposed_capability_id**: cap.nsca.power-exercise-phases
- **proposed_slug**: power-exercise-phases
- **type**: procedure
- **merged_candidates**: [f16-14, f16-15, f16-16, p16-20, p16-21]
- **task_ids**: [T24]
- **importance**: high
- **source_evidence**:
  - source_id: src-nsca-essentials-5e
    location: Chapter 16, Power Exercises 段（ch16.txt 第 2706–2707 行中大腿拉 140% 1RM；高翻/抓举四阶段与推举/借力推 dip–drive–catch 技术说明）
- **R 段可用原文引用**（英文，逐字）:
  > "Although the lift consists of four phases (i.e., first pull, transition, second pull, and catch) the upward movement of the bar occurs in one continuous motion without interruption. ... In the push press, the hip and knee extension thrust is only forceful enough to drive the bar one-half to two-thirds the distance overhead. ... it is not uncommon for athletes to be able to perform the mid-thigh pulls with as much as 140% of the 1RM."
- **V1_source_sufficiency**: passed: true — 回查 ch16.txt：高翻/抓举四阶段（first pull/transition/second pull/catch）与"连续动作"、推举 vs 借力推的冲量差异（1/2–2/3 距离）、中腿拉 140% 1RM 上限与从 power position 起始，均在原文完整给出。**缺口**：原文未给各阶段的**时间或关节角度阈值**（仅定性描述"膝完全伸展时结束""power position"等）——f16-14/f16-15 已登记。此为边界而非阻断。
- **V2_executability**: passed: true
  - check_mode: walkthrough
  - input: 运动员做高翻（power clean），杠在地面起始。
  - expected: 连续完成 first pull→transition→second pull→catch 四阶段；末端绕肘接杠于锁骨/前三角、屈髋膝成四分之一蹲；属爆发动作→不保护、教失杠并清空平台。
  - observed: 依 ch16 阶段定义可产出完整阶段序列与接杠要求，输出明确（阶段边界靠动作描述判定，无需阈值即可教学）。
- **V3_task_utility**: passed: true — expected_benefit: 统一爆发动作的阶段口径与常见错误（髋先于肩、三关节伸展前屈肘），并为"不保护+教失杠"提供依据，改善教学与安全决策。
- **decision**: verified
- **if_not_verified**: —（"无阶段时间/角度阈值"作为已知边界登记，供阶段 2 写入 B 段）

---

## 能力单元 U7 — 变阻负荷计算（链 / 弹力带）

- **proposed_capability_id**: cap.nsca.variable-resistance-load
- **proposed_slug**: chains-bands-load-calc
- **type**: calculation
- **merged_candidates**: [f17-04, f17-05, f17-06, f17-07, f17-08, p17-10, p17-11(rej), p17-12, p17-13, p17-14, p17-15, p17-17(rej), p17-18, c17-1, c17-4, ce17-01, ce17-02, ce17-05]
- **task_ids**: [T26]
- **importance**: medium
- **source_evidence**:
  - source_id: src-nsca-essentials-5e
    location: Chapter 17（ch17.txt 第 471–478 行链负荷算例；第 586–633 行 Table 17.2 与带负荷算例；第 568–584 行 Hooke 定律与带间差异；第 440 行起 Table 17.1）
- **R 段可用原文引用**（英文，逐字）:
  > "the absolute chain resistance at the top and at the bottom portion of the movement are summed and then averaged. ... if their 5RM is 120 kilograms (265 lb), they would subtract the average chain resistance from this load. If at the bottom position the load is 0 kilograms and at the top the chain load is 11.1 kilograms (24.5 lb), the average is 5.55 kilograms (12.2 lb). Thus, the athlete would add 114 to 115 kilograms."
- **V1_source_sufficiency**: passed: true — 回查 ch17.txt：链负荷上下平均法（471–478）、弹力带负荷上下平均法（617–633）、Hooke 定律 Tension=k×d（571）、带间差异 3.2%–5.2% → 平均张力差 8%–19%（580–582）、Table 17.1 链质量-长度-直径表（440）、Table 17.2 带长度-张力表（586）。公式、单位（kg/lb）、输出（杠上加载量）齐全。Table 17.2 预测方程自变量 x 单位未定义（N15 另列）。
- **V2_executability**: passed: true
  - check_mode: walkthrough（数值独立核算）
  - input（链）: 目标卧推 5RM=140 kg（无链）；链底 0 kg、顶 15 kg。input（带）: 目标卧推 5RM=160 kg；带底 0 kg、顶 30 kg。
  - expected: 链——平均=(0+15)/2=7.5 kg，杠上加 140−7.5=**132.5 kg**；带——平均=(0+30)/2=15 kg，杠上减至 160−15=**145 kg**。
  - observed: 按"杠上负荷 = 目标RM负荷 −(底负荷+顶负荷)/2"逐步核算，得链 132.5 kg、带 145 kg，与预期一致；原文算例（120 kg/11.1 kg→114–115 kg；150 kg/26.6 kg→136–137 kg）复核一致。结果明确。
- **V3_task_utility**: passed: true — expected_benefit: 把链/带"顶底平均后从目标 RM 扣除"的统一口径固化，避免把变阻误当恒定额外负荷（ce17-01）；输出可直接执行的杠铃加载量，节省重复换算。
- **decision**: verified
- **if_not_verified**: —

---

## 能力单元 U8 — 强化离心负荷（AEL）编程

- **proposed_capability_id**: cap.nsca.ael-programming
- **proposed_slug**: accentuated-eccentric-loading
- **type**: procedure
- **merged_candidates**: [f17-09, f17-10, p17-19, p17-20, p17-21, p17-22, c17-2, c17-3]
- **task_ids**: [T26]
- **importance**: medium
- **source_evidence**:
  - source_id: src-nsca-essentials-5e
    location: Chapter 17, AEL 段（ch17.txt 第 728–730 行资格规则；第 755–763 行 20%–30% 体重/跳跃；第 776–789 行最大/超最大与 >40% 差值；第 801–821 行三种组结构；亦见 f17-18 weight releaser 设置）
- **R 段可用原文引用**（英文，逐字）:
  > "loads of 20% to 30% of body mass should be implemented during AEL when attempting to potentiate performance during the concentric phase of a plyometric jumping activity (91). ... significant improvements in concentric velocity with loads between 30% and 80% of the 1RM ... when a maximal AEL (100% of the 1RM) is implemented. ... if a differential >40% between the AEL and the concentric load is programmed, significant acute increases in velocity and power occur."
- **V1_source_sufficiency**: passed: true — 回查 ch17.txt：AEL 定义与离心负荷分级（亚最大<100%/最大=100%/超最大>100% 向心 1RM）、跳跃 AEL 20%–30% 体重（755–763）、抗阻最大 AEL(100%)+向心 30%–80% 1RM、超最大 105%–120% 1RM、>40% 差值阈值（776–789）、三种组结构及其休息（每重复 15–40 s cluster；仅首重复；混合 25–35 s）（801–821）、资格规则（728–730）、weight releaser 2–4 in（5–10 cm）脱离设置（1931–1932）。**边界**：原文称"最优策略仍需更多研究"，且跳跃 AEL（%体重）与抗阻 AEL（%1RM）量纲不同。此为边界，不阻断（两分支各有明确数值）。
- **V2_executability**: passed: true
  - check_mode: walkthrough
  - input: ①运动员体重 80 kg，做反向纵跳 AEL；②卧推做 AEL，离心取 100%1RM、向心取 50%1RM。
  - expected: ①离心相施加体重 20%–30% = **16–24 kg**，离心末释放；②离心-向心差值 = 100%−50% = **50% > 40%** → 预期向心速度/功率急性提升；组结构可选"仅首重复加 AEL"或 3 次 cluster（首重复 AEL、簇间 25–35 s）。
  - observed: 依原文数值直接得出 16–24 kg 与 50% 差值判断，输出明确；资格规则（仅经验丰富者）作为前置门槛。
- **V3_task_utility**: passed: true — expected_benefit: 把 AEL 的"负荷分级/差值阈值/组结构/资格"固化为可执行处方，识别失败边界（新手禁用、超最大会使向心变慢），减少误用。
- **decision**: verified
- **if_not_verified**: —（"最优策略待研究""两分支量纲不同"作为已知边界登记）

---

## 能力单元 U9 — 替代模式与非传统器械的采用决策

- **proposed_capability_id**: cap.nsca.alternative-modes-decision
- **proposed_slug**: alternative-modes-decision
- **type**: framework
- **merged_candidates**: [f17-01, f17-02, f17-03, f17-11, f17-13, f17-14, f17-15, f17-16, f17-21, f17-22, p17-01, p17-03, p17-04, p17-05, p17-07, p17-08, p17-09, p17-13, p17-14, p17-18, p17-23, p17-24, p17-25, p17-27, p17-28, p17-29, p17-30, ce17-03, ce17-04]
- **task_ids**: [T26]
- **importance**: medium
- **source_evidence**:
  - source_id: src-nsca-essentials-5e
    location: Chapter 17（ch17.txt：bodyweight/suspension 段、instability 段、free-weight vs machine 段、unilateral/双侧促进段、kettlebell 段、sled/strongman 段）
- **R 段可用原文引用**（英文，逐字）:
  > "the level of the athlete dictates whether use of these methods is warranted. For example, a novice athlete or untrained individual may derive a large benefit from doing bodyweight or core stability exercises. Conversely, the trained or elite athlete may experience greater gains with traditional ground-based free weight exercises. ... During training with instability exercises, the overall agonist force-generating capacity (12) and overall power output (33) may be less than 70% of what can be achieved when the exercise is performed under stable conditions."
- **V1_source_sufficiency**: passed: true — 回查 ch17.txt：按水平的采用决策（新手→自重/核心；精英→传统自由重量；进阶→变阻）、不稳定器械 <70% 力/功率规则、"地面自由重量=特异性+不稳定最佳组合"、单侧 vs 双侧（bilateral facilitation/deficit）、自重/悬吊负荷上限=体重、壶铃定位（一般准备）、雪橇负荷与 PAPE 带（66%–75% 体重→15 m 冲刺）、轮胎翻转规则等，均在原文完整给出。适用条件、分支与输出齐全。
- **V2_executability**: passed: true
  - check_mode: walkthrough
  - input: 一名未训练者，仅可用自重与悬吊带，目标是提升绝对力量。
  - expected: 判定——纯自重/悬吊负荷上限=体重，难以显著提升绝对力量（ce17-03）；该未训练者可从自重/核心稳定性练习获初始收益，但发展绝对力量应转向可超体重的自由重量（如杠铃）或加负重背心；不稳定器械只作平衡/核心入门前置，不作主刺激（<70% 力/功率）。
  - observed: 依 ch17 决策规则可产出"手段选择 + 定位 + 限制说明"，结果明确。
- **V3_task_utility**: passed: true — expected_benefit: 按运动员水平统一"该用什么手段"，识别失败边界（自重练不出绝对力量、不稳定器械削弱功率），改善决策结构与器材投资判断。
- **decision**: verified
- **if_not_verified**: —（"新手/精英"缺客观阈值——需引用 Ch18 training status 分类；作为跨章依赖登记）

---

## 能力单元 U10 — 技术错误排障（缺陷→纠正）

- **proposed_capability_id**: cap.nsca.technique-troubleshooting
- **proposed_slug**: technique-error-correction
- **type**: troubleshooting
- **merged_candidates**: [f17-12, p17-26]
- **task_ids**: [T26]
- **importance**: medium
- **source_evidence**:
  - source_id: src-nsca-essentials-5e
    location: Chapter 17, 轮胎翻转（肩抵轮胎式）Flaw/Correction 段（ch17.txt 相关段落）
- **R 段可用原文引用**（英文，逐字）:
  > "Flaw: Placing the feet too close to the tire when initiating the movement. ... Correction: Have athletes move their feet away from the tire, and instruct them to brace their spine and use a forceful triple extension ... Flaw: Hips rise faster than the shoulders ... Correction: Instruct athletes to keep their hips low and drive the tire forward rather than lifting it."
- **V1_source_sufficiency**: passed: true — 回查 ch17.txt，轮胎翻转（肩抵轮胎式）以完整的 Flaw（缺陷）→后果→Correction（纠正）结构给出三组示例（脚过近/髋先升/用抬代推），是 Ch15–17 中**唯一**具备"症状→操作"闭环的排障段落。适用观察项、纠错操作、输出齐全。
- **V2_executability**: passed: true
  - check_mode: walkthrough
  - input: 运动员做肩抵轮胎式翻胎，观察到"起始脚离轮胎太近"且"髋比肩先上升"。
  - expected: 对症纠正——脚后移、绷紧脊柱、用强力下肢三关节伸展把胸与轮胎抬离地面；保持髋低、向前"推"而非向上"提"，随轮胎前移。
  - observed: 依原文 Flaw→Correction 映射可直接给出纠正口令与动作调整，输出明确。
- **V3_task_utility**: passed: true — expected_benefit: 提供可复制的"缺陷→纠正"排障模板，降低重胎翻胎的肱二头肌撕裂等损伤风险，改善纠错交付格式。
- **decision**: verified
- **if_not_verified**: —（注：Ch15 动态拉伸与 Ch16 各动作的"常见错误"仅列症状、无纠错闭环，已单列为 R13 参考，不并入本单元）

---

## 参考单元 R11 — 动作/拉伸技术目录汇总（resource list）

- **proposed_capability_id**: cap.nsca.technique-catalogs
- **proposed_slug**: technique-catalogs
- **type**: checklist
- **merged_candidates**: [f15-15, p15-24, f16-17, p16-19, f17-20, p17-32]
- **task_ids**: [T19, T24, T26]
- **importance**: low
- **source_evidence**:
  - source_id: src-nsca-essentials-5e
    location: Ch15 技术清单（ch15.txt 第 1126、1455、1812 行）；Ch16 45 动作（p16-19）；Ch17 24 动作（p17-32）
- **R 段可用原文引用**（英文，逐字）:
  > "STATIC STRETCHING TECHNIQUES ... 23 Step Stretch ... DYNAMIC STRETCHING TECHNIQUES 24 Arm Swings ... 40 Spiderman Crawl ... PNF STRETCHING TECHNIQUES 41 Calves ... 45 Shoulders"
- **V1_source_sufficiency**: passed: true — 三类清单在原文存在（静态 23 / 动态 17 / PNF 5；Ch16 45 动作；Ch17 24 动作），字段结构完整。
- **V2_executability**: passed: false — 目录仅提供"编号/名称/页码/步骤/影响肌"资源索引，无"何时选哪个动作"的统一决策规则，本身不产生具体动作/结果。
- **V3_task_utility**: passed: true — expected_benefit: 作为资源路由索引，减少查找成本。
- **decision**: reference
- **if_not_verified**: reference → 并入 Bundle 的 `book/overview.md` 参考区（动作资源目录索引）；原书页码与 .cangjie source 行号无对应，需以 source 文本行号重建索引。

---

## 参考单元 R12 — 热身急性效应与柔韧性影响因素清单

- **proposed_capability_id**: cap.nsca.warmup-flexibility-background
- **proposed_slug**: warmup-flexibility-background
- **type**: checklist
- **merged_candidates**: [p15-06, p15-13, p15-14]
- **task_ids**: [T19]
- **importance**: low
- **source_evidence**:
  - source_id: src-nsca-essentials-5e
    location: Chapter 15 热身效应分类段、柔韧性影响因素段
- **R 段可用原文引用**（英文，逐字）:
  > "they typically can be divided into temperature-related effects and non–temperature-related effects (10). Temperature-related effects include an increase in muscle temperature, core temperature (62), enhanced neural function ... while non–temperature-related effects can include increased blood flow to muscles ... and postactivation potentiation (10)."
- **V1_source_sufficiency**: passed: true — 效应分类与影响因素清单在原文完整给出。
- **V2_executability**: passed: false — 属背景性知识清单，无执行步骤或判定输出。
- **V3_task_utility**: passed: true — expected_benefit: 为 U1/U2 提供机制依据（why），支撑 B 段。
- **decision**: reference
- **if_not_verified**: reference → 并入 `book/overview.md` 机制背景或 `book/glossary.md`（stretch reflex / GTO 相关术语）。

---

## 参考单元 R13 — Ch15/Ch16 症状型常见错误清单（无纠错闭环）

- **proposed_capability_id**: cap.nsca.common-error-symptoms
- **proposed_slug**: common-error-symptoms
- **type**: checklist
- **merged_candidates**: [f15-16, ce16-11, ce16-01, ce16-08, ce16-09]
- **task_ids**: [T24]
- **importance**: medium
- **source_evidence**:
  - source_id: src-nsca-essentials-5e
    location: Ch15 动态拉伸 COMMON ERROR 段；Ch16 各动作 COMMON ERRORS（后蹲/弯举等）
- **R 段可用原文引用**（英文，逐字）:
  > "COMMON ERROR Losing postural integrity as the arms swing ... Allowing the heels to lift off the floor, the torso to flex further forward, or the upper back to round during the upward phase of the movement; Allowing the knees to move in (via hip adduction) or out (via hip abduction) during the movement."
- **V1_source_sufficiency**: passed: true（作为症状清单）— 症状在原文完整列出；但原文**只给症状、未给对应纠错动作**（Ch15 动态拉伸缺 correction 文本；Ch16 的 COMMON ERRORS 亦多为症状）。依方法论"已完整但无法产生具体动作/结果的降为 reference"。
- **V2_executability**: passed: false — 无"症状→纠错→验证"闭环，不能产出明确纠正动作。
- **V3_task_utility**: passed: true — expected_benefit: 作为技术质检观察项清单，帮助识别错误；亦可作 U10 的素材。
- **decision**: reference
- **if_not_verified**: reference → 并入 `book/overview.md` 参考区作"技术错误观察清单"；**缺口登记**：Ch15/Ch16 缺纠错闭环（与 Ch17 轮胎翻转形成对比），若阶段 2 需要纠错能力，须补读或另据他源。

---

## 待核查单元 N14 — 原木（log）直径与训练负荷规则

- **proposed_capability_id**: cap.nsca.log-training
- **proposed_slug**: log-training-diameter
- **type**: rule
- **merged_candidates**: [p17-31]
- **task_ids**: [T26]
- **importance**: low
- **source_evidence**:
  - source_id: src-nsca-essentials-5e
    location: Chapter 17 log 段（ch17.txt 第 1021–1024 行）
- **R 段可用原文引用**（英文，逐字）:
  > "a thinner log (250 mm [1.0 in.] diameter) allowed 10 strongman athletes to produce significantly greater power, velocity, and force than a thicker log (316 mm [1.2 in.] diameter)."
- **V1_source_sufficiency**: passed: false — 回查 ch17.txt 第 1021–1024 行确认：原文对原木直径的**单位换算本身错误**——"250 mm" 却标为 "[1.0 in.]"（250 mm ≈ 9.8 in.），"316 mm" 标为 "[1.2 in.]"（316 mm ≈ 12.4 in.）。mm 与 in. 数值互斥且原文未给出可用解释；直径数值（250/316 mm）与英寸标注冲突未解决 → needs_review。
- **V2_executability**: passed: false
  - check_mode: walkthrough
  - input: 依据"较细原木产生更大功率"选择原木直径。
  - expected: 应能据原文给出可用的直径口径（mm 或 in.）。
  - observed: 因单位冲突，直径的物理量不确定（250 mm 与 1.0 in. 不能同真），无法在不裁定的前提下落定"选多细的原木"，规则不能执行。
- **V3_task_utility**: passed: true — expected_benefit: 若单位确定，可指导原木直径选择（细→更大功率/速度/力）。
- **decision**: needs_review
- **if_not_verified**: needs_review → 具体缺口：原木直径的英寸标注与毫米值矛盾（疑为排版错误，真实值或为 250 mm 对应 9.8 in.，1.0/1.2 in. 疑误植）；需回查原书图表或出版勘误裁定后并入 U9 或作独立参考。

---

## 待核查单元 N15 — 弹力带长度-张力预测方程（自变量单位未定义）

- **proposed_capability_id**: cap.nsca.band-tension-equation
- **proposed_slug**: band-tension-equation
- **type**: calculation
- **merged_candidates**: [p17-16, f17-07]
- **task_ids**: [T26]
- **importance**: low
- **source_evidence**:
  - source_id: src-nsca-essentials-5e
    location: Chapter 17, Table 17.2（ch17.txt 第 586–615 行）
- **R 段可用原文引用**（英文，逐字）:
  > "tension can be predicted based on the length of the band with the use of a prediction equation. TABLE 17.2 Examples of Resistance Band Length–Tension Relationships ... Y = −0.003x2 + 0.98x − 69.82 ... Y = −0.010x2 + 3.73x − 269.21"
- **V1_source_sufficiency**: passed: false — 回查 ch17.txt 第 586–615 行：Table 17.2 给出各带宽/颜色在 110–150 cm 的张力值（这部分可直接查表用），但**预测方程 Y=a·x²+b·x+c 的自变量 x 的物理量（是长度 cm？拉伸量？其余？）及单位原文未定义**，仅笼统说"based on the length of the band"。方程系数对应特定厂商带，跨品牌不可直接用（带间差异 3.2%–5.2%）。自变量未定义 → needs_review。
- **V2_executability**: passed: false
  - check_mode: walkthrough
  - input: 用 67 mm 黑带预测方程估算某长度下张力。
  - expected: 代入 x（长度）得 Y（张力）。
  - observed: 因 x 的单位/量纲未定义，无法确定应代入何值（若 x=150 得 Y=−0.010×22500+3.73×150−269.21=225−... 具体为 −225+559.5−269.21=65.29 kg，与表中 150 cm 的 57.2 kg 不符，进一步说明 x 口径不明）→ 不能直接执行。
  - 备查：查表路径（直接读表中张力值）可用，故 U7 仍成立；仅"预测方程"分支待核查。
- **V3_task_utility**: passed: true — expected_benefit: 若自变量确定，可用方程外推表外长度的张力。
- **decision**: needs_review
- **if_not_verified**: needs_review → 具体缺口：预测方程自变量 x 的物理量/单位未定义，且代入 150 与表中 57.2 kg 不符，口径不明；需回查 McMaster 等 2010 原文或原书脚注裁定。查表分支（U7）不受影响。

---

## 覆盖核查表

| task_id | 任务 | 原文位置 | 对应候选 | decision | 去向 |
|---|---|---|---|---|---|
| T19 | 设计准备活动（RAMP）与柔韧训练 | Ch15；Table 15.1/15.2/15.3 | U1：f15-01/02/03/04、p15-01..11、c15-1/2/4 | verified | cap.nsca.warmup-ramp |
| T19 | （柔韧训练编程部分） | Ch15 静态/动态/PNF | U2：f15-06..13、p15-05/12/14..24、c15-3、ce15-01..07 | needs_review | 参数口径冲突待裁定（静态 10–30 s vs 15–30 s；PNF 3–6 s/≤20%MVC vs 6–10 s） |
| T24 | 技术规范：呼吸、身体稳定、护腰使用 | Ch16 | U3：f16-01..05/13、p16-*；U4：f16-06/p16-09；U6：f16-14..16/p16-20/21 | verified | cap.nsca.exercise-technique-basics / weight-belt-decision / power-exercise-phases |
| T25 | 保护（spotting）规则与判断 | Ch16 | U5：f16-07..12/18、p16-10..17、c16-2、ce16-04..07/10 | verified | cap.nsca.spotting-rules |
| T26 | 替代模式与非传统器械的训练应用 | Ch17 | U7：f17-04..08、p17-10..18、c17-1/4；U8：f17-09/10、p17-19..22、c17-2/3；U9：f17-01..03/11/13..16/21/22、p17-*；U10：f17-12/p17-26 | verified（U7/U8/U9/U10）；N14/N15 needs_review | cap.nsca.variable-resistance-load / ael-programming / alternative-modes-decision / technique-error-correction |

- T19、T24、T25、T26 均在本簇有对应候选，覆盖完整（无"其他簇负责"项）。
- 本簇不负责的 Ch15–17 外移内容：Ch18 training status 分类（供 U9 引用）、Ch16 逐动作技术细节（作 R11 资源）、Ch17 逐动作技术细节（作 R11 资源）——按 BOOK_OVERVIEW 4.2 归入参考而非独立能力。

## 本簇缺口清单

1. **【高优先·阻断】柔韧参数口径冲突（T19/U2）**：原文对静态拉伸保持时长（10–30 s vs 15–30 s）与 PNF 收缩参数（3–6 s/≤20% MVC vs 6–10 s/中等强度）自相矛盾且未澄清适用边界 → 转 needs_review，需回读或专家裁定后方可进能力池。
2. **【中优先·边界】护腰"接近最大/最大"缺 %1RM 量化阈值（T24/U4）**：判据对清晰情形可执行，模糊区（如 70%1RM 后蹲）无法自动裁定；登记为 B 段边界，不以常识补阈值。
3. **【中优先·边界】爆发力动作无阶段时间/角度阈值（T24/U6）**：高翻/抓举/推举/中腿拉的阶段结构为定性描述；登记为 B 段边界。
4. **【中优先·缺口】Ch15 动态拉伸与 Ch16 各动作"常见错误"仅列症状、无纠错闭环（T24/R13）**：与 Ch17 轮胎翻转的 flaw→correction 形成对比；若需要纠错能力须补读或另据他源。
5. **【低优先·待核查】原木直径单位标注错误（T26/N14）**：250 mm=1.0 in.、316 mm=1.2 in. 明显矛盾，原文错误，口径未决 → needs_review。
6. **【低优先·待核查】弹力带预测方程自变量单位未定义（T26/N15）**：x 量纲不明且与表中值不符 → needs_review；查表分支不受影响。

## 去重说明（候选级 rejected，13 条）

以下候选与另一候选内容完全重复、未提供新证据，按方法论"去重后被另一候选完整覆盖"标记，保留 canonical ID（内容已并入相应能力单元，审计轨迹不丢失）：

| 被覆盖候选 | canonical ID | 说明 |
|---|---|---|
| p15-03 | f15-01 | RAMP 三阶段，同内容（framework↔principle） |
| p15-07 | f15-02 | 传统两阶段热身，同内容 |
| p16-01 | f16-01 | 握法分类，同内容 |
| p16-03 | f16-02 | 抓举握距两测量法，同内容 |
| p16-04 | f16-03 | 五点接触位，同内容 |
| p16-07 | f16-04 | 呼吸时机，同内容 |
| p16-08 | f16-05 | Valsalva，同内容 |
| p16-09 | f16-06 | 护腰判据，同内容 |
| p16-10 | f16-07 | 保护适用范围，同内容 |
| p16-11 | f16-12 | 爆发动作不保护/教失杠，同内容 |
| p16-12 | f16-08 | 保护者数量，同内容 |
| p17-11 | f17-05 | 链负荷计算，同内容（calculation↔procedure） |
| p17-17 | f17-08 | 弹力带负荷计算，同内容 |

## 供阶段 2 的提示

- **可组合成一张能力卡的单元**：U1（热身）+ U2（柔韧，待裁定）可合成"准备活动与柔韧"卡；U3+U4 可合成"技术规范与护具"卡；U5+U6 可合成"保护与爆发动作安全"卡；U7+U8 可合成"变阻/离心负荷"卡；U9+U10 可合成"替代模式应用"卡。U7/U8 均为带数值的 calculation，A1 可直接用 c17-1（链 5RM 120 kg）与 c17-2/3（AEL 20 kg / >40% 差值）。
- **A1 可用素材**：c15-1（RAMP 示例表）、c15-4（CNS 预备组合）、c16-1（弯举呼吸）、c16-2（保护者体型）、c17-1（链负荷算例）、c17-4（带长度-张力）。
- **B 段（边界）素材**：ce15-01..07（柔韧误区/拉伸非防伤/长时静态拉伸/牵张反射/为 ROM 牺牲技术/有限 ROM 抗阻/肌肉体积）、ce16-01/02/03/04/05/06/07/08/09/10/11（五点接触/Valsalva/腰带/哑铃保护/爆发不保护/保护人数沟通/架外风险/呼吸时相/椎间 ROM/清场/后蹲错误）、ce17-01..05（链负荷折算/链用于新手/自重上限/不稳定器械/弹力带差异）。
- **需在下游标注的原文局限**：原书页码（383–409、418–473、498–523）与 .cangjie source 行号无对应；R11 资源目录须以 source 文本行号重建。


---

<!-- ===== 簇 G-populations-nutrition-psych ===== -->

# 簇 G-populations-nutrition-psych — 三重验证结果

- 负责任务: T30–T36
- 候选输入: 246 条（来自 cases-g1-ch01-14.md, counter-examples-g1-ch01-14.md, frameworks-g6-ch01-12.md, principles-g7-ch05-08.md, principles-g8-ch09-12.md）
- 归并后能力单元: 24 个
- verified: 21 / reference: 3 / needs_review: 0 / rejected: 0
- 回查原文: `.cangjie/source/ch05.txt`–`ch12.txt`（逐条核对营养/补水/增补剂数值与单位；已解决 `p10-16` 口径冲突，见 U9）

> 说明：本簇四块主题（人群适配 / 营养补水 / 增补剂 / 心理）分别归并。安全相关单元（RED-S、进食障碍、心理健康、增补剂滥用、老年人转诊）全部保留为 verified。`p05-*`/`p06-*`/`f05-01`/`f06-01`（基础适应，47 条）仅本簇收录，且不直接服务 T30–T36，按任务书（e）处理为 1 个 detraining 单元（verified）+ 1 个适应幅度参照（reference），未静默丢弃。营养类候选报告的 ~26 处缺口已在各单元 V1 逐条区分「原文缺」与「候选漏抄」。

> **口径冲突核查结论（`p10-16`）**：ch10.txt Table 10.15（2033–2044 行）Body weight EUH cutoff = `<1%`；同章正文（2024–2026、2112 行）另有「丢失 ≥2% 体重即补水不足 / 应避免超过 2%」。回查确认二者**非真冲突**：`<1%` 是「等水合（EUH）严格判定（偏离基线 1% 以内）」，`≥2%` 是「脱水预警与防脱水操作阈值」——服务不同目的，可并存。相关单元不再登记 needs_review。

---

## 能力单元 U1 — 青少年抗阻训练处方（有效性与剂量 / 指南 / 迷思 / 安全）

- **proposed_capability_id**: cap.nsca.youth-resistance-training
- **proposed_slug**: youth-resistance-training
- **type**: procedure
- **merged_candidates**: [p07-01, p07-02, p07-03, p07-04, p07-05, p07-07, p07-08, p07-09, p07-11, p07-12, f07-01, ce07-01, ce07-02]
- **task_ids**: [T30]
- **importance**: high
- **source_evidence**:
  - source_id: src-nsca-essentials-5e
    location: Chapter 7（ch07.txt 第 484–497 行剂量；guide/myths sidebar；第 751–752 行早期专项化；第 532 行频率效应）
- **R 段可用原文引用**（英文，≤100 词，逐字）:
  > "strength gains of roughly 30% to 40% are typically observed in untrained preadolescent children following short-term (8-20 weeks) resistance training programs. ... resistance training interventions realize larger gains in muscle strength and power when programs exceed 23 weeks in duration. ... strength gains were greater when young athletes were exposed to higher relative intensities (>80% 1RM)."（ch07.txt 484–497）
- **V1_source_sufficiency**: passed: true — 回查 ch07.txt：剂量（10%–90%、typically 30%–40%、>23 周、>80% 1RM）、指南清单 11 条、迷思清单 5 条（均标 False）、生长软骨三处（骺板/关节面/肌腱止点）与「PHV 前后风险最高」、早期专项化定义（>8 个月/年）、1RM 测试安全性、青春期前以神经适应为主（睾酮 20–60 vs ~600 ng/100 mL）均具文可查。ce07-01/02 提示「损伤多源于监督/技术/负荷不当」与原文一致。原文已明示具体剂量散见 guideline 清单，本单元一并纳入，无越界外推。
- **V2_executability**: passed: true
  - check_mode: walkthrough
  - input: 新输入＝13 岁、训练年龄 0、技术一般、无伤史的男孩；目标＝力量 + 动作技能，无器械经验；可用器械＝可调哑铃/杠铃。
  - expected: 产出 (a) 频率 2–3 次/周（非连续日）；(b) 起步轻负荷、每动作 1–3 组 × 8–12 次；(c) 随技术/力量提升按约 5%–10% 渐增负荷；(d) 单/多关节与核心动作；(e) 进阶动作（snatch/clean and jerk）须待技术熟练且负荷适宜；(f) 全年周期化；(g) 预期短期（8–20 周）力量增益约 30%–40%。7 项交付齐备。
  - observed: 依指南 11 条与剂量规则可完整给出上述 (a)–(g)，输出具体可核对（≥13 岁、PHV 前，符合「5 岁起即可受益、青春期前主要靠神经适应」）。
- **V3_task_utility**: passed: true — 统一青少年处方的剂量/频率/进阶口径，防止把成人方案叠加给青少年（ce07-01/02 失败边界），并把「迷思澄清」作为家长沟通模板。
- **decision**: verified
- **if_not_verified**: —

---

## 能力单元 U2 — 生物成熟度评估与 PHV 监测

- **proposed_capability_id**: cap.nsca.maturity-assessment-phv
- **proposed_slug**: maturity-assessment-phv
- **type**: procedure
- **merged_candidates**: [f07-02, p07-06, c07-01, ce07-03]
- **task_ids**: [T30]
- **importance**: medium
- **source_evidence**:
  - source_id: src-nsca-essentials-5e
    location: Chapter 7（ch07.txt 第 203–216 行：测量频率、PHV 位置；Figure 7.1）
- **R 段可用原文引用**（英文，≤100 词，逐字）:
  > "it may be appropriate to measure somatic growth every three months ... as a child nears their peak height velocity (PHV), it may be wise for practitioners to measure more frequently, such as monthly. ... PHV occurs at approximately 91% to 92% of predicted adult height."（ch07.txt 203–216）
- **V1_source_sufficiency**: passed: true — 回查：金标准骨骼龄因成本/设备/资质对多数从业者不可行、sexual maturation 教练无权、最可行是 somatic assessment；测量频率 3 个月（近 PHV 改每月）、PHV ≈ 91%–92% 预测成年身高，均具文。c07-01（13 岁男孩≈90% 预测成年身高）为原文算例，但原文**未给所用回归式**（候选已如实标注），故本单元只承载流程，不承诺具体预测公式。ce07-03（过密测量误读误差）与原文一致。
- **V2_executability**: passed: true
  - check_mode: walkthrough
  - input: 12 岁男孩，当前身高 150 cm、父母身高 158/178 cm；可获取身高、坐高、体重。
  - expected: 用 somatic 法（mid-parental height 估算最终身高）算出当前占预测成年身高的百分比；因接近 PHV，监测频率设为每月；据成熟度调整分组与训练/测试强度，并警惕过用伤。
  - observed: 可得到「成熟度状态 + 监测频率 + 方案调整」三输出；因原文未给回归式，具体百分比以 mid-parental 惯例估算并在交付中标注「原书仅给算例、未给公式」，不补造。
- **V3_task_utility**: passed: true — 把「按日历年龄分组」改为「按成熟度分组」，避免同班差异被误判，并给出可执行的监测节奏（减少遗漏、识别失败边界）。
- **decision**: verified
- **if_not_verified**: —

---

## 能力单元 U3 — 老年人抗阻训练处方与启动筛查（含安全/频率/跌倒预防/骨可逆）

- **proposed_capability_id**: cap.nsca.older-adult-resistance-training
- **proposed_slug**: older-adult-resistance-training
- **type**: procedure
- **merged_candidates**: [p07-13, p07-14, p07-15, p07-16, p07-17, p07-18, p07-19, p07-20, p07-21, p07-22, p07-23, p07-24, p07-25, f07-03, ce07-04, ce07-05]
- **task_ids**: [T30]
- **importance**: high
- **source_evidence**:
  - source_id: src-nsca-essentials-5e
    location: Chapter 7（ch07.txt 第 1442–1454 行：起步/进阶/功率剂量；第 1598–1629 行归因；sidebar 安全建议/迷思澄清/预参加筛查）
- **R 段可用原文引用**（英文，≤100 词，逐字）:
  > "Seniors should gradually progress from 1 set of 8 to 12 repetitions at a relatively low intensity (e.g., 40%-50% 1RM) to higher training volumes and intensities (e.g., 3 sets per exercise with 60%-80% of 1RM) ... older adults should progress toward 2 or 3 sets of 6 to 12 repetitions of one or two multijoint exercises, working at 70% to 85% of the 1RM, two or three times per week."（ch07.txt 1442–1446）
- **V1_source_sufficiency**: passed: true — 回查：起步 1×8–12 @40%–50%→进阶 3 组 @60%–80%→共识终态 2–3 组×6–12 @70%–85%、2–3 次/周；功率训练 1–3 组 @40%–60%、6–10 次高速；安全（预筛、热身 5–10 min、避免 Valsalva、48–72 h 恢复、无痛 ROM）；筛查/转诊（病史问卷、心脏康复/癌症生存者需医生放行）；跌倒预防须伴平衡/柔韧；骨适应停训 >6 个月丢失；BMD 定义（-1~-2.5 SD 骨量减少、<-2.5 SD 骨质疏松）均具文可查。ce07-04/05 与原文一致。
- **V2_executability**: passed: true
  - check_mode: walkthrough
  - input: 新输入＝72 岁、久坐、无心脏康复史、合并轻度高血压；目标＝维持功能、防跌倒。
  - expected: (a) 先完成病史/风险问卷，高血压交医疗人员；无心脏康复/癌症史故不需额外放行；(b) 起步 1 组 × 8–12 次 @40%–50% 1RM，2–3 次/周、课间 48–72 h；(c) 适应后进阶 2–3 组 × 6–12 @70%–85%；(d) 加高速度功率训练 40%–60% 1RM × 6–10 次；(e) 方案含平衡/柔韧以降低跌倒风险；(f) 全程避免 Valsalva、无痛 ROM。
  - observed: 可完整产出 (a)–(f) 个体化处方与转诊边界，与原文剂量逐项对齐，输出明确。
- **V3_task_utility**: passed: true — 统一老年人「筛查→起步→进阶→功率→安全」的剂量口径，明确医疗转诊边界与跌倒预防的组合要求，防止照搬成人方案（ce07-04）。
- **decision**: verified
- **if_not_verified**: —

---

## 能力单元 U4 — 女性运动员损伤风险降低与健康考量

- **proposed_capability_id**: cap.nsca.female-injury-risk-reduction
- **proposed_slug**: female-injury-risk-reduction
- **type**: framework
- **merged_candidates**: [f08-01, p08-04, p08-05, p08-06, p08-07, p08-08, p08-09, p08-10, p08-11, p08-12, p08-15]
- **task_ids**: [T31]
- **importance**: medium
- **source_evidence**:
  - source_id: src-nsca-essentials-5e
    location: Chapter 8（ch08.txt 第 245–260 行 ACL；第 401–419 行 PFD/UI；第 375–391 行心理健康/睡眠；sidebar「How Can Female Athletes Reduce Their Injury Risk」）
- **R 段可用原文引用**（英文，≤100 词，逐字）:
  > "in comparable sports female athletes' relative rate of ACL injuries is two times higher than those reported for male athletes ... the most significant contributing factor is a neuromuscular deficiency ... Recommend preparticipation screening by a sports medicine physician. ... Encourage female athletes to participate in a year-round conditioning program that includes resistance, plyometric, speed and agility, and flexibility training."（ch08.txt 245–260）
- **V1_source_sufficiency**: passed: true — 回查：ACL 相对风险 2×（主因神经肌肉缺陷/落地动态膝外翻）、PFPS >2×、UI 女运动员相对男 5×/相对久坐女 2.7×（患病率 27%/36%）、脑震荡部分项目更高且恢复更长、睡眠 <7 h/晚、心理健康（2021 年 40% vs 22%）、月经周期证据不支持按周期调处方，均具文可查；sidebar 五条降伤操作完整。女性生理机制类（p08-13/14/16–20）归 U6 reference。
- **V2_executability**: passed: true
  - check_mode: walkthrough
  - input: 新输入＝大学女子足球运动员，既往无 ACL 伤，存在轻度动态膝外翻。
  - expected: 产出 (a) 建议参赛前运动医学筛查 + 肌骨测试；(b) 全年周期化训练含抗阻 + 超等长 + 速度敏捷 + 柔韧；(c) 落地/切向动作力学教学与反复演示；(d) 每次课前置一般 + 专项动态热身、激活后链；(e) 提供增补反馈纠正膝外翻；(f) 把睡眠卫生/盆底/心理健康教育纳入；(g) 因证据不支持，**不**按月经周期调处方。
  - observed: 可完整产出 (a)–(g)，与原文风险口径（ACL 2×、UI 5×）一致，输出具体。
- **V3_task_utility**: passed: true — 把女性特定损伤与健康风险收敛为可执行的多环节降伤方案，统一转诊边界（心理健康、盆底、睡眠），避免按月经周期做无证据的处方切换。
- **decision**: verified
- **if_not_verified**: —

---

## 能力单元 U5 — 妊娠期与产后抗阻训练调整

- **proposed_capability_id**: cap.nsca.pregnancy-postpartum-training
- **proposed_slug**: pregnancy-postpartum-training
- **type**: framework
- **merged_candidates**: [f08-02, p08-01, p08-02, p08-03, p08-21, ce08-01]
- **task_ids**: [T31]
- **importance**: medium
- **source_evidence**:
  - source_id: src-nsca-essentials-5e
    location: Chapter 8, Table 8.1/8.2（ch08.txt 第 142–236 行；Table 8.2 各孕期建议 194–236）
- **R 段可用原文引用**（英文，≤100 词，逐字）:
  > "For pregnant females, program design variables (exercise selection, frequency, intensity, and duration) should be based on the baseline level of fitness of the athlete immediately prior to the confirmation of pregnancy." / "Avoid supine positions and exercises; switch to incline, side-lying, or vertical positions." / "caution is elicited in exceeding 90% of maximum heart rate until more research is performed"（ch08.txt）
- **V1_source_sufficiency**: passed: true — 回查 Table 8.1（第一孕期心输出量 ↑20%、分钟通气量 ↑40%–50%；第二孕期 ↑40%、避免仰卧；第三孕期血容量至孕前 +50%；产后 1–2 周多恢复、韧带松弛可至 5 个月）与 Table 8.2（联合心率 + RPE 监控、开始盆底肌训练、增加深蹲与饮水、产后盆底/核心 12–24 周），均具文。ce08-01（仰卧/超 90% HRmax/心率误读）与原文一致。
- **V2_executability**: passed: true
  - check_mode: walkthrough
  - input: 新输入＝孕前每周 3 次抗阻、现第二孕期的健康孕妇，无并发症。
  - expected: (a) 以孕前即时体能定档；(b) 心率 + RPE 联合监控强度，谨慎超 90% HRmax；(c) 避免仰卧，改倾斜/侧卧/直立；(d) 继续盆底肌训练；(e) 按症状/舒适度调整；产后立即盆底 + 核心稳定 ≥12–24 周。
  - observed: 可完整产出分孕期处方与禁忌清单，与 Table 8.2 一致。
- **V3_task_utility**: passed: true — 把孕期处方锚定在「孕前体能基线」，并统一体位/强度禁忌与产后康复窗口（稳定交付格式、识别失败边界）。
- **decision**: verified
- **if_not_verified**: —

---

## 能力单元 U6 — 性别差异生理与激素口径参照（reference）

- **proposed_capability_id**: cap.nsca.sex-difference-reference
- **proposed_slug**: sex-difference-reference
- **type**: reference
- **merged_candidates**: [p08-13, p08-14, p08-16, p08-17, p08-18, p08-19, p08-20]
- **task_ids**: [T31]
- **importance**: medium
- **source_evidence**:
  - source_id: src-nsca-essentials-5e
    location: Chapter 8（ch08.txt 第 520 行线粒体呼吸 +33% 等）
- **R 段可用原文引用**（英文，≤100 词，逐字）:
  > "When considered on a relative basis, sex-related differences in muscular strength are greatly reduced. Females have similar number of muscle fibers as males, and strength is similar when normalized to muscle volume."（ch08.txt）
- **V1_source_sufficiency**: passed: true — 回查：男女力量差异的绝对/相对口径、相对肌肥大相似（≤16 周）、estradiol 双刃、女性睾酮反应、皮质醇反应减弱、GH 急性升高 2–4 倍、线粒体呼吸 +33% 均具文。均为**解释性口径**，不是可独立执行的方法步骤。
- **V2_executability**: passed: false — 为「口径/机制参照」，单独使用不产生可执行动作或可比对结果（提供解释而非处方）。
- **V3_task_utility**: passed: true（参考价值）— 在解释/撰写评估结论时统一男女比较的单位口径（绝对 vs 相对）。
- **decision**: reference
- **if_not_verified**: 并入 `book/overview.md` 参考区「性别差异」小节与 `book/glossary.md`（力量归一化口径、激素反应口径）；阶段 2 不单独建能力卡。canonical 保留 p08-13（归一化口径）。

---

## 能力单元 U7 — 宏量营养素与能量需求估算

- **proposed_capability_id**: cap.nsca.macronutrient-energy-needs
- **proposed_slug**: macronutrient-energy-needs
- **type**: calculation
- **merged_candidates**: [p10-02, p10-03, p10-04, p10-05, p10-06, p10-07, p10-08, p10-09, p11-12, p11-13, p11-16, p11-17, p11-18, p11-19, p11-20, c11-03, c14-14]
- **task_ids**: [T33]
- **importance**: high
- **source_evidence**:
  - source_id: src-nsca-essentials-5e
    location: Chapter 10（ch10.txt 第 489 行 AMDR；蛋白质 RDA/运动员区间）＋ Chapter 11（ch11.txt 第 1237 行 Cunningham；Table 11.3/11.4/11.5）
- **R 段可用原文引用**（英文，≤100 词，逐字）:
  > "The Cunningham equation takes fat-free mass (FFM) into account to estimate RMR, making it more applicable to athletes. RMR = 500 + 22 (FFM in kg)" / "strength or speed athletes should consume 5 to 6 grams of carbohydrate per kilogram body weight per day during peak training periods ... 1.4 to 2.0 grams of protein per kilogram body weight per day."（ch11.txt）
- **V1_source_sufficiency**: passed: true — 回查：蛋白质 RDA 0.8、有氧耐力 1.2–2.0、增肌 1.4–2.0、低热量期上调；蛋白 AMDR 成人 10%–35%（ch10.txt 489）；4/4/9 kcal/g；Cunningham RMR=500+22×FFM；PAL/活动系数（1.00–1.48，Table 11.4）；BMI 式与分类（Table 11.5）；目标体重式 FFM/(100−目标体脂%)（ch11.txt 1381–1382）；高蛋白安全上限 2.8 g/kg；力量/速度运动员 碳水 5–6、蛋白 1.4–2.0 g/kg（Table 11.3 专项档），均具文可查。**原文缺**（非候选漏抄）：p10-06「每降 100 kcal 约升 1%」无精确公式与上下限；p11-20 目标体重式百分号书写歧义；p11-04「正常糖原基线」未定义——已在 V2 限定使用范围，不补造。
- **V2_executability**: passed: true
  - check_mode: walkthrough
  - input: 新输入＝80 kg 力量运动员，FFM = 68 kg，峰值训练期；按蛋白 1.6–2.2 g/kg、碳水 5–6 g/kg 估算；用 Cunningham 估 RMR。
  - expected: 日蛋白 = 1.6×80=128 g 至 2.2×80=176 g；日碳水 = 5×80=400 g 至 6×80=480 g；RMR = 500 + 22×68 = 500 + 1496 = **1996 kcal/天**；乘活动系数（如 Active 1.25）→ TDEE ≈ 2495 kcal/天。容差：RMR 精确值 1996（±1）。
  - observed: 独立核算 RMR = 1996 kcal/天，与公式一致；蛋白/碳水区间明确；目标体重式在给定 FFM 与目标体脂（如 10%）下 = 68/(1−0.10)=75.6 kg（写作 FFM ÷ 期望去脂体重占比）。
- **V3_task_utility**: passed: true — 把「每公斤该吃多少」从口号变成可核算的 g/kg 与 kcal 处方，统一能量需求估算口径（减少遗漏、稳定交付格式）。
- **decision**: verified
- **if_not_verified**: —

---

## 能力单元 U8 — 血糖生成指数/负荷（GI/GL）计算

- **proposed_capability_id**: cap.nsca.glycemic-index-load
- **proposed_slug**: glycemic-index-load
- **type**: calculation
- **merged_candidates**: [p10-10, p10-11, p10-12]
- **task_ids**: [T33]
- **importance**: low
- **source_evidence**:
  - source_id: src-nsca-essentials-5e
    location: Chapter 10（ch10.txt 第 824 行 GI 式；第 853 行 GI 分档；第 901 行 GL 式）
- **R 段可用原文引用**（英文，≤100 词，逐字）:
  > "Glycemic load = GI of an individual food × grams of carbohydrate per serving of food ÷ 100" / "Low-GI foods (<55) / Medium-GI foods (55-69) / High-GI foods (>70)"（ch10.txt 853, 901）
- **V1_source_sufficiency**: passed: true — 回查：GI 式（测试食物 iAUC ÷ 等量标准食物 iAUC ×100，标准食物白面包或葡萄糖、份量 25 或 50 g）、GL 式（GI×每份碳水克数÷100）、GI 三档阈值（<55/55–69/>70）均具文。**原文缺**：GL 无高低分档阈值与每日目标（候选已标注），故本单元只做 GI/GL 计算与 GI 分档，不裁定 GL 分档。
- **V2_executability**: passed: true
  - check_mode: walkthrough
  - input: 新输入＝某食物 GI=72，每份含碳水 30 g。
  - expected: GL = 72 × 30 ÷ 100 = **21.6**；因 GI=72 >70 归「高 GI」。
  - observed: GL = 21.6，GI 分类＝高 GI；结果明确可核对（原文未给 GL 档位，故不判 GL 档）。
- **V3_task_utility**: passed: true — 提供把「GI 概念」落成可算的份量校正指标（GL），并给出训练前后差异化选择口径。
- **decision**: verified
- **if_not_verified**: —

---

## 能力单元 U9 — 个体化补水与电解质方案（汗液率计算 + 水合判定 + 分年龄处方）

- **proposed_capability_id**: cap.nsca.hydration-electrolyte-plan
- **proposed_slug**: hydration-electrolyte-plan
- **type**: calculation
- **merged_candidates**: [f10-02, p10-16, p10-17, p10-18, p10-19, p10-20, p10-21, p10-22, c10-01, c11-02, ce10-01, ce10-02]
- **task_ids**: [T32]
- **importance**: critical
- **source_evidence**:
  - source_id: src-nsca-essentials-5e
    location: Chapter 10（ch10.txt 第 2024–2048 行体重法/≥2%/Table 10.15；第 2053–2059 行汗液率式；第 2164–2186 行分年龄补液；第 1209–2135 行低钠血症）
- **R 段可用原文引用**（英文，≤100 词，逐字）:
  > "Each pound (0.45 kg) lost during practice represents 16 ounces (0.47 L) of fluid. A loss of 2% or more of body weight indicates the athlete is not adequately replacing fluid lost through sweat. ... Sweat rate is equal to preexercise body weight minus postexercise body weight + fluid intake during exercise − urine produced."（ch10.txt 2024–2059）
- **V1_source_sufficiency**: passed: true — 回查并**解决了 p10-16 口径冲突**：Table 10.15（2033–2044）Body weight EUH cutoff `<1%`（严格等水合判定）与正文 ≥2%（脱水预警/防脱水）服务不同目的，非矛盾，详见文首说明。汗液率式、1 lb≈16 oz(0.47 L)、分年龄补液（40 kg→5 oz/20 min、60 kg→9 oz/20 min）、运动饮料（钠 20–30 mEq/L、钾 2–5 mEq/L、碳水 5%–10%）、训练后按每 kg 体重损失补 ~1.5 L、低钠血症 <130/<125/<120 mmol/L、汗钠 0.2–>12.5 g/L 均具文可查（ce10-01/02、c10-01、c11-02 与原文一致）。
- **V2_executability**: passed: true
  - check_mode: walkthrough
  - input: 新输入＝一名 70 kg 成人，1 h 高强度训练前后（擦干、排尿、轻装）称重：前 70.0 kg → 后 69.0 kg；训练中摄入 0.5 L、尿 0.2 L；12 h 内有下一场训练。另：50 kg 青少年按分年龄档插值。
  - expected: 汗液率 = 70.0 − 69.0 + 0.5 − 0.2 = **1.3 L/h**；体重损失 % = (70.0−69.0)/70.0×100 = **1.43%**（<2%，未达脱水预警；但 >1% 未严格达 EUH）；若 12 h 内有下一场，按每 kg 损失补 ~1.5 L → 约 **1.5 L**（含电解质）；青少年 50 kg 在 40–60 kg 间插值 → 约 **7 fl oz（≈207 mL）/20 min**。
  - observed: 汗液率 1.3 L/h、体重损失 1.43%、补液 1.5 L、青少年 7 fl oz/20 min 均可核对。
- **V3_task_utility**: passed: true — 把补水从「多喝水」变成「测出汗率→分时段定量补液」的可执行处方，并以体重法替代不可靠的尿色/USG 急性判读（ce10-01），同时用「补液不超过出汗量」防止低钠血症（ce10-02）。
- **decision**: verified
- **if_not_verified**: —

---

## 能力单元 U10 — 赛前/赛中/赛后竞赛营养策略（时间线 + 碳水负荷 + 补糖补蛋白）

- **proposed_capability_id**: cap.nsca.competition-nutrition-timeline
- **proposed_slug**: competition-nutrition-timeline
- **type**: framework
- **merged_candidates**: [f11-01, p11-01, p11-02, p11-03, p11-04, p11-05, p11-06, p11-07, p11-08, p11-09, p11-10, p11-11, p11-28, c11-01, ce11-03]
- **task_ids**: [T33]
- **importance**: medium
- **source_evidence**:
  - source_id: src-nsca-essentials-5e
    location: Chapter 11（ch11.txt 第 203–229 行 Table 11.1 赛前档；第 292–300 行碳水负荷；第 534/683 行赛中 28–144 g/h；第 720 行赛后补糖；第 880–888 行蛋白/亮氨酸）
- **R 段可用原文引用**（英文，≤100 词，逐字）:
  > "three days of a high-carbohydrate diet in concert with tapering exercise the week before competition and complete rest the day before the event. The diet should provide ... 8 to 10 grams of carbohydrate per kilogram body weight ... increase muscle glycogen stores 20% to 40% above normal." / "a carbohydrate intake ranging from 28 to 144 grams per hour ... during an aerobic endurance activity."（ch11.txt 292–300, 534）
- **V1_source_sufficiency**: passed: true — 回查 Table 11.1（1 h:0.5、2 h:1、≥4 h:1–4 g 碳水/kg + 0.15–0.25 g 蛋白/kg；203–229）、碳水负荷 8–10 g/kg（马拉松 10–12、女性总热量需 >2,400 kcal，ch11.txt 361）、赛中 28–144 g/h、运动饮料 >8% 延迟胃排空、碳水漱口 2%–3%、赛后 1.0–1.85 g/kg/h（第 720 行）、赛前 GI 清单与糖醇警示、赛后蛋白 ≥20–50 g（老 40 g）均具文可查（ce11-03、c11-01 一致）。**原文缺/限定**：Table 11.1 仅针对有氧耐力（注明可适配他项，无力量/团队独立档）；漱口碳水缺浓度/频次——已在 V2 限定。
- **V2_executability**: passed: true
  - check_mode: walkthrough
  - input: 新输入＝70 kg 马拉松运动员，赛前 4 h 进食、赛中 3.5 h、赛后需在 6 h 内恢复。
  - expected: (a) 赛前 4 h：碳水 1–4 g/kg = **70–280 g** + 蛋白 0.15–0.25 g/kg = **10.5–17.5 g**、极低脂低纤；(b) 前一周减量 + 3 天 8–10 g/kg 负荷 = **560–700 g/天**（女性需总热量 >2,400 kcal）；(c) 赛中 28–144 g/h（多类型碳水）；天气热用含钠 20–30 mEq/L 饮料；(d) 赛后 1.0–1.85 g/kg/h = **70–130 g/h**，每 15–60 min 一次至 ≤5 h，配 20–40 g 优质蛋白。
  - observed: 各时间窗碳水/蛋白量均可算出且与原文档位一致，输出含剂量、时机、成分三要素。
- **V3_task_utility**: passed: true — 把赛前/赛中/赛后收敛为一条可套用的时间线，避免「临场随意吃喝」；并用「先练后赛/糖醇/高脂高纤」清单识别失败边界（ce11-03）。
- **decision**: verified
- **if_not_verified**: —

---

## 能力单元 U11 — 体成分改变（增重/减脂）干预

- **proposed_capability_id**: cap.nsca.body-composition-intervention
- **proposed_slug**: body-composition-intervention
- **type**: framework
- **merged_candidates**: [f11-02, p11-14, p11-15, p11-26, p11-27, ce11-02]
- **task_ids**: [T33]
- **importance**: medium
- **source_evidence**:
  - source_id: src-nsca-essentials-5e
    location: Chapter 11（ch11.txt 第 1263 行 +500 kcal；第 1337 行减脂蛋白；第 1380–1382 行肥胖目标/目标体重）
- **R 段可用原文引用**（英文，≤100 词，逐字）:
  > "consume approximately 500 additional calories per day in order to gain weight ... 1.8 to 2.7 grams protein per kilogram body weight per day ... in addition to maintaining a moderate energy deficit of approximately 500 calories per day."（ch11.txt 1263, 1337）
- **V1_source_sufficiency**: passed: true — 回查：增重 +500 kcal/天 + 蛋白 1.6–2.2 g/kg + 可辅一水肌酸；减脂蛋白 1.8–2.7 g/kg（或 ~2.3–3.1 g/kg FFM）+ ~500 kcal 缺口；超重/肥胖 6 个月减 10% 初始体重；目标体重式（ch11.txt 1381）均具文。ce11-02（饮食记录扰乱进食）与原文「记录会改变真实进食」一致，作为估算陷阱纳入。
- **V2_executability**: passed: true
  - check_mode: walkthrough
  - input: 新输入＝85 kg 运动员、体脂 20%（FFM=68 kg），目标增肌。
  - expected: (a) 每日 +500 kcal；(b) 蛋白 1.6–2.2 g/kg = **136–187 g/天**；(c) 可选一水肌酸；(d) 用目标体重式核对目标体脂（如目标 15% → 68/(1−0.15)=80 kg 去脂体重占比口径）。
  - observed: 产出 +500 kcal 增量、蛋白区间、肌酸建议与目标体重核算，均明确。
- **V3_task_utility**: passed: true — 把增重/减脂统一到「先估能量需求→按目标调 ±500 kcal + 蛋白档」的框架，识别「无万能饮食、总热量与依从性是关键」的边界（减少重复试错）。
- **decision**: verified
- **if_not_verified**: —

---

## 能力单元 U12 — 能量可用性（EA）与 RED-S 识别（安全相关）

- **proposed_capability_id**: cap.nsca.energy-availability-red-s
- **proposed_slug**: energy-availability-red-s
- **type**: calculation
- **merged_candidates**: [p11-21, p11-22, f11-03, ce11-04]
- **task_ids**: [T34]
- **importance**: high
- **source_evidence**:
  - source_id: src-nsca-essentials-5e
    location: Chapter 11（ch11.txt 第 1490–1500 行 RED-S/EA 阈值；第 1465 行危险减重）
- **R 段可用原文引用**（英文，≤100 词，逐字）:
  > "LEA is quantified by energy availability (EA), calculated as energy intake minus exercise energy expenditure, relative to fat-free mass (FFM). Optimal EA for healthy function is around 45 kilocalories per kilogram FFM per day, while severe perturbations can occur below 30 kilocalories per kilogram FFM per day."（ch11.txt 1497–1500）
- **V1_source_sufficiency**: passed: true — 回查：EA=(摄入−运动消耗)/FFM、最优 ~45、<30 可现严重紊乱、RED-S 由 LEA 引起并累及代谢/月经/骨/免疫/蛋白合成/心血管，均具文（ch11.txt 1490–1500）。**原文缺**：未给运动能量消耗的测算方法与 30–45 过渡区命名——已在 V2 限定（用可直接测量的运动净消耗输入，过渡区按「亚临床/需警惕」表述，不补造临床分级）。ce11-04 提示「识别+转诊，不越界」与原文一致。
- **V2_executability**: passed: true
  - check_mode: walkthrough
  - input: 新输入＝女运动员 60 kg、FFM 48 kg；能量摄入 2200 kcal/天、运动净消耗 700 kcal/天。另设一例：摄入 1800、消耗 900。
  - expected: 例 1：EA = (2200 − 700)/48 = 1500/48 = **31.25 kcal/kg FFM/天**（>30 但 <45 → 亚临床/需警惕，非健康最优）。例 2：EA = (1800 − 900)/48 = 900/48 = **18.75**（<30 → 严重 LEA，红旗，须转诊多学科团队）。容差：±0.5。
  - observed: 两例 EA 分别 31.25 与 18.75，可据 45/<30 阈值明确判定「警惕」与「转诊」，输出明确。
- **V3_task_utility**: passed: true — 提供把「训练量过大/吃得不够」量化为 EA 的方法与「45/30」硬阈值，使教练能稳定识别并升级到转诊（安全底线，减少重大漏诊）。
- **decision**: verified
- **if_not_verified**: —

---

## 能力单元 U13 — 进食障碍与快速减重识别与转诊（安全相关）

- **proposed_capability_id**: cap.nsca.eating-disorder-rwl-referral
- **proposed_slug**: eating-disorder-rwl-referral
- **type**: troubleshooting
- **merged_candidates**: [p11-23, p11-24, p11-25, f11-03, ce11-04, ce11-01]
- **task_ids**: [T34]
- **importance**: high
- **source_evidence**:
  - source_id: src-nsca-essentials-5e
    location: Chapter 11（ch11.txt 第 1465 行 RWL 危险手段；第 1702 行「不诊断/不治疗」职责边界）
- **R 段可用原文引用**（英文，≤100 词，逐字）:
  > "Potentially dangerous weight loss techniques may include fasting, fad diets, voluntary dehydration (diuretics, sauna, water and salt manipulation, wearing multiple layers of clothing), excessive spitting, self-induced vomiting, laxative abuse ... It is not the responsibility of the strength and conditioning professional to treat or diagnose an eating disorder."（ch11.txt 1465, 1702）
- **V1_source_sufficiency**: passed: true — 回查：进食障碍各亚型信号（神经性厌食/贪食/暴食障碍/ARFID/异食癖/反刍）、失调进食信号（限制、禁食、跳餐、减肥药/泻药/利尿剂）、危险减重手段清单、多学科团队与「教练不诊断不治疗、须建转诊网络」的职责边界均具文。ce11-04/ce11-01 与原文一致。
- **V2_executability**: passed: true
  - check_mode: walkthrough
  - input: 新输入＝有一场比赛前 2 周、男摔跤运动员自述「靠桑拿 + 多层衣物在 3 天内掉 4 kg」，并出现跳餐。
  - expected: (a) 对照红旗清单识别危险减重（主动脱水/跳餐）；(b) 不自行干预，记录并通知教练组；(c) 转介队医/注册营养师/心理团队；(d) 与专业人员共同设定安全体重目标；(e) 若无法安全达标 → 建议考虑改换体重级别。
  - observed: 可完整产出 (a)–(e)，落在「识别—记录—转诊—重评级别」路径内。
- **V3_task_utility**: passed: true — 把高死亡风险的进食障碍/危险减重纳入可执行的转诊路径，明确教练边界，防止越界处置（安全底线）。
- **decision**: verified
- **if_not_verified**: —

---

## 能力单元 U14 — 营养评估口径、膳食换算与转诊边界

- **proposed_capability_id**: cap.nsca.nutrition-assessment-referral
- **proposed_slug**: nutrition-assessment-referral
- **type**: procedure
- **merged_candidates**: [f10-01, p10-01, p10-05, p10-13, p10-14, p10-15, p10-23, p10-24, p10-25, p10-26, p10-27, p10-28, ce11-02]
- **task_ids**: [T32, T33]
- **importance**: medium
- **source_evidence**:
  - source_id: src-nsca-essentials-5e
    location: Chapter 10（ch10.txt 第 489 行 AMDR；第 919 行纤维；第 1140–1143 行饱和脂肪/添加糖；第 1274–1282 行 Table 10.12 血脂；第 1896 行钙）
- **R 段可用原文引用**（英文，≤100 词，逐字）:
  > "athletes with complex nutrition issues should be referred to the appropriate resource, either a team physician or sports dietitian. The team physician is responsible for overseeing the athlete's medical care while the sports dietitian is responsible for providing individualized dietary advice."（ch10.txt）
- **V1_source_sufficiency**: passed: true — 回查：营养转诊职责边界、蛋白 AMDR 成人 10%–35%、纤维（女 21–25、男 30–38 g/天）、饱和脂肪 <10%、添加糖 ≤10%（ch10.txt 1140–1143）、Table 10.12 血脂分类（<100 optimal 等，第 1274 行；9–12 h 空腹）、Table 10.8/10.11 食物换算、铁（heme 15%–35%/nonheme 2%–20%）与钙补充转诊、公卫关注营养素（纤维/维 D/钙/钾）均具文。**原文缺**：食物成分表为节选、缺整表——本单元只承载「查表换算 + 转诊」流程，不补全表数据。
- **V2_executability**: passed: true
  - check_mode: walkthrough
  - input: 新输入＝一名自述「想补铁提高耐力」的女运动员，教练非临床人员。
  - expected: (a) 一般性问题由教练给基本教育；(b) 铁补充属仅医生/注册营养师可推荐（p10-25）→ 转诊；(c) 若问题超出基本范畴（贫血/疾病）→ medical nutrition therapy 归运动营养师；(d) 记录并发起转诊，不自行开方。
  - observed: 明确路由到「医生/注册营养师」，教练不越界，输出为转诊动作清单。
- **V3_task_utility**: passed: true — 统一膳食换算与阈值口径，并把「何时须转诊」写死（减少越界与漏转，稳定交付格式）。
- **decision**: verified
- **if_not_verified**: —

---

## 能力单元 U15 — 增补剂证据评估框架（合法性×安全性×有效性×必要性）

- **proposed_capability_id**: cap.nsca.supplement-evidence-evaluation
- **proposed_slug**: supplement-evidence-evaluation
- **type**: framework
- **merged_candidates**: [f12-01, p12-01, ce12-01, ce12-05]
- **task_ids**: [T35]
- **importance**: medium
- **source_evidence**:
  - source_id: src-nsca-essentials-5e
    location: Chapter 12（ch12.txt 第 501–633 行；ce12-01 引原文「no complete list of banned substances」）
- **R 段可用原文引用**（英文，≤100 词，逐字）:
  > "it is imperative that the athlete become informed about the legality of these substances, understand the potential risks associated with consumption, and know whether scientific research supports the claims (i.e., the efficacy of the product)." / "An athlete's first priority should be to apply sound principles of training, including adequate nutrition, before using any nutritional supplement or ergogenic aid."（ch12.txt）
- **V1_source_sufficiency**: passed: true — 回查：四维（必要性/合法性/安全性/有效性）、「禁用清单不完备、化学相关物亦禁」、污染致误服、先训练营养后补剂的优先级均具文。ce12-01（勿凭标签/清单判安全）、ce12-05（勿先上补剂）与原文一致。
- **V2_executability**: passed: true
  - check_mode: walkthrough
  - input: 新输入＝运动员询问「某网售 SARMs 产品能否用于增肌」。
  - expected: 依四步判定——(1) 必要性：训练/营养是否已到位；(2) 合法性：SARMs 属 WADA 赛内赛外全禁、无 FDA 批准 → 不合法；(3) 安全性：掺假率高、心血管/肝风险；(4) 有效性：非批准药、运动人群证据不足 → **结论：不推荐**。
  - observed: 四维均给出明确「否」，输出为「拒绝 + 先优化训练与营养 + 必要时转介营养专家」。
- **V3_task_utility**: passed: true — 把「要不要用补剂」变成可复用的四维决策，稳定拒答/接受口径，减少被夸大宣称误导（改善决策结构）。
- **decision**: verified
- **if_not_verified**: —

---

## 能力单元 U16 — 增补剂/激素滥用迹象识别与转诊（安全相关）

- **proposed_capability_id**: cap.nsca.ergogenic-abuse-identification
- **proposed_slug**: ergogenic-abuse-identification
- **type**: checklist
- **merged_candidates**: [f12-02, p12-03, p12-06, p12-07, p12-08, p12-12, p12-13, p12-15, ce12-02, ce12-03]
- **task_ids**: [T35]
- **importance**: medium
- **source_evidence**:
  - source_id: src-nsca-essentials-5e
    location: Chapter 12, Table 12.2（ch12.txt 第 699–737 行，逐系统体征）
- **R 段可用原文引用**（英文，≤100 词，逐字）:
  > "TABLE 12.2 Signs and Symptoms of Ergogenic Aid Abuse ... Cardiovascular: Lipid profile changes, Elevated blood pressure, Decreased myocardial function ... Endocrine: Gynecomastia, Decreased sperm count, Testicular atrophy ... Musculoskeletal: Premature epiphyseal plate closure, Increased risk of tendon tears ... Psychological: Mania, Depression, Aggression, Hostility, Mood swings"（ch12.txt 699–737）
- **V1_source_sufficiency**: passed: true — 回查 Table 12.2 逐行（心血管/内分泌/泌尿生殖/皮肤/肝/肌骨/心理）与逐项一致；类固醇用药模式（stacking/cycling/pyramid）、剂量量级（Dianabol 替代 15 mg/天 vs 自述 300 mg/天；典型 3.1 种药、5–10 周、5–29×替代剂量）、HGH 肢端肥大、EPO（Hb +5%–17%、Hct +8%–19%、VO2max/最大功率 +7%–10%）均具文。ce12-02（勿假定运动员剂量 HGH 无害）、ce12-03（EPO 心血管风险）一致。
- **V2_executability**: passed: true
  - check_mode: walkthrough
  - input: 新输入＝一名男运动员近期出现痤疮加重、情绪攻击性、睾酮抑制样表现与注射痕迹。
  - expected: 逐系统对照 Table 12.2 收集体征 → 结合行为线索（情绪波动、注射痕迹、秘密性）→ 得「疑似使用」警觉清单 → 依机构政策与医疗团队沟通/转诊，**不自行诊断**。
  - observed: 可产出按系统分列的可疑体征清单与转诊触发，落点在「提高警觉 + 转介」，非确诊。
- **V3_task_utility**: passed: true — 把散在的滥用体征固化为逐系统清单，提供可检查的转诊触发依据（减少遗漏、识别失败边界）。
- **decision**: verified
- **if_not_verified**: —

---

## 能力单元 U17 — 增能剂证据分级与剂量处方

- **proposed_capability_id**: cap.nsca.ergogenic-dosing-evidence
- **proposed_slug**: ergogenic-dosing-evidence
- **type**: recommendation
- **merged_candidates**: [p12-16, p12-17, p12-18, p12-19, p12-20, p12-21, p12-22, p12-23, p12-24, p12-25, p12-26, p12-27, p12-28, p12-29, p12-30, ce12-04]
- **task_ids**: [T35]
- **importance**: medium
- **source_evidence**:
  - source_id: src-nsca-essentials-5e
    location: Chapter 12（ch12.txt 第 1831–1839 行肌酸；第 1978/2015/2035 行咖啡因；第 1694 行碳酸氢钠；第 1469–1483 行精氨酸不推荐）
- **R 段可用原文引用**（英文，≤100 词，逐字）:
  > "a loading dose of 20 to 25 grams daily for five days, or 0.3 grams per kilogram body mass ... followed by a maintenance dose of 2 grams per day" / "In doses of 3 to 9 milligrams per kilogram body weight consumed approximately 60 minutes before exercise ... caffeine is ergogenic." / "oral arginine supplementation is not recommended for healthy athletes."（ch12.txt 1831, 2015, 1483）
- **V1_source_sufficiency**: passed: true — 回查：肌酸（负荷 20–25 g×5 天或 0.3 g/kg；维持 2 g/天或 0.03 g/kg；饱和 150–160 mmol/kg 干重）、咖啡因（3–9 mg/kg、赛前 ~60 min、≥9 mg/kg 无额外收益、致死 >5 g≈42 杯）、β-丙氨酸（4–6 g/天、>60 s 高酸中毒、感觉异常）、碳酸氢钠（0.3–0.5 g/kg、60–180 min）、HMB（3–6 g/天）、EAA/亮氨酸（2–3 g 亮氨酸或 0.05 g/kg）、精氨酸不推荐（6 g 无效、13–30 g 胃肠不适）、柠檬酸钠（0.44 g/kg；证据不一致）、L-肉碱（2–3 g/天）、麻黄碱+咖啡因（禁用）、酒精（每 g 乙醇多产尿 ~10 mL、标准杯 14 g）均具文。**原文缺**：部分为剂量区间无最优值（候选已标注），V2 只做区间处方。ce12-04 一致。
- **V2_executability**: passed: true
  - check_mode: walkthrough
  - input: 新输入＝70 kg 力量运动员，训练与营养已到位，询问肌酸与咖啡因用法。
  - expected: 肌酸：负荷 20–25 g/天×5 天（或 0.3×70=21 g/天），维持 2 g/天（或 0.03×70=2.1 g/天）；咖啡因：3–9 mg/kg = **210–630 mg**，赛前约 60 min；提示 >9 mg/kg 无额外收益、致死 >5 g。二者证据等级：肌酸「最强」，咖啡因「耐力有效、爆发不确定」。
  - observed: 剂量可算出且落在原文区间，输出含剂量-时机-证据等级，与原文一致。
- **V3_task_utility**: passed: true — 把「某补剂有没有用、吃多少」固化为可查的证据分级 + 剂量口径，稳定给运动员/家长的答复（减少重复查证）。
- **decision**: verified
- **if_not_verified**: —

---

## 能力单元 U18 — 禁用物质名称与剂量口径参照（reference）

- **proposed_capability_id**: cap.nsca.banned-substance-reference
- **proposed_slug**: banned-substance-reference
- **type**: reference
- **merged_candidates**: [p12-02, p12-04, p12-05, p12-09, p12-10, p12-11, p12-14]
- **task_ids**: [T35]
- **importance**: low
- **source_evidence**:
  - source_id: src-nsca-essentials-5e
    location: Chapter 12, Table 12.1/12.3/12.4（ch12.txt；SARMs/肽类/类固醇名称表）
- **R 段可用原文引用**（英文，≤100 词，逐字）:
  > "TABLE 12.1 Generic and Trade Names of Anabolic Steroids Commonly Used by Athletes ... TABLE 12.3 Example Selective Androgen Receptor Modulators (SARMs) ... TABLE 12.4 Example Peptide Hormone Classes and Specific Peptides"（ch12.txt）
- **V1_source_sufficiency**: passed: true — 回查：类固醇通用名/商品名对照（Table 12.1）、SARMs 名（Table 12.3、无 FDA 批准、WADA 全禁、44 产品掺假统计 52%/59%/39%）、肽类激素（Table 12.4）、睾酮前体活性（雄烯二酮 1/5、DHEA 1/10）与效能结论、β 阻滞剂射击（oxprenolol 80 vs 40 mg）均具文。均为**名称/剂量参照**，非可执行方法。
- **V2_executability**: passed: false — 名称对照与描述性剂量统计，单用不产生可执行动作/可核对结果（提供识别素材）。
- **V3_task_utility**: passed: true（参考价值）— 供识别/教育与反兴奋剂培训查名，避免误用禁药名称。
- **decision**: reference
- **if_not_verified**: 并入 `book/glossary.md`（禁用物质名称与类别对照）与 `book/overview.md` 参考区，审计登记；阶段 2 不单独建卡。canonical 保留 p12-03（滥用体征）在本簇 U16。

---

## 能力单元 U19 — 唤醒调控与心理技能（理论 + 降唤醒技术 + 目标设定 + 自我效能）

- **proposed_capability_id**: cap.nsca.arousal-psych-skills
- **proposed_slug**: arousal-psych-skills
- **type**: framework
- **merged_candidates**: [f09-01, p09-01, p09-02, p09-03, p09-04, p09-05, p09-06, p09-07, p09-08, p09-09, p09-10, p09-11, p09-12, p09-13, p09-14, p09-15, p09-16, p09-17, p09-32, ce09-01]
- **task_ids**: [T36]
- **importance**: medium
- **source_evidence**:
  - source_id: src-nsca-essentials-5e
    location: Chapter 9（ch09.txt 第 816–819 行唤醒调向；第 736 行 PMR；第 756–758 行自生训练；第 834 行意象；第 897–904 行自我效能六来源）
- **R 段可用原文引用**（英文，≤100 词，逐字）:
  > "An athlete should employ arousal reduction techniques when performing a new skill or one that is complex or when performing in high-pressure situations. Athletes should employ arousal enhancement techniques when executing simple skills, ones that are well learned, or in situations of minimal pressure."（ch09.txt 816–819）
- **V1_source_sufficiency**: passed: true — 回查：倒 U/IZOF/灾难/逆转理论、降唤醒 vs 升唤醒判据、PMR（10–15 s 最大紧张 + 完全放松、赛前数日练）、腹式呼吸、自生训练（温暖与沉重）、系统脱敏（恐惧层级 + 放松）、意象（由静态到动态、内/外视角）、自我效能六来源、目标设定四准则/过程 vs 结果、正强化优先于惩罚，均具文可查。ce09-01 一致。
- **V2_executability**: passed: true
  - check_mode: walkthrough
  - input: 新输入＝一名技术熟练但比赛发挥不稳的飞镖运动员，赛前自觉「手抖、焦虑」。
  - expected: (a) 判定技能＝已熟练、任务需精细稳定 → 用**降唤醒**技术；(b) 选 PMR（10–15 s 紧张/放松循环）与腹式呼吸；(c) 赛前数日练习、非比赛当天首用；(d) 用系统脱敏 + 意象预演高压情境；(e) 设过程目标（如「每次出手都做完呼吸节律」）而非结果目标。
  - observed: 可产出降唤醒技术组合 + 目标设定清单，输出与原文判据一致（熟练技能 → 降唤醒；高压力 → 降唤醒）。
- **V3_task_utility**: passed: true — 把「紧张怎么办」变成可选的降/升唤醒技术菜单与目标设定模板，稳定交付赛前心理方案（统一口径、稳定格式）。
- **decision**: verified
- **if_not_verified**: —

---

## 能力单元 U20 — 动作技能教学与实践安排

- **proposed_capability_id**: cap.nsca.motor-skill-teaching
- **proposed_slug**: motor-skill-teaching
- **type**: framework
- **merged_candidates**: [f09-03, p09-21, p09-22, p09-23, p09-24, p09-25, p09-26, p09-27, p09-28, c09-01, ce09-02]
- **task_ids**: [T36]
- **importance**: medium
- **source_evidence**:
  - source_id: src-nsca-essentials-5e
    location: Chapter 9（whole/part、练习次序、指导风格、反馈、提示语 sidebar）
- **R 段可用原文引用**（英文，≤100 词，逐字）:
  > "tasks that are challenging but have low interrelatedness of the subcomponents are learned better with part practice ... whole practice would tend to be favored for a task with subcomponents that are highly interrelated ... in instances in which the skill may be dangerous or costly to learn as a whole, part practice is the favored choice."（ch09.txt）
- **V1_source_sufficiency**: passed: true — 回查：whole vs part 判据（关联度/危险度）、segmentation/fractionalization/simplification 与 pure/progressive/repetitive part、blocked vs random（可混合）、variable practice、观察学习、三种指令风格、反馈时机/频率（同步=表现、延迟=学习；低频率更利于学习，复杂技能例外）、提示语简短与 verbal overshadowing、内/外部提示时序、指导性自我对话对专家有害（ce09-02）均具文。c09-01（Gayle Hatch 提示语）为原文案例。
- **V2_executability**: passed: true
  - check_mode: walkthrough
  - input: 新输入＝教一名新手学习抓举（snatch，危险且子成分多）。
  - expected: (a) 因危险且子成分可分段 → 用 **part practice + simplification**（如先用 PVC 管/轻负荷）；(b) 拆为 first pull/transition/second pull/catch 四段；(c) 用 progressive-part 重组；(d) 新手用 guided discovery、低压；成熟后用 explicit；(e) 反馈：初期较密、逐步稀疏；(f) 提示语简短、优先外部提示。
  - observed: 可产出分解方式 + 重组次序 + 指导/反馈/提示语安排，落点在具体教学决策。
- **V3_task_utility**: passed: true — 把「怎么教动作」变成可复用的分解/练习/反馈决策树，减少新手学习中的过载与安全风险（识别失败边界）。
- **decision**: verified
- **if_not_verified**: —

---

## 能力单元 U21 — 心理健康红旗识别与三步转诊（安全相关）

- **proposed_capability_id**: cap.nsca.mental-health-referral
- **proposed_slug**: mental-health-referral
- **type**: troubleshooting
- **merged_candidates**: [f09-02, p09-18, p09-19, p09-20, p08-09]
- **task_ids**: [T36]
- **importance**: high
- **source_evidence**:
  - source_id: src-nsca-essentials-5e
    location: Chapter 9（ch09.txt 第 1272 行 2–3 周阈值；第 1304–1307 行转诊对象分层）
- **R 段可用原文引用**（英文，≤100 词，逐字）:
  > "First, identify the signs and symptoms of distress related to affect, behavior, and cognitions. Second, determine the duration of distress (lasting greater than 2-3 weeks) and potential disruption ... Third, determine how to support the athlete."（ch09.txt 1272）
- **V1_source_sufficiency**: passed: true — 回查：三步流程（识别 ABC 迹象 → 判断 >2–3 周与功能干扰 → 决定支持层级）、Table 9.1 焦虑/抑郁/压力体征症状清单、转诊对象分层（performance coach / counselor / psychologist）、女性心理健康风险（抑郁 2×、2021 焦虑 40% vs 22%）均具文。
- **V2_executability**: passed: true
  - check_mode: walkthrough
  - input: 新输入＝一名运动员连续 3 周情绪低落、睡眠紊乱、对训练失去兴趣。
  - expected: (a) Step 1 识别 ABC：Affect（低落）、Behavior（社交隔离）、Cognitions（无望/反刍）；(b) Step 2 持续 >2–3 周 + 干扰睡眠/社交 → 超阈值；(c) Step 3 判定需转诊 → 转介 counselor/psychologist，并通知运动医学团队、保密沟通；(d) 教练不越界做临床处理。
  - observed: 三步均可执行，判据（>2–3 周 + 功能外溢）明确触发转诊，输出为「支持路径 + 转诊对象」。
- **V3_task_utility**: passed: true — 给出「何时该转诊」的硬阈值与分流对象，把教练角色限定在识别与升级（安全底线、稳定分流）。
- **decision**: verified
- **if_not_verified**: —

---

## 能力单元 U22 — 伤后重返训练的心理支持

- **proposed_capability_id**: cap.nsca.injury-return-psych-support
- **proposed_slug**: injury-return-psych-support
- **type**: procedure
- **merged_candidates**: [f09-04, p09-29, p09-30, p09-31, ce09-03]
- **task_ids**: [T36]
- **importance**: medium
- **source_evidence**:
  - source_id: src-nsca-essentials-5e
    location: Chapter 9（stress-injury model、cognitive appraisal model、体能教练六项行动 sidebar）
- **R 段可用原文引用**（英文，≤100 词，逐字）:
  > "strength and conditioning professionals should maintain regular communication with all athletic trainers, position coaches, parents (if appropriate), and head coaches ... every effort should be made to customize the training program to accommodate the athlete's current abilities and limitations."（ch09.txt）
- **V1_source_sufficiency**: passed: true — 回查：压力—损伤模型三类因素（人格/应激源史/应对资源）、认知评估模型四维（个人/情境/行为/情绪）、体能教练六项行动（沟通、定制、里程碑目标、从一对一过渡到团队、提升自我效能）均具文。ce09-03（心理与身体恢复不同步）一致。
- **V2_executability**: passed: true
  - check_mode: walkthrough
  - input: 新输入＝一名 ACL 术后 3 个月、身体已放行但明显怕再伤的足球运动员。
  - expected: (a) 与运动医学队/教练/家长定期沟通，掌握康复各阶段；(b) 按当前能力订制动作/节奏/器械；(c) 设可控目标（「今天来了吗/做了 10 次吗」）并肯定里程碑；(d) 从一对一渐进到团队活动；(e) 营造心理安全、支持自主环境，降低恐惧。
  - observed: 可产出个体化康复训练 + 沟通计划 + 目标设定 + 过渡路径，落点明确。
- **V3_task_utility**: passed: true — 把「身体过关就上场」改为兼顾心理准备的支持流程，减少再伤与表现波动（识别失败边界）。
- **decision**: verified
- **if_not_verified**: —

---

## 能力单元 U23 — 停训（detraining）时间进程与应对

- **proposed_capability_id**: cap.nsca.detraining-assessment
- **proposed_slug**: detraining-assessment
- **type**: framework
- **merged_candidates**: [f05-01, p05-23, p05-24, p06-16, p06-17, p07-10, p07-22]
- **task_ids**: [T30]（支持；原属 Ch5/6/7 可逆性）
- **importance**: medium
- **source_evidence**:
  - source_id: src-nsca-essentials-5e
    location: Chapter 5（ch05.txt 第 1598–1629 行）；Chapter 6（ch06.txt 第 1243–1270 行）；Chapter 7（ch07.txt 第 532 行 67% 频率效应）
- **R 段可用原文引用**（英文，≤100 词，逐字）:
  > "Strength performance in general is readily maintained for up to four weeks of inactivity ... maximal oxygen uptake is reduced 4% to 14% with short-term and 6% to 20% with long-term detraining ... Detraining is defined as the partial or complete loss of training-induced adaptations in response to an insufficient training stimulus."（ch05.txt 1598; ch06.txt 1243–1270）
- **V1_source_sufficiency**: passed: true — 回查：抗阻力量 4 周内基本维持、8–12 周损失 7%–12%、停训 14 天快肌 CSA ↓6.4%；有氧 VO2max 短期 −4%–14%、长期 −6%–20%；detraining vs tapering 定义；青少年停训回落到对照且 1×/周仅 67% 增益；老年人骨适应停训 >6 个月丢失，均具文可查。
- **V2_executability**: passed: true
  - check_mode: walkthrough
  - input: 新输入＝一名高水平运动员因伤完全停训 6 周。
  - expected: 判定为 detraining（非 tapering，因刺激不足且未保留强度）→ 预期：力量在 4 周内基本维持、8–12 周损失约 7%–12%；有氧 VO2max 短期（4 周）−4%–14%、6 周落在此区间；复训回补快（残余效应）。应对：以减量/维持性训练减小损失。
  - observed: 可给出分素质的丢失区间与应对，输出明确可核对（时间窗 4/8–12 周、幅度 7%–12%、−4%–14%）。
- **V3_task_utility**: passed: true — 把「停训会掉多少」变成可按时长×训练状态预测的框架，并区分减量/停训，指导复训与维持（减少遗漏、改善决策）。
- **decision**: verified
- **if_not_verified**: —

---

## 能力单元 U24 — 训练适应幅度参照与高原/热适应选择（reference）

- **proposed_capability_id**: cap.nsca.adaptation-magnitude-reference
- **proposed_slug**: adaptation-magnitude-reference
- **type**: reference
- **merged_candidates**: [p05-01, p05-02, p05-03, p05-04, p05-05, p05-06, p05-07, p05-08, p05-09, p05-10, p05-11, p05-12, p05-13, p05-14, p05-15, p05-16, p05-17, p05-18, p05-19, p05-20, p05-21, p05-22, p05-25, p05-26, p05-27, p05-28, p06-01, p06-02, p06-03, p06-04, p06-05, p06-06, p06-07, p06-08, p06-09, p06-10, p06-11, p06-12, p06-13, p06-14, p06-15, p06-18, p06-19, f06-01, p07-14]
- **task_ids**: []（支持性；原属 Ch5/6/7 与 T13/T17，非本簇 T30–T36 主线）
- **importance**: medium
- **source_evidence**:
  - source_id: src-nsca-essentials-5e
    location: Chapter 5（Table 5.1/5.2 等）；Chapter 6（Table 6.1/6.2、高原/热适应、血液兴奋剂等）
- **R 段可用原文引用**（英文，≤100 词，逐字）:
  > "TABLE 5.2 Physiological Adaptations to Resistance Training" / "At elevations greater than 3,900 feet (1,189 m), acute physiological adjustments begin to occur ..." / "what is going to have the biggest impact on the athlete's performance on race day, altitude or heat?"（ch05.txt; ch06.txt 695; f06-01）
- **V1_source_sufficiency**: passed: true — 回查：抗阻/有氧适应清单（Table 5.2/6.1）、常模表（Table 6.2）、力量增幅按训练状态（40/20/16/10/2%）、峰值功率最优负荷、骨/结缔组织适应阈值与时间进程、能量底物超量恢复、高原急性/慢性阈值（>1,189 m；Hb +5%–15%、RBC +30%–50%、3–6 周）、热适应（~75% 见于 4–6 天、每天无暴露损失 2.5%）、高原 vs 热选择规则、吸烟/血液兴奋剂/高氧等外部因素均具文。均为**幅度/时间进程参照与机制**，非可独立交付的方法步骤。
- **V2_executability**: passed: false — 提供的是适应方向/幅度/时间窗与选择依据的参照值，单用不产生可交付动作或可核对结果；其可执行部分（停训预测、高原/热协议参数）分别落在 U23 与 Ch21（E-aerobic）。
- **V3_task_utility**: passed: true（参考价值）— 为解释「练多久见效、能提升多少、何时逆转」提供统一参照，避免误读短期变化。
- **decision**: reference
- **if_not_verified**: 并入 `book/overview.md` 参考区「训练适应幅度与时间进程」与 `book/glossary.md`（适应方向、高原/热适应阈值、高原 vs 热选择）；审计登记。阶段 2 不单独建卡（detraining 已由 U23 承载）。

---

## 覆盖核查表

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

## 本簇缺口清单

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

## 供阶段 2 的提示（可选）

- 可组合成一张「竞赛营养卡」：U9（补水）+ U10（时间线）+ U11（体成分）共享体重/能量输入，宜联动 R 与 A1。
- U12（EA/RED-S）与 U13（进食障碍/RWL）是安全核心，建议 A1 采用 `ce11-04`（忽视红旗越界处理）作反面素材、`p11-25`（RWL 清单）作 B 段检查表。
- 关键数值演练素材：U9（汗液率 1.3 L/h）、U12（EA 31.25 与 18.75）、U7（Cunningham RMR=1996）可作为 A2 数值例。
- 案例候选 `c07-01`（成熟度 90%）、`c10-01`（NFL 汗流失率）、`c11-01`（80 kg≈1200 g 糖原）、`c09-01`（Hatch 提示语）适合做 A1 情境锚点。
- U6、U18、U24 三条 reference 建议分别并入 glossary 的「性别差异」「禁用物质」「训练适应幅度」三节。


---

<!-- ===== 簇 H-recovery-management ===== -->

# 簇 H-recovery-management — 三重验证结果

- 负责任务: T27, T28, T29, T38, T39
- 候选输入: **163 条** = 簇表 154 条（frameworks-g5 / principles-g5 / counter-examples-g2 的 ce2x 段）+ **9 条案例**（`cases-g2-ch15-26.md` 的 c24-1…4、c25-1…2、c26-1…3；任务书明确要求纳入，但簇表 `_clusters/H-recovery-management.md` 漏列——已在覆盖核查与本文件说明）。
  - 另核对：`frameworks-g4-ch20-22.md` 仅含 f22-09/10/11（GAS、刺激—疲劳—恢复、体能—疲劳范式），**属 B 簇**，本簇不收；`principles-g4-ch20-22.md` 无 Ch24 内容。簇表注记的“g4（Ch24 部分）”经核为误标。
- 归并后能力单元: **16 个**
- verified: **14** / reference: **2** / needs_review: **0** / rejected: **0**

> 校验口径：V1 均回 ch23–ch26 原文核对（引用下方标注 chXX.txt 行号）；V2 为纸面 walkthrough（非宿主执行）；两处交叉提取器重复（framework 与 principle 各提一次）不构成独立证据，已在各单元记明。

---

## 能力单元 U1 — 过度训练/过度劳累的定义与过度训练连续谱判定（FOR→NFOR→OTS）

- **proposed_capability_id**: cap.nsca.overtraining-continuum-classification
- **proposed_slug**: overtraining-continuum-classification
- **type**: framework
- **merged_candidates**: [f24-01, f24-02, p24-01, p24-02, p24-03, p24-04, p24-05, p24-06, c24-3]
- **task_ids**: [T27]
- **importance**: critical
- **source_evidence**:
  - source_id: src-nsca-essentials-5e
    location: Chapter 24, "Overtraining Defined / Overreaching Defined / Overtraining Continuum"（ch24.txt 第 174–214、316–391 行；SOTS/POTS 第 264–314 行）
- **R 段可用原文引用**（英文）:
  > "overtraining is actually the process (e.g., excessively high volumes and intensities of training) that then can result in an overtraining syndrome... To be overtrained, one actually has the OTS and the required long-term performance impairments (i.e., weeks to months or longer). Performance impairments are necessary for overtraining to have occurred."
- **V1_source_sufficiency**: passed: true — 原文给出 ECSS-ACSM 共识定义（OT：long-term decrement，数周至数月；OR：short-term，数天至数周），明确"过程 vs 结果"区分，并给出 FOR（数天–数周恢复 + supercompensation）、NFOR（疲劳更大、恢复更久、无超量恢复）与 SOTS/POTS 分型。定义、分界与判定条件齐全；`p24-03`/`f24-01`、`p24-04` 等处为同机制重复转述，去重后不构成新证据。
- **V2_executability**: passed: true
  - check_mode: walkthrough
  - input: 某短跑运动员在赛前训练营（一日两练）后成绩下降 8%，撤量 1 个减量周后第 10 天成绩**超过**营前基线并出现个人最好成绩。
  - expected: 归类为 **FOR（功能性过度疲劳）**——短期（天/周）降成绩、可获超量恢复，属可用的训练工具。
  - observed: 按 f24-02/p24-04 判据（恢复时长 days–weeks + 是否超量恢复）命中 FOR；无误判为 OTS（OTS 需 weeks–months 且无超量恢复、仅回基线）。输入合法、结论明确。
- **V3_task_utility**: passed: true — 统一 FOR/NFOR/OTS 与 SOTS/POTS 口径，防止把"练得苦"或"一次降成绩"误判为过度训练；为处置与恢复时长预期提供分级锚点。
- **decision**: verified

---

## 能力单元 U2 — 成绩下降归因排查（并非所有下降都是过度训练）

- **proposed_capability_id**: cap.nsca.underperformance-attribution-triage
- **proposed_slug**: underperformance-attribution-triage
- **type**: troubleshooting
- **merged_candidates**: [f24-03, f24-05, p24-19, p24-20, p24-21, ce24-01, ce24-02, ce24-03]
- **task_ids**: [T27]
- **importance**: high
- **source_evidence**:
  - source_id: src-nsca-essentials-5e
    location: Chapter 24, "Underperformance and Its Relation to Overtraining / Allostatic Load / Factors Contributing"（ch24.txt 第 411–539、456–489 行；Figure 24.2 第 106–121 行）
- **R 段可用原文引用**（英文）:
  > "In summary, not all cases of underperformance are due to overtraining or overreaching... One common training error that can be mistaken for overtraining is due to the timing of the training program with the competition schedule... the reality is that inappropriate timing, not excessive training, was the cause."
- **V1_source_sufficiency**: passed: true — 原文明确列出并列排查项：①OT/OR；②训练峰值与比赛日程错配；③训练量不足；④非训练压力（allostatic load：生活/工作/家庭/旅行等）；⑤营养/睡眠。给出 Figure 24.11/24.12 的直接原因（实线）与贡献因素（虚线）。**承认因果方向难辨**（次要因素也可能由 OTS 引起），该局限已入 B 段。
- **V2_executability**: passed: true
  - check_mode: walkthrough
  - input: 某接力队在目标赛前 3 周成绩下降 2%；回顾发现训练峰值被排在赛前 7 周；静息心率与情绪问卷无异常，训练负荷未升高。
  - expected: 归因为**训练—比赛时机错配**（peak 未与出成绩时点对齐），非过度训练；纠偏方向=重排周期化时点。
  - observed: 依 f24-03/p24-19 命中"timing, not excessive training"示例；排除 OT/OR（无超量负荷、无客观指标异常）。结论明确、可核查。
- **V3_task_utility**: passed: true — 提供多因鉴别结构，避免"成绩一降就减量"的单因误判与错误处置。
- **decision**: verified

---

## 能力单元 U3 — 运动员监控计划设计（测试质量 + 指标选择 + 问卷）

- **proposed_capability_id**: cap.nsca.athlete-monitoring-plan-design
- **proposed_slug**: athlete-monitoring-plan-design
- **type**: procedure
- **merged_candidates**: [f24-06, f24-08, p24-07, p24-08, p24-09, p24-10, p24-13, p24-16, ce24-04, ce24-08, ce24-10, c24-4]
- **task_ids**: [T27]
- **importance**: high
- **source_evidence**:
  - source_id: src-nsca-essentials-5e
    location: Chapter 24, "Assessment of Overreaching and Overtraining"（ch24.txt 第 590–921 行；Table 24.1 §608–666、Table 24.2 §705–774、Figure 24.15 §776–817、Table 24.3 §856–921）
- **R 段可用原文引用**（英文）:
  > "Qualities of the tests included in this program must be specific to the training being performed or the physiological system involved (i.e., valid), reliable..., sensitive to the training and competition stimulus, and easy to incorporate into the regular athlete monitoring program. Furthermore, those administering the tests must precisely follow correct protocols and must ensure that each person performing the tests provides a maximal effort."
- **V1_source_sufficiency**: passed: true — 四项测试质量、施测规范、Figure 24.15 监控测试汇总、Table 24.3 问卷清单、6 项问卷选择考量、Table 24.1 敏感度/出现顺序均完整。**子项 `p24-08`（Table 24.2 机制—证据强度）为 reference 级知识表**（不直接驱动动作），`p24-13` 为判读口径规则；均在正文可查。
- **V2_executability**: passed: true
  - check_mode: walkthrough
  - input: 为某大学女子足球队设计"早期发现过度训练"的监控方案。
  - expected: 依四项质量 + Table 24.1 敏感度排序，优先纳入**速度/冲刺（High，1+ 周）与纵跳动力学（High，1 周内）**，加**恢复感知（Very high，数天内）**等主观项；问卷按 6 项考量选取经效度验证且能快速回传者；建立快速数据反馈通道。
  - observed: 依 f24-06/f24-08/p24-07/p24-09/p24-16 生成指标组合与选问卷决策；未纳入 1RM 作为首发预警（敏感度 Low）。方案明确、可核查。
- **V3_task_utility**: passed: true — 统一测试口径与优先级，避免只盯力量、错过速度/功率的早期窗口（ce24-10）与施测不规范导致数据无意义（ce24-04）。
- **decision**: verified
- **if_not_verified**: 不适用。**缺口登记**：Table 24.1 中部分变量（离心力量、多/单关节 RFD 等）敏感度为 Unknown、无变化幅度阈值（见缺口清单 p24-07）。

---

## 能力单元 U4 — 分级检测升级协议（Category I→II→III）

- **proposed_capability_id**: cap.nsca.overtraining-test-escalation
- **proposed_slug**: overtraining-test-escalation
- **type**: troubleshooting
- **merged_candidates**: [f24-07, p24-15]
- **task_ids**: [T27]
- **importance**: medium
- **source_evidence**:
  - source_id: src-nsca-essentials-5e
    location: Chapter 24, "Integrating Recovery Methods…"（ch24.txt 第 1044–1111 行）
- **R 段可用原文引用**（英文）:
  > "It is suggested that category I testing be performed first. If the results suggest possible overtraining concerns, testing for category II is warranted. Likewise, if the category II test suggests an overtraining problem, a category III test may be performed. In this manner, unnecessary testing can be avoided."
- **V1_source_sufficiency**: passed: true — 三级分类定义（频率/复杂度/侵入性/成本/回传速度）与升级规则均完整给出（引 Bernaciková 等）。
- **V2_executability**: passed: true
  - check_mode: walkthrough
  - input: 某运动员 Category I 每日自评（RPE、睡眠、恢复感）连续 5 天恶化趋势。
  - expected: 判为"possible overtraining concern"→升级至 **Category II**（每几天一次的更长问卷，仍要求快速回传），暂不直接上 Category III。
  - observed: 依 f24-07/p24-15 升级逻辑命中 Category II；避免不必要的高侵入/高成本检测。结论明确。
  - 说明：**触发升级的"具体阈值"原文未给**（"possible overtraining concerns"为定性），但升级决策本身可执行。
- **V3_task_utility**: passed: true — 把监控成本/侵入性做成阶梯，减少不必要检测并保留升级路径。
- **decision**: verified

---

## 能力单元 U5 — 过度训练恢复策略选择与恢复时长预期

- **proposed_capability_id**: cap.nsca.overtraining-recovery-strategy
- **proposed_slug**: overtraining-recovery-strategy
- **type**: procedure
- **merged_candidates**: [f24-09, p24-11, p24-17, c24-1, c24-2]
- **task_ids**: [T28]
- **importance**: high
- **source_evidence**:
  - source_id: src-nsca-essentials-5e
    location: Chapter 24, "Recovery Methods and Strategies"（ch24.txt 第 922–1022 行；Table 24.4 §949–1022）
- **R 段可用原文引用**（英文）:
  > "Once overtraining occurs and overtraining syndrome has developed, the first thing that must be done is a careful revision of the training program. A rapid decrease in the training volume, intensity, or both is typically warranted... decreasing or eliminating the training stress is mandatory when overtraining has occurred."
- **V1_source_sufficiency**: passed: true — Table 24.4 按训练因素/恢复手段/饮食补剂/冷冻疗法给出有效性分级（Most strong/Strong/Promising/Possible/Inconclusive），并给分程度恢复时长（超量约 1 周、高强度抗阻可达 4 周、大容量长跑数月至一年）。步骤与时长口径齐全。
- **V2_executability**: passed: true
  - check_mode: walkthrough
  - input: 一名抗阻训练者出现 NFOR：1RM 下降约 8%，减量 1 周未见超量恢复。
  - expected: 第一步**修订训练计划**（降量/降强度，必要时停训）→ 训练减量 taper → 叠加睡眠（Strong）/正念（Promising）/冷水浸泡（Promising）等；恢复时长预期**可达约 4 周**（抗阻）。
  - observed: 依 f24-09/p24-11/p24-17 命中分层方案与 4 周量级预期；"降低或消除训练压力"为强制项。结论明确、可核查。
- **V3_task_utility**: passed: true — 按证据强度分层、以"先改训练"为硬约束，防止把恢复寄托于证据弱的辅助手段。
- **decision**: verified

---

## 能力单元 U6 — 过度训练预防与恢复整合（含负荷变异 %CV 与 >30% 警戒线）

- **proposed_capability_id**: cap.nsca.overtraining-prevention-integration
- **proposed_slug**: overtraining-prevention-integration
- **type**: checklist
- **merged_candidates**: [f24-04, f24-10, p24-12, p24-14, p24-18, ce24-05, ce24-06, ce24-07, ce24-09]
- **task_ids**: [T27, T28]
- **importance**: high
- **source_evidence**:
  - source_id: src-nsca-essentials-5e
    location: Chapter 24, "Factors Contributing… Training Factors" + "Figure 24.16"（ch24.txt 第 426–451、1032–1105 行）
- **R 段可用原文引用**（英文）:
  > "Exercise caution with excessive training volumes and large increases in training volume (>30% increases)... Variation in the training stimulus is critical, and use of periodized training is important. Avoid excessive training to failure." / "Another training error is a lack of variation in the training load... which can be quantified by calculating the coefficient of variation (%CV; SD/ x–)."
- **V1_source_sufficiency**: passed: true — 应激—恢复平衡框架、Figure 24.16 上（可控风险因素）/下（规避行动项）、%CV 定义式均完整。**唯一数值警戒线 >30% 的口径（单周？累计？按何标量）原文未明**，已入缺口清单。
- **V2_executability**: passed: true
  - check_mode: walkthrough
  - input: 为某大学足球队规划季前超负荷阶段。
  - expected: 行动项=周训练量增幅**不超过 >30% 警戒线**（谨慎）、每周至少 1 个完全休息日、限制超长课/一日多课、引入训练变异（用 %CV 量化）与周期化、避免过度力竭、协调各压力源、监控内外部负荷。
  - observed: 依 f24-10/p24-12/p24-14/p24-18 生成可执行预防清单；>30% 作为警戒而非硬阈值使用（口径不明，按原文措辞"caution"）。清单明确。
- **V3_task_utility**: passed: true — 把事前预防固化为可勾选清单，减少遗漏并抓住最好的干预时点（发生之前）。
- **decision**: verified
- **if_not_verified**: 不适用。**缺口登记**：p24-14 ">30%" 口径未明；其余条目为定性建议、无剂量。

---

## 能力单元 U7 — 组织愈合分期与各期目标（含炎症期急性管理）

- **proposed_capability_id**: cap.nsca.tissue-healing-phase-classification
- **proposed_slug**: tissue-healing-phase-classification
- **type**: framework
- **merged_candidates**: [f23-01, f23-02, p23-01, p23-02, p23-03, p23-04, p23-05, p23-06, p23-11, p23-12, p23-20, ce23-01, ce23-02, ce23-03]
- **task_ids**: [T29]
- **importance**: high
- **source_evidence**:
  - source_id: src-nsca-essentials-5e
    location: Chapter 23, "Tissue Healing / Goals of Rehabilitation"（ch23.txt 第 309–546、663–801 行；Table 23.1 §323–333；POLICE/cryo §483–540）
- **R 段可用原文引用**（英文）:
  > "Following injury, all damaged tissues go through the same general phases of healing: inflammation, repair, and remodeling... the phases of healing progress along a continuum with no definitive timelines." / "This phase typically lasts 72 hours following an acute injury but may last longer with a compromised blood supply and more severe structural damage."
- **V1_source_sufficiency**: passed: true — Table 23.1 三阶段可观测特征、各期治疗目标与时长（炎症 72h、修复 72h–2 月、重塑数月–数年）、sidebar 分阶段练习选项、PRICE→POLICE 转变与冷疗剂量（15 min；冷水 <15 °C）均完整。**"重塑期数月至数年"跨度过大且缺个体推算、重返判据数值**（p23-05），已入缺口清单。
- **V2_executability**: passed: true
  - check_mode: walkthrough
  - input: 某运动员踝关节 II 度扭伤后第 6 天，仍有肿胀、发红、压痛。
  - expected: 依 Table 23.1 特征（疼痛/肿胀/发红、胶原合成下降、炎症细胞增多）判为**炎症反应期**；目标=防止新组织被破坏、避免炎症迁延；措施=相对休息 + 被动因子（冰/加压/抬高/电刺激），**受伤区不做主动练习**，维持未伤部位与心肺功能；可循 POLICE（早期无痛活动）并以冰疗 15 min 辅助。
  - observed: 依 f23-01/p23-02/p23-03/p23-06/p23-11/p23-12 得出分期与允许/禁止活动；结论明确、可核查。
- **V3_task_utility**: passed: true — 把主观"疼不疼"转为"处于哪一期 → 可施加何种负荷"的状态判断，防止过早加量（ce23-02/ce23-03 所述失败模式）。
- **decision**: verified
- **if_not_verified**: 不适用。**缺口登记**：p23-05 重塑期时长与重返判据数值缺失（见缺口清单）。

---

## 能力单元 U8 — 按愈合期调整抗阻训练（DAPRE / DeLorme / Oxford + SAID + 神经肌肉控制）

- **proposed_capability_id**: cap.nsca.rehab-resistance-progression
- **proposed_slug**: rehab-resistance-progression
- **type**: calculation
- **merged_candidates**: [f23-06, p23-07, p23-08, p23-09, p23-10, p23-21, c23-1, c23-2, c23-3, c23-4]
- **task_ids**: [T29]
- **importance**: high
- **source_evidence**:
  - source_id: src-nsca-essentials-5e
    location: Chapter 23, "Program Design / Resistance Training"（ch23.txt 第 802–1002 行；Table 23.2 §851–867；Table 23.3 §908–964；神经肌肉控制 §636–661）
- **R 段可用原文引用**（英文）:
  > "The first set requires 10 repetitions of 50% of the estimated 6RM, and the second set requires 6 repetitions of 75% of the estimated 6RM. The third set... requires the maximum number of repetitions of 100% of the estimated 6RM; the number of repetitions performed during the third set determines the adjustment made in resistance for the fourth set (table 23.2)."
- **V1_source_sufficiency**: passed: true — Table 23.2（DAPRE 第 3 组次数→第 4 组与下次阻力调整）、DeLorme/Oxford 3×10 金字塔、SAID 迁移、Table 23.3（愈合期 × 专项：组×次×强度）、神经肌肉控制三变量（面/视觉/速度）均完整。
- **V2_executability**: passed: true
  - check_mode: walkthrough
  - input: DAPRE 估算 6RM = 110 lb，第 3 组实际完成 9 次；另髌股损伤马拉松跑者处于修复期。
  - expected: (a) 第 3 组 9 次落入 Table 23.2 的 **8–12** 行 → 第 4 组**加 5–10 lb**（115–120 lb），**下次课加 5–15 lb**（115–125 lb）；(b) Table 23.3 修复期 → 跑者 **2–3 组 × 15–20 次 @ ≤50% 1RM**。
  - observed: 依 p23-09 命中 8–12 档调整；依 p23-10 命中修复期跑者处方。数值明确，独立复核一致（容差按原文 5 lb 档）。
- **V3_task_utility**: passed: true — 把"按感觉加片"转为可查表的定量进阶规则，统一康复抗阻口径。
- **decision**: verified

---

## 能力单元 U9 — 体能教练的专业边界与转诊（scope of practice）

- **proposed_capability_id**: cap.nsca.rehab-scope-and-referral
- **proposed_slug**: rehab-scope-and-referral
- **type**: framework
- **merged_candidates**: [f23-03, f23-04, f23-05, p23-19, ce23-04]
- **task_ids**: [T29]
- **importance**: critical
- **source_evidence**:
  - source_id: src-nsca-essentials-5e
    location: Chapter 23, "Allied Health Team / Communication"（ch23.txt 第 46–241 行；Figure 23.1 §223–241；Figure 23.2 §278–308）；Chapter 26 scope of practice（ch26.txt 第 407–421、592–630 行）
- **R 段可用原文引用**（英文）:
  > "To accomplish these tasks, the strength and conditioning professional should consult with the athletic trainer to determine which types of exercises are indicated and contraindicated for the specific injury." / "it is not in the strength and conditioning professional's scope of practice... to diagnose or evaluate an individual's medical or health condition."
- **V1_source_sufficiency**: passed: true — 联合健康团队各角色职责、周会沟通问题清单、indication/contraindication 定义与示例（肩前方不稳时卧推禁忌）、Figure 23.1/23.2 表单字段均完整，并跨 Ch26 取得"不得诊断/放行"的执业边界原文。**前提=存在完备医疗团队**（资源匮乏替代路径缺失，已入 B 段）。
- **V2_executability**: passed: true
  - check_mode: walkthrough
  - input: 某运动员前交叉韧带重建术后 3 周，教练要求"开始加全蹲"。
  - expected: 判为**超出体能教练边界**——不自行放行；先咨询 ATC/PT；据禁忌表单评估（Figure 23.1 示例中 full squats 属禁忌）；在许可范围内落实 indications（如上肢抗阻、渐进固定自行车间歇），并做周会同步。
  - observed: 依 f23-03/f23-04/f23-05/p23-19 得出"咨询-转诊-边界内执行"路径；未越界自定医学取舍。结论明确、可核查。
- **V3_task_utility**: passed: true — 明确"谁写什么、谁放行"，降低越界处方与法律风险（安全相关，必须保留）。
- **decision**: verified

---

## 能力单元 U10 — 环境与医疗急症现场识别与处置（热病 / 横纹肌溶解 / 镰状细胞特质 / 低温症）

- **proposed_capability_id**: cap.nsca.exercise-medical-emergency-response
- **proposed_slug**: exercise-medical-emergency-response
- **type**: troubleshooting
- **merged_candidates**: [f23-08, f23-09, f23-10, f23-11, p23-13, p23-14, p23-15, p23-16]
- **task_ids**: [T29]
- **importance**: high
- **source_evidence**:
  - source_id: src-nsca-essentials-5e
    location: Chapter 23, "Medical Conditions"（ch23.txt 第 1072–1263 行）
- **R 段可用原文引用**（英文）:
  > "core body temperatures in excess of 109.4 °F (43 °C) have been associated with death. Immediate total body cooling measures must be implemented such as total body immersion in ice." / "If rhabdomyolysis is suspected, immediately discontinue activity, lie the client down, implement proper hydration protocols, and closely monitor..."
- **V1_source_sufficiency**: passed: true — 热病连续谱（热痉挛→晕厥→衰竭→中暑）四级的症状与处置、横纹肌溶解识别/处置/预防、SCT 镰变诱因与预防（强度≤无氧阈）、低温症阈值（<35 °C；<32 °C 可致心血管衰竭）均完整给出。
- **V2_executability**: passed: true
  - check_mode: walkthrough
  - input: 八月中，某橄榄球运动员训练中出现意识改变、核心体温 41 °C、皮肤灼热。
  - expected: 判为**热射病（医疗急症）**→立即**全身冰浴降温** + 持续监测核心体温 + 呼叫 EMS（无随队医疗时）；不采用仅"强制风/喷温水"的较轻措施。
  - observed: 依 f23-08/p23-15 命中热射病处置阶梯；并据连续谱前置识别（热衰竭未控即进展）。结论明确、可核查。
- **V3_task_utility**: passed: true — 把致命急症前驱信号转为可执行的分级识别+现场动作，缩短识别与降温时延。
- **decision**: verified
- **if_not_verified**: 不适用。**缺口登记**：补液量、降温目标温度、发病环境温湿度阈值原文未给（分级间无连续温度切点，仅保温衰竭上限 40.5 °C 与中暑致死相关 43 °C）。

---

## 能力单元 U11 — 降低初伤/再伤风险与重返运动判据

- **proposed_capability_id**: cap.nsca.reinjury-risk-and-return-to-play
- **proposed_slug**: reinjury-risk-and-return-to-play
- **type**: framework
- **merged_candidates**: [f23-07, p23-17, p23-18, ce23-05]
- **task_ids**: [T29]
- **importance**: medium
- **source_evidence**:
  - source_id: src-nsca-essentials-5e
    location: Chapter 23, "Reducing Risk of Injury and Reinjury"（ch23.txt 第 1003–1066 行）
- **R 段可用原文引用**（英文）:
  > "Previous injury is one of the most substantial risk factors for future injury in active individuals... Side-to-side differences of less than 10% in strength and functional performance may be considered acceptable."
- **V1_source_sufficiency**: passed: true — 上肢/下肢风险因素清单、结构化预防项目（Sportsmetrics、PEP、Throwers Ten、离心防腘绳肌伤）、对侧差异 **<10%** 判据均给出。**<10% 来自单一引用、样本人群与测试协议未明**，已入缺口清单。
- **V2_executability**: passed: true
  - check_mode: walkthrough
  - input: 某运动员 ACLR 术后 9 个月，等速股四头肌峰力矩较健侧差 14%，单腿跳差 12%。
  - expected: 双侧差异 **>10%** → **不可接受**，不判为可无限制重返；继续康复与神经肌肉控制训练、待达标。
  - observed: 依 p23-17 判据得出"未达标、继续康复"；并据 ce23-05 提示复工后仍需管理残余缺陷。结论明确、可核查。
- **V3_task_utility**: passed: true — 以可计算的对称性阈值替代"感觉好了就上"的复工决策，降低再伤风险。
- **decision**: verified

---

## 能力单元 U12 — 场地空间估算与设备布置（含 Table 25.1/25.2 计算与设施规格）

- **proposed_capability_id**: cap.nsca.facility-space-and-layout-planning
- **proposed_slug**: facility-space-and-layout-planning
- **type**: calculation
- **merged_candidates**: [f25-05, f25-06, p25-02, p25-03, p25-04, p25-05, p25-06, p25-07, p25-08, p25-09, p25-10, p25-11, p25-12, p25-13, p25-14, p25-15, p25-18, c25-1, c25-2, ce25-01, ce25-02, ce25-03, ce25-04, ce25-05]
- **task_ids**: [T38]
- **importance**: medium
- **source_evidence**:
  - source_id: src-nsca-essentials-5e
    location: Chapter 25, "Arranging Equipment / Table 25.1 / Table 25.2 / 环境与结构规格"（ch25.txt 第 644–1020 行；Table 25.1 §798–823；Table 25.2 §888–1010）
- **R 段可用原文引用**（英文）:
  > "If using a 6 ft long weight bench and a 7 ft Olympic bar for the bench press exercise: DEPTH: (6 ft [bench] + 3 ft [safety cushion]) × WIDTH: (7 ft [bar] + 6 ft [double-wide safety cushion]) = 117 ft2."
- **V1_source_sufficiency**: passed: true — Table 25.2 各动作类型公式（俯卧/仰卧、站姿、架上站姿、举重、地雷管、悬吊）与双例（英制+米制近似）、Table 25.1 有氧设备单机面积、3 ft 设备间距/5–7 ft 主通道/30·36 in 安全缓冲、100 ft²/人、层高 12–14 ft、照明 20–30/50 fc、温湿度/换气、镜面 20 in、悬吊锚点 7–9 ft/5000 lb、坡道 1:12 等均给出。**全部为美国标准与英制口径**（ADA/OSHA/ANSI-ASHRAE，见 B 段语境局限）。
- **V2_executability**: passed: true
  - check_mode: walkthrough（按任务书要求做数值演练）
  - input: 独立核算四例 —— ①5 ft 弯举杠站立弯举；②6 ft 杠、8 ft 用户空间的架上深蹲；③5 ft 杠地雷管；④同场 24 人的最低面积。
  - expected: ① 站姿：(2+3)×(5+6)=5×11=**55 ft²**；② 架上：(8)×(6+6)=8×12=**96 ft²**；③ 地雷管：(π×[5+2+3]²)÷4=3.14×100/4=**78.5 ft²**；④ 24×100=**2,400 ft²**。
  - observed: 逐式代入 Table 25.2 公式得 55 / 96 / 78.5 / 2,400，与独立核算一致（地雷管容差 ±0.5 ft²）。另核对原书样例（6 ft 凳+7 ft 杠=117 ft²、7 ft 杠地雷管≈113 ft²）复算无误。
- **V3_task_utility**: passed: true — 把"空间够不够"变为可核算的公式，统一面积/间距口径，避免布置遗漏与安全缓冲被挤占。
- **decision**: verified
- **if_not_verified**: 不适用。**语境局限（跨法域需重新校验）**：ADA（坡道/轮椅）、OSHA（悬吊连接件 5000 lb）、ANSI/ASHRAE 62.1（换气）、英制单位。

---

## 能力单元 U13 — 设施设计流程、需求评估与运维

- **proposed_capability_id**: cap.nsca.facility-design-process
- **proposed_slug**: facility-design-process
- **type**: procedure
- **merged_candidates**: [f25-01, f25-02, f25-03, f25-04, f25-07, f25-08, p25-01, p25-16, p25-17]
- **task_ids**: [T38]
- **importance**: low
- **source_evidence**:
  - source_id: src-nsca-essentials-5e
    location: Chapter 25, "General Aspects of New Facility Design / Assessing Athletic Program Needs / 维护与清洁"（ch25.txt 第 38–181、266–366、1022–1120 行；Table 25.3 §1103–1120）
- **R 段可用原文引用**（英文）:
  > "Figure 25.1 outlines the four phases of designing a new facility... The predesign phase is the first step... This phase should consist of a needs analysis, a feasibility study, and master plan formation."
- **V1_source_sufficiency**: passed: true — 四阶段（predesign/design/construction/preoperation）、需求分析、SWOT 可行性、项目需求七问、改造流程、维护清洁分频与 Table 25.3 耗材清单均完整。**Figure 25.2 改造步骤仅在图中、正文未展开**（轻度细化缺口）。
- **V2_executability**: passed: true
  - check_mode: walkthrough
  - input: 某小型学院拟为 60 名运动员新建举重房。
  - expected: 预设计期 → 需求分析（空间 = 60×100 = **6,000 ft² 最低**）+ 可行性 SWOT + 总规划；随后设计期（蓝图/合规/动线）→ 施工期 → 运营前期（装修/招聘/清洁维护计划）。
  - observed: 能产出分阶段交付物清单与可核查的面积结论。V2 通过。
- **V3_task_utility**: passed: true — 以标准阶段与需求问题清单降低规划遗漏、稳定交付结构。
- **decision**: **reference**
- **if_not_verified**: 去向=并入 `book/overview.md` 的"设施规划"参考区。理由：属**项目管理流程**，强依赖美国建筑规范/ADA/城市规划与委员会（建造方/建筑师/律师/财务/使用者）组织语境（ch25.txt 第 116–120、661–669 行），S&C 单体无法独立执行，BOOK_OVERVIEW 亦提示 T38 管理流程可为 reference；其可核算部分已由 U12 承载。**跨法域需重新校验**。

---

## 能力单元 U14 — 政策与程序手册构建（使命→目标→政策→程序）与场馆行政

- **proposed_capability_id**: cap.nsca.policy-procedure-manual
- **proposed_slug**: policy-procedure-manual
- **type**: framework
- **merged_candidates**: [f26-01, f26-07, f26-08, p26-01, p26-02, p26-03, p26-04, p26-08, p26-14, p26-18, p26-19, p26-20, p26-21, c26-1]
- **task_ids**: [T39]
- **importance**: low
- **source_evidence**:
  - source_id: src-nsca-essentials-5e
    location: Chapter 26, "Mission Statement and Program Goals / Program Objectives / Performance Team / Facility Administration"（ch26.txt 第 49–140、632–680、1063–1103、875–948 行；Table 26.1 §158–196）
- **R 段可用原文引用**（英文）:
  > "Policies are essentially a facility's rules and regulations; they reflect the goals and objectives of the program. Procedures describe how policies are met or carried out... they are the basis on which policies and procedures are created."
- **V1_source_sufficiency**: passed: true — 使命判据（Drucker）与三要素、项目目标样例、Table 26.1 表现团队模板、员工准备清单、场馆规则清单、排课规则（赛季优先 + MWF）、使用资格、补充剂 Standard 9.1、训练卡规则、年度宣讲会内容均完整。**依据美国院校（NCAA/HIPAA）与主管机构规则**。
- **V2_executability**: passed: true
  - check_mode: walkthrough
  - input: 为某高中体能训练项目起草手册骨架。
  - expected: 使命宣言（8 判据 + 3 要素）→ 项目目标 → 具体 objectives → 政策（监督与指导、设施行政、应急预案、使用资格）→ 程序（如何落实）；配套 Table 26.1 表现团队与年度宣讲会。
  - observed: 能产出层级完整的手册大纲（各层缺失可被检出）。V2 通过。
- **V3_task_utility**: passed: true — 提供"目标→政策→程序"的一致结构，稳定交付格式、减少条款遗漏。
- **decision**: **reference**
- **if_not_verified**: 去向=并入 `book/overview.md` 的"项目治理与行政"参考区（Table 26.1 可入 `glossary/参考表`）。理由：本质为**行政/治理流程**，强依赖美国院校体制与主管机构规则，产出（手册）随机构而异，非可独立执行的原子方法；BOOK_OVERVIEW 提示 T39 管理内容可为 reference。**跨法域需重新校验**。

---

## 能力单元 U15 — 风险管理与法律责任（过失四要素、监督原则、记录/产品责任/惩戒）

- **proposed_capability_id**: cap.nsca.risk-management-and-negligence
- **proposed_slug**: risk-management-and-negligence
- **type**: framework
- **merged_candidates**: [f26-02, f26-03, f26-04, f26-09, f26-10, f26-11, p26-05, p26-06, p26-07, p26-09, p26-10, p26-11, p26-12, p26-13, c26-3, ce26-01, ce26-02, ce26-03, ce26-04, ce26-05, ce26-06, ce26-07, ce26-08]
- **task_ids**: [T39]
- **importance**: low
- **source_evidence**:
  - source_id: src-nsca-essentials-5e
    location: Chapter 26, "Legal and Ethical Issues / Common Litigation Issues / Discipline / Instruction and Supervision"（ch26.txt 第 423–630、742–847、950–1016 行）
- **R 段可用原文引用**（英文）:
  > "Four elements must exist for a strength and conditioning professional to be found negligent: duty, breach of duty, proximate cause, and damages... because of the natural and continuous sequence of reasonably foreseeable events (proximate cause)."
- **V1_source_sufficiency**: passed: true — 过失四要素与举证标准（证据优势）、监督九原则与 80% 诉讼引用、记录保存清单与诉讼时效、产品责任规避 7 步、分级惩戒与"严禁以训练为惩罚"、参与前筛查与医学许可均完整。**子项 `p26-05`（法律责任术语）为 definition 级，宜入 glossary**。
- **V2_executability**: passed: true
  - check_mode: walkthrough
  - input: 教练发现阻力器械缆绳过度磨损并记录，但未贴 "Out of Order"，随后运动员使用受伤。
  - expected: 逐关判定 → duty（有修复/挂牌义务）✓；breach（未行动）✓；proximate cause（可预见事态自然连续致伤）✓；damages（人身损害）✓ → **构成过失**（四关全过）。
  - observed: 依 f26-03/p26-06 命中原文示例（ch26.txt 第 468–476 行）结论；并据 ce26-02 提示免责书不能免过失。结论明确、可核查。
- **V3_task_utility**: passed: true — 以四要素自检 + 监督/记录清单，把责任暴露点变成可核查项，改善决策结构。
- **decision**: verified
- **if_not_verified**: 不适用。**语境局限（跨法域需重新校验）**：全部依赖美国侵权法/判例、ADA、Title VI/IX、HIPAA、NCAA、911；`p26-05` 术语建议并入 `book/glossary.md`。

---

## 能力单元 U16 — 应急预案（EAP）构成与分情境应急响应

- **proposed_capability_id**: cap.nsca.emergency-action-plan
- **proposed_slug**: emergency-action-plan
- **type**: procedure
- **merged_candidates**: [f26-05, f26-06, p26-15, p26-16, p26-17, c26-2, ce26-09]
- **task_ids**: [T39]
- **importance**: low
- **source_evidence**:
  - source_id: src-nsca-essentials-5e
    location: Chapter 26, "Emergency Planning and Response / Roles Within the Emergency Team"（ch26.txt 第 1165–1286 行；Figure 26.7 §1251–1286）
- **R 段可用原文引用**（英文）:
  > "Within the emergency team, four principal roles exist. The first is to provide immediate care of the athletes... The second involves emergency equipment retrieval... Next is the activation of the emergency medical system (EMS)... the individual making the call should have been familiarized with the facility location."
- **V1_source_sufficiency**: passed: true — EAP 必备要素（EMS 启动、主/次/三级联系人、具体地址、电话/出口位置、有资质人员、救护车通道、急救箱/AED 位置、火灾/龙卷风等情境方案）、四角色分工、Figure 26.7 四情境分步流程、至少每季度演练要求均完整。
- **V2_executability**: passed: true
  - check_mode: walkthrough
  - input: 举重房内运动员倒地、意识不清（危及生命情境）。
  - expected: ①呼叫 911；②勿移动伤者；③清醒则先征得同意再施救（本例不清醒，直接进入 ④）；④必要时 CPR/AED；⑤陪伴至救援到达；⑥启动应急通信通知相关方；⑦填写伤情报告。
  - observed: 依 f26-06/p26-16 命中 Figure 26.7 危及生命分步序列；四角色（即时照护/取设备/启动 EMS/向导）可对应分配。结论明确、可核查。
- **V3_task_utility**: passed: true — 把"出事怎么办"固化为分情境可演练步骤，缩短响应时延、减少现场遗漏。
- **decision**: verified
- **if_not_verified**: 不适用。**语境局限（跨法域需重新校验）**：以美国 911/EMS 体系为背景，需替换为当地应急号码（原文已注 "or a comparable local emergency response provider"）。

---

## 覆盖核查表

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

## 本簇缺口清单

- **p23-05（U7）**：成熟—重塑期"数月至数年"跨度过大且无个体推算方法；重返判据的具体数值原文未给（重返数值判据仅由 p23-17 的 <10% 对侧差异部分覆盖）。**不补造**。
- **p23-17（U11）**：<10% 对侧差异判据来自**单一引用（ch23 引 60）**，样本人群与测试协议未明，原文用 "may be considered" 属建议性。
- **p24-14（U6）**：>30% 训练量警戒线为原文**唯一数值**，但口径（单周？累计？按何标量）未明；其余规避条目为定性建议、无剂量。
- **p24-07（U3）**：Table 24.1 中离心力量、多/单关节 RFD 等敏感度为 Unknown/"Unknown onset"，无变化幅度阈值；"Within 1 week" 等也无百分比切点。
- **U10（热病/低温）**：补液量、降温目标温度、复温速率、发病环境温湿度阈值原文未给。
- **U13/U14（T38/T39）**：管理流程强依赖美国法规（ADA/OSHA/ANSI-ASHRAE/NCAA/HIPAA/911）与院校体制，**跨法域需重新校验**；已按 reference 出栈。
- **全局**：凡涉及法规/标准/单位者（U12、U13、U14、U15、U16），一律为美国语境 + 英制口径，跨法域须重新校验——这不是缺陷，但须在 B 段如实呈现。

---

## 供阶段 2 的提示

- **建议组合成卡**：
  - (a) 簇 → 一张"过度训练判定与恢复"卡：U1（判定）+U3（监控）+U4（分级检测）作 R/B，U2（归因排障）作 A2/E，U5（恢复）+U6（预防）作 A1/A2；U1/U2/U5 也可各独立成 troubleshooting 卡。
  - (b) 簇 → "康复再训练负荷调整"卡：U7（分期）+U8（抗阻处方数值演练）为主，U9（专业边界/转诊）独立成**安全卡**，U10（医疗急症）独立成**现场处置卡**，U11（重返判据）可并入主卡 B 段或独立。
  - (c) 簇 → U12（空间计算）独立成 calculation 卡；U15（过失推理）独立成 reasoning 卡；U16（EAP）独立成 procedure 卡；U13/U14 作 overview 参考。
- **A1 素材建议**：
  - U1 的 A1 可用 c24-3（FG 超量情境）；U3 用 c24-4（Figure 24.15 监控清单）；U5 用 c24-1（Table 24.4）/c24-2（恢复时长）。
  - U8 用 c23-2（Table 23.3 髌股损伤双专项）、c23-1（踝扭伤进阶）、c23-4（腘绳肌速度特异进阶）；U10 可用病例结构（原文未给完整病例，以症状—处置表作 A1）。
  - U12 用 c25-1（Table 25.2 演算）/c25-2（20 m 跑道不适配 Yo-Yo）。
  - U15 用 c26-3（镰状细胞特质过失判例）；U16 用 c26-2（Figure 26.7 样例）。
- **B 段素材（失败模式/反例）**：U1←（无直接反例）；U2←ce24-01/02/03；U3←ce24-04/08/10；U6←ce24-05/06/07/09；U7←ce23-01/02/03；U9←ce23-04 与 ce26-07；U11←ce23-05；U12←ce25-01..05；U15←ce26-01..06/08；U16←ce26-09。
- **reference/glossary 路由**：U13→overview 设施规划区；U14→overview 治理区 + Table 26.1 入参考表；`p26-05`（法律责任术语）→glossary；`p24-08`（Table 24.2 机制—证据强度）→overview/参考表（U3 内标注为 reference 级子项）。
