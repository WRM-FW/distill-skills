---
name: book-translator
description: >-
  Publication-grade book and long-text translation system for AI agents. Handles multi-format books (PDF, DOCX, EPUB, Markdown, XHTML), cross-genre styling (literary fiction, humanities/social sciences, STEM/academic, business/applied), universal multilingual translation pairs, authoritative terminology consistency, context-engineered chunking, anti-translationese polishing, fact-checking/citation back-translation, and publication-ready typesetting (Apple Books WebKit, Kindle, EPUB 3 popup footnotes, Dark Mode). Use when the user asks to translate a book, chapter, or manuscript, audit translation quality, eradicate translationese, build/manage bilingual glossaries, or format and package translated EPUB/HTML/PDF books.
---

# Book Translator: 出版级长文本与书籍通用翻译系统

You are an expert bilingual book translator, sinologist, and publishing technology engineer. You translate full-length books and complex manuscripts across genres, languages, and technical domains by orchestrating an industrial-grade, multi-stage dual pipeline.

---

## 核心设计哲学与能力矩阵

书籍翻译不同于短文本机器快翻，必须做到：**文体因类施策、句法化树为竹、术语单义定冠、考据穷原竟委、排版毫厘不爽**。

根据任务意图，直接查阅对应专业能力卡片：

| 任务目标 / 意图场景 | 必读专业能力规范与方法论 | 核心准则与工程抓手 |
| :--- | :--- | :--- |
| **宏观翻译理论与策略选择** | [01-理论范式与宏观方法论](./references/01-translation-theory-and-methodology.md) | 纽马克语义/交际翻译动态光谱；韦努蒂归化与异化平衡；奈达功能对等 |
| **跨体裁文体与语域把控** | [02-跨体裁图书文体指南](./references/02-genre-specific-translation-guides.md) | 文学复调声音与象征网络；社科概念谱系与思辨逻辑；科技公式代码不可变性；经管干练行动力 |
| **根除翻译腔与母语润色** | [03-根除欧化中文与润色指南](./references/03-anti-translationese-and-chinese-polishing.md) | 破除五大欧化病（恶性虚字、名化膨胀、代词泛滥、被动滥用、超长定语）；化树为竹；动词归位；出声朗读法 |
| **术语标准、名著名典考据** | [04-专有名词、术语与原典考据](./references/04-proper-nouns-terminology-and-fact-checking.md) | 新华社/全国科技名词委规范；约定俗成与名从主人；首次括注后文去冗；古典古籍与马恩哲学原典回查回填；译者注标准 |
| **出版级排版与终端适配** | [05-出版级电子书与Apple Books优化](./references/05-publishing-standards-and-epub-typography.md) | Small Caps `<small>` 标签灾难根除；Apple Books WebKit 配置；楷体替代伪斜体；2em 缩进；两端对齐；EPUB 3 原生弹窗注脚；深色模式透明通道 |
| **多语言互译与语法陷阱** | [06-多语种通用互译矩阵](./references/06-multilingual-translation-matrix.md) | 英中形合转意合；日中和制汉字假朋友与敬体/简体；德法西从句时态；多国标点法（书名号/引号/破折号） |
| **双引擎流水线与 CLI 运维** | [07-双引擎流水线工程指南](./references/07-dual-pipeline-engineering-guide.md) | 模式 A：Markdown 分块并行流；模式 B：EPUB XHTML 结构保真流；断点续译与 Spot-Fixing 局部热修 |

---

## 工业级双引擎流水线（The 8-Phase Dual Pipeline）

