---
name: logic-system
description: Comprehensive formal, non-classical, inductive, informal, Chinese Mingbian, Minto pyramid, legal, and game-theoretic logic operating system distilled from 20 books in Google Drive (Chen Bo, Zhou Jianwu, Wu Hongzhi, Sun Zhongyuan, Magnus, Graham Priest, Karl Popper, Schopenhauer, Kant, Barbara Minto, Takada, Gause, Weinberg, Luo Xiang, Gu Zhun, Li Ziyang, Wang Zeke, Dixit, Petzold, Kang Huaguang, Zhuzi Baijia) via the Cangjie RIA-TV++ pipeline. Use when the user asks to audit logical laws or Schopenhauer fourfold root of sufficient reason, test syllogisms or Venn diagrams, build truth tables, Fitch proofs, or Karnaugh maps, construct first-order models or unpack Russell definite descriptions, evaluate modal/tense/counterfactual conditionals, resolve self-referential or sorites paradoxes, apply Mill 5 causal methods or Popperian falsification, run Toulmin fallacy critique, dissect Chinese sophistry, structure MECE pyramids, or solve game equilibria and legal causation.
---
# logic-system

基于用户 Google Drive 云盘中 **“逻辑学”文件夹全部 9 部著作**与 **“Library”文件夹全部 11 部逻辑学相关著作**(合计 20 部中西逻辑学、非经典逻辑、科学哲学、批判性思维、名辩学、结构化思维、法律逻辑与博弈论典籍)，按仓颉 `cangjie-skill` (RIA-TV++ 流水线) 蒸馏而成的全书系可执行逻辑学主路由技能。

## When to Use

当用户提出以下请求时调用本技能：

- **底层思维规律与“为什么”四重根体检**：审查概念是否遵守同一律、矛盾律、排中律，运用叔本华《充足理由律的四重根》拆解生成的因果律(`fiendi`)、认识的逻辑律(`cognoscendi`)、存在的时空数学律(`essendi`)与行动的动机律(`agendi`)，或运用康德先验逻辑区分分析判断与综合判断及二律背反(`01`)。
- **经典形式演绎、符号化证明与布尔电路化简**：执行直言命题对当方阵、换质位法、三段论五规则与文恩图检验(`02`)；构造语句逻辑 `SL` 真值表、单行归谬赋值法、Fitch 自然演绎证明(`⊢`)或布尔代数/卡诺图业务规则极小化(`03`)；执行一阶谓词逻辑 `QL` 多重量词转译、二元关系性质核查、有限模型(`UD, extension`)反例构造与罗素确定摹状词宽窄辖域消歧(`04`)。
- **模态、时态、反事实推演与非经典悖论消解**：运用克里普克可能世界语义学(`K, D, T, B, S4, S5`)与刘易斯相似球模型(`C1, C2`)评估必然/可能、应当/允许、宿命论与反事实条件句(`05`)；运用多值逻辑(`K3, LP`)、一度蕴涵(`FDE`)、相干逻辑(`B, R`)、直觉主义逻辑、自由逻辑(`E!`)、模糊逻辑(`Lℵ`)及塔斯基语言层级与哥德尔不完全性定理，消解说谎者悖论、罗素悖论、谷堆连锁悖论并隔离不一致规则库矛盾爆炸(`06`)。
- **科学因果发现、假说证伪与非形式谬误排雷**：运用穆勒五法(求同/求异/共变/剩余/求同求异并用)定位根因，执行波普尔《科学发现的逻辑》可证伪性(`Modus Tollens`)划界、反特设修正(`ad hoc`)审计与贝叶斯逆概率更新(`07`)；运用图尔敏(Toulmin)六要素模型、20大非形式谬误清单与批判性五算子(削弱/加强/假设/解释/评价)拆解自然语言论证(`08`)。
- **中国古典名辩破诡辩、金字塔 MECE 提案与博弈/法律决策**：运用《墨经》“故理类”三物论式、“小故/大故”条件区分、“侔式四界”、荀子《正名》三惑与韩非参验法破拆中式文字诡辩(`09`)；运用高斯/温伯格元问题界定(`期望状态 - 体验状态`)、芭芭拉·明托《金字塔原理》(`SCQA` + 纵横 `MECE`)与高田贵久“天空-乌云-带伞”假说验证构建高说服力方案(`10`)；或运用博弈论纳什均衡/逆向归纳/可信承诺、李子旸反事实机会成本与罗翔“条件说 + 客观归责论”解决策略对抗与法律归责难题(`11`)。

不适用于：

- 纯粹的文学抒情创作、心理情绪宣泄共情(此类需求应路由至心理学技能 `psychology-system`)。
- 替代执业律师出具具有正式法律效力的诉讼代理意见书。

## Core Principles

