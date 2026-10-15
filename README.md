# distill-skills

> **个人 Agent Skill 统一管理仓库**
> 汇聚由经典书籍、专业课程、实用工具及人物语料中深度蒸馏的 Agent Skills。通过结构化与能力化沉淀，打造开箱即用的个人外脑知识资产。
> * 核心代表作：psychology-system（心理学体系化技能）、nsca-5th（体能与力量训练科学）

下面「✨Masterpiece」小节收录这两个核心代表作。仓库内的最高推荐标识统一写作 `✨Masterpiece`，
不再使用其它叫法。

- 仓库地址：<https://github.com/WRM-FW/distill-skills>（原名 `persona-luoxiang`，GitHub 自动重定向旧链接）
- 布局：`skills/<skill-name>/`，一个 Skill 一个目录，仓库根只放索引与规范
- 入口：每个 Skill 的 `SKILL.md`（YAML frontmatter 里的 `name` 与 `description` 即触发依据）
- 全仓库统一许可证：**[PolyForm Noncommercial 1.0.0](LICENSE)**（SPDX `PolyForm-Noncommercial-1.0.0`）

蒸馏的目标不是把资料搬成 markdown，而是把「遇到某类问题时该走哪套判断流程」写成 Agent
可以直接加载并执行的路由文件 + 能力卡。

---

## ✨Masterpiece

两个当前维护最完整、跨场景复用最多的 Skill。想先试一个，从这里开始。

### 1. `psychology-system` — 跨 28 部心理学典籍的整合路由