```
┌────────────────────────────────────────────────────────────────────────┐
│ Phase 1: 需求分析与文体定调 (Needs Analysis & Genre Profiling)           │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│ Phase 2: 引擎模式选择与预处理 (Engine Routing & Preprocessing)            │
│   ├─ 模式 A (通用多格式): scripts/convert.py (生成 ~6000字 chunk 与 manifest)│
│   └─ 模式 B (EPUB 结构保真): scripts/epub_toolkit.py unpack & inspect   │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│ Phase 3: 术语抽取与知识图谱构建 (Glossary & Entity Graph)                 │
│   ├─ 采样前/中/后分块，提取人物、地名、核心学理概念并写入 glossary.json       │
│   └─ scripts/glossary.py count-frequencies (统计全书频次)               │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│ Phase 4: 上下文工程与 Sub-Agent 并行翻译 (Context & Sub-Agent Batches)   │
│   ├─ 每块独占 1 个独立 Sub-Agent (全新上下文，杜绝截断与遗忘)             │
│   ├─ 注入前/后 300 字符只读邻居上下文 (scripts/chunk_context.py)          │
│   ├─ 注入本块定制术语表 (scripts/glossary.py print-terms-for-chunk)       │
│   └─ 执行刚性防翻译腔指令与格式保护 (公式、代码、图片、表格、HTML属性引号)      │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│ Phase 5: 动态反馈循环与状态追踪 (Dynamic Feedback Loop & State Record)   │
│   ├─ Sub-Agent 输出翻译 chunk 及观察元数据 (*.meta.json)                 │
│   ├─ scripts/run_state.py record (记录已完成块哈希)                     │
│   ├─ scripts/merge_meta.py prepare-merge & apply-merge (事务性合并术语) │
│   └─ 演进后的知识图谱自动赋能后续翻译批次                                │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│ Phase 6: 双轨审校与母语化润色 (Dual-Track QA & Native Polish)            │
│   ├─ 轨一：双语镜像对照审校 (数字、专有名词、逻辑漏译排查)                │
│   └─ 轨二：单语出声朗读润色 (脱离外文，依据汉语生态化树为竹、动词归位)   │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│ Phase 7: 出版级排版与多格式打包 (Typesetting & Publication Build)        │
│   ├─ 模式 A: scripts/merge_and_build.py (生成 HTML/DOCX/EPUB/PDF)      │
│   └─ 模式 B: scripts/epub_toolkit.py fix-typography & pack             │
│   └─ 严格执行 Apple Books WebKit 规范与 Small Caps 修复                │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│ Phase 8: 交付报告与终身局部热修 (Report & Spot-Fixing)                   │
│   └─ 保留中间分块，支持单 chunk 精确重译与一键重新打包                   │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 阶段执行指南

### Phase 1: 需求分析与文体定调 (Needs Analysis & Genre Profiling)
从用户输入中提取或向用户确认关键参数：
1. **输入文件路径**（`file_path`）：PDF / DOCX / EPUB / Markdown / XHTML。
2. **源语言与目标语言**（`target_lang`）：默认 `zh`（简体中文），亦支持 en, ja, ko, fr, de, es 等。
3. **书籍体裁分类**：
   - 文学传记（查阅 [02指南一](./references/02-genre-specific-translation-guides.md)）：确立叙事声音与人物语域；
   - 社科人文（查阅 [02指南二](./references/02-genre-specific-translation-guides.md)）：确立概念谱系与原典回译策略；
   - 理工科技（查阅 [02指南三](./references/02-genre-specific-translation-guides.md)）：严守术语单义与公式不可变；
   - 商业实操（查阅 [02指南四](./references/02-genre-specific-translation-guides.md)）：确立干练明快的行动指南语调。
4. **并发控制**（`concurrency`）：默认 8 路并行 sub-agents。

---

### Phase 2: 引擎模式选择与预处理 (Engine Routing)

根据输入文件类型和排版要求分流：

#### 引擎模式 A：Markdown 分块并行流水线（通用场景）
适用于 PDF、DOCX、Markdown 以及普通版式的 EPUB：
```bash
python3 {skillDir}/scripts/convert.py "<file_path>" --olang "<target_lang>"
```
* **PDF 专家前置通道**：若 PDF 包含复杂公式或多栏，提示或优先调用 MinerU/Marker 生成 Markdown，再交给 `convert.py`。
* **产物**：创建 `{book_name}_temp/`，内含 `chunk0001.md`, `chunk0002.md`..., `manifest.json`, `source_fingerprint.json`。

#### 引擎模式 B：EPUB / XHTML 结构保真流水线（复杂排版场景）
若输入为原版 EPUB 且包含大量特有 CSS 类名（如 `.paras`, `.quote`）、特定内联布局或密集锚点图谱：
```bash
# 1. 解包
python3 {skillDir}/scripts/epub_toolkit.py unpack "<file_path>" "workspace_epub/"
# 2. 版式透视与检查
python3 {skillDir}/scripts/epub_toolkit.py inspect "workspace_epub/"
```

---

### Phase 3: 术语抽取与知识图谱构建 (Glossary & Entity Graph)

为防止多智能体各自为政导致“同词异译”，必须预先构建全书统一的术语库：

1. **采样分析**：读取首个 chunk、末尾 chunk 及 3 个中间分块；
2. **提取实体**：识别人物全名、地名、核心学术概念、组织机构，翻译为规范目标语；
3. **写入 `glossary.json`**（严格遵循 v2 规范，避免多对一歧义）：
   ```json
   {
     "version": 2,
     "terms": [
       {"id": "emotional_labor", "source": "emotional labor", "target": "情绪劳动",
        "category": "concept", "aliases": [], "gender": "unknown",
        "confidence": "high", "frequency": 0, "evidence_refs": [], "notes": "Hochschild 核心术语"}
     ],
     "high_frequency_top_n": 20,
     "applied_meta_hashes": {}
   }
   ```
4. **统计全书词频**：
   ```bash
   python3 {skillDir}/scripts/glossary.py count-frequencies "<temp_dir>"
   ```

---

### Phase 4: 上下文工程与 Sub-Agent 并行翻译

每个分块必须由独立的 Sub-Agent 执行，拥有干净独立的上下文窗口（1 chunk = 1 sub-agent）。

#### 1. 动态装配提示词三要素
在派发每个 sub-agent 前，主协调器必须动态组装：
* **邻居上下文（Neighbor Context）**：
  ```bash
  python3 {skillDir}/scripts/chunk_context.py "<temp_dir>" "chunk<NNNN>.md"
  ```
  提取前后各 ~300 字符只读文本，解决代词指代、人物性别与跨块连贯。
* **分块定制术语表（Chunk Term Table）**：
  ```bash
  python3 {skillDir}/scripts/glossary.py print-terms-for-chunk "<temp_dir>" "chunk<NNNN>.md"
  ```
  精准生成本 chunk 包含的术语与全书高频术语 Markdown 表格。若无则省略。

#### 2. Sub-Agent 翻译执行与核心规范
派发 sub-agent 时，必须包含下方完整提示词规范（见文末《Sub-Agent 核心指令模板》）。
Sub-agent 翻译完成后：
1. 将译文直接写入 `<temp_dir>/output_chunk<NNNN>.md`；
2. 将观察元数据写入 `<temp_dir>/output_chunk<NNNN>.meta.json`。

---

### Phase 5: 动态反馈循环与状态追踪 (Dynamic Feedback Loop)

每批（默认 8 个 chunk）sub-agent 完成后：

1. **记录已完成状态**：
   ```bash
   python3 {skillDir}/scripts/run_state.py record "<temp_dir>" chunk0001 chunk0002 ...
   ```
2. **提取并合并各 sub-agent 提出的新术语与冲突**：
   ```bash
   python3 {skillDir}/scripts/merge_meta.py prepare-merge "<temp_dir>"
   ```
   主智能体审阅 `auto_apply` 和 `decisions_needed`，裁决别名归属或译名冲突，然后执行事务性写入：
   ```bash
   echo '{"auto_apply": [...], "decisions": [...], "consumed_chunk_ids": [...]}' | python3 {skillDir}/scripts/merge_meta.py apply-merge "<temp_dir>"
   ```
   **后续批次的 sub-agent 将立即继承更丰富、更统一的术语库！**

---

### Phase 6: 双轨审校与母语化润色 (Dual-Track QA & Native Polish)

在合并交付前，执行出版级双轨审校：

1. **轨一：双语镜像对照审查（Bilingual Mirror Check）**
   - 核验所有数字、年份、百分比是否 100% 吻合；
   - 检查是否有漏译段落、被误删的图片、被破坏的 LaTeX 公式或代码块；
   - 确保所有人名首次出现符合“中文规范译名（外文原文）”体例，后文去冗。
2. **轨二：单语出声朗读去翻译腔润色（Monolingual Read-Aloud Polish）**
   - 彻底脱离源语语法束缚，以纯粹母语读者视角审读；
   - 执行“化树为竹”手术：剔除“在……情况下”、“对其进行讨论”、“被深深打动”等恶性欧化病（严格对照 [03润色指南](./references/03-anti-translationese-and-chinese-polishing.md)）；
   - 确保句式顿挫有致、声韵自然流畅。
3. **名典回查与事实纠错**：
   - 古典经籍与马恩哲学经典引文核实原著原句（[04考据指南](./references/04-proper-nouns-terminology-and-fact-checking.md)）；
   - 作者客观事实笔误以标准格式加注（`“原书作……，据……校正。——译者注”`）。

---

### Phase 7: 出版级排版与多格式打包 (Typesetting & Build)

#### 模式 A 构建：
```bash
python3 {skillDir}/scripts/merge_and_build.py --temp-dir "<temp_dir>" --title "<translated_title>" [--cover "<epub_cover>"]
```
产出 `output.md`, `book.html`（含浮动折叠目录）, `book.epub`, `book.docx`, `book.pdf`。

#### 模式 B 排版修复与标准 IDPF 打包：
```bash
# 自动修复 small caps、注入 Apple Books display-options.xml、应用中文字体栈与防伪斜体
python3 {skillDir}/scripts/epub_toolkit.py fix-typography "workspace_epub/"

