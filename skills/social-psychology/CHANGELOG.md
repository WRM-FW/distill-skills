# CHANGELOG · social-psychology

版本标签命名规则：`social-psychology-v<semver>`，见仓库根 README「维护规范」。

## v1.0.1 — 2026-11-12

- 修复 `SKILL.md` frontmatter：`description` 从单行 plain scalar 改为折叠块 `>-`。
  原文中「social relations: auditing …」的冒号加空格会被 YAML 当作键值分隔符，
  导致整个 frontmatter 解析失败、Skill 加载报错（PyYAML: mapping values are not allowed here）。
- 文本内容未改：折叠后仍是同一段 953 字符的英文描述，仅换行位置不同。
- 校验：全仓 10 个 `SKILL.md` 的 frontmatter 现均可被 PyYAML 正常解析。

## v1.0.0 — 2026-10-15

- 结构：`SKILL.md` 主路由 + `references/book/{overview,glossary}.md` + 12 张 RIA++ 六段式能力卡。
- 来源：迈尔斯《社会心理学》第 11 版（4 编 16 章）。
- 上游：[仓颉 cangjie-skill](https://github.com/kangarooking/cangjie-skill)（`RIA-TV++` 流水线，MIT）——依据是本 Skill 的六段能力卡与阶段命名和该上游 README 一致，无一手声明。
- 许可：PolyForm Noncommercial 1.0.0；原著文字与图表版权仍归原出版社与作者。
- 本条目为迁入本仓库时的初始版本（2026-10-15）；此前的蒸馏过程未在此仓库留存历史。

