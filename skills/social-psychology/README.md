# Social Psychology Skill (`social-psychology`)

基于戴维·迈尔斯（David G. Myers）经典著作《社会心理学》（*Social Psychology*, 第 11 版，侯玉波、乐国安、张智勇等译）与 **Cangjie RIA-TV++（仓颉拆书蒸馏框架）** 构建的可执行社会心理学诊断、行为干预与决策防错 Agent Skill。

## 1. 项目简介（Overview）

本 Skill将《社会心理学》（第 11 版）全书 4 编 16 章的实证研究、经典实验范式、归因与决策模型、说服工程及冲突和解协议，蒸馏为采用 **渐进式披露（Progressive Disclosure）** 架构的标准化 Agent Skill。

适用场景包括但不限于：
- **社会思维审计（Ch 1-4）**：研究效度与相关/因果鉴别、事后聪明偏差（Hindsight Bias）复盘、焦点效应与透明度错觉脱敏、规划谬误校准、凯利三维归因、基本归因错误（FAE）纠偏、计划行为理论（TPB）知行转化、登门槛（FITD）与认知失调内化、过度合理化效应防线。
- **社会影响工程（Ch 5-8）**：跨文化与性别角色规范解析、阿施从众与米尔格拉姆服从风险审计、佩蒂与卡乔波精细可能性模型（ELM 中心/外周路径说服）、麦圭尔态度免疫接种（Attitude Inoculation）、消除社会懈怠与去个体化、贾尼斯群体思维（Groupthink）8 大症状防错及莫斯科维奇少数派影响策略。
- **社会关系与临床/司法/生态应用（Ch 9-16）**：内隐偏见与克劳德·斯蒂尔刻板印象威胁（Stereotype Threat）干预、伯科威茨挫折-攻击模型与反宣泄（Anti-Catharsis）降温协议、亲密关系戈特曼 `5:1` 法则、达利与拉坦纳旁观者效应 5 步破局、公地悲剧与囚徒困境治理、奥斯古德 `GRIT` 冲突降级协议、临床统计预测优先原则与司法双盲连续列队指认规程。

## 2. 目录结构（Directory Structure）

```text
social-psychology/
├── SKILL.md                                                                 # 主路由文件（YAML 元数据 + 7大核心公理 + 12能力卡路由表 + 4步诊断闭环）
├── README.md                                                                # GitHub 仓库说明文档（用途、目录结构、安装使用方法与依赖说明）
├── LICENSE                                                                  # MIT 开源许可证
├── .gitignore                                                               # Git 忽略规则配置
└── references/                                                              # 渐进式披露参考知识库
    ├── book/
    │   ├── overview.md                                                      # 全书四编 16 章结构映射、7大底层定律与跨文化适用边界
    │   └── glossary.md                                                      # 双语核心概念词典、经典实验定量阈值与公式速查表
    └── capabilities/
        ├── 01-research-methods-hindsight-audit.md                           # 能力卡 01（第 1 章）：研究设计、因果推断与事后聪明偏差审计
        ├── 02-self-concept-control-self-serving-bias.md                     # 能力卡 02（第 2 章）：自我认知校准、焦点效应降敏、自控与自我服务偏差
        ├── 03-social-beliefs-heuristics-attribution.md                      # 能力卡 03（第 3 章）：启发式去偏、凯利三维归因与自我实现预言阻断
        ├── 04-attitudes-behavior-dissonance-self-perception.md              # 能力卡 04（第 4 章）：态度-行为转化、登门槛、认知失调与内在动机保护
        ├── 05-genes-culture-gender-roles.md                                 # 能力卡 05（第 5 章）：演化与文化规范解析、性别角色交互与跨文化适配
        ├── 06-conformity-obedience-resistance.md                            # 能力卡 06（第 6 章）：从众与权威服从风险审计、规范/信息影响与独立异议
        ├── 07-persuasion-elm-attitude-inoculation.md                        # 能力卡 07（第 7 章）：ELM 双路径说服工程、四要素优化与麦圭尔态度免疫
        ├── 08-group-dynamics-groupthink-minority-influence.md               # 能力卡 08（第 8 章）：防社会懈怠/去个体化/群体极化/群体思维与少数派影响
        ├── 09-prejudice-stereotype-threat-de-biasing.md                     # 能力卡 09（第 9 章）：偏见三元根源诊断、刻板印象威胁消除与制度化去偏
        ├── 10-aggression-triggers-violence-reduction.md                     # 能力卡 10（第 10 章）：攻击行为归因、挫折/武器/媒体触发器阻断与反宣泄
        ├── 11-attraction-intimacy-altruism-bystander.md                     # 能力卡 11（第 11-12 章）：人际吸引、亲密关系经营、旁观者破局与助人激发
        └── 12-conflict-peacemaking-clinical-legal-sustainability.md         # 能力卡 12（第 13-16 章）：社会困境治理、GRIT 和解、临床/司法防错与可持续幸福
```

## 3. 12 个 RIA-TV++ 能力模块速查表（Capability Modules）