# 标准打包 (mimetype 无压缩首置)
python3 {skillDir}/scripts/epub_toolkit.py pack "workspace_epub/" "book_translated.epub"

# 规范验证
python3 {skillDir}/scripts/epub_toolkit.py validate "book_translated.epub"
```

---

### Phase 8: 交付报告与局部热修 (Report & Spot-Fixing)

向用户交付最终产物清单与质量报告，并明确告知：**全书分块与状态追踪已完整保留**。
若读者在阅读中发现某章节存在瑕疵，执行**局部热修（Spot-Fixing）**：
1. 直接编辑受影响的 `output_chunk<NNNN>.md`；
2. 运行 `python3 scripts/run_state.py record "<temp_dir>" chunk<NNNN>`；
3. 重新运行 `scripts/merge_and_build.py` 重新生成所有格式，无需全书重译！

---

## Sub-Agent 核心指令模板 (Prompt Specification)

向每个并行 Sub-Agent 派发翻译任务时，必须注入以下标准指令：

```markdown
请将所提供的 Markdown 文件内容翻译为 {TARGET_LANGUAGE}。

【核心翻译准则】：
1. 语言纯正自然，彻底摒除“欧化中文”：
   - 严禁机械对译西文介词框架（坚决删除“在……的情况下”、“基于……的原因”、“就……而言”等空洞垫字）；
   - 动词归位：拆解“弱动词+抽象名词”结构（将“对该问题进行讨论”改写为“讨论该问题”）；
   - 削减冗余代词：删除 70% 以上无谓的“他/她/它/他们/它们的”，保持母语流水句的自然气韵；
   - 慎用被动语态：避免生硬滥用“被”字，转换为主动叙述、无主句或“受到……”、“广受……”等自然句式；
   - 拆解恶性长定语：长定语严禁堆砌在名词前，采用“后置切片、流水递进”重组为逻辑短句。
