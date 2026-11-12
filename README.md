# distill-skills

个人 Agent Skill 仓库。每个 Skill 是一个可加载的能力包：把某一类问题的判断流程、
需要核对的参数和该避开的情况写清楚，Agent 加载后按它执行，而不是临时发挥。

共 10 个 Skill，全部以 **PolyForm Noncommercial 1.0.0** 授权（各目录带同一份 `LICENSE`）。
装在 Agent 的 Skill 目录里即可使用，用法见[安装](#安装)。

---

## 先看这里：你要做的事，对应哪个 Skill

| 你要做的事 | 用哪个 | 它给出什么 |
| --- | --- | --- |
| 分析一个心理现象、情绪反应或关系困局，但不确定该用哪个学派 | `psychology-system` | 跨 28 本书的学派路由：先判断问题属于哪一支，再给具体方法 |
| 要某本心理学教材的章节级细节：实验数据、量表计分、概念定义 | `zimbardo-psych-8th` / `social-psychology` / `intimate-relationships-8th` | 单本书的逐章能力卡，参数带原书位置 |
| 判断一段论证成不成立、犯了哪类谬误、前提可不可信 | `logic-system` | 形式化检验 + 谬误定性 + 前提审计 |
| 排训练计划、算负荷、设计测试、处理过度训练或特殊人群 | `nsca-5th` | 26 章教材级流程与阈值（经典查表可用 `nsca-3rd`） |
| 想知道「我的书库里有没有讲 X 的书」 | `personal-library-wisdom` | 228 张书卡的索引与一句话结论，按需展开 |
| 翻译一本书、去掉翻译腔、做成能上架的 EPUB | `book-translator` | 双引擎流水线 + 出版级排版脚本 |
| 用罗翔的思维方式看一件事 | `persona-luoxiang` | 6 个心智模型 + 表达风格 + 输出纪律 |

---

## ✨Masterpiece

四个最完整、验证最多的 Skill。第一次使用建议从这里挑一个。

| Skill | 解决什么问题 | 来源与规模 | 版本 |
| --- | --- | --- | --- |
| [`psychology-system`](skills/psychology-system/) | 心理学问题的**学派路由**：防御机制、人格类型、课题分离、存在焦虑、交互分析、症状分诊、说服与群体、亲密关系、沟通、习惯、决策偏差 | 28 部心理学著作，分五大支柱；12 张能力卡 + 跨书术语表 | `psychology-system-v1.0.0` |
| [`nsca-5th`](skills/nsca-5th/) | 力量与体能训练的**全链路**：计划、负荷、测试、热身、超等长、速度灵敏、周期化、营养、康复、场馆 | NSCA 教材第 5 版，26 章；12 张能力卡，参数精确到组次与百分比 | `nsca-5th-v1.0.0` |
| [`logic-system`](skills/logic-system/) | 论证的**有效性与真实性双审**：三段论、真值表、谓词逻辑、模态与反事实、悖论、归纳与证伪、谬误、名辩、结构化表达、博弈与归责 | 20 部中西逻辑学著作；11 张能力卡 + 跨书判准自检表 | `logic-system-v1.0.0` |
| [`personal-library-wisdom`](skills/personal-library-wisdom/) | 「书库里**有没有、在哪本**」：先给书目和结论，再按需展开方法 | 228 个蒸馏单元，归入 16 个主题簇；索引 + 速查 + 720 条术语 | `personal-library-wisdom-v1.0.0` |

---

## 全部 Skill

按用途分六组。每个 Skill 都是独立目录，可单独安装。

### 心理学与关系

| Skill | 解决什么问题 | 来源 | 规模 |
| --- | --- | --- | --- |
| [`psychology-system`](skills/psychology-system/) | 跨学派整合：不确定该用精神分析、阿德勒、存在主义还是行为经济学时用它 | 28 部著作（五大支柱） | 12 卡 |
| [`zimbardo-psych-8th`](skills/zimbardo-psych-8th/) | 普通心理学底座：感知、学习、记忆、发展、人格、异常心理 | 津巴多《普通心理学》第 8 版 | 12 卡 + 自检脚本 |
| [`social-psychology`](skills/social-psychology/) | 社会影响：从众、服从、说服、群体决策、偏见、攻击、旁观者、冲突降级 | 迈尔斯《社会心理学》第 11 版 | 12 卡 |
| [`intimate-relationships-8th`](skills/intimate-relationships-8th/) | 亲密关系：依恋评估、吸引、沟通、冲突、权力与暴力分诊、分手与修复 | 米勒《亲密关系》第 8 版 | 12 卡 |

### 逻辑与论证

| Skill | 解决什么问题 | 来源 | 规模 |
| --- | --- | --- | --- |
| [`logic-system`](skills/logic-system/) | 形式与非形式逻辑全谱：从三段论、真值表到悖论、证伪、谬误、名辩、金字塔、博弈 | 20 部中西逻辑学著作 | 11 卡 |

### 体能训练

| Skill | 解决什么问题 | 来源 | 规模 |
| --- | --- | --- | --- |
| [`nsca-5th`](skills/nsca-5th/) | 现行标准：新增 SRB/RIR 自动调节、VBT 与测力台、RAMP/PAPE、RED-S、孕产与老年人群 | NSCA 教材第 5 版（26 章） | 12 卡 |
| [`nsca-3rd`](skills/nsca-3rd/) | 经典参数：`%1RM` 查表、线性/波动周期化、基础测试电池、场馆面积与督导比例 | NSCA 教材第 3 版（22 章） | 10 卡 |

### 阅读与检索

| Skill | 解决什么问题 | 来源 | 规模 |
| --- | --- | --- | --- |
| [`personal-library-wisdom`](skills/personal-library-wisdom/) | 书库入口：先确认有没有、在哪本、一句话结论，再决定要不要深读 | 228 个蒸馏单元 | 16 簇 + 228 卡 |

### 语言与出版

| Skill | 解决什么问题 | 来源 | 规模 |
| --- | --- | --- | --- |
| [`book-translator`](skills/book-translator/) | 长文本与整书翻译：分块并行、术语一致、去翻译腔、EPUB 排版与打包 | 原创手写 | 7 份方法规范 + 9 个脚本 |

### 人物视角

| Skill | 解决什么问题 | 来源 | 规模 |
| --- | --- | --- | --- |
| [`persona-luoxiang`](skills/persona-luoxiang/) | 用罗翔的框架看问题：有限性先行、合乎中道、矛头向内，附带表达风格与禁语清单 | B 站公开字幕 132 份 | 11 份调研笔记 |

**上游**：九个 Skill 由 [cangjie-skill](https://github.com/kangarooking/cangjie-skill)（`RIA-TV++` 流水线，MIT）蒸馏；
`persona-luoxiang` 由 [Distilly](https://github.com/titanwings/distilly) 与
[nuwa-skill](https://github.com/alchaincyf/nuwa-skill) 生成（均 MIT）；`book-translator` 为原创手写，无上游。
上游只写作法来源，不改本仓库的许可。

**版本**：每个 Skill 独立发版，标签为 `<skill-name>-v<semver>`，版本差异见各目录 `CHANGELOG.md`。

---

## 容易混淆的三组，怎么选

| 情形 | 选择 |
| --- | --- |
| 心理学问题，先要「该用哪个学派」 | `psychology-system`（整合层） |
| 心理学问题，要某本书的具体实验、量表、章节数据 | 对应的单书 Skill（深挖层）；两者结论冲突时以单书原文为准 |
| 想确认某本书里有没有讲这个，或要一本书的一句话结论 | `personal-library-wisdom`（只给书目与结论，不展开流程） |
| 要把一个问题从头推到结论、并检查推理是否有效 | `logic-system`（完整推演流程） |
| 训练计划要现行标准与自动调节 | `nsca-5th` |
| 只需要经典 `%1RM` 查表与周期化框架 | `nsca-3rd`（参数更集中，但没有 VBT、RED-S、孕产细则） |

---

## 安装

```bash
git clone --depth 1 https://github.com/WRM-FW/distill-skills.git
cp -r distill-skills/skills/<skill-name> <你的 Agent Skill 目录>/
```

- 各 Agent 的 Skill 目录不同（`.claude/skills/`、`.cursor/skills/`、`~/skills/` 等），以其官方文档为准。
- 整个目录都要拷贝，含 `references/` 与脚本；只拷 `SKILL.md` 会丢能力卡。
- 只取一个 Skill 时用稀疏检出：

  ```bash
  git clone --filter=blob:none --sparse https://github.com/WRM-FW/distill-skills.git
  cd distill-skills && git sparse-checkout set skills/book-translator
  ```

- 固定版本：`git clone --depth 1 --branch <skill-name>-v1.0.0 https://github.com/WRM-FW/distill-skills.git`

---

## 维护规范

**目录结构**：一个 Skill 一个目录，目录名与 `SKILL.md` 的 `name` 一致。

```text
skills/<skill-name>/
├── SKILL.md          # 唯一加载入口：触发条件 + 路由 + 执行流程 + 边界
├── README.md         # 给人看的：解决什么、来源、结构、安装、限制
├── CHANGELOG.md      # 版本记录
├── LICENSE           # PolyForm Noncommercial 1.0.0
└── references/       # 能力卡、方法文档、术语表（按需引用，避免 SKILL.md 过长）
```

**新增一个 Skill**：通过结构自检 → 建目录并补四件套 → 在本文「全部 Skill」加一行 →
打标签 `<skill-name>-v<semver>` → 建 Release（写明本版能力、来源、上游、许可）。

**发版**：

```bash
git add skills/<skill-name> && git commit -m "<skill-name>: <变更>" && git push
git tag -a <skill-name>-v<X.Y.Z> -m "<skill-name> vX.Y.Z" && git push origin <skill-name>-v<X.Y.Z>
gh release create <skill-name>-v<X.Y.Z> --title "<skill-name> vX.Y.Z" --notes "<能力变化 / 来源 / 许可>"
```

**许可**：全仓库统一 PolyForm Noncommercial 1.0.0——个人研究、学习、教学与非商业组织可用，
禁止商业用途。许可只覆盖本仓库的原创表达，不覆盖被蒸馏书籍的文字与图表；引用与再分发原著内容需自行确认权利。
`persona-luoxiang` 的 Distilly / nuwa-skill MIT 署名声明保留在 `NOTICE.md` 与 `THIRD_PARTY_NOTICES.md`。

---

## 沿革

- 2026-10-15：仓库由 `persona-luoxiang` 改名为 `distill-skills`，提交历史、star 与旧 URL 重定向保留；
  罗翔 Skill 从根目录迁入 `skills/persona-luoxiang/`。
- 2026-10-15：全仓许可证由 MIT 统一为 PolyForm NC；旧裸标签 `v1.0.0` 与其 Release 删除，改用命名空间标签。
- 2026-11-12：收 `book-translator`；移除 `nsca-5th-deepseek`（教材二次构建的打包件，与 `nsca-5th` 调用名冲突），
  其标签与 Release 一并删除。内容仍可在 git 历史（提交 `c973899`）中找回。