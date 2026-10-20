# nsca-5th — 《Essentials of Strength Training and Conditioning》第 5 版 蒸馏能力包

> **仓库收录说明**：本目录是 cangjie-skill 2.5.0 对同一教材的二次构建，与 [`skills/nsca-5th/`](../nsca-5th/) 并存。
> 两个目录的 `SKILL.md` frontmatter `name` 都是 `nsca-5th`，**同一个 Agent 里只能装其中一个**；
> 需要并存时，安装前把本目录 `SKILL.md` 的 `name` 改成 `nsca-5th-deepseek`（只改这一行，能力卡不动）。
>
> 上游：[仓颉 cangjie-skill](https://github.com/kangarooking/cangjie-skill) v2.5.0（MIT）　｜　许可：[PolyForm Noncommercial 1.0.0](LICENSE)　｜　版本：`nsca-5th-deepseek-v1.0.0`　｜　版本记录：[CHANGELOG.md](CHANGELOG.md)

由 **cangjie-skill 2.5.0**（RIA-TV++）从整本教科书蒸馏而来。源书 26 章 / 1876 页 / 约 40 万词。

> 本包原名 `nsca-vi`，现更名为 **`nsca-5th`**。

## 快速使用

**8 个可发现入口**（已安装到 `~/.codebuddy/skills/`）：

| 入口 | 什么时候用 |
|---|---|
| `nsca-resistance-program-design` | 排抗阻训练计划、定组数/次数/负荷/休息、验收一份力量计划 |
| `nsca-periodization` | 排年度或周期化计划、赛季怎么调整、赛前怎么减量 |
| `nsca-testing-and-evaluation` | 选测试、排测试日流程、解读体测数据、做运动员画像 |
| `nsca-plyometric-design` | 跳跃 / 落地 / 增强式训练计划、触地量、落地技术纠错 |
| `nsca-speed-agility-design` | 冲刺、加速、变向、敏捷（含"该练哪个"的能力判定） |
| `nsca-aerobic-endurance-design` | 有氧耐力计划、目标心率与强度分区、同期训练 |
| `nsca-overtraining-recovery` | 成绩下降的归因、过度训练判定、恢复策略 |
| **`nsca-5th`** | **来源路由入口**，承载其余 **126 张能力卡**（营养补水、竞赛营养、RED-S、增补剂、心理、青少年/老年/女性/孕期人群、护腰与保护、变阻负荷计算、康复边界、医疗急症、场地设计与风险管理等） |

## 目录说明

### 给 Agent 用（可直接安装的产物）

- `nsca-5th/` — 来源路由入口（含全部 133 张能力卡的索引与意图映射 `capability-index.md`、`cheatsheet.md`、`glossary.md`、`overview.md`，以及 `references/capabilities/` 下的全部能力卡正文）
- `nsca-*/` — 7 个晋级 Skill，各自自包含（单个 `SKILL.md` + 可点击的资源清单）
- `capability-destinations.json` — 发布审计清单（每个能力的唯一去向）
- `BUILD_MANIFEST.json` — 构建清单与哈希

### 给读者用

- **`DIGEST.md`（先看这个）** — 面向读者的精华长文，约 6,500 中文字。按书的骨架组织，覆盖 9 个核心方法论、15 条陷阱、8 条作者局限。想快速掌握这本书、不想读 870 页，看它。
- `GLOSSARY.md` — 194 条关键术语（作者本人的用法，非字典义）
- `BOOK_OVERVIEW.md` — 整书理解：结构 / 关键术语 / 批判 / 应用潜力 + T01–T40 关键任务清单

### 审计轨迹（可追溯性）

- `verified.md` — 145 个能力单元的三重验证记录（每个单元的 V1 来源充分性 / V2 可执行性演练 / V3 任务增益与判定理由）
- `references.md` — 13 个有来源价值但不作为可执行能力的参考项及其去向
- `needs-review.md` — 4 个存在来源冲突或关键条件缺失的条目及其具体缺口
- `coverage-audit.md` — T01–T40 逐项覆盖审计（任务 → 原文位置 → 候选 → 判定 → 去向）
- `PIPELINE_STATE.md` — 流水线状态与**已声明缺口**
- `test-prompts.json` / `test-results.md` — 压力测试用例与结果

## 质量指标

| 项 | 值 |
|---|---|
| 提取候选（5 路并行） | 1,143 条（framework 253 / principle 664 / case 97 / counter-example 129）+ 194 条术语 |
| 归并后能力单元 | 145（verified 128 / reference 13 / needs_review 4 / rejected 0） |
| 最终能力卡 | 133 张（R/I/A1/A2/E/B 六段齐全率 100%） |
| 能力间关系 | 440 条（依赖 / 对比 / 组合） |
| 触发精度（独立盲测） | 应触发 35/35 = **100%**；诱饵 17/17 = **100%**；边界用例 8 条人工核查 |
| 编译校验 | `validate_skill_pack.py` **0 errors / 0 warnings** |
| Schema 校验 | `capability-bundle.schema.json` **0 errors** |
| 入口预算 | 8 / 8（含 1 个路由入口） |

## 已知缺口（重要）

1. **实际输出评测未执行** —— 只做了触发/路由精度测试；`old/new/without` 三变体的实际任务输出对照未运行，因此**不宣称相对无 Skill 有提升**。
2. 4 个 needs_review 条目（柔韧参数原文自相矛盾、原木直径单位互斥、弹力带预测方程单位未定义、有氧赛季表源抽取错位）。
3. 原文固有信息不足处已在各能力卡 E/B 段显式写成约束（如 1.5 英里跑推算 VO2max 无回归式、护腰无量化阈值、过度训练无精确切点）。
4. Ch25/Ch26 的场地与法规条款**深度依赖美国法规与场馆标准**，跨法域使用须重新校验。

详见 `PIPELINE_STATE.md`。

## 安装

把本目录下的 `nsca-5th/` 与 7 个 `nsca-*/` 目录一并复制到宿主的 skills 目录即可：

```bash
cp -r nsca-5th nsca-resistance-program-design nsca-periodization \
      nsca-testing-and-evaluation nsca-plyometric-design \
      nsca-speed-agility-design nsca-aerobic-endurance-design \
      nsca-overtraining-recovery  ~/.codebuddy/skills/
```

> 注意：不要把同一本书的 single 与 pack 两套同时安装——两套 description 会重复覆盖意图，二选一。本包只含 pack。

## 复现

```bash
cd <cangjie-skill>/
python3 scripts/cangjie.py compile \
  --bundle <path>/.cangjie/capabilities \
  --out <dist>/nsca-5th --output pack --purpose workflow --yes
python3 scripts/validate_skill_pack.py <dist>/nsca-5th
```

## 自动进化（可选）

本包附带的 `test-prompts.json` 遵循 darwin-skill 格式，可直接用于 ratcheting 自动进化：

```bash
darwin evolve books/nsca-essentials-5e/
```

---

*来源：Essentials of Strength Training and Conditioning, Fifth Edition © 2027 National Strength and Conditioning Association / Human Kinetics。本能力包为其方法论的教学性蒸馏，原文引用限于短段落（英文 ≤100 词）；不替代原书，不构成医疗、营养或法律建议。*
