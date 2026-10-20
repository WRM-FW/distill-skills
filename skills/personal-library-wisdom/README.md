# personal-library-wisdom

> **✨Masterpiece** —— 仓库的核心代表作之一，入选依据见[仓库根 README](../../README.md#masterpiece)。

上游 Skill：[仓颉 cangjie-skill](https://github.com/kangarooking/cangjie-skill) v2.5.0（`RIA-TV++` 流水线，MIT）　｜　许可：[PolyForm Noncommercial 1.0.0](LICENSE)　｜　版本：`v1.0.0`（标签 `personal-library-wisdom-v1.0.0`）　｜　版本记录：[CHANGELOG.md](CHANGELOG.md)

个人书库的方法论索引：把 Google Drive「Library」里的 228 个蒸馏单元整理成 16 个主题簇，
再让 Agent 按问题类型先加载簇、再按需加载单张书卡。它的定位不是「读完 228 本书」，
而是**先确认书库里有没有讲这件事的书，再调用那本书的方法**。

## 能做什么

`SKILL.md` 是唯一入口，先读路由表选 1 份主题簇，再由簇文档指向具体书卡（任务需要时最多再加载 2 张）。

| 任务域 | 簇文档 | 收录书数 |
| --- | --- | --- |
| 论证是否成立、识别谬误、批判性阅读 | `references/clusters/logic.md` | 10 |
| 主张可不可信、科学 vs 伪科学、证据分级 | `references/clusters/sciphil.md` | 3 |
| 梦/口误/重复模式、移情与阴影 | `references/clusters/psychoanalysis.md` | 11 |
| 关系模式、争吵复盘、自助还是求助 | `references/clusters/psychrel.md` | 6 |
| 人生选择、意义感、自由与责任 | `references/clusters/existential.md` | 16 |
| 社会现象、舆论、媒介与消费机制 | `references/clusters/social.md` | 17 |
| 热点案件、构成要件、规范性文件 | `references/clusters/law.md` | 4 |
| 成本收益、激励设计、博弈与谈判 | `references/clusters/econ.md` | 6 |
| 习惯、深度工作、刻意练习、表达与沟通 | `references/clusters/method.md` | 15 |
| 长时段看时事、战略判断、历史类比 | `references/clusters/history.md` | 12 |
| 技术路线、分层抽象、工程史 | `references/clusters/tech.md` | 6 |
| 拍摄参数、用光、看图训练 | `references/clusters/photography.md` | 4 |
| 查经典原文、引用纪律 | `references/clusters/classics.md` | 8 |
| 中文写作、中国式处境分析 | `references/clusters/cnlit.md` | 49 |
| 外国文学文本分析、叙事技法 | `references/clusters/worldlit.md` | 49 |
| 从传记做决策复盘 | `references/clusters/biography.md` | 12 |

非能力类查询走四个入口：`references/books-index.md`（228 单元全库索引，按簇分组）、
`references/cheatsheet.md`（一本书一句话结论）、`references/glossary.md`（720 个工具词条，按方法名查）、
`references/overview.md`（书库整体构成）。

## 目录结构

```text
personal-library-wisdom/
├── SKILL.md                     # 主路由：触发边界 + 5 条核心原则 + 16 簇路由表 + 加载规则
├── README.md                    # 本文件
├── CHANGELOG.md                 # 版本记录
├── LICENSE                      # PolyForm Noncommercial 1.0.0
└── references/
    ├── clusters/                # 16 份主题簇综合（方法论 + 跨书对比 + 薄弱与空白）
    ├── books/                   # 228 张书卡（NNN.md，章节结构 + 跨位置原文抽样）
    ├── books-index.md           # 全库索引
    ├── cheatsheet.md            # 一句话结论速查
    ├── glossary.md              # 720 个工具词条
    └── overview.md              # 书库构成与使用说明
```

目录命名与仓库其他 Skill 不同：这里用 `clusters/` + `books/`，而不是 `capabilities/`，
因为它是 v2.5 的「书卡库」型产物，不是「能力卡」型。原样保留，未做重命名。

## 安装与调用

```bash
git clone --depth 1 https://github.com/WRM-FW/distill-skills.git
cp -r distill-skills/skills/personal-library-wisdom <你的 Agent Skill 目录>/
```

整个目录（含 `references/`）都要拷过去；只拷 `SKILL.md` 会丢掉 16 个簇与 228 张书卡。

常用说法：「我书库里有没有讲 X 的书」「用《某书》的方法帮我做 Y」「这段论证成不成立」。
一次任务最多加载 2 份文档，簇和索引都命中不了时它会明说超出书库范围，不硬套。

## 边界

- 不做受版权保护原文的长段摘录：引用上限 60 字，且只为说明方法。
- 不做作者人设角色扮演。
- 书卡由「章节结构 + 跨位置原文抽样」蒸馏，标注「须回原书核对 / 素材为节选」的内容不能当确证引用。
- 心理簇碰自伤、暴力、成瘾、精神病性症状时必须建议专业帮助；法律簇产出不是法律意见；医学内容不替代医嘱。
- 许可证覆盖本目录的原创表达，不覆盖书库原著的文字与图表。

---

> 本 Skill 由 [distill-skills](https://github.com/WRM-FW/distill-skills) 仓库统一收录维护，全部 Skill 索引见[仓库根 README](../../README.md)。
