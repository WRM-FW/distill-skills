# distill-skills

个人蒸馏 Skill 的统一存储与管理仓库。从书、教材、课程、工具文档与人物公开物料里蒸馏出来的
Agent Skill 都收在这里：一个 Skill 一个目录，仓库根只放索引与规范。

蒸馏的目标不是把资料搬成 markdown，而是把「遇到某类问题时该走哪套判断流程」写成 Agent
可以直接加载并执行的路由文件 + 能力卡。

- 仓库地址：<https://github.com/WRM-FW/distill-skills>（原名 `persona-luoxiang`，GitHub 自动重定向旧链接）
- 布局：`skills/<skill-name>/`
- 入口：每个 Skill 的 `SKILL.md`（YAML frontmatter 里是 `name` 与 `description`，即触发依据）

---

## 精选 Skill

两个当前维护最完整、跨场景复用最多的 Skill。想先试一个，从这里开始。

### 1. `psychology-system` — 跨 28 部心理学典籍的整合路由

| 项目 | 值 |
| --- | --- |
| 目录 | [`skills/psychology-system/`](skills/psychology-system/) |
| 解决的问题 | 心理动力/防御、人格类型、课题分离、存在焦虑、TA 交互分析、症状分诊、说服与群体影响、亲密关系、非暴力沟通与说服性对话、习惯与刻意练习、认知偏差与选择架构 |
| 来源 | Google Drive 心理学书库 28 部核心著作（弗洛伊德、荣格、阿德勒、亚隆、弗洛姆、克尔凯郭尔、戴博德、戈特利布、津巴多、钱铭怡、西奥迪尼、勒庞、迈尔斯、彭凯平、斯滕伯格、卢森堡、都希格、周岭、艾利克森、克利尔、塞勒、芒格等，分属五大支柱） |
| 管线 | 仓颉 `cangjie-skill`（`RIA-TV++`），Single 主路由模式 |
| 结构 | `SKILL.md` 主路由 + `references/book/{overview,glossary}.md` + 12 张六段式能力卡（R/I/A1/A2/E/B） |
| 许可 | MIT |
| 触发 | `@psychology-system 面对领导批评就习惯性道歉、事后又生闷气，用 PAC 状态和课题分离帮我诊断，给一段非暴力沟通的回话` |

它与下面四个单书 Skill 的关系：`psychology-system` 是跨书整合层，横向比较与「该用哪个学派」归它；
`zimbardo-psych-8th` / `social-psychology` / `intimate-relationships-8th` 是单书深挖层，
要原书章节级别的实验数据、量表与阈值时走它们。两者结论冲突时，以单书 Skill 的原文锚点为准。

### 2. `nsca-5th` — NSCA 教材第 5 版整书训练方案引擎

| 项目 | 值 |
| --- | --- |
| 目录 | [`skills/nsca-5th/`](skills/nsca-5th/) |
| 解决的问题 | 抗阻与周期化计划、%1RM/SRB/RIR 与链带/加重离心负荷、测力台与 VBT 测试编排和结果统计、RAMP 热身与 PAPE 激活、超等长与复合对比、冲刺/变向/减速、间歇与有氧配比、过度训练识别与减量、青少年/女性孕产/老年人群适配、运动营养与 RED-S、伤病康复与场馆法务 |
| 来源 | *Essentials of Strength Training and Conditioning, 5th Edition*（Haff & Triplett 主编，2027，全书 26 章） |
| 管线 | 仓颉 `cangjie-skill`（`RIA-TV++`） |
| 结构 | `SKILL.md` 主路由 + `references/book/{overview,glossary}.md` + 12 张六段式能力卡 |
| 许可 | 未附独立许可证文件，见「许可与边界」 |
| 触发 | `用 nsca-5th 给一名打赛季的高校橄榄球线卫排 12 周力量周期，含测试电池和减量周` |

需要更短、参数更集中的经典 `%1RM` 查表版本时看 [`skills/nsca-3rd/`](skills/nsca-3rd/)，
两者的分工写在它的 README 里。

---

## 全部 Skill

| 目录 | 主题 | 来源物料 | 能力卡 | 许可 | 状态 |
| --- | --- | --- | --- | --- | --- |
| [`skills/psychology-system/`](skills/psychology-system/) | 心理学与行为科学整合路由 | 28 部心理学著作 | 12 | MIT | 精选，持续更新 |
| [`skills/nsca-5th/`](skills/nsca-5th/) | 力量与体能训练全链 | NSCA 教材第 5 版（26 章） | 12 | 未定 | 精选，持续更新 |
| [`skills/nsca-3rd/`](skills/nsca-3rd/) | 力量与体能训练（经典参数） | NSCA 教材第 3 版（22 章） | 10 | 未定 | 与 5th 并存，按分工路由 |
| [`skills/intimate-relationships-8th/`](skills/intimate-relationships-8th/) | 亲密关系诊断与冲突降级 | 米勒《亲密关系（第 8 版）》 | 12 | MIT | 稳定 |
| [`skills/social-psychology/`](skills/social-psychology/) | 社会影响、说服与群体决策 | 迈尔斯《社会心理学（第 11 版）》 | 12 | MIT | 稳定 |
| [`skills/zimbardo-psych-8th/`](skills/zimbardo-psych-8th/) | 普通心理学全 14 章 50 概念 | 津巴多《普通心理学（第 8 版）》 | 12 | MIT | 稳定，含 `scripts/validate_skill.py` |
| [`skills/persona-luoxiang/`](skills/persona-luoxiang/) | 人物思维框架与表达风格 | B 站公开视频字幕物料 132 份 | 11 份调研笔记 | MIT（仅覆盖本目录原创内容） | 已发布 `v1.0.0`，仓库重构未改动其内容 |

