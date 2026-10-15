# psychology-system

> **✨Masterpiece** —— 仓库的核心代表作之一，入选依据见[仓库根 README](../../README.md#masterpiece)。

> 上游 Skill：[仓颉 cangjie-skill](https://github.com/kangarooking/cangjie-skill)（`RIA-TV++` 流水线，MIT）　｜　许可：[PolyForm Noncommercial 1.0.0](LICENSE)　｜　版本：`v1.0.0`（标签 `psychology-system-v1.0.0`）　｜　版本记录：[CHANGELOG.md](CHANGELOG.md)

基于 28 部心理学、精神分析、心理治疗、社会心理学、亲密关系、深度沟通、脑科学与行为经济学经典著作，按仓颉 `cangjie-skill` (`RIA-TV++` 流水线) 蒸馏构建的全书系可执行 Agent Skill。

## 项目简介

`psychology-system` 采用 **Single 主路由模式** 组织，将跨学派心理学理论转化为可触发、可执行、可核验的决策矩阵与操作流程。每张能力卡严格遵循 `RIA++` 六段式规范：

- **R (Reading - 原文锚点)**：精确定位原著章节、核心实验与因果机制。
- **I (Interpretation - 方法论骨架)**：提炼定量参数表、诊断矩阵与决策公式。
- **A1 (Past Application - 原著案例闭环)**：还原书中经典案例的【问题 -> 方法 -> 结论 -> 结果】闭环。
- **A2 (Future Trigger - 触发与邻近边界)**：明确用户触发信号及与相邻能力卡的路由分工。
- **E (Execution - 分步执行指令)**：提供确定性的 1-2-3 执行步骤、输入输出与完成判准。
- **B (Boundary - 适用边界与失败模式)**：标注伦理红线、时代局限与典型误用反例。

## 目录结构

```text
psychology-system/
├── README.md                  # 仓库说明文档（用途、目录结构、安装使用与能力总览）
├── LICENSE                    # PolyForm Noncommercial 1.0.0 许可证
├── .gitignore                 # Git 忽略规则配置
├── SKILL.md                   # Skill 主路由入口文件（含 YAML Frontmatter 与四步总控流程）
└── references/
    ├── book/
    │   ├── overview.md        # 阶段 0：Adler 整书/跨书四步理解与五大支柱架构
    │   └── glossary.md        # 跨书标准化术语、公式与定量参数词典
    └── capabilities/          # 12 张 RIA-TV++ 核心能力卡
        ├── 01-freudian-psychodynamics-defense-dream.md
        ├── 02-jungian-analytical-types-individuation.md
        ├── 03-adlerian-teleology-task-separation.md
        ├── 04-existential-psychotherapy-fromm-kierkegaard.md
        ├── 05-transactional-analysis-clinical-process.md
        ├── 06-abnormal-psychology-clinical-triage.md
        ├── 07-persuasion-social-influence-defense.md
        ├── 08-crowd-psychology-collective-dynamics.md
        ├── 09-intimate-relationships-sternberg-love.md
        ├── 10-nonviolent-supercommunication-system.md
        ├── 11-cognitive-awakening-deliberate-habits.md
        └── 12-behavioral-economics-nudge-debiasing.md
```

## 12 大能力卡与 28 部原著映射表

| 模块编号 | 能力卡文件 | 核心算子与定量标尺 | 蒸馏原著书单 |
| :--- | :--- | :--- | :--- |
| **01** | `01-freudian-psychodynamics-defense-dream.md` | 本我-自我-超我三元冲突、3类焦虑、9种防御机制层级、强迫性重复、释梦4工序逆向拆解 | 弗洛伊德《自我与本我》《超越唯乐原则》《集体心理学和自我的分析》《弗洛伊德文集（全12册：释梦/精神分析引论等）》 |
| **02** | `02-jungian-analytical-types-individuation.md` | 荣格八维(`E/I x T/F/S/N`)与第四劣势功能阴影补偿表、情结探测、四大原型、解梦放大法3步、主动想象4步 | 荣格《心理类型》《分析心理学的理论与实践》《未发现的自我》《寻求灵魂的现代人》《原型与集体无意识》《荣格作品集》《荣格自传》《红书》 |
| **03** | `03-adlerian-teleology-task-separation.md` | 原因论向目的论翻转、课题分离黄金判准、纵向表扬批评转横向鼓励感谢、共同体感觉3支柱 | 岸见一郎 & 古贺史健《被讨厌的勇气：“自我启发之父”阿德勒的哲学课》 |
| **04** | `04-existential-psychotherapy-fromm-kierkegaard.md` | 亚隆四大终极关怀（死亡/自由/孤独/无意义）、克尔凯郭尔绝望阶梯、弗洛姆3种逃避自由机制与成熟之爱4要素 | 欧文·亚隆《存在主义心理治疗》《当尼采哭泣》《叔本华的治疗》、弗洛姆《逃避自由》《爱的艺术/论不服从/存在的艺术》、克尔凯郭尔《文集10册》 |
| **05** | `05-transactional-analysis-clinical-process.md` | 伯恩 PAC 三自我状态、4种人生坐标、`PLOM` 与 `NIGYSOB` 心理游戏断电法、“欢迎来到荷兰”哀伤整合 | 罗伯特·戴博德《蛤蟆先生去看心理医生》、洛莉·戈特利布《也许你该找个人聊聊》 |
| **06** | `06-abnormal-psychology-clinical-triage.md` | 临床 4D 异常判准、素质-应激模型、6大临床谱系鉴别、贝克 10 项认知扭曲、行为激活(BA)与暴露反应预防(ERP) | 《变态心理学（第6版）》、钱铭怡《变态心理学》、菲利普·津巴多《津巴多普通心理学（第8版）》 |
| **07** | `07-persuasion-social-influence-defense.md` | 西奥迪尼6大说服武器及反操控防卫（互惠/留面子法、登门槛/抛低球、点名求救、权威双问、稀缺刹车）、自我合理化4策略 | 罗伯特·西奥迪尼《影响力（经典版）》、戴维·迈尔斯《社会心理学》、彭凯平《社会心理学精品译丛（7册）》、《以自我合理化为理论视角》 |
| **08** | `08-crowd-psychology-collective-dynamics.md` | 勒庞群体精神统一律（匿名/传染/暗示）、动员3手段（断言-重复-传染）、去个体化/群体极化/群体思维防呆 | 古斯塔夫·勒庞《乌合之众：群体心理学》、弗洛伊德《集体心理学和自我的分析》、戴维·迈尔斯《社会心理学》 |
| **09** | `09-intimate-relationships-sternberg-love.md` | 斯滕伯格爱情三元论（8种爱情类型）、激情正负过程对手律、成人依恋4象限、`Outcome/CL/CL_alt` 算账公式、`>=5:1` 正负互动比 | 罗伯特·斯滕伯格《爱情心理学》、罗兰·米勒《亲密关系（第8版 / 十周年纪念版）》 |
| **10** | `10-nonviolent-supercommunication-system.md` | 都希格3类对话匹配原则、理解循环3步法、卢森堡 NVC 四要素（观察-感受-需要-请求）、阿德勒知觉检核3步法 | 马歇尔·卢森堡《非暴力沟通》、查尔斯·都希格《超级沟通者》、罗纳德·阿德勒《沟通的艺术（第15版）》 |
| **11** | `11-cognitive-awakening-deliberate-habits.md` | 三重大脑算力比(`1100万 vs 40次/秒`)、舒适区边缘(`+4%-10%`)、原子习惯正反4定律与两分钟规则、刻意练习心理表征与 `3F` | 周岭《认知觉醒》、安德斯·艾利克森《刻意练习》、詹姆斯·克利尔《原子习惯》、尼古拉斯·卡尔《浅薄》、卡尔·纽波特《深度工作》 |
| **12** | `12-behavioral-economics-nudge-debiasing.md` | 双系统(System 1/2)、损失厌恶系数 `2.0-2.5x`、心理账户与沉没成本清零测试、芒格25条误判与 `Lollapalooza` 熔断、`NUDGES` 6步架构 | 理查德·塞勒 & 桑斯坦《助推》《“错误”的行为》、查理·芒格《25种人类误判心理学》、名取芳彦《别想太多啦》 |

## 安装与使用方法

### 1. 从 distill-skills 仓库取包

```bash
git clone --depth 1 https://github.com/WRM-FW/distill-skills.git
cp -r distill-skills/skills/psychology-system <你的 Agent Skill 目录>/
```

### 2. 在支持 Agent Skills 的环境中导入使用

- **Skills Manager UI 手动导入**：
  上传 `skills/psychology-system/` 整个目录（或它单独压缩后的 zip）即可。

本 Skill 不单独建仓，因此不要用 `<your-username>/psychology-system` 这种仓库路径安装。
- **对话触发示例**：
  - `"@psychology-system 我每次面对领导批评就会不自觉道歉并生几天闷气，帮我用《蛤蟆先生》的 PAC 状态和阿德勒课题分离做个诊断，并给我一段非暴力沟通的回话模板。"`
  - `"@psychology-system 我报了个高价课程但很难坚持，每次打开书就想刷手机，帮我用塞勒心理账户、三重大脑和《原子习惯》设计一套两分钟启动与防拖延方案。"`

## 环境依赖与格式规范

- **运行时依赖**：本 Skill 为纯 Markdown 声明式知识与推理路由包，**无外部二进制或第三方 API 强依赖**，兼容所有支持 `SKILL.md` 标准规范的 Agent 运行时。
- **维护校验规范**：
  - `SKILL.md` 的 YAML Frontmatter 必须包含 `name` 与 `description`（长度 `< 1024` 字符），正文行数保持在 `500` 行以内。
  - 所有 `.md` 文件列表前须保留空行，并遵循 `R / I / A1 / A2 / E / B` 六段能力卡与 `Triple Verification Audit` 结构。

## 许可证

本 Skill 的原创内容采用 [PolyForm Noncommercial License 1.0.0](LICENSE) 授权（SPDX `PolyForm-Noncommercial-1.0.0`）：可用于个人研究、学习与非商业组织用途，禁止商业用途。

上游蒸馏管线为 [cangjie-skill](https://github.com/kangarooking/cangjie-skill)（MIT）；原著文字的版权归出版社与作者，本 Skill 不主张对原著的任何权利。

---

> 本 Skill 由 [distill-skills](https://github.com/WRM-FW/distill-skills) 仓库统一收录维护，全部 Skill 索引见[仓库根 README](../../README.md)。
