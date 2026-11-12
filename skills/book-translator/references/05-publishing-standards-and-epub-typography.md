# 05 - 出版级电子书排版与 Apple Books 深度优化指南

一本合格的出版级电子书，不仅要求文字准确通顺，更必须在各类现代移动终端（Apple Books、Kindle、微信读书、多看阅读）上呈现出**赏心悦目、无缩放冲突、深色模式自适应且符合中华排版美学**的顶级视觉质感。

Apple Books 底层基于定制的 WebKit 渲染引擎，对现代 HTML5/CSS3 标准支持完备，但在流式分页（Reflowable）、夜间模式反转、字体内嵌与多栏排版上有严格的沙盒机制。

---

## 一、排版痼疾与西文转中文陷阱排除

### 1. 英文“小型大写字母（Small Caps）”引发的 `<small>` 标签灾难
* **问题起源**：
  在西文传统图书排版中，每个小节或章节开头的头几个单词（例如 `<small>AT NIGHT THE RABBITS</small>`）普遍使用大写字母配合 `<small>` 标签，以呈现传统西文印刷的“小型大写字母首字引导”效果。原版 CSS 普遍定义了 `small { font-size: 80%; }`。
* **中文灾难**：
  翻译为中文时，若机械保留该标签（如 `<small>夜幕降临，野兔</small>从灌木丛中钻了出来...`），会导致每节开头的前几个中文字变成 80% 的缩小字符，随后紧接 100% 正常字号。在电子书阅读器中极其突兀难看，严重损害阅读体验！
* **彻底根除方案**：
  1. **正文标签脱落**：彻底移除或解开包裹中文词句的 `<small>...</small>` 标签；
  2. **CSS 兜底防御**：在全书样式表中重置 small 规则：
     ```css
     small, .small-caps {
       font-size: 1em !important;
       font-weight: inherit !important;
       font-variant: normal !important;
     }
     ```

### 2. CSS 多类别段落字号忽大忽小与字族混乱
* 原版英文常常将访谈、引文、短信、对话（如 `.paras`, `.parash`, `.parasi`）设为 `0.85em; font-family: "Arial", sans-serif;`。
* 在中文阅读器中，0.85em 会使中文字符笔画细小难辨，且宋体与黑体频繁来回跳跃，视觉体验极其破碎。
* **规范重构**：正文、访谈、日记、引文段落一律统一为基准字号 `1em`。对话与引文应通过**左缩进（Blockquote 边距）与优美的楷体字族**进行典雅区分，坚决摒弃依靠缩减字号来区分引文的粗暴手段。

---

## 二、Apple Books (WebKit) 核心专有配置

### 1. 必备配置文件：`META-INF/com.apple.ibooks.display-options.xml`
Apple Books 默认会强制接管并覆盖所有内嵌字体。必须在 EPUB 的 `META-INF/` 目录下放置此文件，以解除系统锁定：

```xml
<?xml version="1.0" encoding="UTF-8"?>
<display_options>
  <platform name="*">
    <!-- 允许自定义字体与字体栈生效，防止被系统预设强行覆盖 -->
    <option name="specified-fonts">true</option>
    <!-- 固定版式或横屏双页策略开启 -->
    <option name="open-to-spread">true</option>
  </platform>
</display_options>
```

---

## 三、中文标准版式与中西文混排规范

### 1. 原生中文字体栈与防伪斜体变形
* **系统级回退字体栈**：
  优先采用 Apple 与主流系统内置的顶级阅读级衬线字体：
  ```css
  font-family: -apple-system, "PingFang SC", "Songti SC", "Source Han Serif SC", "STSong", serif;
  ```
* **彻底根除 iOS 伪斜体锯齿（Faux Italics）**：
  西文传统习惯用斜体（*Italics*）表示强调、书名或内心独白；但中文方块字在历史上不存在原生斜体。在 iOS WebKit 引擎中强行使用 `<i>` 或 `font-style: italic`，系统会通过几何算法强行拉伸笔画，产生极其丑陋的锯齿与字形塌陷！
  **出版级解决方案**：将引文、书名、强调统一映射为雅致的**楷体（Kaiti SC / STKaiti）**并重置为正体字形：
  ```css
  i, em, cite, .quote {
    font-family: "Kaiti SC", "STKaiti", "KaiTi", "楷体", serif;
    font-style: normal;
  }
  ```