1. **问题元界定与四重根分流先行原则 (Meta-Framing & Fourfold Root First)**：在启动任何复杂推演或方案拆解前，先用高斯/温伯格公式(`Problem = 期望状态 - 体验状态`, `10`)确认没有把“具体方案”当成“问题定义”；再用叔本华分解律(`01`)定性当前追问的“为什么”属于**物理生成因(`Root 1`)**、**认识证据根据(`Root 2`)**、**数学空间互决(`Root 3`)**还是**主观利益动机(`Root 4`)**，严禁跨根混用。
2. **形式有效性与实质真实性正交双审原则 (Validity + Truth = Soundness)**：严格区分**推理形式有效 (`Γ ⊨ A`)** 与**前提内容真实 (`True Premises`)**。审查任何论证时，必须先用单行部分真值表(`03`)、有限模型(`04`)或三段论规则(`02`)检验形式结构是否保真，再用波普尔证伪检验(`07`)、韩非参验法(`09`)与图尔敏保证支撑(`08`)核验前提与隐含假设是否真实。
3. **证实与证伪的演绎不对称性铁律 (Popperian Asymmetry & Counterexample Razor)**：顺风枚举再多正例(`Fa ∧ Ga`)也无法演绎证实全称假说(`∀x(Fx → Gx)`，仅构成归纳支持)，但只需构造 **1 个单行反例赋值、1 个双元素有限模型或 1 条真实反常基础陈述 (`Fa ∧ ¬Ga`)**，即可通过 `Modus Tollens` 瞬间证伪全称断言。无论在形式证明还是商业抗辩中，永远优先寻找最小潜在证伪反例。
4. **语境层级剥离与次协调防爆熔断机制 (Hierarchy Separation & Paraconsistent Circuit-Breaker)**：面对自然语言条件句、自指悖论或法规冲突时，切勿盲目套用经典实质蕴涵怪论(`¬A ⊢ A → B`)或爆炸原理(`A ∧ ¬A ⊢ B`)；必须区分从言(`de dicto`)与从事(`de re`)辖域(`05`)、区分对象语言(`L0`)与元语言(`L1`)(`06`)、区分共名与别名(`09`)，并对局部矛盾启用 `FDE/LP` 次协调隔离。
5. **纵向有桥梁、横向守 MECE、博弈看逆推原则 (Vertical Bridge, Horizontal MECE & Backward Induction)**：在输出任何结构化分析或方案时，纵向必须补齐“事实(天空) -> 解读(乌云) -> 行动(带伞)”的隐含保证以消除“真是这样的吗？”(`08/10`)；横向必须在同一概念平面做到 `MECE` 以消除“仅仅如此吗？”(`10`)；一旦涉及多方活体互动，必须切换至“向前展望、倒后推理”的动态博弈视角(`11`)。

## Capability Routing and Reference Cards

根据用户的具体任务场景，按以下路由表读取 `references/capabilities/` 下的对应能力卡(以及 `references/book/overview.md` 和 `references/book/glossary.md`)：

