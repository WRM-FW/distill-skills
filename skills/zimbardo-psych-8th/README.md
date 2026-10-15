# zimbardo-psych-8th

> **《津巴多普通心理学（第8版）》= *Psychology: Core Concepts (8th Edition)* 仓颉 RIA-TV++ 整书蒸馏 Agent Skill**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Pipeline: Cangjie RIA-TV++](https://img.shields.io/badge/Pipeline-Cangjie%20RIA--TV%2B%2B-success.svg)](SKILL.md)
[![Source: Zimbardo 8th Ed.](https://img.shields.io/badge/Source-Psychology%3A%20Core%20Concepts%208e-orange.svg)](references/book/overview.md)

`zimbardo-psych-8th` 是基于菲利普·津巴多（Philip G. Zimbardo）、罗伯特·约翰逊（Robert L. Johnson）与薇薇安·麦卡恩（Vivian McCann）合著的经典心理学教材 **《津巴多普通心理学（第8版）》（*Psychology: Core Concepts, 8th Edition*，全书 14 章、50 个核心概念）**，通过 **仓颉（Cangjie）RIA-TV++ 流水线** 蒸馏而成的结构化、可执行 Agent Skill。

---

## 1. Skill 用途与核心特性

本技能并非静态读书笔记，而是供 AI Agent 在真实任务场景中调用的**心理学分析、诊断与行为干预路由系统**：

- **全书级结构化锚定**：完整覆盖原书 14 章、50 个 `Core Concepts`、经典实验基准（如 Asch 从众率 `37%`、Milgram 服从率 `65%`、工作记忆 `7 +/- 2` 组块、前瞻记忆占日常遗忘 `50%` 等）与第 8 版新增前沿机制（表观遗传学 `Epigenetics`、默认模式网络 `DMN`、卡尼曼双系统 `System 1/2`、德韦克成长型思维 `Growth Mindset`、班杜拉 8 种道德推脱机制、津巴多时间洞察力 `ZTPI` 与时间洞察力疗法 `TPT`、NIMH `RDoC` 脑网络诊断框架）。
- **RIA++ 六段式能力卡架构**：12 张领域能力卡严格遵循 `R (Source Anchor)`、`I (Methodology Skeleton)`、`A1 (Book Applications)`、`A2 (Trigger Scenarios & Neighbor Distinction)`、`E (Executable Steps)`、`B (Boundary & Failure Modes)` 与三重验证（`V1 来源充分性 / V2 可执行性 / V3 任务增益`）。
- **人 × 情境 × 系统（Person × Situation × System）三层诊断视角**：避免基本归因错误（FAE），将个体特质、即时社会情境与底层制度设计结合分析。

---

## 2. 目录结构

```text
zimbardo-psych-8th/
├── README.md                  # 仓库说明文档（用途、目录结构、安装与使用方法、能力路由表）
├── LICENSE                    # MIT 许可证
├── .gitignore                 # Git 忽略规则配置
├── SKILL.md                   # Skill 核心路由入口（含 YAML Frontmatter、触发边界、4 步主工作流与防坑指南）
├── references/
│   ├── book/
│   │   ├── overview.md        # 阶段 0：Adler 整书四步分析（全书 14 章 6 大模块结构映射与第 8 版演进）
│   │   └── glossary.md        # 全书 50 个核心概念（Core Concepts 1.1-14.4）与定量/实验基准词典
│   └── capabilities/          # 12 张 RIA-TV++ 六段式可执行能力卡
│       ├── 01-scientific-method-six-perspectives-critical-thinking.md
│       ├── 02-biopsychology-epigenetics-neuroscience-brain-layers.md
│       ├── 03-sensation-signal-detection-perceptual-organization.md
│       ├── 04-behavioral-learning-conditioning-modification.md
│       ├── 05-memory-encoding-retrieval-seven-sins-mnemonics.md
│       ├── 06-thinking-heuristics-biases-intelligence-mindset.md
│       ├── 07-lifespan-development-attachment-piaget-erikson-moral.md
│       ├── 08-consciousness-circadian-sleep-architecture-states.md
│       ├── 09-motivation-hierarchy-self-control-emotion-regulation.md
│       ├── 10-personality-big-five-ztpi-time-perspective-narratives.md
│       ├── 11-social-psychology-situational-power-lucifer-effect.md
│       └── 12-psychopathology-dsm5-biopsychosocial-therapies-stress-coping.md
└── scripts/
    └── validate_skill.py      # 仓库完整性与 SKILL.md 格式规范校验脚本
```

---

## 3. 12 张能力卡路由总览

| 编号 | 能力卡文件 | 对应章节 | 核心解决的任务场景 |
| :--- | :--- | :--- | :--- |
| **01** | `references/capabilities/01-scientific-method-six-perspectives-critical-thinking.md` | Ch 1 | 批判性思维 6 问审计伪科学断言、操作性定义转化、对照实验设计、6 大心理学视角交叉诊断 |
| **02** | `references/capabilities/02-biopsychology-epigenetics-neuroscience-brain-layers.md` | Ch 2 | 表观遗传机制分析、7 大神经递质与精神药物作用定位、5 类脑扫描选择、三层脑与四脑叶/裂脑功能映射 |
| **03** | `references/capabilities/03-sensation-signal-detection-perceptual-organization.md` | Ch 3 | 绝对阈限与韦伯定律计算、信号检测论（SDT）误报/漏报权衡、疼痛门控调节、格式塔知觉分组与非注意盲视排查 |
| **04** | `references/capabilities/04-behavioral-learning-conditioning-modification.md` | Ch 4 | 经典/操作性条件作用拆解、4 类强化程序表（FR/VR/FI/VI）设计、普雷马克原则、5 步操作性行为矫正与习惯养成 |
| **05** | `references/capabilities/05-memory-encoding-retrieval-seven-sins-mnemonics.md` | Ch 5 | 三阶段记忆优化、深层语义编码与备考策略、沙克特“记忆七宗罪”诊断、前瞻记忆外部线索工程与目击记忆评估 |
| **06** | `references/capabilities/06-thinking-heuristics-biases-intelligence-mindset.md` | Ch 6 | 卡尼曼双系统（System 1/2）切换、启发式解题与破除功能固着、6 大认知偏差去偏、离差智商解读与成长型思维干预 |
| **07** | `references/capabilities/07-lifespan-development-attachment-piaget-erikson-moral.md` | Ch 7 | 依恋类型与权威型教养评估、皮亚杰 4 阶段与维果茨基脚手架、埃里克森 8 阶段危机、青春期双系统脑与班杜拉 8 种道德推脱审计 |
| **08** | `references/capabilities/08-consciousness-circadian-sleep-architecture-states.md` | Ch 8 | 默认模式网络（DMN）与专注力切换、昼夜节律与倒时差方案、90 分钟 5 阶段睡眠架构修复、6 类睡眠障碍鉴别与药物状态分析 |
| **09** | `references/capabilities/09-motivation-hierarchy-self-control-emotion-regulation.md` | Ch 9 | 成就动机与防范“过度合理化效应”、肯里克进化需求层级、米歇尔情境自控策略、勒杜双通路情绪调节与倒 U 型唤醒匹配 |
| **10** | `references/capabilities/10-personality-big-five-ztpi-time-perspective-narratives.md` | Ch 10 | 大五人格（OCEAN）评估、津巴多时间洞察力（ZTPI 5 大时区与平衡时间观）诊断、自我防御机制识别与救赎式自我叙事重构 |
| **11** | `references/capabilities/11-social-psychology-situational-power-lucifer-effect.md` | Ch 11 | 阿希从众与贾尼斯群体思维防范、米尔格拉姆服从杠杆拆解、拉塔内 5 步旁观者干预、基本归因错误纠偏与路西法效应系统审计 |
| **12** | `references/capabilities/12-psychopathology-dsm5-biopsychosocial-therapies-stress-coping.md` | Ch 12-14 | 心理异常 4 指标筛查、DSM-5 vs. RDoC 框架、心理疗法（CBT/REBT/暴露）与生物疗法匹配、塞利 GAS 应激、职业倦怠与时间洞察力疗法（TPT） |

---

## 4. 安装与使用方法

### 方式一：通过 Agent Skills 目录安装（本地或工作区）

1. 将本 Skill克隆或解压至你的 Agent 工作区 `skills/` 目录下：
   ```bash
   git clone --depth 1 https://github.com/WRM-FW/distill-skills.git
   cp -r distill-skills/skills/zimbardo-psych-8th <你的 Agent Skill 目录>/zimbardo-psych-8th
   ```
2. 确保目录路径为 `skills/zimbardo-psych-8th/SKILL.md`，Agent 将自动读取 `SKILL.md` 中的 YAML Frontmatter 并注册触发器。

### 方式二：通过 Skills CLI 或 UI 导入

- **UI 手动上传**：直接将 `skills/zimbardo-psych-8th/` 目录（或它单独压缩后的 zip）上传至支持 Agent Skill 的客户端 Skills Manager 界面。

本 Skill 不单独建仓，因此不要用 `<your-username>/zimbardo-psych-8th` 这种仓库路径安装。

### 触发与调用示例

- **自然语言自动触发**：当提问涉及行为矫正、记忆备考、认知去偏、时间洞察力（ZTPI）、群体从众/路西法效应、应激管理等主题时自动激活。
- **显式点名调用**：
  > `@zimbardo-psych-8th 帮我分析：为什么我每次定下学习计划总是拖延到最后一刻通宵，而且团队开会时大家明明觉得方案有问题却没人敢提反对意见？请结合津巴多时间洞察力（ZTPI）、操作性条件作用和阿希/贾尼斯群体动力学给出可执行改进方案。`

---

## 5. 环境依赖与仓库自检

- **运行时依赖**：本 Skill 为纯 Markdown 知识与决策路由包，**无任何外部运行时代码依赖**，兼容所有支持标准 `SKILL.md` 规范的 Agent 环境（Claude Code、Cursor、Qoder、Gemini 等）。
- **开发校验依赖**（仅运行 `scripts/validate_skill.py` 时可选）：Python 3.8+ 及 `PyYAML`。
  ```bash
  python3 scripts/validate_skill.py
  ```

---

> 本 Skill 由 [distill-skills](https://github.com/WRM-FW/distill-skills) 仓库统一收录维护，全部 Skill 索引见[仓库根 README](../../README.md)。
