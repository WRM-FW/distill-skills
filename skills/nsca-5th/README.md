# nsca-5th

> 上游 Skill：[仓颉 cangjie-skill](https://github.com/kangarooking/cangjie-skill)（`RIA-TV++` 流水线，MIT）　｜　许可：[PolyForm Noncommercial 1.0.0](LICENSE)　｜　版本：`v1.0.0`（标签 `nsca-5th-v1.0.0`）　｜　版本记录：[CHANGELOG.md](CHANGELOG.md)

基于美国国家体能协会（NSCA）教材 *Essentials of Strength Training and Conditioning, 5th Edition*
（G. Gregory Haff & N. Travis Triplett 主编，2027，全书 26 章），用仓颉 `cangjie-skill`（`RIA-TV++` 流水线）
蒸馏而成的整书级力量与体能训练 Agent Skill。

## 能做什么

加载后 `SKILL.md` 作为主路由，按用户意图分发到 12 张能力卡，覆盖：

- 能量系统与 HIIT 间歇配比、内分泌训练变量
- 杠杆/运动面分析、铁链与弹力带可变阻力、加重离心（AEL）
- 测试电池编排与结果统计（IMTP、跳姿 RSI/mRSI、VBT、MAS、30-15 IFT、SWC、效应量）
- RAMP 热身、PAPE 激活、静态/动态/PNF 柔韧
- 动作技术、握法、护举与强人项目
- 7 步抗阻计划（`%1RM` / SRB / RIR）、举重派生动作
- 超等长、弹式、复合对比训练
- 冲刺速度、变向（COD）、减速与反应性灵敏
- 有氧耐力（3/5 区模型）与高原/热适应时间线
- 周期化、过度训练连续体（FOR/NFOR/OTS）、运动心理转介（3-Step ABC）
- 青少年（YPD/PHV/AMSC）、女性与孕产、老年人群
- 运动营养与 RED-S、补剂与兴奋剂、伤病康复（DAPRE）、场馆与法律风险（EAP）

定量参数（阈值、比例、组次表）在卡内，`SKILL.md` 只负责路由与四步流程。

## 目录结构

```text
nsca-5th/
├── SKILL.md                     # 主路由入口（YAML frontmatter + When to Use + 核心原则 + 能力卡路由表 + 四步流程）
└── references/
    ├── book/
    │   ├── overview.md          # 全书 26 章结构映射与适用边界
    │   └── glossary.md          # 术语、公式与定量参数速查
    └── capabilities/            # 12 张 RIA++ 六段式（R/I/A1/A2/E/B）能力卡
```

## 安装与调用

把整个 `nsca-5th/` 目录放入所用 Agent 的 Skill 目录即可（各 Agent 目录位置不同，以其官方文档为准）。
调用方式：直接说「用 NSCA 第5版给我排一个 12 周力量周期」，或显式 `调用 nsca-5th Skill`。

## 边界

- 不做医疗诊断、手术决策、处方药与临床心理治疗；此类需求转执业医师、RD/CSSD、运动防护师、物理治疗师或临床心理师。
- 不用于无参数的闲聊式健身建议。
- 本 Skill 的原创内容以 [PolyForm Noncommercial License 1.0.0](LICENSE) 授权（SPDX `PolyForm-Noncommercial-1.0.0`），禁止商业用途。
- 内容是对受版权保护教材的研究性提炼：本许可只覆盖本目录的原创表达，不覆盖、也不重新授权原书文字与图表；再分发前请自行确认对原书内容的使用权。

---

> 本 Skill 由 [distill-skills](https://github.com/WRM-FW/distill-skills) 仓库统一收录维护，全部 Skill 索引见[仓库根 README](../../README.md)。