| 用户意图 / 核心问题场景 | 主路由能力卡 (Primary Capability Card) | 关键形式算子与核心判准 |
| :--- | :--- | :--- |
| 概念偷换、自相矛盾、模棱两可/假二难、混淆物理原因与认识证据、康德分析/综合判断与二律背反 | `references/capabilities/01-laws-of-thought-fourfold-sufficient-reason.md` | 同一律(`A=A`)、矛盾律(`¬(A∧¬A)`)、排中律(`A∨¬A`)；叔本华充足理由律四重根(`fiendi/cognoscendi/essendi/agendi`)防混矩阵 |
| 包含“所有/有些/都不是”的直言推理、对当方阵真假推演、三段论有效性检验、文恩图判定 | `references/capabilities/02-categorical-syllogism-term-logic-audit.md` | `A/E/I/O` 周延性口诀；换质/换位/换质位规则；三段论五条铁律(防四概念/中项不周延/大小项不当周延)；三圆文恩图法 |
| 复合假言/选言推理(`只有...才/除非...否则`)、真值表、Fitch自然演绎证明、复杂业务规则/数字电路化简 | `references/capabilities/03-propositional-truth-table-boolean-deduction.md` | `SL` 联结词精确转译(`A unless B ≡ ¬B → A`)；单行部分真值表归谬赋值法；Fitch 引入/消去逆向证明策略；布尔卡诺图化简 |
| 多重量词重叠(`∀x∃y` vs `∃y∀x`)、多元比较/排序关系推理、一阶有限模型反例、罗素“当今法国国王”摹状词拆解 | `references/capabilities/04-first-order-predicate-model-descriptions.md` | `QL` 全称配 `→` / 特称配 `∧`；等词数量公式(至少/至多/恰好 `n` 个)；关系自反/对称/传递核查；双元素模型反例；摹状词宽窄辖域 |
| 必然/可能模态推理、道义逻辑(`应当/允许`)、宿命论破拆、反事实条件句(“如果当初...就会...”)评估 | `references/capabilities/05-modal-tense-counterfactual-world-semantics.md` | 可能世界关系语义学 `K/D/T/B/S4/S5`；时态逻辑 `Kt`；从言(`de dicto`) vs 从事(`de re`)范围消歧；刘易斯相似球 `C1/C2` (禁前件加强/传递/换质位) |
| 说谎者/罗素/理发师自指悖论、谷堆/秃头连锁滑坡悖论、不一致法规/数据库防爆、空专名、哥德尔定理 | `references/capabilities/06-nonclassical-paraconsistent-fuzzy-paradox.md` | 真值空缺(`K3`)与真值过剩(`LP/FDE` 次协调阻断 `DS` 与爆炸原理)；相干逻辑变元共享；直觉主义构造性；模糊逻辑 `Lℵ`；塔斯基真层级；自由逻辑 `E!` |
| 实验/故障因果归因、科学假说与伪科学划界、统计与精确数字陷阱排查、贝叶斯概率更新、乌鸦/绿蓝/彩票悖论 | `references/capabilities/07-inductive-mills-methods-popper-falsification.md` | 穆勒五法(求同/求异/共变/剩余/并用)；波普尔可证伪性判准(`Modus Tollens` 证伪、禁 `ad hoc` 特设修正、经验内容 `Ct(T)`)；贝叶斯公式与基础概率 |
| 日常/商业论证漏洞寻找(论证有效性分析)、图尔敏六要素建模、20大非形式谬误反制、削弱/加强/隐含假设挖掘 | `references/capabilities/08-informal-logic-toulmin-fallacy-critique.md` | 定义五规则；图尔敏模型(`C/D/W/B/Q/R`)；相关/预设/歧义/弱归纳 20 大谬误破拆表；否定代入法挖隐含假设；`2×2` 四格表基数审计 |
| 先秦名辩原典解读、公孙龙“白马非马/离坚白”、邓析两可、庄子濠梁之辩、中式文字诡辩与平行类推破拆 | `references/capabilities/09-chinese-mingbian-sophistry-deconstruction.md` | 《墨经》“以名举实/以辞抒意/以说出故”、“故理类”三物、“小故(必要)/大故(充要)”、七推论法与“侔式四界”；荀子《正名》三惑；韩非矛盾参验法 |
| 商业提案/汇报/论文结构化重构、金字塔原理与 `SCQA`、纵横 `MECE` 拆解、假说驱动验证、界定真问题 | `references/capabilities/10-pyramid-mece-hypothesis-problem-framing.md` | 高斯-温伯格问题公式(`期望 - 体验`)；明托金字塔三铁律(结论先行、禁缺乏思想标题、三种逻辑顺序)；高田横向 MECE 五切法与“天空-乌云-带伞” |
| 商业/职场多方博弈策略、囚徒困境/智猪/斗鸡破局、可信威胁与承诺设计、法律因果归责、反事实机会成本核算 | `references/capabilities/11-game-theoretic-legal-causation-decision-logic.md` | 严格优势策略、`IEDS`、纳什均衡、混合策略无差异方程、逆向归纳法(`SPNE`)；可信承诺8机制；罗翔 `But-for` 条件说 + 客观归责三阶层；机会成本 |

## Steps

### Step 1: 问题元界定与逻辑模态分诊 (Meta-Framing & Triage)

收到用户的推理、辩论、排障、提案或决策请求后，首先完成三项定性分诊：

1. **元问题与四重根定性 (`01, 10`)**：当前任务是在**检验/反驳既有论证(破论)**、**形式化演算求解(推论)**，还是在**构建结构化方案/博弈策略(立论)**？追问的“为什么”属于物理生成因(`fiendi`)、逻辑认识根据(`cognoscendi`)、数学结构(`essendi`)还是行为动机(`agendi`)？
2. **形式层级选型 (`02-06`)**：
   - 若仅涉单一主谓词项包含 -> 选词项逻辑(`02`)。
   - 若涉复合条件/选言真值组合或规则化简 -> 选命题逻辑/布尔代数(`03`)。
   - 若涉多重全称/存在量词、多元关系或数量/摹状词 -> 选一阶谓词逻辑(`04`)。
   - 若涉必然/可能/应当/反事实假设 -> 选模态与条件句逻辑(`05`)。
   - 若涉自指悖论、模糊滑坡或局部矛盾防爆 -> 选非经典逻辑(`06`)。
3. **经验与实战场景选型 (`07-11`)**：
   - 科学/工程根因排查与数据检验 -> 选穆勒五法与波普尔证伪(`07`)。
   - 自然语言谬误排雷与批判性削弱/加强 -> 选图尔敏与非形式逻辑(`08`)或中国名辩逻辑(`09`)。
   - 商业汇报/问题拆解与多方博弈/法律归责 -> 选金字塔 MECE(`10`)或博弈/法律/经济决策逻辑(`11`)。

