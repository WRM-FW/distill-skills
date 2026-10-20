# test-results.md — 阶段 4 压力测试结果

## 方法

- **触发精度测试**：独立干净 sub-agent 盲测。给每个 agent 只提供 8 个入口的 name + description（宿主实际可见内容）与待判定 prompt，
  **不给** `type` / `expected_behavior` / `notes` / 通过标准。
- 分 4 组交叉判卷，共 60 条用例。主流程再与 `test-prompts.json` 的预期逐条比对。
- 判定局限：这是**静态描述匹配**测试（agent 依据 description 判断激活），不等于真实宿主路由；
  且末段为机械判卷（按 expected_behavior 中显式写出的目标入口），语义细节仍需人工复核（见"边界用例"节）。

## 汇总

| 类型 | 用例数 | 通过 | 通过率 |
|---|---|---|---|
| 应触发 | 35 | 35 | 100.0% |
| 不应触发（诱饵） | 17 | 17 | 100.0% |
| 边界用例（人工核查） | 8 | — | 见下 |

> 验收标准（测试前固定）：诱饵类（should_not_trigger）容错为 0；
> 应触发类要求 ≥90%（跨 Skill 混淆的实际错误单独列出）。

## 未通过明细

无。

## 跨 Skill 混淆分析（诱饵类）

- 诱饵类 0 失败：所有"应由同书另一 Skill 处理"的 prompt 都未误激活本 Skill。

## 边界用例（人工核查）

**nsca-resistance-program-design--edge-01** — 「我该练几组？」

- 实际选择：`nsca-resistance-program-design`
- 理由：问组数属抗阻变量，但缺目标与状态。
- 激活后动作：先询问训练目标/水平/动作等缺失信息。
- 预期边界理由：信息严重不足（无训练状态/无目标/无项目）→ 可以激活，但必须先询问而不是直接给组数

**nsca-periodization--edge-01** — 「我这周临时只能练两次，怎么办？」

- 实际选择：`nsca-resistance-program-design`
- 理由：临时一周只练两次属周安排微调，非年度周期化。
- 激活后动作：先询问训练目标与项目，再调整本周安排。
- 预期边界理由：短周期临时调整，不应自动展开成套周期化；可激活但只需 microcycle 级微调，并提示若频繁发生才进入周期化范畴

**nsca-testing-and-evaluation--edge-01** — 「我体脂测出来 24%，算高吗？」

- 实际选择：`nsca-testing-and-evaluation`
- 理由：体脂 24% 是否算高，属测试结果对照常模解读
- 激活后动作：先确认性别年龄等，再对照常模解读该数值
- 预期边界理由：可以激活，但必须先确认人群/年龄/性别/测量方法，并提示常模的时效性与人群依赖性

**nsca-plyometric-design--edge-01** — 「我想提高弹跳，是该多练深蹲还是多跳箱？」

- 实际选择：`nsca-plyometric-design`
- 理由：提高弹跳在深蹲与跳箱间取舍，属与抗阻整合排序
- 激活后动作：先明确目标周期与现有力量水平，再给整合排序
- 预期边界理由：跨 skill：需给出主力选择（力量不足者先补最大力量）+ 增强式作为组合，不应只答一边

**nsca-speed-agility-design--edge-01** — 「他短跑起跑总是慢。」

- 实际选择：`nsca-speed-agility-design`
- 理由：起跑慢属线性速度加速阶段问题
- 激活后动作：判定起跑/加速块并给技术纠错
- 预期边界理由：可激活，但需先诊断是技术、力量还是反应问题（技术错误排障路径），不能直接开处方

**nsca-aerobic-endurance-design--edge-01** — 「我想减脂，该多做有氧还是多练力量？」

- 实际选择：`nsca-5th`
- 理由：减脂/身体成分未独立晋级，归 VI 路由
- 激活后动作：先问体重目标与饮食现状，再路由营养卡
- 预期边界理由：跨 skill：应同时涉及 nsca-aerobic-endurance-design 与 nsca-resistance-program-design，并结合能量摄入（路由入口内的营养能力）

**nsca-overtraining-recovery--edge-01** — 「我最近睡不好、静息心率也比平时高。」

- 实际选择：`nsca-overtraining-recovery`
- 理由：睡眠差、静息心率升高属本卡监控早期信号
- 激活后动作：先问是否伴成绩下降与恢复结局
- 预期边界理由：可能指向过度训练也可能来自生活压力/疾病 → 应激活并走归因排查，不应直接下过度训练的结论

**nsca-5th--edge-01** — 「我想让他整体变强。」