---

## 目录约定

```text
distill-skills/
├── README.md                    # 本文件：精选区 + 全量索引 + 规范
└── skills/
    └── <skill-name>/            # kebab-case，与 SKILL.md frontmatter 的 name 一致
        ├── SKILL.md             # 必需，唯一加载入口（路由 + 触发边界 + 执行流程）
        ├── README.md            # 面向人的说明：来源、结构、安装、边界
        ├── LICENSE / NOTICE.md  # 有明确可授权范围时才附；不确定的留空并在索引表标「未定」
        ├── references/
        │   ├── book/            # overview.md（整书结构）+ glossary.md（术语与定量参数）
        │   └── capabilities/    # NN-<主题>.md 能力卡，六段式 R/I/A1/A2/E/B
        └── scripts/             # 可选，校验与生成脚本
```

约束：

- `SKILL.md` 只做路由，正文控制在 500 行以内，细节下沉到 `references/`（渐进式披露）。
- `description` 小于 1024 字符，写清「什么场景该触发」，Agent 靠它选型。
- 每张能力卡必须带 `B`（边界与失败模式）：伦理红线、时代局限、典型误用。
- 同一主题多版本并存时（如 NSCA 3rd/5th），在 README 里写清分工，不要只靠目录名。

## 收录与维护流程

新增一个 Skill：

1. 蒸馏产出先在自己的工作目录完成，通过结构自检后再入库。
2. 建 `skills/<skill-name>/`，目录名与 `SKILL.md` 的 `name` 一致；重复主题先看索引表是否已有。
3. 补 `README.md`：来源物料（书名/版本/章节数或语料份数）、能做什么、目录结构、安装、边界。
4. 在上面的「全部 Skill」表加一行；如果它够格进精选区，同时更新精选小节。
5. 打标签：`<skill-name>-vX.Y.Z`（例如 `nsca-5th-v1.0.0`）。

精选区的入选标准，满足两条以上再进：

- 覆盖的场景跨多个领域，不是单一书目的复读；
- 结构完整：主路由 + 能力卡 + 边界 + 术语表齐全；
- 经过验证：有自检脚本或独立评审记录，且近期仍在更新；
- 有明确许可或来源声明，下游可以判断能不能再分发。

精选区不设数量上限：达到上面标准的 Skill 都可以进；不再满足标准（长期失更、结构残缺）时移回索引表，条目本身不删。

## 安装

```bash
git clone --depth 1 https://github.com/WRM-FW/distill-skills.git
cp -r distill-skills/skills/<skill-name> <你的 Agent Skill 目录>/
```

各 Agent 的 Skill 目录位置不同（如 `.claude/skills/`、`.cursor/skills/`、全局 `~/skills/`），
以其官方文档为准；整个目录（含 `references/`）都要拷过去，只拷 `SKILL.md` 会丢失能力卡。

只想取单个 Skill 时用稀疏检出：

```bash
git clone --filter=blob:none --sparse https://github.com/WRM-FW/distill-skills.git
cd distill-skills && git sparse-checkout set skills/nsca-5th
```

## 历史与兼容性

- 本仓库由 `persona-luoxiang` 重命名而来，原提交历史、`v1.0.0` 标签与 star 全部保留；
  旧 URL 由 GitHub 自动重定向。
- 罗翔 Skill 的内容从仓库根整体迁入 `skills/persona-luoxiang/`，内部相对路径不受影响；
  文中指向 `WRM-FW/persona-luoxiang` 的链接已改为新仓库地址。
- 单 Skill 独立仓库不再维护；今后发版走 `<skill-name>-vX.Y.Z` 标签，
  旧的裸版本号 `v1.0.0` 只对应罗翔 Skill。

## 许可与边界

- 各 Skill 的许可状态见索引表，未标注 MIT 的目录**不代表公共领域**，只是尚无明确授权范围。
- 教材蒸馏类 Skill（NSCA、津巴多、迈尔斯、米勒）提炼的是方法论与参数结构，
  原书文字与图表版权归出版社与作者，本仓库不主张对原书的任何权利；再分发前请自行确认使用权。
- `persona-luoxiang` 是基于公开字幕的人物风格研究实验，**未获得罗翔本人授权、本人未参与、也不代表其认可**；
  详见该目录 README 第七至九节。
- 心理治疗与医学类 Skill 输出的是分析与沟通方案，不构成诊断或处方；出现自伤、伤人或急性症状信号时转专业机构。
