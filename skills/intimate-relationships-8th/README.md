# intimate-relationships-8th

> **《亲密关系（第8版）》整书级可执行 Agent Skill（Cangjie RIA-TV++ Pipeline）**
>
> 基于萨姆休斯顿州立大学杰出心理学教授 **罗兰·米勒（Rowland S. Miller）** 经典著作《亲密关系（第8版）》（*Intimate Relationships, 8th Edition*，王伟平 译，彭凯平 审校，人民邮电出版社 2024 年 1 月出版，ISBN `978-7-115-63021-6`）全书 14 章、52 个专题专栏与 686 篇新增研究文献蒸馏而成。

## 1. 项目简介与核心价值

`intimate-relationships-8th` 是一个遵循 **Agent Skills 开放规范** 与 **仓颉（Cangjie）RIA-TV++ 拆书流水线** 构建的心理学决策与沟通排障技能包。它将《亲密关系（第8版）》中的实证关系科学转化为可触发、可执行、可核验的 **1 个主路由文件（`SKILL.md`）+ 2 个整书基准库（`overview.md`, `glossary.md`）+ 12 张六段式能力卡（`R/I/A1/A2/E/B`）**：

- **告别通俗情感鸡汤与“火星撞金星”伪科学**：基于 87 国 141.9 万人元分析与纵向追踪实证数据，提供科学的伴侣诊断。
- **内置可量化评估量表与阈值方程**：涵盖《自我涵盖他人量表》（IOS）、12 题《关系繁荣量表》（均值 `46.4, SD 7.6`）、12 题 `ECR-S` 成人依恋双维度量表（忧虑均值 `22`、回避均值 `15`）、社会交换 `CL / CLalt` 四象限方程、Rusbult 投入模型、戈特曼 `5:1` 黄金互动比与 `I3` 伴侣暴力成因模型。
- **完整覆盖第 8 版前沿增补**：包含科技干扰（Technoference）与低头症（Phubbing）、吸引力的工具性模型（Instrumentality）、黑三角恶性人格（Dark Triad）、约会 App 数字距离悖论、色情作品双刃剑效应、性成长信念（Sexual Growth Beliefs）、伴侣专属仪式（Rituals）以及分手后的社交媒体关系清理（Relational Cleansing）。

## 2. 目录结构

```text
intimate-relationships-8th/
├── README.md                     # 项目说明文档（用途、目录结构、能力路由表、安装与使用方法）
├── LICENSE                       # MIT 许可证与原著学术引用说明
├── .gitignore                    # Git 忽略规则配置
├── SKILL.md                      # Skill 核心主路由与 4 步执行规程（含 YAML Frontmatter）
└── references/
    ├── book/
    │   ├── overview.md           # 阶段 0：Mortimer Adler 整书四步分析（14章结构、底层定律、适用边界）
    │   └── glossary.md           # 阶段 1：核心定量方程、量表计分常模与双语心理学术语词典
    └── capabilities/             # 阶段 2 & 3：12 张 RIA++ 六段式（R/I/A1/A2/E/B）原子能力卡
        ├── 01-intimacy-architecture-attachment-and-individual-differences.md
        ├── 02-interpersonal-attraction-mate-selection-and-dating-strategy.md
        ├── 03-social-cognition-attributional-patterns-and-partner-perception.md
        ├── 04-nonverbal-and-verbal-communication-and-conflict-deescalation.md
        ├── 05-interdependence-social-exchange-equity-and-commitment-engine.md
        ├── 06-friendship-lifecycle-responsiveness-shyness-and-loneliness.md
        ├── 07-love-taxonomy-passionate-arousal-and-companionate-sustainability.md
        ├── 08-sexuality-attitudes-desire-satisfaction-and-consent-safety.md
        ├── 09-relational-stress-ostracism-jealousy-deception-and-forgiveness.md
        ├── 10-conflict-dynamics-demand-withdraw-and-four-couple-types.md
        ├── 11-power-dynamics-interdependence-asymmetry-and-violence-triage.md
        └── 12-relationship-dissolution-divorce-prediction-and-maintenance-repair.md
```

## 3. 12 张 RIA-TV++ 能力卡路由总览

每张能力卡均严格包含 `R（原文锚点）`、`I（方法论骨架）`、`A1（书中应用案例）`、`A2（未来触发场景与邻近区分）`、`E（可执行步骤）`、`B（适用边界与反例失败模式）`、`Related Capabilities（Zettelkasten 双链）` 与 `Triple Verification Audit（三重验证）`：

