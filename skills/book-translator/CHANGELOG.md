# CHANGELOG · book-translator

版本标签命名规则：`book-translator-v<semver>`，见仓库根 README「维护规范」。

## v1.0.0 — 2026-11-12

- 内容：`SKILL.md` 主路由（344 行）+ 7 份方法规范（翻译理论、体裁指南、去翻译腔、术语考据、出版排版、多语种矩阵、流水线运维）
  + 9 个 Python 脚本 + EPUB 模板与样式。
- 能力：双引擎流水线（Markdown 分块并行 / EPUB XHTML 结构保真）、术语表事务性合并、断点续传与单块热修、
  EPUB 3 弹窗注脚与 Apple Books 深色模式适配。
- 上游：无。原创手写 Skill，不是 cangjie / distilly 管线的产物。
- 许可：PolyForm Noncommercial 1.0.0。
- 首次入库：剔除 `scripts/__pycache__/` 后原样收录，未改动 `SKILL.md`、references 与脚本。
