# CHANGELOG · nsca-5th-deepseek

版本标签命名规则：`nsca-5th-deepseek-v<semver>`，见仓库根 README「版本与 Release 规范」。

## v1.0.0 — 2026-10-20

- 内容：8 个打包 Skill —— 1 个源路由 `nsca-5th/`（133 张能力卡）＋ 7 个可独立安装的子 Skill
  （抗阻计划、周期化、测试与评估、超等长、速度与灵敏、有氧耐力、过度训练与恢复）。
- 构建物料：`BUILD_MANIFEST.json`（逐文件 sha256）、`PIPELINE_STATE.md`、`DIGEST.md`、
  `coverage-audit.md`、`test-results.md`、`verified.md`、`needs-review.md`、`capability-destinations.json`。
- 来源：*Essentials of Strength Training and Conditioning*, 5th Edition（26 章 / 1876 页 / 约 40 万字）。
- 上游：[仓颉 cangjie-skill](https://github.com/kangarooking/cangjie-skill) v2.5.0，构建自
  `3adf9e61eec96edf34055432942f2952cfd7cfd9`（MIT）——依据是该包自带的 `BUILD_INFO.json` / `BUILD_MANIFEST.json`。
- 命名：原始构建名 `nsca-vi`，已重命名为 `nsca-5th`（包内自述）；入库目录改为 `nsca-5th-deepseek` 以与现有
  `skills/nsca-5th/` 区分。**两个目录的 `SKILL.md` frontmatter `name` 都是 `nsca-5th`，同一 Agent 只能装一个。**
- 许可：PolyForm Noncommercial 1.0.0；教材正文与图表版权仍归 Human Kinetics 与原作者。
- 首次入库：压缩包解出后剔除 `__MACOSX` 元数据，其余文件逐字节保留，未改动 `SKILL.md` 与能力卡。