| 编号 | 能力卡文件 | 对应章节 | 核心模型与定量锚点 |
| :---: | :--- | :---: | :--- |
| **01** | `01-intimacy-architecture-attachment-and-individual-differences.md` | 第 1-2 章 | 亲密 7 维度、`IOS` 量表、《关系繁荣量表》12 题、`ECR-S` 12 题依恋量表、双性化（`35%`）、大五神经质/尽责性、自尊社会计量器、同居转变率与低头症 |
| **02** | `02-interpersonal-attraction-mate-selection-and-dating-strategy.md` | 第 3 章 | 工具性吸引模型、`吸引力 = 外表 x 接纳概率`、选择性故作清高、直接/中性开场白（`70%` vs. `24%`）、相识 `>9个月` 弱化外貌匹配、约会 App 与异地恋重聚缓冲 |
| **03** | `03-social-cognition-attributional-patterns-and-partner-perception.md` | 第 4 章 | 第一印象 4 大偏差、维持关系型 vs. 加剧冲突型归因、6 大宿命信念 vs. 成长信念、自我验证低自尊悖论、黑三角特质（自恋/马基雅维利/精神病态）识别 |
| **04** | `04-nonverbal-and-verbal-communication-and-conflict-deescalation.md` | 第 5 章 | 非言语 6 通道与 Hall 人际距离、社会渗透理论、感知到的伴侣回应性、7 大不良沟通病灶清理、**XYZ 精确表述**与复述/知觉检验积极倾听 |
| **05** | `05-interdependence-social-exchange-equity-and-commitment-engine.md` | 第 6 章 | `满意度 = 结果 - CL`、`依赖度 = 结果 - CLalt`、关系四象限、负面成本 `5:1` 定律、接近/回避动机、共有 vs. 交换关系、公平理论与 **Rusbult 投入模型** |
| **06** | `06-friendship-lifecycle-responsiveness-shyness-and-loneliness.md` | 第 7 章 | **资本化 2x2 矩阵**（主动-建设性回应）、**暗中支持（Invisible Support）**、老年社会情绪选择理论、面对面 vs. 肩并肩友谊、羞怯与孤独归因改造 |
| **07** | `07-love-taxonomy-passionate-arousal-and-companionate-sustainability.md` | 第 8 章 | **斯滕伯格爱情三角（8 分类）**、多巴胺唤醒 vs. 催产素相伴系统、吊桥唤醒转移实验、**Aron 自我扩展模型**、李氏 6 种爱情风格、单恋止损与父母反对协调 |
| **08** | `08-sexuality-attitudes-desire-satisfaction-and-consent-safety.md` | 第 9 章 | **社会性性行为取向（SOI）**、出轨预测因子、接近 vs. 回避性动机、独自高频看色情片危害、**性成长信念**、安全套 6 大劝说策略与反性胁迫红线 |
| **09** | `09-relational-stress-ostracism-jealousy-deception-and-forgiveness.md` | 第 10 章 | 感知关系价值、伴侣排斥/冷暴力激活 `dACC` 痛觉区、反应性 vs. 怀疑性妒忌、真相偏差（`54%` 测谎率）、反报复铁律与真诚悔过三要件宽恕闭环 |
| **10** | `10-conflict-dynamics-demand-withdraw-and-four-couple-types.md` | 第 11 章 | 4 类激发事件、**要求/退避模式**（`80%` 女要求/男退避与男性生理泛滥）、**戈特曼四类夫妻**与**末日四骑士**（批评/轻蔑/防御/阻挠）、`69%` 永恒分歧 |
| **11** | `11-power-dynamics-interdependence-asymmetry-and-violence-triage.md` | 第 12 章 | **Waller 最小兴趣原则**、6 大权力来源与 2x2 策略、平权红利、**Johnson 暴力三分类（SCV / IT / VR）**、**`I3` 暴力模型**、防跟踪骚扰**零接触铁律** |
| **12** | `12-relationship-dissolution-divorce-prediction-and-maintenance-repair.md` | 第 13-14 章 | **VSA 脆弱-压力-适应模型**、Huston 早期幻灭模型、Duck 分手四阶段与**社交媒体关系清理**、**米开朗基罗现象**、**感激三步法**、**TBCT / CBCT / IBCT / EFT** |

## 4. 安装与使用方法

### 方式一：从 distill-skills 仓库取包

```bash
git clone --depth 1 https://github.com/WRM-FW/distill-skills.git
cp -r distill-skills/skills/intimate-relationships-8th <你的 Agent Skill 目录>/
```

本 Skill 不单独建仓，因此不要用 `<your-username>/intimate-relationships-8th` 这种仓库路径安装。

### 方式二：本地目录或 ZIP 归档导入

1. 取到完整的 `intimate-relationships-8th/` 目录（含 `SKILL.md` 与 `references/`）。
2. 将其放置于工作区的 `skills/intimate-relationships-8th/` 路径下，或在 Skills Manager UI 中直接上传该目录/ZIP 包。

### 方式三：对话触发示例

- **关系冲突与要求/退避死锁破局**：
  > `@intimate-relationships-8th 我和伴侣最近一吵架就是我追着他要说法、他冷着脸看手机一言不发，事后我总觉得他根本不爱我，请帮我诊断并给出破局话术。`
- **成人依恋与低自尊内耗评估**：
  > `@intimate-relationships-8th 帮我用书里的 12 题依恋量表测一下我的依恋类型，并分析为什么伴侣夸我时我反而觉得他在敷衍我。`
- **社会交换分合抉择与家务重平衡**：
  > `@intimate-relationships-8th 结婚三年感觉变成了室友，家务育儿全是我干，请用社会交换四象限、公平理论和自我扩展模型帮我做一份诊断和改善方案。`

## 5. 环境依赖说明

- **运行时依赖**：本技能为纯 Markdown 知识与结构化决策路由技能（Zero-dependency Markdown Skill），无需安装额外的 Python 或 Node.js 第三方库即可在任何支持 `SKILL.md` 及 `references/` 读取的 Agent 运行时中直接工作。
- **原著参考致谢**：Rowland S. Miller, *Intimate Relationships (8th Edition)*, McGraw-Hill Education, 2018 / [美] 罗兰·米勒 著，王伟平 译，彭凯平 审校，《亲密关系（第8版）》，人民邮电出版社，2024。

---

> 本 Skill 由 [distill-skills](https://github.com/WRM-FW/distill-skills) 仓库统一收录维护，全部 Skill 索引见[仓库根 README](../../README.md)。
