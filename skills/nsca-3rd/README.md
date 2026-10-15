# nsca-3rd

基于美国国家体能协会（NSCA）教材 *Essentials of Strength Training and Conditioning, 3rd Edition*
（Thomas R. Baechle & Roger W. Earle 主编，全书 22 章），用仓颉 `cangjie-skill`（`RIA-TV++` 流水线）
蒸馏而成的整书级力量与体能训练 Agent Skill。

## 与 nsca-5th 的分工

两版并存时按此路由：需要 SRB/RIR 自动调节、VBT 与测力台测试、RAMP/PAPE、减速与反应性灵敏、
RED-S、孕产与特殊人群细则、法律风险（EAP）时用 `nsca-5th`；
只要经典 `%1RM` 查表、线性/波动周期化、基础测试电池与场馆面积公式，`nsca-3rd` 更短、参数更集中。
第 3 版没有的机制不要从它这里推断。

## 能做什么

`SKILL.md` 为主路由，按意图分发到 10 张能力卡，覆盖运动生理与生物力学、体能测试编排、
热身柔韧与动作技术护举、7 步抗阻计划、超等长、速度与灵敏、有氧耐力与减量、周期化年度计划、
运动营养与伤病康复（DAPRE）、力量房管理与督导比例。

## 目录结构

```text
nsca-3rd/
├── SKILL.md                     # 主路由入口（YAML frontmatter + When to Use + 核心原则 + 能力卡路由表 + 执行步骤）
└── references/
    ├── book/
    │   ├── overview.md          # 全书 22 章五支柱结构映射、核心机制与作者局限
    │   └── glossary.md          # 术语、公式与定量参数速查
    └── capabilities/            # 10 张 RIA++ 六段式（R/I/A1/A2/E/B）能力卡
```

## 安装与调用

把整个 `nsca-3rd/` 目录放入所用 Agent 的 Skill 目录即可（各 Agent 目录位置不同，以其官方文档为准）。
调用方式：直接说「按 NSCA 第3版给一个篮球运动员排赛季周期」，或显式 `调用 nsca-3rd Skill`。

## 边界

- 不做医疗诊断、处方与临床康复决策；伤病相关只给训练侧的配合方案，转由执业医师与康复专业人员决定。
- `%1RM`—次数对照表按单组线性衰减，下肢复合动作、器械与高水平运动员会偏离预测值，这一点在 `overview.md` 的局限分析里已标注。
- 内容源自受版权保护教材的研究性提炼，未随附独立许可证文件；再分发前请自行确认使用权（收录状态见仓库根 README 目录表）。

---

> 本 Skill 由 [distill-skills](https://github.com/WRM-FW/distill-skills) 仓库统一收录维护，全部 Skill 索引见[仓库根 README](../../README.md)。
