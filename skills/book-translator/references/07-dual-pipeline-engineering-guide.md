# 07 - 双引擎流水线工程指南与 CLI 运维手册

书籍翻译作为庞大的工业级长文本项目，单一的转换管道难以应对所有类型的书籍出版物。本 Skill 创新性地提供**“双引擎流水线”（Dual-Engine Architecture）**：

```
                      ┌─────────────────────────────────┐
                      │    书籍输入文件 (Source Book)    │
                      └───────────────┬─────────────────┘
                                      │
            ┌─────────────────────────┴─────────────────────────┐
            ▼                                                   ▼
【引擎模式 A：Markdown 分块流】                     【引擎模式 B：XHTML 结构保真流】
(Markdown-Chunk Pipeline)                       (Direct EPUB / XHTML DOM Pipeline)
- 适用：PDF、DOCX、Markdown、标准 EPUB           - 适用：原版具有极其复杂精美排版、内联样式、
- 优势：支持超长书籍并发翻译、跨格式输出          微观类名、锚点网络的商业出版级 EPUB
- 产物：HTML / DOCX / EPUB / PDF                - 优势：100% 字节级保留原始 HTML 结构与标签
```

---

## 一、引擎模式 A：Markdown 分块并行流水线

### 1. 全流程架构图
```
源文件 ──► scripts/convert.py ──► chunk0001.md, chunk0002.md... (manifest.json)
              │
              ├──► scripts/glossary.py (提取术语表 v2 + 统计全书频次)
              │
              ├──► 循环批次执行 (Batch 1..N):
              │     ├── scripts/chunk_context.py (提取前后相邻 300 字符只读上下文)
              │     ├── scripts/glossary.py print-terms-for-chunk (提取当前块精准术语表)
              │     ├── 启动并行 Sub-Agent 翻译当前批次各 chunk (写入 output_chunk*.md)
              │     ├── Sub-Agent 输出元数据反馈 (output_chunk*.meta.json)
              │     ├── scripts/run_state.py record (记录已完成块状态)
              │     ├── scripts/merge_meta.py prepare-merge (分析新实体与冲突)
              │     └── scripts/merge_meta.py apply-merge (事务性合并入术语库)
              │
              └──► scripts/merge_and_build.py ──► output.md / book.html / book.epub / docx / pdf
```

### 2. 核心 CLI 工具命令详解

#### ① 预处理与分块：`scripts/convert.py`
```bash
python3 scripts/convert.py "<file_path>" --olang "<target_lang>"
```
* **参数选项**：
  - `--olang zh`：目标语言代码（默认 `zh`，支持 en, ja, ko, fr, de, es 等）；
  - `--chunk-size 6000`：目标分块字符数（默认 6000 字符，兼顾上下文广度与 API 输出限制）；
  - `--temp-root "<dir>"`：指定工作临时目录的父路径；
  - `--strip-page-numbers`：强制剔除独立页码行（PDF 自动启用，EPUB 默认保留）；
  - `--detect-page-numbers`：对 EPUB/DOCX 也检测并剔除页码文本。
* **PDF 专家建议**：
  若 PDF 包含复杂多栏、密集数学公式或精美表格，Calibre 坐标重排会损坏结构。此时**强烈建议先用 MinerU 或 Marker 转换为 Markdown**，再将 Markdown 输入给 `convert.py`！

#### ② 术语表提取与频次统计：`scripts/glossary.py`
* **统计频次**：
  ```bash
  python3 scripts/glossary.py count-frequencies "<temp_dir>"
  ```
  自动扫描所有 `chunk*.md`，统计每个已识别实体在全书出现的频次，排序并写入 `glossary.json`。
* **为单个 chunk 生成定制术语表**：
  ```bash
  python3 scripts/glossary.py print-terms-for-chunk "<temp_dir>" "chunk0001.md"
  ```
  生成三列 Markdown 术语表（`原文 | 别名 | 译文`），仅包含本 chunk 实际出现的术语以及全书前 N 个最高频术语，动态注入 sub-agent 提示词中。

#### ③ 邻居上下文抽取：`scripts/chunk_context.py`
```bash
python3 scripts/chunk_context.py "<temp_dir>" "chunk0001.md"
```
提取上一分块末尾 ~300 字符与下一分块开头 ~300 字符的只读文本，用于 sub-agent 在翻译时准确消歧代词（he/she/it）、性别与跨章节实体。

#### ④ 状态规划与增量断点续译：`scripts/run_state.py`
* **规划需翻译队列**：
  ```bash
  python3 scripts/run_state.py plan "<temp_dir>"
  ```
  对比源文件 SHA-256、术语表 Hash 与历史翻译记录，输出真正需要翻译的 chunk 列表。
* **记录已完成状态**：
  ```bash
  python3 scripts/run_state.py record "<temp_dir>" chunk0001 chunk0002 ...
  ```