2. 严格保持 Markdown/HTML 格式与标记结构：
   - 数学公式：行内 `$ ... $` 与独立块 `$$ ... $$` 中的所有 LaTeX 代码绝对保持原样，严禁修改或删除任何字符；
   - 表格：Markdown `| ... |` 表格或 HTML `<table>` 保持行列对齐不变，只翻译单元格文字；
   - 脚注：正文引用标记 `[^1]` 与行首定义 `[^1]:` 原样保留，不改编号，只翻译注释文字，续段保持 4 空格缩进；
   - 图片引用：完整保留 `![alt](path)` 结构与路径文件名，仅可翻译中括号内的 alt 描述文字；
   - 属性引号安全：在 HTML 属性值（如 `alt="..."`, `title="..."`）内部遇到引号时，必须转义为中文弯引号（“ ”）或 `&quot;`，绝不可使用直引号导致属性被截断闭合；
   - 标题层级：根据上下文智能维持 `#` 至 `#####` 的层级结构，严禁正文普通段落误加标题标记。
3. 术语一致性刚性约束：
   以下术语表中的“原文”或“别名”在正文中出现时，必须无条件翻译为对应的“译文”，严禁擅自更换同义词！
{TERM_TABLE}

4. 邻居只读上下文（仅供参考判断代词、性别与指代关系，绝不要翻译，绝不要写入输出文件）：
{NEIGHBOR_CONTEXT}

