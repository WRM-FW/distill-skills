# logic-system

> **✨Masterpiece** —— 仓库的核心代表作之一，入选依据见[仓库根 README](../../README.md#masterpiece)。

上游 Skill：[仓颉 cangjie-skill](https://github.com/kangarooking/cangjie-skill)（`RIA-TV++` 流水线，MIT）　｜　许可：[PolyForm Noncommercial 1.0.0](LICENSE)　｜　版本：`v1.0.0`（标签 `logic-system-v1.0.0`）　｜　版本记录：[CHANGELOG.md](CHANGELOG.md)

基于用户 Google Drive「逻辑学」文件夹 9 部著作与「Library」文件夹 11 部逻辑学相关著作（合计 20 部：
陈波、周建武、武宏志、孙中原、诸子百家原典、Magnus、Priest、波普尔、叔本华、康德、明托、高田贵久、
高斯与温伯格、罗翔、顾准、李子旸、王则柯、迪克西特与奈尔伯夫、Petzold、康华光与阎石），
按仓颉 `cangjie-skill`（`RIA-TV++` 流水线）蒸馏而成的全书系可执行逻辑学主路由技能。

## 能做什么

`SKILL.md` 主路由按问题类型分发到 11 张能力卡，横跨形式逻辑、非经典逻辑、归纳与批判性思维、
中国名辩、结构化表达、法律与博弈八个方向：

| 卡 | 主题 | 典型触发 |
| --- | --- | --- |
| 01 | 思维三律 + 叔本华充足理由律四重根 + 康德分析/综合与二律背反 | 「这个'为什么'问的是物理原因、证据、数学关系还是动机？」 |
| 02 | 直言命题、对当方阵、三段论五规则、文恩图 | 「所有 A 都是 B，有些 B 不是 C，能不能推出……」 |
| 03 | 语句逻辑真值表、单行归谬赋值、Fitch 自然演绎、布尔/卡诺图化简 | 「把这段'除非……否则……'符号化并检验有效」 |
| 04 | 一阶谓词、多重量词、有限模型反例、罗素摹状词辖域 | 「∃x∀y Rxy 能不能推出 ∀y∃x Rxy？」 |
| 05 | 模态/道义/时态/反事实、Kripke 与 Lewis 语义 | 「这个反事实条件句的相似球排序对不对？」 |
| 06 | 多值、相干、直觉主义、模糊逻辑、说谎者与谷堆悖论、爆炸隔离 | 「规则库里有两条冲突条款，怎么避免全盘推导崩塌」 |
| 07 | 穆勒五法、波普尔证伪、贝叶斯更新、反特设修正 | 「这条因果结论能不能被证伪，还差哪个对照」 |
| 08 | 图尔敏六要素、20 大非形式谬误、批判性五算子 | 「这段论证的隐含保证（W）站不站得住」 |
| 09 | 《墨经》故理类三物论式、荀子正名三惑、韩非参验法 | 「这句话是文字诡辩还是有效推理」 |
| 10 | 高斯/温伯格元问题、明托金字塔 SCQA + MECE、天空-乌云-带伞 | 「把这份汇报改成一页结论先行」 |
| 11 | 纳什均衡/逆向归纳/可信承诺、条件说 + 客观归责、反事实机会成本 | 「这个多方博弈的均衡在哪，法律上该归责给谁」 |

执行是三步：先做问题元界定与逻辑分支选型（`Step 1`）→ 加载 1-2 张能力卡做形式/结构化推演（`Step 2`）
→ 用跨书黄金标尺自检（`Step 3`，条件句转译、量词与周延、反事实、归纳概率、名辩、金字塔与博弈六类判准）。
`SKILL.md` 末尾另有 Gotchas：谬误谬误、把「有些」读成「有些不是」、混淆否定后件与否定前件、
在矛盾规则库死套经典规则等。

## 目录结构

```text
logic-system/
├── SKILL.md                       # 主路由：触发边界 + 五大核心原则 + 11 卡路由表 + 三步流程 + Gotchas
├── README.md                      # 本文件
├── CHANGELOG.md                   # 版本记录（标签 logic-system-vX.Y.Z）
├── LICENSE                        # PolyForm Noncommercial 1.0.0
└── references/
    ├── book/
    │   ├── overview.md            # 20 部著作的整书结构与适用边界
    │   └── glossary.md            # 符号、公式与术语速查
    └── capabilities/              # 11 张 RIA++ 六段式（R/I/A1/A2/E/B）能力卡
```

## 安装与调用

```bash
git clone --depth 1 https://github.com/WRM-FW/distill-skills.git
cp -r distill-skills/skills/logic-system <你的 Agent Skill 目录>/
```

整个目录（含 `references/`）都要拷过去，只拷 `SKILL.md` 会丢能力卡。
调用方式：直接说「用逻辑学系统把这段论证符号化并检验」，或显式 `调用 logic-system Skill`。

## 边界

- 不做文学抒情与情绪共情——这类需求路由到同仓库的 `psychology-system`。
- 法律部分只做推理与归责结构的检查，不替代执业律师出具正式诉讼意见或法律意见书。
- 形式逻辑的结论只保证「前提真则结论真」；前提是否真实须另行核查（`Validity + Truth = Soundness`）。
- 内容源自受版权保护著作的研究性提炼：PolyForm NC 只覆盖本目录的原创表达，不覆盖、也不重新授权原书文字与图表。

---

> 本 Skill 由 [distill-skills](https://github.com/WRM-FW/distill-skills) 仓库统一收录维护，全部 Skill 索引见[仓库根 README](../../README.md)。