- 实际选择：`nsca-5th`
- 理由："整体变强"意图过宽，尚不确定专项
- 激活后动作：先问目标、专项、赛季以路由专项Skill
- 预期边界理由：意图过宽（未指定素质域）→ 应激活 nsca-5th 路由入口，先澄清目标再分发

## 逐条判卷表

| id | 类型 | 期望 | 实际 | 通过 |
|---|---|---|---|---|
| nsca-resistance-program-design--should-trigger-01 | should_trigger | nsca-resistance-program-design | nsca-resistance-program-design | ✅ |
| nsca-resistance-program-design--should-trigger-02 | should_trigger | nsca-resistance-program-design | nsca-resistance-program-design | ✅ |
| nsca-resistance-program-design--should-trigger-03 | should_trigger | nsca-resistance-program-design | nsca-resistance-program-design | ✅ |
| nsca-resistance-program-design--should-trigger-04 | should_trigger | nsca-resistance-program-design | nsca-resistance-program-design | ✅ |
| nsca-resistance-program-design--should-trigger-05 | should_trigger | nsca-resistance-program-design | nsca-resistance-program-design | ✅ |
| nsca-resistance-program-design--should-not-trigger-01 | should_not_trigger | nsca-overtraining-recovery | nsca-overtraining-recovery | ✅ |
| nsca-resistance-program-design--should-not-trigger-02 | should_not_trigger | nsca-aerobic-endurance-design | nsca-aerobic-endurance-design | ✅ |
| nsca-resistance-program-design--should-not-trigger-03 | should_not_trigger | none | none | ✅ |
| nsca-resistance-program-design--edge-01 | edge_case | （人工） | nsca-resistance-program-design | — |
| nsca-periodization--should-trigger-01 | should_trigger | nsca-periodization | nsca-periodization | ✅ |
| nsca-periodization--should-trigger-02 | should_trigger | nsca-periodization | nsca-periodization | ✅ |
| nsca-periodization--should-trigger-03 | should_trigger | nsca-periodization | nsca-periodization | ✅ |
| nsca-periodization--should-trigger-04 | should_trigger | nsca-periodization | nsca-periodization | ✅ |
| nsca-periodization--should-not-trigger-01 | should_not_trigger | nsca-resistance-program-design | nsca-resistance-program-design | ✅ |
| nsca-periodization--should-not-trigger-02 | should_not_trigger | nsca-testing-and-evaluation | nsca-testing-and-evaluation | ✅ |
| nsca-periodization--edge-01 | edge_case | （人工） | nsca-resistance-program-design | — |
| nsca-testing-and-evaluation--should-trigger-01 | should_trigger | nsca-testing-and-evaluation | nsca-testing-and-evaluation | ✅ |
| nsca-testing-and-evaluation--should-trigger-02 | should_trigger | nsca-testing-and-evaluation | nsca-testing-and-evaluation | ✅ |
| nsca-testing-and-evaluation--should-trigger-03 | should_trigger | nsca-testing-and-evaluation | nsca-testing-and-evaluation | ✅ |
| nsca-testing-and-evaluation--should-trigger-04 | should_trigger | nsca-testing-and-evaluation | nsca-testing-and-evaluation | ✅ |
| nsca-testing-and-evaluation--should-trigger-05 | should_trigger | nsca-testing-and-evaluation | nsca-testing-and-evaluation | ✅ |
| nsca-testing-and-evaluation--should-not-trigger-01 | should_not_trigger | nsca-resistance-program-design | nsca-resistance-program-design | ✅ |
| nsca-testing-and-evaluation--should-not-trigger-02 | should_not_trigger | （人工） | nsca-5th | ✅ |
| nsca-testing-and-evaluation--edge-01 | edge_case | （人工） | nsca-testing-and-evaluation | — |
| nsca-plyometric-design--should-trigger-01 | should_trigger | nsca-plyometric-design | nsca-plyometric-design | ✅ |
| nsca-plyometric-design--should-trigger-02 | should_trigger | nsca-plyometric-design | nsca-plyometric-design | ✅ |
| nsca-plyometric-design--should-trigger-03 | should_trigger | nsca-plyometric-design | nsca-plyometric-design | ✅ |
| nsca-plyometric-design--should-trigger-04 | should_trigger | nsca-plyometric-design | nsca-plyometric-design | ✅ |
| nsca-plyometric-design--should-not-trigger-01 | should_not_trigger | nsca-speed-agility-design | nsca-speed-agility-design | ✅ |
| nsca-plyometric-design--should-not-trigger-02 | should_not_trigger | （人工） | nsca-resistance-program-design | ✅ |
| nsca-plyometric-design--edge-01 | edge_case | （人工） | nsca-plyometric-design | — |
| nsca-speed-agility-design--should-trigger-01 | should_trigger | nsca-speed-agility-design | nsca-speed-agility-design | ✅ |
| nsca-speed-agility-design--should-trigger-02 | should_trigger | nsca-speed-agility-design | nsca-speed-agility-design | ✅ |
| nsca-speed-agility-design--should-trigger-03 | should_trigger | nsca-speed-agility-design | nsca-speed-agility-design | ✅ |
| nsca-speed-agility-design--should-trigger-04 | should_trigger | nsca-speed-agility-design | nsca-speed-agility-design | ✅ |
| nsca-speed-agility-design--should-not-trigger-01 | should_not_trigger | nsca-plyometric-design | nsca-plyometric-design | ✅ |
| nsca-speed-agility-design--should-not-trigger-02 | should_not_trigger | nsca-aerobic-endurance-design | nsca-aerobic-endurance-design | ✅ |
| nsca-speed-agility-design--edge-01 | edge_case | （人工） | nsca-speed-agility-design | — |
| nsca-aerobic-endurance-design--should-trigger-01 | should_trigger | nsca-aerobic-endurance-design | nsca-aerobic-endurance-design | ✅ |
| nsca-aerobic-endurance-design--should-trigger-02 | should_trigger | nsca-aerobic-endurance-design | nsca-aerobic-endurance-design | ✅ |
| nsca-aerobic-endurance-design--should-trigger-03 | should_trigger | nsca-aerobic-endurance-design | nsca-aerobic-endurance-design | ✅ |
| nsca-aerobic-endurance-design--should-trigger-04 | should_trigger | nsca-aerobic-endurance-design | nsca-aerobic-endurance-design | ✅ |
| nsca-aerobic-endurance-design--should-not-trigger-01 | should_not_trigger | nsca-resistance-program-design | nsca-resistance-program-design | ✅ |
| nsca-aerobic-endurance-design--should-not-trigger-02 | should_not_trigger | nsca-overtraining-recovery | nsca-overtraining-recovery | ✅ |
| nsca-aerobic-endurance-design--edge-01 | edge_case | （人工） | nsca-5th | — |
| nsca-overtraining-recovery--should-trigger-01 | should_trigger | nsca-overtraining-recovery | nsca-overtraining-recovery | ✅ |
| nsca-overtraining-recovery--should-trigger-02 | should_trigger | nsca-overtraining-recovery | nsca-overtraining-recovery | ✅ |
| nsca-overtraining-recovery--should-trigger-03 | should_trigger | nsca-overtraining-recovery | nsca-overtraining-recovery | ✅ |
| nsca-overtraining-recovery--should-trigger-04 | should_trigger | nsca-overtraining-recovery | nsca-overtraining-recovery | ✅ |
| nsca-overtraining-recovery--should-not-trigger-01 | should_not_trigger | nsca-periodization | nsca-periodization | ✅ |
| nsca-overtraining-recovery--should-not-trigger-02 | should_not_trigger | nsca-testing-and-evaluation | nsca-testing-and-evaluation | ✅ |
| nsca-overtraining-recovery--edge-01 | edge_case | （人工） | nsca-overtraining-recovery | — |
| nsca-5th--should-trigger-01 | should_trigger | nsca-5th | nsca-5th | ✅ |
| nsca-5th--should-trigger-02 | should_trigger | nsca-5th | nsca-5th | ✅ |
| nsca-5th--should-trigger-03 | should_trigger | nsca-5th | nsca-5th | ✅ |
| nsca-5th--should-trigger-04 | should_trigger | nsca-5th | nsca-5th | ✅ |
| nsca-5th--should-trigger-05 | should_trigger | nsca-5th | nsca-5th | ✅ |
| nsca-5th--should-not-trigger-01 | should_not_trigger | nsca-resistance-program-design | nsca-resistance-program-design | ✅ |
| nsca-5th--should-not-trigger-02 | should_not_trigger | nsca-testing-and-evaluation | nsca-testing-and-evaluation | ✅ |
| nsca-5th--edge-01 | edge_case | （人工） | nsca-5th | — |

## 实际输出评测（代表任务）

本轮做了触发精度测试与边界用例核查；**实际输出评测（old/new/without 三变体对照）未在本轮执行**，
已在 `PIPELINE_STATE.md` 记为待办，交付说明中标为"未实测"。不得据此宣称相对无 Skill 有提升。