#### ⑤ 跨批次观察与术语动态演进：`scripts/merge_meta.py`
Sub-agent 在翻译各 chunk 时，会发现新实体、新人物别名或发现前文术语译法存在缺陷，并写入 `output_chunk*.meta.json`。
* **准备合并**：
  ```bash
  python3 scripts/merge_meta.py prepare-merge "<temp_dir>"
  ```
  输出待决策的实体列表（冲突解决、新别名认领）。
* **事务性应用更新**：
  ```bash
  echo '{"auto_apply": [...], "decisions": [...], "consumed_chunk_ids": [...]}' | python3 scripts/merge_meta.py apply-merge "<temp_dir>"
  ```
  让后序批次的 sub-agent 自动享受到前序批次积累的丰富术语成果！

#### ⑥ 合并与多格式构建：`scripts/merge_and_build.py`
```bash
python3 scripts/merge_and_build.py --temp-dir "<temp_dir>" --title "<translated_title>" [--cover "<cover_image>"]
```
自动完成分块缝合、浮动目录构建、Pandoc/Calibre 格式转换，并在 `{book_name}_temp/` 下生成全部成果。

---

## 二、引擎模式 B：EPUB / XHTML 结构保真流水线

当遇到设计精湛的原版 EPUB（包含复杂对话缩进、手写体信件、特定 class 布局、数百条角标链接，如《The Managed Heart》或人物传记）时，若将其强行扁平化转为普通 Markdown，会导致大量版式元数据丢失。此时应采用模式 B：

### 1. 核心流程
```
1. 解包 EPUB ──► scripts/epub_toolkit.py unpack <book.epub> <workspace_dir>
2. 版式透视 ──► scripts/epub_toolkit.py inspect <workspace_dir>
3. 结构化并发转译 ──► 逐段保留所有 <p class="...">, <a>, <sup> 标签，1:1 精准转译
4. 版式优化与排版修复 ──► scripts/epub_toolkit.py fix-typography <workspace_dir>
5. 标准 IDPF 打包 ──► scripts/epub_toolkit.py pack <workspace_dir> <output.epub>
6. 严格规范验证 ──► scripts/epub_toolkit.py validate <output.epub>
```

### 2. `epub_toolkit.py` 工具命令详解

* **解包 EPUB**：
  ```bash
  python3 scripts/epub_toolkit.py unpack "book.epub" "extracted_dir"
  ```
* **排版漏洞深度透视**：
  ```bash
  python3 scripts/epub_toolkit.py inspect "extracted_dir"
  ```
  自动扫描全书 XHTML 文件，定位所有的 `<small>` 标签、统计 CSS class 频率、统计角标脚注数量，排查 Apple Books 配置缺失。
* **自动化排版升级与 Small Caps 修复**：
  ```bash
  python3 scripts/epub_toolkit.py fix-typography "extracted_dir"
  ```
  一键完成：
  1. 解开/清除正文中导致字号缩小的 `<small>` 标签；
  2. 自动注入 `META-INF/com.apple.ibooks.display-options.xml`；
  3. 注入防伪斜体、标准 2em 首行缩进、楷体引文、两端对齐与深色模式自适应样式。
* **标准 IDPF EPUB 打包**：
  ```bash
  python3 scripts/epub_toolkit.py pack "extracted_dir" "output_translated.epub"
  ```
  严格保证首文件为无压缩 `mimetype`，次文件为 `META-INF/container.xml`，其余文件标准压缩，杜绝任何阅读器解析错误。
* **合规性验证**：
  ```bash
  python3 scripts/epub_toolkit.py validate "output_translated.epub"
  ```
  毫秒级校验 mimetype、container、OPF 以及所有 XHTML 文档的语法完整性。

---

## 三、故障排查、断点续传与局部修改（Spot Fixing）

在长达数十万字的书籍翻译过程中，随时可能遇到单点错误或网络中断。双引擎流水线具备极强的自愈与局部修补能力：

### 1. 局部修改单个段落或 chunk
如果在全书生成后，用户发现第 15 块（chunk0015）中某个概念需要修正：
* **严禁行为**：严禁直接在 `output.md` 中手动修改！因为重新构建时，`output.md` 会被各 chunk 重新覆盖。
* **正确做法**：
  1. 直接编辑 `<temp_dir>/output_chunk0015.md`；
  2. 运行 `python3 scripts/run_state.py record "<temp_dir>" chunk0015`；
  3. 重新运行 `scripts/merge_and_build.py`，流水线自动检测到 chunk0015 更新，重新合并并重新打包所有格式！

### 2. 批次中断恢复（Resume on Interruption）
* 若在翻译第 50 块时中断，直接重新调用 Skill：
* `convert.py` 会通过 `source_fingerprint.json` 自动识别已有临时目录；
* `run_state.py plan` 会精准跳过已经完成且哈希匹配的 49 个块，只将未完成的块派发给 sub-agent，实现零浪费的秒级断点续传！