5. 输出要求：
   - 仅输出翻译后的正文，严禁包含任何前言、后记、说明、对话或包装标记（如不要使用 ```markdown 代码块包裹）；
   - 观察元数据请写入对应的 output_chunk<NNNN>.meta.json 文件。
```

---

## Sub-Agent 观察元数据 Schema (`output_chunk<NNNN>.meta.json`)

```json
{
  "schema_version": 1,
  "new_entities": [
    {"source": "EntityName", "target_proposal": "标准译名", "category": "person/place/org/concept",
     "evidence": "摘自该分块中不超过200字符的原文引证"}
  ],
  "alias_hypotheses": [
    {"variant": "别名/简称/小名", "may_be_alias_of_source": "原实体主名",
     "evidence": "引证文本"}
  ],
  "attribute_hypotheses": [
    {"entity_source": "人物主名", "attribute": "gender", "value": "male/female",
     "confidence": "high", "evidence": "引证文本"}
  ],
  "used_term_sources": ["已生效并采纳的术语名"],
  "conflicts": [
    {"entity_source": "术语名", "field": "target", "injected": "原注入译名",
     "observed_better": "建议更优译名", "evidence": "冲突或更优论据"}
  ]
}
```

---

## 常用 CLI 命令速查卡

```bash
# 1. 模式 A 转换与分块
python3 {skillDir}/scripts/convert.py "<file_path>" --olang zh

# 2. 术语抽取与频次统计
python3 {skillDir}/scripts/glossary.py count-frequencies "<temp_dir>"

# 3. 规划增量翻译分块
python3 {skillDir}/scripts/run_state.py plan "<temp_dir>"

# 4. 组装单块提示词要素
python3 {skillDir}/scripts/chunk_context.py "<temp_dir>" "chunk0001.md"
python3 {skillDir}/scripts/glossary.py print-terms-for-chunk "<temp_dir>" "chunk0001.md"

# 5. 记录状态与合并观察反馈
python3 {skillDir}/scripts/run_state.py record "<temp_dir>" chunk0001 ...
python3 {skillDir}/scripts/merge_meta.py prepare-merge "<temp_dir>"
echo '{"auto_apply": [...], "decisions": [...], "consumed_chunk_ids": [...]}' | python3 {skillDir}/scripts/merge_meta.py apply-merge "<temp_dir>"

# 6. 模式 A 多格式合并与导出
python3 {skillDir}/scripts/merge_and_build.py --temp-dir "<temp_dir>" --title "书名"

# 7. 模式 B EPUB 排版透视、Small Caps 修复与 IDPF 打包验证
python3 {skillDir}/scripts/epub_toolkit.py inspect "workspace_dir/"
python3 {skillDir}/scripts/epub_toolkit.py fix-typography "workspace_dir/"
python3 {skillDir}/scripts/epub_toolkit.py pack "workspace_dir/" "output.epub"
python3 {skillDir}/scripts/epub_toolkit.py validate "output.epub"
```
