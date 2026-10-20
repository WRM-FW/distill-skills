# PIPELINE_STATE — nsca-essentials-5e → nsca-5th

- **skill 目标名**: nsca-5th（宿主内标识 `nsca-5th`，因规范要求小写 kebab-case）
- **蒸馏引擎**: cangjie-skill 2.5.0（RIA-TV++ / ADR-002 Bundle 版）
- **source_id**: `src-nsca-essentials-5e`
- **源文件**: Essentials of Strength Training and Conditioning, 5th Edition（1876 页 PDF → 402,798 词正文）
- **输出模式**: **pack**（1 路由入口 + 7 晋级 Skill，共 8 个可发现入口 = 预算 8）

## 阶段进度

| 阶段 | 状态 | 产出 |
|---|---|---|
| 0 — Adler 整书理解 | ✅ | `BOOK_OVERVIEW.md`（含 T01–T40 原书关键任务清单） |
| 1 — 5 路并行提取 | ✅ | `candidates/*.md`，归并出 **1143 条**候选（framework 253 / principle 664 / case 97 / counter-example 129 / glossary 194 条术语） |
| 1.5 — 三重验证 | ✅ | 9 个能力簇 → **145 个能力单元**（verified 128 / reference 13 / needs_review 4 / rejected 0）；`verified.md` / `references.md` / `needs-review.md` / `coverage-audit.md` |
| 1.6 — 晋级门 | ✅ | `destinations.json`；7 个伞形能力晋级，其余 126 个保留为路由入口内的能力卡 |
| 2 — RIA++ 能力卡 | ✅ | **133 张能力卡**（全部六段齐全）+ Bundle `verified.yaml` |
| 3 — Zettelkasten 链接 | ✅ | 133 个能力全部有链接，**440 条关系**（依赖/对比/组合）；`GLOSSARY.md`（194 条） |
| 4 — 压力测试 | ✅（部分） | `test-prompts.json`（60 条，含诱饵与跨 Skill 混淆）+ `test-results.md`；触发精度 **100%（35/35）**、诱饵 **100%（17/17）**、边界用例 8 条已人工核查 |
| 5 — 编译交付 | ✅ | `DIGEST.md`（6,565 中文字）+ `dist/nsca-5th/`，`validate_skill_pack.py` **0 errors / 0 warnings**，已安装到 `~/.codebuddy/skills/` |

## 交付物

**8 个可发现入口**

| 入口 | 覆盖 |
|---|---|
| `nsca-resistance-program-design` | 抗阻计划设计（需求分析 → 七步变量 → 端到端 SOP） |
| `nsca-periodization` | 周期化与年度计划编排 |
| `nsca-testing-and-evaluation` | 测试选择、实施、数据解释与画像 |
| `nsca-plyometric-design` | 快速伸缩复合（增强式）训练设计 |
| `nsca-speed-agility-design` | 速度与敏捷训练设计（含变向 vs 反应性敏捷判定） |
| `nsca-aerobic-endurance-design` | 有氧耐力设计与强度分区 |
| `nsca-overtraining-recovery` | 过度训练识别与恢复 |
| `nsca-5th` | 来源路由入口：承载其余 **126 张**能力卡（营养补水、竞赛营养、RED-S、增补剂、心理、特殊人群、技术安全、变阻负荷、康复边界、医疗急症、场地与管理等） |

## 已声明的缺口（不得掩盖）

1. **实际输出评测未执行** —— 阶段 4 只完成了触发/路由精度测试与边界用例核查；`old_skill / new_skill / without_skill` 三变体代表任务的**实际输出对照评测未运行**。因此**不得宣称相对无 Skill 有提升**。
2. **4 个 needs_review 单元**（不进入 active 能力池）：
   - `F · 柔韧训练参数` —— 原文自相矛盾（静态拉伸 10–30 s vs 15–30 s；PNF 3–6 s/≤20% MVC vs 6–10 s）
   - `F · 原木（log）直径与负荷规则` —— 直径单位 mm/in. 互斥
   - `F · 弹力带长度-张力预测方程` —— 自变量单位未定义，代入与表不符（实务只能查表）
   - `E · 运动季节到有氧计划变量映射` —— 原文 ch21.txt 第 1035–1053 行 in-season 行排版错位，列对齐无法唯一确证
3. **13 个 reference 单元**（有来源价值但不作为可执行能力）已登记在 `references.md`，并入 Bundle 的 overview/glossary，**未静默丢弃**。
4. **原文固有的信息不足**（已在各能力卡 E/B 段显式写明为约束，未用常识补齐）：
   - 1.5 英里跑推算 VO2max **原文无回归式**，只能查表
   - 单位换算常数原文自相矛盾（lb→N 4.44/4.45、kg→N 9.81/9.807）
   - 护腰使用"接近最大"**无量化阈值**；爆发动作无阶段时间/角度阈值
   - 过度训练"数周—数月"无精确切点；恢复手段证据强度弱
   - Ch25/Ch26 深度依赖美国法规与场馆标准，**跨法域须重新校验**
5. **覆盖审计**：T01–T40 共 40 项关键任务，逐项在 `coverage-audit.md` 登记了任务 → 原文位置 → 候选 → decision → 去向；无 critical/high 任务的"缺失候选"级缺口。

## 复现与再编译

```bash
cd <cangjie-skill>/
python3 scripts/cangjie.py compile \
  --bundle <books/nsca-essentials-5e>/.cangjie/capabilities \
  --out <dist>/nsca-5th --output pack --purpose workflow --yes
python3 scripts/validate_skill_pack.py <dist>/nsca-5th
```

## 下一步（可选）

- 用 `darwin-skill` 自动进化：`darwin evolve books/nsca-essentials-5e/`（会使用这里的 `test-prompts.json` 做 ratcheting）
- 补齐 §"已声明的缺口"第 1 项（实际输出评测）后，可把交付从"草稿范围"提升为"已验收"
