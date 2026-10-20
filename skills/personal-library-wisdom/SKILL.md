---
name: personal-library-wisdom
description: |
  个人书库（246 个文件、228 个蒸馏单元）的方法论知识库。当用户的问题涉及以下任一情形时调用：
  想用书库里某本书的方法；判断论证是否成立、识别谬误；判断一个主张可不可信、证据分级；解读梦、口误、重复出现的心理模式；分析关系模式、复盘争吵；人生选择与意义感、用哲学处理具体处境；分析社会现象、舆论、媒介与消费机制；分析热点案件、拆构成要件、查规范性文件合法性；成本收益分析、激励设计、博弈谈判；养成习惯、深度工作、刻意练习、结构化表达；用长时段视角看时事与战略；技术路线与工程判断；拍摄参数、用光与看图训练；查经典原文与引用纪律；中文写作训练与中国式处境分析；外国文学文本分析与叙事技法；从传记做决策复盘。
  结构：16 份主题簇综合（references/clusters/）＋ 228 张书卡（references/books/）＋ 全库索引（references/books-index.md）。查不到的书先查索引再说没有。
metadata:
  cangjie.generated-by: cangjie-skill v2.5 (RIA-TV++)
  cangjie.bundle-id: bundle.personal-library-wisdom
  cangjie.capability-count: 16
  cangjie.book-cards: 228
  sources: library:pT33yg2hCaAC1I8LU6ywTV/Library
---

# 个人书库思想武器库 — 全书能力入口

## 触发与不触发

**适用**：上面 description 列出的全部任务域；"我书库里有没有讲 X 的书"；"用《某书》的方法帮我做 Y"。
**不适用**：
- 提供受版权保护原文的长段摘录（引用仅限 ≤60 字、且只为说明方法）
- 作者人设角色扮演
- 书库之外书籍的完整方法论（可用通用知识回答，但须注明非本书库来源）
- 心理治疗、法律意见、医学诊断本身（见边界）

## 核心原则（常驻速览，概览类问题读到这里即可回答）

1. **先路由后加载**：任务先匹配主题簇（references/clusters/），需要具体方法时再加载书卡（references/books/），一次最多加载 2 份文档。
2. **结论可溯源**：任何方法必须标注来自《哪本书》，方法名与书卡里的叫法保持一致。
3. **诚实于抽样**：书卡由"章节结构 + 跨位置原文抽样"蒸馏而成；凡标注"须回原书核对 / 素材为节选"的内容，不得当作确证引用。
4. **文学是透镜不是证据**：小说提供分析视角与写作技法，情节细节只在分析任务中使用，不作事实依据。
5. **边界优先**：心理簇涉及自伤、暴力、成瘾、精神病性症状时必须建议专业帮助；法律簇产出不是法律意见；医学内容不替代医嘱。

## 能力路由（先读本表，按任务域加载 1 份簇文档）

| 任务域（用户会说的话） | 先读 | 规模 |
|---|---|---|
| 判断论证是否成立、识别谬误、批判性阅读 | references/clusters/logic.md | 10 本 |
| 判断主张可不可信、科学 vs 伪科学、证据分级 | references/clusters/sciphil.md | 3 本 |
| 解读梦/口误/重复模式、移情与阴影 | references/clusters/psychoanalysis.md | 11 本 |
| 关系模式分析、吵架复盘、该自助还是求助 | references/clusters/psychrel.md | 6 本 |
| 人生选择、意义感、自由与责任 | references/clusters/existential.md | 16 本 |
| 社会现象、舆论、媒介与消费机制 | references/clusters/social.md | 17 本 |
| 热点案件分析、构成要件、规范性文件 | references/clusters/law.md | 4 本 |
| 成本收益、激励设计、博弈与谈判 | references/clusters/econ.md | 6 本 |
| 习惯、深度工作、刻意练习、表达与沟通 | references/clusters/method.md | 15 本 |
| 用长时段看时事、战略判断、历史类比 | references/clusters/history.md | 12 本 |
| 技术路线、分层抽象、工程史视角 | references/clusters/tech.md | 6 本 |
| 拍摄参数、用光、看图训练 | references/clusters/photography.md | 4 本 |
| 查经典原文、诸子与经文引用纪律 | references/clusters/classics.md | 8 本 |
| 中文写作、中国式处境分析 | references/clusters/cnlit.md | 49 本 |
| 外国文学文本分析、叙事技法 | references/clusters/worldlit.md | 49 本 |
| 从传记做决策复盘 | references/clusters/biography.md | 12 本 |

**非能力类查询**：
- 查某本书、某位作者 → references/books-index.md（全库 228 单元索引，按簇分组）
- 只要知道某本书的一句话结论 → references/cheatsheet.md
- 按方法名查工具（如"反例情境法""七格拆要件"）→ references/glossary.md（720 个工具词条）
- 书库整体构成与使用说明 → references/overview.md

## 加载规则

- 每次任务先读本文件，再按路由表加载 1 份簇文档；簇文档内部会指向具体书卡（references/books/<编号>.md），任务明确需要时最多再加载 2 张书卡。
- 查书名/作者/一句话结论，不加载书卡，用索引与速查回答。
- 路由表和索引都无法命中的意图，明确告知超出书库范围，不要硬套。

## 边界与判停

- 用户问题与任何簇及书卡都无关时，说明超出范围后可用通用知识回答，并注明非本书库来源。
- 同一问题已加载 2 份文档仍无法回答时，停止并说明缺口。
- 发现引用与书卡冲突时，以书卡为准并向用户说明。
- 簇文档"薄弱与空白"一节列出的材料缺口（扫描件、节选、样章）不得被当成确证内容输出。