### Step 2: 路由加载对应能力卡并执行形式/结构化推演 (Capability Card Execution)

根据上方路由表读取 1-2 张最核心的 `references/capabilities/*.md` 能力卡(跨界复杂任务按 `composes-with` 组合调用)：

- **形式演算与悖论线 (`02 -> 03 -> 04 -> 05 -> 06`)**：严格执行【符号化词典定义 -> 括号与量词/模态辖域对齐 -> 单行归谬赋值 / 有限模型反例 / 可能世界 Tableau / Fitch 自然演绎证明】。
- **论证批判与名辩破谬线 (`01 -> 08 -> 09 -> 07`)**：严格执行【剥离修辞提取前提结论 -> 图尔敏六要素与隐含保证(`W`)否定测试 -> 荀子三惑 / 墨辩侔式四界 / 20大非形式谬误定性 -> 四格表基数与反例证伪】。
- **结构化立论与博弈决策线 (`10 -> 07 -> 11`)**：严格执行【高斯-温伯格 `R1 -> R2` 真问题锁定 -> `SCQA` 序言与塔尖量化结论先行 -> 横向五切法 `MECE` + 纵向“天空-乌云-带伞”假说验证 -> 博弈树逆向归纳与可信承诺加固】。

### Step 3: 对照跨书定量与形式铁律核验输出 (Quantitative & Formal Audit)

在输出最终结论、证明或方案前，使用以下全书系黄金标尺执行自检：

| 审计维度 | 核心检验公式 / 黄金判准 | 来源典籍锚点 |
| :--- | :--- | :--- |
| **条件句转译检验** | `只有 B 才 A` 必译为 `A → B`；`除非 B 否则 A` 必译为 `¬B → A (≡ A ∨ B)`；`¬(A → B)` 必等值于 `A ∧ ¬B` | Magnus《forall x》第2-3章 + 陈波第2章 |
| **三段论与量词检验** | 中项 `M` 至少周延一次，前提不周延项结论不得周延；`∃x∀y Rxy ⊢ ∀y∃x Rxy` 不可逆；`∃E` 必用全新常元 | 陈波《逻辑学导论》第3-4章 + Magnus 第4-6章 |
| **反事实与模态检验** | 道义逻辑(`D`)禁用 `□A → A`；反事实条件句(`A > B`)禁用前件加强、传递律与换质位；区分 `□(A∨¬A)` 与 `□A∨□¬A` | Priest《Non-Classical Logic》第3, 5章 |
| **归纳与概率检验** | 潜在证伪者类非空(`Fsb(T) > 0`)且无 `ad hoc` 补丁；计算 `P(H|E)` 必代贝叶斯先验 `P(H)`；因果归因必查 `2×2` 四格表与第三因 | 波普尔《科学发现的逻辑》+ 陈波第5章 + 周建武 |
| **名辩与诡辩检验** | 区分“小故(必要)”与“大故(充要)”；区分系词“是”的等同义(`=`)与类属义(`⊆`)；核查侔式推理是否“一周而一不周” | 孙中原《诡辩与逻辑名篇趣谈》+《墨经》《荀子》 |
| **金字塔与博弈检验** | 严禁使用缺乏思想的目录式标题；同层横向满足五切法 `MECE`；序贯博弈执行逆向归纳(`SPNE`)剔除空头威胁 | 明托《金字塔原理》+ 高田《精准表达》+ 迪克西特 |

## Gotchas

- **犯“谬误谬误 (The Fallacy Fallacy)”**：指出对方论证过程无效或犯了非形式谬误，只证明“他的理由推不出该结论”，**绝不自动证明“他的结论本身在事实上为假”**(`08`)。
- **把日常语用的“有些 (`Some`)”当成“有些不是 (`Not all`)”**：在逻辑学中，“有些 `S` 是 `P` (`SIP`)”意为“至少有一个 `S` 是 `P`(可能全部都是)”，从 `SIP` 绝不能逻辑推出 `SOP`(`02/04`)。
- **混淆“否定后件式 (`MT`)”与“否定前件谬误 (`DA`)”**：已知 `A → B`，观察到 `¬B` 推出 `¬A` 是铁板钉钉的演绎有效式(`MT`)；但观察到 `¬A` 却推出 `¬B` 则是典型的形式谬误(`DA`)(`03`)。
- **在非经典或规范场景死套经典规则**：在含矛盾的规则库中盲目使用选言三段论(`DS`)会触发矛盾爆炸(`06`)；在法律归责中只看 `But-for` 条件说而不做“客观归责与自我答责”过滤会导致无限株连(`11`)。
