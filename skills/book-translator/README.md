# Book Translator Skill (出版级长文本与书籍通用翻译系统)

> 本 Skill 由 [distill-skills](https://github.com/WRM-FW/distill-skills) 收录，位于 `skills/book-translator/`；仓库索引见[根 README](../../README.md)。
>
> 上游 Skill：无（原创手写 Skill，不经过 cangjie / distilly 等蒸馏管线）　｜　许可：[PolyForm Noncommercial 1.0.0](LICENSE)　｜　版本：`book-translator-v1.0.0`　｜　版本记录：[CHANGELOG.md](CHANGELOG.md)

面向 Antigravity、Claude Code、Codex 等智能体生态的高质量、出版级通用图书与长文本翻译 Skill。

---

## 🌟 核心目标与特性

本 Skill 旨在解决通用 AI 翻译书籍时的三大核心顽疾：
1. **翻译腔泛滥（欧化中文）**：机械直译西文树状语法（虚字化、名词膨胀、代词泛滥、被动语态滥用、超长定语），导致文字生硬干瘪；
2. **长篇术语漂移与幻觉**：数十万字长书中，不同章节由不同上下文翻译，造成专有名词、核心术语同词异译，甚至古典名著名句被二次错译；
3. **排版崩坏与阅读器兼容性差**：西文 Small Caps 导致中文开头忽小忽大（`<small>` 灾难）、iOS 渲染引擎伪斜体锯齿、Apple Books 强制覆盖自定义字体、深色模式配色死锁、脚注无法弹窗跳转等。

### 核心亮点：
- 🏗️ **双引擎流水线架构（Dual-Engine Pipeline）**：
  - **模式 A（Markdown 分块流）**：输入 PDF/DOCX/EPUB/Markdown 自动切分为 ~6000 字符分块，由独立 Sub-Agent 并行转译，支持多格式（HTML/DOCX/EPUB/PDF）统一导出；
  - **模式 B（EPUB/XHTML 结构保真流）**：解包 EPUB，逐段 100% 保持原始 XHTML 标签、CSS 类名与微观样式，毫秒级扫描与修复排版缺陷，IDPF 标准打包。
- 📚 **跨体裁专业指南（Cross-Genre Mastery）**：
  - 文学虚构与传记：复调声音、人物语域刻画、象征网络全书统一；
  - 社科人文思想：哲学概念谱系、严密因果逻辑、古典经籍与马恩哲学经典文献原典回查回填（严禁二次转译）；
  - 科技理工学术：术语绝对单义性、LaTeX 数学公式与代码块 100% 免疫保护、国家计量单位规范；
  - 商业实用指南：节奏明快干练、行动指导力强。
- 🔬 **动态知识图谱与事务性术语自进化（Dynamic Glossary & State）**：
  - v2 术语表规范与频次自动统计；
  - 前后相邻 300 字符只读上下文动态注入（代词与实体消歧）；
  - Sub-Agent 观察元数据跨批次事务性合并，术语库随翻译进度越战越强；
  - `run_state.json` 追踪分块 SHA-256，支持秒级断点续传与单块局部热修（Spot-Fixing）。
- 📱 **出版级排版与 Apple Books 深度优化**：
  - 彻底铲除 `<small>` 标签引起的小字号突兀 Bug；
  - 自动注入 `META-INF/com.apple.ibooks.display-options.xml` 解除字体锁定；
  - 原生中文阅读级衬线字体栈；
  - 楷体映射防 iOS 伪斜体变形；
  - 2em 标准首行缩进与中西文避头尾两端对齐；
  - EPUB 3 原生浮层弹窗注脚（Pop-up Footnotes）；
  - 深色/羊皮纸/浅色主题全自适应透明通道。

---

## 📂 目录结构

```
book-translator/
├── SKILL.md                  # 主技能指令与工作流编排（YAML frontmatter）
├── README.md                 # 完整系统介绍与使用手册
├── scripts/                  # 工业级自动化 Python 工具链
│   ├── convert.py            # 多格式转 Markdown 分块 (~6000字) 与指纹追踪
│   ├── chunk_context.py      # 上下文滑动窗口提取 (~300字邻居只读上下文)
│   ├── glossary.py           # v2 术语库抽取、词频统计与定制分块术语表生成
│   ├── run_state.py          # 增量断点续译与状态规划
│   ├── merge_meta.py         # 跨批次观察元数据事务性合并与实体冲突裁决
│   ├── merge_and_build.py    # 缝合分块、构建浮动目录与多格式 Calibre/Pandoc 打包
│   ├── calibre_html_publish.py# HTML 发布与目录生成
│   ├── manifest.py           # 分块哈希与完整性校验
│   ├── meta.py               # 观察元数据结构处理
│   ├── epub_toolkit.py       # 纯 Python 零依赖 EPUB 深度解包/扫描/修复/打包/验证工具
│   ├── template.html         # 响应式网页版阅读器模板（含浮动折叠目录）
│   └── template_ebook.html   # 电子书版专用 HTML 模板
├── templates/                # 标准出版级样式与配置文件
│   ├── book_epub_style.css   # 出版级母版 CSS（防伪斜体、2em缩进、暗黑模式适配）
│   └── com.apple.ibooks.display-options.xml # Apple Books 字体解锁与跨页配置
└── references/               # 深度专业方法论与规范卡片
    ├── 01-translation-theory-and-methodology.md       # 理论范式（纽马克/韦努蒂/奈达）
    ├── 02-genre-specific-translation-guides.md        # 四大体裁（文学/社科/科技/经管）指南
    ├── 03-anti-translationese-and-chinese-polishing.md # 五大欧化中文病根除与润色准则
    ├── 04-proper-nouns-terminology-and-fact-checking.md# 权威译名规范、名著考据与译者注
    ├── 05-publishing-standards-and-epub-typography.md  # 出版排版规范与 Apple Books 特性
    ├── 06-multilingual-translation-matrix.md           # 多语种（英/日/德/法/西）互译矩阵
    └── 07-dual-pipeline-engineering-guide.md           # 双引擎流水线与 CLI 运维手册
```

---

## 🚀 快速上手

### 模式 A：通用长篇书籍翻译（PDF / DOCX / EPUB / Markdown）

```bash
# 1. 转换与分块（输出在 <filename>_temp/ 下）
python3 scripts/convert.py "path/to/book.epub" --olang zh

# 2. 统计术语频次
python3 scripts/glossary.py count-frequencies "book_temp/"

# 3. 规划待翻译队列（支持断点续传）
python3 scripts/run_state.py plan "book_temp/"

# 4. 生成单块提示词要素（在派发 sub-agent 前调用）
python3 scripts/chunk_context.py "book_temp/" "chunk0001.md"
python3 scripts/glossary.py print-terms-for-chunk "book_temp/" "chunk0001.md"

# 5. 批次完成后记录状态并合并观察元数据
python3 scripts/run_state.py record "book_temp/" chunk0001 chunk0002 ...
python3 scripts/merge_meta.py prepare-merge "book_temp/"
# 注入决策后合并 apply-merge

# 6. 合并多格式产出
python3 scripts/merge_and_build.py --temp-dir "book_temp/" --title "书名"
```

### 模式 B：EPUB 结构保真与排版深度优化

```bash
# 1. 解包
python3 scripts/epub_toolkit.py unpack "book.epub" "workspace_epub/"

# 2. 检查排版缺陷（定位 <small> 标签与 CSS 问题）
python3 scripts/epub_toolkit.py inspect "workspace_epub/"

# 3. 自动化排版升级（一键根除 Small Caps，注入 Apple Books 配置与中文字体栈）
python3 scripts/epub_toolkit.py fix-typography "workspace_epub/"

# 4. IDPF 标准无损打包
python3 scripts/epub_toolkit.py pack "workspace_epub/" "book_translated.epub"

# 5. 严格验证
python3 scripts/epub_toolkit.py validate "book_translated.epub"
```

---

> 本 Skill 由 [distill-skills](https://github.com/WRM-FW/distill-skills) 仓库统一收录维护，全部 Skill 索引见[仓库根 README](../../README.md)。