| ID | 能力卡文件 | 对应原书章节 | 核心诊断框架与可执行干预协议 |
| :--- | :--- | :--- | :--- |
| **01** | `01-research-methods-hindsight-audit.md` | 第 1 章 | 相关 vs. 因果三向拆解、随机分配实验（RCT）四维规范、事后聪明偏差反事实反转测试 |
| **02** | `02-self-concept-control-self-serving-bias.md` | 第 2 章 | 焦点效应（`50% vs. 23%`）与透明度错觉脱敏、独立/互赖自我建构、规划谬误 `1.3x-1.5x` 校准、防御性悲观主义 |
| **03** | `03-social-beliefs-heuristics-attribution.md` | 第 3 章 | 信念固着反向撰写测试、代表性/易得性启发式与向均数回归审计、凯利三维归因决策树、基本归因错误纠偏 |
| **04** | `04-attitudes-behavior-dissonance-self-perception.md` | 第 4 章 | 计划行为理论（TPB）执行意图、登门槛（`17% -> 55%-76%`）与低球技术、理由不足效应（`$1 vs. $20`）、防过度合理化 |
| **05** | `05-genes-culture-gender-roles.md` | 第 5 章 | 标点时间 vs. 事件时间跨文化调适、能动性 vs. 群体性词汇性别去偏、人×情境（Person × Situation）交互建模 |
| **06** | `06-conformity-obedience-resistance.md` | 第 6 章 | 阿施从众（`37%`）与米尔格拉姆服从（`65%`）五维风险审计、规范影响 vs. 信息影响分离、破冰异议者与描述性规范助推 |
| **07** | `07-persuasion-elm-attitude-inoculation.md` | 第 7 章 | ELM 中心/外周路径路由、霍夫兰说服四要素配置、首因 vs. 近因出场时序、麦圭尔态度免疫三步防御协议 |
| **08** | `08-group-dynamics-groupthink-minority-influence.md` | 第 8 章 | 社会助长与社会懈怠四象限改造、去个体化实名唤醒、贾尼斯群体思维 8 症状与 5 步防错、书面头脑写作、少数派影响三铁律 |
| **09** | `09-prejudice-stereotype-threat-de-biasing.md` | 第 9 章 | 偏见 ABC 与三维根源消解、最小群体偏袒与公正世界信念纠偏、斯蒂尔反刻板印象威胁四步法与“高标准+潜力信任”反馈公式 |
| **10** | `10-aggression-triggers-violence-reduction.md` | 第 10 章 | 敌意性 vs. 工具性攻击分类、伯科威茨挫折-攻击修正模型、武器效应与媒体脱敏排查、证伪宣泄假说与非暴力果敢表达 |
| **11** | `11-attraction-intimacy-altruism-bystander.md` | 第 11-12 章 | 接近性/曝光效应/阿伦森得失曲线、戈特曼夫妻 `5:1` 互动比、达利-拉坦纳旁观者效应 5 步破局脚本、门面技术募捐转化 |
| **12** | `12-conflict-peacemaking-clinical-legal-sustainability.md` | 第 13-16 章 | 囚徒困境与公地悲剧 4C+1 治理、谢里夫超级目标与拼图教室、奥斯古德 `GRIT` 四步破冰、临床统计预测优先、司法双盲连续指认 |

## 4. 安装与使用方法（Installation & Usage）

### 方式一：从 distill-skills 仓库取包
```bash
git clone --depth 1 https://github.com/WRM-FW/distill-skills.git
cp -r distill-skills/skills/social-psychology <你的 Agent Skill 目录>/
```

本 Skill 不单独建仓，因此不要用 `<your-username>/social-psychology` 这种仓库路径安装。

### 方式二：在 Skills Manager 界面直接上传
- 直接在支持 Skill 管理的 AI 助手界面上传本 Skill根目录下的 `SKILL.md` 或整个 `social-psychology` 文件夹 / ZIP 归档包。

### 方式三：本地 Agent 工作区挂载（Claude Code / Cursor / Gemini 等）
- 将解压后的 `social-psychology/` 目录复制到项目的 `.claude/skills/social-psychology/`、`.cursor/skills/social-psychology/` 或全局 `~/skills/social-psychology/` 目录下即可自动识别。

### 调用示例（Example Prompts）
- **组织决策防错**：“使用 `@social-psychology` 审计我们高管团队为什么开会时无人敢提反对意见，并按贾尼斯五步法设计一套防群体思维评审流程。”
- **说服与提案设计**：“使用 `@social-psychology` 帮我设计一份面向持怀疑态度客户的 B2B 方案汇报策略，确定采用中心还是外周路径、单面还是正反双面论证，以及最佳出场顺序。”
- **管理激励与认知去偏**：“使用 `@social-psychology` 分析为什么我们推出按件计酬奖励后，原本热爱钻研的研发人员反而失去主动性了（过度合理化效应），并给出改进方案。”
- **危机冲突降级**：“使用 `@social-psychology` 的奥斯古德 GRIT 协议，为我们两个陷入零信任僵局的业务部门设计一套四步破冰合作方案。”

## 5. 环境依赖与兼容性（Dependencies & Compatibility）

- **运行时依赖**：**零外部代码依赖（Zero External Dependencies）**。本 Skill 采用纯 Markdown（UTF-8）与标准 YAML Frontmatter 编写，无需安装 Python/Node.js 第三方库即可运行。
- **规范兼容性**：严格遵循 Agent Skills 规范：
  - `SKILL.md` 包含标准 `name` 与 `description`（`< 1024` 字符）YAML 头信息。
  - 所有单文件长度均严格控制在 `< 500` 行以内，支持按需加载（Progressive Disclosure / `get_skill_resources`），避免挤占上下文窗口。

## 6. 致谢与文献来源（Credits & Reference）

- **理论原著**：David G. Myers, *Social Psychology* (11th Edition), McGraw-Hill. 中文版：《社会心理学》（第 11 版），戴维·迈尔斯 著，侯玉波、乐国安、张智勇 等译，人民邮电出版社。
- **蒸馏方法论**：Cangjie Skill（仓颉 RIA-TV++ 拆书蒸馏流水线）。

---

> 本 Skill 由 [distill-skills](https://github.com/WRM-FW/distill-skills) 仓库统一收录维护，全部 Skill 索引见[仓库根 README](../../README.md)。