| 项目 | 值 |
| --- | --- |
| 目录 | [`skills/psychology-system/`](skills/psychology-system/) |
| 解决的问题 | 心理动力/防御、人格类型、课题分离、存在焦虑、TA 交互分析、症状分诊、说服与群体影响、亲密关系、非暴力沟通与说服性对话、习惯与刻意练习、认知偏差与选择架构 |
| 来源 | Google Drive 心理学书库 28 部核心著作（弗洛伊德、荣格、阿德勒、亚隆、弗洛姆、克尔凯郭尔、戴博德、戈特利布、津巴多、钱铭怡、西奥迪尼、勒庞、迈尔斯、彭凯平、斯滕伯格、卢森堡、都希格、周岭、艾利克森、克利尔、塞勒、芒格等，分属五大支柱） |
| 上游 Skill | [kangarooking/cangjie-skill](https://github.com/kangarooking/cangjie-skill)（`RIA-TV++` 流水线，MIT）— Single 主路由模式 |
| 结构 | `SKILL.md` 主路由 + `references/book/{overview,glossary}.md` + 12 张六段式能力卡（R/I/A1/A2/E/B） |
| 许可 | PolyForm Noncommercial 1.0.0（原创内容）；原著文字版权归出版社与作者 |
| 版本 | `psychology-system-v1.0.0`，见 [CHANGELOG](skills/psychology-system/CHANGELOG.md) |
| 触发 | `@psychology-system 面对领导批评就习惯性道歉、事后又生闷气，用 PAC 状态和课题分离帮我诊断，给一段非暴力沟通的回话` |

它与下面三个单书 Skill 的关系：`psychology-system` 是跨书整合层，横向比较与「该用哪个学派」归它；
`zimbardo-psych-8th` / `social-psychology` / `intimate-relationships-8th` 是单书深挖层，
要原书章节级别的实验数据、量表与阈值时走它们。两者结论冲突时，以单书 Skill 的原文锚点为准。

### 2. `nsca-5th` — NSCA 教材第 5 版整书训练方案引擎

| 项目 | 值 |
| --- | --- |
| 目录 | [`skills/nsca-5th/`](skills/nsca-5th/) |
| 解决的问题 | 抗阻与周期化计划、%1RM/SRB/RIR 与链带/加重离心负荷、测力台与 VBT 测试编排和结果统计、RAMP 热身与 PAPE 激活、超等长与复合对比、冲刺/变向/减速、间歇与有氧配比、过度训练识别与减量、青少年/女性孕产/老年人群适配、运动营养与 RED-S、伤病康复与场馆法务 |
| 来源 | *Essentials of Strength Training and Conditioning, 5th Edition*（Haff & Triplett 主编，2027，全书 26 章） |
| 上游 Skill | [kangarooking/cangjie-skill](https://github.com/kangarooking/cangjie-skill)（`RIA-TV++` 流水线，MIT） |
| 结构 | `SKILL.md` 主路由 + `references/book/{overview,glossary}.md` + 12 张六段式能力卡 |
| 许可 | PolyForm Noncommercial 1.0.0（原创内容）；教材正文版权归 Human Kinetics 与原作者 |
| 版本 | `nsca-5th-v1.0.0`，见 [CHANGELOG](skills/nsca-5th/CHANGELOG.md) |
| 触发 | `用 nsca-5th 给一名打赛季的高校橄榄球线卫排 12 周力量周期，含测试电池和减量周` |

需要更短、参数更集中的经典 `%1RM` 查表版本时看 [`skills/nsca-3rd/`](skills/nsca-3rd/)，
两者的分工写在它的 README 里。

---

## 全部 Skill

| 目录 | 主题 | 来源物料 | 能力卡 | 上游 Skill | 许可 | 版本 |
| --- | --- | --- | --- | --- | --- | --- |
| [`skills/psychology-system/`](skills/psychology-system/) | 心理学与行为科学整合路由 | 28 部心理学著作 | 12 | [cangjie-skill](https://github.com/kangarooking/cangjie-skill) | PolyForm NC 1.0.0 | `psychology-system-v1.0.0` |
| [`skills/nsca-5th/`](skills/nsca-5th/) | 力量与体能训练全链 | NSCA 教材第 5 版（26 章） | 12 | [cangjie-skill](https://github.com/kangarooking/cangjie-skill) | PolyForm NC 1.0.0 | `nsca-5th-v1.0.0` |
| [`skills/nsca-3rd/`](skills/nsca-3rd/) | 力量与体能训练（经典参数） | NSCA 教材第 3 版（22 章） | 10 | [cangjie-skill](https://github.com/kangarooking/cangjie-skill) | PolyForm NC 1.0.0 | `nsca-3rd-v1.0.0` |
| [`skills/intimate-relationships-8th/`](skills/intimate-relationships-8th/) | 亲密关系诊断与冲突降级 | 米勒《亲密关系（第 8 版）》 | 12 | [cangjie-skill](https://github.com/kangarooking/cangjie-skill) | PolyForm NC 1.0.0 | `intimate-relationships-8th-v1.0.0` |
| [`skills/social-psychology/`](skills/social-psychology/) | 社会影响、说服与群体决策 | 迈尔斯《社会心理学（第 11 版）》 | 12 | [cangjie-skill](https://github.com/kangarooking/cangjie-skill) | PolyForm NC 1.0.0 | `social-psychology-v1.0.0` |
| [`skills/zimbardo-psych-8th/`](skills/zimbardo-psych-8th/) | 普通心理学全 14 章 50 概念 | 津巴多《普通心理学（第 8 版）》 | 12 | [cangjie-skill](https://github.com/kangarooking/cangjie-skill) | PolyForm NC 1.0.0 | `zimbardo-psych-8th-v1.0.0` |
| [`skills/persona-luoxiang/`](skills/persona-luoxiang/) | 人物思维框架与表达风格 | B 站公开视频字幕物料 132 份 | 11 份调研笔记 | [Distilly](https://github.com/titanwings/distilly) + [nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | PolyForm NC 1.0.0 | `persona-luoxiang-v1.0.0` |

### 上游判定依据（不是凭名称推断）

- **cangjie-skill**：六个 Skill 的 `SKILL.md` 与 README 都自述走「仓颉 `cangjie-skill`（`RIA-TV++` 流水线）」，
  其能力卡的 `R / I / A1 / A2 / E / B` 六段、`阶段 0-3`、Triple Verification 与 `references/capabilities/` 目录约定，
  与 [kangarooking/cangjie-skill](https://github.com/kangarooking/cangjie-skill) 的 README 术语逐项对应。
  注意：各 Skill 未内嵌该仓库的提交号或版本号，**具体使用的管线版本待确认**。
- **Distilly + nuwa-skill**：`persona-luoxiang` 在 `NOTICE.md`、`THIRD_PARTY_NOTICES.md`
  与 README 第八节明确列出了两个上游及其复用范围。
- 同名的 [Yeadon8888/cangjie-skill](https://github.com/Yeadon8888/cangjie-skill) 是「基于女娲架构」的人物蒸馏引擎，
  与这六个整书/教材 Skill 的产物形态不符，故未采用。若你有确切的管线版本记录，替换上表链接即可。

---

## 目录约定

```text
distill-skills/
├── README.md                    # 本文件：✨Masterpiece + 全量索引 + 版本规范
├── LICENSE                      # PolyForm Noncommercial 1.0.0
└── skills/
    └── <skill-name>/            # kebab-case，与 SKILL.md frontmatter 的 name 一致
        ├── SKILL.md             # 必需，唯一加载入口（路由 + 触发边界 + 执行流程）
        ├── README.md            # 面向人的说明：上游、来源、结构、安装、边界
        ├── CHANGELOG.md         # 本 Skill 的版本记录（Keep-a-Changelog 风格）
        ├── LICENSE              # 与本仓库根一致
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
2. 建 `skills/<name>/`，目录名与 `SKILL.md` frontmatter 的 `name` 一致；重复主题先看索引表。
3. 补 `README.md`：上游 Skill 链接、来源物料（书名/版本/章节数或语料份数）、能做什么、目录结构、安装、边界。
4. 放 `LICENSE`（PolyForm NC 1.0.0）与本 Skill 的 `CHANGELOG.md`，首条记 `v1.0.0`。
5. 在上面的「全部 Skill」表加一行；达到 ✨Masterpiece 标准的，同时更新 ✨Masterpiece 小节。
6. 提交后按下一节打标签、建 Release。

### ✨Masterpiece 入选标准

满足两条以上即进入 ✨Masterpiece 小节，**不设数量上限**；不再满足标准（长期失更、结构残缺）时
移回索引表，条目本身不删。

- 覆盖的场景跨多个领域，不是单一书目的复读；
- 结构完整：主路由 + 能力卡 + 边界 + 术语表齐全；
- 经过验证：有自检脚本或独立评审记录，且近期仍在更新；
- 上游与来源可追溯，下游可以判断能不能再分发。

## 版本与 Release 规范

一个仓库放多个 Skill，版本按 Skill 命名空间隔离：

- **标签格式**：`<skill-name>-v<semver>`，例如 `nsca-5th-v1.0.0`、`psychology-system-v1.2.0`。
  标签指向该 Skill 内容最后一次变化的提交；只改文档或索引表时用补丁号。
- **CHANGELOG**：每个 Skill 目录独立维护 `CHANGELOG.md`，新增版本时在文件顶部追加一节，
  与标签同名同号，禁止只改标签不改记录。
- **Release**：每个标签建一个 GitHub Release，标题为 `<skill-name> vX.Y.Z`，
  正文写三件事——本版核心功能变化、上游与蒸馏来源（含原书版本/语料范围）、许可证。
- **单 Skill 发版流程**：

  ```bash
  cd <仓库工作目录>
  # 1. 只改这个 Skill 的文件，提交并推送
  git add skills/<skill-name> && git commit -m "<skill-name>: <变更摘要>" && git push
  # 2. 打命名空间标签
  git tag -a <skill-name>-v<X.Y.Z> -m "<skill-name> vX.Y.Z"
  git push origin <skill-name>-v<X.Y.Z>
  # 3. 建 Release
  gh release create <skill-name>-v<X.Y.Z> --title "<skill-name> vX.Y.Z" --notes "<本版变化 / 来源 / 许可>"
  ```

- **历史标签处置**：原仓库的裸 `v1.0.0` 及其 Release 已删除，由 `persona-luoxiang-v1.0.0` 取代；
  新标签指向清理与改签之后的提交（`skills/persona-luoxiang/CHANGELOG.md` 记了这次变更的内容差异）。
- 版本号起点统一为 `v1.0.0`：本次入库的 7 个 Skill 各建一个初始 Release。

## 安装

```bash
git clone --depth 1 https://github.com/WRM-FW/distill-skills.git
cp -r distill-skills/skills/<skill-name> <你的 Agent Skill 目录>/
```

各 Agent 的 Skill 目录位置不同（如 `.claude/skills/`、`.cursor/skills/`、全局 `~/skills/`），
以其官方文档为准；整个目录（含 `references/` 与 `CHANGELOG.md`）都要拷过去，只拷 `SKILL.md` 会丢失能力卡。

只想取单个 Skill 时用稀疏检出：

```bash
git clone --filter=blob:none --sparse https://github.com/WRM-FW/distill-skills.git
cd distill-skills && git sparse-checkout set skills/nsca-5th
```

## 历史与兼容性

- 本仓库由 `persona-luoxiang` 重命名而来，提交历史、`v1.0.0` 之前的全部记录与 star 保留；
  旧 URL 由 GitHub 自动重定向。
- 罗翔 Skill 的内容从仓库根整体迁入 `skills/persona-luoxiang/`，内部相对路径不受影响；
  文中指向 `WRM-FW/persona-luoxiang` 的链接已改为新仓库地址。
- 2026-10-15 清理掉的单体项目遗留文件：`.build/meta.json`（Distilly `skill_writer` 的一次性构建输入）
  与 `knowledge/research/raw/`（11 份与 `references/research/` 逐字重复的输入副本）。
  `skill.yaml`、`meta.json`、`manifest.json`、`persona*.md`、`work*.md`、`scripts/` 作为上游管线溯源证据保留。
- 单 Skill 独立仓库不再维护。

## 许可与边界

- 全仓库统一采用 **[PolyForm Noncommercial License 1.0.0](LICENSE)**：允许个人使用、研究、教学与非商业组织用途，
  **禁止任何商业用途**；如需商业授权，另行联系权利人。
- 各 Skill 目录内的 `LICENSE` 与本仓库根一致；`SKILL.md` frontmatter 不声明许可证，避免与文件冲突。
- 教材蒸馏类 Skill（NSCA、津巴多、迈尔斯、米勒、28 部心理学书库）提炼的是方法论与参数结构，
  原书文字与图表版权归出版社与作者，本仓库不主张对原书的任何权利。
- `persona-luoxiang` 的上游 [Distilly](https://github.com/titanwings/distilly) 与
  [nuwa-skill](https://github.com/alchaincyf/nuwa-skill) 均为 MIT：其版权声明与许可文本按要求保留在
  `NOTICE.md` 与 `THIRD_PARTY_NOTICES.md` 中，这两处不属于本仓库许可证的替换范围。该 Skill 曾以 MIT
  发布 `v1.0.0`，改为 PolyForm NC 只约束此后发布的版本；已在旧 MIT 下取得副本的使用者仍可按 MIT 处理。
- `persona-luoxiang` 是基于公开字幕的人物风格研究实验，**未获得罗翔本人授权、本人未参与、也不代表其认可**；
  详见该目录 README 第七至九节。
- 心理治疗与医学类 Skill 输出的是分析与沟通方案，不构成诊断或处方；出现自伤、伤人或急性症状信号时转专业机构。