### 2. 标准中文缩进与两端对齐
* **首行缩进 2 字符**：
  必须使用 CSS `text-indent: 2em;`，**严禁在正文中使用两个全角空格（`  `）充当缩进**，否则在调整字号或转为语音朗读时会产生空白异常。
* **精准重置缩进**：
  章节首段、副标题后第一段、居中诗歌及引用块首行应显式重置缩进：
  ```css
  h1 + p, h2 + p, h3 + p, .chapter-title + p, blockquote p, .no-indent {
    text-indent: 0;
  }
  ```
* **避头尾与两端对齐**：
  ```css
  body, p {
    text-align: justify;
    text-justify: inter-ideograph;
    word-break: break-word;
    overflow-wrap: break-word;
    -webkit-hyphens: none;
    hyphens: none;
    line-height: 1.65;
  }
  ```

---

## 四、EPUB 3 原生弹出式注脚（Pop-up Footnotes）

在传统电子书中，点击脚注链接会跳转到遥远的附录页面，破坏阅读沉浸感。利用 EPUB 3 标准语义标注，可在 Apple Books 及现代阅读器中直接触发**原生浮层弹窗**：

```html
<!-- 正文引用位置：添加 epub:type="noteref" -->
<p>在情绪劳动理论中，表层扮演扮演着重要角色<a href="#fn1" epub:type="noteref" class="footnote-ref">1</a>。</p>

<!-- 章节尾部注释放置：aside 标签包裹并声明 epub:type="footnote" -->
<aside id="fn1" epub:type="footnote">
  <p>1. 参见霍克希尔德对表层扮演（surface acting）与深层扮演的分类。——译者注</p>
</aside>
```
*读者在 iPad 或 iPhone 上点击角标“1”，屏幕会优雅滑出一个半透明卡片显示注释，无需跳转且支持一键返回正文。*

---

## 五、深色模式（Dark Mode）与羊皮纸主题无缝自适应

Apple Books、微信读书与 Kindle 提供纯白、羊皮纸色（Sepia）、夜间黑等多种主题。排版最忌讳**“配色死锁”**：

### 1. 杜绝死锁硬编码
* 严禁在 `body` 或通用段落上写死 `color: #000000; background-color: #ffffff;`。
* 保持正文颜色继承透明通道：
  ```css
  body {
    color: inherit;
    background-color: transparent;
  }
  ```

### 2. 卡片与引用框适配
使用半透明通道（`rgba`）配合媒体查询：
```css
blockquote, .callout {
  background-color: rgba(0, 0, 0, 0.03);
  border-left: 3px solid #8e9ca8;
  color: inherit;
}

@media (prefers-color-scheme: dark) {
  blockquote, .callout {
    background-color: rgba(255, 255, 255, 0.06);
    border-left-color: #5c6b73;
  }
}
```

---

## 六、页面分割与避坑铁律

1. **防跨页裁切保护**：
   图表、代码块、引用卡片在跨页处断裂会破坏排版：
   ```css
   figure, table, pre, blockquote, .keep-together {
     break-inside: avoid;
     page-break-inside: avoid;
     -webkit-column-break-inside: avoid;
   }
   ```
2. **章节强制分页**：
   ```css
   h1, .chapter-title {
     break-before: page;
     -webkit-break-before: page;
     page-break-before: always;
   }
   ```
3. **孤行与寡行控制**：
   ```css
   p {
     orphans: 2;
     widows: 2;
   }
   ```
4. **排版三大禁忌**：
   - **禁忌一：全书全局使用 Flexbox / Grid 布局**。流式分页跨页裁切时，外层包裹 `display: flex` 会导致 WebKit 分页计算死循环或末尾文本丢失；
   - **禁忌二：使用负边距（Negative Margin）**。如 `margin-left: -20px` 极易撑破视口导致空白跨页；
   - **禁忌三：固定图片像素宽度**。必须统一声明 `max-width: 100%; height: auto;`。
